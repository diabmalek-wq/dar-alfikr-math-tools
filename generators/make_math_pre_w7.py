"""LaTeX for the WEEK 7 pre-session skills sheet — Grade 10, Vertex Form of
a Quadratic Function.

Rendered into the SAME shared index the earlier weeks use
(math_pre/_index.json), so presession.js can pick any key from any week.

Reminder keys are p7_*, warm-up keys are q7_*, and every q7_ uses different
numbers from every p7_ (the Week 2 defect this house rule guards against).

    python3 make_math_pre_w7.py
"""
import json, os, subprocess, tempfile
from PIL import Image

INK = "222E2D"

E = {
    # =============================================== GRADE 10 · priors
    # anchor: T2 L1 Vertex Form of a Quadratic Function
    "p7_transform": r"f(x)\ \to\ f(x-h)+k",
    "p7_parent":    r"f(x)=x^{2}",
    "p7_eval":      r"f(x)=x^{2}.\qquad f(-3)=9",
    "p7_vf":        r"f(x)=a(x-h)^{2}+k",
    "p7_signflip":  (r"f(x)=(x-3)^{2}+5\ \Rightarrow\ \text{vertex}=(3,5)"
                      r"\qquad f(x)=(x+3)^{2}+5\ \Rightarrow\ \text{vertex}=(-3,5)"),
    "p7_signa":     r"a>0\ \text{opens up}\qquad a<0\ \text{opens down}",

    "q7_g10a": r"f(x)=x^{2}.\qquad f(-4)=\underline{\quad}",
    "q7_g10b": r"y=f(x)+7",
    "q7_g10c": r"y=f(x-5)",
    "q7_g10d": r"y=f(x+2)-3",
    "q7_g10e": r"f(x)=x^{2}.\qquad f(5)=\underline{\quad}",
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
    tex = os.path.join(tmp, "prew7.tex")
    open(tex, "w").write("\n".join(doc))
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-output-directory", tmp, tex], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-3000:])
        raise SystemExit("pdflatex failed")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(tmp, "prew7.pdf"), os.path.join(tmp, "p")], check=True)
    pages = sorted(f for f in os.listdir(tmp) if f.startswith("p-") and f.endswith(".png"))
    assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} expressions"
    for k, p in zip(keys, pages):
        im = Image.open(os.path.join(tmp, p)).convert("RGBA")
        dst = os.path.join(out_dir, k + ".png")
        im.save(dst)
        src = E[k]
        lines = 1 + src.count(r"\\")
        idx[k] = {"file": dst, "win": im.width / dpi, "hin": im.height / dpi,
                  "aspect": im.width / im.height, "lines": lines}
    json.dump(idx, open(idx_path, "w"), indent=1)
    print(f"{len(keys)} Week-7 expressions added; index now holds {len(idx)}")


if __name__ == "__main__":
    render()
