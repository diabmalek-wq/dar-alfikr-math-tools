"""LaTeX for part K of the SAAT booklet — the revision compilation.

Rendered into the SAME index the earlier parts use.
"""
import json, os, subprocess, tempfile
from PIL import Image

INK = "222E2D"

FR = lambda a, b: r"\dfrac{%s}{%s}" % (a, b)
PT = lambda x, y: r"\left(%s,\ %s\right)" % (x, y)

E = {
    # ------------------------------------------------------ the floor function
    "kx_floor": r"f(x)=\left\lfloor 0.4x\right\rfloor+2",

    # --------------------------------------------- angles, wheels and vectors
    "kx_ad1": FR(r"4\pi", "3"),
    "kx_ad2": FR(r"2\pi", "3"),
    "kx_ad3": FR(r"3\pi", "2"),
    "kx_ad4": r"12\pi",
    "kx_w1": r"r=30\sin\theta",
    "kx_w2": r"r=15\sin\theta",
    "kx_w3": r"r=30\cos\theta",
    "kx_w4": r"r=15\cos\theta",
    "kx_dl1": PT("3", "{-2}"),
    "kx_dl2": PT("{-3}", "2"),
    "kx_dl3": PT("3", "2"),
    "kx_dl4": PT("{-3}", "{-2}"),

    # ------------------------------------------ what the domain quietly kills
    "kx_div": (FR(r"x^{2}+5x-14", "x-2") + r"\div" + FR(r"x^{2}-9", "x+3")),

    # ---------------------------------------------------------- compositions
    "kx_cp1": r"7",
    "kx_cp2": r"4x^{2}-3x",
    "kx_cp3": r"28x^{2}-21x",
    "kx_cp4": r"175",

    # -------------------------------------------------------------- calculus
    "kx_rad": r"f(x)=\dfrac{1}{3\sqrt[4]{x^{-8}}}",
    "kx_rd1": FR("2x", "3"),
    "kx_rd2": FR("2", r"3x^{3}"),
    "kx_rd3": FR("1", r"3x^{2}"),
    "kx_rd4": FR(r"x^{2}", "3"),
    "kx_lim": r"\lim_{x\to 0}\dfrac{x+\pi}{\cos\left(x+\pi\right)}",
    "kx_lm1": r"{-\pi}",
    "kx_lm2": r"\pi",
    "kx_lm3": r"0",
    "kx_lm4": r"{-1}",
    "kx_disc": (r"f(x)=\begin{cases} 2x & x\geq 3 \\[2pt] x^{2}-5 & x<3"
                r"\end{cases}"),
    "kx_abs": r"\int_{-2}^{4}k\left\lvert x-1\right\rvert\,dx",

    # ------------------------------------------------- algebra, seen properly
    "kx_dos": FR("x-9", r"\sqrt{x}-3"),
    "kx_ds1": r"\sqrt{x}+3",
    "kx_ds2": r"\sqrt{x}-3",
    "kx_ds3": r"x+3",
    "kx_ds4": FR("1", r"\sqrt{x}+3"),
    "kx_exp": r"4^{\,x-1}+6=70",
    "kx_ser": r"9+18x+36x^{2}+72x^{3}+\cdots",
    "kx_sr1": r"\left\lvert x\right\rvert<\dfrac{1}{2}",
    "kx_sr2": r"\left\lvert x\right\rvert<1",
    "kx_sr3": r"\left\lvert x\right\rvert<2",
    "kx_sr4": r"\left\lvert x\right\rvert<\dfrac{1}{9}",
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
    tex = os.path.join(tmp, "saatk.tex")
    open(tex, "w").write("\n".join(doc))
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-output-directory", tmp, tex], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-3000:])
        raise SystemExit("pdflatex failed")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(tmp, "saatk.pdf"), os.path.join(tmp, "r")], check=True)
    pages = sorted(f for f in os.listdir(tmp) if f.startswith("r-") and f.endswith(".png"))
    assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} expressions"
    for k, p in zip(keys, pages):
        im = Image.open(os.path.join(tmp, p)).convert("RGBA")
        dst = os.path.join(out_dir, k + ".png")
        im.save(dst)
        idx[k] = {"file": dst, "win": im.width / dpi, "hin": im.height / dpi,
                  "aspect": im.width / im.height}
    json.dump(idx, open(idx_path, "w"), indent=1)
    print(f"{len(keys)} part-K expressions added; index now holds {len(idx)}")


if __name__ == "__main__":
    render()
