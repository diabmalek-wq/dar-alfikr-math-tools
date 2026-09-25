"""
Grade 11 · Algebra II · Topic 5 · Lesson 5-2
Properties of Exponents and Radical Functions

Expressions are typeset by *real LaTeX* (pdflatex + Computer Modern), one per
page, cropped tight by the preview package, then rasterised to transparent PNG
at 500 dpi with pdftocairo. This gives true stretched vinculums over radicands,
proper \\sqrt[n]{} indices and textbook-grade fraction rules — matplotlib's
mathtext mis-sizes the radical bar when the radicand carries exponents.

Writes math11/_index.json -> {file, aspect}.
"""
import json
import os
import shutil
import subprocess

OUT = "math11"
TMP = ".tex11"
shutil.rmtree(OUT, ignore_errors=True)
shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(OUT, exist_ok=True)
os.makedirs(TMP, exist_ok=True)

INK = "222E2D"
DEEP = "0E4F4C"
WHITE = "FFFFFF"
MAROON = "8A1B17"

EXPR = {
    # ---- headline -------------------------------------------------------
    "def_w":      (r"a^{\frac{m}{n}}=\sqrt[n]{a^{m}}=\bigl(\sqrt[n]{a}\bigr)^{m}", WHITE),
    "def_deep":   (r"a^{\frac{m}{n}}=\sqrt[n]{a^{m}}=\bigl(\sqrt[n]{a}\bigr)^{m}", DEEP),
    "def_ink":    (r"a^{\frac{m}{n}}=\sqrt[n]{a^{m}}=\bigl(\sqrt[n]{a}\bigr)^{m}", INK),

    # ---- prior knowledge -------------------------------------------------
    "pk_prod":    (r"a^{m}\cdot a^{n}=a^{m+n}", DEEP),
    "pk_root":    (r"\sqrt[3]{125}=5", DEEP),
    "pk_square":  (r"\sqrt{36}=6", DEEP),

    # ---- properties of exponents ----------------------------------------
    "p_prod":     (r"a^{m}\cdot a^{n}=a^{m+n}", INK),
    "p_quot":     (r"\dfrac{a^{m}}{a^{n}}=a^{m-n}", INK),
    "p_pow":      (r"\bigl(a^{m}\bigr)^{n}=a^{mn}", INK),
    "p_prodpow":  (r"(ab)^{m}=a^{m}b^{m}", INK),
    "p_quotpow":  (r"\left(\dfrac{a}{b}\right)^{m}=\dfrac{a^{m}}{b^{m}}", INK),
    "p_neg":      (r"a^{-m}=\dfrac{1}{a^{m}}", INK),
    "p_zero":     (r"a^{0}=1", INK),

    "e_prod":     (r"7^{\frac{1}{2}}\cdot 7^{\frac{3}{2}}=7^{2}=49", DEEP),
    "e_quot":     (r"\dfrac{5^{\frac{7}{3}}}{5^{\frac{1}{3}}}=5^{2}=25", DEEP),
    "e_pow":      (r"\bigl(8^{\frac{1}{3}}\bigr)^{2}=8^{\frac{2}{3}}=4", DEEP),
    "e_prodpow":  (r"(9x)^{\frac{1}{2}}=3x^{\frac{1}{2}}", DEEP),
    "e_quotpow":  (r"\left(\dfrac{x}{16}\right)^{\frac{1}{2}}=\dfrac{x^{\frac{1}{2}}}{4}", DEEP),
    "e_neg":      (r"27^{-\frac{2}{3}}=\dfrac{1}{9}", DEEP),
    "e_zero":     (r"\bigl(5\sqrt{3}\bigr)^{0}=1", DEEP),

    # ---- properties of radicals -----------------------------------------
    "r_prod":     (r"\sqrt[n]{a}\cdot\sqrt[n]{b}=\sqrt[n]{ab}", INK),
    "r_quot":     (r"\dfrac{\sqrt[n]{a}}{\sqrt[n]{b}}=\sqrt[n]{\dfrac{a}{b}}", INK),
    "r_prod_ex":  (r"\sqrt{6}\cdot\sqrt{10}=\sqrt{60}=2\sqrt{15}", DEEP),
    "r_quot_ex":  (r"\dfrac{\sqrt[3]{54}}{\sqrt[3]{2}}=\sqrt[3]{27}=3", DEEP),
    "r_warn":     (r"\sqrt{2}+\sqrt{3}\neq\sqrt{5}", MAROON),

    # ---- like radicals ---------------------------------------------------
    "like_yes":   (r"2\sqrt[3]{5}+7\sqrt[3]{5}=9\sqrt[3]{5}", DEEP),
    "like_no":    (r"3\sqrt{2}+3\sqrt[3]{2}", MAROON),

    # ---- conjugates / rationalising --------------------------------------
    "conj_id":    (r"(a-b)(a+b)=a^{2}-b^{2}", INK),
    "conj_num":   (r"\bigl(3-\sqrt{5}\bigr)\bigl(3+\sqrt{5}\bigr)=9-5=4", DEEP),
    "conj_full":  (r"\dfrac{6}{3-\sqrt{5}}\cdot\dfrac{3+\sqrt{5}}{3+\sqrt{5}}"
                   r"=\dfrac{6\bigl(3+\sqrt{5}\bigr)}{4}"
                   r"=\dfrac{3\bigl(3+\sqrt{5}\bigr)}{2}", INK),
    "mono_rat":   (r"\dfrac{6}{\sqrt{3}}\cdot\dfrac{\sqrt{3}}{\sqrt{3}}"
                   r"=\dfrac{6\sqrt{3}}{3}=2\sqrt{3}", INK),

    # ---- diagnostic ------------------------------------------------------
    "d1":         (r"\sqrt{50}", INK),
    "d2":         (r"8^{\frac{2}{3}}", INK),
    "d3":         (r"\sqrt[3]{5}\cdot\sqrt[3]{25}", INK),
    "d4":         (r"\dfrac{10}{\sqrt{5}}", INK),
    "d5":         (r"4\sqrt{7}-\sqrt{7}", INK),

    # ---- modelled example ------------------------------------------------
    "w_start":    (r"\sqrt[3]{54x^{4}y^{7}}", DEEP),
    "w_split":    (r"\sqrt[3]{27x^{3}y^{6}}\cdot\sqrt[3]{2xy}", INK),
    "w_end":      (r"3xy^{2}\sqrt[3]{2xy}", DEEP),

    # ---- quick check -----------------------------------------------------
    "qc":         (r"\left(\dfrac{16x^{8}}{81}\right)^{\frac{3}{4}}", INK),

    # ---- guided practice -------------------------------------------------
    "g1":         (r"\bigl(27x^{6}\bigr)^{\frac{2}{3}}", INK),
    "g2":         (r"\dfrac{14}{\sqrt{7}+\sqrt{2}}", INK),

    # ---- differentiated routes -------------------------------------------
    "t1a":        (r"\sqrt{75}", INK),
    "t2a":        (r"\dfrac{8}{4-\sqrt{2}}", INK),
    "t3a":        (r"\sqrt[3]{a}\cdot\sqrt{a}=a^{\frac{5}{6}}", INK),

    # ---- production: Sakaka solar plant ----------------------------------
    "s_side":     (r"s=\sqrt{A}=A^{\frac{1}{2}}", WHITE),
    "s_ratio":    (r"\dfrac{120}{5+\sqrt{5}}", WHITE),
    "s_answer":   (r"30-6\sqrt{5}", WHITE),
    "s_ratio_ink":(r"\dfrac{120}{5+\sqrt{5}}", INK),
    "diag_rule":  (r"\text{diagonal}=\text{side}\times\sqrt{2}", INK)
,

    # ---- mastery gate ----------------------------------------------------
    "gate1":      (r"\left(\dfrac{8x^{9}}{125}\right)^{\frac{2}{3}}", WHITE),
    "gate2":      (r"\dfrac{4}{5-\sqrt{3}}", WHITE),
    "gate1_ink":  (r"\left(\dfrac{8x^{9}}{125}\right)^{\frac{2}{3}}", INK),
    "gate2_ink":  (r"\dfrac{4}{5-\sqrt{3}}", INK),

    # ---- exam connection -------------------------------------------------
    "x_sat":      (r"x^{\frac{3}{4}}=\sqrt[4]{x^{3}}", INK),

    # ---- teacher answer keys and grouped question strips -----------------
    "d_all":      (r"\sqrt{50}\qquad 8^{\frac{2}{3}}\qquad \sqrt[3]{5}\cdot\sqrt[3]{25}"
                   r"\qquad \dfrac{10}{\sqrt{5}}\qquad 4\sqrt{7}-\sqrt{7}", INK),
    "ans_diag":   (r"5\sqrt{2}\quad;\quad 4\quad;\quad 5\quad;\quad 2\sqrt{5}\quad;\quad 3\sqrt{7}", DEEP),
    "ans_qc":     (r"\dfrac{8x^{6}}{27}", DEEP),
    "guided_all": (r"\bigl(27x^{6}\bigr)^{\frac{2}{3}}\qquad\qquad \dfrac{14}{\sqrt{7}+\sqrt{2}}", INK),
    "ans_guided": (r"9x^{4}\quad;\quad \dfrac{14\bigl(\sqrt{7}-\sqrt{2}\bigr)}{5}", DEEP),
    "routes_all": (r"\sqrt{75}\qquad\qquad \dfrac{8}{4-\sqrt{2}}\qquad\qquad \sqrt[3]{a}\cdot\sqrt{a}=a^{\frac{5}{6}}", INK),
    "gate_all":   (r"\left(\dfrac{8x^{9}}{125}\right)^{\frac{2}{3}}\qquad\qquad \dfrac{4}{5-\sqrt{3}}", INK),
    "ans_gate":   (r"\dfrac{4x^{6}}{25}\quad;\quad \dfrac{2\bigl(5+\sqrt{3}\bigr)}{11}", DEEP),
    "ans_sakaka": (r"20\sqrt{5}\ \mathrm{m}\quad;\quad 20\sqrt{10}\ \mathrm{m},\ \text{ratio}\ \sqrt{2}"
                   r"\quad;\quad 3600\sqrt{5}\ \mathrm{SAR}\quad;\quad 30-6\sqrt{5}", DEEP),
    "ans_court":  (r"6\sqrt{5}\ \mathrm{m}\quad;\quad 24\sqrt{5}\ \mathrm{m}\quad;\quad"
                   r"1560\sqrt{5}\ \mathrm{SAR}\quad;\quad 6\sqrt{10}\ \mathrm{m}", DEEP),

    # ---- worksheet bank ---------------------------------------------------
    "ws_1":       (r"\sqrt{18}", INK),
    "ws_2":       (r"\sqrt{48}", INK),
    "ws_3":       (r"16^{\frac{3}{4}}", INK),
    "ws_4":       (r"32^{\frac{2}{5}}", INK),
    "ws_5":       (r"\sqrt{3}\cdot\sqrt{12}", INK),
    "ws_6":       (r"\dfrac{\sqrt{80}}{\sqrt{5}}", INK),
    "ws_7":       (r"\dfrac{9}{\sqrt{6}}", INK),
    "ws_8":       (r"\dfrac{5}{2+\sqrt{3}}", INK),
    "ws_9":       (r"\dfrac{12}{\sqrt{7}-\sqrt{3}}", INK),
    "ws_10":      (r"6\sqrt{5}+2\sqrt{5}-\sqrt{5}", INK),
    "ws_11":      (r"\sqrt[3]{16}+\sqrt[3]{54}", INK),
    "ws_12":      (r"\bigl(x^{\frac{2}{3}}\bigr)^{\frac{3}{4}}", INK),
    "ws_13":      (r"\sqrt[4]{81x^{8}}", INK),
    "ws_14":      (r"\dfrac{a^{\frac{5}{6}}}{a^{\frac{1}{3}}}", INK),
    "ws_15":      (r"\left(\dfrac{27}{64}\right)^{-\frac{2}{3}}", INK),
    "ws_16":      (r"\sqrt{50x^{3}}", INK),
    "ws_17":      (r"\dfrac{\sqrt{2}}{\sqrt{6}+\sqrt{2}}", INK),
    "ws_18":      (r"\sqrt[3]{8x^{6}y^{9}}", INK),
}

