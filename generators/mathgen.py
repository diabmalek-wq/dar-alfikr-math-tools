"""Render LaTeX expressions to tight transparent PNGs (slides 500 dpi, docs 260 dpi)."""
import json, os, shutil, subprocess
from PIL import Image

def render(EXPR, tag, out_prefix):
    TMP = f".tex_{tag}"
    shutil.rmtree(TMP, ignore_errors=True); os.makedirs(TMP)
    keys = list(EXPR)
    doc = [r"\documentclass[12pt]{article}", r"\usepackage[active,tightpage]{preview}",
           r"\usepackage{amsmath,amssymb,array}", r"\usepackage[dvipsnames]{xcolor}",
           r"\setlength\PreviewBorder{1.5pt}"]
    for k, (_, c) in EXPR.items():
        doc.append(r"\definecolor{c%s}{HTML}{%s}" % (k.replace("_", ""), c))
    doc.append(r"\begin{document}")
    for k in keys:
        doc.append(r"\begin{preview}$\color{c%s}\displaystyle %s$\end{preview}" % (k.replace("_", ""), EXPR[k][0]))
    doc.append(r"\end{document}")
    tex = os.path.join(TMP, f"{tag}.tex"); open(tex, "w").write("\n".join(doc))
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "-output-directory", TMP, tex], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-3000:]); raise SystemExit("pdflatex failed")
    for out, dpi in ((out_prefix, 500), (out_prefix + "_doc", 260)):
        shutil.rmtree(out, ignore_errors=True); os.makedirs(out)
        stem = os.path.join(TMP, f"p{dpi}")
        subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi), os.path.join(TMP, f"{tag}.pdf"), stem], check=True)
        pages = sorted(f for f in os.listdir(TMP) if f.startswith(f"p{dpi}-") and f.endswith(".png"))
        assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} expressions"
        idx = {}
        for k, p in zip(keys, pages):
            im = Image.open(os.path.join(TMP, p)).convert("RGBA")
            dst = os.path.join(out, k + ".png"); im.save(dst)
            idx[k] = {"file": dst, "win": im.width / dpi, "hin": im.height / dpi, "aspect": im.width / im.height}
        json.dump(idx, open(os.path.join(out, "_index.json"), "w"), indent=1)
        print(f"{len(idx)} expressions -> {out} @ {dpi} dpi")
