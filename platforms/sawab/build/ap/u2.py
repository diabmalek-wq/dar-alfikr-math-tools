from common import *
import math
# ---------- 2.1 sequences ----------
@reg('2.1')
def t(r):
    a1=r.randrange(-20,30); d=r.choice([-7,-5,-4,-3,3,4,6,9]); k=r.randrange(3,8); m=k+r.randrange(3,9); n=r.randrange(20,61)
    ak=a1+(k-1)*d; am=a1+(m-1)*d; an=a1+(n-1)*d
    q='An arithmetic sequence has $a_{%d}=%d$ and $a_{%d}=%d$. What is $a_{%d}$?'%(k,ak,m,am,n)
    c='$%d$'%an
    tr=[('$%d$'%(a1+n*d),'Off by one: $a_n=a_1+(n-1)d$, not $a_1+nd$.'),('$%d$'%(ak+(n-k)*(am-ak)),'Used $a_{%d}-a_{%d}$ as the common difference without dividing by the number of steps $%d$.'%(m,k,m-k)),('$%d$'%(an-d),'Counted one step too few from the known term.')]
    st=['$d=\\dfrac{%d-(%d)}{%d-%d}=%d$.'%(am,ak,m,k,d),'$a_{%d}=a_{%d}+(%d-%d)d=%d+%d(%d)=%d$.'%(n,k,n,k,ak,n-k,d,an)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('2.1')
def t(r):
    g0=r.choice([2,3,4,5,6,-3]); ratio=r.choice([2,3,-2,Fr(1,2),Fr(3,2),Fr(-1,2)]); n=r.randrange(4,8)
    gn=g0*ratio**(n-1)
    q='A geometric sequence has first term $g_{1}=%d$ and common ratio $%s$. What is $g_{%d}$?'%(g0,fx(ratio),n)
    c='$%s$'%fx(gn)
    tr=[('$%s$'%fx(g0*ratio**n),'Used exponent $n$; the formula is $g_n=g_1r^{\\,n-1}$.'),('$%s$'%fx(g0+(n-1)*ratio),'Added the ratio as if the sequence were arithmetic.'),('$%s$'%fx((g0*ratio)**(n-1)),'Raised the product $g_1r$ to the power instead of only $r$.')]
    st=['$g_n=g_1r^{\\,n-1}$.','$g_{%d}=%d\\left(%s\\right)^{%d}=%s$.'%(n,g0,fx(ratio),n-1,fx(gn))]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('2.1','Hard')
def t(r):
    g1=r.choice([2,3,5,4]); rr=r.choice([2,3]); k=r.randrange(2,4); n=k+r.randrange(3,5)
    gk=g1*rr**(k-1); gk2=g1*rr**(k+1); gn=g1*rr**(n-1)
    q='A geometric sequence with positive terms has $g_{%d}=%d$ and $g_{%d}=%d$. What is $g_{%d}$?'%(k,gk,k+2,gk2,n)
    c='$%d$'%gn
    tr=[('$%d$'%(gk*(rr*rr)**(n-k)),'Used $\\dfrac{g_{%d}}{g_{%d}}=%d$ as the ratio; it is $r^{2}$, two steps.'%(k+2,k,rr*rr)),('$%d$'%(gk+(n-k)*(gk2-gk)//2),'Treated the sequence as arithmetic.'),('$%d$'%(gn*rr),'Counted one step too many.')]
    st=['Two steps: $r^{2}=\\dfrac{%d}{%d}=%d$, so $r=%d$ (positive terms).'%(gk2,gk,rr*rr,rr),'$g_{%d}=%d\\cdot %d^{%d}=%d$.'%(n,gk,rr,n-k,gn)]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 2.2 linear vs exponential ----------
@reg('2.2')
def t(r):
    a=r.choice([2,3,5,6]); b=r.choice([2,3]); x1=r.randrange(1,3); x2=x1+2; x3=x2+1
    f=lambda x:a*b**x
    q='The function $f$ is exponential, with $f(%d)=%d$ and $f(%d)=%d$. What is $f(%d)$?'%(x1,f(x1),x2,f(x2),x3)
    c='$%d$'%f(x3)
    lin=f(x2)+(f(x2)-f(x1))//2
    tr=[('$%d$'%lin,'Assumed equal differences (linear); exponential functions have equal ratios.'),('$%d$'%(f(x2)*b*b),'Used $\\dfrac{f(%d)}{f(%d)}=%d$ as the one-step ratio; it covers two steps.'%(x2,x1,b*b)),('$%d$'%(f(x2)+b),'Added the ratio instead of multiplying by it.')]
    st=['Two steps multiply by $\\dfrac{%d}{%d}=%d$, so one step multiplies by $%d$.'%(f(x2),f(x1),b*b,b),'$f(%d)=%d\\cdot%d=%d$.'%(x3,f(x2),b,f(x3))]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('2.2')
def t(r):
    k=r.choice([2,3,4,5]); b=r.choice([2,3,5])
    q='For $g(x)=a\\cdot%d^{x}$ with $a\\ne0$, which expression is equal to $g(x+%d)$ for all $x$?'%(b,k)
    c='$%d\\,g(x)$'%(b**k)
    tr=[('$g(x)+%d$'%(b**k),'Exponential functions change by a constant factor, not a constant amount.'),('$%d\\,g(x)$'%(b*k),'Multiplied the base by the step; the factor over $%d$ steps is $%d^{%d}$.'%(k,b,k)),('$g(x)+%d$'%(k),'Linear thinking: adding to the input does not add to the output for an exponential.')]
    st=['$g(x+%d)=a\\cdot%d^{x+%d}=a\\cdot%d^{x}\\cdot%d^{%d}$.'%(k,b,k,b,b,k),'$=%d\\,g(x)$.'%(b**k)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('2.2')
def t(r):
    typ=r.choice(['lin','exp'])
    x=[0,1,2,3,4]
    if typ=='lin': m=r.choice([3,4,6,-5]); b=r.randrange(5,30); y=[b+m*i for i in x]
    else: a=r.choice([2,3,5]); bb=r.choice([2,3]); y=[a*bb**i for i in x]
    tab=', '.join('$(%d,%d)$'%p for p in zip(x,y))
    q='The points %s lie on the graph of a function. Which model fits, and why?'%tab
    L_='Linear, because the outputs change by a constant difference over equal input steps.'; E='Exponential, because the outputs change by a constant ratio over equal input steps.'
    c=L_ if typ=='lin' else E
    tr=[(E if typ=='lin' else L_,'Check differences (linear) and ratios (exponential) over equal input steps.'),
        ('Quadratic, because the second differences are constant.','Second differences of a linear table are $0$; for an exponential table they are not constant.'),
        ('Linear, because the outputs are increasing.' if typ=='exp' else ('Exponential, because the outputs are %s.'%('increasing' if y[-1]>y[0] else 'decreasing')),'The direction of change does not tell linear from exponential.')]
    st=['Differences: $%s$.'%',\\ '.join(str(y[i+1]-y[i]) for i in range(4)),'Ratios: $%s$.'%',\\ '.join(fx(Fr(y[i+1],y[i])) if y[i] else '-' for i in range(4)),c]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 2.3 exponential functions ----------
@reg('2.3')
def t(r):
    a=r.choice([-4,-3,-2,2,3,5]); b=r.choice([2,3,Fr(1,2),Fr(1,3),4]); k=r.randrange(-6,7)
    q='What is the range of $f(x)=%d\\left(%s\\right)^{x}%s$?'%(a,fx(b),term(k,0))
    c='$y>%d$'%k if a>0 else '$y<%d$'%k
    tr=[('$y<%d$'%k if a>0 else '$y>%d$'%k,'The sign of $a$ decides whether the graph lies above or below the asymptote $y=%d$.'%k),('$y>0$' if a>0 else '$y<0$','Forgot the vertical shift: the asymptote is $y=%d$.'%k),('All real numbers','Exponential functions are bounded on one side by their horizontal asymptote.')]
    if k==0: raise Bad
    st=['$%s^{x}>0$ for all $x$, so $%d\\left(%s\\right)^{x}$ is %s.'%('\\left('+fx(b)+'\\right)',a,fx(b),'positive' if a>0 else 'negative'),'Shifting by $%d$: range %s.'%(k,c)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('2.3','Hard')
def t(r):
    a=r.choice([-5,-3,-2,2,3,4]); b=r.choice([2,3,Fr(1,2),Fr(1,4),Fr(2,3)])
    grow=b>1; inc=(a>0)==grow; cu=a>0
    q='Which describes the graph of $f(x)=%d\\left(%s\\right)^{x}$?'%(a,fx(b))
    w=lambda i,c_:'%s and concave %s'%('Increasing' if i else 'Decreasing','up' if c_ else 'down')
    c=w(inc,cu)
    tr=[(w(not inc,cu),'With $a<0$ the reflection reverses increasing and decreasing.' if a<0 else 'Base $%s$ means %s.'%(fx(b),'growth' if grow else 'decay')),(w(inc,not cu),'Concavity follows the sign of $a$: $a>0$ concave up, $a<0$ concave down.'),(w(not inc,not cu),'Both the direction and the concavity are reversed.')]
    st=['$%s^{x}$ is %s and concave up.'%('\\left('+fx(b)+'\\right)','increasing' if grow else 'decreasing'),'Multiplying by $%d$ %s.'%(a,'keeps both' if a>0 else 'reflects over the $x$-axis: direction and concavity both reverse'),c+'.']
    return dict(q=q,c=c,tr=tr,st=st)

@reg('2.3')
def t(r):
    a=r.choice([2,3,4,-2,-3]); b=r.choice([2,3,5,Fr(1,2),Fr(1,3)]); k=r.choice([-5,-2,1,4,7])
    side=r.choice(['-\\infty','\\infty'])
    grow=b>1
    goes_to_k=(side=='-\\infty')==grow
    if goes_to_k: ans='%d'%k
    else: ans='\\infty' if a>0 else '-\\infty'
    q='Let $f(x)=%d\\left(%s\\right)^{x}%s$. What is $\\displaystyle\\lim_{x\\to%s}f(x)$?'%(a,fx(b),term(k,0),side)
    c='$%s$'%ans
    pool=['%d'%k,'\\infty','-\\infty','0','%d'%a]
    tr=[]
    for p in pool:
        if p!=ans and len(tr)<3:
            tr.append(('$%s$'%p,{'0':'Forgot the vertical shift $%d$.'%k,'%d'%a:'$a$ is the initial value $f(0)$ minus the shift, not a limit.','%d'%k:'The output approaches $y=%d$ only on the side where $b^{x}\\to0$.'%k}.get(p,'Check whether $b^{x}$ grows or shrinks on this side, then the sign of $a$.')))
    st=['As $x\\to%s$, $\\left(%s\\right)^{x}\\to%s$.'%(side,fx(b),'0' if goes_to_k else '\\infty'),'So $f(x)\\to %s$.'%ans]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 2.4 exponential manipulation ----------
@reg('2.4')
def t(r):
    b=r.choice([2,3,5]); p=r.choice([2,3]); m=r.randrange(1,4); c0=r.randrange(1,3)
    B=b**p
    q='Which expression is equivalent to $%d\\cdot%d^{x+%d}$?'%(b**c0,B,m)
    e=p*m+c0
    c='$%d^{%dx+%d}$'%(b,p,e)
    tr=[('$%d^{%dx+%d}$'%(b,p,p*m),'Dropped the extra factor $%d=%d^{%d}$.'%(b**c0,b,c0)),('$%d^{x+%d}$'%(b**c0*B,m),'Multiplied the coefficient into the base; $c\\cdot b^{x}\\ne(cb)^{x}$.'),('$%d^{%dx+%d}$'%(b,p,m+c0),'Did not distribute the exponent $%d$ over $x+%d$.'%(p,m))]
    st=['$%d=%d^{%d}$ and $%d=%d^{%d}$.'%(B,b,p,b**c0,b,c0),'$%d^{%d}\\cdot%d^{%d(x+%d)}=%d^{%dx+%d}$.'%(b,c0,b,p,m,b,p,e)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('2.4')
def t(r):
    a=r.choice([2,3,5,7]); b=r.choice([2,3,4,5])
    q='Which function is equivalent to $f(x)=%d\\left(\\dfrac{1}{%d}\\right)^{-x}$?'%(a,b)
    c='$f(x)=%d\\cdot%d^{x}$'%(a,b)
    tr=[('$f(x)=%d\\cdot%d^{-x}$'%(a,b),'The negative exponent flips the base; $\\left(\\frac{1}{b}\\right)^{-x}=b^{x}$.'),('$f(x)=-%d\\cdot%d^{x}$'%(a,b),'A negative exponent does not make the value negative.'),('$f(x)=%d^{x}$'%(a*b),'$a\\cdot b^{x}\\ne(ab)^{x}$.')]
    st=['$\\left(\\dfrac{1}{%d}\\right)^{-x}=\\left(%d^{-1}\\right)^{-x}=%d^{x}$.'%(b,b,b),c]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('2.4','Hard')
def t(r):
    b=r.choice([2,3,5]); k=r.choice([2,3,-2,-1,4])
    q='The graph of $g(x)=%d^{x%s}$ is the image of $f(x)=%d^{x}$ after a horizontal translation. It is also the image of $f$ after which vertical dilation?'%(b,term(k,0),b)
    v=Fr(b)**k
    c='A vertical dilation by a factor of $%s$'%fx(v)
    tr=[('A vertical dilation by a factor of $%d$'%k,'$b^{x+k}=b^{k}\\cdot b^{x}$; the factor is $b^{k}$, not $k$.'),('A vertical dilation by a factor of $%s$'%fx(1/v),'Sign error in the exponent.'),('A vertical dilation by a factor of $%d$'%(b*k),'The factor is $b^{k}$, a power, not the product $bk$.')]
    if k==1 or k*b==b**k: raise Bad
    st=['$%d^{x%s}=%d^{%d}\\cdot%d^{x}$.'%(b,term(k,0),b,k,b),'$=%s\\cdot f(x)$: a vertical dilation by $%s$.'%(fx(v),fx(v))]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 2.5 exponential context ----------
@reg('2.5','Medium','Calculator')
def t(r):
    P=r.choice([1000,2500,4000,5000]); rate=r.choice([3,4,5,6]); n,nm=r.choice([(12,'monthly'),(4,'quarterly'),(2,'twice a year')]); T=r.choice([5,8,10])
    A=P*(1+rate/100/n)**(n*T)
    q='An investment of $%d$ dollars earns $%d\\%%$ annual interest compounded %s. To the nearest dollar, what is its value after $%d$ years?'%(P,rate,nm,T)
    c='$%s$ dollars'%format(round(A),',').replace(',','{,}')
    S=P*(1+rate/100*T); W=P*(1+rate/100)**(n*T); Y=P*(1+rate/100)**T
    f=lambda v:'$%s$ dollars'%format(round(v),',').replace(',','{,}')
    tr=[(f(S),'Used simple interest, $P(1+rt)$, instead of compounding.'),(f(W),'Did not divide the annual rate by the number of compoundings.'),(f(Y),'Compounded once a year instead of %s.'%nm)]
    st=['$A=P\\left(1+\\dfrac{r}{n}\\right)^{nt}=%d\\left(1+\\dfrac{%s}{%d}\\right)^{%d}$.'%(P,('%.2f'%(rate/100)),n,n*T),'$A\\approx %d$.'%round(A)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('2.5','Medium','Calculator')
def t(r):
    A0=r.choice([80,120,200,500]); h=r.choice([4,5,6,8]); k=r.choice([2,3,4]); T=h*k
    q='A substance has a half-life of $%d$ hours. A sample starts with $%d$ grams. How many grams remain after $%d$ hours?'%(h,A0,T)
    v=Fr(A0,2**k)
    c='$%s$ g'%fx(v)
    tr=[('$%s$ g'%fx(Fr(A0,2*k)),'Halved and then divided by the number of half-lives; each half-life multiplies by $\\frac{1}{2}$ again.'),('$%s$ g'%fx(max(A0-Fr(A0,2)*k,Fr(A0,2**(k+1)))),'Subtracted half of the original amount each period (linear decay).'),('$%s$ g'%fx(Fr(A0,2**(k-1))),'Counted one half-life too few.')]
    st=['Number of half-lives: $\\dfrac{%d}{%d}=%d$.'%(T,h,k),'$%d\\left(\\dfrac{1}{2}\\right)^{%d}=%s$.'%(A0,k,fx(v))]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('2.5')
def t(r):
    V=r.choice([1200,5000,24000,800]); p=r.choice([3,6,8,12,15]); grow=r.random()<.5
    word='increases' if grow else 'decreases'
    q='A quantity starts at $%d$ and %s by $%d\\%%$ each year. Which function gives its value after $t$ years?'%(V,word,p)
    g=1+p/100 if grow else 1-p/100
    ff=lambda x:('%.2f'%x).rstrip('0').rstrip('.')
    c='$%d(%s)^{t}$'%(V,ff(g))
    tr=[('$%d(%s)^{t}$'%(V,ff(p/100)),'Used the percent itself as the base; the growth factor is $1%s%s$.'%('+' if grow else '-',ff(p/100))),('$%d(%s)^{t}$'%(V,ff(1-p/100 if grow else 1+p/100)),'Used the factor for the opposite direction of change.'),('$%d%s%dt$'%(V,'+' if grow else '-',V*p//100),'A constant percent change is exponential, not linear.')]
    st=['Each year the value is multiplied by $1%s%s=%s$.'%('+' if grow else '-',ff(p/100),ff(g)),c]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 2.6 competing models ----------
@reg('2.6','Medium','Calculator')
def t(r):
    m=r.choice([1.5,2.4,3.2,-1.8]); b=r.choice([12,20,35]); x=r.randrange(3,12); res=r.choice([-4.2,-2.6,1.8,3.4,5.1])
    pred=m*x+b; act=pred+res
    q='A linear model $\\hat{y}=%sx+%d$ is fitted to data. The data point $(%d,\\,%s)$ is in the set. What is its residual, and what does it show?'%(m,b,x,('%.1f'%act))
    f=lambda v:('%.1f'%v)
    c='Residual $%s$; the model %s this value.'%(f(res),'underestimates' if res>0 else 'overestimates')
    tr=[('Residual $%s$; the model %s this value.'%(f(-res),'overestimates' if res>0 else 'underestimates'),'Residual $=$ actual $-$ predicted, not predicted $-$ actual.'),
        ('Residual $%s$; the model %s this value.'%(f(res),'overestimates' if res>0 else 'underestimates'),'A positive residual means the actual value is above the model (underestimate).'),
        ('Residual $%s$; the model fits this value exactly.'%f(pred),'Reported the predicted value, not the residual.')]
    st=['Predicted: $%s(%d)+%d=%s$.'%(m,x,b,f(pred)),'Residual $=%s-%s=%s$.'%(f(act),f(pred),f(res)),'%s residual: the model %s.'%('Positive' if res>0 else 'Negative','underestimates' if res>0 else 'overestimates')]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('2.6')
def t(r):
    typ=r.choice(['lin','quad','exp'])
    x=[1,2,3,4,5]
    if typ=='lin': y=[7+4*i for i in x]
    elif typ=='quad': a=r.choice([1,2,3]); y=[a*i*i+r.randrange(-3,4)*i+5 for i in x]
    else: y=[3*2**i for i in x]
    q='Which model is most appropriate for the data $%s$ at $x=1,2,3,4,5$?'%(',\\ '.join(map(str,y)))
    opts={'lin':'Linear: constant first differences','quad':'Quadratic: constant second differences','exp':'Exponential: constant ratios of consecutive outputs'}
    c=opts[typ]
    tr=[(v,'Compute first differences, second differences and ratios, then choose the one that is constant.') for k,v in opts.items() if k!=typ]
    tr.append(('Cubic: constant third differences','The first row that is constant decides the model; a constant lower row comes first.'))
    tr=tr[:3]
    d1=[y[i+1]-y[i] for i in range(4)]; d2=[d1[i+1]-d1[i] for i in range(3)]
    st=['First differences: $%s$.'%',\\ '.join(map(str,d1)),'Second differences: $%s$.'%',\\ '.join(map(str,d2)),'Ratios: $%s$.'%',\\ '.join(fx(Fr(y[i+1],y[i])) for i in range(4)),c+'.']
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 2.7 composition ----------
@reg('2.7')
def t(r):
    a=r.choice([1,2,3]); b=r.randrange(-6,7); m=r.choice([2,3,-2,4]); k=r.randrange(-5,6); x0=r.randrange(-3,4)
    f=lambda x:a*x*x+b; g=lambda x:m*x+k
    q='Let $f(x)=%s$ and $g(x)=%s$. What is $f(g(%d))$?'%(poly([(a,2),(b,0)]),lin(m,k),x0)
    c='$%d$'%f(g(x0))
    tr=[('$%d$'%g(f(x0)),'Computed $g(f(%d))$; the inner function $g$ is applied first.'%x0),('$%d$'%(f(x0)*g(x0)),'Multiplied $f(%d)$ and $g(%d)$; composition is not multiplication.'%(x0,x0)),('$%d$'%(f(x0)+g(x0)),'Added the outputs instead of composing.')]
    st=['$g(%d)=%d$.'%(x0,g(x0)),'$f(%d)=%d$.'%(g(x0),f(g(x0)))]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('2.7')
def t(r):
    xs=[1,2,3,4,5]; fv=r.sample(range(1,6),5); gv=r.sample(range(1,6),5)
    x0=r.choice(xs); F=dict(zip(xs,fv)); G=dict(zip(xs,gv))
    q='Tables: $f(1),\\dots,f(5)=%s$ and $g(1),\\dots,g(5)=%s$. What is $(f\\circ g)(%d)$?'%(',\\ '.join(map(str,fv)),',\\ '.join(map(str,gv)),x0)
    ans=F[G[x0]]
    c='$%d$'%ans
    cand=[(G[F[x0]],'Applied $f$ first; in $(f\\circ g)(x)=f(g(x))$, $g$ acts first.'),(F[x0],'Read $f$ at the original input, skipping $g$.'),(G[x0],'Stopped after the inner function.'),(F[x0]*G[x0],'Multiplied the outputs.')]
    tr=[];seen={ans}
    for v,w in cand:
        if v not in seen and len(tr)<3: tr.append(('$%d$'%v,w)); seen.add(v)
    if len(tr)<3: raise Bad
    st=['$g(%d)=%d$.'%(x0,G[x0]),'$f(%d)=%d$.'%(G[x0],ans)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('2.7')
def t(r):
    a=r.randrange(-5,6); b=r.randrange(1,8); 
    if a==0: raise Bad
    q='Let $f(x)=x^{2}+%d$ and $g(x)=%s$. Which expression is $f(g(x))$?'%(b,lin(1,a))
    c='$%s$'%poly([(1,2),(2*a,1),(a*a+b,0)])
    tr=[('$%s$'%poly([(1,2),(a+b,0)]),'Computed $g(f(x))$.'),('$%s$'%poly([(1,2),(a*a+b,0)]),'Expanded $(x%s)^{2}$ as $x^{2}+%d$: the middle term $%dx$ is missing.'%(term(a,0),a*a,2*a)),('$%s$'%poly([(1,3),(a,2),(b,1),(a*b,0)]),'Multiplied $f(x)\\cdot g(x)$.')]
    st=['$f(g(x))=(x%s)^{2}+%d$.'%(term(a,0),b),'$=%s$.'%poly([(1,2),(2*a,1),(a*a+b,0)])]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 2.8 inverse functions ----------
@reg('2.8')
def t(r):
    m=r.choice([2,3,4,5,-2,-3]); k=r.randrange(-9,10)
    if k==0: raise Bad
    q='What is the inverse of $f(x)=%s$?'%lin(m,k)
    c='$f^{-1}(x)=\\dfrac{x%s}{%d}$'%(term(-k,0),m)
    tr=[('$f^{-1}(x)=\\dfrac{x%s}{%d}$'%(term(k,0),m),'Undid the operations but kept the sign of the constant.'),('$f^{-1}(x)=\\dfrac{1}{%s}$'%lin(m,k),'The reciprocal $\\frac{1}{f(x)}$ is not the inverse function.'),('$f^{-1}(x)=\\dfrac{x}{%d}%s$'%(m,term(-k,0)),'Undid the operations in the wrong order: subtract first, then divide.')]
    st=['Swap: $x=%s$.'%lin(m,k,'y'),'Solve: $y=\\dfrac{x%s}{%d}$.'%(term(-k,0),m)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('2.8')
def t(r):
    xs=r.sample(range(-6,10),5); ys=r.sample(range(-6,12),5)
    i=r.randrange(5); F=dict(zip(xs,ys)); 
    q='The table gives $f(%s)=%s$, respectively. What is $f^{-1}(%d)$?'%(',\\,'.join(map(str,xs)),',\\,'.join(map(str,ys)),ys[i])
    c='$%d$'%xs[i]
    alt=F.get(ys[i])
    tr=[('$%d$'%alt if alt is not None and alt!=xs[i] else '$\\dfrac{1}{%d}$'%ys[i],'Evaluated $f(%d)$ instead of finding the input whose output is $%d$.'%(ys[i],ys[i])),('$%s$'%fx(Fr(1,ys[i])) if ys[i] not in (0,) else '$0$','$f^{-1}$ is not the reciprocal $\\frac{1}{f}$.'),('$%d$'%ys[(i+1)%5],'Read the wrong row of the table.')]
    if ys[i] in (0,1,-1): raise Bad
    st=['$f^{-1}(%d)$ is the input $x$ with $f(x)=%d$.'%(ys[i],ys[i]),'From the table, $f(%d)=%d$, so $f^{-1}(%d)=%d$.'%(xs[i],ys[i],ys[i],xs[i])]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('2.8')
def t(r):
    h=r.choice([x for x in range(-6,7) if x]); k=r.choice([x for x in range(-6,7) if x and x!=h])
    q='For $f(x)=%s^{2}%s$, on which domain is $f$ invertible and includes all inputs to the right of the vertex?'%(fac(h),term(k,0))
    c='$x\\ge %d$'%h
    tr=[('$x\\ge %d$'%k,'Used the $y$-coordinate of the vertex; the restriction is on inputs.'),('$x\\ge %d$'%(-h),'Sign error reading the vertex from $%s^{2}$.'%fac(h)),('All real numbers','A parabola fails the horizontal line test on all reals.')]
    st=['Vertex at $(%d,%d)$.'%(h,k),'$f$ is increasing for $x\\ge %d$, so it is one-to-one there.'%h]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 2.9 log expressions ----------
@reg('2.9')
def t(r):
    base,arg,val=pick(r,[(8,2,Fr(1,3)),(27,3,Fr(1,3)),(16,4,Fr(1,2)),(4,8,Fr(3,2)),(9,27,Fr(3,2)),(Fr(1,3),9,-2),(Fr(1,2),8,-3),(25,Fr(1,5),Fr(-1,2)),(32,2,Fr(1,5)),(Fr(1,4),2,Fr(-1,2))])
    q='What is the value of $\\log_{%s}\\left(%s\\right)$?'%(fx(base),fx(arg))
    c='$%s$'%fx(val)
    tr=[('$%s$'%fx(1/val),'Inverted the answer: solve $%s^{y}=%s$ for $y$.'%('\\left('+fx(base)+'\\right)',fx(arg))),('$%s$'%fx(-val),'Sign error with the fractional base or argument.'),('$%s$'%fx(Fr(arg)/Fr(base)),'A logarithm is an exponent, not a quotient.')]
    st=['Let $y=\\log_{%s}\\left(%s\\right)$, so $\\left(%s\\right)^{y}=%s$.'%(fx(base),fx(arg),fx(base),fx(arg)),'Write both as powers of the same base: $y=%s$.'%fx(val)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('2.9')
def t(r):
    b=r.choice([2,3,5]); n=r.randrange(2,5); x=r.randrange(b**n+1,b**(n+1))
    q='Between which two consecutive integers is $\\log_{%d}%d$?'%(b,x)
    c='$%d$ and $%d$'%(n,n+1)
    tr=[('$%d$ and $%d$'%(n-1,n),'$%d^{%d}=%d<%d$, so the logarithm is greater than $%d$.'%(b,n,b**n,x,n)),('$%d$ and $%d$'%(n+1,n+2),'$%d^{%d}=%d>%d$, so the logarithm is less than $%d$.'%(b,n+1,b**(n+1),x,n+1)),('$%d$ and $%d$'%(x//b,x//b+1),'Divided by the base; a logarithm counts factors of the base.')]
    st=['$%d^{%d}=%d$ and $%d^{%d}=%d$.'%(b,n,b**n,b,n+1,b**(n+1)),'$%d<%d<%d$, so $%d<\\log_{%d}%d<%d$.'%(b**n,x,b**(n+1),n,b,x,n+1)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('2.9')
def t(r):
    b,y=pick(r,[(4,Fr(3,2)),(9,Fr(3,2)),(8,Fr(2,3)),(16,Fr(3,4)),(27,Fr(2,3)),(25,Fr(3,2))])
    xv=sp.Integer(b)**sp.Rational(y.numerator,y.denominator)
    q='If $\\log_{%d}x=%s$, what is $x$?'%(b,fx(y))
    c='$%s$'%sx(xv)
    tr=[('$%s$'%fx(b*y),'Multiplied the base by the logarithm; the logarithm is the exponent.'),('$%s$'%sx(sp.Integer(b)**sp.Rational(y.denominator,y.numerator)),'Used the reciprocal exponent.'),('$%s$'%sx(sp.Rational(y.numerator,y.denominator)**b),'Swapped the base and the exponent.')]
    st=['$\\log_{%d}x=%s$ means $x=%d^{%s}$.'%(b,fx(y),b,fx(y)),'$x=%s$.'%sx(xv)]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 2.10 inverses of exponentials ----------
@reg('2.10')
def t(r):
    b=r.choice([2,3,5,10]); n=r.randrange(1,4)
    q='The point $(%d,\\,%d)$ lies on the graph of $f(x)=%d^{x}$. Which point must lie on the graph of $f^{-1}(x)=\\log_{%d}x$?'%(n,b**n,b,b)
    c='$(%d,\\,%d)$'%(b**n,n)
    tr=[('$(%d,\\,%d)$'%(n,b**n),'This point is on $f$; the inverse swaps the coordinates.'),('$(%d,\\,%s)$'%(-n,fx(Fr(1,b**n))),'This point is also on $f$, not on its inverse.'),('$(%s,\\,%d)$'%(fx(Fr(1,b**n)),n),'Took the reciprocal of the output instead of swapping.')]
    st=['Inverse functions swap inputs and outputs.','$(%d,%d)$ on $f$ gives $(%d,%d)$ on $f^{-1}$, since $\\log_{%d}%d=%d$.'%(n,b**n,b**n,n,b,b**n,n)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('2.10')
def t(r):
    a=r.choice([2,3,4,5]); b=r.choice([2,3,10]); 
    q='What is the inverse of $f(x)=%d\\cdot%d^{x}$?'%(a,b)
    c='$f^{-1}(x)=\\log_{%d}\\left(\\dfrac{x}{%d}\\right)$'%(b,a)
    tr=[('$f^{-1}(x)=\\dfrac{\\log_{%d}x}{%d}$'%(b,a),'Divide before taking the logarithm: $\\dfrac{x}{%d}=%d^{y}$.'%(a,b)),('$f^{-1}(x)=%d\\log_{%d}x$'%(a,b),'Kept the coefficient as a multiplier; it must be undone first.'),('$f^{-1}(x)=\\log_{%d}x-%d$'%(b,a),'Subtracted instead of dividing; $%d$ multiplies the power.'%a)]
    st=['Swap: $x=%d\\cdot%d^{y}$.'%(a,b),'$\\dfrac{x}{%d}=%d^{y}$, so $y=\\log_{%d}\\left(\\dfrac{x}{%d}\\right)$.'%(a,b,b,a)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('2.10')
def t(r):
    b=r.choice([2,3,5]); k=r.choice([-4,-3,-2,2,3,5])
    q='What is the inverse of $g(x)=\\log_{%d}x%s$?'%(b,term(k,0))
    c='$g^{-1}(x)=%d^{x%s}$'%(b,term(-k,0))
    tr=[('$g^{-1}(x)=%d^{x}%s$'%(b,term(-k,0)),'Subtract $%d$ before exponentiating, inside the exponent.'%k),('$g^{-1}(x)=%d^{x%s}$'%(b,term(k,0)),'Sign error: undo $%s$ by %s.'%(term(k,0),'subtracting' if k>0 else 'adding')),('$g^{-1}(x)=x^{%d}%s$'%(b,term(-k,0)),'The inverse of $\\log_{b}$ is $b^{x}$, not $x^{b}$.')]
    st=['Swap: $x=\\log_{%d}y%s$, so $x%s=\\log_{%d}y$.'%(b,term(k,0),term(-k,0),b),'$y=%d^{x%s}$.'%(b,term(-k,0))]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 2.11 log functions ----------
@reg('2.11')
def t(r):
    a=r.choice([2,3,4,5]); cc=r.choice([x for x in range(-12,13) if x and x%a])
    q='What is the domain of $f(x)=\\ln(%s)$?'%lin(a,-cc)
    v=Fr(cc,a)
    c='$x>%s$'%fx(v)
    tr=[('$x\\ge %s$'%fx(v),'$\\ln 0$ is undefined, so the endpoint is excluded.'),('$x>%s$'%fx(-v),'Sign error when solving $%s>0$.'%lin(a,-cc)),('$x>%d$'%cc,'Forgot to divide by $%d$.'%a)]
    st=['The argument must be positive: $%s>0$.'%lin(a,-cc),'$x>%s$.'%fx(v)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('2.11')
def t(r):
    a=r.choice([-3,-2,2,3,4]); h=r.choice([x for x in range(-7,8) if x]); k=r.choice([x for x in range(-7,8) if x and x!=h and x!=-h])
    b=r.choice([2,3,10])
    q='Which describes the asymptote of the graph of $f(x)=%d\\log_{%d}%s%s$?'%(a,b,fac(h),term(k,0))
    c='Vertical asymptote $x=%d$'%h
    tr=[('Vertical asymptote $x=%d$'%(-h),'Sign error: $(x-h)$ is zero at $x=h$.'),('Horizontal asymptote $y=%d$'%k,'Logarithmic functions have a vertical asymptote; $k$ only shifts the graph vertically.'),('Vertical asymptote $x=%d$'%k,'Used the vertical shift as the asymptote.')]
    st=['$\\log_{%d}%s$ is defined for $x>%d$.'%(b,fac(h),h),'As $x\\to%d^{+}$ the output is unbounded: vertical asymptote $x=%d$.'%(h,h)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('2.11','Hard')
def t(r):
    a=r.choice([-3,-2,2,3]); h=r.choice([-4,-1,1,3,5]); b=r.choice([2,Fr(1,2),3,Fr(1,3)])
    grow=Fr(b)>1
    ans='-\\infty' if (grow==(a>0)) else '\\infty'
    q='Let $f(x)=%d\\log_{%s}%s$. What is $\\displaystyle\\lim_{x\\to%d^{+}}f(x)$?'%(a,fx(b),fac(h),h)
    opp='\\infty' if ans=='-\\infty' else '-\\infty'
    c='$%s$'%ans
    tr=[('$%s$'%opp,'Near the asymptote, $\\log_{%s}$ of a tiny positive number is %s; then apply the sign of $%d$.'%(fx(b),'very negative' if grow else 'very positive',a)),('$0$','The graph is near the vertical asymptote, so the output is unbounded.'),('$%d$'%h,'Gave the input value, not the limit of the output.')]
    st=['As $x\\to%d^{+}$, the argument $\\to0^{+}$.'%h,'$\\log_{%s}(0^{+})=%s$.'%(fx(b),'-\\infty' if grow else '\\infty'),'Multiply by $%d$: $%s$.'%(a,ans)]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 2.12 log manipulation ----------
@reg('2.12')
def t(r):
    b=r.choice([2,3]); p=r.randrange(2,5); m=r.randrange(2,5); n=r.randrange(2,4)
    q='Which is equivalent to $\\log_{%d}\\left(\\dfrac{%d\\,x^{%d}}{y^{%d}}\\right)$ for $x,y>0$?'%(b,b**p,m,n)
    c='$%d+%d\\log_{%d}x-%d\\log_{%d}y$'%(p,m,b,n,b)
    tr=[('$%d+%d\\log_{%d}x-%d\\log_{%d}y$'%(b**p,m,b,n,b),'$\\log_{%d}%d=%d$, not $%d$.'%(b,b**p,p,b**p)),('$%d+%d\\log_{%d}x+%d\\log_{%d}y$'%(p,m,b,n,b),'Division becomes subtraction of logarithms.'),('$%d\\cdot%d\\log_{%d}x-%d\\log_{%d}y$'%(p,m,b,n,b),'Product inside becomes a sum of logarithms, not a product.')]
    st=['Quotient: $\\log(%dx^{%d})-\\log(y^{%d})$.'%(b**p,m,n),'Product and power: $%d+%d\\log_{%d}x-%d\\log_{%d}y$.'%(p,m,b,n,b)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('2.12')
def t(r):
    a,bb,cc=r.choice([2,3]),r.choice([2,3,4]),r.choice([1,2])
    q='Which is equivalent to $%d\\ln x-%d\\ln y+%s\\ln z$ for positive $x,y,z$?'%(a,bb,'' if cc==1 else str(cc))
    zz='z' if cc==1 else 'z^{%d}'%cc
    c='$\\ln\\left(\\dfrac{x^{%d}%s}{y^{%d}}\\right)$'%(a,zz,bb)
    tr=[('$\\ln\\left(\\dfrac{%dx\\,%s}{%dy}\\right)$'%(a,zz,bb),'Coefficients become exponents, not factors.'),('$\\ln\\left(x^{%d}y^{%d}%s\\right)$'%(a,bb,zz),'The subtracted term goes in the denominator.'),('$\\dfrac{\\ln(x^{%d}%s)}{\\ln(y^{%d})}$'%(a,zz,bb),'A difference of logarithms is the log of a quotient, not a quotient of logs.')]
    st=['Power property: $\\ln x^{%d}-\\ln y^{%d}+\\ln %s$.'%(a,bb,zz),'Product and quotient: %s.'%c]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('2.12','Hard')
def t(r):
    b=r.choice([2,3,5]); k=r.randrange(2,5)
    q='The function $g(x)=\\log_{%d}(%dx)$. Which expression is equivalent to $g(x)$, showing $g$ as a transformation of $f(x)=\\log_{%d}x$?'%(b,b**k,b)
    c='$g(x)=\\log_{%d}x+%d$, a vertical translation up $%d$'%(b,k,k)
    tr=[('$g(x)=%d\\log_{%d}x$, a vertical dilation by $%d$'%(b**k,b,b**k),'$\\log(ab)=\\log a+\\log b$, a sum, not a product.'),('$g(x)=\\log_{%d}x+%d$, a vertical translation up $%d$'%(b,b**k,b**k),'$\\log_{%d}%d=%d$, not $%d$.'%(b,b**k,k,b**k)),('$g(x)=\\log_{%d}(x+%d)$, a horizontal translation'%(b,b**k),'A factor inside the logarithm is not an added term.')]
    st=['$\\log_{%d}(%dx)=\\log_{%d}%d+\\log_{%d}x$.'%(b,b**k,b,b**k,b),'$=%d+\\log_{%d}x$: a vertical translation up $%d$.'%(k,b,k)]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 2.13 equations ----------
@reg('2.13')
def t(r):
    a=r.choice([2,3,4,5]); b=r.choice([2,3]); x0=r.randrange(2,5)
    rhs=a*b**x0
    q='Solve $%d\\cdot%d^{x}=%d$.'%(a,b,rhs)
    c='$x=%d$'%x0
    tr=[('$x=\\log_{%d}%d$'%(b,rhs-a),'Subtracted $%d$ instead of dividing by it.'%a),('$x=%d$'%(b**x0),'Divided correctly but reported $%d^{x}$ instead of $x$.'%b),('$x=%s$'%fx(Fr(rhs,a*b)),'Divided by the base instead of taking a logarithm.')]
    st=['$%d^{x}=\\dfrac{%d}{%d}=%d$.'%(b,rhs,a,b**x0),'$x=\\log_{%d}%d=%d$.'%(b,b**x0,x0)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('2.13','Hard')
def t(r):
    b=r.choice([2,3]); n=r.choice([2,3,4]) if b==2 else 2; N=b**n
    # (x+p)(x+q)=N with root x0 valid
    fs=[(d,N//d) for d in range(1,N+1) if N%d==0]
    d1,d2=r.choice(fs)
    if d1==d2: raise Bad
    x0=r.randrange(1,6); p=d1-x0; q2=d2-x0
    # other root: x^2+(p+q)x+pq-N=0, sum = -(p+q)
    x1=-(p+q2)-x0
    if x1+p>0 and x1+q2>0: raise Bad
    q='Solve $\\log_{%d}%s+\\log_{%d}%s=%d$.'%(b,'(x%s)'%term(p,0) if p else 'x',b,'(x%s)'%term(q2,0) if q2 else 'x',n)
    c='$x=%d$ only'%x0
    tr=[('$x=%d$ or $x=%d$'%(x0,x1),'Check each solution: $x=%d$ makes an argument of a logarithm $\\le0$.'%x1),('$x=%d$ only'%x1,'Kept the extraneous root and dropped the valid one.'),('$x=%s$'%fx(Fr(N-p-q2,2)),'Wrote $\\log A+\\log B=\\log(A+B)$; the sum of logarithms is the log of a product.')]
    st=['$\\log_{%d}[(x%s)(x%s)]=%d$, so $(x%s)(x%s)=%d$.'%(b,term(p,0),term(q2,0),n,term(p,0),term(q2,0),N),'Solutions of the quadratic: $x=%d$ and $x=%d$.'%(x0,x1),'Only $x=%d$ keeps both arguments positive.'%x0]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('2.13','Hard')
def t(r):
    a=r.choice([2,3,4,5,6]); c0=r.choice([1,2,3,4]); 
    if a==c0: raise Bad
    # (u-a)(u+c0)=u^2+(c0-a)u - a c0
    q='What are all real solutions of $e^{2x}%se^{x}%s=0$?'%(term(c0-a,0) if c0-a not in (1,-1) else ('+' if c0-a==1 else '-'),term(-a*c0,0))
    if c0-a==0: raise Bad
    c='$x=\\ln %d$ only'%a
    tr=[('$x=\\ln %d$ or $x=\\ln(-%d)$'%(a,c0),'$e^{x}>0$, so $e^{x}=-%d$ has no solution.'%c0),('$x=%d$'%a,'Solved for $u=e^{x}$ but did not take the logarithm.'),('$x=\\ln %d$'%(a-c0 if a-c0>0 and a-c0!=a else a+c0),'Used the sum (or difference) of the roots instead of factoring.')]
    st=['Let $u=e^{x}$: $u^{2}%su%s=0$.'%(term(c0-a,0) if abs(c0-a)!=1 else ('+' if c0-a==1 else '-'),term(-a*c0,0)),'$(u-%d)(u+%d)=0$, so $u=%d$ or $u=-%d$.'%(a,c0,a,c0),'$e^{x}=%d$ gives $x=\\ln %d$; $e^{x}=-%d$ is impossible.'%(a,a,c0)]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 2.14 log context ----------
@reg('2.14')
def t(r):
    p1=r.randrange(2,6); d=r.choice([1,2,3]); p2=p1+d
    q='The pH of a solution is $\\text{pH}=-\\log[\\text{H}^{+}]$. Solution A has pH $%d$ and solution B has pH $%d$. How many times greater is $[\\text{H}^{+}]$ in A than in B?'%(p1,p2)
    c='$%d$'%(10**d)
    tr=[('$%d$'%d,'A difference of $%d$ on a log scale is a factor of $10^{%d}$.'%(d,d)),('$%s$'%fx(Fr(p2,p1)),'Divided the pH values; the scale is logarithmic.'),('$%d$'%(10*d),'Multiplied $10$ by the difference instead of raising $10$ to it.')]
    if 10*d==10**d: tr[2]=('$%s$'%fx(Fr(1,10**d)),'Inverted the comparison: lower pH means more hydrogen ions.')
    st=['$[\\text{H}^{+}]=10^{-\\text{pH}}$.','$\\dfrac{10^{-%d}}{10^{-%d}}=10^{%d}=%d$.'%(p1,p2,d,10**d)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('2.14')
def t(r):
    dL=r.choice([10,20,30,40])
    q='Sound level is $L=10\\log\\left(\\dfrac{I}{I_{0}}\\right)$ decibels. If the level rises by $%d$ dB, by what factor does the intensity $I$ increase?'%dL
    k=dL//10
    c='$%d$'%(10**k)
    tr=[('$%d$'%dL,'Each $10$ dB is a factor of $10$, so the factors multiply.'),('$%d$'%k,'Counted the number of $10$ dB steps but did not convert to a factor.'),('$%d$'%(10*k*2),'Doubled for each step; the base of the logarithm is $10$.')]
    if 10**k==dL: tr[0]=('$%d$'%(dL*10),'Used one step too many.')
    st=['$\\Delta L=10\\log\\left(\\dfrac{I_2}{I_1}\\right)=%d$.'%dL,'$\\log\\left(\\dfrac{I_2}{I_1}\\right)=%d$, so $\\dfrac{I_2}{I_1}=10^{%d}$.'%(k,k)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('2.14','Medium','Calculator')
def t(r):
    a=r.randrange(10,40); b=r.choice([4,5,6,8]); y=a+b*r.choice([2,3])
    xv=math.exp((y-a)/b)
    q='A model is $y=%d+%d\\ln x$. For what value of $x$ does the model give $y=%d$? Round to three decimal places.'%(a,b,y)
    c='$%s$'%num(xv)
    tr=[('$%s$'%num(10**((y-a)/b)),'Used base $10$; $\\ln$ is the natural logarithm, base $e$.'),('$%s$'%num((y-a)/b),'Solved for $\\ln x$ but did not exponentiate.'),('$%s$'%num(math.exp(y/b)-a),'Exponentiated before isolating $\\ln x$.')]
    st=['$\\ln x=\\dfrac{%d-%d}{%d}=%d$.'%(y,a,b,(y-a)//b),'$x=e^{%d}\\approx%s$.'%((y-a)//b,num(xv))]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 2.15 semi-log ----------
@reg('2.15')
def t(r):
    a=r.choice([2,3,5,7]); b=r.choice([2,3,4,6])
    base=r.choice(['\\ln','\\log'])
    q='The data follow $y=%d\\cdot%d^{x}$. On a semi-log plot of $%s y$ against $x$, what is the slope of the line?'%(a,b,base)
    c='$%s %d$'%(base,b)
    tr=[('$%d$'%b,'The slope is the logarithm of the growth factor, not the factor itself.'),('$%s %d$'%(base,a),'$%s %d$ is the vertical intercept.'%(base,a)),('$%s %d$'%(base,a*b),'$\\log(ab^{x})=\\log a+x\\log b$; the terms separate.')]
    st=['$%s y=%s %d+x\\,%s %d$.'%(base,base,a,base,b),'Linear in $x$ with slope $%s %d$.'%(base,b)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('2.15','Medium','Calculator')
def t(r):
    m=r.choice([0.2,0.3,0.4,0.5]); k=r.choice([0.6,0.9,1.2,1.5])
    q='Data on a semi-log plot lie on the line $\\log_{10}y=%sx+%s$. Which exponential model fits the data? Round to three decimal places.'%(m,k)
    A=10**k; B=10**m
    c='$y=%s\\,(%s)^{x}$'%(num(A),num(B))
    tr=[('$y=%s\\,(%s)^{x}$'%(num(k),num(m)),'Read the line\'s constants directly; undo the logarithm with $10^{(\\cdot)}$.'),('$y=%s\\,(%s)^{x}$'%(num(B),num(A)),'Swapped intercept and slope: $10^{\\text{intercept}}$ is the initial value.'),('$y=%s\\,(%s)^{x}$'%(num(math.exp(k)),num(math.exp(m))),'Used $e$ instead of $10$ as the base.')]
    st=['$y=10^{%sx+%s}=10^{%s}\\cdot(10^{%s})^{x}$.'%(m,k,k,m),'$y\\approx%s\\,(%s)^{x}$.'%(num(A),num(B))]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('2.15')
def t(r):
    kind=r.choice(['exp','lin'])
    q='A scatterplot of $\\ln y$ against $x$ is %s. Which conclusion is best?'%('close to a straight line' if kind=='exp' else 'clearly curved (concave down)')
    if kind=='exp':
        c='An exponential model for $y$ is appropriate.'
        tr=[('A linear model for $y$ is appropriate.','Linear in $\\ln y$ means exponential in $y$.'),('A logarithmic model for $y$ is appropriate.','That would need $y$ linear in $\\ln x$.'),('No model is appropriate, because $y$ is not linear.','The semi-log plot linearizes exponential data.')]
    else:
        c='An exponential model for $y$ is not appropriate.'
        tr=[('An exponential model for $y$ is appropriate.','Exponential data become linear on a semi-log plot; this plot is curved.'),('A linear model for $\\ln y$ is appropriate.','The plot of $\\ln y$ is curved, so a line does not fit it.'),('The data must be quadratic.','A curved semi-log plot rules out exponential, but does not prove quadratic.')]
    st=['If $y=ab^{x}$, then $\\ln y=\\ln a+x\\ln b$, a line.',c]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('2.6')
def t(r):
    good=[round(r.uniform(-1.2,1.2),1) for _ in range(5)]
    bad_=sorted([round(r.uniform(.8,3.5),1) for _ in range(5)])
    bad=[bad_[0],-bad_[2],-bad_[4],-bad_[3],bad_[1]]  # curved pattern: + - - - +
    A,B=('linear','exponential') if r.random()<.5 else ('exponential','linear')
    flip=r.random()<.5
    ra,rb=(good,bad) if flip else (bad,good)
    fmt=lambda v:', '.join('%.1f'%x for x in v)
    q='Two models are fit to the same five data points. Residuals for the %s model: $%s$. Residuals for the %s model: $%s$. Which model is more appropriate?'%(A,fmt(ra),B,fmt(rb))
    best=A if flip else B; worst=B if flip else A
    c='The %s model, because its residuals are small and show no pattern.'%best
    tr=[('The %s model, because its residuals change sign.'%worst,'Residuals changing sign in a $+,-,-,-,+$ pattern show a curve the model missed.'),('The %s model, because it has more negative residuals.'%worst,'Count of negative residuals does not decide fit; size and pattern do.'),('Both models are equally appropriate, because both have positive and negative residuals.','Compare the size and the pattern of the residuals, not just their signs.')]
    st=['%s model residuals: small, no clear pattern.'%best.capitalize(),'%s model residuals: larger, curved pattern ($+,-,-,-,+$).'%worst.capitalize(),c]
    return dict(q=q,c=c,tr=tr,st=st)
