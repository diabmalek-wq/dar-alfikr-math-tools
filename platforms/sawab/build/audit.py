import sys,re,os,json
from playwright.sync_api import sync_playwright
sys.path.insert(0,'/home/claude/v2'); from shots import route
PAGES=['','sat/','saat/','gat/','ap/','sat/mock/','saat/mock/','gat/mock/','ap/mock/','sat/guided/','saat/guided/','gat/guided/','ap/guided/']
VP={'desk':{'width':1280,'height':900},'phone':{'width':390,'height':844}}
res=[]
with sync_playwright() as p:
    b=p.chromium.launch()
    for vn,vp in VP.items():
        for path in PAGES:
            pg=b.new_page(viewport=vp); errs=[]
            pg.on('pageerror',lambda e:errs.append('PAGEERR '+str(e)[:150]))
            pg.on('console',lambda m:errs.append('CONSOLE '+m.text[:150]) if m.type=='error' and 'ERR_' not in m.text and 'Failed to load' not in m.text else None)
            pg.route('**/*',route)
            pg.goto('http://localhost:8765/'+path); pg.wait_for_timeout(1200)
            info=pg.evaluate('''()=>{const W=innerWidth;const over=[...document.querySelectorAll('body *')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&r.right>W+2&&getComputedStyle(e).position!=='fixed'}).slice(0,6).map(e=>e.tagName+'.'+(e.className||'').toString().slice(0,30)+' r='+Math.round(e.getBoundingClientRect().right));
              const imgs=[...document.images].filter(i=>i.complete&&i.naturalWidth===0).map(i=>i.src.slice(0,60));
              const links=[...document.querySelectorAll('a[href]')].map(a=>a.getAttribute('href'));
              const t=document.body.innerText;const raw=(t.match(/\\$[^$\\n]{1,40}\\$/g)||[]).slice(0,3);
              return {sw:document.documentElement.scrollWidth,W,over,imgs,links,kerr:document.querySelectorAll('.katex-error').length,raw,title:document.title}}''')
            bad=[]
            for h in info['links']:
                if h.startswith(('http','mailto','#','javascript')) : continue
                full=os.path.normpath(os.path.join('/home/claude/v2/site',path,h.split('#')[0].split('?')[0]))
                if os.path.isdir(full): full=os.path.join(full,'index.html')
                if not os.path.exists(full): bad.append(h)
            pg.screenshot(path='/tmp/claude-0/aud/%s_%s.png'%(vn,(path or 'home').replace('/','_')))
            res.append((vn,path or '/',info['title'],'scrollW=%d/%d'%(info['sw'],info['W']),info['over'][:3],info['imgs'],bad,info['kerr'],info['raw'],errs[:4]))
            pg.close()
    b.close()
for r in res: print(r)
