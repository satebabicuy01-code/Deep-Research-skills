#!/usr/bin/env python3
"""
PDF-to-Markdown Extractor
Otomatis mendeteksi jenis PDF (teks/gambar/scan) dan mengekstrak teks.

Penggunaan:
    python extract_pdf.py <input.pdf> [--lang eng+ind] [--dpi 200] [--out-dir /tmp]

Output:
    JSON ke stdout berisi metadata dan teks per halaman.
    Format: {"meta": {...}, "pages": [{"page": 1, "text": "...", "method": "..."}]}
"""

import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


# ─── Coba import pdfplumber; kalau gagal, pakai fallback ─────────────────────
def _try_import_pdfplumber():
    try:
        import pdfplumber
        return pdfplumber
    except ImportError:
        return None


def _try_import_pypdf():
    try:
        from pypdf import PdfReader
        return PdfReader
    except ImportError:
        return None


# ─── Helpers ─────────────────────────────────────────────────────────────────

def check_tool(name):
    """Cek apakah tool CLI tersedia."""
    return subprocess.run(
        ["which", name], capture_output=True, text=True
    ).returncode == 0


def ensure_ghostscript():
    if check_tool("gs"):
        return True
    print("[INFO] Ghostscript tidak ditemukan. Mencoba install...", file=sys.stderr)
    r = subprocess.run(
        ["apt-get", "install", "-y", "ghostscript", "--fix-missing", "-q"],
        capture_output=True
    )
    return r.returncode == 0 and check_tool("gs")


def ensure_tesseract():
    if check_tool("tesseract"):
        return True
    print("[INFO] Tesseract tidak ditemukan. Mencoba install...", file=sys.stderr)
    r = subprocess.run(
        ["apt-get", "install", "-y", "tesseract-ocr", "tesseract-ocr-ind", "-q"],
        capture_output=True
    )
    return r.returncode == 0 and check_tool("tesseract")


def get_tesseract_langs():
    """Kembalikan daftar bahasa yang tersedia di tesseract."""
    r = subprocess.run(["tesseract", "--list-langs"], capture_output=True, text=True)
    langs = []
    for line in r.stdout.splitlines() + r.stderr.splitlines():
        line = line.strip()
        if line and not line.startswith("List") and len(line) <= 10:
            langs.append(line)
    return langs


# ─── Metode 1: Ekstraksi teks langsung (PDF berbasis teks) ───────────────────

def extract_text_pdfplumber(pdf_path):
    """Ekstrak teks menggunakan pdfplumber. Kembalikan list (page_num, text)."""
    pdfplumber = _try_import_pdfplumber()
    if pdfplumber is None:
        return None
    try:
        results = []
        with pdfplumber.open(pdf_path) as pdf:
            total = len(pdf.pages)
            for i, page in enumerate(pdf.pages):
                text = page.extract_text() or ""
                results.append((i + 1, text.strip(), total))
        return results
    except Exception as e:
        print(f"[WARN] pdfplumber gagal: {e}", file=sys.stderr)
        return None


def extract_text_pypdf(pdf_path):
    """Fallback: ekstrak teks menggunakan pypdf."""
    PdfReader = _try_import_pypdf()
    if PdfReader is None:
        return None
    try:
        reader = PdfReader(pdf_path)
        results = []
        total = len(reader.pages)
        for i, page in enumerate(reader.pages):
            text = page.extract_text() or ""
            results.append((i + 1, text.strip(), total))
        return results
    except Exception as e:
        print(f"[WARN] pypdf gagal: {e}", file=sys.stderr)
        return None


def is_text_sufficient(pages_data, min_avg_chars=80):
    """
    Cek apakah hasil ekstraksi teks cukup bermakna.
    Kalau rata-rata karakter per halaman < min_avg_chars, anggap PDF gambar.
    """
    if not pages_data:
        return False
    total_chars = sum(len(t) for _, t, _ in pages_data)
    avg = total_chars / max(len(pages_data), 1)
    return avg >= min_avg_chars


