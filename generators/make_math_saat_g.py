"""LaTeX for part G of the SAAT booklet — the ninth sample paper's identities,
coordinate proof, series and calculus.

Rendered into the SAME index the earlier parts use.
"""
import json, os, subprocess, tempfile
from PIL import Image

INK = "222E2D"

DET = lambda body, cols="cc": r"\left|\begin{array}{%s}%s\end{array}\right|" % (cols, body)
PT = lambda x, y: r"\left(%s,\ %s\right)" % (x, y)

E = {
    # --------------------------------------------------- trig identities
    "g_id1": r"\sin^{2}\theta\sec\theta+\cos\theta",
    "g_id1a": r"\sec\theta",
    "g_id1b": r"\cos\theta",
    "g_id1c": r"\sec\theta-\cos\theta",
    "g_id1d": r"\sec\theta+2\cos\theta",
    "g_id2": r"\left(1+\tan^{2}45^{\circ}\right)\left(1-\sin^{2}45^{\circ}\right)",
    "g_hy1": r"1",
    "g_hy2": r"\sin x+\cos x",
    "g_hy3": r"\sin x\cos x",
    "g_hy4": r"\sqrt{2}",
    "g_lc1": r"7",
    "g_lc2": r"\sqrt{129}",
    "g_lc3": r"\sqrt{89}",
    "g_lc4": r"3",

    # ------------------------------------------------ functions and graphs
    "g_rg1": r"y=2\sqrt{x-1}-1",
    "g_rg2": r"y=2\sqrt{x+1}-1",
    "g_rg3": r"y=\sqrt{x-1}-1",
    "g_rg4": r"y=\dfrac{1}{2}\sqrt{x-1}-1",

    # ------------------------------------------ matrices, complex and polar
    "g_det": DET(r"x & 4 \\ 4 & x"),
    "g_pol": r"r=\dfrac{6}{\sec\theta}",
    "g_pc1": r"\left(x-3\right)^{2}+y^{2}=9",
    "g_pc2": r"x^{2}+y^{2}=9",
    "g_pc3": r"x^{2}+\left(y-3\right)^{2}=9",
    "g_pc4": r"\left(x-6\right)^{2}+y^{2}=36",

    # ------------------------------------------------------ coordinate proof
    "g_tz1": PT("b", "c"),
    "g_tz2": PT("a+b", "c"),
    "g_tz3": PT("b+c", "c"),
    "g_tz4": PT("c", "b"),
    "g_pp1": r"y={-\dfrac{1}{2}}x+3",
    "g_pp2": r"y=2x-7",
    "g_pp3": r"y=\dfrac{1}{2}x-1",
    "g_pp4": r"y={-\dfrac{1}{2}}x-3",
    "g_ax1": PT("3", "4"),
    "g_ax2": PT("4", "3"),
    "g_ax3": PT("0", "4"),
    "g_ax4": PT("{-3}", "4"),

    # -------------------------------------------------- sequences and series
    "g_bt1": r"{-160}x^{3}",
    "g_bt2": r"160x^{3}",
    "g_bt3": r"240x^{2}",
    "g_bt4": r"{-8}x^{3}",
    "g_sig": r"\sum_{k=1}^{10}\left(3k+2\right)",

    # -------------------------------------------------------------- calculus
    "g_sd1": r"40x^{3}-6",
    "g_sd2": r"10x^{4}-6x",
    "g_sd3": r"10x^{3}-6",
    "g_sd4": r"40x^{3}-6x",
    "g_ai": r"\int\dfrac{4}{x^{-3}}\,dx",
    "g_ai1": r"x^{4}+C",
    "g_ai2": r"x^{4}",
    "g_ai3": r"{-2}x^{-2}+C",
    "g_ai4": r"2x^{2}+C",
    "g_tr1": PT("{-1}", "{-5}"),
    "g_tr2": PT("2", "{-8}"),
    "g_tr3": PT("11", "1"),
    "g_tr4": PT("{-1}", "{-2}"),
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
    tex = os.path.join(tmp, "saatg.tex")
    open(tex, "w").write("\n".join(doc))
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-output-directory", tmp, tex], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-3000:])
        raise SystemExit("pdflatex failed")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(tmp, "saatg.pdf"), os.path.join(tmp, "r")], check=True)
    pages = sorted(f for f in os.listdir(tmp) if f.startswith("r-") and f.endswith(".png"))
    assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} expressions"
    for k, p in zip(keys, pages):
        im = Image.open(os.path.join(tmp, p)).convert("RGBA")
        dst = os.path.join(out_dir, k + ".png")
        im.save(dst)
        idx[k] = {"file": dst, "win": im.width / dpi, "hin": im.height / dpi,
                  "aspect": im.width / im.height}
    json.dump(idx, open(idx_path, "w"), indent=1)
    print(f"{len(keys)} part-G expressions added; index now holds {len(idx)}")


if __name__ == "__main__":
    render()
