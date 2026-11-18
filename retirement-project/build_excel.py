"""Bangun kalkulator Excel (formula hidup) dari definisi skenario.

Jalankan:  python3 build_excel.py   -> menghasilkan Kalkulator_Pensiun.xlsx
"""
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.workbook.defined_name import DefinedName

from scenarios import AGES, AGE_START, ASSUMPTIONS, PROFILES, RETIRE_AGE, SCENARIOS, YEAR_START

OUT = "Kalkulator_Pensiun.xlsx"
FIRST, LAST = 13, 13 + len(AGES) - 1  # baris data tabel tahunan

INPUT_FILL = PatternFill("solid", fgColor="FFF2CC")
HEAD_FILL = PatternFill("solid", fgColor="1F4E78")
OUT_FILL = PatternFill("solid", fgColor="E2EFDA")
WORK_FILL = PatternFill("solid", fgColor="F2F2F2")
BOLD = Font(bold=True)
WHITE = Font(bold=True, color="FFFFFF")
THIN = Border(*(Side(style="thin", color="BFBFBF"),) * 4)
NUM = "#,##0.0;[Red]-#,##0.0"
NUM0 = "#,##0;[Red]-#,##0"
PCT = "0.0%"

wb = Workbook()

# ------------------------------------------------------------------ Panduan
ws = wb.active
ws.title = "Panduan"
guide = [
    ("KALKULATOR PROYEK PENSIUN - 5 PROFIL x 3 SKENARIO", True),
    ("", False),
    ("Cara pakai", True),
    ("1. Semua angka dalam Rp JUTA dan NILAI HARI INI (2026). Kalkulator menaikkan otomatis dengan inflasi.", False),
    ("2. Sel KUNING = input yang boleh diubah. Sel HIJAU = hasil. Sel lain = rumus (jangan diubah).", False),
    ("3. Sheet 'Asumsi' = asumsi global (inflasi, kenaikan properti, JHT). Mengubahnya memengaruhi semua skenario.", False),
    ("4. Sheet 'Ringkasan' = perbandingan 15 skenario. Sheet P1-A ... P5-C = simulasi tahunan usia 40-75.", False),
    ("5. Sheet 'Kalkulator Saya' = isi data Anda sendiri di bagian atas; tabel tahunan terisi otomatis.", False),
    ("", False),
    ("Definisi kolom tabel tahunan (per bulan, nilai hari ini, kecuali disebut lain)", True),
    ("Gaji = penghasilan bersih rumah tangga (suami + istri) dari pekerjaan utama. Dasar iuran JHT.", False),
    ("Penghasilan tambahan = usaha sampingan, freelance, kerja paruh waktu, kerja di luar negeri.", False),
    ("Pemasukan properti = sewa kos/kontrakan bersih (setelah biaya, kekosongan, pajak).", False),
    ("JP BPJS = Jaminan Pensiun BPJS Ketenagakerjaan suami + istri (mulai usia pensiun JP, diasumsikan 65).", False),
    ("Biaya hidup = semua pengeluaran rutin. Fase kerja: termasuk sewa Jakarta & kesehatan. Fase pensiun: di luar tempat tinggal & kesehatan.", False),
    ("Tempat tinggal = sewa rumah, atau PBB + perawatan bila rumah milik sendiri.", False),
    ("Kesehatan = iuran BPJS + biaya berobat di luar BPJS + asuransi tambahan; naik dengan inflasi kesehatan.", False),
    ("Beli aset (sekaligus, Rp juta nilai hari ini) = harga rumah/kos/kontrakan; naik dengan kenaikan properti.", False),
    ("Lain-lain sekaligus = biaya/pemasukan satu kali (mis. biaya kursus & penempatan kerja luar negeri: negatif).", False),
    ("Saldo investasi = SBN ritel, deposito, reksa dana pasar uang, emas, saham sesuai imbal hasil yang dipilih.", False),
    ("", False),
    ("Membaca hasil", True),
    ("Saldo usia 75 positif = dana cukup. Negatif = dana habis sebelum 75 (lihat 'Usia dana habis').", False),
    ("'Tambahan per bulan' = tabungan/penghasilan ekstra yang harus ditambah SELAMA MASA KERJA (nilai hari ini) agar dana cukup s/d 75.", False),
    ("Nilai properti usia 75 = cadangan terakhir (bisa dijual/disewakan) bila umur lebih panjang dari 75.", False),
    ("", False),
    ("Catatan", True),
    ("Usia pensiun 50 sudah tertanam pada pola input skenario P1-A s/d P5-C. Untuk usia pensiun lain, gunakan 'Kalkulator Saya'.", False),
    ("Ini simulasi edukatif, bukan nasihat keuangan berlisensi. Imbal hasil masa depan tidak dijamin.", False),
]
for r, (txt, bold) in enumerate(guide, 1):
    c = ws.cell(r, 1, txt)
    if bold:
        c.font = Font(bold=True, size=13 if r == 1 else 11)
