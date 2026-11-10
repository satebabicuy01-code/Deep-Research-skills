"""Generate SVG charts for the MR.DIY Indonesia BOD report."""
import io
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib import font_manager

OUT = sys.argv[1] if len(sys.argv) > 1 else "charts"
os.makedirs(OUT, exist_ok=True)

# ---- palette (reference instance, light mode) ----
SURF = "#ffffff"
INK = "#0b0b0b"
INK2 = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
BASE = "#c3c2b7"
BLUE = "#2a78d6"
ORANGE = "#eb6834"
AQUA = "#1baf7a"
BLUE_LIGHT = "#86b6ef"
BLUE_DARK = "#184f95"
GRAY_MID = "#c3c2b7"

plt.rcParams.update({
    "font.family": "Inter",
    "font.size": 9,
    "axes.edgecolor": BASE,
    "axes.labelcolor": INK2,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.spines.left": False,
    "svg.fonttype": "none",
    "figure.facecolor": SURF,
    "axes.facecolor": SURF,
})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name + ".svg"), format="svg", bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)


def rbar(ax, x, h, w, color, horizontal=False, r_frac=0.18, bottom=0.0):
    """Bar with rounded data-end only, square at baseline."""
    if h == 0:
        return
    sign = 1 if h > 0 else -1
    # rounding radius in data units, limited
    if not horizontal:
        x0, x1 = x - w / 2, x + w / 2
        y0, y1 = bottom, bottom + h
        rx = w * 0.18
        ry = min(abs(h) * 0.5, ax_rad_y(ax) )
        verts = [(x0, y0), (x0, y1 - sign * ry), (x0, y1), (x0 + rx, y1),
                 (x1 - rx, y1), (x1, y1), (x1, y1 - sign * ry), (x1, y0), (x0, y0)]
        codes = [Path.MOVETO, Path.LINETO, Path.CURVE3, Path.CURVE3,
                 Path.LINETO, Path.CURVE3, Path.CURVE3, Path.LINETO, Path.CLOSEPOLY]
    else:
        y0, y1 = x - w / 2, x + w / 2
        x0, x1 = bottom, bottom + h
        ry = w * 0.18
        rx = min(abs(h) * 0.5, ax_rad_x(ax))
        verts = [(x0, y0), (x1 - sign * rx, y0), (x1, y0), (x1, y0 + ry),
                 (x1, y1 - ry), (x1, y1), (x1 - sign * rx, y1), (x0, y1), (x0, y0)]
        codes = [Path.MOVETO, Path.LINETO, Path.CURVE3, Path.CURVE3,
                 Path.LINETO, Path.CURVE3, Path.CURVE3, Path.LINETO, Path.CLOSEPOLY]
    ax.add_patch(PathPatch(Path(verts, codes), facecolor=color, edgecolor="none", zorder=3))


_RAD = {}


def ax_rad_y(ax):
    return _RAD.get((id(ax), "y"), 0)


def ax_rad_x(ax):
    return _RAD.get((id(ax), "x"), 0)


def set_rad(ax, xr=None, yr=None):
    if xr is not None:
        _RAD[(id(ax), "x")] = xr
    if yr is not None:
        _RAD[(id(ax), "y")] = yr


