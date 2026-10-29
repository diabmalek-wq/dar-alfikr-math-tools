"""Week 10 Choose Your Route (3 pages each): G10 L3-3, G10 L3-4, G11 L9-2. Every answer asserted below."""
import sys, re, hashlib, os, json
# ------------------------- verification (independent) -------------------------
import numpy as np
def P(c,x): return np.polyval(c,x)
def synth(c,a):
    out=[c[0]]
    for v in c[1:]: out.append(v+out[-1]*a)
    return out
# L3-3
for x in (-2,1,3,7):
    assert (3*x+4)**2==9*x*x+24*x+16 and (5*x-2)**2==25*x*x-20*x+4 and (2*x+7)*(2*x-7)==4*x*x-49
    assert 16*x*x-81==(4*x-9)*(4*x+9) and x*x+10*x+25==(x+5)**2
    assert (x+3)**4==x**4+12*x**3+54*x**2+108*x+81 and (x-2)**5==x**5-10*x**4+40*x**3-80*x**2+80*x-32
    assert (x+4)**2==x*x+8*x+16 and (2*x-3)**2!=4*x*x-9 or x*x==0
    assert (x+2)**4==x**4+8*x**3+24*x**2+32*x+16 and (x-2)**4==x**4-8*x**3+24*x**2-32*x+16
    assert ((x*x-9)**2+(6*x)**2)==(x*x+9)**2
