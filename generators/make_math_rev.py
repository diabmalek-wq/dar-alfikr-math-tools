"""
Ready for Algebra II — prerequisite revision worksheet.
Real LaTeX (pdflatex + Computer Modern), tight-cropped transparent PNG.
Index carries natural inch size for scale-based placement.
"""
import json, os, shutil, subprocess
from PIL import Image

OUT, TMP, DPI = "math_rev", ".tex_rev", 420
shutil.rmtree(OUT, ignore_errors=True); shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(OUT); os.makedirs(TMP)

INK, DEEP, MAROON = "222E2D", "0E4F4C", "8A1B17"

E = {
    # ---------- A · Number, exponents and roots ----------
    "a1": r"-3+(-8)-(-5)",
    "a2": r"(-2)^{4}-2^{4}",
    "a3": r"\dfrac{3}{4}-\dfrac{5}{6}",
    "a4": r"\dfrac{2}{5}\div\dfrac{8}{15}",
    "a5": r"12-3\left(5-2^{3}\right)",
    "a6": r"\dfrac{-24}{-6}+\left|{-7}\right|",
    "a7": r"x^{5}\cdot x^{3}",
    "a8": r"\dfrac{y^{9}}{y^{4}}",
    "a9": r"\left(2a^{3}\right)^{4}",
    "a10": r"\left(\dfrac{3m^{2}}{n}\right)^{3}",
    "a11": r"5x^{0}+3^{-2}",
    "a12": r"\dfrac{8p^{6}q^{2}}{2p^{2}q^{5}}",
    "a13": r"\sqrt{75}",
    "a14": r"\sqrt{48}+\sqrt{27}",
    "a15": r"\sqrt{8}\cdot\sqrt{6}",
    "a16": r"\dfrac{6}{\sqrt{3}}",

    # ---------- B · Expressions: expand and factor ----------
    "b1": r"3(2x-5)-4(x+1)",
    "b2": r"(x+7)(x-2)",
    "b3": r"(2x-3)^{2}",
    "b4": r"(3x+4)(3x-4)",
    "b5": r"-2x\left(x^{2}-4x+6\right)",
    "b6": r"12x^{3}y-18x^{2}y^{2}",
    "b7": r"x^{2}-9x+20",
    "b8": r"x^{2}-49",
    "b9": r"2x^{2}+7x+3",
    "b10": r"3x^{2}-12",
    "b11": r"x^{2}+10x+25",
    "b12": r"6x^{2}-x-15",

    # ---------- C · Equations and inequalities ----------
    "c1": r"5x-8=2x+13",
    "c2": r"4(x-3)=2(x+5)",
    "c3": r"\dfrac{x}{3}+\dfrac{x}{4}=7",
    "c4": r"\dfrac{2x-1}{5}=\dfrac{x+4}{3}",
    "c5": r"-3x+7>19",
    "c6": r"-2\leq 3x-5<10",
    "c7": r"|x-4|=9",
    "c8": r"A=\dfrac{1}{2}bh\ \ \text{for}\ h",
    "c9": r"S=2\pi r^{2}+2\pi rh\ \ \text{for}\ h",

    # ---------- D · Lines ----------
    "d1": r"A(-2,5),\ B(4,-7)",
    "d2": r"y=-\dfrac{2}{3}x+4",
    "d3": r"4x-5y=20",
    "d4": r"y-3=2(x+1)",
    "d5": r"m=\dfrac{y_{2}-y_{1}}{x_{2}-x_{1}}",
    "d6": r"m_{1}m_{2}=-1",
    "d7": r"P(3,-1),\ \ m=\tfrac{1}{2}",
    "d8": r"y=mx+b",
    "d9": r"y=3x-1\qquad\text{and}\qquad x+3y=12",

    # ---------- E · Systems ----------
    "e1": r"\begin{aligned}2x+y&=11\\ x-y&=1\end{aligned}",
    "e2": r"\begin{aligned}3x+2y&=16\\ 5x-2y&=8\end{aligned}",
    "e3": r"\begin{aligned}y&=2x-3\\ 4x-2y&=6\end{aligned}",

    # ---------- F · Quadratics ----------
    "f1": r"x^{2}-5x-14=0",
    "f2": r"2x^{2}+9x=-4",
    "f3": r"x^{2}=64",
    "f4": r"3x^{2}-7x+2=0",
    "f5": r"x=\dfrac{-b\pm\sqrt{b^{2}-4ac}}{2a}",
    "f6": r"b^{2}-4ac",
    "f7": r"y=x^{2}-6x+5",
    "f8": r"x^{2}+4x-1=0",

    # ---------- G · Functions ----------
    "g1": r"f(x)=3x^{2}-2x+1",
    "g2": r"f(-2)",
    "g3": r"f(x)=\sqrt{x-3}",
    "g4": r"g(x)=\dfrac{5}{x+2}",
    "g5": r"\{(1,4),(2,7),(3,4),(5,9)\}",
    "g6": r"f(x)=2x-5",
    "g7": r"f(a+1)",
    "g8": r"[-3,\infty)",

    # ---------- H · Saudi context ----------
    "h1": r"C(n)=45n+180",
    "h2": r"V(p)=1.15p",
    "h3": r"d(t)=110t",
    "h4": r"h(t)=-5t^{2}+20t",

    # ---------- displayed reference ----------
    "r1": r"a^{m}\cdot a^{n}=a^{m+n}\qquad \dfrac{a^{m}}{a^{n}}=a^{m-n}\qquad \left(a^{m}\right)^{n}=a^{mn}",
    "r2": r"a^{0}=1\qquad a^{-n}=\dfrac{1}{a^{n}}\qquad \sqrt{ab}=\sqrt{a}\,\sqrt{b}",
    "r3": r"(a\pm b)^{2}=a^{2}\pm 2ab+b^{2}\qquad a^{2}-b^{2}=(a-b)(a+b)",
}
COLOUR = {k: (MAROON if k.startswith("r") else INK) for k in E}
for k in ("f5", "d5", "d6", "d8"):
    COLOUR[k] = DEEP

keys = list(E)
doc = [r"\documentclass[12pt]{article}", r"\usepackage[active,tightpage]{preview}",
       r"\usepackage{amsmath,amssymb}", r"\usepackage[dvipsnames]{xcolor}",
       r"\setlength\PreviewBorder{1.5pt}"]
for k in keys:
    doc.append(r"\definecolor{c%s}{HTML}{%s}" % (k, COLOUR[k]))
doc.append(r"\begin{document}")
for k in keys:
    doc.append(r"\begin{preview}$\color{c%s}\displaystyle %s$\end{preview}" % (k, E[k]))
doc.append(r"\end{document}")

tex = os.path.join(TMP, "rev.tex")
open(tex, "w").write("\n".join(doc))
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory", TMP, tex], capture_output=True, text=True)
if r.returncode:
    print(r.stdout[-4000:]); raise SystemExit("pdflatex failed")
subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(DPI),
                os.path.join(TMP, "rev.pdf"), os.path.join(TMP, "p")], check=True)

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
