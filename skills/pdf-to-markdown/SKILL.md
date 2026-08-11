---
name: pdf-to-markdown
description: >
  Mengubah file PDF (berbasis teks, gambar, hasil scan, maupun screenshot)
  menjadi file Markdown yang terstruktur rapi. Gunakan skill ini setiap kali
  pengguna meminta konversi PDF ke Markdown, atau menyebut kata-kata seperti
  "konversi PDF", "ubah PDF ke markdown", "jadikan markdown", "convert PDF",
  "PDF to markdown", "ekstrak isi PDF", atau melampirkan file PDF/gambar dan
  meminta hasilnya dalam format teks/Markdown. Skill ini bekerja untuk semua
  jenis PDF: PDF digital (berteks), PDF hasil scan, PDF berisi gambar, maupun
  file gambar (PNG/JPG/JPEG) berupa screenshot dokumen.
---

# PDF to Markdown Skill

Skill ini mengubah file PDF atau gambar dokumen menjadi file Markdown yang
bersih dan terstruktur, dalam satu alur otomatis.

Alur kerja singkat:
1. Jalankan `scripts/extract_pdf.py` → ekstrak teks per halaman (otomatis
   deteksi teks vs OCR)
2. Gunakan kecerdasan Claude untuk menyusun teks mentah menjadi Markdown yang
   rapi dan bermakna
3. Simpan file `.md` di direktori yang sama dengan file sumber (atau sesuai
   permintaan pengguna)

---

## Langkah 0 — Temukan file input

File yang diunggah pengguna mungkin berada di salah satu lokasi:
- `/mnt/user-data/uploads/` (Claude.ai)
- `/root/.claude/uploads/<session-id>/` (Claude Code remote)
- Path yang disebut pengguna secara eksplisit

Cek lokasi yang relevan sebelum lanjut. Jangan asumsikan file sudah ada tanpa
memverifikasinya dengan `ls`.

---

## Langkah 1 — Jalankan skrip ekstraksi

```bash
python /root/.claude/skills/pdf-to-markdown/scripts/extract_pdf.py \
  "<path/ke/file.pdf>" \
  [--lang eng+ind] \
  [--dpi 200] \
  [--force-ocr]
```

**Argumen penting:**

| Argumen | Default | Keterangan |
|---------|---------|------------|
| `input` | *(wajib)* | Path ke PDF, PNG, JPG, atau JPEG |
| `--lang` | otomatis | Bahasa OCR: `eng`, `ind`, `eng+ind`, dll. Jika tidak diset, skrip memilih otomatis dari bahasa yang terinstall |
| `--dpi` | `200` | Resolusi render untuk PDF gambar. Naikkan ke `300` untuk PDF kecil atau teks yang rapat |
| `--force-ocr` | false | Lewati coba-teks-langsung; langsung ke OCR |
| `--min-chars` | `80` | Batas rata-rata karakter/halaman untuk dianggap PDF berteks |

Output skrip adalah JSON ke stdout:
```json
{
  "meta": {"filename": "laporan.pdf", "total_pages": 25, "title": "...", "author": "..."},
  "method": "text-direct | ocr-pdf | ocr-image",
  "ocr_lang": "eng+ind",
  "pages": [
    {"page": 1, "total": 25, "text": "teks halaman 1..."},
    {"page": 2, "total": 25, "text": "teks halaman 2..."}
  ]
}
```

**Tangani error umum:**
- Kalau `pdfplumber` / `pypdf` belum ada: `pip install pdfplumber pypdf cffi -q`
- Kalau `ghostscript` belum ada: `apt-get install -y ghostscript -q`
- Kalau `tesseract` belum ada: `apt-get install -y tesseract-ocr tesseract-ocr-ind -q`
- Kalau CFI backend error: `pip install cffi -q` lalu coba lagi

---

## Langkah 2 — Analisis teks mentah

Setelah mendapat JSON, baca seluruh teks per halaman dan pahami:

1. **Struktur dokumen** — apakah ada judul utama, bab, sub-bab, tabel, daftar?
2. **Bahasa** — Indonesia, Inggris, atau campuran?
3. **Tipe konten** — laporan, artikel, slide presentasi, buku, formulir?
4. **Artefak OCR** — karakter aneh, spasi ganda, baris terpotong, kata
   yang tergabung (misalnya "thisis" → "this is") perlu dibersihkan

Gunakan penilaianmu sebagai pembaca cerdas, bukan sekadar menyalin teks mentah.

---

## Langkah 3 — Susun Markdown yang bermakna

Buat file Markdown mengikuti panduan ini:

### Hierarki heading
- Judul dokumen → `# Judul`
- Bab / bagian utama → `## Bab`
- Sub-bab → `### Sub-bab`
- Sub-sub-bab → `#### Sub-sub-bab`