ws.column_dimensions["A"].width = 130

# ------------------------------------------------------------------ Asumsi
wa = wb.create_sheet("Asumsi")
wa["A1"] = "ASUMSI GLOBAL"
wa["A1"].font = Font(bold=True, size=13)
rows = [
    ("Inflasi", "Inflasi umum per tahun", ASSUMPTIONS["inflasi"], PCT,
     "BPS: inflasi Okt-2026 3,23% yoy; dipakai 4% agar konservatif"),
    ("InflasiKes", "Inflasi biaya kesehatan rumah tangga", ASSUMPTIONS["inflasi_kesehatan"], PCT,
     "Inflasi medis korporat 2026 15-18% (WTW/Mercer); rumah tangga dengan BPJS jauh lebih rendah"),
    ("NaikProperti", "Kenaikan harga properti per tahun", ASSUMPTIONS["kenaikan_properti"], PCT,
     "Rumah123: harga tawaran Semarang naik 6,2% yoy (Agu-2026)"),
    ("IuranJHT", "Iuran JHT (persen gaji)", ASSUMPTIONS["iuran_jht"], PCT, "3,7% pemberi kerja + 2% pekerja"),
    ("ImbalJHT", "Imbal hasil JHT per tahun", ASSUMPTIONS["imbal_jht"], PCT, "JHT konvensional 2025: 5,51%"),
    ("UsiaMulai", "Usia sekarang", AGE_START, "0", "Semua profil berusia 40 tahun"),
    ("UsiaPensiun", "Usia berhenti kerja (gaji tetap hilang)", RETIRE_AGE, "0", "Sesuai brief: pensiun 10 tahun lagi"),
    ("TahunMulai", "Tahun mulai", YEAR_START, "0", ""),
]
wa.append([])
wa.append(["Nama", "Keterangan", "Nilai", "Sumber / alasan"])
for c in wa[3]:
    c.font, c.fill = WHITE, HEAD_FILL
for i, (name, label, val, fmt, src) in enumerate(rows, 4):
    wa.cell(i, 1, name)
    wa.cell(i, 2, label)
    c = wa.cell(i, 3, val)
    c.number_format, c.fill = fmt, INPUT_FILL
    wa.cell(i, 4, src)
    wb.defined_names[name] = DefinedName(name, attr_text=f"Asumsi!$C${i}")
for col, w in zip("ABCD", (14, 42, 10, 90)):
    wa.column_dimensions[col].width = w

# ------------------------------------------------------------------ sheet simulasi
COLS = [  # (judul, lebar)
    ("Usia", 6), ("Tahun", 7), ("Fase", 8), ("Faktor inflasi", 9), ("Faktor inflasi kesehatan", 10),
    ("Gaji bersih RT /bln", 10), ("Penghasilan tambahan /bln", 11), ("Pemasukan properti /bln", 11),
    ("JP BPJS pasangan /bln", 10), ("Biaya hidup /bln", 10), ("Tempat tinggal /bln", 10),
    ("Kesehatan /bln", 10), ("Beli aset sekaligus (Rp jt)", 11), ("Lain-lain sekaligus (Rp jt)", 11),
    ("Iuran JHT setahun (nominal)", 11), ("Saldo JHT (nominal)", 11), ("JHT dicairkan (nominal)", 11),
    ("Arus kas bersih setahun (nominal)", 13), ("Imbal hasil", 8), ("Saldo investasi (nominal)", 13),
    ("Saldo investasi (nilai hari ini)", 13), ("Nilai properti (nominal)", 12),
    ("Kekayaan bersih (nilai hari ini)", 13), ("Indeks pertumbuhan", 10), ("Faktor tambahan", 10),
]
INPUT_KEYS = ["gaji", "tambahan", "properti_income", "jp", "biaya", "tinggal", "kesehatan", "beli_aset", "lain"]


