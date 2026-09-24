#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Model funnel produktivitas toko: menerjemahkan efek desain fasad ke penjualan per m2 & payback.

Penjualan/tahun = pejalan lewat/hari x capture rate x konversi x nilai transaksi x hari buka
Semua input di bawah adalah CONTOH ilustratif, bukan data toko tertentu.
"""

import json
from pathlib import Path

BASE = {
    "passersby_per_day": 3000,      # pejalan yang melewati muka toko per hari
    "capture_rate": 0.10,           # masuk / lewat
    "conversion": 0.30,             # transaksi / masuk
    "atv_idr": 120_000,             # nilai transaksi rata-rata
    "area_m2": 100,
    "open_days": 360,
    "gross_margin": 0.55,
    "facade_capex_idr": 350_000_000,
}

SCENARIOS = [
    # nama, perubahan relatif capture, perubahan relatif konversi, perubahan relatif ATV
    ("Konservatif (setara efek daylight replikasi)", 0.03, 0.0, 0.0),
    ("Etalase & transparansi lebih baik", 0.08, -0.02, 0.0),
    ("Perbaiki defisit visibilitas (sign/sisi buta)", 0.15, -0.03, 0.0),
    ("Fasad + citra premium (ticket naik)", 0.08, -0.02, 0.03),
]


def annual_sales(p, dc=0.0, dv=0.0, da=0.0):
    return (p["passersby_per_day"] * p["capture_rate"] * (1 + dc) * p["conversion"] * (1 + dv)
            * p["atv_idr"] * (1 + da) * p["open_days"])


def main():
    base = annual_sales(BASE)
    rows = []
    for name, dc, dv, da in SCENARIOS:
        s = annual_sales(BASE, dc, dv, da)
        delta = s - base
        gp = delta * BASE["gross_margin"]
        rows.append({
            "scenario": name,
            "capture_change_pct": dc * 100,
            "conversion_change_pct": dv * 100,
            "atv_change_pct": da * 100,
            "sales_change_pct": round(delta / base * 100, 2),
            "sales_per_m2_idr": round(s / BASE["area_m2"]),
            "incremental_gross_profit_idr": round(gp),
            "payback_months": round(BASE["facade_capex_idr"] / gp * 12, 1) if gp > 0 else None,
        })
    # Kenaikan capture (relatif) yang dibutuhkan agar capex kembali dalam 12 & 24 bulan (konversi tetap)
    gp_base = base * BASE["gross_margin"]
    breakeven = {m: round(BASE["facade_capex_idr"] / (gp_base * m / 12) * 100, 2) for m in (12, 24, 36)}
    out = {
        "assumptions_EXAMPLE": BASE,
        "baseline_sales_idr": round(base),
        "baseline_sales_per_m2_idr": round(base / BASE["area_m2"]),
        "scenarios": rows,
        "capture_uplift_needed_pct_for_payback_months": breakeven,
    }
    Path(__file__).with_name("data").joinpath("productivity_model_output.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
