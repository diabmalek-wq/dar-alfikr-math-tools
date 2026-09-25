"""LaTeX for part C of the simulated SAAT bank — Unit 2, sessions 10-18.

Rendered into the SAME index the earlier parts use, so the bank builds from one
maths folder. Run make_math_saat.py and make_math_saat_b.py first.
"""
import json, os, subprocess, tempfile
from PIL import Image

INK = "222E2D"

E = {
    # ------------------------------------------------ session 10 and 11
    "c_elim":  r"\begin{cases}2x+3y=12\\[2pt]4x-3y=6\end{cases}",
    "c_nosol": r"\begin{cases}2x-3y=6\\[2pt]4x-6y=18\end{cases}",
    "c_feas":  r"\begin{cases}x\geq 0,\ \ y\geq 0\\[2pt]x+y\leq 10\\[2pt]2x+y\leq 14\end{cases}",
    "c_feas1": r"({-1},\ 3)",
    "c_feas2": r"(4,\ 6)",
    "c_feas3": r"(6,\ 5)",
    "c_feas4": r"(8,\ 0)",

    # ------------------------------------------------------- session 12
    "c_fac":  r"x^{2}-7x+12=0",
    "c_fac1": r"x=3\ \ \text{or}\ \ x=4",
    "c_fac2": r"x={-3}\ \ \text{or}\ \ x={-4}",
    "c_fac3": r"x=2\ \ \text{or}\ \ x=6",
    "c_fac4": r"x=1\ \ \text{or}\ \ x=12",
    "c_frm1": r"x^{2}+3x-10=0",
    "c_frm2": r"x^{2}-3x-10=0",
    "c_frm3": r"x^{2}-3x+10=0",
    "c_frm4": r"x^{2}+7x+10=0",
    "c_clr":  r"x+\dfrac{6}{x}=5",
    "c_clr1": r"x={-2}\ \ \text{or}\ \ x={-3}",
    "c_clr2": r"x=1\ \ \text{or}\ \ x=6",
    "c_clr3": r"x=2\ \ \text{or}\ \ x=3",
    "c_clr4": r"x=5\ \ \text{or}\ \ x=6",
    "c_zer":  r"y=(2x-6)(x+4)",
    "c_zer1": r"x={-3},\ \ x=4",
    "c_zer2": r"x=6,\ \ x={-4}",
    "c_zer3": r"x=2,\ \ x={-4}",
    "c_zer4": r"x=3,\ \ x={-4}",

    # ------------------------------------------------------- session 13
    "c_cts":  r"y=x^{2}-6x+11",
    "c_cts1": r"y=(x-3)^{2}+2",
    "c_cts2": r"y=(x+3)^{2}+2",
    "c_cts3": r"y=(x-3)^{2}-2",
    "c_cts4": r"y=(x-6)^{2}+11",
    "c_cpx":  r"x^{2}-2x+5=0",
    "c_cpx1": r"x={-1}\pm 2i",
    "c_cpx2": r"x=1\pm 2i",
    "c_cpx3": r"x=1\pm 4i",
    "c_cpx4": r"x=2\pm 4i",
    "c_vtx":  r"y=2(x+4)^{2}-7",
    "c_vtx1": r"(4,\ {-7})",
    "c_vtx2": r"({-4},\ 7)",
    "c_vtx3": r"({-4},\ {-7})",
    "c_vtx4": r"(4,\ 7)",
    "c_recc": r"f(x)=x^{2}+8x+c",

    # ------------------------------------------------------- session 14
    "c_disc":  r"2x^{2}+3x+5=0",
    "c_disc2": r"x^{2}-6x+4=0",
    "c_eqr":   r"x^{2}+kx+9=0",
    "c_eqr1":  r"k=\pm 3",
    "c_eqr2":  r"k=\pm 9",
    "c_eqr3":  r"k=6",
    "c_eqr4":  r"k=\pm 6",

    # ------------------------------------------------------- session 15
    "c_axis":  r"y=x^{2}-4x-5",
    "c_axis1": r"x={-2}",
    "c_axis2": r"x=4",
    "c_axis3": r"x=2",
    "c_axis4": r"y=2",
    "c_max":   r"y={-x^{2}}+6x-5",
    "c_int1":  r"y=x^{2}+2x-3",
    "c_int2":  r"y=x^{2}-2x-3",
    "c_int3":  r"y=x^{2}+2x+3",
    "c_int4":  r"y=x^{2}-4x+3",

    # ------------------------------------------------------- session 16
    "c_syn":  r"x^{3}-4x^{2}+5x-2",
    "c_syn1": r"x^{2}-6x+17",
    "c_syn2": r"x^{2}-2x+1",
    "c_syn3": r"x^{2}-2x-1",
    "c_syn4": r"x^{2}+2x+1",
    "c_rem":  r"f(x)=x^{3}+2x^{2}-5",
    "c_fct":  r"f(x)=x^{3}-4x^{2}+x+6",
    "c_fct1": r"x-4",
    "c_fct2": r"x+2",
    "c_fct3": r"x-2",
    "c_fct4": r"x-6",
    "c_par":  r"f(x)=x^{3}+kx+3",
    "c_cnj1": r"{-3}-i",
    "c_cnj2": r"3+i",
    "c_cnj3": r"{-3}+i",
    "c_cnj4": r"1-3i",

    # ------------------------------------------------------- session 17
    "c_rateq": r"\dfrac{x}{x-3}=\dfrac{3}{x-3}+2",
    "c_prop":  r"\dfrac{x+2}{4}=\dfrac{3x-4}{8}",

    # ------------------------------------------------------- session 18
    "c_rad1": r"\sqrt{3x+4}=5",
    "c_rad2": r"\sqrt{2x-1}=\sqrt{x+5}",
    "c_rad3": r"\sqrt{x+7}=x-5",
    "c_rad4": r"\sqrt{x-3}<4",
    "c_rad4o1": r"3\leq x<19",
    "c_rad4o2": r"x<19",
    "c_rad4o3": r"x\geq 3",
    "c_rad4o4": r"3<x<19",
}


def render(out_dir="math_saat_doc", dpi=300):
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
    tex = os.path.join(tmp, "saatc.tex")
    open(tex, "w").write("\n".join(doc))
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-output-directory", tmp, tex], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-3000:])
        raise SystemExit("pdflatex failed")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(tmp, "saatc.pdf"), os.path.join(tmp, "r")], check=True)
    pages = sorted(f for f in os.listdir(tmp) if f.startswith("r-") and f.endswith(".png"))
    assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} expressions"
    for k, p in zip(keys, pages):
        im = Image.open(os.path.join(tmp, p)).convert("RGBA")
        dst = os.path.join(out_dir, k + ".png")
        im.save(dst)
        idx[k] = {"file": dst, "win": im.width / dpi, "hin": im.height / dpi,
                  "aspect": im.width / im.height}
    json.dump(idx, open(idx_path, "w"), indent=1)
    print(f"{len(keys)} part-C expressions added; index now holds {len(idx)}")


if __name__ == "__main__":
    render()
