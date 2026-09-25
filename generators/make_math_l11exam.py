"""Math expressions for the AP Precalculus L1-1 (1.1 Change in Tandem) EXAM-STYLE deck
(the non-FIKR, 12-slide rebuild per the 18 Sep 2026 standing rule for AP Precalculus PPTs).
Real LaTeX (pdflatex + Computer Modern), tight-cropped, transparent PNG at 500 dpi.
Same pattern as make_math_l12ppt.py so lesson_l11_exam.js's eq() helper can consume it directly.
Numbers verified against build_ap_l11_guide.py / math_ap_l11.py / graphs_ap_l11.py — reused unchanged.
"""
import json, os, shutil, subprocess
from PIL import Image

OUT, TMP = "math_l11exam", ".tex_l11exam"
shutil.rmtree(OUT, ignore_errors=True); shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(OUT); os.makedirs(TMP)

INK, DEEP, WHITE = "222E2D", "0E4F4C", "FFFFFF"

EXPR = {
    "title_eq":     (r"y=f(x)", WHITE),
    "Vt_notation":  (r"V(t)", INK),
    "incr_def":     (r"\text{for all } a,b:\ \ a<b\ \Rightarrow\ f(a)<f(b)", INK),
    "decr_def":     (r"\text{for all } a,b:\ \ a<b\ \Rightarrow\ f(a)>f(b)", INK),
    "vang_linear":  (r"f(x)=2x+3", DEEP),
    "vang_table":   (r"\begin{array}{c|cccc}x&0&1&2&3\\\hline f(x)&3&5&7&9\end{array}", INK),
    "quad_g":       (r"g(x)=x^{2}-4x+3", INK),
    "drone_decr":   (r"\begin{aligned}g(0)&=3\\ g(1)&=0\\ g(2)&=-1\end{aligned}\quad\Rightarrow\ \text{decreasing on }(0,2)", INK),
    "drone_incr":   (r"\begin{aligned}g(2)&=-1\\ g(3)&=0\\ g(4)&=3\end{aligned}\quad\Rightarrow\ \text{increasing on }(2,4)", INK),
    "quad_zero_yint": (r"\text{zeros: } x=1,\ x=3 \qquad y\text{-intercept: }(0,\ 3)", INK),
    "Rt_notation":  (r"R(t)", INK),
    "reservoir_answer": (r"\text{increasing at a decreasing rate on }(4,\ 9)", DEEP),
    "Vt_fuel":      (r"V(t)", INK),
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

tex = os.path.join(TMP, "l11exam.tex")
open(tex, "w").write("\n".join(doc))
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory", TMP, tex], capture_output=True, text=True)
if r.returncode:
    print(r.stdout[-4000:]); raise SystemExit("pdflatex failed")
subprocess.run(["pdftocairo", "-png", "-transp", "-r", "500",
                os.path.join(TMP, "l11exam.pdf"), os.path.join(TMP, "p")], check=True)

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
