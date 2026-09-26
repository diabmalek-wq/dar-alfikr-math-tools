"""
Week 6 — Grade 10 Topic 1 Lesson 6, "Linear Systems". Real LaTeX
(pdflatex + Computer Modern), tight-cropped transparent PNG. Rendered
twice: 500 dpi for the slides, 260 dpi for the documents. The index
records NATURAL INCH SIZE, so both indexes carry identical numbers and a
config can point at either.

  A · Gr10 T1 L6  Linear Systems   (prefix sy_)
"""
import json, os, shutil, subprocess
from PIL import Image

TMP = ".tex_w6"
shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(TMP)

INK, DEEP, WHITE, MAROON = "222E2D", "0E4F4C", "FFFFFF", "8A1B17"

EXPR = {
    # ============ A · Gr10 T1 L6  Linear Systems ============
    "sy_title_w": (r"\begin{cases} a_{1}x+b_{1}y=c_{1}\\ a_{2}x+b_{2}y=c_{2}\end{cases}", WHITE),
    "sy_def":     (r"(x,y)", INK),

    # prior knowledge
    "sy_prior_l5":   (r"f(x)=g(x)", INK),
    "sy_prior_line": (r"y=mx+b", INK),
    "sy_prior_solve": (r"2x+3=11", INK),

    # diagnose
    "sy_d1": (r"2x+3=11.\qquad x=\underline{\qquad}", INK),
    "sy_d2": (r"y=-3x+4", INK),
    "sy_d3": (r"y=2x-1\qquad y=2x+5", INK),
    "sy_d4": (r"y>x+1,\ \ \text{at the point}\ (0,0)", INK),
    "sy_d5": (r"\begin{array}{c|cc} \text{line} & x=1 & x=2\\ \hline f & 1 & 3\\ g & 5 & 3\end{array}", INK),

    # instruction 1 — one point, two equations
    "sy_sys_one":  (r"y=2x-1\qquad y=-x+5", INK),
    "sy_check_one": (r"2(2)-1=3\qquad -(2)+5=3", INK),

    # instruction 2 — three methods, one system
    "sy_row_sub":   (r"y=7-x\ \Rightarrow\ x-(7-x)=1\ \Rightarrow\ x=4,\ y=3", INK),
    "sy_row_elim":  (r"(x+y)+(x-y)=7+1\ \Rightarrow\ 2x=8\ \Rightarrow\ x=4,\ y=3", INK),
    "sy_row_graph": (r"(4,3)", INK),
    "sy_row_agree": (r"x=4,\ y=3", INK),

    # instruction 3 — systems of inequalities
    "sy_ineq_sys": (r"y\leq -x+6\qquad y> 2x-1", INK),
    "sy_test_in":  (r"(0,3):\ \ 3\leq 6\ \checkmark\ ,\ \ 3>-1\ \checkmark", INK),
    "sy_test_out": (r"(4,4):\ \ 4\leq 2\ \text{is false}", INK),

    # quick check, guided
    "sy_qc": (r"2x+y=9\qquad x-y=3", INK),
    "sy_g1": (r"y=x+2\qquad 3x+y=18", INK),
    "sy_g2": (r"y<x+3\qquad y\geq -2x+1", INK),

    # mastery gate
    "sy_gate_w": (r"x+y=7\qquad 2x-y=2", WHITE),
    "sy_gate":   (r"x+y=7\qquad 2x-y=2", INK),

    # worksheet / routes — tier 1 (four systems)
    "sy_ws1": (r"x+y=10\qquad x-y=2", INK),
    "sy_ws2": (r"2x+y=7\qquad x-y=-1", INK),
    "sy_ws3": (r"3x-2y=5\qquad x+2y=7", INK),
    "sy_ws4": (r"y=2x-3\qquad y=-x+9", INK),

    # tier 2 (apply)
    "sy_ws5": (r"y=-2x+8\qquad y=x-1", INK),
    "sy_ws6": (r"y\leq -x+7\qquad y> x-1", INK),

    # tier 3 (investigate) — a parallel pair, used as illustration
    "sy_parallel_pair": (r"y=2x+1\qquad y=2x-3", INK),

    # Saudi context — Al-Ahsa farm land/water constraints
    "sy_farm_w": (r"x+y\leq 40\qquad 3x+5y\leq 150", WHITE),
    "sy_farm":   (r"x+y\leq 40\qquad 3x+5y\leq 150", INK),
    "sy_farm_c": (r"x=25,\ y=10:\ \ 35\leq 40\ \checkmark\ ,\ \ 125\leq 150\ \checkmark", INK),
    "sy_farm_d": (r"x=0,\ y=40:\ \ 5(40)=200>150", INK),

    # exam cards
    "sy_ex_gat":  (r"x+y=8\qquad x-y=2", INK),
    "sy_ex_saat": (r"y=x+3\qquad y=-2x+9", INK),
    "sy_ex_sat":  (r"2x+3y=12\qquad x-y=1", INK),

    # ---- docs-only: classwork ----
    "sy_cw1": (r"y=2x-5\qquad x+y=13", INK),
    "sy_cw2": (r"x=y+4\qquad 2x+3y=18", INK),
    "sy_cw3": (r"2x+3y=14\qquad 2x-y=6", INK),
    "sy_cw4": (r"x+4y=9\qquad x-4y=1", INK),
    "sy_cw5": (r"y=3x+2\qquad y=3x-4", INK),
    "sy_cw6": (r"y=4x-6\qquad 2y=8x-12", INK),
    "sy_cw7": (r"y=x+4\qquad y=-3x+8", INK),
    "sy_cw_poster": (r"7p+3b\geq 210\qquad p+b\leq 40", INK),
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

tex = os.path.join(TMP, "w6.tex")
open(tex, "w").write("\n".join(doc))
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory", TMP, tex], capture_output=True, text=True)
if r.returncode:
    print(r.stdout[-4000:])
    raise SystemExit("pdflatex failed")

for out, dpi in (("math_w6", 500), ("math_w6_doc", 260)):
    shutil.rmtree(out, ignore_errors=True)
    os.makedirs(out)
    stem = os.path.join(TMP, f"p{dpi}")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(TMP, "w6.pdf"), stem], check=True)
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
