"""LaTeX for part E of the SAAT booklet — logic and the skills the bank had not
reached. Rendered into the SAME index the earlier parts use.
"""
import json, os, subprocess, tempfile
from PIL import Image

INK = "222E2D"

E = {
    # --------------------------------------------- exponential and logarithmic
    "e_ilog1": r"f^{-1}(x)=5^{x}",
    "e_ilog2": r"f^{-1}(x)=\dfrac{1}{\log_{5}x}",
    "e_ilog3": r"f^{-1}(x)=\left(\tfrac{1}{5}\right)^{x}",
    "e_ilog4": r"f^{-1}(x)=\log_{x}5",
    "e_comp":  r"2^{\,4\log_{2}x}",
    "e_comp1": r"x^{4}",
    "e_comp2": r"4x",
    "e_comp3": r"x",
    "e_comp4": r"4^{x}",
    "e_ci1": r"A=20000\left(1.05\right)^{t}",
    "e_ci2": r"A=20000\left(0.05\right)^{t}",
    "e_ci3": r"A=20000+20000(0.05)t",
    "e_ci4": r"A=20000\left(5\right)^{t}",

    # --------------------------------------------- special triangles and trig
    "e_sp1": r"5\sqrt{3}\ \ \text{and}\ \ 10",
    "e_sp2": r"5\sqrt{2}\ \ \text{and}\ \ 10",
    "e_sp3": r"10\ \ \text{and}\ \ 10\sqrt{3}",
    "e_sp4": r"5\sqrt{3}\ \ \text{and}\ \ 15",
    "e_exv":  r"\sin^{2}30^{\circ}-\cos^{2}60^{\circ}",
    "e_exv1": r"0",
    "e_exv2": r"{-\dfrac{1}{2}}",
    "e_exv3": r"\dfrac{1}{2}",
    "e_exv4": r"\dfrac{1}{4}",
    "e_ni1": r"\sin\theta+\cos\theta=1",
    "e_ni2": r"\sin^{2}\theta+\cos^{2}\theta=1",
    "e_ni3": r"\tan\theta=\dfrac{\sin\theta}{\cos\theta}",
    "e_ni4": r"\sec\theta=\dfrac{1}{\cos\theta}",

    # --------------------------------------------- analytic geometry
    "e_vsc1": r"(3,\ 6)",
    "e_vsc2": r"(11,\ 6)",
    "e_vsc3": r"(13,\ 10)",
    "e_vsc4": r"({-1},\ 6)",

    # --------------------------------------------- the chain rule
    "e_ch1":  r"y=\left(3x^{2}+5\right)^{4}",
    "e_ch1a": r"24x\left(3x^{2}+5\right)^{3}",
    "e_ch1b": r"4\left(3x^{2}+5\right)^{3}",
    "e_ch1c": r"24x\left(3x^{2}+5\right)^{4}",
    "e_ch1d": r"6x",
    "e_ch2":  r"y=\sqrt{x^{2}+9}",
    "e_ch2a": r"\dfrac{x}{\sqrt{x^{2}+9}}",
    "e_ch2b": r"\dfrac{2x}{\sqrt{x^{2}+9}}",
    "e_ch2c": r"\dfrac{1}{2\sqrt{x^{2}+9}}",
    "e_ch2d": r"\dfrac{1}{2\sqrt{x}}",

    # --------------------------------------------- transcendental derivatives
    "e_tr1":  r"y=\sin\left(5x\right)",
    "e_tr1a": r"y'=5\cos\left(5x\right)",
    "e_tr1b": r"y'={-5}\cos\left(5x\right)",
    "e_tr1c": r"y'=\cos\left(5x\right)",
    "e_tr1d": r"y'=5\sin\left(5x\right)",
    "e_tr2":  r"y=\ln\left(x^{3}+2\right)",
    "e_tr2a": r"y'=\dfrac{3x^{2}}{x^{3}+2}",
    "e_tr2b": r"y'=\dfrac{1}{x^{3}+2}",
    "e_tr2c": r"y'=3x^{2}\ln\left(x^{3}+2\right)",
    "e_tr2d": r"y'=\dfrac{x^{3}+2}{3x^{2}}",

    # --------------------------------------------- implicit differentiation
    "e_im1": r"\dfrac{dy}{dx}={-\dfrac{x}{y}}",
    "e_im2": r"\dfrac{dy}{dx}=\dfrac{x}{y}",
    "e_im3": r"\dfrac{dy}{dx}={-2x}",
    "e_im4": r"\dfrac{dy}{dx}={-\dfrac{y}{x}}",

    # --------------------------------------------- integration
    "e_ap":  r"\displaystyle\int 6x^{2}\,dx",
    "e_ap1": r"2x^{3}+C",
    "e_ap2": r"2x^{3}",
    "e_ap3": r"12x+C",
    "e_ap4": r"3x^{3}+C",
    "e_pa1": r"F(x)=2x^{2}-3x+3",
    "e_pa2": r"F(x)=2x^{2}-3x+5",
    "e_pa3": r"F(x)=2x^{2}-3x",
    "e_pa4": r"F(x)=2x^{2}-3x-3",
    "e_is":  r"\displaystyle\int\left(3x^{2}-4x+7\right)dx",
    "e_is1": r"x^{3}-2x^{2}+7x+C",
    "e_is2": r"x^{3}-2x^{2}+7+C",
    "e_is3": r"x^{3}-4x^{2}+7x+C",
    "e_is4": r"6x-4+C",
    "e_in":  r"\displaystyle\int x^{-3}\,dx",
    "e_in1": r"{-\dfrac{1}{2x^{2}}}+C",
    "e_in2": r"\dfrac{1}{2x^{2}}+C",
    "e_in3": r"\ln\left|x^{3}\right|+C",
    "e_in4": r"{-\dfrac{1}{4x^{4}}}+C",
    "e_sub":  r"\displaystyle\int 2x\left(x^{2}+1\right)^{5}dx",
    "e_sub1": r"\dfrac{\left(x^{2}+1\right)^{6}}{6}+C",
    "e_sub2": r"\dfrac{\left(x^{2}+1\right)^{6}}{5}+C",
    "e_sub3": r"\dfrac{2x\left(x^{2}+1\right)^{6}}{6}+C",
    "e_sub4": r"\dfrac{\left(x^{2}+1\right)^{5}}{5}+C",
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
    tex = os.path.join(tmp, "saate.tex")
    open(tex, "w").write("\n".join(doc))
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-output-directory", tmp, tex], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-3000:])
        raise SystemExit("pdflatex failed")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(tmp, "saate.pdf"), os.path.join(tmp, "r")], check=True)
    pages = sorted(f for f in os.listdir(tmp) if f.startswith("r-") and f.endswith(".png"))
    assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} expressions"
    for k, p in zip(keys, pages):
        im = Image.open(os.path.join(tmp, p)).convert("RGBA")
        dst = os.path.join(out_dir, k + ".png")
        im.save(dst)
        idx[k] = {"file": dst, "win": im.width / dpi, "hin": im.height / dpi,
                  "aspect": im.width / im.height}
    json.dump(idx, open(idx_path, "w"), indent=1)
    print(f"{len(keys)} part-E expressions added; index now holds {len(idx)}")


if __name__ == "__main__":
    render()
