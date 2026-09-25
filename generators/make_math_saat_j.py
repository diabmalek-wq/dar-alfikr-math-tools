"""Stem expressions that were being written as plain text.

Ten stems carried a radical typed as the character "√" with nothing over the
radicand, so "√75 + √48 − √12" printed with no vinculum and no indication of
what each root covered. Every one of them is typeset here and shown as a
display expression under its stem, the way the rest of the bank already does it.

Rendered into the SAME index the earlier parts use.
"""
import json, os, subprocess, tempfile
from PIL import Image

INK = "222E2D"

E = {
    "j_shiftroot": r"y=\sqrt{x}",
    "j_sumdom": r"f(x)=x^{2}+4x\qquad g(x)=\sqrt{x+2}",
    "j_raypoint": r"\left({-3\sqrt{3}},\ 3\right)",
    "j_argz": r"z=1+\sqrt{3}\,i",
    "j_modpow": r"\left(1+\sqrt{3}\,i\right)^{6}",
    "j_vec": r"\left\langle 6,\ 6\sqrt{3}\right\rangle",
    "j_addrad": r"\sqrt{75}+\sqrt{48}-\sqrt{12}",
    "j_cscval": r"\sin\theta=\dfrac{\sqrt{6}}{4}",
    "j_acos": r"\cos^{-1}\left({-\dfrac{\sqrt{2}}{2}}\right)",
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
    tex = os.path.join(tmp, "saatj.tex")
    open(tex, "w").write("\n".join(doc))
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-output-directory", tmp, tex], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-3000:])
        raise SystemExit("pdflatex failed")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(tmp, "saatj.pdf"), os.path.join(tmp, "r")], check=True)
    pages = sorted(f for f in os.listdir(tmp) if f.startswith("r-") and f.endswith(".png"))
    assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} expressions"
    for k, p in zip(keys, pages):
        im = Image.open(os.path.join(tmp, p)).convert("RGBA")
        dst = os.path.join(out_dir, k + ".png")
        im.save(dst)
        idx[k] = {"file": dst, "win": im.width / dpi, "hin": im.height / dpi,
                  "aspect": im.width / im.height}
    json.dump(idx, open(idx_path, "w"), indent=1)
    print(f"{len(keys)} stem expressions added; index now holds {len(idx)}")


if __name__ == "__main__":
    render()
