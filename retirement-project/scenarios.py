"""Definisi asumsi & 15 skenario pensiun (5 profil x 3 skenario).

Semua angka dalam Rp juta, NILAI HARI INI (2026). Bulanan kecuali disebut lain.
Model menaikkan angka-angka ini dengan inflasi secara otomatis.
"""

AGE_START, AGE_END, RETIRE_AGE, YEAR_START = 40, 75, 50, 2026

ASSUMPTIONS = {
    "inflasi": 0.04,            # inflasi umum jangka panjang (BPS Okt-2026: 3,23% yoy)
    "inflasi_kesehatan": 0.07,  # biaya kesehatan rumah tangga (lebih tinggi dari umum)
    "kenaikan_properti": 0.05,  # kenaikan harga rumah/tanah per tahun
    "iuran_jht": 0.057,         # 3,7% pemberi kerja + 2% pekerja, dari gaji
    "imbal_jht": 0.055,         # imbal hasil JHT (konvensional 2025: 5,51%)
}

AGES = list(range(AGE_START, AGE_END + 1))


def seg(*parts, default=0.0):
    """parts: (usia_awal, usia_akhir_inklusif, nilai). Hasil: dict usia->nilai."""
    out = {a: default for a in AGES}
    for a0, a1, v in parts:
        for a in range(a0, a1 + 1):
            out[a] = v
    return out


def one(age, value):
    out = {a: 0.0 for a in AGES}
    out[age] = value
    return out


W, R = (40, 49), (50, 75)  # fase kerja / fase pensiun

PROFILES = {
    "P1": {"nama": "Profil 1 - Penghasilan Rp10 juta", "gaji": 10, "biaya_jkt": 12},
    "P2": {"nama": "Profil 2 - Penghasilan Rp20 juta", "gaji": 20, "biaya_jkt": 11},
    "P3": {"nama": "Profil 3 - Penghasilan Rp30 juta", "gaji": 30, "biaya_jkt": 12},
    "P4": {"nama": "Profil 4 - Penghasilan Rp50 juta", "gaji": 50, "biaya_jkt": 13.5},
    "P5": {"nama": "Profil 5 - Penghasilan Rp75 juta (>50 juta)", "gaji": 75, "biaya_jkt": 15},
}

# Komponen biaya hidup pensiun pasangan (di luar kesehatan & tempat tinggal), nilai hari ini
HEMAT_DESA, HEMAT, STANDAR, NYAMAN, NYAMAN_PLUS = 4.0, 4.5, 6.0, 8.0, 10.0
RAWAT_RUMAH = 0.3   # PBB + perawatan rumah milik sendiri
SEWA_SMG = 1.75     # sewa rumah sederhana Semarang (~Rp21 jt/tahun)
SEWA_PKL = 1.25     # sewa rumah sederhana Pekalongan/Pemalang

SCENARIOS = []


def add(code, profile, label, judul, r_acc, r_ret, gaji, tambahan, biaya, kesehatan,
        tinggal, properti_income, jp, beli_aset, lain, ringkas):
    SCENARIOS.append(dict(code=code, profile=profile, label=label, judul=judul,
                          r_acc=r_acc, r_ret=r_ret, gaji=gaji, tambahan=tambahan,
                          biaya=biaya, kesehatan=kesehatan, tinggal=tinggal,
                          properti_income=properti_income, jp=jp, beli_aset=beli_aset,
                          lain=lain, ringkas=ringkas))


# ---------------- P1: 10 jt, biaya 12 jt (defisit) ----------------
add("P1-A", "P1", "A. Paling bisa dilakukan", "Hemat ketat + kerja sampingan, pensiun ke Pekalongan/Comal",
    0.055, 0.055,
    gaji=seg((40, 49, 10)),
    tambahan=seg((41, 49, 1.0), (50, 59, 4.0), (60, 64, 2.5), (65, 69, 1.0)),
    biaya=seg((40, 49, 9.5), (50, 75, HEMAT_DESA)),
    kesehatan=seg((50, 75, 0.75)),
    tinggal=seg((50, 75, SEWA_PKL)),
    properti_income=seg(), jp=seg((65, 75, 2.1)),
    beli_aset=seg(), lain=seg(),
    ringkas="Biaya dipangkas 12->9,5 jt, sampingan 1 jt; usia 50 pindah dekat keluarga di Pekalongan/Comal (sewa murah); tetap bekerja/usaha kecil 4 jt s/d 60, 2,5 jt s/d 65, 1 jt s/d 70.")

