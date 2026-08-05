#!/usr/bin/env python3
"""Generate markdown report from deep research JSON files."""
import json
import glob
import os
import re
import yaml

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(BASE_DIR, "results")
FIELDS_FILE = os.path.join(BASE_DIR, "fields.yaml")
OUTPUT_FILE = os.path.join(BASE_DIR, "report.md")

# Fields to show in TOC (user-selected)
TOC_FIELDS = ["status_di_indonesia"]

# Category mapping: fields.yaml category name -> possible JSON keys
CATEGORY_MAPPING = {
    "Basic Info": ["basic_info", "Basic Info"],
    "China Trend Detail": ["china_trend_detail", "China Trend Detail"],
    "Status Indonesia Saat Ini": ["indonesia_status", "Status Indonesia Saat Ini"],
    "Analisis Lag": ["lag_analysis", "Analisis Lag"],
    "Probabilitas Transfer ke Indonesia": ["transfer_probability", "Probabilitas Transfer ke Indonesia"],
    "Faktor Pendorong": ["enabling_factors", "Faktor Pendorong"],
    "Hambatan & Faktor Pembatal": ["barriers", "Hambatan & Faktor Pembatal"],
    "Prediksi Timeline di Indonesia": ["timeline_prediction", "Prediksi Timeline di Indonesia"],
    "Dampak Sosial-Ekonomi": ["socioeconomic_impact", "Dampak Sosial-Ekonomi"],
    "Kaitan Pendidikan": ["education_connection", "Kaitan Pendidikan"],
    "Pelajaran Kebijakan dari China": ["policy_lessons", "Pelajaran Kebijakan dari China"],
    "Peluang & Rekomendasi Aksi": ["opportunities", "Peluang & Rekomendasi Aksi"],
    "Faktor Risiko & Sisi Gelap": ["risk_dark_side", "Faktor Risiko & Sisi Gelap"],
    "Contoh Kasus Konkret": ["case_examples", "Contoh Kasus Konkret"],
    "Tingkat Keyakinan & Kualitas Sumber": ["confidence", "Tingkat Keyakinan & Kualitas Sumber"],
    # English fallbacks
    "Technical Features": ["technical_features"],
    "Performance Metrics": ["performance_metrics"],
    "Business Info": ["business_info"],
}

