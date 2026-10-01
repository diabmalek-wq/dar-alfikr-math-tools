import io, contextlib, re, subprocess, sys, os
with contextlib.redirect_stdout(io.StringIO()):
    import sat6
from sat6 import ITEMS

PRE = r"""
\documentclass[10pt]{article}
\usepackage[a4paper,left=1.7cm,right=1.7cm,top=3.0cm,bottom=2.2cm,headheight=1.6cm,headsep=0.3cm,footskip=1.0cm]{geometry}
\usepackage{amsmath,amssymb,mathtools}
\usepackage{xcolor,graphicx,array,booktabs,enumitem,lastpage}
\usepackage{tikz}\usetikzlibrary{arrows.meta,calc}
\usepackage[most]{tcolorbox}
\usepackage{fancyhdr}
\usepackage{fontspec}\usepackage{microtype}
\definecolor{NAVY}{HTML}{1F3A5F}\definecolor{INK}{HTML}{1A1A1A}\definecolor{GREY}{HTML}{6B7280}
\definecolor{LINE}{HTML}{C7CDD6}\definecolor{MAROON}{HTML}{8B1E3F}\definecolor{BLUE}{HTML}{2F6DB5}
\setlength{\parindent}{0pt}\setlength{\parskip}{3pt}
\renewcommand{\arraystretch}{1.25}
\pagestyle{fancy}\fancyhf{}
\renewcommand{\headrulewidth}{0.5pt}\renewcommand{\headrule}{\hbox to\headwidth{\color{NAVY}\leaders\hrule height \headrulewidth\hfill}}
\fancyhead[L]{\raisebox{-0.35\height}{\includegraphics[height=1.05cm]{dept_logo_doc.png}}}
\fancyhead[C]{\raisebox{-0.35\height}{\includegraphics[height=1.15cm]{cognia_badge_doc.png}}}
\fancyhead[R]{\raisebox{-0.35\height}{\includegraphics[height=1.15cm]{school_logo_doc.png}}}
\fancyfoot[L]{\footnotesize\color{GREY}SAT-M \textperiodcentered\ W6 \textperiodcentered\ G11@@KEYCODE@@}
\fancyfoot[C]{\footnotesize\color{NAVY}{\addfontfeatures{LetterSpace=18}\textsc{Faith, Righteousness and Wisdom}}}
\fancyfoot[R]{\footnotesize\color{GREY}Mr Malek Thiab \textperiodcentered\ Page \thepage\ of \pageref{LastPage}}
\newcommand{\lvl}[1]{\textcolor{GREY}{\scriptsize\textsc{#1}}}
\newcommand{\optrow}[4]{\par\vspace{1pt}\begin{tabular}{@{}p{0.47\linewidth}p{0.47\linewidth}@{}}(A)\ #1 & (B)\ #2\\ (C)\ #3 & (D)\ #4\end{tabular}}
\newcommand{\optlist}[4]{\par\vspace{1pt}\begin{tabular}{@{}l@{\ }p{0.93\linewidth}@{}}(A)&#1\\(B)&#2\\(C)&#3\\(D)&#4\end{tabular}}
\begin{document}
"""

TOOL = {"N": "No calculator", "C": "Calculator", "D": "Desmos"}

HIST = r"""\begin{center}\begin{tikzpicture}[x=0.19cm,y=0.33cm]
\foreach \y in {2,4,6,8,10}{\draw[LINE,very thin] (0,\y)--(50,\y);}
\foreach \l/\h in {0/2,10/5,20/9,30/3,40/1}{\draw[fill=BLUE!25,draw=NAVY,thick] (\l,0) rectangle (\l+10,\h);}
\draw[thick,INK] (0,0)--(52,0);\draw[thick,INK] (0,0)--(0,10.6);
\foreach \x in {0,10,20,30,40,50}{\draw (\x,0.1)--(\x,-0.25) node[below,font=\scriptsize]{$\x$};}
\foreach \y in {0,2,4,6,8,10}{\draw (0.5,\y)--(-0.5,\y) node[left,font=\scriptsize]{$\y$};}
\node[font=\scriptsize,rotate=90] at (-6.2,5) {Frequency};
\node[font=\scriptsize] at (25,-2.6) {Value};
\end{tikzpicture}\end{center}"""