def ygrid(ax):
    ax.yaxis.grid(True, color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    ax.tick_params(axis="both", length=0)


def xgrid(ax):
    ax.xaxis.grid(True, color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    ax.tick_params(axis="both", length=0)


def fmt(v, dec=0):
    s = f"{v:,.{dec}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


# ---------------------------------------------------------------- 1 store growth
def chart_store_growth():
    labels = ["2018", "2021", "2022", "2023", "2024", "2025", "Sep-26"]
    vals = [73, 324, 478, 698, 961, 1226, 1416]
    fig, ax = plt.subplots(figsize=(6.6, 2.7))
    ymax = 1650
    ax.set_ylim(0, ymax)
    ax.set_xlim(-0.6, len(vals) - 0.4)
    set_rad(ax, yr=ymax * 0.025)
    for i, v in enumerate(vals):
        rbar(ax, i, v, 0.5, BLUE if i < len(vals) - 1 else BLUE_DARK)
        ax.text(i, v + 35, fmt(v), ha="center", va="bottom", color=INK, fontsize=9, fontweight="semibold")
    ax.set_xticks(range(len(vals)), labels)
    ax.set_yticks([0, 500, 1000, 1500], ["0", "500", "1.000", "1.500"])
    ygrid(ax)
    ax.spines["bottom"].set_color(BASE)
    save(fig, "c01_store_growth")


# ---------------------------------------------------------------- 2 revenue & PAT
def chart_rev_pat():
    yrs = ["2021", "2022", "2023", "2024", "2025", "9M25", "9M26"]
    rev = [894, 2216, 3905, 6790, 7922, 5772, 7188]
    pat = [-80, 128, 353, 1078, 1131, 792, 894]
    fig, axes = plt.subplots(1, 2, figsize=(6.8, 2.6), gridspec_kw={"wspace": 0.3})
    for ax, data, title, ymax, ymin, tick in [
        (axes[0], rev, "Pendapatan (Rp miliar)", 9000, 0, [0, 3000, 6000, 9000]),
        (axes[1], pat, "Laba bersih / PAT (Rp miliar)", 1300, -150, [0, 400, 800, 1200]),
    ]:
        ax.set_ylim(ymin, ymax)
        ax.set_xlim(-0.6, len(data) - 0.4)
        set_rad(ax, yr=(ymax - ymin) * 0.025)
        for i, v in enumerate(data):
            col = BLUE if i < 5 else (BLUE_LIGHT if i == 5 else BLUE_DARK)
            rbar(ax, i, v, 0.55, col)
            off = (ymax - ymin) * 0.02
            ax.text(i, v + off if v >= 0 else v - off, fmt(v), ha="center",
                    va="bottom" if v >= 0 else "top", color=INK, fontsize=7.5)
        ax.axvline(4.5, color=GRID, linewidth=0.8)
        ax.set_xticks(range(len(yrs)), yrs, fontsize=8)
        ax.set_yticks(tick, [fmt(t) for t in tick])
        ax.axhline(0, color=BASE, linewidth=0.8)
        ygrid(ax)
        ax.spines["bottom"].set_visible(False)
        ax.set_title(title, loc="left", color=INK, fontsize=9.5, fontweight="semibold", pad=8)
    save(fig, "c02_rev_pat")


# ---------------------------------------------------------------- 3 margins
def chart_margins():
    per = ["FY2023 (proforma)", "FY2024", "FY2025", "9M2026"]
    gpm = [53.0, 55.0, 55.1, 51.3]
    ebitda = [28.0, 32.9, 32.7, 29.6]
    patm = [13.6, 15.9, 14.3, 12.4]
    fig, ax = plt.subplots(figsize=(6.6, 2.6))
    x = list(range(len(per)))
    series = [("Gross margin", gpm, BLUE), ("EBITDA margin", ebitda, ORANGE), ("PAT margin", patm, AQUA)]
    for name, s, c in series:
        xs = [i for i, v in zip(x, s) if v is not None]
        ys = [v for v in s if v is not None]
        ax.plot(xs, ys, color=c, linewidth=2, solid_capstyle="round", solid_joinstyle="round", zorder=3, label=name)
        ax.scatter(xs, ys, s=30, color=c, edgecolor=SURF, linewidth=1.5, zorder=4)
        ax.text(xs[-1] + 0.12, ys[-1], f"{fmt(ys[-1],1)}%", va="center", color=INK, fontsize=8)
        ax.text(xs[0] - 0.12, ys[0], f"{fmt(ys[0],1)}%", va="center", ha="right", color=INK2, fontsize=8)
    ax.set_ylim(0, 62)
    ax.set_xlim(-0.6, len(per) - 0.3)
    ax.set_xticks(x, per)
    ax.set_yticks([0, 20, 40, 60], ["0%", "20%", "40%", "60%"])
    ygrid(ax)
    ax.spines["bottom"].set_color(BASE)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.18), ncol=3, frameon=False, fontsize=8, labelcolor=INK2)
    save(fig, "c03_margins")


