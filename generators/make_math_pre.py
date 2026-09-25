"""LaTeX expressions for the WEEKLY PRE-SESSION SHEETS.

Same pipeline as the bank: pdflatex + preview, Computer Modern, transparent PNG.
The sheet is laid out in HTML and printed by Chromium, so every expression on it
is a rendered image from here — nothing on the sheet is typed as plain text with
slashes, per the house typography rule.

    python3 make_math_pre.py         -> pre_math/ at 300 dpi + _index.json
"""
import json, os, shutil, subprocess, tempfile
from PIL import Image

INK = "222E2D"

E = {
    # ---- week 3: the equivalence table, one image ------------------------
    "w3_table": r"""\begin{array}{c|c|c@{\qquad}c|c|c}
\text{fraction}&\text{decimal}&\text{percent}&\text{fraction}&\text{decimal}&\text{percent}\\[10pt]
\hline
\dfrac{1}{2}&0.5&50\%&\dfrac{1}{8}&0.125&12.5\%\\[10pt]
\dfrac{1}{3}&0.333\ldots&33\tfrac{1}{3}\%&\dfrac{3}{8}&0.375&37.5\%\\[10pt]
\dfrac{1}{4}&0.25&25\%&\dfrac{5}{8}&0.625&62.5\%\\[10pt]
\dfrac{1}{5}&0.2&20\%&\dfrac{2}{3}&0.666\ldots&66\tfrac{2}{3}\%\\[10pt]
\dfrac{1}{6}&0.1666\ldots&16\tfrac{2}{3}\%&\dfrac{3}{4}&0.75&75\%\\[10pt]
\dfrac{1}{20}&0.05&5\%&\dfrac{7}{20}&0.35&35\%
\end{array}""",

    # ---- the methods -----------------------------------------------------
    "w3_cross":  r"\dfrac{a}{b}\ \ \text{vs}\ \ \dfrac{c}{d}\qquad\Longrightarrow\qquad ad\ \ \text{vs}\ \ bc",
    "w3_add":    r"\dfrac{a}{b}+\dfrac{c}{d}=\dfrac{ad+bc}{bd}",
    "w3_divf":   r"\dfrac{a}{b}\div\dfrac{c}{d}=\dfrac{a}{b}\times\dfrac{d}{c}",
    "w3_decdiv": r"\dfrac{0.36}{0.004}=\dfrac{360}{4}=90",
    "w3_of":     r"\text{“of”}\ \Longrightarrow\ \times\qquad\quad \dfrac{3}{8}\ \text{of}\ 640=640\div 8\times 3=240",
    "w3_lowest": r"35\%=\dfrac{35}{100}=\dfrac{7}{20}",
    "w3_round":  r"3.4\underline{5}67\ \longrightarrow\ 3.46",

    # ---- the traps -------------------------------------------------------
    "w3_t1":  r"\dfrac{3}{7}>\dfrac{3}{8}\qquad\text{(bigger bottom, smaller value)}",
    "w3_t2":  r"\dfrac{2}{3}+\dfrac{3}{4}=\dfrac{17}{12}\ ,\qquad \textbf{not}\ \ \dfrac{5}{7}",
    "w3_t3":  r"12\div 0.5=24\qquad\text{(dividing by a number below 1 makes it \emph{bigger})}",
    "w3_t4":  r"0.06\times 0.5=0.03\qquad\text{(three decimal places, not two)}",
    "w3_t5":  r"\dfrac{1}{8}=0.125\ ,\qquad \textbf{not}\ \ 0.18",

    # ---- the six readiness questions ------------------------------------
    "w3_q1": r"\text{Which is larger: }\ \dfrac{5}{8}\ \text{ or }\ \dfrac{7}{11}\ ?",
    "w3_q2": r"\dfrac{3}{4}-\dfrac{2}{5}",
    "w3_q3": r"\dfrac{0.48}{0.006}",
    "w3_q4": r"\dfrac{5}{8}\ \text{of}\ 4\,800\ \text{SAR}",
    "w3_q5": r"\text{Round }\ 47.0952\ \text{ to two decimal places.}",
    "w3_q6": r"\dfrac{2}{3}\div\dfrac{8}{9}",
    "w3_a":  r"\text{Answers: }\ \dfrac{5}{8}\ \ \cdot\ \ \dfrac{7}{20}\ \ \cdot\ \ 80\ \ \cdot\ \ 3\,000\ \text{SAR}\ \ \cdot\ \ 47.10\ \ \cdot\ \ \dfrac{3}{4}",

    # ---- the "connect what is given" cues --------------------------------
    "w3_c1": r"\text{two fractions to compare}\ \Rightarrow\ ad\ \text{vs}\ bc",
    "w3_c2": r"\text{a decimal on the bottom}\ \Rightarrow\ \times 10^{n}\ \text{top and bottom}",
    "w3_c3": r"\text{“of a quantity”}\ \Rightarrow\ \div\ \text{bottom},\ \times\ \text{top}",
    "w3_c4": r"\text{“in lowest terms”}\ \Rightarrow\ \text{cancel by the HCF}",

    # ================================================== WEEK 1 · number sense
    "w1_table": r"""\begin{array}{c|l@{\qquad}c|l}
\text{by}&\text{test}&\text{by}&\text{test}\\[6pt]\hline
2&\text{last digit even}&8&\text{last \emph{three} digits}\div 8\\[8pt]
3&\text{digit sum}\div 3&9&\text{digit sum}\div 9\\[8pt]
4&\text{last \emph{two} digits}\div 4&10&\text{last digit }0\\[8pt]
5&\text{last digit }0\ \text{or}\ 5&11&\text{alternating digit sum}\div 11\\[8pt]
6&\text{passes }2\ \textbf{and}\ 3&&
\end{array}""",
    "w1_primes": r"2,\ 3,\ 5,\ 7,\ 11,\ 13,\ 17,\ 19,\ 23,\ 29,\ 31,\ 37,\ 41,\ 43,\ 47",
    "w1_order":  r"(\ )\ \rightarrow\ x^{n}\ \rightarrow\ \div\,\times\ \rightarrow\ +\,-",
    "w1_pf":     r"360=2^{3}\times 3^{2}\times 5",
    "w1_count":  r"(3+1)(2+1)(1+1)=24",
    "w1_sign":   r"({-2})^{4}=16\qquad ({-2})^{5}={-32}",
    "w1_cycle":  r"7,\,9,\,3,\,1,\ 7,\,9,\,3,\,1,\ \ldots",
    "w1_t1": r"1\ \text{is not prime};\qquad 2\ \text{is prime, and it is even}",
    "w1_t2": r"51=3\times 17\ ,\qquad 57=3\times 19\ ,\qquad 91=7\times 13",
    "w1_t3": r"\text{factor}\ \leq\ \text{the number}\ \leq\ \text{multiple}",
    "w1_t4": r"{-3}^{2}={-9}\ ,\qquad ({-3})^{2}=9",
    "w1_t5": r"1\,234\ \text{is even, but}\ 34\div 4\ \text{is not whole}",
    "w1_c1": r"\text{“how many factors”}\ \Rightarrow\ \text{prime factorise first}",
    "w1_c2": r"\text{“divisible by }6\text{”}\ \Rightarrow\ \text{test }2\ \textbf{and}\ 3",
    "w1_c3": r"\text{“last digit of }a^{n}\text{”}\ \Rightarrow\ \text{find the cycle}",
    "w1_c4": r"\text{“smallest / largest with …”}\ \Rightarrow\ \text{build it digit by digit}",
    "w1_q1": r"\text{Which is prime: }\ 51,\ 57,\ 61,\ 91\ ?",
    "w1_q2": r"12+18\div 3\times 2",
    "w1_q3": r"\text{How many factors has }\ 72\ ?",
    "w1_q4": r"({-2})^{3}\times({-5})",
    "w1_q5": r"\text{Is }\ 3\,516\ \text{ divisible by }4\ ?",
    "w1_q6": r"\text{The digit sum of }\ 2\,7\,q\,3\ \text{is a multiple of }9.\ \text{Find }q.",
    "w1_a":  r"\text{Answers: }\ 61\ \cdot\ 24\ \cdot\ 12\ \cdot\ 40\ \cdot\ \text{yes}\ (16\div 4)\ \cdot\ q=6",

    # ================================================== WEEK 2 · HCF and LCM
    "w2_table": r"""\begin{array}{l|l}
\text{HCF — the \emph{largest} that divides both}&\text{LCM — the \emph{smallest} both divide}\\[6pt]\hline
\text{take the LOWEST power of each prime}&\text{take the HIGHEST power of each prime}\\[8pt]
\text{HCF}\ \leq\ \text{the smaller number}&\text{LCM}\ \geq\ \text{the larger number}\\[8pt]
\text{cutting into equal pieces}&\text{events happening together again}\\[8pt]
\multicolumn{2}{c}{\text{HCF}\times\text{LCM}=a\times b}
\end{array}""",
    "w2_pf":   r"24=2^{3}\times 3\ ,\qquad 36=2^{2}\times 3^{2}",
    "w2_hcf":  r"\text{HCF}=2^{2}\!\times\!3=12",
    "w2_lcm":  r"\text{LCM}=2^{3}\!\times\!3^{2}=72",
    "w2_check": r"12\times 72=864=24\times 36",
    "w2_rem":  r"n=dk+r\ ,\qquad 0\leq r<d",
    "w2_one":  r"\text{LCM}-1=11",
    "w2_cnt":  r"\text{multiples of }24\ \text{below}\ 100:\ \left\lfloor\dfrac{99}{24}\right\rfloor=4",
    "w2_t1": r"\text{HCF}(12,18)=6\ ,\qquad \text{LCM}(12,18)=36",
    "w2_t2": r"\text{LCM}(4,6)=12\ ,\qquad \textbf{not}\ \ 24",
    "w2_t3": r"r<d\ :\ \text{a remainder of }7\ \text{when dividing by }5\ \text{is impossible}",
    "w2_t4": r"49\div 9=5\ \text{remainder}\ 4\ \Rightarrow\ 6\ \text{boxes, not }5",
    "w2_t5": r"\text{“both again”}\ \Rightarrow\ \text{LCM},\qquad\text{“equal pieces”}\ \Rightarrow\ \text{HCF}",
    "w2_c1": r"\text{“at the same time again”}\ \Rightarrow\ \text{LCM}",
    "w2_c2": r"\text{“largest that divides both”}\ \Rightarrow\ \text{HCF}",
    "w2_c3": r"\text{“leaves remainder }r\text{”}\ \Rightarrow\ n=dk+r",
    "w2_c4": r"\text{“how many below }N\text{”}\ \Rightarrow\ \left\lfloor N\div n\right\rfloor",
    "w2_q1": r"\text{HCF of }\ 36\ \text{and}\ 60",
    "w2_q2": r"\text{LCM of }\ 12\ \text{and}\ 18",
    "w2_q3": r"\text{How many numbers below }100\ \text{are multiples of }6\ \text{and}\ 8\ ?",
    "w2_q4": r"\text{Smallest number leaving remainder }2\ \text{when divided by}\ 3,4\ \text{and}\ 5",
    "w2_q5": r"\text{HCF}(a,b)=6\ ,\ \text{LCM}(a,b)=72\ ,\ a=24.\ \text{Find }b.",
    "w2_q6": r"58\ \text{people, cars hold }4.\ \text{How many cars?}",
    "w2_a":  r"\text{Answers: }\ 12\ \cdot\ 36\ \cdot\ 4\ \cdot\ 62\ \cdot\ 18\ \cdot\ 15",

    # ================================================== WEEK 4 · percentages
    "w4_table": r"""\begin{array}{c|c@{\qquad}c|c}
\text{change}&\text{multiplier}&\text{percent}&\text{fraction}\\[6pt]\hline
\text{up }10\%&\times 1.1&5\%&\dfrac{1}{20}\\[10pt]
\text{up }15\%\ (\text{VAT})&\times 1.15&12.5\%&\dfrac{1}{8}\\[10pt]
\text{down }20\%&\times 0.8&25\%&\dfrac{1}{4}\\[10pt]
\text{down }25\%&\times 0.75&33\tfrac{1}{3}\%&\dfrac{1}{3}\\[10pt]
\text{up then down }20\%&\times 0.96&75\%&\dfrac{3}{4}
\end{array}""",
    "w4_of":     r"p\%\ \text{of}\ A=\dfrac{p}{100}\times A",
    "w4_change": r"\text{percent change}=\dfrac{\text{change}}{\textbf{original}}\times 100",
    "w4_rev":    r"\text{original}=\dfrac{\text{new value}}{\text{multiplier}}",
    "w4_succ":   r"0.75\times 1.15=0.8625",
    "w4_part":   r"\text{whole}=\text{part}\div\dfrac{p}{100}",
    "w4_t1": r"\times 1.2\ \text{then}\ \times 0.8=\times 0.96\ ,\qquad \textbf{not}\ \text{back to the start}",
    "w4_t2": r"\dfrac{\text{change}}{\text{original}}\ ,\qquad \textbf{not}\ \ \dfrac{\text{change}}{\text{new}}",
    "w4_t3": r"\text{“}20\%\ \text{more than}\ x\text{”}=1.2x\ ,\qquad \text{“}20\%\ \text{of}\ x\text{”}=0.2x",
    "w4_t4": r"\text{profit }\%=\dfrac{\text{profit}}{\textbf{cost}}\times 100",
    "w4_t5": r"15\%\ \text{of}\ 1\,200=180\ >\ \text{a cap of}\ 150",
    "w4_c1": r"\text{“after a discount, find the original”}\ \Rightarrow\ \div\ \text{multiplier}",
    "w4_c2": r"\text{“then VAT is added”}\ \Rightarrow\ \times\ \text{the next multiplier}",
    "w4_c3": r"\text{“this }p\%\ \text{came to }N\text{”}\ \Rightarrow\ \text{find the whole first}",
    "w4_c4": r"\text{“by what percent”}\ \Rightarrow\ \text{divide by the \textbf{original}}",
    "w4_q1": r"18\%\ \text{of}\ 4\,500\ \text{SAR}",
    "w4_q2": r"\text{A price rises }40\to 50.\ \text{By what percent?}",
    "w4_q3": r"\text{After }25\%\ \text{off, a coat costs }360\ \text{SAR. Original?}",
    "w4_q4": r"400\ \text{SAR},\ 25\%\ \text{off, then}\ 15\%\ \text{VAT}",
    "w4_q5": r"60\%\ \text{of a test is}\ 30\ \text{questions. How many are left?}",
    "w4_q6": r"\text{Cost}\ 80,\ \text{sold}\ 100.\ \text{Profit percent?}",
    "w4_a":  r"\text{Answers: }\ 810\ \cdot\ 25\%\ \cdot\ 480\ \cdot\ 345\ \cdot\ 20\ \cdot\ 25\%",

    # ================================================== WEEK 5 · rates
    "w5_table": r"""\begin{array}{l|l}
\text{speed}=\dfrac{\text{distance}}{\text{time}}&\text{time}=\dfrac{\text{distance}}{\text{speed}}\\[12pt]\hline
\text{average speed}=\dfrac{\text{TOTAL distance}}{\text{TOTAL time}}&\text{never the mean of two speeds}\\[12pt]
\text{one worker's rate}=\dfrac{1}{a}\ \text{per hour}&\text{together}=\dfrac{1}{a}+\dfrac{1}{b}\\[12pt]
\text{time together}=\dfrac{ab}{a+b}&\text{workers}\times\text{days}=\text{constant}\\[12pt]
\text{approaching}\ \Rightarrow\ \text{add the speeds}&1\ \text{km/h}=\dfrac{1}{3.6}\ \text{m/s}
\end{array}""",
    "w5_tri":   r"d=s\times t\ ,\qquad s=\dfrac{d}{t}\ ,\qquad t=\dfrac{d}{s}",
    "w5_avg":   r"\dfrac{120}{1+2}=40\ \text{km/h}",
    "w5_work":  r"\dfrac{2\times 3}{2+3}=1.2\ \text{h}",
    "w5_ppl":   r"6\times 10=4\times 15=60",
    "w5_conv":  r"90\ \text{km/h}=90\div 3.6=25\ \text{m/s}",
    "w5_t1": r"\dfrac{60+30}{2}=45\ \text{km/h}\ \ \textbf{is wrong};\ \ \text{the answer is}\ 40",
    "w5_t2": r"1.5\ \text{hours}=1\ \text{h}\ 30\ \text{min}\ ,\qquad \textbf{not}\ \ 1\ \text{h}\ 50\ \text{min}",
    "w5_t3": r"\text{rates add, \emph{times} do not}:\ \dfrac{1}{2}+\dfrac{1}{3}\neq\dfrac{1}{5}",
    "w5_t4": r"\text{a head start is distance already covered}:\ 340-60=280",
    "w5_t5": r"\text{more workers}\ \Rightarrow\ \text{fewer days (inverse, not direct)}",
    "w5_c1": r"\text{“the same route at two speeds”}\ \Rightarrow\ \dfrac{\text{total }d}{\text{total }t}",
    "w5_c2": r"\text{“working together”}\ \Rightarrow\ \text{add the rates}",
    "w5_c3": r"\text{“towards each other”}\ \Rightarrow\ \text{add the speeds}",
    "w5_c4": r"\text{“more workers, less time”}\ \Rightarrow\ \text{inverse proportion}",
    "w5_q1": r"\text{A car covers }150\ \text{km at}\ 60\ \text{km/h. How long?}",
    "w5_q2": r"\text{Two taps fill a tank in}\ 4\ \text{and}\ 12\ \text{hours. Together?}",
    "w5_q3": r"72\ \text{km/h in m/s}",
    "w5_q4": r"\text{40 km at 80 km/h, then 40 km at 40 km/h. Average speed?}",
    "w5_q5": r"5\ \text{workers take}\ 12\ \text{days}.\ 6\ \text{workers take}\ \underline{\quad}\ \text{days.}",
    "w5_q6": r"\text{Towns }300\ \text{km apart, cars at}\ 70\ \text{and}\ 80\ \text{km/h towards each other.}",
    "w5_a":  r"\text{Answers: }\ 2\tfrac{1}{2}\ \text{h}\ \cdot\ 3\ \text{h}\ \cdot\ 20\ \text{m/s}\ \cdot\ 53\tfrac{1}{3}\ \text{km/h}\ \cdot\ 10\ \cdot\ 2\ \text{h}",
}