add("P1-B", "P1", "B. Paling menguntungkan", "Kerja ke Jepang (Tokutei Ginou) 5 tahun berdua, pulang beli rumah + kontrakan",
    0.06, 0.055,
    gaji=seg((40, 41, 10), (47, 49, 7)),
    tambahan=seg((42, 46, 36), (50, 59, 4.0), (60, 64, 2.5)),
    biaya=seg((40, 41, 9.0), (42, 46, 18), (47, 49, 5.5), (50, 75, HEMAT)),
    kesehatan=seg((50, 75, 0.75)),
    tinggal=seg((47, 75, RAWAT_RUMAH)),
    properti_income=seg((48, 75, 2.5)), jp=seg((65, 75, 1.6)),
    beli_aset=one(47, 900), lain=one(41, -15),
    ringkas="Usia 40-41 belajar bahasa Jepang (N4) & uji keterampilan; 42-46 kerja di Jepang berdua; 47 pulang, beli rumah 400 jt + kontrakan 5 pintu 500 jt dekat kawasan industri Batang/Kendal.")

add("P1-C", "P1", "C. Saran saya", "Naik kelas lewat bahasa Mandarin, pindah kerja ke koridor industri Semarang-Kendal-Batang",
    0.06, 0.055,
    gaji=seg((40, 43, 10), (44, 49, 13)),
    tambahan=seg((41, 49, 2.0), (50, 59, 7.0), (60, 64, 3.5), (65, 69, 1.0)),
    biaya=seg((40, 49, 8.5), (50, 75, HEMAT)),
    kesehatan=seg((50, 75, 0.75)),
    tinggal=seg((48, 75, RAWAT_RUMAH)),
    properti_income=seg(), jp=seg((65, 75, 2.1)),
    beli_aset=one(48, 400), lain=seg(),
    ringkas="Biaya 8,5 jt (kontrakan pinggiran dekat KRL); salah satu belajar Mandarin s/d HSK 4-5, gaji rumah tangga naik ke 13 jt di usia 44 + sampingan 2 jt; usia 48 beli rumah 400 jt di pinggir Semarang/Kendal/Batang; berdua kerja di kawasan industri 7 jt s/d 60, 3,5 jt s/d 65.")

# ---------------- P2: 20 jt, biaya 11 jt ----------------
add("P2-A", "P2", "A. Paling bisa dilakukan", "Autodebet SBN/RDPU, beli rumah Semarang saat pensiun",
    0.055, 0.055,
    gaji=seg((40, 49, 20)),
    tambahan=seg((50, 59, 2.0)),
    biaya=seg((40, 49, 10.5), (50, 75, STANDAR)),
    kesehatan=seg((50, 75, 1.0)),
    tinggal=seg((50, 75, RAWAT_RUMAH)),
    properti_income=seg(), jp=seg((65, 75, 4.2)),
    beli_aset=one(50, 600), lain=seg(),
    ringkas="Biaya 10,5 jt, sisa 9,5 jt/bln otomatis ke SBN ritel & RDPU; usia 50 beli rumah 600 jt tunai di Semarang; kerja ringan 2 jt s/d 60.")

add("P2-B", "P2", "B. Paling menguntungkan", "Rumah kos di Semarang usia 47 + sampingan skill + 30% saham",
    0.07, 0.06,
    gaji=seg((40, 49, 20)),
    tambahan=seg((42, 49, 3.0), (50, 59, 5.0), (60, 64, 2.0)),
    biaya=seg((40, 49, 9.0), (50, 75, STANDAR)),
    kesehatan=seg((50, 75, 1.0)),
    tinggal=seg((50, 75, RAWAT_RUMAH)),
    properti_income=seg((48, 75, 3.75)), jp=seg((65, 75, 4.2)),
    beli_aset=one(47, 1000), lain=seg(),
    ringkas="Biaya ditekan ke 9 jt; sampingan 3 jt dari 42; usia 47 beli rumah kos 6 kamar + unit pemilik (1 M) dekat kampus; 50 tinggal di unit pemilik; konsultan/freelance 5 jt s/d 60.")

