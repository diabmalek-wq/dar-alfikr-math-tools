"""
Week 2, lessons 2-4. Real LaTeX (pdflatex + Computer Modern), tight-cropped,
transparent PNG at 500 dpi. Index carries natural inch size so the deck engine
can scale every expression to one common type size.

  A · Gr10 1-2  Transformations of Functions
  B · Gr11 5-3  Graphing Radical Functions
  C · Gr11 5-4  Solving Radical Equations
"""
import json, os, shutil, subprocess
from PIL import Image

OUT, TMP = "math_w2", ".tex_w2"
shutil.rmtree(OUT, ignore_errors=True); shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(OUT); os.makedirs(TMP)

INK, DEEP, WHITE, MAROON = "222E2D", "0E4F4C", "FFFFFF", "8A1B17"

EXPR = {
    # ---------- A · Gr10 1-2 Transformations ----------
    "t_general_w": (r"g(x)=a\,f\bigl(b(x-h)\bigr)+k", WHITE),
    "t_general":   (r"g(x)=a\,f\bigl(b(x-h)\bigr)+k", DEEP),
    "t_parent":    (r"f(x)=x^{2}", DEEP),
    "t_up":        (r"f(x)+k", INK),
    "t_right":     (r"f(x-h)", INK),
    "t_reflx":     (r"-f(x)", INK),
    "t_refly":     (r"f(-x)", INK),
    "t_stretch":   (r"a\,f(x),\ \ a>1", INK),
    "t_compress":  (r"a\,f(x),\ \ 0<a<1", INK),
    "t_horiz":     (r"f(bx)", INK),
    "t_ex":        (r"g(x)=-2(x-3)^{2}+5", DEEP),
    "t_ex_w":      (r"g(x)=-2(x-3)^{2}+5", WHITE),
    "t_qc":        (r"g(x)=\tfrac{1}{2}(x+4)^{2}-1", INK),
    "t_g1":        (r"g(x)=(x-5)^{2}+2", INK),
    "t_g2":        (r"g(x)=-3x^{2}", INK),
    "t_gate":      (r"g(x)=-\bigl(x+2\bigr)^{2}+7", WHITE),
    "t_gate_ink":  (r"g(x)=-\bigl(x+2\bigr)^{2}+7", INK),
    "t_d1":        (r"f(x)+3", INK),
    "t_d2":        (r"f(x-2)", INK),
    "t_d3":        (r"-f(x)", INK),
    "t_d4":        (r"4f(x)", INK),
    "t_d5":        (r"f(-x)", INK),
    "t_ans_d":     (r"\text{up }3\ ;\ \text{right }2\ ;\ \text{reflect in the }x\text{-axis}"
                    r"\ ;\ \text{stretch}\times 4\ ;\ \text{reflect in the }y\text{-axis}", DEEP),
    "t_ws1":       (r"g(x)=(x+1)^{2}-4", INK),
    "t_ws2":       (r"g(x)=2(x-3)^{2}", INK),
    "t_ws3":       (r"g(x)=-\tfrac{1}{3}x^{2}+6", INK),
    "t_ws4":       (r"g(x)=(2x)^{2}", INK),
    "t_ws5":       (r"g(x)=-(x-1)^{2}-2", INK),
    "t_ws6":       (r"g(x)=\tfrac{1}{4}(x+5)^{2}+3", INK),

    # ---------- B · Gr11 5-3 Graphing Radical Functions ----------
    "r_parent_w":  (r"f(x)=\sqrt{x}\qquad f(x)=\sqrt[3]{x}", WHITE),
    "r_sqrt":      (r"f(x)=\sqrt{x}", DEEP),
    "r_cbrt":      (r"f(x)=\sqrt[3]{x}", DEEP),
    "r_nth":       (r"f(x)=\sqrt[n]{x}", DEEP),
    "r_general":   (r"g(x)=a\sqrt[n]{b(x-h)}+k", DEEP),
    "r_general_w": (r"g(x)=a\sqrt[n]{b(x-h)}+k", WHITE),
    "r_dom_even":  (r"[\,0,\ \infty\,)", INK),
    "r_dom_odd":   (r"(\,{-\infty},\ \infty\,)", INK),
    "r_ex":        (r"g(x)=2\sqrt{x-3}+1", DEEP),
    "r_ex_w":      (r"g(x)=2\sqrt{x-3}+1", WHITE),
    "r_ex_dom":    (r"[\,3,\ \infty\,)", INK),
    "r_qc":        (r"g(x)=\sqrt{x+5}-2", INK),
    "r_g1":        (r"g(x)=\sqrt{x-4}", INK),
    "r_g2":        (r"g(x)=-\sqrt[3]{x}+2", INK),
    "r_gate":      (r"g(x)=3\sqrt{x+1}-4", WHITE),
    "r_gate_ink":  (r"g(x)=3\sqrt{x+1}-4", INK),
    "r_ws1":       (r"g(x)=\sqrt{x}+5", INK),
    "r_ws2":       (r"g(x)=\sqrt{x-2}", INK),
    "r_ws3":       (r"g(x)=-\sqrt{x}", INK),
    "r_ws4":       (r"g(x)=\sqrt[3]{x+4}", INK),
    "r_ws5":       (r"g(x)=\tfrac{1}{2}\sqrt{x}", INK),
    "r_ws6":       (r"g(x)=\sqrt{-x}", INK),
    "r_ws7":       (r"g(x)=2\sqrt[3]{x}-3", INK),
    "r_ws8":       (r"g(x)=\sqrt{4-x}", INK),

    # ---------- C · Gr11 5-4 Solving Radical Equations ----------
    "s_head_w":    (r"\sqrt{x+5}=x-1", WHITE),
    "s_step1":     (r"\sqrt{x+5}=x-1", INK),
    "s_step2":     (r"x+5=(x-1)^{2}", INK),
    "s_step3":     (r"x+5=x^{2}-2x+1", INK),
    "s_step4":     (r"x^{2}-3x-4=0", INK),
    "s_step5":     (r"(x-4)(x+1)=0", INK),
    "s_step6":     (r"x=4\ \ \text{or}\ \ x=-1", INK),
    "s_check_ok":  (r"\sqrt{4+5}=3=4-1\ \ \checkmark", DEEP),
    "s_check_no":  (r"\sqrt{-1+5}=2\neq-1-1\ \ \times", MAROON),
    "s_qc":        (r"\sqrt{2x+3}=x", INK),
    "s_g1":        (r"\sqrt{3x-2}=4", INK),
    "s_g2":        (r"\sqrt[3]{x-1}=2", INK),
    "s_ineq":      (r"\sqrt{x-2}<3", INK),
    "s_ineq_ans":  (r"2\leq x<11", DEEP),
    "s_gate":      (r"\sqrt{x+7}=x-5", WHITE),
    "s_gate_ink":  (r"\sqrt{x+7}=x-5", INK),
    "s_ws1":       (r"\sqrt{x}=7", INK),
    "s_ws2":       (r"\sqrt{x+4}=5", INK),
    "s_ws3":       (r"\sqrt[3]{2x}=4", INK),
    "s_ws4":       (r"\sqrt{5x-1}=2", INK),
    "s_ws5":       (r"\sqrt{x+6}=x", INK),
    "s_ws6":       (r"\sqrt{3x+1}=x-3", INK),
    "s_ws7":       (r"\sqrt{x-3}\geq 2", INK),
    "s_ws8":       (r"\sqrt{2x+1}<5", INK),

    # ---------- Saudi contexts ----------
    "ctx_pend_w":  (r"T=2\pi\sqrt{\dfrac{L}{g}}", WHITE),
    "ctx_pend":    (r"T=2\pi\sqrt{\dfrac{L}{g}}", INK),
    "ctx_speed_w": (r"v=\sqrt{2gh}", WHITE),
    "ctx_speed":   (r"v=\sqrt{2gh}", INK),
    "ctx_arch_w":  (r"h(x)=-0.02(x-30)^{2}+18", WHITE),
    "ctx_arch":    (r"h(x)=-0.02(x-30)^{2}+18", INK),
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

tex = os.path.join(TMP, "w2.tex")
open(tex, "w").write("\n".join(doc))
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory", TMP, tex], capture_output=True, text=True)
if r.returncode:
    print(r.stdout[-4000:]); raise SystemExit("pdflatex failed")
subprocess.run(["pdftocairo", "-png", "-transp", "-r", "500",
                os.path.join(TMP, "w2.pdf"), os.path.join(TMP, "p")], check=True)

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
