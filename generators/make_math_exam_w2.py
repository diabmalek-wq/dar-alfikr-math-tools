"""
Week 2 exam-prep expressions. Real LaTeX (pdflatex + Computer Modern),
tight-cropped transparent PNG at 500 dpi, then a 260 dpi document copy.
Keys: g<item>_<part> for GAT, s<item>_<part> for SAAT.
"""
import json, os, shutil, subprocess
from PIL import Image

OUT, DOC, TMP = "math_ex2", "math_ex2_doc", ".tex_ex2"
for d in (OUT, DOC, TMP): shutil.rmtree(d, ignore_errors=True); os.makedirs(d)

INK = "222E2D"

E = {}
def add(k, tex): E[k] = tex

# ---------------- GAT ----------------
add("g12_s", r"2^{5}\times 2^{3}\div 2^{6}")
add("g13_s", r"\sqrt{0.49}")
add("g17_a", r"5\sqrt{2}");  add("g17_b", r"5\sqrt{3}")
add("g17_c", r"10");         add("g17_d", r"10\sqrt{3}")
add("g18_a", r"3\pi");  add("g18_b", r"6\pi");  add("g18_c", r"12\pi");  add("g18_d", r"36\pi")
add("g23_a", r"\dfrac{1}{5}");  add("g23_b", r"\dfrac{3}{10}")
add("g23_c", r"\dfrac{1}{2}");  add("g23_d", r"\dfrac{3}{5}")
add("g23_e", r"\dfrac{2}{5}")
add("g24_a", r"\dfrac{1}{4}");  add("g24_b", r"\dfrac{1}{3}")
add("g24_c", r"\dfrac{1}{2}");  add("g24_d", r"\dfrac{3}{4}")
add("g1_s",  r"f(x)=3x-5")
add("g3_s",  r"f(x)=x^{2}-4x")
add("g4_s",  r"g(x)=2x+1")
add("g5_s",  r"f(x)=\dfrac{x+2}{x-3}")

# ---------------- SAAT ----------------
add("s1_s", r"\sqrt{50}")
add("s1_a", r"5\sqrt{2}"); add("s1_b", r"2\sqrt{5}"); add("s1_c", r"25\sqrt{2}"); add("s1_d", r"10\sqrt{5}")
add("s2_s", r"\sqrt[3]{54}")
add("s2_a", r"3\sqrt[3]{2}"); add("s2_b", r"2\sqrt[3]{3}"); add("s2_c", r"6"); add("s2_d", r"9\sqrt[3]{2}")
add("s3_s", r"\sqrt{18}+\sqrt{8}")
add("s3_a", r"5\sqrt{2}"); add("s3_b", r"\sqrt{26}"); add("s3_c", r"5\sqrt{10}"); add("s3_d", r"6\sqrt{2}")
add("s4_s", r"\dfrac{6}{\sqrt{3}}")
add("s4_a", r"2\sqrt{3}"); add("s4_b", r"6\sqrt{3}"); add("s4_c", r"3\sqrt{2}"); add("s4_d", r"\dfrac{2}{\sqrt{3}}")
add("s5_s", r"\bigl(2+\sqrt{3}\bigr)\bigl(2-\sqrt{3}\bigr)")
add("s6_s", r"f(x)=\sqrt{2x-6}")
add("s6_a", r"x\geq 3"); add("s6_b", r"x>3"); add("s6_c", r"x\geq 6"); add("s6_d", r"x\leq 3")
add("s7_s", r"f(x)=\sqrt[3]{x-5}")
add("s7_a", r"x\geq 5"); add("s7_b", r"x\leq 5"); add("s7_d", r"x\neq 5")
add("s8_s", r"\sqrt{x+7}=x-5")
add("s9_s", r"\sqrt{3x+1}=4")
add("s10_s", r"\sqrt[3]{2x-1}=3")
add("s11_s", r"x^{\frac{3}{2}}=27")
add("s12_s", r"x^{\frac{1}{2}}\cdot x^{\frac{1}{3}}")
add("s12_a", r"x^{\frac{5}{6}}"); add("s12_b", r"x^{\frac{1}{6}}")
add("s12_c", r"x^{\frac{2}{5}}"); add("s12_d", r"x^{\frac{6}{5}}")
add("s13_s", r"\sqrt{49x^{4}}\quad (x>0)")
add("s13_a", r"7x^{2}"); add("s13_b", r"49x^{2}"); add("s13_c", r"7x^{4}"); add("s13_d", r"7x")
add("s14_s", r"\sqrt{x+2}=x-4")
add("s15_s", r"\dfrac{x^{2}-9}{x+3}")
add("s15_a", r"x-3"); add("s15_b", r"x+3"); add("s15_c", r"-3"); add("s15_d", r"x^{2}-3")
add("s16_s", r"\dfrac{x+1}{x^{2}-4}")
add("s16_a", r"x=-1"); add("s16_b", r"x=2\ \text{only}")
add("s16_c", r"x=\pm 2"); add("s16_d", r"x=\pm 4")
add("s17_s", r"(-3,\,4)\ \ \text{and}\ \ (5,\,-2)")
add("s17_a", r"(1,\,1)"); add("s17_b", r"(2,\,2)"); add("s17_c", r"(4,\,3)"); add("s17_d", r"(1,\,3)")
add("s18_s", r"(2,\,-1)\ \ \text{and}\ \ (6,\,7)")
add("s18_b", r"\tfrac{1}{2}"); add("s18_c", r"-2")
add("s20_s", r"(3,\,-5)")
add("s20_a", r"(-3,\,-5)"); add("s20_b", r"(3,\,5)"); add("s20_c", r"(-3,\,5)"); add("s20_d", r"(-5,\,3)")
add("s21_s", r"2x^{2}-4x+5=0")
add("s22_s", r"i^{\,26}")
add("s22_c", r"i"); add("s22_d", r"-i")
add("s23_s", r"a_{1}=5,\ \ d=3")
add("s24_s", r"\log_{2}32")

