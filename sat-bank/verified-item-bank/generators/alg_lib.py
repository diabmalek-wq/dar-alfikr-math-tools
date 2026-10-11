from fractions import Fraction as Fr
import math, itertools
SRC="**Source:** House-authored, coverage-matched to a College Board Question Bank Hard archetype (archetype only; no official item, wording or numbers reproduced)."
A="Algebra — "
LE1=A+"Linear equations in one variable";LE2=A+"Linear equations in two variables";LF=A+"Linear functions";LI=A+"Linear inequalities in one or two variables";SYS=A+"Systems of two linear equations in two variables"
L="ABCD"
I=[]
def tx(v):
    v=Fr(v)
    if v.denominator==1: return str(v.numerator)
    s='-' if v<0 else ''
    return f"{s}\\dfrac{{{abs(v.numerator)}}}{{{v.denominator}}}"
def m(v): return f"${tx(v)}$"
def add(skill,diff,q,opts,correct,ans,rat,mis):
    if opts: 
        assert len(opts)==4 and len(set(opts))==4,q[:40]
        ans=f"({L[correct]}) {opts[correct]}"
    I.append(dict(skill=skill,diff=diff,q=q,opts=opts,correct=correct,ans=ans,rat=rat,mis=mis))
def lin_solve(f):  # f(x) = lhs-rhs linear -> solution, or 'none'/'inf'
    a=f(Fr(1))-f(Fr(0)); b=f(Fr(0))
    if a==0: return 'inf' if b==0 else 'none'
    return -b/a
def mc(correct_val,distract,fmt=m):
    vals=[correct_val]+list(distract)
    assert len(set(map(Fr,vals)))==4,vals
    opts=[fmt(v) for v in vals]
    return opts,0
def shuffled(opts,ci,seed):
    import random
    r=random.Random(seed); idx=list(range(4)); r.shuffle(idx)
    return [opts[i] for i in idx], idx.index(ci)
