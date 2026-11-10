# Rencana Riset: Peta Kompetitor AZKO & Informa

> Status: **DISETUJUI & DIJALANKAN**. Hasil ada di [`report.md`](report.md).
> Tanggal draf: 10 November 2026

---

## 0. Tujuan & Pertanyaan Kunci

**Tujuan:** Mengidentifikasi brand/retailer (offline, online, lokal, asing, maupun calon pendatang) yang
bisa menggerus pangsa pasar **AZKO** (eks-ACE Hardware Indonesia) dan **Informa**. Analisis dilakukan
**per kategori produk**, bukan hanya per label industri seperti "home improvement" atau "furniture".

**Pertanyaan kunci:**
1. Apa saja yang dijual AZKO & Informa, dan kategori mana yang paling berat (jumlah SKU, kontribusi
   penjualan, porsi luas toko)?
2. Di kategori mana mereka **kuat** dan di mana **lemah**, dan apa buktinya (harga, kelengkapan
   barang, private label, pengalaman belanja, jangkauan toko, layanan)?
3. Siapa yang bermain di tiap kategori, dari kompetitor langsung sampai pengganti tidak langsung?
4. Siapa yang **sedang** menggerus pasar mereka, dan siapa yang **berpotensi** masuk (ekspansi pemain
   yang sudah ada, pemain asing baru, pemain online yang mulai buka toko fisik)?
5. Dari sisi segmen harga, wilayah (kota tier 1/2/3), dan kanal, di mana posisi AZKO/Informa paling
   rentan?

---

## 1. Kerangka Berpikir (Top-down → Bottom-up)

```
[Fase 1] Bedah AZKO & Informa ── jualan apa? mana yang paling besar?
        │
        ▼
[Fase 2] Peta kategori + posisi (kuat/lemah) tiap kategori
        │
        ▼
[Fase 3] Cari pemain per kategori, dalam 5 lapis kompetisi
        │
        ▼
[Fase 4] Profil mendalam tiap kompetitor terpilih (field terstruktur)
        │
        ▼
[Fase 5] Analisis silang: overlap matrix, benchmark harga, positioning map,
         white space wilayah, skor ancaman, skenario
        │
        ▼
[Fase 6] Laporan + rekomendasi
```

Alur ini dijalankan dengan workflow di repo ini: `/research` (outline: items + fields) →
`/research-deep` (riset paralel per item) → `/research-report`.

---

## 2. Fase 1 – Bedah AZKO & Informa ("dia jualan apa saja?")

### 2.1 Yang akan dicatat
| Dimensi | Detail |
|---|---|
| Struktur kategori | Kategori → subkategori (mis. Tools & Hardware → Power Tools, Hand Tools, Fastener; Housewares → Kitchen, Storage; dst.) |
| Kedalaman assortment | Jumlah SKU per kategori/subkategori (proksi seberapa banyak barang yang mereka taruh di tiap area) |
| Rentang harga | Harga min, median, dan max per subkategori (price band) |
| Private label vs brand pihak ketiga | Mis. Krisbow, Kris, Selma, label milik Informa, vs Bosch, Makita, Philips, Lock&Lock, dll. |
| Kontribusi penjualan | Dari laporan tahunan/public expose ACES (PT Aspirasi Hidup Indonesia Tbk): penjualan per kategori/segmen, SSSG, margin |
| Jaringan & format | Jumlah toko, kota, format (besar/kecil/express), toko gabungan AZKO+Informa |
| Kanal | Toko fisik, ruparupa.com, official store marketplace, TikTok Shop, B2B/korporat |
| Program pelanggan | Membership/rewards, garansi, layanan rakit/pasang, cicilan |
| Segmen target | Kelas ekonomi, demografi, B2C vs B2B |

### 2.2 Sumber
- Situs resmi & katalog online (AZKO, Informa, ruparupa.com), dengan crawl/pengamatan struktur kategori dan hitungan SKU
- Laporan tahunan, public expose, dan keterbukaan informasi ACES di IDX
- Laporan analis sekuritas (Mirae, Mandiri Sekuritas, BRI Danareksa, dll.)
- Berita: Kontan, Bisnis Indonesia, CNBC Indonesia, Katadata, DealStreetAsia
- Store locator + Google Maps (jumlah & sebaran toko)

### 2.3 Output Fase 1
- **Peta kategori AZKO & Informa** beserta bobotnya (SKU share, revenue share jika tersedia, price band)
- Daftar **kategori prioritas**, yaitu kategori dengan bobot terbesar dan kategori margin tinggi seperti private label

> Catatan: rincian penjualan per kategori untuk Informa dan AZKO bisa saja tidak dipublikasikan
> terpisah. Kalau begitu, saya akan memakai proksi (jumlah SKU, porsi luas toko, intensitas promo)
> dan menandainya dengan jelas sebagai estimasi.

