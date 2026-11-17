import json,re
it=json.load(open('items_all.json'))
add="A-343 A-344 A-345 AM-332 AM-333 AM-334 AM-335 AM-336 AM-337 AM-338 AM-339 AM-340 AM-341 AM-342 AM-343 GT-123 GT-141 GT-157 GT-169 GT-275 GT-276 GT-277 PS-211 PS-212 PS-213 A-346 A-347 A-348 AM-344 AM-345 AM-346 AM-347 AM-348 AM-349 AM-350 GT-278 GT-279 PS-214 PS-215".split()
M={ # id: (domain, skill, sub)
'A':'Algebra','AM':'Advanced Math','GT':'Geometry and Trigonometry','PS':'Problem-Solving and Data Analysis'}
S={
'A-343':('Linear equations in one variable','Equations with constants and parameters'),
'A-344':('Linear equations in one variable','Word problems and writing equations'),
'A-345':('Linear inequalities','Systems of inequalities'),
'AM-332':('Nonlinear equations and systems','Quadratic equations and discriminant'),
'AM-333':('Nonlinear equations and systems','Linear-nonlinear and nonlinear systems'),
'AM-334':('Nonlinear functions','Quadratic functions and vertex form'),
'AM-335':('Nonlinear functions','Quadratic functions and vertex form'),
'AM-336':('Nonlinear functions','Polynomial and rational function graphs'),
'AM-337':('Equivalent expressions','Polynomial division and remainder'),
'AM-338':('Equivalent expressions','Factoring and expanding'),
'AM-339':('Equivalent expressions','Factoring and expanding'),
'AM-340':('Equivalent expressions','Exponents and radicals'),
'AM-341':('Equivalent expressions','Factoring and expanding'),
'AM-342':('Nonlinear equations and systems','Quadratic equations and discriminant'),
'AM-343':('Nonlinear functions','Polynomial and rational function graphs'),
'GT-123':('Circles','Equation of a circle'),'GT-157':('Circles','Equation of a circle'),
'GT-141':('Lines, angles, and triangles','Other triangle problems'),
'GT-169':('Circles','Tangent lines'),'GT-275':('Circles','Tangent lines'),
'GT-276':('Circles','Equation of a circle'),'GT-277':('Circles','Inscribed angles and chords'),
'PS-211':('One-variable data','Mean, median and mode'),
'PS-212':('Ratios, rates and units','Ratios and scale'),
'PS-213':('Ratios, rates and units','Unit conversion'),
'A-346':('Linear equations in one variable','Equations with constants and parameters'),
'A-347':('Systems of linear equations','No solution or infinitely many solutions'),
'A-348':('Linear functions','Slope and graph features'),
'AM-344':('Nonlinear functions','Function transformations and notation'),
'AM-345':('Equivalent expressions','Exponents and radicals'),
'AM-346':('Equivalent expressions','Factoring and expanding'),
'AM-347':('Nonlinear functions','Polynomial and rational function graphs'),
'AM-348':('Nonlinear functions','Exponential growth and decay'),
'AM-349':('Nonlinear functions','Exponential growth and decay'),
'AM-350':('Nonlinear functions','Quadratic functions and vertex form'),
'GT-278':('Right triangles and trigonometry','Sine, cosine, tangent ratios'),
'GT-279':('Lines, angles, and triangles','Congruence and special triangles'),
'PS-214':('Percentages','Percent of a quantity and parts'),
'PS-215':('Percentages','Percent change and growth'),
}
import fractions
def num(a):
    import sympy as sp
    s=a.strip().split(' (')[0].strip().strip('$')
    s=re.sub(r'\\left|\\right|\\,|\\!','',s).replace('\\dfrac','\\frac')
    s=re.sub(r'\\frac\{([^{}]+)\}\{([^{}]+)\}',r'((\1)/(\2))',s)
    s=re.sub(r'\\sqrt\{([^{}]+)\}',r'sqrt(\1)',s).replace('\\pi','pi').replace('{','(').replace('}',')').replace('^','**').replace(' ','')
    s=re.sub(r'(\d),(\d{3})',r'\1\2',s)
    return float(sp.N(sp.sympify(s)))
out=[];n=0
for k in add:
    v=it[k]; q=re.sub(r'\n+',' ',v['q'])
    dom=M[k.split('-')[0]]; skill,sub=S[k]
    lv='M' if v['diff'].startswith('Medium') else 'H'
    steps=[s.strip() for s in re.split(r'\n\s*\d+\.\s+',"\n"+v['r']) if s.strip()]
    if len(steps)==1: steps=[s.strip() for s in re.split(r'(?<=\.)\s+(?=[A-Z$])',v['r']) if s.strip()]
    steps=[re.sub(r'\s*\n\s*',' ',s) for s in steps]
    if v.get('m'): steps.append('Trap: '+re.sub(r'\s+',' ',v['m']).replace('Students ','students ',1) if False else 'Trap: '+re.sub(r'\s+',' ',v['m']))
    # table -> html
    mt=re.search(r'\|(.+)\|\s*\|[-| ]+\|\s*\|(.+)\|',q)
    if mt:
        hd=[c.strip() for c in mt[1].split('|')]; rw=[c.strip() for c in mt[2].split('|')]
        tb='<table style="border-collapse:collapse;margin:8px auto"><tr>'+''.join('<th style="border:1px solid #999;padding:3px 10px">%s</th>'%c for c in hd)+'</tr><tr>'+''.join('<td style="border:1px solid #999;padding:3px 10px;text-align:center">%s</td>'%c for c in rw)+'</tr></table>'
        q=q[:mt.start()].rstrip()+' '+tb+' '+q[mt.end():]
    mo=re.search(r'\(A\)',q)
    if mo:
        stem=q[:mo.start()].strip()
        opts=[o[1].strip() for o in re.findall(r'\(([A-D])\)\s*(.*?)(?=\s*\([A-D]\)|\Z)',q[mo.start():])]
        assert len(opts)==4,k
        key=ord(re.search(r'\(([A-D])\)',v['a'])[1])-65
        # rotate so key spreads
        tgt=n%4; n+=1
        order=list(range(4)); cur=order[key]
        opts2=opts[:]; ko=opts2.pop(key); opts2.insert(tgt,ko)
        out.append(dict(id=k,lv=lv,mc=True,domain=dom,skill=skill,q=stem,opts=opts2,key=tgt,steps=steps,sub=sub))
    else:
        a=v['a']
        if k=='A-348': val,disp=0.75,'\\dfrac{3}{4}'
        elif k=='PS-214': val,disp=0.53,'0.53'
        else:
            val=num(a); disp=a.strip().split(' (')[0].strip().strip('$')
        if abs(val-round(val))<1e-9: val=int(round(val))
        out.append(dict(id=k,lv=lv,mc=False,domain=dom,skill=skill,q=q,key=val,disp=disp,steps=steps,sub=sub))
json.dump(out,open('new_live_items.json','w'),ensure_ascii=False)
print(len(out))
for o in out: print(o['id'],o['key'],o.get('disp',''),o.get('opts') and len(o['opts']))
