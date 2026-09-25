"""Expressions for the Grade 10 and Grade 11 Algebra II diagnostic tests.
Same LaTeX pipeline as the other sheets — see spec §12.
"""
import json, os, shutil, subprocess
from PIL import Image

OUT, TMP, DPI = "math_diag", ".tex_diag", 420
shutil.rmtree(OUT, ignore_errors=True); shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(OUT); os.makedirs(TMP)
INK = "222E2D"

E = {
 # ================= GRADE 10 =================
 "a1":  r"(3x^{2}y)(4xy^{3})",
 "a1o": r"12x^{3}y^{4}",  "a1p": r"12x^{2}y^{3}",
 "a1q": r"7x^{3}y^{4}",   "a1r": r"12x^{3}y^{3}",
 "a2":  r"\left(2x^{3}\right)^{4}",
 "a2o": r"16x^{12}",  "a2p": r"8x^{12}",  "a2q": r"16x^{7}",  "a2r": r"2x^{12}",
 "a3":  r"\dfrac{x^{7}}{x^{3}}",
 "a3o": r"x^{4}",  "a3p": r"x^{10}",  "a3q": r"x^{21}",  "a3r": r"x^{3}",
 "a4":  r"3(x-2)^{2}\quad\text{when}\quad x=5",
 "a5":  r"5(2x-3)+4x",
 "a5o": r"14x-15",  "a5p": r"14x-3",  "a5q": r"6x-15",  "a5r": r"10x-15",
 "a6":  r"4x-7=2x+9",
 "a7":  r"3(x+2)=2x+11",
 "a8":  r"-2x+5>13",
 "a8o": r"x<-4",  "a8p": r"x>-4",  "a8q": r"x<4",  "a8r": r"x>4",
 "a9":  r"A=\tfrac{1}{2}bh",
 "a9o": r"h=\dfrac{2A}{b}",  "a9p": r"h=\dfrac{A}{2b}",
 "a9q": r"h=2A-b",           "a9r": r"h=\dfrac{b}{2A}",
 "a10o": r"C=0.25m+40",  "a10p": r"C=40m+0.25",
 "a10q": r"C=40.25m",    "a10r": r"C=0.25(m+40)",
 "a12": r"2x+3y=12",
 "a14": r"x+y=10\qquad\text{and}\qquad x-y=4",
 "a15": r"y=-3x+5",
 "a16": r"x^{2}-9",
 "a16o": r"(x-3)(x+3)",  "a16p": r"(x-3)^{2}",
 "a16q": r"(x+3)^{2}",   "a16r": r"(x-9)(x+1)",
 "a17": r"x^{2}+5x+6",
 "a17o": r"(x+2)(x+3)",  "a17p": r"(x-2)(x-3)",
 "a17q": r"(x+1)(x+6)",  "a17r": r"(x+5)(x+1)",
 "a18": r"(x-4)(x+1)=0",
 "a19": r"x^{2}=49",
 "a20": r"y=(x-2)^{2}-5",
 "a21": r"\sqrt{72}",
 "a21o": r"6\sqrt{2}",  "a21p": r"3\sqrt{8}",  "a21q": r"2\sqrt{18}",  "a21r": r"36\sqrt{2}",
 "a25o": r"36\pi",  "a25p": r"12\pi",  "a25q": r"18\pi",  "a25r": r"144\pi",
 # ================= GRADE 11 =================
 "b1":  r"f(x)=x^{2}-4x+3",
 "b2":  r"g(x)=f(x-3)+2",
 "b3":  r"f(x)=\sqrt{x-5}",
 "b3o": r"x\geq 5",  "b3p": r"x\geq 0",  "b3q": r"x\leq 5",  "b3r": r"x\geq -5",
 "b4":  r"y=-(x+1)^{2}+4",
 "b5":  r"f(x)=2x+1\qquad g(x)=x^{2}",
 "b6":  r"x^{2}-6x+13=0",
 "b7":  r"x^{2}+4=0",
 "b7o": r"x=\pm 2i",  "b7p": r"x=\pm 2",  "b7q": r"x=\pm 4i",  "b7r": r"x=\pm i\sqrt{2}",
 "b8":  r"(3+2i)+(1-5i)",
 "b8o": r"4-3i",  "b8p": r"4+7i",  "b8q": r"2-3i",  "b8r": r"4-7i",
 "b9":  r"x^{2}-7x+10=0",
 "b10": r"x^{2}-6x+5=0",
 "b11": r"4x^{3}-2x^{5}+7",
 "b12": r"\dfrac{x^{3}-1}{x-1}",
 "b12o": r"x^{2}+x+1",  "b12p": r"x^{2}-x+1",
 "b12q": r"x^{2}+1",    "b12r": r"x^{2}-1",
 "b13": r"x^{3}-2x+1\ \div\ (x-2)",
 "b14": r"x^{2}-x-6",
 "b15": r"f(x)=x(x-2)(x+5)",
 "b16": r"27^{2/3}",
 "b17": r"\sqrt{50}+\sqrt{18}",
 "b17o": r"8\sqrt{2}",  "b17p": r"5\sqrt{2}",  "b17q": r"\sqrt{68}",  "b17r": r"4\sqrt{2}",
 "b18": r"x^{1/2}\cdot x^{3/2}",
 "b18o": r"x^{2}",  "b18p": r"x^{3/4}",  "b18q": r"x^{4}",  "b18r": r"x",
 "b19": r"\sqrt{2x+3}=7",
 "b20": r"\left(x^{4}\right)^{3/2}",
 "b20o": r"x^{6}",  "b20p": r"x^{8}",  "b20q": r"x^{5.5}",  "b20r": r"x^{12}",
 "b21": r"2x+3y=12\qquad\text{and}\qquad x-y=1",
 "la10": r"h(t)=-(t-3)^{2}+9",
 "la11": r"R(x)=-2x^{2}+40x-50",
 "sa11": r"f(x)=2x+1,\qquad g(x)=x^{2}",
}

keys = list(E)
doc = [r"\documentclass[12pt]{article}", r"\usepackage[active,tightpage]{preview}",
       r"\usepackage{amsmath,amssymb}", r"\usepackage[dvipsnames]{xcolor}",
       r"\setlength\PreviewBorder{1.5pt}",
       r"\definecolor{ink}{HTML}{%s}" % INK, r"\begin{document}"]
for k in keys:
    doc.append(r"\begin{preview}$\color{ink}\displaystyle %s$\end{preview}" % E[k])
doc.append(r"\end{document}")

tex = os.path.join(TMP, "diag.tex")
open(tex, "w").write("\n".join(doc))
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory", TMP, tex], capture_output=True, text=True)
if r.returncode:
    print(r.stdout[-3000:]); raise SystemExit("pdflatex failed")
subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(DPI),
                os.path.join(TMP, "diag.pdf"), os.path.join(TMP, "p")], check=True)

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
