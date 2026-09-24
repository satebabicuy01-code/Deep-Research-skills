# Desain Gerai & Pertumbuhan Pendapatan Starbucks China

**Untuk:** Director of Design · Corporate Strategic Direction
**Tanggal:** 24 September 2026
**Cakupan data:** FY2016 s.d. Q2 FY2026 (periode terakhir Starbucks China dilaporkan sebagai company-operated), ditambah pembaruan JV Starbucks–Boyu s.d. 15 September 2026.
**Lampiran:** katalog 10 format desain di [report.md](report.md) · data & skrip di [data/](data/), [analysis.py](analysis.py)

---

## Jawaban singkat

Belum ada data publik yang menghubungkan desain shopfront gerai tertentu dengan penjualannya. Starbucks tidak melaporkan kinerja per format maupun per gerai. Dari bukti yang tersedia, ada tiga kesimpulan:

1. **Di tingkat gerai dan pelanggan, korelasinya positif.** Desain visual yang terasa mewah menaikkan kesediaan konsumen China membayar lebih mahal (Li dkk., 2022). Flagship Roastery Shanghai mencetak rekor penjualan Starbucks, dan kuartal ketika 38 gerai dihias bertema Harry Potter (Q1 FY2026) menghasilkan comp +7%, satu-satunya kuartal dengan ticket positif dalam rentang Q4 FY2023–Q2 FY2026.
2. **Di tingkat jaringan (FY2019→FY2025), pendapatan tumbuh karena jumlah gerai bertambah, bukan karena gerai makin produktif.** Jumlah gerai naik **94%**, pendapatan dalam RMB hanya naik **15,5%** (CAGR 2,4%), dan pendapatan per gerai turun **43%**. Korelasi jumlah gerai dengan pendapatan per gerai **r = −0,91**. Selama periode itu portofolio bergeser ke gerai lebih kecil, pickup, dan kota tier bawah, sementara perang harga menekan ticket.
3. **Jadi pertanyaannya adalah desain mana yang cocok untuk peran apa, bukan apakah desain berpengaruh.** Campuran format menentukan pertumbuhan pendapatan, dan desain signature menentukan kemampuan menjaga harga premium. Strategi JV 2026, 千店千面 ("seribu gerai, seribu wajah", format dari 10 m² hingga 800+ gerai Reserve & tematik, tanpa potongan harga), sudah mengarah ke sana. Yang belum ada adalah sistem pengukuran yang menghubungkan atribut desain dengan kinerja.

## Angka kunci

| Indikator | Nilai | Sumber |
|---|---|---|
| Pendapatan Starbucks China FY2019 → FY2025 | US$2,87 miliar → US$3,16 miliar (+10,1%; **+15,5% dalam RMB**) | 10-K Starbucks |
| Gerai company-operated FY2019 → FY2025 | 4.123 → 8.009 (**+94%**) | 10-K Starbucks |
| Pendapatan per gerai rata-rata | RMB 5,17 juta → **RMB 2,92 juta (−43%)** | Kalkulasi (10-K + kurs FRED) |
| Comp sales FY2025 | −1% (transaksi +4%, ticket −5%) | Press release Q4 FY2025 |
| Comp Q1 FY2026 / Q2 FY2026 | +7% (ticket +2%) / +0,5% (ticket −1,6%) | Press release Q1–Q2 FY2026 |
| Pangsa pasar kopi Starbucks di China | 34% (2019) → 14% (2024) | Euromonitor, via Reuters & Fortune |
| Luckin 2025 | 31.048 gerai (99,1% self-operated berupa pickup 20–60 m²); pendapatan RMB 49,3 miliar (**2,16×** Starbucks China) | 20-F Luckin FY2025 |
| JV Starbucks–Boyu | Ditutup 2 Apr 2026; Boyu 60%, Starbucks 40% + lisensi merek; EV ~US$4 miliar; aspirasi 20.000 gerai | 8-K Starbucks |
| Gerai per 15 Sep 2026 | 8.238 (+227 neto FY2026; 69 county baru) | Media China (QQ News) |

---

## 1. Konteks: dari "menyewakan sofa" ke "seribu gerai, seribu wajah"

