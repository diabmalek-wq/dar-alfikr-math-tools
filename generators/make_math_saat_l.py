"""LaTeX for part L of the SAAT booklet — three items from the 17 Sep practice set.

Rendered into the SAME index the earlier parts use.
"""
import json, os, subprocess, tempfile
from PIL import Image

INK = "222E2D"
FR = lambda a, b: r"\dfrac{%s}{%s}" % (a, b)

E = {
    # ---------------------------------------- a logarithm whose BASE is a radical
    "lx_log": r"\log_{\sqrt{3}}9",
    "lx_l1": r"4",
    "lx_l2": r"2",
    "lx_l3": r"1",
    "lx_l4": FR("1", "2"),

    # ------------------------------------ a quotient with a PURE IMAGINARY divisor
    "lx_div": FR("5+2i", "3i"),
    "lx_d1": FR("2", "3") + r"-" + FR("5", "3") + r"i",
    "lx_d2": r"{-" + FR("2", "3") + r"}+" + FR("5", "3") + r"i",
    "lx_d3": FR("5", "3") + r"+" + FR("2", "3") + r"i",
    "lx_d4": FR("2", "3") + r"+" + FR("5", "3") + r"i",

    # ------------------------------------- the binomial mean and standard deviation
    "lx_bin": r"n=100,\qquad p=0.2",
    "lx_b1": r"\mu=20,\ \ \sigma=4",
    "lx_b2": r"\mu=20,\ \ \sigma=16",
    "lx_b3": r"\mu=20,\ \ \sigma=\sqrt{20}",
    "lx_b4": r"\mu=0.2,\ \ \sigma=4",
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
    tex = os.path.join(tmp, "saatl.tex")
    open(tex, "w").write("\n".join(doc))
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-output-directory", tmp, tex], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-2500:])
        raise SystemExit("pdflatex failed")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(tmp, "saatl.pdf"), os.path.join(tmp, "r")], check=True)
    pages = sorted(f for f in os.listdir(tmp) if f.startswith("r-") and f.endswith(".png"))
    assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} expressions"
    for k, p in zip(keys, pages):
        im = Image.open(os.path.join(tmp, p)).convert("RGBA")
        dst = os.path.join(out_dir, k + ".png")
        im.save(dst)
        idx[k] = {"file": dst, "win": im.width / dpi, "hin": im.height / dpi,
                  "aspect": im.width / im.height}
    json.dump(idx, open(idx_path, "w"), indent=1)
    print(f"{len(keys)} part-L expressions added; index now holds {len(idx)}")


if __name__ == "__main__":
    render()
