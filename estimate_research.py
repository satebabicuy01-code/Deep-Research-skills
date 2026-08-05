#!/usr/bin/env python3
"""
estimate_research.py — Estimasi token & biaya SEBELUM menjalankan /research-deep
Jalankan: python estimate_research.py [path/ke/folder/riset]

Tanpa argumen: cari outline.yaml + fields.yaml di direktori saat ini.
"""

import yaml
import glob
import os
import sys
import json
from pathlib import Path


# ── Token per field berdasarkan detail_level ─────────────────────────────────
TOKEN_PER_FIELD = {
    "brief":    200,
    "moderate": 500,
    "detailed": 1_200,
}
# Overhead per agen: system prompt + instruksi + cold start
AGENT_OVERHEAD = 4_000
# Faktor pengali web-search (hasil search dimuat ke konteks)
WEB_SEARCH_MULTIPLIER = 2.2

# Harga Sonnet (input+output gabungan, estimasi kasar)
# claude-sonnet-4-6: $3/MTok input, $15/MTok output → rata-rata ~$6/MTok
PRICE_PER_MILLION = 6.0


def find_yaml(base_dir, filename):
    matches = glob.glob(os.path.join(base_dir, "**", filename), recursive=True)
    return matches[0] if matches else None


def load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def count_fields(fields_data):
    """Hitung field per detail_level dari fields.yaml."""
    counts = {"brief": 0, "moderate": 0, "detailed": 0}
    heavy_fields = []  # field detailed yang paling mahal

    for cat_key, cat_data in fields_data.get("fields", {}).items():
        cat_name = cat_data.get("name", cat_key)
        for field in cat_data.get("fields", []):
            level = field.get("detail_level", "moderate")
            counts[level] = counts.get(level, 0) + 1
            if level == "detailed":
                heavy_fields.append((cat_name, field["name"]))

    return counts, heavy_fields


