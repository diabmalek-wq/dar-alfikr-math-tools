"""LaTeX for part H of the SAAT booklet — the skills taken from the Tahsili
recall album.

Rendered into the SAME index the earlier parts use.
"""
import json, os, subprocess, tempfile
from PIL import Image

INK = "222E2D"

E = {
    # -------------------------------------------------- vectors and modelling
    "h_cp1": r"\sqrt{230}",
    "h_cp2": r"\dfrac{\sqrt{230}}{2}",
    "h_cp3": r"8",
    "h_cp4": r"\sqrt{294}",
    "h_bx1": r"\left(24-2x\right)\left(18-2x\right)",
    "h_bx2": r"\left(24-4x\right)\left(18-4x\right)",
    "h_bx3": r"\left(24-x\right)\left(18-x\right)",
    "h_bx4": r"432-4x^{2}",

    # ----------------------------------------------- a piecewise graph read off
    "h_dm1": r"\left({-\infty},\ 1\right)\cup\left[3,\ 6\right]",
    "h_dm2": r"\left({-\infty},\ 1\right]\cup\left[3,\ 6\right]",
    "h_dm3": r"\left({-\infty},\ 6\right]",
    "h_dm4": r"\left({-\infty},\ {-1}\right)\cup\left\{2\right\}",
    "h_rg1": r"\left({-\infty},\ {-1}\right)\cup\left\{2\right\}",
    "h_rg2": r"\left({-\infty},\ {-1}\right]\cup\left\{2\right\}",
    "h_rg3": r"\left({-\infty},\ 2\right]",
    "h_rg4": r"\left({-\infty},\ 1\right)\cup\left[3,\ 6\right]",

    # ------------------------------------------------------------ trigonometry
    "h_sa": r"\sqrt{2}\,\sin\left(x+45^{\circ}\right)",
    "h_sa1": r"\sin x+\cos x",
    "h_sa2": r"\sqrt{2}\left(\sin x+\cos x\right)",
    "h_sa3": r"\sin x-\cos x",
    "h_sa4": r"\sqrt{2}\,\sin x+\cos x",
    "h_q31": r"{-\dfrac{\sqrt{3}}{2}}",
    "h_q32": r"\dfrac{\sqrt{3}}{2}",
    "h_q33": r"{-\dfrac{1}{2}}",
    "h_q34": r"{-\dfrac{\sqrt{2}}{2}}",
    "h_ct1": r"\dfrac{\sqrt{3}}{2}",
    "h_ct2": r"{-\dfrac{\sqrt{3}}{2}}",
    "h_ct3": r"\dfrac{1}{2}",
    "h_ct4": r"\dfrac{\sqrt{2}}{2}",
    "h_cs1": r"\dfrac{2\sqrt{6}}{3}",
    "h_cs2": r"\dfrac{\sqrt{6}}{4}",
    "h_cs3": r"\dfrac{3}{2\sqrt{6}}",
    "h_cs4": r"\dfrac{2}{3}",

    # ------------------------------------------------- inverse and coordinate
    "h_iv1": r"\dfrac{3x+1}{x-2}",
    "h_iv2": r"\dfrac{x-3}{2x+1}",
    "h_iv3": r"\dfrac{3x-1}{x+2}",
    "h_iv4": r"\dfrac{3x+1}{x+2}",
    "h_sl1": r"{-3}",
    "h_sl2": r"3",
    "h_sl3": r"{-\dfrac{1}{3}}",
    "h_sl4": r"{-9}",

    # ------------------------------------------------------------- calculus
    "h_li": r"\lim_{x\to\infty}\dfrac{3x\lvert x\rvert+5}{x^{2}-4x}",
    "h_ul": r"\int_{1}^{n}3x^{2}\,dx",
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
    tex = os.path.join(tmp, "saath.tex")
    open(tex, "w").write("\n".join(doc))
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-output-directory", tmp, tex], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-3000:])
        raise SystemExit("pdflatex failed")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(tmp, "saath.pdf"), os.path.join(tmp, "r")], check=True)
    pages = sorted(f for f in os.listdir(tmp) if f.startswith("r-") and f.endswith(".png"))
    assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} expressions"
    for k, p in zip(keys, pages):
        im = Image.open(os.path.join(tmp, p)).convert("RGBA")
        dst = os.path.join(out_dir, k + ".png")
        im.save(dst)
        idx[k] = {"file": dst, "win": im.width / dpi, "hin": im.height / dpi,
                  "aspect": im.width / im.height}
    json.dump(idx, open(idx_path, "w"), indent=1)
    print(f"{len(keys)} part-H expressions added; index now holds {len(idx)}")


if __name__ == "__main__":
    render()
