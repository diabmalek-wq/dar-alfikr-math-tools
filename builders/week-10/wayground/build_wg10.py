import subprocess, io, contextlib
from wg10 import L, verify
verify()
PRE = open("/home/claude/sat_w6/build_sat6.py").read().split('PRE = r"""')[1].split('"""')[0]
PRE = PRE.replace(r"SAT-M \textperiodcentered\ W6 \textperiodcentered\ G11@@KEYCODE@@", r"Wayground \textperiodcentered\ W10 \textperiodcentered\ @@CODE@@")
PRE = PRE.replace(r"\definecolor{BLUE}", r"\definecolor{OK}{HTML}{1B7F4B}\definecolor{BLUE}")
TAG = {"S": ("MAROON", "SELF-REPORT"), "P": ("MAROON", "PRE-SESSION CHECK"), "R": ("NAVY", "READINESS")}

def opts_tex(q):
    out = []
    if q["type"] == "Match":
        rows = " \\\\ ".join(r"%s & $\to$ & \textcolor{OK}{\textbf{%s}}" % p for p in q["pairs"])
        return r"\begin{tabular}{@{}p{4.2cm}c l@{}}%s\end{tabular}" % rows + r"\ {\scriptsize\color{GREY}(shown shuffled in Wayground)}"
    if q["type"] == "Reorder":
        return r"\textcolor{OK}{\textbf{Correct order:}}\ " + r"\ $\to$\ ".join(r"\textcolor{OK}{%s}" % o for o in q["order"])
    if "ans" in q:
        return r"\textcolor{OK}{\textbf{Accept:}}\ %s" % q["ans"]
    cells = []
    for i, o in enumerate(q["opts"]):
        if i in q["ok"]: cells.append(r"\textcolor{OK}{\textbf{$\checkmark$\ %s.\ %s}}" % ("ABCD"[i], o))
        else: cells.append(r"\phantom{$\checkmark$\ }%s.\ %s" % ("ABCD"[i], o))
    if len(cells) == 2: return r"\quad ".join(cells)
    while len(cells) < 4: cells.append("")
    a = r"\renewcommand{\arraystretch}{2.2}" if any("dfrac" in o for o in q["opts"]) else ""
    return r"{%s\begin{tabular}{@{}p{0.47\linewidth}p{0.47\linewidth}@{}}%s & %s\\ %s & %s\end{tabular}}" % (a, *cells)

def card(q):
    col, lab = TAG[q["tag"]]
    ti = r"\textbf{%d}\ \ %s\ \textperiodcentered\ 30\,s\hfill\textcolor{%s}{\scriptsize\bfseries %s}" % (q["n"], q["type"].upper(), col, lab)
    sg = r"\par\vspace{2pt}{\scriptsize\color{GREY}\textit{Signal.}\ %s}" % q["sig"]
    if q.get("img"):
        body = r"\begin{minipage}[c]{0.64\linewidth}" + q["t"] + r"\par\vspace{3pt}" + opts_tex(q) + r"\end{minipage}\hfill\begin{minipage}[c]{0.32\linewidth}\centering\includegraphics[width=\linewidth]{%s.png}\end{minipage}" % q["img"] + sg
    else:
        body = q["t"] + r"\par\vspace{2pt}" + opts_tex(q) + sg
    return (r"\begin{tcolorbox}[enhanced,colback=white,colframe=LINE,colbacktitle=%s!9,coltitle=INK,fonttitle=\small,boxrule=0.5pt,arc=2pt,left=7pt,right=7pt,top=3pt,bottom=3pt,toptitle=1.5pt,bottomtitle=1.5pt,title={%s},before skip=5pt,after skip=0pt]%s\end{tcolorbox}" % (col, ti, body))