| Periode | Peristiwa desain/format | Sinyal kinerja |
|---|---|---|
| 1999–2016 | Model third place: gerai besar, banyak kursi. Quartz (2013) menyebut Starbucks China "tidak menjual kopi, tetapi menyewakan sofa"; menurut laporan CCTV (Okt 2013), latte di Beijing ~⅓ lebih mahal dari Chicago | FY2016: Starbucks menyebut gerai baru di China mencetak "Record AUV's, ROI and Profitability" |
| Des 2017 | Shanghai Reserve Roastery (~30.000 sq ft) | Penjualan harian ~2× penjualan **mingguan** rata-rata gerai AS; ticket hari pertama ~US$29 (CNBC) |
| FY2018 | Akuisisi JV East China (1.477 gerai jadi company-operated) | Comp China Q3 FY2018 −2% walau Roastery baru buka |
| Jul 2019 | Starbucks Now: format express/pickup pertama (Beijing), pickup portal di dinding, fungsi dispatch delivery | Respons terhadap model pickup Luckin |
| FY2020–FY2022 | COVID-19 | Comp −17%, +17%, −24% |
| FY2023–FY2025 | Ekspansi ke county: 166 county baru di FY2024; perang harga | Pangsa pasar turun ke 14%; ticket negatif berturut-turut |
| s.d. Agu 2025 | 5 gerai tematik warisan budaya takbenda (ICH), terbaru Hefang Street, Hangzhou (29 Agu 2025) | Tidak ada data penjualan publik |
| Q1 FY2026 | 38 gerai bertema Harry Potter | Comp +7%, transaksi +5%, ticket +2% |
| Apr 2026 | JV ditutup; strategi 千店千面: gerai 10 m² di area wisata, convenience kantor modular, kereta kopi, gerai rumah sakit, 800+ Reserve & tematik; "tidak menurunkan harga" | Belum ada data per format |
| Sep 2026 | Flagship generasi baru "Starbucks Reserve 星意坊" di Beijing SKP | 8.238 gerai |

## 2. Metode dan batasannya

- **Data keuangan resmi.** Pendapatan China diambil dari catatan geografis 10-K ("Net revenues: China"), jumlah gerai dari tabel store data 10-K, dan comp/transaksi/ticket dari press release kuartalan. Semua pendapatan dikonversi ke RMB dengan rata-rata kurs harian FRED (DEXCHUS) per tahun fiskal Okt–Sep, supaya depresiasi RMB tidak terbaca sebagai penurunan kinerja.
- **Seri produktivitas** dimulai FY2019. FY2018 dikecualikan karena konsolidasi East China di tengah tahun membuatnya tidak sebanding.
- **Korelasi** bersifat deskriptif. Seri tahunan hanya n = 7 dan kuartalan n = 10, dan hasilnya dipengaruhi faktor lain: COVID, perang harga, FY2021 yang berisi 53 minggu, serta perubahan kanal (delivery).
- **Desain shopfront secara spesifik** (lebar muka gerai, rasio kaca, signage) tidak punya dataset publik. Karena itu dipakai proksi: pergeseran campuran format, gerai tematik, studi kasus flagship, dan literatur servicescape. Bagian 6 mengusulkan cara mengukurnya secara internal.

## 3. Temuan

### Temuan 1: Pendapatan tumbuh dari jumlah gerai, sementara produktivitas per gerai turun

| FY | Pendapatan (US$ jt) | Pendapatan (RMB jt) | Gerai akhir | Pendapatan/gerai (RMB jt) | Gerai baru neto | Comp |
|---|---|---|---|---|---|---|
| 2019 | 2.872 | 19.746 | 4.123 | 5,17 | +17,1% | +4% |
| 2020 | 2.583 | 18.094 | 4.704 | 4,10 | +14,1% | −17% |
| 2021* | 3.675 | 23.913 | 5.358 | 4,75 | +13,9% | +17% |
| 2022 | 3.008 | 19.714 | 6.019 | 3,47 | +12,3% | −24% |
| 2023 | 3.082 | 21.735 | 6.804 | 3,39 | +13,0% | +2% |
| 2024 | 3.008 | 21.672 | 7.594 | 3,01 | +11,6% | −8% |
| 2025 | 3.161 | 22.797 | 8.009 | 2,92 | +5,5% | −1% |