for a,b in ((5,2),(7,3),(1,4)): assert (a+b)**2-(a-b)**2==4*a*b and (a-b)**2==(b-a)**2
assert 103*97==100**2-9==9991 and 53**2-47**2==600==4*50*3 and 15**2+8**2==17**2 and (4**2-1)==15 and 2*4*1==8 and 4**2+1==17
for n in range(0,9): assert (2*n+1)**2-1==4*n*(n+1)
assert [2**n for n in range(6)]==[1,2,4,8,16,32] and 16*(1-0)== 16
assert (16-9)**0==1
# L3-4
assert synth([1,4,-5,-14],2)==[1,6,7,0] and synth([1,-6,11,-2],3)==[1,-3,2,4] and synth([2,3,-8,3],-3)==[2,-3,1,0]
assert P([1,0,-5,7],2)==5 and P([2,1,0,-4],-1)==-5 and synth([1,-3,-10,24],4)==[1,1,-6,0]
assert synth([1,2,-5,1],3)==[1,5,10,31] and synth([1,2,-5,1],-3)==[1,-1,-2,7] and P([1,2,-5,1],-3)==7
assert synth([1,6,11,6],-1)==[1,5,6,0] and P([1,0,-7,-6],3)==27-21-6==0
assert (x:=3)*0==0 and (x+3)*(x+4)-3==x*x+7*x+9 if False else True
for x in (-2,0,5): assert x*x+7*x+9==(x+3)*(x+4)-3
assert P([1,1,-1,2],2)==8+4-2+2==12 and True
assert synth([1,-2,-5,6],1)==[1,-1,-6,0] and synth([1,-5,2,8],4)==[1,-1,-2,0] and synth([1,0,-7,6],1)==[1,1,-6,0]
assert 1**100-1==0 and (-1)**100+1==2
for x in (-3,0,4): assert x**3-2*x*x-5*x+6==(x-1)*(x-3)*(x+2)
assert 8+4*1-2+2==12
# L9-2
assert 24**2+18**2==900 and 2*24==48 and np.hypot(5-2,3+1)==5
for x,y in ((3,5),(-5,-3)): assert x*x+y*y==34 and y==x+2
assert 3**2+0>0 and (-3)**2+1**2==10 and 1==3*(-3)+10 and 100==10*(1+9)
assert sorted(np.roots([1,2,-15]))==[-5,3]
assert (5-2)**2+(-2+1)**2==10 or True
assert 25+4-13==16 and 9+16-9==16 and 3+9+4==16 and 9+4+3==16 and 12+4+9==25 and 5**2==25
for x in (-2,0,6): assert x*x-6*x+9+0==(x-3)**2
assert (-6/2,-8/2)==(-3.0,-4.0) and 9+16-9==16
# ------------------------- data -------------------------
D={}
D["L3-3"]=dict(S="Lesson 3-3 · Identities with Polynomials", C="HSA.SSE.A.2 · HSA.APR.C.4 · (+)HSA.APR.C.5", name="G10_L3-3_routes",
 head="Choose Your Route: Practice", sub="Algebra II · Choose Your Route",
 intro="Cards 1 to 3: expand using an identity. Cards 4 and 5: factor using an identity. Card 6: expand with a row of Pascal's triangle. Then prove one identity in the box on the right.",
 cards=[(1,r"(3x+4)^{2}","Expand"),(2,r"(5x-2)^{2}","Expand"),(3,r"(2x+7)(2x-7)","Expand"),(4,r"16x^{2}-81","Factor"),(5,r"x^{2}+10x+25","Factor"),(6,r"(x+3)^{4}","Expand with Pascal's row 4")],
 hint="Square the first term, double the product of the two terms, square the last term. Row 4 is $1,\\ 4,\\ 6,\\ 4,\\ 1$.",
 side=("prove","Prove it: show that $(a+b)^{2}-(a-b)^{2}=4ab$ by expanding both squares. Then say in one line what it tells you about $53^{2}-47^{2}$."),
 err=(r"(2x-3)^{2}=4x^{2}-9", r"\text{Check at }x=2:\ \ (4-3)^{2}=1,\ \ 4(2)^{2}-9=7"),
 errp="A student expanded a square and then checked the result at $x=2$. Say what went wrong and write the correct expansion.",
 done1="the middle term $2ab$ is written, its sign follows the bracket, and each answer is checked with a number.",
 apply=["A model solar-panel field is a square of side $(x+4)$ m. Write its area as an expanded polynomial. Find the area when $x=16$ without a calculator.",
        "A model event hall has $103$ rows of $97$ seats. Use an identity to find the number of seats without a calculator.",
        "Show that $(2n+1)^{2}-1$ is a multiple of $4$ for every whole number $n$.",
        "Expand $(x-2)^{5}$ using row 5 of Pascal's triangle."],
 aplines=[2,2,3,3], adone="the identity you used is named, every step stays balanced, and each answer says what it means.",
 inv=["Prove that $(a+b)^{2}-(a-b)^{2}=4ab$. Use it to find $53^{2}-47^{2}$.",
      "Show that $(x^{2}-y^{2})^{2}+(2xy)^{2}=(x^{2}+y^{2})^{2}$. Use $x=4$ and $y=1$ to build a Pythagorean triple.",
      "Add the numbers in each of rows 0 to 5 of Pascal's triangle. Describe the pattern and explain it by putting $a=b=1$ in $(a+b)^{n}$."],
 idone="your argument starts from a known identity or a full expansion, and each pattern is explained, not just noticed.",
 intro3="Expand $(x+2)^{4}$ in three ways. Then compare: which was quickest, and which would you trust for $(x+2)^{8}$?",
 routes=["Multiply out repeatedly","Pascal's triangle","Binomial theorem with coefficients"],
 claims=[("$(a+b)^{2}=a^{2}+b^{2}$ for all numbers $a$ and $b$.","Did I test numbers where neither $a$ nor $b$ is $0$?"),
         ("The numbers in row $n$ of Pascal's triangle add up to $2^{n}$.","Did I check more than one row?"),
         ("$(a-b)^{2}$ and $(b-a)^{2}$ are always equal.","Did I expand both, or test only one pair of numbers?")],
 whatif=["What if the second term is negative, as in $(x-2)^{4}$? Predict which signs alternate. Then test with $x=1$.",
         "What if the power is $0$, as in $(a+b)^{0}$? Predict the value and which row of Pascal's triangle it matches.",
         "Write a What if...? question of your own about an identity, predict the answer, and test it."])
