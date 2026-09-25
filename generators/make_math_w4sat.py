"""Expressions for the Week 4 SAT/GAT (Grade 10) and SAAT/SAT (Grade 11) worksheets.
Real LaTeX (pdflatex + Computer Modern), tight-cropped transparent PNG.
Same pipeline as make_math_sg.py.
"""
import json, os, shutil, subprocess
from PIL import Image

OUT, TMP, DPI = "math_w4sat", ".tex_w4sat", 420
shutil.rmtree(OUT, ignore_errors=True); shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(OUT); os.makedirs(TMP)
INK = "222E2D"

E = {
    # ---------------- Grade 10, Week 4 — SAT (arithmetic sequences + spiral)
    "g10s_seq1":  r"a_{1}=7,\ \ d=4",
    "g10s_seq2":  r"a_{5}=23,\ \ a_{9}=39",
    "g10s_sys":   r"3x+2y=16\qquad\text{and}\qquad x-y=2",
    "g10s_pw":    r"f(x)=\begin{cases}2x+5,& x<1\\ x^{2}-4,& x\geq 1\end{cases}",
    "g10s_ineq":  r"-2x+5\leq 17",
    "g10s_vert":  r"f(x)=3(x-1)^{2}-4",
    "g10s_trans": r"g(x)=f(x+2)-3",
    "g10s_pts":   r"(2,\,3)\ \ \text{and}\ \ (10,\,9)",
    "g10s_o_n30": r"n=30",
    "g10s_o_n28": r"n=28",
    "g10s_o_n32": r"n=32",
    "g10s_o_n26": r"n=26",
    # ---------------- Grade 10, Week 4 — GAT
    "g10g_diff":  r"5,\ 12,\ 23,\ 38,\ 57,\ \ldots",
    "g10g_seq":   r"a_{1}=4,\ \ d=7",
    "g10g_ident": r"a+b=9\qquad\text{and}\qquad ab=14",
    "g10g_angles": r"3x,\quad (2x+10),\quad (4x-10)",
    "g10g_o_out1": r"144-36\pi",
    "g10g_o_out2": r"144-18\pi",
    "g10g_o_out3": r"36\pi",
    "g10g_o_out4": r"144-6\pi",
    # ---------------- Grade 11, Week 4 — SAAT (exp/log + radical/rational)
    "g11a_log1":  r"\log_{3}81",
    "g11a_exp1":  r"2^{\,x+1}=32",
    "g11a_log2":  r"\log_{5}20-\log_{5}4",
    "g11a_exp2":  r"3^{\,2x}=27",
    "g11a_rat1":  r"\dfrac{x^{2}-16}{x-4}",
    "g11a_rat2":  r"f(x)=\dfrac{x+3}{x^{2}-9}",
    "g11a_rad1":  r"\sqrt{3x+4}=x",
    "g11a_rz1":   r"\dfrac{10}{\sqrt{5}}",
    "g11a_exp3":  r"(x^{3})^{2}\cdot x^{-4}",
    "g11a_log3":  r"\log_{2}64",
    "g11a_ident": r"a-b=4\qquad\text{and}\qquad ab=12",
    "g11a_o_r1":  r"2\sqrt{5}",  "g11a_o_r2": r"\sqrt{5}",
    "g11a_o_r3":  r"5\sqrt{5}",  "g11a_o_r4": r"\dfrac{2}{\sqrt{5}}",
    "g11a_o_x4o": r"x=4\ \text{only}", "g11a_o_xm1o": r"x=-1\ \text{only}",
    "g11a_o_both": r"x=4\ \text{and}\ x=-1", "g11a_o_none": r"\text{no real solution}",
    # ---------------- Grade 11, Week 4 — SAT (inverse functions + spiral)
    "g11s_inv1":  r"f(x)=4x-9",
    "g11s_inv2":  r"f(x)=\dfrac{x-5}{3}",
    "g11s_restq": r"f(x)=x^{2}+6x+5,\quad x\geq -3",
    "g11s_pair":  r"f(x)=5x+2\qquad g(x)=\dfrac{x-2}{5}",
    "g11s_exch":  r"Y=3.75X",
    "g11s_temp":  r"C=\dfrac{5}{9}(F-32)",
    "g11s_trans": r"g(x)=-f(x-1)",
    "g11s_o_i1":  r"f^{-1}(x)=\dfrac{x+9}{4}",
    "g11s_o_i2":  r"f^{-1}(x)=\dfrac{x-9}{4}",
    "g11s_o_i3":  r"f^{-1}(x)=4x+9",
    "g11s_o_i4":  r"f^{-1}(x)=\dfrac{9-x}{4}",
    "g11s_o_r1":  r"f^{-1}(x)=-3+\sqrt{x+4}",
    "g11s_o_r2":  r"f^{-1}(x)=-3-\sqrt{x+4}",
    "g11s_o_r3":  r"f^{-1}(x)=3+\sqrt{x+4}",
    "g11s_o_r4":  r"f^{-1}(x)=\sqrt{x+4}-3",
    # ---------------- Grade 10, Week 4 — SAT (regenerated from the verified SAT bank)
    "g10n_a006sys":  r"2x+3y=12\qquad\text{and}\qquad x-y=1",
    "g10n_a015sys":  r"\begin{array}{l} y>3x-4\\[3pt] y\leq -2x+10\end{array}",
    "g10n_a004fn":   r"h(k)=c,\qquad h(k+5)=c+15",
    "g10n_am002pop": r"P(t)=5000\left(1.15\right)^{t}",
    "g10n_am011frac": r"\dfrac{x^{2}-9}{x-3}",
    "g10n_am001foun": r"h(t)=-4\left(t-3\right)^{2}+45",
    "g10n_am005exp":  r"f(x)=a\cdot 2^{x}",
    "g10n_gt004circ": r"x^{2}+y^{2}-6x+8y=0",
    "g10n_gt006theta": r"\theta=\dfrac{5\pi}{6}\ \text{radians}",
    "g10n_gt006o1":   r"\dfrac{75\pi}{2}",
    "g10n_gt006o4":   r"\dfrac{25\pi}{2}",
    # ---------------- Grade 11, Week 4 — SAT (regenerated from the verified SAT bank)
    "g11n_a010eq":   r"4x-2y=10",
    "g11n_a017eq":   r"a\left(x-3\right)+5=bx-2a+11",
    "g11n_am004dep": r"V(t)=120000\left(0.88\right)^{t}",
    "g11n_am006quad": r"h(x)=2x^{2}-12x+7",
    "g11n_am009eq":  r"x^{2}-2x-3",
    "g11n_am008rad": r"\sqrt{x+7}=x-5",
}

keys = list(E)
doc = [r"\documentclass[12pt]{article}", r"\usepackage[active,tightpage]{preview}",
       r"\usepackage{amsmath,amssymb}", r"\usepackage[dvipsnames]{xcolor}",
       r"\setlength\PreviewBorder{1.5pt}",
       r"\definecolor{ink}{HTML}{%s}" % INK, r"\begin{document}"]
for k in keys:
    doc.append(r"\begin{preview}$\color{ink}\displaystyle %s$\end{preview}" % E[k])
doc.append(r"\end{document}")

tex = os.path.join(TMP, "w4sat.tex")
open(tex, "w").write("\n".join(doc))
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory", TMP, tex], capture_output=True, text=True)
if r.returncode:
    print(r.stdout[-3000:]); raise SystemExit("pdflatex failed")
subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(DPI),
                os.path.join(TMP, "w4sat.pdf"), os.path.join(TMP, "p")], check=True)

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
