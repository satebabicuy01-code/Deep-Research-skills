#!/usr/bin/env python3
"""
IHSG Retracement Screener
=========================

Menyaring emiten Bursa Efek Indonesia (IHSG/IDX) yang:

  1. PERNAH NAIK TINGGI  -> sebelum puncak, harga sudah rally minimal `--min-runup`%
                            (default +100%, alias harga sempat >= 2x lipat).
  2. SEDANG RETRACEMENT   -> dari high terakhir (`--peak-window` hari) sudah drop
                            di zona `--min-drop`%..`--max-drop`% (default 50%..61.8%,
                            zona golden ratio Fibonacci).
  3. LIKUID               -> rata-rata nilai transaksi harian (close x volume) dalam
                            `--liq-window` candle terakhir (default 20) minimal
                            `--min-value` rupiah (default Rp 1.000.000.000).

Sumber data : Yahoo Finance chart API (gratis, tanpa API key). Ticker IDX pakai
              akhiran `.JK` (mis. BBCA.JK). Harga & volume sudah disesuaikan split
              (split-adjusted) sehingga stock-split tidak terbaca sebagai crash.

Dependensi  : hanya `requests` (Python 3.9+). Tidak butuh pandas / yfinance.

Contoh:
    python3 screener.py                       # pakai universe & default bawaan
    python3 screener.py --limit 30            # uji cepat 30 emiten pertama
    python3 screener.py --min-drop 50 --max-drop 78.6
    python3 screener.py --tickers my_list.txt --out hasil.csv
"""
from __future__ import annotations

import argparse
import csv
import os
import sys
import time
import datetime as dt
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    import requests
except ImportError:  # pragma: no cover
    sys.exit("Butuh paket 'requests'. Install dengan: pip install requests")

CHART_URL = "https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
HEADERS = {"User-Agent": "Mozilla/5.0 (screener; +https://github.com)"}
HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_TICKERS = os.path.join(HERE, "tickers.txt")


# --------------------------------------------------------------------------- #
# Data fetching                                                               #
# --------------------------------------------------------------------------- #
def load_universe(path: str) -> list[str]:
    """Baca daftar kode emiten. Satu kode per baris, '#' = komentar.

    Kode boleh dengan atau tanpa akhiran .JK. Duplikat dibuang, urutan dijaga.
    """
    seen: set[str] = set()
    out: list[str] = []
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.split("#", 1)[0].strip().upper()
            if not line:
                continue
            for code in line.replace(",", " ").split():
                code = code.strip().upper()
                if not code:
                    continue
                if not code.endswith(".JK"):
                    code += ".JK"
                if code not in seen:
                    seen.add(code)
                    out.append(code)
    return out


def fetch_chart(symbol: str, yrange: str, session: requests.Session,
                retries: int = 4) -> dict | None:
    """Ambil data harian OHLCV dari Yahoo. None jika gagal/tidak ada data."""
    params = {"range": yrange, "interval": "1d"}
    delay = 1.0
    for attempt in range(retries):
        try:
            r = session.get(CHART_URL.format(symbol=symbol), params=params,
                            headers=HEADERS, timeout=30)
            if r.status_code == 404:
                return None  # emiten tidak ada / delisted
            if r.status_code in (429, 500, 502, 503, 504):
                time.sleep(delay)
                delay *= 2
                continue
            r.raise_for_status()
            data = r.json()
            res = (data.get("chart") or {}).get("result")
            if not res:
                return None
            return res[0]
        except (requests.RequestException, ValueError):
            time.sleep(delay)
            delay *= 2
    return None


def parse_series(result: dict) -> dict | None:
    """Ubah payload Yahoo menjadi deret rapi (tanpa titik kosong)."""
    ts = result.get("timestamp") or []
    quote = ((result.get("indicators") or {}).get("quote") or [{}])[0]
    highs = quote.get("high") or []
    lows = quote.get("low") or []
    closes = quote.get("close") or []
    vols = quote.get("volume") or []
    meta = result.get("meta") or {}
    gmt = meta.get("gmtoffset", 0) or 0

    dates, H, L, C, V = [], [], [], [], []
    for i in range(len(ts)):
        c = closes[i] if i < len(closes) else None
        h = highs[i] if i < len(highs) else None
        low = lows[i] if i < len(lows) else None
        v = vols[i] if i < len(vols) else None
        if c is None or h is None or low is None:
            continue
        d = dt.datetime.utcfromtimestamp(ts[i] + gmt).date()
        dates.append(d)
        H.append(float(h))
        L.append(float(low))
        C.append(float(c))
        V.append(float(v) if v is not None else 0.0)
    if not C:
        return None
    return {
        "dates": dates, "high": H, "low": L, "close": C, "volume": V,
        "name": meta.get("longName") or meta.get("shortName") or "",
        "currency": meta.get("currency") or "",
    }