---

## 3. Fase 2 – Posisi per Kategori (kuat / lemah)

Untuk **setiap kategori prioritas**, saya akan menilai:

| Indikator | Cara mengukur |
|---|---|
| Kelengkapan barang | SKU AZKO/Informa vs pesaing utama di kategori yang sama |
| Daya saing harga | Basket benchmark ±30–50 SKU identik/setara, dibandingkan dengan pesaing offline & marketplace |
| Kekuatan private label | Porsi private label, rating, persepsi kualitas |
| Pengalaman & layanan | Review Google Maps, keluhan di media sosial, layanan rakit/antar/garansi |
| Jangkauan | Jumlah toko per provinsi/kota vs pesaing |
| Persepsi konsumen | Google Trends, survei publik (Jakpat, Populix, Katadata Insight), sentimen TikTok/IG/X |

**Hasil:** matriks **Kategori × (Kuat / Netral / Lemah)** dengan bukti untuk tiap penilaian. Ini
menjawab pertanyaan "kuat di mana, lemah di mana, dan siapa yang bermain di sana".

---

## 4. Fase 3 – Pemetaan Kompetitor dalam 5 Lapis

Kompetitor dicari **per kategori**, bukan hanya per industri. Setiap kategori prioritas dipetakan ke
lima lapis berikut:

| Lapis | Definisi | Contoh kandidat awal (akan diverifikasi) |
|---|---|---|
| **A. Format langsung** | Retailer dengan format mirip (big box home/hardware/furnishing) | Mitra10, Depo Bangunan, IKEA (dioperasikan Hero), MR.D.I.Y., Courts, Transmart/Hypermart home section |
| **B. Spesialis kategori** | Fokus di satu kategori yang dipegang AZKO/Informa | Tools: toko/dealer Bosch, Makita, Ingco, Tekiro · Kasur: King Koil, Airland, Serta, Florence, Comforta · Furniture: Olympic, Vivere, Ligna, Chitose, Dekoruma, Ashley · Elektronik: Electronic City, Hartono, Erafone · Kitchen: Lock&Lock, Modena · Cat: toko cat/dealer Nippon, Avian · Lifestyle/murah: Miniso, Daiso, KKV, Yoyoso, Mumuso, Muji |
| **C. Online & D2C** | Marketplace, social commerce, brand yang menjual langsung | Shopee, Tokopedia/TikTok Shop, Lazada, Blibli; brand D2C furniture/home lokal; toko impor China di marketplace |
| **D. Substitusi/tidak langsung** | Cara lain konsumen memenuhi kebutuhan yang sama | Toko bangunan tradisional, mebel Jepara/custom, kontraktor & jasa interior, kitchen set custom, paket furnish developer properti, barang bekas (OLX/FB Marketplace) |
| **E. Calon pendatang/ekspansi** | Pemain yang belum besar di Indonesia atau sedang ekspansi | Ekspansi MR.D.I.Y./KKV/Daiso, pemain regional (Nitori, JYSK, HomePro, Index Living Mall, Bunnings, Kmart/Anko), pemain online yang membuka toko fisik |

Untuk B2B (Kawan Lama/Krisbow sebagai supplier korporat), saya juga mempertimbangkan lapis tambahan:
platform procurement B2B (mis. Monotaro Indonesia, Mbizmarket, Bhinneka) — **opsional, tergantung
cakupan yang Anda pilih**.

**Hasil Fase 3:** longlist kompetitor (perkiraan 40–60 nama), lalu disaring menjadi **shortlist 20–30**
untuk profil mendalam, berdasarkan tingkat overlap kategori × skala × momentum pertumbuhan.

---

## 5. Fase 4 – Profil Mendalam per Kompetitor (field terstruktur)

Setiap kompetitor dalam shortlist akan diriset dengan field yang sama (akan menjadi `fields.yaml`):

**Info dasar:** nama, pemilik/grup, status (Tbk/privat/asing), tahun masuk Indonesia
**Skala:** jumlah toko, sebaran kota/provinsi, pertumbuhan toko 2023–2026, luas toko rata-rata
**Finansial** (jika tersedia): pendapatan, pertumbuhan, margin, SSSG
**Assortment:** kategori yang overlap dengan AZKO dan dengan Informa, kedalaman di tiap kategori
**Harga:** positioning (low/mid/premium) dan hasil benchmark basket
**Segmen & kanal:** target konsumen, kanal offline/online, B2B
**Diferensiasi:** private label, layanan, pengalaman toko, membership
**Langkah terbaru:** ekspansi, toko baru, kemitraan, pendanaan, M&A (2024–2026)
**Penilaian ancaman:** di kategori mana, di wilayah mana, dan seberapa besar (skala 1–5) beserta alasannya
**Sumber** dan tanda **[uncertain]** untuk data yang belum terverifikasi

