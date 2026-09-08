# IHSG Retracement Screener

Screener saham **Bursa Efek Indonesia (IHSG / IDX)** untuk menemukan emiten dengan
pola: **pernah naik tinggi → sekarang sedang retracement dalam → tapi tetap likuid.**

Cocok untuk mempersempit watchlist mencari kandidat *pullback / mean-reversion* pada
saham yang sempat terbang lalu terkoreksi ke zona golden ratio Fibonacci.

---

## Pola yang dicari

| # | Kriteria | Default | Alasan |
|---|----------|---------|--------|
| 1 | **Pernah naik tinggi** | rally ke puncak **≥ 100%** | memastikan saham memang sempat "terbang", bukan sekadar sideways |
| 2 | **Sedang retracement** | drop **50%–61,8%** dari *high terakhir* | zona koreksi dalam (0.5–0.618 Fibonacci) |
| 3 | **Likuid** | rata-rata nilai transaksi 20 candle **≥ Rp 1 miliar** | menyingkirkan saham "tidur"/tidak bisa ditransaksikan |

- **High terakhir** = harga tertinggi dalam **250 candle** (~1 tahun bursa) terakhir.
- **Nilai transaksi harian** = `harga penutupan × volume` (pendekatan *turnover*).
- Harga & volume sudah **disesuaikan stock-split**, jadi split tidak terbaca sebagai crash.

---

## Instalasi

Butuh **Python 3.9+** dan satu paket saja:

```bash
pip install -r requirements.txt   # atau: pip install requests
```

Tidak perlu API key. Data diambil dari Yahoo Finance chart API (ticker IDX = `KODE.JK`).

---

## Pemakaian

```bash
# Screening penuh dengan default (universe bawaan tickers.txt)
python3 screener.py

# Uji cepat 30 emiten pertama
python3 screener.py --limit 30

# Simpan hasil ke file tertentu
python3 screener.py --out hasil_hari_ini.csv
```

Output:
1. **Tabel di terminal** — kode, drop%, runup%, nilai transaksi/hari, harga, puncak, tanggal puncak, nama.
2. **File CSV** `ihsg_retracement_<tanggal>.csv` berisi seluruh kolom metrik.

Contoh cuplikan output:

```
KODE    DROP%   RUNUP%       NILAI/HR     HARGA    PUNCAK  TGL PUNCAK  NAMA
BUMI     53.3      591 Rp572.197.796.715       226       484  2026-01-06  PT Bumi Resources Tbk
PTRO     58.3     1150 Rp244.244.142.750     5.425    13.000  2026-01-15  PT Petrosea Tbk
WIFI     52.5     1711 Rp76.587.527.025     2.100     4.420  2025-12-12  PT Solusi Sinergi Digital Tbk
...
```

---

## Opsi (CLI)

| Opsi | Default | Keterangan |
|------|---------|------------|
| `--tickers PATH` | `tickers.txt` | file daftar kode emiten (1 per baris, `#` komentar) |
| `--min-drop` | `50` | batas bawah drop dari high terakhir (%) |
| `--max-drop` | `61.8` | batas atas drop dari high terakhir (%) |
| `--min-runup` | `100` | minimal rally ke puncak ("pernah naik tinggi", %) |
| `--no-runup` | off | matikan filter "pernah naik tinggi" |
| `--peak-window` | `250` | jumlah candle terakhir untuk mencari high terakhir |
| `--price` | `high` | acuan high: `high` (intraday) atau `close` (penutupan) |
| `--liq-window` | `20` | jumlah candle untuk rata-rata nilai transaksi |
| `--min-value` | `1000000000` | minimal rata-rata nilai transaksi harian (Rupiah) |
| `--range` | `2y` | rentang histori Yahoo (`1y`,`2y`,`5y`,`10y`,`max`) |
| `--workers` | `8` | jumlah thread pengambil data paralel |
| `--limit` | `0` | batasi jumlah emiten (0 = semua) untuk uji cepat |
| `--sort` | `value` | urutan hasil: `value` / `drop` / `runup` |
| `--out` | otomatis | path CSV output |
| `--quiet` | off | sembunyikan progres |

### Resep umum

```bash
# "Minimal drop 50%" tanpa batas atas
python3 screener.py --min-drop 50 --max-drop 100

# Zona retracement lebih dalam (50%–78,6%)
python3 screener.py --min-drop 50 --max-drop 78.6

# Pakai high sepanjang masa (all-time high), bukan 1 tahun
python3 screener.py --peak-window 9999 --range max

# Anti bad-tick: acuan high pakai harga penutupan
python3 screener.py --price close

# Hanya saham sangat likuid (≥ Rp 5 miliar/hari), urut drop terdalam
python3 screener.py --min-value 5000000000 --sort drop
```

---

## Universe emiten (`tickers.txt`)

- Berisi **ratusan kode IDX** lintas sektor (perbankan, energi, tambang, konsumer,
  properti, teknologi, dll). **Cukup tulis kodenya**; nama perusahaan diambil
  otomatis dari Yahoo saat run.
- Daftar ini **luas tapi belum lengkap** (~900 emiten total di IDX). Silakan tambah
  kode yang belum ada — makin lengkap universe, makin baik hasil screening.
- Kode yang salah/delisting otomatis dilewati (respons 404).
- Ingin universe sendiri? Buat file teks (1 kode/baris) lalu:
  `python3 screener.py --tickers daftar_saya.txt`.

---

## Cara kerja singkat

Untuk tiap emiten:
1. Ambil histori harian OHLCV (default 2 tahun) dari Yahoo Finance.
2. `peak` = nilai tertinggi (high/close) dalam `peak-window` candle terakhir → `drop% = (peak − harga_terkini) / peak`.
3. `runup% = (peak − low terendah sebelum puncak) / low terendah` → seberapa tinggi ia sempat naik.
4. `nilai transaksi rata-rata` = mean(`close × volume`) selama `liq-window` candle terakhir.
5. Lolos bila ketiga kriteria terpenuhi. Pengambilan data paralel (thread) + retry otomatis.

---

## Keterbatasan & disclaimer

- **Bukan rekomendasi jual/beli.** Ini alat *screening teknikal* untuk mempersempit
  watchlist. Selalu verifikasi fundamental, aksi korporasi, dan konteks berita.
- Nilai transaksi = pendekatan `harga × volume`, bukan angka *value* resmi broker/IDX.
- Data Yahoo Finance bisa terlambat/berbeda tipis dari data bursa; sesekali ada
  *bad tick* pada high intraday — pakai `--price close` untuk hasil lebih tahan-banting.
- Universe tidak memuat seluruh emiten; kandidat di luar daftar tidak akan muncul.
