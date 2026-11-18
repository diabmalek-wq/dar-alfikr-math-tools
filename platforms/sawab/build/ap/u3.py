from common import *
import math
PI=sp.pi
def ang(a):  # sympy angle -> latex
    return sx(a)
SPECIAL=[sp.Rational(k,6)*PI for k in range(12)]+[sp.Rational(k,4)*PI for k in (1,3,5,7)]
def trigv(f,a): return sp.nsimplify(f(a))
# ---------- 3.1 periodic ----------
@reg('3.1')
def t(r):
    P=r.choice([4,5,6,8]); vals=[r.randrange(-6,10) for _ in range(P)]
    N=r.randrange(30,90)
    tab=', '.join('$f(%d)=%d$'%(i,v) for i,v in enumerate(vals))
    q='A periodic function $f$ has period $%d$. One period of values is %s. What is $f(%d)$?'%(P,tab,N)
    ans=vals[N%P]
    c='$%d$'%ans
    cand=[(vals[(N-1)%P],'Off by one when reducing: $%d=%d\\cdot%d+%d$.'%(N,P,N//P,N%P)),(vals[(N//P)%P],'Used the number of full periods instead of the remainder.'),(vals[(N+1)%P],'Off by one when reducing: $%d=%d\\cdot%d+%d$.'%(N,P,N//P,N%P)),(vals[N%(P-1)],'Used the wrong period length.')]
    tr=[];seen={ans}
    for v,w in cand:
        if v not in seen and len(tr)<3: tr.append(('$%d$'%v,w)); seen.add(v)
    if len(tr)<3: raise Bad
    st=['$f(x+%d)=f(x)$, so reduce $%d$ by multiples of $%d$.'%(P,N,P),'$%d=%d\\cdot%d+%d$, so $f(%d)=f(%d)=%d$.'%(N,P,N//P,N%P,N,N%P,ans)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.1')
def t(r):
    P=r.choice([4,6,8]); h=P//2
    k=r.randrange(4,12); part=r.choice(['rise','fall'])
    a=k*P+(0 if part=='rise' else h); b=a+h
    q='One period of $f$ on $0\\le x\\le %d$: $f$ increases on $0<x<%d$ and decreases on $%d<x<%d$. The period is $%d$. On $%d<x<%d$, is $f$ increasing or decreasing?'%(P,h,h,P,P,a,b)
    c='%s, because $%d<x<%d$ is $%d$ periods after $%s$.'%('Increasing' if part=='rise' else 'Decreasing',a,b,k,'$0<x<%d$'%h if part=='rise' else '$%d<x<%d$'%(h,P))
    c=c.replace('$$','$')
    tr=[('%s, because $%d$ is greater than $%d$.'%('Decreasing' if part=='rise' else 'Increasing',a,P),'Large inputs do not change behaviour; reduce by whole periods.'),('Both, because the interval is longer than one period.','The interval has length $%d$, half a period.'%h),('Neither, because the function repeats.','Repeating behaviour still increases and decreases within each period.')]
    st=['Subtract $%d\\cdot%d=%d$: the interval becomes $%d<x<%d$.'%(k,P,k*P,a-k*P,b-k*P),'On that part of the period $f$ is %s.'%('increasing' if part=='rise' else 'decreasing')]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.1')
def t(r):
    P=r.choice([3,4,5]); base=[r.randrange(0,9) for _ in range(P)]
    if len(set(base))<P: raise Bad
    seq=(base*4)[:3*P]
    q='A function $f$ takes the values $%s$ at $x=0,1,2,\\dots$ and the pattern continues. What is the period of $f$?'%(',\\ '.join(map(str,seq)))
    c='$%d$'%P
    tr=[('$%d$'%(2*P),'The period is the smallest positive shift that repeats the pattern.'),('$%d$'%(P-1),'Counted the gaps between equal values incorrectly.'),('$%s$'%fx(Fr(1,P)),'That is the frequency, the reciprocal of the period.')]
    st=['The block $%s$ repeats.'%(',\\ '.join(map(str,base))),'Smallest shift: $%d$.'%P]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 3.2 radians, sin cos tan ----------
@reg('3.2','Medium','Calculator')
def t(r):
    rad=round(r.uniform(2,9),1); th=round(r.uniform(0.6,4.5),2); s=round(rad*th,3)
    q='An angle in standard position subtends an arc of length $%s$ on a circle of radius $%s$. What is the angle measure in radians?'%(s,rad)
    c='$%s$'%num(s/rad)
    tr=[('$%s$'%num(s*rad),'Multiplied; $\\theta=\\dfrac{s}{r}$.'),('$%s$'%num(rad/s),'Inverted the ratio: arc length goes on top.'),('$%s$'%num(s/rad*180/math.pi),'Converted to degrees; the question asks for radians.')]
    st=['$\\theta=\\dfrac{s}{r}=\\dfrac{%s}{%s}$.'%(s,rad),'$\\theta\\approx%s$ radians.'%num(s/rad)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.2')
def t(r):
    k=r.randrange(2,9); f=r.choice([1,3,5,7,9,11,13,15,17,19])
    x=Fr(f,10)+2*k if r.random()<.5 else Fr(f,10)+2*k-0  # positive
    red=x-2*int(x/2)
    qd=1+int(red*2)  # quarter index
    names={1:'Quadrant I',2:'Quadrant II',3:'Quadrant III',4:'Quadrant IV'}
    if red in (0,Fr(1,2),1,Fr(3,2)): raise Bad
    dec=('%.1f'%float(x))
    q='An angle in standard position measures $%s\\pi$ radians. In which quadrant is its terminal ray?'%dec
    c=names[qd]
    wrong=[names[(qd)%4+1],names[(qd+1)%4+1],names[(qd+2)%4+1]]
    tr=[(wrong[0],'Reduce by multiples of $2\\pi$ (whole revolutions), not by $\\pi$.' ),(wrong[1],'Each quadrant spans $0.5\\pi$; recheck which half-$\\pi$ block contains the reduced angle.'),(wrong[2],'Counted the quadrants clockwise.')]
    st=['Subtract $%d\\pi$ (whole revolutions): $%s\\pi$.'%(int(x/2)*2,('%.1f'%float(red))),'$%s\\pi$ lies in %s.'%(('%.1f'%float(red)),c)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.2')
def t(r):
    a,b,h=r.choice([(3,4,5),(5,12,13),(8,15,17),(7,24,25),(6,8,10)])
    if r.random()<.5: a,b=b,a
    sx_,sy=r.choice([(1,1),(-1,1),(-1,-1),(1,-1)])
    x,y=sx_*a,sy*b
    fn=r.choice(['sin','cos','tan'])
    val={'sin':Fr(y,h),'cos':Fr(x,h),'tan':Fr(y,x)}[fn]
    q='The terminal ray of $\\theta$ in standard position passes through $(%d,%d)$ on a circle centred at the origin. What is $\\%s\\theta$?'%(x,y,fn)
    c='$%s$'%fx(val)
    pool={'sin':[(Fr(x,h),'Used the horizontal displacement; $\\sin\\theta=\\dfrac{y}{r}$.'),(Fr(abs(y),h),'Dropped the sign: the point is below/left of an axis.'),(Fr(y,x),'That is $\\tan\\theta$.')],
          'cos':[(Fr(y,h),'Used the vertical displacement; $\\cos\\theta=\\dfrac{x}{r}$.'),(Fr(abs(x),h),'Dropped the sign of $x$.'),(Fr(x,y),'That is $\\cot\\theta=\\dfrac{x}{y}$.')],
          'tan':[(Fr(x,y),'Inverted: $\\tan\\theta=\\dfrac{y}{x}$.'),(Fr(y,h),'That is $\\sin\\theta$.'),(Fr(abs(y),abs(x)),'Dropped the sign; check the quadrant.')]}[fn]
    tr=[('$%s$'%fx(v),w) for v,w in pool]
    st=['$r=\\sqrt{(%d)^{2}+(%d)^{2}}=%d$.'%(x,y,h),'$\\%s\\theta=%s$.'%(fn,fx(val))]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 3.3 values and coordinates ----------
@reg('3.3')
def t(r):
    a=r.choice([sp.Rational(k,6)*PI for k in (2,4,5,7,8,10,11)]+[sp.Rational(k,4)*PI for k in (3,5,7)])
    fn=r.choice([sp.sin,sp.cos]); nm='sin' if fn==sp.sin else 'cos'; other=sp.cos if fn==sp.sin else sp.sin
    v=trigv(fn,a); w=trigv(other,a)
    q='What is the exact value of $\\%s\\left(%s\\right)$?'%(nm,ang(a))
    c='$%s$'%sx(v)
    cand=[(w,'That is the other coordinate: $\\cos\\theta=x$, $\\sin\\theta=y$.'),(-v,'Sign error: check the quadrant of $%s$.'%ang(a)),(-w,'Wrong coordinate and wrong sign.'),(sp.nsimplify(abs(v)),'Dropped the sign.')]
    tr=[];seen={sx(v)}
    for val,why in cand:
        s_=sx(val)
        if s_ not in seen and len(tr)<3: tr.append(('$%s$'%s_,why)); seen.add(s_)
    if len(tr)<3: raise Bad
    st=['$%s$ is in quadrant %s; reference angle $%s$.'%(ang(a),['I','II','III','IV'][int((a/(PI/2)))%4],ang(sp.pi-a if a<PI and a>PI/2 else (a-PI if a<3*PI/2 and a>PI else (2*PI-a if a>3*PI/2 else a)))),'Point $\\left(%s,\\ %s\\right)$, so $\\%s\\left(%s\\right)=%s$.'%(sx(trigv(sp.cos,a)),sx(trigv(sp.sin,a)),nm,ang(a),sx(v))]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.3')
def t(r):
    a=r.choice([sp.Rational(k,6)*PI for k in (1,2,4,5,7,8,10,11)]+[sp.Rational(k,4)*PI for k in (1,3,5,7)])
    R=r.choice([2,4,6,8,10,12])
    x=sp.nsimplify(R*sp.cos(a)); y=sp.nsimplify(R*sp.sin(a))
    q='An angle of $%s$ radians is in standard position. Its terminal ray meets a circle of radius $%d$ centred at the origin at which point?'%(ang(a),R)
    P=lambda u,v:'$\\left(%s,\\ %s\\right)$'%(sx(u),sx(v))
    c=P(x,y)
    tr=[(P(y,x),'Swapped: $x=r\\cos\\theta$ and $y=r\\sin\\theta$.'),(P(sp.cos(a),sp.sin(a)),'Forgot to multiply by the radius $%d$.'%R),(P(-x,y) if x!=0 else P(x,-y),'Sign error: check the quadrant.')]
    st=['$(x,y)=(r\\cos\\theta,\\ r\\sin\\theta)$.','$=\\left(%d\\cos%s,\\ %d\\sin%s\\right)=%s$.'%(R,ang(a),R,ang(a),c.strip('$'))]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.3','Hard')
def t(r):
    a=r.choice([sp.Rational(k,6)*PI for k in (1,2,4,5,7,8,10,11)]+[sp.Rational(k,4)*PI for k in (1,3,5,7)])
    R=r.choice([2,4,6,8])
    x=sp.nsimplify(R*sp.cos(a)); y=sp.nsimplify(R*sp.sin(a))
    q='The terminal ray of $\\theta$, with $0\\le\\theta<2\\pi$, meets a circle centred at the origin at $\\left(%s,\\ %s\\right)$. What are $\\theta$ and the radius $r$?'%(sx(x),sx(y))
    ref=sp.atan(abs(y/x)) if x!=0 else PI/2
    c='$\\theta=%s,\\ r=%d$'%(ang(a),R)
    alt=[ang(ref),ang(PI-ref),ang(PI+ref),ang(2*PI-ref)]
    alt=[v for v in alt if v!=ang(a)]
    tr=[('$\\theta=%s,\\ r=%d$'%(alt[0],R),'Used the reference angle without placing it in the correct quadrant.'),('$\\theta=%s,\\ r=%d$'%(alt[1],R),'Placed the angle in the wrong quadrant.'),('$\\theta=%s,\\ r=%s$'%(ang(a),sx(abs(x)+abs(y))),'$r=\\sqrt{x^{2}+y^{2}}$, not $|x|+|y|$.')]
    st=['$r=\\sqrt{x^{2}+y^{2}}=%d$.'%R,'$\\cos\\theta=%s$, $\\sin\\theta=%s$, so $\\theta=%s$.'%(sx(x/R),sx(y/R),ang(a))]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 3.4 sine/cosine graphs ----------
QI=[(0,'0','\\dfrac{\\pi}{2}'),(1,'\\dfrac{\\pi}{2}','\\pi'),(2,'\\pi','\\dfrac{3\\pi}{2}'),(3,'\\dfrac{3\\pi}{2}','2\\pi')]
@reg('3.4')
def t(r):
    k,a,b=r.choice(QI); fn=r.choice(['sin','cos'])
    if fn=='sin': inc=k in (0,3); cu=k in (2,3)
    else: inc=k in (2,3); cu=k in (1,2)
    W=lambda i,c_:'%s and concave %s'%('Increasing' if i else 'Decreasing','up' if c_ else 'down')
    q='Describe $f(\\theta)=\\%s\\theta$ on the interval $%s<\\theta<%s$.'%(fn,a,b)
    c=W(inc,cu)
    tr=[(W(not inc,cu),'Trace the %s-coordinate around the unit circle on this quarter turn.'%('$y$' if fn=='sin' else '$x$')),(W(inc,not cu),'%s is concave down where it is above its midline and concave up below.'%('$\\sin$' if fn=='sin' else '$\\cos$')),(W(not inc,not cu),'Mixed up the graphs of sine and cosine.')]
    st=['On this quarter turn the %s-coordinate %s.'%('$y$' if fn=='sin' else '$x$','increases' if inc else 'decreases'),'The graph is %s the midline $y=0$, so concave %s.'%('below' if cu else 'above','up' if cu else 'down')]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.4')
def t(r):
    fn=r.choice(['sin','cos']); rel=r.choice(['pi','2pi','pi-'])
    expr={'pi':'\\theta+\\pi','2pi':'\\theta+2\\pi','pi-':'\\pi-\\theta'}[rel]
    q='For every angle $\\theta$, how does $\\%s(%s)$ compare with $\\%s\\theta$?'%(fn,expr,fn)
    same=(rel=='2pi') or (rel=='pi-' and fn=='sin')
    c='$\\%s(%s)=\\%s\\theta$'%(fn,expr,fn) if same else '$\\%s(%s)=-\\%s\\theta$'%(fn,expr,fn)
    o2='$\\%s(%s)=-\\%s\\theta$'%(fn,expr,fn) if same else '$\\%s(%s)=\\%s\\theta$'%(fn,expr,fn)
    oth='cos' if fn=='sin' else 'sin'
    tr=[(o2,'Locate both terminal rays on the unit circle: %s.'%{'pi':'adding $\\pi$ reaches the opposite point','2pi':'adding $2\\pi$ is a full turn','pi-':'$\\pi-\\theta$ reflects over the $y$-axis'}[rel]),('$\\%s(%s)=\\%s\\theta$'%(fn,expr,oth),'Changing the angle by $\\pi$ or $2\\pi$ does not swap sine and cosine.'),('It depends on the value of $\\theta$.','The relation holds for every $\\theta$ by the symmetry of the unit circle.')]
    st=[{'pi':'$\\theta+\\pi$ ends at the point opposite $\\theta$: both coordinates change sign.','2pi':'$\\theta+2\\pi$ is one full revolution: the same point.','pi-':'$\\pi-\\theta$ reflects the point over the $y$-axis: $x$ changes sign, $y$ does not.'}[rel],c]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.4')
def t(r):
    fn,val=r.choice([('cos',1),('cos',-1),('sin',1),('sin',-1),('sin',0),('cos',0)])
    sol={('cos',1):'2\\pi k',('cos',-1):'\\pi+2\\pi k',('sin',1):'\\dfrac{\\pi}{2}+2\\pi k',('sin',-1):'\\dfrac{3\\pi}{2}+2\\pi k',('sin',0):'\\pi k',('cos',0):'\\dfrac{\\pi}{2}+\\pi k'}
    q='What are all solutions of $\\%s\\theta=%d$? ($k$ is any integer.)'%(fn,val)
    c='$\\theta=%s$'%sol[(fn,val)]
    others=[v for kk,v in sol.items() if kk!=(fn,val)]
    r.shuffle(others)
    tr=[('$\\theta=%s$'%others[0],'Check the point on the unit circle where the %s-coordinate is $%d$.'%('$x$' if fn=='cos' else '$y$',val)),('$\\theta=%s$'%others[1],'Confused sine ($y$) with cosine ($x$).'),('$\\theta=%s$'%(sol[(fn,val)].replace('2\\pi k','\\pi k') if '2\\pi k' in sol[(fn,val)] else sol[(fn,val)].replace('\\pi k','2\\pi k')),'Wrong spacing between solutions.')]
    st=['On the unit circle, %s-coordinate $=%d$ at %s.'%('$x$' if fn=='cos' else '$y$',val,c),'Add whole periods for all solutions.']
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 3.5 sinusoidal functions ----------
@reg('3.5')
def t(r):
    M=r.randrange(20,120); m=M-2*r.randrange(4,30)
    q='A sinusoidal function has maximum value $%d$ and minimum value $%d$. What are its amplitude and midline?'%(M,m)
    A=Fr(M-m,2); D=Fr(M+m,2)
    c='Amplitude $%s$; midline $y=%s$'%(fx(A),fx(D))
    tr=[('Amplitude $%d$; midline $y=%s$'%(M-m,fx(D)),'Amplitude is half the distance from max to min.'),('Amplitude $%s$; midline $y=%s$'%(fx(D),fx(A)),'Swapped: midline is the average of max and min.'),('Amplitude $%s$; midline $y=0$'%fx(A),'The graph has been shifted; the midline is $y=\\dfrac{\\max+\\min}{2}$.')]
    st=['$a=\\dfrac{%d-(%d)}{2}=%s$.'%(M,m,fx(A)),'$d=\\dfrac{%d+(%d)}{2}=%s$.'%(M,m,fx(D))]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.5')
def t(r):
    a=r.choice([2,3,4,5]); b=r.choice([sp.Rational(1,2),2,3,4,sp.pi,sp.pi/2,sp.pi/3])
    fn=r.choice(['sin','cos']); ask=r.choice(['period','frequency'])
    P=sp.nsimplify(2*sp.pi/b); F=sp.nsimplify(b/(2*sp.pi))
    q='What is the %s of $f(\\theta)=%d\\%s\\left(%s\\theta\\right)$?'%(ask,a,fn,sx(b))
    ans=P if ask=='period' else F
    c='$%s$'%sx(ans)
    cand=[(F if ask=='period' else P,'Period and frequency are reciprocals; this is the %s.'%('frequency' if ask=='period' else 'period')),(sp.nsimplify(2*sp.pi*b),'Multiplied by $b$; the period is $\\dfrac{2\\pi}{b}$.'),(sp.nsimplify(b),'$b$ is not the period or frequency itself.'),(sp.nsimplify(sp.pi/b),'$\\dfrac{\\pi}{b}$ is the period of tangent, not sine or cosine.')]
    tr=[];seen={sx(ans)}
    for v,w in cand:
        if sx(v) not in seen and len(tr)<3: tr.append(('$%s$'%sx(v),w)); seen.add(sx(v))
    st=['Period $=\\dfrac{2\\pi}{b}=%s$.'%sx(P),'Frequency $=\\dfrac{1}{\\text{period}}=%s$.'%sx(F)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.5','Hard','Calculator')
def t(r):
    A=r.choice([20,30,40]); b=r.choice([0.15,0.2,0.25,0.3]); D=r.choice([50,60,70]); t0=r.randrange(5,40)
    fn=r.choice(['cos','sin'])
    d1=(-A*b*math.sin(b*t0)) if fn=='cos' else (A*b*math.cos(b*t0)); d2=-A*b*b*(math.cos(b*t0) if fn=='cos' else math.sin(b*t0))
    if abs(d1)<1e-2 or abs(d2)<1e-3: raise Bad
    inc=d1>0; acc=(d2>0)==inc  # rate increasing in magnitude?
    W=lambda i,j:'%s at %s rate'%('Increasing' if i else 'Decreasing','an increasing' if j else 'a decreasing')
    # 'increasing rate' means rate of change is increasing (d2>0)
    c=W(inc,d2>0)
    q='The patience level $P(t)=%d\\%s(%st)+%d$, with $t$ in minutes. Which describes $P$ at $t=%d$? (Use radians.)'%(A,fn,b,D,t0)
    tr=[(W(not inc,d2>0),'Find whether the graph is rising or falling at $t=%d$ in radian mode.'%t0),(W(inc,not d2>0),'Concave up means the rate of change is increasing; concave down means decreasing.'),(W(not inc,not d2>0),'Both the direction and the concavity are reversed; check radian mode.')]
    st=['In radian mode, $P(%d)\\approx%s$.'%(t0,num(A*(math.cos(b*t0) if fn=='cos' else math.sin(b*t0))+D)),'Near $t=%d$ the graph is %s and %s the midline $y=%d$, so concave %s.'%(t0,'rising' if inc else 'falling','below' if d2>0 else 'above',D,'up' if d2>0 else 'down'),c]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 3.6 transformations ----------
@reg('3.6','Hard')
def t(r):
    a=r.choice([2,3,4]); b=r.choice([2,3,4]); e=r.choice([sp.pi,sp.pi/2,sp.pi/3,-sp.pi,-sp.pi/2]); d=r.randrange(-5,6)
    fn=r.choice(['sin','cos'])
    ps=sp.nsimplify(-e/b)
    q='What is the phase shift of $y=%d\\%s\\left(%dx%s%s\\right)%s$?'%(a,fn,b,'+' if e>0 else '-',sx(abs(e)),term(d,0))
    D=lambda v:'%s by $%s$'%('Left' if v<0 else 'Right',sx(abs(v)))
    c=D(ps)
    tr=[(D(-e),'Factor out $b$ first: $%dx%s%s=%d\\left(x%s%s\\right)$.'%(b,'+' if e>0 else '-',sx(abs(e)),b,'+' if e>0 else '-',sx(abs(e/b)))),(D(-ps),'Direction error: $x+c$ shifts left, $x-c$ shifts right.'),(D(sp.nsimplify(-e*b)),'Multiplied by $b$ instead of dividing.')]
    st=['$%dx%s%s=%d\\left(x%s%s\\right)$.'%(b,'+' if e>0 else '-',sx(abs(e)),b,'+' if e>0 else '-',sx(abs(e/b))),'Phase shift: %s.'%c.lower()]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.6')
def t(r):
    A=r.choice([2,3,5,6,11]); P=r.choice([sp.pi,4*sp.pi,6*sp.pi,sp.pi/2,4,6]); D=r.choice([-4,-3,2,7,9])
    b=sp.nsimplify(2*sp.pi/P)
    q='Which sine function has amplitude $%d$, period $%s$ and a vertical shift of $%d$?'%(A,sx(P),D)
    F=lambda bb:'$y=%d\\sin\\left(%sx\\right)%s$'%(A,sx(bb) if bb!=1 else '',term(D,0))
    c=F(b)
    tr=[(F(P),'Used the period as $b$; $b=\\dfrac{2\\pi}{\\text{period}}$.'),(F(sp.nsimplify(P/(2*sp.pi))),'Inverted: $b=\\dfrac{2\\pi}{\\text{period}}$, not $\\dfrac{\\text{period}}{2\\pi}$.'),('$y=%d\\sin\\left(%sx\\right)%s$'%(2*A,sx(b) if b!=1 else '',term(D,0)),'Doubled the amplitude; the coefficient is the amplitude itself.')]
    st=['$b=\\dfrac{2\\pi}{%s}=%s$.'%(sx(P),sx(b)),c]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.6')
def t(r):
    a=r.choice([-4,-3,-2,2,3,5]); b=r.choice([2,3,4]); d=r.randrange(-6,7); fn=r.choice(['sin','cos'])
    q='What is the range of $y=%s%d\\%s(%dx)$?'%('%d'%d if d else '',a if not d else a,fn,b) if not d else 'What is the range of $y=%d%s\\%s(%dx)$?'%(d,('+%d'%a) if a>0 else '%d'%a,fn,b)
    A=abs(a)
    c='$[%d,\\ %d]$'%(d-A,d+A)
    tr=[('$[%d,\\ %d]$'%(-A,A),'Forgot the vertical shift (midline $y=%d$).'%d),('$[%d,\\ %d]$'%(d-2*A,d+2*A),'Used $2|a|$ instead of $|a|$ on each side of the midline.'),('$[%d,\\ %d]$'%(d-b,d+b),'Used $b$ (which changes the period) instead of the amplitude.')]
    if d==0: tr[0]=('$[%d,\\ %d]$'%(-A+1,A+1),'Shifted the midline without reason.')
    st=['Midline $y=%d$, amplitude $|%d|=%d$.'%(d,a,A),'Range: $[%d-%d,\\ %d+%d]=[%d,\\ %d]$.'%(d,A,d,A,d-A,d+A)]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 3.7 modeling ----------
@reg('3.7')
def t(r):
    H=r.choice([30,40,55,60]); R=r.choice([20,25,30,50]); T=r.choice([20,30,40,60])
    if R>=H: raise Bad
    start=r.choice(['bottom','top'])
    q='A Ferris wheel has its centre $%d$ m above the ground and radius $%d$ m. It turns once every $%d$ seconds, and a rider is at the %s at $t=0$. Which models the rider\'s height $h(t)$, in meters?'%(H,R,T,start)
    sg='-' if start=='bottom' else '+'
    k=sp.nsimplify(2*sp.pi/T)
    c='$h(t)=%d%s%d\\cos\\left(%st\\right)$'%(H,sg,R,sx(k))
    o='+' if sg=='-' else '-'
    tr=[('$h(t)=%d%s%d\\cos\\left(%st\\right)$'%(H,o,R,sx(k)),'At $t=0$ the rider is at the %s, so $h(0)$ must be $%d$.'%(start,H-R if start=='bottom' else H+R)),('$h(t)=%d%s%d\\sin\\left(%st\\right)$'%(H,sg,R,sx(k)),'Sine starts at the midline, not at a maximum or minimum.'),('$h(t)=%d%s%d\\cos\\left(%dt\\right)$'%(H,sg,R,T),'Use $b=\\dfrac{2\\pi}{\\text{period}}$, not the period.')]
    st=['Midline $%d$, amplitude $%d$, $b=\\dfrac{2\\pi}{%d}=%s$.'%(H,R,T,sx(k)),'Start at the %s: $h(0)=%d$, so use $%s\\cos$.'%(start,H-R if start=='bottom' else H+R,sg)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.7','Hard')
def t(r):
    x1=r.randrange(-4,4); dx=r.choice([2,3,4,5,6]); m=r.randrange(-5,10); M=m+2*r.randrange(3,12)
    q='The graph of $f(x)=a\\sin(b(x-c))+d$, with $a,b>0$, has a minimum at $(%d,%d)$ and the next maximum at $(%d,%d)$. What are $a$, $d$ and $b$?'%(x1,m,x1+dx,M)
    A=Fr(M-m,2); D=Fr(M+m,2); b=sp.nsimplify(sp.pi/dx)
    c='$a=%s,\\ d=%s,\\ b=%s$'%(fx(A),fx(D),sx(b))
    tr=[('$a=%s,\\ d=%s,\\ b=%s$'%(fx(A),fx(D),sx(2*sp.pi/dx)),'Min to the next max is half a period, so the period is $%d$.'%(2*dx)),('$a=%d,\\ d=%s,\\ b=%s$'%(M-m,fx(D),sx(b)),'Amplitude is half of max minus min.'),('$a=%s,\\ d=%s,\\ b=%s$'%(fx(A),fx(A),sx(b)),'The midline is the average of max and min.')]
    st=['$a=\\dfrac{%d-(%d)}{2}=%s$, $d=\\dfrac{%d+(%d)}{2}=%s$.'%(M,m,fx(A),M,m,fx(D)),'Half period $=%d$, period $=%d$, $b=\\dfrac{2\\pi}{%d}=%s$.'%(dx,2*dx,2*dx,sx(b))]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.7','Medium','Calculator')
def t(r):
    A=r.choice([50,55,85]); T=r.choice([40,60,72]); s=r.choice([4,6,10]); D=A+r.choice([5,8,10]); t0=0
    v=A*math.sin(2*math.pi/T*(t0-s))+D
    q='A rider\'s height is $h(t)=%d\\sin\\left(\\dfrac{2\\pi}{%d}(t-%d)\\right)+%d$ feet, $t$ in seconds. What is the height when the ride begins, at $t=0$?'%(A,T,s,D)
    c='$%s$ ft'%num(v)
    vdeg=A*math.sin(math.radians(2*math.pi/T*(t0-s)))+D
    tr=[('$%s$ ft'%num(vdeg),'Calculator in degree mode; use radians.'),('$%s$ ft'%num(A*math.sin(2*math.pi/T*(s))+D),'Sign error inside: $t-%d$ at $t=0$ is $-%d$.'%(s,s)),('$%d$ ft'%D,'The rider is not on the midline at $t=0$ because of the phase shift.')]
    st=['$h(0)=%d\\sin\\left(-\\dfrac{%d\\pi}{%d}\\right)+%d$.'%(A,2*s,T,D),'In radians, $h(0)\\approx%s$.'%num(v)]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 3.8 tangent ----------
@reg('3.8')
def t(r):
    a=r.choice([sp.Rational(k,6)*PI for k in (1,2,4,5,7,8,10,11)]+[sp.Rational(k,4)*PI for k in (1,3,5,7)])
    v=sp.nsimplify(sp.tan(a))
    q='What is the slope of the terminal ray of an angle of $%s$ radians in standard position?'%ang(a)
    c='$%s$'%sx(v)
    cand=[(sp.nsimplify(1/v),'That is $\\cot\\theta=\\dfrac{x}{y}$; slope is $\\dfrac{y}{x}$.'),(-v,'Sign error: check the quadrant.'),(sp.nsimplify(sp.sin(a)),'That is $\\sin\\theta$; slope is $\\tan\\theta$.'),(sp.nsimplify(-1/v),'Inverted and changed sign.')]
    tr=[];seen={sx(v)}
    for val,w in cand:
        if sx(val) not in seen and len(tr)<3: tr.append(('$%s$'%sx(val),w)); seen.add(sx(val))
    if len(tr)<3: raise Bad
    st=['Slope of the terminal ray $=\\tan\\theta=\\dfrac{\\sin\\theta}{\\cos\\theta}$.','$=\\dfrac{%s}{%s}=%s$.'%(sx(sp.sin(a)),sx(sp.cos(a)),sx(v))]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.8')
def t(r):
    b=r.choice([2,3,4,6,sp.Rational(1,2),sp.Rational(1,3)])
    q='Which equation gives all vertical asymptotes of $f(\\theta)=\\tan(%s\\theta)$? ($k$ is any integer.)'%sx(b)
    c='$\\theta=%s+%s k$'%(sx(sp.pi/(2*b)),sx(sp.pi/b))
    tr=[('$\\theta=\\dfrac{\\pi}{2}+\\pi k$','Those are the asymptotes of $\\tan\\theta$ before the horizontal dilation.'),('$\\theta=%s+\\pi k$'%sx(sp.pi/(2*b)),'The spacing between asymptotes is the period $\\dfrac{\\pi}{b}$, not $\\pi$.'),('$\\theta=%s+%s k$'%(sx(sp.pi/b),sx(sp.pi/b)),'The first asymptote is at $\\dfrac{\\pi}{2b}$, where $b\\theta=\\dfrac{\\pi}{2}$.')]
    st=['Asymptotes where $%s\\theta=\\dfrac{\\pi}{2}+\\pi k$.'%sx(b),'$\\theta=%s+%s k$.'%(sx(sp.pi/(2*b)),sx(sp.pi/b))]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.8')
def t(r):
    a=r.choice([2,3,-2,4]); b=r.choice([2,3,4,sp.Rational(1,2),sp.pi,sp.pi/2]); c0=r.randrange(-3,4); d=r.randrange(-4,5)
    q='What is the period of $g(x)=%d\\tan\\left(%s(x%s)\\right)%s$?'%(a,sx(b),term(c0,0),term(d,0))
    P=sp.nsimplify(sp.pi/b)
    c='$%s$'%sx(P)
    cand=[(sp.nsimplify(2*sp.pi/b),'$\\dfrac{2\\pi}{b}$ is the period of sine and cosine; tangent repeats every $\\dfrac{\\pi}{b}$.'),(sp.nsimplify(sp.pi*b),'Multiplied by $b$ instead of dividing.'),(sp.pi,'$\\pi$ is the period of $\\tan x$ before the dilation.'),(sp.nsimplify(sp.pi/abs(a)),'$a$ stretches vertically; it does not change the period.')]
    tr=[];seen={sx(P)}
    for v,w in cand:
        if sx(v) not in seen and len(tr)<3: tr.append(('$%s$'%sx(v),w)); seen.add(sx(v))
    if len(tr)<3: raise Bad
    st=['Period of $\\tan(bx)$ is $\\dfrac{\\pi}{|b|}$.','$\\dfrac{\\pi}{%s}=%s$.'%(sx(b),sx(P))]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 3.9 inverse trig ----------
@reg('3.9')
def t(r):
    fn,x=r.choice([('arcsin',-sp.sqrt(3)/2),('arcsin',-sp.Rational(1,2)),('arcsin',-sp.sqrt(2)/2),('arccos',-sp.Rational(1,2)),('arccos',-sp.sqrt(2)/2),('arccos',-sp.sqrt(3)/2),('arctan',-1),('arctan',-sp.sqrt(3)),('arctan',-sp.sqrt(3)/3),('arcsin',sp.sqrt(3)/2),('arccos',sp.Rational(1,2))])
    F={'arcsin':sp.asin,'arccos':sp.acos,'arctan':sp.atan}[fn]
    v=sp.nsimplify(F(x))
    q='What is $\\%s\\left(%s\\right)$?'%(fn,sx(x))
    c='$%s$'%sx(v)
    if fn=='arccos': alts=[(-v if v!=0 else PI,'$\\arccos$ outputs lie in $[0,\\pi]$; negative angles are not allowed.'),(2*PI-v,'Correct cosine value, but outside the principal range $[0,\\pi]$.'),(PI-v,'Used the reference angle in the wrong quadrant.')]
    elif fn=='arcsin': alts=[(PI-v if v<0 else PI-v,'Outside the principal range $\\left[-\\dfrac{\\pi}{2},\\dfrac{\\pi}{2}\\right]$.'),(2*PI+v if v<0 else -v,'Same sine value but not the principal value.' if v<0 else 'Sign error.'),(sp.nsimplify(PI/2-v),'That is the $\\arccos$ value (complementary angle).')]
    else: alts=[(PI+v,'Outside the principal range $\\left(-\\dfrac{\\pi}{2},\\dfrac{\\pi}{2}\\right)$.'),(-v,'Sign error: $\\arctan$ of a negative number is negative.'),(sp.nsimplify(PI/2+v),'Mixed up the reference angle.')]
    tr=[];seen={sx(v)}
    for val,w in alts:
        s_=sx(sp.nsimplify(val))
        if s_ not in seen and len(tr)<3: tr.append(('$%s$'%s_,w)); seen.add(s_)
    if len(tr)<3: raise Bad
    rng={'arcsin':'\\left[-\\dfrac{\\pi}{2},\\dfrac{\\pi}{2}\\right]','arccos':'[0,\\pi]','arctan':'\\left(-\\dfrac{\\pi}{2},\\dfrac{\\pi}{2}\\right)'}[fn]
    st=['The principal value lies in $%s$.'%rng,'The angle there with %s $%s$ is $%s$.'%({'arcsin':'sine','arccos':'cosine','arctan':'tangent'}[fn],sx(x),sx(v))]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.9','Hard')
def t(r):
    a,b,h=r.choice([(3,4,5),(5,12,13),(8,15,17),(7,24,25)])
    outer,inner=r.choice([('sin','arccos'),('cos','arcsin'),('tan','arccos'),('tan','arcsin')])
    sgn=r.choice([1,-1])
    x=Fr(sgn*a,h)
    # angle theta=inner(x)
    if inner=='arccos': cs=x; sn=Fr(b,h)  # arccos in [0,pi], sin>=0
    else: sn=x; cs=Fr(b,h)  # arcsin in [-pi/2,pi/2], cos>=0
    val={'sin':sn,'cos':cs,'tan':sn/cs}[outer]
    q='What is the exact value of $\\%s\\left(\\%s\\left(%s\\right)\\right)$?'%(outer,inner,fx(x))
    c='$%s$'%fx(val)
    cand=[(-val,'Sign: the output of $\\%s$ lies in %s, where %s.'%(inner,'$[0,\\pi]$' if inner=='arccos' else '$\\left[-\\frac{\\pi}{2},\\frac{\\pi}{2}\\right]$','$\\sin\\ge0$' if inner=='arccos' else '$\\cos\\ge0$')),(x,'$\\%s$ and $\\%s$ do not cancel; they are not inverses of each other.'%(outer,inner)),(1/val if val else Fr(h,a),'Inverted the ratio.'),(Fr(b,a),'Used the wrong pair of sides.')]
    tr=[];seen={fx(val)}
    for v,w in cand:
        if fx(v) not in seen and len(tr)<3: tr.append(('$%s$'%fx(v),w)); seen.add(fx(v))
    st=['Let $\\theta=\\%s\\left(%s\\right)$: %s.'%(inner,fx(x),'$\\cos\\theta=%s$, $0\\le\\theta\\le\\pi$'%fx(x) if inner=='arccos' else '$\\sin\\theta=%s$, $-\\frac{\\pi}{2}\\le\\theta\\le\\frac{\\pi}{2}$'%fx(x)),'Right triangle with sides $%d,%d,%d$: $\\sin\\theta=%s$, $\\cos\\theta=%s$.'%(a,b,h,fx(sn),fx(cs)),'$\\%s\\theta=%s$.'%(outer,fx(val))]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.9')
def t(r):
    a=r.choice([2,3,4,5]); d=r.choice([-5,-3,-1,1,2,4])
    q='For $f(x)=%d\\sin x%s$ with $-\\dfrac{\\pi}{2}\\le x\\le\\dfrac{\\pi}{2}$, what is the domain of $f^{-1}$?'%(a,term(d,0))
    c='$[%d,\\ %d]$'%(d-a,d+a)
    tr=[('$\\left[-\\dfrac{\\pi}{2},\\ \\dfrac{\\pi}{2}\\right]$','That is the range of $f^{-1}$; its domain is the range of $f$.'),('$[-1,\\ 1]$','Forgot the dilation and shift of sine.'),('$[%d,\\ %d]$'%(-a,a),'Forgot the vertical shift $%d$.'%d)]
    st=['Range of $f$: $%d\\sin x$ runs from $-%d$ to $%d$, then shift by $%d$.'%(a,a,a,d),'Domain of $f^{-1}$ = range of $f$ = $[%d,\\ %d]$.'%(d-a,d+a)]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 3.10 equations ----------
SOLS={sp.Rational(1,2):('\\dfrac{\\pi}{6}','\\dfrac{5\\pi}{6}'),-sp.Rational(1,2):('\\dfrac{7\\pi}{6}','\\dfrac{11\\pi}{6}'),sp.sqrt(2)/2:('\\dfrac{\\pi}{4}','\\dfrac{3\\pi}{4}'),-sp.sqrt(2)/2:('\\dfrac{5\\pi}{4}','\\dfrac{7\\pi}{4}'),sp.sqrt(3)/2:('\\dfrac{\\pi}{3}','\\dfrac{2\\pi}{3}'),-sp.sqrt(3)/2:('\\dfrac{4\\pi}{3}','\\dfrac{5\\pi}{3}')}
CSOLS={sp.Rational(1,2):('\\dfrac{\\pi}{3}','\\dfrac{5\\pi}{3}'),-sp.Rational(1,2):('\\dfrac{2\\pi}{3}','\\dfrac{4\\pi}{3}'),sp.sqrt(2)/2:('\\dfrac{\\pi}{4}','\\dfrac{7\\pi}{4}'),-sp.sqrt(2)/2:('\\dfrac{3\\pi}{4}','\\dfrac{5\\pi}{4}'),sp.sqrt(3)/2:('\\dfrac{\\pi}{6}','\\dfrac{11\\pi}{6}'),-sp.sqrt(3)/2:('\\dfrac{5\\pi}{6}','\\dfrac{7\\pi}{6}')}
@reg('3.10')
def t(r):
    fn=r.choice(['sin','cos']); k=r.choice([sp.Rational(1,2),-sp.Rational(1,2),sp.sqrt(3)/2,-sp.sqrt(3)/2,sp.sqrt(2)/2,-sp.sqrt(2)/2])
    m=2; c0=r.randrange(-3,5)
    rhs=sp.nsimplify(m*k+c0)
    S=(SOLS if fn=='sin' else CSOLS)[k]; S2=(CSOLS if fn=='sin' else SOLS)[k]
    q='Solve $%d\\%s x%s=%s$ for $0\\le x<2\\pi$.'%(m,fn,term(c0,0),sx(rhs))
    c='$x=%s$ or $x=%s$'%S
    pos=(SOLS if fn=='sin' else CSOLS)[abs(k)]
    tr=[('$x=%s$ only'%S[0],'There are two solutions in one revolution.'),('$x=%s$ or $x=%s$'%S2,'Used the %s values; the equation involves $\\%s$.'%('cosine' if fn=='sin' else 'sine',fn)),('$x=%s$ or $x=%s$'%pos if k<0 else '$x=%s$ or $x=%s$'%(SOLS if fn=='cos' else CSOLS)[-k],'Sign error: placed the angles where $\\%s x$ has the opposite sign.'%fn)]
    st=['$\\%s x=%s$.'%(fn,sx(k)),'In $[0,2\\pi)$: $x=%s$ or $x=%s$.'%S]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.10','Hard')
def t(r):
    b=r.choice([2,3,4]); a=r.choice([2,4]); fn=r.choice(['sin','cos'])
    k=r.choice([sp.Rational(1,2),-sp.Rational(1,2)])
    d=sp.nsimplify(-a*k)
    q='The function $f(x)=%d\\%s(%dx)%s$. For how many values of $x$ with $0\\le x<2\\pi$ is $f(x)=0$?'%(a,fn,b,('+' if d>0 else '-')+sx(abs(d)))
    n=2*b
    c='$%d$'%n
    tr=[('$2$','$%dx$ runs through $%d$ full revolutions on $[0,2\\pi)$, each with two solutions.'%(b,b)),('$%d$'%b,'Each revolution gives two solutions, not one.'),('$%d$'%(4*b),'Counted solutions for $%dx$ on $[0,4\\pi)$.'%b)]
    st=['$\\%s(%dx)=%s$.'%(fn,b,sx(k)),'As $x$ goes from $0$ to $2\\pi$, $%dx$ goes from $0$ to $%d\\pi$: $%d$ revolutions.'%(b,2*b,b),'Two solutions per revolution: $%d$.'%n]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.10')
def t(r):
    fn=r.choice(['sin','cos']); k=r.choice([sp.Rational(1,2),sp.sqrt(2)/2,sp.sqrt(3)/2]); sign=r.choice(['>','<'])
    S=(SOLS if fn=='sin' else CSOLS)[k]
    q='Solve $\\%s x%s%s$ for $0\\le x<2\\pi$.'%(fn,sign,sx(k))
    if fn=='sin':
        inside='$%s<x<%s$'%S; outside='$0\\le x<%s$ or $%s<x<2\\pi$'%S
    else:
        inside='$0\\le x<%s$ or $%s<x<2\\pi$'%S; outside='$%s<x<%s$'%S
    c=inside if sign=='>' else outside
    w=outside if sign=='>' else inside
    tr=[(w,'Chose the region where $\\%s x%s%s$; sketch the graph and the line $y=%s$.'%(fn,'<' if sign=='>' else '>',sx(k),sx(k))),(c.replace('<x<','\\le x\\le') if '<x<' in c else c.replace('x<','x\\le'),'The inequality is strict, so the endpoints are excluded.'),('$x>%s$'%S[0],'Only the first boundary was used; the graph crosses the line twice.')]
    st=['$\\%s x=%s$ at $x=%s$ and $x=%s$.'%(fn,sx(k),S[0],S[1]),'From the graph, $\\%s x%s%s$ on %s.'%(fn,sign,sx(k),c)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.10','Hard')
def t(r):
    fn=r.choice(['sin','cos']); a=r.choice([2]); 
    q='What are all solutions of $2\\%s^{2}x=\\%s x$ on $0\\le x<2\\pi$?'%(fn,fn)
    if fn=='sin': z='0,\\ \\pi'; h='\\dfrac{\\pi}{6},\\ \\dfrac{5\\pi}{6}'
    else: z='\\dfrac{\\pi}{2},\\ \\dfrac{3\\pi}{2}'; h='\\dfrac{\\pi}{3},\\ \\dfrac{5\\pi}{3}'
    c='$x=%s,\\ %s$'%(z,h)
    tr=[('$x=%s$'%h,'Dividing by $\\%s x$ loses the solutions where $\\%s x=0$; factor instead.'%(fn,fn)),('$x=%s$'%z,'Lost the factor $2\\%s x-1=0$.'%fn),('$x=%s,\\ %s$'%(z,'\\dfrac{\\pi}{3},\\ \\dfrac{2\\pi}{3}' if fn=='sin' else '\\dfrac{\\pi}{6},\\ \\dfrac{11\\pi}{6}'),'Solved $\\%s x=\\dfrac{1}{2}$ with the wrong unit-circle values.'%fn)]
    st=['$\\%s x(2\\%s x-1)=0$.'%(fn,fn),'$\\%s x=0$: $x=%s$. $\\%s x=\\dfrac{1}{2}$: $x=%s$.'%(fn,z,fn,h)]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 3.11 sec csc cot ----------
@reg('3.11')
def t(r):
    fn=r.choice(['sec','csc','cot'])
    a=r.choice([sp.Rational(k,6)*PI for k in (1,2,4,5,7,8,10,11)]+[sp.Rational(k,4)*PI for k in (1,3,5,7)])
    F={'sec':lambda t:1/sp.cos(t),'csc':lambda t:1/sp.sin(t),'cot':lambda t:sp.cos(t)/sp.sin(t)}[fn]
    base={'sec':sp.cos,'csc':sp.sin,'cot':sp.tan}[fn]
    v=sp.nsimplify(sp.radsimp(F(a)))
    q='What is the exact value of $\\%s\\left(%s\\right)$?'%(fn,ang(a))
    c='$%s$'%sx(v)
    cand=[(sp.nsimplify(base(a)),'That is $\\%s$; take the reciprocal.'%{'sec':'cos','csc':'sin','cot':'tan'}[fn]),(-v,'Sign error: the sign matches $\\%s$ in this quadrant.'%{'sec':'cos','csc':'sin','cot':'tan'}[fn]),(sp.nsimplify(sp.radsimp({'sec':1/sp.sin(a),'csc':1/sp.cos(a),'cot':sp.tan(a)}[fn])),'Paired with the wrong function: $\\sec=\\frac{1}{\\cos}$, $\\csc=\\frac{1}{\\sin}$, $\\cot=\\frac{\\cos}{\\sin}$.')]
    tr=[];seen={sx(v)}
    for val,w in cand:
        s_=sx(val)
        if s_ not in seen and len(tr)<3: tr.append(('$%s$'%s_,w)); seen.add(s_)
    if len(tr)<3: tr.append(('$%s$'%sx(sp.nsimplify(-base(a))),'Took the opposite instead of the reciprocal.'))
    if len(tr)<3 or len({t_[0] for t_ in tr}|{c})<4: raise Bad
    st=['$\\%s\\theta=%s$.'%(fn,{'sec':'\\dfrac{1}{\\cos\\theta}','csc':'\\dfrac{1}{\\sin\\theta}','cot':'\\dfrac{\\cos\\theta}{\\sin\\theta}'}[fn]),'$=%s$.'%sx(v)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.11')
def t(r):
    fn=r.choice(['sec','csc','cot'])
    va={'sec':'x=\\dfrac{\\pi}{2}+\\pi k','csc':'x=\\pi k','cot':'x=\\pi k'}
    q='Where are the vertical asymptotes of $f(x)=\\%s x$? ($k$ is any integer.)'%fn
    c='$%s$'%va[fn]
    pool=['x=\\dfrac{\\pi}{2}+\\pi k','x=\\pi k','x=2\\pi k','x=\\dfrac{\\pi}{4}+\\pi k']
    tr=[]
    for p in pool:
        if p!=va[fn] and len(tr)<3: tr.append(('$%s$'%p,{'x=\\dfrac{\\pi}{2}+\\pi k':'These are the zeros of $\\cos x$ (asymptotes of $\\sec$ and $\\tan$).','x=\\pi k':'These are the zeros of $\\sin x$ (asymptotes of $\\csc$ and $\\cot$).','x=2\\pi k':'Asymptotes repeat every $\\pi$, not $2\\pi$.','x=\\dfrac{\\pi}{4}+\\pi k':'Asymptotes are where the denominator is $0$.'}[p]))
    st=['$\\%s x$ has denominator $%s$.'%(fn,'\\cos x' if fn=='sec' else '\\sin x'),'It is $0$ at $%s$.'%va[fn]]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.11')
def t(r):
    a=r.choice([2,3,4]); d=r.choice([-3,-1,1,2,5]); fn=r.choice(['sec','csc'])
    q='What is the range of $f(x)=%d\\%s x%s$?'%(a,fn,term(d,0))
    c='$(-\\infty,%d]\\cup[%d,\\infty)$'%(d-a,d+a)
    tr=[('$[%d,\\ %d]$'%(d-a,d+a),'That is the range of $%d\\%s x%s$; reciprocals lie outside it.'%(a,'cos' if fn=='sec' else 'sin',term(d,0))),('$(-\\infty,%d]\\cup[%d,\\infty)$'%(-a,a),'Forgot the vertical shift $%d$.'%d),('All real numbers','$|\\%s x|\\ge1$, so the outputs skip an interval.'%fn)]
    st=['$\\%s x\\le-1$ or $\\%s x\\ge1$.'%(fn,fn),'Multiply by $%d$ and add $%d$: $y\\le%d$ or $y\\ge%d$.'%(a,d,d-a,d+a)]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 3.12 identities ----------
IDS=[('\\tan x\\cos x','\\sin x',['\\cos x','\\tan x','1']),('\\dfrac{1-\\cos^{2}x}{\\sin x}','\\sin x',['\\cos x','1-\\cos x','\\csc x']),
     ('\\dfrac{\\csc^{2}x}{\\sec^{2}x}','\\cot^{2}x',['\\tan^{2}x','\\cos^{2}x','\\sin^{2}x']),('\\dfrac{1-\\cos^{2}x}{\\cos^{2}x}+1','\\sec^{2}x',['\\tan^{2}x','\\csc^{2}x','\\cot^{2}x']),
     ('\\dfrac{\\csc\\theta\\cot\\theta\\sin\\theta}{\\cos\\theta}','\\csc\\theta',['\\sec\\theta','\\sin\\theta','\\tan\\theta']),('(1-\\sin^{2}x)\\tan^{2}x','\\sin^{2}x',['\\cos^{2}x','\\tan^{2}x','1']),
     ('\\dfrac{\\sec^{2}x-1}{\\sin^{2}x}','\\sec^{2}x',['\\tan^{2}x','1','\\csc^{2}x']),('\\cot^{2}\\theta(1-\\cos^{2}\\theta)','\\cos^{2}\\theta',['\\sin^{2}\\theta','\\cot^{2}\\theta','1'])]
@reg('3.12')
def t(r):
    e,ans,bad=r.choice(IDS)
    q='Which single trigonometric expression is equivalent to $%s$ (where defined)?'%e
    c='$%s$'%ans
    why=['Rewrite everything in $\\sin$ and $\\cos$ before cancelling.','Use $\\sin^{2}x+\\cos^{2}x=1$ in the form that matches the expression.','Cancelled a factor that appears only once.']
    tr=[('$%s$'%b_,w) for b_,w in zip(bad,why)]
    st=['Rewrite in $\\sin$ and $\\cos$; replace squared terms using $\\sin^{2}x+\\cos^{2}x=1$.','Simplify: $%s$.'%ans]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.12','Hard')
def t(r):
    A=r.choice([PI/4,PI/3,PI/6]); B=r.choice([PI/4,PI/3,PI/6,2*PI/3,5*PI/6,3*PI/4]); op=r.choice(['+','-']); fn=r.choice(['sin','cos'])
    if A==B: raise Bad
    tot=A+B if op=='+' else A-B
    F={'sin':sp.sin,'cos':sp.cos}[fn]
    v=sp.nsimplify(sp.radsimp(sp.expand_trig(F(tot))))
    q='What is the exact value of $\\%s\\left(%s%s%s\\right)$?'%(fn,ang(A),op,ang(B))
    c='$%s$'%sx(v)
    naive=sp.nsimplify(F(A)+F(B)) if op=='+' else sp.nsimplify(F(A)-F(B))
    sw=sp.nsimplify(sp.radsimp(sp.expand_trig(F(A-B if op=='+' else A+B))))
    cand=[(naive,'$\\%s(A%sB)\\ne\\%s A%s\\%s B$; use the sum/difference identity.'%(fn,op,fn,op,fn)),(sw,'Used the wrong sign in the identity.'),(-v,'Sign error.'),(sp.nsimplify(sp.radsimp(sp.expand_trig((sp.cos if fn=='sin' else sp.sin)(tot)))),'Used the identity for the other function.')]
    tr=[];seen={sx(v)}
    for val,w in cand:
        s_=sx(sp.radsimp(val))
        if s_ not in seen and len(tr)<3: tr.append(('$%s$'%s_,w)); seen.add(s_)
    if len(tr)<3: raise Bad
    idt={'sin':'\\sin A\\cos B%s\\cos A\\sin B'%op,'cos':'\\cos A\\cos B%s\\sin A\\sin B'%('-' if op=='+' else '+')}[fn]
    st=['$\\%s(A%sB)=%s$.'%(fn,op,idt),'Substitute unit-circle values: $%s$.'%sx(v)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.12')
def t(r):
    a,b,h=r.choice([(3,4,5),(5,12,13),(8,15,17)])
    giv=r.choice(['sin','cos']); s=Fr(a,h) if giv=='sin' else Fr(b,h)
    q='If $\\%s\\theta=%s$, what is $\\cos(2\\theta)$?'%(giv,fx(s))
    v=1-2*s*s if giv=='sin' else 2*s*s-1
    c='$%s$'%fx(v)
    other=Fr(b,h) if giv=='sin' else Fr(a,h)
    tr=[('$%s$'%fx(2*s),'$\\cos(2\\theta)\\ne2\\%s\\theta$; use a double-angle identity.'%giv),('$%s$'%fx(-v),'Used the wrong form: $\\cos2\\theta=1-2\\sin^{2}\\theta=2\\cos^{2}\\theta-1$.'),('$%s$'%fx(2*s*other),'That is $|\\sin(2\\theta)|=2|\\sin\\theta\\cos\\theta|$.')]
    st=['$\\cos(2\\theta)=%s$.'%('1-2\\sin^{2}\\theta' if giv=='sin' else '2\\cos^{2}\\theta-1'),'$=%s$.'%fx(v)]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 3.13 polar coordinates and complex numbers ----------
@reg('3.13')
def t(r):
    a=r.choice([sp.Rational(k,6)*PI for k in (1,2,4,5,7,8,10,11)]+[sp.Rational(k,4)*PI for k in (1,3,5,7)]); R=r.choice([2,4,5,6])
    x=sp.nsimplify(R*sp.cos(a)); y=sp.nsimplify(R*sp.sin(a))
    q='Convert the polar point $\\left(%d,\\ %s\\right)$ to rectangular coordinates.'%(R,ang(a))
    P=lambda u,v:'$\\left(%s,\\ %s\\right)$'%(sx(u),sx(v))
    c=P(x,y)
    tr=[(P(y,x),'Swapped: $x=r\\cos\\theta$, $y=r\\sin\\theta$.'),(P(-x,-y),'Sign error: plot the angle first.'),(P(sp.cos(a),sp.sin(a)),'Forgot to multiply by $r=%d$.'%R)]
    st=['$x=%d\\cos%s=%s$.'%(R,ang(a),sx(x)),'$y=%d\\sin%s=%s$.'%(R,ang(a),sx(y))]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.13','Hard','Calculator')
def t(r):
    x=r.choice([-5,-4,-3,-2,2,3,4]); y=r.choice([-6,-5,-4,-2,1,3,5])
    if x>0 and y>0: raise Bad
    R=math.hypot(x,y); th=math.atan2(y,x)%(2*math.pi); naive=math.atan(y/x)
    q='Convert $(%d,%d)$ to polar coordinates $(r,\\theta)$ with $r>0$ and $0\\le\\theta<2\\pi$. Round to three decimal places.'%(x,y)
    rs=sx(sp.sqrt(x*x+y*y))
    c='$\\left(%s,\\ %s\\right)$'%(rs,num(th))
    tr=[('$\\left(%s,\\ %s\\right)$'%(rs,num(naive)),'$\\tan^{-1}\\dfrac{y}{x}$ gives a quadrant I or IV angle; adjust for the quadrant of the point.'),('$\\left(%s,\\ %s\\right)$'%(rs,num(naive%(2*math.pi)) if (naive%(2*math.pi))!=th else num(th+math.pi/2)),'Added $2\\pi$ but the point is not in that quadrant; add $\\pi$ when $x<0$.'),('$\\left(%d,\\ %s\\right)$'%(abs(x)+abs(y),num(th)),'$r=\\sqrt{x^{2}+y^{2}}$, not $|x|+|y|$.')]
    st=['$r=\\sqrt{(%d)^{2}+(%d)^{2}}=%s$.'%(x,y,rs),'Point in quadrant %s: $\\theta\\approx%s$.'%({(True,True):'I',(False,True):'II',(False,False):'III',(True,False):'IV'}[(x>0,y>0)],num(th))]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.13')
def t(r):
    R=r.choice([2,3,4,5]); a=r.choice([PI/6,PI/4,PI/3,2*PI/3,3*PI/4])
    q='The point $A$ has polar coordinates $\\left(%d,\\ %s\\right)$. Which also gives the location of $A$?'%(R,ang(a))
    c='$\\left(-%d,\\ %s\\right)$'%(R,ang(a+PI))
    tr=[('$\\left(-%d,\\ %s\\right)$'%(R,ang(a)),'A negative $r$ points the opposite way; the angle must also change by $\\pi$.'),('$\\left(%d,\\ %s\\right)$'%(R,ang(a+PI)),'Adding $\\pi$ with positive $r$ gives the opposite point.'),('$\\left(%d,\\ %s\\right)$'%(R,ang(-a)),'Negating the angle reflects the point over the polar axis.')]
    st=['$(r,\\theta)$ and $(-r,\\theta+\\pi)$ name the same point.','So $\\left(-%d,\\ %s\\right)$.'%(R,ang(a+PI))]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.13')
def t(r):
    a=r.choice([sp.Rational(k,6)*PI for k in (1,2,4,5,7,8,10,11)]+[sp.Rational(k,4)*PI for k in (1,3,5,7)]); R=r.choice([2,4,6])
    x=sp.nsimplify(R*sp.cos(a)); y=sp.nsimplify(R*sp.sin(a))
    z='%s%s%si'%(sx(x),'+' if y>=0 else '-',sx(abs(y)) if abs(y)!=1 else '')
    q='Which is the polar form of the complex number $%s$?'%z
    F=lambda rr,aa:'$%s\\left(\\cos%s+i\\sin%s\\right)$'%(rr,ang(aa),ang(aa))
    ref=sp.atan(abs(y/x)) if x!=0 else PI/2
    c=F(R,a)
    wr=[v for v in (ref,PI-ref,PI+ref,2*PI-ref) if sp.simplify(v-a)!=0]
    tr=[(F(R,wr[0]),'Used the reference angle in the wrong quadrant.'),(F(R*R,a),'$|z|=\\sqrt{a^{2}+b^{2}}=%d$, not $%d$.'%(R,R*R)),(F(R,wr[1]),'Check the signs of the real and imaginary parts.')]
    st=['$|z|=\\sqrt{(%s)^{2}+(%s)^{2}}=%d$.'%(sx(x),sx(y),R),'$\\cos\\theta=%s$, $\\sin\\theta=%s$, so $\\theta=%s$.'%(sx(x/R),sx(y/R),ang(a))]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 3.14 polar graphs ----------
@reg('3.14')
def t(r):
    a=r.choice([2,3,4,5,6,8]); n=r.choice([2,3,4,5,6,7]); fn=r.choice(['sin','cos'])
    q='How many petals does the graph of $r=%d\\%s(%d\\theta)$ have?'%(a,fn,n)
    p=n if n%2 else 2*n
    c='$%d$'%p
    tr=[('$%d$'%(2*n if n%2 else n),'Odd $n$ gives $n$ petals; even $n$ gives $2n$ petals.'),('$%d$'%a,'$a$ is the petal length, not the number of petals.'),('$%d$'%(p+1 if p+1!=a else p+2),'Miscounted: apply the odd/even rule for $n$.')]
    st=['$n=%d$ is %s.'%(n,'odd' if n%2 else 'even'),'Number of petals: $%d$.'%p]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.14')
def t(r):
    kind=r.choice(['card','loop','dimp'])
    b=r.choice([2,3,4,5])
    a={'card':b,'loop':b-r.choice([1,2]) if b>2 else 1,'dimp':b+1}[kind]
    if a<=0: raise Bad
    fn=r.choice(['sin','cos']); sg=r.choice(['+','-'])
    q='The polar graph $r=%d%s%d\\%s\\theta$ is which type of curve?'%(a,sg,b,fn)
    names={'card':'A cardioid','loop':'A limaçon with an inner loop','dimp':'A dimpled limaçon (no inner loop)','rose':'A rose curve'}
    c=names[kind]
    why={'card':'A cardioid needs $a=b$.','loop':'An inner loop needs $a<b$.','dimp':'A dimpled limaçon has $a>b$.','rose':'A rose has the form $a\\cos(n\\theta)$ with no constant term.'}
    tr=[(names[k],why[k]) for k in ('card','loop','dimp','rose') if k!=kind][:3]
    st=['Compare $a=%d$ with $b=%d$.'%(a,b),'%s.'%c]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.14')
def t(r):
    a=r.choice([2,3,4,5]); b=r.choice([2,3,6,7]); fn=r.choice(['sin','cos'])
    sg=r.choice(['+','-'])
    q='What is the greatest distance from the pole to the graph of $r=%d%s%d\\%s\\theta$?'%(a,sg,b,fn)
    c='$%d$'%(a+b)
    tr=[('$%d$'%a,'The constant alone is the distance where $\\%s\\theta=0$.'%fn),('$%d$'%abs(a-b),'Distance is $|r|$; the greatest value of $|r|$ is $a+b$.'),('$%d$'%(2*(a+b)),'That is the width of the curve, not the distance from the pole.')]
    if abs(a-b)==a: raise Bad
    st=['$\\%s\\theta$ ranges over $[-1,1]$.'%fn,'$|r|$ is greatest when $%s%d\\%s\\theta=%d$: distance $%d$.'%(sg,b,fn,b,a+b)]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 3.15 rates of change in polar ----------
@reg('3.15','Medium','Calculator')
def t(r):
    a=r.choice([2,3,4]); b=r.choice([3,5,6]); A,B=r.choice([(PI/6,PI/2),(0,PI/3),(PI/4,PI/2),(0,PI/6)])
    f=lambda t:a+b*sp.sin(t)
    v=sp.nsimplify((f(B)-f(A))/(B-A))
    q='For $r=f(\\theta)=%d+%d\\sin\\theta$, what is the average rate of change of $r$ on $%s\\le\\theta\\le%s$?'%(a,b,ang(A),ang(B))
    c='$%s\\approx%s$'%(sx(v),num(float(v)))
    tr=[('$%s$'%sx(sp.nsimplify(f(B)-f(A))),'Found the change in $r$ but did not divide by the change in $\\theta$.'),('$%s$'%num(float((B-A)/(f(B)-f(A)))),'Inverted the ratio: $\\dfrac{\\Delta r}{\\Delta\\theta}$.'),('$%s$'%num(float((f(B)-f(A))/((B-A)*180/PI))),'Measured $\\theta$ in degrees.')]
    st=['$f(%s)=%s$, $f(%s)=%s$.'%(ang(A),sx(f(A)),ang(B),sx(f(B))),'$\\dfrac{%s-%s}{%s-%s}=%s\\approx%s$.'%(sx(f(B)),sx(f(A)),ang(B),ang(A),sx(v),num(float(v)))]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.15','Hard')
def t(r):
    pos=r.choice([True,False]); inc=r.choice([True,False])
    q='On an interval, the polar function $r=f(\\theta)$ is %s and %s. What happens to the distance between the point $(f(\\theta),\\theta)$ and the pole?'%('positive' if pos else 'negative','increasing' if inc else 'decreasing')
    away=(pos==inc)
    c='The distance is %s.'%('increasing' if away else 'decreasing')
    tr=[('The distance is %s.'%('decreasing' if away else 'increasing'),'Distance is $|r|$: when $r<0$, increasing $r$ moves toward $0$.' if not pos else 'Distance is $|r|$; with $r>0$ it follows $r$.'),('The distance is constant.','The distance $|r|$ changes whenever $r$ changes.'),('It cannot be determined without a graph.','The sign of $r$ and whether $r$ increases decide $|r|$.')]
    st=['Distance from the pole $=|r|$.','$r$ %s and %s: $|r|$ is %s.'%('positive' if pos else 'negative','increasing' if inc else 'decreasing','increasing' if away else 'decreasing')]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('3.15','Medium','Calculator')
def t(r):
    a=r.choice([4,5,6,8]); fn=r.choice(['sin','cos']); n=r.choice([1,2])
    F=(sp.sin if fn=='sin' else sp.cos)
    f=lambda t:a*F(n*t)
    t0,t1=0,PI/4; tm=PI/8
    est=float(f(t0)+(f(t1)-f(t0))/(t1-t0)*(tm-t0))
    act=float(f(tm))
    q='For $r=%d\\%s(%s\\theta)$, estimate $f\\left(\\dfrac{\\pi}{8}\\right)$ using the average rate of change on $0\\le\\theta\\le\\dfrac{\\pi}{4}$. Round to three decimal places.'%(a,fn,'' if n==1 else str(n))
    c='$%s$'%num(est)
    tr=[('$%s$'%num(act),'That is the actual value, not the linear estimate.'),('$%s$'%num(float((f(t1)-f(t0))/(t1-t0))),'Reported the rate of change, not the estimated value.'),('$%s$'%num(float(f(t0)+(f(t1)-f(t0))/(t1-t0)*(t1-t0)+(1 if a==8 else 0)*0)) if abs(float(f(t1))-est)>1e-6 else '$%s$'%num(est+1),'Stepped across the whole interval instead of $\\dfrac{\\pi}{8}$.')]
    st=['AROC $=\\dfrac{f(\\pi/4)-f(0)}{\\pi/4}\\approx%s$.'%num(float((f(t1)-f(t0))/(t1-t0))),'$f(\\pi/8)\\approx f(0)+\\text{AROC}\\cdot\\dfrac{\\pi}{8}\\approx%s$.'%num(est)]
    return dict(q=q,c=c,tr=tr,st=st)
