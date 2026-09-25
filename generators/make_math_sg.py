"""Expressions for the combined SAT + GAT worksheets (Grades 10 and 11).
Real LaTeX (pdflatex + Computer Modern), tight-cropped transparent PNG.
Same pipeline as make_math_gat.py — see spec §12 for the gotchas.
"""
import json, os, shutil, subprocess
from PIL import Image

OUT, TMP, DPI = "math_sg", ".tex_sg", 420
shutil.rmtree(OUT, ignore_errors=True); shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(OUT); os.makedirs(TMP)
INK = "222E2D"

E = {
    # ---------------- Grade 10, Week 2 — SAT half
    "a_lin1":   r"3(2x-5)=4x+7",
    "a_sys":    r"x+y=12\qquad\text{and}\qquad 2x-y=3",
    "a_quad":   r"f(x)=x^{2}-6x+5",
    "a_fact":   r"f(x)=(x-2)(x+5)",
    "a_o_25pi": r"25\pi",
    "a_o_10pi": r"10\pi",
    "a_o_50pi": r"50\pi",
    "a_o_100pi": r"100\pi",
    # ---------------- Grade 10, Week 2 — GAT half
    "a_pow":    r"3^{17}",
    "a_root":   r"\sqrt{0.25}",
    "a_div4":   r"\dfrac{x}{4}=4",
    "a_ident":  r"(a+b)^{2}=49\qquad\text{and}\qquad ab=10",
    # ---------------- Grade 10, Week 2 — added for the four-full-page rebuild
    "a_vertex":  r"f(x)=2(x-3)^{2}-8",
    "a_domrad":  r"f(x)=\sqrt{x-4}",
    "a_ineq":    r"-3x+7>19",
    "a_abs":     r"|2x-5|=9",
    "g_recipx":  r"x+\dfrac{1}{x}=5",
    "g_cmp230":  r"A:\ 2^{30}\qquad\qquad B:\ 3^{20}",
    "g_o_sh1":   r"100-25\pi",
    "g_o_sh2":   r"100-50\pi",
    "g_o_sh3":   r"100-10\pi",
    "g_o_sh4":   r"25\pi",
    "p_o_a":     r"\dfrac{3}{28}",
    "p_o_b":     r"\dfrac{9}{64}",
    "p_o_c":     r"\dfrac{1}{8}",
    "p_o_d":     r"\dfrac{3}{8}",
    "a_expo":    r"f(x)=3(2)^{x}",
    "g_quadr":   r"x^{2}-7x+10=0",
    # ---------------- Grade 10, Week 3 (transformations + piecewise)
    "b_trans":  r"g(x)=f(x-3)+2",
    "b_vertex2": r"y=-(x+2)^{2}+5",
    "b_absg":   r"y=|x-4|-3",
    "b_sys2":   r"2x+3y=12\qquad\text{and}\qquad x-y=1",
    "b_ineq2":  r"\dfrac{2x-1}{3}\leq 5",
    "b_exp":    r"y=200(1.05)^{t}",
    "b_pw":     r"f(x)=\begin{cases}2x+1,& x<2\\ x^{2}-3,& x\geq 2\end{cases}",
    "b_stretch": r"h(x)=3f(x)",
    "b_o_p1":   r"(f\circ g)(x)",
    # ---------------- Grade 11, Week 2 (radical functions and equations)
    "c_rad1":   r"\sqrt{2x+3}=7",
    "c_rad2":   r"\sqrt{x+7}=x-5",
    "c_dom":    r"y=\sqrt{3x-9}",
    "c_ratexp": r"27^{2/3}",
    "c_simp":   r"\sqrt{50}+\sqrt{18}",
    "c_expr":   r"\dfrac{x^{1/2}\cdot x^{3/2}}{x}",
    "c_cube":   r"\sqrt[3]{-64}",
    "c_shift":  r"y=\sqrt{x-4}+1",
    "c_o_r1":   r"5\sqrt{2}",
    "c_o_r2":   r"8\sqrt{2}",
    "c_o_r3":   r"4\sqrt{2}",
    "c_o_r4":   r"\sqrt{68}",
    # ---------------- Grade 11, Week 3 (operations and inverses)
    "d_fg":     r"f(x)=2x+1\qquad g(x)=x^{2}-3",
    "d_inv":    r"f(x)=\dfrac{3x-5}{2}",
    "d_o_i1":   r"f^{-1}(x)=\dfrac{2x+5}{3}",
    "d_o_i2":   r"f^{-1}(x)=\dfrac{2x-5}{3}",
    "d_o_i3":   r"f^{-1}(x)=\dfrac{3x+5}{2}",
    "d_o_i4":   r"f^{-1}(x)=\dfrac{2}{3x-5}",
    "d_quot":   r"\left(\dfrac{f}{g}\right)(x)",
    "d_sqrtc":  r"f(x)=\sqrt{x-1}\qquad g(x)=x^{2}+1",
    "c_rat":    r"\dfrac{6}{\sqrt{3}}",
    "c_x32":    r"x^{3/2}=27",
    "c_o_t1":   r"2\sqrt{3}",
    "c_o_t2":   r"3\sqrt{3}",
    "c_o_t3":   r"\sqrt{3}",
    "c_o_t4":   r"6\sqrt{3}",
    # ---------------- option sets: typeset so the choices match the stem
    "o_x":      r"x",
    "o_x2":     r"x^{2}",
    "o_sqx":    r"\sqrt{x}",
    "o_one":    r"1",
    "o_absx":   r"|x|",
    "o_xp1":    r"x+1",
    # domains and intervals
    "o_xge0":   r"x\geq 0",
    "o_xge3":   r"x\geq 3",
    "o_xle3":   r"x\leq 3",
    "o_xge4":   r"x\geq 4",
    "o_xle4":   r"x\leq 4",
    "o_xlt1":   r"x<1",
    "o_xgt1":   r"x>1",
    "o_xltm4":  r"x<-4",
    "o_xgtm4":  r"x>-4",
    "o_xlt4":   r"x<4",
    "o_xgt4":   r"x>4",
    "o_xle8":   r"x\leq 8",
    "o_xge8":   r"x\geq 8",
    "o_xle7":   r"x\leq 7",
    "o_xge7":   r"x\geq 7",
    "o_yge4":   r"y\geq -4",
    "o_yle4":   r"y\leq -4",
    "o_yge1":   r"y\geq 1",
    "o_ygtm4":  r"y>-4",
    "o_m1x3":   r"-1<x<3",
    # zeros
    "o_z1":     r"x=-2\ \text{and}\ x=5",
    "o_z2":     r"x=2\ \text{and}\ x=-5",
    "o_z3":     r"x=2\ \text{and}\ x=5",
    "o_z4":     r"x=-2\ \text{and}\ x=-5",
    # cost models
    "o_c1":     r"C=45m+0.30",
    "o_c2":     r"C=0.30m+45",
    "o_c3":     r"C=45.30m",
    "o_c4":     r"C=0.30(m+45)",
    # transformations
    "o_fnegx":  r"y=f(-x)",
    "o_negfx":  r"y=-f(x)",
    "o_absfx":  r"y=|f(x)|",
    "o_fxm1":   r"y=f(x)-1",
    "o_x43":    r"x=\tfrac{4}{3}",
    "o_x4":     r"x=4",
    "o_x12":    r"x=12",
    # vertices and points
    "o_vm25":   r"(-2,\,5)",
    "o_v25":    r"(2,\,5)",
    "o_vm2m5":  r"(-2,\,-5)",
    "o_v2m5":   r"(2,\,-5)",
    "o_p41":    r"(4,\,1)",
    "o_pm41":   r"(-4,\,1)",
    "o_p4m1":   r"(4,\,-1)",
    "o_p14":    r"(1,\,4)",
    "o_c3m2":   r"(3,\,-2)",
    "o_cm32":   r"(-3,\,2)",
    "o_c6m4":   r"(6,\,-4)",
    "o_cm64":   r"(-6,\,4)",
    # lines
    "o_l1":     r"y=3x-1",
    "o_l2":     r"y=3x+1",
    "o_l3":     r"y=4x-3",
    "o_l4":     r"y=12x-19",
    "o_m1":     r"y=4x+1",
    "o_m2":     r"y=4x-1",
    "o_m3":     r"y=3x+3",
    "o_m4":     r"y=12x-15",
    # literal rearrangement
    "o_h1":     r"h=2A-(a+b)",
    "o_h2":     r"h=\dfrac{2A}{a+b}",
    "o_h3":     r"h=\dfrac{A}{2(a+b)}",
    "o_h4":     r"h=\dfrac{a+b}{2A}",
    # linear expressions
    "o_5am1":   r"5a-1",
    "o_5ap3":   r"5a+3",
    "o_5ap5":   r"5a+5",
    "o_5am2":   r"5a-2",
    # fractions and symbolic options found by the audit
    "f_38":  r"\dfrac{3}{8}",   "f_12":  r"\dfrac{1}{2}",
    "f_58":  r"\dfrac{5}{8}",   "f_78":  r"\dfrac{7}{8}",
    "f_14":  r"\dfrac{1}{4}",   "f_34":  r"\dfrac{3}{4}",
    "f_16":  r"\dfrac{1}{6}",   "f_13":  r"\dfrac{1}{3}",
    "f_1136": r"\dfrac{11}{36}",
    "f_724": r"\dfrac{7}{24}",  "f_725": r"\dfrac{7}{25}",
    "f_2425": r"\dfrac{24}{25}","f_257": r"\dfrac{25}{7}",
    "f_815": r"\dfrac{8}{15}",  "f_817": r"\dfrac{8}{17}",
    "f_1517": r"\dfrac{15}{17}","f_178": r"\dfrac{17}{8}",
    "o_x0":   r"x=0",
    "o_xsq3": r"x=\sqrt{3}",
    "o_x3":   r"x=3",
    "o_pair1": r"f(x)=x+2\ \text{and}\ g(x)=x-2",
    "o_pair2": r"f(x)=2x\ \text{and}\ g(x)=x^{2}",
    "o_pair3": r"f(x)=x^{2}\ \text{and}\ g(x)=\sqrt{x}",
    "o_pair4": r"f(x)=3x\ \text{and}\ g(x)=x+3",
    "o_ci1":  r"5000\times 3\times 1.06",
    "o_ci2":  r"5000\times 1.18",
    "o_ci3":  r"5000\times 1.06^{3}",
    "o_ci4":  r"5000+3(0.06)",
    # stems that were left inline while their neighbours were typeset
    "s_absg10":  r"|3x-6|=9",
    "s_idg10":   r"a-b=3\qquad\text{and}\qquad ab=10",
    "s_rad11":   r"\sqrt{x+5}-x=3",
    "s_brk11":   r"3(x-4)=2(x+5)",
    "s_circ11":  r"x^{2}+y^{2}-6x+4y=12",
    "s_abs11":   r"|2x+3|=11",
    "s_inv11":   r"f(x)=4x-7",
    "s_lin11":   r"f(x)=5x-2",
    "s_frac11":  r"\dfrac{x+4}{5}=\dfrac{x-2}{3}",
    "s_prod11":  r"f(x)=x+3\qquad g(x)=2x",
    "s_abs11b":  r"|4x-8|=12",




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