keys = list(EXPR.keys())

head = [
    r"\documentclass[12pt]{article}",
    r"\usepackage[active,tightpage]{preview}",
    r"\usepackage{amsmath,amssymb}",
    r"\usepackage[dvipsnames]{xcolor}",
    r"\setlength\PreviewBorder{1.5pt}",
]
for k, (_, c) in EXPR.items():
    head.append(r"\definecolor{c%s}{HTML}{%s}" % (k.replace("_", ""), c))
head.append(r"\begin{document}")
for k in keys:
    latex, _ = EXPR[k]
    head.append(r"\begin{preview}$\color{c%s}\displaystyle %s$\end{preview}"
                % (k.replace("_", ""), latex))
head.append(r"\end{document}")

tex = os.path.join(TMP, "all.tex")
with open(tex, "w") as f:
    f.write("\n".join(head))

r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory", TMP, tex],
                   capture_output=True, text=True)
if r.returncode != 0:
    print(r.stdout[-4000:])
    raise SystemExit("pdflatex failed")

subprocess.run(["pdftocairo", "-png", "-transp", "-r", "500",
                os.path.join(TMP, "all.pdf"), os.path.join(TMP, "p")], check=True)

from PIL import Image

pages = sorted(f for f in os.listdir(TMP) if f.startswith("p-") and f.endswith(".png"))
assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} expressions"

index = {}
for k, page in zip(keys, pages):
    dst = os.path.join(OUT, f"{k}.png")
    im = Image.open(os.path.join(TMP, page)).convert("RGBA")
    im.save(dst)
    index[k] = {"file": dst, "aspect": im.width / im.height}

with open(os.path.join(OUT, "_index.json"), "w") as f:
    json.dump(index, f, indent=1)
print(f"{len(index)} expressions typeset with LaTeX")
