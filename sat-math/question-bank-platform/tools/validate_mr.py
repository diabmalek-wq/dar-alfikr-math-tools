import json,sys,re,glob
sys.path.insert(0,'/home/claude/repo/qb')
rows=[l.split('|') for l in open('/home/claude/repo/qb/tools/subtopic_counts.md') if l.startswith('| ') and 'Domain' not in l and '---' not in l]
TAX={(r[1].strip(),r[2].strip(),r[3].strip()) for r in rows}
bad=[];allitems=[]
for f in sys.argv[1:]:
    out=json.load(open(f));allitems+=out
    skp=json.load(open(f.replace('.json','_skip.json')))
    for n,x in enumerate(out,1):
        i=x['id']
        if (x.get('domain'),x.get('skill'),x.get('sub')) not in TAX: bad.append((i,'taxonomy',x.get('sub')))
        if x['lv'] not in ('M','H'): bad.append((i,'lv'))
        for t in [x['q']]+x.get('opts',[])+x['steps']:
            if t.count('$')%2: bad.append((i,'odd $'))
            if re.search(r'\\\\|\\par|\\\$|—|<table|\|---',t): bad.append((i,'forbidden',t[:30]))
        if not 3<=len(x['steps'])<=4: bad.append((i,'steps'))
        if x['mc']:
            if len(x.get('opts',[]))!=4 or len(set(x['opts']))!=4: bad.append((i,'opts'))
            elif x['key']!=n%4: bad.append((i,'key pos',x['key'],n%4))
        else:
            if not x.get('disp') or not isinstance(x['key'],(int,float)): bad.append((i,'spr'))
    ids=[x['src_q'] for x in out]+[s['q'] for s in skp]
    if len(ids)!=len(set(ids)): bad.append((f,'dup q'))
print('items',len(allitems),'BAD',len(bad));[print(b) for b in bad]
