import sys, itertools
from fractions import Fraction
from figlib import *
import os
PRE=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'pre.txt')).read()
LEVEL_NAME={'E':'Easy','M':'Medium','H':'Hard','C':'SAT Challenge'}
LINES={'E':4,'M':6,'H':8,'C':10}
TOOL={'N':'No calculator needed','C':'Calculator','D':'Desmos'}
EXTRA=r"""
\usepackage{needspace}
\newcommand{\choiceK}[4]{\par\vspace{2pt}{\renewcommand{\arraystretch}{1.9}\begin{tabular}{@{}p{0.47\linewidth}p{0.47\linewidth}@{}}#1 & #2\\ #3 & #4\end{tabular}}}
\definecolor{SOLGREEN}{HTML}{15803D}
\newsavebox{\okb}\newcommand{\okopt}[1]{\sbox{\okb}{\textcolor{SOLGREEN}{\textbf{#1\ \checkmark}}}\ifdim\wd\okb>\dimexpr\linewidth-2\fboxsep\relax\colorbox{SOLGREEN!14}{\parbox[t]{\dimexpr\linewidth-2\fboxsep\relax}{\textcolor{SOLGREEN}{\textbf{#1\ \checkmark}}}}\else\colorbox{SOLGREEN!14}{\usebox{\okb}}\fi}

\newcommand{\keyspace}[2]{\par\nopagebreak
 \setbox0\vbox{\hsize\linewidth\color{SOLGREEN}\small #2\par}%
 \setbox1\vbox{\foreach \i in {1,...,#1}{\par\vspace{0.74cm}{\color{LINE}\hrule height 0.4pt}}}%
 \ifdim\ht0>\ht1 \dimen2=\ht0 \else \dimen2=\ht1 \fi
 \vbox to \dimen2{\nointerlineskip\vbox to 0pt{\box1\vss}\nointerlineskip\box0\vss}\par\vspace{4pt}}
\newcommand{\stepsbox}[1]{\par\vspace{3pt}\begin{tcolorbox}[enhanced,breakable,colback=TEAL!4,colframe=TEAL!70!black,boxrule=0.5pt,arc=2pt,left=5pt,right=5pt,top=2pt,bottom=2pt,fonttitle=\bfseries\small,title={Worked solution}]#1\end{tcolorbox}}
"""
def fig(body, scale=1.0, xu=0.55, yu=0.55):
    return (r"\begin{center}\begin{tikzpicture}[x=%scm,y=%scm,scale=%s]"%(xu,yu,scale)+FIGSTYLE+body+r"\end{tikzpicture}\end{center}")

def opts_tex(opts, correct, mode):
    cells=[]
    for i,o in enumerate("ABCD"):
        t="(%s)\\ %s"%(o,opts[i])
        if mode=='key' and i==correct: t=r"\okopt{%s}"%t
        cells.append(t)
    return r"\choiceK{%s}{%s}{%s}{%s}"%tuple(cells)

def problem_tex(n,p,mode):
    t=(r"\newpage " if p.get("pb") else "")+r"\begin{minipage}{\linewidth}"+r"\textbf{\textcolor{NAVY}{%d.}}\hfill\lvl{%s \textperiodcentered\ %s}\\[1pt]"%(n,LEVEL_NAME[p['lv']],TOOL[p.get('tool','N')])
    t+=p['q']
    if p.get('fig'): t+=p['fig']
    if p.get('opts'): t+=opts_tex(p['opts'],p['correct'],mode)
    if mode=='key':
        ans=("(%s)"%"ABCD"[p['correct']]) if p.get('opts') else "$%s$"%p['ans']
        st=r"\begin{enumerate}[leftmargin=1.5em,itemsep=0pt,topsep=1pt,label=\textbf{\arabic*.}]"+"".join(r"\item "+s for s in p['steps'])+r"\end{enumerate}"
        t+=r"\keyspace{%d}{"%p.get('lines',LINES[p['lv']])+st+r"\textbf{Answer: "+ans+r"}}"
    else:
        t+=r"\par\nopagebreak\foreach \i in {1,...,%d}{\par\vspace{0.74cm}{\color{LINE}\hrule height 0.4pt}}\par\vspace{4pt}"%p.get('lines',LINES[p['lv']])
    t+=r"\end{minipage}"+r"\par\vspace{3pt}"+"\n"
    return t

def build(meta,guided,problems,mode,out):
    key=(mode=='key')
    head=meta.get('headfull') or "Week %s%s \\textemdash\\ %s"%(meta['week'],meta['session'],meta.get('short',meta['title']))
    L=[PRE.replace("@@CODE@@",meta['code']+"").replace("@@HEAD@@",head).replace("\\begin{document}",EXTRA+"\\begin{document}")]
    L.append(r"""
\begin{tcolorbox}[enhanced,colback=NAVY!4,colframe=NAVY,boxrule=0.8pt,arc=3pt]
{\Large\bfseries\color{NAVY} SAT Math Mastery \textperiodcentered\ %s}\\[2pt]
{\large\bfseries %s%s}\\[3pt]
\begin{tabular}{@{}p{0.2\linewidth}p{0.75\linewidth}@{}}
\textbf{Time} & %s\\
\textbf{Topics} & %s\\
\textbf{Name / Date} & \rule{5.5cm}{0.3pt}\ \ \rule{3cm}{0.3pt}\\
\end{tabular}
\end{tcolorbox}
"""%(meta.get('boxhead') or 'Week %s%s'%(meta['week'],meta['session']),meta['title'],"",meta.get('time',"120 minutes: 90 min solving \\,+\\, 30 min self-check and error log"),meta['topics']))
    L.append(r"\banner{1 \textperiodcentered\ Skills \& Ideas}"+meta['skills'])
    L.append(r"\banner{2 \textperiodcentered\ Required Facts}"+meta['facts'])
    L.append(r"\banner{3 \textperiodcentered\ Required Formulas}"+meta['formulas'])
    L.append(r"\banner{4 \textperiodcentered\ Mini Theory Sheet}"+meta['theory'].replace("\n\\textbf{","\n\n\\textbf{"))
    L.append(r"\banner{5 \textperiodcentered\ Guided Examples}"+guided)
    L.append(r"\newpage\banner{6 \textperiodcentered\ Practice Set \textemdash\ %d problems \textperiodcentered\ %s}"%(len(problems),meta.get('setsub',"Easy $\\to$ Medium $\\to$ Hard $\\to$ SAT Challenge")))
    L.append(r"\small Each problem states its tool. Write your work in the space below. Multiple choice: one correct option. Student-produced response (SPR): enter an exact value (fraction or decimal).\normalsize\par\vspace{4pt}")
    for i,p in enumerate(problems,1): L.append(problem_tex(i,p,mode))
    L.append(r"\end{document}")
    open(out,"w").write("\n".join(L))

def prep(P):
    """verify, then rotate options to balance answer letters"""
    for i,p in enumerate(P):
        r=p['chk']()
        if p.get('opts'):
            assert r==('idx',p['correct']),(i+1,r,p['correct'])
        else:
            assert abs(float(r)-float(p['val']))<1e-9,(i+1,r,p['val'])
        p['n']=i+1
    pos=0
    for p in P:
        if p.get('opts') and not p.get('norot'):
            tgt=[1,2,0,3,2,1,3,0][pos%8]; pos+=1
            k=(tgt-p['correct'])%4
            p['opts']=p['opts'][-k:]+p['opts'][:-k] if k else p['opts']
            p['correct']=tgt
    return P
