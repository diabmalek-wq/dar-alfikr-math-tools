import json,re,sys
F0=json.load(open('/home/claude/cb/tp2_final.json'))+json.load(open('/home/claude/cb/tp3_final.json'))
import collections
SETN=int(sys.argv[1])
g=collections.defaultdict(list)
for f in sorted(F0,key=lambda f:(f['id'].split('-')[0],int(f['id'].split('-')[1]))): g[(f['id'].split('-')[0],f['diff'],f['tool'])].append(f)
F=[];k=0
for key in sorted(g):
    for f in g[key]:
        if k%2==SETN-1: F.append(f)
        k+=1
print(len(F),collections.Counter(f['id'].split('-')[0] for f in F),collections.Counter(f['diff'] for f in F))
def fx(s): return s.replace('✓',r'$\checkmark$').replace('²',r'\textsuperscript{2}').replace('–','--')
DOM=[("Algebra","A-"),("Advanced Math","AM-"),("Geometry and Trigonometry","GT-"),("Problem-Solving and Data Analysis","PS-")]
def build(ans):
    L=[r"""\documentclass[10.5pt]{article}
\usepackage[a4paper,margin=1.7cm,top=1.5cm,bottom=1.6cm]{geometry}
\usepackage[utf8]{inputenc}\usepackage[T1]{fontenc}\usepackage{amsmath,amssymb,xcolor,helvet,fancyhdr,enumitem,needspace}
\renewcommand{\familydefault}{\sfdefault}
\definecolor{navy}{HTML}{1F3864}\definecolor{teal}{HTML}{17A199}\definecolor{ans}{HTML}{1B7F3B}\definecolor{tag}{HTML}{6B3FA0}
\pagestyle{fancy}\fancyhf{}\renewcommand{\headrulewidth}{0pt}
\fancyfoot[L]{\scriptsize SAT Math $\cdot$ Final Revision Set @S@}\fancyfoot[R]{\scriptsize Mr Malek Thiab $\cdot$ Page \thepage}
\setlength{\parindent}{0pt}\setlength{\parskip}{1.2mm}
\newcommand{\dom}[1]{\needspace{8\baselineskip}\vspace{3mm}{\color{white}\colorbox{navy}{\parbox{\dimexpr\linewidth-2\fboxsep}{\bfseries\large\ #1}}}\par\vspace{1mm}}
\begin{document}
{\color{navy}\LARGE\bfseries SAT Math Final Revision Set @S@}\par
{\color{teal}\large\bfseries @N@ questions $\cdot$ 2 hours  """+("$\\cdot$ Answers and solutions" if ans else "")+r"""}\par\vspace{1mm}
{\small Name \makebox[6cm]{\dotfill}\hfill Date \makebox[3.5cm]{\dotfill}}\par\vspace{1mm}
{\footnotesize Each question states its tool: \textbf{No calculator needed}, \textbf{Calculator} or \textbf{Desmos}. Multiple-choice questions have one correct answer. For student-produced responses (SPR), write your answer in the box.}\par\rule{\linewidth}{0.5pt}
"""]
    n=0
    for dn,pre in DOM:
        items=[f for f in F if f['id'].startswith(pre)]
        L.append(r"\dom{"+dn+f" ({len(items)} items)"+"}")
        for f in items:
            n+=1
            L.append(r"\needspace{7\baselineskip}")
            L.append(rf"\textbf{{\color{{navy}}{n}.}}\ {{\scriptsize\color{{tag}}\textbf{{{f['id']}}} $\cdot$ {f['diff']} $\cdot$ {'Multiple choice' if f['opts_final'] else 'SPR'} $\cdot$ \textbf{{{f['tool']}}}}}\par")
            L.append(fx(f['q'])+r"\par")
            if f['opts_final']:
                L.append(r"\begin{enumerate}[label=\Alph*),leftmargin=2.2em,itemsep=0.6mm,topsep=0.6mm]")
                for o in f['opts_final']: L.append(r"\item "+fx(o))
                L.append(r"\end{enumerate}")
            elif not ans:
                L.append(r"\fbox{\rule{0pt}{5mm}\hspace{3cm}}\par")
            if ans:
                L.append(r"{\color{ans}\textbf{Answer: "+fx(f['ans_final'])+r"}\par "+fx(f['rat'])+r"\par{\small\textit{Trap:} "+fx(f['mis'])+r"}}\par")
            else:
                L.append(r"\vspace{14mm}")
            L.append(r"\vspace{1mm}{\color{gray!50}\rule{\linewidth}{0.3pt}}\par")
    L.append(r"\end{document}")
    return "\n".join(L).replace("@S@",str(SETN)).replace("@N@",str(len(F)))
open('ws%d.tex'%SETN,'w').write(build(False));open('ans%d.tex'%SETN,'w').write(build(True))