def doc(d):
    Q = d["qs"]
    t = PRE.replace("@@CODE@@", "WG-" + d["code"].replace("/", "-"))
    t += r"""{\Large\bfseries\color{NAVY}Kick-off Diagnostic \textperiodcentered\ %s \textemdash\ %s}\hfill{\small\color{GREY}%s}\par
\vspace{2pt}{\small\color{GREY}8 questions \textperiodcentered\ 30 seconds each \textperiodcentered\ about 4 minutes \textperiodcentered\ Diagnose phase (6 min of 60)}\par\vspace{3pt}\hrule\vspace{4pt}
""" % (d["code"], d["title"], d["grade"])
    t += r"""\begin{tcolorbox}[colback=NAVY!5,colframe=NAVY!40,boxrule=0.4pt,arc=2pt,left=7pt,right=7pt,top=3pt,bottom=3pt,before skip=2pt,after skip=0pt]
\small\textbf{Pre-session anchor} (stations 1 and 2 of the pre-session say this, so items 2 and 6 test it).\\
\textbf{The one idea:} %s\\
\textbf{The mistake most students make:} %s\\
\textbf{Readiness items 3, 4, 5, 7, 8 test:} %s.\par\vspace{1pt}
\textbf{Wayground set-up:} timer 30\,s on every question; shuffle options on, questions off; hide the leaderboard; show answers after the quiz, not after each item. Item 1 is a poll (no points). Items 2 to 8 are 1 point each. Tags below: \textcolor{MAROON}{\textbf{maroon}} = tells you about the pre-session, \textcolor{NAVY}{\textbf{navy}} = readiness for today. \textcolor{OK}{\textbf{Green}} = correct.
\end{tcolorbox}
""" % (d["idea"], d["mistake"], d["prior"])
    for q in Q: t += card(q) + "\n"
    r0, r1 = d["route"]
    t += r"""\par\vspace{7pt}{\large\bfseries\color{NAVY}Read the results (90 seconds)}\par\vspace{2pt}
\begin{tabular}{@{}p{3.6cm}p{13.4cm}@{}}
\textbf{Readiness} $R$ &
\textbf{Items 3, 4, 5, 7, 8 (out of 5).} \textbf{0--2} $\to$ @@R0@@. \textbf{3--4} $\to$ @@R1@@; fix the missed item in passing. \textbf{5} $\to$ start the Investigate prompt now.\\[3pt]
\textbf{Pre-session} $P$ &
\textbf{Items 2 and 6 (out of 2), read with the item 1 poll.}\\
\end{tabular}\par\vspace{3pt}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{@{}p{5.2cm}p{3.7cm}p{8.1cm}@{}}
\toprule
\textbf{What you see} & \textbf{Reading} & \textbf{What you do}\\\midrule
Poll ``all'' or ``read'', $P=2$ & Prepared & Nothing extra. Use their $R$ score to route.\\
Poll ``all'' or ``read'', $P=0$ & Claimed, did not retain & Two-minute recap of the one idea at the start. Ask them to restate it in their own words.\\
Poll ``opened'' or ``did not open'' & Task not done & No penalty. Pair with a prepared partner for Targeted Instruction; note it for your task tracker.\\
$R\le 2$ and $P=2$ & Content gap & Re-teach group. The task was done, so the idea needs a different explanation.\\
$R\ge 4$ and $P\le 1$ & Task skipped, skills fine & Move on. Chase the task, not the content.\\
\bottomrule
\end{tabular}\par\vspace{3pt}
{\small\textbf{Class-level rule.} If more than $30\%$ of the class chose ``opened'' or ``did not open'', or the class average on $P$ is below $1$, spend three minutes recapping the one idea above before Targeted Instruction. If more than $30\%$ score $R\le 2$, the whole class takes the re-teach route first.}
\end{document}""".replace("@@R0@@", r0).replace("@@R1@@", r1)
    return t

for k, d in L.items():
    n = d["file"]
    open(n + ".tex", "w").write(doc(d))
    for _ in range(2): subprocess.run(["xelatex", "-interaction=nonstopmode", n + ".tex"], capture_output=True, text=True)
    log = open(n + ".log", errors="ignore").read()
    print(n, [l for l in log.splitlines() if l.startswith("!")][:4])
    out = subprocess.run(["pdfinfo", n + ".pdf"], capture_output=True, text=True).stdout
    print([l for l in out.splitlines() if l.startswith("Pages")])
