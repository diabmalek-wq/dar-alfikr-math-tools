"""LaTeX for the simulated SAAT (Tahsili) bank.

Same pipeline as every other Dar Alfikr sheet: pdflatex + preview, Computer
Modern, one expression per page, transparent PNG at 300 dpi. Nothing on the
paper is typed as plain-text mathematics.

House rules followed here: \\dfrac never \\tfrac, \\leq never \\le, and a unary
minus is wrapped as {-4} so it keeps a digit's spacing instead of a binary
operator's.
"""
import json, os, shutil, subprocess, tempfile
from PIL import Image

INK = "222E2D"

E = {
    # ------------------------------------------------------------- binomial
    "a_bin1":   r"(2x+3)^{5}",
    "a_bin2":   r"(x-3)^{5}",
    "a_bin2o1": r"{-270}x^{2}",
    "a_bin2o2": r"270x^{2}",
    "a_bin2o3": r"405x",
    "a_bin2o4": r"{-27}x^{2}",

    # -------------------------------------------------------------- matrices
    "a_mati":   r"\begin{pmatrix}4&3\\3&2\end{pmatrix}",
    "a_matio1": r"\begin{pmatrix}2&{-3}\\{-3}&4\end{pmatrix}",
    "a_matio2": r"\begin{pmatrix}{-2}&3\\3&{-4}\end{pmatrix}",
    "a_matio3": r"\begin{pmatrix}{-4}&3\\3&{-2}\end{pmatrix}",
    "a_matio4": r"\begin{pmatrix}4&{-3}\\{-3}&2\end{pmatrix}",
    "a_matsys": r"\begin{cases}2x+y=7\\[2pt]3x+4y=13\end{cases}",
    "a_sing":   r"\begin{pmatrix}k&{-2}\\6&3\end{pmatrix}",

    # ------------------------------------------------------------ logarithms
    "a_lg1":  r"\log_{4}256",
    "a_lg2":  r"\log_{5}125",
    "a_lg3":  r"\log_{3}81",
    "a_lg4":  r"\log_{2}16",
    "a_cmb":  r"3\log_{2}x-\log_{2}(x+1)",
    "a_cmb1": r"\log_{2}\dfrac{3x}{x+1}",
    "a_cmb2": r"\log_{2}\dfrac{x^{3}}{x+1}",
    "a_cmb3": r"\log_{2}\dfrac{x+1}{x^{3}}",
    "a_cmb4": r"\log_{2}\bigl(x^{3}-x-1\bigr)",
    "a_exp":  r"\log_{5}\dfrac{25x^{4}}{\sqrt{y}}",
    "a_exp1": r"2+4\log_{5}x-\dfrac{1}{2}\log_{5}y",
    "a_exp2": r"2+4\log_{5}x+\dfrac{1}{2}\log_{5}y",
    "a_exp3": r"25+4\log_{5}x-\dfrac{1}{2}\log_{5}y",
    "a_exp4": r"2+4\log_{5}x-2\log_{5}y",
    "a_lgv":  r"\log_{3}x=0.4\ ,\qquad \log_{2}y=0.2",
    "a_cob1": r"\dfrac{\log 8}{\log 5}",
    "a_cob2": r"\dfrac{\log 5}{\log 8}",
    "a_cob3": r"\log 5-\log 8",
    "a_cob4": r"\dfrac{\log 5}{8}",

    # ------------------------------------------------- absolute value family
    "a_par1": r"y=\lvert x\rvert",
    "a_par2": r"y=\lvert x\rvert+1",
    "a_par3": r"y=\lvert x-3\rvert",
    "a_par4": r"y=\lvert x\rvert-3",
    "a_sh1":  r"y=\lvert x-4\rvert-2",
    "a_sh2":  r"y=\lvert x+4\rvert+2",
    "a_sh3":  r"y=\lvert x+4\rvert-2",
    "a_sh4":  r"y=\lvert x-2\rvert-4",

    # ---------------------------------------------------------- complex numbers
    "a_cx1":   r"(3-2i)^{2}",
    "a_cx1o1": r"13-12i",
    "a_cx1o2": r"5-12i",
    "a_cx1o3": r"9+4i",
    "a_cx1o4": r"5+12i",
    "a_cx2":   r"\dfrac{5}{2-i}",
    "a_cx2o1": r"2-i",
    "a_cx2o2": r"10+5i",
    "a_cx2o3": r"2+i",
    "a_cx2o4": r"\dfrac{10+5i}{3}",
    "a_dm1":   r"\bigl[\,2\left(\cos 60^{\circ}+i\sin 60^{\circ}\right)\bigr]^{3}",
    "a_dm1o1": r"{-8}",
    "a_dm1o2": r"{-6}",
    "a_dm1o3": r"8",
    "a_dm1o4": r"4+4\sqrt{3}\,i",

    # ------------------------------------------------- scientific notation
    "a_sci1":   r"6\times 10^{-4}",
    "a_sci2":   r"\left(4\times 10^{5}\right)\left(2.5\times 10^{-8}\right)",
    "a_sci2o1": r"10\times 10^{-3}",
    "a_sci2o2": r"1\times 10^{-3}",
    "a_sci2o3": r"1\times 10^{-2}",
    "a_sci2o4": r"1\times 10^{2}",

    # -------------------------------------------------------------- units
    "a_dim1":   r"A=B\cdot C\cdot D",
    "a_dim1o1": r"\mathrm{kg\cdot m/s^{2}}",
    "a_dim1o2": r"\mathrm{kg/(m\cdot s^{2})}",
    "a_dim1o3": r"\mathrm{kg/(m^{2}\cdot s^{2})}",
    "a_dim1o4": r"\mathrm{kg/s^{2}}",
    "a_dim2o1": r"\dfrac{v}{t}",
    "a_dim2o2": r"v\,t^{2}",
    "a_dim2o3": r"v\,t",
    "a_dim2o4": r"\dfrac{v}{t^{2}}",

    # ------------------------------------------------------------- vectors
    "a_vec1":   r"A=\langle 5,{-3}\rangle\ ,\qquad B=\langle 1,4\rangle",
    "a_vec1o1": r"\langle 9,{-2}\rangle",
    "a_vec1o2": r"\langle 11,{-2}\rangle",
    "a_vec1o3": r"\langle 4,{-7}\rangle",
    "a_vec1o4": r"\langle 9,{-10}\rangle",
    "a_vec2":   r"\langle {-6},8\rangle",
    "a_dot1":   r"v=\langle b,{-3},1\rangle\ ,\qquad u=\langle {-2},{-1},3\rangle",
    "a_dot2":   r"\langle 4,{-1},2\rangle\cdot\langle 3,5,{-2}\rangle",

    # ------------------------------------------------------ odd and even
    "a_odd1": r"y=\lvert x\rvert",
    "a_odd2": r"y=x^{2}",
    "a_odd3": r"y=x^{7}",
    "a_odd4": r"y=\sqrt{x}",
    "a_odd5": r"f(x)=x^{3}-x",

    # ------------------------------------------------------------ conics
    "a_par_a": r"x^{2}=8(y-8)",
    "a_par_b": r"(y+2)^{2}={-12}(x-5)",

    # ---------------------------------------------------------- trigonometry
    "a_tr1":   r"\dfrac{\sin^{2}\theta}{\tan^{2}\theta}",
    "a_tr1o1": r"\dfrac{\sin^{4}\theta}{\cos^{2}\theta}",
    "a_tr1o2": r"\cos^{2}\theta",
    "a_tr1o3": r"\sin^{2}\theta",
    "a_tr1o4": r"\tan^{2}\theta",
    "a_tr2":   r"\dfrac{1-\cos^{2}\theta}{\sin\theta\,\cos\theta}",
    "a_tr2o1": r"\cot\theta",
    "a_tr2o2": r"1",
    "a_tr2o3": r"\tan\theta",
    "a_tr2o4": r"\sin\theta",
    "a_tr3":   r"\dfrac{2\tan\theta}{1+\tan^{2}\theta}",
    "a_tr3o1": r"\cos 2\theta",
    "a_tr3o2": r"\sin 2\theta",
    "a_tr3o3": r"\tan 2\theta",
    "a_tr3o4": r"2\sin\theta",
    "a_tr4o1": r"\dfrac{7}{25}",
    "a_tr4o2": r"\dfrac{12}{25}",
    "a_tr4o3": r"\dfrac{24}{25}",
    "a_tr4o4": r"\dfrac{6}{5}",
    "a_pol1":   r"(r,\theta)=\left({-2},\ 60^{\circ}\right)",
    "a_pol1o1": r"\left(1,\ \sqrt{3}\right)",
    "a_pol1o2": r"\left({-1},\ \sqrt{3}\right)",
    "a_pol1o3": r"\left(1,\ {-\sqrt{3}}\right)",
    "a_pol1o4": r"\left({-1},\ {-\sqrt{3}}\right)",

    # ------------------------------------------------------------- calculus
    "a_arc":   r"f(x)=6x^{2}-4x+2",
    "a_arc2":  r"f(x)=x^{2}",
    "a_dv1":   r"y=x^{4}",
    "a_dv1o1": r"3x^{4}",
    "a_dv1o2": r"4x^{3}",
    "a_dv1o3": r"4x^{4}",
    "a_dv1o4": r"\dfrac{x^{5}}{5}",
    "a_dv2":   r"f(x)=3\sqrt{x}+\dfrac{2}{x}",
    "a_dv2o1": r"\dfrac{3}{2\sqrt{x}}-\dfrac{2}{x^{2}}",
    "a_dv2o2": r"\dfrac{3}{2\sqrt{x}}+\dfrac{2}{x^{2}}",
    "a_dv2o3": r"\dfrac{3}{2\sqrt{x}}-\dfrac{2}{x}",
    "a_dv2o4": r"\dfrac{1}{2\sqrt{x}}-\dfrac{2}{x^{2}}",
    "a_dv3":   r"f(x)=15x^{2}-5x+c",
    "a_dv4":   r"y=x^{3}-4x",
    "a_dv4o1": r"y={-4x}+8",
    "a_dv4o2": r"y=8x-16",
    "a_dv4o3": r"y=8x",
    "a_dv4o4": r"y=12x-24",
    "a_int1":   r"\int_{0}^{3}f(x)\,dx",
    "a_int1o1": r"F(0)-F(3)",
    "a_int1o2": r"F(3)-F(0)",
    "a_int1o3": r"F(3)",
    "a_int1o4": r"f(3)-f(0)",
    "a_int2":  r"\int_{2}^{3}(4x+1)\,dx",
    "a_int3":  r"\int_{1}^{3}(6x-2)\,dx",
    "a_max":   r"f(x)=6x^{2}-x^{3}",
    "a_crit":  r"f(x)=x^{3}-3x^{2}+3x-1",
    "a_lim1":  r"\lim_{x\to 5}\dfrac{x^{2}-25}{x-5}",
    "a_lim2":  r"\lim_{x\to 0}\dfrac{\sqrt{x+9}-3}{x}",
    "a_lim2o1": r"0",
    "a_lim2o2": r"\dfrac{1}{6}",
    "a_lim2o3": r"\dfrac{1}{3}",
    "a_lim2o4": r"6",
    "a_sdt":   r"f(x)=2+3x-x^{3}",
    "a_inf":   r"f(x)=x^{3}-6x^{2}+5",

    # ---------------------------------------------------------- probability
    "a_pr1o1": r"\dfrac{1}{9}",
    "a_pr1o2": r"\dfrac{1}{4}",
    "a_pr1o3": r"\dfrac{1}{2}",
    "a_pr1o4": r"\dfrac{2}{5}",
    "a_pr2o1": r"\dfrac{2}{5}",
    "a_pr2o2": r"\dfrac{1}{2}",
    "a_pr2o3": r"\dfrac{3}{5}",
    "a_pr2o4": r"\dfrac{2}{3}",
}


def render(out_dir="math_saat_doc", dpi=300):
    shutil.rmtree(out_dir, ignore_errors=True)
    os.makedirs(out_dir)
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
    tex = os.path.join(tmp, "saat.tex")
    open(tex, "w").write("\n".join(doc))
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-output-directory", tmp, tex], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-3000:])
        raise SystemExit("pdflatex failed")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(tmp, "saat.pdf"), os.path.join(tmp, "p")], check=True)
    pages = sorted(f for f in os.listdir(tmp) if f.startswith("p-") and f.endswith(".png"))
    assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} expressions"
    idx = {}
    for k, p in zip(keys, pages):
        im = Image.open(os.path.join(tmp, p)).convert("RGBA")
        dst = os.path.join(out_dir, k + ".png")
        im.save(dst)
        idx[k] = {"file": dst, "win": im.width / dpi, "hin": im.height / dpi,
                  "aspect": im.width / im.height}
    json.dump(idx, open(os.path.join(out_dir, "_index.json"), "w"), indent=1)
    print(f"{len(idx)} expressions -> {out_dir} @ {dpi} dpi")


if __name__ == "__main__":
    render()
