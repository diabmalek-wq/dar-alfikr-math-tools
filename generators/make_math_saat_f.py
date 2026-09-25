"""LaTeX for part F of the SAAT booklet — polar, complex, vectors, matrices and
the algebra the official sample papers lean on.

Rendered into the SAME index the earlier parts use.
"""
import json, os, subprocess, tempfile
from PIL import Image

INK = "222E2D"

M = lambda body, cols="cc": r"\left[\begin{array}{%s}%s\end{array}\right]" % (cols, body)
DET = lambda body, cols="cc": r"\left|\begin{array}{%s}%s\end{array}\right|" % (cols, body)
POL = lambda r, d: r"%s\left(\cos %s^{\circ}+i\sin %s^{\circ}\right)" % (r, d, d)

E = {
    # ------------------------------------------------------------- polar
    "f_pc1": r"r=24\sin\theta",
    "f_pc2": r"r=24\cos\theta",
    "f_pc3": r"r=12\sin\theta",
    "f_pc4": r"r=12\cos\theta",
    "f_pf1": POL("3", "30"),
    "f_pf2": r"3\left(\sin 30^{\circ}+i\cos 30^{\circ}\right)",
    "f_pf3": r"\cos 30^{\circ}+i\sin 30^{\circ}",
    "f_pf4": POL("30", "3"),
    "f_ar1": r"\dfrac{\pi}{3}",
    "f_ar2": r"\dfrac{\pi}{6}",
    "f_ar3": r"\dfrac{\pi}{2}",
    "f_ar4": r"\dfrac{\pi}{4}",
    "f_pp1": POL("12", "60"),
    "f_pp2": POL("12", "800"),
    "f_pp3": POL("7", "60"),
    "f_pp4": POL("12", "20"),
    "f_pq1": POL("2", "30"),
    "f_pq2": r"2\left(\cos({-30^{\circ}})+i\sin({-30^{\circ}})\right)",
    "f_pq3": POL("2", "130"),
    "f_pq4": POL("5", "30"),
    "f_dm1": r"4.5+4.5\sqrt{3}\,i",
    "f_dm2": r"3+3\sqrt{3}\,i",
    "f_dm3": r"\dfrac{9\sqrt{3}}{2}+\dfrac{9}{2}i",
    "f_dm4": r"4.5\sqrt{3}+4.5i",
    "f_pl1": r"r=6\csc\theta",
    "f_pl2": r"r=6\sec\theta",
    "f_pl3": r"r=3\csc\theta",
    "f_pl4": r"r=\dfrac{\sin\theta}{6}",
    "f_cr1": r"x^{2}+y^{2}=64",
    "f_cr2": r"x^{2}+y^{2}=8",
    "f_cr3": r"x+y=64",
    "f_cr4": r"x^{2}-y^{2}=64",
    "f_nr1": r"\left({-2},\ {-2\sqrt{3}}\right)",
    "f_nr2": r"\left(2,\ 2\sqrt{3}\right)",
    "f_nr3": r"\left({-2\sqrt{3}},\ {-2}\right)",
    "f_nr4": r"\left(2\sqrt{3},\ 2\right)",
    "f_pd1": r"2\sqrt{13}",
    "f_pd2": r"\sqrt{148}",
    "f_pd3": r"2",
    "f_pd4": r"10",

    # ----------------------------------------------------------- vectors
    "f_rv1": r"\left\langle 7,\ 3\right\rangle",
    "f_rv2": r"\left\langle {-1},\ 12\right\rangle",
    "f_rv3": r"\left\langle 7,\ 5\right\rangle",
    "f_rv4": r"\left\langle 13,\ {-11}\right\rangle",
    "f_uv31": r"\left\langle \tfrac{2}{7},\ {-\tfrac{3}{7}},\ \tfrac{6}{7}\right\rangle",
    "f_uv32": r"\left\langle \tfrac{2}{49},\ {-\tfrac{3}{49}},\ \tfrac{6}{49}\right\rangle",
    "f_uv33": r"\left\langle \tfrac{2}{\sqrt{13}},\ {-\tfrac{3}{\sqrt{13}}},\ \tfrac{6}{\sqrt{13}}\right\rangle",
    "f_uv34": r"\left\langle \tfrac{1}{3},\ {-\tfrac{1}{2}},\ 1\right\rangle",

    # ---------------------------------------------------------- matrices
    "f_mc": (r"A=" + M(r"1 & 3\\ {-4} & 6", "rr") + r",\quad B=" +
             M(r"2 & 5\\ 0 & {-1}", "rr")),
    "f_dk": DET(r"4 & {-3}\\ {-2} & k", "rr") + r"\;=\;26",
    "f_me": (r"3X-B=" + M(r"1 & 0\\ 7 & 2", "rr") + r",\quad B=" +
             M(r"2 & 4\\ 5 & 1", "rr")),
    "f_mv": M(r"2 & {-1}\\ 5 & 2", "rr") + M(r"3\\ 4", "r"),
    "f_mv1": M(r"2\\ 23", "r"),
    "f_mv2": M(r"6\\ 8", "r"),
    "f_mv3": M(r"2 & 23", "rr"),
    "f_mv4": r"25",

    # ------------------------------------------------------ from a graph
    "f_gd1": r"[{-4},\,2)\cup(2,\,4]",
    "f_gd2": r"[{-4},\,4]",
    "f_gd3": r"({-4},\,2)\cup(2,\,4]",
    "f_gd4": r"[{-4},\,5]",
    "f_id1": r"({-2},\ 2)",
    "f_id2": r"(2,\ \infty)",
    "f_id3": r"(1.7,\ {-1.7})",
    "f_id4": r"(0,\ 2)",
    "f_ar1a": r"\dfrac{16}{3}",
    "f_ar2a": r"\dfrac{32}{3}",
    "f_ar3a": r"16",
    "f_ar4a": r"8",

    # -------------------------------------------------------- logarithms
    "f_ls1": r"x=\pm 9",
    "f_ls2": r"x=9",
    "f_ls3": r"x=\pm 2",
    "f_ls4": r"x=81",
    "f_lr":  r"\log_{2}\sqrt{2^{6}}",
    "f_lr1": r"3",
    "f_lr2": r"6",
    "f_lr3": r"\dfrac{1}{3}",
    "f_lr4": r"{-3}",

    # --------------------------------------------- rational and function
    "f_hole": r"f(x)=\dfrac{x^{2}-2x-15}{x+3}",
    "f_h1": r"({-3},\ {-8})",
    "f_h2": r"(3,\ {-8})",
    "f_h3": r"({-3},\ {-15})",
    "f_h4": r"(3,\ 8)",
    "f_ca1": r"f(x)=\dfrac{1}{x-4}",
    "f_ca2": r"f(x)=\dfrac{x-4}{(x-4)(x+1)}",
    "f_ca3": r"f(x)=\dfrac{2x}{x-4}",
    "f_ca4": r"f(x)=\dfrac{1}{x+4}",
    "f_ic1": r"f^{-1}(x)=\sqrt[3]{x-5}",
    "f_ic2": r"f^{-1}(x)=\sqrt[3]{x+5}",
    "f_ic3": r"f^{-1}(x)=\sqrt{x-5}",
    "f_ic4": r"f^{-1}(x)=(x-5)^{3}",
    "f_pi1": r"{-i}",
    "f_pi2": r"i",
    "f_pi3": r"{-1}",
    "f_pi4": r"1",
    "f_deg2": r"5x^{3}+2^{6}x-7x^{4}+9",
    "f_lead": r"7x^{3}+9x^{2}-2x^{5}+5",
    "f_div":  r"x^{3}-3x^{2}-4x+12",
    "f_dv1": r"x^{2}-x-6",
    "f_dv2": r"x^{2}-5x+6",
    "f_dv3": r"x^{3}-x-6",
    "f_dv4": r"x^{2}-6",

    # ---------------------------------------------------------- calculus
    "f_lim": r"\lim_{x\to 0}\,3x\cos x",
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
    tex = os.path.join(tmp, "saatf.tex")
    open(tex, "w").write("\n".join(doc))
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-output-directory", tmp, tex], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-3000:])
        raise SystemExit("pdflatex failed")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(tmp, "saatf.pdf"), os.path.join(tmp, "r")], check=True)
    pages = sorted(f for f in os.listdir(tmp) if f.startswith("r-") and f.endswith(".png"))
    assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} expressions"
    for k, p in zip(keys, pages):
        im = Image.open(os.path.join(tmp, p)).convert("RGBA")
        dst = os.path.join(out_dir, k + ".png")
        im.save(dst)
        idx[k] = {"file": dst, "win": im.width / dpi, "hin": im.height / dpi,
                  "aspect": im.width / im.height}
    json.dump(idx, open(idx_path, "w"), indent=1)
    print(f"{len(keys)} part-F expressions added; index now holds {len(idx)}")


if __name__ == "__main__":
    render()