BOX = r"""\begin{center}\begin{tikzpicture}[x=0.17cm,y=0.5cm]
\def\bx#1#2#3#4#5#6{\draw[thick,INK] (#1,#6)--(#2,#6);\draw[thick,INK] (#5,#6)--(#4,#6);
 \draw[thick,INK] (#1,#6-0.28)--(#1,#6+0.28);\draw[thick,INK] (#5,#6-0.28)--(#5,#6+0.28);
 \draw[fill=BLUE!20,draw=NAVY,thick] (#2,#6-0.4) rectangle (#4,#6+0.4);\draw[very thick,NAVY] (#3,#6-0.4)--(#3,#6+0.4);}
\bx{40}{55}{68}{80}{96}{1.8}\bx{50}{60}{64}{72}{90}{0.4}
\node[left,font=\small] at (36,1.8) {Class $X$};\node[left,font=\small] at (36,0.4) {Class $Y$};
\draw[thick,INK] (36,-0.5)--(100,-0.5);
\foreach \x in {40,50,60,70,80,90,100}{\draw (\x,-0.4)--(\x,-0.62) node[below,font=\scriptsize]{$\x$};}
\node[font=\scriptsize] at (68,-1.7) {Score};
\end{tikzpicture}\end{center}"""

def item_tex(n, p, key=False):
    q = p["q"].replace(r"\HIST", HIST).replace(r"\BOX", BOX)
    t = r"\begin{minipage}{\linewidth}\textbf{\textcolor{NAVY}{%d.}}\hfill\lvl{%s}\\[1pt]" % (n, TOOL[p["tool"]])
    t += q
    if "opts" in p:
        body = (r"\optrow" if p["mode"] == "grid" else r"\optlist") + "".join("{%s}" % o for o in p["opts"])
        if any("dfrac" in o for o in p["opts"]):
            body = r"{\renewcommand{\arraystretch}{2.2}" + body + "}"
        t += body
    else:
        t += r"\par\smallskip\hfill\textit{\small Student-produced response: enter your answer as a number.}"
    return t + r"\end{minipage}"

# ---------- student paper: 4 pages, items per page chosen to fill each page
PAGES = [["A1", "A2", "A3", "B1", "B2", "B3"],
         ["C1", "C2", "C3", "C4", "C5"],
         ["C6", "C7", "C8", "C9"],
         ["C10", "C11", "C12", "C13", "D1", "D2", "D3"]]
if os.path.exists("pages.txt"):
    PAGES = [l.split() for l in open("pages.txt").read().strip().splitlines()]
byid = {i["id"]: i for i in ITEMS}
num = {i["id"]: k for k, i in enumerate(ITEMS, 1)}
assert sorted(sum(PAGES, [])) == sorted(byid) and len(sum(PAGES, [])) == 22

def paper():
    L = [PRE.replace("@@KEYTAG@@", "").replace("@@KEYCODE@@", "")]
    L.append(r"""{\Large\bfseries\color{NAVY}SAT Math \textperiodcentered\ Week 6 Practice Set}\hfill{\small\color{GREY}22 questions \textperiodcentered\ 32 minutes}\par
\vspace{2pt}\noindent Name\ \rule{6.2cm}{0.3pt}\hfill Class\ \rule{2.2cm}{0.3pt}\hfill Date\ \rule{2.8cm}{0.3pt}\par\vspace{4pt}\hrule\vspace{6pt}""")
    for pi, pg in enumerate(PAGES):
        for j, iid in enumerate(pg):
            L.append(item_tex(num[iid], byid[iid]) + r"\par\vfill")
        if pi < len(PAGES) - 1:
            L.append(r"\newpage")
    L.append(r"\end{document}")
    return "\n".join(L)

