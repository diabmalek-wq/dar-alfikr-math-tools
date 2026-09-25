"""LaTeX for the WEEK 4 pre-session skills sheets.

Rendered into the SAME index the Week 2 sheets use (math_pre/_index.json), so
presession.js can pick any key from either week.

THE WEEK 2 DEFECT, not repeated here: a page-1 reminder must never be the same
instance as a page-2 warm-up, or the answer is printed on the previous page.
Reminder keys are p4_*, warm-up keys are q4_*, and every q4_ uses different
numbers from every p4_.

    python3 make_math_pre_w4.py
"""
import json, os, subprocess, tempfile
from PIL import Image

INK = "222E2D"

E = {
    # =============================================== GRADE 10 · SAT & GAT
    # anchor: T1 L4 Arithmetic Sequences and Series
    "p4_seq":   r"7,\ 11,\ 15,\ 19,\ 23,\ \ldots\qquad d=11-7=4",
    "p4_nth":   r"a_{n}=a_{1}+(n-1)d",
    "p4_sum":   r"S_{n}=\dfrac{n}{2}\left(a_{1}+a_{n}\right)",
    "p4_slope": r"m=\dfrac{y_{2}-y_{1}}{x_{2}-x_{1}}",
    "p4_count": r"n=\dfrac{\text{last}-\text{first}}{d}+1",
    "p4_lin":   r"a_{n}=dn+\left(a_{1}-d\right)",

    "q4_g10a": r"3,\ 10,\ 17,\ 24,\ \ldots\qquad d=\underline{\quad}",
    "q4_g10b": r"a_{1}=5,\ d=6.\qquad a_{12}=\underline{\quad}",
    "q4_g10c": r"9,\ 14,\ 19,\ \ldots,\ 79.\qquad n=\underline{\quad}",
    "q4_g10d": r"S_{20}\ \text{of}\ \ 2,\ 5,\ 8,\ \ldots=\underline{\quad}",
    "q4_g10e": r"a_{n}=4n+3.\qquad d=\underline{\quad}",

    # =============================================== GRADE 11 · SAAT & SAT
    # anchor: T5 L5-6 Inverse Functions
    "p4_comp":  r"\left(f\circ g\right)(x)=f\!\left(g(x)\right)",
    "p4_inv":   r"y=3x-8\ \Longrightarrow\ x=3y-8\ \Longrightarrow\ y=\dfrac{x+8}{3}",
    "p4_check": r"f\!\left(f^{-1}(x)\right)=x\qquad\text{and}\qquad f^{-1}\!\left(f(x)\right)=x",
    "p4_rex":   r"x^{\frac{1}{n}}=\sqrt[n]{x}\qquad x^{\frac{m}{n}}=\sqrt[n]{x^{m}}",
    "p4_sqrt":  r"\sqrt{x^{2}}=\left\lvert x\right\rvert\quad\text{not}\quad x",
    "p4_dom":   r"f:\ \left[0,\infty\right)\to\left[0,\infty\right)\ \Longrightarrow\ f^{-1}:\ \left[0,\infty\right)\to\left[0,\infty\right)",

    "q4_g11a": r"f(x)=5x+2.\qquad f^{-1}(x)=\underline{\quad}",
    "q4_g11b": r"f(x)=\dfrac{x-7}{4}.\qquad f^{-1}(x)=\underline{\quad}",
    "q4_g11c": r"f(x)=x^{3}+1.\qquad f^{-1}(2)=\underline{\quad}",
    "q4_g11d": r"g(x)=\sqrt{x-9}.\qquad \text{domain of }g^{-1}=\underline{\quad}",
    "q4_g11e": r"27^{\frac{2}{3}}=\underline{\quad}",

    # =============================================== GRADE 9 · MAWHIBA
    # Unit 1 Linear equations, Activity 3 Number Pyramids
    "p4_pyr":   (r"\begin{array}{ccccc}"
                 r" & & 14 & & \\[4pt]"
                 r" & 6 & & 8 & \\[4pt]"
                 r"2 & & 4 & & 4"
                 r"\end{array}"),
    "p4_pyralg": (r"\begin{array}{ccccc}"
                  r" & & x+2y+z & & \\[4pt]"
                  r" & x+y & & y+z & \\[4pt]"
                  r"x & & y & & z"
                  r"\end{array}"),
    "p4_like":  r"3n+5+2n-1=5n+4",
    "p4_solve": r"4x+7=31\ \Longrightarrow\ 4x=24\ \Longrightarrow\ x=6",

    "q4_g9a": (r"\begin{array}{ccccc}"
               r" & & ? & & \\[4pt]"
               r" & ? & & ? & \\[4pt]"
               r"5 & & 3 & & 9"
               r"\end{array}"),
    "q4_g9b": (r"\begin{array}{ccccc}"
               r" & & 30 & & \\[4pt]"
               r" & ? & & 17 & \\[4pt]"
               r"4 & & ? & & ?"
               r"\end{array}"),
    "q4_g9c": r"\text{Bottom row } n,\ n,\ n.\ \text{Top} =\underline{\quad}",
    "q4_g9d": r"\text{Bottom row } a,\ b,\ c.\ \text{Top} =\underline{\quad}",
    "q4_g9e": r"\text{Bottom } 2,\ x,\ 6.\ \text{Top} =26.\ x=\underline{\quad}",
}


def render(out_dir="math_pre", dpi=300):
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
           r"\renewcommand{\arraystretch}{1.25}",
           r"\begin{document}"]
    for k in keys:
        doc.append(r"\begin{preview}$\color{ink}\displaystyle %s$\end{preview}" % E[k])
    doc.append(r"\end{document}")
    tex = os.path.join(tmp, "prew4.tex")
    open(tex, "w").write("\n".join(doc))
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-output-directory", tmp, tex], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-3000:])
        raise SystemExit("pdflatex failed")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(tmp, "prew4.pdf"), os.path.join(tmp, "p")], check=True)
    pages = sorted(f for f in os.listdir(tmp) if f.startswith("p-") and f.endswith(".png"))
    assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} expressions"
    for k, p in zip(keys, pages):
        im = Image.open(os.path.join(tmp, p)).convert("RGBA")
        dst = os.path.join(out_dir, k + ".png")
        im.save(dst)
        src = E[k]
        lines = 1 + src.count(r"\\")
        if "dfrac" in src or r"\frac" in src:
            lines = max(lines, 2)
        if "begin{array}" in src:
            lines = max(lines, 3)
        idx[k] = {"file": dst, "win": im.width / dpi, "hin": im.height / dpi,
                  "aspect": im.width / im.height, "lines": lines}
    json.dump(idx, open(idx_path, "w"), indent=1)
    print(f"{len(keys)} Week-4 expressions added; index now holds {len(idx)}")


if __name__ == "__main__":
    render()