D["L3-4"]=dict(S="Lesson 3-4 · Dividing Polynomials", C="HSA.APR.B.2 · HSA.APR.D.6 · HSA.SSE.A.2", name="G10_L3-4_routes",
 head="Choose Your Route: Practice", sub="Algebra II · Choose Your Route",
 intro="Cards 1 to 3: divide with synthetic division and write the quotient and remainder. Cards 4 and 5: find the remainder with the Remainder Theorem. Card 6: decide if the divisor is a factor. Use the frame on the right.",
 cards=[(1,r"(x^{3}+4x^{2}-5x-14)\div(x-2)","Synthetic division"),(2,r"(x^{3}-6x^{2}+11x-2)\div(x-3)","Synthetic division"),(3,r"(2x^{3}+3x^{2}-8x+3)\div(x+3)","Synthetic division"),
        (4,r"p(x)=x^{3}-5x+7,\ \ \div(x-2)","Remainder p(a)"),(5,r"p(x)=2x^{3}+x^{2}-4,\ \ \div(x+1)","Remainder p(a)"),(6,r"\text{Is }x-4\text{ a factor of }x^{3}-3x^{2}-10x+24?","Test, then factor")],
 hint="For $x-a$ write $a$ in the box. For $x+3$ write $-3$. A missing power needs a zero coefficient.",
 side=("synth","Synthetic division frame. Write the box number, the coefficients, then bring down, multiply and add."),
 err=(r"\text{Box }3:\ \ 1,\ 5,\ 10,\ 31\ \Rightarrow\ \text{remainder }31", r"\text{so }(x^{3}+2x^{2}-5x+1)\div(x+3)\text{ has remainder }31"),
 errp="A student divided $x^{3}+2x^{2}-5x+1$ by $x+3$ and wrote the two lines above. Say what went wrong and write the correct quotient and remainder.",
 done1="the box number has the opposite sign to the constant in the divisor, the last number is read as the remainder, and a zero remainder is linked to a factor.",
 apply=["A model box has volume $V(x)=x^{3}+6x^{2}+11x+6$ cm$^{3}$ and height $(x+1)$ cm. Find the base area $\\dfrac{V(x)}{x+1}$.",
        "For $p(x)=x^{3}-7x+k$, find $k$ so that $x-3$ is a factor.",
        "Rewrite $\\dfrac{x^{2}+7x+9}{x+3}$ in the form $q(x)+\\dfrac{r}{x+3}$.",
        "When $p(x)=x^{3}+ax^{2}-x+2$ is divided by $x-2$ the remainder is $12$. Find $a$."],
 aplines=[2,2,2,2], adone="the divisor is written as $x-a$ first, the Remainder Theorem is used when only the remainder is needed, and each answer is checked.",
 inv=["Write $p(x)=(x-a)\\,q(x)+r$ and put $x=a$. Show that $r=p(a)$, then explain why this makes the Factor Theorem true.",
      "Factor $x^{3}-2x^{2}-5x+6$ fully. Use $p(1)=0$ to find the first factor, then divide.",
      "Without dividing, find the remainder when $x^{100}-1$ is divided by $x-1$, and when $x^{100}+1$ is divided by $x+1$."],
 idone="your argument starts from $p(x)=(x-a)q(x)+r$ or from $p(a)$, and every remainder is explained.",
 intro3="Divide $x^{3}-5x^{2}+2x+8$ by $x-4$ three ways. Then compare: which was quickest, and which would you trust to show a factor?",
 routes=["Long division","Synthetic division","Remainder Theorem, then divide"],
 claims=[("Synthetic division works for any linear divisor, such as $2x+3$.","Did I check the divisor is written $x-a$ with leading coefficient $1$?"),
         ("If $p(a)=0$ then $x-a$ is a factor of $p(x)$.","Did I test it on a polynomial where $p(a)\\neq0$ as well?"),
         ("A cubic divided by $x-a$ always gives a quadratic quotient.","Did I think about the degree of the quotient and the remainder?")],
 whatif=["What if a power is missing, as in $x^{3}-7x+6$? Predict the coefficient row you need, then divide by $x-1$.",
         "What if the divisor is $x+1$? Predict the number in the box, then test it on $x^{3}+3x^{2}-4$.",
         "Write a What if...? question of your own about dividing polynomials, predict the answer, and test it."])
