import json,sys,re,glob
from fractions import Fraction
orig={i['id']:i for i in json.load(open('orig.json'))}
def num(s):
    s=re.sub(r'\\[dt]?frac\{([^}]*)\}\{([^}]*)\}',r'(\1)/(\2)',s)
    s=s.replace('$','').replace('{,}','').replace(',','').replace('\\%','').replace('%','').replace('\\$','').replace('\\,','').replace('\\ ','')
    s=re.sub(r'\\sqrt\{([^}]*)\}',r'(\1)**0.5',s).replace('\\pi','3.14159265358979').replace('\\cdot','*').replace('^','**').replace('{','(').replace('}',')').replace('\\','')
    s=re.sub(r'[A-Za-z]+','',s)
    try: return float(eval(s,{}))
    except Exception: return None
def check(f):
    bad=[]
    out=json.load(open(f)); 
    for x in out:
        o=orig.get(x['id'])
        if not o: bad.append((x['id'],'unknown id'));continue
        q=x.get('q','')
        if q.count('$')%2: bad.append((x['id'],'odd $'))
        if '|---' in q: bad.append((x['id'],'table'))
        if len(x.get('steps',[]))<2: bad.append((x['id'],'steps'))
        if o['opts']:
            if not x.get('mc') or len(x.get('opts',[]))!=4 or len(set(x['opts']))!=4: bad.append((x['id'],'opts'));continue
            if not isinstance(x['key'],int) or not 0<=x['key']<4: bad.append((x['id'],'key'));continue
            if any(s.count('$')%2 for s in x['opts']): bad.append((x['id'],'odd $ opt'))
            a=num(o['opts'][o['key']]); b=num(x['opts'][x['key']])
            if a is not None and b is not None:
                if abs(a-b)>1e-6*max(1,abs(a)): bad.append((x['id'],f'answer changed {a} -> {b}'))
            elif a is None or b is None:
                if re.sub(r'\W','',o['opts'][o['key']])!=re.sub(r'\W','',x['opts'][x['key']]): bad.append((x['id'],'answer text differs (manual)'))
        else:
            if x.get('mc'): bad.append((x['id'],'mc flag'));continue
            kn=o.get('key_num')
            if kn is None or not isinstance(x['key'],(int,float)) or abs(kn-x['key'])>1e-6*max(1,abs(kn)): bad.append((x['id'],f"spr key {kn} vs {x.get('key')}"))
            if not x.get('disp'): bad.append((x['id'],'disp'))
        if x['q'].strip()==o['q'].strip(): bad.append((x['id'],'copied'))
    ids=[i['id'] for i in json.load(open(f.replace('out/','batches/')))]
    miss=set(ids)-{x['id'] for x in out}
    if miss: bad.append(('missing',sorted(miss)))
    return len(out),bad
if __name__=='__main__':
    for f in sorted(glob.glob(sys.argv[1] if len(sys.argv)>1 else 'out/b*.json')):
        n,b=check(f);print(f,n,'BAD',len(b));[print('  ',x) for x in b[:12]]
