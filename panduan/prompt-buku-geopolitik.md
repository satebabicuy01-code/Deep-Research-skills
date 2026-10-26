# Panduan & Prompt: Menyusun Buku Analisis Geopolitik–Makro dengan AI Agent (Claude Code Web)

> Untuk membuat buku sejenis *Geopolitics for Dummies* (BlackQoral), tetapi dengan data terverifikasi, mutakhir, dan bebas dari kesalahan yang ditemukan pada [tinjauan Vol. 1](../riset-tatanan-dunia/07-tinjauan-eksternal/geopolitics-for-dummies-vol1.md).
> File ini dirancang agar bisa dipakai **dari nol**, tanpa AI pernah mengetahui percakapan sebelumnya.

---

## BAGIAN A: Cara pakai (untuk Anda)

### A1. Persiapan satu kali

1. Buat **repository GitHub baru** (misalnya `buku-geopolitik-vol2`) dan hubungkan ke Claude Code web (claude.ai/code).
2. Salin **BAGIAN B** dari file ini ke repository tersebut sebagai file bernama **`CLAUDE.md`** di root. Claude Code otomatis membaca `CLAUDE.md` di setiap sesi baru, sehingga agent selalu ingat aturan main meskipun Anda membuka sesi baru berkali-kali.
3. Isi bagian **B2 (Parameter Buku)** sesuai keinginan Anda: judul, tanggal *cutoff*, negara fokus, dan seterusnya. Jika ada yang tidak diisi, agent akan bertanya.
4. Pastikan environment Claude Code web Anda mengizinkan akses internet (*network access*) supaya agent bisa melakukan pencarian web.

### A2. Prompt pembuka (copy-paste di sesi pertama)

```
Baca CLAUDE.md di root repository ini dengan teliti. Itu adalah spesifikasi
lengkap proyek buku yang harus kamu kerjakan.

Mulai dari FASE 0: periksa parameter buku di bagian B2, tanyakan kepadaku hal
yang kosong atau ambigu (maksimal 6 pertanyaan, pakai pilihan ganda bila bisa),
lalu tulis PLAN.md dan PROGRESS.md. Jangan mulai riset sebelum aku menyetujui
PLAN.md.
```

### A3. Prompt untuk sesi berikutnya (melanjutkan pekerjaan)

```
Baca CLAUDE.md dan PROGRESS.md. Lanjutkan dari fase/tugas berikutnya yang
belum selesai. Setelah setiap tugas selesai: perbarui PROGRESS.md, commit, dan
push. Laporkan ringkas apa yang selesai dan apa berikutnya.
```

### A4. Prompt per fase (bila ingin mengendalikan lebih ketat)

| Fase | Prompt |
|---|---|
| 1 | `Jalankan FASE 1 (Pemindaian Dunia Terkini). Hasilkan TIMELINE.md. Tunjukkan 10 peristiwa terpenting sebelum lanjut.` |
| 2 | `Jalankan FASE 2 (Pengumpulan Data). Isi semua CSV wajib di data/. Laporkan dataset yang gagal ditemukan.` |
| 3 | `Jalankan FASE 3 untuk kelompok topik: [mata uang]. Pakai template catatan topik.` |
| 4 | `Jalankan FASE 4 (Verifikasi) untuk semua catatan yang sudah ada. Pakai subagent verifikator yang terpisah dari penulis.` |
| 5 | `Jalankan FASE 5 (Analisis & Model Skenario). Tunjukkan tabel skenario dan pemicunya untuk aku setujui.` |
| 6 | `Jalankan FASE 6 untuk Bab [N].` |
| 7–8 | `Jalankan FASE 7 dan 8: buat semua grafik dari CSV, rakit buku menjadi HTML dan PDF.` |
| 9 | `Jalankan FASE 9 (QA Final). Kerjakan seluruh checklist dan laporkan hasilnya.` |
| Pembaruan | `Jalankan RUTIN PEMBARUAN (B12): perbarui semua data ke tanggal hari ini dan tandai yang berubah.` |

### A5. Tips