keys = list(E)
doc = [r"\documentclass[12pt]{article}", r"\usepackage[active,tightpage]{preview}",
       r"\usepackage{amsmath,amssymb}", r"\usepackage[dvipsnames]{xcolor}",
       r"\setlength\PreviewBorder{1.5pt}",
       r"\definecolor{ink}{HTML}{%s}" % INK, r"\begin{document}"]
for k in keys:
    doc.append(r"\begin{preview}$\color{ink}\displaystyle %s$\end{preview}" % E[k])
doc.append(r"\end{document}")

tex = os.path.join(TMP, "ex2.tex")
open(tex, "w").write("\n".join(doc))
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory", TMP, tex], capture_output=True, text=True)
if r.returncode:
    print(r.stdout[-3000:]); raise SystemExit("pdflatex failed")
subprocess.run(["pdftocairo", "-png", "-transp", "-r", "500",
                os.path.join(TMP, "ex2.pdf"), os.path.join(TMP, "p")], check=True)
pages = sorted(f for f in os.listdir(TMP) if f.startswith("p-") and f.endswith(".png"))
assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} keys"
idx, didx = {}, {}
for k, p in zip(keys, pages):
    im = Image.open(os.path.join(TMP, p)).convert("RGBA")
    im.save(os.path.join(OUT, k + ".png"))
    idx[k] = {"file": f"{OUT}/{k}.png", "win": im.width / 500, "hin": im.height / 500,
              "aspect": im.width / im.height}
    d = im.resize((max(1, int(im.width * 260 / 500)), max(1, int(im.height * 260 / 500))), Image.LANCZOS)
    d.save(os.path.join(DOC, k + ".png"))
    didx[k] = dict(idx[k], file=f"{DOC}/{k}.png")
json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
json.dump(E, open(os.path.join(OUT, "_tex.json"), "w"), indent=1)
json.dump(didx, open(os.path.join(DOC, "_index.json"), "w"), indent=1)
print(len(idx), "expressions typeset")
