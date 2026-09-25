"""LaTeX for part J of the SAAT booklet — the three recalled summer papers.

Rendered into the SAME index the earlier parts use.
"""
import json, os, subprocess, tempfile
from PIL import Image

INK = "222E2D"

FR = lambda a, b: r"\dfrac{%s}{%s}" % (a, b)

E = {
    # ----------------------------------------------------- force components
    "jx_f1": r"60\sqrt{3}\ \mathrm{N}",
    "jx_f2": r"60\ \mathrm{N}",
    "jx_f3": r"120\ \mathrm{N}",
    "jx_f4": r"60\sqrt{2}\ \mathrm{N}",

    # ------------------------------------------------------ polar to a circle
    "jx_pol": r"r=4\cos\theta+6\sin\theta",
    "jx_pc1": r"\left(x-2\right)^{2}+\left(y-3\right)^{2}=13",
    "jx_pc2": r"\left(x-3\right)^{2}+\left(y-2\right)^{2}=13",
    "jx_pc3": r"\left(x+2\right)^{2}+\left(y+3\right)^{2}=13",
    "jx_pc4": r"\left(x-2\right)^{2}+\left(y-3\right)^{2}=\sqrt{13}",

    # --------------------------------------------------------- stacked squares
    "jx_sq1": r"13",
    "jx_sq2": r"12",
    "jx_sq3": r"17",
    "jx_sq4": r"\sqrt{74}",

    # ---------------------------------------------- counting and probability
    "jx_hg1": FR("15", "28"),
    "jx_hg2": FR("5", "28"),
    "jx_hg3": FR("13", "56"),
    "jx_hg4": FR("5", "8"),
    "jx_d51": FR("1", "4"),
    "jx_d52": FR("1", "5"),
    "jx_d53": FR("1", "24"),
    "jx_d54": FR("1", "6"),
    "jx_cir1": FR("1", "720"),
    "jx_cir2": FR("1", "5040"),
    "jx_cir3": FR("1", "7"),
    "jx_cir4": FR("1", "49"),

    # ------------------------------------------------------ structural algebra
    "jx_hole": FR(r"x^{2}-9", r"\left(x-3\right)\left(x+5\right)"),
    "jx_neg": FR("a", "6") + r"\cdot" + FR("3-x", "x-3"),
    "jx_ng1": r"{-\dfrac{a}{6}}",
    "jx_ng2": FR("a", "6"),
    "jx_ng3": FR(r"a\left(3-x\right)", r"6\left(x-3\right)"),
    "jx_ng4": r"{-\dfrac{a}{2}}",

    # ----------------------------------------------------- structural calculus
    "jx_cont": (r"f(x)=\begin{cases} x^{2}+a & x<2 \\[2pt] 3x-1 & x\geq 2"
                r"\end{cases}"),
    "jx_semi": r"\int_{-3}^{3}\sqrt{9-x^{2}}\,dx",
    "jx_si1": FR(r"9\pi", "2"),
    "jx_si2": r"9\pi",
    "jx_si3": r"3\pi",
    "jx_si4": r"6\pi",

    # -------------------------------------------------------- trigonometry
    "jx_s751": FR(r"\sqrt{6}+\sqrt{2}", "4"),
    "jx_s752": FR(r"\sqrt{6}-\sqrt{2}", "4"),
    "jx_s753": FR(r"\sqrt{2}+1", "4"),
    "jx_s754": FR(r"\sqrt{6}+\sqrt{2}", "2"),
    "jx_coll": r"\cos 70^{\circ}\cos 20^{\circ}-\sin 70^{\circ}\sin 20^{\circ}",
    "jx_cl1": r"0",
    "jx_cl2": r"1",
    "jx_cl3": FR("1", "2"),
    "jx_cl4": FR(r"\sqrt{3}", "2"),
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
    tex = os.path.join(tmp, "saatjx.tex")
    open(tex, "w").write("\n".join(doc))
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-output-directory", tmp, tex], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-3000:])
        raise SystemExit("pdflatex failed")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(tmp, "saatjx.pdf"), os.path.join(tmp, "r")], check=True)
    pages = sorted(f for f in os.listdir(tmp) if f.startswith("r-") and f.endswith(".png"))
    assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} expressions"
    for k, p in zip(keys, pages):
        im = Image.open(os.path.join(tmp, p)).convert("RGBA")
        dst = os.path.join(out_dir, k + ".png")
        im.save(dst)
        idx[k] = {"file": dst, "win": im.width / dpi, "hin": im.height / dpi,
                  "aspect": im.width / im.height}
    json.dump(idx, open(idx_path, "w"), indent=1)
    print(f"{len(keys)} part-J expressions added; index now holds {len(idx)}")


if __name__ == "__main__":
    render()
