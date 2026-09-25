"""
Expressions for the GAT worksheets, Weeks 2 and 4.
Real LaTeX (pdflatex + Computer Modern), tight-cropped transparent PNG.
"""
import json, os, shutil, subprocess
from PIL import Image

OUT, TMP, DPI = "math_gat", ".tex_gat", 420
shutil.rmtree(OUT, ignore_errors=True); shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(OUT); os.makedirs(TMP)
INK = "222E2D"

E = {
    # ---------------- Week 2 stems
    "w2_dec":   r"8.905+8.095-7.5",
    "w2_div":   r"\dfrac{96}{0.008}",
    "w2_mult":  r"0.2\times 0.3\times 0.5\times 0.4",
    "w2_pow":   r"(-3)^{3}-3^{3}",
    "w2_rad":   r"\dfrac{\sqrt{27}+\sqrt{48}}{\sqrt{3}}",
    "w2_cmpA":  r"A:\ \dfrac{13}{7}-\dfrac{7}{13}\qquad\qquad B:\ \dfrac{7}{13}-\dfrac{13}{7}",
    "w2_frac":  r"1-\dfrac{1}{2}-\dfrac{1}{4}-\dfrac{1}{8}",
    "w2_inv":   r"x^{-1}=\dfrac{\sqrt{3}}{9}",
    "w2_lin":   r"5x-y=22\qquad\text{and}\qquad \dfrac{x}{5}=5",
    "w2_recip": r"\dfrac{1}{(x-3)^{3}}=\dfrac{1}{1000}",
    "w2_sq":    r"x^{2}=81",
    "w2_root":  r"\sqrt{x-4}=5",
    "w2_expo":  r"\dfrac{3^{8}}{3^{-2}}",
    "w2_cmpB":  r"A:\ \text{the number of right angles in a triangle}\qquad B:\ 1",
    # Week 2 options
    "w2_o_9h":  r"9\dfrac{1}{2}",
    "w2_o_3r3": r"3\sqrt{3}",
    "w2_o_9r3": r"9\sqrt{3}",
    "w2_o_r3":  r"\sqrt{3}",
    "w2_o_r39": r"\dfrac{\sqrt{3}}{9}",
    "w2_o_38":  r"\dfrac{3}{8}",
    "w2_o_58":  r"\dfrac{5}{8}",
    "w2_o_13":  r"\dfrac{1}{3}",
    "w2_o_18":  r"\dfrac{1}{8}",
    "w2_o_12":  r"\dfrac{1}{2}",
    "w2_o_14":  r"\dfrac{1}{4}",
    "w2_o_15":  r"\dfrac{1}{5}",
    "w2_o_pm9": r"\pm 9",
    "w2_o_mp9": r"\mp 9",
    "w2_o_310": r"3^{10}",
    "w2_o_36":  r"3^{6}",
    "w2_o_316": r"3^{16}",
    "w2_o_3m6": r"3^{-6}",

    # ---------------- Week 4 stems
    "w4_dec":   r"12.75-3.4+0.65",
    "w4_mult":  r"0.06\times 0.5",
    "w4_expo":  r"\dfrac{5^{7}}{5^{-2}}",
    "w4_neg":   r"\left(\dfrac{2}{5}\right)^{-3}",
    "w4_rad":   r"\sqrt{50}\cdot\sqrt{2}",
    "w4_rat":   r"\dfrac{6}{\sqrt{2}}",
    "w4_cmpA":  r"A:\ (0.3)^{2}\qquad\qquad B:\ (0.3)^{3}",
    "w4_of":    r"\dfrac{3}{4}\ \text{of}\ \dfrac{2}{3}\ \text{of}\ 96",
    "w4_lin":   r"2x+3y=18",
    "w4_pow":   r"3^{\,n}=\dfrac{1}{27}",
    "w4_sqrt":  r"x-\sqrt{x}=90",
    "w4_roots": r"x^{2}=4",
    "w4_cmpB":  r"A:\ \text{the number of diagonals of a quadrilateral}\qquad B:\ 2",
    # Week 4 options
    "w4_o_59":  r"5^{9}",
    "w4_o_55":  r"5^{5}",
    "w4_o_514": r"5^{14}",
    "w4_o_5m9": r"5^{-9}",
    "w4_o_1258": r"\dfrac{125}{8}",
    "w4_o_8125": r"\dfrac{8}{125}",
    "w4_o_827": r"\dfrac{8}{27}",
    "w4_o_6125": r"-\dfrac{6}{125}",
    "w4_o_3r2": r"3\sqrt{2}",
    "w4_o_6r2": r"6\sqrt{2}",
    "w4_o_r6":  r"\sqrt{6}",
    "w4_o_r3":  r"3\sqrt{3}",
    "w4_o_45":  r"\dfrac{4}{5}",
    "w4_o_49":  r"\dfrac{4}{9}",
    "w4_o_59f": r"\dfrac{5}{9}",
    "w4_o_23":  r"\dfrac{2}{3}",
    "w4_o_m3":  r"-3",
    "w4_o_p3":  r"3",
    "w4_o_13n": r"\dfrac{1}{3}",
    "w4_o_m13": r"-\dfrac{1}{3}",

    # ---------------- Week 3 (higher difficulty)
    "w3_cmp":   r"A:\ 2^{30}\qquad\qquad B:\ 3^{20}",
    "w3_root":  r"\sqrt{0.16}",
    "w3_big":   r"\text{Which fraction is the largest?}",
    "w3_ident": r"a+b=7\qquad\text{and}\qquad ab=12",
    "w3_abs":   r"|x-3|=5",
    "w3_pow":   r"2^{\,x+1}=32",
    "w3_comp":  r"f(x)=2x+1",
    "w3_ineq":  r"-3(x-2)\geq 15",
    "w3_o_23":  r"\dfrac{2}{3}",
    "w3_o_58":  r"\dfrac{5}{8}",
    "w3_o_711": r"\dfrac{7}{11}",
    "w3_o_35":  r"\dfrac{3}{5}",
    "w3_o_le3": r"x\leq -3",
    "w3_o_ge3": r"x\geq -3",
    "w3_o_le3p": r"x\leq 3",
    "w3_o_ge7": r"x\geq 7",
    "w3_o_s1":  r"16-4\pi",
    "w3_o_s2":  r"16-2\pi",
    "w3_o_s3":  r"16-8\pi",
    "w3_o_s4":  r"4-\pi",

    # ---------------- Week 5 (higher difficulty)
    "w5_pct":   r"25\%\ \text{of}\ 60\%\ \text{of}\ 200",
    "w5_div":   r"0.75\div 0.025",
    "w5_cmp":   r"A:\ \dfrac{3}{7}\qquad\qquad B:\ \dfrac{4}{9}",
    "w5_roots": r"\sqrt{0.09}+\sqrt{0.25}",
    "w5_tel":   r"\dfrac{1}{2}+\dfrac{1}{6}+\dfrac{1}{12}+\dfrac{1}{20}",
    "w5_recip": r"x+\dfrac{1}{x}=4",
    "w5_sq":    r"(a-b)^{2}=25\qquad\text{and}\qquad ab=6",
    "w5_ineq":  r"3(x-2)\leq 2(x+4)",
    "w5_f":     r"f(x)=x^{2}-3x",
    "w5_vieta": r"x^{2}-7x+12=0",
    "w5_o_35":  r"\dfrac{3}{5}",
    "w5_o_45":  r"\dfrac{4}{5}",
    "w5_o_56":  r"\dfrac{5}{6}",
    "w5_o_1":   r"1",
    "w5_o_le14": r"x\leq 14",
    "w5_o_ge14": r"x\geq 14",
    "w5_o_le2":  r"x\leq -2",
    "w5_o_ge2":  r"x\geq -2",
    "w5_o_30pi": r"30\pi",
    "w5_o_60pi": r"60\pi",
    "w5_o_90pi": r"90\pi",
    "w5_o_180pi": r"180\pi",
    "w5_o_half": r"\dfrac{1}{2}",
    "w5_o_310":  r"\dfrac{3}{10}",
    "w5_o_15":   r"\dfrac{1}{5}",
    "w5_o_110":  r"\dfrac{1}{10}",

    # ---------------- realignment items (Sep 2026)
    "r_w2_fx":  r"f(x)=4x-3",
    "r_w2_p14": r"\dfrac{1}{4}",
    "r_w2_p25": r"\dfrac{2}{5}",
    "r_w2_p35": r"\dfrac{3}{5}",
    "r_w2_p23": r"\dfrac{2}{3}",
    "r_w4_gx":  r"g(x)=\dfrac{x}{2}+3",
    "r_w4_p38": r"\dfrac{3}{8}",
    "r_w4_p12": r"\dfrac{1}{2}",
    "r_w4_p58": r"\dfrac{5}{8}",
    "r_w4_p35": r"\dfrac{3}{5}",
    "r_w5_ang": r"(3x+10)^{\circ}\qquad\text{and}\qquad (2x-5)^{\circ}",
    "r_w5_sys": r"x+y=12\qquad\text{and}\qquad x-y=4",
    "r_w3_pct": r"40\%\ \text{of a number is}\ 60",
}

