import io, contextlib, subprocess
with contextlib.redirect_stdout(io.StringIO()):
    import saat6
from saat6 import ITEMS
from collections import Counter

PRE = r"""
\documentclass[10pt]{article}
\usepackage[a4paper,left=1.7cm,right=1.7cm,top=3.0cm,bottom=2.2cm,headheight=1.6cm,headsep=0.3cm,footskip=1.0cm]{geometry}
\usepackage{amsmath,amssymb,mathtools}
\usepackage{xcolor,graphicx,array,booktabs,enumitem,lastpage}
\usepackage{fancyhdr}
\usepackage{fontspec}\usepackage{microtype}
\definecolor{NAVY}{HTML}{1F3A5F}\definecolor{INK}{HTML}{1A1A1A}\definecolor{GREY}{HTML}{6B7280}
\definecolor{MAROON}{HTML}{8B1E3F}
\setlength{\parindent}{0pt}\setlength{\parskip}{3pt}
\renewcommand{\arraystretch}{1.25}
\pagestyle{fancy}\fancyhf{}
\renewcommand{\headrulewidth}{0.5pt}\renewcommand{\headrule}{\hbox to\headwidth{\color{NAVY}\leaders\hrule height \headrulewidth\hfill}}
\fancyhead[L]{\raisebox{-0.35\height}{\includegraphics[height=1.05cm]{dept_logo_doc.png}}}
\fancyhead[C]{\raisebox{-0.35\height}{\includegraphics[height=1.15cm]{cognia_badge_doc.png}}}
\fancyhead[R]{\raisebox{-0.35\height}{\includegraphics[height=1.15cm]{school_logo_doc.png}}}
\fancyfoot[L]{\footnotesize\color{GREY}SAAT-M \textperiodcentered\ W6 \textperiodcentered\ G11@@KEYCODE@@}
\fancyfoot[C]{\footnotesize\color{NAVY}{\addfontfeatures{LetterSpace=18}\textsc{Faith, Righteousness and Wisdom}}}
\fancyfoot[R]{\footnotesize\color{GREY}Mr Malek Thiab \textperiodcentered\ Page \thepage\ of \pageref{LastPage}}
\newcommand{\lvl}[1]{\textcolor{GREY}{\scriptsize\textsc{#1}}}
\newcommand{\optrow}[4]{\par\vspace{1pt}\begin{tabular}{@{}p{0.47\linewidth}p{0.47\linewidth}@{}}(A)\ #1 & (B)\ #2\\ (C)\ #3 & (D)\ #4\end{tabular}}
\newcommand{\optlist}[4]{\par\vspace{1pt}\begin{tabular}{@{}l@{\ }p{0.93\linewidth}@{}}(A)&#1\\(B)&#2\\(C)&#3\\(D)&#4\end{tabular}}
\begin{document}
"""
PAGES = [list(range(1, 7)), list(range(7, 13)), list(range(13, 19)), list(range(19, 25))]
LISTMODE = {8}

def item_tex(it):
    n = it["n"]
    t = r"\begin{minipage}{\linewidth}\textbf{\textcolor{NAVY}{%d.}}\\[1pt]" % n + it["q"]
    body = (r"\optlist" if n in LISTMODE else r"\optrow") + "".join("{%s}" % o["tex"] for o in it["opts"])
    if any("dfrac" in o["tex"] for o in it["opts"]) or any("\\frac" in o["tex"] for o in it["opts"]):
        body = r"{\renewcommand{\arraystretch}{2.1}" + body + "}"
    return t + body + r"\end{minipage}"

def paper():
    L = [PRE.replace("@@KEYCODE@@", "")]
    L.append(r"""{\Large\bfseries\color{NAVY}SAAT (Tahsili) Mathematics \textperiodcentered\ Week 6 Practice Set}\hfill{\small\color{GREY}24 questions \textperiodcentered\ 28 minutes}\par
\vspace{2pt}\noindent Name\ \rule{6.2cm}{0.3pt}\hfill Class\ \rule{2.2cm}{0.3pt}\hfill Date\ \rule{2.8cm}{0.3pt}\par\vspace{4pt}\hrule\vspace{6pt}""")
    for pi, pg in enumerate(PAGES):
        for n in pg:
            L.append(item_tex(ITEMS[n-1]) + r"\par\vfill")
        if pi < 3: L.append(r"\newpage")
    L.append(r"\end{document}")
    return "\n".join(L)