\*FY2021 berisi 53 minggu. Pendapatan per gerai = pendapatan ÷ rata-rata gerai awal & akhir tahun.

**Dekomposisi FY2019→FY2025 (log):** efek jumlah gerai **+0,71**, efek produktivitas **−0,57**, total **+0,14**. Kira-kira empat perlima dorongan dari penambahan gerai habis oleh turunnya produktivitas.

Cara membacanya:
- **r = −0,91** antara jumlah gerai dan pendapatan per gerai. Arahnya konsisten, termasuk bila tahun COVID dikeluarkan (n = 4, terlalu kecil untuk dijadikan kesimpulan).
- Laju pembukaan gerai tidak berkorelasi dengan comp tahunan (**r = 0,12**). Jadi data publik tidak menunjukkan kanibalisasi sebagai penyebab utama. Penurunan produktivitas lebih konsisten dengan **pergeseran campuran format** (gerai lebih kecil, pickup, tier bawah dengan sewa dan harga lebih rendah) dan **erosi ticket**.
- Sejak FY2024 produktivitas **mendatar** di sekitar US$380–430 ribu per gerai per tahun (disetahunkan dari data kuartalan). Penurunannya tidak berlanjut. Level ini menjadi titik awal model JV.

**Implikasi desain:** portofolio yang sehat bisa saja punya pendapatan per gerai lebih rendah asalkan capex dan sewa per format juga lebih rendah. Masalahnya, data publik tidak memungkinkan penilaian ROI per format. Tanpa data itu, pertumbuhan jumlah gerai bisa menutupi format yang merusak nilai.

### Temuan 2: Comp ditentukan traffic, sementara ticket terus tergerus

| Kuartal | Comp | Transaksi | Ticket | Gerai | Pendapatan (US$ jt) |
|---|---|---|---|---|---|
| Q1 FY24 | +10% | +21% | −9% | 6.975 | 735,0 |
| Q2 FY24 | −11% | −4% | −8% | 7.093 | 705,8 |
| Q3 FY24 | −14% | −7% | −7% | 7.306 | 733,8 |
| Q4 FY24 | −14% | −6% | −8% | 7.596 | 783,7 |
| Q1 FY25 | −6% | −2% | −4% | 7.685 | 743,6 |
| Q2 FY25 | −0,1% | +4,4% | −4,2% | 7.758 | 739,7 |
| Q3 FY25 | +2% | +6% | −4% | 7.828 | 790,0 |
| Q4 FY25 | +2% | +9% | −7% | 8.011 | 831,6 |
| Q1 FY26 | **+7%** | +5% | **+2%** | 8.011 | 823,4 |
| Q2 FY26 | +0,5% | +2,1% | −1,6% | 7.991 | 799,8 |

- Korelasi comp dengan transaksi **r = 0,91** (kuartalan) dan **0,95** (tahunan). Korelasi comp dengan ticket hanya **0,40**.
- Ticket negatif di **9 dari 10 kuartal**. Pemulihan FY2025 datang dari traffic yang dibeli dengan harga lebih rendah (transaksi +9%, ticket −7% di Q4 FY2025).
- Satu-satunya kuartal dengan ticket naik (Q1 FY2026) bersamaan dengan kampanye pengalaman di gerai: 38 gerai bertema IP, inovasi produk, dan pertumbuhan delivery menurut CFO. Ini korelasi waktu, bukan bukti kausal, tetapi cocok dengan dugaan bahwa pengalaman dan desain adalah tuas untuk ticket.

**Implikasi desain:** shopfront punya dua tugas yang bisa diukur. Pertama, **mendatangkan traffic** lewat visibilitas, kemudahan pickup, dan alasan untuk mampir. Kedua, **menaikkan ticket** di format premium lewat bar seduh yang terlihat dari luar, merchandise, dan suasana. Selama tiga tahun terakhir, tugas kedua belum berhasil di tingkat jaringan.

### Temuan 3: Di tingkat gerai dan pelanggan, desain berkorelasi positif dengan harga premium dan kunjungan

