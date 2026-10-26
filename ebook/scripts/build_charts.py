"""Bangun semua data CSV dan grafik SVG untuk ebook "Membaca Dunia 2026".

Semua angka di grafik berasal dari tabel DATA di bawah, dan setiap tabel
punya sumber. Jalankan: python3 ebook/scripts/build_charts.py
"""
import csv
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")
CHART_DIR = os.path.join(ROOT, "charts")
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(CHART_DIR, exist_ok=True)

# ---------------------------------------------------------------- style
INK = "#16233a"
SOFT = "#5b6878"
RULE = "#d5dbe2"
TEAL = "#1f6f78"
AMBER = "#c8811a"
RED = "#a63d40"
GREEN = "#3c7a4a"
NAVY = "#2e4a7d"
PLUM = "#6b4c8a"
OLIVE = "#7b7d2a"
SERIES = [NAVY, TEAL, AMBER, RED, PLUM, GREEN, OLIVE]

for f in font_manager.findSystemFonts():
    if "Inter" in f:
        try:
            font_manager.fontManager.addfont(f)
        except Exception:
            pass

plt.rcParams.update({
    "font.family": "Inter",
    "font.size": 9.5,
    "svg.fonttype": "none",
    "axes.edgecolor": RULE,
    "axes.labelcolor": SOFT,
    "axes.titlesize": 11,
    "axes.titleweight": "bold",
    "axes.titlecolor": INK,
    "axes.titlelocation": "left",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.color": "#eceff3",
    "grid.linewidth": 0.8,
    "xtick.color": SOFT,
    "ytick.color": SOFT,
    "legend.frameon": False,
    "figure.dpi": 100,
    "axes.axisbelow": True,
})


def save(fig, name, source):
    fig.canvas.draw()
    bottom = min(a.get_tightbbox(fig.canvas.get_renderer()).transformed(fig.transFigure.inverted()).y0
                 for a in fig.axes)
    fig.text(0.0, bottom - 0.02, "Sumber: " + source, fontsize=7.5, color=SOFT, ha="left", va="top",
             wrap=True)
    fig.savefig(os.path.join(CHART_DIR, name + ".svg"), bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)


