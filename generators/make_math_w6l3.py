"""
Gr11 T6 L6-3 Logarithms. Same pipeline as make_math_w5core.py — real LaTeX
(pdflatex + Computer Modern), tight-cropped transparent PNG, rendered at
500 dpi for slides and 260 dpi for documents. Prefix l_.
"""
import json, os, shutil, subprocess
from PIL import Image

TMP = ".tex_w6l3"
shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(TMP)

INK, DEEP, WHITE, MAROON = "222E2D", "0E4F4C", "FFFFFF", "8A1B17"

EXPR = {
    "l_title_w": (r"\log_b x = y \iff b^{y}=x", WHITE),
    "l_def":     (r"\log_b x = y \iff b^{y}=x", INK),

    "l_exp1":    (r"2^{x}=8", INK),
    "l_exp2":    (r"10^{x}=1000", INK),

    # diagnose
    "l_d1":      (r"2^{5}=\underline{\qquad}", INK),
    "l_d2":      (r"10^{3}=\underline{\qquad}", INK),
    "l_d3":      (r"f(x)=2(3)^{x}.\quad f(0)=\underline{\qquad}", INK),
    "l_d4":      (r"\text{Solve for }x:\ \ 2^{x}=16", INK),
    "l_d5":      (r"\text{Between which two integers is}\ \ \log_2 20\,?", INK),

    # instruction 1 — understanding and evaluating logs / converting forms
    "l_conv1":   (r"b^{y}=x \ \ \Longleftrightarrow\ \ \log_b x = y", INK),
    "l_ex_eval1": (r"\log_2 8 = 3\quad\text{because}\quad 2^{3}=8", INK),
    "l_ex_eval2": (r"\log_5 1 = 0\quad\text{because}\quad 5^{0}=1", INK),
    "l_ex_conv1": (r"3^{4}=81 \ \ \Longrightarrow\ \ \log_3 81 = 4", INK),
    "l_ex_conv2": (r"\log_7 49 = 2 \ \ \Longrightarrow\ \ 7^{2}=49", INK),
    "l_row_q1":   (r"\log_4 64 = \underline{\qquad}", INK),
    "l_row_q2":   (r"\log_{10} 0.01 = \underline{\qquad}", INK),
    "l_row_q3":   (r"5^{3}=125 \ \Rightarrow\ \log_{\square}\square=\square", INK),

    # instruction 2 — common and natural logs, technology
    "l_common":  (r"\log_{10}x = \log x", INK),
    "l_natural": (r"\log_e x = \ln x", INK),
    "l_e_def":   (r"e \approx 2.71828\ldots", INK),
    "l_calc1":   (r"\log 50 \approx 1.699", INK),
    "l_calc2":   (r"\ln 50 \approx 3.912", INK),
    "l_oom1":    (r"\log(6.3\times10^{8}) \approx 8.8", INK),
    "l_oom2":    (r"\text{order of magnitude} \approx 9", INK),

    # instruction 3 — logs to solve exponential-model problems
    "l_model1":  (r"A = A_0\,b^{t}", INK),
    "l_model2":  (r"b^{t}=\dfrac{A}{A_0}\ \Longrightarrow\ t=\log_b\!\left(\dfrac{A}{A_0}\right)", INK),
    "l_model_w": (r"t=\log_b\!\left(\dfrac{A}{A_0}\right)", WHITE),

    # quick check, guided, gate
    "l_qc":      (r"\log_3 27 = \underline{\qquad}", INK),
    "l_g1":      (r"\log_2 32 = \underline{\qquad}", INK),
    "l_g2":      (r"\log_{10} 10\,000 = \underline{\qquad}", INK),
    "l_gate":    (r"\log_5 125 = \underline{\qquad}", INK),
    "l_gate_w":  (r"\log_5 125 = \underline{\qquad}", WHITE),
    "l_gate2":   (r"\ln e^{4} = \underline{\qquad}", INK),

    # worksheet / routes
    "l_ws1":     (r"\log_2 16 = \underline{\qquad}", INK),
    "l_ws2":     (r"\log_{10} 1000 = \underline{\qquad}", INK),
    "l_ws3":     (r"6^{x}=216", INK),
    "l_ws4":     (r"\log_4 x = 3", INK),

    # Saudi context — NEOM data-center growth, solved with logs
    "l_ctx_w":   (r"t=\log_{1.18}\!\left(\dfrac{50\,000}{6\,000}\right)", WHITE),
    "l_ctx":     (r"6\,000(1.18)^{t}=50\,000", INK),
    "l_ctx2":    (r"t=\log_{1.18}\!\left(\dfrac{50\,000}{6\,000}\right)\approx 13.1\ \text{years}", INK),

    # exam cards
    "l_ex_saat": (r"\log_4 64 = \underline{\qquad}", INK),
    "l_ex_sat":  (r"500(1.06)^{t}=1\,000", INK),
    "l_ex_gat":  (r"\log_2 512 = \underline{\qquad}", INK),
}

keys = list(EXPR)
doc = [r"\documentclass[12pt]{article}", r"\usepackage[active,tightpage]{preview}",
       r"\usepackage{amsmath,amssymb,array}", r"\usepackage[dvipsnames]{xcolor}",
       r"\setlength\PreviewBorder{1.5pt}"]
for k, (_, c) in EXPR.items():
    doc.append(r"\definecolor{c%s}{HTML}{%s}" % (k.replace("_", ""), c))
doc.append(r"\begin{document}")
for k in keys:
    doc.append(r"\begin{preview}$\color{c%s}\displaystyle %s$\end{preview}"
               % (k.replace("_", ""), EXPR[k][0]))
doc.append(r"\end{document}")

tex = os.path.join(TMP, "w6l3.tex")
open(tex, "w").write("\n".join(doc))
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory", TMP, tex], capture_output=True, text=True)
if r.returncode:
    print(r.stdout[-4000:])
    raise SystemExit("pdflatex failed")

for out, dpi in (("math_w6l3", 500), ("math_w6l3_doc", 260)):
    shutil.rmtree(out, ignore_errors=True)
    os.makedirs(out)
    stem = os.path.join(TMP, f"p{dpi}")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(TMP, "w6l3.pdf"), stem], check=True)
    pages = sorted(f for f in os.listdir(TMP)
                   if f.startswith(f"p{dpi}-") and f.endswith(".png"))
    assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} expressions"
    idx = {}
    for k, p in zip(keys, pages):
        im = Image.open(os.path.join(TMP, p)).convert("RGBA")
        dst = os.path.join(out, k + ".png")
        im.save(dst)
        idx[k] = {"file": dst, "win": im.width / dpi, "hin": im.height / dpi,
                  "aspect": im.width / im.height}
    json.dump(idx, open(os.path.join(out, "_index.json"), "w"), indent=1)
    print(f"{len(idx)} expressions -> {out} @ {dpi} dpi")