- **Riset akademik di China.** Li, Laroche, Richard & Cui (2022, *Journal of Retailing and Consumer Services*) menemukan bahwa kesan mewah dari desain visual kedai kopi di China menaikkan persepsi kualitas kopi dan kecocokan dengan citra diri (self-congruity), lalu menaikkan **kesediaan membayar harga premium**. Ge dkk. (2021, *Sustainability*) meneliti 385 pelanggan Starbucks Reserve di Shanghai dan menemukan rantai kualitas layanan → nilai yang dirasakan → kepuasan → niat kembali dan merekomendasikan. Venkatraman & Nelson (2008, *JIBS*) menunjukkan konsumen muda urban China memakai Starbucks sebagai ruang untuk membangun makna dan identitas.
- **Riset shopfront umum** (bukan khusus kopi atau China): display jendela dan muka toko memengaruhi keputusan masuk toko (Sen, Block & Chandran, 2002; Oh & Petrie, 2012). Ini mendukung KPI *capture rate* di Bagian 6.
- **Flagship.** Roastery Shanghai memecahkan rekor penjualan harian perusahaan. Namun dua kuartal kemudian comp China negatif (−2%). Efeknya kuat di satu gerai tetapi tidak terlihat mengangkat seluruh jaringan.
- **Program induk di AS.** "Coffeehouse uplift" (kursi lebih nyaman, warna hangat, lebih banyak stopkontak) sudah melewati 1.000 remodel di Amerika Utara pada FY2026 dengan target 1.500 per akhir September. Manajemen melaporkan "transaction lift across access points, dayparts, formats and customer segments", dan comp Amerika Utara Q3 FY2026 +8,1% (transaksi +4,5%, ticket +3,5%). Angka uplift per gerai belum dipublikasikan, dan program ini tidak berlaku langsung untuk China yang kini dijalankan JV.

### Temuan 4: Kompetitor dengan desain berbasis efisiensi memenangkan volume, lalu ikut membangun gerai premium

| Tahun | Pendapatan Luckin (RMB jt) | Gerai Luckin | Pendapatan/gerai Luckin (RMB jt) | Margin level gerai (self-op) |
|---|---|---|---|---|
| 2021 | 7.965 | 6.024 | 1,47 | 20,2% |
| 2022 | 13.293 | 8.214 | 1,87 | 26,4% |
| 2023 | 24.903 | 16.248 | 2,04 | 22,2% |
| 2024 | 34.475 | 22.340 | 1,79 | 19,0% |
| 2025 | 49.288 | 31.048 | 1,85 | 17,8% |

- Pendapatan per gerai Starbucks China (RMB 2,92 juta di FY2025) masih **1,58×** Luckin. Angka Luckin sebenarnya lebih rendah dari penjualan riil, karena untuk partnership store yang dicatat hanya penjualan material ke mitra.
- Luckin memakai gerai 20–60 m². Starbucks tidak mengungkap luas rata-rata gerainya. **Sebagai ilustrasi dengan asumsi** luas rata-rata Starbucks 120/180/250 m² dan Luckin 40 m², pendapatan per m² Starbucks sekitar RMB 24/16/12 ribu, sedangkan Luckin sekitar RMB 46 ribu. Angka ini perlu divalidasi dengan data luas internal sebelum dipakai.
- Luckin membuka gerai high-end pertamanya pada Februari 2026 (dilaporkan ~420 m²). Kedua pemain kini menuju **portofolio format**: Luckin menambah gerai pengalaman, Starbucks menambah format mikro.

### Temuan 5: Arah JV 2026 menjadikan desain sistem portofolio, tetapi kendali Starbucks atas desain berkurang

- Pilar 千店千面 meliputi kopi spesialis sebagai dasar premium, inovasi produk, **ekspansi berbasis skenario (format fleksibel)**, "satu gerai, satu komunitas", dan AI untuk pemasaran. Harga tidak diturunkan.
- Target 1.500+ county dalam tiga tahun (sekitar 170 per tahun), sekitar separuh gerai baru di kota tier 3 ke bawah, dan aspirasi 20.000 gerai.
- Starbucks kini **pemberi lisensi dengan kepemilikan 40%**. Standar desain, review desain, dan akses ke data kinerja per format harus diatur dalam perjanjian lisensi atau tata kelola JV, karena tidak lagi datang otomatis dari kepemilikan penuh.

