# Proyek Pensiun Usia 50: 5 Profil × 3 Skenario

| File | Isi |
|---|---|
| `LAPORAN_PENSIUN.md` | Laporan lengkap: asumsi, fakta 2026, pilihan kota, investasi aman, keterampilan, opsi luar negeri, 15 skenario, uji ketahanan, rencana aksi, sumber |
| `Kalkulator_Pensiun.xlsx` | Kalkulator dengan formula hidup: Asumsi, Ringkasan, 15 sheet simulasi (P1-A s/d P5-C), Kalkulator Saya, Data Riset |
| `scenarios.py` | Definisi asumsi & 15 skenario (sumber kebenaran angka) |
| `model.py` | Simulasi Python (sama persis dengan rumus Excel); `python3 model.py` |
| `build_excel.py` | Membangun ulang Excel dari `scenarios.py`; `python3 build_excel.py` |

Hasil Excel sudah diverifikasi: 15 skenario dihitung ulang dengan LibreOffice dan cocok dengan model Python.
