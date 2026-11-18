import json, sys
sys.path.insert(0,'.')
from spec_q import ITEMS
out=[]; bad=0
for n,it in enumerate(ITEMS,1):
    vals=it['vals']; fmt=it['fmt']
    passing=[i for i,v in enumerate(vals) if it['pred'](v)]
    strs=[fmt(v) for v in vals]
    ok = passing==[0] and len(set(strs))==4 and len(it['notes'])==3
    print(('OK  ' if ok else 'FAIL'), n, it['sig'], '->', strs[0], '' if ok else f'passing={passing} strs={strs}')
    bad+= (not ok)
    r=(n-1)%4  # rotate so the key lands on A/B/C/D evenly
    order=list(range(4)); order=order[-r:]+order[:-r] if r else order
    opts=[strs[i] for i in order]; ans=order.index(0)
    L='ABCD'; traps=[]
    for k in range(1,4):
        pos=order.index(k); traps.append(f"{L[pos]}: {strs[k]} — {it['notes'][k-1][3:].strip()}")
    traps.sort()
    out.append(dict(sig=it['sig'],code=f"SAAT-Q.{n}",unit=it['unit'],topic=it['topic'],lvl=it['lvl'],stem=it['stem'],opts=opts,ans=ans,trick=it['trick'],why=it['why'],traps=traps))
print(len(out),'items,',bad,'failures')
if bad: sys.exit(1)
head="// SAAT BANK — part Q: skills read (skill and trap only) from nine leak and trial PDFs (Nov 2026).\n// Stems, numbers and options are original; every key is re-derived by a predicate in spec_q.py.\nmodule.exports = "
open('saat_items_q.js','w').write(head+json.dumps(out,ensure_ascii=False,indent=2)+";\n")
from collections import Counter
print(Counter('ABCD'[o['ans']] for o in out))
