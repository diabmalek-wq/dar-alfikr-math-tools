"""LaTeX for part B of the simulated SAAT bank — Unit 1, sessions 1-9.

Rendered into the SAME index the part A expressions use, so the bank builds from
one maths folder. Run make_math_saat.py first; this appends to its output.
"""
import json, os, subprocess, tempfile
from PIL import Image

INK = "222E2D"

E = {
    # ---------------------------------------- session 1, real numbers
    "b_set1": r"\sqrt{36}",
    "b_prop": r"3\left(x-\dfrac{7}{6}\right)=3x-\dfrac{7}{2}",
    "b_mi":   r"{-\dfrac{3}{5}}",
    "b_mi1":  r"\dfrac{5}{3}",
    "b_mi2":  r"{-\dfrac{5}{3}}",
    "b_mi3":  r"\dfrac{3}{5}",
    "b_mi4":  r"{-\dfrac{3}{5}}",

    # ------------------------------- session 2, rational and irrational
    "b_ir1": r"\dfrac{22}{7}",
    "b_ir2": r"0.\overline{32}",
    "b_ir3": r"{-\sqrt{121}}",
    "b_ir4": r"\sqrt{8}",
    "b_sur": r"\sqrt{2}\times\sqrt{8}",
    "b_bet": r"\sqrt{55}",

    # ------------------------------------ session 3, exponents and radicals
    "b_pow":  r"\left(2x^{-3}y^{3}\right)\left(7x^{5}y^{-6}\right)",
    "b_pow1": r"\dfrac{14y^{9}}{x^{8}}",
    "b_pow2": r"14x^{2}y^{-3}",
    "b_pow3": r"\dfrac{14x^{2}}{y^{3}}",
    "b_pow4": r"\dfrac{9x^{2}}{y^{3}}",
    "b_rad":  r"\sqrt[3]{x^{7}}",
    "b_rad1": r"x^{\frac{7}{3}}",
    "b_rad2": r"x^{\frac{3}{7}}",
    "b_rad3": r"x^{4}",
    "b_rad4": r"x^{21}",
    "b_abs":  r"\sqrt[8]{(a-1)^{24}}",
    "b_abs1": r"(a-1)^{3}",
    "b_abs2": r"\lvert a-1\rvert^{3}",
    "b_abs3": r"\lvert a-1\rvert^{192}",
    "b_abs4": r"\lvert a-1\rvert^{16}",
    "b_qr":   r"\dfrac{\sqrt{63}}{\sqrt{28}}",
    "b_qr1":  r"\sqrt{35}",
    "b_qr2":  r"\sqrt{7}",
    "b_qr3":  r"\dfrac{3}{2}",
    "b_qr4":  r"\dfrac{9}{4}",
    "b_ratl":  r"\dfrac{2}{\sqrt{3}+1}",
    "b_ratl1": r"\sqrt{3}-1",
    "b_ratl2": r"\sqrt{3}+1",
    "b_ratl3": r"\dfrac{\sqrt{3}-1}{2}",
    "b_ratl4": r"\dfrac{2\sqrt{3}-2}{\sqrt{3}+1}",

    # --------------------------------------- session 4, scientific notation
    "b_cmp1": r"9.9\times 10^{-3}",
    "b_cmp2": r"1.2\times 10^{-2}",
    "b_cmp3": r"8.5\times 10^{-3}",
    "b_cmp4": r"1.05\times 10^{-2}",

    # ------------------------------------- session 5, algebraic expressions
    "b_lead":  r"{-x}-3x^{2}-2x^{4}",
    "b_area1": r"x-8",
    "b_area2": r"x+8",
    "b_area3": r"x+5",
    "b_area4": r"8x",
    "b_negp":  r"\dfrac{2a^{3}b^{2}}{6ba^{5}}",
    "b_negp1": r"\dfrac{a^{8}b^{3}}{3}",
    "b_negp2": r"{-\dfrac{b}{4a^{2}}}",
    "b_negp3": r"\dfrac{a^{2}b}{3}",
    "b_negp4": r"\dfrac{b}{3a^{2}}",
    "b_subm":  r"f(x)=2x^{2}-3x-3",
    "b_subm1": r"{-2x^{2}}+6x-3",
    "b_subm2": r"8x^{2}-6x-3",
    "b_subm3": r"8x^{2}+6x-3",
    "b_subm4": r"8x^{2}+6x+6",

    # ------------------------------------------------ session 6, factoring
    "b_dos":  r"\dfrac{a^{2}-b^{2}}{3b}\times\dfrac{9b^{2}}{a-b}",
    "b_dos1": r"\dfrac{9b\left(a^{2}-b^{2}\right)}{3(a-b)}",
    "b_dos2": r"3b(a+b)",
    "b_dos3": r"\dfrac{3(a+b)}{b}",
    "b_dos4": r"3b(a-b)",
    "b_tri1": r"x+5",
    "b_tri2": r"x-5",
    "b_tri3": r"x+4",
    "b_tri4": r"x+1",
    "b_pr1":  r"2x+4",
    "b_pr2":  r"x^{2}-y^{2}",
    "b_pr3":  r"3x-7",
    "b_pr4":  r"x^{2}+5x",
    "b_grp":  r"x^{3}+2x^{2}-3x-6",
    "b_grp1": r"(x+2)\left(x^{2}+3\right)",
    "b_grp2": r"(x+2)\left(x-\sqrt{3}\right)\left(x+\sqrt{3}\right)",
    "b_grp3": r"(x-2)\left(x^{2}-3\right)",
    "b_grp4": r"(x+2)\left(x^{2}-3\right)",

    # --------------------------------------- session 7, algebraic fractions
    "b_rat":  r"\dfrac{(x-2)(x-3)^{2}}{(4x-12)\left(x^{2}+x-6\right)}",
    "b_rat1": r"\dfrac{x-3}{4(x+3)}",
    "b_rat2": r"\dfrac{1}{4(x+3)}",
    "b_rat3": r"\dfrac{4(x-3)}{x+3}",
    "b_rat4": r"\dfrac{x-3}{4(x+2)}",
    "b_sub":  r"\dfrac{a}{a-1}-\dfrac{a}{a+1}",
    "b_sub1": r"0",
    "b_sub2": r"\dfrac{2a}{a^{2}+1}",
    "b_sub3": r"\dfrac{2a}{a^{2}-1}",
    "b_sub4": r"\dfrac{2a^{2}}{a^{2}-1}",
    "b_cf":   r"\dfrac{\ \dfrac{x}{6}\ }{\ \dfrac{x-3}{5}\ }",
    "b_cf1":  r"\dfrac{6(x-3)}{5x}",
    "b_cf2":  r"\dfrac{5x}{6x-18}",
    "b_cf3":  r"\dfrac{x(x-3)}{30}",
    "b_cf4":  r"\dfrac{x}{6x-18}",
    "b_und":  r"\dfrac{x-3}{x^{2}+4x-21}",
    "b_und1": r"x={-7}",
    "b_und2": r"x=3",
    "b_und3": r"x={-3}\ \ \text{and}\ \ x=7",
    "b_und4": r"x=3\ \ \text{and}\ \ x={-7}",
    "b_lcm":  r"20x^{3}y^{5}\qquad\text{and}\qquad 4x^{2}y^{6}",
    "b_lcm1": r"4x^{2}y^{5}",
    "b_lcm2": r"80x^{3}y^{6}",
    "b_lcm3": r"20x^{3}y^{6}",
    "b_lcm4": r"20x^{5}y^{11}",

    # --------------------------------- session 8, linear equations and inequalities
    "b_lin":   r"\dfrac{3x+4}{5}=\dfrac{2x-1}{3}",
    "b_ineq":  r"{-4x}+3>19",
    "b_ineq1": r"x>{-4}",
    "b_ineq2": r"x<{-4}",
    "b_ineq3": r"x>{-5.5}",
    "b_ineq4": r"x<4",
    "b_int":   r"{-2}\leq x<5",
    "b_int1":  r"[-2,\ 5]",
    "b_int2":  r"(-2,\ 5)",
    "b_int3":  r"[-2,\ 5)",
    "b_int4":  r"(-2,\ 5]",
    "b_sys":   r"\begin{cases}y\leq 2x-3\\[2pt] y\geq x+4\end{cases}",
    "b_sys1":  r"(0,\ 5)",
    "b_sys2":  r"(8,\ 10)",
    "b_sys3":  r"(5,\ 2)",
    "b_sys4":  r"(10,\ 15)",
    "b_vert":  r"\begin{cases}y\geq {-3x}+12\\[2pt] y\leq 9\\[2pt] x\leq 4\end{cases}",
    "b_vert1": r"(1,\ 9)",
    "b_vert2": r"(3,\ 9)",
    "b_vert3": r"(9,\ 1)",
    "b_vert4": r"({-1},\ 9)",

    # ----------------------------------------------- session 9, absolute value
    "b_avn":  r"\lvert 2x-6\rvert={-4}",
    "b_avi":  r"\lvert x-4\rvert<3",
    "b_avi1": r"x<7",
    "b_avi2": r"x<1\ \ \text{or}\ \ x>7",
    "b_avi3": r"1<x<7",
    "b_avi4": r"{-7}<x<{-1}",
}