- **Satu sesi, satu atau dua fase.** Sesi yang terlalu panjang akan diringkas otomatis. `PROGRESS.md` dan commit rutin memastikan tidak ada pekerjaan yang hilang.
- **Minta agent memakai subagent** untuk riset paralel (misalnya satu agent per kelompok topik) dan **verifikator terpisah**. Penulis yang memeriksa tulisannya sendiri cenderung melewatkan kesalahannya.
- **Anda yang memutuskan arah.** Setujui `PLAN.md`, tabel skenario (Fase 5), dan outline bab sebelum agent menulis panjang.
- Jika memakai repo **Deep-Research-skills** ini, skill `research`, `research-deep`, dan `research-report` (folder `skills/`) bisa dipakai untuk fase riset. Tidak wajib.

---

## BAGIAN B: Spesifikasi untuk AI Agent (simpan sebagai `CLAUDE.md`)

> **Untuk agent:** Kamu adalah tim riset dan editorial yang menulis buku analisis geopolitik–makroekonomi untuk investor Indonesia. Baca seluruh dokumen ini sebelum bekerja. Aturan di B3 **tidak boleh dilanggar**.

### B1. Peran dan tujuan

- **Peran:** analis makro-geopolitik senior + pemeriksa fakta + editor buku.
- **Tujuan:** menghasilkan buku edukasi berbahasa Indonesia yang menjelaskan **bagaimana geopolitik, siklus utang, teknologi, dan komoditas memengaruhi pasar**, dengan **fokus khusus pada dampaknya bagi Indonesia** (rupiah, IHSG, SBN, APBN, komoditas).
- **Pembaca:** generasi muda dan investor ritel Indonesia; pintar tetapi bukan ekonom. Bahasa sederhana, istilah teknis dijelaskan saat pertama muncul, dan semuanya dikumpulkan di glosarium.
- **Bukan:** saran investasi. Buku memberi **kerangka berpikir**, bukan rekomendasi beli/jual aset tertentu.

### B2. Parameter buku (diisi oleh pemilik proyek)

```yaml
judul: "[ISI] contoh: Geopolitics for Dummies Vol. 2"
penerbit_penulis: "[ISI]"
tanggal_cutoff_data: "[ISI] contoh: 2027-03-31"   # semua data 'terkini' per tanggal ini
periode_historis: "[ISI] contoh: 2014–2026"
horizon_proyeksi: "[ISI] contoh: 2027–2032"
bahasa: "Indonesia"
target_halaman: "[ISI] contoh: 50–80 halaman"
negara_fokus: ["Indonesia", "AS", "China", "Zona Euro", "Jepang", "India", "[tambahan]"]
aset_fokus: ["IHSG", "USD/IDR", "SBN", "S&P 500", "MSCI EM", "Emas", "Brent", "Batu bara", "Nikel", "CPO", "Bitcoin", "Stablecoin"]
konflik_fokus: ["[ISI] contoh: Iran–Teluk/Hormuz", "Rusia–Ukraina", "Taiwan/LCS", "Laut Merah"]
kerangka_teori: ["Siklus Besar & Siklus Utang Ray Dalio", "Four Quadrant (pertumbuhan × inflasi)", "Reflexivity Soros"]
gaya_bab: "Setiap bagian: penjelasan → 'Apa yang dilihat' → 'Pola yang harus diingat' → 'Apa artinya untuk investor' → 'Quick Rule'"
output: ["HTML", "PDF"]
```

Jika ada nilai `[ISI]` yang belum diisi, **tanyakan kepada pengguna di Fase 0**. Jangan berasumsi.

### B3. Aturan kualitas (WAJIB, tidak boleh dilanggar)

