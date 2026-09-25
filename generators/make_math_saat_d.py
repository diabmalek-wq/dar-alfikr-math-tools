"""LaTeX for part D of the simulated SAAT bank — the yield of the 204 examples.

Rendered into the SAME index the earlier parts use. Run make_math_saat.py,
make_math_saat_b.py and make_math_saat_c.py first.
"""
import json, os, subprocess, tempfile
from PIL import Image

INK = "222E2D"

M = lambda body, cols="cc": r"\left[\begin{array}{%s}%s\end{array}\right]" % (cols, body)
DET = lambda body, cols="ccc": r"\left|\begin{array}{%s}%s\end{array}\right|" % (cols, body)

E = {
    # ------------------------------------------------- session 3
    "d_prin":  r"\sqrt{16y^{4}}",
    "d_prin1": r"4y^{2}",
    "d_prin2": r"\pm 4y^{2}",
    "d_prin3": r"4\left|y^{2}\right|",
    "d_prin4": r"16y^{2}",
    "d_rat1":  r"\dfrac{3}{\sqrt{5}}",
    "d_rat1a": r"\dfrac{3\sqrt{5}}{5}",
    "d_rat1b": r"\dfrac{3\sqrt{5}}{\sqrt{5}}",
    "d_rat1c": r"\dfrac{\sqrt{5}}{5}",
    "d_rat1d": r"3\sqrt{5}",
    "d_srad":  r"\sqrt{50x^{6}}",
    "d_srad1": r"x^{3}\sqrt{50}",
    "d_srad2": r"25x^{3}\sqrt{2}",
    "d_srad3": r"5x^{3}\sqrt{2}",
    "d_srad4": r"5x^{2}\sqrt{2}",

    # ------------------------------------------------- session 5
    "d_subp":  r"\left(5x^{2}-3x+4\right)-\left(2x^{2}+6x-1\right)",
    "d_subp1": r"3x^{2}+3x+5",
    "d_subp2": r"3x^{2}-9x+5",
    "d_subp3": r"3x^{2}-9x+3",
    "d_subp4": r"7x^{2}+3x+3",
    "d_deg":   r"4x^{4}y^{3}+2x^{5}-7y^{2}+1",
    "d_poly1": r"x^{3}-2x+9",
    "d_poly2": r"{-6}x^{2}+x",
    "d_poly3": r"\sqrt{x}+x+4",
    "d_poly4": r"x^{8}-3x^{2}+11",
    "d_divm":  r"\dfrac{12x^{4}y^{3}+8x^{3}y^{2}-4x^{2}y}{4x^{2}y}",
    "d_divm1": r"3x^{2}y^{2}+2xy-1",
    "d_divm2": r"3x^{2}y^{2}+2xy",
    "d_divm3": r"3x^{2}y^{2}+8x^{3}y^{2}-4x^{2}y",
    "d_divm4": r"3x^{6}y^{4}+2x^{5}y^{3}-1",

    # ------------------------------------------------- session 6
    "d_cube":  r"(x-5)\left(x^{2}+5x+25\right)",
    "d_cube1": r"x^{3}+125",
    "d_cube2": r"x^{3}+5x^{2}-25x-125",
    "d_cube3": r"x^{3}-15",
    "d_cube4": r"x^{3}-125",
    "d_fcub":  r"8x^{3}-27",
    "d_fcub1": r"(2x-3)(2x-3)^{2}",
    "d_fcub2": r"(2x-3)\left(4x^{2}+6x+9\right)",
    "d_fcub3": r"(2x+3)\left(4x^{2}-6x+9\right)",
    "d_fcub4": r"(2x-3)(2x+3)",

    # ------------------------------------------------- session 7
    "d_mulr":  r"\dfrac{x^{2}-9}{x+2}\cdot\dfrac{x+2}{x-3}",
    "d_mulr1": r"x+3",
    "d_mulr2": r"1",
    "d_mulr3": r"x-3",
    "d_mulr4": r"\dfrac{x^{2}-9}{x-3}",
    "d_divr":  r"\dfrac{3x}{8}\div\dfrac{9x^{2}}{4}",
    "d_divr1": r"\dfrac{6x}{1}",
    "d_divr2": r"\dfrac{27x^{3}}{32}",
    "d_divr3": r"\dfrac{1}{6x}",
    "d_divr4": r"\dfrac{1}{6}",

    # ------------------------------------------------- session 10
    "d_mord": M(r"12 & {-8}\\ {-2} & 10\\ 6 & {-1}", "rr"),
    "d_msc":  r"{-3}\," + M(r"4 & 1\\ 7 & {-2}", "rr"),
    "d_msc1": M(r"{-12} & {-3}\\ 7 & {-2}", "rr"),
    "d_msc2": M(r"{-12} & {-3}\\ {-21} & 6", "rr"),
    "d_msc3": M(r"{-12} & {-3}\\ {-21} & {-6}", "rr"),
    "d_msc4": M(r"1 & {-2}\\ 4 & {-5}", "rr"),
    "d_mpr":  M(r"2 & 3\\ 1 & 4") + M(r"5 & 6\\ 7 & 8"),
    "d_mpr1": M(r"10 & 18\\ 7 & 32"),
    "d_mpr2": M(r"27 & 38\\ 26 & 46"),
    "d_mpr3": M(r"16 & 39\\ 18 & 53"),
    "d_mpr4": M(r"31 & 36\\ 33 & 38"),
    "d_det3": DET(r"2 & 1 & 3\\ 0 & 4 & 5\\ 1 & 0 & 6", "rrr"),

    # ------------------------------------------------- session 13
    "d_sqp":  r"(x-5)^{2}=9",
    "d_sqp1": r"x=8",
    "d_sqp2": r"x=2\ \ \text{or}\ \ x={-8}",
    "d_sqp3": r"x=8\ \ \text{or}\ \ x=2",
    "d_sqp4": r"x=9.5\ \ \text{or}\ \ x=0.5",
    "d_cts2":  r"x^{2}+6x-14=0",
    "d_cts2a": r"x={-3}\pm\sqrt{5}",
    "d_cts2b": r"x={-3}\pm\sqrt{23}",
    "d_cts2c": r"x=3\pm\sqrt{23}",
    "d_cts2d": r"x={-3}+\sqrt{23}",
    "d_sump":  r"2x^{2}+8x-10=0",

    # ------------------------------------------------- session 16
    "d_dis":  r"x^{4}-13x^{2}+36=0",
    "d_dis1": r"x=\pm 2\ \ \text{or}\ \ x=\pm 3",
    "d_dis2": r"x=4\ \ \text{or}\ \ x=9",
    "d_dis3": r"x=2\ \ \text{or}\ \ x=3",
    "d_dis4": r"x=\pm 1\ \ \text{or}\ \ x=\pm 6",
    "d_nrt":  r"x^{5}+2x^{3}-7=0",

    # ------------------------------------------------- session 17
    "d_rin": r"\dfrac{x-2}{x-5}\geq 0",

    # ------------------------------------------------- session 19
    "d_o2o1": r"f(x)=x^{4}",
    "d_o2o2": r"f(x)=\left|x\right|",
    "d_o2o3": r"f(x)=x^{3}+x",
    "d_o2o4": r"f(x)=x^{2}-4",

    # ------------------------------------------------- session 20
    "d_dmr":  r"f(x)=\sqrt{x+4}",
    "d_dmr1": r"x\geq 4",
    "d_dmr2": r"x>{-4}",
    "d_dmr3": r"x\leq{-4}",
    "d_dmr4": r"x\geq{-4}",
    "d_dmq":  r"f(x)=\dfrac{2+x}{x^{2}-7x}",
    "d_dmq1": r"x\neq 0\ \ \text{and}\ \ x\neq 7",
    "d_dmq2": r"x\neq 7",
    "d_dmq3": r"x\neq 0",
    "d_dmq4": r"x\neq{-2}",
    "d_rga":  r"f(x)=\left|2x\right|-4",
    "d_rga1": r"f(x)\geq 4",
    "d_rga2": r"f(x)\geq{-4}",
    "d_rga3": r"x\in\mathbb{R}",
    "d_rga4": r"f(x)\geq{-2}",

    # ------------------------------------------------- session 21
    "d_ev2": r"f(x)=2x^{2}-8",
    "d_pw":  r"f(x)=\begin{cases}3x+2 & x<1\\[2pt] x^{2}-1 & x\geq 1\end{cases}",
    "d_fk":  r"f(x)=x^{2}+x",
    "d_fk1": r"x=4\ \ \text{or}\ \ x={-3}",
    "d_fk2": r"x=3",
    "d_fk3": r"x={-4}\ \ \text{or}\ \ x=3",
    "d_fk4": r"x=2\ \ \text{or}\ \ x=6",

    # ------------------------------------------------- session 22
    "d_zyi": r"f(x)=2x^{2}+x-15",

    # ------------------------------------------------- session 23
    "d_par":  r"y={-3}(x+2)^{2}+7",
    "d_par1": r"f(x)={-x^{2}}",
    "d_par2": r"f(x)=x^{2}",
    "d_par3": r"f(x)=x",
    "d_par4": r"f(x)=x^{3}",
    "d_hcr":  r"g(x)={-(2x)^{2}}",
    "d_tpg1": r"y=\sqrt{x+3}-5",
    "d_tpg2": r"y=\sqrt{x+3}+5",
    "d_tpg3": r"y=\sqrt{x-3}-5",
    "d_tpg4": r"y=\sqrt{x-3-5}",

    # ------------------------------------------------- session 24
    "d_invr":  r"f(x)=\sqrt{x-4}",
    "d_invr1": r"f^{-1}(x)=x^{2}-4,\ \ x\geq 0",
    "d_invr2": r"f^{-1}(x)=x^{2}+4",
    "d_invr3": r"f^{-1}(x)=\sqrt{x+4},\ \ x\geq{-4}",
    "d_invr4": r"f^{-1}(x)=x^{2}+4,\ \ x\geq 0",

    # ------------------------------------------------- session 25
    "d_sfp1": r"x^{2}+x+5",
    "d_sfp2": r"x^{2}+x-5",
    "d_sfp3": r"x^{2}+7x-5",
    "d_sfp4": r"x^{2}-x+5",
    "d_dsf1": r"x\in\mathbb{R}",
    "d_dsf2": r"x\geq 2",
    "d_dsf3": r"x\geq{-2}",
    "d_dsf4": r"x>{-2}",

    # ------------------------------------------------- session 31
    "d_kite1": r"2\sqrt{5}",
    "d_kite2": r"2\sqrt{13}",
    "d_kite3": r"\sqrt{2}",
    "d_kite4": r"\sqrt{20}",

    # ------------------------------------------------- session 36
    "d_mid31": r"\left(0,\ {-1},\ {-\tfrac{1}{2}}\right)",
    "d_mid32": r"\left(3,\ 3,\ {-\tfrac{5}{2}}\right)",
    "d_mid33": r"(0,\ {-2},\ {-1})",
    "d_mid34": r"\left(0,\ {-1},\ \tfrac{1}{2}\right)",

    # ------------------------------------------------- session 38
    "d_perp1": r"\dfrac{5}{2}",
    "d_perp2": r"{-\dfrac{5}{2}}",
    "d_perp3": r"\dfrac{2}{5}",
    "d_perp4": r"{-\dfrac{2}{5}}",
    "d_pb1":   r"y=x-3",
    "d_pb2":   r"y={-x}+7",
    "d_pb3":   r"y={-x}+9",
    "d_pb4":   r"y={-x}+21",

    # ------------------------------------------------- session 39
    "d_mep1": r"(10,\ 7)",
    "d_mep2": r"(4,\ 1)",
    "d_mep3": r"(4,\ 4)",
    "d_mep4": r"(10,\ 5)",
    "d_dst1": r"3\sqrt{2}",
    "d_dst2": r"\sqrt{22}",
    "d_dst3": r"6",
    "d_dst4": r"\sqrt{18}",

    # ------------------------------------------------- session 40
    "d_trf1": r"({-6},\ 3)",
    "d_trf2": r"({-6},\ {-1})",
    "d_trf3": r"(6,\ {-3})",
    "d_trf4": r"(10,\ {-1})",
    "d_dil1": r"({-3},\ 1)",
    "d_dil2": r"({-3},\ 2)",
    "d_dil3": r"\left({-\tfrac{13}{2}},\ \tfrac{3}{2}\right)",
    "d_dil4": r"({-12},\ 4)",

    # ------------------------------------------------- session 47 and 48
    "d_gd1": r"y=5\left(3\right)^{x}",
    "d_gd2": r"y={-5}\left(3\right)^{x}",
    "d_gd3": r"y=5\left(\tfrac{1}{3}\right)^{x}",
    "d_gd4": r"y=5\left(3\right)^{2x}",
    "d_eeq":   r"2^{x}=8^{3}",
    "d_eineq": r"4\cdot 2^{8x-12}>16",
    "d_ein1":  r"x<\dfrac{7}{4}",
    "d_ein2":  r"x>\dfrac{7}{4}",
    "d_ein3":  r"x>\dfrac{3}{2}",
    "d_ein4":  r"x>2",

    # ------------------------------------------------- session 49 and 51
    "d_lef1": r"3^{y}=27",
    "d_lef2": r"27^{y}=3",
    "d_lef3": r"3y=27",
    "d_lef4": r"3^{27}=y",
    "d_lineq": r"\log_{3}x>4",
    "d_li1":   r"x>81",
    "d_li2":   r"x>12",
    "d_li3":   r"x<81",
    "d_li4":   r"x>64",
    "d_scl1": r"x=\dfrac{\log 19}{\log 4}",
    "d_scl2": r"x=\log\dfrac{19}{4}",
    "d_scl3": r"x=\dfrac{\log 4}{\log 19}",
    "d_scl4": r"x=\log 19-\log 4",

    # ------------------------------------------------- session 61
    "d_cws1": r"{-3}-4i",
    "d_cws2": r"3+4i",
    "d_cws3": r"3-4i",
    "d_cws4": r"{-3}+8i",

    # ------------------------------------------------- sessions 67 and 69
    "d_d2r1": r"\dfrac{3\pi}{4}",
    "d_d2r2": r"\dfrac{24300}{\pi}",
    "d_d2r3": r"\dfrac{3}{4}",
    "d_d2r4": r"\dfrac{135\pi}{180}",
    "d_rts1": r"\dfrac{3}{5}",
    "d_rts2": r"{-\dfrac{3}{5}}",
    "d_rts3": r"{-\dfrac{4}{5}}",
    "d_rts4": r"{-\dfrac{3}{4}}",
    "d_csq1": r"\dfrac{\sqrt{5}}{3}",
    "d_csq2": r"{-\dfrac{\sqrt{5}}{3}}",
    "d_csq3": r"\dfrac{1}{3}",
    "d_csq4": r"\dfrac{5}{9}",

    # ------------------------------------------------- sessions 73 and 74
    "d_neg1": r"\sin({-\theta})={-\sin\theta}",
    "d_neg2": r"\cos({-\theta})={-\cos\theta}",
    "d_neg3": r"\sin({-\theta})=\sin\theta",
    "d_neg4": r"\tan({-\theta})=\tan\theta",
    "d_cof1": r"\cos\left(\dfrac{\pi}{2}-\theta\right)",
    "d_cof2": r"\cos\left(\pi-\theta\right)",
    "d_cof3": r"\sin\left(\dfrac{\pi}{2}-\theta\right)",
    "d_cof4": r"\cos\left(\dfrac{\pi}{2}+\theta\right)",
    "d_cd1": r"{-\dfrac{7}{25}}",
    "d_cd2": r"\dfrac{6}{5}",
    "d_cd3": r"\dfrac{7}{25}",
    "d_cd4": r"\dfrac{24}{25}",

    # ------------------------------------------------- session 76
    "d_gen1": r"\theta=\pi+2\pi k",
    "d_gen2": r"\theta=\pi+\pi k",
    "d_gen3": r"\theta=2\pi k",
    "d_gen4": r"\theta=\dfrac{\pi}{2}+2\pi k",

    # ------------------------------------------------- session 79
    "d_cmp1": r"\left\langle 7,\ {-7}\right\rangle",
    "d_cmp2": r"\left\langle {-7},\ 7\right\rangle",
    "d_cmp3": r"\left\langle {-1},\ {-3}\right\rangle",
    "d_cmp4": r"\left\langle {-1},\ {-7}\right\rangle",
    "d_uv1": r"\left\langle {-\dfrac{2}{\sqrt{13}}},\ \dfrac{3}{\sqrt{13}}\right\rangle",
    "d_uv2": r"\left\langle {-\dfrac{2}{13}},\ \dfrac{3}{13}\right\rangle",
    "d_uv3": r"\left\langle {-\dfrac{2}{3}},\ 1\right\rangle",
    "d_uv4": r"\left\langle {-1},\ \dfrac{3}{2}\right\rangle",
    "d_md1": r"\left\langle 5\sqrt{2},\ 5\sqrt{2}\right\rangle",
    "d_md2": r"\left\langle \dfrac{\sqrt{2}}{2},\ \dfrac{\sqrt{2}}{2}\right\rangle",
    "d_md3": r"\left\langle 10,\ 45\right\rangle",
    "d_md4": r"\left\langle \sqrt{2},\ \sqrt{2}\right\rangle",
    "d_cr1": r"\left\langle {-5},\ {-6},\ 3\right\rangle",
    "d_cr2": r"\left\langle {-5},\ 6,\ 3\right\rangle",
    "d_cr3": r"\left\langle 5,\ 6,\ {-3}\right\rangle",
    "d_cr4": r"\left\langle {-9},\ {-6},\ 1\right\rangle",

    # ------------------------------------------------- session 80
    "d_pol1": r"\sqrt{29}",
    "d_pol2": r"\sqrt{29-20\cos 390^{\circ}}",
    "d_pol3": r"3",
    "d_pol4": r"\sqrt{19}",

    # ------------------------------------------------- sessions 82 to 85
    "d_cd1e": r"(x-3)^{2}+(y+1)^{2}=65",
    "d_cd2e": r"(x-3)^{2}+(y+1)^{2}=260",
    "d_cd3e": r"(x+3)^{2}+(y-1)^{2}=65",
    "d_cd4e": r"(x-3)^{2}+(y+1)^{2}=\sqrt{65}",
    "d_pf1": r"(y+4)^{2}=8(x-1)",
    "d_pf2": r"(x-1)^{2}=8(y+4)",
    "d_pf3": r"(y+4)^{2}=2(x-1)",
    "d_pf4": r"(y-4)^{2}=8(x+1)",
    "d_as1": r"\pm\dfrac{4}{3}",
    "d_as2": r"\pm\dfrac{3}{4}",
    "d_as3": r"\pm\dfrac{16}{9}",
    "d_as4": r"\dfrac{4}{3}",

    # ------------------------------------------------- session 91
    "d_lf": r"\lim_{x\to 1}\dfrac{x^{2}-1}{x-1}",
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
    tex = os.path.join(tmp, "saatd.tex")
    open(tex, "w").write("\n".join(doc))
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-output-directory", tmp, tex], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-3000:])
        raise SystemExit("pdflatex failed")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(tmp, "saatd.pdf"), os.path.join(tmp, "r")], check=True)
    pages = sorted(f for f in os.listdir(tmp) if f.startswith("r-") and f.endswith(".png"))
    assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} expressions"
    for k, p in zip(keys, pages):
        im = Image.open(os.path.join(tmp, p)).convert("RGBA")
        dst = os.path.join(out_dir, k + ".png")
        im.save(dst)
        idx[k] = {"file": dst, "win": im.width / dpi, "hin": im.height / dpi,
                  "aspect": im.width / im.height}
    json.dump(idx, open(idx_path, "w"), indent=1)
    print(f"{len(keys)} part-D expressions added; index now holds {len(idx)}")


if __name__ == "__main__":
    render()
