"""LaTeX expressions for the GAT question bank, part 10.
Same pipeline as make_math_gat.py — pdflatex, Computer Modern, transparent PNG.
Two resolutions: 500 dpi for slides/screen, 260 dpi for Word (spec §5, §6a).
"""
import json, os, shutil, subprocess
from PIL import Image

INK = "222E2D"
E = {
    # --- stems ---------------------------------------------------------
    "p10_ratio":  r"4\times 10^{6}\qquad\text{and}\qquad 8\times 10^{6}",
    "p10_150":    r"150\%\ \text{of}\ A \;=\; 2500",
    "p10_xyc":    r"xy=c\ ,\qquad xc=y",
    "p10_xy4":    r"\dfrac{x}{4}+\dfrac{y}{4}=25",
    "p10_aeac":   r"\dfrac{AE}{AC}",
    "p10_sq64":   r"(n-1)^{2}=64",
    # --- fraction options ----------------------------------------------
    "f14": r"\dfrac{1}{4}",
    "f12": r"\dfrac{1}{2}",
    "f34": r"\dfrac{3}{4}",
    "f23": r"\dfrac{2}{3}",
    # --- area options ----------------------------------------------------
    "a6":  r"6\ \text{cm}^{2}",
    "a24": r"24\ \text{cm}^{2}",
}


def render(out_dir, dpi):
    tmp = f".tex_p10_{dpi}"
    shutil.rmtree(out_dir, ignore_errors=True); shutil.rmtree(tmp, ignore_errors=True)
    os.makedirs(out_dir); os.makedirs(tmp)
    keys = list(E)
    doc = [r"\documentclass[12pt]{article}", r"\usepackage[active,tightpage]{preview}",
           r"\usepackage{amsmath,amssymb}", r"\usepackage[dvipsnames]{xcolor}",
           r"\setlength\PreviewBorder{1.5pt}",
           r"\definecolor{ink}{HTML}{%s}" % INK, r"\begin{document}"]
    for k in keys:
        doc.append(r"\begin{preview}$\color{ink}\displaystyle %s$\end{preview}" % E[k])
    doc.append(r"\end{document}")
    tex = os.path.join(tmp, "p10.tex")
    open(tex, "w").write("\n".join(doc))
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-output-directory", tmp, tex], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-2500:]); raise SystemExit("pdflatex failed")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(tmp, "p10.pdf"), os.path.join(tmp, "p")], check=True)
    pages = sorted(f for f in os.listdir(tmp) if f.startswith("p-") and f.endswith(".png"))
    assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} expressions"
    idx = {}
    for k, p in zip(keys, pages):
        im = Image.open(os.path.join(tmp, p)).convert("RGBA")
        dst = os.path.join(out_dir, k + ".png"); im.save(dst)
        idx[k] = {"file": dst, "win": im.width / dpi, "hin": im.height / dpi,
                  "aspect": im.width / im.height}
    json.dump(idx, open(os.path.join(out_dir, "_index.json"), "w"), indent=1)
    print(f"{len(idx)} expressions -> {out_dir} @ {dpi} dpi")


render("math_p10", 500)
render("math_p10_doc", 260)
