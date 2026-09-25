"""LaTeX for the SAAT (Tahsili) PREPARATION SHEETS.

One expression per key, rendered by pdflatex + preview into transparent PNG at
300 dpi, exactly as the weekly GAT sheets do. Nothing on a preparation sheet is
typed as plain-text mathematics.

The facts come from the department's Tahsili revision source; the wording,
worked numbers and the choice of what to put on the page are ours.
"""
import json, os, shutil, subprocess, tempfile
from PIL import Image

INK = "222E2D"
RED = "C62828"
NAVY = "1F3864"

E = {
# ===================================================================== UNIT 1
"u1_table": r"""\begin{array}{r@{\ \ }l@{\qquad}l}
\mathbb{N} & 1,\,2,\,3,\dots & \text{counting numbers}\\[2pt]
\mathbb{W} & 0,\,1,\,2,\,3,\dots & \text{whole numbers}\\[2pt]
\mathbb{Z} & \dots,{-2},{-1},0,1,2,\dots & \text{integers}\\[2pt]
\mathbb{Q} & \dfrac{a}{b},\ b\neq 0 & \text{terminating or repeating}\\[6pt]
\mathbb{I} & \sqrt{2},\ \pi,\ 0.1010010001\dots & \text{never repeats, never ends}\\[2pt]
\mathbb{R} & \mathbb{Q}\cup\mathbb{I} &
\end{array}""",

"u1_chain": r"\mathbb{N}\subset\mathbb{W}\subset\mathbb{Z}\subset\mathbb{Q}\subset\mathbb{R}",

"u1_idx":  r"a^{m}a^{n}=a^{m+n},\quad \dfrac{a^{m}}{a^{n}}=a^{m-n},\quad a^{-n}=\dfrac{1}{a^{n}}",
"u1_rad":  r"\sqrt[n]{a^{m}}=a^{\frac{m}{n}},\qquad \sqrt[2k]{x^{2k}}=\lvert x\rvert",
"u1_ratl": r"\dfrac{c}{\sqrt{a}+b}\times\dfrac{\sqrt{a}-b}{\sqrt{a}-b}",
"u1_sci":  r"a\times 10^{n},\qquad 1\leq a<10",
"u1_abs":  r"\lvert x\rvert<c\ \Leftrightarrow\ {-c}<x<c",
"u1_abs2": r"\lvert x\rvert>c\ \Leftrightarrow\ x<{-c}\ \ \text{or}\ \ x>c",

"u1_c1": r"\text{“simplest form”}\ \longrightarrow\ \text{factor, then cancel}",
"u1_c2": r"\text{“undefined”}\ \longrightarrow\ \text{set the DENOMINATOR}=0",
"u1_c3": r"\text{“smallest set”}\ \longrightarrow\ \text{evaluate first, then classify}",
"u1_c4": r"\text{“no solution”}\ \longrightarrow\ \lvert\ \rvert=\text{negative}",

"u1_t1": r"\sqrt{36}=6\quad\text{is a NATURAL number}",
"u1_t2": r"\sqrt{2}\times\sqrt{8}=\sqrt{16}=4\quad\text{is RATIONAL}",
"u1_t3": r"{-4x}>16\ \Longrightarrow\ x<{-4}",
"u1_t4": r"\sqrt[8]{(a-1)^{24}}=\lvert a-1\rvert^{3}",
"u1_t5": r"\dfrac{x-3}{(x+7)(x-3)}\ \text{is undefined at}\ x=3\ \text{too}",

"u1_q1": r"1.\ \ \left(2x^{-3}y^{3}\right)\left(7x^{5}y^{-6}\right)",
"u1_q2": r"2.\ \ \sqrt[3]{x^{7}}=x^{?}",
"u1_q3": r"3.\ \ \dfrac{2}{\sqrt{3}+1}",
"u1_q4": r"4.\ \ {-4x}+3>19",
"u1_q5": r"5.\ \ \lvert x-4\rvert<3",
"u1_q6": r"6.\ \ \dfrac{x-3}{x^{2}+4x-21}\ \text{undefined?}",
"u1_a":  r"""\text{\bf Answers}\quad
1.\ \dfrac{14x^{2}}{y^{3}}\quad
2.\ x^{\frac{7}{3}}\quad
3.\ \sqrt{3}-1\quad
4.\ x<{-4}\quad
5.\ 1<x<7\quad
6.\ x=3,\ x={-7}""",

# ===================================================================== UNIT 2
"u2_table": r"""\begin{array}{l@{\qquad}l}
b^{2}-4ac>0 & \text{two different real roots}\\[3pt]
b^{2}-4ac=0 & \text{one repeated real root}\\[3pt]
b^{2}-4ac<0 & \text{two conjugate complex roots}\\[6pt]
\multicolumn{2}{l}{\text{a PERFECT SQUARE discriminant}\ \Rightarrow\ \text{the roots are rational}}
\end{array}""",

"u2_form": r"x=\dfrac{{-b}\pm\sqrt{b^{2}-4ac}}{2a}",
"u2_vert": r"y=a(x-h)^{2}+k,\qquad x=\dfrac{{-b}}{2a}",
"u2_det":  r"\begin{vmatrix}a&b\\c&d\end{vmatrix}=ad-bc",
"u2_inv":  r"A^{-1}=\dfrac{1}{ad-bc}\begin{pmatrix}d&{-b}\\{-c}&a\end{pmatrix}",
"u2_rem":  r"f(x)\div(x-r)\ \Rightarrow\ \text{remainder}=f(r)",
"u2_fact": r"f(r)=0\ \Longleftrightarrow\ (x-r)\ \text{is a factor}",
"u2_rad":  r"\sqrt{A}=B\ \Rightarrow\ A=B^{2}",

"u2_c1": r"\text{“nature of the roots”}\ \longrightarrow\ b^{2}-4ac,\ \text{never solve}",
"u2_c2": r"\text{“no inverse”}\ \longrightarrow\ ad-bc=0",
"u2_c3": r"\text{“is a factor”}\ \longrightarrow\ \text{substitute, look for }0",
"u2_c4": r"\text{“extraneous”}\ \longrightarrow\ \text{a root the ORIGINAL rejects}",

"u2_t1": r"\text{4th term}\ \Rightarrow\ k=3,\ \text{not }4",
"u2_t2": r"\sqrt{x+7}=x-5\ \Rightarrow\ x=2\ \text{FAILS},\ x=9\ \text{holds}",
"u2_t3": r"\dfrac{x}{x-3}=\dfrac{3}{x-3}+2\ \Rightarrow\ x=3\ \text{is rejected}",
"u2_t4": r"\det=ad-bc\ \text{may be NEGATIVE}",
"u2_t5": r"3x+(x+8)=2\times 12\quad\text{(double the midsegment first)}",

"u2_q1": r"1.\ \ x^{2}-7x+12=0",
"u2_q2": r"2.\ \ 2x^{2}+3x+5:\ \text{roots?}",
"u2_q3": r"3.\ \ x^{2}-6x+11\ \to\ \text{vertex}",
"u2_q4": r"4.\ \ \text{rem.}\ \dfrac{x^{3}+2x^{2}-5}{x-2}",
"u2_q5": r"5.\ \ \sqrt{3x+4}=5",
"u2_q6": r"6.\ \ \begin{vmatrix}k&{-2}\\6&3\end{vmatrix}=0,\ \ k=?",
"u2_a":  r"""\text{\bf Answers}\quad
1.\ x=3,\,4\quad
2.\ \text{two complex}\quad
3.\ (x-3)^{2}+2\quad
4.\ 11\quad
5.\ x=7\quad
6.\ k={-4}""",
}