def build_sim(ws, title, subtitle, note, r_acc, r_ret, inputs=None, header_formulas=None):
    """inputs: dict key->dict(age->value) (nilai statis), atau None bila pakai header_formulas."""
    ws["A1"] = title
    ws["A1"].font = Font(bold=True, size=13)
    ws["A2"] = subtitle
    ws["A2"].font = BOLD
    ws["A3"] = note
    ws["A3"].alignment = Alignment(wrap_text=False)
    ws["A5"], ws["A6"] = "Imbal hasil investasi fase kerja", "Imbal hasil investasi fase pensiun"
    for r, v in ((5, r_acc), (6, r_ret)):
        c = ws.cell(r, 3, v)
        c.number_format, c.fill = PCT, INPUT_FILL
    outs = [
        ("Saldo investasi usia 49 (nilai hari ini, Rp jt)",
         f"=INDEX($U${FIRST}:$U${LAST},MATCH(UsiaPensiun-1,$A${FIRST}:$A${LAST},0))"),
        ("JHT dicairkan usia 50 (nilai hari ini, Rp jt)",
         f"=INDEX($Q${FIRST}:$Q${LAST},MATCH(UsiaPensiun,$A${FIRST}:$A${LAST},0))"
         f"/INDEX($D${FIRST}:$D${LAST},MATCH(UsiaPensiun,$A${FIRST}:$A${LAST},0))"),
        ("Saldo investasi usia 75 (nilai hari ini, Rp jt)", f"=$U${LAST}"),
        ("Nilai properti usia 75 (nilai hari ini, Rp jt)", f"=$V${LAST}/$D${LAST}"),
        ("Usia dana investasi habis",
         f'=IF(MIN($Z${FIRST}:$Z${LAST})=999,"Cukup s/d 75",MIN($Z${FIRST}:$Z${LAST}))'),
        ("Tambahan tabungan/penghasilan per bulan selama kerja agar cukup s/d 75 (nilai hari ini, Rp jt)",
         f"=IF(SUM($Y${FIRST}:$Y${LAST})=0,0,MAX(0,-$T${LAST})/SUM($Y${FIRST}:$Y${LAST}))"),
    ]
    for i, (lab, f) in enumerate(outs):
        ws.cell(5 + i, 5, lab)
        c = ws.cell(5 + i, 11, f)
        c.fill, c.font = OUT_FILL, BOLD
        c.number_format = NUM0
    hr = FIRST - 1
    for j, (name, width) in enumerate(COLS, 1):
        c = ws.cell(hr, j, name)
        c.font, c.fill, c.border = WHITE, HEAD_FILL, THIN
        c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
        ws.column_dimensions[get_column_letter(j)].width = width
    ws.row_dimensions[hr].height = 58
    in_cols = "FGHIJKLMN"
    for k, age in enumerate(AGES):
        r = FIRST + k
        p = r - 1
        ws.cell(r, 1, age)
        ws.cell(r, 2, f"=TahunMulai+A{r}-UsiaMulai")
        ws.cell(r, 3, f'=IF(A{r}<UsiaPensiun,"Kerja","Pensiun")')
        ws.cell(r, 4, f"=(1+Inflasi)^(A{r}-UsiaMulai)")
        ws.cell(r, 5, f"=(1+InflasiKes)^(A{r}-UsiaMulai)")
        for col, key in zip(in_cols, INPUT_KEYS):
            if inputs is not None:
                v = inputs[key][age]
                ws[f"{col}{r}"] = v
            else:
                ws[f"{col}{r}"] = header_formulas[key].format(r=r)
            ws[f"{col}{r}"].fill = INPUT_FILL if inputs is not None else PatternFill()
        ws[f"O{r}"] = f'=IF(C{r}="Kerja",IuranJHT*F{r}*12*D{r},0)'
        ws[f"P{r}"] = (f'=IF(C{r}="Kerja",O{r},0)' if k == 0
                       else f'=IF(C{r}="Kerja",P{p}*(1+ImbalJHT)+O{r},0)')
        ws[f"Q{r}"] = "=0" if k == 0 else f"=IF(A{r}=UsiaPensiun,P{p},0)"
        ws[f"R{r}"] = (f"=12*D{r}*(F{r}+G{r}+H{r}+I{r}-J{r}-K{r})-12*E{r}*L{r}"
                       f"-M{r}*(1+NaikProperti)^(A{r}-UsiaMulai)+N{r}*D{r}+Q{r}")
        ws[f"S{r}"] = f'=IF(C{r}="Kerja",$C$5,$C$6)'
        ws[f"T{r}"] = (f"=R{r}*(1+S{r}/2)" if k == 0 else f"=T{p}*(1+S{r})+R{r}*(1+S{r}/2)")
        ws[f"U{r}"] = f"=T{r}/D{r}"
        ws[f"V{r}"] = (f"=M{r}*(1+NaikProperti)^(A{r}-UsiaMulai)" if k == 0
                       else f"=V{p}*(1+NaikProperti)+M{r}*(1+NaikProperti)^(A{r}-UsiaMulai)")
        ws[f"W{r}"] = f"=(T{r}+V{r})/D{r}"
        ws[f"X{r}"] = f"=1+S{r}" if k == 0 else f"=X{p}*(1+S{r})"
        ws[f"Y{r}"] = f'=IF(C{r}="Kerja",12*D{r}*(1+S{r}/2)*$X${LAST}/X{r},0)'
        ws[f"Z{r}"] = f'=IF(AND(T{r}<0,A{r}>=UsiaPensiun),A{r},999)'
        for j in range(1, len(COLS) + 1):
            c = ws.cell(r, j)
            c.border = THIN
            if j in (4, 5, 24, 25, 26):
                c.number_format = "0.000"
            elif j == 19:
                c.number_format = PCT
            elif j >= 6:
                c.number_format = NUM
        if age < RETIRE_AGE:
            for j in (1, 2, 3):
                ws.cell(r, j).fill = WORK_FILL
    ws.freeze_panes = ws.cell(FIRST, 4)


