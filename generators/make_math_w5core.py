"""
Week 5 core lessons. Real LaTeX (pdflatex + Computer Modern), tight-cropped
transparent PNG. Rendered twice: 500 dpi for the slides, 260 dpi for the
documents. The index records NATURAL INCH SIZE, so both indexes carry
identical numbers and a config can point at either.

  A · Gr10 T1 L5  Solving Equations and Inequalities by Graphing   (prefix s_)
  B · Gr11 T6 L6-1  Key Features of Exponential Functions          (prefix x_)
"""
import json, os, shutil, subprocess
from PIL import Image

TMP = ".tex_w5core"
shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(TMP)

INK, DEEP, WHITE, MAROON = "222E2D", "0E4F4C", "FFFFFF", "8A1B17"
FR = lambda a, b: r"\dfrac{%s}{%s}" % (a, b)

EXPR = {
    # ============ A · Gr10 T1 L5  Solving Equations/Inequalities by Graphing ============
    "s_title_w": (r"f(x)=g(x)", WHITE),
    "s_def":     (r"f(x)=g(x)", INK),

    "s_lin":     (r"y=2x-1", INK),
    "s_eval":    (r"f(x)=2x-1,\qquad f(3)=\underline{\qquad}", INK),
    "s_tbl":     (r"x:\ 1,\,2,\,3\qquad y:\ {-1},\,1,\,3", INK),

    # diagnose
    "s_d1":      (r"2x-3=-x+9.\qquad x=\underline{\qquad}", INK),
    "s_d2":      (r"f(x)=3x-1.\qquad f(2)=\underline{\qquad}", INK),
    "s_d3":      (r"2x-1>x+2,\ \ \text{at}\ x=3", INK),
    "s_d4":      (r"g(x)=x^{2}-5.\qquad g(2)=-1,\ \ g(3)=4", INK),

    # instruction 1 — solving equations graphically
    "s_sys1":    (r"y=3x-2\qquad y=-x+6", INK),
    "s_check1":  (r"3(2)-2=4\qquad -(2)+6=4", INK),

    # instruction 2 — rows: equation vs inequality
    "s_row_eq":    (r"3x-2=-x+6\ \Longrightarrow\ x=2", INK),
    "s_row_ineq":  (r"3x-2>-x+6\ \Longrightarrow\ x>2", INK),
    "s_row_set":   (r"\{\,x : x>2\,\}", INK),
    "s_row_ge":    (r"3x-2\geq -x+6\ \Longrightarrow\ x\geq 2", INK),

    # instruction 3 — tables to approximate
    "s_quad_sys":  (r"y=x^{2}\qquad y=2x+1", INK),
    "s_quad_eq":   (r"x^{2}-2x-1=0\ \Longrightarrow\ x=1\pm\sqrt{2}", INK),

    # quick check, guided, gate
    "s_qc":      (r"4x-1=-2x+11", INK),
    "s_g1":      (r"3x-2=-2x+8", INK),
    "s_g2":      (r"x^{2}-4x+1=0", INK),
    "s_gate":    (r"-2x+9=3x-1", INK),
    "s_gate_w":  (r"-2x+9=3x-1", WHITE),
    "s_gate2":   (r"x^{2}-3x-1=0", INK),

    # worksheet / routes
    "s_ws1":     (r"x+3=2x-1", INK),
    "s_ws2":     (r"5-x=2x-4", INK),
    "s_ws3":     (r"-3x+7=x-1", INK),
    "s_ws4":     (r"2x+1=x+6", INK),
    "s_ws5":     (r"2x-1\geq -x+8", INK),

    # Saudi context — two ride-hailing pricing plans
    "s_ctx_w":   (r"C_{A}(d)=5+2d,\qquad C_{B}(d)=15+d", WHITE),
    "s_ctx":     (r"C_{A}(d)=5+2d,\qquad C_{B}(d)=15+d", INK),
    "s_ctx2":    (r"5+2d=15+d\ \Longrightarrow\ d=10\ \text{km},\ \ C=25\ \text{SAR}", INK),

    # exam cards
    "s_ex_gat":  (r"y=3x-2\qquad y=-x+6", INK),
    "s_ex_saat": (r"y=x+1\qquad y=-2x+10", INK),
    "s_ex_sat":  (r"y=x+2\qquad y=3x-6", INK),

    # ============ B · Gr11 T6 L6-1  Key Features of Exponential Functions ============
    "x_title_w": (r"y=a\cdot b^{x}", WHITE),
    "x_def":     (r"y=a\cdot b^{x}", INK),

    "x_exprules": (r"b^{m}\cdot b^{n}=b^{m+n}", INK),
    "x_lincontrast": (r"y=mx+b\ \ \text{adds}\ m\ \text{each step}", INK),
    "x_pct":     (r"15\%\ \text{increase}\ \Longrightarrow\ \times\,1.15", INK),

    # diagnose
    "x_d1":      (r"f(x)=2^{x}.\qquad f(0)=\underline{\qquad},\ \ f(3)=\underline{\qquad}", INK),
    "x_d2":      (r"\text{Start at }2.\ \ \text{Add }3\ \text{vs.}\ \times\,1.5,\ 5\ \text{times}", INK),
    "x_d3":      (r"8\%\ \text{increase}\ \Longrightarrow\ \text{growth factor}=\underline{\qquad}", INK),
    "x_d4":      (r"15\%\ \text{decrease}\ \Longrightarrow\ \text{decay factor}=\underline{\qquad}", INK),
    "x_d5":      (r"\begin{array}{c|cccc} x & 0 & 1 & 2 & 3\\ \hline y & 5 & 10 & 20 & 40\end{array}", INK),

    # instruction 1 — reading the graph
    "x_parent":  (r"f(x)=2^{x}", INK),
    "x_ptable":  (r"\begin{array}{c|ccccc} x & -2 & -1 & 0 & 1 & 2\\ \hline f(x) & \tfrac14 & \tfrac12 & 1 & 2 & 4\end{array}", INK),

    # instruction 2 — rows: shifts and reflections
    "x_row_shift":  (r"g(x)=2^{x}-3", INK),
    "x_row_asym1":  (r"\text{new asymptote: }y=-3", INK),
    "x_row_reflect": (r"h(x)=-2^{x}", INK),
    "x_row_range2": (r"\text{new range: }y<0", INK),

    # instruction 3 — growth/decay factors
    "x_growth_form": (r"y=a(1+r)^{t},\quad b=1+r>1", INK),
    "x_decay_form":  (r"y=a(1-r)^{t},\quad 0<b=1-r<1", INK),

    # quick check, guided, gate
    "x_qc":      (r"f(x)=5(3)^{x}", INK),
    "x_g1":      (r"f(x)=3(2)^{x}", INK),
    "x_g2":      (r"g(x)=100(0.8)^{x}", INK),
    "x_gate":    (r"f(x)=4(0.6)^{x}", INK),
    "x_gate_w":  (r"f(x)=4(0.6)^{x}", WHITE),

    # worksheet / routes
    "x_ws1":     (r"f(x)=5(1.2)^{x}", INK),
    "x_ws2":     (r"f(x)=2(0.9)^{x}", INK),
    "x_ws3":     (r"f(x)=4(3)^{x}", INK),
    "x_ws4":     (r"f(x)=10(0.5)^{x}", INK),
    "x_pctcheck": (r"\text{new}=\text{old}+0.08\cdot\text{old}=1.08\cdot\text{old}", INK),

    # Saudi context — an eco-tourism destination growing by a fixed percentage
    "x_ctx_w":   (r"V(t)=40\,000(1.25)^{t}", WHITE),
    "x_ctx":     (r"V(t)=40\,000(1.25)^{t}", INK),
    "x_ctx2":    (r"V(3)=40\,000(1.25)^{3}=78\,125\ \text{visitors}", INK),

    # exam cards
    "x_ex_saat": (r"f(x)=3(2)^{x}", INK),
    "x_ex_sat":  (r"g(t)=500(0.75)^{t}", INK),
    "x_ex_gat":  (r"200(1.10)^{2}", INK),
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

tex = os.path.join(TMP, "w5core.tex")
open(tex, "w").write("\n".join(doc))
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory", TMP, tex], capture_output=True, text=True)
if r.returncode:
    print(r.stdout[-4000:])
    raise SystemExit("pdflatex failed")

for out, dpi in (("math_w5core", 500), ("math_w5core_doc", 260)):
    shutil.rmtree(out, ignore_errors=True)
    os.makedirs(out)
    stem = os.path.join(TMP, f"p{dpi}")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(TMP, "w5core.pdf"), stem], check=True)
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
