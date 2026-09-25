"""
Gr11 T6 L6-4 Logarithmic Functions. Same pipeline as make_math_w6l3.py — real
LaTeX (pdflatex + Computer Modern), tight-cropped transparent PNG, rendered at
500 dpi for slides and 260 dpi for documents. Prefix m_.
"""
import json, os, shutil, subprocess
from PIL import Image

TMP = ".tex_w6l4"
shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(TMP)

INK, DEEP, WHITE, MAROON = "222E2D", "0E4F4C", "FFFFFF", "8A1B17"

EXPR = {
    "m_title_w": (r"f(x)=\log_b x \quad\Longleftrightarrow\quad f^{-1}(x)=b^{x}", WHITE),
    "m_def":     (r"f(x)=\log_b x,\quad b>0,\ b\neq 1", INK),

    # prior knowledge
    "m_prior_log":  (r"\log_b x = y \iff b^{y}=x", INK),
    "m_prior_exp":  (r"g(x)=2^{x}", INK),
    "m_prior_inv":  (r"(a,b)\in f \iff (b,a)\in f^{-1}", INK),

    # diagnose
    "m_d1":  (r"\log_2 8 = \underline{\qquad}", INK),
    "m_d2":  (r"g(x)=2^{x}", INK),
    "m_d3":  (r"f(x)=x+5", INK),
    "m_d4":  (r"f^{-1}(x)\ \text{reflects}\ f(x)\ \text{across}\ y=x", INK),
    "m_d5":  (r"g(x)=3^{x}-2", INK),

    # instruction 1 — key features of logarithmic functions
    "m_kf_form":   (r"f(x)=\log_b x", INK),
    "m_kf_dom":    (r"\text{Domain: } x>0", INK),
    "m_kf_ran":    (r"\text{Range: all reals}", INK),
    "m_kf_xint":   (r"\text{$x$-intercept: } (1,0),\ \ \text{since } \log_b 1 = 0", INK),
    "m_kf_va":     (r"\text{Vertical asymptote: } x=0", INK),
    "m_kf_end":    (r"\text{as } x\to 0^{+},\ f(x)\to -\infty; \quad \text{as } x\to\infty,\ f(x)\to\infty", INK),
    "m_row_q1":    (r"f(x)=\log_5 x:\ \ \text{domain, range, asymptote, intercept}", INK),
    "m_row_q2":    (r"g(x)=\log_2(x+3):\ \ \text{asymptote } x=\underline{\qquad}", INK),

    # instruction 2 — inverse properties
    "m_ip1":       (r"\log_b\!\left(b^{x}\right)=x \quad \text{for all } x", INK),
    "m_ip1_bare":  (r"\log_b\!\left(b^{x}\right)=x", INK),
    "m_ip2_bare":  (r"b^{\log_b x}=x", INK),
    "m_ip2":       (r"b^{\log_b x}=x \quad \text{for } x>0", INK),
    "m_ip_check1": (r"\log_2\!\left(2^{5}\right)=5", INK),
    "m_ip_check2": (r"3^{\log_3 7}=7", INK),
    "m_swap":      (r"\text{domain of } \log_b x = \text{range of } b^{x};\quad \text{range of } \log_b x = \text{domain of } b^{x}", INK),

    # instruction 3 — graphing transformations, writing/interpreting inverses
    "m_shift1":    (r"g(x)=\log_b(x)+k \ \ \Rightarrow\ \ \text{vertical shift, asymptote stays } x=0", INK),
    "m_shift2":    (r"g(x)=\log_b(x-h) \ \ \Rightarrow\ \ \text{asymptote moves to } x=h", INK),
    "m_inv_steps": (r"y=\log_3(x-1)\ \ \to\ \ x=\log_3(y-1)\ \ \to\ \ 3^{x}=y-1\ \ \to\ \ y=3^{x}+1", INK),
    "m_inv_ans":   (r"f(x)=\log_3(x-1)\ \ \Longrightarrow\ \ f^{-1}(x)=3^{x}+1", INK),

    # quick check
    "m_qc": (r"f(x)=\log_5 x", INK),

    # guided
    "m_g1": (r"f(x)=\log_3 x", INK),
    "m_g2": (r"f(x)=\log_2(x)+4", INK),

    # worksheet / routes
    "m_ws1": (r"f(x)=\log_4 x", INK),
    "m_ws2": (r"g(x)=\log_2(x-3)", INK),
    "m_ws3": (r"h(x)=\log_5(x)+2", INK),
    "m_ws4": (r"j(x)=\log_3(x+1)-1", INK),
    "m_inv_ws1": (r"f(x)=\log_2 x\ \ \Rightarrow\ \ f^{-1}(x)=\underline{\qquad}", INK),
    "m_inv_ws2": (r"g(x)=\log_5(x)-3\ \ \Rightarrow\ \ g^{-1}(x)=\underline{\qquad}", INK),

    # Saudi context — desalination-plant water pH
    "m_ctx_w":   (r"\text{pH}=-\log_{10}[\text{H}^{+}]", WHITE),
    "m_ctx1":    (r"\text{pH}=-\log_{10}[\text{H}^{+}]", INK),
    "m_ctx2":    (r"[\text{H}^{+}]=4\times10^{-8}\ \text{mol/L}", INK),
    "m_ctx3":    (r"\text{pH}=-\log_{10}\!\left(4\times10^{-8}\right)\approx 7.40", INK),
    "m_ctx_inv": (r"[\text{H}^{+}]=10^{-\text{pH}}", INK),

    # mastery gate
    "m_gate1_w": (r"g(x)=\log_2(x+5)", WHITE),
    "m_gate1":   (r"g(x)=\log_2(x+5)", INK),
    "m_gate2":   (r"f(x)=\log_4(x)-1\ \ \Rightarrow\ \ f^{-1}(x)=\underline{\qquad}", INK),

    # exam cards
    "m_ex_saat": (r"\text{State the vertical asymptote of } f(x)=\log_3(x-4).", INK),
    "m_ex_sat":  (r"\text{Find the inverse of } f(x)=\log_2(x)+5.", INK),
    "m_ex_gat":  (r"\text{Domain of } f(x)=\log_5(x-9)\ \text{is}\ \underline{\qquad}", INK),
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

tex = os.path.join(TMP, "w6l4.tex")
open(tex, "w").write("\n".join(doc))
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory", TMP, tex], capture_output=True, text=True)
if r.returncode:
    print(r.stdout[-4000:])
    raise SystemExit("pdflatex failed")

for out, dpi in (("math_w6l4", 500), ("math_w6l4_doc", 260)):
    shutil.rmtree(out, ignore_errors=True)
    os.makedirs(out)
    stem = os.path.join(TMP, f"p{dpi}")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(TMP, "w6l4.pdf"), stem], check=True)
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
