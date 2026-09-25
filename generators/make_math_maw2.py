"""LaTeX for MAWHIBA Grade 9 · Unit 1 · Activity 2 — Rectangular Areas.

Rendered into the SAME index Activity 1 uses (maw_math/_index.json).
Nothing on the sheet is typed as plain-text mathematics.
"""
import json, os, subprocess, tempfile
from PIL import Image

INK = "222E2D"

E = {
    # ---- the worked route on the front page
    "n2_whole":  r"12\times 7-3x",
    "n2_strips": r"12\left(7-3\right)+3\left(12-x\right)",
    "n2_simp":   r"84-3x",

    # ---- the identity of task 4
    "n2_id":     r"\left(a+b\right)\left(c+d\right)=ac+ad+bc+bd",
    "n2_2738":   r"27\times 38=\left(20+7\right)\left(30+8\right)",
    "n2_2738b":  r"600+160+210+56=1026",

    # ---- task 5
    "n2_diff":   r"a^{2}-b^{2}",
    "n2_factor": r"a^{2}-b^{2}=\left(a-b\right)\left(a+b\right)",
    "n2_pieces": r"a\left(a-b\right)+b\left(a-b\right)",

    # ---- the key
    "k2_f1a": r"12\times 7-3x=84-3x",
    "k2_f1b": r"12\left(7-3\right)+3\left(12-x\right)=48+36-3x=84-3x",
    "k2_f1c": r"x\left(7-3\right)+\left(12-x\right)7=4x+84-7x=84-3x",
    "k2_f2a": r"8\times 8-2p=64-2p",
    "k2_f2b": r"8\left(8-p\right)+\left(8-2\right)p=64-8p+6p=64-2p",
    "k2_f3a": r"12m-7\times 1=12m-7",
    "k2_f3b": r"12\left(m-1\right)+\left(3+2\right)1=12m-12+5=12m-7",
    "k2_f4a": r"10p-6\times 2=10p-12",
    "k2_f4b": r"2p+qp+2\left(2+r\right),\quad q=6,\ p=8+r\ \Longrightarrow\ 10p-12",
    "k2_f5a": r"a\left(a-b\right)+b\left(a-b\right)=\left(a-b\right)\left(a+b\right)",
    "k2_f5b": r"\left(a-b\right)\left(a+b\right)=a^{2}+ab-ab-b^{2}=a^{2}-b^{2}",
}


# The "Done when..." strip is a dark navy band, and ink-coloured mathematics
# disappears on it. This one expression is rendered again in white.
WHITE = {"n2_factor_w": E["n2_factor"]}


def render(out_dir="maw_math", dpi=300, expressions=None, ink=INK):
    E_ = expressions if expressions is not None else E
    idx_path = os.path.join(out_dir, "_index.json")
    idx = json.load(open(idx_path)) if os.path.exists(idx_path) else {}
    tmp = tempfile.mkdtemp()
    keys = list(E_)
    doc = [r"\documentclass[12pt]{article}",
           r"\usepackage[active,tightpage]{preview}",
           r"\usepackage{amsmath,amssymb}",
           r"\usepackage[T1]{fontenc}",
           r"\usepackage[dvipsnames]{xcolor}",
           r"\setlength\PreviewBorder{1.5pt}",
           r"\definecolor{ink}{HTML}{%s}" % ink,
           r"\begin{document}"]
    for k in keys:
        doc.append(r"\begin{preview}$\color{ink}\displaystyle %s$\end{preview}" % E_[k])
    doc.append(r"\end{document}")
    tex = os.path.join(tmp, "maw2.tex")
    open(tex, "w").write("\n".join(doc))
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-output-directory", tmp, tex], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-3000:])
        raise SystemExit("pdflatex failed")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(tmp, "maw2.pdf"), os.path.join(tmp, "m")], check=True)
    pages = sorted(f for f in os.listdir(tmp) if f.startswith("m-") and f.endswith(".png"))
    assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} expressions"
    for k, p in zip(keys, pages):
        im = Image.open(os.path.join(tmp, p)).convert("RGBA")
        dst = os.path.join(out_dir, k + ".png")
        im.save(dst)
        idx[k] = {"file": dst, "win": im.width / dpi, "hin": im.height / dpi,
                  "aspect": im.width / im.height}
    json.dump(idx, open(idx_path, "w"), indent=1)
    print(f"{len(keys)} Activity 2 expressions added; index now holds {len(idx)}")


if __name__ == "__main__":
    render()
    render(expressions=WHITE, ink="FFFFFF")
