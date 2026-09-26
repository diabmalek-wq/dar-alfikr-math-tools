"""
Week 8 — Grade 11 Topic 6 Lesson 6-6, "Exponential and Logarithmic Equations
and Inequalities". Real LaTeX (pdflatex + Computer Modern), tight-cropped
transparent PNG. Rendered twice: 500 dpi for the slides, 260 dpi for the
documents. The index records NATURAL INCH SIZE, so both indexes carry
identical numbers and a config can point at either.

  A · Gr11 T6 L6-6  Exponential and Logarithmic Equations and Inequalities  (prefix e_)
"""
import json, os, shutil, subprocess
from PIL import Image

TMP = ".tex_w6l6"
shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(TMP)

INK, DEEP, WHITE, MAROON = "222E2D", "0E4F4C", "FFFFFF", "8A1B17"

EXPR = {
    # ============ A · Gr11 T6 L6-6  Exponential and Logarithmic Equations/Inequalities ============
    "e_title_w": (r"b^{x}=y\ \Longleftrightarrow\ x=\log_{b} y", WHITE),
    "e_def":     (r"b^{x}=y\ \Longleftrightarrow\ x=\log_{b} y", INK),

    # prior
    "e_prior_base":  (r"b^{m}=b^{n}\ \Rightarrow\ m=n", INK),
    "e_prior_inv":   (r"\log_{b}(b^{x})=x", INK),
    "e_prior_props": (r"\log_{b}(xy)=\log_{b}x+\log_{b}y", INK),

    # diagnose
    "e_d1": (r"2^{x}=8.\qquad x=\underline{\qquad}", INK),
    "e_d2": (r"\log_{3}(3^{5})=\underline{\qquad}", INK),
    "e_d3": (r"\log_{2}20-\log_{2}5=\underline{\qquad}", INK),
    "e_d4": (r"\log_{7}30\approx\underline{\qquad}\ \ (\text{3 d.p., change of base})", INK),
    "e_d5": (r"2x-1>5.\qquad x>\underline{\qquad}", INK),

    # instruction 1 — common base equations and inequalities
    "e_eq1":       (r"3^{2x-1}=27", INK),
    "e_eq1_sol":   (r"3^{2x-1}=3^{3}\ \Rightarrow\ 2x-1=3\ \Rightarrow\ x=2", INK),
    "e_ineq1":     (r"2^{x+1}\leq 32", INK),
    "e_ineq1_sol": (r"2^{x+1}\leq 2^{5}\ \Rightarrow\ x+1\leq 5\ \Rightarrow\ x\leq 4", INK),
    "e_ineq2":     (r"\left(\tfrac{1}{2}\right)^{x}<8", INK),
    "e_ineq2_sol": (r"\left(\tfrac{1}{2}\right)^{x}<\left(\tfrac{1}{2}\right)^{-3}\ \Rightarrow\ x>-3\ \ (\text{base}<1:\text{ flips})", INK),

    # instruction 2 — logarithmic equations and inequalities
    "e_leq1":      (r"\log_{2}(x+3)=4", INK),
    "e_leq1_sol":  (r"x+3=2^{4}=16\ \Rightarrow\ x=13", INK),
    "e_leq2":      (r"\log_{3}x+\log_{3}(x-2)=1", INK),
    "e_leq2_sol":  (r"x(x-2)=3^{1}\ \Rightarrow\ x^{2}-2x-3=0\ \Rightarrow\ x=3\ \ (x=-1\ \text{rejected})", INK),
    "e_lineq1":    (r"\log_{5}(x-1)\leq 2", INK),
    "e_lineq1_sol": (r"0<x-1\leq 5^{2}\ \Rightarrow\ 1<x\leq 26", INK),

    # instruction 3 — using logarithms to solve, no common base
    "e_nobase":     (r"5^{x}=40", INK),
    "e_nobase_sol": (r"x=\dfrac{\log 40}{\log 5}\approx 2.292", INK),
    "e_model":      (r"E(t)=500{,}000(0.9)^{t}", INK),
    "e_model_w":    (r"E(t)=500{,}000(0.9)^{t}", WHITE),
    "e_model_sol":  (r"500{,}000(0.9)^{t}=250{,}000\ \Rightarrow\ (0.9)^{t}=0.5\ \Rightarrow\ t=\dfrac{\log 0.5}{\log 0.9}\approx 6.58", INK),

    # quick check, guided
    "e_qc": (r"3^{x}=50", INK),
    "e_g1": (r"\log_{2}(x-1)=5", INK),
    "e_g2": (r"6^{x}=200", INK),

    # mastery gate
    "e_gate1": (r"5^{2x-1}=125", INK),
    "e_gate2": (r"\log_{4}(x+5)=3", INK),

    # worksheet / routes — tier 1
    "e_ws1":  (r"2^{x}=16", INK),
    "e_ws2":  (r"3^{x+2}=81", INK),
    "e_ws3":  (r"5^{2x}=125", INK),
    "e_ws4":  (r"2^{x-1}\geq 8", INK),
    "e_ws5":  (r"\log_{2}(x+1)=5", INK),
    "e_ws6":  (r"7^{x}=90", INK),

    # tier 2 (apply) — Saudi contexts
    "e_ws7":  (r"U(t)=U_{0}(1.08)^{t}", INK),
    "e_ws8":  (r"\log_{3}(x-4)<2", INK),
    "e_ws9":  (r"B(t)=2000(1.05)^{t}", INK),

    # tier 3 (investigate)
    "e_inv1": (r"2^{x}=-8", INK),
    "e_inv2": (r"\log_{5}(x-3)=2", INK),

    # Saudi Green Initiative production context
    "e_ctx_w":  (r"E(t)=500{,}000(0.9)^{t}", WHITE),
    "e_ctx2":   (r"(0.9)^{t}=0.30\ \Rightarrow\ t=\dfrac{\log 0.30}{\log 0.9}\approx 11.43", INK),

    # exam cards
    "e_ex_gat":  (r"4^{x}=64", INK),
    "e_ex_saat": (r"\log_{2}(x-1)=4", INK),
    "e_ex_sat":  (r"3^{x}=20", INK),
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

tex = os.path.join(TMP, "w6l6.tex")
open(tex, "w").write("\n".join(doc))
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory", TMP, tex], capture_output=True, text=True)
if r.returncode:
    print(r.stdout[-4000:])
    raise SystemExit("pdflatex failed")

for out, dpi in (("math_w6l6", 500), ("math_w6l6_doc", 260)):
    shutil.rmtree(out, ignore_errors=True)
    os.makedirs(out)
    stem = os.path.join(TMP, f"p{dpi}")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(TMP, "w6l6.pdf"), stem], check=True)
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
