import re,json,html,collections,os,sys,signal
sys.path.insert(0,'/home/claude/v2')
import desmos_steps as DZ
import twins as TWN
SITE='/home/claude/v2/site'; OLD='/home/claude/acesat_site'
def jx(t,id_):
    m=re.search(r'<script[^>]*id="%s"[^>]*>(.*?)</script>'%id_,t,re.S); return json.loads(m.group(1))
def esc(s): return html.escape(str(s),quote=False)
def code_ok(s):
    s=esc(s); return s.replace('&lt;code&gt;','<code>').replace('&lt;/code&gt;','</code>')
def nz(s): return re.sub(r'\s+',' ',s).strip()

# ---------- SAT ----------
import sat_traps
STR=sat_traps.TR
def sat():
    t=open(f'{SITE}/sat/mock/index.html',encoding='utf8').read(); B=jx(t,'bankdata'); items=[];groups=collections.OrderedDict()
    for x in B:
        steps=x['steps']; trap=[s for s in steps if s.lower().startswith('trap')]; body=[s for s in steps if not s.lower().startswith('trap')]
        ktxt=re.sub(r'^traps?:\s*','',trap[0],flags=re.I) if trap else ''
        if not trap:  # trap note written inside a step ("... Trap: ...")
            for j,st in enumerate(steps):
                mm=re.search(r'\s*\bTraps?:\s*(.+)$',st,re.S)
                if mm:
                    ktxt=mm.group(1).strip(); head=st[:mm.start()].strip()
                    body=steps[:j]+([head] if head else [])+steps[j+1:]; break
        it={'id':x['id'],'u':x['sub'],'l':{'E':1,'M':2,'H':3}[x['lv']],'q':'<div class="stem">%s</div>'%esc(x['q']),'s':[code_ok(s) for s in body] or [code_ok(s) for s in steps],'k':code_ok(ktxt) if ktxt else ''}
        if x['mc']:
            it['o']=[esc(o) for o in x['opts']]; it['a']=x['key']
            clauses=[c.strip() for c in re.split(r',\s*(?:and\s+|or\s+)?|;\s+|\.\s+|\s+and\s+',ktxt) if c.strip()]
            c=[]
            for i,o in enumerate(x['opts']):
                if i==x['key']: c.append(None); continue
                hit=next((cl for cl in clauses if o in cl),None)
                c.append(code_ok(hit[0].upper()+hit[1:]+('.' if not hit.endswith('.') else '')) if hit else None)
            for oi,note in (STR.get(x['id']) or {}).items():
                if oi!=x['key'] and oi<len(c) and not c[oi]: c[oi]=note
            it['c']=c
            if sum(1 for v in c if v)==3 and False: pass
        else:
            it['n']=x['key']; it['d']='$%s$'%x['disp']
        h=body[1:2] and body[0]
        it['h']=code_ok('Start here: '+body[0]) if len(body)>1 else ''
        if 3<=len(body)<=6: it['ord']=[code_ok(s) for s in body]
        signal.signal(signal.SIGALRM,_to); signal.alarm(4)
        try:
            it['dz']=DZ.build(x)[0]
        except BaseException:
            it['dz']=None
        finally:
            signal.alarm(0)
        items.append(it); groups.setdefault((x['domain'],x['skill']),[]).append(x['id'])
    # most common question types: per skill, the largest sub-topics that together make up 60% of the skill
    by=collections.defaultdict(collections.Counter)
    for x in B: by[x['skill']][x['sub']]+=1
    common=set()
    for sk,c in by.items():
        tot=sum(c.values()); acc=0
        for s_,n in c.most_common():
            if acc/tot>=0.6: break
            common.add((sk,s_)); acc+=n
    raw={x['id']:x for x in B}
    ids={it['id'] for it in items}
    for it in items:
        if it['id']+'-2' in ids: it['tw']=it['id']+'-2'; it['wk']=1
        elif it['id'].endswith('-2') and it['id'][:-2] in ids: it['tw']=it['id'][:-2]
    for it in items:
        r_=raw[it['id']]
        if (r_['skill'],r_['sub']) in common: it['cm']=1
    G=[{'id':re.sub(r'\W+','-',sk.lower()).strip('-'),'label':sk,'cat':dm,'ids':ids,'blurb':blurb(dm,sk,len(ids))} for (dm,sk),ids in groups.items()]
    G.append({'id':'mixed','label':'Mixed review','cat':'All skills','ids':'*','blurb':'Every skill, matched by sub-topic. A good test of whether you can tell which idea a question is asking for.'})
    return items,G
