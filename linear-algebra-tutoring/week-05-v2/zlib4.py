# Exact Gaussian-rational arithmetic + row-reduction tracer with LaTeX output
from fractions import Fraction as Fr
class Z:
    __slots__=("re","im")
    def __init__(s,re=0,im=0): s.re=Fr(re); s.im=Fr(im)
    def __add__(a,b): b=zz(b); return Z(a.re+b.re,a.im+b.im)
    __radd__=__add__
    def __sub__(a,b): b=zz(b); return Z(a.re-b.re,a.im-b.im)
    def __rsub__(a,b): return zz(b)-a
    def __neg__(a): return Z(-a.re,-a.im)
    def __mul__(a,b): b=zz(b); return Z(a.re*b.re-a.im*b.im,a.re*b.im+a.im*b.re)
    __rmul__=__mul__
    def inv(a): d=a.re*a.re+a.im*a.im; return Z(a.re/d,-a.im/d)
    def __truediv__(a,b): return a*zz(b).inv()
    def __eq__(a,b): b=zz(b); return a.re==b.re and a.im==b.im
    def __hash__(a): return hash((a.re,a.im))
    def iszero(a): return a.re==0 and a.im==0
def zz(x): return x if isinstance(x,Z) else Z(x)
I=Z(0,1)
def fF(f,sign=True):
    f=Fr(f)
    if f.denominator==1: return str(f.numerator)
    s="-" if f<0 else ""
    return r"%s\dfrac{%d}{%d}"%(s,abs(f.numerator),f.denominator)
def tx(z):
    z=zz(z)
    if z.im==0: return fF(z.re)
    if z.im==1: ims="i"
    elif z.im==-1: ims="-i"
    else: ims=fF(z.im)+"i"
    if z.re==0: return ims
    return fF(z.re)+("+" if z.im>0 else "")+ims
def coef(c):  # coefficient text for 'c R_i' (positive-looking c)
    c=zz(c)
    if c.im==0: return "" if c.re==1 else fF(c.re)
    if c.re==0: return "i" if c.im==1 else fF(c.im)+"i"
    return "("+tx(c)+")"
def pos(c): c=zz(c); return c.re>0 or (c.re==0 and c.im>0)
def mat(M,ncoef=None):
    n=len(M[0])
    rows=[" & ".join(tx(x) for x in r) for r in M]
    body=r" \\ ".join(rows)
    if ncoef is not None and ncoef<n:
        spec="c"*ncoef+"|"+"c"*(n-ncoef)
        return r"\left(\begin{array}{%s}%s\end{array}\right)"%(spec,body)
    return r"\begin{pmatrix}%s\end{pmatrix}"%body
def M_(rows): return [[zz(x) for x in r] for r in rows]
def trace(M,ncoef=None,bar=None):
    """Gauss-Jordan; returns (steps, R, pivcols). steps are LaTeX strings."""
    M=[r[:] for r in M]; m=len(M); n=len(M[0]); nc=ncoef or n
    steps=[]; r=0; piv=[]
    def sh(d): steps.append(r"Apply $%s$:\par\smallskip $\displaystyle %s$"%(d,mat(M,ncoef if bar is None else bar)))
    for c in range(nc):
        if r>=m: break
        p=next((i for i in range(r,m) if not M[i][c].iszero()),None)
        if p is None: continue
        if p!=r:
            M[r],M[p]=M[p],M[r]; sh(r"R_%d\leftrightarrow R_%d"%(r+1,p+1))
        pv=M[r][c]
        if not (pv==1):
            M[r]=[x/pv for x in M[r]]
            inv=Z(1)/pv
            sh(r"R_%d\to %s R_%d"%(r+1, (tx(Z(1)/pv) if (pv.im==0 and pv.re.denominator!=1) else "\\dfrac{1}{%s}"%tx(pv)), r+1))
        ops=[]
        for i in range(m):
            if i!=r and not M[i][c].iszero():
                k=M[i][c]
                M[i]=[a-k*b for a,b in zip(M[i],M[r])]
                ops.append(r"R_%d\to R_%d%s%sR_%d"%(i+1,i+1,"-" if pos(k) else "+",coef(k if pos(k) else -k),r+1))
        if ops: sh(r",\ ".join(ops))
        piv.append(c); r+=1
    return steps,M,piv
def is_ref(M):
    last=-1; seenzero=False
    for row in M:
        lead=next((j for j,x in enumerate(row) if not x.iszero()),None)
        if lead is None: seenzero=True; continue
        if seenzero or lead<=last: return False
        last=lead
    return True
def is_rref(M):
    if not is_ref(M): return False
    for row in M:
        lead=next((j for j,x in enumerate(row) if not x.iszero()),None)
        if lead is None: continue
        if not row[lead]==1: return False
        if any(not M2[lead].iszero() for M2 in M if M2 is not row): return False
    return True
def matvec(A,x): return [sum((a*b for a,b in zip(r,x)),Z(0)) for r in A]
def solve(A,b):
    """returns None if inconsistent else (particular, [null basis vectors], free cols, piv)"""
    n=len(A[0]); M=[A[i]+[b[i]] for i in range(len(A))]
    st,R,piv=trace(M,n)
    if incons(R,n) is not None: return None
    free=[j for j in range(n) if j not in piv]
    part=[Z(0)]*n
    for k,c in enumerate(piv): part[c]=R[k][n]
    null=[]
    for f in free:
        v=[Z(0)]*n; v[f]=Z(1)
        for k,c in enumerate(piv): v[c]=-R[k][f]
        null.append(v)
    assert matvec(A,part)==list(b)
    for v in null: assert all(z.iszero() for z in matvec(A,v))
    return part,null,free,piv
def vec(v): return r"\begin{pmatrix}%s\end{pmatrix}"%r"\\".join(tx(x) for x in v)
def general(part,null,free,names="stuvw"):
    s=vec(part) if any(not z.iszero() for z in part) else ""
    for k,v in enumerate(null):
        s+=("+" if s else "")+names[k]+vec(v)
    return s or vec(part)

def incons(R,n):
    for k,row in enumerate(R):
        if all(z.iszero() for z in row[:n]) and not row[n].iszero(): return k
    return None
