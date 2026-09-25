"""Math expressions for the AP Precalculus L1-1 (1.1 Change in Tandem) lesson deck.
Real LaTeX (pdflatex + Computer Modern), tight-cropped, transparent PNG at 500 dpi.
Same pattern as make_math_w2.py so lesson_engine.js's eq() can consume it directly.
"""
import json, os, shutil, subprocess
from PIL import Image

OUT, TMP = "math_l11ppt", ".tex_l11ppt"
shutil.rmtree(OUT, ignore_errors=True); shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(OUT); os.makedirs(TMP)

INK, DEEP, WHITE = "222E2D", "0E4F4C", "FFFFFF"

EXPR = {
    "title_ht":       (r"h(t)", WHITE),
    "prior_fx":       (r"f(x)", INK),
    "np_notation":    (r"N(p)", INK),
    "cd_notation":    (r"C(d)", INK),
    "vang_linear":    (r"f(x)=2x+3", DEEP),
    "vang_table":     (r"\begin{array}{c|cccc}x&0&1&2&3\\\hline f(x)&3&5&7&9\end{array}", INK),
    "quick_check_func": (r"k(x)=-2x+7", INK),
    "drone_g":        (r"g(x)=x^{2}-4x+3", INK),
    "reservoir_Rt":   (r"R(t)", INK),
    "fuel_Vt":        (r"V(t)", WHITE),
    "gate_func":      (r"m(x)=-x^{2}+4x+1", WHITE),
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

tex = os.path.join(TMP, "l11ppt.tex")
open(tex, "w").write("\n".join(doc))
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory", TMP, tex], capture_output=True, text=True)
if r.returncode:
    print(r.stdout[-4000:]); raise SystemExit("pdflatex failed")
subprocess.run(["pdftocairo", "-png", "-transp", "-r", "500",
                os.path.join(TMP, "l11ppt.pdf"), os.path.join(TMP, "p")], check=True)

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