def slugify(text):
    """Convert text to anchor-safe slug."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text.strip('-')

def get_field_value(data, field_name):
    """Look up a field in flat or nested JSON structure."""
    # 1. Top level
    if field_name in data:
        return data[field_name]
    # 2. Traverse all nested dicts
    for v in data.values():
        if isinstance(v, dict) and field_name in v:
            return v[field_name]
    return None

def is_uncertain(data, field_name, value):
    """Check if a field should be skipped."""
    uncertain_list = data.get("uncertain", [])
    if field_name in uncertain_list:
        return True
    if value is None or value == "":
        return True
    if isinstance(value, str) and "[uncertain]" in value:
        return True
    return False

def format_value(value):
    """Format a field value for markdown display."""
    if isinstance(value, list):
        if not value:
            return ""
        if all(isinstance(i, dict) for i in value):
            lines = []
            for item in value:
                parts = [f"**{k}**: {v}" for k, v in item.items()]
                lines.append(" | ".join(parts))
            return "\n".join(f"- {l}" for l in lines)
        if len(value) <= 5:
            return ", ".join(str(i) for i in value)
        return "\n".join(f"- {i}" for i in value)
    if isinstance(value, dict):
        parts = []
        for k, v in value.items():
            parts.append(f"**{k}**: {v}")
        return "; ".join(parts)
    if isinstance(value, str) and len(value) > 120:
        # Break long text into readable blockquote
        return "> " + value.replace(". ", ".\n> ")
    return str(value)

def load_fields_structure(fields_file):
    """Load fields.yaml and return ordered list of (category_name, [field_defs])."""
    with open(fields_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    categories = []
    for cat_key, cat_data in data.get("fields", {}).items():
        cat_name = cat_data.get("name", cat_key)
        fields = cat_data.get("fields", [])
        categories.append((cat_name, fields))
    return categories

def get_all_defined_fields(categories):
    """Get set of all defined field names."""
    defined = set()
    for _, fields in categories:
        for f in fields:
            defined.add(f["name"])
    return defined

def load_all_results(results_dir):
    """Load all JSON files, return list of (filename, data) sorted by item order."""
    # Define preferred sort order matching outline.yaml
    ORDER = [
        "E-Commerce_Social_Commerce",
        "Electric_Vehicles_EV",
        "Gig_Economy_Informal_Labor",
        "Short_Video_Creator_Economy",
        "Fintech_Digital_Payment",
        "Platform_Food_Beverage_Kopi_Teh_Murah",
        "Consumer_Downgrade_Trading_Down",
        "Cross-border_E-Commerce_Ekspansi_Merek_China",
        "AI_Otomasi_Tenaga_Kerja",
        "Real_Estate_Housing_Crisis",
        "Youth_Unemployment_Anti-Hustle_Culture",
        "Restrukturisasi_Pendidikan_Tinggi",
        "Smart_Manufacturing_Industry_4.0",
        "New_Energy_Solar",
        "Silver_Economy",
        "Gaming_Esports_Industry",
        "Health_Tech_Telemedicine",
        "Rural_Revitalization_Sinking_Market",
        "Emotional_Economy_GuziIP_Economy",
        "Anti-Involution_Platform_Backlash_Regulation",
        "Embodied_AI_Robot_Humanoid",
        "Low-Altitude_Economy_Drone_eVTOL",
        "Demographic_Crisis_Pernikahan_Kelahiran",
        "Instant_Retail_Quick_Commerce",
        "Consumer_Debt_Crisis_BNPL_Risk",
        "Robotaxi_Kendaraan_Otonom",
        "Pet_Economy_Single-Person_Household_Economy",
        "Vocational_Education_Reform",
        "AI+_National_Policy_Difusi_AI_Masif",
    ]
    files = glob.glob(os.path.join(results_dir, "*.json"))
    def sort_key(f):
        stem = os.path.splitext(os.path.basename(f))[0]
        try:
            return ORDER.index(stem)
        except ValueError:
            return 999
    files.sort(key=sort_key)
    results = []
    for f in files:
        with open(f, 'r', encoding='utf-8') as fh:
            data = json.load(fh)
        data["_source_file"] = os.path.basename(f)
        results.append(data)
    return results

def generate_report():
    categories = load_fields_structure(FIELDS_FILE)
    defined_fields = get_all_defined_fields(categories)
    results = load_all_results(RESULTS_DIR)

    lines = []

    # Header
    lines.append("# Indonesia Laggard vs China: Riset Tren dari China yang Akan Datang ke Indonesia")
    lines.append("")
    lines.append(f"**Total Item**: {len(results)} tren dianalisis  ")
    lines.append("**Periode Riset**: 2020–2026  ")
    lines.append("**Fokus**: Lag, kemungkinan transfer, dampak sosio-ekonomi, dan implikasi pendidikan")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Wave sections for TOC
    WAVES = {
        "🌊 Gelombang 1 — Sudah/Hampir Tiba di Indonesia": list(range(0, 8)),
        "🌊 Gelombang 2 — Baru Mulai / Belum Masif": list(range(8, 18)),
        "🌊 Gelombang 3 — Belum Ada / Horizon Jauh": list(range(18, 29)),
    }

    lines.append("## Daftar Isi")
    lines.append("")
    for wave_title, indices in WAVES.items():
        lines.append(f"### {wave_title}")
        for i in indices:
            if i >= len(results):
                continue
            data = results[i]
            name = get_field_value(data, "nama_domain") or os.path.splitext(data["_source_file"])[0]
            anchor = slugify(name)
            # TOC summary field
            toc_extras = []
            for tf in TOC_FIELDS:
                val = get_field_value(data, tf)
                if val and not is_uncertain(data, tf, val):
                    # Shorten if needed
                    short = str(val)
                    if len(short) > 50:
                        short = short[:47] + "..."
                    toc_extras.append(f"*{short}*")
            extra_str = " — " + " | ".join(toc_extras) if toc_extras else ""
            lines.append(f"{i+1}. [{name}](#{anchor}){extra_str}")
        lines.append("")

    lines.append("---")
    lines.append("")

    # Detailed content per item
    for i, data in enumerate(results):
        name = get_field_value(data, "nama_domain") or os.path.splitext(data["_source_file"])[0]
        kategori = get_field_value(data, "kategori") or ""
        anchor = slugify(name)

        lines.append(f"## {i+1}. {name}")
        if kategori:
            lines.append(f"**Kategori**: {kategori}")
        lines.append("")

        # Quick summary bar
        lag = get_field_value(data, "estimasi_lag_tahun")
        prob = get_field_value(data, "probabilitas_transfer")
        tipe = get_field_value(data, "tipe_lag")
        status = get_field_value(data, "status_di_indonesia")
        conf = get_field_value(data, "confidence_level")
        summary_parts = []
        if lag and not is_uncertain(data, "estimasi_lag_tahun", lag): summary_parts.append(f"⏱ Lag: {lag}")
        if tipe and not is_uncertain(data, "tipe_lag", tipe): summary_parts.append(f"📊 {tipe}")
        if prob and not is_uncertain(data, "probabilitas_transfer", prob): summary_parts.append(f"🎯 Prob: {prob}")
        if conf and not is_uncertain(data, "confidence_level", conf): summary_parts.append(f"🔍 Keyakinan: {conf}")
        if summary_parts:
            lines.append(" | ".join(summary_parts))
            lines.append("")

        if status and not is_uncertain(data, "status_di_indonesia", status):
            lines.append(f"> **Status di Indonesia**: {status}")
            lines.append("")

        # Per category
        for cat_name, fields in categories:
            # Skip confidence at end — we already show it in header
            cat_lines = []
            for field_def in fields:
                fname = field_def["name"]
                # Skip internal/already shown fields
                if fname in ("nama_domain", "kategori", "confidence_level", "uncertain"):
                    continue
                val = get_field_value(data, fname)
                if is_uncertain(data, fname, val):
                    continue
                formatted = format_value(val)
                if not formatted:
                    continue
                label = fname.replace("_", " ").title()
                cat_lines.append((label, formatted))

            if not cat_lines:
                continue

            lines.append(f"### {cat_name}")
            lines.append("")
            for label, formatted in cat_lines:
                if "\n" in formatted or len(formatted) > 80:
                    lines.append(f"**{label}**")
                    lines.append("")
                    lines.append(formatted)
                else:
                    lines.append(f"**{label}**: {formatted}")
                lines.append("")

        # Uncertain fields notice
        uncertain_list = data.get("uncertain", [])
        if uncertain_list:
            lines.append("### ⚠️ Field Tidak Pasti")
            lines.append("")
            for uf in uncertain_list:
                lines.append(f"- `{uf}`")
            lines.append("")

        lines.append("---")
        lines.append("")

    # Write output
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))
    print(f"✅ Report generated: {OUTPUT_FILE}")
    print(f"   Items: {len(results)}")
    wc = len("\n".join(lines).split())
    print(f"   ~{wc} words")

if __name__ == "__main__":
    generate_report()