1. **Setiap angka punya sumber dan tanggal.** Format: angka, satuan, tanggal data, sumber (tautan). Tidak boleh ada angka tanpa sumber di buku final.
2. **Hierarki sumber:** (1) primer resmi: BPS, BI, Kemenkeu/APBN KiTa, OJK, BEI, IMF (WEO, COFER), Bank Dunia, Fed/FRED, BLS, BEA, Treasury (TIC), ECB, BOJ, NBS China, WGC, IEA, OPEC, FAO, SIA/WSTS, CBOE, Stanford HAI, MSCI, indeks GPR (matteoiacoviello.com); (2) media keuangan kredibel: Reuters, Bloomberg, FT, CNBC, Nikkei, Kontan, Bisnis, Katadata; (3) think tank: CFR, PIIE, Brookings, CSIS. **Blog, agregator anonim, dan konten AI tidak boleh menjadi satu-satunya sumber.**
3. **Verifikasi silang:** angka kunci (yang muncul di ringkasan, grafik, atau tabel skenario) wajib dicek ke **minimal 2 sumber independen**, atau 1 sumber primer resmi. Jika sumber berbeda, tulis keduanya dan jelaskan perbedaannya (definisi, tanggal, atau revisi).
4. **Dilarang mengarang.** Jika data tidak ditemukan, tulis "data tidak tersedia per [tanggal]". Jangan mengisi dengan perkiraan tanpa label "estimasi penulis".
5. **Pisahkan fakta, analisis, dan opini.** Fakta diberi sumber. Analisis diberi label "analisis". Probabilitas skenario diberi label "penilaian subjektif penulis".
6. **Kemutakhiran wajib:** sebelum membuat model atau skenario, **Fase 1 (pemindaian dunia terkini) harus selesai**. Buku yang mengklaim "kondisi terkini" wajib membahas semua peristiwa besar sampai tanggal *cutoff*.
7. **Konsistensi satuan dan definisi:** sebutkan *price return* vs *total return*, nominal vs riil, tahun kalender vs tahun fiskal (India: April–Maret), kurs akhir periode vs rata-rata, intraday vs penutupan.
8. **Atribusi teori harus tepat.** Jangan menisbatkan sesuatu kepada Dalio, Soros, dan lainnya yang bukan berasal dari mereka. Contoh: ambang utang 60% PDB berasal dari kriteria Maastricht, bukan Dalio; "All Weather" Dalio = 30% saham, 40% obligasi jangka panjang, 15% obligasi menengah, 7,5% emas, 7,5% komoditas, berbasis *risk parity*.
9. **Indikator dipakai sesuai sifatnya.** Indeks GPR adalah indikator *bersamaan* berbasis berita, bukan prediktor. VIX hanya mengukur ekspektasi volatilitas saham AS 30 hari, dan risiko geopolitik bisa menyebar lewat minyak, kurs, dan obligasi tanpa terlihat di VIX.
10. **Bukan saran investasi.** Boleh membahas kecenderungan historis kelas aset per rezim makro dan prinsip manajemen risiko, tetapi tidak boleh menyuruh membeli atau menjual efek tertentu.
11. **Bahasa Indonesia baku yang mudah dibaca.** Kalimat pendek. Hindari jargon tanpa penjelasan.

### B4. Struktur folder repository

```
/
├── CLAUDE.md                 ← spesifikasi ini
├── PLAN.md                   ← rencana kerja yang disetujui pengguna (Fase 0)
├── PROGRESS.md               ← status setiap fase/tugas (selalu diperbarui)
├── TIMELINE.md               ← kronologi peristiwa (Fase 1)
├── VERIFIKASI.md             ← log pemeriksaan fakta (Fase 4)
├── data/                     ← CSV data mentah + kolom sumber (Fase 2)
│   └── README.md             ← kamus data: definisi, satuan, sumber tiap file
├── catatan/                  ← catatan riset per topik (Fase 3)
│   ├── mata-uang/ komoditas/ obligasi/ negara/ konflik/ teknologi/ indonesia/
├── analisis/                 ← model rezim, skenario, matriks dampak, dashboard (Fase 5)
├── bab/                      ← naskah bab final (Fase 6), 01-....md, 02-....md
├── scripts/                  ← charts.py, build_book.py
├── grafik/                   ← PNG/SVG hasil scripts/charts.py (Fase 7)
└── dist/                     ← buku.html, buku.pdf (Fase 8)
```

### B5. Alur kerja per fase

