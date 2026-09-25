"""Expressions for Mawhiba G9 Unit 1 Activity 3 (Number Pyramids)."""
import json, os, shutil, subprocess
from PIL import Image

OUT, TMP, DPI = "maw_math3", ".tex_maw3", 420
shutil.rmtree(OUT, ignore_errors=True); shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(OUT); os.makedirs(TMP)
INK = "222E2D"

E = {
    "m3_top1":   r"10n+3",
    "m3_top2":   r"417-2n",
    "m3_formula": r"t=a+3b+3c+d",
    "m3_formula2": r"t=a+3b+3c+d",
    "m3_formula_w": r"\color{white}t=a+3b+3c+d",
    "m3_rearr":  r"a=t-(3b+3c+d)\qquad b=\dfrac{t-a-3c-d}{3}\qquad c=\dfrac{t-a-3b-d}{3}\qquad d=t-(a+3b+3c)",
    "m3_t1eq":   r"(40+2n)+(n+65)=267\ \Rightarrow\ 3n+105=267\ \Rightarrow\ n=54",
    "m3_t2i":    r"(73+3n)=157\ \Rightarrow\ n=28",
    "m3_t2ii":   r"(145+3n)=217\ \Rightarrow\ n=24",
    "m3_t2iii":  r"(81+n)=119\ \Rightarrow\ n=38",
    "m3_t4i":    r"(59+3n)=10n+3\ \Rightarrow\ 7n=56\ \Rightarrow\ n=8",
    "m3_t4ii":   r"(207+3n)=417-2n\ \Rightarrow\ 5n=210\ \Rightarrow\ n=42",
}

keys = list(E)
doc = [r"\documentclass[12pt]{article}", r"\usepackage[active,tightpage]{preview}",
       r"\usepackage{amsmath,amssymb}", r"\usepackage[dvipsnames]{xcolor}",
       r"\setlength\PreviewBorder{1.5pt}",
       r"\definecolor{ink}{HTML}{%s}" % INK, r"\begin{document}"]
for k in keys:
    doc.append(r"\begin{preview}$\color{ink}\displaystyle %s$\end{preview}" % E[k])
doc.append(r"\end{document}")

tex = os.path.join(TMP, "maw3.tex")
open(tex, "w").write("\n".join(doc))
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory", TMP, tex], capture_output=True, text=True)
if r.returncode:
    print(r.stdout[-3000:]); raise SystemExit("pdflatex failed")
subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(DPI),
                os.path.join(TMP, "maw3.pdf"), os.path.join(TMP, "p")], check=True)

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
