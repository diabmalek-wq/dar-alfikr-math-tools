"""Post-build: inject icons, manifest, share-preview tags and offline service worker into every page (idempotent)."""
import re,glob,os,html
SITE='/home/claude/v2/site'; BASE='https://sawabmath.pages.dev'
DESC={'':'Free practice studios for SAT Math, SAAT (Tahsili), GAT (Qudurat) and AP Precalculus: mock exams, guided practice, and every wrong option explained.',
 'sat':'Adaptive Bluebook-style SAT Math mock exams with Desmos, plus guided practice where every wrong option is a named trap.',
 'saat':'Tahsili (SAAT) math without a calculator: weighted mocks, strand drills and guided practice with named traps.',
 'gat':'Qudurat (GAT) quantitative practice on the ETEC blueprint: mocks, sprints, a comparison clinic and guided practice.',
 'ap':'AP Precalculus Units 1 to 3: book-aligned lessons, 400+ questions with named traps, guided practice and an FRQ workshop.'}
A,B='<!--sawab-head-->','<!--/sawab-head-->'; C,D='<!--sawab-sw-->','<!--/sawab-sw-->'
for f in glob.glob(SITE+'/**/*.html',recursive=True):
    rel=os.path.relpath(f,SITE); sec=rel.split('/')[0] if '/' in rel else ''
    if sec not in DESC: sec=''
    h=open(f,encoding='utf8').read()
    h=re.sub(re.escape(A)+'.*?'+re.escape(B),'',h,flags=re.S); h=re.sub(re.escape(C)+'.*?'+re.escape(D),'',h,flags=re.S)
    t=re.search(r'<title>(.*?)</title>',h,re.S); title=html.unescape(t.group(1).strip()) if t else 'Sawab'
    url=BASE+'/'+(os.path.dirname(rel)+'/' if os.path.dirname(rel) else '')
    d=DESC[sec]; e=lambda s:html.escape(s,quote=True)
    head=(A+'<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/assets/apple-touch-icon.png"><link rel="manifest" href="/manifest.webmanifest"><meta name="theme-color" content="#070b10">'
          '<meta name="description" content="%s"><meta property="og:type" content="website"><meta property="og:site_name" content="Sawab · صواب"><meta property="og:title" content="%s"><meta property="og:description" content="%s"><meta property="og:url" content="%s"><meta property="og:image" content="%s/assets/og.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">'%(e(d),e(title),e(d),e(url),BASE)+B)
    sw=C+"<script>if('serviceWorker' in navigator&&location.protocol==='https:')addEventListener('load',()=>navigator.serviceWorker.register('/sw.js').catch(()=>{}))</script>"+D
    i=h.find('</head>')
    if i<0: i=h.find('</title>')+len('</title>')
    h=h[:i]+head+h[i:]
    j=h.rfind('</body>'); h=h[:j]+sw+h[j:] if j>0 else h+sw
    open(f,'w',encoding='utf8').write(h)
    print('polished',rel)