add("P2-C", "P2", "C. Saran saya", "Inti SBN + 20% reksa dana indeks, beli rumah usia 47, sampingan skill",
    0.065, 0.055,
    gaji=seg((40, 49, 20)),
    tambahan=seg((42, 49, 3.0), (50, 59, 4.0), (60, 64, 2.0)),
    biaya=seg((40, 49, 9.5), (50, 75, STANDAR)),
    kesehatan=seg((50, 75, 1.0)),
    tinggal=seg((50, 75, RAWAT_RUMAH)),
    properti_income=seg((48, 49, 1.0)), jp=seg((65, 75, 4.2)),
    beli_aset=one(47, 600), lain=seg(),
    ringkas="Biaya 9,5 jt; sampingan 3 jt dari 42; usia 47 beli rumah 600 jt di Semarang (disewakan s/d 50); kerja paruh waktu/konsultan 4 jt s/d 60, 2 jt s/d 65.")

# ---------------- P3: 30 jt, biaya 12 jt ----------------
add("P3-A", "P3", "A. Paling bisa dilakukan", "Gaya hidup tetap, semua surplus ke instrumen aman, pensiun penuh",
    0.055, 0.055,
    gaji=seg((40, 49, 30)),
    tambahan=seg(),
    biaya=seg((40, 49, 12), (50, 75, STANDAR)),
    kesehatan=seg((50, 75, 1.0)),
    tinggal=seg((50, 75, RAWAT_RUMAH)),
    properti_income=seg(), jp=seg((65, 75, 4.4)),
    beli_aset=one(50, 650), lain=seg(),
    ringkas="Tanpa ubah gaya hidup; 18 jt/bln ke SBN/RDPU/deposito; usia 50 beli rumah 650 jt; berhenti kerja total.")

add("P3-B", "P3", "B. Paling menguntungkan", "Rumah kos 8 kamar usia 45 + sampingan + 30% saham, pensiun nyaman",
    0.07, 0.06,
    gaji=seg((40, 49, 30)),
    tambahan=seg((42, 49, 3.0), (50, 59, 5.0)),
    biaya=seg((40, 49, 10.5), (50, 75, NYAMAN)),
    kesehatan=seg((50, 75, 1.75)),
    tinggal=seg((50, 75, RAWAT_RUMAH)),
    properti_income=seg((46, 75, 5.6)), jp=seg((65, 75, 4.4)),
    beli_aset=one(45, 1500), lain=seg(),
    ringkas="Biaya 10,5 jt; sampingan 3 jt; usia 45 beli rumah kos 8 kamar (1,5 M) dekat Undip/Unnes; konsultan 5 jt s/d 60; gaya hidup pensiun nyaman + asuransi kesehatan tambahan.")

add("P3-C", "P3", "C. Saran saya", "Rumah usia 47 + kontrakan dekat kawasan industri, portofolio 80/20",
    0.065, 0.055,
    gaji=seg((40, 49, 30)),
    tambahan=seg((42, 49, 2.0), (50, 57, 3.0)),
    biaya=seg((40, 49, 11), (50, 75, 6.5)),
    kesehatan=seg((50, 75, 1.25)),
    tinggal=seg((50, 75, RAWAT_RUMAH)),
    properti_income=seg((48, 49, 1.2), (51, 75, 2.5)), jp=seg((65, 75, 4.4)),
    beli_aset={**one(47, 700), 50: 500}, lain=seg(),
    ringkas="Biaya 11 jt; usia 47 beli rumah 700 jt (disewakan s/d 50); usia 50 bangun kontrakan 500 jt dekat KEK Kendal/Batang; paruh waktu 3 jt s/d 57.")

# ---------------- P4: 50 jt, biaya 13,5 jt ----------------
add("P4-A", "P4", "A. Paling bisa dilakukan", "Autopilot instrumen aman, pensiun nyaman tanpa kerja",
    0.055, 0.055,
    gaji=seg((40, 49, 50)),
    tambahan=seg(),
    biaya=seg((40, 49, 13.5), (50, 75, NYAMAN)),
    kesehatan=seg((50, 75, 1.75)),
    tinggal=seg((50, 75, RAWAT_RUMAH)),
    properti_income=seg(), jp=seg((65, 75, 4.4)),
    beli_aset=one(50, 800), lain=seg(),
    ringkas="Gaya hidup tetap; 36,5 jt/bln ke SBN/RDPU/deposito; usia 50 beli rumah 800 jt; pensiun nyaman penuh.")

