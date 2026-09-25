"""LaTeX expressions for the SAT Booklet build -- same pdflatex pipeline as
make_math_sim.py (Computer Modern, transparent PNG)."""
import json, os, shutil, subprocess
from PIL import Image

INK = "222E2D"
E = json.load(open("sat_full_mathsrc.json", encoding="utf-8"))


def render(out_dir, dpi):
    tmp = f".tex_satfull_{dpi}"
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
    tex = os.path.join(tmp, "satb.tex")
    open(tex, "w").write("\n".join(doc))
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-output-directory", tmp, tex], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-2500:]); raise SystemExit("pdflatex failed")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(tmp, "satb.pdf"), os.path.join(tmp, "p")], check=True)
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


render("math_satfull_doc", 260)