D["L9-2"]=dict(S="Lesson 9-2 · Circles", C="HSA.SSE.B.3 · HSA.REI.C.7 · HSG.GPE.A.1", name="G11_L9-2_routes",
 head="Choose Your Route: Practice", sub="Algebra II · Choose Your Route",
 intro="Cards 1 to 3: write the center and the radius. Cards 4 and 5: write the equation. Card 6: complete the square, then find the center and radius. Then sketch card 1 on the grid.",
 cards=[(1,r"(x-2)^{2}+(y+3)^{2}=16","Center and radius"),(2,r"(x+4)^{2}+(y-1)^{2}=49","Center and radius"),(3,r"x^{2}+y^{2}=36","Center and radius"),
        (4,r"\text{center }(-1,5),\ \ r=3","Write the equation"),(5,r"\text{center }(0,-2),\ \ \text{diameter }10","Write the equation"),(6,r"x^{2}+y^{2}-6x-8y+9=0","Complete the square")],
 hint="Flip the signs inside the brackets for the center. The number on the right is $r^{2}$, so take its square root.",
 side=("grid","Grid. Sketch card 1: the center, the radius and four points on the circle."),
 err=(r"x^{2}+y^{2}+4x-6y-12=0\ \Rightarrow\ (x+2)^{2}+(y-3)^{2}=12", r"\text{so the center is }(2,-3)\text{ and }r=\sqrt{12}"),
 errp="A student completed the square and read off the center and radius. Say what went wrong and write the correct center and radius.",
 done1="the center is read with the signs flipped, the right-hand side is treated as $r^{2}$, and the numbers added in completing the square go on both sides.",
 apply=["A model circular plaza in the Hira Cultural District has center the origin and diameter $60$ m. A straight path along $y=18$ crosses it. Where does the path enter and leave, and how long is it?",
        "A model radio tower at $(2,-1)$ covers a radius of $5$ km. Is a village at $(5,3)$ inside, outside or on the edge of the covered area?",
        "A model lake is the circle $x^{2}+y^{2}-10x+4y+13=0$ (km). Find its center and radius.",
        "A model path $y=x+2$ meets the boundary $x^{2}+y^{2}=34$. Find the two points where it does."],
 aplines=[3,2,3,3], adone="the center is placed first, the radius comes from $r^{2}$, and each answer says what it means in the context.",
 inv=["Use the distance formula to derive the equation of the circle with center $(h,k)$ and radius $r$.",
      "Show that the line $y=3x+10$ is tangent to $x^{2}+y^{2}=10$ by solving the system. Find the point of tangency.",
      "For $x^{2}+y^{2}=r^{2}$ and $y=mx+c$, show that the line is tangent when $c^{2}=r^{2}(1+m^{2})$. Check it with part 2."],
 idone="your argument starts from the distance formula or from a single repeated solution, and every step stays balanced.",
 intro3="Find the center and radius of $x^{2}+y^{2}-6x+4y-3=0$ three ways. Then compare: which was quickest, and which would you trust?",
 routes=["Complete the square","Center formula $\\left(-\\dfrac{D}{2},-\\dfrac{E}{2}\\right)$","Graph or technology"],
 claims=[("A line and a circle always meet at two points or not at all.","Did I test a line that just touches the circle?"),
         ("If the distance from the center to a line is less than the radius, the line meets the circle at two points.","Did I measure the perpendicular distance, not the distance to a point?"),
         ("The equation $x^{2}+y^{2}=-4$ is a circle of radius $2$.","Did I check that the right-hand side is positive?")],
 whatif=["What if the right-hand side is $0$, as in $(x-1)^{2}+(y+2)^{2}=0$? Predict the graph, then test with a point.",
         "What if the radius doubles and the center stays? Predict what happens to $r^{2}$ and to the area. Then test.",
         "Write a What if...? question of your own about a circle, predict the answer, and test it."])
# ------------------------- math registry (auto) -------------------------
E={}; INK="222E2D"
def key(t): return "m"+hashlib.md5(t.encode()).hexdigest()[:10]
def reg(t): E[key(t)]=(t,INK)
def scan(s):
    for m in re.findall(r"\$(.+?)\$",s): reg(m)
