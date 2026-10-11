import json,re,sys,subprocess
from fractions import Fraction as Fr
sys.path.insert(0,'/home/claude/sat_s1')
from lib import *
from steps import S,N
ESC={'\\':r'\textbackslash{}','{':r'\{','}':r'\}','^':r'\textasciicircum{}','_':r'\_','~':r'\textasciitilde{}','#':r'\#','%':r'\%','&':r'\&','$':r'\$'}
def code(m):
    c=m.group(1).replace('\\{','{').replace('\\}','}')
    return r"\dzc{"+"".join(ESC.get(ch,ch) for ch in c)+"}"
def conv(s): return re.sub(r"\[\[(.+?)\]\]",code,s)
items=json.load(open('/home/claude/cb/s1_items.json'))
CLEAN=[("$2{,}400$ SAR","$2{,}400$ dollars"),(" in Riyadh",""),(" for a NEOM greenhouse"," for a greenhouse"),(" in Al-Ula",""),("A cooperative in Al-Ahsa tracks its annual date export tonnage","A cooperative tracks its annual export tonnage"),("a Jeddah desalination reservoir","a water reservoir"),("in thousands of SAR, from selling a product priced at $x$ SAR","in thousands of dollars, from selling a product priced at $x$ dollars"),("revenue, in SAR,","revenue, in dollars,"),("is $2{,}400$ SAR","is $2{,}400$ dollars"),("°C","$^\\circ$C")]
def tab(md):
    rows=[r.strip().strip('|').split('|') for r in md.strip().split('\n') if r.strip().startswith('|') and not re.match(r'^\|\s*-',r.strip())]
    n=len(rows[0]);t=r"\begin{center}\renewcommand{\arraystretch}{2.1}\begin{tabular}{|"+"c|"*n+"}\hline "
    for r in rows: t+=" & ".join(c.strip() for c in r)+r" \\ \hline "
    return t+r"\end{tabular}\end{center}"
def parse(o):
    q=o['q']
    for a,b in CLEAN: q=q.replace(a,b)
    lines=q.split('\n');stem=[];opts=[]
    for ln in lines:
        m=re.match(r'^\(?([A-D])\)\s*(.*)$',ln.strip())
        if m and (opts or m.group(1)=='A'): opts.append(m.group(2).strip())
        elif opts and ln.strip()=='' : continue
        elif opts: opts[-1]+=' '+ln.strip()
        else: stem.append(ln)
    stem='\n'.join(stem).strip()
    # tables
    tl=[l for l in stem.split('\n') if l.strip().startswith('|')]
    if tl:
        tb=tab('\n'.join(tl)); first=stem.split('\n').index(tl[0])
        pre='\n'.join(stem.split('\n')[:first]).strip();post='\n'.join(l for l in stem.split('\n')[first+len(tl):]).strip()
        stem=(pre+'\n\n' if pre else '')+tb+('\n\n'+post if post else '')
    stem=re.sub(r'\n\s*\n','\n\n',stem)
    stem=re.sub(r'^\s*I\.\s*(.*?)\s+II\.\s*(.*?)\s+III\.\s*(.*)$',r'\\begin{enumerate}[label=\\Roman*.,leftmargin=2em,itemsep=0pt,topsep=2pt]\\item \1\\item \2\\item \3\\end{enumerate}',stem) if False else stem
    return stem,(opts if len(opts)==4 else None)
def num(s):
    s=s.replace('{','').replace('}','').replace('\\dfrac','').replace('$','').replace(',','')
    return s