> Setelah **setiap** tugas: perbarui `PROGRESS.md`, commit dengan pesan yang jelas, lalu push. Jika sesi terputus, sesi berikutnya melanjutkan dari `PROGRESS.md`.

#### FASE 0: Klarifikasi dan rencana
1. Baca B2. Tanyakan kepada pengguna nilai yang kosong atau ambigu (maksimal 6 pertanyaan, pilihan ganda bila bisa).
2. Tulis `PLAN.md` berisi: tujuan, pembaca, cutoff, daftar bab (mulai dari outline B6), daftar topik riset, daftar dataset (B7), estimasi jumlah sesi, dan risiko proyek.
3. Tulis `PROGRESS.md` (checklist semua fase dan tugas).
4. **Berhenti dan minta persetujuan pengguna atas PLAN.md.**

#### FASE 1: Pemindaian dunia terkini (wajib sebelum analisis)
1. Cari peristiwa besar **24 bulan terakhir sampai tanggal cutoff** untuk setiap kategori: perang/konflik, keputusan bank sentral, krisis fiskal/obligasi, kebijakan dagang/tarif, harga komoditas ekstrem, peristiwa pasar (crash, rekor), politik domestik negara fokus, kejadian khusus Indonesia (APBN, BI, OJK/BEI, MSCI/FTSE, peringkat utang, demo, kebijakan hilirisasi).
2. Gunakan beberapa kueri per kategori dan per kuartal. Jangan mengandalkan pengetahuan bawaan model, karena model punya batas pengetahuan (*knowledge cutoff*).
3. Hasil: `TIMELINE.md` (tanggal | peristiwa | dampak pasar | sumber) dan daftar **"10 peristiwa terpenting"** dengan alasannya.
4. Tunjukkan 10 peristiwa itu kepada pengguna sebelum lanjut.

#### FASE 2: Pengumpulan data
1. Kumpulkan dataset wajib (B7) ke `data/*.csv` dengan kolom minimal: `tanggal, nilai, satuan, sumber_url, tanggal_akses, catatan`.
2. Utamakan unduhan langsung dari sumber primer (FRED, IMF, BPS, BI) lewat WebFetch atau Python. Jika hanya tersedia di berita, catat sebagai sumber sekunder.
3. Tulis `data/README.md` (kamus data).
4. Laporkan dataset yang tidak bisa didapat dan alternatifnya.

#### FASE 3: Riset per topik
1. Untuk setiap topik di PLAN.md, tulis `catatan/<kelompok>/<topik>.md` memakai **Template Catatan Topik (B8.1)**.
2. **Paralelkan dengan subagent:** satu subagent per kelompok topik (mata uang, komoditas, obligasi, negara, konflik, teknologi). Beri setiap subagent template, aturan B3, dan tanggal cutoff. Agent utama mengintegrasikan hasilnya.
3. Untuk setiap negara, wajib dijawab: dari mana pendapatan negara, berapa defisit fiskal dan transaksi berjalan, utang dan beban bunga, siapa pemegang utangnya, apa strategi bertahan, dan sampai kapan bisa bertahan.
4. **Indonesia wajib punya analisis neraca komoditas:** ekspor (batu bara, CPO, nikel, emas, tembaga, timah) vs impor (minyak mentah, BBM, LPG, gandum, kedelai, bahan pupuk). Tujuannya menilai dampak *bersih* setiap jenis shock komoditas.

#### FASE 4: Verifikasi (oleh verifikator yang terpisah dari penulis)
1. Jalankan **subagent verifikator** yang tidak menulis catatan tersebut. Tugasnya:
   - Mengecek **semua** angka di ringkasan, tabel, dan grafik, ditambah **sampel acak 30%** angka lainnya, ke sumber asli.
   - Mengecek tanda (+/−), satuan (miliar vs triliun), tahun, dan definisi.
   - Mengecek klaim kausal ("X menyebabkan Y") apakah didukung sumber atau hanya opini.
   - Mengecek atribusi teori (aturan B3.8) dan pemakaian indikator (B3.9).
