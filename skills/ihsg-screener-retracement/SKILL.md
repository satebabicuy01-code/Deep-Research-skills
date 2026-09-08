---
name: ihsg-screener-retracement
user-invocable: true
allowed-tools: Bash, Read, Write
description: Screener saham IHSG / Bursa Efek Indonesia untuk menemukan emiten yang PERNAH NAIK TINGGI lalu SEDANG RETRACEMENT — sudah drop 50%-61,8% dari high terakhir tapi tetap likuid (rata-rata nilai transaksi 20 candle >= Rp 1 miliar). Data live dari Yahoo Finance, tanpa API key. Pakai saat pengguna minta "screener IHSG", "cari saham yang lagi retracement/koreksi dalam", "saham turun 50% dari puncak tapi likuid", "screener pullback saham Indonesia".
---

# IHSG Retracement Screener

Menyaring emiten Bursa Efek Indonesia (IDX) dengan pola **"pernah terbang, sekarang
sedang retracement dalam, tapi masih ramai ditransaksikan"**.

## Trigger
`/ihsg-screener-retracement` — atau permintaan natural seperti "buatkan screener
IHSG untuk saham yang sudah drop 50-61% dari puncaknya tapi likuid".

## Kriteria (default)
1. **Pernah naik tinggi** — sebelum puncak, harga sudah rally minimal **+100%**
   (harga sempat >= 2x lipat dari titik terendah sebelumnya).
2. **Sedang retracement** — dari **high terakhir** (250 candle / ~1 tahun terakhir)
   sudah drop di zona **50%–61,8%** (zona golden ratio Fibonacci).
3. **Likuid** — rata-rata **nilai transaksi** harian (harga penutupan × volume)
   dalam **20 candle** terakhir minimal **Rp 1.000.000.000**.

## Cara Menjalankan (Workflow)

### Step 1 — Cek dependensi
Script hanya butuh `requests` (Python 3.9+). Jika belum ada:
```bash
pip install requests
```

### Step 2 — Jalankan screener
Dari folder skill ini:
```bash
python3 screener.py
```
Untuk uji cepat sebelum run penuh, batasi jumlah emiten:
```bash
python3 screener.py --limit 30
```

### Step 3 — Sajikan hasil ke pengguna
- Tabel tercetak di terminal (diurutkan dari nilai transaksi terbesar).
- File CSV lengkap `ihsg_retracement_<tanggal>.csv` untuk ditinjau lebih lanjut.
Ringkas temuan penting (emiten paling likuid + drop paling dalam) untuk pengguna,
dan ingatkan bahwa ini alat screening teknikal — **bukan rekomendasi beli/jual**.

## Menyesuaikan Kriteria
| Kebutuhan | Perintah |
|---|---|
| Ubah zona drop (mis. 50%–78,6%) | `--min-drop 50 --max-drop 78.6` |
| "Minimal drop 50%" (tanpa batas atas) | `--min-drop 50 --max-drop 100` |
| Longgarkan syarat "pernah naik tinggi" | `--min-runup 50` |
| Matikan syarat "pernah naik tinggi" | `--no-runup` |
| Naikkan ambang likuiditas ke Rp 5 M | `--min-value 5000000000` |
| Pakai high all-time, bukan 1 tahun | `--peak-window 9999 --range max` |
| Acuan high pakai harga penutupan (anti bad-tick) | `--price close` |
| Urutkan berdasar drop terdalam | `--sort drop` |
| Universe sendiri | `--tickers /path/daftar.txt` |

Lihat semua opsi: `python3 screener.py --help`. Detail lengkap ada di `README.md`.

## Universe Emiten
`tickers.txt` memuat ratusan kode IDX lintas sektor (kode saja; nama perusahaan
diambil otomatis dari Yahoo). Daftar ini luas namun belum memuat seluruh ~900
emiten — tambahkan kode yang belum ada agar hasil makin lengkap. Kode delisting/
keliru otomatis dilewati.

## Catatan Penting
- Sumber data Yahoo Finance (ticker `.JK`), gratis & tanpa key; harga sudah
  disesuaikan stock-split.
- Nilai transaksi = harga × volume (pendekatan turnover), bukan angka broker resmi.
- Hasil hanya screening teknikal untuk mempersempit watchlist; selalu verifikasi
  fundamental & konteks berita sebelum mengambil keputusan.