# ---------------------------------------------------------------- 4 SSSG
def chart_sssg():
    per = ["2021", "2022", "2023", "2024", "2025", "1Q26", "2Q26", "3Q26"]
    v = [2.6, 43.1, 30.1, 5.1, -7.6, 3.9, -5.9, 1.5]
    fig, ax = plt.subplots(figsize=(6.6, 2.5))
    ax.set_ylim(-14, 50)
    ax.set_xlim(-0.6, len(v) - 0.4)
    set_rad(ax, yr=1.4)
    for i, val in enumerate(v):
        rbar(ax, i, val, 0.5, BLUE if val >= 0 else ORANGE)
        ax.text(i, val + (1.2 if val >= 0 else -1.2), f"{'+' if val>0 else ''}{fmt(val,1)}%",
                ha="center", va="bottom" if val >= 0 else "top", color=INK, fontsize=8)
    ax.axhline(0, color=BASE, linewidth=0.8)
    ax.axvline(4.5, color=GRID, linewidth=0.8)
    ax.set_xticks(range(len(v)), per)
    ax.set_yticks([-10, 0, 10, 20, 30, 40], ["-10%", "0%", "10%", "20%", "30%", "40%"])
    ygrid(ax)
    ax.spines["bottom"].set_visible(False)
    save(fig, "c04_sssg")


# ---------------------------------------------------------------- 5 tiers (actual Jun 2024)
def chart_tiers():
    tiers = ["Small\n< 500 m²", "Medium\n500–900 m²", "Large\n> 900 m²"]
    stand = [335, 254, 11]
    mall = [42, 130, 52]
    fig, ax = plt.subplots(figsize=(6.6, 2.0))
    ax.set_xlim(0, 440)
    set_rad(ax, xr=6)
    y = [2, 1, 0]
    for yi, s, m in zip(y, stand, mall):
        # stacked: standalone then mall, with 2px-ish gap
        ax.barh(yi, s, height=0.5, color=BLUE, zorder=3)
        rbar(ax, yi, m, 0.5, ORANGE, horizontal=True, bottom=s + 2.5)
        ax.text(s + m + 10, yi, f"{s+m}  ({(s+m)/824*100:.0f}%)".replace(".", ","), va="center", color=INK, fontsize=9, fontweight="semibold")
        if s > 40:
            ax.text(s / 2, yi, str(s), va="center", ha="center", color="#ffffff", fontsize=8)
        if m > 35:
            ax.text(s + 2.5 + m / 2, yi, str(m), va="center", ha="center", color="#ffffff", fontsize=8)
    ax.set_yticks(y, tiers)
    ax.tick_params(axis="y", labelsize=9, labelcolor=INK2)
    ax.set_xticks([0, 100, 200, 300, 400])
    xgrid(ax)
    ax.spines["bottom"].set_visible(False)
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=BLUE, label="Stand-alone shopfront (ruko)"), Patch(color=ORANGE, label="Mall-based")],
              loc="lower right", frameon=False, fontsize=8, labelcolor=INK2)
    save(fig, "c05_tiers")