def render(out_dir="math_saat_doc", dpi=300):
    """Render into the existing part A folder and merge the two indexes."""
    idx_path = os.path.join(out_dir, "_index.json")
    idx = json.load(open(idx_path)) if os.path.exists(idx_path) else {}
    tmp = tempfile.mkdtemp()
    keys = list(E)
    doc = [r"\documentclass[12pt]{article}",
           r"\usepackage[active,tightpage]{preview}",
           r"\usepackage{amsmath,amssymb}",
           r"\usepackage[T1]{fontenc}",
           r"\usepackage[dvipsnames]{xcolor}",
           r"\setlength\PreviewBorder{1.5pt}",
           r"\definecolor{ink}{HTML}{%s}" % INK,
           r"\begin{document}"]
    for k in keys:
        doc.append(r"\begin{preview}$\color{ink}\displaystyle %s$\end{preview}" % E[k])
    doc.append(r"\end{document}")
    tex = os.path.join(tmp, "saatb.tex")
    open(tex, "w").write("\n".join(doc))
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-output-directory", tmp, tex], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-3000:])
        raise SystemExit("pdflatex failed")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(tmp, "saatb.pdf"), os.path.join(tmp, "q")], check=True)
    pages = sorted(f for f in os.listdir(tmp) if f.startswith("q-") and f.endswith(".png"))
    assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} expressions"
    for k, p in zip(keys, pages):
        im = Image.open(os.path.join(tmp, p)).convert("RGBA")
        dst = os.path.join(out_dir, k + ".png")
        im.save(dst)
        idx[k] = {"file": dst, "win": im.width / dpi, "hin": im.height / dpi,
                  "aspect": im.width / im.height}
    json.dump(idx, open(idx_path, "w"), indent=1)
    print(f"{len(keys)} part-B expressions added; index now holds {len(idx)}")


if __name__ == "__main__":
    render()