def write_csv(name, header, rows, source):
    with open(os.path.join(DATA_DIR, name + ".csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(header + ["sumber"])
        for r in rows:
            w.writerow(list(r) + [source])


YEARS = list(range(2014, 2025))

# ---------------------------------------------------------------- 1. PDB
GDP = {
    "AS": [2.5, 3.1, 1.7, 2.3, 2.9, 2.3, -2.8, 5.9, 2.1, 2.5, 2.8],
    "China": [7.4, 7.0, 6.7, 6.9, 6.7, 6.1, 2.2, 8.4, 3.0, 5.2, 5.0],
    "Zona Euro": [1.4, 2.1, 1.9, 2.7, 1.8, 1.6, -5.9, 5.4, 3.5, 0.4, 0.9],
    "Indonesia": [5.0, 4.9, 5.0, 5.1, 5.2, 5.0, -2.1, 3.7, 5.3, 5.1, 5.0],
    # India: tahun fiskal; 2019 dikoreksi dari 6,0% (buku) ke 4,0% (revisi resmi FY2019-20)
    "India": [7.4, 7.9, 8.3, 6.8, 6.5, 4.0, -5.8, 9.1, 7.2, 8.2, 7.0],
}
SRC_GDP = "IMF WEO (via buku Vol. 1); India 2019 dikoreksi ke 4,0% (MoSPI, revisi Jan 2021)"
write_csv("pdb_riil", ["negara"] + YEARS, [[k] + v for k, v in GDP.items()], SRC_GDP)

fig, ax = plt.subplots(figsize=(7.2, 3.4))
for (name, vals), c in zip(GDP.items(), SERIES):
    ax.plot(YEARS, vals, marker="o", ms=3.5, lw=1.8, color=c, label=name)
ax.axhline(0, color=SOFT, lw=0.8)
ax.annotate("COVID-19", xy=(2020, -5.9), xytext=(2017.6, -5.2), color=SOFT, fontsize=8,
            arrowprops=dict(arrowstyle="-", color=SOFT, lw=0.7))
ax.annotate("India 2019: 4,0%\n(buku: 6,0%)", xy=(2019, 4.0), xytext=(2014.1, -3.6), color=RED, fontsize=7.5,
            arrowprops=dict(arrowstyle="-", color=RED, lw=0.7))
ax.set_ylabel("% per tahun")
ax.set_xticks(YEARS)
ax.set_title("Pertumbuhan PDB riil 2014–2024")
ax.legend(ncol=5, loc="upper center", bbox_to_anchor=(0.5, -0.1), fontsize=8)
save(fig, "c01_pdb", SRC_GDP)

# ---------------------------------------------------------------- 2. PDB terkini 2026
LATEST = [
    ("India (Apr–Jun 2026, yoy)", 7.8), ("Indonesia (Q2 2026, yoy)", 5.29), ("China (Q3 2026, yoy)", 4.5),
    ("AS (Q3 2026, estimasi GDPNow)", 3.5), ("Zona Euro (proyeksi ECB 2026)", 0.9),
    ("Dubai (H1 2026)", -2.3), ("Arab Saudi (proyeksi 2026)", -3.6),
]
SRC_LATEST = "MoSPI; BPS; NBS; Atlanta Fed GDPNow; ECB (Sep 2026); Dubai Statistics Center; Kemenkeu Saudi (30 Sep 2026)"
write_csv("pdb_terkini_2026", ["ukuran", "persen"], LATEST, SRC_LATEST)
fig, ax = plt.subplots(figsize=(7.2, 3.0))
labels = [x[0] for x in LATEST][::-1]
vals = [x[1] for x in LATEST][::-1]
ax.barh(labels, vals, color=[RED if v < 0 else TEAL for v in vals], height=0.6)
for i, v in enumerate(vals):
    ax.text(v + (0.15 if v >= 0 else -0.15), i, f"{v:+.1f}%".replace(".", ","), va="center",
            ha="left" if v >= 0 else "right", fontsize=8.5, color=INK)
ax.axvline(0, color=SOFT, lw=0.8)
ax.set_xlim(-5.5, 9.5)
ax.grid(axis="y", visible=False)
ax.set_title("Pertumbuhan terkini 2026: India memimpin, Teluk terpukul perang")
save(fig, "c02_pdb_2026", SRC_LATEST)

# ---------------------------------------------------------------- 3. Heatmap return aset
RET = {
    "S&P 500": [13.7, 1.4, 12.0, 21.8, -4.4, 31.5, 18.4, 28.7, -18.1, 26.3, 25.0],
    "IHSG": [22.3, -12.1, 15.3, 20.0, -2.5, 1.7, -5.1, 10.1, 4.1, 6.2, -2.65],
    "MSCI EM": [-2.2, -14.9, 11.2, 37.3, -14.6, 18.4, 18.3, -2.5, -20.1, 9.8, 7.5],
    "Emas": [-0.2, -10.4, 8.1, 13.1, -1.6, 18.3, 25.1, -3.6, -0.3, 13.1, 27.2],
    "Bitcoin": [-57.6, 34.5, 123.8, 1369.0, -73.6, 92.2, 303.2, 59.7, -64.3, 155.4, 121.1],
}
SRC_RET = ("S&P 500 & MSCI EM: total return (buku Vol. 1, cocok dgn data S&P/MSCI); IHSG: BEI/OJK "
           "(2024 dikoreksi ke −2,65%); Emas: spot akhir tahun (LBMA/JM Bullion, ±1–2 poin antarsumber); "
           "Bitcoin: dihitung dari harga penutupan akhir tahun CoinMarketCap")
write_csv("return_tahunan", ["aset"] + YEARS, [[k] + v for k, v in RET.items()], SRC_RET)
fig, ax = plt.subplots(figsize=(7.4, 2.9))
import numpy as np  # noqa: E402
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm  # noqa: E402

cmap = LinearSegmentedColormap.from_list("rg", [RED, "#f3d9d6", "#ffffff", "#d6ebe6", GREEN])
arr = np.array([RET[k] for k in RET])
ax.imshow(np.clip(arr, -40, 40), cmap=cmap, norm=TwoSlopeNorm(0, -40, 40), aspect="auto")
for i, k in enumerate(RET):
    for j, v in enumerate(RET[k]):
        txt = f"{v:+.0f}" if abs(v) >= 100 else f"{v:+.1f}"
        color = RED if (k == "IHSG" and YEARS[j] == 2024) else INK
        weight = "bold" if (k == "IHSG" and YEARS[j] == 2024) else "normal"
        ax.text(j, i, txt.replace(".", ","), ha="center", va="center", fontsize=7.6, color=color, weight=weight)
ax.set_xticks(range(len(YEARS)))
ax.set_xticklabels(YEARS, fontsize=8)
ax.set_yticks(range(len(RET)))
ax.set_yticklabels(list(RET), fontsize=8.5)
ax.grid(False)
for s in ax.spines.values():
    s.set_visible(False)
ax.tick_params(length=0)
ax.set_title("Return tahunan (%): hijau = naik, merah = turun (warna dibatasi ±40%)")
ax.add_patch(plt.Rectangle((9.5, 0.5), 1, 1, fill=False, ec=RED, lw=1.6))
save(fig, "c03_return_heatmap", SRC_RET)

# ---------------------------------------------------------------- 4. IHSG & IDR
IHSG = [("2014", 5227), ("2015", 4593), ("2016", 5297), ("2017", 6356), ("2018", 6195), ("2019", 6300),
        ("2020", 5979), ("2021", 6581), ("2022", 6851), ("2023", 7273), ("2024", 7080), ("2025", 8647),
        ("Okt 2026", 5388)]
IDR = [12440, 13795, 13436, 13548, 14481, 13901, 14105, 14269, 15568, 15399, 16157, 16680, 18071]
SRC_II = ("IHSG: penutupan akhir tahun BEI via Bisnis/Bareksa/Investortrust; 22 Okt 2026: RRI. "
          "USD/IDR: spot akhir tahun (Bloomberg via media; 2024–2025 Investortrust/Antara); 22 Okt 2026: Databoks")
write_csv("ihsg_idr", ["periode", "ihsg", "usd_idr"], [(a, b, c) for (a, b), c in zip(IHSG, IDR)], SRC_II)
fig, ax = plt.subplots(figsize=(7.2, 3.3))
x = range(len(IHSG))
ax.bar(x, [v for _, v in IHSG], color=[RED if p == "Okt 2026" else "#9fb4cf" for p, _ in IHSG], width=0.62,
       label="IHSG (kiri)")
ax.set_xticks(list(x))
ax.set_xticklabels([p for p, _ in IHSG], fontsize=7.6, rotation=0)
ax.set_ylim(0, 10000)
ax.set_ylabel("IHSG")
for i, (_, v) in enumerate(IHSG):
    if i in (11, 12):
        ax.text(i, v + 180, f"{v:,}".replace(",", "."), ha="center", fontsize=7.6, color=INK, weight="bold")
ax2 = ax.twinx()
ax2.plot(list(x), IDR, color=AMBER, marker="o", ms=3.5, lw=2, label="USD/IDR (kanan)")
ax2.set_ylim(11000, 19500)
ax2.grid(False)
ax2.spines["right"].set_visible(True)
ax2.set_ylabel("Rp per US$")
ax2.text(12, 18071 + 350, "±18.071", ha="center", fontsize=7.6, color=AMBER, weight="bold")
ax.set_title("IHSG vs rupiah: 2026 menghapus seluruh kenaikan 2025")
h1, l1 = ax.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=8)
save(fig, "c04_ihsg_idr", SRC_II)

# ---------------------------------------------------------------- 5. VIX per episode
VIX = [("Krimea (Mar 2014)", 18), ("Devaluasi yuan (Agu 2015)", 40.7), ("Brexit (Jun 2016)", 25.8),
       ("'Volmageddon' (Feb 2018)", 37.3), ("Perang dagang (Des 2018)", 36.1), ("COVID-19 (Mar 2020)", 82.69),
       ("Invasi Ukraina (Mar 2022)", 36.5), ("Unwind carry yen (Agu 2024)", 38.57),
       ("Tarif 'Liberation Day' (Apr 2025)", 52.33), ("Perang Iran, VIX Okt 2026", 21)]
SRC_VIX = ("CBOE (penutupan tertinggi per episode, dibulatkan); COVID 82,69: CNBC; Agu 2024 & Apr 2025: Macroption; "
           "Okt 2026 ±16–21: liputan pasar 16 Okt 2026")
write_csv("vix_episode", ["episode", "vix_puncak"], VIX, SRC_VIX)
fig, ax = plt.subplots(figsize=(7.2, 3.4))
lab = [a for a, _ in VIX][::-1]
val = [b for _, b in VIX][::-1]
colors = [RED if "COVID" in a else (AMBER if "Iran" in a else NAVY) for a in lab]
ax.barh(lab, val, color=colors, height=0.62)
for i, v in enumerate(val):
    ax.text(v + 1, i, f"{v:.1f}".replace(".", ","), va="center", fontsize=8, color=INK)
ax.axvline(30, color=SOFT, ls="--", lw=0.8)
ax.text(30.5, 9.4, "ambang 'panik' ±30", fontsize=7.5, color=SOFT)
ax.set_xlim(0, 92)
ax.grid(axis="y", visible=False)
ax.set_title("Puncak VIX per episode: perang Iran 2026 hampir tak terlihat di VIX")
save(fig, "c05_vix", SRC_VIX)

# ---------------------------------------------------------------- 6. AI: klaim buku vs data
fig, ax = plt.subplots(figsize=(7.2, 2.9))
cats = ["AS 2023", "China 2023", "AS 2024", "China 2024"]
book = [103, 68, 120, 80]
hai = [67.2, 7.8, 109.1, 9.3]
xx = np.arange(len(cats))
ax.bar(xx - 0.18, book, 0.36, color="#d9b8b9", label="Klaim buku Vol. 1")
ax.bar(xx + 0.18, hai, 0.36, color=NAVY, label="Stanford HAI AI Index (investasi swasta)")
for i in range(len(cats)):
    ax.text(i - 0.18, book[i] + 2, f"{book[i]}", ha="center", fontsize=8, color=RED)
    ax.text(i + 0.18, hai[i] + 2, f"{hai[i]:.1f}".replace(".", ","), ha="center", fontsize=8, color=INK, weight="bold")
ax.set_xticks(xx)
ax.set_xticklabels(cats)
ax.set_ylabel("US$ miliar")
ax.set_ylim(0, 150)
ax.legend(loc="upper center", ncol=2, fontsize=8)
ax.set_title("Investasi AI: buku melebih-lebihkan China sampai ±9 kali")
SRC_AI = "Stanford HAI, AI Index 2024 & 2025 (bab Economy)"
write_csv("investasi_ai", ["kategori", "klaim_buku", "stanford_hai"], list(zip(cats, book, hai)), SRC_AI)
save(fig, "c06_ai", SRC_AI)

# ---------------------------------------------------------------- 7. Penjualan chip
CHIP = [335.8, 335.2, 338.9, 412.2, 468.8, 412.3, 440.4, 555.9, 574.1, 526.8, 627.6]
SRC_CHIP = "WSTS via SIA (2024: US$627,6 miliar; kemudian direvisi ke 630,5)"
write_csv("penjualan_chip", ["tahun", "usd_miliar"], list(zip(YEARS, CHIP)), SRC_CHIP)
fig, ax = plt.subplots(figsize=(7.2, 2.8))
ax.bar(YEARS, CHIP, color=[TEAL if y != 2024 else NAVY for y in YEARS], width=0.65)
for y, v in zip(YEARS, CHIP):
    ax.text(y, v + 8, f"{v:.0f}", ha="center", fontsize=7.6, color=INK)
ax.set_xticks(YEARS)
ax.set_ylim(0, 700)
ax.set_ylabel("US$ miliar")
ax.set_title("Penjualan semikonduktor global: rekor 2024 berkat AI")
save(fig, "c07_chip", SRC_CHIP)

# ---------------------------------------------------------------- 8. Komposisi cadangan devisa
fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.4, 3.0), gridspec_kw={"width_ratios": [1, 1.35]})
comp = [("USD", 56.7), ("EUR", 20.6), ("CNY", 2.1), ("Lainnya", 20.6)]
a1.pie([v for _, v in comp], colors=[NAVY, TEAL, RED, "#c9d2dc"], startangle=90, counterclock=False,
       wedgeprops=dict(width=0.38, edgecolor="white"))