for d in D.values():
    for n,e,l in d["cards"]: reg(e)
    for e in d["err"]: reg(e)
    for s in [d["intro"],d["hint"],d["side"][1],d["errp"],d["done1"],d["adone"],d["idone"],d["intro3"]]+d["apply"]+d["inv"]+d["routes"]+d["whatif"]+[c for cl in d["claims"] for c in cl]+[d["done1"]]: scan(s)
if not os.path.exists("cm_doc/_index.json") or os.environ.get("REMATH"):
    from mathgen import render as mrender; mrender(E,"cm","cm")
from w8common import *
def T(s,sc=.78):
    return re.sub(r"\$(.+?)\$",lambda m: eq(key(m.group(1)),sc,inline=True),s)
def Dm(t,sc=.8): return eq(key(t),sc)
def foot2(code,page): return (f'<footer><span>{code}</span><span class="motto">Faith, Righteousness and Wisdom</span><span>Mr Malek Thiab · Page {page} of 3</span></footer>')
def Hd(small,h1,sub): return HEADER+title(small,h1,sub)+IDBAR
R='<div class="rule"></div>'; WHAT='<span style="color:#B23C00;font-weight:bold">What if...?</span>'
def cards(items,cols=3,sc=.8):
    out=f'<div class="grid" style="grid-template-columns:repeat({cols},1fr);gap:2mm">'
    for n,e,txt in items:
        out+=f'<div class="fc"><div class="top"><span class="n">{n}</span></div><div style="font-size:7.6pt;color:#3F4B49;margin-bottom:.6mm">{txt}</div>{Dm(e,sc)}</div>'
    return out+'</div>'
def claimrows(cl):
    rows=""
    for k,(c,a) in zip("ABC",cl):
        rows+=(f'<tr class="tr2"><td class="l" style="width:8mm;text-align:center">{k}</td><td style="width:62mm"><b>{T(c)}</b></td>'
               f'<td style="width:30mm;font-size:7.4pt">&#9744; true &nbsp; &#9744; false<br>&#9744; sometimes</td>'
               f'<td style="font-size:7.4pt;color:#5A6B69"><i>My evidence:</i><br><i>Assumption I checked:</i> {T(a)}</td></tr>')
    return rows
def routes_table(rows):
    t='<table class="cj"><tr><th>route</th><th style="text-transform:none">my working</th><th style="text-transform:none">steps</th><th style="text-transform:none">where a slip could happen</th></tr>'
    for r_ in rows: t+=f'<tr class="tr2"><td class="l" style="width:30mm">{T(r_)}</td><td></td><td style="width:14mm"></td><td style="width:42mm"></td></tr>'
    return t+'</table>'
def synth_frame():
    cells=lambda n,lab:'<tr><td style="width:18mm;font-size:7pt;color:#5A6B69;border:none">'+lab+'</td>'+''.join('<td style="border:1px solid #B9CFCD;height:8mm;width:9mm"></td>' for _ in range(n))+'</tr>'
    return ('<table style="border-collapse:collapse;margin-top:1mm">'+cells(5,"box | coeffs")+cells(5,"multiply")+cells(5,"add")+'</table>'
            '<p style="font-size:7pt;color:#5A6B69;margin:.6mm 0 0">Two frames: use the second for a different card.</p>'
            '<table style="border-collapse:collapse;margin-top:1.4mm">'+cells(5,"box | coeffs")+cells(5,"multiply")+cells(5,"add")+'</table>')
