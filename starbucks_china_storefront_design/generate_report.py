#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mengubah results/*.json menjadi report.md (katalog format desain), sesuai skill research-report."""

import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent
OUTLINE = yaml.safe_load((ROOT / "outline.yaml").read_text(encoding="utf-8"))
FIELDS = yaml.safe_load((ROOT / "fields.yaml").read_text(encoding="utf-8"))
RESULTS_DIR = ROOT / OUTLINE["execution"]["output_dir"]

CATEGORY_MAPPING = {
    "basic_info": ["basic_info", "Basic Info"],
    "design_attributes": ["design_attributes", "Design Attributes"],
    "performance_metrics": ["performance_metrics", "performance", "Performance Metrics"],
    "market_positioning": ["market_positioning", "market", "Market Positioning"],
    "implications": ["implications", "Implications"],
}
CATEGORY_TITLES = {
    "basic_info": "Info Dasar",
    "design_attributes": "Atribut Desain",
    "performance_metrics": "Bukti Kinerja",
    "market_positioning": "Posisi Strategis",
    "implications": "Implikasi",
}
SUMMARY_FIELDS = ["format_type", "evidence_strength"]
INTERNAL = {"_source_file", "uncertain"}


def is_uncertain(name, value, uncertain):
    if name in uncertain or value in (None, "", []):
        return True
    return isinstance(value, str) and "[uncertain]" in value


def lookup(data, name, category):
    if name in data:
        return data[name]
    for key in CATEGORY_MAPPING.get(category, []):
        if isinstance(data.get(key), dict) and name in data[key]:
            return data[key][name]
    for v in data.values():
        if isinstance(v, dict) and name in v:
            return v[name]
    return None


def fmt(value):
    if isinstance(value, list):
        if value and all(isinstance(v, dict) for v in value):
            return "<br>".join(" | ".join(f"{k}: {v}" for k, v in d.items()) for d in value)
        if all(isinstance(v, str) and v.startswith("http") for v in value):
            return "<br>".join(f"[{v}]({v})" for v in value)
        joined = ", ".join(map(str, value))
        return joined if len(joined) <= 100 else "<br>".join(f"- {v}" for v in value)
    if isinstance(value, dict):
        return "; ".join(f"{k}: {fmt(v)}" for k, v in value.items())
    return str(value)


def anchor(text):
    return re.sub(r"[^a-z0-9\- ]", "", text.lower()).strip().replace(" ", "-")


def main():
    items = []
    for path in sorted(RESULTS_DIR.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        data["_source_file"] = path.name
        items.append(data)
    order = [i["name"] for i in OUTLINE["items"]]
    items.sort(key=lambda d: order.index(d["name"]) if d["name"] in order else len(order))

    defined = {f["name"] for c in FIELDS["field_categories"] for f in c["fields"]}
    lines = [
        f"# {OUTLINE['topic']}",
        "",
        f"Katalog format desain gerai (hasil `/research-deep`). Audiens: {OUTLINE['audience']}. "
        f"Tanggal riset: {OUTLINE['research_date']}. Nilai bertanda [uncertain] tidak ditampilkan.",
        "",
        "Analisis utama dan rekomendasi ada di [laporan_eksekutif.md](laporan_eksekutif.md).",
        "",
        "## Daftar Isi",
        "",
    ]
    for n, d in enumerate(items, 1):
        summary = " | ".join(
            f"{d.get(f)}" for f in SUMMARY_FIELDS if not is_uncertain(f, d.get(f), d.get("uncertain", []))
        )
        lines.append(f"{n}. [{d['name']}](#{anchor(d['name'])}) - {summary}")
    lines.append("")

    for d in items:
        uncertain = d.get("uncertain", [])
        lines += [f"## {d['name']}", ""]
        for cat in FIELDS["field_categories"]:
            rows = []
            for field in cat["fields"]:
                v = lookup(d, field["name"], cat["category"])
                if is_uncertain(field["name"], v, uncertain):
                    continue
                rows.append(f"| {field['description']} | {fmt(v)} |")
            if rows:
                lines += [f"### {CATEGORY_TITLES.get(cat['category'], cat['category'])}", "",
                          "| Field | Nilai |", "|---|---|", *rows, ""]
        extra = {k: v for k, v in d.items() if k not in defined and k not in INTERNAL}
        if extra:
            lines += ["### Info Lain", ""] + [f"- **{k}**: {fmt(v)}" for k, v in extra.items()] + [""]
        if uncertain:
            lines += ["### Field tidak pasti (dilewati)", ""] + [f"- {u}" for u in uncertain] + [""]

    (ROOT / "report.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"report.md ditulis ({len(items)} item)")


if __name__ == "__main__":
    main()
