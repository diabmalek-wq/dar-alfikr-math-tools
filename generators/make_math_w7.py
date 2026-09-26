"""
Week 7 — Grade 10 Topic 2 Lesson 1, "Vertex Form of a Quadratic Function".
Real LaTeX (pdflatex + Computer Modern), tight-cropped transparent PNG.
Rendered twice: 500 dpi for the slides, 260 dpi for the documents. The
index records NATURAL INCH SIZE, so both indexes carry identical numbers
and a config can point at either.

  A · Gr10 T2 L1  Vertex Form of a Quadratic Function  (prefix vf_)
"""
import json, os, shutil, subprocess
from PIL import Image

TMP = ".tex_w7"
shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(TMP)

INK, DEEP, WHITE, MAROON = "222E2D", "0E4F4C", "FFFFFF", "8A1B17"

EXPR = {
    # ============ A · Gr10 T2 L1  Vertex Form of a Quadratic Function ============
    "vf_title_w": (r"f(x)=a(x-h)^{2}+k", WHITE),
    "vf_def":     (r"f(x)=a(x-h)^{2}+k", INK),

    # prior
    "vf_prior_transform": (r"f(x)\ \to\ f(x-h)+k", INK),
    "vf_prior_parent":    (r"f(x)=x^{2}", INK),
    "vf_prior_eval":      (r"f(x)=x^{2}.\qquad f(-3)=9", INK),

    # diagnose
    "vf_d1": (r"y=f(x)+3", INK),
    "vf_d2": (r"y=f(x-2)", INK),
    "vf_d3": (r"f(x)=x^{2}.\qquad f(-3)=\underline{\qquad}", INK),
    "vf_d4": (r"y=(x-1)^{2}+4", INK),
    "vf_d5": (r"y=-3(x+2)^{2}-1", INK),

    # instruction 1 — reading key features (rows)
    "vf_ex1":   (r"f(x)=2(x-3)^{2}+4", INK),
    "vf_feat1": (r"\text{vertex }(3,4),\ \text{opens up, min}=4", INK),
    "vf_ex2":   (r"g(x)=-(x+1)^{2}+5", INK),
    "vf_feat2": (r"\text{vertex }(-1,5),\ \text{opens down, max}=5", INK),
    "vf_ex3":   (r"h(x)=\tfrac{1}{2}x^{2}-2", INK),
    "vf_feat3": (r"\text{vertex }(0,-2),\ \text{opens up, wider}", INK),

    # instruction 2 — graphing via transformations
    "vf_parent":      (r"y=x^{2}", INK),
    "vf_transformed": (r"f(x)=2(x-3)^{2}+4", INK),

    # instruction 3 — write vertex form from key features
    "vf_write_ex":    (r"\text{vertex }(2,-3),\quad \text{point }(4,5)", INK),
    "vf_write_sol1":  (r"5=a(4-2)^{2}-3", INK),
    "vf_write_sol2":  (r"5=4a-3\ \Rightarrow\ a=2", INK),
    "vf_write_final": (r"f(x)=2(x-2)^{2}-3", INK),

    # quick check, guided
    "vf_qc": (r"f(x)=-2(x+5)^{2}+7", INK),
    "vf_g1": (r"f(x)=(x-2)^{2}-3", INK),
    "vf_g2": (r"\text{vertex }(-1,4),\quad \text{point }(1,-4)", INK),

    # mastery gate
    "vf_gate1": (r"f(x)=3(x-1)^{2}-2", INK),
    "vf_gate2": (r"\text{vertex }(2,5),\quad \text{point }(0,1)", INK),

    # worksheet / routes — tier 1
    "vf_ws1": (r"f(x)=(x-4)^{2}+1", INK),
    "vf_ws2": (r"f(x)=-2(x+3)^{2}+6", INK),
    "vf_ws3": (r"f(x)=\tfrac{1}{3}x^{2}-5", INK),
    "vf_ws4": (r"\text{vertex }(3,-1),\quad \text{point }(5,7)", INK),

    # tier 2 (apply)
    "vf_ws5": (r"h(x)=-0.5(x-3)^{2}+5", INK),
    "vf_ws6": (r"\text{vertex }(2,4),\quad \text{point }(0,0)", INK),

    # Saudi context — decorative fountain
    "vf_fountain_w":    (r"h(x)=a(x-2)^{2}+4", WHITE),
    "vf_fountain":      (r"h(x)=a(x-2)^{2}+4", INK),
    "vf_fountain_sol":  (r"0=a(0-2)^{2}+4\ \Rightarrow\ a=-1", INK),
    "vf_fountain_final": (r"h(x)=-(x-2)^{2}+4", INK),
    "vf_fountain_eval":  (r"h(1)=-(1-2)^{2}+4=3", INK),

    # exam cards
    "vf_ex_gat":  (r"f(x)=4(x-1)^{2}+6", INK),
    "vf_ex_saat": (r"f(x)=-2(x+3)^{2}+9", INK),
    "vf_ex_sat":  (r"\text{vertex }(3,-4),\quad \text{point }(5,4)", INK),

    # ---- docs-only: classwork ----
    "vf_cw1": (r"f(x)=(x-5)^{2}+2", INK),
    "vf_cw2": (r"f(x)=-3(x+2)^{2}-1", INK),
    "vf_cw3": (r"f(x)=\tfrac{1}{4}x^{2}+6", INK),
    "vf_cw4": (r"f(x)=2(x-1)^{2}-4", INK),
    "vf_cw5": (r"\text{vertex }(1,2),\quad \text{point }(3,10)", INK),
    "vf_cw6": (r"\text{vertex }(-2,-5),\quad \text{point }(0,-1)", INK),
    "vf_cw_fountain": (r"h(x)=a(x-3)^{2}+5", INK),
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

tex = os.path.join(TMP, "w7.tex")
open(tex, "w").write("\n".join(doc))
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory", TMP, tex], capture_output=True, text=True)
if r.returncode:
    print(r.stdout[-4000:])
    raise SystemExit("pdflatex failed")

for out, dpi in (("math_w7", 500), ("math_w7_doc", 260)):
    shutil.rmtree(out, ignore_errors=True)
    os.makedirs(out)
    stem = os.path.join(TMP, f"p{dpi}")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(TMP, "w7.pdf"), stem], check=True)
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