for s in SCENARIOS:
    w = wb.create_sheet(s["code"])
    prof = PROFILES[s["profile"]]
    build_sim(w, f"{s['code']} | {prof['nama']} | biaya Jakarta saat ini Rp{prof['biaya_jkt']} jt/bln",
              f"{s['label']}: {s['judul']}", s["ringkas"], s["r_acc"], s["r_ret"],
              inputs={k: s[k] for k in INPUT_KEYS})

# ------------------------------------------------------------------ Kalkulator Saya
wk = wb.create_sheet("Kalkulator Saya")
params = [  # (label, nilai default, format)
    ("Gaji bersih rumah tangga sekarang (Rp jt/bln)", 30, NUM),
    ("Biaya hidup sekarang termasuk sewa (Rp jt/bln)", 12, NUM),
    ("Penghasilan tambahan selama masih kerja (Rp jt/bln)", 2, NUM),
    ("Mulai penghasilan tambahan pada usia", 42, "0"),
    ("Biaya hidup pensiun di luar rumah & kesehatan (Rp jt/bln)", 6, NUM),
    ("Biaya kesehatan saat pensiun (Rp jt/bln)", 1, NUM),
    ("Tempat tinggal saat pensiun: sewa ATAU PBB+perawatan (Rp jt/bln)", 0.3, NUM),
    ("Penghasilan setelah usia pensiun (Rp jt/bln)", 3, NUM),
    ("Penghasilan setelah pensiun berlangsung s/d usia", 59, "0"),
    ("Jaminan Pensiun BPJS suami+istri (Rp jt/bln)", 4.4, NUM),
    ("JP mulai usia", 65, "0"),
    ("Harga rumah/properti yang dibeli (Rp jt, nilai hari ini)", 650, NUM),
    ("Dibeli pada usia", 50, "0"),
    ("Pemasukan sewa bersih dari properti tsb (Rp jt/bln, 0 bila ditempati)", 0, NUM),
]
# parameter di kolom AA-AB agar tidak bertabrakan dengan tabel tahunan (A-Y)
wk_inputs = {}
for i, (lab, val, fmt) in enumerate(params):
    r = 5 + i
    wk.cell(r, 27, lab)
    c = wk.cell(r, 28, val)
    c.fill, c.number_format = INPUT_FILL, fmt
    wk_inputs[i] = f"$AB${r}"