# --------------------------------------------------------------------------- #
# Screening logic                                                             #
# --------------------------------------------------------------------------- #
def analyze(symbol: str, series: dict, cfg: argparse.Namespace) -> dict | None:
    """Hitung metrik retracement & likuiditas untuk satu emiten."""
    close = series["close"]
    high = series["high"]
    low = series["low"]
    vol = series["volume"]
    dates = series["dates"]
    n = len(close)
    if n < max(cfg.liq_window, 20):
        return None  # data terlalu pendek untuk dipercaya

    current = close[-1]
    last_date = dates[-1]

    # Deret acuan untuk "high": high intraday (default) atau harga penutupan.
    # Pakai --price close bila ingin tahan terhadap 1 tick harga yang keliru.
    peak_series = close if cfg.price == "close" else high

    # --- High terakhir: nilai tertinggi dalam `peak_window` candle terakhir ---
    w0 = max(0, n - cfg.peak_window)
    peak_rel = max(range(w0, n), key=lambda i: peak_series[i])
    peak = peak_series[peak_rel]
    peak_date = dates[peak_rel]
    if peak <= 0:
        return None
    drop_pct = (peak - current) / peak * 100.0

    # --- Run-up ke arah puncak ("pernah naik tinggi") ---
    # base = low terendah dari seluruh histori yang tersedia SEBELUM/HINGGA puncak.
    base_slice = low[: peak_rel + 1]
    base_low = min(base_slice) if base_slice else peak
    runup_pct = ((peak - base_low) / base_low * 100.0) if base_low > 0 else 0.0

    # --- Likuiditas: rata-rata nilai transaksi = close*volume, `liq_window` hari ---
    k = cfg.liq_window
    values = [close[i] * vol[i] for i in range(n - k, n)]
    avg_value = sum(values) / len(values) if values else 0.0

    return {
        "ticker": symbol.replace(".JK", ""),
        "name": series["name"],
        "current": current,
        "peak": peak,
        "peak_date": peak_date.isoformat(),
        "drop_pct": drop_pct,
        "base_low": base_low,
        "runup_pct": runup_pct,
        "avg_value": avg_value,
        "avg_value_bn": avg_value / 1e9,
        "last_date": last_date.isoformat(),
        "bars": n,
    }


def passes(row: dict, cfg: argparse.Namespace) -> bool:
    if not (cfg.min_drop <= row["drop_pct"] <= cfg.max_drop):
        return False
    if row["avg_value"] < cfg.min_value:
        return False
    if not cfg.no_runup and row["runup_pct"] < cfg.min_runup:
        return False
    return True


def screen_one(symbol: str, cfg: argparse.Namespace,
               session: requests.Session) -> tuple[str, dict | None, str]:
    result = fetch_chart(symbol, cfg.range, session)
    if result is None:
        return symbol, None, "no-data"
    series = parse_series(result)
    if series is None:
        return symbol, None, "empty"
    if series.get("currency") and series["currency"] != "IDR":
        return symbol, None, "non-idr"
    row = analyze(symbol, series, cfg)
    if row is None:
        return symbol, None, "short-history"
    return symbol, row, "ok"


# --------------------------------------------------------------------------- #
# Output                                                                       #
# --------------------------------------------------------------------------- #
def fmt_idr(x: float) -> str:
    return f"{x:,.0f}".replace(",", ".")


def print_table(rows: list[dict]) -> None:
    if not rows:
        print("\n(Tidak ada emiten yang lolos kriteria.)")
        return
    hdr = f"{'KODE':<6} {'DROP%':>6} {'RUNUP%':>8} {'NILAI/HR':>14} {'HARGA':>9} {'PUNCAK':>9} {'TGL PUNCAK':>11}  NAMA"
    print("\n" + hdr)
    print("-" * len(hdr))
    for r in rows:
        print(f"{r['ticker']:<6} {r['drop_pct']:>6.1f} {r['runup_pct']:>8.0f} "
              f"{'Rp'+fmt_idr(r['avg_value']):>14} {fmt_idr(r['current']):>9} "
              f"{fmt_idr(r['peak']):>9} {r['peak_date']:>11}  {r['name'][:34]}")


def write_csv(rows: list[dict], path: str) -> None:
    cols = ["ticker", "name", "current", "peak", "peak_date", "drop_pct",
            "base_low", "runup_pct", "avg_value", "avg_value_bn",
            "last_date", "bars"]
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow({c: r[c] for c in cols})


