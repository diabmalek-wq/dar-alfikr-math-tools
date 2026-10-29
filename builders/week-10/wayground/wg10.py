# Wayground kick-off, Week 10: G10 L3-3, G10 L3-4, G11 L9-2. Data + independent verification.
import numpy as np
POLL = dict(n=1, type="Poll", tag="S", t=r"Be honest: how much of the pre-session task did you do?",
  opts=[r"All of it, including the readiness check", r"I watched and read but skipped the check",
        r"I opened it but did not finish", r"I did not open it"], ok=[],
  sig=r"Ungraded. Tally it first; it is the self-report half of the pre-session test.")
def mc(n,type_,tag,t,opts,ok,sig,img=None): return dict(n=n,type=type_,tag=tag,t=t,opts=opts,ok=ok,sig=sig,img=img)
L={}
L["L3-3"]=dict(code="L3-3",file="WG_G10_L3-3",grade="Grade 10",title="Identities with Polynomials",
 idea=r"An identity is true for every value of $x$; $(a+b)^{2}=a^{2}+2ab+b^{2}$ and $(a+b)(a-b)=a^{2}-b^{2}$ let you expand, factor and calculate quickly, and row $n$ of Pascal's triangle gives the coefficients of $(a+b)^{n}$.",
 mistake=r"Writing $(a+b)^{2}=a^{2}+b^{2}$ and losing the middle term $2ab$.",
 route=(r"re-teach expanding two brackets and the three square patterns with me", r"straight to proving identities and the binomial theorem"),
 prior=r"expanding two brackets, the square and difference-of-squares patterns, and testing a statement with a number",
 qs=[POLL,
  mc(2,"Multiple choice","P",r"In the pre-session, the coefficients of $(x+y)^{4}$ came from row 4 of Pascal's triangle. Which row is it?",
     [r"$1,\ 4,\ 6,\ 4,\ 1$", r"$1,\ 3,\ 3,\ 1$", r"$1,\ 5,\ 10,\ 10,\ 5,\ 1$", r"$1,\ 4,\ 4,\ 1$"],[0],
     r"Wrong $\to$ skipped station 1. B = row 3; C = row 5; D = guessed a symmetric row."),
  dict(n=3,type="Fill in the blank",tag="R",t=r"Complete the product: $(x+5)(x-5)=x^{2}-\underline{\hspace{1.2cm}}$",opts=[],ok=[],ans=r"$25$",
     sig=r"$10$ = kept a middle term; $5$ = did not square the $5$. Difference of squares is not yet secure."),
  mc(4,"Checkbox","R",r"Select the \textbf{two} correct expansions.",
     [r"$(x+4)^{2}=x^{2}+8x+16$", r"$(x-3)^{2}=x^{2}-6x+9$", r"$(x+2)^{2}=x^{2}+4$", r"$(x-5)^{2}=x^{2}-25$"],[0,1],
     r"C = lost the middle term $4x$; D = treated a square as a difference of squares."),
  dict(n=5,type="Match",tag="R",t=r"Match each expression with its factored form.",opts=[],ok=[],
     pairs=[(r"$x^{2}-9$",r"$(x-3)(x+3)$"),(r"$x^{2}+6x+9$",r"$(x+3)^{2}$"),(r"$x^{2}-6x+9$",r"$(x-3)^{2}$")],
     sig=r"Mixing the last two = sign of the middle term; $(x-3)^{2}$ for $x^{2}-9$ = missed that a difference of squares has no middle term."),
  mc(6,"Multiple choice","P",r"The pre-session warned that $(x+3)^{2}$ is not $x^{2}+9$. Which is the correct expansion?",
     [r"$x^{2}+9$", r"$x^{2}+6x+9$", r"$x^{2}+3x+9$", r"$x^{2}+6x+6$"],[1],
     r"Wrong $\to$ the middle term is the gap. A = squared each term; C = used $x\cdot3$ once; D = added $3+3$ at the end."),
  dict(n=7,type="Reorder",tag="R",t=r"Put the steps in order to prove the identity $(x+2)(x-2)=x^{2}-4$.",opts=[],ok=[],
     order=[r"$(x+2)(x-2)$",r"$x^{2}-2x+2x-4$",r"$x^{2}-4$",r"true for every $x$, so it is an identity"],
     sig=r"Wrong $\to$ expanding every term of one bracket over the other is the gap; it is today's proof method."),
  mc(8,"Dropdown","R",r"Is $(x+1)^{2}=x^{2}+1$ an identity? Test it at $x=2$: the two sides are\ldots",
     [r"$9$ and $5$, so it is not an identity", r"$9$ and $9$, so it is an identity", r"$5$ and $5$, so it is an identity", r"$3$ and $5$, so it is not an identity"],[0],
     r"B and C = evaluated a side wrongly; D = did not square the bracket. One failing value is enough to disprove an identity."),
 ])
