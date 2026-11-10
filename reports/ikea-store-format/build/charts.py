"""Generate SVG charts for the IKEA store-format BOD report."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

OUT = os.path.join(os.path.dirname(__file__), "charts")
os.makedirs(OUT, exist_ok=True)

for f in fm.findSystemFonts():
    if "Inter" in f:
        fm.fontManager.addfont(f)
plt.rcParams.update({
    "font.family": "Inter", "font.size": 9, "axes.edgecolor": "#C9CED6",
    "axes.labelcolor": "#4A5361", "xtick.color": "#4A5361", "ytick.color": "#4A5361",
    "axes.spines.top": False, "axes.spines.right": False, "svg.fonttype": "none",
    "axes.titlesize": 10, "axes.titleweight": "bold", "axes.titlecolor": "#1B2430",
})
NAVY, AMBER, TEAL, CORAL, PURPLE = "#1F5FA8", "#E3A21A", "#2A9D8F", "#C8475A", "#7B5EA7"
MUTED, INK, INK2, GRID = "#B7C0CC", "#1B2430", "#4A5361", "#E6E9EE"


def save(fig, name):
    fig.savefig(os.path.join(OUT, name + ".svg"), bbox_inches="tight", transparent=True)
    plt.close(fig)


def grid(ax, axis="y"):
    ax.grid(axis=axis, color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)


# 1. Total IKEA retail sales FY19-FY26 (EUR bn)
yrs = ["FY19", "FY20", "FY21", "FY22", "FY23", "FY24", "FY25", "FY26"]
val = [41.3, 39.6, 41.9, 44.6, 47.6, 45.1, 44.6, 43.8]
fig, ax = plt.subplots(figsize=(6.6, 2.35))
cols = [MUTED] * 4 + [NAVY] + [MUTED] * 2 + [AMBER]
bars = ax.bar(yrs, val, color=cols, width=0.62)
for b, v in zip(bars, val):
    ax.text(b.get_x() + b.get_width() / 2, v + 0.5, f"{v:.1f}", ha="center", fontsize=8.5, color=INK)
ax.set_ylim(30, 51)
ax.set_ylabel("EUR miliar")
grid(ax)
ax.annotate("Puncak FY23\n(efek inflasi harga)", xy=(4, 47.6), xytext=(1.6, 49.2), fontsize=7.5,
            color=INK2, arrowprops=dict(arrowstyle="-", color=INK2, lw=0.6))
ax.annotate("3 tahun turun berturut-turut\n(price-cut + demand lemah)", xy=(7, 43.8), xytext=(5.0, 49.2),
            fontsize=7.5, color=INK2, arrowprops=dict(arrowstyle="-", color=INK2, lw=0.6))
save(fig, "c1_sales")

# 2. Franchisee markets (63 markets, 13 groups)
fr = [("Ingka Group", 31), ("Ikano Group", 5), ("Al-Futtaim", 4), ("DFI (incl. Indonesia)", 4),
      ("Al-Homaizi", 3), ("House Market", 3), ("Sarton", 3), ("Inter IKEA Retail", 3),
      ("Al-Sulaiman", 2), ("Falabella", 2), ("Miklatorg", 1), ("MAPA", 1), ("Northern Birch", 1)]
fig, ax = plt.subplots(figsize=(3.4, 3.5))
names = [f[0] for f in fr][::-1]
nums = [f[1] for f in fr][::-1]
c = [AMBER if "DFI" in n else (NAVY if n == "Ingka Group" else MUTED) for n in names]
ax.barh(names, nums, color=c, height=0.66)
for i, v in enumerate(nums):
    ax.text(v + 0.4, i, str(v), va="center", fontsize=8, color=INK)
ax.set_xlabel("Jumlah pasar (negara) per 31 Agustus 2025")
ax.tick_params(axis="y", labelsize=8)
grid(ax, "x")
save(fig, "c2_franchisees")

# 3. Channel mix FY25 (single 100% bar)
fig, ax = plt.subplots(figsize=(3.4, 0.75))
parts = [("Toko", 69, NAVY), ("Online", 28, TEAL), ("Jasa", 3, AMBER)]
left = 0
for lab, v, col in parts:
    ax.barh([0], [v], left=left, color=col, height=0.6, edgecolor="white", linewidth=2)
    if v > 5:
        ax.text(left + v / 2, 0, f"{lab} {v}%", ha="center", va="center", color="white", fontsize=8.5, fontweight="bold")
    else:
        ax.text(left + v + 0.6, 0.48, f"{lab} {v}%", ha="right", va="bottom", color=INK, fontsize=8)
    left += v
ax.set_xlim(0, 100)
ax.axis("off")
save(fig, "c3_channel")

# 4. Ingka top selling countries FY25 (% of Ingka retail sales)
cty = [("Jerman", 15.4), ("Amerika Serikat", 12.6), ("Prancis", 9.0), ("Inggris", 6.8), ("Italia", 5.6), ("Negara lain (26)", 50.6)]
fig, ax = plt.subplots(figsize=(3.3, 2.3))
n = [x[0] for x in cty][::-1]
v = [x[1] for x in cty][::-1]
ax.barh(n, v, color=[MUTED] + [NAVY] * 5, height=0.62)
for i, x in enumerate(v):
    ax.text(x + 0.8, i, f"{x:.1f}%", va="center", fontsize=8, color=INK)
ax.set_xlim(0, 62)
ax.set_title("Top-5 negara (% penjualan Ingka)", loc="left")
ax.tick_params(axis="y", labelsize=8)
grid(ax, "x")
save(fig, "c4_countries")

fig, ax = plt.subplots(figsize=(3.3, 2.5))
reg = [("Eropa", 73.8, NAVY), ("Amerika", 17.2, TEAL), ("Asia Pasifik", 9.0, AMBER)]
ax.bar([r[0] for r in reg], [r[1] for r in reg], color=[r[2] for r in reg], width=0.58)
for i, r in enumerate(reg):
    ax.text(i, r[1] + 1.5, f"{r[1]:.1f}%", ha="center", fontsize=8.5, color=INK)
ax.set_ylim(0, 85)
ax.set_title("Penjualan per region (Ingka)", loc="left")
grid(ax)
save(fig, "c5_regions")

# 6. Ingka format mix FY24 vs FY25 (stacked)
fig, ax = plt.subplots(figsize=(6.6, 2.0))
yrsx = ["FY24", "FY25"]
bb = [375, 375]; cs = [25, 36]; of = [174, 209]
ax.barh(yrsx, bb, color=NAVY, height=0.55, edgecolor="white", linewidth=2, label="Blue box (toko besar)")
ax.barh(yrsx, cs, left=bb, color=AMBER, height=0.55, edgecolor="white", linewidth=2, label="City store")
ax.barh(yrsx, of, left=[a + b for a, b in zip(bb, cs)], color=TEAL, height=0.55, edgecolor="white", linewidth=2,
        label="Format lain (planning studio, P&O, small store, pick-up)")
for i in range(2):
    ax.text(bb[i] / 2, i, f"{bb[i]}", ha="center", va="center", color="white", fontweight="bold", fontsize=8.5)
    ax.text(bb[i] + cs[i] / 2, i, f"{cs[i]}", ha="center", va="center", color=INK, fontweight="bold", fontsize=8.5)
    ax.text(bb[i] + cs[i] + of[i] / 2, i, f"{of[i]}", ha="center", va="center", color="white", fontweight="bold", fontsize=8.5)
    tot = bb[i] + cs[i] + of[i]
    ax.text(tot + 6, i, f"Total {tot}", va="center", fontsize=8.5, color=INK)
ax.set_xlim(0, 690)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.18), ncol=3, frameon=False, fontsize=7.5)
ax.set_xlabel("")
grid(ax, "x")
save(fig, "c6_formatmix")

# 7. Store size spectrum by tier (log scale, m2)
tiers = [
    ("T1  Large / Blue box", 15000, 65000, NAVY, [("Memphis 25,2k", 25200, "d", "right"), ("Alam Sutera 35k", 35000, "u", "center"), ("Pasay Manila 65k", 65000, "d", "left")]),
    ("T2  City store (medium)", 4500, 18000, AMBER, [("Paris Madeleine 5,4k", 5400, "d", "right"), ("Taman Anggrek 9,4k", 9400, "u", "center"), ("Hamburg-Altona 18k", 18000, "d", "left")]),
    ("T3  Small store / IKEA Shop", 1500, 4500, TEAL, [("Beijing 1,5k", 1500, "d", "right"), ("Limoges 2k", 2000, "u", "center"), ("Coimbra 4k", 4000, "d", "left")]),
    ("T4  Plan & Order Point", 190, 1400, CORAL, [("Pleasanton 195", 195, "u", "center"), ("Manila TriNoma 500", 500, "d", "left")]),
    ("T5  Pick-up point / locker", 30, 500, PURPLE, []),
]
fig, ax = plt.subplots(figsize=(6.8, 2.5))
for i, (lab, lo, hi, col, ex) in enumerate(tiers[::-1]):
    ax.plot([lo, hi], [i, i], color=col, lw=9, solid_capstyle="round", alpha=0.35)
    for en, x, pos, ha in ex:
        ax.plot([x], [i], "o", ms=7, color=col, mec="white", mew=1.5)
        ax.text(x, i + (0.26 if pos == "u" else -0.42), en, ha=ha, fontsize=6.8, color=INK2)
ax.set_yticks(range(len(tiers)))
ax.set_yticklabels([t[0] for t in tiers[::-1]], fontsize=8)
ax.set_xscale("log")
ax.set_xlim(20, 300000)
ax.set_ylim(-0.7, len(tiers) - 0.3)
ax.set_xticks([30, 100, 300, 1000, 3000, 10000, 30000, 100000])
ax.set_xticklabels(["30", "100", "300", "1.000", "3.000", "10.000", "30.000", "100.000"])
ax.set_xlabel("Luas area penjualan/bangunan (m², skala log)")
grid(ax, "x")
save(fig, "c7_spectrum")

# 8. Capex estimate per tier (EUR m, log, analyst estimate)
cap = [("T1  Large / Blue box", 50, 150, NAVY), ("T2  City store", 15, 60, AMBER), ("T3  Small store", 3, 10, TEAL),
       ("T4  Plan & Order", 0.5, 2, CORAL), ("T5  Pick-up point", 0.05, 0.5, PURPLE)]
fig, ax = plt.subplots(figsize=(6.8, 2.5))
for i, (lab, lo, hi, col) in enumerate(cap[::-1]):
    ax.plot([lo, hi], [i, i], color=col, lw=11, solid_capstyle="butt")
    def fmt(x):
        return f"{x:g}"
    ax.text(hi * 1.15, i, f"€{fmt(lo)}–{fmt(hi)} jt", va="center", fontsize=8, color=INK)
ax.set_yticks(range(len(cap)))
ax.set_yticklabels([c[0] for c in cap[::-1]], fontsize=8)
ax.set_xscale("log")
ax.set_xlim(0.03, 600)
ax.set_xticks([0.1, 1, 10, 100])
ax.set_xticklabels(["€0,1 jt", "€1 jt", "€10 jt", "€100 jt"])
ax.set_xlabel("Estimasi capex per unit (EUR juta, skala log) — termasuk fit-out, IT & stok awal; T1 termasuk lahan")
grid(ax, "x")
save(fig, "c8_capex")

# 9. Ingka capex & D&A
fig, ax = plt.subplots(figsize=(3.3, 2.4))
labs = ["Capex\n(additions)", "Depresiasi\nPP&E", "Arus kas\noperasi"]
v24 = [3.436, 1.569, 2.9]; v25 = [3.404, 1.615, 4.0]
import numpy as np
x = np.arange(3)
ax.bar(x - 0.19, v24, 0.36, color=MUTED, label="FY24", edgecolor="white")
ax.bar(x + 0.19, v25, 0.36, color=NAVY, label="FY25", edgecolor="white")
for i in range(3):
    ax.text(i + 0.19, v25[i] + 0.08, f"{v25[i]:.1f}", ha="center", fontsize=8, color=INK)
    ax.text(i - 0.19, v24[i] + 0.08, f"{v24[i]:.1f}", ha="center", fontsize=7.5, color=INK2)
ax.set_xticks(x)
ax.set_xticklabels(labs, fontsize=7.5)
ax.set_ylim(0, 4.8)
ax.set_ylabel("EUR miliar")
ax.legend(frameon=False, fontsize=7.5, loc="upper left")
grid(ax)
save(fig, "c9_capex_ingka")

# 10. Ingka network growth
fig, ax = plt.subplots(figsize=(3.3, 2.4))
gx = ["2020", "FY24", "FY25", "Mar-26"]
gv = [375, 574, 620, 640]
ax.plot(gx, gv, color=NAVY, lw=2, marker="o", ms=7, mec="white", mew=1.5)
for xx, yy, t in zip(gx, gv, ["~375", "574", "620", ">640"]):
    ax.text(xx, yy + 22, t, ha="center", fontsize=8.5, color=INK)
ax.set_ylim(300, 720)
ax.set_ylabel("Jumlah lokasi IKEA Retail (Ingka)")
grid(ax)
save(fig, "c10_network")

# 11. Inter IKEA revenue composition FY25
fig, ax = plt.subplots(figsize=(6.6, 0.55))
p = [("Penjualan barang ke franchisee €24,9 mlr", 24.86, NAVY), ("Franchise fee 3% €1,32 mlr", 1.32, AMBER), ("Lainnya €0,13 mlr", 0.13, MUTED)]
left = 0
for lab, val_, col in p:
    ax.barh([0], [val_], left=left, color=col, height=0.6, edgecolor="white", linewidth=2)
    left += val_
ax.text(12.4, 0, p[0][0], ha="center", va="center", color="white", fontsize=8.5, fontweight="bold")
ax.text(26.4, 0.36, "Franchise fee €1,32 mlr (5%) ▼", ha="right", va="bottom", fontsize=8, color=INK)
ax.set_xlim(0, 26.4)
ax.axis("off")
save(fig, "c11_interikea")
print("ok", sorted(os.listdir(OUT)))
