import json, re, subprocess, sys, os, io, contextlib
HERE=os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE); sys.path.insert(0,HERE)
with contextlib.redirect_stdout(io.StringIO()):
    import figs9
IT={o['id']:o for o in json.load(open('items9.json'))}
def gt(i,tool,mode=None):
    o=IT[i]; p=dict(id=i,lv='M' if o['d']=='Medium' else 'H',tool=tool,q=o['q'].replace('°','^\\circ'),fig=figs9.FIG[i]() if i in figs9.FIG else "")
    if o['opts']: p['opts']=o['opts']; p['mode']=mode or ('grid' if max(len(x) for x in o['opts'])<28 else 'list')
    return p
def am(i,tool,q,lv='H',opts=None):
    p=dict(id=i,lv=lv,tool=tool,q=q,fig="")
    if opts: p['opts']=opts; p['mode']='grid'
    return p
ITEMS=[
 am('AM-094','N',r"The functions $f$ and $h$ are defined by $f(x)=x^{2}+3x-40$ and $h(x)=x^{2}$. If $3h(x)=f(2x)$, what is the positive value of $x$?"),
 am('AM-087','N',r"$$x^{2}(x+5)(x-b)=0$$ In the given equation, $b$ is a positive constant. The sum of the solutions of the equation is $7$. What is the value of $b$?"),
 am('AM-081','N',r"If $\dfrac{x^{a^{2}}}{x^{b^{2}}}=x^{20}$, $x>1$, and $a+b=4$, what is the value of $a-b$?"),
 am('AM-091','N',r"$a$ and $b$ are positive consecutive integers, and $b>a$. If $b$ is thirteen more than $\sqrt{a}$, what is the value of $a$?"),
 am('AM-031','N',r"If $x^{2}-8x+5=0$ has roots $r$ and $s$, what is the value of $r^{2}+s^{2}$?"),
 am('AM-007','D',r"In the $xy$-plane, the graphs of $y=x^{2}-6x+8$ and $y=2x-4$ intersect at two points. What is the sum of the $x$-coordinates of these two points?"),
 am('AM-090','N',r"If $s^{2}=t^{-1}$ and $t^{1/3}=u^{-1/2}$, then what is the value of $s$ in terms of $u$, for $s>0$?",opts=[r"$u^{-3/4}$",r"$u^{-1/2}$",r"$u^{1/2}$",r"$u^{3/4}$"]),
 am('AM-028','N',r"The function $N$ is defined by $N(t)=k\cdot2^{-at}$ for positive constants $k$ and $a$. The table shows values of $N$ for select values of $t$.\par\smallskip\begin{center}\renewcommand{\arraystretch}{1.2}\begin{tabular}{|c|c|c|c|}\hline $t$&$0$&$1$&$2$\\\hline $N(t)$&$200$&$50$&$12.5$\\\hline\end{tabular}\end{center}What is the value of $a$?"),
 gt('GT-004','N'),gt('GT-018','N'),gt('GT-005','N'),gt('GT-040','D'),gt('GT-006','N'),gt('GT-028','N'),gt('GT-029','N'),gt('GT-038','C'),gt('GT-039','N'),gt('GT-194-2','C'),
 gt('GT-043','D'),gt('GT-151','D'),gt('GT-128','N'),gt('GT-178','C'),gt('GT-263','C'),gt('GT-087','C'),gt('GT-023-2','N')]
NQ=len(ITEMS); MIN=round(NQ*1.45); assert NQ==25 and len({p['id'] for p in ITEMS})==25
src=open('build_sat9.py').read()
PRE=re.search(r'PRE = r"""(.*?)"""',src,re.S).group(1).replace(r"\definecolor{NAVY}",r"\definecolor{ORANGE}{HTML}{E8762C}\definecolor{NAVY}").replace("W9","W10")
TOOL={"N":"No calculator","C":"Calculator","D":"Desmos"}
def item_tex(n,p):
    q=p['q']
    t=r"\begin{minipage}{\linewidth}\textbf{\textcolor{NAVY}{%d.}}\hfill\lvl{%s}\\[1pt]"%(n,TOOL[p['tool']])+q+p['fig']
    if p.get('opts'):
        body=(r"\optrow" if p['mode']=='grid' else r"\optlist")+"".join("{%s}"%o for o in p['opts'])
        if any("dfrac" in o for o in p['opts']): body=r"{\renewcommand{\arraystretch}{2.2}"+body+"}"
        t+=body
    else: t+=r"\par\smallskip\hfill\textit{\small Student-produced response: enter your answer as a number.}"
    return t+r"\end{minipage}"
PAGES=[l.split() for l in open('pages.txt').read().strip().splitlines()] if os.path.exists('pages.txt') else None
def paper():
    L=[PRE.replace("@@KEYCODE@@","")]
    L.append(r"""{\Large\bfseries\color{NAVY}SAT Math \textperiodcentered\ Week 10 Practice Set}\hfill{\small\color{GREY}%d questions \textperiodcentered\ %d minutes}\par
\vspace{2pt}\noindent Name\ \rule{6.2cm}{0.3pt}\hfill Class\ \rule{2.2cm}{0.3pt}\hfill Date\ \rule{2.8cm}{0.3pt}\par\vspace{4pt}\hrule\vspace{6pt}"""%(NQ,MIN))
    ids=[p['id'] for p in ITEMS]; byid={p['id']:p for p in ITEMS}; num={i:k for k,i in enumerate(ids,1)}
    pg=PAGES or [ids[0:6],ids[6:12],ids[12:18],ids[18:24]]
    assert sorted(sum(pg,[]))==sorted(ids)
    for pi,page in enumerate(pg):
        for iid in page: L.append(item_tex(num[iid],byid[iid])+r"\par\vfill")
        if pi<len(pg)-1: L.append(r"\newpage")
    L.append(r"\end{document}"); return "\n".join(L)
open("SAT10_paper.tex","w").write(paper())
for _ in range(2): subprocess.run(["xelatex","-interaction=nonstopmode","SAT10_paper.tex"],capture_output=True,text=True)
log=open("SAT10_paper.log",errors="ignore").read(); print([l for l in log.splitlines() if l.startswith("!")][:5], 'overfull',log.count('Overfull'))
