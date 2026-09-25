"""
Week 4. Real LaTeX (pdflatex + Computer Modern), tight-cropped transparent PNG.
Rendered twice: 500 dpi for the slides, 260 dpi for the documents. The index
records NATURAL INCH SIZE, so both indexes carry identical numbers and a
config can point at either.

  A · Gr10 1-4  Arithmetic Sequences and Series
  B · Gr11 5-6  Inverse Relations and Functions
"""
import json, os, shutil, subprocess
from PIL import Image

TMP = ".tex_w4"
shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(TMP)

INK, DEEP, WHITE, MAROON = "222E2D", "0E4F4C", "FFFFFF", "8A1B17"
FR = lambda a, b: r"\dfrac{%s}{%s}" % (a, b)

EXPR = {
    # ============ A · Gr10 1-4  Arithmetic Sequences and Series ============
    "a_seq_w":   (r"5,\ 9,\ 13,\ 17,\ 21,\ \ldots", WHITE),
    "a_seq":     (r"5,\ 9,\ 13,\ 17,\ 21,\ \ldots", DEEP),
    "a_d":       (r"d=a_{n}-a_{n-1}", INK),
    "a_d_w":     (r"d=a_{n}-a_{n-1}", WHITE),
    "a_rec":     (r"a_{1}=5,\qquad a_{n}=a_{n-1}+4\ \ \text{for}\ n\geq 2", INK),
    "a_exp":     (r"a_{n}=a_{1}+(n-1)d", INK),
    "a_exp_w":   (r"a_{n}=a_{1}+(n-1)d", WHITE),
    "a_exp_ex":  (r"a_{n}=5+(n-1)4=4n+1", INK),
    "a_lin":     (r"a_{n}=dn+\left(a_{1}-d\right)", INK),
    "a_sum":     (r"S_{n}=" + FR("n", "2") + r"\left(a_{1}+a_{n}\right)", INK),
    "a_sum_w":   (r"S_{n}=" + FR("n", "2") + r"\left(a_{1}+a_{n}\right)", WHITE),
    "a_sum2":    (r"S_{n}=" + FR("n", "2") + r"\left[\,2a_{1}+(n-1)d\,\right]", INK),
    "a_sigma":   (r"S_{n}=\sum_{k=1}^{n}a_{k}", INK),
    "a_sigma_ex": (r"\sum_{k=1}^{12}\left(3k+2\right)", INK),
    "a_count":   (r"n=" + FR(r"a_{n}-a_{1}", "d") + r"+1", INK),

    # diagnose
    "a_d1":      (r"7,\ 12,\ 17,\ 22,\ \ldots\qquad d=\underline{\qquad}", INK),
    "a_d2":      (r"a_{1}=3,\ d=5.\qquad a_{4}=\underline{\qquad}", INK),
    "a_d3":      (r"2,\ 6,\ 18,\ 54,\ \ldots\ \ \text{arithmetic?}", INK),
    "a_d4":      (r"a_{n}=6n-1.\qquad a_{1}=\underline{\qquad}", INK),
    "a_d5":      (r"\sum_{k=1}^{4}k^{2}=\underline{\qquad}", INK),

    # quick check, guided, gate
    "a_qc":      (r"a_{1}={-8},\qquad d=3", INK),
    "a_g1":      (r"11,\ 4,\ {-3},\ {-10},\ \ldots", INK),
    "a_g2":      (r"a_{1}=2,\ a_{20}=97", INK),
    "a_gate":    (r"6,\ 11,\ 16,\ \ldots,\ 201", INK),
    "a_gate_w":  (r"6,\ 11,\ 16,\ \ldots,\ 201", WHITE),

    # worksheet and routes
    "a_ws1":     (r"4,\ 11,\ 18,\ 25,\ \ldots", INK),
    "a_ws2":     (r"30,\ 24,\ 18,\ 12,\ \ldots", INK),
    "a_ws3":     (r"a_{1}=7,\qquad a_{n}=a_{n-1}+9", INK),
    "a_ws4":     (r"a_{n}=5n-3", INK),
    "a_ws5":     (r"\sum_{k=1}^{15}\left(2k+7\right)", INK),
    "a_ws6":     (r"9,\ 14,\ 19,\ \ldots,\ 124", INK),
    "a_ws7":     (r"a_{3}=17,\qquad a_{8}=42", INK),
    "a_ws8":     (r"S_{n}=" + FR("n", "2") + r"\left(a_{1}+a_{n}\right)"
                  r"\quad\text{and}\quad S_{n}=" + FR("n", "2")
                  + r"\left[\,2a_{1}+(n-1)d\,\right]", INK),

    # Saudi context — a Vision 2030 savings plan
    "ctx_save_w": (r"a_{1}=400,\qquad d=150\ \ \text{SAR per month}", WHITE),
    "ctx_save":   (r"a_{1}=400,\qquad d=150\ \ \text{SAR per month}", INK),
    "ctx_save2":  (r"S_{12}=" + FR("12", "2") + r"\left(400+2050\right)=14\,700\ \text{SAR}", INK),

    # ============ B · Gr11 5-6  Inverse Relations and Functions ============
    "v_inv_w":   (r"f^{-1}(x)", WHITE),
    "v_inv":     (r"f^{-1}(x)", DEEP),
    "v_def":     (r"f\!\left(f^{-1}(x)\right)=x\qquad\text{and}\qquad "
                  r"f^{-1}\!\left(f(x)\right)=x", INK),
    "v_def_w":   (r"f\!\left(f^{-1}(x)\right)=x\qquad\text{and}\qquad "
                  r"f^{-1}\!\left(f(x)\right)=x", WHITE),
    "v_swap":    (r"y=3x-8\ \Longrightarrow\ x=3y-8\ \Longrightarrow\ y="
                  + FR("x+8", "3"), INK),
    "v_notrecip": (r"f^{-1}(x)\neq" + FR("1", "f(x)"), MAROON),
    "v_solve":   (r"f(x)=c", INK),
    "v_restrict": (r"f(x)=x^{2},\ x\geq 0\ \Longrightarrow\ f^{-1}(x)=\sqrt{x}", INK),
    "v_domran":  (r"\text{domain of }f^{-1}=\text{range of }f", INK),
    "v_relation": (r"\left(a,\,b\right)\in f\ \Longleftrightarrow\ "
                   r"\left(b,\,a\right)\in f^{-1}", INK),

    # diagnose
    "v_d1":      (r"f(x)=2x+9.\qquad f(4)=\underline{\qquad}", INK),
    "v_d2":      (r"f(x)=x-6,\ g(x)=x+6.\quad f\!\left(g(2)\right)=?", INK),
    "v_d3":      (r"y=5x-1.\ \ \text{Make }x\text{ the subject.}", INK),
    "v_d4":      (r"\sqrt{x^{2}}=\underline{\qquad}\ \ \text{for}\ x<0", INK),
    "v_d5":      (r"\left\{(1,4),(2,4),(3,9)\right\}\ \text{one-to-one?}", INK),

    # quick check, guided, gate
    "v_qc":      (r"f(x)=" + FR("x-5", "2"), INK),
    "v_g1":      (r"f(x)=7x+3", INK),
    "v_g2":      (r"f(x)=x^{3}-4", INK),
    "v_gate":    (r"f(x)=" + FR("2x+1", "5"), INK),
    "v_gate_w":  (r"f(x)=" + FR("2x+1", "5"), WHITE),

    # worksheet and routes
    "v_ws1":     (r"f(x)=6x-11", INK),
    "v_ws2":     (r"f(x)=" + FR("x", "4") + r"+9", INK),
    "v_ws3":     (r"f(x)=\sqrt{x-2},\ \ x\geq 2", INK),
    "v_ws4":     (r"f(x)=x^{2}-6x+5,\ \ x\geq 3", INK),
    "v_ws5":     (r"f(x)=" + FR("3", "x-4") + r",\ \ x\neq 4", INK),
    "v_ws6":     (r"f(x)=x^{5}+2", INK),
    "v_ws7":     (r"f\!\left(g(x)\right)=x\ \ \text{and}\ \ g\!\left(f(x)\right)=x", INK),
    "v_ws8":     (r"f(x)=|x|", INK),
    # a compact form of the two-way check, for the narrow classwork cell
    "v_bothc":   (r"f\circ f^{-1}\ \ \text{and}\ \ f^{-1}\circ f", INK),
    # the same radical without its domain, which the narrow cell cannot hold
    "v_ws3n":    (r"f(x)=\sqrt{x-2}", INK),

    # Saudi context — the riyal is pegged, so conversion is an exact inverse pair
    "ctx_sar_w": (r"U(s)=" + FR("s", "3.75") + r",\qquad S(u)=3.75u", WHITE),
    "ctx_sar":   (r"U(s)=" + FR("s", "3.75") + r",\qquad S(u)=3.75u", INK),
    "ctx_taxi":  (r"F(d)=10+2.5d", INK),
    "ctx_taxi2": (r"F^{-1}(c)=" + FR("c-10", "2.5"), INK),
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

tex = os.path.join(TMP, "w4.tex")
open(tex, "w").write("\n".join(doc))
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory", TMP, tex], capture_output=True, text=True)
if r.returncode:
    print(r.stdout[-4000:])
    raise SystemExit("pdflatex failed")

for out, dpi in (("math_w4", 500), ("math_w4_doc", 260)):
    shutil.rmtree(out, ignore_errors=True)
    os.makedirs(out)
    stem = os.path.join(TMP, f"p{dpi}")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(TMP, "w4.pdf"), stem], check=True)
    pages = sorted(f for f in os.listdir(TMP)
                   if f.startswith(f"p{dpi}-") and f.endswith(".png"))
    assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} expressions"
    idx = {}
    for k, p in zip(keys, pages):
        im = Image.open(os.path.join(TMP, p)).convert("RGBA")
        dst = os.path.join(out, k + ".png")
        im.save(dst)
        idx[k] = {"file": dst, "win": im.width / dpi, "hin": im.height / dpi,
                  "aspect": im.width / im.height}
    json.dump(idx, open(os.path.join(out, "_index.json"), "w"), indent=1)
    print(f"{len(idx)} expressions -> {out} @ {dpi} dpi")