class _TO(Exception): pass
def _to(*a): raise _TO()
def blurb(dm,sk,n): return 'Worked examples with step-by-step solutions, then your turn.'

# ---------- SAAT ----------
def sentences(w):
    parts=re.split(r'(?<=[.!?])\s+(?=[A-Z(\d∠√−-])',w.strip())
    return [p for p in parts if p]
def letter_traps(p,nopts,key):
    c=[None]*nopts
    for s in p or []:
        m=re.match(r'^([A-D]):\s*(.*)$',s,re.S)
        if m:
            i='ABCD'.index(m.group(1))
            if i<nopts: c[i]=esc(m.group(2))
    return c
def hintfrom(t):
    t=t or ''
    m=re.split(r'\s+—\s+|\s+-\s+',t,1)
    return esc(m[0][0].upper()+m[0][1:]) if m[0] else ''
def saat():
    t=open(f'{SITE}/saat/mock/index.html',encoding='utf8').read(); B=jx(t,'bank'); F=jx(t,'figs'); items=[];groups=collections.OrderedDict()
    B=add_twins(B,TWN.SAAT,dict(f=None))
    for x in B:
        fig=''
        if x.get('f') and x['f'] in F: fig='<div class="plate fig"><img alt="Figure for the question" src="%s"></div>'%F[x['f']]
        it={'id':x['id'],'u':x.get('u') or x['s'],'l':x['l'],'q':'<div class="stem">%s</div>'%esc(x['q']),'f':fig,'o':[esc(o) for o in x['o']],'a':x['a'],'t':esc(x['t']),'s':[esc(s) for s in sentences(x['w'])] or [esc(x['w'])],'c':letter_traps(x['p'],len(x['o']),x['a']),'h':hintfrom(x['t'])}
        it['k']=''
        items.append(it); groups.setdefault(x['s'],[]).append(x['id'])
    link_twins(items)
    G=[{'id':re.sub(r'\W+','-',k.lower()).strip('-'),'label':k,'cat':'Tahsili strands','ids':ids,'blurb':'Every wrong option is a named trap, explained as you go.'} for k,ids in groups.items()]
    G.append({'id':'mixed','label':'Mixed strands','cat':'All strands','ids':'*','blurb':'All strands together, like the paper. Spot which idea each question is testing.'})
    return items,G

# ---------- GAT ----------
def gat():
    t=open(f'{SITE}/gat/mock/index.html',encoding='utf8').read(); B=jx(t,'bank'); IM=jx(t,'imgs'); items=[];groups=collections.OrderedDict()
    B=add_twins(B,TWN.GAT,dict(e=None,f=None,fw=None))
    def eq(k,s=1.2):
        m=IM['e:'+k]; return '<img alt="" src="data:image/webp;base64,%s" width="%d" height="%d">'%(m['d'],round(m['w']*96/260*s),round(m['h']*96/260*s))
    def fg(k):
        m=IM['f:'+k]; w=min(520,round((m.get('k') or 3)*130)); return '<img alt="Figure for the question" src="data:image/webp;base64,%s" width="%d" height="%d">'%(m['d'],w,round(w*m['h']/m['w']))
    for x in B:
        q=x['q']; m=re.match(r'^([\s\S]*?)\s{3}A: ([\s\S]*?)\s{3}B: ([\s\S]*)$',q)
        qh='<div class="stem">%s</div><div class="qab"><div><small>QUANTITY A</small><span>%s</span></div><div><small>QUANTITY B</small><span>%s</span></div></div>'%(esc(m[1]),esc(m[2]),esc(m[3])) if m else '<div class="stem">%s</div>'%esc(q)
        plate=''
        pl=[]
        if x.get('e'): pl.append(eq(x['e']))
        if x.get('f'): pl.append(fg(x['f']))
        if pl: plate='<div class="plate%s">%s</div>'%(' fig' if x.get('f') else '',''.join(pl))
        opts=[esc(o) if isinstance(o,str) else '<span class="oe">%s</span>'%eq(o['e'],1.05) for o in x['o']]
        code=re.match(r'GAT-Q-([A-Z]+\.\d+)',x['id']); code=code.group(1) if code else x['c']
        it={'id':x['id'],'u':code,'l':x['l'],'q':qh+plate,'o':opts,'a':x['a'],'t':esc(x['t']),'s':[esc(s) for s in sentences(x['w'])] or [esc(x['w'])],'c':letter_traps(x['p'],len(x['o']),x['a']),'h':hintfrom(x['t']),'k':''}
        items.append(it); groups.setdefault(x['c'],[]).append(x['id'])
    link_twins(items)
    names={'ARI':'Arithmetic','ALG':'Algebra','GEO':'Geometry','DAT':'Data & Statistics','LOG':'Word Logic'}
    G=[{'id':k.lower(),'label':names[k],'cat':'ETEC strands','ids':groups[k],'blurb':'Every wrong option is a named student error, explained as you go.'} for k in ['ARI','ALG','GEO','DAT','LOG']]
    G.append({'id':'mixed','label':'Mixed strands','cat':'All strands','ids':'*','blurb':'All five strands together. Learn to recognise the trick before you start computing.'})
    return items,G

