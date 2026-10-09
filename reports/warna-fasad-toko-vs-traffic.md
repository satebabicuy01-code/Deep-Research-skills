# Warna Fasad Toko vs Traffic Pelanggan

Laporan untuk BOD · per 9 Oktober 2026 · Versi utama (dokumen hidup): https://claude.ai/code/artifact/61c119f0-6a05-4e07-9e93-0551176ffd65

## Kesimpulan untuk BOD

**Klaim "toko berwarna hijau selalu ramai" belum terbukti oleh data.** Tidak ada satu pun studi, global maupun Indonesia, yang menunjukkan bahwa fasad hijau menaikkan jumlah kunjungan ke toko independen.

- **Bukti yang ada menunjuk ke hal lain.** Studi yang mengukur kunjungan menemukan bahwa yang berpengaruh adalah kualitas tampilan (kreativitas etalase, rasa senang saat melihat fasad), bukan satu warna tertentu.
- **Warna berpengaruh lewat emosi dan bergantung pada konteks.** Studi fasad mal di China (2024) menemukan warna netral dan warna hangat yang terang memberi respons paling positif, bukan hijau.
- **Untuk Indonesia, data spesifiknya tidak ada.** Riset lokal hanya mengukur "eksterior toko" secara umum lewat kuesioner, dan hasilnya interior justru lebih berpengaruh.
- **Kesan "toko hijau selalu ramai" kemungkinan besar bias.** Kita mengingat toko hijau yang ramai, tetapi tidak menghitung toko hijau yang sepi atau sudah tutup. Lokasi dan arus pejalan kaki jauh lebih berpengaruh.

**Rekomendasi:** jangan mengecat ulang toko berdasarkan klaim ini. Jika ingin menguji, lakukan uji coba terkontrol di 10–20 toko dengan alat penghitung pengunjung.

## Bukti riset yang tersedia

| Studi | Setting | Metode & sampel | Temuan utama | Relevansi |
| --- | --- | --- | --- | --- |
| [Lange, Rosengren & Blom (2016), JBR](https://research.hhs.se/esploro/outputs/journalArticle/Store-window-creativitys-impact-on-shopper-behavior/991001480353106056) | Swedia | Studi lapangan n=1.834 + online n=480 | Etalase lebih kreatif → lebih banyak kunjungan | Kuat untuk kualitas tampilan; bukan warna |
| [Fasad mal, Buildings (2024)](https://doi.org/10.3390/buildings14082302) | China | 149 responden, 10 render fasad | Netral & hangat terang paling disukai; rasa senang (β=0,557) prediktor terkuat | Hijau tidak unggul; simulasi |
| [Radboud University (tesis)](https://theses.ubn.ru.nl/items/e70b3d98-87fc-4790-a41b-b3092d41f796) | Belanda | 391 observasi lapangan + skenario | Etalase berpengaruh hanya pada pembelanja rekreasional | Efek bergantung konteks |
| [Babin, Hardesty & Suter (2003)](https://aquila.usm.edu/fac_pubs/3235) | AS | Eksperimen interior biru vs oranye | Biru → niat kunjung lebih tinggi; pencahayaan memoderasi | Interior, bukan fasad |
| Bellizzi, Crowley & Hasty (1983), J. of Retailing | AS | Eksperimen lab | Warna hangat menarik perhatian, sejuk lebih nyaman | Ringkasan sekunder tidak seragam |
| [Labrecque & Milne (2012), JAMS](https://colab.ws/articles/10.1007%2Fs11747-010-0245-y) | AS | 4 eksperimen | Warna membentuk kepribadian merek & niat beli | Identitas merek, bukan traffic |
| [Albar (2019)](https://ejournal.uigm.ac.id/index.php/EGMK/article/view/846) | Indonesia (Yogyakarta) | Kuesioner 100 responden | Eksterior 0,330; interior 0,522 | Warna fasad tidak diukur terpisah |
| [Kajian store atmosphere, Fokus UAD](https://journal2.uad.ac.id/index.php/fokus/article/download/5728/3071/24213) | Indonesia | Kajian literatur | Warna berpengaruh positif ke minat beli | Minat beli, bukan kunjungan |
| [Skripsi UGM (2020)](https://etd.repository.ugm.ac.id/home/detail_pencarian_downloadfiles/523070) | Indonesia | Eksperimen kemasan merah vs hijau | Hijau + logo organik → kesan lebih sehat | Hanya relevan untuk kategori sehat/segar |

## Mengapa toko hijau terlihat ramai

- **Bias ingatan (survivorship bias):** hanya toko yang bertahan dan ramai yang terlihat.
- **Lokasi dan arus pejalan kaki:** pendorong traffic terkuat, apa pun warna fasadnya.
- **Kategori dan merek:** hijau diasosiasikan dengan sehat dan alami; kategori yang memang ramai bisa membuat hijau tampak "laris" (hipotesis, perlu dicek).
- **Kualitas tampilan:** satu-satunya faktor fasad dengan bukti lapangan kuat.

## Rekomendasi: buktikan dengan data internal

1. Pasang penghitung pengunjung di 20 toko yang mirip.
2. Rekam baseline 4 minggu (orang lewat, masuk, capture rate, transaksi, konversi).
3. Bagi acak: 10 toko diubah warna fasadnya, 10 tetap sebagai pembanding; hanya warna yang diubah.
4. Ukur 8 minggu dan bandingkan dengan difference-in-differences.
5. Tetapkan ambang keputusan di awal (misalnya capture rate naik ≥ 10% dan signifikan).

Langkah murah lebih dulu: audit warna fasad seluruh jaringan terhadap traffic/omzet, dengan kontrol lokasi dan ukuran toko.
