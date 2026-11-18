import sys,re
from playwright.sync_api import sync_playwright
V='/home/claude/v2/site/ap/vendor/'
def route(r):
    u=r.request.url
    if 'katex.min.css' in u: r.fulfill(path=V+'katex.min.css',content_type='text/css')
    elif 'auto-render' in u: r.fulfill(path=V+'auto-render.min.js',content_type='application/javascript')
    elif 'katex.min.js' in u: r.fulfill(path=V+'katex.min.js',content_type='application/javascript')
    elif 'fonts.g' in u or 'cdnjs' in u: r.abort()
    else: r.continue_()
with sync_playwright() as p:
    b=p.chromium.launch()
    for k,g in [('sat','linear-functions'),('saat','geometry'),('gat','ari'),('ap','l1-11')]:
        pg=b.new_page(viewport={'width':1100,'height':900}); pg.route('**/*',route)
        pg.goto(f'http://localhost:8765/{k}/guided/'); pg.wait_for_timeout(900)
        pg.screenshot(path=f'/tmp/g_{k}_home.png')
        pg.evaluate('(g)=>__GP.build(g)',g); pg.wait_for_timeout(300)
        pg.click('#next'); pg.wait_for_timeout(300); pg.screenshot(path=f'/tmp/g_{k}_w.png')
        (pg.click('#all') if pg.locator('#all').count() else None); pg.click('#go'); pg.wait_for_timeout(300)
        # pick wrong option on mc/tf, then screenshot
        pg.evaluate("(()=>{const s=__GP.S.steps[__GP.S.i];if(s.type!=='mc'){s.type='mc';}})()") if False else None
        pg.screenshot(path=f'/tmp/g_{k}_t.png',full_page=True)
        pg.close()
    b.close()