L["L3-4"]=dict(code="L3-4",file="WG_G10_L3-4",grade="Grade 10",title="Dividing Polynomials",
 idea=r"Dividing $p(x)$ by $x-a$ leaves the remainder $p(a)$, and a remainder of $0$ means $x-a$ is a factor; synthetic division finds the quotient and remainder using only the coefficients.",
 mistake=r"Writing $-a$ instead of $a$ in the synthetic division box, or forgetting a zero for a missing power.",
 route=(r"re-teach substituting into a polynomial and the synthetic division steps with me", r"straight to the Remainder and Factor Theorems"),
 prior=r"evaluating a polynomial at a number, factoring a quadratic, and reading coefficients",
 qs=[POLL,
  mc(2,"Multiple choice","P",r"In the pre-session, you divided by $x-2$ with synthetic division. Which number went in the box?",
     [r"$2$", r"$-2$", r"$1$", r"$0$"],[0],
     r"Wrong $\to$ the pre-session misconception: use $a$, not $-a$. B = took the sign of the constant term; C = the leading coefficient; D = the remainder."),
  dict(n=3,type="Fill in the blank",tag="R",t=r"Let $p(x)=x^{3}-2x+1$. Then $p(2)=\underline{\hspace{1.2cm}}$",opts=[],ok=[],ans=r"$5$",
     sig=r"$3$ = $2^{3}$ replaced by $2\cdot3$ or an arithmetic slip; $-3$ = sign slip. Substituting is not yet secure."),
  mc(4,"Checkbox","R",r"For $p(x)=x^{2}-5x+6$, select the \textbf{two} true statements.",
     [r"$p(2)=0$", r"$p(3)=0$", r"$p(1)=0$", r"$p(-2)=0$"],[0,1],
     r"C = $1-5+6=2$; D = sign error on $-5x$. This is the factor idea that today's theorem names."),
  dict(n=5,type="Match",tag="R",t=r"Match each division with its quotient.",opts=[],ok=[],
     pairs=[(r"$(x^{2}-9)\div(x-3)$",r"$x+3$"),(r"$(x^{2}-x-6)\div(x-3)$",r"$x+2$"),(r"$(x^{2}+x-2)\div(x+2)$",r"$x-1$")],
     sig=r"Mixing the first two = factored $x^{2}-x-6$ with the wrong pair; $x+2$ for the third = did not check the factor pair."),
  mc(6,"Multiple choice","P",r"The pre-session said a remainder of $0$ tells you\ldots",
     [r"the divisor is a factor", r"the polynomial has no roots", r"the quotient is $0$", r"the divisor is $0$"],[0],
     r"Wrong $\to$ skipped station 4's last prompt. C = confused remainder with quotient."),
  dict(n=7,type="Reorder",tag="R",t=r"Put the steps in order to test whether $x-1$ is a factor of $x^{3}+3x^{2}-4$.",opts=[],ok=[],
     order=[r"write the coefficients $1,\ 3,\ 0,\ -4$ (zero for the missing $x$)",r"bring down $1$, then multiply by $1$ and add: $1,\ 4,\ 4,\ 0$",r"the last number, the remainder, is $0$",r"so $x-1$ is a factor"],
     sig=r"Wrong $\to$ the placeholder zero is the gap; without it the coefficients shift."),
  mc(8,"Dropdown","R",r"What is the remainder when $2x^{2}+3x-5$ is divided by $x+2$?",
     [r"$-3$", r"$9$", r"$3$", r"$-5$"],[0],
     r"B = used $p(2)$ for $x+2$; C = sign slip in $p(-2)$; D = the constant term."),
 ])
