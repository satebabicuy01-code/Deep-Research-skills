# Memo: Kesenjangan Integrasi Loyalty Antar-Pilar KLG
### Ditujukan untuk: Director of CRM / Loyalty (Commercial Technology — Ruparupa)
*Scope: satu proyek yang bisa dieksekusi satu direktorat, bukan restrukturisasi grup.*

---

## 1. Temuan: Situasi Loyalty Saat Ini (bukan dugaan — hasil riset lapangan)

Sebelum menuduh loyalty KLG "silo total" seperti asumsi awal saya, faktanya **lebih baik dari dugaan** di satu sisi, tapi ada **satu celah nyata yang belum tertutup**:

### Yang sudah terintegrasi dengan baik: **ruparupa rewards**
- Satu program loyalty (mata uang: **"Coins"**) yang resmi menaungi hampir semua brand Consumer Retail: AZKO (eks-ACE), INFORMA Furnishings, INFORMA Electronics, Krisbow, Toys Kingdom, Pendopo, Pet Kingdom, SELMA, ATARU, EYE SOUL — plus Chatime terdaftar sebagai partner.
- Fitur cukup matang: pendaftaran gratis, harga khusus member, akumulasi & penukaran poin **lintas brand**, gratis ongkir/pasang, member seumur hidup.
- Bahkan sudah menang penghargaan **"Best Engagement Strategy (Omnichannel) — Loyalty & Engagement Awards 2025"**.
- Sudah mulai ekspansi ke **partner pihak ketiga** (mis. Tugu Insurance, Nov 2024) — tanda program ini sedang dijadikan platform loyalty yang lebih besar dari sekadar diskon toko.

**Kesimpulan bagian ini: tim Ruparupa Rewards sudah mengerjakan PR besar (unifikasi lintas-brand retail) dengan cukup baik.** Pain point saya sebelumnya di sini agak berlebihan.

### Yang BELUM terintegrasi: **F&B ID punya ekosistem loyalty sendiri, terpisah**
- F&B ID (Chatime, Cupbop, Gindaco, Chatime Atelier, 88SEOUL) punya aplikasi sendiri — **"My F&B ID"** — dengan mata uang poin sendiri: **"Happy Koin"**, bukan "Coins" ruparupa.
- Meski Chatime *terdaftar* sebagai partner ruparupa rewards, dua sistem poin (Coins vs Happy Koin) berjalan **paralel**, bukan satu ledger — pelanggan yang aktif belanja di AZKO/Informa *dan* rutin beli Chatime kemungkinan besar punya **dua akun, dua saldo poin, dua histori transaksi yang tidak saling bicara**.
- Chatime bahkan sudah punya kanal loyalty pihak ketiga tambahan (redeem via Telkomsel Poin) — makin menambah fragmentasi titik masuk pelanggan yang sama.

### Yang tidak punya jejak loyalty sama sekali: **Property & Hospitality**
- Tidak ditemukan bukti Living World, Living Plaza, atau hotel Anumana terhubung ke ruparupa rewards maupun program lain. Pengunjung mal/tamu hotel yang notabene berada di properti milik grup sendiri **tidak mendapat/memberi sinyal loyalty apa pun** ke sistem CRM KLG.

---

## 2. Kenapa Ini Penting (Business Case yang Terukur untuk Director-level)

Ini bukan proyek "nice to have" — ada logika bisnis konkret:

1. **F&B adalah kanal frekuensi tertinggi di grup.** Orang beli furnitur/perkakas mungkin 1-2x/tahun, tapi minum Chatime bisa mingguan. F&B ID adalah **sensor perilaku pelanggan paling sering menyala** di seluruh grup (500+ lokasi, 62+ kota) — tapi datanya terkunci di silo terpisah dari mesin CRM utama (ruparupa rewards).
2. **F&B ID mengisi tenant di properti milik grup sendiri (Living World/Living Plaza).** Ini rantai yang seharusnya nyambung: pengunjung mal → beli Chatime → belanja AZKO/Informa di mal yang sama. Tanpa satu ledger poin, KLG kehilangan kemampuan melihat **customer journey lintas-pilar** yang sebenarnya sudah terjadi secara fisik (satu orang, satu kunjungan, tiga transaksi berbeda sistem).
3. **Kompetitor bukan cuma toko lain, tapi ekosistem loyalty lain.** Kalau member Chatime individual lebih sering dapat insentif lewat Telkomsel Poin daripada lewat KLG sendiri, KLG kehilangan kepemilikan atas relasi pelanggannya sendiri ke pihak ketiga.
4. **Property yang "buta" terhadap loyalty adalah biaya peluang.** Living World/Anumana sudah bergerak jadi profit center sendiri (lihat riset pilar sebelumnya) — kalau loyalty tidak menyentuh properti, grup kehilangan cara termurah untuk mendorong lalu lintas silang (mal → toko, hotel → F&B) yang justru menjadi alasan properti ini dulu dibangun.

---

## 3. Rekomendasi — Scope yang Bisa Dieksekusi Satu Direktorat (bukan proyek IT raksasa grup)

**Bukan** disarankan: memaksa merger total dua aplikasi (My F&B ID vs ruparupa) dalam satu proyek besar — itu proyek berisiko tinggi, lintas-direktorat, butuh restrukturisasi backend F&B ID yang sudah stabil dilayani 500+ toko.

