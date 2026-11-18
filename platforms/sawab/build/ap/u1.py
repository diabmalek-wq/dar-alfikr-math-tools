from common import *

# ---------- 1.1 Change in Tandem ----------
@reg('1.1')
def t(r):
    xs=sorted(r.sample(range(-8,10),5)); ys=sorted(r.sample(range(-20,25),5),reverse=True)
    k=r.choice([1,2,3]); a,b=ys[k-1],ys[k+1]
    rows=' & '.join('$%d$'%x for x in xs); vals=' & '.join('$a$' if i==k else '$%d$'%y for i,y in enumerate(ys))
    q=('The function $f$ is decreasing for all real numbers. Selected values are $f(%d)=%d$, $f(%d)=%d$, $f(%d)=a$, $f(%d)=%d$ and $f(%d)=%d$. '
       'Which of the following gives all possible values of $a$?')%(xs[0],ys[0],xs[1],ys[1] if k!=1 else ys[0],xs[k],xs[3],ys[3],xs[4],ys[4])
    # rebuild cleanly so the missing slot is xs[k]
    parts=[]
    for i in range(5):
        parts.append('$f(%d)=%s$'%(xs[i],'a' if i==k else str(ys[i])))
    q='The function $f$ is decreasing for all real numbers. Selected values are '+', '.join(parts)+'. Which of the following gives all possible values of $a$?'
    c='$%d<a<%d$'%(b,a)
    tr=[('$%d<a<%d$'%(xs[k-1],xs[k+1]),'Used the neighbouring input values, not the neighbouring output values.'),
        ('$%d<a<%d$'%(ys[4],ys[0]),'Used the smallest and largest outputs in the table instead of the two neighbours of the missing value.'),
        ('$%d<a<%d$'%(a,a+abs(a-b)),'Treated $f$ as increasing, so placed $a$ above the earlier output.')]
    st=['Decreasing means: if $p<q$ then $f(p)>f(q)$.','The missing input $%d$ lies between $%d$ and $%d$.'%(xs[k],xs[k-1],xs[k+1]),
        'So $f(%d)>a>f(%d)$, which gives $%d>a>%d$.'%(xs[k-1],xs[k+1],a,b)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('1.1')
def t(r):
    inc=r.random()<.5
    x0=r.randrange(1,10); h=r.choice([2,3,5]); xs=[x0+h*i for i in range(5)]
    d=sorted(r.sample(range(1,15),4),reverse=r.random()<.5)
    y=[r.randrange(-10,30)]
    for v in d: y.append(y[-1]+(v if inc else -v))
    tab='; '.join('$f(%d)=%d$'%(a,b) for a,b in zip(xs,y))
    q='The function $f$ is either increasing or decreasing on $%d\\le x\\le %d$, but not both. Values: %s. Which statement is correct?'%(xs[0],xs[-1],tab)
    w='increasing' if inc else 'decreasing'; o='decreasing' if inc else 'increasing'
    rel='<' if inc else '>'
    c='$f$ is %s, because for all $a<b$ in the interval, $f(a)%sf(b)$.'%(w,rel)
    tr=[('$f$ is %s, because the outputs change by different amounts.'%o,'Confused the size of the change (the rate) with the direction of change.'),
        ('$f$ is %s, because the inputs increase.'%w,'A correct conclusion with a wrong reason: the inputs always increase; the outputs decide.'),
        ('$f$ cannot be classified, because the output changes are not constant.','Constant change is needed for a linear function, not for increasing or decreasing.')]
    st=['Read the outputs from left to right: %s.'%', '.join('$%d$'%v for v in y),'Every output is %s than the one before.'%('greater' if inc else 'less'),
        'So for all $a<b$, $f(a)%sf(b)$: $f$ is %s.'%(rel,w)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('1.1')
def t(r):
    inc=r.random()<.5; up=r.random()<.5
    base=r.randrange(5,30); h=r.choice([1,2])
    d=sorted(r.sample(range(1,12),4)); 
    if not up: d=d[::-1]
    # increasing: diffs positive; concave up => diffs increasing
    if not inc: d=[-v for v in (d[::-1])]
    y=[base]
    for v in d: y.append(y[-1]+v)
    xs=[h*i for i in range(5)]
    tab='; '.join('$g(%d)=%d$'%(a,b) for a,b in zip(xs,y))
    q='Values of $g$ at equally spaced inputs are %s. The graph of $g$ has no inflection point on this interval. Which best describes $g$?'%tab
    dif=[y[i+1]-y[i] for i in range(4)]
    incr=dif[1]>dif[0]
    w=('increasing' if inc else 'decreasing')+' at '+('an increasing' if incr else 'a decreasing')+' rate'
    cu='concave up' if incr else 'concave down'
    c='$g$ is %s and the graph is %s.'%( 'increasing' if inc else 'decreasing',cu)
    other='concave down' if incr else 'concave up'
    tr=[('$g$ is %s and the graph is %s.'%('increasing' if inc else 'decreasing',other),'Read concavity from the size of the changes instead of whether the changes grow or shrink (as signed numbers).'),
        ('$g$ is %s and the graph is %s.'%('decreasing' if inc else 'increasing',cu),'Direction error: compare each output with the one before it.'),
        ('$g$ is %s and the graph is %s.'%('decreasing' if inc else 'increasing',other),'Both the direction and the concavity are reversed.')]
    st=['Successive changes: %s.'%', '.join('$%d$'%v for v in dif),
        'The changes are %s, so $g$ is %s.'%('positive' if inc else 'negative','increasing' if inc else 'decreasing'),
        'As signed numbers the changes are %s, so the rate of change is %s and the graph is %s.'%('increasing' if incr else 'decreasing','increasing' if incr else 'decreasing',cu)]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 1.2 Rates of Change ----------
@reg('1.2')
def t(r):
    ts=sorted(r.sample(range(1,60),4)); ds=[r.randrange(5,150) for _ in ts]
    i,j=0,r.choice([2,3])
    unit=pick(r,[('seconds','meters'),('minutes','liters'),('hours','kilometers')]); what=pick(r,['The table gives the amount $d(t)$','A sensor records the quantity $d(t)$'])
    tab='; '.join('$d(%d)=%d$'%(a,b) for a,b in zip(ts,ds))
    q=what+', in %s, at selected times $t$, in %s: %s. What is the average rate of change of $d$ on $%d\\le t\\le %d$?'%(unit[1],unit[0],tab,ts[i],ts[j])
    v=Fr(ds[j]-ds[i],ts[j]-ts[i])
    if v==0: raise Bad
    c='$%s$ %s per %s'%(fx(v),unit[1],unit[0][:-1])
    tr=[('$%s$ %s per %s'%(fx(1/v),unit[1],unit[0][:-1]),'Divided the change in input by the change in output; outputs go in the numerator.'),
        ('$%s$ %s per %s'%(fx(-v),unit[1],unit[0][:-1]),'Subtracted in opposite orders on top and bottom.'),
        ('$%s$ %s per %s'%(fx(Fr(ds[j]-ds[j-1],ts[j]-ts[j-1])),unit[1],unit[0][:-1]),'Used only the last step of the table, not the whole interval.')]
    st=['Average rate of change $=\\dfrac{d(%d)-d(%d)}{%d-%d}$.'%(ts[j],ts[i],ts[j],ts[i]),'$=\\dfrac{%d-%d}{%d}=%s$.'%(ds[j],ds[i],ts[j]-ts[i],fx(v)),'Units: %s per %s.'%(unit[1],unit[0][:-1])]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('1.2')
def t(r):
    a=r.choice([-3,-2,-1,1,2,3]); b=r.randrange(-6,7); cc=r.randrange(-9,10)
    p=r.randrange(-4,3); q2=p+r.choice([2,3,4])
    f=lambda x:a*x*x+b*x+cc
    v=Fr(f(q2)-f(p),q2-p)
    q='What is the average rate of change of $h(t)=%s$ over the interval $%d\\le t\\le %d$?'%(poly([(a,2),(b,1),(cc,0)],'t'),p,q2)
    c='$%s$'%fx(v)
    tr=[('$%s$'%fx(f(q2)-f(p)),'Found the change in output but did not divide by the change in input.'),
        ('$%s$'%fx(Fr(f(q2)+f(p),2)),'Averaged the two output values; a rate of change compares changes.'),
        ('$%s$'%fx(Fr(f(p)-f(q2),q2-p)),'Reversed the order of subtraction in the numerator only.')]
    st=['$h(%d)=%d$ and $h(%d)=%d$.'%(q2,f(q2),p,f(p)),'AROC $=\\dfrac{h(%d)-h(%d)}{%d-(%d)}=\\dfrac{%d}{%d}=%s$.'%(q2,p,q2,p,f(q2)-f(p),q2-p,fx(v))]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('1.2')
def t(r):
    S=[('the number of hours a phone is used','its battery charge','neg'),('the number of tickets sold','the total revenue','pos'),
       ('the altitude of a climber','the air temperature','neg'),('the number of workers on a job','the time to finish the job','neg'),
       ('the time spent practising','the typing speed','pos'),('the price of an item','the number of items sold','neg'),
       ('the temperature outside','the number of people at the beach','pos'),('the distance from a speaker','the loudness heard','neg')]
    a,b,s=pick(r,S)
    q='As %s increases, %s %s. Which describes the rate of change of %s with respect to %s?'%(a,b,'decreases' if s=='neg' else 'increases',b,a)
    if s=='neg':
        c='Negative: as one quantity increases, the other decreases.'
        tr=[('Positive: both quantities are changing.','Any change is not a positive rate; the sign compares the directions of change.'),
            ('Negative: both quantities are decreasing.','Only one quantity decreases; the input is increasing.'),
            ('Zero: the two changes cancel out.','A zero rate means the output does not change at all.')]
    else:
        c='Positive: as one quantity increases, the other also increases.'
        tr=[('Negative: the second quantity depends on the first.','Dependence does not decide the sign; compare the directions of change.'),
            ('Positive: as one quantity increases, the other decreases.','That pairing describes a negative rate of change.'),
            ('Zero: the quantities change together at the same pace.','A zero rate means the output does not change.')]
    st=['Input: %s. Output: %s.'%(a,b),'Both change in the %s direction.'%('opposite' if s=='neg' else 'same'),'So the rate of change is %s.'%('negative' if s=='neg' else 'positive')]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 1.3 Linear and quadratic ----------
@reg('1.3')
def t(r):
    m=Fr(r.choice([-5,-4,-3,-2,2,3,4,5]),r.choice([1,1,2])); b0=r.randrange(-10,11)
    xs=sorted(r.sample(range(-8,9),2)); x3=r.choice([x for x in range(-12,16) if x not in xs])
    h=lambda x:m*x+b0
    if h(xs[0]).denominator!=1 or h(xs[1]).denominator!=1: raise Bad
    q='The function $h$ is linear, with $h(%d)=%s$ and $h(%d)=%s$. What is the value of $h(%d)$?'%(xs[0],fx(h(xs[0])),xs[1],fx(h(xs[1])),x3)
    c='$%s$'%fx(h(x3))
    tr=[('$%s$'%fx(h(xs[1])+(1/m)*(x3-xs[1])),'Used $\\dfrac{\\Delta x}{\\Delta y}$ as the slope.'),
        ('$%s$'%fx(m*x3),'Multiplied by the slope but forgot the starting value (the intercept).'),
        ('$%s$'%fx(h(xs[1])-m*(x3-xs[1])),'Moved in the wrong direction from the known point (sign error).')]
    st=['Slope $=\\dfrac{%s-(%s)}{%d-(%d)}=%s$.'%(fx(h(xs[1])),fx(h(xs[0])),xs[1],xs[0],fx(m)),
        '$h(%d)=h(%d)+\\left(%s\\right)(%d-%d)=%s$.'%(x3,xs[1],fx(m),x3,xs[1],fx(h(x3)))]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('1.3','Hard')
def t(r):
    p=r.randrange(-6,3); h=r.choice([2,3,4,5]); m1=r.randrange(-8,9); dm=r.choice([-6,-4,-3,-2,2,3,4,6])
    m2=m1+dm; m3=m2+dm
    q=('A quadratic function $g$ has average rate of change $%d$ on $%d\\le x\\le %d$ and average rate of change $%d$ on $%d\\le x\\le %d$. '
       'What is the average rate of change of $g$ on $%d\\le x\\le %d$?')%(m1,p,p+h,m2,p+h,p+2*h,p+2*h,p+3*h)
    c='$%d$'%m3
    tr=[('$%d$'%m2,'Assumed the average rate of change stays constant; that is true only for linear functions.'),
        ('$%d$'%dm,'Found the change in the rates but did not add it to the last rate.'),
        ('$%d$'%(m1+m2),'Added the two rates instead of continuing the constant change between them.')]
    st=['For a quadratic, consecutive equal-length intervals give average rates that change by a constant amount.','Change: $%d-(%d)=%d$.'%(m2,m1,dm),'Next rate: $%d+(%d)=%d$.'%(m2,dm,m3)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('1.3')
def t(r):
    a=r.choice([-5,-4,-3,-2,2,3,4,5]); b=r.randrange(-7,8); cc=r.randrange(-9,10); L_=r.choice([1,2])
    q='The function $f(x)=%s$. Over consecutive intervals of length $%d$, by how much does each average rate of change differ from the one before it?'%(poly([(a,2),(b,1),(cc,0)]),L_)
    v=2*a*L_*L_
    c='$%d$'%v
    tr=[('$%d$'%(a*L_*L_),'Forgot the factor $2$: for intervals of length $h$ the change is $2ah^{2}$.'),('$0$','Treated the quadratic as linear; only linear functions have constant average rates.'),('$%d$'%(2*a+b),'Mixed the linear coefficient into the constant change.')]
    st=['For $f(x)=ax^{2}+bx+c$, the average rate on $[x,x+h]$ is $a(2x+h)+b$.','Moving the interval right by $h$ adds $2ah\\cdot h=2ah^{2}$.','Here $2(%d)(%d)^{2}=%d$.'%(a,L_,v)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('1.3')
def t(r):
    up=r.random()<.5; x0=r.randrange(-10,5); h=r.choice([2,3,4])
    d=sorted(r.sample(range(-12,13),4))
    if not up: d=d[::-1]
    y=[r.randrange(-20,40)]
    for v in d: y.append(y[-1]+v)
    xs=[x0+h*i for i in range(5)]
    tab='; '.join('$g(%d)=%d$'%(a,b) for a,b in zip(xs,y))
    q='The concavity of $g$ does not change. Values: %s. Which conclusion is justified?'%tab
    cu='concave up' if up else 'concave down'; co='concave down' if up else 'concave up'
    c='$g$ is %s, because the average rates of change over consecutive equal-length intervals are %s.'%(cu,'increasing' if up else 'decreasing')
    tr=[('$g$ is %s, because the outputs are %s.'%(cu,'increasing' if y[-1]>y[0] else 'decreasing'),'Direction of the outputs does not decide concavity; compare the rates of change.'),
        ('$g$ is %s, because the average rates of change are %s.'%(co,'increasing' if up else 'decreasing'),'Increasing rates mean concave up; decreasing rates mean concave down.'),
        ('$g$ is linear, because the inputs are equally spaced.','Equal spacing lets you compare rates; it does not make the function linear.')]
    rates=[Fr(v,h) for v in d]
    st=['Average rates: %s.'%', '.join('$%s$'%fx(v) for v in rates),'They are %s.'%('increasing' if up else 'decreasing'),'So $g$ is %s.'%cu]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 1.4 Polynomial functions and rates of change ----------
@reg('1.4')
def t(r):
    pw=r.sample(range(0,8),4); cs=[r.choice([-9,-7,-5,-4,-3,-2,2,3,4,5,6,8,10]) for _ in pw]
    n=max(pw); lc=cs[pw.index(n)]
    if pw[0]==n: raise Bad
    big=max(cs,key=abs)
    if big==lc: raise Bad
    q='What are the degree and the leading coefficient of $p(x)=%s$?'%poly(list(zip(cs,pw)))
    c='Degree $%d$, leading coefficient $%d$'%(n,lc)
    tr=[('Degree $%d$, leading coefficient $%d$'%(pw[0],cs[0]),'Read the first term written; the leading term has the greatest exponent.'),
        ('Degree $%d$, leading coefficient $%d$'%(n,big),'Took the largest coefficient; the leading coefficient belongs to the term of highest degree.'),
        ('Degree $4$, leading coefficient $%d$'%lc,'Counted the number of terms instead of the greatest exponent.')]
    if n==4: raise Bad
    st=['The greatest exponent is $%d$, on the term $%s$.'%(n,term(lc,n,'x',True)),'Degree $%d$, leading coefficient $%d$.'%(n,lc)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('1.4')
def t(r):
    a=r.randrange(-8,-1); b=r.randrange(1,7); m=r.randrange(a+1,b); e=r.randrange(b+2,b+8)
    vm=r.choice([-7,-5,-3,3,5,8]); ve=r.choice([-4,-2,1,2,6])
    q='A polynomial function $f$ has $f(%d)=0$, $f(%d)=%d$, $f(%d)=0$ and $f(%d)=%d$. Which statement must be true?'%(a,m,vm,b,e,ve)
    c='$f$ has at least one local extremum on the interval $%d<x<%d$.'%(a,b)
    tr=[('$f$ has a local %s at $x=%d$.'%('maximum' if vm>0 else 'minimum',m),'A listed value need not be the extremum; only its existence between the zeros is guaranteed.'),
        ('$f$ has a local extremum on $%d<x<%d$.'%(b,e),'Between a zero and a nonzero value no turning point is guaranteed.'),
        ('No extremum is guaranteed, because the degree is unknown.','Between two real zeros of a nonconstant polynomial there is always a local extremum.')]
    st=['$x=%d$ and $x=%d$ are two zeros of a nonconstant polynomial.'%(a,b),'Between two distinct real zeros the graph must turn, so there is at least one local extremum on $%d<x<%d$.'%(a,b)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('1.4')
def t(r):
    k=r.choice([-4,-3,-2,2,3,5]); e1=r.choice([1,2,3]); e2=r.choice([1,2,3]); r1=r.randrange(-5,0); r2=r.randrange(1,6)
    flip=r.random()<.4
    n=e1+e2+(1 if flip else 0); lc=k*(-1 if flip else 1)
    f='%d%s^{%d}%s^{%d}%s'%(k,fac(r1),e1,fac(r2),e2,'(%d-x)'%r.randrange(1,9) if flip else '')
    f=f.replace('^{1}','')
    q='For $p(x)=%s$, which statement is true?'%f
    if n%2==0:
        ans='an absolute maximum' if lc<0 else 'an absolute minimum'
        c='$p$ has %s, because the leading term $%s$ has even degree and a %s coefficient.'%(ans,term(lc,n,'x',True),'negative' if lc<0 else 'positive')
        oth='an absolute minimum' if lc<0 else 'an absolute maximum'
        tr=[('$p$ has %s, because the leading term $%s$ has even degree.'%(oth,term(lc,n,'x',True)),'The sign of the leading coefficient decides max or min: positive opens up (min), negative opens down (max).'),
            ('$p$ has neither, because the degree is odd.','Add the multiplicities (and any extra factor): the degree is $%d$, which is even.'%n),
            ('$p$ has both an absolute maximum and an absolute minimum.','A nonconstant polynomial is unbounded in at least one direction.')]
    else:
        c='$p$ has neither an absolute maximum nor an absolute minimum, because its degree $%d$ is odd.'%n
        tr=[('$p$ has an absolute maximum, because $%d<0$.'%lc if lc<0 else '$p$ has an absolute minimum, because $%d>0$.'%lc,'With odd degree the two ends go in opposite directions, so there is no absolute extremum.'),
            ('$p$ has an absolute %s, because one factor is squared.'%('minimum' if lc>0 else 'maximum'),'A squared factor makes a bounce at a zero; it does not bound the whole graph.'),
            ('$p$ has both an absolute maximum and an absolute minimum.','A nonconstant polynomial is unbounded in at least one direction.')]
    st=['Leading term: multiply the leading terms of the factors: $%s$.'%term(lc,n,'x',True),'Degree $%d$ (%s), leading coefficient $%d$.'%(n,'even' if n%2==0 else 'odd',lc)]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 1.5 Complex zeros, even and odd ----------
@reg('1.5')
def t(r):
    z=r.sample(range(-15,17),3); m=[1,1,1]; i=r.randrange(3); m[i]=r.choice([2,3,4,5])
    s=sum(m); nr=r.choice([2,4,6]); n=s+nr
    q='A polynomial of degree $%d$ has real zeros only at $x=%d$, $x=%d$ and $x=%d$, where $x=%d$ has multiplicity $%d$ and the others have multiplicity $1$. How many non-real zeros does it have?'%(n,z[0],z[1],z[2],z[i],m[i])
    c='$%d$'%nr
    tr=[('$%d$'%(n-3),'Counted each real zero once; multiplicity counts toward the degree.'),('$%d$'%(nr+1),'Non-real zeros come in conjugate pairs, so the count must be even.'),('$0$','A degree-$n$ polynomial has exactly $n$ complex zeros counted with multiplicity.')]
    if n-3==nr+1: raise Bad
    st=['Real zeros counted with multiplicity: $%s=%d$.'%('+'.join(map(str,m)),s),'Non-real zeros: $%d-%d=%d$ (an even number, as conjugate pairs).'%(n,s,nr)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('1.5')
def t(r):
    a=r.choice([x for x in range(-9,10) if x]); b=r.choice([x for x in range(-9,10) if x not in (0,a,-a)])
    z=lambda x,y:'%s%s%si'%('' if x==0 else str(x),'+' if y>0 and x!=0 else ('-' if y<0 else ''),'' if abs(y)==1 else str(abs(y)))
    q='A polynomial with real coefficients has $%s$ as a zero. Which of the following must also be a zero?'%z(a,b)
    c='$%s$'%z(a,-b); tr=[('$%s$'%z(-a,b),'Changed the sign of the real part; the conjugate changes only the imaginary part.'),('$%s$'%z(-a,-b),'This is the opposite of the zero, not its conjugate.'),('$%s$'%z(b,a),'Swapped the real and imaginary parts.')]
    st=['Non-real zeros of a polynomial with real coefficients come in conjugate pairs.','The conjugate of $a+bi$ is $a-bi$, so $%s$ is also a zero.'%z(a,-b)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('1.5','Hard')
def t(r):
    n=r.choice([2,3,4]); cs=[r.choice([-3,-2,-1,1,2,3])]+[r.randrange(-5,6) for _ in range(n)]
    f=lambda x:sum(c*x**(n-i) for i,c in enumerate(cs))
    vals=[f(x) for x in range(8)]
    q='Input values $0,1,2,\\dots,7$ give outputs $%s$ for a polynomial function. What is its least possible degree?'%(',\\ '.join(map(str,vals)))
    c='$%d$'%n; tr=[('$%d$'%(n-1),'Stopped one level early: the degree is the level at which differences first become constant.'),('$%d$'%(n+1),'Went one level past the first constant row.'),('$%d$'%(n+2 if n<4 else 1),'Did not compute successive differences of equally spaced inputs.')]
    st=['Take successive differences of the outputs (the inputs are equally spaced).','The %s differences are the first constant row.'%(['','first','second','third','fourth'][n]),'So the degree is $%d$.'%n]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('1.5')
def t(r):
    kind=r.choice(['even','odd','neither'])
    if kind=='even': pw=sorted(r.sample([0,2,4,6],3),reverse=True)
    elif kind=='odd': pw=sorted(r.sample([1,3,5,7],3),reverse=True)
    else: pw=sorted(r.sample([1,2,3,4,5,6],2),reverse=True)+[0]; 
    if kind=='neither' and (all(p%2==0 for p in pw) or all(p%2 for p in pw)): raise Bad
    cs=[r.choice([-6,-5,-4,-3,-2,2,3,4,5,7]) for _ in pw]
    f=poly(list(zip(cs,pw)))
    q='Is $f(x)=%s$ even, odd, or neither?'%f
    E='Even, because $f(-x)=f(x)$ for all $x$.'; O='Odd, because $f(-x)=-f(x)$ for all $x$.'; N='Neither, because $f(-x)$ equals neither $f(x)$ nor $-f(x)$.'
    lead='Even, because the leading term has even degree.' if pw[0]%2==0 else 'Odd, because the leading term has odd degree.'
    c={'even':E,'odd':O,'neither':N}[kind]
    pool=[(E,'Check every term: $(-x)^{n}=x^{n}$ only for even $n$.'),(O,'Odd needs every term to have odd degree; a constant term is degree $0$ (even).'),(N,'Each term has the same parity of exponent, so $f(-x)$ is $f(x)$ or $-f(x)$.'),(lead,'One term does not decide symmetry; every term must match.')]
    tr=[p for p in pool if p[0]!=c][:3]
    st=['Substitute $-x$: even powers keep their sign, odd powers change sign.','Exponents: %s.'%', '.join(map(str,pw)),'Conclusion: %s'%c]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('1.5','Hard')
def t(r):
    a,b,c0=sorted(r.sample(range(-7,8),3)); sq=r.choice([a,b,c0]); others=[x for x in (a,b,c0) if x!=sq]
    sign=r.choice(['>','<'])
    f='%s^{2}%s%s'%(fac(sq),fac(others[0]),fac(others[1]))
    q='For $p(x)=%s$, on which intervals is $p(x)%s0$?'%(f,sign)
    pts=sorted([a,b,c0]); tests=[pts[0]-1,(pts[0]+pts[1])/2,(pts[1]+pts[2])/2,pts[2]+1]
    pv=lambda x:(x-sq)**2*(x-others[0])*(x-others[1])
    ints=['(-\\infty,%d)'%pts[0],'(%d,%d)'%(pts[0],pts[1]),'(%d,%d)'%(pts[1],pts[2]),'(%d,\\infty)'%pts[2]]
    intsC=['(-\\infty,%d]'%pts[0],'[%d,%d]'%(pts[0],pts[1]),'[%d,%d]'%(pts[1],pts[2]),'[%d,\\infty)'%pts[2]]
    ok=[ (pv(x)>0) if sign=='>' else (pv(x)<0) for x in tests]
    U=lambda m:'$'+'\\cup'.join(ints[i] for i in range(4) if m[i])+'$' if any(m) else '$\\varnothing$'
    alt=[True,False,True,False] if sign=='>' else [False,True,False,True]
    comp=[not x for x in ok]
    # include-zero trap: closed brackets
    cz=U(ok).replace('(-\\infty,%d)'%pts[0],'(-\\infty,%d]'%pts[0])
    c=U(ok)
    tr=[(U(comp),'Picked the intervals with the opposite sign.'),(U(alt) if U(alt)!=c else U([True,True,False,False]),'Assumed the sign changes at every zero; at the squared factor the graph bounces and keeps its sign.'),
        ('$'+'\\cup'.join(i for i,k in zip(intsC,ok) if k)+'$' if c!='$\\varnothing$' else '$(-\\infty,\\infty)$','Included a zero, where $p(x)=0$, in a strict inequality.')]
    st=['Zeros: $x=%d$ (multiplicity $2$), $x=%d$, $x=%d$.'%(sq,others[0],others[1]),'Test one value in each interval; the sign does not change at $x=%d$ (even multiplicity).'%sq,'$p(x)%s0$ on %s.'%(sign,c)]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 1.6 End behavior ----------
def lims(lc,n,f='p'):
    R='\\infty' if lc>0 else '-\\infty'
    Lf=R if n%2==0 else ('-\\infty' if lc>0 else '\\infty')
    return '$\\lim_{x\\to-\\infty}%s(x)=%s$ and $\\lim_{x\\to\\infty}%s(x)=%s$'%(f,Lf,f,R)
def limsLR(Lf,R,f='p'): return '$\\lim_{x\\to-\\infty}%s(x)=%s$ and $\\lim_{x\\to\\infty}%s(x)=%s$'%(f,Lf,f,R)
@reg('1.6')
def t(r):
    pw=r.sample(range(1,8),3); cs=[r.choice([-8,-6,-5,-3,-2,2,3,4,7,9]) for _ in pw]
    n=max(pw); lc=cs[pw.index(n)]
    if pw[0]==n: raise Bad
    I,M='\\infty','-\\infty'
    q='Which describes the end behavior of $p(x)=%s$?'%poly(list(zip(cs,pw))+[(r.randrange(-9,10),0)])
    c=lims(lc,n); allx=[limsLR(a,b) for a in (I,M) for b in (I,M)]
    wrong=[x for x in allx if x!=c]
    fl=lims(cs[0],pw[0])
    tr=[(wrong[0],'Check the leading term $%s$: degree $%d$ (%s), coefficient %s.'%(term(lc,n,'x',True),n,'even' if n%2==0 else 'odd','positive' if lc>0 else 'negative')),
        (wrong[1],'Used the first written term instead of the term with the greatest exponent.' if fl==wrong[1] else 'Reversed the behaviour on one side.'),(wrong[2],'Reversed the behaviour on one side.')]
    st=['Leading term: $%s$.'%term(lc,n,'x',True),'%s degree: the ends %s; coefficient %s: right end %s.'%('Even' if n%2==0 else 'Odd','match' if n%2==0 else 'are opposite','positive' if lc>0 else 'negative','up' if lc>0 else 'down'),c]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('1.6','Hard')
def t(r):
    k=r.choice([-3,-2,2,3,5]); e1,e2=r.choice([1,2,3]),r.choice([1,2])
    a1=r.randrange(1,8); a2=r.randrange(1,8)
    f='%d(x-%d)^{%d}(%d-x)^{%d}'%(k,a1,e1,a2,e2)
    n=e1+e2; lc=k*(-1)**e2
    q='The function $p(x)=%s$. Which describes its end behavior?'%f.replace('^{1}','')
    I,M='\\infty','-\\infty'
    c=lims(lc,n); allx=[limsLR(a,b) for a in (I,M) for b in (I,M)]
    w=[x for x in allx if x!=c]
    naive=lims(k,n)
    tr=[(naive if naive!=c else w[0],'The factor $(%d-x)$ has leading term $-x$; its sign must be included.'%a2),(w[1] if w[1]!=naive else w[2],'Reversed the behaviour on one side.'),(w[2] if w[2]!=naive else w[0],'Used the wrong degree: add the exponents of the factors.')]
    vals=[t_[0] for t_ in tr]
    if len(set(vals+[c]))<4: raise Bad
    st=['Leading term: $%d\\cdot x^{%d}\\cdot(-x)^{%d}=%s$.'%(k,e1,e2,term(lc,n,'x',True)),c]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('1.6')
def t(r):
    I,M='\\infty','-\\infty'
    Lf,R=r.choice([(I,I),(M,M),(M,I),(I,M)])
    n=r.choice([3,5]) if Lf!=R else r.choice([4,6]); lc=r.randrange(2,7)*(1 if R==I else -1)
    lower=r.randrange(1,n); lc2=r.choice([-7,-4,3,8])
    good='%s%s'%(term(lc,n,'x',True),term(lc2,lower))
    bads=['%s%s'%(term(-lc,n,'x',True),term(lc2,lower)),'%s%s'%(term(lc,n+1,'x',True),term(lc2,lower)),'%s%s'%(term(-abs(lc2) if lc>0 else abs(lc2),n+2,'x',True),term(lc,n))]
    q='A polynomial $p$ satisfies %s. Which could define $p$?'%limsLR(Lf,R)
    c='$p(x)=%s$'%good
    tr=[('$p(x)=%s$'%bads[0],'Opposite sign of the leading coefficient flips both ends.'),('$p(x)=%s$'%bads[1],'Changing the parity of the degree changes whether the ends match.'),('$p(x)=%s$'%bads[2],'The term of highest degree controls the end behavior, not the last term written.')]
    st=['%s ends: degree is %s.'%('Matching' if Lf==R else 'Opposite','even' if Lf==R else 'odd'),'Right end %s: leading coefficient %s.'%('up' if R==I else 'down','positive' if R==I else 'negative'),'Only $%s$ has this leading term.'%good]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 1.7 Rational functions and end behavior ----------
@reg('1.7')
def t(r):
    case=r.choice(['eq','lt','gt'])
    a=r.choice([-6,-4,-3,2,3,5,8]); b=r.choice([-5,-2,2,3,4,7])
    if case=='eq': n=m=r.choice([2,3])
    elif case=='lt': n,m=r.choice([(1,2),(2,3),(1,3)])
    else: n,m=r.choice([(3,2),(4,2),(3,1)])
    num=poly([(a,n),(r.randrange(-9,10),n-1),(r.randrange(-9,10),0)]); den=poly([(b,m),(r.randrange(-9,10),0)])
    q='Which describes the horizontal asymptote of the graph of $f(x)=\\dfrac{%s}{%s}$?'%(num,den)
    if case=='eq': c='$y=%s$'%fx(Fr(a,b)); tr=[('$y=0$','$y=0$ needs the denominator degree to be greater.'),('There is no horizontal asymptote.','Equal degrees give $y=$ the ratio of leading coefficients.'),('$y=%s$'%fx(Fr(b,a)),'Inverted the ratio of leading coefficients.')]
    elif case=='lt': c='$y=0$'; tr=[('$y=%s$'%fx(Fr(a,b)),'The ratio of leading coefficients applies only when the degrees are equal.'),('There is no horizontal asymptote.','When the denominator dominates, the outputs approach $0$.'),('$y=%s$'%fx(Fr(a,1)),'Read the numerator\'s leading coefficient alone.')]
    else: c='There is no horizontal asymptote.'; tr=[('$y=%s$'%fx(Fr(a,b)),'Equal degrees are needed for $y=\\dfrac{a}{b}$.'),('$y=0$','$y=0$ is for a denominator of greater degree; here the numerator dominates.'),('$x=%s$'%fx(Fr(a,b)),'A horizontal asymptote has the form $y=$ constant.')]
    st=['Numerator degree $%d$, denominator degree $%d$.'%(n,m),{'eq':'Equal degrees: $y=\\dfrac{%d}{%d}=%s$.'%(a,b,fx(Fr(a,b))),'lt':'Denominator dominates for inputs of large magnitude: $y=0$.','gt':'Numerator dominates: the outputs are unbounded, so no horizontal asymptote.'}[case]]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('1.7','Hard')
def t(r):
    a=r.choice([-5,-3,-2,2,3,4]); b=r.choice([-4,-3,-1,1,2,5]); n=r.choice([3,4]); m=n-r.choice([1,2])
    dirx=r.choice(['\\infty','-\\infty'])
    num=poly([(a,n),(r.randrange(-6,7),1)]); den=poly([(r.randrange(1,9),0),(b,m)])
    lead=Fr(a,b); p=n-m
    sgn=lead*((-1)**p if dirx=='-\\infty' else 1)
    ans='\\infty' if sgn>0 else '-\\infty'; opp='-\\infty' if ans=='\\infty' else '\\infty'
    q='What is $\\displaystyle\\lim_{x\\to%s}\\dfrac{%s}{%s}$?'%(dirx,num,den)
    c='$%s$'%ans
    tr=[('$%s$'%opp,'Sign error: the quotient of leading terms is $%s$, then substitute large %s $x$.'%(term(lead,p,'x',True),'negative' if dirx[0]=='-' else 'positive')),('$%s$'%fx(lead),'$\\dfrac{a}{b}$ is the limit only when the degrees are equal.'),('$0$','$0$ is the limit when the denominator has the greater degree.')]
    st=['For large $|x|$: $\\dfrac{%s}{%s}=%s$.'%(term(a,n,'x',True),term(b,m,'x',True),term(lead,p,'x',True)),'As $x\\to%s$, this goes to $%s$.'%(dirx,ans)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('1.7')
def t(r):
    p,q_=sorted(r.sample([x for x in range(-9,10) if x],2)); z=r.choice([x for x in range(-9,10) if x not in (p,q_)])
    s=-(p+q_); pr=p*q_
    den=poly([(1,2),(s,1),(pr,0)])
    q='What is the domain of $g(x)=\\dfrac{%s}{%s}$?'%(lin(1,-z),den)
    D=lambda a,b:'$(-\\infty,%d)\\cup(%d,%d)\\cup(%d,\\infty)$'%(a,a,b,b)
    c=D(p,q_)
    a2,b2=sorted([-p,-q_])
    tr=[(D(a2,b2),'Sign error: the factor $(x-a)$ is zero at $x=a$, not $x=-a$.'),('$(-\\infty,%d)\\cup(%d,\\infty)$'%(z,z),'Excluded the zero of the numerator; only zeros of the denominator are excluded.'),('$(-\\infty,\\infty)$','A rational function is undefined where its denominator is $0$.')]
    st=['Factor the denominator: $%s%s$.'%(fac(p),fac(q_)),'It is $0$ at $x=%d$ and $x=%d$, which are excluded.'%(p,q_),'Domain: %s.'%c]
    return dict(q=q,c=c,tr=tr,st=st)

# ---------- 1.14 Function model construction ----------
@reg('1.14','Medium','Calculator')
def t(r):
    d1=r.choice([2,3,4,5]); k=r.choice([2,3,4]); F1=r.choice([36,48,60,72,90]); F2=Fr(F1,k*k); d2=d1*k
    q='The force $F$, in newtons, between two magnets is inversely proportional to the square of the distance $d$, in centimeters. If $F=%d$ when $d=%d$, what is $d$ when $F=%s$?'%(F1,d1,fx(F2))
    c='$%d$ cm'%d2
    tr=[('$%s$ cm'%fx(d1*k*k),'Used inverse proportion to $d$, not to $d^{2}$.'),('$%s$ cm'%fx(Fr(d1,k)),'Used direct proportion: a smaller force means a greater distance here.'),('$%s$ cm'%fx(d1*k*k*d1),'Squared the wrong quantity when solving for $d$.')]
    st=['$F=\\dfrac{k}{d^{2}}$, so $k=%d\\cdot%d^{2}=%d$.'%(F1,d1,F1*d1*d1),'$%s=\\dfrac{%d}{d^{2}}\\Rightarrow d^{2}=%d\\Rightarrow d=%d$.'%(fx(F2),F1*d1*d1,d2*d2,d2)]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('1.14')
def t(r):
    B=r.choice([60,75,90,120]); k=r.choice([5,8,10,12]); e=r.choice([4,5,6,7]); n=k+r.randrange(3,12)
    q='A gym membership costs $%d$ dollars per month and includes $%d$ classes. Each class after the first $%d$ costs $%d$ dollars. The monthly cost $C(n)$ is piecewise-defined, where $n$ is the number of classes. What is $C(%d)$?'%(B,k,k,e,n)
    c='$%d$ dollars'%(B+e*(n-k))
    tr=[('$%d$ dollars'%(B+e*n),'Charged every class; the first $%d$ are included in the base cost.'%k),('$%d$ dollars'%(e*(n-k)),'Left out the fixed monthly cost.'),('$%d$ dollars'%(B+e*(n-k+1)),'Off by one: classes $%d$ to $%d$ is $%d-%d=%d$ extra classes.'%(k+1,n,n,k,n-k))]
    st=['$C(n)=%d$ for $0\\le n\\le %d$, and $C(n)=%d(n-%d)+%d$ for $n>%d$.'%(B,k,e,k,B,k),'$C(%d)=%d(%d)+%d=%d$.'%(n,e,n-k,B,B+e*(n-k))]
    return dict(q=q,c=c,tr=tr,st=st)

@reg('1.14')
def t(r):
    a=r.choice([2,3,4]); b=r.randrange(-5,6); c1=r.choice([3,4,5,6]); m=r.choice([-3,-2,2,3]); k=r.randrange(5,20)
    x0=r.choice([c1,c1+2])
    f1=lambda x:a*x+b; f2=lambda x:m*(x-c1)+k
    val=f1(x0) if x0<=c1 else f2(x0)
    other=f2(x0) if x0<=c1 else f1(x0)
    q='$f(x)=\\begin{cases}%s, & x\\le %d\\\\ %d(x-%d)+%d, & x>%d\\end{cases}$. What is $f(%d)$?'%(lin(a,b),c1,m,c1,k,c1,x0)
    c='$%d$'%val
    tr=[('$%d$'%other,'Used the wrong piece: check which condition $x=%d$ satisfies.'%x0),('$%d$'%(val+other),'Added the two pieces; only one piece applies at each input.'),('$%d$'%(k),'Read the constant of the second piece as the output.')]
    if x0==c1: tr[2]=('$%d$'%(f1(x0)+1),'Arithmetic slip in evaluating the first piece.')
    st=['$x=%d$ satisfies $x%s%d$.'%(x0,'\\le' if x0<=c1 else '>',c1),'$f(%d)=%d$.'%(x0,val)]
    return dict(q=q,c=c,tr=tr,st=st)