a1.text(0, 0, "Q2\n2026", ha="center", va="center", fontsize=9, color=INK, weight="bold")
a1.legend([f"{a}  {str(b).replace('.', ',')}%" for a, b in comp], loc="upper center", bbox_to_anchor=(0.5, 0.02),
          fontsize=7.6, ncol=2)
a1.set_title("Komposisi cadangan devisa dunia")
pts = [("Q4 2024", 57.80), ("Q1 2025", 57.79), ("Q2 2025", 57.08), ("Q3 2025", 56.92),
       ("Q1 2026", 57.18), ("Q2 2026", 56.70)]
a2.plot(range(len(pts)), [v for _, v in pts], color=NAVY, marker="o", lw=2)
a2.set_xticks(range(len(pts)))
a2.set_xticklabels([p for p, _ in pts], fontsize=7, rotation=30)
for i, (_, v) in enumerate(pts):
    a2.text(i, v + 0.8, f"{v:.1f}".replace(".", ","), ha="center", fontsize=7.4, color=INK)
a2.axhline(71, color=SOFT, ls="--", lw=0.8)
a2.text(0, 71.5, "±71% sekitar 1999–2000", fontsize=7.4, color=SOFT)
a2.set_ylim(50, 75)
a2.set_title("Porsi USD (%)")
SRC_RES = "IMF COFER (rilis Q4 2024 s.d. Q2 2026); ±71% sekitar 1999–2000 menurut IMF/CEPR"
write_csv("cadangan_devisa", ["periode", "porsi_usd"], pts, SRC_RES)
fig.text(0.01, -0.16, "Sumber: " + SRC_RES, fontsize=7.5, color=SOFT)
fig.savefig(os.path.join(CHART_DIR, "c08_cadangan.svg"), bbox_inches="tight", pad_inches=0.15)
plt.close(fig)

