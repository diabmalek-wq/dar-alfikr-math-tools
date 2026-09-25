"""LaTeX expressions for the Grade 11 Lesson 5-2 pre-session video.
Same pipeline as the decks and worksheets (spec §12) — real LaTeX, Computer
Modern, transparent PNG. Canva cannot do this; a video that is 90% notation
has to be typeset properly or it undercuts every other resource.
"""
import json, os, shutil, subprocess
from PIL import Image

OUT, TMP, DPI = "math_g11vid", ".tex_g11vid", 500
shutil.rmtree(OUT, ignore_errors=True); shutil.rmtree(TMP, ignore_errors=True)
os.makedirs(OUT); os.makedirs(TMP)

NAVY = "1F3864"
MAROON = "AD2A22"
TEAL = "17A199"

# key: (latex, colour)
E = {
    # --- the bridge, general form -------------------------------------------
    "gen_rad":   (r"\sqrt[n]{x^{m}}", NAVY),
    "gen_exp":   (r"x^{\frac{m}{n}}", NAVY),
    "gen_both":  (r"\sqrt[n]{x^{m}}\;=\;x^{\frac{m}{n}}", NAVY),
    "gen_n":     (r"n", MAROON),
    "gen_m":     (r"m", TEAL),

    # --- anatomy of a radical ------------------------------------------------
    "anat":      (r"\sqrt[n]{x^{m}}", NAVY),

    # --- conversion 1 : cube root of 8 --------------------------------------
    "c1_a":      (r"\sqrt[3]{8}", NAVY),
    "c1_b":      (r"\sqrt[3]{8}\;=\;8^{\frac{1}{3}}", NAVY),
    "c1_c":      (r"\sqrt[3]{8}\;=\;8^{\frac{1}{3}}\;=\;2", NAVY),

    # --- conversion 2 : x to the two-fifths ---------------------------------
    "c2_a":      (r"x^{\frac{2}{5}}", NAVY),
    "c2_b":      (r"x^{\frac{2}{5}}\;=\;\sqrt[5]{x^{2}}", NAVY),

    # --- conversion 3 : cube root of 27 squared -----------------------------
    "c3_a":      (r"\sqrt[3]{27^{2}}", NAVY),
    "c3_b":      (r"\sqrt[3]{27^{2}}\;=\;27^{\frac{2}{3}}", NAVY),
    "c3_c":      (r"\sqrt[3]{27^{2}}\;=\;27^{\frac{2}{3}}\;=\;9", NAVY),

    # --- recap ---------------------------------------------------------------
    "recap":     (r"\sqrt[n]{x^{m}}\;=\;x^{\frac{m}{n}}", NAVY),
}

# Highlighted variants. Each colours ONE part of an otherwise-navy expression,
# so the build script can find that part's exact pixel box by looking for the
# highlight colour — no hand-tuned anchor coordinates, no guessing where the
# index sits inside a rendered radical.
HL = {
    "exp_n":  r"x^{\frac{m}{\color{hlA}n}}",          # denominator of exponent
    "exp_m":  r"x^{\frac{\color{hlB}m}{n}}",          # numerator of exponent
    "rad_n":  r"\sqrt[{\color{hlA}n}]{x^{m}}",        # index of radical
    "rad_m":  r"\sqrt[n]{x^{\color{hlB}m}}",          # power inside radical
    "rad_rc": r"\sqrt[n]{\color{hlB}x^{m}}",          # the radicand
}

for k, tex in HL.items():
    E["hl_" + k] = (tex, NAVY)

keys = list(E)
doc = [r"\documentclass[12pt]{article}", r"\usepackage[active,tightpage]{preview}",
       r"\usepackage{amsmath,amssymb}", r"\usepackage[dvipsnames]{xcolor}",
       r"\setlength\PreviewBorder{2pt}",
       # the two highlight colours the build script searches for
       r"\definecolor{hlA}{HTML}{%s}" % MAROON,
       r"\definecolor{hlB}{HTML}{%s}" % TEAL,
       r"\begin{document}"]
for k in keys:
    tex, col = E[k]
    doc.append(r"\definecolor{ink%s}{HTML}{%s}" % (k.replace("_", ""), col))
    doc.append(r"\begin{preview}$\color{ink%s}\displaystyle %s$\end{preview}"
               % (k.replace("_", ""), tex))
doc.append(r"\end{document}")

tex_path = os.path.join(TMP, "v.tex")
open(tex_path, "w").write("\n".join(doc))
r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                    "-output-directory", TMP, tex_path],
                   capture_output=True, text=True)
if r.returncode:
    print(r.stdout[-3000:]); raise SystemExit("pdflatex failed")
subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(DPI),
                os.path.join(TMP, "v.pdf"), os.path.join(TMP, "p")], check=True)

pages = sorted(f for f in os.listdir(TMP) if f.startswith("p-") and f.endswith(".png"))
assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} expressions"
idx = {}
for k, p in zip(keys, pages):
    im = Image.open(os.path.join(TMP, p)).convert("RGBA")
    dst = os.path.join(OUT, k + ".png"); im.save(dst)
    idx[k] = {"file": dst, "w": im.width, "h": im.height}
json.dump(idx, open(os.path.join(OUT, "_index.json"), "w"), indent=1)
print(len(idx), "expressions typeset")
