from zlib4 import *
F,I_,C='Foundational','Intermediate','Challenge'
def M(rows): return M_(rows)
def V(*x): return [zz(t) for t in x]
def eqs(A,b,vs):
    out=[]
    for r,bb in zip(A,b):
        s=""
        for a,v in zip(r,vs):
            if a.iszero(): continue
            c=tx(a) if (a.im!=0 and a.re!=0) else tx(a)
            if a.im!=0 and a.re!=0: c="("+c+")"
            if a==1: c=""
            elif a==-1: c="-"
            if not s: s=c+v
            else:
                if c.startswith("-"): s+=c+v
                else: s+="+"+c+v
            if a==1 and s.endswith(v) and False: pass
        out.append((s or "0")+"="+tx(bb))
    return out
def sysbox(A,b,vs):
    return r"\begin{cases}"+r"\\ ".join(eqs(A,b,vs))+r"\end{cases}"
def expr(const,terms):
    """const: Z; terms: list of (Z coef, name)"""
    s=tx(const) if not const.iszero() else ""
    for c,nm in terms:
        if c.iszero(): continue
        if c==1: t="+"+nm
        elif c==-1: t="-"+nm
        else:
            t=tx(c); t=("+"+t if not t.startswith("-") else t)
            if c.im!=0 and c.re!=0: t="+("+tx(c)+")"
            t+=nm
        s+=t
    if s.startswith("+"): s=s[1:]
    return s or "0"
def solve_steps(A,b,vs,names="stuvw"):
    n=len(A[0]); Mx=[A[i]+[b[i]] for i in range(len(A))]
    st=[r"Write the system as an augmented matrix, one row per equation, with a bar before the right-hand side:\par\smallskip $\displaystyle %s$"%mat(Mx,n)]
    t,R,piv=trace(Mx,n); st+=t
    if t==[]: st.append("The matrix is already in reduced row echelon form.")
    k=incons(R,n)
    if k is not None:
        st.append(r"Row %d reads $0=1$, a contradiction. No numbers $%s$ can satisfy it, so the system is \emph{inconsistent}."%(k+1,",".join(vs)))
        return st,"No solution (inconsistent)."
    free=[j for j in range(n) if j not in piv]
    pc=", ".join("$%s$"%vs[c] for c in piv)
    if free:
        fc=", ".join("$%s$"%vs[c] for c in free)
        st.append(r"Pivot columns are the columns of the basic variables: %s. The remaining variable(s) %s are \emph{free}: call them %s."%(pc,fc,", ".join("$%s=%s$"%(vs[f],names[k]) for k,f in enumerate(free))))
    else:
        st.append(r"Every column of the coefficient part holds a pivot, so there are no free variables and the solution is unique.")
    lines=[]
    for k,c in enumerate(piv):
        lines.append("%s=%s"%(vs[c],expr(R[k][n],[(-R[k][f],names[j]) for j,f in enumerate(free)])))
    for j,f in enumerate(free): lines.append("%s=%s"%(vs[f],names[j]))
    lines.sort(key=lambda s:vs.index(s.split("=")[0]))
    st.append(r"Read each nonzero row as an equation for its basic variable:\par\smallskip $\displaystyle\begin{aligned}%s\end{aligned}$"%r"\\ ".join(l.replace("=","&=",1) for l in lines))
    s=solve(A,b); part,null,fr,pv=s
    if free:
        st.append(r"Write this as a vector: $\displaystyle \mathbf x=%s$ (the parameters %s may be any numbers)."%(general(part,null,fr,names),", ".join("$%s$"%names[j] for j in range(len(free)))))
        ch=[Z(1)]*len(free); x=[p+sum((nv[i]*ch[j] for j,nv in enumerate(null)),Z(0)) for i,p in enumerate(part)]
        assert matvec(A,x)==list(b)
        st.append(r"Check with %s: $\mathbf x=%s$, and substituting into the original equations gives the right-hand sides $%s$ \checkmark."%(", ".join("$%s=1$"%names[j] for j in range(len(free))),vec(x),"("+",".join(tx(t) for t in b)+")"))
        return st,r"Infinitely many solutions: $\mathbf x=%s$."%general(part,null,fr,names)
    x=part
    st.append(r"Check by substituting $(%s)=(%s)$ into the original equations: the left sides give $(%s)$, the right-hand sides \checkmark."%(",".join(vs),",".join(tx(t) for t in x),",".join(tx(t) for t in matvec(A,x))))
    return st,r"Unique solution: $(%s)=(%s)$."%(",".join(vs),",".join(tx(t) for t in x))
