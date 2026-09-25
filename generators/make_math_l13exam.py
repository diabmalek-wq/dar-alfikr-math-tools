"""Math expressions for the AP Precalculus L1-3 (1.3 Rates of Change in Linear and
Quadratic Functions) EXAM-STYLE deck (non-FIKR, 12-slide, rich-content rebuild).
Same pattern as make_math_l11exam.py so lesson_l13_exam.js's eq() helper can consume it.
Numbers verified in-session (Python) before being typeset here.
"""
import json, os, shutil, subprocess
from PIL import Image

OUT, TMP = "math_l13exam", ".tex_l13exam"
shutil.rmtree(OUT, ignore_errors=True); shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(OUT); os.makedirs(TMP)

INK, DEEP, WHITE, MAROON = "222E2D", "0E4F4C", "FFFFFF", "8A1B17"

EXPR = {
    "title_eq":      (r"\text{AROC}_{[a,b]}=\dfrac{f(b)-f(a)}{b-a}", WHITE),

    "linear_f":      (r"f(x)=mx+b", INK),
    "linear_proof":  (r"\text{AROC}_{[a,b]}=\dfrac{f(b)-f(a)}{b-a}=\dfrac{m(b-a)}{b-a}={m}", DEEP),

    "albalad_f":     (r"f(x)=6x+26", INK),
    "albalad_table": (r"\begin{array}{c|ccc}x&-4&-1&5\\\hline f(x)&2&20&56\end{array}", INK),
    "albalad_check": (r"\dfrac{20-2}{-1-(-4)}=\dfrac{18}{3}=6 \qquad \dfrac{56-20}{5-(-1)}=\dfrac{36}{6}=6", INK),
    "albalad_ans":   (r"f(10)=6(10)+26={86}", WHITE),

    "quad_f":        (r"f(x)=ax^{2}+bx+c", INK),
    "quad_deriv":    (r"\text{AROC}_{[x,\,x+h]}=\dfrac{f(x+h)-f(x)}{h}=a(2x+h)+b", INK),
    "quad_note":     (r"\text{linear in }x,\ \text{slope}=2ah \qquad (h{=}1:\ \text{slope}=2a)", DEEP),

    "ex2_f":         (r"f(x)=2x^{2}-3x+5 \qquad (a=2)", INK),
    "ex2_aroc":      (r"\text{AROC}(x)=f(x+1)-f(x)=4x-1", INK),
    "ex2_check":     (r"\text{slope}=4=2(2)=2a \ \checkmark", DEEP),
    "ex2_turn":      (r"\text{AROC}_{[0,2]}=10,\ \ \text{AROC}_{[2,4]}=18 \ \Rightarrow\ \text{AROC}_{[6,8]}={34}", DEEP),

    "concav_up":     (r"\Delta^{2}f>0 \ \Rightarrow\ \text{concave up}", WHITE),
    "concav_down":   (r"\Delta^{2}f<0 \ \Rightarrow\ \text{concave down}", WHITE),

    "ex3_table":     (r"\begin{array}{c|ccccc}x&0&1&2&3&4\\\hline g(x)&10&7&3&-2&-8\end{array}", INK),
    "ex3_d1":        (r"\text{1st diffs: } -3,\ -4,\ -5,\ -6", INK),
    "ex3_d2":        (r"\text{2nd diffs: } -1,\ -1,\ -1 \ \Rightarrow\ \text{concave down}", MAROON),

    "units_bad":     (r"v(t)\ \text{in m/s} \quad\Rightarrow\quad \text{rate of the rate }\neq\ \text{m/s}", WHITE),
    "units_good":    (r"\text{rate of the rate of } v \ \text{has units}\ \dfrac{\text{m/s}}{\text{s}} = \text{m/s per second}", WHITE),

    "trap10_setup":  (r"p(x)=g(x+1)-g(x)", INK),
    "trap10_given":  (r"p(x)=5\ \text{ for all } x", INK),
    "trap10_ans":    (r"\Rightarrow\ g\ \text{is linear, rate of change }5 \quad (\text{NOT concave up or down})", MAROON),
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

tex = os.path.join(TMP, "l13exam.tex")
open(tex, "w").write("\n".join(doc))
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory", TMP, tex], capture_output=True, text=True)
if r.returncode:
    print(r.stdout[-4000:]); raise SystemExit("pdflatex failed")
subprocess.run(["pdftocairo", "-png", "-transp", "-r", "500",
                os.path.join(TMP, "l13exam.pdf"), os.path.join(TMP, "p")], check=True)

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