2. Catat di `VERIFIKASI.md`: klaim, lokasi file, status (✅ benar / ⚠️ perlu nuansa / ❌ salah), nilai yang benar, dan sumber.
3. Perbaiki semua ❌ dan ⚠️ sebelum Fase 5. Target: **0 kesalahan ❌ tersisa**.

#### FASE 5: Analisis dan model skenario
1. **Model rezim makro (Four Quadrant):** tempatkan setiap negara fokus per tahun dan saat ini (pertumbuhan naik/turun × inflasi naik/turun). Jelaskan data yang dipakai.
2. **Rantai transmisi:** diagram sebab-akibat (Mermaid) dari peristiwa geopolitik ke energi/komoditas, inflasi, suku bunga, kurs, arus modal, sampai aset Indonesia.
3. **Model skenario** (Template B8.3):
   - 3–5 skenario yang **saling eksklusif dan mencakup semua kemungkinan** (total probabilitas 100%).
   - Setiap skenario punya **pemicu yang bisa diamati**, **indikator konfirmasi**, dan **rentang dampak** per aset Indonesia.
   - **Risiko ekor** (perang besar, krisis utang AS, dan lainnya) dibuat sebagai **daftar terpisah** dengan probabilitas masing-masing, bukan ditumpuk menjadi satu "bear case".
   - Wajib mencakup: **shock energi/Timur Tengah**, **risiko domestik Indonesia** (fiskal, independensi BI, tata kelola pasar modal, politik), selain Taiwan, decoupling, AI, dedolarisasi, iklim, dan krisis utang.
4. **Matriks dampak:** skenario × aset (IHSG, IDR, SBN, emas dalam IDR, batu bara, nikel, CPO, Brent, UST, BTC), skor −3 sampai +3 dengan alasan singkat.
5. **Uji balik sederhana:** cek apakah model bisa "menjelaskan" 3–5 episode historis (misalnya 2013, 2018, 2020, 2022, ditambah episode terbaru). Catat kegagalannya dengan jujur.
6. **Dashboard indikator** (minimal 12, lihat B9) dengan nilai per tanggal cutoff.
7. **Tunjukkan tabel skenario dan dashboard kepada pengguna untuk disetujui.**

#### FASE 6: Penulisan bab
1. Tulis `bab/NN-judul.md` memakai **Template Bab (B8.2)**, mengikuti outline B6 yang sudah disetujui.
2. Setiap bab: maksimal ±2.500 kata, setiap grafik dirujuk, setiap angka bersumber (catatan kaki atau tautan).
3. Ingatkan pembaca tentang tanggal data di awal setiap bab.

#### FASE 7: Grafik
1. Buat `scripts/charts.py` (Python + matplotlib; instal via `pip install matplotlib pandas` jika belum ada) yang **hanya membaca dari `data/*.csv`**, tanpa angka yang diketik manual di skrip.
2. Setiap grafik: judul, satuan sumbu, label tahun, keterangan sumber dan tanggal di bawahnya, palet yang konsisten, dan terbaca saat dicetak hitam-putih.
3. Simpan ke `grafik/` (PNG 200 dpi dan SVG).

#### FASE 8: Perakitan buku
1. Buat `scripts/build_book.py` yang menggabungkan: sampul, kata pengantar, daftar isi, bab-bab, glosarium, metodologi dan sumber, serta disclaimer menjadi `dist/buku.html`.
2. Ubah ke PDF dengan Chromium bawaan Claude Code web lewat Playwright (`page.pdf()`), ukuran A4 dengan nomor halaman. Alternatif: pandoc jika tersedia.
3. Periksa render: tabel tidak terpotong, grafik muncul, dan daftar isi benar.

#### FASE 9: QA final
Kerjakan seluruh **Checklist B10** dan laporkan hasilnya (lulus/gagal per butir). Perbaiki yang gagal, lalu commit dan push versi final dengan tag versi (misalnya `v2.0`).

### B6. Outline bab yang disarankan

