"""
Week 3. Real LaTeX (pdflatex + Computer Modern), tight-cropped transparent PNG
at 500 dpi. Index carries natural inch size for scale-based placement.

  A · Gr10 1-3  Piecewise-Defined Functions
  B · Gr11 5-5  Operations on Functions
"""
import json, os, shutil, subprocess
from PIL import Image

OUT, TMP = "math_w3", ".tex_w3"
shutil.rmtree(OUT, ignore_errors=True); shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(OUT); os.makedirs(TMP)

INK, DEEP, WHITE, MAROON = "222E2D", "0E4F4C", "FFFFFF", "8A1B17"

CASES = lambda body: r"f(x)=\begin{cases}" + body + r"\end{cases}"

EXPR = {
    # ================= A · Gr10 1-3 Piecewise-Defined Functions =================
    "p_general_w": (CASES(r"\text{rule 1},& x<a\\ \text{rule 2},& x\geq a"), WHITE),
    "p_general":   (CASES(r"\text{rule 1},& x<a\\ \text{rule 2},& x\geq a"), DEEP),
    "p_abs":       (r"f(x)=|x|", DEEP),
    "p_abs_w":     (r"f(x)=|x|", WHITE),
    "p_abs_pw":    (r"|x|=\begin{cases}x,& x\geq 0\\ -x,& x<0\end{cases}", INK),
    "p_floor":     (r"f(x)=\lfloor x\rfloor", DEEP),
    "p_ceil":      (r"f(x)=\lceil x\rceil", DEEP),
    "p_floor_ex":  (r"\lfloor 3.7\rfloor=3\qquad \lfloor -1.2\rfloor=-2", INK),
    "p_ceil_ex":   (r"\lceil 3.2\rceil=4\qquad \lceil -1.8\rceil=-1", INK),
    "p_sub":       (r"x<2\ \ \text{and}\ \ x\geq 2", INK),
    "p_disjoint":  (r"(-\infty,2)\cap[2,\infty)=\varnothing", INK),
    "p_dom":       (r"(-\infty,\infty)", INK),
    "p_ex":        (CASES(r"2x+1,& x<1\\ 5-x,& x\geq 1"), DEEP),
    "p_ex_w":      (CASES(r"2x+1,& x<1\\ 5-x,& x\geq 1"), WHITE),
    "p_ex_a":      (r"f(-2)=2(-2)+1=-3", INK),
    "p_ex_b":      (r"f(1)=5-1=4", INK),
    "p_ex_c":      (r"f(4)=5-4=1", INK),
    # diagnostic
    "p_d1":        (CASES(r"x+4,& x<0\\ 4-x,& x\geq 0"), INK),
    "p_d2":        (r"f(3)\ \ \text{for}\ \ f(x)=|x-5|", INK),
    "p_d3":        (r"\lfloor 7.9\rfloor", INK),
    "p_d4":        (r"\lceil 2.1\rceil", INK),
    "p_d5":        (r"x\geq -3", INK),
    # quick check + guided + gate
    "p_qc":        (CASES(r"-2x,& x\leq -1\\ x^{2},& x>-1"), INK),
    "p_g1":        (CASES(r"3x-2,& x<2\\ 4,& x\geq 2"), INK),
    "p_g2":        (r"f(x)=|x+3|-2", INK),
    "p_gate":      (CASES(r"\ \ ?\ \ ,& x<1\\ \ \ ?\ \ ,& x\geq 1"), INK),
    # worksheet
    "p_ws1":       (CASES(r"x+5,& x<-1\\ 2,& x\geq -1"), INK),
    "p_ws2":       (CASES(r"-x,& x\leq 0\\ 3x,& x>0"), INK),
    "p_ws3":       (r"f(x)=|x-2|+1", INK),
    "p_ws4":       (r"f(x)=-|x|+4", INK),
    "p_ws5":       (r"f(x)=\lfloor x\rfloor+2", INK),
    "p_ws6":       (r"f(x)=\lceil 2x\rceil", INK),
    "p_ws7":       (CASES(r"\tfrac{1}{2}x+3,& x<-2\\ x^{2}-1,& -2\leq x\leq 2\\ 5,& x>2"), INK),
    "p_ws8":       (r"f(-3),\ f(0),\ f(2),\ f(5)", INK),
    # Saudi contexts
    "ctx_tariff_w": (r"C(x)=\begin{cases}0.18x,& 0\leq x\leq 6000\\ 1080+0.30(x-6000),& x>6000\end{cases}", WHITE),
    "ctx_tariff":   (r"C(x)=\begin{cases}0.18x,& 0\leq x\leq 6000\\ 1080+0.30(x-6000),& x>6000\end{cases}", INK),
    "ctx_park":     (r"P(t)=3\lceil t\rceil", INK),
    "ctx_park_w":   (r"P(t)=3\lceil t\rceil", WHITE),

    # ================= B · Gr11 5-5 Operations on Functions =================
    "o_four_w":    (r"(f+g)(x)\quad (f-g)(x)\quad (fg)(x)\quad \left(\dfrac{f}{g}\right)(x)", WHITE),
    "o_sum":       (r"(f+g)(x)=f(x)+g(x)", DEEP),
    "o_diff":      (r"(f-g)(x)=f(x)-g(x)", DEEP),
    "o_prod":      (r"(fg)(x)=f(x)\cdot g(x)", DEEP),
    "o_quot":      (r"\left(\dfrac{f}{g}\right)(x)=\dfrac{f(x)}{g(x)},\quad g(x)\neq 0", DEEP),
    "o_comp":      (r"(f\circ g)(x)=f\bigl(g(x)\bigr)", DEEP),
    "o_comp_w":    (r"(f\circ g)(x)=f\bigl(g(x)\bigr)", WHITE),
    "o_comp2":     (r"(g\circ f)(x)=g\bigl(f(x)\bigr)", DEEP),
    "o_noncomm":   (r"(f\circ g)(x)\neq (g\circ f)(x)", MAROON),
    "o_dom":       (r"D_{f+g}=D_f\cap D_g", INK),
    "o_dom_comp":  (r"x\in D_g\ \ \text{and}\ \ g(x)\in D_f", INK),
    # base pair used all lesson
    "o_fg_w":      (r"f(x)=x^{2}-4,\qquad g(x)=x+3", WHITE),
    "o_fg":        (r"f(x)=x^{2}-4,\qquad g(x)=x+3", DEEP),
    "o_ex_sum":    (r"(f+g)(x)=x^{2}+x-1", INK),
    "o_ex_diff":   (r"(f-g)(x)=x^{2}-x-7", INK),
    "o_ex_prod":   (r"(fg)(x)=x^{3}+3x^{2}-4x-12", INK),
    "o_ex_quot":   (r"\left(\dfrac{f}{g}\right)(x)=\dfrac{x^{2}-4}{x+3},\quad x\neq -3", INK),
    "o_ex_comp1":  (r"(f\circ g)(x)=(x+3)^{2}-4=x^{2}+6x+5", INK),
    "o_ex_comp2":  (r"(g\circ f)(x)=x^{2}-4+3=x^{2}-1", INK),
    # short cards for the prior-knowledge slide
    "o_pk1":       (r"f\bigl(g(2)\bigr)", DEEP),
    "o_pk2":       (r"(x+3)^{2}", DEEP),
    "o_pk3":       (r"g(x)\neq 0", DEEP),
    # diagnostic
    "o_d1":        (r"f(x)=2x,\ g(x)=x-5:\ \ (f+g)(x)=?", INK),
    "o_d2":        (r"f(2)=7,\ g(2)=-3:\ \ (fg)(2)=?", INK),
    "o_d3":        (r"g(x)=x+1,\ f(x)=x^{2}:\ \ f\bigl(g(2)\bigr)=?", INK),
    "o_d4":        (r"\left(\dfrac{f}{g}\right)(x)\ \ \text{is undefined when}\ \ \_\_\_", INK),
    "o_d5":        (r"(f\circ g)(x)\ \ \text{means}\ \ \_\_\_", INK),
    # quick check, guided, gate
    "o_qc":        (r"f(x)=3x-1,\ \ g(x)=x^{2}", INK),
    "o_g1":        (r"f(x)=x+6,\ \ g(x)=2x-1", INK),
    "o_g2":        (r"f(x)=\sqrt{x},\ \ g(x)=x-9", INK),
    "o_gate":      (r"f(x)=x^{2}+1,\qquad g(x)=3x-2", INK),
    "o_gate_w":    (r"f(x)=x^{2}+1,\qquad g(x)=3x-2", WHITE),
    # worksheet
    "o_ws1":       (r"f(x)=4x+1,\ \ g(x)=x-7", INK),
    "o_ws2":       (r"f(x)=x^{2}-9,\ \ g(x)=x+3", INK),
    "o_ws3":       (r"f(x)=\dfrac{1}{x},\ \ g(x)=x-2", INK),
    "o_ws4":       (r"f(x)=\sqrt{x+4},\ \ g(x)=x^{2}", INK),
    "o_ws5":       (r"(f\circ g)(3)\ \ \text{and}\ \ (g\circ f)(3)", INK),
    "o_ws6":       (r"h(x)=(2x+5)^{3}", INK),
    "o_ws7":       (r"h(x)=\sqrt{x^{2}+1}", INK),
    "o_ws8":       (r"f\bigl(g(x)\bigr)=x\ \ \text{for all }x", INK),
    # Saudi contexts — discount then VAT
    "ctx_disc_w":  (r"D(p)=0.80p,\qquad V(p)=1.15p", WHITE),
    "ctx_disc":    (r"D(p)=0.80p,\qquad V(p)=1.15p", INK),
    "ctx_vd":      (r"(V\circ D)(p)=1.15(0.80p)=0.92p", INK),
    "ctx_dv":      (r"(D\circ V)(p)=0.80(1.15p)=0.92p", INK),
    "ctx_solar_w": (r"E(t)=4.5A\,t,\qquad R(E)=0.18E", WHITE),
    "ctx_solar":   (r"E(t)=4.5A\,t,\qquad R(E)=0.18E", INK),
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

tex = os.path.join(TMP, "w3.tex")
open(tex, "w").write("\n".join(doc))
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory", TMP, tex], capture_output=True, text=True)
if r.returncode:
    print(r.stdout[-4000:]); raise SystemExit("pdflatex failed")
subprocess.run(["pdftocairo", "-png", "-transp", "-r", "500",
                os.path.join(TMP, "w3.pdf"), os.path.join(TMP, "p")], check=True)

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