P=[]
order=[o for o in items if o['part']=='In class']+[o for o in items if o['part']!='In class']
for o in order:
    stem,opts=parse(o)
    # roman statements on one block
    if re.search(r'(^|\s)I\.\s',stem) and re.search(r'\sII\.\s',stem):
        stem=re.sub(r'\s+(I{1,3}\.)\s',r'\n\n\1 ',stem)
    p=dict(lv='M' if o['d']=='Medium' else 'H',tool='N' if o['id'] in N else 'D',q=stem,id=o['id'])
    if opts:
        L_=o['ans'].strip()[0]
        if L_ not in 'ABCD': L_='ABCD'[0]
        p['opts']=opts;p['correct']="ABCD".index(L_);p['norot']=False
        p['chk']=lambda c=p['correct']:('idx',c)
    else:
        a=o['ans'].replace('$','').strip()
        m=re.match(r'^\\dfrac\{(\d+)\}\{(\d+)\}$',a.replace('{-','-{') ) 
        a2=re.sub(r'\\dfrac\{(-?\d+)\}\{(\d+)\}',r'\1/\2',a).replace('{','').replace('}','')
        val=float(Fr(a2)) if '/' in a2 else float(a2)
        p['val']=val;p['ans']=o['ans'].strip().strip('$') if '$' in o['ans'] else a
        p['chk']=lambda v=val:v
    p['steps']=[conv(x) for x in S[o['id']]];p['lines']=5 if p['lv']=='M' else 6
    P.append(p)
P=prep(P)
for p in P: p['ans']=p.get('ans')
json.dump([[p['id'],p['correct'] if p.get('opts') else p['val']] for p in P],open('keyed.json','w'))
meta=dict(week='',session='',title='Quadratics and Nonlinear Functions',code='SAT-M \\textperiodcentered\\ Session 1',headfull='Session 1 \\textemdash\\ Quadratics and Nonlinear Functions',boxhead='Session 1',time='3 hours: Part A in class (140 min solving) + 40 min self-check and error log. Part B is the self-assessment, done independently.',topics='parabolas: vertex, zeros and intercepts \\textperiodcentered\\ function notation and composition \\textperiodcentered\\ transformations \\textperiodcentered\\ exponential and power functions \\textperiodcentered\\ direct, inverse and joint variation \\textperiodcentered\\ equivalent forms \\textperiodcentered\\ undefined values')
def build_s1(mode,out):
    key=(mode=='key')
    L=[PRE.replace("@@CODE@@",meta['code']).replace("@@HEAD@@",meta['headfull']).replace("\\begin{document}",EXTRA+r"\setmonofont[Scale=0.9]{DejaVu Sans Mono}\newcommand{\dzc}[1]{\colorbox{black!8}{\texttt{\small\textcolor{black}{#1}}}}"+"\n\\begin{document}")]
    L.append(r"""
\begin{tcolorbox}[enhanced,colback=NAVY!4,colframe=NAVY,boxrule=0.8pt,arc=3pt]
{\Large\bfseries\color{NAVY} SAT Math Mastery \textperiodcentered\ Session 1}\\[2pt]
{\large\bfseries %s}\\[3pt]
\begin{tabular}{@{}p{0.2\linewidth}p{0.75\linewidth}@{}}
\textbf{Time} & %s\\
\textbf{Topics} & %s\\
\textbf{Name / Date} & \rule{5.5cm}{0.3pt}\ \ \rule{3cm}{0.3pt}\\
\end{tabular}
\end{tcolorbox}
"""%(meta['title'],meta['time'],meta['topics']))
    L.append(r"\banner{Part A \textperiodcentered\ In class \textemdash\ 35 problems}")
    L.append(r"\small Each problem states its tool. Write your work in the space below. Multiple choice: one correct option. Student-produced response (SPR): enter an exact value (fraction or decimal)."+(r" Grey boxes show exactly what to type in Desmos, one expression per line; tap a grey dot to read an intersection, intercept or vertex. A letter such as $a$, $c$ or $k$ becomes a slider when you accept Desmos's offer to add one." if key else "")+r"\normalsize\par\vspace{4pt}")
    for i,p in enumerate(P,1):
        if i==36: L.append(r"\newpage\banner{Part B \textperiodcentered\ Self-assessment \textemdash\ 23 problems}")
        L.append(problem_tex(i,p,mode))
    L.append(r"\end{document}")
    open(out,'w').write("\n".join(L))
for mode,out in (('ws','S1_ws.tex'),('key','S1_key.tex')):
    build_s1(mode,out)
    for _ in range(2): r=subprocess.run(['xelatex','-interaction=nonstopmode',out],capture_output=True,text=True)
    log=open(out[:-4]+'.log').read();print(out,'overfull',log.count('Overfull'),'err',len(re.findall(r'^!',log,re.M)))