# ---------------------------------------------------------------- 6 region
def chart_region():
    reg = ["Jawa (ex-Jabodetabek)", "Sumatra", "Jabodetabek", "Sulawesi", "Kalimantan", "Nusa Tenggara & Bali", "Papua", "Maluku"]
    d24 = [243, 249, 145, 112, 93, 62, 34, 23]
    s26 = [336, 291, 241, 190, 180, 85, 56, 37]
    fig, ax = plt.subplots(figsize=(6.6, 3.0))
    n = len(reg)
    ys = list(range(n))[::-1]
    ax.set_xlim(0, 400)
    set_rad(ax, xr=5)
    for y, a, b in zip(ys, d24, s26):
        rbar(ax, y + 0.17, a, 0.3, BLUE_LIGHT, horizontal=True)
        rbar(ax, y - 0.17, b, 0.3, BLUE_DARK, horizontal=True)
        ax.text(b + 6, y - 0.17, f"{b}  (+{(b/a-1)*100:.0f}%)", va="center", color=INK, fontsize=8)
    ax.set_yticks(ys, reg)
    ax.tick_params(axis="y", labelsize=8.5, labelcolor=INK2)
    xgrid(ax)
    ax.spines["bottom"].set_visible(False)
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=BLUE_LIGHT, label="Des 2024 (961 toko)"), Patch(color=BLUE_DARK, label="Sep 2026 (1.416 toko)")],
              loc="lower right", frameon=False, fontsize=8, labelcolor=INK2)
    save(fig, "c06_region")


# ---------------------------------------------------------------- 7 category mix
def chart_category():
    cats = [("Household (alat rumah tangga)", 26), ("Furnishing (perabot)", 13), ("Stationery & Sports", 11), ("Toys (mainan)", 11),
            ("Jewellery & Cosmetics", 10), ("Hardware (perkakas)", 9), ("Gifts (hadiah)", 5), ("Electrical", 4),
            ("Car accessories", 3), ("Computer & HP acc.", 3), ("Lainnya / F&B*", 5)]
    fig, ax = plt.subplots(figsize=(6.4, 3.1))
    n = len(cats)
    ax.set_xlim(0, 30)
    set_rad(ax, xr=0.5)
    for i, (c, v) in enumerate(cats):
        y = n - 1 - i
        rbar(ax, y, v, 0.55, BLUE if i < 2 else BLUE_LIGHT if c.startswith("Lainnya") else BLUE, horizontal=True)
        ax.text(v + 0.4, y, f"{v}%", va="center", color=INK, fontsize=8.5)
    ax.set_yticks(range(n)[::-1], [c for c, _ in cats])
    ax.tick_params(axis="y", labelsize=8.5, labelcolor=INK2)
    ax.set_xticks([0, 10, 20, 30], ["0%", "10%", "20%", "30%"])
    xgrid(ax)
    ax.spines["bottom"].set_visible(False)
    save(fig, "c07_category")


# ---------------------------------------------------------------- 8 capex per new store
def chart_capex():
    per = ["FY2024", "FY2025", "9M2026"]
    capex = [706.7, 726.4, 615.7]
    stores = [270, 272, 202]
    per_store = [c / s for c, s in zip(capex, stores)]
    fig, axes = plt.subplots(1, 2, figsize=(6.8, 2.4), gridspec_kw={"wspace": 0.35})
    ax = axes[0]
    ax.set_ylim(0, 850)
    ax.set_xlim(-0.6, 2.6)
    set_rad(ax, yr=20)
    for i, v in enumerate(capex):
        rbar(ax, i, v, 0.5, BLUE)
        ax.text(i, v + 15, fmt(v, 1), ha="center", color=INK, fontsize=8.5)
    ax.set_xticks(range(3), per)
    ax.set_yticks([0, 400, 800])
    ygrid(ax)
    ax.spines["bottom"].set_color(BASE)
    ax.set_title("Belanja aset tetap (Rp miliar)", loc="left", fontsize=9.5, color=INK, fontweight="semibold", pad=8)
    ax = axes[1]
    ax.set_ylim(0, 3.6)
    ax.set_xlim(-0.6, 2.6)
    set_rad(ax, yr=0.09)
    for i, v in enumerate(per_store):
        rbar(ax, i, v, 0.5, BLUE_DARK)
        ax.text(i, v + 0.06, fmt(v, 2), ha="center", color=INK, fontsize=8.5)
    ax.set_xticks(range(3), [f"{p}\n({s} toko)" for p, s in zip(per, stores)], fontsize=8)
    ax.set_yticks([0, 1, 2, 3])
    ygrid(ax)
    ax.spines["bottom"].set_color(BASE)
    ax.set_title("Capex ÷ toko baru (Rp miliar, all-in)", loc="left", fontsize=9.5, color=INK, fontweight="semibold", pad=8)
    save(fig, "c08_capex")


