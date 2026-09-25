"""LaTeX expressions for the SIMULATED GAT bank.
Same pipeline as the transcription banks — pdflatex, Computer Modern,
transparent PNG, 500 dpi for screen and 260 dpi for Word (spec section 5, 6a).
"""
import json, os, shutil, subprocess
from PIL import Image

INK = "222E2D"
E = {
    # ---- arithmetic -----------------------------------------------------
    "s_ratio_pow": r"6\times 10^{5}\qquad\text{and}\qquad 1.5\times 10^{5}",
    "s_pct_unk":   r"180\%\ \text{of}\ K \;=\; 3600\qquad\text{A: }\ K"
                   r"\qquad\text{B: }\ 2200",
    "s_surd_cmp":  r"\text{A: }\ 3\sqrt{5}\qquad\qquad"
                   r"\text{B: }\ \dfrac{12\sqrt{20}}{4\sqrt{4}}",
    "s_surd_frac": r"\dfrac{\sqrt{5}\left(2\sqrt{3}+4\sqrt{3}\right)}"
                   r"{\dfrac{\sqrt{5}}{3\sqrt{3}}}",
    "s_neg_exp":   r"\left(t^{\frac{2}{7}}\div t^{-\frac{5}{7}}\right)\cdot t^{3}=16",
    "s_pow2":      r"3^{12}",
    "s_estimate":  r"\text{A: }\ \dfrac{0.25\times 63.98}{1.001}\qquad\qquad"
                   r"\text{B: }\ 15",
    "s_longdiv":   r"64\,431\,516\div 372",
    "s_nested":    r"0.05\%\ \text{of}\ 0.02\ \text{of}\ 4000",
    "s_decsum":    r"\dfrac{75}{1000}+\dfrac{45}{100}+\dfrac{606}{10}",
    "s_factor":    r"\dfrac{{-18}\times 35+11\times 35}{7}",
    "s_negfrac":   r"\text{A: }\ \dfrac{2}{5}-\dfrac{9}{10}\qquad\qquad"
                   r"\text{B: }\ \dfrac{1}{10}-\dfrac{9}{10}",
    "s_pct_cross": r"\text{A: }\ 15\%\ \text{of}\ 480\qquad\qquad"
                   r"\text{B: }\ 0.8\%\ \text{of}\ 9000",
    # ---- algebra --------------------------------------------------------
    "s_eval":      r"3w^{3}-2w^{2}+5w\qquad\text{when}\ w={-2}",
    "s_sqrt2roots": r"(k+3)^{2}=121",
    "s_denpair":   r"\dfrac{a}{5}+\dfrac{b}{5}=18",
    "s_sysinv":    r"4x+y=40\ ,\qquad y+\dfrac{4}{3}z=24",
    "s_prop":      r"\dfrac{7}{9}=\dfrac{0.7v}{9}",
    "s_solvecmp":  r"5^{p}=125\ ,\qquad 9q=54\qquad\text{A: }\ 4p\qquad\text{B: }\ 3q",
    "s_ineq":      r"3+4h>0\qquad\text{A: }\ h\qquad\text{B: }\ {-\dfrac{5}{6}}",
    "s_nosign":    r"7u=3v\qquad\qquad\text{A: }\ u\qquad\text{B: }\ v",
    "s_recip":     r"g<n\ ,\quad g,n\neq 0\qquad\text{A: }\ \dfrac{1}{g}"
                   r"\qquad\text{B: }\ \dfrac{1}{n}",
    "s_substcmp":  r"u={-\dfrac{1}{5}}\ ,\quad u+v=0\qquad"
                   r"\text{A: }\ u-v\qquad\text{B: }\ 7u",
    "s_casesplit": r"ab=k\ ,\qquad ak=b\qquad\text{A: }\ k\qquad\text{B: }\ b-a",
    "s_false":     r"p+q=r\ ,\qquad p=q",
    "s_undo":      r"24m-83=1069",
    "s_identity":  r"c+d=9\ ,\qquad cd=14",
    "s_areaeq":    r"\text{sides}\ 9,\ 12,\ 15",
    "s_pyth":      r"\text{hypotenuse}=26\ ,\qquad\text{legs}\ y\ \text{and}\ y+14",
    # ---- geometry / options ---------------------------------------------
    "i_frac34":  r"\tfrac{3}{4}\%",
    "i_recur":   r"a_{1}={-8}\ ,\qquad a_{n+1}={-a_{n}}+3",
    "i_zeroprod": r"k\,\ell\,m\,n=0\ ,\qquad \ell\,m\,n=1",
    "i_prodsq":  r"ab=18\ ,\qquad a^{2}-b^{2}=27",
    "i_fracsys": r"\dfrac{p+2}{q+1}=1\ ,\qquad \dfrac{p-1}{q-3}=2",
    "i_seq_nn":  r"1,\ 4,\ 27,\ \underline{\quad},\ 3125",
    "i_o_v1": r"xy=5(x+y)-7", "i_o_v2": r"xy=7-5(x+y)",
    "i_o_v3": r"xy=5x+y-7",  "i_o_v4": r"xy=5(x-y)-7",
    "i_o_f1": r"\dfrac{1}{3}", "i_o_f2": r"\dfrac{3}{4}",
    "i_o_f3": r"\dfrac{1}{2}", "i_o_f4": r"\dfrac{2}{3}",
    # ---- part I (expanded worksheet mining) ------------------------------
    "i_998":     r"998\times 25",
    "i_1001":    r"1001\times 372",
    "i_dec_abc": r"A=0.06\ ,\quad B=0.5\ ,\quad C=0.022"
                 r"\qquad\text{find}\ \ A\times B+C",
    "i_symsum":  r"1+2+3+4+5+6+6+5+4+3+2+1",
    "i_num9":    r"\overline{2\,q\,q\,6}",
    "i_cmp_near": r"\text{A: }\ \dfrac{100}{99}\qquad\qquad"
                  r"\text{B: }\ \dfrac{1000}{999}",
    "i_third_of": r"\dfrac{1}{3}N=\dfrac{2}{3}",
    "i_chain":   r"A-B=5\ ,\qquad B-C=3\ ,\qquad C+D=1",
    "i_quadtrap": r"10n+n^{2}=10n+4n",
    "i_seq2nd":  r"52,\ \underline{\quad},\ 34,\ 28,\ 24",
    "i_seqsq":   r"4,\ 9,\ 16,\ 25,\ \ldots",
    "i_zerodiv": r"x\neq 0\qquad\text{A: }\ 0\div x\qquad\text{B: }\ x\div 0",
    "i_prodsum3": r"(n-1)\,n\,(n+1)=5\left[(n-1)+n+(n+1)\right]",
    # ---- part J (level 1-2 top-up: ARI, ALG, DAT, LOG) --------------------
    "j_pf1": r"\dfrac{7}{25}", "j_pf2": r"\dfrac{7}{20}",
    "j_pf3": r"\dfrac{3}{5}",  "j_pf4": r"\dfrac{35}{50}",
    "j_58":   r"\dfrac{5}{8}",
    "j_sqrt576": r"\sqrt{576}",
    "j_cbrt": r"\sqrt[3]{216}",
    "j_pow":  r"\left({-2}\right)^{5}",
    "j_sn1": r"4.2\times 10^{-4}", "j_sn2": r"4.2\times 10^{4}",
    "j_sn3": r"42\times 10^{-5}",  "j_sn4": r"4.2\times 10^{-3}",
    "j_expo": r"\dfrac{2^{7}\times 2^{5}}{2^{9}}",
    "j_add":  r"\dfrac{2}{3}+\dfrac{3}{4}",
    "j_a1": r"\dfrac{5}{7}",  "j_a2": r"\dfrac{17}{12}",
    "j_a3": r"\dfrac{6}{12}", "j_a4": r"\dfrac{5}{12}",
    "j_abs":  r"\left|{-7}\right|+\left|3-9\right|",
    "j_ooo":  r"12+6\div 2\times\left(5-3\right)",
    "j_sub2": r"3a-2b\qquad\text{when}\ \ a=4\ ,\ \ b={-1}",
    "j_2step": r"5x-7=23",
    "j_brack": r"3\left(x-4\right)=18",
    "j_clt":  r"5x+3y-2x+7y",
    "j_c1": r"3x+10y", "j_c2": r"7x+10y",
    "j_c3": r"3x+4y",  "j_c4": r"13xy",
    "j_ineq": r"4x-5<11",
    "j_i1": r"x<4", "j_i2": r"x>4",
    "j_i3": r"x<\dfrac{3}{2}", "j_i4": r"x<16",
    "j_exp":  r"\left(x+3\right)\left(x-5\right)",
    "j_e1": r"x^{2}-2x-15", "j_e2": r"x^{2}+2x-15",
    "j_e3": r"x^{2}-2x+15", "j_e4": r"x^{2}-15",
    "j_fac":  r"6x^{2}+9x",
    "j_g1": r"3x\left(2x+3\right)", "j_g2": r"3\left(2x^{2}+3x\right)",
    "j_g3": r"x\left(6x+9\right)",  "j_g4": r"3x\left(2x+9\right)",
    "j_fn":   r"f(x)=2x^{2}-3\qquad\text{find}\ \ f({-2})",
    "j_p16": r"\dfrac{1}{6}", "j_p13": r"\dfrac{1}{3}",
    "j_p12": r"\dfrac{1}{2}", "j_p23": r"\dfrac{2}{3}",
    "j_p14": r"\dfrac{1}{4}", "j_p34": r"\dfrac{3}{4}",
    "j_p112": r"\dfrac{1}{12}", "j_p17": r"\dfrac{1}{7}",
    "j_p736": r"\dfrac{7}{36}",
    # ---- part K (skills from the computerised-section inventory) ----------
    "k_pow50":  r"2^{50}",
    "k_h1": r"2^{25}", "k_h2": r"2^{49}", "k_h3": r"2^{50}-2", "k_h4": r"1^{50}",
    "k_sq999":  r"999^{2}",
    "k_powdiff": r"10^{7}-10^{6}",
    "k_d1": r"9\times 10^{6}", "k_d2": r"10^{1}",
    "k_d3": r"10^{6}",         "k_d4": r"9\times 10^{7}",
    "k_decprod": r"0.3\times 0.03\times 0.003",
    "k_p1": r"2.7\times 10^{-5}", "k_p2": r"2.7\times 10^{-6}",
    "k_p3": r"27\times 10^{-5}",  "k_p4": r"9\times 10^{-5}",
    "k_xy": r"xy<0",
    "k_s1": r"x^{2}y^{2}", "k_s2": r"x^{2}y",
    "k_s3": r"xy^{2}",     "k_s4": r"x^{3}y^{3}",
    "k_terms": r"n\ ,\qquad n+2\ ,\qquad n+10",
    "k_m1": r"n+4", "k_m2": r"n+6", "k_m3": r"3n+12", "k_m4": r"n+12",
    "k_ratio": r"\dfrac{\text{water}}{\text{electricity}}=\dfrac{1}{20}",
    "k_a1": r"\dfrac{a}{2}", "k_a2": r"a", "k_a3": r"2a", "k_a4": r"180-a",
    "k_q1": r"3\pi", "k_q2": r"4\pi", "k_q3": r"12\pi", "k_q4": r"16\pi",
    "k_pr1": r"\dfrac{2}{5}", "k_pr2": r"\dfrac{1}{2}",
    "k_pr3": r"\dfrac{1}{5}", "k_pr4": r"\dfrac{3}{10}",
    # ---- part L (unified practice sheet: level 1-2 word logic and algebra) --
    "u_seq":     r"2,\ 5,\ 11,\ 23,\ \underline{\quad}",
    "u_frac_eq": r"\dfrac{x}{3}+\dfrac{x}{6}=9",
    "u_prod3":   r"ab=1\ ,\qquad bc=2\ ,\qquad ac=8",
    "u_cmp_sq":  r"\text{A: }\ 606^{2}+505^{2}\qquad\qquad\text{B: }\ 707^{2}",
    "u_sqcube":  r"s^{2}=s^{3}\ ,\qquad s>0",
    "u_selfref": r"h=\dfrac{1}{4}h+30",
    "u_rect":    r"x\left(x+4\right)=45\ ,\qquad x>0",
    "h_sumsq":   r"x^{2}+y^{2}=0\qquad\text{find}\quad x^{2}-y^{2}",
    "h_fourth":  r"\dfrac{1}{(x+8)^{4}}=\dfrac{1}{10\,000}",
    "h_recip":   r"\dfrac{1}{2x+1}=\dfrac{1}{x+2}",
    "h_circ36":  r"36\pi\ \text{cm}^{2}",
    "s_circle_eq":  r"(x-4)^{2}+(y+3)^{2}=49",
    "s_radius":    r"r=5\ \text{cm}",
    "o8r3":  r"8\sqrt{3}",
    "o16r3": r"16\sqrt{3}",
    "o4r3":  r"4\sqrt{3}",
    "o32r3": r"32\sqrt{3}",
    # ---- fraction options -----------------------------------------------
    "f914": r"\dfrac{9}{14}",
    "f57":  r"\dfrac{5}{7}",
    "f47":  r"\dfrac{4}{7}",
    "f12":  r"\dfrac{1}{2}",
    "f13":  r"\dfrac{1}{3}",
    "f14":  r"\dfrac{1}{4}",
    "f25":  r"\dfrac{2}{5}",
    "f35":  r"\dfrac{3}{5}",
    "f15":  r"\dfrac{1}{5}",
    "f16":  r"\dfrac{1}{6}",
    # ---- part 6 skills ---------------------------------------------------
    "s_powtower":  r"\text{A: }\ \left(5^{2}\right)^{-2}\times\left(25^{-1}\right)^{-3}"
                   r"\qquad\qquad\text{B: }\ 25",
    "s_samebase":  r"\sqrt[3]{\dfrac{1}{8}}\times\left(\dfrac{1}{8}\right)^{\frac{2}{3}}",
    "s_recippair": r"\dfrac{7}{x-2}+\dfrac{x-2}{7}=\dfrac{7}{11}+\dfrac{11}{7}",
    "s_absval":    r"4\left|m\right|=28\qquad\qquad\text{A: }\ m\qquad\text{B: }\ 7",
    "s_cfrac":     r"\dfrac{1+\dfrac{2}{n}}{\,n-\dfrac{4}{n}\,}",
    "s_minsq":     r"\text{A: the least value of }\ (w-4)^{2}\qquad\qquad\text{B: }\ 1",
    "s_signpow":   r"k<0",
    "s_subquad":   r"3y^{2}+x=6\ ,\qquad y=\dfrac{x}{3}",
    "s_arearatio": r"\text{areas}\ \ 1:196",
    "s_swapfrac":  r"\text{A: }\ \dfrac{1}{3}\ \text{of}\ 12\qquad\qquad"
                   r"\text{B: }\ \dfrac{1}{12}\ \text{of}\ 3",
    # options
    "cf1": r"\dfrac{1}{n+2}",
    "cf2": r"\dfrac{1}{n-2}",
    "cf3": r"\dfrac{1}{n}",
    "cf4": r"\dfrac{n}{n-2}",
    "sp1": r"6k",   "sp2": r"k^{3}",   "sp3": r"k^{4}",   "sp4": r"\dfrac{1}{k}",
    "f18": r"\dfrac{1}{8}",
    # ---- part 5 skills ---------------------------------------------------
    "s_powcmp":   r"\text{A: }\ 3^{75}\qquad\qquad\text{B: }\ 2^{100}",
    "s_radcmp":   r"\text{A: }\ \sqrt{3}\qquad\qquad\text{B: }\ \sqrt{1+\sqrt{2}}",
    "s_recipx":   r"x^{-1}=\dfrac{\sqrt{2}}{6}",
    "s_splitfr":  r"\dfrac{x}{y}=5\qquad\text{find}\quad\dfrac{x+3y}{y}",
    "s_cancelm":  r"x=14\ ,\quad y=15\qquad\text{find}\quad\dfrac{1}{35}\times x\times y",
    "s_addfrac":  r"\text{A: }\ \dfrac{1}{2}+\dfrac{1}{3}\qquad\qquad"
                  r"\text{B: }\ \dfrac{1}{3+2}",
    "s_selfover": r"\dfrac{1}{\frac{1}{3}}+\dfrac{2}{\frac{2}{6}}+\dfrac{7}{\frac{7}{3}}",
    "o3r2": r"3\sqrt{2}",  "o2r2": r"2\sqrt{2}",  "o6r2": r"6\sqrt{2}",
    # ---- formula-book skills ---------------------------------------------
    "s_sumn":     r"1+2+3+\cdots+60",
    "s_sumodd":   r"1+3+5+\cdots+29",
    "s_sumeven":  r"2+4+6+\cdots+40",
    "s_unitsdig": r"4738\times 2691",
    "s_tensdig":  r"5847\times 3163",
    "s_unitconv": r"\text{A: }\ 2.4\ \text{m}\qquad\qquad\text{B: }\ 240\ \text{cm}",
    "s_decplace": r"0.4\times 0.02\times 0.5",
    "s_crossfr":  r"\text{A: }\ \dfrac{5}{7}\qquad\qquad\text{B: }\ \dfrac{7}{10}",
    "s_zeroone":  r"0<k<1\qquad\text{A: }\ k^{2}\qquad\text{B: }\ k",
    "s_rootapx":  r"\text{A: }\ \sqrt{50}\qquad\qquad\text{B: }\ 7",
    "s_rootdec":  r"\sqrt{0.0049}",
    "s_ident":    r"5x-2=5x-2",
    "s_parity":   r"n\ \text{is odd}",
    "s_prodinc":  r"\text{A: }\ 61\times 30\qquad\qquad\text{B: }\ 62\times 29",
    "s_addrad":   r"2\sqrt{18}+5\sqrt{2}",
    "s_sameexp":  r"x^{6}=5^{6}",
    "s_diffsq":   r"a+b=13\ ,\qquad a-b=4",
    "s_countrng": r"\text{the even numbers from }18\text{ to }96",
    # options
    "p1": r"n^{2}+2",  "p2": r"3n+2",  "p3": r"n^{2}+n",  "p4": r"2n+5",
    "r72": r"7\sqrt{2}",  "r11r2": r"11\sqrt{2}",  "r7r18": r"7\sqrt{18}",
    "r10r2": r"10\sqrt{2}",
    "pm5": r"\pm 5",  "just5": r"5",  "pm6": r"\pm 6",  "just6": r"6",
    # ---- option images that carry notation -------------------------------
    "q1a": r"p=\dfrac{r}{2}",
    "q1b": r"p+r=q+r",
    "q1c": r"3p+3q=3r",
    "q1d": r"r-q=3p",
}


def render(out_dir, dpi):
    tmp = f".tex_sim_{dpi}"
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
    tex = os.path.join(tmp, "sim.tex")
    open(tex, "w").write("\n".join(doc))
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-output-directory", tmp, tex], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-2500:]); raise SystemExit("pdflatex failed")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(tmp, "sim.pdf"), os.path.join(tmp, "p")], check=True)
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


render("math_sim", 500)
render("math_sim_doc", 260)