## 4. Peta format desain

| Format | Peran strategis | Mekanisme pendapatan | Kekuatan bukti |
|---|---|---|---|
| Shanghai Reserve Roastery | Brand halo, legitimasi "otoritas kopi" | Ticket sangat tinggi, trafik destinasi, nilai media | Kuat (satu gerai) / lemah (jaringan) |
| Gerai & bar Reserve | Menjaga batas atas harga | Ticket & campuran produk premium | Tidak ada data publik |
| Heritage adaptive reuse (mis. Tianjin Riverside 66) | Legitimasi lokal, lokasi ikonik | Trafik destinasi & PR | Lemah |
| Gerai tematik ICH (5 gerai) | Relevansi budaya & ESG | Merchandise, workshop, afinitas merek | Tidak ada data publik |
| Third place inti | Dasar harga premium | Harga premium karena ruang; sewa tinggi | Sedang (agregat) |
| Starbucks Now (express) | Okasi on-the-go & delivery | Throughput, capex rendah | Lemah |
| Gerai county/tier bawah | Mesin pertumbuhan jumlah gerai | Footprint baru; biaya lebih rendah | Sedang (agregat) |
| Takeover fasad bertema IP | Pemicu kunjungan | Traffic + ticket (bundel merchandise) | Sedang (korelasi waktu) |
| Format mikro 千店千面 (10 m², kereta kopi, kantor, RS) | Okasi & lokasi baru | Capex per unit rendah | Belum ada data |
| Pembanding: pickup Luckin | Pemimpin volume & harga | Volume, sewa & dekorasi rendah | Kuat (20-F) |

Rincian lengkap tiap format, termasuk sumber, ada di [report.md](report.md).

## 5. Implikasi dan rekomendasi

Rekomendasi berlaku untuk tim yang mengelola merek kopi premium dalam situasi serupa: ekspansi cepat, kompetitor murah berbasis pickup, dan model lisensi atau JV.

**Untuk Director of Design**

1. **Susun sistem desain per peran, bukan satu template.** Tetapkan empat peran format: destinasi/flagship, premium Reserve, komunitas third place, dan konvenien/mikro. Masing-masing punya spesifikasi shopfront dan KPI sendiri. Gerai 10 m² tidak dinilai dengan KPI dwell time, dan flagship tidak dinilai dengan P&L gerai.
2. **Rancang shopfront hibrida untuk era delivery.** Pisahkan jalur rider dan pickup (jendela atau loker di muka gerai, layar status pesanan) dari pintu masuk tamu yang duduk. Keluhan third place di China tahun 2025, ketika kursi penuh sementara pesanan delivery menumpuk di counter, adalah masalah tata ruang yang bisa diselesaikan lewat desain.
3. **Buat kit "lapisan budaya" modular untuk county.** Dengan sekitar 170 county baru per tahun, desain bespoke seperti gerai ICH tidak bisa diskalakan. Pisahkan kerangka standar yang murah dari lapisan lokal (material, kerajinan, cerita), sehingga 千店千面 bisa dijalankan dengan capex terkendali.
4. **Perlakukan fasad sebagai media yang bisa diprogram.** Panel, window box, dan pencahayaan yang dapat diganti per kampanye (IP, musiman) dengan biaya rendah, dan setiap pemasangan diukur sebagai eksperimen (gerai treatment vs kontrol).

**Untuk Corporate Strategic Direction**

5. **Nilai pertumbuhan dengan produktivitas dan ROI per format, bukan jumlah gerai.** Pantau pendapatan per gerai dan per m², margin empat dinding, dan payback per format dan tier kota. Dari FY2019 sampai FY2025, pendapatan per gerai turun 43% sementara jumlah gerai hampir dua kali lipat.
6. **Masukkan tata kelola desain dan data ke perjanjian JV atau lisensi.** Hak review desain untuk format baru dan flagship, standar merek minimum untuk shopfront, dan kewajiban berbagi data kinerja per atribut desain.
7. **Anggarkan flagship sebagai capex merek.** Ukur dengan brand lift, share of voice di Xiaohongshu dan Douyin, serta ticket di gerai Reserve sekitarnya, bukan P&L gerai flagship saja.
8. **Pakai desain untuk menjaga ticket.** Karena JV memilih tidak menurunkan harga, format premium harus membenarkan harga itu. Setelah sembilan dari sepuluh kuartal ticket negatif, ticket adalah KPI utama untuk investasi desain premium.