# ---------------------------------------------------------------- 9. Pembelian emas bank sentral
CB = [("Rata-rata\n2010–2021", 473), ("2018", 656), ("2022", 1082), ("2023", 1037), ("2024", 1045), ("2025", 863)]
SRC_CB = "World Gold Council, Gold Demand Trends (FY2022–FY2025); rata-rata 2010–2021 per WGC via media"
write_csv("emas_bank_sentral", ["periode", "ton"], CB, SRC_CB)
fig, ax = plt.subplots(figsize=(7.2, 2.9))
ax.bar(range(len(CB)), [v for _, v in CB], color=["#c9d2dc", "#9fb4cf", AMBER, AMBER, AMBER, TEAL], width=0.62)
for i, (_, v) in enumerate(CB):
    ax.text(i, v + 20, f"{v:,}".replace(",", "."), ha="center", fontsize=8.5, color=INK, weight="bold")
ax.set_xticks(range(len(CB)))
ax.set_xticklabels([p for p, _ in CB], fontsize=8)
ax.set_ylim(0, 1250)
ax.set_ylabel("ton")
ax.annotate("Pembekuan cadangan Rusia\n(Feb 2022)", xy=(2, 1082), xytext=(0.2, 960), fontsize=7.5, color=SOFT,
            arrowprops=dict(arrowstyle="-", color=SOFT, lw=0.7))
