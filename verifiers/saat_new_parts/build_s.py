import json,sys
sys.path.insert(0,'.')
from spec_s import ITEMS
out=[];bad=0
for n,it in enumerate(ITEMS,1):
    vals=it['vals'];fmt=it['fmt']
    passing=[i for i,v in enumerate(vals) if it['pred'](v)]
    strs=[fmt(v) for v in vals]
    ok=len(passing)==1 and passing[0]==(0 if not it['natural'] else passing[0]) and len(set(strs))==4 and len(it['notes'])==3
    if not it['natural']: ok=ok and passing==[0]
    print(('OK  ' if ok else 'FAIL'),n,it['sig'],'->',strs[passing[0]] if passing else None,'' if ok else f'passing={passing} strs={strs}')
    bad+=(not ok)
    if not ok: continue
    L='ABCD'
    if it['natural']:
        opts=strs;ans=passing[0];wrong=[j for j in range(4) if j!=ans]
        traps=[f"{L[j]}: {strs[j]} — {it['notes'][i][3:].split(' — ',1)[1]}" for i,j in enumerate(wrong)]
    else:
        r=(n-1)%4;order=list(range(4));order=order[-r:]+order[:-r] if r else order
        opts=[strs[i] for i in order];ans=order.index(0);traps=[]
        for kk in range(1,4):
            pos=order.index(kk);traps.append(f"{L[pos]}: {strs[kk]} — {it['notes'][kk-1][3:].strip().split(' — ',1)[-1] if ' — ' in it['notes'][kk-1] else it['notes'][kk-1][3:].strip()}")
        traps.sort()
    LV2={'average-speed','pure-water','filling-with','catch-up','age-problem','years-until','speed-of-a-boat','power-of-i','coefficient-of-a-single','sum-of-all-zeros','touch-or-cross','count-the-integers','sum-of-the-two','within-a','greatest-integer','strict-budget','change-in-area','inner-area','which-provider','first-error','solutions-of-a-quadratic','condition-for-two','equate-real','target-combination','sum-of-cubes','degree-after','tolerance','isolate-x','combine-fractions','make-a-variable'}
    lv=2 if any(it['sig'].startswith(k) or k in it['sig'] for k in LV2) and it['lvl']==3 else it['lvl']
    out.append(dict(sig=it['sig'],code=f"SAAT-S.{n}",unit=it['unit'],topic=it['topic'],lvl=lv,stem=it['stem'],opts=opts,ans=ans,trick=it['trick'],why=it['why'],traps=traps))
print(len(out),'items,',bad,'failures')
json.dump(out,open('out_s.json','w'),ensure_ascii=False,indent=1)
if bad: sys.exit(1)
