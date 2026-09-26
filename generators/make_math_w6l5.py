"""
Gr11 T6 L6-5 Properties of Logarithms. Same pipeline as make_math_w6l4.py — real
LaTeX (pdflatex + Computer Modern), tight-cropped transparent PNG, rendered at
500 dpi for slides and 260 dpi for documents. Prefix m_.
"""
import json, os, shutil, subprocess
from PIL import Image

TMP = ".tex_w6l5"
shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(TMP)

INK, DEEP, WHITE, MAROON = "222E2D", "0E4F4C", "FFFFFF", "8A1B17"

EXPR = {
    "m_title_w": (r"\log_b x = \dfrac{\log_c x}{\log_c b}", WHITE),
    "m_def":     (r"\log_b(xy)=\log_b x+\log_b y", INK),

    # prior knowledge
    "m_prior_exp_rules": (r"x^{a}\cdot x^{b}=x^{a+b}", INK),
    "m_prior_log_def":   (r"\log_b x = y \iff b^{y}=x", INK),
    "m_prior_inverse":   (r"\log_b(b^{x})=x \qquad b^{\log_b x}=x", INK),

    # diagnose (recall exponent rules and Lesson 6-4 inverse properties)
    "m_d1": (r"\log_5 25 = \underline{\qquad}", INK),
    "m_d2": (r"2^{3}\cdot 2^{4} = \underline{\qquad}", INK),
    "m_d3": (r"\dfrac{3^{7}}{3^{2}} = \underline{\qquad}", INK),
    "m_d4": (r"\log_4(4^{6}) = \underline{\qquad}", INK),
    "m_d5": (r"(5^{2})^{3} = \underline{\qquad}", INK),

    # instruction 1 — product and quotient properties
    "m_prod_rule":  (r"\log_b(xy) = \log_b x + \log_b y \qquad (x,y>0)", INK),
    "m_quot_rule":  (r"\log_b\!\left(\dfrac{x}{y}\right) = \log_b x - \log_b y \qquad (x,y>0)", INK),
    "m_prod_proof": (r"\log_b(xy)=\log_b\!\left(b^{\log_b x}\cdot b^{\log_b y}\right)=\log_b\!\left(b^{\log_b x + \log_b y}\right)=\log_b x+\log_b y", INK),
    "m_prod_ex1":   (r"\log_2 5 + \log_2 3 = \log_2(5\cdot 3) = \log_2 15", INK),
    "m_quot_ex1":   (r"\log_7 40 - \log_7 8 = \log_7\!\left(\dfrac{40}{8}\right) = \log_7 5", INK),
    "m_prod_result": (r"\log_2 15", INK),
    "m_quot_result": (r"\log_7 5", INK),
    "m_cond_ex":    (r"\log_3 4 + \log_3 5 - \log_3 2 = \log_3\!\left(\dfrac{4\cdot 5}{2}\right) = \log_3 10", INK),

    # instruction 2 — power property, expand / condense
    "m_pow_rule":    (r"\log_b(x^{n}) = n\log_b x", INK),
    "m_pow_proof":   (r"\log_b(x^{n}) = \log_b\!\left(b^{\,n\log_b x}\right) = n\log_b x", INK),
    "m_special1":    (r"\log_b 1 = 0 \qquad \log_b b = 1", INK),
    "m_expand_ex":   (r"\log_5\!\left(\dfrac{x^{3}y}{z^{2}}\right) = 3\log_5 x + \log_5 y - 2\log_5 z", INK),
    "m_condense_ex": (r"2\log_4 x - \dfrac{1}{2}\log_4 y = \log_4\!\left(\dfrac{x^{2}}{\sqrt{y}}\right)", INK),

    # instruction 3 — change of base, solving for an exponent (geometric growth)
    "m_cob_formula": (r"\log_b x = \dfrac{\log_c x}{\log_c b} \qquad (\text{any base } c>0,\ c\neq 1)", INK),
    "m_cob_calc":    (r"\log_5 12 = \dfrac{\log 12}{\log 5} \approx 1.544", INK),
    "m_cob_calc_ln": (r"\log_5 12 = \dfrac{\ln 12}{\ln 5} \approx 1.544", INK),
    "m_geo_recur":   (r"a_n = 1.12\,a_{n-1}, \quad a_1 = 40", INK),
    "m_geo_explicit":(r"a_n = 40(1.12)^{\,n-1}", INK),
    "m_geo_solve":   (r"40(1.12)^{\,n-1} = 100 \;\Rightarrow\; (1.12)^{\,n-1} = 2.5 \;\Rightarrow\; n-1 = \log_{1.12} 2.5 = \dfrac{\log 2.5}{\log 1.12} \approx 8.09", INK),
    "m_geo_answer":  (r"n \approx 9.09 \;\Rightarrow\; \text{capacity first exceeds 100 MW during year 9}", INK),

    # quick check
    "m_qc": (r"\log_2 20 - \log_2 5 = \underline{\qquad}", INK),

    # guided
    "m_g1": (r"\log_6 4 + \log_6 9 = \underline{\qquad}", INK),
    "m_g2": (r"\log_7\!\left(\dfrac{x^{4}}{y^{3}}\right) = \underline{\qquad}", INK),

    # worksheet / routes
    "m_ws1": (r"\log_3 8 + \log_3 6", INK),
    "m_ws2": (r"\log_5 100 - \log_5 4", INK),
    "m_ws3": (r"\log_2(x^{5}y)", INK),
    "m_ws4": (r"3\log_4 x + 2\log_4 y - \log_4 z", INK),
    "m_cob_ws1": (r"\log_7 50 = \underline{\qquad}\quad(\text{use change of base})", INK),
    "m_cob_ws2": (r"\log_3 200 = \underline{\qquad}\quad(\text{use change of base})", INK),

    # mastery gate
    "m_gate1_w": (r"\log_2 40 - \log_2 5", WHITE),
    "m_gate1":   (r"\log_2 40 - \log_2 5", INK),
    "m_gate2":   (r"\log_5\!\left(\dfrac{x^{2}}{y}\right) = \underline{\qquad}", INK),
    "m_gate3_w": (r"\log_4 3 + \log_4 12", WHITE),

    # exam cards
    "m_ex_saat": (r"\text{Simplify } \log_2 24 - \log_2 3.", INK),
    "m_ex_sat":  (r"\text{Evaluate } \log_6 50 \text{ to three decimal places using change of base.}", INK),
    "m_ex_gat":  (r"\log_4 3 + \log_4 12 = \underline{\qquad}", INK),

    # production task — solar capacity growth (Vision 2030)
    "m_prod_w":     (r"a_n = 40(1.12)^{\,n-1}", WHITE),
    "m_prod_eq":    (r"a_n = 40(1.12)^{\,n-1}", INK),
}

keys = list(EXPR)
doc = [r"\documentclass[12pt]{article}", r"\usepackage[active,tightpage]{preview}",
       r"\usepackage{amsmath,amssymb,array}", r"\usepackage[dvipsnames]{xcolor}",
       r"\setlength\PreviewBorder{1.5pt}"]
for k, (_, c) in EXPR.items():
    doc.append(r"\definecolor{c%s}{HTML}{%s}" % (k.replace("_", ""), c))
doc.append(r"\begin{document}")
for k in keys:
    doc.append(r"\begin{preview}$\color{c%s}\displaystyle %s$\end{preview}"
               % (k.replace("_", ""), EXPR[k][0]))
doc.append(r"\end{document}")

tex = os.path.join(TMP, "w6l5.tex")
open(tex, "w").write("\n".join(doc))
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory", TMP, tex], capture_output=True, text=True)
if r.returncode:
    print(r.stdout[-4000:])
    raise SystemExit("pdflatex failed")

for out, dpi in (("math_w6l5", 500), ("math_w6l5_doc", 260)):
    shutil.rmtree(out, ignore_errors=True)
    os.makedirs(out)
    stem = os.path.join(TMP, f"p{dpi}")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(TMP, "w6l5.pdf"), stem], check=True)
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