# ---------- AP ----------
def ap():
    t=open(f'{SITE}/ap/mock/index.html',encoding='utf8').read()
    D=jx(t,'data'); les={l['no']:l for l in D['lessons']}; items=[];by=collections.OrderedDict()
    for x in add_twins(D['mcq'],TWN.AP,dict(fig=None,trapnote='',lvl=None)):
        fig=''
        if x.get('fig') and x['fig'] in D['figs']:
            m=D['figs'][x['fig']]; w=min(520,m['w']); fig='<div class="plate fig"><img alt="Figure for the question" src="data:image/webp;base64,%s" width="%d" height="%d"></div>'%(m['d'],w,round(w*m['h']/m['w']))
        c=[None]*len(x['o'])
        for k,v in (x.get('traps') or {}).items():
            i='ABCD'.index(k)
            if i<len(c): c[i]=esc(v)
        l=les.get(x['t']); rec=l['recap'] if l else ''
        lv={'Hard':3,'Medium':2}.get(x.get('lvl'),2)
        it={'id':x['id'],'u':x['t'],'l':lv,'q':'<div class="stem">%s</div>'%esc(x['q']),'f':fig,'o':[esc(o) for o in x['o']],'a':x['a'],'s':([esc(z) for z in x['steps']] if x.get('steps') else [esc(x['sol'])]),'c':c,'h':esc('Lesson %s idea: %s'%(x['t'],rec)) if rec else '','k':esc(x.get('trapnote') or ''),'t':''}
        items.append(it); by.setdefault(x['t'],[]).append(x['id'])
    link_twins(items)
    G=[]
    for no,ids in by.items():
        if len(ids)>=6: G.append({'id':'l'+no.replace('.','-'),'label':'Lesson %s · %s'%(no,D['titles'].get(no,'')),'cat':'Unit %s'%no.split('.')[0],'ids':ids,'blurb':'Worked examples from this lesson, each wrong option a named trap.'})
    G.append({'id':'mixed','label':'Mixed review','cat':'All lessons','ids':'*','blurb':'Questions across Units 1 to 3. Practise choosing the right tool for each question.'})
    return items,G

def add_twins(B,TW,extra):
    out=list(B); byid={x['id']:x for x in B}
    for oid,tw in TW.items():
        if oid not in byid: print('MISSING twin source',oid); continue
        x2=dict(byid[oid]); x2.update({k:v for k,v in tw.items() if k!='chk'}); x2.update(extra); x2['id']=oid+'~t'
        out.append(x2)
    return out
def link_twins(items):
    ids={it['id'] for it in items}
    for it in items:
        if it['id']+'~t' in ids: it['tw']=it['id']+'~t'; it['wk']=1
        elif it['id'].endswith('~t'): it['tw']=it['id'][:-2]
