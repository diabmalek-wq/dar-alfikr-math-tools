"""Expressions for Mawhiba G9 Unit 1 Activity 4 (Grid of Squares).

Only the GIVEN notation and the two comparison formulas for Task 3 are
typeset here — every derived answer (9n+4, 2mn+m+n, n=14, ...) is left for
the student to write in the blank working space, the same rule Activities 1
and 3 followed.
"""
import json, os, shutil, subprocess
from PIL import Image

OUT, TMP, DPI = "maw_math4", ".tex_maw4", 420
shutil.rmtree(OUT, ignore_errors=True); shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(OUT); os.makedirs(TMP)
INK = "222E2D"

E = {
    "maw4_44":  r"4\times 4",
    "maw4_4n":  r"4\times n",
    "maw4_mn":  r"m\times n",
    "maw4_f1":  r"5n+4(n+1)",
    "maw4_f2":  r"(2n+8)+(7n-4)",
}

keys = list(E)
doc = [r"\documentclass[12pt]{article}", r"\usepackage[active,tightpage]{preview}",
       r"\usepackage{amsmath,amssymb}", r"\usepackage[dvipsnames]{xcolor}",
       r"\setlength\PreviewBorder{1.5pt}",
       r"\definecolor{ink}{HTML}{%s}" % INK, r"\begin{document}"]
for k in keys:
    doc.append(r"\begin{preview}$\color{ink}\displaystyle %s$\end{preview}" % E[k])
doc.append(r"\end{document}")

tex = os.path.join(TMP, "maw4.tex")
open(tex, "w").write("\n".join(doc))
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory", TMP, tex], capture_output=True, text=True)
if r.returncode:
    print(r.stdout[-3000:]); raise SystemExit("pdflatex failed")
subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(DPI),
                os.path.join(TMP, "maw4.pdf"), os.path.join(TMP, "p")], check=True)

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
