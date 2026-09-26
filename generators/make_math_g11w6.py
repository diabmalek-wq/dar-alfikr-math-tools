"""LaTeX expressions for the Grade 11 SAAT · SAT · GAT combined Week 6
worksheet — anchor: Topic 6, Lessons 6-3/6-4 (Logarithms and Logarithmic
Functions). Matches the exact house format captured from the real,
already-delivered SAAT_SAT_GAT_Gr11_W5_Paper.pdf.

Real LaTeX (pdflatex + Computer Modern), tight-cropped transparent PNG,
rendered once for the docx pipeline (260 dpi, matching exam_engine's other
math indexes).

    python3 make_math_g11w6.py
"""
import json, os, shutil, subprocess
from PIL import Image

TMP = ".tex_g11w6"
shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(TMP)

INK = "222E2D"

EXPR = {
    # ---- Section 1 · SAAT
    "g6_log1": r"\log_{2}32",
    "g6_log2": r"\log_{4}x=3",
    "g6_log3": r"\log_{2}40-\log_{2}5",
    "g6_log4": r"\log_{2}(x+2)=4",

    # ---- Section 3 · GAT
    "g6_log5":     r"\log_{2}x=3",
    "g6_cmp":      r"A=\log_{2}1000 \qquad B=\log_{4}1\,000\,000",
    "g6_logexpand": r"\log\left(x^{2}y\right)",
    "g6_opt_a": r"2\log x+\log y",
    "g6_opt_b": r"\log(2x)+\log y",
    "g6_opt_c": r"(\log x)^{2}\log y",
    "g6_opt_d": r"2\log x\cdot\log y",
}

keys = list(EXPR)
doc = [r"\documentclass[12pt]{article}", r"\usepackage[active,tightpage]{preview}",
       r"\usepackage{amsmath,amssymb}", r"\usepackage[T1]{fontenc}",
       r"\usepackage[dvipsnames]{xcolor}", r"\setlength\PreviewBorder{1.5pt}",
       r"\definecolor{ink}{HTML}{%s}" % INK, r"\begin{document}"]
for k in keys:
    doc.append(r"\begin{preview}$\color{ink}\displaystyle %s$\end{preview}" % EXPR[k])
doc.append(r"\end{document}")

tex = os.path.join(TMP, "g11w6.tex")
open(tex, "w").write("\n".join(doc))
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory", TMP, tex], capture_output=True, text=True)
if r.returncode:
    print(r.stdout[-4000:])
    raise SystemExit("pdflatex failed")

OUT, DPI = "math_g11w6", 260
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT)
stem = os.path.join(TMP, "p")
subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(DPI),
                os.path.join(TMP, "g11w6.pdf"), stem], check=True)
pages = sorted(f for f in os.listdir(TMP) if f.startswith("p-") and f.endswith(".png"))
assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} expressions"
idx = {}
for k, p in zip(keys, pages):
    im = Image.open(os.path.join(TMP, p)).convert("RGBA")
    dst = os.path.join(OUT, k + ".png")
    im.save(dst)
    idx[k] = {"file": dst, "win": im.width / DPI, "hin": im.height / DPI,
              "aspect": im.width / im.height}
json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
print(f"{len(idx)} expressions -> {OUT} @ {DPI} dpi")
