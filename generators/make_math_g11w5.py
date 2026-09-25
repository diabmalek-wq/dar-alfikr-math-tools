"""LaTeX for the Grade 11 SAAT + SAT + GAT Week 5 worksheet.

Anchor: Algebra II Topic 6, Lessons 6-1 and 6-3 -- Key Features of
Exponential Functions and Logarithms, which the class has now reached.
Same pipeline as make_math_s4.py: pdflatex, Computer Modern, transparent
PNG, 300 dpi for Word.
"""
import json, os, shutil, subprocess
from PIL import Image

OUT, TMP, DPI = "math_g11w5", ".tex_g11w5", 300
shutil.rmtree(OUT, ignore_errors=True); shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(OUT); os.makedirs(TMP)
INK = "222E2D"

E = {
    # ---------------- SAAT section (curriculum language, direct)
    "g11w5_log1":  r"\log_{4}64",
    "g11w5_exp1":  r"3^{\,x-1}=81",
    "g11w5_log2":  r"\log_{2}40-\log_{2}5",
    "g11w5_logx":  r"\log_{x}49=2",
    # ---------------- GAT section (trap-heavy, no calculator)
    "g11w5_2x32":   r"2^{x}=32",
    "g11w5_logcmp": r"\text{A: }\ \log_{2}32\qquad\qquad\text{B: }\ \log_{3}81",
    "g11w5_pow46":  r"4^{6}\div 4^{2}",
    "g11w5_o_43":   r"4^{3}",
    "g11w5_o_44":   r"4^{4}",
    "g11w5_o_48":   r"4^{8}",
    "g11w5_o_412":  r"4^{12}",
}

keys = list(E)
doc = [r"\documentclass[12pt]{article}", r"\usepackage[active,tightpage]{preview}",
       r"\usepackage{amsmath,amssymb}", r"\usepackage[dvipsnames]{xcolor}",
       r"\setlength\PreviewBorder{1.5pt}",
       r"\definecolor{ink}{HTML}{%s}" % INK, r"\begin{document}"]
for k in keys:
    doc.append(r"\begin{preview}$\color{ink}\displaystyle %s$\end{preview}" % E[k])
doc.append(r"\end{document}")

tex = os.path.join(TMP, "g11w5.tex")
open(tex, "w").write("\n".join(doc))
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory", TMP, tex], capture_output=True, text=True)
if r.returncode:
    print(r.stdout[-3000:]); raise SystemExit("pdflatex failed")
subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(DPI),
                os.path.join(TMP, "g11w5.pdf"), os.path.join(TMP, "p")], check=True)

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
