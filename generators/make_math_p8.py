"""LaTeX expressions for the question bank, part 8.
Same pipeline as make_math_p10.py — pdflatex, Computer Modern, transparent PNG.
Two resolutions: 500 dpi for slides/screen, 260 dpi for Word (spec section 5, 6a).
"""
import json, os, shutil, subprocess
from PIL import Image

INK = "222E2D"
E = {
    # --- stems ---------------------------------------------------------
    "p8_cubic":  r"2x^{3}-x^{2}+8x\qquad\text{when}\ x={-1}",
    "p8_sys":    r"2x+\dfrac{1}{2}y=21\ ,\qquad y+\dfrac{4}{3}m=18",
    "p8_prop":   r"\dfrac{3}{5}=\dfrac{0.3x}{5}",
    "p8_pow":    r"\left(x^{\frac{1}{5}}\div x^{-\frac{4}{5}}\right)\cdot x^{2}=27",
    "p8_ineq":   r"1+2n>0",
    "p8_two15":  r"2^{15}",
    "p8_div":    r"87\,956\,220\div 284",
    "p8_est":    r"0.499\times 0.76\times 8",
    "p8_2x5y":   r"2x=5y",
    "p8_7m8k":   r"7^{m}=49\ ,\qquad 8k=48",
    "p8_x13":    r"x={-\dfrac{1}{3}}\ ,\qquad x+y=0",
    "p8_mid":    r"eg=fh=\dfrac{1}{3}\,ce=\dfrac{1}{3}\,df\ ,\qquad\text{find}\quad \dfrac{ce+eg+df}{2\,ca+ce}",
    "p8_r2r2":   r"r=2\sqrt{2}",
    "a8r2":      r"8\sqrt{2}",
    # --- comparison quantities ------------------------------------------
    "p8_c28a":   r"\dfrac{0.75\times 87.99}{1.999}",
    "p8_c17a":   r"2\sqrt{2}",
    "p8_c17b":   r"\dfrac{6\sqrt{6}}{3\sqrt{3}}",
    "p8_c33b":   r"{-\dfrac{3}{4}}",
    "p8_c45a":   r"x-y",
    "p8_c45b":   r"5x",
    "p8_c24a":   r"3m",
    "p8_c24b":   r"2k",
    # --- comparison quantities, printed as the item shows them ----------
    "p8_cmp17": r"\text{A: }\ 2\sqrt{2}\qquad\qquad\text{B: }\ \dfrac{6\sqrt{6}}{3\sqrt{3}}",
    "p8_cmp28": r"\text{A: }\ \dfrac{0.75\times 87.99}{1.999}\qquad\qquad\text{B: }\ 30",
    "p8_cmp24": r"7^{m}=49\ ,\quad 8k=48\qquad\text{A: }\ 3m\qquad\text{B: }\ 2k",
    "p8_cmp33": r"1+2n>0\qquad\text{A: }\ n\qquad\text{B: }\ {-\dfrac{3}{4}}",
    "p8_cmp40": r"2x=5y\qquad\qquad\text{A: }\ x\qquad\text{B: }\ y",
    "p8_cmp45": r"x={-\dfrac{1}{3}}\ ,\quad x+y=0\qquad\text{A: }\ x-y\qquad\text{B: }\ 5x",
    # --- fraction options ------------------------------------------------
    "f513": r"\dfrac{5}{13}",
    "f711": r"\dfrac{7}{11}",
    "f911": r"\dfrac{9}{11}",
    "f12":  r"\dfrac{1}{2}",
}


def render(out_dir, dpi):
    tmp = f".tex_p8_{dpi}"
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
    tex = os.path.join(tmp, "p8.tex")
    open(tex, "w").write("\n".join(doc))
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-output-directory", tmp, tex], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-2500:]); raise SystemExit("pdflatex failed")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(tmp, "p8.pdf"), os.path.join(tmp, "p")], check=True)
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


render("math_p8", 500)
render("math_p8_doc", 260)