# ---------------------------------------------------------------- 9 capex mix
def chart_capex_mix():
    items = [("Renovasi", 196.0), ("Fixtures (rak/display)", 63.1), ("Signboard", 35.1), ("Komputer & software", 30.2), ("Equipment", 24.9), ("Furniture", 8.9)]
    tot = sum(v for _, v in items)
    fig, ax = plt.subplots(figsize=(6.4, 0.95))
    left = 0
    cols = [BLUE, ORANGE, AQUA, "#eda100", "#e87ba4", "#6250d6"]
    for (n, v), c in zip(items, cols):
        w = v / tot * 100
        ax.barh(0, w - 0.4, left=left, height=0.55, color=c, zorder=3)
        if w > 7:
            ax.text(left + w / 2, 0, f"{w:.0f}%".replace(".", ","), ha="center", va="center", color="#0b0b0b" if c == "#eda100" else "#ffffff", fontsize=8)
        left += w
    ax.set_xlim(0, 100)
    ax.set_yticks([])
    ax.set_xticks([])
    ax.spines["bottom"].set_visible(False)
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=c, label=f"{n} {v/tot*100:.0f}%") for (n, v), c in zip(items, cols)],
              loc="upper center", bbox_to_anchor=(0.5, -0.05), ncol=3, frameon=False, fontsize=7.5, labelcolor=INK2)
    save(fig, "c09_capex_mix")


# ---------------------------------------------------------------- 10 payback curve
def chart_payback():
    # illustrative standard store (~550 m2): investment 3.5bn; 4-wall cash flow ramp
    inv = 3.5
    cf = [1.12, 1.41, 1.60, 1.60, 1.60]  # yearly
    months = list(range(0, 61))
    cum = []
    for m in months:
        if m == 0:
            cum.append(-inv)
            continue
        y = (m - 1) // 12
        cum.append(cum[-1] + cf[min(y, 4)] / 12)
    fig, ax = plt.subplots(figsize=(6.6, 2.5))
    ax.fill_between(months, cum, 0, where=[c < 0 for c in cum], color=ORANGE, alpha=0.10, linewidth=0)
    ax.fill_between(months, cum, 0, where=[c >= 0 for c in cum], color=BLUE, alpha=0.10, linewidth=0)
    ax.plot(months, cum, color=BLUE, linewidth=2, solid_capstyle="round")
    ax.axhline(0, color=BASE, linewidth=0.8)
    be = next(m for m, c in zip(months, cum) if c >= 0)
    pb = 2 + (inv - cf[0] - cf[1]) / cf[2]
    ax.annotate(f"Payback ≈ {pb:.1f} tahun (bulan ke-{be})".replace(".", ","), (pb * 12, 0), xytext=(be - 24, 1.6),
                color=INK, fontsize=8.5, arrowprops=dict(arrowstyle="-", color=MUTED, linewidth=0.8))
    ax.scatter([pb * 12], [0], s=40, color=BLUE_DARK, edgecolor=SURF, linewidth=1.5, zorder=5)
    ax.text(60.8, cum[-1], f"Rp{fmt(cum[-1],1)} M", va="center", color=INK, fontsize=8)
    ax.text(14, -3.6, "Investasi awal −Rp3,5 M (bulan 0)", color=INK2, fontsize=8)
    ax.set_xlim(0, 66)
    ax.set_ylim(-4, 4.5)
    ax.set_xticks([0, 12, 24, 36, 48, 60], ["0", "Th 1", "Th 2", "Th 3", "Th 4", "Th 5"])
    ax.set_yticks([-4, -2, 0, 2, 4], ["−4", "−2", "0", "2", "4"])
    ax.set_ylabel("Kumulatif arus kas (Rp miliar)", fontsize=8, color=INK2)
    ygrid(ax)
    ax.spines["bottom"].set_visible(False)
    save(fig, "c10_payback")


