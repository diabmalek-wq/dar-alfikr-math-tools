import re,sys,collections
TWO = len(sys.argv)>1 and sys.argv[1]=='2'
t=open('/home/claude/cb/bank_new5.md').read()
idx={}
for r in re.findall(r'^\| ([A-Z]{1,3}-\d+) \| ([^|]*) \| ([^|]*) \| ([^|]*) \| ([^|]*) \|',t,flags=re.M):
    idx[r[0]]=[x.strip() for x in r[1:]]
bl=re.split(r'^### (?=[A-Z]{1,3}-\d+\s*$)',t,flags=re.M)[1:]
SKN={('Advanced Math','Function notation'):'Nonlinear functions',('Algebra','Function notation'):'Linear functions',
('Advanced Math','Nonlinear equations in one variable'):'Nonlinear equations in one variable and systems of equations in two variables'}
def normskill(d,s):
    if (d,s) in SKN: return SKN[(d,s)]
    if s.startswith('One-variable data'): return 'One-variable data: Distributions and measures of center and spread'
    return s
ORDER={'Algebra':['Linear equations in one variable','Linear equations in two variables','Linear functions','Systems of two linear equations in two variables','Linear inequalities in one or two variables'],
'Advanced Math':['Equivalent expressions','Nonlinear equations in one variable and systems of equations in two variables','Nonlinear functions'],
'Geometry and Trigonometry':['Area and volume','Lines, angles, and triangles','Right triangles and trigonometry','Circles'],
'Problem-Solving and Data Analysis':['Ratios, rates, proportional relationships, and units','Percentages','One-variable data: Distributions and measures of center and spread','Two-variable data: Models and scatterplots','Probability and conditional probability','Inference from sample statistics and margin of error','Evaluating statistical claims: Observational studies and experiments']}
def esc(s):
    s=s.replace('&nbsp;','\\quad ').replace('✓','$\\checkmark$').replace('²','\\textsuperscript{2}').replace('³','\\textsuperscript{3}')
    s=s.replace('°','$^\\circ$').replace('—','---').replace('–','--').replace('×','$\\times$').replace('≤','$\\le$').replace('≥','$\\ge$').replace('π','$\\pi$').replace('≈','$\\approx$')
    s=re.sub(r'(?<!\\)([%&#_])',r'\\\1',s)
    s=re.sub(r'\*\*(.+?)\*\*',r'\\textbf{\1}',s)
    s=s.replace('~','\\textasciitilde{}')
    return s
def mathfix(m):
    return m.replace('°','^\\circ ').replace('²','^2').replace('≤','\\le ').replace('≥','\\ge ').replace('–','-')
MATH=re.compile(r'(?<!\\)\$\$.*?(?<!\\)\$\$|(?<!\\)\$.*?(?<!\\)\$',re.S)
def inline(s):
    out=[];p=0
    for m in MATH.finditer(s):
        out.append(esc(s[p:m.start()])); g=mathfix(m.group(0))
        if g.startswith('$$'): g='\\['+g[2:-2]+'\\]'
        out.append(g); p=m.end()
    out.append(esc(s[p:])); return ''.join(out)
def table(lines):
    rows=[[c.strip() for c in l.strip().strip('|').split('|')] for l in lines if not re.match(r'^\s*\|[\s:|-]+\|\s*$',l)]
    n=len(rows[0]); 
    s='\\begin{center}\\renewcommand{\\arraystretch}{1.15}\\small\\setlength{\\tabcolsep}{3pt}\\begin{tabular}{|'+'c|'*n+'}\\hline\n'
    for i,r in enumerate(rows):
        s+=' & '.join(inline(c) for c in r)+'\\\\\\hline\n'
    return s+'\\end{tabular}\\end{center}\n'
