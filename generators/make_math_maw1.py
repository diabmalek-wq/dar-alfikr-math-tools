"""LaTeX for the Mawhiba Grade 9 · Unit 1 · Activity 1 worksheet.

Same pipeline as every other sheet: pdflatex + preview, Computer Modern,
transparent PNG. Nothing on the sheet is typed as plain-text mathematics.
"""
import json, os, shutil, subprocess, tempfile
from PIL import Image

INK = "222E2D"

E = {
    "m_stmt":   r"a+b=ab",
    "m_rearr":  r"b(a-1)=a",
    "m_gen":    r"b=\dfrac{a}{a-1}\ ,\qquad a\neq 1",
    "m_a1":     r"a=1:\quad 1+b=b\ \Longrightarrow\ 1=0",
    "m_a3":     r"a=3:\quad 3+b=3b",
    "m_a4":     r"a=4:\quad 4+b=4b",
    "m_int":    r"(0,\,0)\quad\text{and}\quad (2,\,2)",

    # the twelve statements
    "s_A": r"a+7=20",
    "s_B": r"m+5=m+13",
    "s_C": r"3k+6=6+3k",
    "s_D": r"4p-6=6-4p",
    "s_E": r"6+2x=4x",
    "s_F": r"r+8=s+8",
    "s_G": r"6q>5+q",
    "s_H": r"b+4<17",
    "s_I": r"3(y+4)=3y+12",
    "s_J": r"3(7+t)=21+3t",
    "s_K": r"y^{2}>9",
    "s_L": r"y^{2}=4y",

    # identity notation, shown once as the worked example
    "m_idsym":  r"3k+6\equiv 6+3k",
    "m_ident":  r"\equiv\ \text{means true for EVERY value}",

    # the investigate tasks
    "m_ch2":    r"x^{2}+4\leq 0",
    "m_ch3":    r"x,\ y\neq 0",

    # key
    "k_gen":    r"b=\dfrac{a}{a-1}",
    "k_a3":     r"a=3\ \Rightarrow\ b=\dfrac{3}{2}\qquad a=4\ \Rightarrow\ b=\dfrac{4}{3}",
    "k_C": r"3k+6\equiv 6+3k",
    "k_I": r"3(y+4)\equiv 3y+12",
    "k_J": r"3(7+t)\equiv 21+3t",
    "k_D": r"8p=12\ \Rightarrow\ p=1.5",
    "k_E": r"2x=6\ \Rightarrow\ x=3",
    "k_G": r"5q>5\ \Rightarrow\ q>1",
    "k_H": r"b<13",
    "k_K": r"y>3\ \ \text{or}\ \ y<{-3}",
    "k_L": r"y(y-4)=0\ \Rightarrow\ y=0\ \text{or}\ y=4",
    "k_B": r"5=13\ \ \text{is false for every}\ m",
    "k_ch2": r"x^{2}\geq 0\ \Rightarrow\ x^{2}+4\geq 4>0",
    "k_ch3": r"(x+y)^{2}-(x-y)^{2}\equiv 4xy",
}


def render(out_dir="maw_math", dpi=300):
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
           r"\begin{document}"]
    for k in keys:
        doc.append(r"\begin{preview}$\color{ink}\displaystyle %s$\end{preview}" % E[k])
    doc.append(r"\end{document}")
    tex = os.path.join(tmp, "maw.tex")
    open(tex, "w").write("\n".join(doc))
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-output-directory", tmp, tex], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-2500:]); raise SystemExit("pdflatex failed")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(tmp, "maw.pdf"), os.path.join(tmp, "p")], check=True)
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
    print(f"{len(idx)} expressions -> {out_dir} @ {dpi} dpi")


if __name__ == "__main__":
    render()
