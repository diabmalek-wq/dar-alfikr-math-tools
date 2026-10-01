PREAMBLE = r"""
\documentclass[10pt]{article}
\usepackage[a4paper,left=1.7cm,right=1.7cm,top=2.3cm,bottom=2.3cm,headheight=0.9cm,headsep=0.35cm,footskip=1.0cm]{geometry}
\usepackage{amsmath,amssymb,mathtools}
\usepackage{xcolor,graphicx,array,booktabs,enumitem,lastpage,pgffor}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,patterns}
\usepackage[most]{tcolorbox}
\usepackage{fancyhdr}
\usepackage{fontspec}\usepackage{microtype}
\definecolor{NAVY}{HTML}{1F3A5F}\definecolor{INK}{HTML}{1A1A1A}\definecolor{TEAL}{HTML}{1A7F8E}
\definecolor{BLUE}{HTML}{2F6DB5}\definecolor{ORANGE}{HTML}{E07B39}\definecolor{GREY}{HTML}{6B7280}
\definecolor{GOLD}{HTML}{C9A227}\definecolor{LINE}{HTML}{C7CDD6}
\setlength{\parindent}{0pt}\setlength{\parskip}{3pt}
\renewcommand{\arraystretch}{1.25}
\newcommand{\WSCODE}{@@CODE@@}
\pagestyle{fancy}\fancyhf{}
\renewcommand{\headrulewidth}{0.5pt}\renewcommand{\headrule}{\hbox to\headwidth{\color{NAVY}\leaders\hrule height \headrulewidth\hfill}}
\renewcommand{\footrulewidth}{0pt}
\fancyhead[L]{\small\bfseries\color{NAVY}SAT Math Mastery \textperiodcentered\ @@HEAD@@}
\fancyhead[R]{\small\color{GREY}Mr Malek Thiab}
\fancyfoot[L]{\footnotesize\color{GREY}\WSCODE}
\fancyfoot[C]{\footnotesize\color{NAVY}{\addfontfeatures{LetterSpace=18}\textsc{Faith, Righteousness and Wisdom}}}
\fancyfoot[R]{\footnotesize\color{GREY}Mr Malek Thiab \textperiodcentered\ Page \thepage\ of \pageref{LastPage}}
\newtcolorbox{cbox}[2][]{enhanced,breakable,colback=#2!5,colframe=#2!70!black,boxrule=0.6pt,arc=2pt,left=5pt,right=5pt,top=3pt,bottom=3pt,fonttitle=\bfseries\small,#1}
\newcommand{\banner}[1]{\vspace{6pt}\par\noindent\begin{tcolorbox}[enhanced,colback=NAVY,colframe=NAVY,boxrule=0pt,arc=2pt,left=6pt,top=1pt,bottom=1pt,nobeforeafter]\color{white}\bfseries\small\MakeUppercase{#1}\end{tcolorbox}\par\nopagebreak\vspace{2pt}}
\newcommand{\worklines}[1]{\par\nopagebreak\foreach \i in {1,...,#1}{\par\vspace{0.74cm}{\color{LINE}\hrule height 0.4pt}}\par\vspace{4pt}}
\newcommand{\lvl}[1]{\textcolor{GREY}{\scriptsize\textsc{#1}}}
\newcommand{\choice}[4]{\par\vspace{2pt}\begin{tabular}{@{}p{0.47\linewidth}p{0.47\linewidth}@{}}(A)\ #1 & (B)\ #2\\ (C)\ #3 & (D)\ #4\end{tabular}}
\begin{document}
"""

FIGSTYLE = r"""
\tikzset{axisline/.style={-{Stealth[length=2.2mm]},thick,INK},gridl/.style={LINE!80,very thin},
 ln/.style={very thick,BLUE},pt/.style={circle,fill=ORANGE,inner sep=1.6pt}}
"""


def axes(xmin, xmax, ymin, ymax, xs=1, ys=1, xl='x', yl='y', lab_x=None, lab_y=None, ymult=1):
    """return tikz code (inside picture) for a grid with axes and tick labels"""
    s = []
    s.append(r"\draw[gridl] (%s,%s) grid[xstep=%s,ystep=%s] (%s,%s);" % (xmin, ymin, xs, ys, xmax, ymax))
    s.append(r"\draw[axisline] (%s,0) -- (%s,0) node[right]{$%s$};" % (xmin, xmax + 0.35, xl))
    s.append(r"\draw[axisline] (0,%s) -- (0,%s) node[above]{$%s$};" % (ymin, ymax + 0.35, yl))
    lx = lab_x if lab_x is not None else xs
    ly = lab_y if lab_y is not None else ys
    x = xmin
    xt = []
    import math
    k = math.ceil(xmin / lx)
    while k * lx <= xmax:
        v = k * lx
        if abs(v) > 1e-9:
            xt.append(r"\draw (%s,0.07)--(%s,-0.07) node[below,font=\scriptsize]{$%g$};" % (v, v, v))
        k += 1
    k = math.ceil(ymin / ly)
    while k * ly <= ymax:
        v = k * ly
        if abs(v) > 1e-9:
            xt.append(r"\draw (0.07,%s)--(-0.07,%s) node[left,font=\scriptsize]{$%g$};" % (v, v, v*ymult))
        k += 1
    s += xt
    s.append(r"\node[below left,font=\scriptsize] at (0,0) {$O$};")
    return "\n".join(s)