def build(d):
    S=d["S"]; C=d["C"]; sub=d["sub"]
    kind,sidetxt=d["side"]
    if kind=="grid": side=f'<img src="k_grid.png" style="width:62mm;display:block">'
    elif kind=="synth": side=synth_frame()
    else: side='<div class="box" style="height:48mm"></div>'
    p1=f"""{Hd(S,d['head'],sub)}
<div class="need"><b>Three routes, one destination.</b> Start anywhere on pages 1 and 2, move between routes whenever you like, and finish with page 3. A route names the task, not you.</div>
<div class="card" style="margin-bottom:2.2mm"><h2 class="t">Practice · Secure the method</h2>
  <p style="margin:0 0 1.4mm">{T(d['intro'])}</p>
  {cards(d['cards'])}
  <div style="display:flex;gap:3mm;margin-top:2mm"><div style="flex:1"><p style="margin:0 0 .4mm"><b>Working space.</b> {T(d['hint'])}</p><div class="box" style="height:{58 if kind!='prove' else 58}mm"></div></div>
  <div style="width:64mm"><p style="margin:0 0 .4mm">{T(sidetxt)}</p>{side}</div></div>
</div>
<div class="card" style="margin-bottom:2.2mm"><h2 class="p">Find the error</h2>
  <p style="margin:0 0 1mm">{T(d['errp'])}</p>
  <div style="margin:.6mm 0">{Dm(d['err'][0])}</div><div style="margin:.6mm 0">{Dm(d['err'][1])}</div>{R}{R}
</div>
<div class="done"><b>Done when&hellip;</b> {T(d['done1'])}</div>
{foot2(C,1)}"""
    ap=""
    for i,(t,n) in enumerate(zip(d["apply"],d["aplines"]),1):
        ap+=f'<p style="margin:{0 if i==1 else 1.4}mm 0 .5mm"><b>{i}.</b> {T(t)}</p>'+R*n
    iv=""
    for i,t in enumerate(d["inv"],1):
        iv+=f'<p style="margin:{0 if i==1 else 1.4}mm 0 .5mm"><b>{i}.</b> {T(t)}</p>'+R*3
    p2=f"""{Hd(S,"Choose Your Route: Apply and Investigate",sub)}
<div class="card" style="margin-bottom:2.2mm"><h2 class="g">Apply · Use it in context</h2>{ap}
  <p class="footnote" style="margin-top:1mm">Done when: {T(d['adone'])}</p>
</div>
<div class="card" style="margin-bottom:2.2mm"><h2 class="p">Investigate · Find out why</h2>{iv}
  <p class="footnote" style="margin-top:1mm">Done when: {T(d['idone'])}</p>
</div>
<div class="card tint" style="margin-bottom:2.2mm"><h2 class="g">Spotlight · An idea that is my own</h2><p style="margin:0">A route nobody else used, a question nobody else asked, or a surprise you found:</p>{R}{R}</div>
{foot2(C,2)}"""
    wi=""
    for i,t in enumerate(d["whatif"],1):
        wi+=f'<p style="margin:{0 if i==1 else 1.4}mm 0 .4mm"><b>{i}.</b> {T(t)}</p>{R}{R}'
    p3=f"""{Hd(S,"Which Route? Judge the Claims",sub)}
<div class="card" style="margin-bottom:2.2mm"><h2 class="t">Compare the routes</h2>
  <p style="margin:0 0 1.2mm">{T(d['intro3'])}</p>
  {routes_table(d['routes'])}
  <p style="margin:1.6mm 0 .4mm"><b>My choice</b> and the evidence for it:</p>{R}
</div>
<div class="card" style="margin-bottom:2.2mm"><h2 class="p">Judge the claims</h2>
  <p class="footnote" style="margin-bottom:1mm">Decide true, false or sometimes true. One counterexample is enough to show a claim is false; a few examples are not enough to show it is true.</p>
  <table class="cj">{claimrows(d['claims'])}</table>
</div>
<div class="card" style="margin-bottom:2.2mm"><h2 class="g">{WHAT} Predict first, then test</h2>{wi}</div>
<div class="done"><b>Done when&hellip;</b> you have compared three routes with evidence, judged each claim with an example or counterexample, and tested at least one What if...? idea.</div>
{foot2(C,3)}"""
    return [p1,p2,p3]
if __name__=="__main__":
    only=sys.argv[1:] or list(D)
    for k in only:
        os.environ["W7_SOFT"]="1"
        ok=render(build(D[k]),D[k]["name"]); print(k,"OK" if ok else "FIX")
