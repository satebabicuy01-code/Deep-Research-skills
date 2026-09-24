#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Menulis satu file JSON (struktur datar) per tuas desain fasad ke results/.

Setiap klaim merujuk ke sumber di field `sources`. Nilai yang tidak dapat
diverifikasi ditandai [uncertain] dan dicantumkan di array `uncertain`.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "results"

GEHL = "https://doi.org/10.1057/palgrave.udi.9000162"
GEHL_PDF = "https://www.urbaplan.ch/wp-content/uploads/2015/02/jangehl_urbandesign_article-1.pdf"

ITEMS = [
    {
        "name": "Window Display",
        "lever_type": "Konten fasad",
        "funnel_stage": "Perhatian -> masuk toko (capture rate); citra toko",
        "key_evidence": (
            "Lange, Rosengren & Blom (2016, J. Business Research): studi lapangan kuasi-eksperimen di jalan belanja fashion "
            "(n = 1.834 pejalan) + eksperimen online (n = 480). Etalase yang lebih kreatif lebih berhasil mengubah pejalan "
            "menjadi pengunjung toko; efeknya dimediasi sikap terhadap etalase, keyakinan tentang produk, dan persepsi "
            "usaha peritel, serta dimoderasi frekuensi belanja. Oh & Petrie (2012, JRCS): efektivitas display produk vs "
            "artistik bergantung pada motif belanja (membeli vs rekreasi) dan beban kognitif. Cornelius, Natter & Faure "
            "(2010, JRCS): display yang lebih inovatif menghasilkan penilaian citra lebih baik, dan citra toko ikut "
            "terangkat oleh keberadaan display. Sen, Block & Chandran (2002, JRCS): informasi di etalase dipakai konsumen "
            "dalam keputusan masuk dan membeli."
        ),
        "effect_size": "Arah positif dan signifikan untuk masuk toko (Lange dkk.); besaran persen tidak tersedia di abstrak.",
        "evidence_type": "Eksperimen lapangan + eksperimen online/lab",
        "evidence_strength": "Sedang-kuat (untuk capture rate); tidak mengukur penjualan langsung",
        "productivity_metric": "Capture rate (masuk / pejalan lewat) per jam; dwell di depan etalase; konversi pengunjung baru.",
        "design_guidelines": (
            "Perlakukan etalase sebagai media yang dirotasi (kreatif, bukan sekadar tumpukan produk). Sesuaikan jenis "
            "display dengan motif lokasi: display produk di lokasi 'misi' (kantor, transit), display artistik di lokasi "
            "rekreasi (mal akhir pekan, high street). Uji setiap konsep dengan kontrol."
        ),
        "risks_limitations": "Studi mayoritas fashion/apparel; efek kreativitas bisa memudar (novelty); pengunjung tambahan belum tentu membeli.",
        "sources": [
            "https://doi.org/10.1016/j.jbusres.2015.08.013",
            "https://ideas.repec.org/a/eee/jbrese/v69y2016i3p1014-1021.html",
            "https://doi.org/10.1016/j.jretconser.2011.08.003",
            "https://doi.org/10.1016/j.jretconser.2009.11.004",
            "https://doi.org/10.1016/S0969-6989(01)00037-6",
        ],
    },
    {
        "name": "Facade Transparency",
        "lever_type": "Arsitektur fasad",
        "funnel_stage": "Perhatian & daya tarik -> niat mendekat",
        "key_evidence": (
            "Kalantari, Xu, Govani & Mostafavi (2022, JRCS): eksperimen virtual reality yang hanya mengubah transparansi "
            "etalase. Etalase sangat transparan dinilai lebih menarik dan diamati lebih lama, dimediasi oleh kompleksitas "
            "visual yang lebih rendah dan rasa senang yang lebih tinggi. TIDAK ada perbedaan signifikan pada perilaku "
            "mendekat (peserta tahu mereka tidak bisa masuk toko VR). Gehl dkk. (2006) mengutip studi Gil Lopez (Madrid): "
            "kaca pada ~63% panjang fasad sebagai pedoman fasad yang hidup."
        ),
        "effect_size": "Daya tarik & durasi observasi naik (signifikan); perilaku mendekat tidak berbeda signifikan.",
        "evidence_type": "Eksperimen VR (lab) + pedoman urban design",
        "evidence_strength": "Sedang (lab; belum ada bukti penjualan)",
        "productivity_metric": "Waktu tatap/berhenti di depan toko, capture rate, konversi.",
        "design_guidelines": (
            "Jaga garis pandang ke interior dari jalur pejalan (hindari etalase tertutup penuh/film gelap). "
            "Targetkan porsi kaca tinggi pada lantai dasar; tata display agar tidak menambah kerumitan visual."
        ),
        "risks_limitations": "Hasil VR; transparansi menuntut interior yang rapi (back-of-house terlihat = negatif); isu panas/silau di iklim tropis.",
        "sources": [
            "https://doi.org/10.1016/j.jretconser.2022.103080",
            "https://ideas.repec.org/a/eee/joreco/v69y2022ics0969698922001734.html",
            GEHL,
        ],
    },
    {
        "name": "Active Frontage and Rhythm",
        "lever_type": "Arsitektur fasad / urban design",
        "funnel_stage": "Perlambatan & berhenti pejalan -> peluang masuk",
        "key_evidence": (
            "Gehl, Kaefer & Reigstad (2006, Urban Design International): observasi segmen fasad 10 m di tujuh area "
            "Kopenhagen. Di depan fasad aktif (kelas A) pejalan 13% lebih lambat; 75% menoleh ke fasad vs 21% di fasad "
            "tertutup (kelas E); 25% berhenti vs 1%; total aktivitas & waktu tinggal 7x lebih banyak. Jalan belanja yang "
            "hidup memiliki 15-20 unit dan 20-25 pintu per 100 m. Studi Gil Lopez (Madrid) menyarankan pintu setiap 7-9 m, "
            "kaca ~63% panjang fasad, ceruk/bukaan yang menambah panjang fasad 30%, dan zona tepi 0,7-2,0 m untuk berhenti."
        ),
        "effect_size": "Berhenti 25% vs 1%; menoleh 75% vs 21%; kecepatan -13%; aktivitas 7x (fasad A vs E).",
        "evidence_type": "Observasi lapangan (perilaku pejalan)",
        "evidence_strength": "Kuat untuk perilaku pejalan; tidak mengukur penjualan",
        "productivity_metric": "Laju berhenti & menoleh per 100 pejalan, capture rate, penjualan per meter frontage.",
        "design_guidelines": (
            "Pecah fasad panjang menjadi ritme unit/pintu; beri ceruk dan zona tepi untuk berhenti tanpa menghalangi arus; "
            "hindari dinding buta di lantai dasar. Untuk mal: prinsip ritme yang sama berlaku di koridor."
        ),
        "risks_limitations": "Konteks jalan kota Eropa; berhenti belum tentu masuk/membeli.",
        "sources": [GEHL, GEHL_PDF],
    },
    {
        "name": "On-Premise Signage",
        "lever_type": "Identitas & visibilitas",
        "funnel_stage": "Ditemukan (visibilitas) -> kunjungan, terutama pembelian impulsif",
        "key_evidence": (
            "Studi Signage Foundation (dilaporkan Sign Media Canada, 2013): pada toko Pier 1 Imports, sign gedung/pylon/"
            "sign multi-tenant baru menambah 5-15% penjualan lokasi; kenaikan terbesar pada toko berkinerja rendah dan saat "
            "sign ditambahkan pada sisi bangunan yang sebelumnya tanpa sign. Taylor, Sarkees & Bang (2012, J. Public Policy "
            "& Marketing): 85% pengguna sign di sampel AS menyatakan akan kehilangan penjualan tanpa sign on-premise "
            "(rata-rata estimasi kehilangan 34,5%, dikutip Taylor/SRF). SBA (2003, dikutip SRF): kunjungan impulsif 15-45% "
            "penjualan tergantung jenis usaha."
        ),
        "effect_size": "+5% s.d. +15% penjualan (kasus Pier 1, sign baru); estimasi kehilangan tanpa sign 34,5% (self-report).",
        "evidence_type": "Studi kasus & survei yang didanai industri",
        "evidence_strength": "Lemah-sedang (didanai industri, sebagian self-report)",
        "productivity_metric": "Pejalan/kendaraan yang 'melihat' toko (visibility audit), capture rate, penjualan per lokasi sebelum-sesudah.",
        "design_guidelines": (
            "Audit visibilitas dari arah datang utama (pejalan, kendaraan, eskalator mal). Prioritaskan sisi/arah tanpa "
            "sign dan toko berkinerja rendah, tempat efek terbesar dilaporkan."
        ),
        "risks_limitations": "Bias pendana; hasil per-kasus; tunduk pada aturan reklame lokal.",
        "sources": [
            "https://www.signmedia.ca/studies-show-benefits-of-on-premise-signage/",
            "https://doi.org/10.1509/jppm.10.054",
            "https://www.signresearch.org/wp-content/uploads/Illuminated-vs-Non-Illuminated-Signage-Economic-Impact-of-Illumination.pdf",
        ],
    },
    {
        "name": "Facade and Sign Lighting",
        "lever_type": "Identitas & visibilitas",
        "funnel_stage": "Visibilitas malam -> perlambatan & kunjungan",
        "key_evidence": (
            "Taylor (Villanova, untuk Sign Research Foundation): survei 333 pengguna sign (response rate 47,4%). Lebih dari "
            "separuh responden memperkirakan kehilangan penjualan bila sign tidak boleh dinyalakan; kelompok ini "
            "memperkirakan kehilangan 21%, rata-rata seluruh sampel 11%. 81% menyalakan sign di luar jam buka. Gehl dkk. "
            "(2006): pada studi malam hari, pejalan melewati fasad A yang terang lebih lambat daripada fasad E yang gelap."
        ),
        "effect_size": "Estimasi kehilangan penjualan 11% (rata-rata) bila sign tidak diterangi (self-report).",
        "evidence_type": "Survei industri + observasi",
        "evidence_strength": "Lemah (self-report) - sedang (arah perilaku)",
        "productivity_metric": "Capture rate & penjualan per jam setelah gelap; konsumsi energi per penjualan.",
        "design_guidelines": "Rancang skenario cahaya siang/malam; terangi etalase dan interior dekat kaca, bukan hanya logo.",
        "risks_limitations": "Self-report pemilik usaha; regulasi cahaya & energi.",
        "sources": [
            "https://www.signresearch.org/wp-content/uploads/Illuminated-vs-Non-Illuminated-Signage-Economic-Impact-of-Illumination.pdf",
            GEHL,
        ],
    },
    {
        "name": "Daylighting and Glazing",
        "lever_type": "Selubung bangunan",
        "funnel_stage": "Pengalaman di dalam toko -> penjualan",
        "key_evidence": (
            "Heschong Mahone Group (1999, untuk PG&E): toko dengan skylight tercatat penjualan 40% lebih tinggi. Studi "
            "replikasi (Peet, Heschong, Wright & Aumann, ACEEE 2004): 73 toko rantai lain (24 dengan daylight signifikan), "
            "3 tahun data bulanan, regresi dengan banyak kontrol. Angka 40% dinilai 'improbably high' dan paling jauh batas "
            "atas; efek rata-rata daylight se-rantai hanya +1% s.d. +6%, tidak cukup besar untuk kepastian statistik tinggi; "
            "efek bergantung pada faktor lain (mis. parkir: -8,7% s.d. +19,7%)."
        ),
        "effect_size": "Klaim awal +40%; replikasi +1% s.d. +6% (rata-rata rantai).",
        "evidence_type": "Regresi observasional antar-toko (dengan replikasi)",
        "evidence_strength": "Sedang (efek kecil setelah replikasi)",
        "productivity_metric": "Penjualan per m2 dengan kontrol lokasi; energi per penjualan.",
        "design_guidelines": "Manfaatkan cahaya alami untuk kualitas ruang dan energi, tetapi jangan membenarkan capex dengan angka 40%.",
        "risks_limitations": "Studi AS/California, format big-box; di iklim tropis panas & silau perlu dikelola.",
        "sources": [
            "https://www.aceee.org/files/proceedings/2004/data/papers/SS04_Panel7_Paper24.pdf",
        ],
    },
    {
        "name": "Frontage Width and Zone A",
        "lever_type": "Geometri & properti",
        "funnel_stage": "Nilai sewa & produktivitas ruang dekat muka toko",
        "key_evidence": (
            "Konvensi penilaian ritel Inggris (zoning/ITZA, dirujuk RICS): unit high street dibagi zona sedalam 6,1 m "
            "(20 kaki) dari muka toko; Zona A paling bernilai, Zona B dinilai A/2, Zona C A/4 ('halving back'). Pasar sewa "
            "secara eksplisit menilai ruang dekat fasad jauh lebih produktif daripada ruang belakang."
        ),
        "effect_size": "Nilai sewa per m2 ruang Zona B = 1/2 Zona A; Zona C = 1/4 (konvensi).",
        "evidence_type": "Konvensi pasar properti",
        "evidence_strength": "Kuat sebagai sinyal pasar (bukan eksperimen)",
        "productivity_metric": "Penjualan per m2 per zona kedalaman; penjualan per meter frontage; sewa ITZA.",
        "design_guidelines": (
            "Utamakan lebar frontage dibanding kedalaman saat memilih unit; tempatkan penawaran bermargin tinggi dan "
            "pemicu kunjungan di 6 m pertama; hindari fungsi mati (gudang, kasir tertutup) di Zona A."
        ),
        "risks_limitations": "Konvensi Inggris; tidak dipakai untuk department store/supermarket besar.",
        "sources": [
            "https://www.ricsfirms.com/glossary/zoning/",
            "https://www.kirkbydiamond.co.uk/news-and-insights/time-to-get-in-the-zone-a/",
        ],
    },
    {
        "name": "Exterior Landscaping",
        "lever_type": "Eksterior",
        "funnel_stage": "Kesukaan terhadap eksterior -> niat berkunjung",
        "key_evidence": (
            "Mower, Kim & Childs (2012, J. Fashion Marketing and Management): eksperimen dengan mahasiswa untuk butik "
            "apparel. Window display dan lanskap tidak berpengaruh langsung pada rasa senang/arousal, tetapi keberadaannya "
            "meningkatkan kesukaan terhadap eksterior dan niat berkunjung. Mereka mencatat Turley & Milliman (2000) menyebut "
            "variabel eksterior paling sedikit diteliti."
        ),
        "effect_size": "Kesukaan eksterior & niat berkunjung naik (signifikan); besaran tidak di abstrak.",
        "evidence_type": "Eksperimen (sampel mahasiswa)",
        "evidence_strength": "Lemah-sedang (niat, bukan perilaku)",
        "productivity_metric": "Capture rate, kunjungan ulang.",
        "design_guidelines": "Untuk toko jalan/ruko: tanaman, peneduh, dan tempat berhenti di depan toko sebagai sinyal peduli.",
        "risks_limitations": "Sampel mahasiswa; niat belum tentu perilaku.",
        "sources": [
            "https://doi.org/10.1108/13612021211265836",
            "https://doi.org/10.1016/s0148-2963(99)00010-7",
        ],
    },
    {
        "name": "Interactive Digital Storefront",
        "lever_type": "Teknologi fasad",
        "funnel_stage": "Keterlibatan -> niat masuk & word of mouth",
        "key_evidence": (
            "Pantano, Priporas & Foroudi (2019, IJRDM): survei 341 konsumen yang mendekati etalase berteknologi interaktif "
            "di dua toko apparel di New York. Konsumen yang merasakan teknologi interaktif di etalase bersedia masuk toko "
            "dan menyebarkan word of mouth positif. Pantano (2016, JRCS) memodelkan keterlibatan konsumen di storefront "
            "interaktif."
        ),
        "effect_size": "Hubungan positif pada niat masuk & WOM (model struktural); tanpa angka penjualan.",
        "evidence_type": "Survei di lokasi (niat)",
        "evidence_strength": "Lemah-sedang",
        "productivity_metric": "Interaksi per jam, capture rate, biaya konten per kunjungan tambahan.",
        "design_guidelines": "Gunakan untuk flagship/lokasi berlalu-lintas tinggi; ukur biaya konten & perawatan terhadap kunjungan tambahan.",
        "risks_limitations": "Efek novelty; biaya operasional layar; bukti niat, bukan transaksi.",
        "sources": [
            "https://doi.org/10.1108/ijrdm-07-2018-0120",
            "https://doi.org/10.1016/j.jretconser.2015.09.007",
        ],
    },
    {
        "name": "Full Remodel Programs",
        "lever_type": "Program renovasi (termasuk fasad)",
        "funnel_stage": "Seluruh funnel (traffic, konversi, ticket)",
        "key_evidence": (
            "Target (manajemen, Q1 FY2025, via Zacks/Globe and Mail): comp lift 2-4% pada tahun pertama setelah remodel, "
            "ditambah hampir 3% di tahun kedua. Dollar General (manajemen, via Zacks): Project Renovate (remodel penuh toko "
            ">= 7 tahun) sekitar +6% comp tahunan; Project Elevate (perbaikan lebih ringan) sekitar +3%; rencana FY2026 "
            "~2.000 Renovate & ~2.250 Elevate (8-K Des 2025). Starbucks 'coffeehouse uplift': 1.000+ remodel Amerika Utara "
            "(FY2026), manajemen melaporkan kenaikan transaksi tanpa angka per toko."
        ),
        "effect_size": "+2% s.d. +4% (Target th.1) + ~3% (th.2); ~+6% / ~+3% (Dollar General).",
        "evidence_type": "Laporan manajemen (bukan uji terkontrol publik)",
        "evidence_strength": "Sedang (skala besar, tetapi paket intervensi & dilaporkan sendiri)",
        "productivity_metric": "Comp sales toko remodel vs kontrol berpasangan; payback capex.",
        "design_guidelines": (
            "Gunakan angka remodel penuh sebagai BATAS ATAS untuk intervensi fasad saja. Pisahkan komponen fasad dalam desain "
            "uji (fasad saja vs fasad + interior) agar kontribusinya dapat diukur."
        ),
        "risks_limitations": "Remodel mencakup interior, merchandising, operasi; pemilihan toko tidak acak.",
        "sources": [
            "https://www.theglobeandmail.com/investing/markets/stocks/DG/pressreleases/33275312/can-remodeling-efforts-revive-targets-in-store-traffic-trends/",
            "https://www.tradingview.com/news/zacks:cdcb092b0094b:0-dollar-general-s-project-renovate-and-elevate-drive-comp-sales-lift/",
            "https://www.sec.gov/Archives/edgar/data/29534/000110465925118286/tm2532496d1_ex99.htm",
            "https://www.restaurantdive.com/news/starbucks-q3-turnaround-gains-sales-momentum/826543/",
        ],
    },
    {
        "name": "Service Facade for Omnichannel",
        "lever_type": "Fasad fungsional",
        "funnel_stage": "Throughput (transaksi per jam per m2 / per jam kerja)",
        "key_evidence": (
            "Starbucks Now (Beijing, Jul 2019): format express dengan 'pickup portal' di dinding yang diakses pelanggan & "
            "kurir. Luckin Coffee: 99,1% gerai self-operated adalah pickup store 20-60 m2 (20-F FY2025). Bukti publik yang "
            "memisahkan efek fasad fungsional terhadap produktivitas belum tersedia [uncertain besaran efek]."
        ),
        "effect_size": "[uncertain] belum ada angka publik",
        "evidence_type": "Kasus format",
        "evidence_strength": "Lemah (kasus, tanpa angka efek)",
        "productivity_metric": "Waktu serah pesanan, pesanan per jam per m2, antrean rider, penjualan per jam kerja.",
        "design_guidelines": "Pisahkan jalur pickup/kurir dari pintu tamu; tampilkan status pesanan di muka toko.",
        "risks_limitations": "Dapat mengurangi suasana bila tidak dirancang; efek bergantung porsi order digital.",
        "sources": [
            "https://www.nrn.com/news/starbucks-opens-first-express-store-format-china",
            "https://www.sec.gov/Archives/edgar/data/1767582/000110465926035712/lk-20251231x20f.htm",
        ],
    },
]


def slugify(name):
    return re.sub(r"[^A-Za-z0-9_]", "", name.replace(" ", "_"))


def main():
    OUT.mkdir(exist_ok=True)
    for item in ITEMS:
        data = dict(item)
        data["uncertain"] = [k for k, v in item.items() if isinstance(v, str) and "[uncertain]" in v]
        path = OUT / f"{slugify(item['name'])}.json"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(path.name, "uncertain:", data["uncertain"])


if __name__ == "__main__":
    main()
