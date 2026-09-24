#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Menulis satu file JSON per item riset (format/kasus desain) ke results/.

Isi diambil dari riset web & dokumen resmi (lihat field `sources` tiap item).
Nilai yang tidak dapat diverifikasi ditandai [uncertain] dan dicantumkan di array `uncertain`.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "results"

SEC = "https://www.sec.gov/Archives/edgar/data/829224/"
PR_Q4FY25 = SEC + "000082922425000074/sbux-09282025xexhibit991.htm"
PR_Q1FY26 = SEC + "000082922426000010/sbux-12282025xearningsrele.htm"
PR_Q2FY26 = SEC + "000082922426000078/sbux-03292026xearningsrele.htm"
TENK_FY25 = SEC + "000082922425000114/sbux-20250928.htm"
TENK_FY23 = SEC + "000082922423000058/sbux-20231001.htm"
JV_CLOSE = SEC + "000082922426000064/sbux-04022026xexhibit991.htm"
INVESTOR_2018 = "https://www.starbucks.com.cn/en/about/news/starbucks-first-ever-china-investor-conference/"

ITEMS = [
    {
        "basic_info": {
            "name": "Shanghai Reserve Roastery",
            "format_type": "Flagship imersif (Roastery)",
            "launch_period": "Desember 2017",
            "scale": "1 lokasi (HKRI Taikoo Hui, Shanghai); ~30.000 sq ft (~2.700 m2), Roastery pertama di Asia",
        },
        "design_attributes": {
            "size_and_layout": "~30.000 sq ft; area roasting terbuka, beberapa bar, bakery, retail merchandise; alur pengunjung dirancang sebagai 'teater kopi'.",
            "storefront_treatment": "Fasad dan interior mengekspos proses roasting (cask tembaga besar, dinding ukir); bangunan menjadi landmark yang dikunjungi, bukan sekadar dilewati.",
            "localization_elements": "Referensi kerajinan tembaga dan motif tradisional Tiongkok dipadukan dengan estetika industrial.",
        },
        "performance_metrics": {
            "performance_evidence": "CNBC (Jan 2018): setelah 8 minggu, penjualan harian Roastery ~2x rata-rata penjualan MINGGUAN gerai AS (~US$32 ribu/minggu); ticket rata-rata hari pertama ~US$29. Howard Schultz: 'We shattered every sales record in the history of the company.' Namun comp sales China turun menjadi -2% di Q3 FY2018 (dua kuartal setelah pembukaan), menunjukkan efek halo tidak otomatis mengangkat jaringan.",
            "evidence_strength": "Kuat untuk unit tunggal; lemah untuk efek ke jaringan",
        },
        "market_positioning": {
            "strategic_role": "Brand halo & legitimasi premium ('coffee authority') di pasar yang sedang mengedukasi budaya kopi.",
            "revenue_mechanism": "Ticket sangat tinggi + volume turis/destinasi; nilai utamanya adalah media & persepsi premium, bukan kontribusi pendapatan jaringan.",
        },
        "implications": {
            "design_implication": "Perlakukan flagship sebagai capex pemasaran: ukur dengan brand lift, share of voice sosial (Xiaohongshu/Douyin), dan ticket premium di gerai Reserve sekitarnya, bukan dengan P&L gerai semata.",
            "risks_limitations": "Data penjualan unit tunggal hanya dari pernyataan manajemen ke media; tidak ada data per-gerai resmi. Efek novelty memudar.",
            "sources": [
                "https://www.cnbc.com/2018/01/25/eight-weeks-in-starbucks-shanghai-roastery-is-raking-in-insane-sales.html",
                "https://stories.starbucks.com/asia/press/2017/starbucks-opens-state-of-the-art-premium-reserve-roastery-in-shanghai/",
                SEC + "000082922418000033/sbux-07012018xexhibit991.htm",
            ],
        },
    },
    {
        "basic_info": {
            "name": "Reserve Stores dan Reserve Bars",
            "format_type": "Premium (Reserve)",
            "launch_period": "2014-sekarang",
            "scale": "150+ Reserve Bar (Mei 2018, target 200 akhir FY2018); 800+ gerai Reserve & tematik (April 2026)",
        },
        "design_attributes": {
            "size_and_layout": "Bar Reserve di dalam gerai inti atau gerai Reserve penuh; metode seduh manual/alternatif sebagai titik fokus.",
            "storefront_treatment": "Signage Reserve ('R' bintang) dan material lebih gelap/premium; bar seduh ditempatkan terlihat dari muka gerai.",
            "localization_elements": "Varian per lokasi; flagship generasi baru 'Reserve 星意坊' di Beijing SKP (Sept 2026) memadukan kopi Reserve, patisserie Italia, dan merchandise eksklusif SKP.",
        },
        "performance_metrics": {
            "performance_evidence": "Tidak ada data penjualan terpisah untuk gerai Reserve di China. Manajemen JV (2026) menyatakan tidak akan memotong harga dan menjadikan kopi spesialis sebagai dasar premium merek.",
            "evidence_strength": "Tidak ada data publik",
        },
        "market_positioning": {
            "strategic_role": "Menjaga price ceiling & persepsi keahlian kopi di tengah perang harga (Luckin/Cotti di kisaran RMB 9,9).",
            "revenue_mechanism": "Ticket lebih tinggi dan mix produk premium; dampak pada ticket rata-rata jaringan belum terlihat (ticket comp negatif di 9 dari 10 kuartal Q1 FY24-Q2 FY26).",
        },
        "implications": {
            "design_implication": "Gerai Reserve adalah alat utama untuk memulihkan ticket. Uji apakah lapisan desain Reserve (bar seduh terlihat dari shopfront) menaikkan ticket di catchment premium, dengan kontrol gerai inti sekitarnya.",
            "risks_limitations": "Kanibalisasi antar-gerai Starbucks sendiri; ukuran gerai besar menaikkan sewa per unit.",
            "sources": [
                INVESTOR_2018,
                "https://news.qq.com/rain/a/20260916A0CGMJ00",
                "http://finance.sina.com.cn/jjxw/2026-04-08/doc-inhtuyvv6406966.shtml",
            ],
        },
    },
    {
        "basic_info": {
            "name": "Heritage Adaptive Reuse Stores",
            "format_type": "Lokalisasi arsitektur",
            "launch_period": "2000-an-sekarang; contoh unggulan 2019",
            "scale": "Puluhan gerai di bangunan/kawasan bersejarah [uncertain]; contoh: Starbucks Reserve Tianjin Riverside 66 (2019)",
        },
        "design_attributes": {
            "size_and_layout": "Mengikuti struktur bangunan lama; tata ruang menyesuaikan kolom, void, dan fasad cagar budaya.",
            "storefront_treatment": "Fasad bersejarah dipertahankan; signage Starbucks minimal dan tunduk pada karakter bangunan. Tianjin: bangunan bergaya Renaisans tahun 1921 di Riverside 66.",
            "localization_elements": "Material, ornamen, dan narasi sejarah lokal; memenangi Gold, Hong Kong Design Awards 2020 (Tianjin).",
        },
        "performance_metrics": {
            "performance_evidence": "Tidak ada data penjualan yang dipublikasikan. Bukti tidak langsung: statement Starbucks FY2016-2017 bahwa gerai China menghasilkan 'record AUVs' dan 'world-leading returns on investment' pada periode gerai berdesain lokal dan third place mendominasi portofolio.",
            "evidence_strength": "Lemah (anekdot & pernyataan manajemen)",
        },
        "market_positioning": {
            "strategic_role": "Legitimasi lokal (izin kawasan, goodwill pemerintah/komunitas) dan konten sosial media ('打卡' destinasi).",
            "revenue_mechanism": "Traffic destinasi & wisata; nilai PR dan akses lokasi premium yang sulit ditiru pesaing.",
        },
        "implications": {
            "design_implication": "Cocok sebagai 'anchor' kota, bukan template. Dokumentasikan biaya & waktu perizinan vs uplift traffic untuk keputusan investasi berikutnya.",
            "risks_limitations": "Capex & waktu pembangunan tinggi; tidak dapat diskalakan ke ribuan gerai.",
            "sources": [
                "https://stories.starbucks.com/asia/stories/2019/starbucks-preserves-heritage-site-in-china-to-open-flagship-location-in-tianjin/",
                "https://betterfutureawards.com/HKG20/project.asp?ID=20512",
                SEC + "000082922416000078/sbux-1022016xexhibit991.htm",
                SEC + "000082922417000033/sbux-722017xexhibit991.htm",
            ],
        },
    },
    {
        "basic_info": {
            "name": "ICH Themed Concept Stores",
            "format_type": "Lokalisasi budaya (warisan budaya takbenda)",
            "launch_period": "[uncertain] awal program; gerai ke-5 dibuka Agustus 2025",
            "scale": "5 gerai: Beijing, Shanghai, Suzhou, Nanjing, Hangzhou (Hefang Street, dibuka 29 Agustus 2025)",
        },
        "design_attributes": {
            "size_and_layout": "Gerai dengan area workshop/demonstrasi kerajinan; Hangzhou menempatkan alat tenun tangan di lantai 1.",
            "storefront_treatment": "Menempati bangunan komersial hampir seabad di Hefang Street; tekstil hangluo (kain sutra Hangzhou) dipakai sebagai instalasi yang terlihat dari luar.",
            "localization_elements": "Kerajinan takbenda (hangluo, tie-dye Bai, emboss kulit Mongolia Dalam) dikreasikan bersama perajin desa; program fase 3 (2025-2028) fokus Yunnan.",
        },
        "performance_metrics": {
            "performance_evidence": "Tidak ada data penjualan/traffic publik; komunikasi Starbucks menekankan dampak sosial (perajin, pemimpin perempuan desa).",
            "evidence_strength": "Tidak ada data publik",
        },
        "market_positioning": {
            "strategic_role": "Relevansi budaya & ESG; diferensiasi dari pesaing berbasis harga.",
            "revenue_mechanism": "Merchandise edisi khusus, minuman tematik, workshop berbayar; brand affinity jangka panjang.",
        },
        "implications": {
            "design_implication": "Pisahkan 'lapisan budaya' (material, kerajinan, cerita) dari 'kerangka' gerai agar bisa dimodulkan ke gerai kabupaten berbiaya rendah, sesuai strategi 千店千面.",
            "risks_limitations": "Sampel kecil (5 gerai); dampak sulit dipisahkan dari PR. Risiko dianggap 'cultural appropriation' bila kolaborasi tidak autentik.",
            "sources": [
                "https://stories.starbucks.com/asia/stories/2025/how-starbucks-intangible-cultural-heritage-themed-stores-in-china-empower-communities/",
                "https://english.news.cn/20250829/926124dbefdf4f1181bc1bc868c3a9e4/c.html",
                "https://www.ehangzhou.gov.cn/2025-09/01/c_294812.htm",
            ],
        },
    },
    {
        "basic_info": {
            "name": "Core Third Place Coffeehouse",
            "format_type": "Format inti (third place)",
            "launch_period": "1999-2019 (dominan), masih mayoritas portofolio",
            "scale": "Mayoritas dari 8.011 gerai (akhir FY2025) [uncertain proporsi pasti]",
        },
        "design_attributes": {
            "size_and_layout": "Relatif besar dengan banyak kursi untuk pelanggan yang berlama-lama; luas rata-rata gerai China tidak diungkap Starbucks.",
            "storefront_treatment": "Fasad kaca lebar, siren logo menonjol, visibilitas interior (orang duduk) sebagai sinyal sosial.",
            "localization_elements": "Terbatas; standar global dengan penyesuaian interior per kota.",
        },
        "performance_metrics": {
            "performance_evidence": "FY2016: Starbucks menyebut China mencetak 'Record AUV's, ROI and Profitability'. Sejak itu pendapatan per gerai rata-rata turun dari RMB 5,17 juta (FY2019) ke RMB 2,92 juta (FY2025), -43%. Isu 2025: keluhan 'third place' (kursi dipakai non-pembeli) sementara pesanan delivery menumpuk di counter.",
            "evidence_strength": "Sedang (data agregat resmi; atribusi ke desain tidak langsung)",
        },
        "market_positioning": {
            "strategic_role": "Dasar premium harga Starbucks China ('menyewakan sofa', Quartz 2013); laporan CCTV Okt 2013: latte di Beijing 27 yuan, ~1/3 lebih mahal dari Chicago.",
            "revenue_mechanism": "Harga premium dibenarkan oleh ruang; tetapi sewa & luas per gerai tinggi sehingga pendapatan per m2 rendah dibanding format pickup.",
        },
        "implications": {
            "design_implication": "Re-desain third place untuk era hibrida: zona duduk + jalur pickup/rider terpisah di shopfront, sehingga ruang tidak dikorbankan oleh delivery. Ini paralel dengan program 'coffeehouse uplift' Starbucks AS (1.000+ remodel FY2026).",
            "risks_limitations": "Tidak ada data luas gerai rata-rata China; penurunan per gerai juga dipengaruhi COVID, perang harga, dan ekspansi tier bawah.",
            "sources": [
                "https://qz.com/125138/in-china-starbucks-doesnt-sell-coffee-to-make-its-millions-it-rents-couches",
                "https://www.cnbc.com/2013/10/21/starbucks-under-fire-in-china-over-high-prices.html",
                SEC + "000082922416000078/sbux-1022016xexhibit991.htm",
                "https://finance.biggo.com/news/f1823dac-b7c7-4061-8fd2-ce52ee7fe763",
                TENK_FY25,
            ],
        },
    },
    {
        "basic_info": {
            "name": "Starbucks Now Express Format",
            "format_type": "Konvenien / digital-first",
            "launch_period": "Juli 2019 (gerai pertama, Beijing)",
            "scale": "Jumlah gerai format ini tidak diungkap [uncertain]; layanan mobile order 'Starbucks Now' di 1.300+ gerai empat kota (Juli 2019)",
        },
        "design_attributes": {
            "size_and_layout": "Kecil, 1-2 barista, beberapa stool; berfungsi juga sebagai pusat dispatch delivery dalam radius tertentu.",
            "storefront_treatment": "Minimalis; 'pickup portal' di dinding yang dapat diakses pelanggan & kurir; concierge counter.",
            "localization_elements": "Minim; fokus fungsi.",
        },
        "performance_metrics": {
            "performance_evidence": "Tidak ada data per gerai. Konteks: comp transactions China -2% (Q1 FY2019) dan -1% (Q2 FY2019) sebelum peluncuran; 10-K FY2023 menyebut format ini untuk 'seamless integration of physical and digital'.",
            "evidence_strength": "Lemah",
        },
        "market_positioning": {
            "strategic_role": "Respons defensif terhadap model pickup Luckin; menangkap okasi on-the-go & delivery.",
            "revenue_mechanism": "Throughput tinggi, capex & sewa rendah; ticket cenderung lebih rendah.",
        },
        "implications": {
            "design_implication": "Format konvenien menurunkan pendapatan per gerai rata-rata tetapi dapat menaikkan ROI; jangan dinilai dengan KPI gerai third place. Shopfront harus dirancang untuk kecepatan (antrian, visibilitas status pesanan, akses rider).",
            "risks_limitations": "Mengaburkan diferensiasi Starbucks bila terlalu dominan; bersaing langsung di arena harga.",
            "sources": [
                "https://www.nrn.com/news/starbucks-opens-first-express-store-format-china",
                "https://www.retail-insight-network.com/news/starbucks-now-store-beijing-china/",
                TENK_FY23,
            ],
        },
    },
    {
        "basic_info": {
            "name": "County Level and Lower Tier Stores",
            "format_type": "Ekspansi geografis (tier 3 ke bawah)",
            "launch_period": "FY2023-sekarang (akselerasi FY2024)",
            "scale": "166 pasar county baru di FY2024 (~1.000 total); 1.103 county-level city (Q1 FY2026); target 1.500+ dalam 3 tahun (~170/tahun); ~setengah gerai baru di tier bawah",
        },
        "design_attributes": {
            "size_and_layout": "Umumnya format inti yang lebih ramping [uncertain]; strategi 2026 memakai kombinasi format fleksibel.",
            "storefront_treatment": "Shopfront standar Starbucks sebagai penanda 'merek internasional' di kota kecil.",
            "localization_elements": "Menu & kampanye lokal; sedikit kustomisasi arsitektur.",
        },
        "performance_metrics": {
            "performance_evidence": "China Daily (Okt 2024) mengutip analis: sewa & biaya tenaga kerja lebih rendah memberi margin relatif lebih besar; tidak ada angka resmi. Secara agregat, pertumbuhan gerai +94% (FY2019-FY2025) hanya menghasilkan pendapatan RMB +15,5%.",
            "evidence_strength": "Sedang (agregat) / lemah (per gerai)",
        },
        "market_positioning": {
            "strategic_role": "Mesin pertumbuhan jumlah gerai menuju aspirasi 20.000 gerai JV.",
            "revenue_mechanism": "Pendapatan tumbuh via footprint; produktivitas per gerai lebih rendah namun biaya lebih rendah.",
        },
        "implications": {
            "design_implication": "Butuh 'kit desain' modular berbiaya rendah dengan lapisan lokal, serta disiplin site selection (visibilitas shopfront, frontage) karena di kota kecil shopfront adalah media iklan utama.",
            "risks_limitations": "Kanibalisasi & penurunan AUV; data per tier tidak diungkap.",
            "sources": [
                "https://www.chinadaily.com.cn/a/202410/31/WS67231b00a310f1265a1caab8.html",
                "https://global.chinadaily.com.cn/a/202601/30/WS697c02a0a310d6866eb368ab.html",
                "https://www.chinadaily.com.cn/a/202604/08/WS69d647e6a310d6866eb424b0.html",
                PR_Q4FY25,
            ],
        },
    },
    {
        "basic_info": {
            "name": "IP Themed Storefront Takeovers",
            "format_type": "Tematik / temporer",
            "launch_period": "Berulang; contoh Q1 FY2026 (Okt-Des 2025)",
            "scale": "38 gerai bertema Harry Potter (Q1 FY2026); 194.000 'tongkat sihir' terdistribusi dalam satu minggu",
        },
        "design_attributes": {
            "size_and_layout": "Overlay dekorasi pada gerai yang ada.",
            "storefront_treatment": "Fasad, jendela, dan interior diubah sementara menjadi set tematik; sangat 'shareable'.",
            "localization_elements": "IP global dikurasi untuk konsumen muda China.",
        },
        "performance_metrics": {
            "performance_evidence": "Q1 FY2026: comp sales China +7% (transaksi +5%, ticket +2%) - kuartal terbaik sejak Q1 FY2024 dan satu-satunya kuartal dengan ticket positif dalam rentang Q4 FY2023-Q2 FY2026. CFO mengaitkannya dengan inovasi produk, marketing efektif, dan delivery; kolaborasi IP disebut oleh CTR Market Research.",
            "evidence_strength": "Sedang (korelasi waktu, banyak faktor bersamaan)",
        },
        "market_positioning": {
            "strategic_role": "Pemicu kunjungan (traffic) dan pembelian merchandise berharga lebih tinggi.",
            "revenue_mechanism": "Traffic + ticket (bundle merchandise).",
        },
        "implications": {
            "design_implication": "Shopfront sebagai 'media' yang dapat diprogram: siapkan sistem fasad modular (panel, window box, lighting) yang dapat diganti per kampanye dengan biaya rendah dan diukur per gerai (treatment vs kontrol).",
            "risks_limitations": "Efek sementara; tidak bisa dipisahkan dari kampanye produk & harga pada kuartal yang sama.",
            "sources": [
                "https://global.chinadaily.com.cn/a/202601/30/WS697c02a0a310d6866eb368ab.html",
                PR_Q1FY26,
            ],
        },
    },
    {
        "basic_info": {
            "name": "Qian Dian Qian Mian Micro Formats",
            "format_type": "Portofolio format JV (千店千面 - 'seribu gerai, seribu wajah')",
            "launch_period": "April 2026-sekarang (pasca penutupan JV Starbucks-Boyu 2 April 2026)",
            "scale": "8.238 gerai per 15 Sept 2026 (+227 neto FY2026; 69 county baru); format dari 10 m2 hingga 800+ gerai Reserve & tematik",
        },
        "design_attributes": {
            "size_and_layout": "Gerai 10 m2 di area wisata, convenience store modular di gedung kantor, kereta kopi di konser, gerai rumah sakit, hingga flagship Reserve (SKP Beijing).",
            "storefront_treatment": "Beragam; dari kios/cart tanpa fasad hingga flagship berdesain khusus.",
            "localization_elements": "'Hyper-localization' (CEO Molly Liu); 'satu gerai satu komunitas'.",
        },
        "performance_metrics": {
            "performance_evidence": "Belum ada data kinerja per format. Posisi harga: 'tidak menurunkan harga'. Starbucks menilai total nilai bisnis ritel China > US$13 miliar (EV transaksi ~US$4 miliar untuk 60%).",
            "evidence_strength": "Belum ada data (strategi baru)",
        },
        "market_positioning": {
            "strategic_role": "Menjangkau okasi & lokasi yang tidak ekonomis untuk format third place; menuju aspirasi 20.000 gerai.",
            "revenue_mechanism": "Footprint & okasi baru dengan capex per unit rendah; flagship untuk menjaga premium.",
        },
        "implications": {
            "design_implication": "Desain berubah dari 'satu standar' menjadi 'sistem portofolio'. Diperlukan design governance dalam model licensed (standar merek, review desain, klausul berbagi data kinerja per format).",
            "risks_limitations": "Konsistensi merek dapat terfragmentasi; Starbucks kini licensor (40%) sehingga kendali langsung atas desain berkurang.",
            "sources": [
                "https://news.qq.com/rain/a/20260916A0CGMJ00",
                "http://finance.sina.com.cn/jjxw/2026-04-08/doc-inhtuyvv6406966.shtml",
                "https://c.m.163.com/news/a/KQ2ORQGL05198NMR.html",
                JV_CLOSE,
                SEC + "000082922425000079/a20251103-form8xkxex991.htm",
            ],
        },
    },
    {
        "basic_info": {
            "name": "Luckin Pickup Store Benchmark",
            "format_type": "Kompetitor (pickup-first)",
            "launch_period": "2017-sekarang",
            "scale": "31.048 gerai (31 Des 2025; 20.234 self-operated, 10.814 partnership); 99,1% self-operated adalah pickup store",
        },
        "design_attributes": {
            "size_and_layout": "Pickup store umumnya 20-60 m2 dengan kursi terbatas; 'relax store' >120 m2 untuk branding (2,4% gerai pada 2022). Feb 2026: gerai high-end pertama (dilaporkan ~420 m2).",
            "storefront_treatment": "Fasad sempit, brand biru, fokus pada titik pickup; desain sebagai alat efisiensi, bukan pengalaman.",
            "localization_elements": "Minim.",
        },
        "performance_metrics": {
            "performance_evidence": "Pendapatan 2025 RMB 49,3 miliar (+43%), 2,16x pendapatan Starbucks China FY2025 (~RMB 22,8 miliar). Pendapatan per gerai rata-rata ~RMB 1,85 juta (understated karena pendapatan partnership) vs Starbucks ~RMB 2,92 juta. Margin level gerai self-operated 17,8% (2025). Pangsa pasar Starbucks China turun dari 34% (2019) ke 14% (2024) menurut Euromonitor.",
            "evidence_strength": "Kuat (data resmi 20-F)",
        },
        "market_positioning": {
            "strategic_role": "Pemimpin volume & harga; menggeser ekspektasi konsumen ke kopi sebagai komoditas harian.",
            "revenue_mechanism": "Volume tinggi, sewa & dekorasi rendah, ekspansi cepat.",
        },
        "implications": {
            "design_implication": "Starbucks tidak dapat menang dengan meniru format Luckin secara penuh; nilai desain Starbucks adalah justifikasi harga. Namun pergerakan Luckin ke gerai high-end (2026) menandakan konvergensi: keduanya membangun portofolio format.",
            "risks_limitations": "Definisi pendapatan berbeda (Luckin mencatat penjualan material ke mitra); ukuran gerai Starbucks China tidak diungkap sehingga perbandingan per m2 hanya ilustratif.",
            "sources": [
                "https://www.sec.gov/Archives/edgar/data/1767582/000110465926035712/lk-20251231x20f.htm",
                "https://www.sec.gov/Archives/edgar/data/1767582/000110465923042448/lk-20221231x20f.htm",
                "https://www.cnbc.com/2026/02/08/chinas-luckin-coffee-opens-its-first-high-end-store.html",
                "https://finance.yahoo.com/news/analysis-starbuckss-china-comeback-relies-000443589.html",
            ],
        },
    },
]


def slugify(name):
    return re.sub(r"[^A-Za-z0-9_]", "", name.replace(" ", "_"))


def find_uncertain(obj, prefix=""):
    found = []
    for k, v in obj.items():
        if isinstance(v, dict):
            found += find_uncertain(v)
        elif isinstance(v, str) and "[uncertain]" in v:
            found.append(k)
    return found


def main():
    OUT.mkdir(exist_ok=True)
    for item in ITEMS:
        # Struktur datar (didukung validate_json.py & research-report): field langsung di level atas
        flat = {k: v for category in item.values() for k, v in category.items()}
        flat["uncertain"] = find_uncertain(item)
        path = OUT / f"{slugify(flat['name'])}.json"
        path.write_text(json.dumps(flat, ensure_ascii=False, indent=2), encoding="utf-8")
        print(path.name, "uncertain:", flat["uncertain"])


if __name__ == "__main__":
    main()