P = wk_inputs
hf = {
    "gaji": f'=IF(A{{r}}<UsiaPensiun,{P[0]},0)',
    "tambahan": f'=IF(AND(A{{r}}<UsiaPensiun,A{{r}}>={P[3]}),{P[2]},0)+IF(AND(A{{r}}>=UsiaPensiun,A{{r}}<={P[8]}),{P[7]},0)',
    "properti_income": f'=IF(A{{r}}>{P[12]},{P[13]},0)',
    "jp": f'=IF(A{{r}}>={P[10]},{P[9]},0)',
    "biaya": f'=IF(A{{r}}<UsiaPensiun,{P[1]},{P[4]})',
    "tinggal": f'=IF(A{{r}}>=UsiaPensiun,{P[6]},0)',
    "kesehatan": f'=IF(A{{r}}>=UsiaPensiun,{P[5]},0)',
    "beli_aset": f'=IF(A{{r}}={P[12]},{P[11]},0)',
    "lain": "=0",
}
build_sim(wk, "KALKULATOR SAYA - isi sel kuning di kolom AA-AB (geser ke kanan) dan imbal hasil di C5:C6",
          "Tabel tahunan di bawah terisi otomatis dari parameter. Usia pensiun diatur di sheet Asumsi.",
          "Tips: coba ubah usia pensiun, biaya hidup pensiun, atau penghasilan setelah pensiun, lalu lihat hasil di kolom K.",
          0.06, 0.055, inputs=None, header_formulas=hf)
wk.column_dimensions["AA"].width = 62
wk.column_dimensions["AB"].width = 10
wk["AA4"] = "PARAMETER ANDA (isi sel kuning)"
wk["AA4"].font = BOLD

# ------------------------------------------------------------------ Ringkasan
wr = wb.create_sheet("Ringkasan", 1)
wr["A1"] = "RINGKASAN 15 SKENARIO (Rp juta, nilai hari ini 2026)"
wr["A1"].font = Font(bold=True, size=13)
heads = ["Kode", "Profil", "Skenario", "Strategi", "Saldo investasi usia 49", "JHT cair usia 50",
         "Saldo investasi usia 75", "Nilai properti usia 75", "Usia dana habis",
         "Tambahan per bulan agar cukup", "Ringkasan langkah"]
for j, h in enumerate(heads, 1):
    c = wr.cell(3, j, h)
    c.font, c.fill, c.border = WHITE, HEAD_FILL, THIN
    c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
wr.row_dimensions[3].height = 45
for i, s in enumerate(SCENARIOS, 4):
    sh = f"'{s['code']}'"
    vals = [s["code"], PROFILES[s["profile"]]["nama"], s["label"], s["judul"],
            f"={sh}!K5", f"={sh}!K6", f"={sh}!K7", f"={sh}!K8", f"={sh}!K9", f"={sh}!K10", s["ringkas"]]
    for j, v in enumerate(vals, 1):
        c = wr.cell(i, j, v)
        c.border = THIN
        c.alignment = Alignment(wrap_text=True, vertical="top")
        if 5 <= j <= 10:
            c.number_format = NUM0 if j != 10 else NUM
            c.fill = OUT_FILL
for col, w in zip("ABCDEFGHIJK", (7, 26, 22, 42, 12, 10, 12, 12, 11, 12, 90)):
    wr.column_dimensions[col].width = w
wr.freeze_panes = "B4"