Deteksi heading dari pola: baris pendek yang diikuti paragraf, teks semua
huruf kapital, nomor bab (mis. "BAB 1", "Section 2"), atau ukuran font berbeda
yang terlihat dari konteks.

### Tabel
Kalau teks mentah terlihat seperti data tabular (kolom yang sejajar, angka
terstruktur), konversikan ke tabel Markdown:
```markdown
| Kolom A | Kolom B | Kolom C |
|---------|---------|---------|
| nilai   | nilai   | nilai   |
```

### Daftar / bullet
Kalau ada pola `•`, `-`, `*`, nomor, atau indentasi terstruktur, gunakan
daftar Markdown:
```markdown
- item satu
- item dua
  - sub-item
```

### Blockquote & callout
Untuk kotak highlight, catatan penting, atau kutipan:
```markdown
> **Catatan:** isi catatan penting di sini
```

### Kode / formula
Untuk teks monospace, kode, atau rumus matematika:
```markdown
`kode inline` atau blok kode:
```python
print("hello")
```
```

### Pembatas halaman (opsional)
Kalau dokumen punya bab yang jelas, tambahkan `---` sebagai pemisah bagian.
Jangan tambahkan `---` antar setiap halaman — hanya antar bagian logis.

### Artefak yang harus dibersihkan
- Header/footer berulang (nomor halaman, nama perusahaan, tanggal) → hapus
  jika muncul di setiap halaman
- Baris kosong berlebihan → maksimal 1 baris kosong antar paragraf
- Spasi ganda di dalam kata → normalisasi
- Tanda baca OCR yang salah → perbaiki jika jelas salah
- Kata terpotong di batas halaman → sambungkan

---

## Langkah 4 — Simpan file

Nama file default: nama PDF yang sama, ekstensi diganti `.md`.
Contoh: `laporan_keuangan.pdf` → `laporan_keuangan.md`

Simpan di direktori kerja aktif atau direktori yang diminta pengguna.

Setelah menyimpan, laporkan:
- Nama file yang disimpan
- Jumlah halaman yang diproses
- Metode yang digunakan (ekstraksi teks langsung / OCR)
- Bahasa OCR (jika OCR digunakan)

Kirimkan file ke pengguna menggunakan tool `SendUserFile` (jika tersedia).

---

## Panduan kualitas

**Tujuan:** Pembaca yang membaca Markdown hasilnya harus mendapat pemahaman
yang sama dengan membaca PDF asli — tanpa perlu melihat PDF-nya.

- Jaga kesetiaan pada isi: jangan mengarang, jangan merangkum kecuali diminta
- Jaga nama, angka, dan urutan: persis seperti di sumber
- Jika ada bagian yang tidak bisa dibaca (gambar chart, diagram, foto), tambahkan
  catatan: `> *[Gambar: deskripsi singkat konten visual]*`
- Jika OCR menghasilkan teks yang tidak masuk akal, tandai:
  `> *[Teks tidak terbaca — kemungkinan gambar atau tabel kompleks]*`

---

## Penanganan kasus khusus

| Kasus | Penanganan |
|-------|------------|
| PDF terenkripsi (password-protected) | Minta password ke pengguna, atau: `qpdf --password=PASS --decrypt in.pdf out.pdf` |
| PDF hasil scan tanpa teks | Otomatis ke OCR; kalau kualitas rendah, naikkan `--dpi 300` |
| Slide presentasi (PowerPoint-to-PDF) | Setiap slide jadi satu sub-bagian; caption gambar dipertahankan |
| Formulir PDF | Ekstrak label field dan nilai yang terisi; susun sebagai daftar atau tabel |
| PDF multi-kolom (koran, majalah) | pdfplumber sering menggabungkan kolom secara acak; gunakan `--force-ocr` jika hasilnya kacau |
| Screenshot gambar (PNG/JPG) | Langsung OCR; tidak perlu render ulang |
| PDF sangat besar (>100 halaman) | Proses tetap utuh; skrip menangani per halaman tanpa memuat semuanya ke memori |
| Bahasa campuran | Gunakan `--lang eng+ind` (atau tambahkan bahasa lain yang terinstall) |

---

## Checklist sebelum selesai

- [ ] Semua halaman diproses (cek `total_pages` di meta vs jumlah elemen `pages`)
- [ ] Heading terdeteksi dan menggunakan hierarki `#` / `##` / `###` yang benar
- [ ] Tabel disusun sebagai tabel Markdown (bukan teks mentah berjajar)
- [ ] Daftar menggunakan `-` atau `1.` (bukan karakter OCR acak)
- [ ] Header/footer berulang sudah dihapus
- [ ] Artefak OCR (kata terpotong, spasi ganda) sudah dibersihkan
- [ ] File `.md` sudah disimpan dan dikirim ke pengguna