# --------------------------------------------------------------------------- #
# CLI                                                                          #
# --------------------------------------------------------------------------- #
def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Screener retracement emiten IHSG (Yahoo Finance).",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument("--tickers", default=DEFAULT_TICKERS,
                   help="File daftar kode emiten (satu per baris).")
    p.add_argument("--min-drop", type=float, default=50.0,
                   help="Batas bawah drop dari high terakhir (%%).")
    p.add_argument("--max-drop", type=float, default=61.8,
                   help="Batas atas drop dari high terakhir (%%).")
    p.add_argument("--min-runup", type=float, default=100.0,
                   help="Minimal rally ke puncak agar dianggap 'pernah naik tinggi' (%%).")
    p.add_argument("--no-runup", action="store_true",
                   help="Nonaktifkan filter 'pernah naik tinggi'.")
    p.add_argument("--peak-window", type=int, default=250,
                   help="Jumlah candle terakhir untuk mencari 'high terakhir'.")
    p.add_argument("--price", choices=["high", "close"], default="high",
                   help="Acuan 'high terakhir': high intraday atau harga penutupan.")
    p.add_argument("--liq-window", type=int, default=20,
                   help="Jumlah candle untuk rata-rata nilai transaksi.")
    p.add_argument("--min-value", type=float, default=1_000_000_000.0,
                   help="Minimal rata-rata nilai transaksi harian (Rupiah).")
    p.add_argument("--range", default="2y",
                   help="Rentang histori Yahoo (1y,2y,5y,10y,max).")
    p.add_argument("--workers", type=int, default=8,
                   help="Jumlah thread pengambil data paralel.")
    p.add_argument("--limit", type=int, default=0,
                   help="Batasi jumlah emiten (0 = semua). Untuk uji cepat.")
    p.add_argument("--sort", choices=["value", "drop", "runup"], default="value",
                   help="Urutan hasil: nilai transaksi / drop / run-up.")
    p.add_argument("--out", default="",
                   help="Path CSV output (default: ihsg_retracement_<tgl>.csv).")
    p.add_argument("--quiet", action="store_true", help="Sembunyikan progres.")
    return p


def main(argv: list[str] | None = None) -> int:
    cfg = build_parser().parse_args(argv)

    if cfg.min_drop > cfg.max_drop:
        sys.exit("--min-drop tidak boleh lebih besar dari --max-drop.")
    if not os.path.exists(cfg.tickers):
        sys.exit(f"File universe tidak ditemukan: {cfg.tickers}")

    universe = load_universe(cfg.tickers)
    if cfg.limit > 0:
        universe = universe[: cfg.limit]
    total = len(universe)
    if total == 0:
        sys.exit("Universe kosong.")

    if not cfg.quiet:
        print(f"IHSG Retracement Screener")
        print(f"  Universe        : {total} emiten ({os.path.basename(cfg.tickers)})")
        print(f"  Drop dari high  : {cfg.min_drop:g}%..{cfg.max_drop:g}% "
              f"(high terakhir = {cfg.peak_window} candle)")
        print(f"  Pernah naik     : {'OFF' if cfg.no_runup else f'>= {cfg.min_runup:g}%'}")
        print(f"  Likuiditas      : rata-rata {cfg.liq_window} candle >= "
              f"Rp{fmt_idr(cfg.min_value)}")
        print(f"  Histori         : {cfg.range}, {cfg.workers} worker\n")

    rows: list[dict] = []
    reasons: dict[str, int] = {}
    done = 0
    session = requests.Session()

    with ThreadPoolExecutor(max_workers=cfg.workers) as ex:
        futures = {ex.submit(screen_one, s, cfg, session): s for s in universe}
        for fut in as_completed(futures):
            symbol, row, reason = fut.result()
            reasons[reason] = reasons.get(reason, 0) + 1
            done += 1
            if row is not None and passes(row, cfg):
                rows.append(row)
            if not cfg.quiet and (done % 25 == 0 or done == total):
                print(f"  ...diproses {done}/{total}  (lolos sementara: {len(rows)})",
                      file=sys.stderr)

    key = {"value": lambda r: r["avg_value"],
           "drop": lambda r: r["drop_pct"],
           "runup": lambda r: r["runup_pct"]}[cfg.sort]
    rows.sort(key=key, reverse=True)

    print_table(rows)

    out = cfg.out or f"ihsg_retracement_{dt.date.today().isoformat()}.csv"
    write_csv(rows, out)

    print(f"\nRingkasan: {len(rows)} lolos dari {total} emiten diperiksa.")
    if not cfg.quiet:
        detail = ", ".join(f"{k}={v}" for k, v in sorted(reasons.items()))
        print(f"  Status pengambilan: {detail}")
    print(f"Hasil lengkap disimpan ke: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