## 6. Kerangka pengukuran: supaya korelasi bisa diukur secara internal

**a. Tandai atribut desain setiap gerai:** peran format, luas (m²), lebar muka gerai (m), rasio kaca pada fasad (%), skor visibilitas signage dari jalan/mal, jumlah pintu, ada tidaknya jalur rider terpisah, jumlah kursi, lapisan lokal/budaya (ya/tidak, jenis), tier kota, tipe lokasi (mal, jalan, kantor, transit, wisata), dan umur gerai.

**b. Ukur hasil yang terkait langsung dengan desain:**

| KPI | Dipengaruhi desain lewat | Alat ukur |
|---|---|---|
| Capture rate (orang lewat → masuk) | Shopfront, visibilitas, display | Sensor footfall di pintu & di depan gerai |
| Transaksi per jam per m² | Tata ruang, alur, pickup | POS + luas |
| Ticket rata-rata & campuran premium | Bar Reserve, merchandise, suasana | POS |
| Dwell time & okupansi kursi | Kenyamanan, zonasi | Sensor atau sampling |
| Porsi digital/delivery & waktu serah | Jalur rider, loker | Data aplikasi & delivery |
| Pendapatan per m², margin empat dinding, payback | Semua | Keuangan gerai |

**c. Metode (dari yang paling cepat):**
1. **Regresi lintas gerai** dengan kontrol lokasi, tier, catchment, dan umur gerai untuk memetakan atribut desain yang berasosiasi dengan kinerja.
2. **Difference-in-differences** untuk setiap remodel atau perubahan shopfront: gerai treatment dibandingkan dengan gerai kontrol berpasangan (tier, tipe lokasi, dan tren pra-perlakuan serupa) selama 12–24 minggu.
3. **Uji terkontrol untuk kampanye fasad**, misalnya tema IP: sebagian gerai yang sebanding ditahan tanpa tema sebagai kontrol.
4. Mulai dengan pilot sekitar 30–50 gerai treatment dan kontrol berpasangannya. Ukuran sampel final dihitung dari variansi transaksi mingguan internal.

## 7. Keterbatasan

- Tidak ada data publik per gerai atau per format, sehingga hubungan desain dan pendapatan di tingkat jaringan disimpulkan dari data agregat.
- Periode analisis mengandung guncangan besar (COVID, perang harga, perubahan kanal) yang mendominasi variasi comp.
- Pendapatan geografis "China" di 10-K dihitung berdasarkan lokasi pelanggan dan mencakup pendapatan non-ritel kecil. Sejak Q3 FY2026 Starbucks hanya melaporkan royalti dan penjualan produk ke JV, sehingga seri company-operated berhenti di Q2 FY2026.
- Beberapa bukti berasal dari pernyataan manajemen di media (Roastery, county) atau media sekunder (keluhan third place). Bukti ini diberi bobot lebih rendah di peta format.

## 8. Sumber utama