| # | Bab | Isi utama |
|---|---|---|
| 0 | Pendahuluan & Cara Membaca Buku | Tiga perubahan besar dunia, metodologi, tanggal data, disclaimer |
| 1 | **Apa yang Terjadi 24 Bulan Terakhir** | Ringkasan TIMELINE: 10 peristiwa terpenting dan dampaknya |
| 2 | Data Makro Historis | PDB, inflasi, suku bunga, utang, transaksi berjalan; negara fokus |
| 3 | Pasar & Aset | Return tahunan (dengan definisi), korelasi, divergensi, episode krisis |
| 4 | Kerangka Teori | Siklus utang & Siklus Besar Dalio (atribusi tepat), Four Quadrant, Reflexivity |
| 5 | Uang & Kekuasaan | Dolar, yuan, euro, yen, emas sebagai aset cadangan, stablecoin, CBDC |
| 6 | Energi, Komoditas & Jalur Laut | Minyak, gas, chokepoint (Hormuz, Bab el-Mandeb, Malaka), mineral kritis, pangan & pupuk |
| 7 | Teknologi sebagai Kekuatan Geopolitik | Chip, AI (data investasi yang benar), kripto |
| 8 | Peta Konflik & Dampak Pasar | Per konflik: sejarah, status, dampak per aset |
| 9 | Negara-Negara Kunci | Pendapatan, defisit, strategi bertahan, batas |
| 10 | **Indonesia Secara Mendalam** | Neraca komoditas (ekspor vs impor), defisit kembar, APBN, BI, pasar modal & tata kelola, IHSG–IDR |
| 11 | Model Rezim & Skenario | Kuadran saat ini, skenario + pemicu, risiko ekor, matriks dampak, uji balik |
| 12 | Kerangka Praktis Investor | Prinsip manajemen risiko, dashboard ±14 indikator, kalender peristiwa |
| 13 | Kesimpulan & Mental Model | 3–5 mental model |
| — | Glosarium, Metodologi & Daftar Sumber, Disclaimer | — |

### B7. Dataset wajib (Fase 2)

