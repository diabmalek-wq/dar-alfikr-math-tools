"""
Week 9 — Grade 11 Topic 6 Lesson 6-7, "Geometric Sequences and Series". Real
LaTeX (pdflatex + Computer Modern), tight-cropped transparent PNG. Rendered
twice: 500 dpi for the slides, 260 dpi for the documents. The index records
NATURAL INCH SIZE, so both indexes carry identical numbers and a config can
point at either.

  A · Gr11 T6 L6-7  Geometric Sequences and Series  (prefix gs_)
"""
import json, os, shutil, subprocess
from PIL import Image

TMP = ".tex_w6l7"
shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(TMP)

INK, DEEP, WHITE, MAROON = "222E2D", "0E4F4C", "FFFFFF", "8A1B17"

EXPR = {
    # ============ A · Gr11 T6 L6-7  Geometric Sequences and Series ============
    "gs_title_w": (r"S_{n}=\dfrac{a_{1}(1-r^{n})}{1-r}", WHITE),
    "gs_def":     (r"a_{n}=a_{1}r^{\,n-1}", INK),

    # prior
    "gs_prior_exp":      (r"y=a\cdot b^{x}", INK),
    "gs_prior_factor":   (r"r>1:\ \text{growth}\qquad 0<r<1:\ \text{decay}", INK),
    "gs_prior_logsolve": (r"b^{x}=c\ \Rightarrow\ x=\dfrac{\log c}{\log b}", INK),

    # diagnose
    "gs_d1": (r"3,\ 6,\ 12,\ 24,\ldots\qquad r=\underline{\qquad}", INK),
    "gs_d2": (r"f(x)=5(2)^{x}.\qquad f(3)=\underline{\qquad}", INK),
    "gs_d3": (r"3^{x}=20.\qquad x\approx\underline{\qquad}\ \ (\text{2 d.p.})", INK),
    "gs_d4": (r"2+6+18+54=\underline{\qquad}", INK),
    "gs_d5": (r"5,\ 8,\ 11,\ 14,\ldots\qquad \text{arithmetic, geometric, or neither?}", INK),

    # instruction 1 — identify, recursive, explicit
    "gs_seq1":       (r"3,\ 6,\ 12,\ 24,\ 48,\ldots", INK),
    "gs_ratio_check": (r"\dfrac{6}{3}=\dfrac{12}{6}=\dfrac{24}{12}=2", INK),
    "gs_rec":        (r"a_{n}=2\,a_{n-1},\quad a_{1}=3", INK),
    "gs_exp":        (r"a_{n}=3(2)^{\,n-1}", INK),
    "gs_check_term": (r"a_{5}=3(2)^{4}=48", INK),

    # instruction 2 — derive the series formula
    "gs_series_def": (r"S_{n}=a_{1}+a_{1}r+a_{1}r^{2}+\cdots+a_{1}r^{\,n-1}", INK),
    "gs_derive1":    (r"rS_{n}=a_{1}r+a_{1}r^{2}+\cdots+a_{1}r^{\,n}", INK),
    "gs_derive2":    (r"S_{n}-rS_{n}=a_{1}-a_{1}r^{\,n}", INK),
    "gs_formula":    (r"S_{n}=\dfrac{a_{1}(1-r^{\,n})}{1-r},\quad r\neq 1", INK),
    "gs_verify":     (r"S_{4}=\dfrac{3(1-2^{4})}{1-2}=3(15)=45\ \ (=3+6+12+24)", INK),

    # instruction 3 — sigma notation and the waqf context
    "gs_sigma":       (r"\sum_{k=1}^{5}10{,}000(1.2)^{k-1}", INK),
    "gs_sigma_label": (r"\text{summand}\qquad \text{start } k=1 \qquad \text{end } k=5", INK),
    "gs_ctx":         (r"S_{5}=\dfrac{10{,}000\left(1-1.2^{5}\right)}{1-1.2}", INK),
    "gs_ctx_w":       (r"S_{5}=\dfrac{10{,}000\left(1-1.2^{5}\right)}{1-1.2}", WHITE),
    "gs_ctx_result":  (r"S_{5}=74{,}416\ \text{SAR}", INK),

    # quick check, guided
    "gs_qc": (r"a_{1}=5,\ r=3.\qquad \text{Find } S_{6}.", INK),
    "gs_g1": (r"4,\ 12,\ 36,\ 108,\ldots", INK),
    "gs_g2": (r"a_{1}=2,\ r=4.\qquad \text{Find } S_{5}.", INK),

    # mastery gate
    "gs_gate1": (r"5,\ 15,\ 45,\ 135,\ldots", INK),
    "gs_gate2": (r"a_{1}=6,\ r=2.\qquad \text{Find } S_{4}.", INK),

    # worksheet / routes — tier 1
    "gs_ws1": (r"2,\ 6,\ 18,\ 54,\ldots", INK),
    "gs_ws2": (r"100,\ 50,\ 25,\ 12.5,\ldots", INK),
    "gs_ws3": (r"a_{1}=4,\ r=3.\qquad \text{Find } S_{5}.", INK),
    "gs_ws4": (r"a_{1}=1,\ r=2.\qquad \text{Find } S_{6}.", INK),

    # tier 2 (apply)
    "gs_ws5": (r"500,\ 1000,\ 2000,\ 4000,\ldots\qquad \text{Find } S_{4}.", INK),
    "gs_ws6": (r"7,\ 14,\ 28,\ 56,\ldots", INK),

    # tier 3 (investigate)
    "gs_inv1": (r"r=1\ \Rightarrow\ S_{n}=a_{1}n", INK),
    "gs_inv2": (r"4,\ -8,\ 16,\ -32,\ldots", INK),

    # exam cards
    "gs_ex_gat":  (r"2,\ 6,\ 18,\ 54,\ldots", INK),
    "gs_ex_saat": (r"a_{1}=3,\ r=2.\qquad \text{Find } S_{5}.", INK),
    "gs_ex_sat":  (r"a_{1}=4,\ r=3.\qquad \text{Find } S_{4}.", INK),
}

