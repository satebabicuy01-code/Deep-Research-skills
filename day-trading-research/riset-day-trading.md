# Riset: Day Trading — Asal-usul, Landasan Teori, dan Konsep Praktis (Pasar AS & Indonesia)

> **Tanggal riset:** 23 Oktober 2026
> **Cakupan:** sejarah ide day trading, materi/teori dasar, bukti empiris, konsep yang bisa diterapkan, serta perbedaan praktik di pasar saham Amerika Serikat (NYSE/Nasdaq) dan Indonesia (BEI/IDX).
> **Disclaimer:** Dokumen ini adalah bahan belajar, **bukan rekomendasi investasi**. Aturan bursa (terutama di BEI) sedang sering berubah pada Oktober 2026; selalu cek pengumuman resmi [idx.co.id](https://www.idx.co.id), [ojk.go.id](https://www.ojk.go.id), [finra.org](https://www.finra.org), dan [sec.gov](https://www.sec.gov) sebelum bertransaksi.

---

## Daftar Isi

1. [Ringkasan Eksekutif](#1-ringkasan-eksekutif)
2. [Apa Itu Day Trading](#2-apa-itu-day-trading)
3. [Dari Mana Ide Day Trading Berasal (Sejarah)](#3-dari-mana-ide-day-trading-berasal-sejarah)
4. [Materi & Teori yang Menjadi Dasar Day Trading](#4-materi--teori-yang-menjadi-dasar-day-trading)
5. [Bukti Empiris: Apakah Day Trader Untung?](#5-bukti-empiris-apakah-day-trader-untung)
6. [Konsep-konsep yang Bisa Diterapkan](#6-konsep-konsep-yang-bisa-diterapkan)
7. [Manajemen Risiko & Matematika Trading](#7-manajemen-risiko--matematika-trading)
8. [Perbandingan Aturan Main: AS vs Indonesia](#8-perbandingan-aturan-main-as-vs-indonesia)
9. [Kondisi Terkini (Oktober 2026) & Implikasinya](#9-kondisi-terkini-oktober-2026--implikasinya)
10. [Kerangka Rutin Harian & Template Trading Plan](#10-kerangka-rutin-harian--template-trading-plan)
11. [Rambu Hukum & Etika](#11-rambu-hukum--etika)
12. [Daftar Bacaan yang Disarankan](#12-daftar-bacaan-yang-disarankan)
13. [Daftar Referensi](#13-daftar-referensi)

---

## 1. Ringkasan Eksekutif

- **Asal ide.** Day trading bukan ide baru. Akarnya ada pada spekulan "ticker tape" dan *bucket shop* akhir abad ke-19 (Jesse Livermore mulai berdagang di bucket shop pada usia 14 tahun), pembaca pita (*tape reader*) seperti Richard Wyckoff (1910), dan para *scalper/local* di lantai bursa berjangka Chicago. Day trading oleh **ritel** baru meledak setelah: (1) dihapusnya komisi tetap di AS pada **1 Mei 1975**, (2) sistem eksekusi otomatis Nasdaq **SOES** pasca-crash 1987 yang dimanfaatkan "SOES bandits", (3) **Order Handling Rules 1997** dan lahirnya ECN, (4) broker online dan bubble dot-com akhir 1990-an, lalu (5) komisi nol (2019) dan aplikasi mobile.
- **Landasan teori.** Tidak ada "satu teori" day trading. Dasarnya adalah gabungan: **mikrostruktur pasar** (spread, likuiditas, order flow), **pola intraday yang terdokumentasi secara akademik** (momentum 30 menit pertama → 30 menit terakhir, pola musiman per setengah jam, volume berbentuk U), **analisis teknikal klasik** (Dow, Wyckoff, Livermore, Market Profile, VWAP), dan **keuangan perilaku** (overconfidence, disposition effect).
- **Bukti empiris keras.** Riset berskala besar konsisten menunjukkan **mayoritas day trader ritel rugi**: di Taiwan < 1% day trader yang bisa untung secara konsisten setelah biaya; di Brasil 97% day trader yang bertahan > 300 hari rugi; di India > 70% trader intraday rugi (FY23). Strategi yang terlihat menguntungkan di paper (misalnya Opening Range Breakout) sering **hilang edge-nya setelah spread dan slippage** dihitung.
- **Konsep yang bisa diterapkan.** Seleksi *stocks in play*, Opening Range Breakout, VWAP, intraday momentum, gap strategy, level kunci (high/low hari sebelumnya), Volume/Market Profile, tape reading/order book, bandarmologi & foreign flow (khas IDX), strategi sesi pre-closing — **semuanya hanya berguna jika dibungkus manajemen risiko** (risk per trade, batas rugi harian, expectancy positif setelah biaya).
- **Perubahan besar 2026.**
  - **AS:** aturan *Pattern Day Trader* (minimum ekuitas USD 25.000) **dihapus**, diganti standar *intraday margin*, efektif **4 Juni 2026**; perdagangan **23 jam/5 hari** di Nasdaq/NYSE Arca ditargetkan mulai **6 Desember 2026**.
  - **Indonesia:** **Short selling & Intraday Short Selling (IDSS)** mulai **1 Oktober 2026**; harga minimum saham turun ke **Rp1** (28 Sep 2026); ARB **asimetris 7%** sejak 19 Oktober 2026 setelah IHSG anjlok tajam terkait konsultasi reklasifikasi MSCI; trading halt terpicu beberapa kali sepanjang 2026.

---

## 2. Apa Itu Day Trading

**Day trading** = membeli dan menjual (atau short lalu menutup) instrumen yang sama **dalam satu hari bursa**, sehingga tidak membawa posisi menginap (*overnight*). Tujuannya mengambil keuntungan dari pergerakan harga jangka pendek, bukan dari pertumbuhan nilai perusahaan.

Spektrum gaya trading berdasarkan lama memegang posisi:

| Gaya | Lama posisi | Sumber "edge" yang dicari |
|---|---|---|
| **Scalping** | detik – menit | Spread, antrian order, ketidakseimbangan order jangka sangat pendek |
| **Day trading (momentum/intraday)** | menit – jam | Momentum, breakout, reaksi berita, pola intraday |
| **Swing trading** | hari – minggu | Tren jangka pendek, pola grafik harian |
| **Position trading / investasi** | bulan – tahun | Fundamental, tren besar |

Di Indonesia, istilah populer yang terkait: **"scalping"**, **"trading harian"**, **"BSJP" (Beli Sore Jual Pagi)** — catatan: BSJP sebenarnya *overnight*, jadi secara definisi bukan day trading murni — serta **"bandarmologi"**.

---

## 3. Dari Mana Ide Day Trading Berasal (Sejarah)

### 3.1 Akar global (abad ke-19 – awal abad ke-20)

| Periode | Peristiwa | Relevansi bagi day trading |
|---|---|---|
| Akhir 1800-an | **Ticker tape** menyiarkan harga hampir real-time ke kantor broker | Pertama kalinya harga bisa "dibaca" sepanjang hari → lahir *tape reading* |
| 1890-an – 1900-an | **Bucket shop**: tempat taruhan naik-turun harga saham tanpa benar-benar membeli saham | Bentuk awal spekulasi jangka sangat pendek oleh publik. **Jesse Livermore** mulai di sini pada usia 14 tahun dan akhirnya dilarang masuk banyak bucket shop di Boston karena terlalu sering menang ([Wikipedia – Livermore](https://en.wikipedia.org/wiki/Jesse_Livermore); [Wikipedia – Bucket shop](https://en.wikipedia.org/wiki/Bucket_shop_(stock_market))) |
| 1910 | **Richard D. Wyckoff** (nama pena *Rollo Tape*) menulis *Studies in Tape Reading* | Salah satu "buku teks" pertama membaca harga & volume intraday ([IFA Book Library](https://www.ifa.com/book-library/2154/studies_in_tape_reading)) |
| 1923 | **Edwin Lefèvre**, *Reminiscences of a Stock Operator* — biografi semi-fiksi Livermore | Hingga kini dianggap bacaan wajib trader; kini domain publik di [Project Gutenberg](https://www.gutenberg.org/ebooks/60979) |
| 1930-an – 1980-an | *Locals* & *scalper* di lantai bursa berjangka Chicago (CBOT/CME). **J. Peter Steidlmayer** (CBOT) mengembangkan **Market Profile** (ca. 1959–1985) | Konsep *initial balance*, *value area*, dan opening range lahir dari pengamatan trader lantai ([Wikipedia – Market Profile](https://en.wikipedia.org/wiki/Market_profile); [Traders.com](https://store.traders.com/traderscom/-v07-c04-underst-pdf.html)) |

### 3.2 Demokratisasi day trading di AS (1975 – 2000)

1. **"May Day" – 1 Mei 1975.** SEC menghapus komisi broker tetap yang sudah berlaku 183 tahun. Charles Schwab memangkas biaya > 50% dan lahirlah *discount broker* ([About Schwab](https://www.aboutschwab.com/mss/story/the-action-that-forever-altered-investing)). Biaya transaksi murah adalah syarat mutlak day trading.
2. **Crash 1987 → SOES.** Setelah market maker Nasdaq "tidak angkat telepon" saat crash 1987, Nasdaq mewajibkan **Small Order Execution System (SOES)**: order ≤ 500 lembar dieksekusi otomatis di harga terbaik market maker. Sekelompok trader — dijuluki **"SOES bandits"** — memanfaatkan kecepatan sistem ini untuk mengambil untung kecil berulang kali ([CNBC](https://www.cnbc.com/id/39038914); [SuperMoney](https://www.supermoney.com/encyclopedia/stock-bandit)).
3. **Harvey Houtkin & All-Tech.** Houtkin mengajarkan gaya ini dan membuka "ruang trading" berisi deretan layar tempat orang trading seharian. All-Tech kemudian membuat ECN *Attain* (1998) yang akhirnya menjadi *Direct Edge* ([CNBC](https://www.cnbc.com/id/39038914)).
4. **Order Handling Rules (Januari 1997) & ECN.** SEC mewajibkan market maker menampilkan limit order nasabah yang lebih baik ke publik/ECN. **Island ECN** (anak usaha Datek) termasuk ECN pertama yang memanfaatkan aturan ini ([Island ECN history](https://www.fundinguniverse.com/company-histories/the-island-ecn-inc-history/)). Hasilnya: spread menyempit dan ritel bisa "masuk" ke order book.
5. **Broker online & dot-com (1995–2000).** Komisi online turun ke sekitar USD 14,95 lalu USD 4,95 per transaksi ([Fortune](https://www.fortune.com/2019/10/03/zero-commissions-stock-trading-fees-as-brokerages-drop-wave-consolidation-follow/)). Day trading menjadi fenomena budaya; banyak yang bangkrut ketika bubble pecah 2000.
6. **2001 – Pattern Day Trader (PDT) rule.** FINRA (dulu NASD/NYSE) menetapkan: akun margin yang melakukan ≥ 4 day trade dalam 5 hari kerja wajib berekuitas minimal **USD 25.000** ([tastytrade](https://tastytrade.com/learn/markets/industry/pattern-day-trading/)).

### 3.3 Era aplikasi & komisi nol (2019 – 2026)

- **Oktober 2019:** Schwab menghapus komisi; TD Ameritrade dan E*Trade mengikuti dalam sehari ([Fortune](https://www.fortune.com/2019/10/03/zero-commissions-stock-trading-fees-as-brokerages-drop-wave-consolidation-follow/)).
- **2020–2021:** Ledakan ritel saat pandemi (fenomena "meme stocks" seperti GameStop) — pengetahuan umum.
- **2024:** Settlement saham AS dipersingkat ke **T+1** mulai 28 Mei 2024 ([LSEG/FTSE Russell](https://www.lseg.com/en/ftse-russell/research/market-index-impact-shorter-equity-settlement-cycles)).
- **2026:**
  - SEC menyetujui amandemen FINRA Rule 4210 pada 14 April 2026 yang **menghapus rezim PDT dan syarat USD 25.000**, diganti **intraday margin** berbasis *real-time margin excess*. Efektif **4 Juni 2026**; broker yang butuh waktu diberi batas akhir kepatuhan **20 Oktober 2027** ([Federal Register](https://www.federalregister.gov/documents/2026/01/14/2026-00519/self-regulatory-organizations-financial-industry-regulatory-authority-inc-notice-of-filing-of-a); [FINRA](https://www.finra.org/compliance-tools/weekly-archive/01072026); [King & Spalding](https://www.kslaw.com/insights/articles/finra-adopts-sweeping-changes-to-margin-requirements-for-day-trading); [E*Trade](https://us.etrade.com/knowledge/library/margin/pattern-day-trading-rule-change); [TradeStation](https://www.tradestation.com/insights/2026/05/06/day-trade-rule-change/)).
  - SEC menyetujui proposal **"23/5" trading** Nasdaq (10 April 2026). Sesi malam 21.00–04.00 ET ditargetkan mulai **6 Desember 2026**, bergantung kesiapan SIP & infrastruktur ([Simpson Thacher](https://www.stblaw.com/docs/default-source/memos/firmmemo_04_29_26); [Jones Day](https://www.jonesday.com/en/insights/2026/09/nyse-and-nasdaq-move-to-23hour-trading-day-overnight-session-is-an-evolution-but-not-yet-a-revolution); [WilmerHale](https://www.wilmerhale.com/en/insights/client-alerts/20260929-23x5-trading-comes-to-us-exchanges-what-firms-should-know-before-launch)).

### 3.4 Perjalanan di Indonesia

| Periode | Peristiwa | Dampak bagi trader harian |
|---|---|---|
| 1977 | Pasar modal modern diaktifkan kembali (BEJ) | HUT pasar modal diperingati setiap Agustus ([Bisnis.com](https://market.bisnis.com/read/20260810/7/1994994/hut-ke-49-pasar-modal-total-investor-tembus-3030-juta-sid)) |
| 1995 | Perdagangan BEJ beralih dari manual ke **JATS** (Jakarta Automated Trading System) | Order book elektronik → dasar scalping modern *(pengetahuan umum)* |
| 2000-an | Remote trading & online trading oleh sekuritas | Ritel bisa trading dari rumah *(pengetahuan umum)* |
| 2007 | BEJ + BES bergabung menjadi **Bursa Efek Indonesia (BEI/IDX)** | *(pengetahuan umum)* |
| 2018 | Settlement dipercepat dari T+3 ke **T+2** ([Kontan](https://investasi.kontan.co.id/news/aturan-t2-berlaku-mulai-semester-i-2018)) | Perputaran modal lebih cepat |
| 2020–2021 | Ledakan investor ritel saat pandemi; populer istilah "saham gorengan", "pom-pom", "bandarmologi" | Day trading jadi tren di media sosial |
| 2023–2024 | **Papan Pemantauan Khusus (PPK)** dengan *Full Periodic Call Auction* (fase II 25 Maret 2024) | Saham bermasalah tidak lagi diperdagangkan kontinu → tidak cocok untuk scalping ([ANTARA](https://www.antaranews.com/berita/4027269/bei-implementasikan-papan-pemantauan-khusus-full-periodic-call-auction)) |
| April 2025 | Ambang trading halt dinaikkan ke 8% / 15% / 20% ([Katadata](https://katadata.co.id/finansial/bursa/67f46ab19a26f/bei-naikan-ambang-batas-trading-halt-jadi-8)) | |
| 2025 | Porsi ritel ~50% dari perdagangan harian (naik dari ~33% tahun sebelumnya) ([The Diplomat](https://thediplomat.com/2026/02/indonesias-stock-market-sell-off-explained/)) | Pasar makin didominasi ritel |
| 2026 | SID tembus **32,17 juta** (Sep 2026); >80% investor berusia ≤ 40 tahun ([IDX Channel/RCTI+](https://www.rctiplus.com/news/detail/idxchannel/5493985/ojk-sebut-gen-z-dan-milenial-dominasi-pasar-modal--jumlah-investor-tembus-32-juta)) | |
| Okt 2026 | **Short selling & IDSS** resmi berjalan; **ARB asimetris 7%**; harga minimum saham Rp1 | Lihat [Bagian 9](#9-kondisi-terkini-oktober-2026--implikasinya) |

**Kesimpulan bagian ini:** ide day trading lahir dari (a) ketersediaan harga real-time, (b) biaya transaksi yang turun drastis, dan (c) akses langsung ritel ke order book. Indonesia mengikuti pola yang sama dengan jeda waktu, dan baru pada 2026 memiliki instrumen short intraday.

---

## 4. Materi & Teori yang Menjadi Dasar Day Trading

Day trading berdiri di atas lima "pilar" materi. Penting dipahami: sebagian berbasis riset akademik yang teruji, sebagian lagi berbasis pengalaman praktisi (heuristik).

### 4.1 Pilar 1 — Mikrostruktur Pasar (cara harga terbentuk)

Konsep inti:
- **Bid–ask spread**: biaya implisit setiap kali masuk-keluar. Bagi scalper, spread sering lebih besar dari target profit.
- **Likuiditas & kedalaman order book**: seberapa banyak lot yang bisa ditransaksikan tanpa menggeser harga.
- **Order flow & ketidakseimbangan order**: pihak yang "agresif" (market order / *hajar kanan–kiri*) menggerakkan harga.
- **Market maker vs. limit order book**: AS memakai kombinasi market maker, exchange, ECN, dan *dark pool*; BEI memakai **order-driven continuous auction** (JATS) dengan pre-opening dan pre-closing call auction.
- **Tick size (fraksi harga)**: di BEI fraksi yang besar relatif terhadap harga (mis. saham Rp150 dengan fraksi Rp1 = 0,67% per tick) memengaruhi biaya dan peluang scalping.

Rujukan akademik: Larry Harris, *Trading and Exchanges: Market Microstructure for Practitioners* (2003); model Kyle (1985) dan Glosten–Milgrom (1985) tentang informasi & spread *(rujukan standar mikrostruktur)*. VWAP sebagai tolok ukur biaya eksekusi diformalkan oleh **Berkowitz, Logue & Noser (1988, Journal of Finance)** ([Wikipedia – VWAP](https://en.wikipedia.org/wiki/Volume-weighted_average_price); [Madhavan 2002](https://www.smallake.kr/wp-content/uploads/2014/07/TP_Spring_2002_Madhavan.pdf)).

### 4.2 Pilar 2 — Pola Intraday yang Terdokumentasi Akademik

| Temuan | Sumber | Inti | Catatan |
|---|---|---|---|
| **Market intraday momentum** | Gao, Han, Li & Zhou (2018), *Journal of Financial Economics* | Return 30 menit pertama (dihitung dari close kemarin) memprediksi return 30 menit terakhir pada SPY; lebih kuat di hari volatil, volume tinggi, dan hari rilis data makro | R² kecil (~2% pada draf awal) → sinyal lemah, butuh disiplin ([WUSTL](https://profiles.wustl.edu/en/publications/market-intraday-momentum/); [Alpha Architect](https://alphaarchitect.com/2014/08/attention-prop-traders-the-first-half-hour-of-trading-predicts-the-last-half-hour/)) |
| **Pola musiman per setengah jam** | Heston, Korajczyk & Sadka (2010), *Journal of Finance* | Return pada interval setengah jam yang sama cenderung berulang di hari-hari berikutnya (hingga ≥ 40 hari); ada *reversal* jangka sangat pendek akibat bid-ask bounce | Manfaat utama: **menghemat biaya eksekusi** setara spread efektif ([Kellogg](https://www.kellogg.northwestern.edu/academics-research/research/detail/2010/intraday-patterns-in-the-cross-section-of-stock-returns); [arXiv](https://ar5iv.arxiv.org/html/1005.3535)) |
| **Intraday momentum di BEI** | *Intraday Return of Winners vs Losers: Indonesian Capital Market Evidence* (IJBS UNIMAS, 2024) | 177 emiten, 2021–2022: 30 menit pertama signifikan memprediksi 30 menit terakhir, baik saham *winner* maupun *loser* | Bukti lokal bahwa pola Gao dkk. juga muncul di IDX ([IJBS](https://publisher.unimas.my/ojs/index.php/IJBS/article/view/7630)) |
| **Volume berbentuk "U"** | Admati & Pfleiderer (1988, *Review of Financial Studies*), Jain & Joh (1988) *(rujukan klasik)* | Volume & volatilitas tinggi di awal dan akhir sesi, sepi di tengah hari | Implikasi: strategi breakout cenderung di awal sesi; tengah hari rawan *false breakout* ([Otago WP](https://ourarchive.otago.ac.nz/bitstream/handle/10523/1540/ImprovingVWAPStrategiesADynamicalVolumeApproach2006.pdf?sequence=3)) |
| **Opening Range Breakout (ORB)** | Zarattini & Aziz (2023, SSRN 4416622); Zarattini, Barbon & Aziz (2024, SSRN 4729284) | ORB 5 menit pada QQQ dan pada *Stocks in Play* (saham dengan volume relatif tinggi) diklaim Sharpe ~2,4 | Replikasi independen: **edge kotor terulang, edge bersih ≈ nol** setelah spread & slippage ([CXO Advisory](https://www.cxoadvisory.com/individual-investing/intraday-trading-of-overactive-stocks-via-opening-range-breakout/); [MQL5 replikasi](https://www.mql5.com/en/blogs/post/776235)) |
| **Trading halt di BEI** | Ekaputra & Dwijayanti (2008) | Trading halt tidak signifikan menurunkan volatilitas intraday (sampel 2004) | ([RePEc](https://ideas.repec.org/a/lpe/efijnl/200813.html)) |

### 4.3 Pilar 3 — Analisis Teknikal Klasik & Praktisi

| Tokoh/karya | Kontribusi untuk day trader |
|---|---|
| **Charles Dow** (teori Dow, ~1900) | Tren, konfirmasi volume, struktur higher-high/higher-low |
| **Richard Wyckoff** — *Studies in Tape Reading* (1910) | Akumulasi–distribusi, *effort vs result* (volume vs pergerakan harga), membaca pita |
| **Jesse Livermore / Lefèvre** — *Reminiscences of a Stock Operator* (1923); *How to Trade in Stocks* (1940) | *Pivotal points*, "garis resistensi terkecil", cut loss, jangan averaging down saat salah |
| **Edwards & Magee** — *Technical Analysis of Stock Trends* (1948) | Pola grafik (flag, triangle, head & shoulders) |
| **Steve Nison** — *Japanese Candlestick Charting Techniques* (1991) | Candlestick sebagai pembacaan psikologi per bar |
| **J. Peter Steidlmayer** — Market Profile (CBOT) | *Initial Balance*, *Value Area*, *Point of Control* |
| **Toby Crabel** — *Day Trading with Short Term Price Patterns and Opening Range Breakout* (1990) | Formalisasi ORB, NR4/NR7 (hari rentang sempit) ([Wikipedia – Crabel](https://en.wikipedia.org/wiki/Toby_Crabel)) |
| **Linda Raschke & Larry Connors** — *Street Smarts* (1995) | Pola swing/intraday jangka pendek yang terdefinisi |
| **Al Brooks** — seri *Reading Price Charts Bar by Bar* | Price action murni per bar |
| **Andrew Aziz** — *How to Day Trade for a Living* | Pendekatan modern ritel: Stocks in Play, ORB, VWAP, risk per trade |

### 4.4 Pilar 4 — Keuangan Perilaku (psikologi)

- **Overconfidence → overtrading.** Barber & Odean (2000), 66.465 rumah tangga (1991–1996): kelompok yang paling sering trading memperoleh return 11,4%/tahun vs pasar 17,9% ([Odean – Haas](https://faculty.haas.berkeley.edu/odean/papers/returns/Returns.html)).
- **Disposition effect** (Shefrin & Statman, 1985): cepat menjual yang untung, menahan yang rugi. Survei 385 investor ritel BEI menemukan efek ini merugikan kinerja, dan overconfidence mendorong frekuensi trading berlebihan ([Asian Publisher – JACTA](https://asianpublisher.id/journal/index.php/jacta/article/view/1030)).
- **Prospect theory** (Kahneman & Tversky, 1979): rasa sakit rugi > senangnya untung yang sama besar → trader cenderung "balas dendam" setelah rugi.
- **Herding** (ikut-ikutan): relevan untuk fenomena saham gorengan & pom-pom di media sosial ([Trisakti – herding & broker summary](https://e-journal.trisakti.ac.id/index.php/mraai/article/view/9502)).
- Bacaan praktis psikologi: Mark Douglas — *Trading in the Zone* (2000); Brett Steenbarger — *The Psychology of Trading* (2003); Ellen May — *Smart Traders Not Gamblers* (Indonesia) ([Gramedia](https://www.gramedia.com/products/smart-traders-not-gamblers-cd-cover-baru)).

### 4.5 Pilar 5 — Materi Khas Pasar Indonesia

- **Bandarmologi**: membaca jejak broker melalui *Broker Summary* → *Done Detail* → *Broker Distribution* untuk menduga akumulasi/distribusi. Keterbatasan penting: **satu kode broker mewakili banyak nasabah**, jadi tidak selalu mencerminkan satu "bandar" ([Reku](https://reku.id/campus/apa-itu-bandarmology); [Ajaib](https://ajaib.co.id/belajar/jadi-trader-handal/toolkit-bandarmology-di-ajaib-terminal)).
- **Foreign flow**: aliran beli/jual bersih investor asing sebagai proksi dana besar ([Ajaib](https://ajaib.co.id/belajar/investasi/strategi-trading-mengikuti-foreign-flow)). Studi lima juta transaksi di BEI menemukan investor asing mengungguli investor domestik baik dari return maupun nominal profit ([MDPI – IJFS 2024](https://www.mdpi.com/2227-7072/12/4/100)).
- **Mekanisme khas BEI**: ARA/ARB, fraksi harga, satuan lot (100 lembar), pre-opening & pre-closing call auction, UMA, suspensi, notasi khusus, Papan Pemantauan Khusus (lihat [Bagian 8](#8-perbandingan-aturan-main-as-vs-indonesia)).

---

## 5. Bukti Empiris: Apakah Day Trader Untung?

Bagian ini paling penting sebelum mencoba day trading.

| Studi | Pasar & data | Temuan utama |
|---|---|---|
| **Barber, Lee, Liu & Odean (2014)** — *The Cross-Section of Speculator Skill*, Journal of Financial Markets | Taiwan, 1992–2006, seluruh day trader | **< 1%** day trader mampu secara konsisten & dapat diprediksi memperoleh return abnormal positif setelah biaya. Top 500 trader tahun lalu: +38 bps/hari setelah biaya; kelompok terbawah: −28,9 bps/hari ([eScholarship](https://www.escholarship.org/uc/item/7k75v0qx); [PDF Haas](https://faculty.haas.berkeley.edu/odean/papers/day%20traders/Day%20Trading%20Skill%20110523.pdf)) |
| **Barber, Lee, Liu, Odean & Zhang** — *Learning Fast or Slow?* (Review of Asset Pricing Studies, 2020) | Taiwan | **97%** day trader kemungkinan rugi di masa depan; **74%** volume day trading dihasilkan trader yang punya riwayat rugi — mereka tidak berhenti walau terus rugi ([RePEc](https://ideas.repec.org/a/oup/rasset/v10y2020i1p61-93..html)) |
| **Chague, De-Losso & Giovannetti** — *Day Trading for a Living?* (2019/2020) | Brasil, futures indeks, pemula 2013–2015 | **97%** yang bertahan > 300 hari **rugi**; hanya ~1,1% yang menghasilkan di atas upah minimum; **tidak ada bukti belajar** — makin lama makin buruk ([SSRN/RePEc](https://econpapers.repec.org/RePEc:fgv:eesptd:525); [Quantpedia](https://quantpedia.com/retail-day-trading-is-an-uphill-battle/)) |
| **SEBI (2024)** | India, FY2023 | **> 70%** trader intraday individu rugi ([Business Standard](https://www.business-standard.com/markets/news/over-70-intra-day-traders-incur-losses-during-fy23-reveals-sebi-study-124072401110_1.html)) |
| **Barber & Odean (2000)** | AS, 66.465 rumah tangga | Makin sering trading, makin rendah return bersih ([Haas](https://faculty.haas.berkeley.edu/odean/papers/returns/Returns.html)) |
| **Replikasi ORB** | Futures indeks (5 pasar) | Edge kotor terulang (+0,13R), tapi **bersih ≈ nol**; 4 dari 5 pasar negatif setelah spread & slippage ([MQL5](https://www.mql5.com/en/blogs/post/776235)) |
| **Indonesia** | — | Belum ditemukan studi publik berskala besar tentang laba-rugi day trader di BEI. Bukti tidak langsung: investor asing mengungguli domestik ([MDPI](https://www.mdpi.com/2227-7072/12/4/100)); bias perilaku merugikan investor ritel ([JACTA](https://asianpublisher.id/journal/index.php/jacta/article/view/1030)) |

**Pelajaran yang bisa ditarik:**
1. Day trading adalah **permainan berbiaya tinggi**: biaya (fee, pajak, spread, slippage) adalah "lawan" yang pasti, sedangkan edge tidak pasti.
2. **Sebagian kecil** trader memang konsisten untung (Taiwan) — artinya skill ada, tetapi langka.
3. Pengalaman **tidak otomatis** membuat lebih baik (Brasil). Yang membedakan adalah **pengukuran** (jurnal & statistik) dan **berhenti/menyesuaikan** jika data menunjukkan tidak ada edge.
4. Paper yang menunjukkan strategi menguntungkan harus diuji ulang dengan **biaya riil pasar Anda**.

---

## 6. Konsep-konsep yang Bisa Diterapkan

Format setiap konsep: **Ide → Dasar → Cara pakai → Penyesuaian AS / Indonesia → Jebakan.**

### 6.1 Seleksi "Stocks in Play" (memilih saham yang tepat)

- **Ide:** Day trading hanya masuk akal pada saham yang **sedang bergerak dan likuid** hari itu.
- **Dasar:** Zarattini, Barbon & Aziz (2024) — ORB hanya diuji pada saham dengan volume relatif tidak biasa (mis. rata-rata volume ≥ 1 juta lembar/14 hari dan *relative volume* tinggi) ([CXO Advisory](https://www.cxoadvisory.com/individual-investing/intraday-trading-of-overactive-stocks-via-opening-range-breakout/)).
- **Cara pakai (scanner pagi):**
  1. Ada **katalis**: laporan keuangan, aksi korporasi, berita, rilis data makro.
  2. **Relative Volume (RVOL)** ≥ 2× rata-rata pada jam yang sama.
  3. **Gap** dari close kemarin (mis. > 2–3%).
  4. **Likuiditas**: spread sempit, nilai transaksi besar.
- **AS:** pre-market scanner (04.00–09.30 ET), earnings calendar, float, short interest.
- **Indonesia:** gunakan *top value*/*top gainer* di aplikasi sekuritas, cek keterbukaan informasi di IDX, hindari saham di **Papan Pemantauan Khusus (FCA)**, saham ber-**notasi khusus**, atau baru terkena **UMA**. Utamakan saham dengan nilai transaksi harian besar (mis. konstituen LQ45/IDX80).
- **Jebakan:** saham "terbang" dengan volume tipis = mudah masuk, sulit keluar.

### 6.2 Opening Range Breakout (ORB)

- **Ide:** Rentang harga 5/15/30 menit pertama (*opening range*) menjadi acuan; tembus atas → long, tembus bawah → short.
- **Dasar:** Crabel (1990); Steidlmayer (*initial balance*); Zarattini & Aziz (2023, 2024).
- **Cara pakai (versi sederhana):**
  1. Tandai high & low 5 menit pertama.
  2. Entry saat candle berikutnya menembus high (long) / low (short).
  3. Stop di sisi berlawanan opening range (atau setengahnya).
  4. Target: 2R atau keluar di akhir hari (*time stop*).
- **AS:** bisa long & short; paling umum pada saham *in play* atau ETF (QQQ/SPY).
- **Indonesia:** buka 09.00 WIB setelah pre-opening (08.45–08.59). Short hanya mungkin lewat **IDSS** di saham yang ada di Daftar Efek Short Selling dan melalui sekuritas berlisensi. Perhatikan bahwa **ARA/ARB** membatasi pergerakan harian.
- **Jebakan:** biaya & slippage menghapus edge (lihat replikasi). Gunakan hanya di saham sangat likuid dan uji dengan biaya riil.

### 6.3 VWAP (Volume Weighted Average Price)

- **Rumus:** `VWAP = Σ(harga × volume) / Σ(volume)` sejak pembukaan.
- **Ide:** VWAP adalah tolok ukur eksekusi institusi (dana pensiun/reksa dana) ([Wikipedia](https://en.wikipedia.org/wiki/Volume-weighted_average_price)). Harga di atas VWAP = pembeli dominan hari itu; di bawah = penjual dominan.
- **Cara pakai:**
  - *VWAP reclaim*: harga sempat di bawah lalu menembus & bertahan di atas VWAP → long.
  - *VWAP rejection*: harga gagal menembus VWAP dari bawah → hindari long / pertimbangkan short.
  - Sebagai **filter**: hanya long jika harga di atas VWAP.
- **Indonesia:** banyak aplikasi sekuritas & TradingView menyediakan VWAP intraday untuk saham IDX. Pada saham yang sepi, VWAP kurang bermakna.
- **Jebakan:** VWAP adalah indikator *lagging*; di hari tren kuat harga bisa jauh dari VWAP lama.

### 6.4 Intraday Momentum (30 menit pertama → 30 menit terakhir)

- **Ide & dasar:** Gao dkk. (2018) dan studi BEI (2024) menunjukkan arah 30 menit pertama cenderung berlanjut di 30 menit terakhir.
- **Cara pakai:** Jika return dari close kemarin hingga 30 menit pertama positif kuat (dan didukung volume), pertimbangkan posisi searah menjelang akhir sesi.
  - **AS:** ambil posisi ±15.30 ET, tutup di close (16.00 ET).
  - **Indonesia:** perhatikan sesi II berakhir 15.49 WIB, lalu **pre-closing 15.50–16.00 WIB** (call auction dengan *random closing*) — eksekusi di pre-closing berbeda karakter dengan pasar kontinu ([Bloomberg Technoz](https://www.bloombergtechnoz.com/detail-news/119339/jam-trading-saham-cek-panduan-lengkap-bursa-indonesia-2026/2)).
- **Jebakan:** daya prediksi kecil (R² rendah); hanya berguna sebagai *tilt* statistik dengan banyak sampel.

### 6.5 Gap and Go / Gap Fade

- **Gap and Go:** saham gap naik karena katalis kuat + volume tinggi → beli saat menembus high pre-market/opening range.
- **Gap Fade:** gap tanpa katalis/volume lemah → spekulasi menutup gap (kembali ke close kemarin).
- **Indonesia:** harga pembukaan ditentukan **pre-opening call auction**; gap besar di saham lapis bawah sering diikuti tekanan jual. ARA membatasi gap atas maksimal (mis. 20–35% sesuai rentang harga).
- **Jebakan:** memaksakan fade pada saham berita besar.

### 6.6 Level Kunci: High/Low Kemarin, Pre-market, Pivot, Angka Bulat

- **Ide:** Level yang dilihat banyak trader menjadi area reaksi (support/resistance).
- **Cara pakai:** Tandai *Previous Day High/Low/Close*, high/low pre-market (AS), *pivot point* klasik `P = (H + L + C)/3`, dan angka bulat (mis. Rp1.000, Rp5.000 — di BEI juga batas pergantian fraksi harga).
- **Jebakan:** level bukan dinding; konfirmasi dengan volume/order flow.

### 6.7 Volume Profile / Market Profile

- **Ide:** Tempat volume terbesar terjadi (*Point of Control*, *Value Area* ~70% volume) menunjukkan harga "wajar" yang diterima pasar; keluar dari value area dengan volume = potensi tren, kembali ke dalam = potensi rotasi.
- **Dasar:** Steidlmayer, CBOT ([Wikipedia](https://en.wikipedia.org/wiki/Market_profile)).
- **Cara pakai:** gunakan profil hari sebelumnya; perhatikan *initial balance* (1 jam pertama) sebagai bias hari itu.

### 6.8 Tape Reading & Order Book (Level 2 / Bid-Offer)

- **Ide:** Membaca siapa yang agresif: tumpukan antrian bid/offer, kecepatan *done trade*, order besar yang "dimakan" atau ditarik.
- **Dasar:** Wyckoff (1910), Livermore; mikrostruktur modern.
- **AS:** Level 2, *Time & Sales*; waspada **spoofing** (order palsu) — ilegal.
- **Indonesia:** antrian **bid/offer** & *running trade* sangat transparan per broker (Done Detail). Tanda klasik: antrian bid tebal yang tiba-tiba hilang, offer tebal yang terus "dihajar".
- **Jebakan:** order besar bisa dipasang untuk memancing; konteks harga & volume tetap utama.

### 6.9 Bandarmologi & Foreign Flow (khas IDX)

- **Ide:** Jika broker tertentu konsisten mengakumulasi dengan harga rata-rata tertentu, harga cenderung dijaga di atasnya.
- **Cara pakai:** Broker Summary (net buy/sell, average price) → Done Detail → Broker Distribution; filter investor *foreign* untuk saham big cap ([Reku](https://reku.id/campus/apa-itu-bandarmology); [Ajaib](https://ajaib.co.id/belajar/investasi/strategi-trading-mengikuti-foreign-flow)).
- **Bukti:** masih terbatas (skripsi/uji kecil, mis. [Telkom University](https://repository.telkomuniversity.ac.id/pustaka/files/195647/abstraksi/sistem-pengambilan-keputusan-transaksi-saham-menggunakan-analisis-bandarmologi-berbasis-web.pdf)).
- **Jebakan:** satu broker = ribuan nasabah; data bisa disalahartikan; "bandar" juga bisa distribusi ke ritel.

### 6.10 Mean Reversion Intraday

- **Ide:** Pergerakan ekstrem jangka sangat pendek akibat ketidakseimbangan likuiditas cenderung berbalik (Heston dkk., 2010: reversal < 1 jam).
- **Cara pakai:** Harga jauh dari VWAP (mis. > 2 deviasi standar) tanpa berita → spekulasi kembali ke VWAP, dengan stop ketat.
- **Jebakan:** di hari tren/berita, mean reversion = "menangkap pisau jatuh".

### 6.11 Scalping & Ekonomi Fraksi Harga

- **Ide:** Mengambil 1–3 tick berulang kali di saham sangat likuid.
- **Hitung dulu:** di IDX biaya pulang-pergi umum sekitar **0,15% beli + 0,25% jual (sudah termasuk PPh final 0,1% saat jual)** ≈ **0,4%** ([Ajaib – biaya](https://ajaib.co.id/biaya); [Hukumonline](https://www.hukumonline.com/klinik/a/4-aspek-perpajakan-dalam-transaksi-saham-lt5b7e9044e2d9d/)). Contoh:
  - Saham Rp9.000 dengan fraksi Rp25 → 1 tick = 0,28%. Untung 1 tick **belum menutup biaya** 0,4%.
  - Saham Rp180 dengan fraksi Rp1 → 1 tick = 0,56%. Butuh ≥ 1 tick hanya untuk impas, tapi saham murah biasanya lebih berisiko.
- **AS:** komisi banyak broker nol, tick USD 0,01 sangat kecil relatif terhadap harga → scalping lebih masuk akal secara biaya, tetapi persaingan dengan HFT sangat ketat.
- **Jebakan:** scalping di IDX dengan target < 1% hampir pasti tergerus biaya.

### 6.12 Strategi Sesi Penutupan

- **AS:** *Market-on-Close (MOC) imbalance* diumumkan bursa menjelang 16.00 ET; arus rebalancing indeks/ETF menciptakan pergerakan akhir hari (terkait penjelasan Gao dkk. tentang *infrequent rebalancing*).
- **Indonesia:** **pre-closing call auction 15.50–16.00 WIB** dengan *random closing*; harga penutupan dibentuk dari volume terbesar yang dapat dipertemukan. Sesi **post-closing** (±16.01–16.15) bertransaksi di harga penutupan ([Fortune IDN](https://www.fortuneidn.com/market/jam-perdagangan-bursa-00-fykp7-kl8qbd)).
- **Jebakan:** manipulasi harga penutupan (*marking the close*) adalah pelanggaran.

---

## 7. Manajemen Risiko & Matematika Trading

> Strategi apa pun dari Bagian 6 hanya bernilai jika **expectancy setelah biaya > 0** dan ukuran posisi membuat Anda tetap bertahan.

### 7.1 Konsep R (unit risiko)

`1R = jarak entry ke stop loss × jumlah lembar` = jumlah uang yang siap hilang per trade.

### 7.2 Expectancy

```
Expectancy (R) = (Win% × Rata-rata Untung dalam R) − (Loss% × Rata-rata Rugi dalam R)
```

Contoh: win rate 40%, rata-rata untung 2R, rata-rata rugi 1R
→ `0,4 × 2 − 0,6 × 1 = +0,2R per trade` (positif).
Jika biaya rata-rata = 0,3R per trade → expectancy bersih **−0,1R** (negatif). **Biaya mengubah strategi "bagus" menjadi merugi.**

### 7.3 Position Sizing (contoh Indonesia)

- Modal Rp100 juta, risiko per trade 1% = **Rp1 juta**.
- Entry Rp2.000, stop Rp1.940 → risiko Rp60/lembar.
- Jumlah lembar = 1.000.000 / 60 ≈ 16.666 lembar → **166 lot** (1 lot = 100 lembar) ≈ Rp33,2 juta nilai posisi.
- Jika stop terlalu dekat sehingga nilai posisi > modal, **perlebar stop yang logis atau kecilkan risiko**, jangan pakai margin berlebihan.

### 7.4 Aturan pengaman yang umum dipakai

| Aturan | Contoh |
|---|---|
| Risiko per trade | 0,5%–1% modal |
| Batas rugi harian (*daily stop*) | −2R s/d −3R atau −2% modal → berhenti trading hari itu |
| Batas trade per hari | mis. maksimal 3–5 setup A+ |
| Time stop | tutup posisi jika tidak bergerak dalam X menit |
| Tidak averaging down | menambah posisi rugi dilarang dalam day trading |
| Tidak membawa posisi intraday menginap | wajib, apalagi posisi IDSS (akan di-*forced buy* otomatis) |
| Hindari jam/kondisi berisiko | pengumuman data besar, saham UMA/suspensi, saham FCA |

### 7.5 Jurnal & Statistik

Catat setiap trade: tanggal, saham, setup, alasan entry, entry/stop/target, ukuran, hasil (R), biaya, emosi, screenshot. Setelah **≥ 50–100 trade**, hitung win rate, rata-rata R, expectancy bersih, max drawdown. Studi Brasil menunjukkan pengalaman saja tidak membuat lebih baik — **data** yang membuat lebih baik (atau menunjukkan kapan harus berhenti).

---

## 8. Perbandingan Aturan Main: AS vs Indonesia

| Aspek | Amerika Serikat | Indonesia (BEI) |
|---|---|---|
| **Jam reguler** | 09.30–16.00 ET; pre-market & after-hours tersedia; sesi malam 21.00–04.00 ET ditargetkan mulai 6 Des 2026 ([Jones Day](https://www.jonesday.com/en/insights/2026/09/nyse-and-nasdaq-move-to-23hour-trading-day-overnight-session-is-an-evolution-but-not-yet-a-revolution)) | Pre-opening 08.45–08.59; Sesi I 09.00–12.00 (Jumat s/d 11.30); Sesi II 13.30–15.49 (Jumat 14.00–15.49); pre-closing 15.50–16.00; post-closing ±16.01–16.15 WIB ([Bloomberg Technoz](https://www.bloombergtechnoz.com/detail-news/119339/jam-trading-saham-cek-panduan-lengkap-bursa-indonesia-2026/2)) |
| **Settlement** | T+1 (sejak 28 Mei 2024) | T+2 (sejak 2018); belum T+1 per laporan awal 2024 ([Bisnis.com](https://market.bisnis.com/read/20240101/7/1728507/bursa-amerika-terapkan-settlement-t1-bei-bakal-nyusul)) |
| **Aturan khusus day trader** | PDT/USD 25.000 **dihapus** (efektif 4 Jun 2026), diganti intraday margin real-time; broker boleh menetapkan syarat lebih ketat | Tidak ada aturan PDT; day trading tunai bisa dilakukan dengan modal kecil (1 lot) memanfaatkan T+2 |
| **Short selling** | Umum (perlu *locate*/pinjam saham; Reg SHO) | **Baru** sejak 1 Okt 2026: short selling & **IDSS** — tahap awal 2 AB (Ajaib Sekuritas, Semesta Indovest), 5 saham (ASII, BBCA, BREN, BUMI, INDF — satu sumber menyebut BRPT, cek daftar resmi), jaminan awal min. **Rp50 juta atau 50%** nilai transaksi (mana yang lebih tinggi), posisi IDSS **wajib ditutup hari yang sama** dengan *forced buy* otomatis; hingga 31 Des 2026 hanya investor individu domestik ([Investortrust](https://investortrust.id/market/118164/bei-mulai-terapkan-intraday-short-selling-ini-batas-transaksi-dan-risiko-bagi-investor); [Tempo](https://www.tempo.co/ekonomi/bei-terapkan-intraday-short-selling-dengan-manajemen-risiko-terukur-dan-menyeluruh-2299727); [Metro TV](https://www.metrotvnews.com/read/NA0Czqm2-bei-terapkan-intraday-short-selling-investor-wajib-siapkan-rp50-juta)) |
| **Batas harga harian** | Tidak ada batas harian tetap; ada **LULD** (jeda per saham) dan **market-wide circuit breaker** 7%/13%/20% S&P 500 *(aturan umum)* | **ARA/ARB**: ARA 35% (Rp15–200), 25% (>Rp200–5.000), 20% (>Rp5.000); **ARB asimetris 7%** sejak 19 Okt 2026; untuk Rp11–14 ARB Rp1 (20 Okt–31 Des 2026) ([Bareksa](https://www.bareksa.com/berita/saham/2026-10-20/bei-ubah-lagi-aturan-arb-mulai-20-oktober-saham-rp11rp14-dibatasi-turun-rp1); [Bisnis.com](https://market.bisnis.com/read/20261019/7/2013755/bei-terapkan-arb-asimetris-7-jaga-ihsg-usai-pengumuman-msci)) |
| **Trading halt indeks** | Circuit breaker S&P 500 | IHSG turun > 8% → halt 30 menit; > 15% → halt 30 menit lagi; > 20% → trading suspend ([Bisnis.com](https://market.bisnis.com/read/20261016/7/2013109/ihsg-anjlok-8-picu-trading-halt-simak-aturannya)) |
| **Tick size** | USD 0,01 (saham ≥ USD 1) | Fraksi harga berjenjang (umumnya Rp1 untuk < Rp200, Rp2, Rp5, Rp10, hingga Rp25 untuk ≥ Rp5.000 — cek ketentuan terbaru BEI); harga minimum **Rp1** sejak 28 Sep 2026 ([Cermati](https://invest.cermati.com/artikel/perubahan-harga-minimum-saham-dan-batas-auto-rejection)) |
| **Satuan transaksi** | 1 lembar (bahkan pecahan di sebagian broker) | 1 lot = 100 lembar |
| **Biaya** | Banyak broker komisi nol; ada biaya regulator kecil, spread, slippage, *payment for order flow* | Fee broker ±0,15% beli / ±0,25% jual (termasuk levy, PPN, PPh final 0,1% saat jual) ([Ajaib](https://ajaib.co.id/biaya); [Brights](https://www.brights.id/id/blog/biaya-transaksi-saham)) |
| **Pajak** | Warga AS: *short-term capital gain* dikenai tarif pajak penghasilan biasa; ada *wash-sale rule*. Investor Indonesia di saham AS: aturan berbeda (perjanjian pajak), konsultasikan ke ahli pajak | **PPh final 0,1%** dari nilai jual bruto — tetap dipungut walau transaksi rugi |
| **Papan/peringatan khusus** | OTC/pink sheets berisiko tinggi | UMA, suspensi, notasi khusus, Papan Pemantauan Khusus (*Full Call Auction*) ([Investasiku](https://www.investasiku.id/eduvest/saham/unusual-market-activity); [Help Bions – FCA](https://help.bions.id/docs/full-call-auction/)) |
| **Regulator** | SEC, FINRA | OJK, BEI (SRO), KPEI, KSEI |

**Implikasi praktis:**
- Di **AS**, biaya eksplisit rendah dan ada short selling sejak lama → strategi dua arah (long/short) dan scalping lebih memungkinkan; tantangannya kompetisi dengan algoritma dan risiko leverage.
- Di **Indonesia**, biaya pulang-pergi ±0,4% dan fraksi harga relatif besar → target profit per trade harus jauh lebih besar dari biaya; strategi short baru bisa di sedikit saham via IDSS; ARA/ARB mengubah dinamika (antrian ARA/ARB, risiko tidak bisa keluar saat ARB).

---

## 9. Kondisi Terkini (Oktober 2026) & Implikasinya

### Indonesia
- **Gejolak besar IHSG.** Pada 15 Okt 2026 MSCI membuka konsultasi untuk mereklasifikasi Indonesia dari *Emerging Market* menjadi *Standalone Market* dengan sorotan transparansi kepemilikan dan dugaan perdagangan terkoordinasi. IHSG dilaporkan anjlok 11,57% pada 16 Okt 2026 (trading halt terpicu) dan masih tertekan pada 19 Okt; konsultasi MSCI berlangsung hingga 30 April 2027 ([Bisnis.com](https://market.bisnis.com/read/20261019/7/2013755/bei-terapkan-arb-asimetris-7-jaga-ihsg-usai-pengumuman-msci); [Bareksa](https://www.bareksa.com/berita/saham/2026-10-19/bei-minta-klarifikasi-msci-arb-7-redam-kepanikan-namun-ihsg-masih-turun-5)). Trading halt juga terjadi pada 28–29 Januari 2026 ([Republika](https://en.republika.co.id/berita/t9kgo7502/ihsg-drops-8-triggering-trading-halt-as-msci-flags-market)).
- **ARB asimetris 7%** (19 Okt 2026) dan penyesuaian ARB Rp1 untuk saham Rp11–14 (20 Okt–31 Des 2026).
- **Short selling & IDSS** baru berjalan sejak 1 Okt 2026 — likuiditas, kuota per anggota bursa, dan daftar saham masih terbatas.
- **OJK sedang mengevaluasi Full Call Auction** di Papan Pemantauan Khusus ([Asatunews](https://www.asatunews.co.id/ojk-evaluasi-aturan-full-call-auction)).

**Implikasi untuk day trader di IDX:**
1. Volatilitas sangat tinggi = peluang **dan** risiko ekstrem; kecilkan ukuran posisi.
2. ARB 7% mempercepat saham "mentok bawah" → risiko **tidak bisa keluar** (antrian jual menumpuk).
3. Risiko **trading halt** di tengah sesi → posisi bisa "terkunci".
4. Aturan bisa berubah dalam hitungan hari → baca pengumuman BEI setiap pagi.

### Amerika Serikat
- **PDT dihapus** (4 Juni 2026) → akun kecil boleh day trading lebih sering, namun leverage intraday mengikuti margin real-time; broker bisa memberlakukan aturan sendiri ([TradeZero](https://tradezero.com/en-us/blog/the-usd25-000-day-trading-minimum-is-gone-here-s-what-it-means-for-you); [QuantInsti](https://www.quantinsti.com/articles/finra-pdt-rule-removal-2026/)).
- **23/5 trading** (target 6 Des 2026): sesi malam tumpang tindih dengan jam siang Indonesia (21.00–04.00 ET ≈ 09.00–16.00 WIB saat ET berstatus standar time), tetapi likuiditasnya kemungkinan tipis — spread lebih lebar.
- **Risiko baru:** hilangnya "rem" PDT berpotensi meningkatkan overtrading pada pemula; riset Barber–Odean dan studi Taiwan/Brasil tetap relevan.

---

## 10. Kerangka Rutin Harian & Template Trading Plan

### 10.1 Rutin harian (contoh untuk IDX)

| Waktu (WIB) | Aktivitas |
|---|---|
| 07.30–08.30 | Cek berita global (Wall Street semalam, komoditas, kurs), pengumuman BEI (UMA, suspensi, perubahan aturan), keterbukaan informasi emiten |
| 08.30–08.45 | Susun watchlist 3–5 saham *in play*: katalis, level kunci (high/low/close kemarin), rencana entry–stop–target |
| 08.45–08.59 | Pantau pre-opening (indikasi harga pembukaan & volume) |
| 09.00–10.00 | Jendela utama (volume tertinggi): ORB, gap strategy, VWAP |
| 10.00–12.00 | Lebih selektif; kelola posisi yang ada |
| 13.30–15.00 | Volume biasanya lebih rendah; hindari overtrading |
| 15.00–15.49 | Intraday momentum, persiapan tutup semua posisi |
| 15.50–16.00 | Pre-closing: hanya jika strategi memang dirancang untuk call auction |
| Setelah tutup | Isi jurnal, evaluasi R & biaya, catat pelajaran |

### 10.2 Template trading plan (salin & isi)

```markdown
## Trading Plan — [Tanggal]
- Kondisi pasar: [trend / range / volatil] | Berita penting: [...]
- Batas rugi harian: Rp[...] (= [..]R) | Maks trade: [..]
- Watchlist:
  | Kode | Katalis | Level kunci | Setup | Entry | Stop | Target | Lot |
  |------|---------|-------------|-------|-------|------|--------|-----|
- Aturan wajib: tidak averaging down; stop dipasang saat entry; berhenti jika batas rugi tercapai.

## Review
- Hasil (R) & biaya: [...]
- Apakah semua trade sesuai rencana? [ya/tidak — kenapa]
- Pelajaran: [...]
```

---

## 11. Rambu Hukum & Etika

- **Manipulasi pasar dilarang** di kedua negara: *pump & dump*, *spoofing/layering*, *wash trade*, *marking the close*, penyebaran informasi menyesatkan ("pom-pom" terkoordinasi). Di Indonesia diatur UU Pasar Modal (UU No. 8/1995 sebagaimana diubah UU No. 4/2023 tentang P2SK); di AS oleh Securities Exchange Act 1934 & aturan SEC/FINRA *(pengetahuan umum)*.
- **Insider trading** dilarang.
- **Waspadai "guru trading" & grup sinyal berbayar** yang menjanjikan profit pasti; cek legalitas di OJK.
- **Gunakan broker resmi** (diawasi OJK untuk Indonesia; FINRA/SEC untuk AS). Untuk akses saham AS dari Indonesia, pastikan status perizinan platform.
- FINRA sendiri mengingatkan day trading "berisiko dan mungkin tidak cocok" untuk nasabah dengan sumber daya, pengalaman, atau toleransi risiko terbatas, serta rugi bisa melebihi modal awal jika memakai margin ([FINRA Reg. Notice 24-13](https://www.finra.org/rules-guidance/notices/24-13)).

---

## 12. Daftar Bacaan yang Disarankan

**Urutan belajar yang disarankan:** (1) psikologi & bukti empiris → (2) mikrostruktur & aturan bursa → (3) satu–dua setup → (4) manajemen risiko & jurnal → (5) paper trading/akun kecil.

### Buku klasik & praktisi
1. Edwin Lefèvre — *Reminiscences of a Stock Operator* (1923) — gratis di [Project Gutenberg](https://www.gutenberg.org/ebooks/60979)
2. Richard D. Wyckoff — *Studies in Tape Reading* (1910)
3. Jesse Livermore — *How to Trade in Stocks* (1940)
4. Edwards & Magee — *Technical Analysis of Stock Trends*
5. Steve Nison — *Japanese Candlestick Charting Techniques*
6. Toby Crabel — *Day Trading with Short Term Price Patterns and Opening Range Breakout* (1990)
7. Linda Raschke & Larry Connors — *Street Smarts*
8. James Dalton — *Mind Over Markets* (Market Profile)
9. Al Brooks — *Trading Price Action Trends*
10. Andrew Aziz — *How to Day Trade for a Living*
11. Mark Douglas — *Trading in the Zone*
12. Brett Steenbarger — *The Psychology of Trading* / *The Daily Trading Coach*
13. Van K. Tharp — *Trade Your Way to Financial Freedom* (expectancy & position sizing)
14. Larry Harris — *Trading and Exchanges* (mikrostruktur, tingkat lanjut)

### Konteks Indonesia
15. Ellen May — *Smart Traders Not Gamblers* dan *Smart Trader Rich Investor* ([Gramedia](https://www.gramedia.com/products/smart-trader-rich-investor-cover-baru))
16. Materi edukasi resmi: Sekolah Pasar Modal BEI & modul edukasi OJK ([idx.co.id](https://www.idx.co.id); [sikapiuangmu.ojk.go.id](https://sikapiuangmu.ojk.go.id))

### Paper akademik inti
17. Barber & Odean (2000) — *Trading Is Hazardous to Your Wealth*
18. Barber, Lee, Liu & Odean (2014) — *The Cross-Section of Speculator Skill*
19. Barber, Lee, Liu, Odean & Zhang (2020) — *Learning, Fast or Slow*
20. Chague, De-Losso & Giovannetti — *Day Trading for a Living?*
21. Gao, Han, Li & Zhou (2018) — *Market Intraday Momentum*
22. Heston, Korajczyk & Sadka (2010) — *Intraday Patterns in the Cross-Section of Stock Returns*
23. Zarattini & Aziz (2023); Zarattini, Barbon & Aziz (2024) — ORB
24. *Intraday Return of Winners vs Losers: Indonesian Capital Market Evidence* (2024)

---

## 13. Daftar Referensi

### Sejarah & latar belakang
- Jesse Livermore — https://en.wikipedia.org/wiki/Jesse_Livermore
- Bucket shop (stock market) — https://en.wikipedia.org/wiki/Bucket_shop_(stock_market)
- Reminiscences of a Stock Operator (Project Gutenberg) — https://www.gutenberg.org/ebooks/60979
- Studies in Tape Reading (IFA) — https://www.ifa.com/book-library/2154/studies_in_tape_reading
- Market Profile — https://en.wikipedia.org/wiki/Market_profile
- Understanding Market Profile (Traders.com) — https://store.traders.com/traderscom/-v07-c04-underst-pdf.html
- Toby Crabel — https://en.wikipedia.org/wiki/Toby_Crabel
- CNBC: How the Crash of '87 Gave Birth to HFT (SOES) — https://www.cnbc.com/id/39038914
- SOES Bandits (SuperMoney) — https://www.supermoney.com/encyclopedia/stock-bandit
- The Island ECN History — https://www.fundinguniverse.com/company-histories/the-island-ecn-inc-history/
- Schwab & May Day 1975 — https://www.aboutschwab.com/mss/story/the-action-that-forever-altered-investing
- Fortune (zero commission, 2019) — https://www.fortune.com/2019/10/03/zero-commissions-stock-trading-fees-as-brokerages-drop-wave-consolidation-follow/
- Volume-weighted average price — https://en.wikipedia.org/wiki/Volume-weighted_average_price

### Akademik
- Barber & Odean (2000) — https://faculty.haas.berkeley.edu/odean/papers/returns/Returns.html
- Barber, Lee, Liu & Odean — Cross-Section of Speculator Skill — https://www.escholarship.org/uc/item/7k75v0qx ; https://faculty.haas.berkeley.edu/odean/papers/day%20traders/Day%20Trading%20Skill%20110523.pdf
- Learning Fast or Slow (RAPS 2020) — https://ideas.repec.org/a/oup/rasset/v10y2020i1p61-93..html
- Chague, De-Losso & Giovannetti — Day Trading for a Living? — https://econpapers.repec.org/RePEc:fgv:eesptd:525 ; https://repositorio.fgv.br/items/e87d04fc-4b4c-4a56-ab5a-1c84c1afde1b/full
- Quantpedia: Retail Day Trading is an Uphill Battle — https://quantpedia.com/retail-day-trading-is-an-uphill-battle/
- CXO Advisory: Day Trading a Bust? — https://www.cxoadvisory.com/investing-expertise/day-trading-a-bust/
- Gao, Han, Li & Zhou — Market Intraday Momentum — https://profiles.wustl.edu/en/publications/market-intraday-momentum/
- Alpha Architect (ringkasan intraday momentum) — https://alphaarchitect.com/2014/08/attention-prop-traders-the-first-half-hour-of-trading-predicts-the-last-half-hour/
- Heston, Korajczyk & Sadka (2010) — https://www.kellogg.northwestern.edu/academics-research/research/detail/2010/intraday-patterns-in-the-cross-section-of-stock-returns ; https://ar5iv.arxiv.org/html/1005.3535
- Madhavan (2002) VWAP — https://www.smallake.kr/wp-content/uploads/2014/07/TP_Spring_2002_Madhavan.pdf
- Improving VWAP Strategies (Otago, 2006) — https://ourarchive.otago.ac.nz/bitstream/handle/10523/1540/ImprovingVWAPStrategiesADynamicalVolumeApproach2006.pdf?sequence=3
- ORB Stocks in Play (CXO Advisory) — https://www.cxoadvisory.com/individual-investing/intraday-trading-of-overactive-stocks-via-opening-range-breakout/
- Replikasi ORB (MQL5) — https://www.mql5.com/en/blogs/post/776235
- SEBI intraday study FY23 (Business Standard) — https://www.business-standard.com/markets/news/over-70-intra-day-traders-incur-losses-during-fy23-reveals-sebi-study-124072401110_1.html
- Intraday Return of Winners vs Losers: Indonesian Evidence — https://publisher.unimas.my/ojs/index.php/IJBS/article/view/7630
- Foreign vs Domestic Investors in Indonesia (MDPI IJFS) — https://www.mdpi.com/2227-7072/12/4/100
- Ekaputra & Dwijayanti — Trading halts IDX — https://ideas.repec.org/a/lpe/efijnl/200813.html
- Analisis Perilaku Investor Ritel (JACTA) — https://asianpublisher.id/journal/index.php/jacta/article/view/1030
- Herding & Broker Summary (Trisakti) — https://e-journal.trisakti.ac.id/index.php/mraai/article/view/9502
- Bandarmologi berbasis web (Telkom University) — https://repository.telkomuniversity.ac.id/pustaka/files/195647/abstraksi/sistem-pengambilan-keputusan-transaksi-saham-menggunakan-analisis-bandarmologi-berbasis-web.pdf
- Dampak Full Call Auction pada PPK (COSTING) — https://journal.ipm2kpe.or.id/index.php/COSTING/article/view/17666

### Regulasi & pasar AS
- Federal Register — FINRA Rule 4210 intraday margin — https://www.federalregister.gov/documents/2026/01/14/2026-00519/self-regulatory-organizations-financial-industry-regulatory-authority-inc-notice-of-filing-of-a
- FINRA weekly update (Jan 2026) — https://www.finra.org/compliance-tools/weekly-archive/01072026
- FINRA Regulatory Notice 24-13 — https://www.finra.org/rules-guidance/notices/24-13
- King & Spalding — FINRA adopts sweeping changes — https://www.kslaw.com/insights/articles/finra-adopts-sweeping-changes-to-margin-requirements-for-day-trading
- E*Trade — PDT rule change — https://us.etrade.com/knowledge/library/margin/pattern-day-trading-rule-change
- TradeStation — Good-Bye $25,000 — https://www.tradestation.com/insights/2026/05/06/day-trade-rule-change/
- TradeZero — The $25,000 minimum is gone — https://tradezero.com/en-us/blog/the-usd25-000-day-trading-minimum-is-gone-here-s-what-it-means-for-you
- QuantInsti — FINRA PDT removal 2026 — https://www.quantinsti.com/articles/finra-pdt-rule-removal-2026/
- tastytrade — Pattern Day Trading — https://tastytrade.com/learn/markets/industry/pattern-day-trading/
- Investor.gov — Margin bulletin — https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/margin
- Simpson Thacher — SEC approves Nasdaq 23/5 — https://www.stblaw.com/docs/default-source/memos/firmmemo_04_29_26
- Jones Day — NYSE & Nasdaq 23-hour day — https://www.jonesday.com/en/insights/2026/09/nyse-and-nasdaq-move-to-23hour-trading-day-overnight-session-is-an-evolution-but-not-yet-a-revolution
- WilmerHale — 23x5 trading — https://www.wilmerhale.com/en/insights/client-alerts/20260929-23x5-trading-comes-to-us-exchanges-what-firms-should-know-before-launch
- Troutman — Nasdaq 23-hour approval — https://www.troutman.com/insights/nasdaq-23-hour-equity-trading-proposal-approved-by-sec/
- LSEG — T+1 settlement — https://www.lseg.com/en/ftse-russell/research/market-index-impact-shorter-equity-settlement-cycles

### Regulasi & pasar Indonesia
- Investortrust — IDSS mulai berlaku — https://investortrust.id/market/118164/bei-mulai-terapkan-intraday-short-selling-ini-batas-transaksi-dan-risiko-bagi-investor
- Tempo — BEI terapkan IDSS — https://www.tempo.co/ekonomi/bei-terapkan-intraday-short-selling-dengan-manajemen-risiko-terukur-dan-menyeluruh-2299727
- Metro TV — IDSS jaminan Rp50 juta — https://www.metrotvnews.com/read/NA0Czqm2-bei-terapkan-intraday-short-selling-investor-wajib-siapkan-rp50-juta
- Kompas — BEI buka short selling — https://money.kompas.com/read/2026/10/03/072200526/bei-buka-short-selling-ini-modal-dan-risiko-yang-perlu-diketahui-investor
- Bisnis.com — ARB asimetris 7% & MSCI — https://market.bisnis.com/read/20261019/7/2013755/bei-terapkan-arb-asimetris-7-jaga-ihsg-usai-pengumuman-msci
- Bisnis.com — BEI pangkas ARB 7% — https://market.bisnis.com/read/20261019/7/2013651/bei-pangkas-batas-auto-rejection-bawah-arb-jadi-asimetris-7
- Bareksa — ARB Rp1 untuk saham Rp11–14 — https://www.bareksa.com/berita/saham/2026-10-20/bei-ubah-lagi-aturan-arb-mulai-20-oktober-saham-rp11rp14-dibatasi-turun-rp1
- Bareksa — BEI minta klarifikasi MSCI — https://www.bareksa.com/berita/saham/2026-10-19/bei-minta-klarifikasi-msci-arb-7-redam-kepanikan-namun-ihsg-masih-turun-5
- Kontan — BEI kembali ubah aturan ARB — https://investasi.kontan.co.id/news/breaking-news-bei-kembali-ubah-aturan-arb-ini-rinciannya
- Cermati — Harga minimum saham & auto rejection — https://invest.cermati.com/artikel/perubahan-harga-minimum-saham-dan-batas-auto-rejection
- Bisnis.com — Trading halt IHSG 8% (Okt 2026) — https://market.bisnis.com/read/20261016/7/2013109/ihsg-anjlok-8-picu-trading-halt-simak-aturannya
- Katadata — Ambang trading halt 8% (2025) — https://katadata.co.id/finansial/bursa/67f46ab19a26f/bei-naikan-ambang-batas-trading-halt-jadi-8
- Republika — Trading halt Januari 2026 — https://en.republika.co.id/berita/t9kgo7502/ihsg-drops-8-triggering-trading-halt-as-msci-flags-market
- Bloomberg Technoz — Jam perdagangan BEI 2026 — https://www.bloombergtechnoz.com/detail-news/119339/jam-trading-saham-cek-panduan-lengkap-bursa-indonesia-2026/2
- Fortune IDN — Jam perdagangan bursa — https://www.fortuneidn.com/market/jam-perdagangan-bursa-00-fykp7-kl8qbd
- Kontan — T+2 berlaku 2018 — https://investasi.kontan.co.id/news/aturan-t2-berlaku-mulai-semester-i-2018
- Bisnis.com — BEI & T+1 — https://market.bisnis.com/read/20240101/7/1728507/bursa-amerika-terapkan-settlement-t1-bei-bakal-nyusul
- ANTARA — PPK Full Periodic Call Auction — https://www.antaranews.com/berita/4027269/bei-implementasikan-papan-pemantauan-khusus-full-periodic-call-auction
- Help Bions — Full Call Auction — https://help.bions.id/docs/full-call-auction/
- Asatunews — OJK evaluasi FCA — https://www.asatunews.co.id/ojk-evaluasi-aturan-full-call-auction
- Investasiku — Unusual Market Activity — https://www.investasiku.id/eduvest/saham/unusual-market-activity
- IDX Channel/RCTI+ — Investor tembus 32 juta — https://www.rctiplus.com/news/detail/idxchannel/5493985/ojk-sebut-gen-z-dan-milenial-dominasi-pasar-modal--jumlah-investor-tembus-32-juta
- Bisnis.com — HUT ke-49 pasar modal, 30,30 juta SID — https://market.bisnis.com/read/20260810/7/1994994/hut-ke-49-pasar-modal-total-investor-tembus-3030-juta-sid
- The Diplomat — Indonesia's stock market sell-off explained — https://thediplomat.com/2026/02/indonesias-stock-market-sell-off-explained/
- Ajaib — Biaya transaksi — https://ajaib.co.id/biaya
- Hukumonline — Aspek perpajakan transaksi saham — https://www.hukumonline.com/klinik/a/4-aspek-perpajakan-dalam-transaksi-saham-lt5b7e9044e2d9d/
- Brights — Biaya transaksi saham — https://www.brights.id/id/blog/biaya-transaksi-saham
- Reku — Apa itu bandarmology — https://reku.id/campus/apa-itu-bandarmology
- Ajaib — Toolkit bandarmology — https://ajaib.co.id/belajar/jadi-trader-handal/toolkit-bandarmology-di-ajaib-terminal
- Ajaib — Strategi mengikuti foreign flow — https://ajaib.co.id/belajar/investasi/strategi-trading-mengikuti-foreign-flow
- Gramedia — Smart Traders Not Gamblers — https://www.gramedia.com/products/smart-traders-not-gamblers-cd-cover-baru

---

### Catatan Metodologi & Keterbatasan
- Riset dilakukan melalui penelusuran web pada 23 Oktober 2026. Sebagian data terbaru (aturan BEI Oktober 2026) bersumber dari media yang mengutip BEI/OJK, bukan dokumen SK asli — **verifikasi ke idx.co.id**.
- Ada perbedaan antar-sumber pada beberapa detail: daftar saham IDSS (BREN vs BRPT), angka benchmark upah pada studi Brasil (versi working paper vs SSRN), dan tanggal pasti peluncuran sesi malam AS (target, belum final).
- Butir bertanda *(pengetahuan umum)* adalah fakta yang lazim diketahui namun tidak diverifikasi ulang dalam penelusuran ini.
- Belum ditemukan studi publik berskala besar tentang profitabilitas day trader di BEI — ini celah riset yang menarik.
