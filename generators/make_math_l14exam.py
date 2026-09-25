"""Math expressions for the AP Precalculus L1-4 (1.4 Polynomial Functions and Rates of
Change) EXAM-STYLE deck (non-FIKR, 12-slide). Same pattern as make_math_l13exam.py so
lesson_l14_exam.js's eq() helper can consume it. Numbers verified in-session (Python,
numpy.poly1d root-finding + scipy CubicHermiteSpline) before being typeset here.
"""
import json, os, shutil, subprocess
from PIL import Image

OUT, TMP = "math_l14exam", ".tex_l14exam"
shutil.rmtree(OUT, ignore_errors=True); shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(OUT); os.makedirs(TMP)

INK, DEEP, WHITE, MAROON = "222E2D", "0E4F4C", "FFFFFF", "8A1B17"

EXPR = {
    "title_eq":      (r"M(x)=ax^{n}+\cdots \qquad \text{critical points: } M'(x)=0", WHITE),

    # Core Fact 1
    "cf1_method":    (r"\begin{array}{l}\text{On }[a,b]:\ \text{find every } x \text{ with } f'(x)=0,\\[2pt] \text{then compare } f(a),\,f(b),\text{ and every } f(x_{\text{crit}})\end{array}", INK),

    # Worked Example 1 — Red Sea International Airport
    "we1_setup":     (r"A(t)=t^{5}-8t^{4}+18t^{3}-8t^{2}+15,\quad 0\leq t\leq 5", INK),
    "we1_crit":      (r"A'(t)=0 \text{ at } t=0,\ 0.375,\ 2.282,\ 3.743", INK),
    "we1_table":     (r"\begin{array}{c|ccccc}t&0&0.375&2.282&3.743&5\\\hline A(t)&15&14.673&32.182&{11.262}&190\end{array}", INK),
    "we1_ans":       (r"\text{Absolute minimum: } A(3.743)\approx{11.262}", WHITE),

    # Core Fact 2
    "cf2_rule":      (r"\begin{array}{l}M''=R' \quad\Rightarrow\quad M \text{ has a point of inflection wherever } R'(x)=0,\\[2pt] \text{not where } R(x)=0\end{array}", WHITE),

    # Worked Example 2 — KAEC port
    "we2_setup":     (r"V(d)=-0.002d^{4}+0.15d^{3}-3.2d^{2}+25d+40,\quad 0\leq d\leq 45", INK),
    "we2_crit":      (r"V'(d)=0 \text{ at } d=6.642,\ 12.774,\ 36.835", INK),
    "we2_ans":       (r"N \text{ has inflection points at } d\approx{6.642,\ 12.774,\ 36.835}", WHITE),

    # Trap / Worked Example 3 — restricted domain
    "we3_given":     (r"k \text{ has a local max at } x=0 \text{ and local mins at } x=-3,\,4,\ \text{ on } [-5,8]", WHITE),
    "we3_restrict":  (r"m = k\big|_{[-2,\,6]}", INK),
    "we3_ans":       (r"m \text{ has FOUR local extrema: } x=-2\ (\min),\ 0\ (\max),\ 4\ (\min),\ 6\ (\max)", MAROON),

    # Core Fact 3
    "cf3_form":      (r"f(x)=c(x-r_{1})^{k_{1}}(x-r_{2})^{k_{2}}\cdots", INK),
    "cf3_rule":      (r"\text{degree}=\textstyle\sum k_{i} \qquad \text{leading coeff.}=c\cdot\prod (\text{each factor's own leading coeff.})^{k_{i}}", INK),

    # Worked Example 4 — factored polynomial
    "we4_setup":     (r"f(x)=(2x-5)(x+1)^{3}", INK),
    "we4_expand":    (r"f(x)=2x^{4}+x^{3}-9x^{2}-13x-5", INK),
    "we4_ans":       (r"\text{degree}={4} \qquad \text{leading coefficient}=2\cdot 1^{3}={2}", WHITE),
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

tex = os.path.join(TMP, "l14exam.tex")
open(tex, "w").write("\n".join(doc))
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory", TMP, tex], capture_output=True, text=True)
if r.returncode:
    print(r.stdout[-4000:]); raise SystemExit("pdflatex failed")
subprocess.run(["pdftocairo", "-png", "-transp", "-r", "500",
                os.path.join(TMP, "l14exam.pdf"), os.path.join(TMP, "p")], check=True)

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