def estimate(outline_path, fields_path):
    outline = load_yaml(outline_path)
    fields  = load_yaml(fields_path)

    items      = outline.get("items", [])
    n_items    = len(items)
    exec_cfg   = outline.get("execution", {})
    per_agent  = exec_cfg.get("items_per_agent", 1)
    batch_size = exec_cfg.get("batch_size", 3)
    output_dir = exec_cfg.get("output_dir", "./results")

    # Cek item yang sudah selesai
    results_dir = os.path.join(os.path.dirname(outline_path), output_dir)
    done = len(glob.glob(os.path.join(results_dir, "*.json"))) if os.path.isdir(results_dir) else 0
    remaining = n_items - done

    counts, heavy_fields = count_fields(fields)
    total_fields = sum(counts.values())

    # Token per item (hanya untuk mengisi JSON, sebelum web search)
    json_tokens_per_item = (
        counts["brief"]    * TOKEN_PER_FIELD["brief"] +
        counts["moderate"] * TOKEN_PER_FIELD["moderate"] +
        counts["detailed"] * TOKEN_PER_FIELD["detailed"]
    )

    # Token per agen (bisa handle beberapa item sekaligus)
    tokens_per_agent_base = AGENT_OVERHEAD + json_tokens_per_item * per_agent

    # Termasuk web search overhead
    tokens_per_agent_total = tokens_per_agent_base * WEB_SEARCH_MULTIPLIER

    # Total agen yang dibutuhkan
    import math
    n_agents    = math.ceil(remaining / per_agent)
    n_batches   = math.ceil(n_agents / batch_size)

    total_tokens = tokens_per_agent_total * n_agents
    total_cost   = total_tokens / 1_000_000 * PRICE_PER_MILLION

    # Estimasi waktu (asumsikan 1 agen ~3-8 menit, berjalan paralel per batch)
    minutes_per_batch = 5  # rata-rata
    total_minutes = n_batches * minutes_per_batch

    # ── PRINT REPORT ─────────────────────────────────────────────────────────
    SEP = "─" * 62

    print(f"\n{'═'*62}")
    print(f"  ESTIMASI RISET: {outline.get('topic', 'Unknown')}")
    print(f"{'═'*62}")

    print(f"\n📋 ITEM & EKSEKUSI")
    print(SEP)
    print(f"  Total item          : {n_items}")
    print(f"  Sudah selesai       : {done}  ({'✅' if done > 0 else '—'})")
    print(f"  Sisa item           : {remaining}")
    print(f"  items_per_agent     : {per_agent}")
    print(f"  batch_size          : {batch_size}")
    print(f"  Agen yang dijalankan: {n_agents}")
    print(f"  Jumlah batch        : {n_batches}")

    print(f"\n📐 FIELD ANALYSIS")
    print(SEP)
    print(f"  Total field         : {total_fields}")
    print(f"    brief   ({TOKEN_PER_FIELD['brief']:>4} tok/field) : {counts['brief']:>3} field")
    print(f"    moderate({TOKEN_PER_FIELD['moderate']:>4} tok/field) : {counts['moderate']:>3} field")
    print(f"    detailed({TOKEN_PER_FIELD['detailed']:>4} tok/field) : {counts['detailed']:>3} field  ← paling mahal")
    print(f"  Token JSON/item     : {json_tokens_per_item:,}")

    # Indikator bahaya
    if total_fields > 35:
        print(f"\n  ⚠️  {total_fields} field = TERLALU BANYAK → target ≤25 field")
    elif total_fields > 25:
        print(f"\n  🟡 {total_fields} field = SEDANG → bisa dikurangi lagi")
    else:
        print(f"\n  ✅ {total_fields} field = AMAN")

    if counts["detailed"] > 10:
        print(f"  ⚠️  {counts['detailed']} field 'detailed' = BERAT → target ≤8")

    print(f"\n💰 ESTIMASI TOKEN & BIAYA")
    print(SEP)
    print(f"  Token/agen (base)   : {tokens_per_agent_base:>10,}")
    print(f"  Token/agen (+search): {int(tokens_per_agent_total):>10,}  (×{WEB_SEARCH_MULTIPLIER} web search)")
    print(f"  Total token         : {int(total_tokens):>10,}")
    print(f"  Estimasi biaya      : ${total_cost:>8.2f}  (Sonnet ~$6/MTok)")

    # Risiko limit
    MONTHLY_LIMIT = 5_000_000  # estimasi spending limit/sesi
    ratio = total_tokens / MONTHLY_LIMIT
    if ratio > 0.8:
        status = "🔴 TINGGI — kemungkinan besar kena limit"
    elif ratio > 0.4:
        status = "🟡 SEDANG — mungkin perlu 2 sesi"
    else:
        status = "🟢 AMAN — bisa selesai 1 sesi"
    print(f"  Risiko kena limit   : {status}")

    print(f"\n⏱️  ESTIMASI WAKTU")
    print(SEP)
    print(f"  ~{total_minutes} menit ({total_minutes//60}j {total_minutes%60}m) jika berjalan lancar")
    print(f"  (asumsi {minutes_per_batch} menit/batch, tanpa retry)")

    # Field terberat
    if heavy_fields:
        print(f"\n🏋️  FIELD 'DETAILED' PALING MAHAL (pertimbangkan → moderate):")
        print(SEP)
        for cat, fname in heavy_fields:
            print(f"  [{cat}] {fname}")

    # Saran otomatis
    print(f"\n💡 REKOMENDASI")
    print(SEP)
    suggestions = []
    if total_fields > 35:
        suggestions.append(f"Kurangi field dari {total_fields} → 20–25 (hemat ~{int((1-20/total_fields)*100)}% token)")
    if counts["detailed"] > 8:
        savings = (counts["detailed"] - 8) * (TOKEN_PER_FIELD["detailed"] - TOKEN_PER_FIELD["moderate"])
        suggestions.append(f"Ubah {counts['detailed']-8} field 'detailed' → 'moderate' (hemat ~{savings*remaining:,} token)")
    if per_agent == 1 and remaining > 10:
        suggestions.append(f"Naikkan items_per_agent: 1 → 3 di outline.yaml (hemat ~60% agen overhead)")
    if not suggestions:
        suggestions.append("Konfigurasi sudah cukup efisien!")
    for s in suggestions:
        print(f"  → {s}")

    # Perbandingan skenario — selalu pakai n_items (bukan remaining) untuk proyeksi
    proj_base = n_items  # pakai total item untuk perbandingan apples-to-apples
    print(f"\n📊 PERBANDINGAN SKENARIO (proyeksi untuk {proj_base} item)")
    print(SEP)
    scenarios = [
        ("Saat ini (kondisi aktual)",     total_fields, counts["detailed"], per_agent),
        ("Lite (≤20 field, brief++)",     20,           4,                  3),
        ("Balanced (25 field, moderate)", 25,           6,                  2),
    ]
    for label, nf, nd, ipa in scenarios:
        nm = max(0, nf - nd - 4)
        nb = max(0, nf - nd - nm)
        tok_item = nd*1200 + nm*500 + nb*200
        n_ag = math.ceil(proj_base / ipa)
        tok_total = (AGENT_OVERHEAD + tok_item*ipa) * WEB_SEARCH_MULTIPLIER * n_ag
        cost = tok_total / 1_000_000 * PRICE_PER_MILLION
        marker = " ◀ kondisi riset kamu" if label.startswith("Saat ini") else ""
        print(f"  {label:<35} {int(tok_total/1000):>5}K tok  ${cost:>5.1f}{marker}")

    print(f"\n{'═'*62}\n")


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else "."
    base = os.path.abspath(base)

    outline_path = find_yaml(base, "outline.yaml")
    fields_path  = find_yaml(base, "fields.yaml")

    if not outline_path:
        print(f"❌ outline.yaml tidak ditemukan di: {base}")
        sys.exit(1)
    if not fields_path:
        print(f"❌ fields.yaml tidak ditemukan di: {base}")
        sys.exit(1)

    print(f"📂 outline : {outline_path}")
    print(f"📂 fields  : {fields_path}")

    estimate(outline_path, fields_path)


if __name__ == "__main__":
    main()
