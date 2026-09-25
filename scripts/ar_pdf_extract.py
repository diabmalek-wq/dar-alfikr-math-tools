"""Extract Arabic text from a text-layer PDF, cheaply and in the right order.

Two problems have to be solved together, and neither mode of pdftotext solves
both on its own:

  pdftotext -layout   keeps word order right, but interleaves columns and text
                      boxes, so a two-column revision sheet comes out shuffled.
  pdftotext -raw      keeps each text box together, but emits Arabic in VISUAL
                      order, so every line reads back to front.

So: take -raw for the block order, then reverse the token order on any line that
carries Arabic. Latin and numeric lines are left alone.

Then strip the bidi control marks and the whitespace padding. On the sample book
that alone cut 170,853 characters to 42,589 — three quarters of the extraction
was padding, and padding costs exactly as much to read as content does.

    python3 ar_pdf_extract.py file.pdf out.txt
"""
import re, subprocess, sys

ARABIC = re.compile(r"[؀-ۿݐ-ݿﭐ-﷿ﹰ-﻿]")
BIDI = re.compile(r"[‎‏‪-‮⁦-⁩﻿]")


def fix_line(line):
    """Reverse the token order on Arabic-bearing lines, restoring logical order."""
    if not ARABIC.search(line):
        return line
    return " ".join(reversed(line.split()))


def extract(pdf):
    raw = subprocess.run(["pdftotext", "-raw", pdf, "-"],
                         capture_output=True, text=True, check=True).stdout
    t = BIDI.sub("", raw)
    t = "\n".join(fix_line(l.strip()) for l in t.split("\n"))
    t = re.sub(r"[ \t]{2,}", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return raw, t.strip()


def main():
    if len(sys.argv) < 2:
        print(__doc__); return
    pdf = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else "extracted.txt"
    raw, clean = extract(pdf)
    open(out, "w", encoding="utf-8").write(clean)
    saved = 100 - 100 * len(clean) / max(len(raw), 1)
    print(f"{len(raw):>8,} chars raw  ->  {len(clean):>8,} clean "
          f"({saved:.0f}% dropped)  ~{len(clean)//3:,} tokens to read")
    print("written to", out)


if __name__ == "__main__":
    main()
