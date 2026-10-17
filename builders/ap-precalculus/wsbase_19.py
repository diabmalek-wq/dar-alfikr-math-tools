import sys,subprocess
sys.path.insert(0,"/home/claude/quiz2")
from build import PRE
PRE=PRE.replace(r"\begin{document}",r"\definecolor{SOL}{HTML}{1B7A3E}\begin{document}")
L="ABCD"
def D(s): return s
# ---------- items: (stem, correct, [3 distractors], pos, why)
def mcq(n,stem,c,dis,pos,fig=None):
    o=list(dis); o.insert(pos,c)
    return o
def build(name,top,title,M,F,fig,solved):
    key=[]
    t=PRE
    t+=r"\hd{%s}{%s}{%s}{%s}"%(top,title,"Section 1 --- Multiple Choice","Circle the letter of the correct answer"+(r" \,\textbf{\color{SOL}SOLVED}" if solved else ""))+"\n\\namebox\n\\vspace{5pt}\n"
    t+=r"{\small No credit for unsupported answers in Section 2. Questions 1--8: 1 point each (8 points).}\par\vspace{7pt}"+"\n"
    t+=r"{\small "
    for i,(s,c,d,p,why) in enumerate(M,1):
        o=mcq(i,s,c,d,p); key.append(L[p])
        def opt(k):
            x=r"\textbf{%s.}\ %s"%(L[k],o[k])
            return (r"\textcolor{SOL}{\textbf{%s}}"%("") if False else (r"\colorbox{TEALL}{\textcolor{SOL}{%s}}"%x if (solved and k==p) else x))
        figtxt=""
        if fig and i==3:
            figtxt=r"\hfill\raisebox{-1.6cm}{\includegraphics[height=2.6cm]{%s}}"%fig
        t+=r"\noindent\begin{minipage}{\linewidth}\qn{%d}\ %s\par\vspace{4pt}"%(i,s)
        long_=max(len(x) for x in o)>34
        if fig and i==3:
            t+=r"\begin{minipage}[t]{0.64\linewidth}\hspace{18pt}\begin{minipage}[t]{0.85\linewidth}%s\par\vspace{3pt}%s\par\vspace{3pt}%s\par\vspace{3pt}%s\end{minipage}\end{minipage}\hfill\begin{minipage}[t]{0.33\linewidth}\raggedleft\vspace{-8pt}\includegraphics[height=3.7cm]{%s}\end{minipage}"%(opt(0),opt(1),opt(2),opt(3),fig)
        elif long_:
            t+=r"\hspace{18pt}\begin{minipage}[t]{0.9\linewidth}%s\par\vspace{3pt}%s\par\vspace{3pt}%s\par\vspace{3pt}%s\end{minipage}"%(opt(0),opt(1),opt(2),opt(3))
        else:
            t+=r"\hspace{18pt}\begin{tabular}{@{}p{0.45\linewidth}p{0.42\linewidth}@{}}%s & %s\\[%s] %s & %s\end{tabular}"%(opt(0),opt(1),"8pt" if "dfrac" in o[0]+o[1]+o[2]+o[3] else "5pt",opt(2),opt(3))
        if solved:
            w=why
            for j in range(3): w=w.replace("{d%d}"%j,L[j if j<p else j+1])
            t+=r"\par\vspace{2pt}\hspace{18pt}{\footnotesize\color{SOL}\textbf{%s.}\ %s}"%(L[p],w)
        t+=r"\end{minipage}"+("\n\\vspace{2pt}\n" if i<len(M) else "\n")
    t+="}"
    t+=r"\par\newpage"+"\n"
    t+=r"\hd{%s}{%s}{%s}{%s}"%(top.replace("Questions","")+" · SECTION 2",title,"Section 2 --- Free Response","Show all working; answers need units and limit notation where relevant")+"\n"
    qn=9
    for f in F:
        t+=r"""\begin{tcolorbox}[colback=PANEL,colframe=TEALL!80!black,boxrule=0.5pt,arc=3pt,left=8pt,right=8pt,top=4pt,bottom=4pt,breakable=false]
{\small\colorbox{NAVY}{\color{white}\bfseries\ Question %d\ }}\ {\footnotesize\bfseries\color{GREY}%s \ ·\ %d points}\par\vspace{4pt}
%s\par\vspace{4pt}
"""%(qn,f["tag"],f["pts"],f["ctx"])
        for j,(q,pts,sol,h) in enumerate(f["parts"]):
            t+=r"\textbf{(%s)} %s\hfill\dok{%d}{%d}\par\vspace{3pt}"%("abc"[j],q,f["dok"],pts)
            if solved:
                t+=r"\begin{tcolorbox}[colback=white,colframe=SOL,boxrule=0.5pt,arc=2pt,left=6pt,top=2pt,bottom=2pt]{\small\color{SOL}%s}\end{tcolorbox}"%sol
            else:
                t+=r"\begin{tcolorbox}[colback=white,colframe=TEALL!80!black,enhanced,boxrule=0.4pt,frame style={dashed},height=%.1fcm,arc=2pt]\end{tcolorbox}"%(h*2.3)
            t+=r"\par\vspace{4pt}"
        t+=r"\end{tcolorbox}\vspace{6pt}"+"\n"
        qn+=1
    if solved:
        t+=r"\par{\footnotesize\bfseries\color{SOL}Answer key (Section 1): %s}"%"\\ ".join("%d%s"%(i+1,k) for i,k in enumerate(key))
    t+=r"\end{document}"
    open(name+".tex","w").write(t)
    for _ in range(2): r=subprocess.run(["xelatex","-interaction=nonstopmode",name+".tex"],capture_output=True,text=True)
    errs=[l for l in r.stdout.split("\n") if l.startswith("!")]
    n=subprocess.run(["pdfinfo",name+".pdf"],capture_output=True,text=True).stdout.split("Pages:")[1].split()[0]
    print(name,errs,n,"pages",''.join(key))
