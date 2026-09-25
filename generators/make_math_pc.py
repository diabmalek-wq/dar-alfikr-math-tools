"""LaTeX expressions for the question bank, Set C.
Same pipeline as make_math_p8.py — pdflatex, Computer Modern, transparent PNG.
Two resolutions: 500 dpi for slides/screen, 260 dpi for Word (spec section 5, 6a).
"""
import json, os, shutil, subprocess
from PIL import Image

INK = "222E2D"
E = {
    # --- stems -----------------------------------------------------------
    "pc_q1":   r"x+y=z\ ,\qquad x=y",
    "pc_q2":   r"x+y=m\ ,\quad x,y\neq 0\qquad\text{A: }\ \dfrac{1}{x}"
               r"\qquad\text{B: }\ \dfrac{1}{y}",
    "pc_q3":   r"m>x\ ,\quad m,x\neq 0\qquad\text{A: }\ \dfrac{1}{m}"
               r"\qquad\text{B: }\ \dfrac{1}{x}",
    "pc_q8":   r"\dfrac{\sqrt{3}\left(\sqrt{2}+4\sqrt{2}\right)}"
               r"{\dfrac{\sqrt{3}}{2\sqrt{2}}}",
    "pc_q12":  r"\text{A: }\ \dfrac{1}{4+m}\qquad\qquad"
               r"\text{B: }\ \dfrac{1}{4}m+1",
    "pc_q20":  r"\text{A: }\ 25\%\ \text{of}\ 240\qquad\qquad"
               r"\text{B: }\ 0.5\%\ \text{of}\ 12\,000",
    "pc_q21":  r"\text{hypotenuse}=10\ ,\qquad\text{legs}\ x\ \text{and}\ x+2",
    "pc_q23":  r"30n-57=1203",
    "pc_q25":  r"\text{A: }\ \dfrac{3}{4}-\dfrac{7}{8}\qquad\qquad"
               r"\text{B: }\ \dfrac{5}{8}-\dfrac{7}{8}",
    # --- options for Q1 ---------------------------------------------------
    "q1a": r"x=\dfrac{z}{2}",
    "q1b": r"x-z=y-z",
    "q1c": r"2x+2y=2z",
    "q1d": r"z-y=2x",
    # --- options for Q24 --------------------------------------------------
    "o3r3":  r"3\sqrt{3}",
    "o45r3": r"4.5\sqrt{3}",
    "o9r3":  r"9\sqrt{3}",
    "o2r3":  r"2\sqrt{3}",
}


def render(out_dir, dpi):
    tmp = f".tex_pc_{dpi}"
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
    tex = os.path.join(tmp, "pc.tex")
    open(tex, "w").write("\n".join(doc))
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-output-directory", tmp, tex], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-2500:]); raise SystemExit("pdflatex failed")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(tmp, "pc.pdf"), os.path.join(tmp, "p")], check=True)
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


render("math_pc", 500)
render("math_pc_doc", 260)