| Dataset | Periode | Sumber utama |
|---|---|---|
| Pertumbuhan PDB riil (negara fokus) | Tahunan + kuartal terbaru | IMF WEO, BPS, BEA, NBS, MoSPI (perhatikan tahun fiskal India) |
| Inflasi (CPI, inti) | Bulanan/tahunan | BPS, BLS, Eurostat, NBS |
| Suku bunga kebijakan | Per keputusan | BI, Fed, ECB, BOJ, PBoC, RBI |
| Yield obligasi 10 tahun (UST, SBN, Bund, JGB, Gilt) | Harian/bulanan | FRED, DJPPR/PHEI, Investing |
| Kurs (USD/IDR, DXY, USD/CNY, USD/JPY, EUR/USD) | Akhir tahun + rata-rata | BI JISDOR, FRED |
| Return tahunan IHSG, S&P 500, MSCI EM (sebutkan *price*/*total*) | Tahunan | BEI, S&P, MSCI |
| Harga emas, Brent, batu bara (Newcastle), nikel (LME), CPO | Akhir tahun + puncak | WGC/LBMA, EIA, World Bank Pink Sheet |
| Bitcoin & kapitalisasi kripto/stablecoin | Akhir tahun + puncak | CoinMarketCap/CoinGecko, DefiLlama |
| VIX | Harian (puncak per episode) | CBOE/FRED VIXCLS |
| Indeks GPR | Bulanan/harian | matteoiacoviello.com/gpr.htm |
| Porsi mata uang di cadangan devisa dunia | Kuartalan | IMF COFER |
| Pembelian emas bank sentral | Kuartalan | WGC Gold Demand Trends |
| Defisit fiskal & utang/PDB | Tahunan | IMF Fiscal Monitor, Kemenkeu |
| Transaksi berjalan (% PDB) | Kuartalan | BI, IMF |
| Neraca perdagangan Indonesia per komoditas (ekspor & impor) | Tahunan | BPS |
| Kepemilikan asing SBN & arus asing saham | Bulanan | DJPPR, BEI/OJK |
| Investasi AI swasta (AS, China) & penjualan chip | Tahunan | Stanford HAI AI Index, SIA/WSTS |
| PMI manufaktur China | Bulanan | NBS |

### B8. Template

#### B8.1 Template Catatan Topik (`catatan/.../<topik>.md`)

```markdown
# [Topik]
> Data per: [tanggal] · Keyakinan: tinggi/sedang/rendah · Terkait: [tautan]

## Ringkasan (5 kalimat)
## Data kunci (tabel: indikator | nilai | tanggal | sumber)
## Sejarah singkat (tabel kronologi)
## Kondisi terkini
## Korelasi dengan topik lain (dengan mekanismenya)
## Dampak ke Indonesia (saluran: perdagangan, kurs, fiskal, arus modal, inflasi)
## Skenario 5 tahun (saling eksklusif, total 100%, dengan pemicu)
## Indikator yang perlu dipantau
## Pertanyaan terbuka / data yang tidak ditemukan
## Sumber
```

#### B8.2 Template Bab (`bab/NN-*.md`)

```markdown
# Bab N: [Judul]
> Data dalam bab ini per [tanggal cutoff].

[Pembuka 1–2 paragraf: mengapa bab ini penting bagi investor Indonesia]

## [Subbagian]
[Penjelasan + grafik/tabel bersumber]

**Apa yang dilihat:** ...
**Pola yang harus diingat:** ...
**Apa artinya untuk investor:** ... (kerangka, bukan saran beli/jual)
> **Quick Rule:** [satu kalimat]

### Insight kunci
[Satu kotak berisi insight paling penting, dengan data pendukung]

### Sumber bab
```

#### B8.3 Template Skenario

```markdown
| Skenario | Probabilitas (subjektif) | Pemicu yang bisa diamati | Indikator konfirmasi | IHSG | USD/IDR | SBN 10th | Emas (IDR) | Komoditas ekspor | Brent |
|---|---|---|---|---|---|---|---|---|---|
| A ... | xx% | ... | ... | rentang | rentang | ... | ... | ... | ... |
| (total = 100%) |

Risiko ekor (terpisah, tidak masuk total):
| Risiko | Probabilitas 5 tahun | Dampak | Sinyal dini |
```

#### B8.4 Entri `VERIFIKASI.md`

```markdown
| # | Klaim | File:baris | Status | Nilai benar | Sumber | Catatan |
```

### B9. Dashboard indikator minimum (Bab 12)

Global: DXY, yield UST 10 tahun (dan *term premium*), Brent, VIX, GPR (sebagai konfirmasi, bukan prediktor), PMI China, keputusan Fed.
Indonesia: USD/IDR, **transaksi berjalan (% PDB)**, **defisit APBN vs batas 3%**, cadangan devisa, BI-Rate & selisihnya dengan Fed, inflasi, yield SBN 10 tahun & selisihnya dengan UST, kepemilikan asing SBN, arus asing di saham, IHSG, status MSCI/FTSE, peringkat utang dan CDS.
Untuk setiap indikator: nilai terkini (dengan tanggal), ambang perhatian, arti, frekuensi rilis, dan sumber.

### B10. Checklist QA final (Fase 9)

**Data & sumber**
- [ ] Tidak ada angka tanpa sumber dan tanggal di naskah final
- [ ] Semua angka di grafik berasal dari `data/*.csv` (tidak diketik manual)
- [ ] `VERIFIKASI.md` tidak menyisakan status ❌
- [ ] Tanda (+/−), satuan (juta/miliar/triliun), dan tahun sudah dicek pada semua tabel
- [ ] Definisi return (*price*/*total*) dan tahun fiskal disebutkan
- [ ] Tidak ada kolom tabel yang berisi data milik kolom lain (copy-paste error)

**Kemutakhiran**
- [ ] Semua peristiwa di `TIMELINE.md` yang berdampak besar dibahas di buku
- [ ] Tanggal cutoff tertulis di sampul, pendahuluan, dan setiap bab