L["L9-2"]=dict(code="L9-2",file="WG_G11_L9-2",grade="Grade 11",title="Circles",
 idea=r"A circle is every point at distance $r$ from its center, so $(x-h)^{2}+(y-k)^{2}=r^{2}$ has center $(h,k)$ and radius $r$; completing the square rewrites any circle equation into this form.",
 mistake=r"Reading $r^{2}=25$ as $r=25$, or copying the signs of $h$ and $k$ from the brackets.",
 route=(r"re-teach the distance formula and completing the square with me", r"straight to deriving the circle equation and line-circle systems"),
 prior=r"the distance formula, completing the square, and solving a quadratic",
 qs=[POLL,
  mc(2,"Multiple choice","P",r"In the pre-session, $x^{2}+y^{2}-6x+4y-12=0$ became a circle with right-hand side $25$. What is the radius?",
     [r"$5$", r"$25$", r"$12$", r"$\sqrt{12}$"],[0],
     r"Wrong $\to$ the pre-session mistake. B = read $r^{2}$ as $r$; C = the constant of the original; D = square-rooted the wrong number."),
  dict(n=3,type="Fill in the blank",tag="R",t=r"The distance between $(1,\,2)$ and $(4,\,6)$ is $\underline{\hspace{1.2cm}}$",opts=[],ok=[],ans=r"$5$",
     sig=r"$25$ = forgot the square root; $7$ = added the differences. The distance formula is the circle's definition."),
  mc(4,"Checkbox","R",r"Select the \textbf{two} correct completions of the square.",
     [r"$x^{2}-10x=(x-5)^{2}-25$", r"$x^{2}+4x=(x+2)^{2}-4$", r"$x^{2}-6x=(x-3)^{2}-6$", r"$x^{2}+8x=(x+8)^{2}-64$"],[0,1],
     r"C = subtracted $6$ instead of $9$; D = used the whole coefficient, not half."),
  dict(n=5,type="Match",tag="R",t=r"Match each circle with its center.",opts=[],ok=[],
     pairs=[(r"$(x-1)^{2}+(y-4)^{2}=9$",r"$(1,\,4)$"),(r"$(x+1)^{2}+(y+4)^{2}=9$",r"$(-1,\,-4)$"),(r"$(x-4)^{2}+(y+1)^{2}=9$",r"$(4,\,-1)$")],
     sig=r"Mixing the first and third = swapped $h$ and $k$; sign errors = copied the brackets."),
  mc(6,"Multiple choice","P",r"What are the center and radius of $(x+2)^{2}+(y-3)^{2}=49$?",
     [r"center $(-2,\,3)$, radius $7$", r"center $(2,\,-3)$, radius $7$", r"center $(-2,\,3)$, radius $49$", r"center $(2,\,-3)$, radius $49$"],[0],
     r"Pre-session item. B = copied the signs from the brackets; C = read $r^{2}$ as $r$; D = both errors."),
  dict(n=7,type="Reorder",tag="R",t=r"Put the steps in order to solve $x^{2}+y^{2}=25$ with $y=x+1$.",opts=[],ok=[],
     order=[r"substitute: $x^{2}+(x+1)^{2}=25$",r"collect: $2x^{2}+2x-24=0$",r"divide by $2$ and factor: $(x+4)(x-3)=0$",r"use $y=x+1$: $(-4,-3)$ and $(3,4)$"],
     sig=r"Wrong $\to$ substituting a line into a circle is the new move today; check the order of expand, collect, factor."),
  mc(8,"Dropdown","R",r"Solve $x^{2}+x-12=0$.",
     [r"$x=3$ or $x=-4$", r"$x=-3$ or $x=4$", r"$x=12$ or $x=-1$", r"$x=3$ or $x=4$"],[0],
     r"B = signs reversed; C = factor pair product $-12$ but sum $11$; D = both positive."),
 ])
def verify():
    # L3-3
    for x in (-3,0,2,5): assert (x+5)*(x-5)==x*x-25 and (x+4)**2==x*x+8*x+16 and (x-3)**2==x*x-6*x+9 and (x+3)**2==x*x+6*x+9
    assert (2+1)**2!=2**2+1 and (2+2)**2!=2**2+4 and (2-5)**2!=2**2-25
    assert [int(v) for v in np.polynomial.polynomial.polyfromroots([-1]*4)]==[1,4,6,4,1]
    # L3-4
    p=lambda x:x**3-2*x+1; assert p(2)==5
    q=lambda x:x*x-5*x+6; assert q(2)==0 and q(3)==0 and q(1)!=0 and q(-2)!=0
    for x in (-3,0,4): assert x*x-9==(x-3)*(x+3) and x*x-x-6==(x-3)*(x+2) and x*x+x-2==(x+2)*(x-1)
    r=lambda x:x**3+3*x*x-4; assert r(1)==0
    s=lambda x:2*x*x+3*x-5; assert s(-2)==-3 and s(2)==9
    # L9-2
    assert np.hypot(3,4)==5
    assert 6**2/4*0+9+4+12==25 and (3)**2+(-2)**2-(-12)==25
    for x in (-3,0,5): assert x*x-10*x==(x-5)**2-25 and x*x+4*x==(x+2)**2-4
    assert (3**2+4**2+(-12)*0)==25
    for x in (3,-4): assert x*x+(x+1)**2==25 and x*x+x-12==0
    assert sorted(np.roots([1,1,-12]))==[-4,3]
    for k,d in L.items():
        q=d["qs"]; assert [x["n"] for x in q]==list(range(1,9))
        assert sum(1 for x in q if x["tag"]=="P")==2 and sum(1 for x in q if x["tag"]=="R")==5
        for qd in q:
            if qd["tag"]=="S": continue
            if qd.get("opts"): assert qd["ok"] and len(qd["opts"])==4 and len(set(qd["opts"]))==4
            elif "pairs" in qd: assert len(qd["pairs"])==3 and len({p[1] for p in qd["pairs"]})==3
            elif "order" in qd: assert len(qd["order"])==4
            else: assert qd.get("ans")
    print("verify ok")
if __name__=="__main__": verify()
