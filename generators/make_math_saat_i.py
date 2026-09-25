"""LaTeX for part I of the SAAT booklet — the eleventh ETEC sample paper.

Rendered into the SAME index the earlier parts use.
"""
import json, os, subprocess, tempfile
from PIL import Image

INK = "222E2D"

FR = lambda a, b: r"\dfrac{%s}{%s}" % (a, b)

E = {
    # ------------------------------------------ functions and expressions
    "i_sh1": r"x^{2}-8x+16",
    "i_sh2": r"x^{2}+8x+16",
    "i_sh3": r"x^{2}-16",
    "i_sh4": r"x^{2}+16",
    "i_nr1": FR(r"\sqrt{x}+1", r"x^{2}+4"),
    "i_nr2": FR(r"\sqrt{7}\,x+1", r"x^{2}+4"),
    "i_nr3": FR(r"x^{5}-3x+2", r"x-6"),
    "i_nr4": FR("3", "x"),
    "i_ri1": r"y\leq\sqrt{x+2}",
    "i_ri2": r"y\geq\sqrt{x+2}",
    "i_ri3": r"y\leq\sqrt{x-2}",
    "i_ri4": r"y\geq\sqrt{x-2}",
    "i_ar1": r"7\sqrt{3}",
    "i_ar2": r"11\sqrt{3}",
    "i_ar3": r"\sqrt{111}",
    "i_ar4": r"9\sqrt{3}",

    # ----------------------------------------------------- complex numbers
    "i_cb1": r"8+i",
    "i_cb2": r"4+i",
    "i_cb3": r"8+7i",
    "i_cb4": r"6-2i",
    "i_pw1": r"{-8i}",
    "i_pw2": r"8i",
    "i_pw3": r"{-8}",
    "i_pw4": r"8",

    # -------------------------------------------------------- trigonometry
    "i_ce1": r"{-\dfrac{\sqrt{3}}{2}}",
    "i_ce2": r"\dfrac{\sqrt{3}}{2}",
    "i_ce3": r"{-\dfrac{1}{2}}",
    "i_ce4": r"\dfrac{1}{2}",
    "i_ls1": r"7\sqrt{6}",
    "i_ls2": r"\dfrac{14\sqrt{6}}{3}",
    "i_ls3": r"14",
    "i_ls4": r"7\sqrt{2}",
    "i_ic1": FR(r"\pi", "3"),
    "i_ic2": FR(r"\pi", "6"),
    "i_ic3": FR(r"\pi", "2"),
    "i_ic4": FR(r"\pi", "4"),

    # ---------------------------------------------- counting & probability
    "i_sa1": FR("1", "120"),
    "i_sa2": FR("1", "5"),
    "i_sa3": FR("1", "25"),
    "i_sa4": FR("1", "20"),
    "i_ms1": FR("1", "2"),
    "i_ms2": FR("1", "4"),
    "i_ms3": FR("1", "8"),
    "i_ms4": FR(r"\sqrt{2}", "2"),
    "i_ec1": FR("1", "10"),
    "i_ec2": FR("1", "20"),
    "i_ec3": FR("2", "5"),
    "i_ec4": FR("1", "120"),
    "i_co1": FR("2", "21"),
    "i_co2": FR("1", "14"),
    "i_co3": FR("8", "9"),
    "i_co4": FR("1", "63"),
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
    tex = os.path.join(tmp, "saati.tex")
    open(tex, "w").write("\n".join(doc))
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-output-directory", tmp, tex], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-3000:])
        raise SystemExit("pdflatex failed")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(tmp, "saati.pdf"), os.path.join(tmp, "r")], check=True)
    pages = sorted(f for f in os.listdir(tmp) if f.startswith("r-") and f.endswith(".png"))
    assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} expressions"
    for k, p in zip(keys, pages):
        im = Image.open(os.path.join(tmp, p)).convert("RGBA")
        dst = os.path.join(out_dir, k + ".png")
        im.save(dst)
        idx[k] = {"file": dst, "win": im.width / dpi, "hin": im.height / dpi,
                  "aspect": im.width / im.height}
    json.dump(idx, open(idx_path, "w"), indent=1)
    print(f"{len(keys)} part-I expressions added; index now holds {len(idx)}")


if __name__ == "__main__":
    render()
