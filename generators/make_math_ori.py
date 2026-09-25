"""Signature expressions for the Week 1 orientation decks — real LaTeX, as §5 requires."""
import json, os, shutil, subprocess
from PIL import Image

OUT, TMP = "math_ori", ".tex_ori"
shutil.rmtree(OUT, ignore_errors=True); shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(OUT); os.makedirs(TMP)

WHITE, DEEP, INK = "FFFFFF", "0E4F4C", "222E2D"

EXPR = {
    "quad_w":   (r"x=\dfrac{-b\pm\sqrt{b^{2}-4ac}}{2a}", WHITE),
    "pyth_w":   (r"\sin^{2}\theta+\cos^{2}\theta=1", WHITE),
    "gat_w":    (r"\dfrac{a}{b}=\dfrac{c}{d}\ \Longrightarrow\ ad=bc", WHITE),
    "sat_w":    (r"y=mx+b", WHITE),
    "saat_w":   (r"\log_{b}(xy)=\log_{b}x+\log_{b}y", WHITE),
    "maw_w":    (r"1+2+3+\cdots+n=\dfrac{n(n+1)}{2}", WHITE),
    "quad_d":   (r"x=\dfrac{-b\pm\sqrt{b^{2}-4ac}}{2a}", DEEP),
    "pyth_d":   (r"\sin^{2}\theta+\cos^{2}\theta=1", DEEP),
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

tex = os.path.join(TMP, "o.tex")
open(tex, "w").write("\n".join(doc))
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory", TMP, tex], capture_output=True, text=True)
if r.returncode: print(r.stdout[-3000:]); raise SystemExit("pdflatex failed")
subprocess.run(["pdftocairo", "-png", "-transp", "-r", "500",
                os.path.join(TMP, "o.pdf"), os.path.join(TMP, "p")], check=True)

pages = sorted(f for f in os.listdir(TMP) if f.startswith("p-") and f.endswith(".png"))
idx = {}
for k, p in zip(keys, pages):
    im = Image.open(os.path.join(TMP, p)).convert("RGBA")
    dst = os.path.join(OUT, k + ".png"); im.save(dst)
    idx[k] = {"file": dst, "win": im.width / 500, "hin": im.height / 500,
              "aspect": im.width / im.height}
json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
print(len(idx), "orientation expressions typeset")
