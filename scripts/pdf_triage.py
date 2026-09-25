"""Triage Arabic PDFs before spending anything on them.

The whole cost question is one question: does the PDF carry a REAL text layer,
or is it page images? A text layer extracts for nothing. Page images have to be
looked at, and looking is what costs.

Run this on a folder of PDFs and it says, per file, which bucket it is in and
what the cheapest route is. Reading its output costs a few hundred tokens for
any number of files; reading the files themselves would cost thousands per page.

    python3 pdf_triage.py /path/to/folder
"""
import sys, os, glob, subprocess, unicodedata

AR = range(0x0600, 0x0700)          # Arabic block


def arabic_ratio(s):
    letters = [c for c in s if c.isalpha()]
    if not letters:
        return 0.0
    return sum(ord(c) in AR for c in letters) / len(letters)


def report(path):
    try:
        txt = subprocess.run(["pdftotext", "-layout", path, "-"],
                             capture_output=True, text=True, timeout=120).stdout
    except Exception as e:
        return path, "?", 0, 0.0, 0, f"could not read ({e})"
    try:
        pages = int(subprocess.run(["pdfinfo", path], capture_output=True,
                                   text=True).stdout.split("Pages:")[1].split()[0])
    except Exception:
        pages = 0
    imgs = len(subprocess.run(["pdfimages", "-list", path], capture_output=True,
                              text=True).stdout.strip().split("\n")) - 2
    chars = len(txt.strip())
    per_page = chars / pages if pages else 0
    ratio = arabic_ratio(txt)

    if per_page > 200 and ratio > 0.30:
        verdict = "TEXT LAYER, Arabic — extract free, translate text only. CHEAPEST"
    elif per_page > 200:
        verdict = f"TEXT LAYER but only {ratio:.0%} Arabic letters — check encoding"
    elif imgs >= max(1, pages):
        verdict = "SCANNED — needs OCR before it can be read cheaply"
    else:
        verdict = "little text and few images — inspect one page by hand"
    return os.path.basename(path), pages, chars, ratio, max(imgs, 0), verdict


def main(root):
    pdfs = sorted(glob.glob(os.path.join(root, "**", "*.pdf"), recursive=True)) \
        if os.path.isdir(root) else [root]
    if not pdfs:
        print("no PDFs found at", root); return
    print(f"{'file':38s} {'pp':>4s} {'chars':>8s} {'ar':>5s} {'imgs':>5s}  verdict")
    print("-" * 118)
    buckets = {}
    for p in pdfs:
        name, pages, chars, ratio, imgs, verdict = report(p)
        buckets[verdict.split(",")[0].split(" but")[0]] = \
            buckets.get(verdict.split(",")[0].split(" but")[0], 0) + 1
        print(f"{name[:38]:38s} {pages:>4} {chars:>8} {ratio:>4.0%} {imgs:>5}  {verdict}")
    print("-" * 118)
    for k, v in sorted(buckets.items(), key=lambda kv: -kv[1]):
        print(f"  {v:>3} file(s): {k}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