ax.text(5, 960, "Q2 2026 saja:\n289 ton (rekor Q2)", ha="center", fontsize=7.5, color=TEAL)
ax.set_title("Bank sentral memborong emas sejak sanksi 2022")
save(fig, "c09_emas_bank_sentral", SRC_CB)

# ---------------------------------------------------------------- 10. Bitcoin (log)
BTC = [("2014", 320), ("2015", 431), ("2016", 964), ("2017", 14156), ("2018", 3743), ("2019", 7194),
       ("2020", 29002), ("2021", 46306), ("2022", 16547), ("2023", 42265), ("2024", 93429),
       ("Okt 2025\npuncak", 126210), ("Jun 2026\nterendah", 58900), ("23 Okt\n2026", 81546)]
SRC_BTC = ("CoinMarketCap (penutupan akhir tahun); puncak Okt 2025: KuCoin/Kraken; Jun 2026: Benzinga (<$59 rb); "
           "23 Okt 2026: Fortune")
write_csv("bitcoin", ["periode", "usd"], [(a.replace("\n", " "), b) for a, b in BTC], SRC_BTC)
fig, ax = plt.subplots(figsize=(7.2, 3.2))
ax.plot(range(len(BTC)), [v for _, v in BTC], color=AMBER, marker="o", lw=2)
ax.set_yscale("log")
ax.set_xticks(range(len(BTC)))
ax.set_xticklabels([a for a, _ in BTC], fontsize=7)
for i, (a, v) in enumerate(BTC):
    if a in ("2017", "2018", "2022", "2024") or "\n" in a:
        below = a in ("2018", "2022") or "terendah" in a
        ax.text(i, v / 1.9 if below else v * 1.35, f"${v:,.0f}".replace(",", "."), ha="center", fontsize=7,
                color=INK)
ax.set_ylim(150, 400000)
ax.set_ylabel("US$ (skala log)")
ax.set_title("Bitcoin: siklus boom-bust, belum menjadi safe haven perang")
save(fig, "c10_bitcoin", SRC_BTC)

# ---------------------------------------------------------------- 11. Stablecoin
ST = [("USDT (Tether)", 182.4), ("USDC (Circle)", 71.7), ("Lainnya", 46.2)]
SRC_ST = "DefiLlama, 25 Okt 2026 (total ±US$300,3 miliar)"
write_csv("stablecoin", ["stablecoin", "usd_miliar"], ST, SRC_ST)
fig, ax = plt.subplots(figsize=(7.2, 1.5))
left = 0
for (n, v), c in zip(ST, [TEAL, NAVY, "#c9d2dc"]):
    ax.barh([0], [v], left=left, color=c, height=0.5)
    ax.text(left + v / 2, 0, f"{n}\nUS${v:.0f} miliar", ha="center", va="center", fontsize=8,
            color="white" if c != "#c9d2dc" else INK)
    left += v
ax.set_xlim(0, 300.3)
ax.set_yticks([])
ax.set_xlabel("US$ miliar")
ax.grid(False)
ax.set_title("Stablecoin ±US$300 miliar: hampir seluruhnya berbasis dolar AS")
save(fig, "c11_stablecoin", SRC_ST)

# ---------------------------------------------------------------- 12. Brent 2026
BRENT = [("27 Feb", 70, ""), ("2 Mar", 81, "Perang dimulai 28 Feb"), ("8 Mar", 100, ""),
         ("akhir Mar", 118, "Puncak ±$118–126"), ("1 Jul", 70, "Islamabad Memorandum"), ("akhir Jul", 100, "Gencatan\nruntuh"),
         ("Agu", 90, ""), ("awal Sep", 109, ""), ("23 Okt", 116.72, "Settle $116,72"), ("26 Okt", 114.6, "")]
SRC_BR = ("Titik harga Brent yang dilaporkan (bukan seri harian): Wikipedia 2026 Iran war fuel crisis; "
          "CNBC & FinanceFeeds (23 Okt); Vantage (26 Okt)")
write_csv("brent_2026", ["titik", "usd_per_barel", "peristiwa"], BRENT, SRC_BR)
fig, ax = plt.subplots(figsize=(7.2, 3.2))
xs = range(len(BRENT))
ax.plot(list(xs), [b for _, b, _ in BRENT], color=RED, marker="o", lw=2)
ax.fill_between(list(xs), [b for _, b, _ in BRENT], 60, color=RED, alpha=0.07)
for i, (_, v, e) in enumerate(BRENT):
    if e:
        dy = {"Perang dimulai 28 Feb": (-0.1, -9), "Islamabad Memorandum": (0, -7)}.get(e, (0, 4))
        ax.text(i + dy[0], v + dy[1], e, ha="center", fontsize=7, color=INK)
ax.set_xticks(list(xs))
ax.set_xticklabels([a for a, _, _ in BRENT], fontsize=7.6)
ax.set_ylim(60, 138)
ax.set_ylabel("US$/barel")
ax.set_title("Brent 2026: shock pasokan terbesar dalam sejarah (IEA)")
save(fig, "c12_brent", SRC_BR)

