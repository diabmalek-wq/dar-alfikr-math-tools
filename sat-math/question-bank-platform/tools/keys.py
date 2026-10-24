import re,json,math
from fractions import Fraction
it=json.load(open('orig.json'))
def clean(s):
    s=s.replace('\\dfrac','\\frac').replace('\\tfrac','\\frac').replace('\\left','').replace('\\right','').replace('\\,','').replace('{,}','').replace('\\!','')
    return s
def tonum(expr):
    e=clean(expr).strip().strip('$').strip()
    e=re.sub(r'\\text\{[^}]*\}','',e); e=e.replace('\\%','').replace('%','').replace('\\$','').replace('°','').replace('\\circ','').replace('^\\circ','').strip()
    e=e.replace('{','(').replace('}',')')
    e=re.sub(r'\\frac\(([^()]*)\)\(([^()]*)\)',r'((\1)/(\2))',e); e=re.sub(r'\\frac(\d)(\d)',r'((\1)/(\2))',e); e=re.sub(r'\\frac(\d)\(',r'((\1)/(',e)
    e=e.replace('\\sqrt','sqrt').replace('\\pi','pi').replace('\\cdot','*').replace('\\times','*').replace('^','**')
    e=re.sub(r'(\d)\s*(sqrt|pi)',r'\1*\2',e); e=re.sub(r'\)\s*(\(|sqrt|pi)',r')*\1',e)
    e=re.sub(r'(\d),(\d{3})',r'\1\2',e)
    try: return float(eval(e,{'sqrt':math.sqrt,'pi':math.pi,'__builtins__':{}}))
    except Exception: return None
out=[];fail=[]
for i in it:
    if i['spr'] is None: continue
    s=i['spr']; main=re.split(r'\s*\(or\s',s)[0].split(' or ')[0]
    v=tonum(main)
    if v is None: fail.append((i['id'],s))
    i['key_num']=v
print('SPR',sum(1 for i in it if i['spr']),'fail',len(fail)); print(fail[:40])
json.dump(it,open('orig.json','w'))