def body(s):
    s=re.sub(r'\[Figure:(.*?)(?: — diagram file[^\]]*)?\]',lambda m:'\n\n@@FIG'+m.group(1).strip()+'@@\n\n',s,flags=re.S)
    blocks=[];tik=re.findall(r'```latex\n(.*?)```',s,re.S)
    s=re.sub(r'\*\*Figure \(TikZ source[^\n]*\n+```latex\n.*?```','\n@@TIKZ@@\n',s,flags=re.S)
    out=[];lines=s.split('\n');i=0;ti=0
    while i<len(lines):
        l=lines[i]
        if l.strip().startswith('|'):
            j=i
            while j<len(lines) and lines[j].strip().startswith('|'): j+=1
            out.append(table(lines[i:j])); i=j; continue
        if l.strip()=='@@TIKZ@@': out.append(tik[ti]); ti+=1
        elif l.startswith('@@FIG'): out.append('\\figbox{'+inline(l[5:-2])+'}')
        elif l.strip()=='': out.append('')
        else: out.append(inline(l)+('\\\\' if (i+1<len(lines) and lines[i+1].strip() and not lines[i+1].strip().startswith(('|','@@')) and not MATH.fullmatch(l.strip()) and not l.strip().startswith('$$')) and False else ''))
        i+=1
    return '\n'.join(out)
items=[]
for b in bl:
    iid=b.split('\n',1)[0].strip()
    d,s,df,fm=idx[iid]; s=normskill(d,s); df='Hard' if df.startswith('Hard') else 'Medium' if df.startswith('Medium') else df
    tm=re.search(r'\*\*Tool:\*\*\s*(.*)',b); tool=tm.group(1).strip() if tm else ''
    q=re.search(r'\*\*Question:\*\*(.*?)\*\*Correct Answer',b,re.S).group(1)
    q=re.split(r'\n\*\*Source:\*\*',q)[0]
    q=q.replace('\r','')
    # options
    ol=list(re.finditer(r'^[ \t]*\(?([A-D])\)[ \t]+',q,re.M))
    opts=[]
    if len(ol)==4:
        stem=q[:ol[0].start()]
        for k,m in enumerate(ol):
            e=ol[k+1].start() if k<3 else len(q)
            opts.append(q[m.end():e].strip())
    else: stem=q
    items.append(dict(id=iid,d=d,s=s,df=df,tool=tool,stem=stem.strip(),opts=opts))
def optblock(o):
    texts=[inline(x).replace('\n','\\\\ ') for x in o]
    short=max(len(x) for x in o)<34 and not any('\n' in x for x in o)
    L='ABCD'
    if short:
        return '\\begin{tabular}{@{}p{0.46\\linewidth}p{0.46\\linewidth}@{}}'+f'\\textbf{{A)}}\\ {texts[0]}&\\textbf{{B)}}\\ {texts[1]}\\\\[1pt]\\textbf{{C)}}\\ {texts[2]}&\\textbf{{D)}}\\ {texts[3]}'+'\\end{tabular}'
    return '\\begin{itemize}[leftmargin=0pt,label={},itemsep=0pt,topsep=1pt,parsep=0pt]'+''.join(f'\\item[] \\textbf{{{L[k]})}}\\ {texts[k]}' for k in range(4))+'\\end{itemize}'
