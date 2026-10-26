# Ebook: Membaca Dunia 2026 (Edisi Terverifikasi)

PDF siap baca: **[`dist/Membaca-Dunia-2026.pdf`](dist/Membaca-Dunia-2026.pdf)** (37 halaman A4, 20 grafik).

Ebook ini menggabungkan kerangka *Geopolitics for Dummies Vol. 1* (BlackQoral) dengan verifikasi dan pembaruan data dari folder [`riset-tatanan-dunia/`](../riset-tatanan-dunia/README.md). Data per 26 Oktober 2026. Bukan saran investasi.

## Struktur

| Folder | Isi |
|---|---|
| `data/` | CSV untuk setiap grafik, lengkap dengan kolom sumber |
| `charts/` | Grafik SVG yang dihasilkan dari `data/` |
| `src/` | Naskah HTML (`buku.html`, `cover.html`) dan gaya cetak (`style.css`) |
| `scripts/` | `build_charts.py` (data → grafik) dan `build_pdf.js` (HTML → PDF) |
| `dist/` | PDF final |

## Cara membangun ulang

```bash
pip install matplotlib pandas pypdf
python3 ebook/scripts/build_charts.py          # data → charts/*.svg dan data/*.csv
node ebook/scripts/build_pdf.js                # HTML → build/cover.pdf + build/isi.pdf (Playwright/Chromium)
python3 -c "from pypdf import PdfWriter, PdfReader; w=PdfWriter(); [w.append(PdfReader(f)) for f in ['ebook/build/cover.pdf','ebook/build/isi.pdf']]; w.write('ebook/dist/Membaca-Dunia-2026.pdf')"
```

Untuk memperbarui angka: ubah data di `scripts/build_charts.py` dan teks di `src/buku.html`, lalu jalankan ketiga perintah di atas.