# ─── Metode 2: OCR (PDF gambar / screenshot / hasil scan) ────────────────────

def pdf_to_images(pdf_path, out_dir, dpi=200):
    """
    Render setiap halaman PDF menjadi PNG menggunakan Ghostscript.
    Kembalikan list path PNG yang dihasilkan.
    """
    if not ensure_ghostscript():
        raise RuntimeError("Ghostscript tidak dapat diinstall. Install manual: apt-get install ghostscript")

    template = os.path.join(out_dir, "page_%04d.png")
    cmd = [
        "gs", "-dNOPAUSE", "-dBATCH",
        "-sDEVICE=png16m",
        f"-r{dpi}",
        f"-sOutputFile={template}",
        str(pdf_path)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Ghostscript gagal: {result.stderr[:500]}")

    pngs = sorted(Path(out_dir).glob("page_*.png"))
    return pngs


def image_to_text_tesseract(image_path, lang="eng"):
    """
    OCR satu gambar menggunakan Tesseract.
    Kembalikan teks hasil OCR.
    """
    if not ensure_tesseract():
        raise RuntimeError("Tesseract tidak dapat diinstall. Install manual: apt-get install tesseract-ocr")

    out_base = str(image_path).replace(".png", "")
    cmd = ["tesseract", str(image_path), out_base, "-l", lang]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"[WARN] Tesseract error pada {image_path.name}: {result.stderr[:200]}", file=sys.stderr)

    txt_path = out_base + ".txt"
    if os.path.exists(txt_path):
        with open(txt_path, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read().strip()
        os.remove(txt_path)
        return text
    return ""


def run_ocr_pipeline(pdf_path, lang="eng", dpi=200):
    """
    Pipeline OCR lengkap: render halaman → OCR setiap halaman → gabungkan.
    Kembalikan list (page_num, text, total).
    """
    with tempfile.TemporaryDirectory(prefix="pdf2md_ocr_") as tmp:
        print(f"[INFO] Render PDF ke gambar (DPI={dpi})...", file=sys.stderr)
        pngs = pdf_to_images(pdf_path, tmp, dpi=dpi)
        total = len(pngs)
        print(f"[INFO] {total} halaman dirender. Menjalankan OCR (lang={lang})...", file=sys.stderr)

        results = []
        for i, png in enumerate(pngs, 1):
            print(f"[INFO]   OCR halaman {i}/{total}...", file=sys.stderr)
            text = image_to_text_tesseract(png, lang=lang)
            results.append((i, text, total))

    return results


# ─── Metode 3: Gambar langsung (PNG/JPG/JPEG screenshot) ─────────────────────

def run_ocr_on_image(image_path, lang="eng"):
    """OCR langsung pada file gambar (bukan PDF)."""
    image_path = Path(image_path)
    if not ensure_tesseract():
        raise RuntimeError("Tesseract tidak dapat diinstall.")
    text = image_to_text_tesseract(image_path, lang=lang)
    return [(1, text, 1)]


# ─── Utilitas metadata PDF ───────────────────────────────────────────────────

def get_pdf_metadata(pdf_path):
    """Ekstrak metadata dasar dari PDF."""
    meta = {"path": str(pdf_path), "filename": Path(pdf_path).name}
    pdfplumber = _try_import_pdfplumber()
    if pdfplumber:
        try:
            with pdfplumber.open(pdf_path) as pdf:
                meta["total_pages"] = len(pdf.pages)
                info = pdf.metadata or {}
                for key in ("Title", "Author", "Subject", "Creator", "Producer", "CreationDate"):
                    val = info.get(f"/{key}") or info.get(key)
                    if val:
                        meta[key.lower()] = str(val)
        except Exception:
            pass
    else:
        PdfReader = _try_import_pypdf()
        if PdfReader:
            try:
                reader = PdfReader(pdf_path)
                meta["total_pages"] = len(reader.pages)
                info = reader.metadata or {}
                for key in ("/Title", "/Author", "/Subject", "/Creator"):
                    val = info.get(key)
                    if val:
                        meta[key.lstrip("/").lower()] = str(val)
            except Exception:
                pass
    return meta


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Ekstrak teks dari PDF/gambar untuk konversi ke Markdown"
    )
    parser.add_argument("input", help="Path ke file PDF, PNG, JPG, atau JPEG")
    parser.add_argument(
        "--lang", default=None,
        help="Bahasa OCR Tesseract (mis. eng, ind, eng+ind). Default: otomatis."
    )
    parser.add_argument(
        "--dpi", type=int, default=200,
        help="Resolusi render untuk PDF gambar (default: 200)"
    )
    parser.add_argument(
        "--force-ocr", action="store_true",
        help="Paksa gunakan OCR meskipun PDF mengandung teks"
    )
    parser.add_argument(
        "--min-chars", type=int, default=80,
        help="Minimal rata-rata karakter/halaman agar dianggap PDF berteks (default: 80)"
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(json.dumps({"error": f"File tidak ditemukan: {args.input}"}))
        sys.exit(1)

    suffix = input_path.suffix.lower()
    is_image = suffix in {".png", ".jpg", ".jpeg", ".tiff", ".tif", ".bmp", ".gif", ".webp"}
    is_pdf = suffix == ".pdf"

    if not is_image and not is_pdf:
        print(json.dumps({"error": f"Format tidak didukung: {suffix}. Gunakan PDF, PNG, JPG, atau JPEG."}))
        sys.exit(1)

    # Tentukan bahasa OCR
    ocr_lang = args.lang
    if ocr_lang is None:
        available = get_tesseract_langs() if check_tool("tesseract") or ensure_tesseract() else []
        if "ind" in available and "eng" in available:
            ocr_lang = "eng+ind"
        elif "ind" in available:
            ocr_lang = "ind"
        else:
            ocr_lang = "eng"
        print(f"[INFO] Bahasa OCR otomatis: {ocr_lang}", file=sys.stderr)

    output = {"meta": {}, "pages": [], "method": ""}

    # ── GAMBAR LANGSUNG ──────────────────────────────────────────────────────
    if is_image:
        print(f"[INFO] Mode: OCR gambar langsung ({suffix})", file=sys.stderr)
        output["meta"] = {"path": str(input_path), "filename": input_path.name, "total_pages": 1}
        output["method"] = "ocr-image"
        pages_data = run_ocr_on_image(input_path, lang=ocr_lang)

    # ── PDF ──────────────────────────────────────────────────────────────────
    else:
        output["meta"] = get_pdf_metadata(input_path)

        # Coba ekstrak teks dulu (PDF berbasis teks)
        pages_data = None
        method = "ocr-pdf"

        if not args.force_ocr:
            print("[INFO] Mencoba ekstraksi teks langsung...", file=sys.stderr)
            pages_data = extract_text_pdfplumber(input_path) or extract_text_pypdf(input_path)

            if pages_data and is_text_sufficient(pages_data, args.min_chars):
                method = "text-direct"
                print(f"[INFO] PDF berbasis teks terdeteksi. Ekstraksi langsung.", file=sys.stderr)
            else:
                if pages_data:
                    avg = sum(len(t) for _, t, _ in pages_data) / max(len(pages_data), 1)
                    print(
                        f"[INFO] Teks tidak mencukupi (rata-rata {avg:.0f} karakter/halaman). "
                        f"Beralih ke OCR...", file=sys.stderr
                    )
                else:
                    print("[INFO] Ekstraksi teks gagal. Beralih ke OCR...", file=sys.stderr)
                pages_data = None

        if pages_data is None:
            print("[INFO] Mode: OCR (render + tesseract)...", file=sys.stderr)
            pages_data = run_ocr_pipeline(input_path, lang=ocr_lang, dpi=args.dpi)

        output["method"] = method

    # ── Susun output ─────────────────────────────────────────────────────────
    for page_num, text, total in pages_data:
        output["pages"].append({
            "page": page_num,
            "total": total,
            "text": text
        })

    output["meta"].setdefault("total_pages", len(output["pages"]))
    output["ocr_lang"] = ocr_lang

    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