cols='\\begin{multicols}{2}' if TWO else ''
cole='\\end{multicols}' if TWO else ''
P=[r"""\documentclass[10pt]{article}
\usepackage[a4paper,margin=1.6cm,top=1.5cm,bottom=1.6cm]{geometry}
\usepackage[utf8]{inputenc}\usepackage[T1]{fontenc}\usepackage{amsmath,amssymb,xcolor,helvet,fancyhdr,enumitem,needspace,multicol,tikz,hyperref,tcolorbox}
\usetikzlibrary{arrows.meta,calc,patterns}
\renewcommand{\familydefault}{\sfdefault}
\definecolor{navy}{HTML}{1F3864}\definecolor{teal}{HTML}{17A199}\definecolor{tag}{HTML}{6B3FA0}
\definecolor{NAVY}{HTML}{1F3A5F}\definecolor{INK}{HTML}{1A1A1A}\definecolor{TEAL}{HTML}{1A7F8E}\definecolor{BLUE}{HTML}{2F6DB5}\definecolor{ORANGE}{HTML}{E07B39}\definecolor{GREY}{HTML}{6B7280}\definecolor{GOLD}{HTML}{C9A227}\definecolor{LINE}{HTML}{C7CDD6}\definecolor{MAROON}{HTML}{8B1E3F}
\hypersetup{hidelinks}
\pagestyle{fancy}\fancyhf{}\renewcommand{\headrulewidth}{0pt}
\fancyfoot[L]{\scriptsize SAT Math Question Booklet}\fancyfoot[R]{\scriptsize Mr Malek Thiab $\cdot$ Page \thepage}
\setlength{\parindent}{0pt}\setlength{\parskip}{1mm}\setlength{\columnsep}{0.8cm}\setlength{\columnseprule}{0.2pt}
\newcommand{\figbox}[1]{\par\begin{tcolorbox}[colback=black!4,colframe=black!25,boxrule=0.4pt,left=3pt,right=3pt,top=2pt,bottom=2pt]\footnotesize\textit{Figure (described):} #1\end{tcolorbox}\par}
\newcommand{\spr}{\par\vspace{1mm}\fbox{\parbox{3.2cm}{\vspace{4mm}\footnotesize Answer:\vspace{4mm}}}\par}
\newcommand{\qh}[3]{\needspace{9\baselineskip}\textbf{\color{navy}#1.}\ {\scriptsize\color{tag}\textbf{#2} $\cdot$ #3}\par\nopagebreak}
\setcounter{tocdepth}{2}
\setcounter{secnumdepth}{0}
\newcommand{\dsec}[1]{\clearpage\addcontentsline{toc}{section}{#1}\noindent\colorbox{navy}{\parbox{\dimexpr\linewidth-2\fboxsep}{\color{white}\bfseries\Large\ #1}}\par\vspace{2mm}}
\newcommand{\ssec}[1]{\needspace{12\baselineskip}\addcontentsline{toc}{subsection}{#1}\vspace{3mm}\noindent{\color{navy}\bfseries\large #1}\ {\color{navy}\hrulefill}\par\vspace{1.5mm}}
\begin{document}
\thispagestyle{empty}
\vspace*{3cm}
{\color{navy}\fontsize{30}{34}\selectfont\bfseries SAT Math\par Question Booklet}\par\vspace{4mm}
{\color{teal}\Large\bfseries 1,146 questions classified by topic}\par\vspace{8mm}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{@{}lr@{}}
"""]
cnt=collections.Counter(i['d'] for i in items)
for d in ORDER: P.append(f'\\textbf{{{d}}} & {cnt[d]}\\\\\n')
P.append(r"""\end{tabular}
\vspace{10mm}

{\large Every question appears within its domain and skill, Medium before Hard. Each question carries its bank ID, its difficulty and, where recorded, its tool (No calculator needed, Calculator or Desmos). Multiple-choice questions have one correct answer; for student-produced responses (SPR) write the value in the answer box.}

\vspace{6mm}
{\large This booklet contains questions only: no answers, solutions or explanations.}

\vfill
{\large Mr Malek Thiab}
\newpage
\tableofcontents
\newpage
""")
n=0
for d in ORDER:
    P.append(f'\\dsec{{{d} ({cnt[d]})}}\n')
    for s in ORDER[d]:
        its=[i for i in items if i['d']==d and i['s']==s]
        its.sort(key=lambda i:(i['df']!='Medium',int(i['id'].split('-')[1]),i['id']))
        assert its,(d,s)
        P.append(f'\\ssec{{{s} ({len(its)})}}\n'+cols)
        for i in its:
            n+=1
            tag=f"{i['df']}"+(' $\\cdot$ SPR' if not i['opts'] else '')+(f" $\\cdot$ {i['tool']}" if i['tool'] else '')
            P.append(f"\\qh{{{n}}}{{{i['id']}}}{{{tag}}}\n"+body(i['stem'])+'\n')
            if i['opts']: P.append(optblock(i['opts'])+'\n')
            else: P.append('\\spr\n')
            P.append('\\vspace{2mm}\n')
        P.append(cole)
assert n==1146,n
P.append('\\end{document}')
open('book%s.tex'%('2' if TWO else '1'),'w').write('\n'.join(P))
print(n, sum(1 for i in items if not i['opts']))
