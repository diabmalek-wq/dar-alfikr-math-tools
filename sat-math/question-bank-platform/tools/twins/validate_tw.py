import json,sys,re
rows=[l.split('|') for l in open('/home/claude/repo/qb/tools/subtopic_counts.md') if l.startswith('| ') and 'Domain' not in l and '---' not in l]
TAX={(r[1].strip(),r[2].strip(),r[3].strip()) for r in rows}
bad=[];tot=0
for f in sys.argv[1:]:
    src=json.load(open(f.replace('/out/','/b/')))
    out=json.load(open(f)); tot+=len(out)
    if [x['id'] for x in out]!=[s['src_id']+'-2' for s in src]: bad.append((f,'ids/order'))
    for n,x in enumerate(out,1):
        i=x['id']; s=src[n-1]
        if (x.get('domain'),x.get('skill'),x.get('sub'))!=(s['domain'],s['skill'],s['sub']): bad.append((i,'taxonomy'))
        if x['mc']!=s['mc']: bad.append((i,'format'))
        if x['lv'] not in ('M','H'): bad.append((i,'lv'))
        if x['q'].strip()==s['src_q'].strip(): bad.append((i,'same q'))
        for t in [x['q']]+x.get('opts',[])+x['steps']:
            if t.count('$')%2: bad.append((i,'odd $'))
            if re.search(r'\\\\|\\par|\\\$|—|<table|\|---',t): bad.append((i,'forbidden',t[:30]))
        if not 3<=len(x['steps'])<=4: bad.append((i,'steps'))
        if x['mc']:
            if len(x.get('opts',[]))!=4 or len(set(x['opts']))!=4: bad.append((i,'opts'))
            elif x['key']!=n%4: bad.append((i,'key pos',x['key'],n%4))
        else:
            if not x.get('disp') or not isinstance(x['key'],(int,float)): bad.append((i,'spr'))
print('items',tot,'BAD',len(bad));[print(b) for b in bad]