# ------------------------------------------------------------------ Data Riset
wd = wb.create_sheet("Data Riset")
wd["A1"] = "DATA PASAR & REFERENSI (per November 2026)"
wd["A1"].font = Font(bold=True, size=13)
data = [
    ("Instrumen / data", "Angka", "Risiko harga turun dalam?", "Catatan"),
    ("BI-Rate", "5,75%", "-", "Ditahan Sep & Okt 2026"),
    ("Bunga penjaminan LPS (bank umum)", "3,75%", "Tidak (dijamin s/d Rp2 M/bank/nasabah bila bunga <= 3,75%)", "Berlaku Okt-2026 s/d Jan-2027"),
    ("Bunga penjaminan LPS (BPR)", "6,25%", "Tidak, selama bunga <= batas & syarat LPS terpenuhi", "Pilih BPR sehat; patuhi batas bunga"),
    ("ORI030 (kupon tetap)", "6,90% (3 th) / 7,00% (6 th)", "Tidak bila dipegang s/d jatuh tempo", "Dijamin negara; pajak kupon 10%"),
    ("SR025 (sukuk, kupon tetap)", "6,80% (3 th) / 6,90% (5 th)", "Tidak bila dipegang s/d jatuh tempo", "Syariah"),
    ("SBR015 (kupon mengambang, ada batas bawah)", "6,75%-6,85% awal", "Tidak - tidak bisa dijual di pasar sekunder, nilai pokok tetap", "Kupon bulanan; early redemption terbatas"),
    ("ST016 (kupon mengambang)", "6,05% / 6,25% awal", "Tidak - nilai pokok tetap", "ST017 ditawarkan 6 Nov - 2 Des 2026"),
    ("Reksa dana pasar uang", "4-5,5% per tahun", "Sangat kecil", "Untuk dana darurat & parkir sementara"),
    ("JHT BPJS (konvensional)", "5,51% (2025)", "Tidak", "Bisa dicairkan saat berhenti kerja"),
    ("Emas Antam", "~Rp2,5 jt/gram; buyback ~Rp2,29 jt", "YA - Jan-2026 turun 12% sehari; 2011-2015 turun ~44% (USD)", "Selisih jual-beli ~9%; maks 10-15% portofolio"),
    ("Saham / reksa dana indeks", "harapan 8-10% jangka panjang", "YA - bisa turun 30-50%", "Hanya untuk dana >5 tahun"),
    ("Inflasi umum", "3,23% yoy (Okt-2026)", "-", "Model memakai 4%"),
    ("Inflasi medis (korporat)", "15,1% (WTW) - 17,8% (Mercer)", "-", "Angka klaim asuransi korporat, bukan biaya rumah tangga"),
    ("Kurs", "~Rp18.200/USD; ~Rp106/JPY", "-", "Rupiah melemah ~1,8% sebulan (Nov-2026)"),
    ("UMP DKI Jakarta 2026", "Rp5,73 jt", "-", ""),
    ("UMK Kota Semarang 2026", "Rp3,70 jt", "-", "UMP Jateng Rp2,33 jt"),
    ("Biaya hidup Jakarta (SBH BPS 2022)", "Rp14,88 jt/rumah tangga", "-", "Rata-rata RT 2-6 orang"),
    ("Sewa rumah sederhana Semarang", "Rp12-25 jt/tahun", "-", "Banyumanik/Pedurungan, tipe 36-72"),
    ("Harga rumah Semarang", "median tawaran Rp1,7 M; rumah sederhana pinggiran Rp300-700 jt", "-", "Rumah123 Agu-2026; subsidi ~Rp150-185 jt"),
    ("Rumah kos dekat Undip Tembalang", "Rp1,5-1,6 M (8-10 kamar)", "-", "Listing penjual; verifikasi okupansi"),
    ("BPJS Kesehatan mandiri", "Kls 1 Rp150rb, Kls 2 Rp100rb, Kls 3 Rp35rb /orang", "-", "KRIS belum berlaku penuh"),
    ("Gaji penerjemah Mandarin", "Rp4-19 jt/bln", "-", "Umumnya minta HSK 4-5"),
    ("Gaji Tokutei Ginou kaigo (Jepang)", "¥175-200 rb pokok; bawa pulang ~¥175-185 rb", "-", "Tidak ada batas usia atas resmi; praktiknya pemberi kerja memilih yang lebih muda"),
]
for i, row in enumerate(data, 3):
    for j, v in enumerate(row, 1):
        c = wd.cell(i, j, v)
        c.border = THIN
        c.alignment = Alignment(wrap_text=True, vertical="top")
        if i == 3:
            c.font, c.fill = WHITE, HEAD_FILL
for col, w in zip("ABCD", (40, 34, 50, 50)):
    wd.column_dimensions[col].width = w

wb.save(OUT)
print("saved", OUT)