# ---------------------------------------------------------------- 13. Emas 2026
GOLD = [("12 Jan", 4600), ("29 Jan", 5595), ("30 Jan", 4860), ("akhir Jun", 3995), ("9 Okt", 4194), ("Okt", 4075)]
SRC_G = "Rekor intraday ±$5.595 (beberapa sumber); crash 30 Jan: Money.org/CNBC; Juni: LBMA via MetalsMine; Okt: GoldSilver"
write_csv("emas_2026", ["titik", "usd_per_oz"], GOLD, SRC_G)
fig, ax = plt.subplots(figsize=(7.2, 2.9))
ax.plot(range(len(GOLD)), [v for _, v in GOLD], color=AMBER, marker="o", lw=2)
for i, (a, v) in enumerate(GOLD):
    ax.text(i, v + 90, f"${v:,}".replace(",", "."), ha="center", fontsize=8, color=INK)
ax.annotate("Nominasi Warsh:\n−10% dalam sehari", xy=(2, 4860), xytext=(2.6, 5250), fontsize=7.5, color=RED,
            arrowprops=dict(arrowstyle="-", color=RED, lw=0.7))
ax.set_xticks(range(len(GOLD)))
ax.set_xticklabels([a for a, _ in GOLD])
ax.set_ylim(3700, 5900)
ax.set_ylabel("US$/oz")
ax.set_title("Emas 2026: rekor, crash, lalu ditopang bank sentral")
save(fig, "c13_emas_2026", SRC_G)

# ---------------------------------------------------------------- 14. Defisit fiskal
DEF = [("China (defisit luas)", -9.2), ("AS (FY2026)", -6.3), ("Prancis", -5.4), ("Arab Saudi (revisi)", -4.9),
       ("Inggris", -4.4), ("India (pusat, target FY27)", -4.3), ("Rusia (proyeksi tengah)", -4.0),
       ("Jerman (2025)", -3.0), ("Indonesia (proyeksi)", -2.85), ("Hong Kong (proyeksi 26/27)", 0.6)]
SRC_DEF = ("CBO/Treasury; CRS (China); Kemenkeu Prancis; Kemenkeu Saudi; House of Commons Library; PRS India; "
           "Reuters (Rusia 3,5–4,4%); ifo; Kemenkeu RI (Purbaya); Pemerintah HK")
write_csv("defisit_fiskal_2026", ["negara", "persen_pdb"], DEF, SRC_DEF)
fig, ax = plt.subplots(figsize=(7.2, 3.4))
lab = [a for a, _ in DEF][::-1]
val = [b for _, b in DEF][::-1]
ax.barh(lab, val, color=[GREEN if v > 0 else (RED if v <= -5 else AMBER) for v in val], height=0.62)
for i, v in enumerate(val):
    ax.text(v - 0.15 if v < 0 else v + 0.15, i, f"{v:+.1f}".replace(".", ","), va="center",
            ha="right" if v < 0 else "left", fontsize=8, color=INK)
ax.axvline(-3, color=SOFT, ls="--", lw=0.8)
ax.text(-2.95, 9.35, "batas 3% (UU Keuangan Negara RI / Maastricht)", fontsize=7, color=SOFT)
ax.set_xlim(-11, 2)
ax.grid(axis="y", visible=False)
ax.set_xlabel("saldo fiskal, % PDB (negatif = defisit)")
ax.set_title("Defisit fiskal 2026: negara maju lebih boros dari batas aman")
save(fig, "c14_defisit", SRC_DEF)

# ---------------------------------------------------------------- 15. Yield 10 tahun
YLD = [("SBN Indonesia (Sep)", 7.2), ("Gilt Inggris (23 Okt)", 5.37), ("UST AS (23 Okt)", 4.99),
       ("OAT Prancis (6 Okt)", 4.85), ("BTP Italia (6 Okt)", 4.61), ("Bund Jerman (6 Okt)", 3.45),
       ("JGB Jepang (Okt)", 2.81)]
PEAK = {"Gilt Inggris (23 Okt)": 5.53, "UST AS (23 Okt)": 5.36, "OAT Prancis (6 Okt)": 4.94}
SRC_Y = "Trading Economics; Investing; QuiFinanza/Money.it; Kontan (SBN); puncak Okt 2026: Vantage, Top1Markets, Euronews"
write_csv("yield_10th", ["obligasi", "yield_persen"], YLD, SRC_Y)
fig, ax = plt.subplots(figsize=(7.2, 3.0))
lab = [a for a, _ in YLD][::-1]
val = [b for _, b in YLD][::-1]
ax.barh(lab, val, color=[RED if "SBN" in a else NAVY for a in lab], height=0.6)
for i, (a, v) in enumerate(zip(lab, val)):
    t = f"{v:.2f}%".replace(".", ",")
    if a in PEAK:
        t += f"  (puncak {PEAK[a]:.2f}%, tertinggi sejak 2002/2007)".replace(".", ",")
    ax.text(v + 0.08, i, t, va="center", fontsize=7.6, color=INK)