# ---------------------------------------------------------------- 11 competitor
def chart_competitors():
    comp = [("MR.DIY (Sep-26)", 1416), ("MR.DIY (Jun-24)", 824), ("Miniso (2026)", 357), ("Ace Hardware (Jun-24)", 236),
            ("Miniso (Jun-24)", 230), ("Niceso (Jun-24)", 203), ("BOLDe (Jun-24)", 61), ("Mitra10 (Jun-24)", 49),
            ("Gramedia (Jun-24)", 47), ("Oh!Some (Jun-24)", 38)]
    fig, ax = plt.subplots(figsize=(6.4, 2.6))
    n = len(comp)
    ax.set_xlim(0, 1650)
    set_rad(ax, xr=18)
    for i, (c, v) in enumerate(comp):
        y = n - 1 - i
        col = BLUE_DARK if c.startswith("MR.DIY (Sep") else BLUE if c.startswith("MR.DIY") else GRAY_MID
        rbar(ax, y, v, 0.55, col, horizontal=True)
        ax.text(v + 15, y, fmt(v), va="center", color=INK, fontsize=8.5)
    ax.set_yticks(range(n)[::-1], [c for c, _ in comp])
    ax.tick_params(axis="y", labelsize=8.5, labelcolor=INK2)
    ax.set_xticks([0, 500, 1000, 1500], ["0", "500", "1.000", "1.500"])
    xgrid(ax)
    ax.spines["bottom"].set_visible(False)
    save(fig, "c11_competitors")


# ---------------------------------------------------------------- 12 transactions & basket
def chart_traffic():
    yrs = ["2023", "2024", "2025"]
    trx = [64.5, 88.8, 100.3]
    basket = [83.5, 84.5, 87.5]
    fig, axes = plt.subplots(1, 2, figsize=(6.8, 2.3), gridspec_kw={"wspace": 0.35})
    ax = axes[0]
    ax.set_ylim(0, 120)
    ax.set_xlim(-0.6, 2.6)
    set_rad(ax, yr=3)
    for i, v in enumerate(trx):
        rbar(ax, i, v, 0.5, BLUE)
        ax.text(i, v + 2.5, fmt(v, 1), ha="center", color=INK, fontsize=8.5)
    ax.set_xticks(range(3), yrs)
    ax.set_yticks([0, 40, 80, 120])
    ygrid(ax)
    ax.spines["bottom"].set_color(BASE)
    ax.set_title("Jumlah transaksi (juta)", loc="left", fontsize=9.5, color=INK, fontweight="semibold", pad=8)
    ax = axes[1]
    ax.set_ylim(0, 100)
    ax.set_xlim(-0.6, 2.6)
    set_rad(ax, yr=2.5)
    for i, v in enumerate(basket):
        rbar(ax, i, v, 0.5, AQUA)
        ax.text(i, v + 2, fmt(v, 1), ha="center", color=INK, fontsize=8.5)
    ax.set_xticks(range(3), yrs)
    ax.set_yticks([0, 25, 50, 75, 100])
    ygrid(ax)
    ax.spines["bottom"].set_color(BASE)
    ax.set_title("Nilai belanja / transaksi (Rp ribu)", loc="left", fontsize=9.5, color=INK, fontweight="semibold", pad=8)
    save(fig, "c12_traffic")


for f in [chart_store_growth, chart_rev_pat, chart_margins, chart_sssg, chart_tiers, chart_region,
          chart_category, chart_capex, chart_capex_mix, chart_payback, chart_competitors, chart_traffic]:
    f()
print("ok", sorted(os.listdir(OUT)))
