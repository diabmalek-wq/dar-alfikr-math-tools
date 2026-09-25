"""LaTeX-rendered stacked fractions for the two Week 4 study guides.
Same pipeline as make_math_g11w5.py: pdflatex, Computer Modern, transparent
PNG, 300 dpi. Every fraction that previously appeared as a flat "a/b" slash
is rendered here as a proper \\dfrac stacked fraction.
"""
import json, os, shutil, subprocess
from PIL import Image

OUT, TMP, DPI = "math_studyguides", ".tex_studyguides", 300
shutil.rmtree(OUT, ignore_errors=True); shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(OUT); os.makedirs(TMP)
INK = "222E2D"

E = {
    "half_n":       r"\dfrac{n}{2}",
    "half_10":      r"\dfrac{10}{2}",
    "half_20":      r"\dfrac{20}{2}",
    "frac_112_12":  r"\dfrac{112}{12}",
    "frac_1_fx":    r"\dfrac{1}{f(x)}",
    "frac_x5_3":    r"\dfrac{x+5}{3}",
    "frac_13p5_3":  r"\dfrac{13+5}{3}",
    "frac_18_3":    r"\dfrac{18}{3}",
    "frac_x9_4":    r"\dfrac{x+9}{4}",
    "frac_x2_5":    r"\dfrac{x-2}{5}",
    "frac_2_5":     r"\dfrac{2}{5}",
    "frac_5_2":     r"\dfrac{5}{2}",
}

keys = list(E)
doc = [r"\documentclass[12pt]{article}", r"\usepackage[active,tightpage]{preview}",
       r"\usepackage{amsmath,amssymb}", r"\usepackage[dvipsnames]{xcolor}",
       r"\setlength\PreviewBorder{1.5pt}",
       r"\definecolor{ink}{HTML}{%s}" % INK, r"\begin{document}"]
for k in keys:
    doc.append(r"\begin{preview}$\color{ink}\displaystyle %s$\end{preview}" % E[k])
doc.append(r"\end{document}")

tex = os.path.join(TMP, "sg.tex")
open(tex, "w").write("\n".join(doc))
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory", TMP, tex], capture_output=True, text=True)
if r.returncode:
    print(r.stdout[-3000:]); raise SystemExit("pdflatex failed")
subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(DPI),
                os.path.join(TMP, "sg.pdf"), os.path.join(TMP, "p")], check=True)

pages = sorted(f for f in os.listdir(TMP) if f.startswith("p-") and f.endswith(".png"))
assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} expressions"
idx = {}
for k, p in zip(keys, pages):
    im = Image.open(os.path.join(TMP, p)).convert("RGBA")
    dst = os.path.join(OUT, k + ".png"); im.save(dst)
    idx[k] = {"file": dst, "win": im.width / DPI, "hin": im.height / DPI,
              "aspect": im.width / im.height}
json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
print(len(idx), "expressions typeset")
