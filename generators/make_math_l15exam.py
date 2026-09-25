"""Math expressions for the AP Precalculus L1-5 (1.5 Polynomial Functions and Complex
Zeros) EXAM-STYLE deck (non-FIKR, 12-slide). Same pattern as make_math_l14exam.py so
lesson_l15_exam.js's eq() helper can consume it. Numbers verified in-session (Python,
numpy.poly1d root-finding + numpy.diff) before being typeset here.
"""
import json, os, shutil, subprocess
from PIL import Image

OUT, TMP = "math_l15exam", ".tex_l15exam"
shutil.rmtree(OUT, ignore_errors=True); shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(OUT); os.makedirs(TMP)

INK, DEEP, WHITE, MAROON = "222E2D", "0E4F4C", "FFFFFF", "8A1B17"

EXPR = {
    "title_eq":      (r"a+bi \text{ is a zero} \ \Rightarrow\ a-bi \text{ is also a zero}", WHITE),

    # Core Fact 1 — zeros, x-intercepts, factors, multiplicity
    "cf1_zero":      (r"p(a)=0 \ \Leftrightarrow\ (x-a) \text{ is a factor of } p \ \Leftrightarrow\ a \text{ is an } x\text{-intercept}", INK),
    "cf1_mult":      (r"\text{even multiplicity}\ \Rightarrow\ \text{touches (bounces)} \qquad \text{odd multiplicity}\ \Rightarrow\ \text{crosses}", INK),

    # Worked Example 1 — multiplicity from a graph
    "we1_setup":     (r"w(x)=(x-1)^{2}(x+2)(x+6)", INK),
    "we1_table":     (r"\begin{array}{c|ccccc}x&-6&-2&-1&1&2\\\hline w(x)&0&0&20&0&32\end{array}", INK),
    "we1_ans":       (r"x={1} \text{ has multiplicity } {2}: \text{ the graph touches (bounces), it does not cross}", WHITE),

    # Core Fact 2 — complex zeros
    "cf2_count":     (r"\deg p = n \ \Rightarrow\ p \text{ has exactly } n \text{ complex zeros (counting multiplicity)}", WHITE),
    "cf2_conj":      (r"a+bi \text{ is a non-real zero of } p \ \Rightarrow\ a-bi \text{ is also a zero of } p", WHITE),

    # Worked Example 2 — conjugate-pair cubic
    "we2_given":     (r"w \text{ is cubic}; \text{ non-real zero } 3-4i; \text{ real zero } x=-6", INK),
    "we2_conj":      (r"\text{conjugate forces a second zero: } 3+4i", INK),
    "we2_poly":      (r"w(x)=(x+6)\big(x^{2}-6x+25\big)={x^{3}-11x+150}", WHITE),

    # Trap — non-real zeros silently force the minimum degree upward
    "trap_given":    (r"\text{Given factors: } (x-4),\ (x-2i),\ (x-(1+3i))", WHITE),
    "trap_force":    (r"\begin{array}{l}(x-2i) \text{ is non-real} \Rightarrow (x+2i) \text{ must also be a factor}\\[2pt] (x-(1+3i)) \text{ is non-real} \Rightarrow (x-(1-3i)) \text{ must also be a factor}\end{array}", WHITE),
    "trap_ans":      (r"\text{least possible degree} = 1+2+2={5}\ \text{, not }3", WHITE),

    # Worked Example 3 — least-degree trap, fresh numbers
    "we3_setup":     (r"q \text{ has a real zero } x=5 \text{ with multiplicity } 3, \text{ and a non-real zero } 1-2i", INK),
    "we3_conj":      (r"1-2i \text{ is non-real} \ \Rightarrow\ 1+2i \text{ must also be a zero}", INK),
    "we3_ans":       (r"\text{least possible degree} = 3+2={5}", WHITE),

    # Core Fact 3 — even/odd polynomials and the symmetry-extrema consequence
    "cf3_odd":       (r"f(-x)=-f(x)\ \Rightarrow\ f \text{ is ODD (symmetric about the origin)}", INK),
    "cf3_even":      (r"f(-x)=f(x)\ \Rightarrow\ f \text{ is EVEN (symmetric about the } y\text{-axis)}", INK),
    "cf3_extrema":   (r"\begin{array}{l}\text{If } f \text{ is odd and } f(a) \text{ is a local max,}\\[2pt] \text{then } f(-a)=-f(a) \text{ is a local MIN — not another max}\end{array}", INK),

    # Worked Example 4a — odd-symmetry extremum trap
    "we4a_given":    (r"p \text{ is odd}; \ p(5)=-9 \text{ is a relative maximum}", INK),
    "we4a_ans":      (r"p(-5)=-p(5)={9}, \text{ a relative MINIMUM}", WHITE),

    # Worked Example 4b — successive-differences degree technique
    "we4b_table":    (r"\begin{array}{c|cccccc}x&0&1&2&3&4&5\\\hline q(x)&-4&0&20&74&180&356\end{array}", INK),
    "we4b_diffs":    (r"\Delta^{1}\!:4,20,54,106,176 \quad \Delta^{2}\!:16,34,52,70 \quad \Delta^{3}\!:18,18,18", INK),
    "we4b_ans":      (r"\Delta^{3} \text{ is constant} \ \Rightarrow\ \deg q = {3}", WHITE),
}

keys = list(EXPR)
doc = [r"\documentclass[12pt]{article}", r"\usepackage[active,tightpage]{preview}",
       r"\usepackage{amsmath,amssymb}", r"\usepackage[dvipsnames]{xcolor}",
       r"\setlength\PreviewBorder{1.5pt}"]
for k, (_, c) in EXPR.items():
    doc.append(r"\definecolor{c%s}{HTML}{%s}" % (k.replace("_", ""), c))
doc.append(r"\begin{document}")
for k in keys:
    doc.append(r"\begin{preview}$\color{c%s}\displaystyle %s$\end{preview}"
               % (k.replace("_", ""), EXPR[k][0]))
doc.append(r"\end{document}")

tex = os.path.join(TMP, "l15exam.tex")
open(tex, "w").write("\n".join(doc))
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory", TMP, tex], capture_output=True, text=True)
if r.returncode:
    print(r.stdout[-4000:]); raise SystemExit("pdflatex failed")
subprocess.run(["pdftocairo", "-png", "-transp", "-r", "500",
                os.path.join(TMP, "l15exam.pdf"), os.path.join(TMP, "p")], check=True)

pages = sorted(f for f in os.listdir(TMP) if f.startswith("p-") and f.endswith(".png"))
assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} expressions"
idx = {}
for k, p in zip(keys, pages):
    im = Image.open(os.path.join(TMP, p)).convert("RGBA")
    dst = os.path.join(OUT, k + ".png"); im.save(dst)
    idx[k] = {"file": dst, "win": im.width / 500, "hin": im.height / 500,
              "aspect": im.width / im.height}
json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
print(len(idx), "expressions typeset")