add("P4-B", "P4", "B. Paling menguntungkan", "Dua properti produktif + 40% saham + bisnis/konsultan",
    0.075, 0.06,
    gaji=seg((40, 49, 50)),
    tambahan=seg((42, 49, 5.0), (50, 59, 8.0)),
    biaya=seg((40, 49, 12), (50, 75, NYAMAN)),
    kesehatan=seg((50, 75, 1.75)),
    tinggal=seg((50, 75, RAWAT_RUMAH)),
    properti_income=seg((45, 47, 5.6), (48, 75, 9.6)), jp=seg((65, 75, 4.4)),
    beli_aset={**one(44, 1500), 47: 800}, lain=seg(),
    ringkas="Biaya 12 jt; usia 44 rumah kos 1,5 M; usia 47 kontrakan 800 jt; bisnis/konsultan 5-8 jt; portofolio 60/40.")

add("P4-C", "P4", "C. Saran saya", "Pensiun nyaman + 1 rumah kos, kerja opsional, dana darurat besar",
    0.065, 0.055,
    gaji=seg((40, 49, 50)),
    tambahan=seg((50, 56, 3.0)),
    biaya=seg((40, 49, 12.5), (50, 75, NYAMAN)),
    kesehatan=seg((50, 75, 1.75)),
    tinggal=seg((50, 75, RAWAT_RUMAH)),
    properti_income=seg((47, 49, 1.5), (51, 75, 5.6)), jp=seg((65, 75, 4.4)),
    beli_aset={**one(46, 800), 50: 1500}, lain=seg(),
    ringkas="Biaya 12,5 jt; usia 46 beli rumah 800 jt (disewakan dulu); usia 50 rumah kos 1,5 M; kerja opsional 3 jt s/d 56.")

# ---------------- P5: 75 jt, biaya 15 jt ----------------
add("P5-A", "P5", "A. Paling bisa dilakukan", "Autopilot instrumen aman, pensiun nyaman-plus",
    0.055, 0.055,
    gaji=seg((40, 49, 75)),
    tambahan=seg(),
    biaya=seg((40, 49, 15), (50, 75, NYAMAN_PLUS)),
    kesehatan=seg((50, 75, 2.0)),
    tinggal=seg((50, 75, RAWAT_RUMAH)),
    properti_income=seg(), jp=seg((65, 75, 4.4)),
    beli_aset=one(50, 1000), lain=seg(),
    ringkas="Gaya hidup tetap; 60 jt/bln ke SBN/RDPU/deposito; usia 50 beli rumah 1 M; pensiun nyaman-plus.")

add("P5-B", "P5", "B. Paling menguntungkan", "Properti produktif + 40% saham + bisnis; opsi pensiun dini / luar negeri",
    0.075, 0.06,
    gaji=seg((40, 49, 75)),
    tambahan=seg((42, 49, 5.0), (50, 59, 10.0)),
    biaya=seg((40, 49, 13), (50, 75, NYAMAN_PLUS)),
    kesehatan=seg((50, 75, 2.0)),
    tinggal=seg((50, 75, RAWAT_RUMAH)),
    properti_income=seg((44, 46, 5.6), (47, 75, 11.6)), jp=seg((65, 75, 4.4)),
    beli_aset={**one(43, 1500), 46: 1200}, lain=seg(),
    ringkas="Biaya 13 jt; usia 43 rumah kos 1,5 M; usia 46 kontrakan/ruko 1,2 M; bisnis 5-10 jt; portofolio 60/40.")

add("P5-C", "P5", "C. Saran saya", "Mandiri finansial lebih cepat, pensiun nyaman-plus + rumah kos",
    0.065, 0.055,
    gaji=seg((40, 49, 75)),
    tambahan=seg((50, 54, 5.0)),
    biaya=seg((40, 49, 14), (50, 75, NYAMAN_PLUS)),
    kesehatan=seg((50, 75, 2.0)),
    tinggal=seg((50, 75, RAWAT_RUMAH)),
    properti_income=seg((48, 49, 2.0), (51, 75, 5.6)), jp=seg((65, 75, 4.4)),
    beli_aset={**one(47, 1000), 50: 1500}, lain=seg(),
    ringkas="Biaya 14 jt; usia 47 beli rumah 1 M; usia 50 rumah kos 1,5 M; kerja/proyek opsional 5 jt s/d 54; portofolio 80/20.")
