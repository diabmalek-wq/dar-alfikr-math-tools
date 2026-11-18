import json,sys
from spec_r import ITEMS
out=[];bad=0
for n,it in enumerate(ITEMS,1):
    vals=it['vals'];fmt=it['fmt'];passing=[i for i,v in enumerate(vals) if it['pred'](v)]
    strs=[fmt(v) for v in vals]; ok=passing==[0] and len(set(strs))==4 and len(it['notes'])==3
    print('OK  ' if ok else 'FAIL',n,it['sig'],'->',strs[0],'' if ok else f'passing={passing}'); bad+=(not ok)
    r=(n-1)%4; order=list(range(4)); order=order[-r:]+order[:-r] if r else order
    opts=[strs[i] for i in order]; ans=order.index(0); L='ABCD'; traps=[]
    for k in range(1,4): traps.append(f"{L[order.index(k)]}: {strs[k]} — {it['notes'][k-1][3:].strip()}")
    traps.sort()
    out.append(dict(sig=it['sig'],code=f"SAAT-R.{n}",unit=it['unit'],topic=it['topic'],lvl=it['lvl'],fig=it['fig'],figW=it['figW'],stem=it['stem'],opts=opts,ans=ans,trick=it['trick'],why=it['why'],traps=traps))
print(len(out),'items,',bad,'failures')
if bad: sys.exit(1)
open('saat_items_r.js','w').write("// SAAT BANK — part R: figure items redrawn from skills seen in leak/trial papers (Nov 2026). Figures drawn from the answer's own coordinates (spec_r.py).\nmodule.exports = "+json.dumps(out,ensure_ascii=False,indent=2)+";\n")
from collections import Counter; print(Counter('ABCD'[o['ans']] for o in out))
