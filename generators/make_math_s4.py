"""LaTeX for the Grade 11 SAAT + SAT + GAT prior-knowledge worksheet.
Same pipeline as every other set: pdflatex, Computer Modern, transparent PNG,
260 dpi for Word."""
import json, os, shutil, subprocess
from PIL import Image

INK = "222E2D"
E = {
    "s4_lin":    r"3(x-4)=2x+5",
    "s4_expo":   r"\left(2x^{3}\right)\left(5x^{4}\right)",
    "s4_quad":   r"x^{2}-7x+12=0",
    "s4_sys":    r"3x+2y=19\ ,\qquad x-y=3",
    "s4_cmp":    r"\text{A: }\ 15\%\ \text{of}\ 240\qquad\qquad"
                 r"\text{B: }\ 24\%\ \text{of}\ 150",
    "s4_units":  r"7^{23}",
    "s4_pts":    r"(2,\,5)\quad\text{and}\quad(6,\,17)",
    # option glyphs that need real typesetting
    "o4_a1": r"10x^{7}",  "o4_a2": r"10x^{12}",
    "o4_a3": r"7x^{7}",   "o4_a4": r"10x^{5}",
}


def render(out_dir, dpi):
    shutil.rmtree(out_dir, ignore_errors=True); os.makedirs(out_dir)
    tmp = out_dir + "_tmp"; shutil.rmtree(tmp, ignore_errors=True); os.makedirs(tmp)
    keys = list(E)
    doc = [r"\documentclass[12pt]{article}",
           r"\usepackage[active,tightpage]{preview}",
           r"\usepackage{amsmath,amssymb,xcolor}",
           r"\definecolor{ink}{HTML}{%s}" % INK,
           r"\begin{document}"]
    for k in keys:
        doc.append(r"\begin{preview}$\color{ink}\displaystyle %s$\end{preview}" % E[k])
    doc.append(r"\end{document}")
    tex = os.path.join(tmp, "s4.tex"); open(tex, "w").write("\n".join(doc))
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-output-directory", tmp, tex], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-2000:]); raise SystemExit("pdflatex failed")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(tmp, "s4.pdf"), os.path.join(tmp, "p")], check=True)
    pages = sorted(f for f in os.listdir(tmp) if f.startswith("p-") and f.endswith(".png"))
    assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)}"
    idx = {}
    for k, p in zip(keys, pages):
        im = Image.open(os.path.join(tmp, p)).convert("RGBA")
        dst = os.path.join(out_dir, k + ".png"); im.save(dst)
        idx[k] = {"file": dst, "win": im.width / dpi, "hin": im.height / dpi,
                  "aspect": im.width / im.height}
    json.dump(idx, open(os.path.join(out_dir, "_index.json"), "w"), indent=1)
    shutil.rmtree(tmp, ignore_errors=True)
    print(f"{len(idx)} expressions -> {out_dir}")


render("math_s4_doc", 260)
