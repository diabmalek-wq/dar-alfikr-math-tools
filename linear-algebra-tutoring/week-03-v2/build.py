import subprocess,sys
from data import *
import data as D
def pre(ans):
    sub = "Worksheet with Worked Answers" if ans else "Worksheet"
    return r"""\documentclass[11pt]{article}
\usepackage[a4paper,margin=1.9cm,top=2.4cm,bottom=2.2cm]{geometry}
\usepackage{amsmath,amssymb,amsfonts,fontspec,microtype,fancyhdr,lastpage,enumitem,needspace}
\usepackage[most]{tcolorbox}
\usepackage{xcolor}
\definecolor{ink}{HTML}{1F3A5F}\definecolor{soft}{HTML}{EEF3F9}\definecolor{ans}{HTML}{F3F8F1}\definecolor{ansb}{HTML}{3C7A3C}
\pagestyle{fancy}\fancyhf{}
\lhead{\small\color{ink}\textbf{Linear Algebra I} \textperiodcentered\ Week @W@ --- @H@}
\rhead{}\cfoot{\small Mr Malek Thiab \textperiodcentered\ %s \textperiodcentered\ Page \thepage\ of \pageref{LastPage}}
\renewcommand{\headrulewidth}{0.4pt}
\setlength{\parindent}{0pt}\setlength{\parskip}{4pt}
\newcommand{\lv}[1]{\textsc{\small #1}}
\begin{document}
""".replace("@W@",str(D.WEEK)).replace("@H@",D.HEADT) % sub
def title():
    return r"""{\Large\bfseries\color{ink} Linear Algebra I --- Week @W@}\\[2pt]
{\large\bfseries\color{ink} """+TITLE+r"""}\\[3pt]
{\small Name: \underline{\hspace{5cm}}\hfill Date: \underline{\hspace{3cm}}\qquad All work \textbf{by hand} --- no calculator, no software.}
\vspace{4pt}\hrule\vspace{8pt}
""".replace("@W@",str(D.WEEK))
FACTS=r"""
\begin{tcolorbox}[colback=soft,colframe=ink,title={\bfseries Key Facts}]
\textbf{Complex numbers.} $i^{2}=-1$; $\overline{a+bi}=a-bi$; $z\overline z=|z|^{2}=a^{2}+b^{2}$; $\dfrac{z}{w}=\dfrac{z\,\overline w}{|w|^{2}}$. Also $\overline{z+w}=\overline z+\overline w$, $\overline{zw}=\overline z\,\overline w$, and $z=\overline z\iff z\in\mathbb{R}$.

\textbf{Matrices over $\mathbb{C}$.} $M_{m\times n}(\mathbb{C})$ is the set of $m\times n$ matrices with complex entries. Addition and scalar multiplication are entrywise; $(AB)_{jk}=\sum_{l}A_{jl}B_{lk}$. Multiplication is associative but \emph{not} commutative.

\textbf{Conjugate transpose.} $(A^{*})_{jk}=\overline{A_{kj}}$. Rules: $(A+B)^{*}=A^{*}+B^{*}$, $(\lambda A)^{*}=\overline{\lambda}A^{*}$, $(AB)^{*}=B^{*}A^{*}$, $(A^{*})^{*}=A$.
$A$ is \textbf{Hermitian} if $A^{*}=A$; \textbf{skew-Hermitian} if $A^{*}=-A$.

\textbf{Vector space over $\mathbb{F}$.} A set $V$ with $+$ and scalar multiplication satisfying: commutativity and associativity of $+$; a zero vector $\mathbf 0$; additive inverses; $1v=v$; $(\lambda\mu)v=\lambda(\mu v)$; $\lambda(u+v)=\lambda u+\lambda v$; $(\lambda+\mu)v=\lambda v+\mu v$.
Standard examples: $\mathbb{F}^{n}$, $M_{m\times n}(\mathbb{F})$, $P_{n}(\mathbb{F})$ (polynomials of degree $\le n$), $\mathcal F(S,\mathbb{F})$ (functions $S\to\mathbb{F}$, pointwise operations).

\textbf{Subspace test.} $W\subseteq V$ is a subspace iff (i) $\mathbf 0\in W$, (ii) $u,v\in W\Rightarrow u+v\in W$, (iii) $\lambda\in\mathbb{F},\,v\in W\Rightarrow\lambda v\in W$. To disprove: exhibit one failure. The field matters: a set can be a subspace over $\mathbb{R}$ but not over $\mathbb{C}$.
\end{tcolorbox}
"""
def example(n,e):
    t,st,steps,a=e
    s=r"\begin{tcolorbox}[colback=white,colframe=ink!60,title={\bfseries Example %d \textperiodcentered\ %s}]"%(n,t)
    s+=st+"\n\\par\\smallskip\n\\textbf{Solution.} "
    s+=r"\begin{enumerate}[leftmargin=1.6em,itemsep=1pt,topsep=2pt,label=\arabic*.]"+"".join(r"\item "+x+"\n" for x in steps)+r"\end{enumerate}"
    s+=r"\textbf{Answer:} "+a+"\n\\end{tcolorbox}\n"
    return s
def prob(n,p,ans):
    sec,lvl,st,sp,steps,a=p
    s=(r"\Needspace{%d\baselineskip}"%(9 if ans else 6))+r"\begin{minipage}{\linewidth}\textbf{%d.} \hfill{\scriptsize\color{ink}[%s]}\par\nopagebreak "%(n,lvl)+st+"\n"
    if not ans:
        s+=r"\vspace{%.1fcm}"%sp+r"\end{minipage}\par\vspace{4pt}"+"\n"
    else:
        s+=r"\end{minipage}\par\nopagebreak"+"\n"
        s+=r"\begin{tcolorbox}[breakable,colback=ans,colframe=ansb,boxrule=0.5pt,left=4pt,right=4pt,top=2pt,bottom=2pt]"
        s+=r"\begin{enumerate}[leftmargin=2.2em,itemsep=1pt,topsep=1pt,label=\textbf{Step \arabic*.}]"+"".join(r"\item "+x+"\n" for x in steps)+r"\end{enumerate}"
        s+=r"\textbf{Answer:} "+a+r"\end{tcolorbox}"+"\n\\par\\vspace{2pt}\n"
    return s
def build(ans,name):
    t=pre(ans)+title()+D.FACTS+"\n\\newpage\n\\section*{\\large\\color{ink} Worked Examples}\n"
    for i,e in enumerate(EX,1): t+=example(i,e)
    t+="\\newpage\n\\section*{\\large\\color{ink} Practice Problems}\n"
    cur=None;n=0
    for p in P:
        n+=1
        if p[0]!=cur:
            cur=p[0]; t+=r"\Needspace{10\baselineskip}\subsection*{\normalsize\color{ink} Part %s --- %s}"%(cur,dict(SECS)[cur])+"\n"
        t+=prob(n,p,ans)
    t+="\\end{document}\n"
    t=t.replace("@W@",str(D.WEEK))
    open(name+".tex","w").write(t)
    for _ in range(2):
        r=subprocess.run(["xelatex","-interaction=nonstopmode",name+".tex"],capture_output=True,text=True)
    if "Error" in r.stdout or "!" in r.stdout:
        print([l for l in r.stdout.split("\n") if l.startswith("!")][:5])
build(False,D.FILE+"_Worksheet")
build(True,D.FILE+"_Worksheet-with-Answers")
