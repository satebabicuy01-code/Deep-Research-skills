# Builds the NEKA BOD-style HTML report (rendered to PDF by render.js)
import html, sys, pathlib

OUT = pathlib.Path(sys.argv[1])

NAVY = "#14215E"; BLUE = "#2F49C8"; LBLUE = "#9DAEF0"; YEL = "#F5C400"; GREY = "#A9A9A9"; INK = "#1B1F2A"; MUTED = "#5B6170"

# ---------- SVG helpers ----------
def vbar(data, w=560, h=300, ymax=140, ticks=(0, 35, 70, 105, 140), colors=None):
    """data: list of (label, value, kind) kind in {'a','p'}"""
    padl, padb, padt = 34, 34, 18
    cw = w - padl - 10; ch = h - padb - padt
    n = len(data); bw = cw / n * 0.62; gap = cw / n
    s = [f'<svg viewBox="0 0 {w} {h}" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter" >']
    for t in ticks:
        y = padt + ch - ch * t / ymax
        s.append(f'<line x1="{padl}" x2="{w-10}" y1="{y:.1f}" y2="{y:.1f}" stroke="#E4E6EC" stroke-width="1"/>')
        s.append(f'<text x="{padl-6}" y="{y+3:.1f}" font-size="9" fill="{MUTED}" text-anchor="end">{t}</text>')
    for i, (lab, v, k) in enumerate(data):
        x = padl + gap * i + (gap - bw) / 2
        bh = ch * v / ymax; y = padt + ch - bh
        col = BLUE if k == 'a' else LBLUE
        s.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="2" fill="{col}"/>')
        s.append(f'<text x="{x+bw/2:.1f}" y="{y-5:.1f}" font-size="10" font-weight="700" text-anchor="middle" fill="{INK}">{v}</text>')
        s.append(f'<text x="{x+bw/2:.1f}" y="{h-padb+16:.1f}" font-size="8.5" text-anchor="middle" fill="{INK}">{lab}</text>')
    s.append(f'<line x1="{padl}" x2="{w-10}" y1="{padt+ch}" y2="{padt+ch}" stroke="#888"/>')
    s.append('</svg>')
    return "".join(s)

def hbar(data, w=300, rowh=26, vmax=None, labw=110, colors=None, fmt=lambda v: f"{v:,}".replace(",", ".")):
    vmax = vmax or max(v for _, v, _ in data)
    h = rowh * len(data) + 8
    s = [f'<svg viewBox="0 0 {w} {h}" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter">']
    for i, (lab, v, hi) in enumerate(data):
        y = 4 + i * rowh
        bwid = (w - labw - 44) * v / vmax
        col = BLUE if hi else GREY
        s.append(f'<text x="{labw-8}" y="{y+rowh/2+3}" font-size="9.5" text-anchor="end" fill="{INK}" font-weight="{700 if hi else 400}">{lab}</text>')
        s.append(f'<rect x="{labw}" y="{y+5}" width="{max(bwid,2):.1f}" height="{rowh-11}" fill="{col}" rx="1.5"/>')
        s.append(f'<text x="{labw+max(bwid,2)+5:.1f}" y="{y+rowh/2+3}" font-size="9.5" font-weight="700" fill="{INK}">{fmt(v)}</text>')
    s.append(f'<line x1="{labw}" x2="{labw}" y1="2" y2="{h-2}" stroke="#333"/>')
    s.append('</svg>')
    return "".join(s)