def key_tex():
    L = [PRE.replace("@@KEYCODE@@", r" \textperiodcentered\ KEY")]
    L.append(r"""{\Large\bfseries\color{NAVY}SAAT (Tahsili) Mathematics \textperiodcentered\ Week 6 \textemdash\ Answer Key}\par
{\small\color{GREY}Teacher copy \textperiodcentered\ Grade 11 (11C) \textperiodcentered\ do not circulate with the student paper}\par\vspace{4pt}\hrule\vspace{4pt}""")
    L.append(r"\textbf{Conditions.} $24$ questions, $28$ minutes, no calculator, one mark each. Options carrying maths are typeset; numeric options print in ascending order, so their letters follow the value.\par")
    strip = " \\quad ".join(r"\textbf{%d}\,(%s)" % (i["n"], "ABCD"[i["key"]]) for i in ITEMS)
    L.append(r"\par\textbf{Answer strip.}\ " + strip + r"\par")
    cnt = Counter("ABCD"[i["key"]] for i in ITEMS)
    st = Counter(i["strand"] for i in ITEMS); org = Counter(i["wk"].split(" \u00b7 ")[0] for i in ITEMS)
    L.append(r"\par\textbf{Balance.} Answer letters A $%d$, B $%d$, C $%d$, D $%d$. Strands: algebra %d, geometry %d, statistics and probability %d, trigonometry, vectors and complex numbers %d, calculus %d. Origin: anchor to this week %d, spiral %d, seeded from later units %d.\par" % (cnt["A"], cnt["B"], cnt["C"], cnt["D"], st["ALG"], st["GEO"], st["STA"], st["TRI"], st["CAL"], org["Anchor"], org["Spiral"], org["Seed"]))
    L.append(r"\par\textbf{Week 6 anchor (items 1--8).} Logarithms and exponential decay (this week's Grade 11 lessons 6-3 and 6-4) and the three forms of a quadratic (this week's Grade 10 lessons 2-1 to 2-3). \textbf{Spiral (9 items):} exponents and radicals, linear systems in context, composite domains, similarity, circle angles, coordinate geometry, percentages, the normal distribution, counting. \textbf{Seeded (7 items):} solids, double-angle trigonometry, vectors, complex powers, limits, derivatives and integration, which Tahsili tests before the course reaches them.\par")
    L.append(r"\vspace{2pt}\hrule\vspace{6pt}")
    for it in ITEMS:
        t = r"\begin{minipage}{\linewidth}\textbf{\textcolor{NAVY}{%d.}}\ \textbf{Answer: (%s)}\hfill\lvl{%s \textperiodcentered\ %s}\\[1pt]" % (it["n"], "ABCD"[it["key"]], {"ALG": "Algebra", "GEO": "Geometry", "STA": "Statistics and probability", "TRI": "Trigonometry, vectors, complex", "CAL": "Calculus"}[it["strand"]], it["wk"].replace("\u00b7", r"\textperiodcentered"))
        t += r"\textbf{\textcolor{MAROON}{THE TRICK \textemdash\ %s.}}\ " % it["trick"].rstrip(".") + it["sol"]
        wrong = "; ".join("(%s) %s" % ("ABCD"[j], o["note"].rstrip(".").replace(r"\,", "")) if False else r"(%s) %s" % ("ABCD"[j], o["note"].rstrip(".")) for j, o in enumerate(it["opts"]) if not o["ok"])
        t += r"\\[1pt]{\small\textit{Wrong options.}\ " + wrong + ".}"
        t += r"\end{minipage}\par\vspace{5pt}"
        L.append(t)
    L.append(r"\end{document}")
    return "\n".join(L)

def build(name, tex):
    open(name + ".tex", "w").write(tex)
    for _ in range(2): subprocess.run(["xelatex", "-interaction=nonstopmode", name + ".tex"], capture_output=True, text=True)
    log = open(name + ".log", errors="ignore").read()
    print(name, [l for l in log.splitlines() if l.startswith("!")][:5])

build("SAAT6_paper", paper()); build("SAAT6_key", key_tex())