**Dokumen resmi**
1. Starbucks 10-K FY2016–FY2025 (catatan geografis & store data): [FY2025](https://www.sec.gov/Archives/edgar/data/829224/000082922425000114/sbux-20250928.htm), [FY2023](https://www.sec.gov/Archives/edgar/data/829224/000082922423000058/sbux-20231001.htm), [FY2021](https://www.sec.gov/Archives/edgar/data/829224/000082922421000086/sbux-20211003.htm), [FY2020](https://www.sec.gov/Archives/edgar/data/829224/000082922420000078/sbux-20200927.htm), [FY2018](https://www.sec.gov/Archives/edgar/data/829224/000082922418000052/sbux-9302018x10xk.htm)
2. Press release kuartalan Starbucks (comp, transaksi, ticket, China Supplemental Data): [Q4 FY2016](https://www.sec.gov/Archives/edgar/data/829224/000082922416000078/sbux-1022016xexhibit991.htm), [Q4 FY2017](https://www.sec.gov/Archives/edgar/data/829224/000082922417000044/sbux-1012017xexhibit991.htm), [Q4 FY2018](https://www.sec.gov/Archives/edgar/data/829224/000082922418000044/sbux-09302018xexhibit991.htm), [Q4 FY2019](https://www.sec.gov/Archives/edgar/data/829224/000082922419000047/sbux-9292019xexhibit991.htm), [Q4 FY2020](https://www.sec.gov/Archives/edgar/data/829224/000082922420000073/sbux-9272020xexhibit991.htm), [Q4 FY2021](https://www.sec.gov/Archives/edgar/data/829224/000082922421000081/sbux-1032021xexhibit991.htm), [Q4 FY2022](https://www.sec.gov/Archives/edgar/data/829224/000082922422000052/sbux-1022022xexhibit991.htm), [Q4 FY2023](https://www.sec.gov/Archives/edgar/data/829224/000082922423000051/sbux-1012023xexhibit991.htm), [Q4 FY2024](https://www.sec.gov/Archives/edgar/data/829224/000082922424000051/sbux-9292024xexhibit991.htm), [Q1 FY2025](https://www.sec.gov/Archives/edgar/data/829224/000082922425000013/sbux-12292024xexhibit991.htm), [Q2 FY2025](https://www.sec.gov/Archives/edgar/data/829224/000082922425000033/sbux-03302025xexhibit991.htm), [Q3 FY2025](https://www.sec.gov/Archives/edgar/data/829224/000082922425000057/sbux-06292025xexhibit991.htm), [Q4 FY2025](https://www.sec.gov/Archives/edgar/data/829224/000082922425000074/sbux-09282025xexhibit991.htm), [Q1 FY2026](https://www.sec.gov/Archives/edgar/data/829224/000082922426000010/sbux-12282025xearningsrele.htm), [Q2 FY2026](https://www.sec.gov/Archives/edgar/data/829224/000082922426000078/sbux-03292026xearningsrele.htm), [Q3 FY2026](https://www.sec.gov/Archives/edgar/data/829224/000082922426000129/sbux-06282026xearningsrele.htm)
3. JV Starbucks–Boyu: [pengumuman 3 Nov 2025](https://www.sec.gov/Archives/edgar/data/829224/000082922425000079/a20251103-form8xkxex991.htm), [penutupan 2 Apr 2026](https://www.sec.gov/Archives/edgar/data/829224/000082922426000064/sbux-04022026xexhibit991.htm)
4. [Starbucks China Investor Conference 2018](https://www.starbucks.com.cn/en/about/news/starbucks-first-ever-china-investor-conference/)
5. Luckin Coffee 20-F: [FY2025](https://www.sec.gov/Archives/edgar/data/1767582/000110465926035712/lk-20251231x20f.htm), [FY2022](https://www.sec.gov/Archives/edgar/data/1767582/000110465923042448/lk-20221231x20f.htm)
6. [FRED DEXCHUS, kurs USD/CNY](https://fred.stlouisfed.org/series/DEXCHUS)

**Media & industri**
7. [CNBC: penjualan Roastery Shanghai (Jan 2018)](https://www.cnbc.com/2018/01/25/eight-weeks-in-starbucks-shanghai-roastery-is-raking-in-insane-sales.html)
8. [Quartz: "In China, Starbucks … rents couches" (2013)](https://qz.com/125138/in-china-starbucks-doesnt-sell-coffee-to-make-its-millions-it-rents-couches) · [CNBC: laporan CCTV soal harga (Okt 2013)](https://www.cnbc.com/2013/10/21/starbucks-under-fire-in-china-over-high-prices.html)
9. [NRN: format express Starbucks Now (Jul 2019)](https://www.nrn.com/news/starbucks-opens-first-express-store-format-china)
10. [China Daily: kinerja gerai county (Okt 2024)](https://www.chinadaily.com.cn/a/202410/31/WS67231b00a310f1265a1caab8.html) · [tier bawah (Jan 2026)](https://global.chinadaily.com.cn/a/202601/30/WS697c02a0a310d6866eb368ab.html) · [ekspansi pasca-JV (Apr 2026)](https://www.chinadaily.com.cn/a/202604/08/WS69d647e6a310d6866eb424b0.html)
11. [Sina Finance: "不降价，开更多店型" (Apr 2026)](http://finance.sina.com.cn/jjxw/2026-04-08/doc-inhtuyvv6406966.shtml) · [QQ News: 千店千面 & Reserve 星意坊 SKP (Sep 2026)](https://news.qq.com/rain/a/20260916A0CGMJ00)
12. [Reuters via Yahoo Finance: pangsa pasar Euromonitor 34%→14% (Mar 2025)](https://finance.yahoo.com/news/analysis-starbuckss-china-comeback-relies-000443589.html) · [Fortune (Nov 2025)](https://fortune.com/2025/11/04/starbucks-china-boyu-luckin-brian-niccol/)
13. [Xinhua: gerai ICH Hangzhou (Agu 2025)](https://english.news.cn/20250829/926124dbefdf4f1181bc1bc868c3a9e4/c.html) · [Starbucks Stories: gerai ICH](https://stories.starbucks.com/asia/stories/2025/how-starbucks-intangible-cultural-heritage-themed-stores-in-china-empower-communities/) · [Starbucks Stories: Tianjin Riverside 66 (2019)](https://stories.starbucks.com/asia/stories/2019/starbucks-preserves-heritage-site-in-china-to-open-flagship-location-in-tianjin/)
14. [Restaurant Dive: coffeehouse uplift (Jul 2026)](https://www.restaurantdive.com/news/starbucks-q3-turnaround-gains-sales-momentum/826543/)
15. [CNBC: gerai high-end Luckin (Feb 2026)](https://www.cnbc.com/2026/02/08/chinas-luckin-coffee-opens-its-first-high-end-store.html)
16. [BigGo Finance: krisis "third place" Starbucks China (2025)](https://finance.biggo.com/news/f1823dac-b7c7-4061-8fd2-ce52ee7fe763) (media sekunder)

**Akademik**
17. Li, R., Laroche, M., Richard, M.-O., & Cui, X. (2022). More than a mere cup of coffee: When perceived luxuriousness triggers Chinese customers' perceptions of quality and self-congruity. *Journal of Retailing and Consumer Services*, 64. [doi:10.1016/j.jretconser.2021.102759](https://doi.org/10.1016/j.jretconser.2021.102759)
18. Ge, Y., Yuan, Q., Wang, Y., & Park, K. (2021). The structural relationship among perceived service quality, perceived value, and customer satisfaction: Focused on Starbucks Reserve coffee shops in Shanghai, China. *Sustainability*, 13(15), 8633. [doi:10.3390/su13158633](https://doi.org/10.3390/su13158633)
19. Venkatraman, M., & Nelson, T. (2008). From servicescape to consumptionscape: A photo-elicitation study of Starbucks in the New China. *Journal of International Business Studies*, 39(6), 1010–1026. [doi:10.1057/palgrave.jibs.8400353](https://doi.org/10.1057/palgrave.jibs.8400353)
20. Bitner, M. J. (1992). Servicescapes: The impact of physical surroundings on customers and employees. *Journal of Marketing*, 56(2), 57–71. [doi:10.1177/002224299205600205](https://doi.org/10.1177/002224299205600205)
21. Sen, S., Block, L. G., & Chandran, S. (2002). Window displays and consumer shopping decisions. *Journal of Retailing and Consumer Services*, 9(5), 277–290. [doi:10.1016/S0969-6989(01)00037-6](https://doi.org/10.1016/S0969-6989(01)00037-6)
22. Oh, H., & Petrie, J. (2012). How do storefront window displays influence entering decisions of clothing stores? *Journal of Retailing and Consumer Services*, 19(1), 27–35. [doi:10.1016/j.jretconser.2011.08.003](https://doi.org/10.1016/j.jretconser.2011.08.003)

---

*Reproduksi angka:* `python3 analysis.py` (menghasilkan `data/analysis_output.json`), `python3 build_results.py`, `python3 generate_report.py`.
