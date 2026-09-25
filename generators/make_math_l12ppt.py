"""Math expressions for the AP Precalculus L1-2 (1.2 Rates of Change) exam-style deck.
Real LaTeX (pdflatex + Computer Modern), tight-cropped, transparent PNG at 500 dpi.
Same pattern as make_math_l11ppt.py so a pptxgenjs eq() helper can consume it directly.
Numbers verified in graphs_ap_l12.py / build_ap_l12_guide.py — reused here unchanged.
"""
import json, os, shutil, subprocess
from PIL import Image

OUT, TMP = "math_l12ppt", ".tex_l12ppt"
shutil.rmtree(OUT, ignore_errors=True); shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(OUT); os.makedirs(TMP)

INK, DEEP, WHITE = "222E2D", "0E4F4C", "FFFFFF"

EXPR = {
    "title_eq":     (r"\dfrac{\Delta y}{\Delta x}", WHITE),
    "H_notation":   (r"H(t)", INK),
    "aroc_def":     (r"\dfrac{\Delta y}{\Delta x}=\dfrac{y_2-y_1}{x_2-x_1}", INK),
    "abc_answer":   (r"B<C<A", INK),
    "ex2_steps":    (r"\begin{aligned}\dfrac{y_2-y_1}{x_2-x_1}&=\dfrac{500-150}{9-2}\\[2pt]&=\dfrac{350}{7}=50\ \text{kg/hr}\end{aligned}", INK),
    "ex3_steps":    (r"\begin{aligned}\dfrac{V(18)-V(4)}{18-4}&=\dfrac{132-20}{14}\\[2pt]&=\dfrac{112}{14}=8\ \text{ML/hr}\end{aligned}", INK),
    "ex3_turn":     (r"\begin{aligned}[0,10]:&\ \ \dfrac{70-0}{10}=7\\[2pt]{[10,18]:}&\ \ \dfrac{132-70}{8}=7.75\end{aligned}", INK),
    "secant_steps": (r"\begin{aligned}\dfrac{H(9)-H(7)}{9-7}&=\dfrac{194.8-156.8}{2}\\[2pt]&\approx 19.0\ \text{m/min}\end{aligned}", WHITE),
    "secant_exact": (r"\text{exact rate at }t=8:\ \ 19.06\ \text{m/min}", "CFE8E6"),
    "solar_func":   (r"P(x)=0.4x^2", INK),
    "solar_steps":  (r"\begin{aligned}\dfrac{P(6.5)-P(5.5)}{6.5-5.5}&=\dfrac{16.9-12.1}{1}\\[2pt]&=4.8\ \text{MW/hr}\end{aligned}", INK),
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

tex = os.path.join(TMP, "l12ppt.tex")
open(tex, "w").write("\n".join(doc))
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory", TMP, tex], capture_output=True, text=True)
if r.returncode:
    print(r.stdout[-4000:]); raise SystemExit("pdflatex failed")
subprocess.run(["pdftocairo", "-png", "-transp", "-r", "500",
                os.path.join(TMP, "l12ppt.pdf"), os.path.join(TMP, "p")], check=True)

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
