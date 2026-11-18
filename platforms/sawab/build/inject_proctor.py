import re
SITE='/home/claude/v2/site'; P=open('/home/claude/v2/proctor.js').read()
HOOK={
 'saat':"window.__PX={title:'SAAT Lab mock exam',active:()=>S.phase==='exam'&&S.cfg&&S.cfg.mode==='mock',submit:()=>finish(),isReport:()=>S.phase==='report',where:()=>'Question '+(S.i+1)};",
 'gat':"window.__PX={title:'GAT Atelier mock exam',active:()=>S.phase==='exam'&&S.cfg&&['mock','sprint'].includes(S.cfg.mode),submit:()=>finish(),isReport:()=>S.phase==='report',where:()=>'Question '+(S.i+1)};",
 'ap':"window.__PX={title:'AP Precalc mixed mock',active:()=>S.v==='quiz'&&S.cfg&&!!S.cfg.min,submit:()=>finish(),isReport:()=>S.v==='report'&&S.cfg&&!!S.cfg.min,where:()=>'Question '+(S.i+1)};",
}
for k,h in HOOK.items():
    p=f'{SITE}/{k}/mock/index.html'; t=open(p,encoding='utf8').read()
    t=re.sub(r'<script id="sawab-proctor">.*?</script>','',t,flags=re.S)
    t=t.replace('/*PXHOOK*/'+h,'') if k=='saat' else t
    if k=='saat':
        t=re.sub(r'/\*PXHOOK\*/window\.__PX=\{.*?\};','',t,flags=re.S)
        i=t.rfind('render();\n})();'); assert i>0
        t=t[:i]+'/*PXHOOK*/'+h+'\n'+t[i:]
        add=f'<script id="sawab-proctor">{P}</script>'
    else:
        add=f'<script id="sawab-proctor">{h}\n{P}</script>'
    j=t.rfind('</body>'); t=t[:j]+add+t[j:]
    open(p,'w',encoding='utf8').write(t); print(k,'ok')