**Yang direkomendasikan** — 3 fase bertahap, tiap fase punya pemilik jelas dan bisa diukur direktur CRM sendiri:

### Fase 1 (0-3 bulan) — Interoperabilitas Poin, bukan Merger Sistem
- Buat **kurs konversi** Happy Koin ↔ Coins (mirip konversi poin maskapai-hotel partner), lewat API sederhana antar dua sistem yang sudah ada. Tidak perlu satu database, cukup satu jembatan konversi.
- Deliverable: fitur "Tukar Happy Koin ke Coins ruparupa" (dan sebaliknya) di kedua app.

### Fase 2 (3-6 bulan) — Single Customer ID, Bukan Single App
- Satukan **identitas login** (nomor HP/email sebagai key yang sama) di kedua sistem, supaya backend bisa mengenali "1 orang" walau tetap pakai 2 app berbeda — ini fondasi untuk analitik cross-pillar tanpa memaksa pelanggan pindah app.
- Deliverable: dashboard internal yang bisa menjawab "berapa % member Chatime yang juga member AZKO/Informa, dan berapa nilai transaksi gabungannya" — sebelumnya pertanyaan ini kemungkinan tidak bisa dijawab sama sekali.

### Fase 3 (6-12 bulan) — Tarik Property & Hospitality Masuk Ekosistem
- Uji coba di **satu mal** dulu (mis. Living World Grand Wisata yang baru) — QR code loyalty check-in untuk pengunjung mal, dan konfirmasi menginap di Anumana, yang memberi Coins.
- Deliverable: pilot terukur di satu lokasi sebelum diperluas — sesuai skala proyek yang wajar untuk satu direktorat, bukan rollout nasional sekaligus.

---

## 4. Metrik yang Bisa Dipegang Director Ini (bukan metrik CEO/holding)

- **Overlap rate**: % member F&B ID yang juga member ruparupa rewards (baseline sekarang: kemungkinan besar tidak terukur/rendah karena dua sistem terpisah).
- **Redemption cross-pillar**: jumlah penukaran Happy Koin→Coins atau sebaliknya per bulan.
- **Uplift kunjungan bersilang**: naiknya transaksi AZKO/Informa dari segmen "member Chatime aktif" pasca-fase 1&2.
- **Pilot properti**: jumlah check-in loyalty di lokasi mal percobaan (Fase 3) sebagai indikator kelayakan sebelum ekspansi.

---

## 5. Batasan yang Disengaja (supaya proyek ini tidak membengkak jadi masalah tier-1 lagi)

- Tidak menyentuh keputusan merger organisasi F&B ID ke Commercial Technology.
- Tidak mengubah aplikasi utama pelanggan (My F&B ID tetap ada, ruparupa tetap ada) — cukup jembatan data.
- Tidak menuntut keputusan investasi properti/hotel baru — hanya memakai aset yang sudah berjalan (Living World, Anumana) sebagai lokasi pilot.

---

## Sumber Tambahan (loyalty-specific)

- [kawanlamagroup.com — Best Engagement Strategy Omnichannel via ruparupa rewards](https://www.kawanlamagroup.com/en/article/kawan-lama-group-meraih-best-engagement-strategy-omnichannel-melalui-ruparupa-rewards)
- [Kompas Biz — Tugu Insurance & ruparupa rewards sinergi](https://biz.kompas.com/read/2024/11/19/135422028/tugu-insurance-dan-ruparupa-rewards-jalin-sinergi-strategis-hadirkan-manfaat)
- [AZKO — Halaman Membership](https://azko.id/membership)
- [AZKO — Upgrade membership ruparupa rewards ke Gold](https://azko.id/en/promo/gratis-upgrade-membership-ruparupa-rewards-ke-level-gold)
- [Informa — Membership](https://informa.co.id/membership)
- [Kompas Biz — Chatime, Cupbop, Gindaco, Chatime Atelier lewat aplikasi My F&B ID](https://biz.kompas.com/read/2022/10/13/114026428/chatime-cupbop-gindaco-dan-chatime-atealier-kini-bisa-dipesan-sekaligus-lewat)
- [Chatime Indonesia FAQ](https://chatime.co.id/faq)
- [Google Play — F&B ID App (Chatime Indonesia), com.klg.chatime](https://play.google.com/store/apps/details?id=com.klg.chatime)
- [Telkomsel — Tukar Poin Telkomsel jadi Voucher Chatime](https://www.telkomsel.com/jelajah/jelajah-lifestyle/begini-cara-dapat-voucher-chatime-pakai-poin-telkomsel)
- [Google Play — ruparupa app](https://play.google.com/store/apps/details?id=com.mobileappruparupa)
- [Merdeka.com — Ruparupa gabungkan toko fisik dan platform online](https://www.merdeka.com/uang/persaingan-e-commerce-makin-ketat-ruparupa-gabungkan-toko-fisik-dan-platform-online-421585-mvk.html)

*Catatan: tidak ditemukan sumber publik yang menyebut integrasi loyalty untuk Living World/Living Plaza/Anumana — kesimpulan "belum ada" di memo ini didasarkan pada ketiadaan bukti, bukan konfirmasi eksplisit dari KLG. Sebelum eksekusi Fase 3, validasi dulu langsung ke tim Property apakah program semacam itu sudah ada secara internal (tidak dipublikasikan) atau memang belum ada.*
