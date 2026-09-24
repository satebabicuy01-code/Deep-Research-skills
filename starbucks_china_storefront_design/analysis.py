#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Analisis kuantitatif: produktivitas gerai Starbucks China vs ekspansi jaringan & format.

Input : data/*.csv (sumber: 10-K, press release Starbucks, 20-F Luckin, FRED DEXCHUS)
Output: data/analysis_output.json + ringkasan di stdout
"""

import csv
import json
import math
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"


def read_csv(name):
    with (DATA / name).open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def num(v):
    return None if v in ("", None) else float(v)


def pearson(xs, ys):
    pairs = [(x, y) for x, y in zip(xs, ys) if x is not None and y is not None]
    n = len(pairs)
    mx = sum(p[0] for p in pairs) / n
    my = sum(p[1] for p in pairs) / n
    sxy = sum((x - mx) * (y - my) for x, y in pairs)
    sxx = sum((x - mx) ** 2 for x, _ in pairs)
    syy = sum((y - my) ** 2 for _, y in pairs)
    return {"r": round(sxy / math.sqrt(sxx * syy), 3), "n": n}


def fiscal_year_fx():
    """Rata-rata USD/CNY per tahun fiskal Starbucks (Okt tahun lalu - Sep)."""
    buckets = {}
    for row in read_csv("fred_dexchus_usdcny_daily.csv"):
        v = row["DEXCHUS"]
        if not v or v == ".":
            continue
        d = date.fromisoformat(row["observation_date"])
        fy = d.year + 1 if d.month >= 10 else d.year
        buckets.setdefault(fy, []).append(float(v))
    return {fy: sum(v) / len(v) for fy, v in buckets.items()}


def annual_analysis(fx):
    rows = read_csv("starbucks_china_annual.csv")
    by_fy = {int(r["fiscal_year"]): r for r in rows}
    out = []
    for fy in range(2019, 2026):
        r, prev = by_fy[fy], by_fy[fy - 1]
        rev_usd = num(r["revenue_usd_m"])
        stores_end = num(r["company_operated_stores_end"])
        stores_begin = num(prev["company_operated_stores_end"])
        avg_stores = (stores_end + stores_begin) / 2
        rev_rmb = rev_usd * fx[fy]
        out.append({
            "fiscal_year": fy,
            "revenue_usd_m": rev_usd,
            "usdcny_avg": round(fx[fy], 4),
            "revenue_rmb_m": round(rev_rmb, 1),
            "stores_end": int(stores_end),
            "avg_stores": avg_stores,
            "revenue_per_store_usd_k": round(rev_usd / avg_stores * 1000, 1),
            "revenue_per_store_rmb_m": round(rev_rmb / avg_stores, 3),
            "net_new_pct_of_base": round((stores_end - stores_begin) / stores_begin * 100, 1),
            "stores_opened": int(num(r["stores_opened"])),
            "comp_sales_pct": num(r["comp_sales_pct"]),
            "comp_transactions_pct": num(r["comp_transactions_pct"]),
            "comp_ticket_pct": num(r["comp_ticket_pct"]),
        })
    return out


def quarterly_analysis():
    rows = read_csv("starbucks_china_quarterly.csv")
    out = []
    prev_stores = 6806  # akhir Q4 FY23 (press release Q4 FY2024)
    for r in rows:
        stores = num(r["store_count_end"])
        avg = (stores + prev_stores) / 2
        rev = num(r["revenue_usd_m"])
        out.append({
            "fiscal_quarter": r["fiscal_quarter"],
            "revenue_usd_m": rev,
            "store_count_end": int(stores),
            "revenue_per_store_usd_k_annualized": round(rev / avg * 4 * 1000, 1),
            "comp_sales_pct": num(r["comp_sales_pct"]),
            "comp_transactions_pct": num(r["comp_transactions_pct"]),
            "comp_ticket_pct": num(r["comp_ticket_pct"]),
        })
        prev_stores = stores
    return out


def luckin_analysis(fx_calendar):
    rows = read_csv("luckin_annual.csv")
    out = []
    for prev, r in zip(rows, rows[1:]):
        stores_end = num(r["total_stores_end"])
        avg = (stores_end + num(prev["total_stores_end"])) / 2
        rev = num(r["net_revenue_rmb_m"])
        out.append({
            "year": int(r["year"]),
            "net_revenue_rmb_m": rev,
            "stores_end": int(stores_end),
            "revenue_per_store_rmb_m": round(rev / avg, 3),
            "store_level_op_margin_pct": num(r["store_level_op_margin_pct"]),
        })
    return out


def calendar_fx():
    buckets = {}
    for row in read_csv("fred_dexchus_usdcny_daily.csv"):
        v = row["DEXCHUS"]
        if not v or v == ".":
            continue
        y = int(row["observation_date"][:4])
        buckets.setdefault(y, []).append(float(v))
    return {y: sum(v) / len(v) for y, v in buckets.items()}


def main():
    fx = fiscal_year_fx()
    annual = annual_analysis(fx)
    quarterly = quarterly_analysis()
    luckin = luckin_analysis(calendar_fx())

    a0, a1 = annual[0], annual[-1]
    store_effect = math.log(a1["avg_stores"] / a0["avg_stores"])
    productivity_effect = math.log(a1["revenue_per_store_rmb_m"] / a0["revenue_per_store_rmb_m"])
    total = math.log(a1["revenue_rmb_m"] / a0["revenue_rmb_m"])

    non_covid = [a for a in annual if a["fiscal_year"] not in (2020, 2021, 2022)]

    correlations = {
        "annual_store_count_vs_revenue_per_store_rmb": pearson(
            [a["stores_end"] for a in annual], [a["revenue_per_store_rmb_m"] for a in annual]),
        "annual_store_count_vs_revenue_per_store_rmb_ex_covid": pearson(
            [a["stores_end"] for a in non_covid], [a["revenue_per_store_rmb_m"] for a in non_covid]),
        "annual_net_new_pct_vs_comp_sales": pearson(
            [a["net_new_pct_of_base"] for a in annual], [a["comp_sales_pct"] for a in annual]),
        "annual_comp_sales_vs_transactions": pearson(
            [a["comp_sales_pct"] for a in annual], [a["comp_transactions_pct"] for a in annual]),
        "quarterly_transactions_vs_ticket": pearson(
            [q["comp_transactions_pct"] for q in quarterly], [q["comp_ticket_pct"] for q in quarterly]),
        "quarterly_comp_sales_vs_ticket": pearson(
            [q["comp_sales_pct"] for q in quarterly], [q["comp_ticket_pct"] for q in quarterly]),
        "quarterly_comp_sales_vs_transactions": pearson(
            [q["comp_sales_pct"] for q in quarterly], [q["comp_transactions_pct"] for q in quarterly]),
    }

    sbux_fy25_rmb = a1["revenue_rmb_m"]
    lk25 = luckin[-1]
    summary = {
        "revenue_rmb_growth_fy19_fy25_pct": round((a1["revenue_rmb_m"] / a0["revenue_rmb_m"] - 1) * 100, 1),
        "revenue_usd_growth_fy19_fy25_pct": round((a1["revenue_usd_m"] / a0["revenue_usd_m"] - 1) * 100, 1),
        "revenue_rmb_cagr_fy19_fy25_pct": round(((a1["revenue_rmb_m"] / a0["revenue_rmb_m"]) ** (1 / 6) - 1) * 100, 2),
        "store_growth_fy19_fy25_pct": round((a1["stores_end"] / a0["stores_end"] - 1) * 100, 1),
        "revenue_per_store_rmb_change_fy19_fy25_pct": round(
            (a1["revenue_per_store_rmb_m"] / a0["revenue_per_store_rmb_m"] - 1) * 100, 1),
        "revenue_per_store_usd_change_fy19_fy25_pct": round(
            (a1["revenue_per_store_usd_k"] / a0["revenue_per_store_usd_k"] - 1) * 100, 1),
        "log_decomposition_fy19_fy25": {
            "total_log_change": round(total, 3),
            "store_count_effect": round(store_effect, 3),
            "productivity_effect": round(productivity_effect, 3),
        },
        "starbucks_china_fy25_revenue_rmb_m": sbux_fy25_rmb,
        "luckin_2025_revenue_rmb_m": lk25["net_revenue_rmb_m"],
        "luckin_to_starbucks_revenue_ratio_2025": round(lk25["net_revenue_rmb_m"] / sbux_fy25_rmb, 2),
        "starbucks_vs_luckin_revenue_per_store_ratio_2025": round(
            a1["revenue_per_store_rmb_m"] / lk25["revenue_per_store_rmb_m"], 2),
    }

    # Sensitivitas pendapatan per m2 (ASUMSI ukuran gerai, BUKAN data yang dilaporkan)
    size_scenarios = []
    for sbux_sqm in (120, 180, 250):
        for lk_sqm in (40,):
            size_scenarios.append({
                "starbucks_avg_sqm_assumed": sbux_sqm,
                "luckin_avg_sqm_assumed": lk_sqm,
                "starbucks_rev_per_sqm_rmb_k": round(a1["revenue_per_store_rmb_m"] * 1000 / sbux_sqm, 1),
                "luckin_rev_per_sqm_rmb_k": round(lk25["revenue_per_store_rmb_m"] * 1000 / lk_sqm, 1),
            })

    output = {
        "generated": date.today().isoformat(),
        "notes": [
            "Pendapatan China = 'Net revenues: China' pada catatan geografis 10-K (berdasarkan lokasi pelanggan).",
            "Jumlah gerai = gerai company-operated akhir tahun fiskal; rata-rata = (awal + akhir)/2.",
            "FY2018 dikecualikan dari seri produktivitas karena konsolidasi JV East China di tengah tahun.",
            "Kurs = rata-rata harian FRED DEXCHUS per tahun fiskal (Okt-Sep).",
            "Pendapatan Luckin mencakup penjualan ke mitra (partnership stores), bukan GMV penuh; per-gerai Luckin karenanya understated.",
            "Korelasi dengan n=7 (tahunan) / n=10 (kuartalan) bersifat deskriptif, bukan bukti kausal.",
        ],
        "annual": annual,
        "quarterly": quarterly,
        "luckin": luckin,
        "correlations": correlations,
        "summary": summary,
        "revenue_per_sqm_sensitivity_ASSUMPTION": size_scenarios,
    }
    (DATA / "analysis_output.json").write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")

    print("FY | Rev USD m | Rev RMB m | Gerai | Rev/gerai RMB m | Net new % | Comp")
    for a in annual:
        print(f"{a['fiscal_year']} | {a['revenue_usd_m']:.1f} | {a['revenue_rmb_m']:.0f} | {a['stores_end']} | "
              f"{a['revenue_per_store_rmb_m']:.3f} | {a['net_new_pct_of_base']} | {a['comp_sales_pct']}")
    print("\nKuartalan:")
    for q in quarterly:
        print(q)
    print("\nLuckin:")
    for l in luckin:
        print(l)
    print("\nKorelasi:")
    for k, v in correlations.items():
        print(f"  {k}: r={v['r']} (n={v['n']})")
    print("\nRingkasan:")
    print(json.dumps(summary, indent=2))
    print("\nSensitivitas per m2 (asumsi):")
    for s in size_scenarios:
        print(s)


if __name__ == "__main__":
    main()