ax.set_xlim(0, 10.5)
ax.grid(axis="y", visible=False)
ax.set_xlabel("yield obligasi 10 tahun, %")
ax.set_title("Yield obligasi negara: selisih SBN–UST tinggal ±2,2 poin")
save(fig, "c15_yield", SRC_Y)

# ---------------------------------------------------------------- 16. Transaksi berjalan Indonesia
CA = [("Q2 2013\n(taper tantrum)", -4.4, -10.1), ("Q1 2026", -1.0, -3.6), ("Q2 2026", -3.3, -12.5)]
SRC_CA = "Bank Indonesia, Neraca Pembayaran Q2 2026 (21 Agu 2026); Q2 2013: BI (defisit kuartalan ±US$10,1 miliar)"
write_csv("transaksi_berjalan_ri", ["periode", "persen_pdb", "usd_miliar"], [(a.replace("\n", " "), b, c) for a, b, c in CA], SRC_CA)
fig, ax = plt.subplots(figsize=(7.2, 2.7))
ax.bar(range(3), [b for _, b, _ in CA], color=["#c9d2dc", AMBER, RED], width=0.55)
for i, (_, b, c) in enumerate(CA):
    ax.text(i, b - 0.3, f"{b:.1f}% PDB\n(−US${-c:.1f} miliar)".replace(".", ",").replace("-", "−"), ha="center",
            va="top", fontsize=8, color=INK)
ax.set_xticks(range(3))
ax.set_xticklabels([a for a, _, _ in CA])
ax.set_ylim(-6.2, 0.5)
ax.axhline(0, color=SOFT, lw=0.8)
ax.set_ylabel("% PDB")
ax.set_title("Defisit transaksi berjalan Indonesia: rekor nominal sejak 2004")
save(fig, "c16_transaksi_berjalan", SRC_CA)

# ---------------------------------------------------------------- 17. Kuadran rezim
fig, ax = plt.subplots(figsize=(6.2, 4.6))
ax.axhline(0, color=INK, lw=1)
ax.axvline(0, color=INK, lw=1)
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_xticks([])
ax.set_yticks([])
ax.grid(False)
quad = [(0.5, 0.92, "QUAD 2 · Reflasi", "pertumbuhan ↑ inflasi ↑\nkomoditas, saham siklikal", TEAL),
        (-0.5, 0.92, "QUAD 3 · Stagflasi", "pertumbuhan ↓ inflasi ↑\nemas, komoditas, kas", RED),
        (0.5, -0.78, "QUAD 1 · Goldilocks", "pertumbuhan ↑ inflasi ↓\nsaham, teknologi, EM", GREEN),
        (-0.5, -0.78, "QUAD 4 · Deflasi", "pertumbuhan ↓ inflasi ↓\nobligasi, USD, kas", NAVY)]
for x0, y0, t, s, c in quad:
    ax.text(x0, y0, t, ha="center", fontsize=9.5, weight="bold", color=c)
    ax.text(x0, y0 - 0.1, s, ha="center", va="top", fontsize=7.6, color=SOFT)
pos = [("AS", 0.12, 0.45), ("Zona Euro", -0.45, 0.35), ("Inggris", -0.55, 0.5), ("Jepang", -0.35, 0.18),
       ("Indonesia", -0.1, 0.28), ("China", 0.35, -0.15), ("India", 0.65, 0.12)]
for n, x0, y0 in pos:
    ax.scatter([x0], [y0], s=70, color=AMBER if n == "Indonesia" else INK, zorder=3)
    ax.text(x0 + (-0.04 if n == "Jepang" else 0.04), y0 + 0.03, n, ha="right" if n == "Jepang" else "left", fontsize=8.5, color=INK, weight="bold" if n == "Indonesia" else "normal")
ax.set_xlabel("pertumbuhan melambat ←   → pertumbuhan menguat", fontsize=8)
ax.set_ylabel("inflasi turun ←   → inflasi naik", fontsize=8)
for s in ax.spines.values():
    s.set_visible(False)
ax.set_title("Posisi rezim makro, Q3 2026 (penilaian penulis)")
save(fig, "c17_kuadran", "PDB & inflasi terkini (BPS, BLS, Eurostat/ECB, NBS, MoSPI); penempatan = analisis penulis")

# ---------------------------------------------------------------- 18. Heatmap dampak skenario
SC = ["A. Multipolar keruh", "B. Kebangkitan teknologi", "C1. Eskalasi Teluk", "C2. Krisis utang negara maju",
      "C3. Krisis kepercayaan domestik RI", "C4. Blokade Taiwan"]
AS = ["IHSG", "Rupiah", "SBN", "Emas (Rp)", "Batu bara", "Nikel", "Brent", "UST", "BTC"]
M = [[-1, -1, -1, 2, 1, 1, 1, -1, 0],
     [2, 2, 2, -1, 0, 1, -1, 1, 2],
     [-2, -3, -2, 3, 2, 0, 3, 0, -1],
     [-2, -2, -2, 3, 0, -1, 0, -3, 1],
     [-3, -3, -3, 3, 0, 0, 0, 0, 0],
     [-3, -3, -2, 3, -1, -2, 1, 2, -2]]