def render(out_dir, dpi):
    shutil.rmtree(out_dir, ignore_errors=True)
    os.makedirs(out_dir)
    tmp = tempfile.mkdtemp()
    keys = list(E)
    doc = [r"\documentclass[12pt]{article}",
           r"\usepackage[active,tightpage]{preview}",
           r"\usepackage{amsmath,amssymb}",
           r"\usepackage[T1]{fontenc}",
           r"\usepackage[utf8]{inputenc}",
           r"\usepackage[dvipsnames]{xcolor}",
           r"\setlength\PreviewBorder{1.5pt}",
           r"\definecolor{ink}{HTML}{%s}" % INK,
           r"\renewcommand{\arraystretch}{2.05}",
           r"\begin{document}"]
    for k in keys:
        doc.append(r"\begin{preview}$\color{ink}\displaystyle %s$\end{preview}" % E[k])
    doc.append(r"\end{document}")
    tex = os.path.join(tmp, "pre.tex")
    open(tex, "w").write("\n".join(doc))
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-output-directory", tmp, tex], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-2500:]); raise SystemExit("pdflatex failed")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(tmp, "pre.pdf"), os.path.join(tmp, "p")], check=True)
    pages = sorted(f for f in os.listdir(tmp) if f.startswith("p-") and f.endswith(".png"))
    assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} expressions"
    idx = {}
    for k, p in zip(keys, pages):
        im = Image.open(os.path.join(tmp, p)).convert("RGBA")
        dst = os.path.join(out_dir, k + ".png")
        im.save(dst)
        # A stacked fraction makes the whole image taller, so sizing every image
        # by its BOX height prints those glyphs smaller than the rest. Record how
        # many text lines tall the expression is, and let the sheet size by that.
        src_tex = E[k]
        lines = 1 + src_tex.count(r"\\")
        if r"dfrac" in src_tex or r"\frac" in src_tex:
            lines = max(lines, 2)
        if r"begin{array}" in src_tex:
            lines = max(lines, 6)
        idx[k] = {"file": dst, "win": im.width / dpi, "hin": im.height / dpi,
                  "aspect": im.width / im.height, "lines": lines}
    json.dump(idx, open(os.path.join(out_dir, "_index.json"), "w"), indent=1)
    print(f"{len(idx)} expressions -> {out_dir} @ {dpi} dpi")


render("pre_math", 300)