# ---------- teacher key
def key_tex():
    L = [PRE.replace("@@KEYTAG@@", r" \textperiodcentered\ Answer Key").replace("@@KEYCODE@@", r" \textperiodcentered\ KEY")]
    L.append(r"""{\Large\bfseries\color{NAVY}SAT Math \textperiodcentered\ Week 6 \textemdash\ Answer Key and Worked Solutions}\par
{\small\color{GREY}Teacher copy \textperiodcentered\ Grade 11 (11C) \textperiodcentered\ do not circulate with the student paper}\par\vspace{4pt}\hrule\vspace{4pt}""")
    L.append(r"\textbf{Conditions.} $22$ questions, $32$ minutes (about $1.45$ min each), the student paper carries no preamble. Each question shows its tool: no calculator, calculator, or Desmos. Student-produced responses accept any equivalent exact value; write decimals as printed.\par")
    mc = [i for i in ITEMS if "opts" in i]
    strip = " \\quad ".join(r"\textbf{%d}\,%s" % (num[i["id"]], ("(%s)" % "ABCD"[i["key"]]) if "opts" in i else "$%s$" % i["ans"]) for i in ITEMS)
    L.append(r"\par\textbf{Answer strip.}\ " + strip + r"\par")
    from collections import Counter
    cnt = Counter("ABCD"[i["key"]] for i in mc)
    org = Counter(i["wk"].split(" \u00b7 ")[0] for i in ITEMS)
    lv = Counter(i["lv"] for i in ITEMS)
    L.append(r"\par\textbf{Balance.} Multiple-choice letters (15 items): A $%d$, B $%d$, C $%d$, D $%d$. Numeric options are printed in ascending order, as on the real test, so their letters follow the value. Student-produced responses: 7 items. Difficulty: Medium %d, Hard %d. Origin: anchor to this week %d, spiral from Weeks 1--5 %d, seeded from Weeks 7--9 %d.\par" % (cnt["A"], cnt["B"], cnt["C"], cnt["D"], lv["M"], lv["H"], org["Anchor"], org["Spiral"], org["Seed"]))
    L.append(r"\par\textbf{Week 6 anchor (9 items).} 6A Percents, items 7--10 (percent change, chained and reversed changes, table subsets, mixtures). 6B Center, Spread and Plots, items 11--15 (frequency tables, outliers, histograms, box plots, effect of shifting and scaling). \textbf{Spiral (7 items):} linear equations and systems, budget inequalities, transformations, tangency, exponential models, unit conversion. \textbf{Seeded (6 items):} residuals, probability, margin of error, right-triangle trigonometry, circle equations, sphere surface area.\par")
    L.append(r"\vspace{2pt}\hrule\vspace{6pt}")
    for i in ITEMS:
        n = num[i["id"]]
        ans = ("(%s)" % "ABCD"[i["key"]]) if "opts" in i else "$%s$" % i["ans"]
        lvname = {"M": "Medium", "H": "Hard"}[i["lv"]]
        t = r"\begin{minipage}{\linewidth}\textbf{\textcolor{NAVY}{%d.}}\ \textbf{Answer: %s}\hfill\lvl{%s \textperiodcentered\ %s \textperiodcentered\ %s}\\[1pt]" % (n, ans, lvname, TOOL[i["tool"]], i["wk"].replace("\u00b7", r"\textperiodcentered"))
        t += r"{\small\color{GREY}%s}\\[1pt]" % i["sk"].replace("&", r"\&")
        t += r"\textbf{\textcolor{MAROON}{THE TRICK \textemdash\ %s.}}\ " % i["trick"].rstrip(".")
        t += i["sol"]
        if "opts" in i:
            t += r"\\[1pt]{\small\textit{Wrong options.}\ " + i["why"] + "}"
        else:
            t += r"\\[1pt]{\small\textit{Common error.}\ " + i["why"] + "}"
        t += r"\end{minipage}\par\vspace{5pt}"
        L.append(t)
    L.append(r"\end{document}")
    return "\n".join(L)

def build(name, tex):
    open(name + ".tex", "w").write(tex)
    r = subprocess.run(["xelatex", "-interaction=nonstopmode", name + ".tex"], capture_output=True, text=True)
    r = subprocess.run(["xelatex", "-interaction=nonstopmode", name + ".tex"], capture_output=True, text=True)
    log = open(name + ".log", errors="ignore").read()
    errs = [l for l in log.splitlines() if l.startswith("!")]
    print(name, "errors:", errs[:5])

if __name__ == "__main__":
    build("SAT6_paper", paper())
    build("SAT6_key", key_tex())