def render(out_dir="prep_math", dpi=300):
    shutil.rmtree(out_dir, ignore_errors=True)
    os.makedirs(out_dir)
    tmp = tempfile.mkdtemp()
    keys = list(E)
    doc = [r"\documentclass[12pt]{article}",
           r"\usepackage[active,tightpage]{preview}",
           r"\usepackage{amsmath,amssymb}",
           r"\usepackage[T1]{fontenc}",
           r"\usepackage[dvipsnames]{xcolor}",
           r"\setlength\PreviewBorder{1.5pt}",
           r"\definecolor{ink}{HTML}{%s}" % INK,
           r"\definecolor{red}{HTML}{%s}" % RED,
           r"\definecolor{navy}{HTML}{%s}" % NAVY,
           r"\begin{document}"]
    for k in keys:
        doc.append(r"\begin{preview}$\color{ink}\displaystyle %s$\end{preview}" % E[k])
    doc.append(r"\end{document}")
    tex = os.path.join(tmp, "prep.tex")
    open(tex, "w").write("\n".join(doc))
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-output-directory", tmp, tex], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-3000:])
        raise SystemExit("pdflatex failed")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(tmp, "prep.pdf"), os.path.join(tmp, "p")], check=True)
    pages = sorted(f for f in os.listdir(tmp) if f.startswith("p-") and f.endswith(".png"))
    assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} expressions"
    idx = {}
    for k, p in zip(keys, pages):
        im = Image.open(os.path.join(tmp, p)).convert("RGBA")
        dst = os.path.join(out_dir, k + ".png")
        im.save(dst)
        idx[k] = {"file": dst, "win": im.width / dpi, "hin": im.height / dpi,
                  "aspect": im.width / im.height}
    json.dump(idx, open(os.path.join(out_dir, "_index.json"), "w"), indent=1)
    print(f"{len(idx)} preparation expressions -> {out_dir} @ {dpi} dpi")


if __name__ == "__main__":
    render()