write_csv("matriks_dampak", ["skenario"] + AS, [[s] + r for s, r in zip(SC, M)], "Penilaian penulis (−3 s.d. +3)")
fig, ax = plt.subplots(figsize=(7.4, 3.2))
cm2 = LinearSegmentedColormap.from_list("rg2", [RED, "#f6e3e1", "#ffffff", "#dcefe9", GREEN])
ax.imshow(np.array(M), cmap=cm2, vmin=-3, vmax=3, aspect="auto")
for i in range(len(SC)):
    for j in range(len(AS)):
        ax.text(j, i, f"{M[i][j]:+d}" if M[i][j] else "0", ha="center", va="center", fontsize=8.5, color=INK)
ax.set_xticks(range(len(AS)))
ax.set_xticklabels(AS, fontsize=8)
ax.set_yticks(range(len(SC)))
ax.set_yticklabels(SC, fontsize=8)
ax.xaxis.tick_top()
ax.grid(False)
for s in ax.spines.values():
    s.set_visible(False)
ax.tick_params(length=0)
ax.set_title("Matriks dampak skenario terhadap aset (−3 sangat negatif … +3 sangat positif)", pad=22)
save(fig, "c18_matriks", "Penilaian penulis berdasarkan rantai transmisi di Bab 11; bukan prediksi")

# ---------------------------------------------------------------- 19. All Weather vs adaptasi buku
fig, (b1, b2) = plt.subplots(1, 2, figsize=(7.2, 2.9))
aw = [("Saham", 30), ("Obligasi panjang", 40), ("Obligasi menengah", 15), ("Emas", 7.5), ("Komoditas", 7.5)]
bk = [("Saham IDR", 30), ("SBN", 25), ("Emas", 20), ("USD/global", 15), ("Komoditas", 10)]
pal = [NAVY, TEAL, "#8fbcc1", AMBER, OLIVE]
for axx, data, title in ((b1, aw, "All Weather (Dalio, versi populer)"), (b2, bk, "'Adaptasi' di buku Vol. 1")):
    axx.pie([v for _, v in data], colors=pal, startangle=90, counterclock=False,
            wedgeprops=dict(width=0.4, edgecolor="white"))
    axx.legend([f"{a} {str(b).replace('.', ',')}%" for a, b in data], loc="upper center", bbox_to_anchor=(0.5, 0.02),
               fontsize=7.2, ncol=2)
    axx.set_title(title, fontsize=9.5)
fig.text(0.01, -0.2, "Sumber: All Weather versi Tony Robbins, 'Money: Master the Game' (2014), berbasis risk parity; "
         "buku Vol. 1 hlm. 36", fontsize=7.5, color=SOFT)
fig.savefig(os.path.join(CHART_DIR, "c19_allweather.svg"), bbox_inches="tight", pad_inches=0.15)
plt.close(fig)

# ---------------------------------------------------------------- 20. Skenario buku vs realita
fig, (r1, r2) = plt.subplots(2, 1, figsize=(7.2, 2.9))
for axx, title, base, bear, real, fmt, lim in (
        (r1, "IHSG", (8000, 10000), (4500, 5500), 5388, "{:,.0f}", (4000, 10500)),
        (r2, "USD/IDR", (15000, 17000), (18000, 20000), 18071, "{:,.0f}", (14500, 20500))):
    axx.barh([0], [base[1] - base[0]], left=base[0], color="#cfe3df", height=0.5)
    axx.barh([0], [bear[1] - bear[0]], left=bear[0], color="#f0d0ce", height=0.5)
    axx.text(sum(base) / 2, -0.45, "base case buku", ha="center", va="center", fontsize=7.6, color=GREEN)
    axx.text(sum(bear) / 2, -0.45, "bear case buku", ha="center", va="center", fontsize=7.6, color=RED)
    axx.scatter([real], [0], s=90, color=INK, zorder=3, marker="D")
    axx.text(real, 0.42, "realita Okt 2026: " + fmt.format(real).replace(",", "."), ha="center", fontsize=8,
             color=INK, weight="bold")
    axx.set_xlim(*lim)
    axx.set_ylim(-0.7, 0.8)
    axx.set_yticks([0])
    axx.set_yticklabels([title])
    axx.grid(axis="y", visible=False)
r1.set_title("Skenario Indonesia di buku Vol. 1 vs kenyataan")
fig.text(0.01, -0.05, "Sumber: buku Vol. 1 hlm. 31–32; IHSG 22 Okt 2026 (RRI); USD/IDR 22 Okt 2026 (Databoks)",
         fontsize=7.5, color=SOFT)
fig.tight_layout()
fig.savefig(os.path.join(CHART_DIR, "c20_buku_vs_realita.svg"), bbox_inches="tight", pad_inches=0.15)
plt.close(fig)

print("charts:", sorted(os.listdir(CHART_DIR)))