keys = list(EXPR)
doc = [r"\documentclass[12pt]{article}", r"\usepackage[active,tightpage]{preview}",
       r"\usepackage{amsmath,amssymb,array}", r"\usepackage[dvipsnames]{xcolor}",
       r"\setlength\PreviewBorder{1.5pt}"]
for k, (_, c) in EXPR.items():
    doc.append(r"\definecolor{c%s}{HTML}{%s}" % (k.replace("_", ""), c))
doc.append(r"\begin{document}")
for k in keys:
    doc.append(r"\begin{preview}$\color{c%s}\displaystyle %s$\end{preview}"
               % (k.replace("_", ""), EXPR[k][0]))
doc.append(r"\end{document}")

tex = os.path.join(TMP, "w6l7.tex")
open(tex, "w").write("\n".join(doc))
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory", TMP, tex], capture_output=True, text=True)
if r.returncode:
    print(r.stdout[-4000:])
    raise SystemExit("pdflatex failed")

for out, dpi in (("math_w6l7", 500), ("math_w6l7_doc", 260)):
    shutil.rmtree(out, ignore_errors=True)
    os.makedirs(out)
    stem = os.path.join(TMP, f"p{dpi}")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(TMP, "w6l7.pdf"), stem], check=True)
    pages = sorted(f for f in os.listdir(TMP)
                   if f.startswith(f"p{dpi}-") and f.endswith(".png"))
    assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} expressions"
    idx = {}
    for k, p in zip(keys, pages):
        im = Image.open(os.path.join(TMP, p)).convert("RGBA")
        dst = os.path.join(out, k + ".png")
        im.save(dst)
        idx[k] = {"file": dst, "win": im.width / dpi, "hin": im.height / dpi,
                  "aspect": im.width / im.height}
    json.dump(idx, open(os.path.join(out, "_index.json"), "w"), indent=1)
    print(f"{len(idx)} expressions -> {out} @ {dpi} dpi")