def fig(body, scale=1.0, xu=0.55, yu=0.55):
    return (r"\begin{center}\begin{tikzpicture}[x=%scm,y=%scm,scale=%s]" % (xu, yu, scale)
            + FIGSTYLE + body + r"\end{tikzpicture}\end{center}")


def choices_tex(opts):
    return r"\choice{%s}{%s}{%s}{%s}" % tuple(opts)


LEVEL_NAME = {'E': 'Easy', 'M': 'Medium', 'H': 'Hard', 'C': 'SAT Challenge'}
LINES = {'E': 4, 'M': 6, 'H': 8, 'C': 10}


TOOL={'N':'No calculator needed','C':'Calculator','D':'Desmos'}
def problem_tex(n, p):
    t = r"\begin{minipage}{\linewidth}\textbf{\textcolor{NAVY}{%d.}}\hfill\lvl{%s \textperiodcentered\ %s}\\[1pt]" % (n, LEVEL_NAME[p['lv']], TOOL[p.get('tool','N')])
    t += p['q']
    if p.get('fig'):
        t += p['fig']
    if p.get('opts'):
        t += choices_tex(p['opts'])
    t += r"\worklines{%d}" % p.get('lines', LINES[p['lv']]) + r"\end{minipage}\par\vspace{2pt}" + "\n"
    return t


def answer_display(p):
    if p.get('opts'):
        return "%s" % "ABCD"[p['correct']]
    return p['ans']


def build(meta, guided, problems, out):
    """meta: dict with code,week,session,title,topics,skills,facts,formulas,theory,strategy"""
    L = [PREAMBLE.replace("@@CODE@@", meta['code']).replace("@@HEAD@@", "Week %s \\textperiodcentered\\ Session %s \\textemdash\\ %s" % (meta['week'], meta['session'], meta['title']))]
    # header block
    L.append(r"""
\begin{tcolorbox}[enhanced,colback=NAVY!4,colframe=NAVY,boxrule=0.8pt,arc=3pt]
{\Large\bfseries\color{NAVY} SAT Math Mastery Program \textperiodcentered\ Week %s, Session %s}\\[2pt]
{\large\bfseries %s}\\[3pt]
\begin{tabular}{@{}p{0.2\linewidth}p{0.75\linewidth}@{}}
\textbf{Time} & 120 minutes: 90 min solving \,+\, 30 min self-check and error log\\
\textbf{Target topics} & %s\\
\textbf{Teacher} & Mr Malek Thiab \textperiodcentered\ Dar Alfikr School\\
\textbf{Name / Date} & \rule{5.5cm}{0.3pt}\ \ \rule{3cm}{0.3pt}\\
\end{tabular}
\end{tcolorbox}
""" % (meta['week'], meta['session'], meta['title'], meta['topics']))
    L.append(r"\banner{1 \textperiodcentered\ Skills \& Ideas}" + meta['skills'])
    L.append(r"\banner{2 \textperiodcentered\ Required Facts}" + meta['facts'])
    L.append(r"\banner{3 \textperiodcentered\ Required Formulas}" + meta['formulas'])
    L.append(r"\banner{4 \textperiodcentered\ Mini Theory Sheet}" + meta['theory'].replace("\n\\textbf{", "\n\n\\textbf{"))
    L.append(r"\begin{cbox}[title={5 \textperiodcentered\ Strategy Box}]{ORANGE}" + meta['strategy'] + r"\end{cbox}")
    L.append(r"\banner{6 \textperiodcentered\ Guided Examples}" + guided)
    L.append(r"\newpage\banner{7 \textperiodcentered\ Practice Set \textemdash\ %d problems \textperiodcentered\ Easy $\to$ Medium $\to$ Hard $\to$ SAT Challenge}" % len(problems))
    L.append(r"\small Write your work in the space below each problem. Circle your final answer. Multiple choice: one correct option. Student-produced response (SPR): enter an exact value (fraction or decimal).\normalsize\par\vspace{4pt}")
    for i, p in enumerate(problems, 1):
        L.append(problem_tex(i, p))
    # hints
    L.append(r"\newpage\banner{8 \textperiodcentered\ Hint Section \textemdash\ hints only, no solutions}")
    L.append(r"\begin{enumerate}[leftmargin=1.6em,itemsep=1.5pt,label=\textbf{\arabic*.}]")
    for p in problems:
        L.append(r"\item " + p['hint'])
    L.append(r"\end{enumerate}")
    L.append(r"\newpage\banner{9 \textperiodcentered\ Full Solutions}")
    for i, p in enumerate(problems, 1):
        L.append(r"\begin{minipage}{\linewidth}\textbf{\textcolor{NAVY}{%d.}} \textbf{Answer: %s}.\ %s\end{minipage}\par\vspace{5pt}" % (
            i, ("(%s)" % answer_display(p)) if p.get('opts') else "$%s$" % p['ans'], p['sol']))
    L.append(r"\end{document}")
    open(out, "w").write("\n".join(L))