def lines(series, xlabels, w=520, h=270, ymin=0, ymax=200, ticks=None, refs=(), endlabels=True, xticklabels=None):
    padl, padr, padb, padt = 38, 96, 30, 20
    cw = w - padl - padr; ch = h - padb - padt
    ticks = ticks or []
    def X(i): return padl + cw * i / (len(xlabels) - 1)
    def Y(v): return padt + ch - ch * (v - ymin) / (ymax - ymin)
    s = [f'<svg viewBox="0 0 {w} {h}" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter">']
    for t in ticks:
        s.append(f'<line x1="{padl}" x2="{w-padr}" y1="{Y(t):.1f}" y2="{Y(t):.1f}" stroke="#E4E6EC"/>')
        s.append(f'<text x="{padl-6}" y="{Y(t)+3:.1f}" font-size="9" fill="{MUTED}" text-anchor="end">{t:g}</text>')
    if ymin < 0:
        s.append(f'<rect x="{padl}" y="{Y(0):.1f}" width="{cw}" height="{Y(ymin)-Y(0):.1f}" fill="#EEF1FB"/>')
        s.append(f'<line x1="{padl}" x2="{w-padr}" y1="{Y(0):.1f}" y2="{Y(0):.1f}" stroke="#222"/>')
    for (lab, val, col) in refs:
        s.append(f'<line x1="{padl}" x2="{w-padr}" y1="{Y(val):.1f}" y2="{Y(val):.1f}" stroke="#555" stroke-dasharray="4 3"/>')
        s.append(f'<text x="{padl+4}" y="{Y(val)-4:.1f}" font-size="8.5" fill="#444">{lab}</text>')
    for (name, vals, col, bold, labpts) in series:
        pts = " ".join(f"{X(i):.1f},{Y(v):.1f}" for i, v in enumerate(vals) if v is not None)
        s.append(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="{2.4 if bold else 1.8}"/>')
        for i, v in enumerate(vals):
            if v is None: continue
            if i in labpts:
                s.append(f'<circle cx="{X(i):.1f}" cy="{Y(v):.1f}" r="3" fill="{col}"/>')
                s.append(f'<text x="{X(i):.1f}" y="{Y(v)-7:.1f}" font-size="9" text-anchor="middle" font-weight="{700 if bold else 400}" fill="{INK}">{labpts[i]}</text>')
        if endlabels:
            lv = [v for v in vals if v is not None][-1]
            s.append(f'<text x="{w-padr+6}" y="{Y(lv)+3:.1f}" font-size="9.5" font-weight="{700 if bold else 400}" fill="{INK}">{name}</text>')
    xt = xticklabels or {i: l for i, l in enumerate(xlabels)}
    for i, l in xt.items():
        s.append(f'<text x="{X(i):.1f}" y="{h-padb+16}" font-size="8.5" text-anchor="middle" fill="{MUTED}">{l}</text>')
    s.append('</svg>')
    return "".join(s)

# ---------- charts ----------
c_growth = vbar([("Sep-25", 1, 'a'), ("Des-25", 10, 'a'), ("Mar-26", 12, 'a'), ("Jun-26", 20, 'a'), ("Agu-26", 26, 'a'),
                 ("Sep-26", 31, 'a'), ("Okt-26", 35, 'a'), ("Des-26 P", 42, 'p'), ("Des-27 P", 84, 'p'), ("Des-28 P", 126, 'p')],
                w=600, h=290)

c_cluster = hbar([("Jabodetabek", 13, True), ("Lampung", 5, True), ("Jateng & DIY", 5, False), ("Banten (Serang, Pandeglang)", 2, False),
                  ("Sumatera Selatan", 2, False), ("Jabar (Subang, Cirebon)", 2, False), ("Jawa Timur (Kediri)", 1, False),
                  ("Belum teridentifikasi", 5, False)], w=330, rowh=24, labw=150)

# payback: cumulative cash (Rp miliar) months 0..40
months = list(range(0, 41))
def cum(capex, c): return [round(-capex + c * m, 3) for m in months]
base = cum(1.8, 0.048); opt = cum(1.5, 0.119); pes = cum(2.1, 0.0)
lab_months = {0: "bln 0", 6: "bln 6", 12: "bln 12", 18: "bln 18", 24: "bln 24", 30: "bln 30", 36: "bln 36"}
c_payback = lines([
    ("Optimis", [v if v <= 2.6 else None for v in opt], "#8C8C8C", False, {13: "BEP bln 13"}),
    ("Dasar", base, BLUE, True, {37: "BEP bln 37"}),
    ("Pesimis", pes, "#C0392B", False, {}),
], [str(m) for m in months], w=520, h=260, ymin=-2.4, ymax=2.6, ticks=[-2, -1, 0, 1, 2],
    xticklabels={i: lab_months[i] for i in lab_months})

c_proj = lines([
    ("Agresif: 189", [35, 45, 117, 189], "#8C8C8C", False, {2: "117"}),
    ("Dasar: 126", [35, 42, 84, 126], BLUE, True, {0: "35 (aktual)", 2: "84"}),
    ("Konservatif: 87", [35, 39, 63, 87], "#B8B8B8", False, {}),
], ["Okt 2026", "Des 2026", "Des 2027", "Des 2028"], w=540, h=260, ymin=0, ymax=300, ticks=[0, 100, 200, 300],
    refs=[("AZKO saat ini (Sep 2026): 282 toko", 282, "#555")])

c_comp = hbar([("MR. DIY", 1416, False), ("MINISO", 300, False), ("AZKO (induk sama)", 282, False), ("NEKA", 35, True), ("KKV (rencana awal)", 10, False)],
              w=470, rowh=30, labw=130)

# ---------- page template ----------
def page(n, kicker, title, lede, body):
    return f'''<section class="page"><div class="kicker">{kicker}</div><h1>{title}</h1>
<p class="lede">{lede}</p>{body}<footer><span>NEKA · Laporan Riset Independen</span><span>{n}</span></footer></section>'''

EST = '<span class="tag est">EST</span>'
DATA = '<span class="tag data">DATA</span>'

css = f'''
@page {{ size: 297mm 210mm; margin: 0; }}
* {{ box-sizing: border-box; }}
body {{ margin:0; font-family: Inter, sans-serif; color:{INK}; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
.page {{ width:297mm; height:210mm; padding:14mm 16mm 12mm 16mm; position:relative; background:#FAF9F7; page-break-after:always; overflow:hidden; }}
.kicker {{ font-size:8.6pt; letter-spacing:.18em; font-weight:700; color:{BLUE}; text-transform:uppercase; }}
h1 {{ font-size:21pt; line-height:1.15; margin:4px 0 6px; color:{NAVY}; font-weight:800; letter-spacing:-.01em; max-width:250mm; }}
.lede {{ font-size:10.4pt; color:#3B4150; margin:0 0 12px; max-width:240mm; line-height:1.45; }}
.hl {{ background:#FCE7A6; padding:0 2px; }}
footer {{ position:absolute; bottom:8mm; left:16mm; right:16mm; border-top:1px solid #DDD; padding-top:5px; display:flex; justify-content:space-between; font-size:7.6pt; color:{MUTED}; }}
.grid {{ display:grid; gap:12px; }}
.g2 {{ grid-template-columns: 1fr 1fr; }} .g3 {{ grid-template-columns: 1fr 1fr 1fr; }} .g4 {{ grid-template-columns: repeat(4,1fr); }}
.card {{ background:#fff; border:1px solid #E5E3DE; border-radius:10px; padding:12px 14px; }}
.soft {{ background:#F0EEEA; border-radius:10px; padding:12px 14px; }}
.card h3, .soft h3 {{ font-size:11pt; margin:0 0 8px; color:{INK}; }}
.kpi {{ background:#F0EEEA; border-radius:10px; padding:9px 13px; }}
.kpi .v {{ font-size:19pt; font-weight:800; color:{NAVY}; line-height:1.1; }}
.kpi .l {{ font-size:8.8pt; margin-top:4px; font-weight:600; }}
.kpi .s {{ font-size:7.8pt; color:{MUTED}; margin-top:4px; line-height:1.35; }}
.tag {{ font-size:6.6pt; font-weight:700; padding:1px 5px; border-radius:3px; letter-spacing:.05em; vertical-align:middle; margin-left:4px; }}
.tag.est {{ background:#FBE1DC; color:#B03A2E; }} .tag.data {{ background:#DCE5FB; color:#2341A8; }}
.blk {{ border-left:3px solid {BLUE}; padding:3px 0 3px 10px; font-size:9.1pt; line-height:1.45; }}
.blk b {{ color:{NAVY}; }}
ul {{ margin:0; padding-left:15px; }} li {{ font-size:8.8pt; line-height:1.42; margin-bottom:3px; }}
table {{ width:100%; border-collapse:collapse; font-size:8.4pt; }}
th {{ text-align:left; font-size:7.2pt; letter-spacing:.08em; text-transform:uppercase; color:{MUTED}; border-bottom:1.5px solid #333; padding:5px 6px; }}
td {{ border-bottom:1px solid #E3E1DC; padding:4px 6px; vertical-align:top; line-height:1.35; }}
tr.hi td {{ background:#EAF0FD; }}
td.r, th.r {{ text-align:right; }}
.note {{ font-size:7.4pt; color:{MUTED}; line-height:1.4; margin-top:6px; }}
.legend {{ font-size:8pt; color:{MUTED}; display:flex; gap:12px; align-items:center; margin-bottom:4px; }}
.sw {{ display:inline-block; width:9px; height:9px; border-radius:2px; margin-right:4px; vertical-align:middle; }}
.num {{ display:inline-flex; width:22px; height:22px; border-radius:50%; background:{BLUE}; color:#fff; font-weight:700; font-size:9pt; align-items:center; justify-content:center; flex:none; }}
.step {{ display:flex; gap:10px; margin-bottom:9px; }} .step b {{ font-size:9.6pt; }} .step div div {{ font-size:8.4pt; color:#3B4150; line-height:1.4; }}
.box {{ border:1px solid #DCDCE4; background:#fff; border-radius:6px; padding:6px 9px; font-size:8.4pt; }}
.box.dark {{ background:{BLUE}; color:#fff; border-color:{BLUE}; }}
.arrow {{ text-align:center; color:#666; font-size:8pt; margin:2px 0; }}
.swot div {{ border-radius:10px; padding:11px 13px; }} .swot h4 {{ margin:0 0 6px; font-size:10pt; }}
.S {{ background:#E3EDE2; }} .W {{ background:#F9E3DE; }} .O {{ background:#E1E8F7; }} .T {{ background:#F5EBD9; }}
.cover {{ background:{NAVY}; color:#fff; padding:18mm 20mm; }}
.cover .bar1 {{ position:absolute; right:22mm; top:0; bottom:0; width:7mm; background:#3E52B8; }}
.cover .bar2 {{ position:absolute; right:0; top:0; bottom:0; width:22mm; background:{YEL}; }}
.verdict {{ background:{NAVY}; color:#fff; border-radius:10px; padding:11px 14px; font-size:9.1pt; line-height:1.5; }}
.verdict b {{ color:{YEL}; }}
.src li {{ font-size:7.7pt; margin-bottom:3.5px; line-height:1.35; }}
.src b {{ font-weight:700; }}
.photo img {{ width:100%; border-radius:6px; display:block; }}
.cap {{ font-size:7.4pt; color:{MUTED}; margin-top:5px; }}
'''

pages = []

# ---- Cover
pages.append(f'''<section class="page cover"><div class="bar1"></div><div class="bar2"></div>
<div style="font-size:8.6pt;letter-spacing:.2em;font-weight:700;color:#AFC0FF">LAPORAN RISET INDEPENDEN · RETAIL INTELLIGENCE</div>
<div style="margin-top:38mm;font-size:33pt;font-weight:800;line-height:1.12;max-width:215mm;">NEKA: Model Bisnis, Store Concept &amp; Prospek Format Diskon Rumah Tangga ACES</div>
<div style="margin-top:8mm;font-size:12.5pt;line-height:1.5;max-width:200mm;color:#DCE2FF">Bagaimana PT Aspirasi Hidup Indonesia Tbk (Grup Kawan Lama) membuka 35 toko diskon di ruko permukiman dalam 13 bulan, berapa kira-kira keekonomiannya per toko, dan apa yang belum terbukti</div>
<div style="position:absolute;left:20mm;right:60mm;bottom:16mm;border-top:1px solid #4A5A9E;padding-top:10px;display:flex;gap:28mm;font-size:8pt;color:#C9D1F5">
<div>Tanggal data<br><b style="color:#fff;font-size:10pt">27 November 2026</b></div>
<div>Sudut pandang<br><b style="color:#fff;font-size:10pt">Analis independen</b></div>
<div>Basis data<br><b style="color:#fff;font-size:10pt">Sumber publik saja</b></div></div></section>''')

# ---- 01 Executive summary
pages.append(page(2, "01 · Ringkasan Eksekutif",
  "NEKA: opsi pertumbuhan yang murah dan masuk akal, tetapi belum menjadi mesin pertumbuhan",
  'NEKA adalah toko diskon kebutuhan rumah dan gaya hidup milik ACES. <span class="hl">Tokonya berupa ruko kecil (&lt;700 m²) di jalan permukiman pinggiran kota dan kota tier-2,</span> dengan harga mulai Rp5 ribu. Jaringannya tumbuh cepat dan sudah menyebar ke 8 provinsi, tetapi lajunya masih di bawah target manajemen. Profitabilitas per tokonya juga belum pernah diungkap.',
  f'''<div class="grid g4" style="margin-bottom:12px">
<div class="kpi"><div class="v">35</div><div class="l">Toko per 31 Okt 2026 {DATA}</div><div class="s">+25 toko sejak awal 2026; 31 toko per 30 Sep (laporan 9M26)</div></div>
<div class="kpi"><div class="v">Rp0,15–0,25 T</div><div class="l">Run-rate omzet tahunan {EST}</div><div class="s">35 toko × Rp0,36–0,60 M/bulan; ≈2–3% pendapatan ACES (annualisasi)</div></div>
<div class="kpi"><div class="v">25 / 40–50</div><div class="l">Toko baru 2026: realisasi vs target {DATA}</div><div class="s">Per Okt 2026; perlu 15–25 toko lagi dalam 2 bulan</div></div>
<div class="kpi"><div class="v">~126 toko</div><div class="l">Proyeksi akhir 2028 (dasar) {EST}</div><div class="s">Rentang skenario 87–189; MR. DIY sudah 1.416 toko</div></div></div>
<div class="grid g2" style="gap:10px 22px">
<div class="blk"><b>Konsep:</b> toko diskon "aneka kebutuhan rumah &amp; gaya hidup" untuk konsumen massal. Manajemen mengklaim lebih dari 10 ribu SKU dalam 15+ kategori, rata-rata belanja Rp80–100 ribu, dan &lt;10 karyawan per toko. Tagline-nya "Belanja Hepi, Gak Mikir Lagi!".</div>
<div class="blk"><b>Pola ekspansi:</b> dimulai dari Jabodetabek–Banten (10 toko di 2025), lalu melompat ke Lampung, Palembang, Semarang, Solo, Yogya, Cirebon dan Kediri pada 2026. Pembiayaannya dari kas internal ACES, yang tidak punya utang berbunga.</div>
<div class="blk"><b>Pembeda vs MR. DIY:</b> menjual FMCG (Mayora, Wings, Aice) dan produk kecantikan yang tidak ada di MR. DIY, ditambah white label NEKA serta Krisbow/KRIS. SKU yang tumpang tindih dengan AZKO di bawah 5%, sehingga risiko saling makan pasar dengan AZKO rendah.</div>
<div class="blk"><b>Keekonomian per toko (estimasi):</b> omzet sekitar Rp0,45 M/bulan dan margin kotor yang ditargetkan sekitar 45% memberi kontribusi toko sekitar 11%. Balik modal ±3 tahun pada skenario dasar. Titik impas sekitar 120 transaksi per hari.</div>
<div class="blk"><b>Yang belum terbukti:</b> laba per toko, kemampuan menjaga margin kotor 45% di tengah persaingan harga dengan MR. DIY (margin kotor MR. DIY sendiri turun sekitar 4 poin dalam setahun), dan kemampuan mempercepat pembukaan toko ke 4–6 per bulan.</div>
<div class="blk"><b>Dampak bagi ACES:</b> kecil hingga 2028. Pada skenario dasar, omzet NEKA sekitar Rp0,5 T atau ±5% pendapatan ACES. NEKA baru menjadi material jika laju pembukaan naik ke ≥6 toko/bulan dengan produktivitas per toko yang terjaga.</div></div>
<div class="note"><span class="tag data">DATA</span> diungkapkan perusahaan atau media · <span class="tag est">ESTIMASI</span> perhitungan analis. Omzet per toko diturunkan dari kunjungan toko oleh BRI Danareksa Sekuritas (Jan 2026; 150–200 transaksi/hari × Rp80–100 ribu).</div>'''))

# ---- 02 Profile & trajectory
pages.append(page(3, "02 · Profil & Trajektori Pertumbuhan",
  "Dari 1 ke 35 toko dalam 13 bulan; laju naik sejak Juni 2026",
  "Fase uji di Jabodetabek–Banten menghasilkan 10 toko hingga akhir 2025. Kuartal I-2026 nyaris diam (hanya +2 toko). Sejak Juni lajunya naik ke rata-rata 4,2 toko per bulan, dan jaringan masuk ke Sumatera serta Jawa Tengah–Timur.",
  f'''<div class="grid" style="grid-template-columns:1.55fr 1fr">
<div class="card"><h3>Jumlah toko NEKA (akhir periode)</h3>
<div class="legend"><span><span class="sw" style="background:{BLUE}"></span>Aktual</span><span><span class="sw" style="background:{LBLUE}"></span>Proyeksi skenario dasar</span>{EST}</div>
{c_growth}
<div class="note">Sumber: Sep-25 dari blog lokal (toko pertama Serang, 23 Sep 2025). Des-25 dan Mar-26 dari rilis dan paparan ACES. Jun-26 (20) dan Agu-26 (26) dari paparan publik 10 Sep 2026. Sep-26 (31) dari laporan 9M26. Okt-26 (35) = 31 + 4 toko yang dibuka di bulan Oktober. Belum ditemukan pengumuman pembukaan di bulan November. P = proyeksi.</div></div>
<div>
<div class="soft" style="margin-bottom:10px"><h3>Struktur kepemilikan</h3>
<div class="box"><b>Grup Kawan Lama</b> · pemegang saham pengendali</div><div class="arrow">▼</div>
<div class="box"><b>PT Aspirasi Hidup Indonesia Tbk (ACES)</b><br>AZKO (282 toko), Toys Kingdom, ATARU, Pendopo</div><div class="arrow">▼ merek/format baru</div>
<div class="box dark"><b>NEKA</b> · diluncurkan Q3-2025<br>GM Sales Operations: Amir Situmorang</div></div>
<div class="soft"><h3>Fakta kunci</h3><ul>
<li>Toko pertama: Jl. Ahmad Yani 152, Serang, dibuka 23 Sep 2025 (sumber: blog lokal, belum dikonfirmasi rilis resmi)</li>
<li>Diperkenalkan resmi ke media pada 29–30 Jan 2026; kontribusinya dipandu &lt;5% pendapatan dan laba ACES pada 2026</li>
<li>Target 2026: 40–50 toko baru (Apr 2026), masih dipertahankan per Nov 2026 menurut BRI Danareksa</li>
<li>Pendanaan internal: ACES dalam posisi kas bersih, tanpa utang berbunga</li></ul></div></div></div>'''))

# ---- 03 Market & target
pages.append(page(4, "03 · Pasar & Target Market",
  "Membidik keluarga muda kelas menengah-bawah di permukiman padat, bukan pengunjung mal",
  "Dari 30 toko yang lokasinya teridentifikasi, belum ada satu pun yang berada di mal. Semuanya ruko di jalan raya permukiman, di kota satelit Jabodetabek, ibu kota provinsi di Sumatera, dan kota tier-2 di Jawa.",
  f'''<div class="grid g3">
<div class="card"><h3>Sebaran 35 toko per klaster</h3>{c_cluster}
<div class="note">Jabodetabek: Ciputat, Ciledug, Kreo, Pinang, Cisoka, Condet, Meruya, Hankam, Jatimakmur, Meruyung, Dramaga, Leuwiliang, Cilendek. Lampung: Bandar Jaya, Ratu Dibalau, Urip, Metro, Diponegoro. Jateng &amp; DIY: Kaliurang, Gedong Kuning, Semarang Hasanudin dan Mulawarman, Nusukan (Solo). Sumsel: M. Isa (Palembang), Kayuagung. Ada 5 toko yang dibuka Jul–Agu 2026 tanpa rilis lokasi.</div></div>
<div class="card"><h3>Segmen sasaran</h3>
<div class="step"><span class="num">1</span><div><b>Keluarga muda &amp; pelajar usia 20–40 tahun</b><div>Sasaran yang dinyatakan manajemen. Kunjungan broker ke toko Jatimakmur (Bekasi) mencatat lalu lintas pembeli dari pelajar dan ibu rumah tangga, karena toko dekat sekolah.</div></div></div>
<div class="step"><span class="num">2</span><div><b>"Mass customer" di pinggiran kota &amp; tier 2–3</b><div>Kawasan padat yang "belum terlayani optimal oleh ritel modern" (rilis ACES, Sep 2026).</div></div></div>
<div class="step"><span class="num">3</span><div><b>Pembeli harian bernilai kecil</b><div>Rata-rata transaksi Rp80–100 ribu. Barang terlaris: aksesori, alat tulis, dan sebagian perlengkapan rumah tangga (BRIDS).</div></div></div>
<div class="note">Segmen 1 dan 2 dinyatakan manajemen. Segmen 3 disimpulkan dari data transaksi.</div></div>
<div class="card"><h3>Pola lokasi &amp; perilaku</h3><ul>
<li><b>Dekat aktivitas harian:</b> ruko di jalan arteri permukiman, dekat sekolah dan perumahan</li>
<li><b>Lompat ke ibu kota provinsi di luar Jawa:</b> Lampung menjadi klaster terbesar kedua (5 toko)</li>
<li><b>Mengisi celah di bawah AZKO:</b> AZKO berada di mal/standalone besar; NEKA di lokasi yang terlalu kecil untuk AZKO</li></ul>
<h3 style="margin-top:12px">Konteks pasar {DATA}</h3><ul>
<li>Konsumsi rumah tangga Q2-2026 tumbuh 5,06% yoy, tetapi ekonom (CORE, BRI) menilai daya beli kelas menengah-bawah masih tertekan</li>
<li>20% kelompok terkaya menyumbang ±45% konsumsi rumah tangga (CORE)</li>
<li>SSSG ACES melambat dari 4,3% (Q1) ke 2,2% (H1) dan 2,4% (9M26)</li></ul></div></div>'''))

# ---- 04 Merchandise & marketing
pages.append(page(5, "04 · Barang Jualan & Strategi Marketing",
  "Yang dijual adalah harga murah dan kunjungan rutin; FMCG menjadi pembeda",
  'Kategori NEKA mirip MR. DIY. <span class="hl">Bedanya, NEKA menjual camilan, minuman, es krim dan produk kecantikan</span> agar orang datang lebih sering, ditambah white label NEKA dan merek grup Kawan Lama.',
  f'''<div class="grid" style="grid-template-columns:1fr 1.35fr 1fr">
<div class="card"><h3>Merchandise mix</h3><table><tr><th>Kategori</th><th>Catatan</th></tr>
<tr class="hi"><td><b>Aksesori &amp; alat tulis</b></td><td><b>Terlaris</b> menurut kunjungan toko BRIDS</td></tr>
<tr><td>Rumah tangga, dapur, kebersihan, penyimpanan</td><td>Inti assortment; sebagian white label NEKA</td></tr>
<tr><td>Listrik, gadget &amp; aksesori elektronik</td><td>Kipas portabel, power bank, earphone; overlap kecil dengan AZKO</td></tr>
<tr><td>Snack, minuman &amp; kecantikan</td><td>Mayora, Wings, Paragon, Aice: pembeda vs MR. DIY</td></tr>
<tr><td>Otomotif, olahraga, travel, mainan</td><td>Terlihat di foto toko (karpet dan perawatan mobil)</td></tr>
<tr><td>Dekorasi, tekstil, taman &amp; hewan</td><td>Sesuai daftar kategori resmi</td></tr></table>
<div class="note">Klaim manajemen &gt;10 ribu SKU; BRIDS hanya menghitung ±4 ribu SKU di Jatimakmur (Jan 2026).</div></div>
<div class="card"><h3>Value proposition vs pesaing</h3><table>
<tr><th>Atribut</th><th>NEKA</th><th>MR. DIY</th><th>AZKO</th></tr>
<tr><td>Lokasi</td><td><b>Ruko jalan permukiman</b></td><td>Ruko, mal, hingga kota kecil</td><td>Mal &amp; standalone kota</td></tr>
<tr><td>Luas toko</td><td><b>&lt;700 m²</b> (400–800)</td><td>Tidak diungkap</td><td>2.000–2.500 m²</td></tr>
<tr class="hi"><td>Harga</td><td><b>Mulai Rp5 ribu; rak serba Rp10 ribu/Rp25 ribu</b></td><td>Harga rendah, perkakas lengkap</td><td>Menengah–atas</td></tr>
<tr><td>Pembeda</td><td>FMCG + kecantikan + white label</td><td>Skala 1.416 toko, variasi perkakas</td><td>Luas assortment, layanan</td></tr>
<tr><td>Tenaga kerja</td><td>7 orang / 2 shift</td><td>Tidak diungkap</td><td>&gt;2× NEKA (toko standalone kecil)</td></tr>
<tr><td>Margin kotor</td><td>Target ±45%</td><td>51,3% (9M26)</td><td>47–48%</td></tr></table>
<div class="note">MR. DIY: margin kotor dihitung dari laba kotor Rp3,69 T ÷ pendapatan Rp7,19 T (9M26). AZKO dan NEKA: BRIDS (Jan 2026). Perbandingan harga per barang belum dilakukan.</div></div>
<div class="card"><h3>Taktik promosi</h3><ul>
<li><b>Jangkar harga:</b> spanduk "Harga mulai dari Rp5 ribu" di fasad</li>
<li><b>Rak harga tetap:</b> serba Rp10.000 dan Rp25.000 (blog lokal)</li>
<li><b>Maskot &amp; tagline:</b> kucing oranye "Niko", "Belanja Hepi, Gak Mikir Lagi!"</li>
<li><b>Impulse buying:</b> freezer Aice di depan toko, snack dan aksesori ponsel di kasir</li>
<li><b>Community marketing:</b> disebut manajemen sebagai pendorong produktivitas</li></ul>
<h3 style="margin-top:10px">Omnichannel</h3><ul>
<li>Instagram @haloneka; domain neka.id disebut media (tidak dapat diakses saat riset)</li>
<li>Belum ditemukan penjualan online NEKA atau integrasi ke ruparupa</li>
<li>Program loyalti khusus NEKA: tidak ditemukan</li></ul></div></div>'''))

# ---- 05 Store concept
pages.append(page(6, "05 · Store Concept",
  "Satu format inti: ruko kecil berfasad biru-kuning dengan rak terbuka",
  "Fasad berfungsi sebagai papan iklan: logo besar, spanduk harga mulai Rp5 ribu, dan maskot. Di dalam, rak putih dengan keranjang warna-warni membuat toko terlihat penuh barang dan mudah dijelajahi.",
  f'''<div class="grid" style="grid-template-columns:1fr 1.05fr 0.95fr">
<div class="card photo"><img src="assets/neka-fasad.webp"><div class="cap">Fasad toko NEKA: ruko 2–3 lantai dengan parkir depan. Foto dari pemesan laporan; lokasi tidak disebutkan.</div></div>
<div class="card photo"><img src="assets/neka-interior.webp"><div class="cap">Interior: zona snack dengan pegboard, kasir dengan barang impulsif, lorong storage, dan lorong otomotif. Sumber foto sama.</div></div>
<div class="soft"><h3>Anatomi toko</h3>
<div class="step"><span class="num">1</span><div><b>Fasad &amp; papan nama</b><div>Biru-kuning, logo NEKA berukuran besar, terbaca dari jalan raya</div></div></div>
<div class="step"><span class="num">2</span><div><b>Spanduk jangkar harga</b><div>"Aneka Kebutuhan Rumah &amp; Gaya Hidup – Harga mulai dari Rp5 ribu"</div></div></div>
<div class="step"><span class="num">3</span><div><b>Teras aktif</b><div>Freezer es krim, maskot Niko, area promo; parkir motor/mobil di depan</div></div></div>
<div class="step"><span class="num">4</span><div><b>Interior swalayan</b><div>Rak terbuka, keranjang warna, signage kategori; kasir dikelilingi snack dan aksesori</div></div></div>
<div class="step"><span class="num">5</span><div><b>Operasi ramping</b><div>7–&lt;10 karyawan, 2 shift; buka 09.00–22.00 setiap hari</div></div></div></div></div>
<table style="margin-top:10px"><tr><th>Format</th><th class="r">Jumlah</th><th>Lokasi</th><th>Luas</th><th>SKU</th><th>Peran</th></tr>
<tr><td><b>Ruko standalone</b></td><td class="r">35</td><td>Jalan raya permukiman, kota satelit &amp; tier-2</td><td>400–800 m² (paparan terbaru: &lt;700 m²)</td><td>±4 ribu (observasi) s.d. &gt;10 ribu (klaim)</td><td>Format inti</td></tr>
<tr><td>Ruko bertingkat (contoh: M. Isa Palembang)</td><td class="r">≥1</td><td>Kota besar luar Jawa</td><td>3 lantai (blog lokal)</td><td>Tidak diungkap</td><td>Variasi untuk lokasi padat</td></tr></table>
<div class="note">Belum ada format shop-in-shop di AZKO atau mal yang teridentifikasi.</div>'''))

# ---- 06 Unit economics
pages.append(page(7, "06 · Capex & Unit Economics",
  "Skenario dasar: satu toko NEKA balik modal sekitar 3 tahun, dengan rentang yang sangat lebar",
  "ACES tidak mengungkap capex, omzet, atau laba per toko NEKA. Estimasi di bawah dibangun dari data transaksi hasil kunjungan broker, target margin kotor manajemen, dan biaya operasional ruko yang wajar. MR. DIY dipakai sebagai patokan produktivitas.",
  f'''<div class="grid g2">
<div class="card"><h3>Asumsi per toko (per bulan) {EST}</h3><table>
<tr><th>Metrik</th><th class="r">Pesimis</th><th class="r">Dasar</th><th class="r">Optimis</th></tr>
<tr><td>Transaksi/hari × nilai rata-rata</td><td class="r">150 × Rp80rb</td><td class="r">170 × Rp88rb</td><td class="r">200 × Rp100rb</td></tr>
<tr><td>Omzet per bulan</td><td class="r">Rp360 jt</td><td class="r"><b>Rp450 jt</b></td><td class="r">Rp600 jt</td></tr>
<tr><td>Margin kotor</td><td class="r">43%</td><td class="r">45%</td><td class="r">46%</td></tr>
<tr><td>Gaji (7–8 org), sewa, utilitas</td><td class="r">Rp130 jt</td><td class="r">Rp118 jt</td><td class="r">Rp115 jt</td></tr>
<tr><td>Logistik, susut, overhead (% omzet)</td><td class="r">9%</td><td class="r">8%</td><td class="r">7%</td></tr>
<tr><td>Kontribusi toko</td><td class="r">≈ Rp0</td><td class="r"><b>Rp48 jt (11%)</b></td><td class="r">Rp119 jt (20%)</td></tr>
<tr><td>Capex (fit-out, rak, AC, IT, signage)</td><td class="r">Rp2,1 M</td><td class="r">Rp1,8 M</td><td class="r">Rp1,5 M</td></tr>
<tr class="hi"><td><b>Payback</b></td><td class="r">tidak balik modal</td><td class="r"><b>~37 bulan</b></td><td class="r">~13 bulan</td></tr></table>
<div class="note">Belum termasuk persediaan awal (±Rp0,6–0,9 M) dan sewa dibayar di muka. Cek silang: capex ACES 9M26 sebesar Rp144,8 M membiayai 19 AZKO + 21 NEKA + renovasi; angka itu konsisten dengan capex NEKA sekitar Rp1,5–2 M per toko jika AZKO standalone sekitar Rp5 M per toko.</div></div>
<div class="card"><h3>Kurva payback ilustratif per toko (Rp miliar, kumulatif) {EST}</h3>{c_payback}
<div class="note">Arus kas dianggap konstan sejak bulan pertama, tanpa masa ramp-up. Skenario pesimis berada di titik impas operasional sehingga tidak pernah menutup capex.</div></div></div>
<div class="grid g4" style="margin-top:9px">
<div class="kpi"><div class="v">~120 trx/hari</div><div class="l">Titik impas operasional per toko {EST}</div><div class="s">Biaya tetap Rp118 jt ÷ (45% − 8%) ≈ Rp319 jt/bulan</div></div>
<div class="kpi"><div class="v">74%</div><div class="l">Produktivitas vs MR. DIY {EST}</div><div class="s">Rp450 jt vs ±Rp608 jt/toko/bulan (MDIY 9M26: Rp7,19 T ÷ rata-rata 1.315 toko)</div></div>
<div class="kpi"><div class="v">45% / 51%</div><div class="l">Margin kotor NEKA (target) vs MR. DIY {DATA}</div><div class="s">Margin kotor MR. DIY turun dari 55,5% (9M25) ke 51,3% (9M26): tanda persaingan harga</div></div>
<div class="kpi"><div class="v">~1%</div><div class="l">Porsi NEKA dari pendapatan ACES 2026 {EST}</div><div class="s">±Rp75–125 M dari ±Rp9,1–9,4 T; sejalan dengan panduan manajemen "&lt;5%"</div></div></div>'''))

# ---- 07 Expansion & projections
pages.append(page(8, "07 · Strategi Ekspansi & Proyeksi",
  "Target 40–50 toko baru di 2026 kemungkinan meleset; skenario dasar ~126 toko pada akhir 2028",
  "Realisasi 25 toko baru hingga Oktober berarti NEKA perlu membuka 15–25 toko dalam November–Desember, atau 7–12 toko per bulan. Itu 2–3 kali laju terbaiknya selama ini. Modal bukan kendala; yang menentukan laju adalah ketersediaan lokasi, kesiapan rantai pasok, dan bukti produktivitas toko.",
  f'''<div class="grid" style="grid-template-columns:0.9fr 1.1fr">
<div>
<div class="step"><span class="num">1</span><div><b>Uji di satu koridor (Sep–Des 2025)</b><div>10 toko di Serang, Pandeglang, Tangerang, Depok, Bogor, Bekasi, Condet</div></div></div>
<div class="step"><span class="num">2</span><div><b>Jeda &amp; lompat ke luar Jawa (Mar–Mei 2026)</b><div>Hanya 4 toko baru, semuanya di Lampung (Bandar Lampung, Bandar Jaya, Metro)</div></div></div>
<div class="step"><span class="num">3</span><div><b>Akselerasi (Jun–Agu 2026)</b><div>12 toko: Bogor, Tangerang, Palembang, Yogyakarta, Subang, dan lainnya</div></div></div>
<div class="step"><span class="num">4</span><div><b>Masuk Jawa Tengah &amp; Timur (Sep–Okt 2026)</b><div>9 toko: Semarang (2), Solo, Cirebon, Lampung, Yogyakarta, Kayuagung, Meruya, Kediri</div></div></div>
<div class="step"><span class="num">5</span><div><b>Kriteria lokasi (manajemen)</b><div>Potensi pasar lokal, estimasi penjualan per m², kesiapan rantai pasok; memakai data pelanggan grup</div></div></div>
<div class="soft" style="margin-top:6px"><h3>Target vs realisasi {DATA}</h3><table>
<tr><th>Periode</th><th class="r">Target 2026</th><th class="r">Realisasi kumulatif</th></tr>
<tr><td>Apr 2026 (target awal)</td><td class="r">40–50</td><td class="r">2 (Mar)</td></tr>
<tr><td>Agu 2026 (paparan publik)</td><td class="r">40–50</td><td class="r">16</td></tr>
<tr><td>Okt 2026</td><td class="r">40–50</td><td class="r"><b>25</b></td></tr></table></div></div>
<div><div class="card"><h3>Proyeksi jumlah toko per skenario {EST}</h3>{c_proj}</div>
<table style="margin-top:8px"><tr><th>Skenario</th><th>Laju</th><th class="r">Toko 2026</th><th class="r">Omzet 2027</th><th class="r">Omzet 2028</th><th class="r">Capex tambahan s.d. 2028</th></tr>
<tr><td>Konservatif</td><td>~2 toko/bln</td><td class="r">39</td><td class="r">~Rp0,19 T</td><td class="r">~Rp0,29 T</td><td class="r">~Rp0,09 T</td></tr>
<tr class="hi"><td><b>Dasar</b></td><td><b>~3,5 toko/bln</b></td><td class="r"><b>42</b></td><td class="r"><b>~Rp0,29 T</b></td><td class="r"><b>~Rp0,51 T</b></td><td class="r"><b>~Rp0,15 T</b></td></tr>
<tr><td>Agresif</td><td>5–6 toko/bln</td><td class="r">45</td><td class="r">~Rp0,45 T</td><td class="r">~Rp0,91 T</td><td class="r">~Rp0,26 T</td></tr></table>
<div class="note">Omzet = rata-rata jumlah toko × omzet per toko (Rp0,36 / 0,45 / 0,55 M per bulan) × 12 × faktor ramp-up (0,85 di 2027; 0,9 di 2028). Capex = toko baru × Rp1,8 M. Pada skenario dasar, NEKA ≈ 5% pendapatan ACES 2028 (asumsi ACES tumbuh 7%/tahun).</div></div></div>'''))

# ---- 08 Competition & SWOT
pages.append(page(9, "08 · Lanskap Persaingan & SWOT",
  "Pendatang kecil di arena yang dikuasai MR. DIY; skalanya 1/40",
  "NEKA bersaing langsung dengan MR. DIY di segmen diskon non-pangan menengah-bawah. MR. DIY menambah sekitar 270 toko per tahun, kira-kira delapan kali jumlah seluruh toko NEKA saat ini. Miniso dan KKV bermain di mal dengan harga lebih tinggi.",
  f'''<div class="grid" style="grid-template-columns:1.05fr 1fr">
<div><div class="card"><h3>Jumlah toko ritel diskon/gaya hidup non-pangan (2026)</h3>{c_comp}
<div class="note">MR. DIY dan AZKO per Sep 2026 (laporan 9M26). MINISO: "lebih dari 300 toko" (rilis Nov 2026; sumber lain menyebut 357–380). KKV: rencana awal 10 toko (Apr 2026). NEKA per Okt 2026.</div></div>
<table style="margin-top:8px"><tr><th></th><th>NEKA</th><th>MR. DIY</th><th>MINISO</th></tr>
<tr><td>Induk</td><td><b>ACES / Kawan Lama</b></td><td>MDIY (Mr DIY Group, Malaysia)</td><td>MINISO (Tiongkok)</td></tr>
<tr><td>Format</td><td><b>Ruko permukiman</b></td><td>Ruko &amp; mal, hingga kabupaten</td><td>Mal</td></tr>
<tr><td>Ekspansi 2026</td><td>25 toko (s.d. Okt)</td><td>202 toko (s.d. Sep); target ≥270</td><td>Format besar (SUPER MINISO)</td></tr>
<tr><td>Kinerja 9M26</td><td>Tidak diungkap</td><td>Pendapatan Rp7,19 T (+24,5%); laba Rp894 M</td><td>Tidak diungkap (non-listed ID)</td></tr></table></div>
<div class="grid g2 swot" style="gap:10px">
<div class="S"><h4>Strengths</h4><ul><li>Neraca ACES: kas bersih, tanpa utang berbunga</li><li>Sourcing dan white label grup (Krisbow/KRIS), sistem dan DC yang sudah ada</li><li>Format ramping: 7 karyawan, capex di bawah AZKO</li><li>FMCG dan kecantikan menambah frekuensi kunjungan</li><li>Overlap SKU dengan AZKO &lt;5%: kanibalisasi rendah</li></ul></div>
<div class="W"><h4>Weaknesses</h4><ul><li>Belum ada bukti toko menghasilkan laba</li><li>Skala 2,5% dari MR. DIY: daya tawar pembelian lebih lemah</li><li>Realisasi pembukaan toko di bawah target</li><li>Klaim SKU (&gt;10 ribu) jauh di atas observasi (±4 ribu)</li><li>Merek baru, belum ada kanal online sendiri</li></ul></div>
<div class="O"><h4>Opportunities</h4><ul><li>Kota tier 2–3 dan Sumatera dengan penetrasi ritel modern rendah</li><li>Konsumen makin "value-driven" saat daya beli tertekan</li><li>Menambah porsi white label untuk menaikkan margin</li><li>Data pelanggan grup untuk memilih lokasi</li></ul></div>
<div class="T"><h4>Threats</h4><ul><li>MR. DIY merebut lokasi lebih dulu; margin kotornya turun sekitar 4 poin, tanda tekanan harga</li><li>Marketplace (Shopee, TikTok Shop) untuk barang murah</li><li>Daya beli menengah-bawah melemah</li><li>Rupiah melemah dan aturan impor menekan harga pokok barang impor</li></ul></div></div></div>'''))

# ---- 09 Independent assessment
pages.append(page(10, "09 · Penilaian Independen & Indikator yang Perlu Dipantau",
  "Proposisi nilainya menjanjikan; profitabilitas dan kecepatannya belum terbukti",
  "Penilaian ini tidak memihak ACES maupun pesaingnya. Setiap kesimpulan disertai bukti yang mendukung dan hal yang bisa membuktikannya salah.",
  f'''<div class="grid g3" style="margin-bottom:12px">
<div class="card"><h3>Sudah terbukti</h3><ul>
<li><b>Bisa direplikasi lintas wilayah:</b> 8 provinsi dalam 13 bulan, termasuk Sumatera</li>
<li><b>Ada permintaan:</b> 150–200 transaksi per hari di toko yang dikunjungi broker, di atas estimasi titik impas (±120)</li>
<li><b>Tidak memakan pasar AZKO:</b> overlap SKU &lt;5%, lokasi berbeda</li>
<li><b>Didanai dengan nyaman:</b> capex NEKA hingga 2028 (dasar ±Rp0,15 T) kecil dibanding anggaran capex ACES ±Rp0,4 T per tahun</li></ul></div>
<div class="card"><h3>Belum terbukti</h3><ul>
<li><b>Laba per toko:</b> tidak ada pengungkapan; estimasi payback 1–3 tahun, atau tidak balik modal di skenario pesimis</li>
<li><b>Margin kotor 45%</b> bertahan di tengah perang harga dengan MR. DIY</li>
<li><b>Data 1 toko bisa mewakili jaringan:</b> data transaksi hanya dari 1 toko di Bekasi (Jan 2026)</li>
<li><b>Laju 4–6 toko per bulan</b> berkelanjutan; jeda di Q1-2026 menunjukkan lajunya belum stabil</li></ul></div>
<div class="card"><h3>Apa yang akan mengubah penilaian</h3><ul>
<li><b>Lebih positif:</b> ACES mulai mengungkap omzet atau SSSG NEKA; toko di luar Jawa terus dibuka; tidak ada toko yang tutup</li>
<li><b>Lebih negatif:</b> target 2026 dipangkas; ada penutupan atau relokasi toko; margin kotor ACES tertekan; pembukaan per bulan turun di bawah 2</li></ul></div></div>
<div class="grid" style="grid-template-columns:1.25fr 1fr">
<div class="card"><h3>KPI yang perlu dipantau setiap kuartal</h3><table>
<tr><th>Indikator</th><th>Sumber</th><th>Ambang perhatian</th></tr>
<tr><td>Jumlah toko &amp; toko baru per bulan</td><td>Laporan kuartalan ACES, ahi.id</td><td>&lt;2 toko/bulan selama 2 kuartal</td></tr>
<tr><td>Pengungkapan omzet/SSSG NEKA</td><td>Paparan publik, laporan tahunan</td><td>Tetap tidak diungkap hingga FY2027</td></tr>
<tr><td>Margin kotor konsolidasi ACES</td><td>Laporan keuangan</td><td>&lt;47% (target manajemen 47%)</td></tr>
<tr><td>Harga keranjang belanja NEKA vs MR. DIY</td><td>Cek harga lapangan</td><td>Selisih harga &gt;10%</td></tr>
<tr><td>Penutupan/relokasi toko</td><td>Google Maps, media lokal</td><td>Toko pertama yang tutup</td></tr></table></div>
<div><div class="verdict"><b>Kesimpulan:</b> NEKA adalah taruhan kecil yang rasional bagi ACES. Modalnya kecil, menjangkau segmen yang tidak dilayani AZKO, dan sudah ada tanda permintaan. Namun hingga data per toko diungkap, NEKA layak dinilai sebagai <b>opsi</b>, bukan pendorong laba. Pada laju sekarang, dampaknya ke ACES baru terasa (≥5% pendapatan) sekitar 2028. Bagi MR. DIY, NEKA saat ini lebih merupakan gangguan lokal daripada ancaman nasional.</div>
<div class="soft" style="margin-top:10px"><h3>Keterbatasan data</h3><ul>
<li>Ekonomi per toko adalah estimasi (hal. 7); lokasi 5 toko Jul–Agu 2026 tidak diumumkan</li>
<li>Situs ahi.id tidak dapat diakses; isi rilis diambil dari kutipan media</li>
<li>Pembukaan November 2026 belum ditemukan; jumlah toko per 27 Nov bisa &gt;35</li></ul></div></div></div>'''))

# ---- Sources
src_l = [
 ("Fortune IDN, peluncuran NEKA (30 Jan 2026)", "fortuneidn.com/business/garap-pasar-pinggir-kota-aces-tambah-merek-baru-neka-00-4pj81-fk998m"),
 ("Industry.co.id, AHI hadirkan NEKA (31 Jan 2026)", "industry.co.id/read/147685"),
 ("Fimela, AHI perkenalkan NEKA (30 Jan 2026)", "fimela.com/info/read/6268756"),
 ("Disway, strategi NEKA (30 Jan 2026)", "disway.id/read/926551"),
 ("BRI Danareksa Sekuritas, NEKA store visit (30 Jan 2026)", "brights.id/.../nekas-store-visit-takeaways"),
 ("Jawa Pos, sinergi AZKO dan NEKA (25 Feb 2026)", "jawapos.com/ekonomi/2602250254"),
 ("detikFinance, AHI hadirkan NEKA (10 Mar 2026)", "finance.detik.com/d-8393967"),
 ("Fortune IDN, target 80 gerai AZKO–NEKA (10 Apr 2026)", "fortuneidn.com/business/ekspansi-di-tengah-gejolak-global-aces-buka-80-gerai-baru-azko-neka-d-00-4pj81-b2l6ny"),
 ("KapanLagi Plus, kinerja Q1-2026 ACES (5 Mei 2026)", "plus.kapanlagi.com/...d936b2.html"),
 ("DIY International, low-end format (15 Apr 2026)", "diyinternational.com/content/news/2026/04/15"),
 ("Blog lokal: toko NEKA Serang, M. Isa Palembang, Kreo Ciledug", "nurahmanafandi.wordpress.com (2025–2026)"),
 ("Blog ritel: NEKA vs MR. DIY", "speand.blogspot.com/2025/09"),
 ("Bloomberg Technoz, laba H1-2026 ACES (4 Agu 2026)", "bloombergtechnoz.com/detail-news/117255"),
]
src_r = [
 ("Fortune IDN / IDX Channel / Investortrust / Infobank, paparan publik ACES (10–11 Sep 2026)", "fortuneidn.com, idxchannel.com, investortrust.id/business/115856, infobanknews.com"),
 ("BCA Sekuritas, serapan capex ACES (10 Sep 2026)", "bcasekuritas.co.id/latest-news/news/serapan-capex-aces-baru-rp91-miliar-hingga-semester-i-2026"),
 ("Harian Energi / Properti Terkini, paparan publik (11–14 Sep 2026)", "harianenergi.com/detail/1440905; propertiterkini.com"),
 ("Industry.co.id, laba H1 AHI (13 Sep 2026)", "industry.co.id/read/155880"),
 ("Investor.id, kondisi toko NEKA (1 Okt 2026)", "investor.id/market/456246"),
 ("Hasil pencarian rilis ahi.id: NEKA Lampung, 6 toko Juni, 5 toko Sep 2026", "ahi.id/en/news/ekspansineka; ahi.id/en/news/nekalampung"),
 ("Liputan6 / The Iconomics, kinerja 9M26 ACES (2–3 Nov 2026)", "liputan6.com/saham/read/8327002; theiconomics.com"),
 ("PintarSaham, analisis 9M26 ACES (30 Okt 2026)", "pintarsaham.id"),
 ("Investor.id, BRI Danareksa TP Rp520 (18 Nov 2026)", "investor.id/market/462440"),
 ("detikFinance / Investor.id / Indikator Bisnis, 7 toko Oktober (20–27 Nov 2026)", "finance.detik.com/d-8772016; investor.id/market/462741"),
 ("EmitenNews / Bisnis / Kontan, kinerja MDIY 9M26 (1–3 Nov 2026)", "emitennews.com; market.bisnis.com/read/20261101; industri.kontan.co.id"),
 ("Katadata, MDIY 9M25: 1.154 toko, laba kotor Rp3,20 T", "katadata.co.id/.../690344a13c3d7"),
 ("MINISO rilis Nov 2026; KKV masuk Indonesia (Apr 2026)", "kyodonewsprwire.jp/release/202611049408; jpnn.com"),
 ("Kontan / Bisnis, daya beli kelas menengah-bawah 2026", "nasional.kontan.co.id; ekonomi.bisnis.com/read/20260318"),
 ("Foto toko NEKA", "diberikan pemesan laporan"),
]
def lis(xs): return "".join(f"<li><b>{html.escape(a)}</b> {html.escape(b)}</li>" for a, b in xs)
pages.append(f'''<section class="page"><div class="kicker">Lampiran · Sumber</div><h1>Daftar sumber</h1>
<div class="grid g2 src" style="gap:20px;margin-top:10px"><ul>{lis(src_l)}</ul><ul>{lis(src_r)}</ul></div>
<p class="note" style="margin-top:14px">Laporan lengkap berbasis teks: research/neka/neka-model-bisnis.md. Beberapa situs (Bisnis.com, Kontan, ahi.id) memblokir atau tidak merespons akses otomatis. Angka dari situs tersebut diambil dari ringkasan mesin pencari dan diperiksa silang dengan sumber lain bila tersedia.</p>
<footer><span>NEKA · Laporan Riset Independen</span><span>11</span></footer></section>''')

doc = f'''<!DOCTYPE html><html lang="id"><head><meta charset="utf-8"><title>NEKA – Laporan Riset Independen</title><style>{css}</style></head><body>{"".join(pages)}</body></html>'''
OUT.write_text(doc, encoding="utf-8")
print("wrote", OUT)
