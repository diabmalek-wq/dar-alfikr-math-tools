import sys,json,random
from playwright.sync_api import sync_playwright
exams=sys.argv[1:] or ['sat','saat','gat','ap']
def fmt(v):
    return str(v)
with sync_playwright() as p:
    b=p.chromium.launch()
    for k in exams:
        pg=b.new_page(viewport={'width':1100,'height':900}); errs=[]
        pg.on('pageerror',lambda e:errs.append(str(e))); pg.on('console',lambda m:errs.append(m.text) if m.type=='error' else None)
        pg.goto(f'http://localhost:8765/{k}/guided/'); pg.wait_for_timeout(800)
        groups=pg.evaluate('__GP.CFG.groups.map(g=>g.id)')
        types={};res=[]
        for g in groups:
            pg.evaluate('(g)=>__GP.build(g)',g); pg.wait_for_timeout(150)
            n=pg.evaluate('__GP.S.steps.length'); wrong_at=random.randrange(n)
            for step in range(n):
                s=pg.evaluate('(()=>{const s=__GP.S.steps[__GP.S.i];return {kind:s.kind,type:s.type,a:s.it.a,n:s.it.n,claim:s.claim,ans:s.ans,rows:s.rows,ordn:s.it.ord&&s.it.ord.length,oo:s.it.o&&s.it.o.length,id:s.it.id}})()')
                if s['kind']=='w':
                    pg.click('#all'); pg.click('#go'); continue
                types[s['type']]=types.get(s['type'],0)+1
                wrong = (step==wrong_at)
                t=s['type']
                if t=='mc':
                    i=s['a']; 
                    if wrong: i=(i+1)%s['oo']
                    pg.click(f'.opt[data-i="{i}"]')
                elif t=='tf':
                    truth = s['claim']==s['a']; v = (not truth) if wrong else truth
                    pg.click(f'.opt[data-b="{1 if v else 0}"]')
                elif t=='fill':
                    v=pg.evaluate('(()=>{const s=__GP.S.steps[__GP.S.i],it=s.it;const nv=it.o?(it.o.map(__GP.parseNum)[it.a]):it.n;return nv})()')
                    if wrong: v=v+7
                    pg.fill('#fin',fmt(v))
                elif t=='order':
                    order=list(range(s['ordn']))
                    if wrong: order=order[::-1]
                    for i in order: pg.click(f'[data-add="{i}"]')
                elif t=='match':
                    for r in s['rows']:
                        pg.select_option(f'select[data-r="{r}"]', str(r if not wrong else s['rows'][0]) )
                pg.click('#chk'); pg.wait_for_timeout(30)
                if pg.locator('#hint').count()==0 and pg.evaluate('!__GP.S.steps[__GP.S.i].done'):
                    # guided retry: solve correctly now
                    pass
                done=pg.evaluate('__GP.S.steps[__GP.S.i].done')
                if not done:
                    # retry correctly
                    if t=='mc': pg.click(f'.opt[data-i="{s["a"]}"]')
                    elif t=='tf':
                        truth = s['claim']==s['a']; pg.click(f'.opt[data-b="{1 if truth else 0}"]')
                    elif t=='fill':
                        v=pg.evaluate('(()=>{const s=__GP.S.steps[__GP.S.i],it=s.it;return it.o?(it.o.map(__GP.parseNum)[it.a]):it.n})()'); pg.fill('#fin',fmt(v))
                    elif t=='order':
                        for i in range(len(s['rows']) if False else 0): pass
                        pg.evaluate('(()=>{const s=__GP.S.steps[__GP.S.i];s.seq=[]})()')
                        pg.evaluate('(()=>{const s=__GP.S.steps[__GP.S.i];s.seq=s.it.ord.map((_,i)=>i)})()')
                    elif t=='match':
                        for r in s['rows']: pg.select_option(f'select[data-r="{r}"]', str(r))
                    pg.click('#chk',timeout=3000) if t!='order' else pg.evaluate('document.querySelector("#chk")&&(document.querySelector("#chk").disabled=false)')
                    if t=='order': pg.evaluate('(()=>{const s=__GP.S.steps[__GP.S.i];})()')
                    # for order, rerender via hint-less path: click chk
                    if t=='order':
                        pg.evaluate("document.querySelector('#chk').click()")
                pg.click('#cont')
            txt=pg.inner_text('#app')
            assert 'independent block' in txt.lower(), (k,g,txt[:200]); res.append((g,txt.lower().count('mastery gate passed')))
        print(k,'passed',sum(r[1] for r in res),'of',len(res),'OK groups',len(groups),'types',types,'errors',errs[:5])
        pg.close()
    b.close()