---

## 6. Fase 5 – Analisis Silang

1. **Overlap matrix:** Kategori × Kompetitor (tingkat overlap & kekuatan)
2. **Positioning map:** (a) harga vs keluasan assortment; (b) harga vs pengalaman/desain
3. **Benchmark harga:** indeks harga basket AZKO/Informa = 100 vs pesaing
4. **Peta geografis/white space:** sebaran toko per provinsi/kota tier untuk melihat di mana pesaing lebih
   dulu hadir dan di mana AZKO/Informa belum ada
5. **Skor ancaman:** gabungan dari overlap kategori, keunggulan harga, momentum ekspansi, dan kekuatan
   finansial. Hasilnya peringkat siapa yang paling berpotensi menggerus, di kategori apa
6. **Skenario:** misalnya "MR.D.I.Y. masuk kota tier 2–3 → kategori housewares & hand tools AZKO
   tergerus"; "TikTok Shop + brand China → kategori small appliances/organizer"; "IKEA format kecil →
   furniture Informa"
7. **Kategori yang "aman" vs "rentan"**, plus peluang/opsi respons

---

## 7. Fase 6 – Struktur Laporan Akhir

1. Ringkasan eksekutif (top 10 ancaman + kategori paling rentan)
2. Profil AZKO & Informa: portofolio kategori dan bobotnya
3. Posisi per kategori (kuat/lemah) dengan bukti
4. Peta kompetitor 5 lapis per kategori
5. Profil kompetitor (tabel + ringkasan)
6. Analisis silang: matriks, positioning map, harga, geografis
7. Calon pendatang & skenario
8. Implikasi/rekomendasi
9. Lampiran: daftar sumber, metodologi, data mentah (JSON/Excel)

Format bisa berupa **Markdown/Word report**, **Excel** (matriks & data), dan/atau **PowerPoint**.

---

## 8. Sumber Data yang Akan Digunakan

| Jenis | Contoh |
|---|---|
| Data resmi perusahaan | Laporan tahunan, public expose, IDX disclosure (ACES, CSAP/Mitra10, HERO/IKEA, MR.D.I.Y. Group di Bursa Malaysia) |
| Riset sekuritas & industri | Laporan analis, rilis asosiasi (APRINDO, HIPPINDO), Statista/Euromonitor (cuplikan publik) |
| Berita & media bisnis | Kontan, Bisnis, CNBC Indonesia, Katadata, DealStreetAsia, Tech in Asia |
| Data toko/katalog | Situs resmi, store locator, Google Maps, katalog online & marketplace |
| Data konsumen | Review Google Maps, sentimen media sosial, Google Trends, survei publik |
| Sinyal ekspansi | Lowongan kerja (lokasi toko baru), berita pembukaan toko, pengumuman mal |

---

## 9. Keterbatasan

- Tidak ada akses ke data internal maupun database berbayar (Nielsen, Euromonitor penuh). Pangsa pasar
  akan berupa **estimasi** dari data publik.
- Hitungan SKU dari situs/marketplace bisa terhambat anti-bot. Kalau terjadi, saya pakai sampling.
- Benchmark harga adalah potret pada saat riset, bukan data historis.
- Konektor Similarweb (data traffic web) saat ini belum terotorisasi. Kalau ingin data traffic
  ruparupa.com vs pesaing, konektor itu perlu diotorisasi di pengaturan konektor claude.ai.

---

## 10. Keputusan yang Dibutuhkan dari Anda

1. **Cakupan:** AZKO & Informa sama dalamnya, atau salah satu jadi fokus utama?
2. **B2B:** Apakah segmen korporat/proyek (Krisbow, Informa Business) ikut dianalisis?
3. **Wilayah:** Nasional, atau fokus ke kota/pulau tertentu?
4. **Rentang waktu berita/data:** usulan 2023–2026.
5. **Benchmark harga basket:** dilakukan atau tidak (paling memakan waktu, tapi paling tajam)?
6. **Jumlah kompetitor yang diprofil mendalam:** usulan 20–30.
7. **Format output:** Markdown/Word, Excel, PowerPoint, atau kombinasi?

---

## 11. Keputusan Pengguna (final)
1. AZKO & Informa dianalisis **sama dalamnya**.
2. B2B (Krisbow, Informa Business) **sekilas saja**.
3. Wilayah: **nasional**.
4. Rentang waktu: **2023–2026**.
5. Benchmark harga: **sebagian saja, kisaran**.
6. Profil mendalam: **20–30 kompetitor** (terealisasi 26).
7. Output: **Markdown lengkap dulu**, konversi format menyusul.
8. Tambahan: **analisis format & konsep toko** (misalnya alasan flagship MR.D.I.Y.).
