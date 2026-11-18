import re,json,sys
sys.path.insert(0,'/home/claude/v2/apx')
import common,u1,u2,u3,lessons,figs
P='/home/claude/v2/site/ap/mock/index.html'
h=open(P,encoding='utf8').read()
m=re.search(r'(<script id="data"[^>]*>)(.*?)(</script>)',h,re.S)
D=json.loads(m.group(2))
key=lambda no:tuple(int(x) for x in no.split('.'))
# lessons
import re as _r
def _fix(o):
    if isinstance(o,str):
        o=_r.sub(r'\$[^$]*\$',lambda m:m.group(0).replace('<','\\lt ').replace('>','\\gt '),o)
        out=_r.sub(r'\$[^$]*\$','',o)
        if '<' in out or '>' in out: print('ANGLE OUTSIDE MATH',o[:80])
        return o
    if isinstance(o,list): return [_fix(x) for x in o]
    if isinstance(o,dict): return {k:(_fix(v) if k not in ('fig',) else v) for k,v in o.items()}
    return o
lessons.LES=[_fix(l) for l in lessons.LES]
have={l['no'] for l in D['lessons']}
for l in lessons.LES:
    if l['no'] in have: D['lessons']=[x for x in D['lessons'] if x['no']!=l['no']]
    D['lessons'].append(l)
D['lessons'].sort(key=lambda l:key(l['no']))
D['lessons']=[_fix(l) for l in D['lessons']]
for l in D['lessons']:
    if l['no']=='3.3': l['blocks'][0]['fig']='f3_3'
    if l['no']=='1.6': l['blocks'][0]['fig']='f1_6'
    D['titles'][l['no']]=l['title']
D['figs'].update(figs.FIGS)
# mcq
old=[x for x in D['mcq'] if '-g' not in x['id']]
for x in old:
    if x['id']=='BK-M6' and not x.get('traps'):
        x['traps']={'A':'Reversed only the direction: the reflection over the $x$-axis also flips concave down to concave up.','C':'Kept the parent function $\\ln(x-3)$; the factor $-\\frac12$ reflects the graph.','D':'Reversed only the concavity; the negative factor also turns increasing into decreasing.'}
gen=common.make_all()
ws=[x for x in old+gen if x['src']=='ws']; bk=[x for x in old if x['src']!='ws']
ws.sort(key=lambda x:(key(x['t']),x['id'].endswith('~t'),x['id']))
# keep twin pairs adjacent: sort by base id then ~t
ws.sort(key=lambda x:(key(x['t']),x['id'].replace('~t',''),x['id'].endswith('~t')))
D['mcq']=ws+bk
js=json.dumps(D,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
h=h[:m.start(2)]+js+h[m.end(2):]
# UI text
reps=[("${[1,2].map(u=>`<div><h2>Unit ${u}","${[1,2,3].map(u=>`<div><h2>Unit ${u}"),
      ("guided lessons across Units 1 and 2","guided lessons across Units 1 to 3"),
      ("${LES.length} topics · Units 1–2","${LES.length} topics · Units 1–3")]
for a,b in reps:
    if a in h: h=h.replace(a,b)
    elif b not in h: print('MISSING',a)
open(P,'w',encoding='utf8').write(h)
from collections import Counter
c=Counter(x['t'] for x in D['mcq'] if x['src']=='ws')
print('lessons',len(D['lessons']),'mcq',len(D['mcq']),'ws topics',len(c),'min',min(c.values()))
print(sorted(c.items(),key=lambda kv:key(kv[0])))