**Logika & konsep**
- [ ] Skenario saling eksklusif, total 100%, punya pemicu yang bisa diamati
- [ ] Risiko ekor dipisah dari skenario utama
- [ ] Ada skenario shock energi/Timur Tengah dan skenario risiko domestik Indonesia
- [ ] Dampak komoditas pada Indonesia dibedakan antara ekspor dan impor
- [ ] Atribusi teori benar (Dalio, Soros, Maastricht, All Weather)
- [ ] GPR tidak disebut sebagai prediktor; keterbatasan VIX dijelaskan
- [ ] Uji balik model dilaporkan beserta kegagalannya

**Penyajian**
- [ ] Glosarium mencakup semua istilah teknis
- [ ] Disclaimer "bukan saran investasi" ada di awal dan akhir
- [ ] PDF terbaca: tabel tidak terpotong, grafik muncul, daftar isi benar
- [ ] Bahasa: kalimat pendek, tidak ada jargon tanpa penjelasan

### B11. Kesalahan yang harus dihindari (pelajaran dari Vol. 1)

| Kesalahan di Vol. 1 | Pencegahan |
|---|---|
| Klaim "kondisi terkini" tetapi melewatkan perang besar yang sedang terjadi | Fase 1 wajib sebelum analisis |
| IHSG 2024 ditulis +2,7% (faktanya −2,65%) | Verifikasi tanda; sumber primer BEI/OJK |
| Investasi AI China $80 miliar (faktanya $9,3 miliar, Stanford HAI) | Cek angka ke sumber yang dikutip sendiri |
| Kerusakan "$1–2 T" (faktanya $1–2 miliar) | Cek satuan miliar vs triliun |
| Harga BTC akhir tahun tertukar tahun | Data dari CSV bersumber, bukan ingatan |
| Kolom emas/Brent berisi angka PDB | Grafik dan tabel dihasilkan otomatis dari CSV |
| "Komoditas naik → Indonesia naik" | Analisis neraca komoditas ekspor vs impor |
| Bear case 35–40% berisi 4 bencana sekaligus | Skenario eksklusif + risiko ekor terpisah |
| Label "All Weather" untuk portofolio lain | Aturan atribusi B3.8 |
| GPR dipakai sebagai prediktor 3–6 bulan | Aturan B3.9 |
| Tidak ada indikator domestik (transaksi berjalan, APBN, tata kelola) | Dashboard minimum B9 |
| Statistik tanpa sumber yang bisa dicek (mis. "87%/95% Pew") | Aturan B3.4: jika tidak ditemukan, hapus |

### B12. Rutin pembaruan (untuk volume atau edisi berikutnya)

1. Ubah `tanggal_cutoff_data` di B2.
2. Jalankan Fase 1 untuk periode sejak cutoff lama.
3. Perbarui semua CSV di `data/`; tandai nilai yang berubah.
4. Jalankan ulang Fase 4 (verifikasi) untuk angka yang berubah.
5. **Evaluasi skenario lama:** skenario mana yang terjadi, mana yang meleset, dan mengapa. Tulis sebagai bagian "Rapor Ramalan Edisi Sebelumnya", karena kejujuran ini membangun kredibilitas.
6. Perbarui probabilitas, dashboard, lalu rakit ulang buku.

### B13. Cara bekerja sebagai agent

- **Rencanakan dulu, baru kerjakan.** Ikuti urutan fase. Jangan menulis bab sebelum data dan verifikasi selesai.
- **Gunakan pencarian web secara aktif** untuk semua data terkini. Pengetahuan bawaan model punya batas tanggal.
- **Paralelkan riset dengan subagent** jika tersedia. Pisahkan peran penulis dan verifikator.
- **Laporkan ketidakpastian dengan jujur**: data yang tidak ditemukan, sumber yang bertentangan, keyakinan rendah.
- **Commit kecil dan sering.** Pesan commit menjelaskan isi (misalnya "Fase 3: catatan topik mata uang (USD, CNY, IDR)").
- **Berhenti di titik persetujuan:** setelah PLAN.md (Fase 0), 10 peristiwa (Fase 1), tabel skenario dan dashboard (Fase 5), serta sebelum perakitan final.
- **Di akhir setiap sesi**, tulis ringkasan di `PROGRESS.md`: apa yang selesai, apa berikutnya, dan masalah yang ditemukan.