THEMES={
'sat':dict(name='SAT Aceit',sub='Digital SAT · Math',logo='S',key='sat',math=True,eyebrow='Digital SAT · Math',title='Learn the move, <em>then</em> make it yours.',lede='Pick a skill. You will watch a worked example, try a new question with hints, then solve a block on your own. Every wrong option names the mistake behind it.',
 css=':root{--bg:#f4f6fb;--card:#fff;--ink:#1e2a3a;--muted:#5d6b7e;--line:#d5dbe4;--accent:#2f4bd6;--accent-ink:#fff;--navy:#1f3a5f;--gold:#d9a21b;--goldink:#7a5600;--good:#17803d;--bad:#b42318;--sans:Roboto,system-ui,sans-serif;--serif:"Noto Serif",Georgia,serif;--mono:"IBM Plex Mono",ui-monospace,monospace;--logobg:#1f3a5f;--logoink:#fff;--rad:14px;--qfont:"Noto Serif",Georgia,serif}',
 fonts='https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&family=Noto+Serif:wght@400;500;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap',
 head='<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css"><script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.js"></script><script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/contrib/auto-render.min.js"></script>',norm=sat),
'saat':dict(name='SAAT Lab',sub='Tahsili · Math',logo='Σ',key='saat',math=False,eyebrow='Tahsili · Math · no calculator',title='See the idea. <em>Then</em> prove it alone.',lede='Choose a strand. A worked example shows the idea behind the trap, a hinted turn lets you try it, and an independent block checks you can do it with nothing but pencil and reasoning.',
 css=':root{--bg:#0b1311;--card:#121c19;--ink:#e6f1ee;--muted:#93aaa3;--line:#24332f;--accent:#2fd1a0;--accent-ink:#04251b;--navy:#8fd9c3;--gold:#f2a93b;--goldink:#f6c46a;--good:#34d399;--bad:#f87171;--sans:Inter,system-ui,sans-serif;--serif:Newsreader,Georgia,serif;--mono:"IBM Plex Mono",ui-monospace,monospace;--logobg:linear-gradient(135deg,#2fd1a0,#f2a93b);--logoink:#06231a;--rad:16px;--qfont:Newsreader,Georgia,serif;--bgimg:radial-gradient(800px 500px at 10% -5%,rgba(47,209,160,.14),transparent 60%)}body{background-repeat:no-repeat;background-attachment:fixed}.plate.fig img{background:#fff}',
 fonts='https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Newsreader:ital,wght@0,400;0,500;1,400&family=IBM+Plex+Mono:wght@400;500;600&display=swap',head='',norm=saat),
'gat':dict(name='GAT Atelier',sub='Qudurat · Quantitative',logo='ق',key='gat',math=False,eyebrow='Qudurat · Quantitative · no calculator',title='Quantitative reasoning, <em>learned</em> step by step.',lede='Choose a strand. Watch the trick worked through, try the same idea with hints, then solve a block alone. Wrong options are named student errors, explained as you go.',
 css=':root{--bg:#f4ecdc;--card:#fffaf0;--ink:#172447;--muted:#5b6482;--line:#dccfae;--accent:#a8741a;--accent-ink:#fff;--navy:#172447;--gold:#b98a2e;--goldink:#6b4a0a;--good:#2f7d4a;--bad:#b3402a;--sans:Inter,system-ui,sans-serif;--serif:Newsreader,Georgia,serif;--mono:"IBM Plex Mono",ui-monospace,monospace;--logobg:#172447;--logoink:#f4d58a;--rad:6px;--sh:3px 3px 0 rgba(23,36,71,.85);--qfont:Newsreader,Georgia,serif}.btn{box-shadow:2px 2px 0 var(--navy)!important;border-radius:6px!important}.pill,.ghost{border-radius:6px}',
 fonts='https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Newsreader:ital,wght@0,400;0,500;1,400&family=IBM+Plex+Mono:wght@400;500;600&display=swap',head='',norm=gat),
'ap':dict(name='AP Precalc Studio',sub='College Board · Precalculus',logo='f',key='ap',math=True,eyebrow='College Board · AP Precalculus',title='Watch it worked. <em>Try</em> it. Then own it.',lede='Choose a lesson. Each session walks from a worked example to a hinted turn to an independent block, with the trap behind every wrong option named.',
 css=':root{--bg:#edf1fa;--card:#fff;--ink:#0f1b3d;--muted:#5a6685;--line:#d3dbef;--accent:#2a54d4;--accent-ink:#fff;--navy:#0f1b3d;--gold:#e0a100;--goldink:#7a5800;--good:#1b7f45;--bad:#c8102e;--sans:Inter,system-ui,sans-serif;--serif:"Source Serif 4",Georgia,serif;--mono:"IBM Plex Mono",ui-monospace,monospace;--logobg:#0f1b3d;--logoink:#fff;--rad:14px;--qfont:"Source Serif 4",Georgia,serif;--bgimg:linear-gradient(rgba(42,84,212,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(42,84,212,.06) 1px,transparent 1px)}body{background-size:28px 28px}',
 fonts='https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Source+Serif+4:ital,wght@0,400;0,600;1,400&family=IBM+Plex+Mono:wght@400;500;600&display=swap',head='<link rel="stylesheet" href="../vendor/katex.min.css"><script src="../vendor/katex.min.js"></script><script src="../vendor/auto-render.min.js"></script>',norm=ap),
}
def safe(j): return json.dumps(j,ensure_ascii=False,separators=(',',':')).replace('</','<\\/').replace('\u2028','\\u2028').replace('\u2029','\\u2029')
CSS=open('/home/claude/v2/guided.css').read(); JS=open('/home/claude/v2/guided.js').read()
def build_guided(k):
    T=THEMES[k]; items,groups=T['norm']()
    cfg={'filters':(k=='sat'),'desmos':({'key':os.environ.get('DESMOS_API_KEY','REPLACE_DESMOS_KEY')} if k=='sat' else None),'key':T['key'],'name':T['name'],'sub':T['sub'],'logo':T['logo'],'math':T['math'],'eyebrow':T['eyebrow'],'title':T['title'],'lede':T['lede'],'groups':groups}
    page='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>%s · Guided practice · Sawab</title><link rel="stylesheet" href="%s">%s<style>%s\n%s</style></head><body><div id="app"></div><script id="cfg" type="application/json">%s</script><script id="items" type="application/json">%s</script><script>%s</script></body></html>'%(T['name'],T['fonts'],T['head'],T['css'],CSS,safe(cfg),safe(items),JS)
    os.makedirs(f'{SITE}/{k}/guided',exist_ok=True); open(f'{SITE}/{k}/guided/index.html','w',encoding='utf8').write(page)
    print(k,len(items),'items',len(groups),'groups',len(page)//1024,'KB')
    return len(items),len(groups)

HUB='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>%(name)s · Sawab</title><link rel="stylesheet" href="%(fonts)s"><style>%(css)s
*{box-sizing:border-box}body{margin:0;background:var(--bg);background-image:var(--bgimg,none);color:var(--ink);font-family:var(--sans);min-height:100vh}
.wrap{max-width:900px;margin:0 auto;padding:22px 20px 50px}.top{display:flex;justify-content:space-between;align-items:center;gap:12px;padding-bottom:16px;border-bottom:1px solid var(--line)}
.brand{display:flex;gap:12px;align-items:center}.logo{width:40px;height:40px;border-radius:var(--rad,12px);display:grid;place-items:center;background:var(--logobg);color:var(--logoink);font:700 1.1rem var(--serif)}
.brand b{display:block;font:600 1.05rem var(--serif)}.brand small{color:var(--muted);letter-spacing:.1em;text-transform:uppercase;font-size:.66rem}
.pill{border:1px solid var(--line);border-radius:999px;padding:6px 14px;font-size:.82rem;text-decoration:none;color:var(--ink);background:var(--card)}
.eyebrow{font:600 .72rem var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--accent);margin:30px 0 8px}
h1{font:500 clamp(2rem,5vw,3.1rem)/1.08 var(--serif);margin:0 0 10px;letter-spacing:-.015em}h1 em{font-style:italic;color:var(--accent)}
.lede{color:var(--muted);max-width:620px;margin:0 0 26px}
.two{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px}
.opt{display:flex;flex-direction:column;gap:10px;text-decoration:none;color:var(--ink);background:var(--card);border:1.5px solid var(--line);border-radius:var(--rad,18px);padding:24px 24px 22px;box-shadow:var(--sh,none);transition:.15s}
.opt:hover{border-color:var(--accent);transform:translateY(-3px)}
.opt .no{font:600 .7rem var(--mono);letter-spacing:.14em;color:var(--accent);text-transform:uppercase}.opt h2{margin:0;font:600 1.6rem var(--serif)}.opt p{margin:0;color:var(--muted);flex:1}
.opt ul{margin:0;padding-left:18px;color:var(--muted);font-size:.9rem}.opt .go{font-weight:700;color:var(--accent)}
.opt.g{border-color:var(--accent)}
footer{text-align:center;color:var(--muted);font-size:.78rem;margin-top:40px}
</style></head><body><div class="wrap"><header class="top"><div class="brand"><span class="logo">%(logo)s</span><span><b>%(name)s</b><small>%(sub)s</small></span></div><a class="pill" href="../">⟵ All exams</a></header>
<div class="eyebrow">Choose how to practise</div><h1>%(h1)s</h1><p class="lede">%(lede)s</p>
<div class="two"><a class="opt" href="mock/"><span class="no">01 · Test yourself</span><h2>Mock exam</h2><p>%(mock_p)s</p><ul>%(mock_li)s</ul><span class="go">Open mock exam →</span></a>
<a class="opt g" href="guided/"><span class="no">02 · Learn by doing</span><h2>Guided practice</h2><p>Worked example, then a hinted turn, then a block on your own. Every wrong option explains the mistake behind it.</p><ul><li>%(ng)s topics plus a mixed set</li><li>Mixed question types: choice, true or false, type it, order the steps, match the mistake</li><li>Hints on in the guided block, off in the independent block</li></ul><span class="go">Open guided practice →</span></a></div>
<footer>Sawab · Original practice questions</footer></div></body></html>'''
HUBS={'sat':dict(h1='SAT Aceit',lede='Two ways in. Take a full adaptive mock under test conditions, or learn skill by skill with guidance.',mock_p='Two timed modules in the Bluebook style, with the Desmos calculator, reference sheet and a score band at the end.',mock_li='<li>Adaptive: Module 2 follows your Module 1 score</li><li>Built-in Desmos graphing calculator</li><li>Every skill appears, weighted like the real test</li>'),
'saat':dict(h1='SAAT Lab',lede='Two ways in. Sit a weighted Tahsili mock with a scratch pad, or learn strand by strand with guidance.',mock_p='Timed, weighted mocks, strand drills and a Daily 10. No calculator, like the real paper.',mock_li='<li>Weighted: Algebra, Geometry, Calculus, Trig, Stats</li><li>Scratch pad, no calculator</li><li>Report and trap diary</li>'),
'gat':dict(h1='GAT Atelier',lede='Two ways in. Sit a blueprint paper, or build each strand step by step with guidance.',mock_p='A 40-question ETEC blueprint mock, sprints, the comparison clinic and a Daily 10. No calculator.',mock_li='<li>14·7·7·7·5 blueprint</li><li>Comparison clinic for quantity questions</li><li>Report at the end</li>'),
'ap':dict(h1='AP Precalc Studio',lede='Two ways in. Use the studio for lessons, exam-style sets and FRQs, or follow a guided session lesson by lesson.',mock_p='Lessons, topic practice, a hard MCQ set, a timed mixed mock, the FRQ workshop and the exam guide.',mock_li='<li>All 44 topics of Units 1, 2 and 3, from the book</li><li>Timed mixed mock with trap diary</li><li>24 FRQ tasks with 6-point self-scoring</li>')}
def build_hub(k,n,ng):
    T=THEMES[k]; h=HUBS[k]
    page=HUB%dict(name=T['name'],fonts=T['fonts'],css=T['css'],logo=T['logo'],sub=T['sub'],n=n,ng=ng,**h)
    open(f'{SITE}/{k}/index.html','w',encoding='utf8').write(page)
if __name__=='__main__':
    for k in ['sat','saat','gat','ap']:
        n,ng=build_guided(k); build_hub(k,f'{n:,}',ng-1)