keys = list(E)
doc = [r"\documentclass[12pt]{article}", r"\usepackage[active,tightpage]{preview}",
       r"\usepackage{amsmath,amssymb}", r"\usepackage[dvipsnames]{xcolor}",
       r"\setlength\PreviewBorder{1.5pt}",
       r"\definecolor{ink}{HTML}{%s}" % INK, r"\begin{document}"]
for k in keys:
    doc.append(r"\begin{preview}$\color{ink}\displaystyle %s$\end{preview}" % E[k])
doc.append(r"\end{document}")

tex = os.path.join(TMP, "gat.tex")
open(tex, "w").write("\n".join(doc))
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory", TMP, tex], capture_output=True, text=True)
if r.returncode:
    print(r.stdout[-3000:]); raise SystemExit("pdflatex failed")
subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(DPI),
                os.path.join(TMP, "gat.pdf"), os.path.join(TMP, "p")], check=True)

pages = sorted(f for f in os.listdir(TMP) if f.startswith("p-") and f.endswith(".png"))
assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} expressions"
idx = {}
for k, p in zip(keys, pages):
    im = Image.open(os.path.join(TMP, p)).convert("RGBA")
    dst = os.path.join(OUT, k + ".png"); im.save(dst)
    idx[k] = {"file": dst, "win": im.width / DPI, "hin": im.height / DPI,
              "aspect": im.width / im.height}
json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
print(len(idx), "expressions typeset")
