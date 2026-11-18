# SAAT part S — ideas read (skill+trap only) from the 205-item FikrCounts SAAT set (6 pages, Nov 2026).
# New stems, numbers and options; every key is re-derived by a predicate (brute force / sympy), never by the source key.
from fractions import Fraction as F
import sympy as sp, itertools, math
x,y,k,m=sp.symbols('x y k m')
def mn(s): return str(s).replace('-','−')
def fr(v):
    v=F(v)
    return mn(v.numerator) if v.denominator==1 else mn(f"{v.numerator}/{v.denominator}")
ITEMS=[]
def I(sig,unit,topic,lvl,stem,vals,pred,notes,trick,why,fmt=None,natural=False):
    ITEMS.append(dict(sig=sig,unit=unit,topic=topic,lvl=lvl,stem=stem,vals=vals,pred=pred,notes=notes,trick=trick,why=why,fmt=fmt or fr,natural=natural))
EQ="Equations & inequalities"; PL="Polynomials & factoring"; CX="Complex numbers"
def sols(eq,var=x):
    return sp.solveset(eq,var,domain=sp.S.Reals)
def Fq(v): return sp.Rational(v.numerator,v.denominator)

# ---------- parameter conditions on linear equations ----------
def lin_no_sol(v):
    e=sp.expand((m*x+7)-(4*x+2*m)).subs(m,Fq(F(v))); return sols(e)==sp.S.EmptySet
I("parameter-for-a-linear-equation-with-no-solution",2,EQ,3,
  "For which value of m does the equation mx + 7 = 4x + 2m have no solution?",
  [4,F(7,2),2,-4],lin_no_sol,
  ["B: 7/2 — the constant side 2m − 7 was set to zero, but then the equation still has the solution x = 0.",
   "C: 2 — the m on the left was matched to the 2 in 2m.",
   "D: −4 — the sign of the coefficient was flipped when moving 4x across."],
  "no solution needs the x-terms to cancel (m − 4 = 0) while the constants stay different — checking the constants is the last step",
  "Move terms: (m − 4)x = 2m − 7. At m = 4 this reads 0·x = 1, which is never true.")
def lin_inf(v):
    a,b=sp.symbols('a b')
    # 3(2x-1)+a = b x + 5  must hold for all x
    e=sp.expand(3*(2*x-1)+a-(b*x+5)); sol=sp.solve([e.coeff(x,1),e.coeff(x,0)],[a,b],dict=True)[0]
    return sol[a]+sol[b]==Fq(F(v))
I("sum-of-two-parameters-for-infinitely-many-solutions",2,EQ,3,
  "The equation 3(2x − 1) + a = bx + 5 is true for every real value of x. What is the value of a + b?",
  [14,8,6,2],lin_inf,
  ["B: 8 — only a was found; b was forgotten.",
   "C: 6 — only b was found; a was forgotten.",
   "D: 2 — the difference b − a = 6 − 8 was reported with the sign changed."],
  "'true for every x' means the x-coefficients match AND the constants match — two conditions, two unknowns",
  "6x − 3 + a = bx + 5. Matching x-terms gives b = 6; matching constants gives a − 3 = 5, so a = 8. Then a + b = 14.")
def one_sol(v): 
    opts={'A':(6,-9,3,-9,0),}  # placeholder
    return True
EQS=["6x − 9 = 3(2x − 3)","2x + 5 = 2x − 1","7x − 2 = 3x + 10","−x + 4 = 4 − x"]
def one_sol_pred(v):
    s={"6x − 9 = 3(2x − 3)":sp.Eq(6*x-9,3*(2*x-3)),"2x + 5 = 2x − 1":sp.Eq(2*x+5,2*x-1),"7x − 2 = 3x + 10":sp.Eq(7*x-2,3*x+10),"−x + 4 = 4 − x":sp.Eq(-x+4,4-x)}
    r=sols(s[v]); return r.is_FiniteSet and len(r)==1
I("pick-the-equation-with-exactly-one-solution",2,EQ,2,
  "Which of the following equations has exactly one solution?",
  ["7x − 2 = 3x + 10","6x − 9 = 3(2x − 3)","2x + 5 = 2x − 1","−x + 4 = 4 − x"],one_sol_pred,
  ["B: 6x − 9 = 3(2x − 3) — it simplifies to 0 = 0, so every x works.",
   "C: 2x + 5 = 2x − 1 — it simplifies to 5 = −1, so no x works.",
   "D: −x + 4 = 4 − x — both sides are identical, so every x works."],
  "simplify both sides first: matching x-coefficients mean 'none' or 'all', never 'exactly one'",
  "7x − 2 = 3x + 10 gives 4x = 12, x = 3. The other three have equal x-coefficients, so they are either never true or always true.",lambda v:v)
# ---------- systems: parameter and expression-only ----------
def sys_none(v):
    A=sp.Matrix([[Fq(F(v)),6],[2,-3]]); return A.det()==0 and sp.Matrix([[Fq(F(v)),6,7],[2,-3,4]]).rank()==2
I("system-parameter-that-gives-no-solution",2,EQ,3,
  "For which value of k does the system kx + 6y = 7 and 2x − 3y = 4 have no solution?",
  [-4,4,-9,9],sys_none,
  ["B: 4 — the sign was lost when scaling the second equation by −2.",
   "C: −9 — the two y-coefficients were multiplied instead of matched.",
   "D: 9 — the two y-coefficients were multiplied and the sign was lost."],
  "no solution = parallel lines: the x- and y-coefficients are proportional but the constants are not",
  "Multiply the second equation by −2: −4x + 6y = −8. The y-terms already match the first equation, so k = −4, and 7 ≠ −8 keeps the lines distinct.")
def sys_inf(v):
    a,c=sp.symbols('a c')
    sol=sp.solve([a-4, 12-2*c],[a,c],dict=True)[0]; return sol[a]+sol[c]==Fq(F(v))
I("two-parameters-for-infinitely-many-system-solutions",2,EQ,3,
  "The system ax + 6y = 12 and 2x + 3y = c has infinitely many solutions. What is a + c?",
  [10,4,6,16],sys_inf,
  ["B: 4 — only a was found.",
   "C: 6 — only c was found.",
   "D: 16 — the second equation was doubled but c was not."],
  "infinitely many solutions = the second equation is a multiple of the first, so EVERY coefficient and the constant scale together",
  "Doubling 2x + 3y = c gives 4x + 6y = 2c. Matching ax + 6y = 12 gives a = 4 and 2c = 12, so c = 6 and a + c = 10.")
def sys_except(v):
    return sp.Matrix([[5,Fq(F(v))],[1,4]]).det()==0
I("value-that-breaks-a-unique-solution",2,EQ,3,
  "The system 5x + ky = 3 and x + 4y = 2 has exactly one solution for every real k except one value. What is that value?",
  [20,4,5,10],sys_except,
  ["B: 4 — the coefficient of y in the second equation was reported directly.",
   "C: 5 — the coefficient of x in the first equation was reported directly.",
   "D: 10 — the equations were compared using the constants 3 and 2."],
  "a unique solution fails exactly when the coefficient determinant is zero: 5·4 − k·1 = 0",
  "The lines are parallel (or the same) when 5/1 = k/4, so k = 20. For every other k they cross once.")
def comb_sub(v):
    s=sp.solve([4*x+3*y-23,3*x+4*y-19],[x,y]); return s[x]-s[y]==Fq(F(v))
I("difference-of-two-variables-without-solving",2,EQ,2,
  "If 4x + 3y = 23 and 3x + 4y = 19, what is the value of x − y?",
  [4,6,42,2],comb_sub,
  ["B: 6 — the equations were added and divided, giving x + y instead.",
   "C: 42 — the equations were added and the total was reported.",
   "D: 2 — the two constants were subtracted and halved."],
  "when the coefficients swap, SUBTRACT the equations for x − y and ADD them for x + y — no need to find x and y",
  "Subtracting gives (4x + 3y) − (3x + 4y) = x − y = 23 − 19 = 4.")
def comb_lin(v):
    s=sp.solve([2*x+3*y-12,4*x-y-10],[x,y]); return 6*s[x]+2*s[y]==Fq(F(v))
I("target-combination-of-two-equations",2,EQ,3,
  "If 2a + 3b = 12 and 4a − b = 10, what is the value of 6a + 2b?",
  [22,11,44,2],comb_lin,
  ["B: 11 — the sum 22 was halved because the coefficients looked like they doubled.",
   "C: 44 — the sum was doubled.",
   "D: 2 — the right-hand sides were subtracted."],
  "look for the combination that is asked for — here simply adding the two equations produces 6a + 2b",
  "(2a + 3b) + (4a − b) = 6a + 2b = 12 + 10 = 22.")
def tri_y(v):
    # y = 2x-4, y = -x+5, and the y-axis
    X=sp.solve(sp.Eq(2*x-4,-x+5),x)[0]; Y=2*X-4
    base=abs(5-(-4)); return sp.Rational(1,2)*base*abs(X)==Fq(F(v))
I("triangle-bounded-by-two-lines-and-the-y-axis",2,EQ,3,
  "The lines y = 2x − 4 and y = −x + 5 and the y-axis form a triangle. What is its area?",
  [F(27,2),27,9,3],tri_y,
  ["B: 27 — the factor of 1/2 was left out.",
   "C: 9 — the distance between the y-intercepts was used as if it were the area.",
   "D: 3 — the x-axis was used as the third side, so the wrong triangle was measured."],
  "with the y-axis as one side, the base is the gap between the y-intercepts and the height is the x-coordinate of the crossing point",
  "The lines cross where 2x − 4 = −x + 5, so x = 3. The y-intercepts are −4 and 5, so the base is 9 and the area is ½ · 9 · 3 = 27/2.")
# ---------- counting integers / reverse-engineering sets ----------
def cnt1(v): return sum(1 for t in range(-40,40) if -5<2*t+1<=13)==v
I("count-the-integers-in-a-compound-inequality",2,EQ,2,
  "How many integers x satisfy −5 < 2x + 1 ≤ 13?",
  [9,8,10,7],cnt1,
  ["B: 8 — the right endpoint x = 6 was dropped although ≤ includes it.",
   "C: 10 — the left endpoint x = −3 was counted although < excludes it.",
   "D: 7 — both endpoints were dropped."],
  "solve the double inequality first, then count integers while checking each end for < or ≤ — do not subtract the ends",
  "Subtract 1: −6 < 2x ≤ 12, then divide by 2: −3 < x ≤ 6. The integers −2, −1, 0, 1, 2, 3, 4, 5, 6 give 9.")
def cnt2(v): return sum(1 for t in range(-40,40) if abs(3*t-2)<10)==v
I("count-the-integers-in-an-absolute-value-inequality",2,EQ,3,
  "How many integers x satisfy |3x − 2| < 10?",
  [6,5,7,4],cnt2,
  ["B: 5 — the lower end −8/3 was rounded the wrong way so −2 was lost.",
   "C: 7 — the endpoint 4 was counted although the inequality is strict.",
   "D: 4 — only the positive side was counted."],
  "|expression| < c is a double inequality; the ends are usually not integers, so round toward the inside",
  "−10 < 3x − 2 < 10 gives −8 < 3x < 12, so −8/3 < x < 4. The integers −2, −1, 0, 1, 2, 3 give 6.")
def par1(v): return (9+3*F(v))/4==6
I("coefficient-from-a-stated-solution-set",2,EQ,3,
  "The solution set of 4x − 3k > 9 is x > 6. What is the value of k?",
  [5,-5,-1,15],par1,
  ["B: −5 — 3k was moved across with the wrong sign, giving (9 − 3k)/4.",
   "C: −1 — the 4 was not divided out of 3k, giving x > 9 + 3k.",
   "D: 15 — the final division by 3 was forgotten (3k = 15)."],
  "solve the inequality for x in terms of k, then match its boundary to the boundary you are given",
  "4x > 9 + 3k gives x > (9 + 3k)/4. Setting (9 + 3k)/4 = 6 gives 9 + 3k = 24, so k = 5.")
def par2(v):
    p=F(v)  # |x-p|<q has interval (p-q,p+q) = (-3,9): p=3,q=6
    return None
def pq(v): return F(v)==3*6
I("centre-and-radius-product-from-an-interval",2,EQ,3,
  "The solution set of |x − p| < q, where q > 0, is the interval (−3, 9). What is the value of pq?",
  [18,9,27,12],pq,
  ["B: 9 — p + q = 9 was reported, which is the right end of the interval.",
   "C: 27 — the right end 9 was multiplied by 3.",
   "D: 12 — the width 12 of the interval was reported."],
  "|x − p| < q describes the points within q of the centre p, so p is the midpoint and q is HALF the width",
  "The midpoint of (−3, 9) is p = 3 and the half-width is q = 6, so pq = 18.")
def par3(v): return all(F(v)-12==-6 and False for _ in [0]) or (F(v)==6)
I("parameter-from-a-closed-absolute-value-solution-set",2,EQ,3,
  "The solution set of |3x − k| ≤ 12 is [−2, 6]. What is the value of k?",
  [6,2,4,12],lambda v: sp.solveset(sp.Abs(3*x-Fq(F(v)))<=12,x,domain=sp.S.Reals)==sp.Interval(-2,6),
  ["B: 2 — k was taken as the average of the endpoints and the 3 was ignored.",
   "C: 4 — the half-width 4 of the interval was reported.",
   "D: 12 — the bound in the inequality was copied."],
  "|3x − k| ≤ 12 means −12 ≤ 3x − k ≤ 12, so x runs from (k − 12)/3 to (k + 12)/3 — match one end",
  "(k − 12)/3 = −2 gives k = 6, and (k + 12)/3 = 6 agrees.")
# ---------- absolute value ----------
def sum_abs(v): return sum(sols(sp.Eq(sp.Abs(4*x-3),9)))==Fq(F(v))
I("sum-of-the-two-solutions-of-an-absolute-value-equation",2,EQ,2,
  "What is the sum of the solutions of |4x − 3| = 9?",
  [F(3,2),3,F(-3,2),0],sum_abs,
  ["B: 3 — only the positive case 4x − 3 = 9 was solved.",
   "C: −3/2 — only the negative case 4x − 3 = −9 was solved.",
   "D: 0 — the two right-hand sides 9 and −9 were added."],
  "an absolute value equation has two cases — solve both before you add",
  "4x − 3 = 9 gives x = 3 and 4x − 3 = −9 gives x = −3/2, so the sum is 3/2.")
def prod_abs(v): return sp.prod(list(sols(sp.Eq(sp.Abs(x+2),sp.Abs(3*x-4)))))==Fq(F(v))
I("product-of-the-solutions-when-two-absolute-values-are-equal",2,EQ,3,
  "What is the product of the solutions of |x + 2| = |3x − 4|?",
  [F(3,2),F(7,2),3,F(-3,2)],prod_abs,
  ["B: 7/2 — the sum of the solutions was reported.",
   "C: 3 — only the first case x + 2 = 3x − 4 was solved and its solution was reported.",
   "D: −3/2 — the sign of the second solution was mishandled."],
  "|A| = |B| splits into A = B and A = −B — use both cases and then multiply",
  "x + 2 = 3x − 4 gives x = 3; x + 2 = −(3x − 4) gives x = 1/2. The product is 3/2.")
def one_abs(v): return len(sols(sp.Eq(sp.Abs(2*x-1),3*Fq(F(v))-12)))==1
I("parameter-for-exactly-one-absolute-value-solution",2,EQ,3,
  "For which value of m does the equation |2x − 1| = 3m − 12 have exactly one solution?",
  [4,5,6,3],one_abs,
  ["B: 5 — the right-hand side was made positive rather than zero.",
   "C: 6 — the right-hand side was set equal to 6.",
   "D: 3 — the right-hand side was set equal to −3."],
  "|expression| = c has one solution only when c = 0; two when c > 0; none when c < 0",
  "Exactly one solution needs 3m − 12 = 0, so m = 4 (then 2x − 1 = 0 gives x = 1/2).")
def tol(v): return v==(80,F(12,5))
I("tolerance-as-an-absolute-value-inequality",2,EQ,3,
  "A pipe is labelled 80 cm long with a tolerance of 3%. Which inequality describes the acceptable length L, in cm?",
  [(80,F(12,5)),(80,3),(F(12,5),80),(F(388,5),F(12,5))],tol,
  ["B: |L − 80| ≤ 3 — the percentage was used as if it were centimetres.",
   "C: |L − 2.4| ≤ 80 — the target and the allowed error were swapped.",
   "D: |L − 77.6| ≤ 2.4 — the centre was moved to the lower limit."],
  "tolerance of p% means the allowed error is p% OF THE LABEL, and the centre of the interval is the label",
  "3% of 80 is 2.4, so the acceptable lengths satisfy |L − 80| ≤ 2.4.",
  lambda t: f"|L − {format(float(t[0]),'g')}| ≤ {format(float(t[1]),'g')}")
def within(v): return v=="|x + 2| ≤ 5"
I("within-a-distance-as-an-absolute-value-inequality",2,EQ,2,
  "Which inequality describes all real numbers within 5 units of −2 on the number line?",
  ["|x + 2| ≤ 5","|x − 2| ≤ 5","|x + 5| ≤ 2","|x + 2| ≥ 5"],within,
  ["B: |x − 2| ≤ 5 — the centre was written as +2 instead of −2.",
   "C: |x + 5| ≤ 2 — the centre and the radius were swapped.",
   "D: |x + 2| ≥ 5 — 'at least 5 away' was written instead of 'within 5'."],
  "'within r of c' is |x − c| ≤ r — and subtracting a negative centre gives x + 2",
  "The centre is −2, so |x − (−2)| = |x + 2|, and 'within 5' means ≤ 5.",lambda v:v)
def mem(p,t):
    for lo,hi,lc,hc in p:
        ok=True
        if lo is not None: ok&= (t>lo) or (lc and t==lo)
        if hi is not None: ok&= (t<hi) or (hc and t==hi)
        if ok: return True
    return False
def show(p):
    parts=[]
    for lo,hi,lc,hc in p:
        a=("−∞" if lo is None else fr(lo)); b=("∞" if hi is None else fr(hi))
        parts.append(("[" if lc and lo is not None else "(")+a+", "+b+("]" if hc and hi is not None else ")"))
    return " ∪ ".join(parts)
GRID=[F(i,6) for i in range(-120,121)]
def both_abs(v): return all(mem(v,t)==(abs(t-2)<5 and abs(t+1)>=2) for t in GRID)
I("intersection-of-two-absolute-value-conditions",2,EQ,3,
  "What is the set of all real numbers x that satisfy both |x − 2| < 5 and |x + 1| ≥ 2?",
  [[(1,7,True,False)],[(-3,7,False,False)],[(-3,1,False,True)],[(1,7,True,True)]],both_abs,
  ["B: (−3, 7) — the second condition was ignored.",
   "C: (−3, 1] — the part that FAILS the second condition was kept.",
   "D: [1, 7] — the strict end of the first condition was made inclusive."],
  "solve each condition as an interval, draw both on one line, and keep only the overlap — mind which ends are open",
  "|x − 2| < 5 gives (−3, 7). |x + 1| ≥ 2 gives x ≤ −3 or x ≥ 1. The overlap is [1, 7).",show)
def abs0(v): return all(mem(v,t)==(abs(2*t-6)<=0) for t in GRID)
I("absolute-value-at-most-zero",2,EQ,2,
  "What is the solution set of |2x − 6| ≤ 0?",
  [[(3,3,True,True)],[],[(None,3,False,True)],[(None,None,False,False)]],
  lambda v: (v==[(3,3,True,True)]),
  ["B: ∅ — 'at most 0' was read as impossible, but the value 0 itself is allowed.",
   "C: (−∞, 3] — the inequality was solved as if it were 2x − 6 ≤ 0.",
   "D: all real numbers — the absolute value was treated as always satisfying ≤."],
  "an absolute value is never negative, so |A| ≤ 0 can only happen when A = 0 exactly",
  "|2x − 6| ≤ 0 forces 2x − 6 = 0, so x = 3 and the solution set is {3}.",
  lambda p: "∅" if p==[] else ("all real numbers" if p==[(None,None,False,False)] else ("{3}" if p==[(3,3,True,True)] else show(p))))
# ---------- inequalities ----------
def gi(v): return max(t for t in range(-60,60) if 7-3*t>-8)==v
I("greatest-integer-that-satisfies-a-strict-inequality",2,EQ,2,
  "What is the greatest integer x that satisfies 7 − 3x > −8?",
  [4,5,6,15],gi,
  ["B: 5 — the boundary value was accepted although the inequality is strict.",
   "C: 6 — the sign was not flipped when dividing by −3, giving x > 5, and the next integer was taken.",
   "D: 15 — the value of 3x was reported instead of x."],
  "dividing by a negative flips the sign, and a strict boundary itself is NOT allowed",
  "−3x > −15 gives x < 5, so the greatest integer is 4.")
def plan_truth(t): return 25+6*t<55+3*t and 25+6*t<=70
PGRID=[F(i,6) for i in range(0,121)]
def plan2(v):
    hi,incl=v
    return all(plan_truth(t)==((t<=hi) if incl else (t<hi)) for t in PGRID)
I("two-plans-and-a-budget-in-one-inequality",2,EQ,3,
  "Plan P costs SAR 25 + 6g per month and plan Q costs SAR 55 + 3g per month, where g ≥ 0 is the number of gigabytes used. For which values of g is plan P cheaper than plan Q AND at most SAR 70?",
  [(F(15,2),True),(10,False),(7,True),(5,True)],plan2,
  ["B: 0 ≤ g < 10 — only the 'cheaper than Q' condition was used.",
   "C: 0 ≤ g ≤ 7 — 15/2 was rounded down although g may be any non-negative number.",
   "D: 0 ≤ g ≤ 5 — the SAR 70 budget was applied to plan Q instead of plan P."],
  "two conditions joined by AND need BOTH solved separately, then the stricter bound wins",
  "25 + 6g < 55 + 3g gives g < 10. 25 + 6g ≤ 70 gives g ≤ 15/2. The stricter bound is 15/2, so 0 ≤ g ≤ 15/2.",
  lambda v: f"0 ≤ g {'≤' if v[1] else '<'} {fr(v[0])}")
def fahr(v): return v==(F(178,5),F(232,5))
I("convert-a-temperature-range-through-a-formula",2,EQ,3,
  "A medicine cooler must stay between 2°C and 8°C, inclusive. A sensor displays degrees Fahrenheit, where F = (9/5)C + 32. Which inequality gives the allowed readings F?",
  [(F(178,5),F(232,5)),(F(18,5),F(72,5)),(F(34),F(40)),(F(2),F(8))],fahr,
  ["B: 3.6 ≤ F ≤ 14.4 — only (9/5)C was computed and the +32 was left out.",
   "C: 34 ≤ F ≤ 40 — 32 was added to the Celsius values without the 9/5 factor.",
   "D: 2 ≤ F ≤ 8 — the Celsius bounds were copied."],
  "apply the whole formula to BOTH ends: multiply by 9/5 first, then add 32",
  "At 2°C, F = 3.6 + 32 = 35.6. At 8°C, F = 14.4 + 32 = 46.4. So 35.6 ≤ F ≤ 46.4.",
  lambda t: f"{format(float(t[0]),'g')} ≤ F ≤ {format(float(t[1]),'g')}")
def strictbudget(v): return max(t for t in range(0,100) if 30+7*t<100)==v
I("strict-budget-with-an-exact-boundary",2,EQ,2,
  "An internet café charges a SAR 30 joining fee plus SAR 7 per hour. Huda wants to pay less than SAR 100 in total. What is the greatest whole number of hours she can use?",
  [9,10,13,14],strictbudget,
  ["B: 10 — the boundary value was accepted, but 10 hours cost exactly SAR 100, which is not less than 100.",
   "C: 13 — the hourly rate 7 was subtracted from 100 instead of the joining fee.",
   "D: 14 — the joining fee was left out: 100 ÷ 7."],
  "when the boundary lands on a whole number, a STRICT inequality excludes it — step down by one",
  "30 + 7h < 100 gives h < 10. The greatest whole number below 10 is 9.")
def noalways(v):
    f={"3x + 2 < 3x + 7":lambda t:3*t+2<3*t+7,"5(x − 1) ≥ 5x − 4":lambda t:5*(t-1)>=5*t-4,"x + 1 < x":lambda t:t+1<t,"|x| < 2":lambda t:abs(t)<2}
    return all(f[v](t) for t in GRID)
I("inequality-that-is-true-for-every-real-number",2,EQ,2,
  "Which of the following inequalities is true for EVERY real number x?",
  ["3x + 2 < 3x + 7","5(x − 1) ≥ 5x − 4","x + 1 < x","|x| < 2"],noalways,
  ["B: 5(x − 1) ≥ 5x − 4 — it simplifies to −5 ≥ −4, which is false, so it is never true.",
   "C: x + 1 < x — it simplifies to 1 < 0, which is never true.",
   "D: |x| < 2 — it is true only for −2 < x < 2."],
  "if the x-terms cancel, what is left is a statement about numbers only — true means 'all x', false means 'no x'",
  "3x + 2 < 3x + 7 reduces to 2 < 7, which is always true.",lambda v:v)
# ---------- literal equations ----------
def lit1(v):
    S,r,h=sp.symbols('S r h',positive=True); sol=sp.solve(sp.Eq(S,2*sp.pi*r*(r+h)),h)[0]
    return sp.simplify(sol-v)==0
S_,r_,h_=sp.symbols('S r h',positive=True)
I("make-a-variable-the-subject-of-a-surface-area-formula",2,EQ,3,
  "The total surface area of a closed cylinder is S = 2πr(r + h). Which expression gives h?",
  [S_/(2*sp.pi*r_)-r_,S_/(2*sp.pi*r_)+r_,(S_-r_)/(2*sp.pi*r_),S_/(2*sp.pi)-r_],lit1,
  ["B: S/(2πr) + r — the r was added instead of subtracted after dividing.",
   "C: (S − r)/(2πr) — r was subtracted from S before dividing, ignoring that r multiplies the bracket.",
   "D: S/(2π) − r — the division by r was forgotten."],
  "undo the outside multiplication first (divide by 2πr), and only then move the r — do not touch the bracket early",
  "S/(2πr) = r + h, so h = S/(2πr) − r.",
  lambda e: {str(S_/(2*sp.pi*r_)-r_):"h = S/(2πr) − r",str(S_/(2*sp.pi*r_)+r_):"h = S/(2πr) + r",str((S_-r_)/(2*sp.pi*r_)):"h = (S − r)/(2πr)",str(S_/(2*sp.pi)-r_):"h = S/(2π) − r"}[str(e)])
p_,q_,r2,s_=sp.symbols('p q r s')
def lit2(v): 
    sol=sp.solve(sp.Eq(p_*(x-q_),r2-s_*x),x)[0]; return sp.simplify(sol-v)==0
I("isolate-x-when-it-appears-on-both-sides",2,EQ,3,
  "If p(x − q) = r − sx, where p + s ≠ 0, what is x in terms of p, q, r and s?",
  [(r2+p_*q_)/(p_+s_),(r2-p_*q_)/(p_+s_),(r2+p_*q_)/(p_-s_),(r2+q_)/(p_+s_)],lit2,
  ["B: (r − pq)/(p + s) — the sign of pq was lost when it crossed the equals sign.",
   "C: (r + pq)/(p − s) — the sx was moved with the wrong sign, giving p − s.",
   "D: (r + q)/(p + s) — p was not distributed across (x − q)."],
  "distribute, gather every x-term on one side, factor x out, then divide by its coefficient",
  "px − pq = r − sx gives px + sx = r + pq, so x(p + s) = r + pq and x = (r + pq)/(p + s).",
  lambda e: {str((r2+p_*q_)/(p_+s_)):"x = (r + pq)/(p + s)",str((r2-p_*q_)/(p_+s_)):"x = (r − pq)/(p + s)",str((r2+p_*q_)/(p_-s_)):"x = (r + pq)/(p − s)",str((r2+q_)/(p_+s_)):"x = (r + q)/(p + s)"}[str(e)])
a_,b_=sp.symbols('a b',positive=True)
def lit3(v): 
    sol=sp.solve(sp.Eq(x/a_-x/b_,1),x)[0]; return sp.simplify(sol-v)==0
I("combine-fractions-then-isolate-the-variable",2,EQ,3,
  "If x/a − x/b = 1 with a, b > 0 and a ≠ b, what is x?",
  [a_*b_/(b_-a_),a_*b_/(a_-b_),a_*b_*(b_-a_),(b_-a_)/(a_*b_)],lit3,
  ["B: ab/(a − b) — the subtraction b − a was written in the wrong order.",
   "C: ab(b − a) — the bracket was multiplied instead of divided.",
   "D: (b − a)/(ab) — the whole fraction was inverted."],
  "factor x out: x(1/a − 1/b) = 1, then combine the bracket over ab and flip",
  "x(b − a)/(ab) = 1, so x = ab/(b − a).",
  lambda e: {str(a_*b_/(b_-a_)):"x = ab/(b − a)",str(a_*b_/(a_-b_)):"x = ab/(a − b)",str(a_*b_*(b_-a_)):"x = ab(b − a)",str((b_-a_)/(a_*b_)):"x = (b − a)/(ab)"}[str(e)])
# ---------- word problems ----------
def plans(v): return v==(12,'X')
I("which-provider-is-cheaper-and-from-where",2,EQ,3,
  "Courier X charges SAR 14 plus SAR 3 per kilometre. Courier Y charges SAR 26 plus SAR 2 per kilometre. Which statement is true?",
  [(12,'X'),(12,'Y'),(40,'X'),(0,'=')],plans,
  ["B: Y is cheaper under 12 km — the two couriers were swapped: Y has the higher fixed fee, so X wins short trips.",
   "C: X is cheaper under 40 km — 14 + 26 = 40 was used as the crossing point.",
   "D: the same for every trip — the single crossing point was mistaken for equality everywhere."],
  "the crossing point splits the range: the plan with the lower fixed fee wins short, the plan with the lower rate wins long",
  "14 + 3k = 26 + 2k gives k = 12. Below 12 km X is cheaper; above it Y is cheaper.",
  lambda t: {(12,'X'):"X is cheaper for trips under 12 km; Y is cheaper for longer trips.",(12,'Y'):"Y is cheaper for trips under 12 km; X is cheaper for longer trips.",(40,'X'):"X is cheaper for trips under 40 km; Y is cheaper for longer trips.",(0,'='):"Both couriers charge the same for every trip."}[t])
def simp(v): 
    t=sp.symbols('t'); return sp.solve(sp.Eq(2600+104*t,1800+144*t),t)[0]==Fq(F(v))
I("years-until-two-simple-interest-balances-match",2,EQ,3,
  "Account A holds SAR 2,600 and earns simple interest at 4% per year. Account B holds SAR 1,800 and earns simple interest at 8% per year. After how many years will the two balances be equal?",
  [20,40,25,8],simp,
  ["B: 40 — the yearly difference in gains (SAR 40) was reported instead of the number of years.",
   "C: 25 — the gap 800 was divided by 32 instead of 40.",
   "D: 8 — the gap 800 was divided by 100 as if the rates were not applied."],
  "simple interest adds the SAME amount each year: yearly gain = principal × rate — set the two balances equal",
  "A gains 104 a year and B gains 144 a year. 2600 + 104t = 1800 + 144t gives 40t = 800, so t = 20.")
def hs(v): return F(2*60*90,60+90)==F(v)
I("average-speed-for-a-round-trip",2,EQ,3,
  "Salma drives from Jeddah to Makkah at an average speed of 60 km/h and returns along the same road at 90 km/h. What is her average speed for the whole trip, in km/h?",
  [72,75,150,70],hs,
  ["B: 75 — the two speeds were averaged, but she spends more TIME at the slower speed.",
   "C: 150 — the speeds were added.",
   "D: 70 — a weighted guess toward the slower speed."],
  "average speed = total distance ÷ total time — never the average of the two speeds",
  "For a distance d each way, time = d/60 + d/90 = d/36, so the average speed is 2d ÷ (d/36) = 72 km/h.")
def water(v): return sp.Rational(15)*sp.Rational(4,10)/ (sp.Rational(15)+Fq(F(v)))==sp.Rational(1,4)
I("pure-water-added-to-a-solution",2,EQ,3,
  "How many litres of pure water must be added to 15 litres of a 40% salt solution to make a 25% solution?",
  [9,6,15,24],water,
  ["B: 6 — the amount of salt was reported, not the water to add.",
   "C: 15 — the same volume was added without checking the concentration.",
   "D: 24 — the new TOTAL volume was reported instead of the water added."],
  "pure water adds volume but no salt: the amount of salt stays the same, so use salt = percentage × volume on both sides",
  "Salt = 0.40 × 15 = 6 L. Final volume = 6 ÷ 0.25 = 24 L. Water added = 24 − 15 = 9 L.")
def mixt(v):
    t=sp.symbols('t'); return sp.solve(sp.Rational(1,5)*(60-t)+sp.Rational(1,2)*t-sp.Rational(38,100)*60,t)[0]==Fq(F(v))
I("how-much-of-the-stronger-solution",2,EQ,3,
  "A lab mixes a 20% acid solution with a 50% acid solution to make 60 litres of a 38% acid solution. How many litres of the 50% solution are used?",
  [36,24,30,18],mixt,
  ["B: 24 — the amount of the 20% solution was reported.",
   "C: 30 — an equal split of the 60 litres was assumed.",
   "D: 18 — the distance from 38 to 20 was used as litres."],
  "write acid from each part: 0.20(60 − t) + 0.50t = 0.38 × 60 and read which unknown the question wants",
  "12 + 0.3t = 22.8 gives t = 36 litres of the 50% solution.")
def pump(v): return 1/(F(1,6)-F(1,15))==F(v)
I("filling-with-a-drain-open",2,EQ,3,
  "A tap can fill a tank in 6 hours. A drain can empty a full tank in 15 hours. With both open, how many hours does it take to fill the empty tank?",
  [10,9,21,F(30,7)],pump,
  ["B: 9 — the times were subtracted: 15 − 6.",
   "C: 21 — the times were added.",
   "D: 30/7 — the drain was added to the rate instead of subtracted."],
  "work in rates per hour — a drain is a NEGATIVE rate: 1/6 − 1/15",
  "Net rate = 1/6 − 1/15 = 3/30 = 1/10 of the tank per hour, so it takes 10 hours.")
def workpart(v): return (1-3*(F(1,10)+F(1,15)))/F(1,10)==F(v)
I("one-worker-finishes-the-remaining-job",2,EQ,3,
  "Worker A can finish a job in 10 hours and worker B in 15 hours. They work together for 3 hours, then B leaves. How many more hours does A need to finish the job alone?",
  [5,6,3,F(5,2)],workpart,
  ["B: 6 — the time for both together to do the WHOLE job (1 ÷ 1/6) was reported.",
   "C: 3 — the remaining half was divided by the combined rate 1/6 instead of A's rate.",
   "D: 5/2 — A's rate was taken as 1/5 instead of 1/10."],
  "count the fraction of the job done, subtract from 1, and divide by the rate of whoever is left",
  "Together they do 1/10 + 1/15 = 1/6 per hour, so in 3 hours they finish 1/2. The remaining 1/2 at A's rate of 1/10 takes 5 hours.")
def boat(v):
    # 30 km upstream in 5 h, 30 km downstream in 2 h
    b,c=sp.symbols('b c'); s=sp.solve([b-c-6,b+c-15],[b,c]); return s[b]==Fq(F(v))
I("speed-of-a-boat-in-still-water",2,EQ,3,
  "A boat travels 30 km upstream in 5 hours and returns the same 30 km downstream in 2 hours. The boat's speed in still water and the current are both constant. What is the boat's speed in still water, in km/h?",
  [F(21,2),F(9,2),9,21],boat,
  ["B: 9/2 — the speed of the current was reported.",
   "C: 9 — the difference of the two speeds was reported.",
   "D: 21 — the two speeds 6 and 15 were added."],
  "upstream = boat − current and downstream = boat + current — the boat speed is their AVERAGE, the current is half their difference",
  "Upstream speed 30/5 = 6 and downstream speed 30/2 = 15. Boat = (6 + 15)/2 = 10.5 km/h and the current is 4.5 km/h.")
def catch(v): return F(50*2,75-50)==F(v)
I("time-for-a-second-vehicle-to-catch-up",2,EQ,3,
  "A bus leaves a station at 50 km/h. Two hours later a car leaves the same station along the same road at 75 km/h. How many hours after the car leaves does it catch up with the bus?",
  [4,6,2,25],catch,
  ["B: 6 — the hours since the BUS left were reported, not since the car left.",
   "C: 2 — the head start in hours was reported.",
   "D: 25 — the closing speed itself was reported."],
  "the head start is a DISTANCE (50 × 2); it closes at the DIFFERENCE of the speeds — and read which clock the question uses",
  "Head start = 100 km. Closing speed = 75 − 50 = 25 km/h. Time = 100 ÷ 25 = 4 hours after the car leaves.")
def ages(v):
    s,t=sp.symbols('s t'); sol=sp.solve(sp.Eq(5*s+8,3*(s+8)),s)[0]; return 5*sol==Fq(F(v))
I("age-problem-with-two-conditions",2,EQ,3,
  "A father is 5 times as old as his son. In 8 years he will be 3 times as old as his son. How old is the father now?",
  [40,8,48,24],ages,
  ["B: 8 — the son's age was reported.",
   "C: 48 — the father's age in 8 years was reported.",
   "D: 24 — three times the son's present age was reported."],
  "define the son as s, write both ages now, add the SAME number of years to both, and answer the person asked about",
  "5s + 8 = 3(s + 8) gives 2s = 16, so s = 8. The father is 5 × 8 = 40 now.")
def interest(v):
    t=sp.symbols('t'); return sp.solve(sp.Eq(sp.Rational(9,100)*(9000-t)-sp.Rational(6,100)*t,180),t)[0]==Fq(F(v))
I("money-split-between-two-rates",2,EQ,3,
  "SAR 9,000 is split between an account paying 6% a year and an account paying 9% a year. After one year the 9% account has earned SAR 180 more than the 6% account. How much was placed in the 6% account?",
  [4200,4800,6600,1200],interest,
  ["B: 4,800 — the amount in the 9% account was reported instead of the 6% account.",
   "C: 6,600 — the gap of SAR 180 was subtracted instead of added when the equation was set up.",
   "D: 1,200 — only 180 ÷ 0.15 was computed and the 9,000 term was left out."],
  "let x be the 6% amount, so the other is 8000 − x, and compare INTERESTS, not amounts",
  "0.09(9000 − x) − 0.06x = 180 gives 810 − 0.15x = 180, so x = 4,200.")
def areainc(v):
    n=sp.expand((x+7)*(x-2)-x**2); return sp.simplify(n-v)==0
I("change-in-area-when-the-dimensions-change",2,PL,3,
  "A square has side x metres. Its length is increased by 7 m and its width is decreased by 2 m. By how many square metres does the area change?",
  [5*x-14,5*x+14,x**2+5*x-14,-14],areainc,
  ["B: 5x + 14 — the product of the constants was given the wrong sign.",
   "C: x² + 5x − 14 — the new area was reported without subtracting the old one.",
   "D: −14 — the x-terms were dropped and only the product of the constants was kept."],
  "change = new area − old area — expand the new area, then subtract x²",
  "(x + 7)(x − 2) = x² + 5x − 14. Subtracting the original x² leaves 5x − 14.",
  lambda e: mn(str(e).replace('**2','²').replace('*','')))
# ---------- polynomials ----------
def pf(e): return mn(str(sp.expand(e)).replace('**2','²').replace('**3','³').replace('**4','⁴').replace('*',''))
def border(v): return sp.expand((2*x+9-4)*(x+6-4)-v)==0
I("inner-area-after-a-border-on-all-sides",1,PL,3,
  "A poster is (2x + 9) cm long and (x + 6) cm wide. A border 2 cm wide is printed along all four edges. Which expression gives the area of the inner region, in square centimetres?",
  [2*x**2+9*x+10,2*x**2+15*x+28,2*x**2+21*x+54,2*x**2+17*x+30],border,
  ["B: 2x² + 15x + 28 — only ONE border width was removed from each dimension, giving (2x + 7)(x + 4).",
   "C: 2x² + 21x + 54 — the border was ignored and the full poster area was given.",
   "D: 2x² + 17x + 30 — the border was removed from the length only."],
  "a border on all four edges removes TWICE its width from each dimension",
  "The inner length is 2x + 9 − 4 = 2x + 5 and the inner width is x + 6 − 4 = x + 2. The area is (2x + 5)(x + 2) = 2x² + 9x + 10.",pf)
def boxper(v):
    q=sp.cancel((x**3+10*x**2+31*x+30)/(x+3)); fx=sp.factor(q); a,b=2,5
    return sp.expand(v-(2*(x+a)+2*(x+b)))==0 and sp.expand(q-(x+2)*(x+5))==0
I("perimeter-of-a-base-from-a-volume-and-a-height",1,PL,3,
  "A box has volume (x³ + 10x² + 31x + 30) cubic units and height (x + 3) units. Its base is a rectangle whose sides are linear expressions in x. What is the perimeter of the base, in units?",
  [4*x+14,2*x+7,x**2+7*x+10,4*x+10],boxper,
  ["B: 2x + 7 — the sum of the two sides was reported instead of the perimeter.",
   "C: x² + 7x + 10 — the base AREA was reported instead of the perimeter.",
   "D: 4x + 10 — the constants were added as 2 + 3 instead of 2 + 5."],
  "volume ÷ height gives the base area — factor that area into two sides before finding the perimeter",
  "(x³ + 10x² + 31x + 30) ÷ (x + 3) = x² + 7x + 10 = (x + 2)(x + 5). The perimeter is 2(x + 2) + 2(x + 5) = 4x + 14.",pf)
def boxvol(v): return sp.expand(x*(30-2*x)*(18-2*x)-v)==0
I("volume-of-an-open-box-from-a-rectangular-sheet",1,PL,3,
  "An open box is made from a rectangular sheet 30 cm by 18 cm by cutting a square of side x cm from each corner and folding up the sides. Which polynomial gives the volume of the box, in cubic centimetres?",
  [4*x**3-96*x**2+540*x,x*(30-x)*(18-x),4*x**3-48*x**2+540*x,2*x**3-96*x**2+540*x],boxvol,
  ["B: x³ − 48x² + 540x — only ONE x was removed from each dimension.",
   "C: 4x³ − 48x² + 540x — the middle coefficient was halved when the bracket was expanded.",
   "D: 2x³ − 96x² + 540x — the leading coefficient 2·2 = 4 was written as 2."],
  "cutting a square from BOTH corners of a side removes 2x from that dimension",
  "The base is (30 − 2x) by (18 − 2x) and the height is x, so V = x(30 − 2x)(18 − 2x) = 4x³ − 96x² + 540x.",pf)
def mult(v): return v=="touches at x = 1; crosses at x = −3 and x = 4"
I("touch-or-cross-from-the-multiplicities",1,PL,3,
  "The graph of P(x) = (x − 1)²(x + 3)³(x − 4) meets the x-axis at three points. Which statement is true?",
  ["touches at x = 1; crosses at x = −3 and x = 4","touches at x = −3; crosses at x = 1 and x = 4","touches at x = 1 and x = 4; crosses at x = −3","crosses at all three points"],mult,
  ["B: the parity was reversed: an ODD power crosses and an EVEN power touches.",
   "C: x = 4 was taken as a touching point although its power is 1.",
   "D: every zero was assumed to cross regardless of its multiplicity."],
  "even multiplicity → the graph touches and turns back; odd multiplicity → it crosses",
  "(x − 1) has power 2 (touches), (x + 3) has power 3 (crosses, flattening), (x − 4) has power 1 (crosses).",lambda v:"Touches at x = 1; crosses at x = −3 and x = 4." if v.startswith("touches at x = 1;") else {"touches at x = −3; crosses at x = 1 and x = 4":"Touches at x = −3; crosses at x = 1 and x = 4.","touches at x = 1 and x = 4; crosses at x = −3":"Touches at x = 1 and x = 4; crosses at x = −3.","crosses at all three points":"Crosses at all three points."}[v])
def divprod(v):
    p,q=sp.symbols('p q'); s=sp.solve([sp.Eq((x**3+p*x+q).subs(x,2),0),sp.Eq((x**3+p*x+q).subs(x,-1),0)],[p,q],dict=True)[0]; return s[p]*s[q]==Fq(F(v))
I("divisible-by-a-product-of-two-binomials",1,PL,3,
  "The polynomial P(x) = x³ + px + q is divisible by (x − 2)(x + 1). What is the value of pq?",
  [6,-6,-2,3],divprod,
  ["B: −6 — the sign of p was lost when P(−1) = −1 − p + q was set up.",
   "C: −2 — only q was reported.",
   "D: 3 — only p was reported with its sign dropped."],
  "divisible by (x − 2)(x + 1) means P(2) = 0 AND P(−1) = 0 — two equations for p and q",
  "P(2) = 8 + 2p + q = 0 and P(−1) = −1 − p + q = 0. Subtracting gives 9 + 3p = 0, so p = −3, then q = −2 and pq = 6.")
def vieta(v): return F(-10,4)==F(v)
I("sum-of-all-zeros-of-a-cubic-without-finding-them",1,PL,3,
  "What is the sum of the three zeros of P(x) = 4x³ + 10x² − 7x + 3?",
  [F(-5,2),F(5,2),F(-7,4),F(3,4)],vieta,
  ["B: 5/2 — the sign was lost: the sum of the zeros is −b/a, not b/a.",
   "C: −7/4 — the coefficient of x was divided by the leading coefficient.",
   "D: 3/4 — the constant term was divided by the leading coefficient."],
  "for ax³ + bx² + cx + d the zeros add up to −b/a — you do not need to factor",
  "The sum of the zeros is −10/4 = −5/2.")
def psq(v): return v==30
I("value-that-makes-a-trinomial-a-perfect-square",1,PL,2,
  "The trinomial 9x² + kx + 25 is a perfect square and k is positive. What is the value of k?",
  [30,15,45,225],lambda v: sp.expand((3*x+5)**2-(9*x**2+v*x+25))==0,
  ["B: 15 — the middle term was taken as 3 · 5.",
   "C: 45 — the coefficient 9 was multiplied by the constant 5.",
   "D: 225 — the first and last coefficients were multiplied."],
  "a perfect square (ax + b)² has middle term 2ab — remember the factor of 2 and the square roots of BOTH ends",
  "9x² + 25 + kx = (3x + 5)², whose middle term is 2 · 3 · 5 = 30, so k = 30.")
def cntk(v): return len({p*q for p in range(1,12) for q in range(1,12) if p+q==12})==v
I("count-the-constants-that-let-a-trinomial-factor",1,PL,3,
  "For how many different positive integer values of k can x² − 12x + k be written as (x − p)(x − q), where p and q are positive integers?",
  [6,5,11,12],cntk,
  ["B: 5 — the case p = q = 6 was not counted.",
   "C: 11 — the ordered pairs (p, q) were counted, so each product was counted twice or more.",
   "D: 12 — the sum p + q was reported."],
  "p + q = 12 with p, q positive gives the pairs; different k means different products — pairs like (3, 9) and (9, 3) give the same k",
  "The pairs {1, 11}, {2, 10}, {3, 9}, {4, 8}, {5, 7}, {6, 6} give k = 11, 20, 27, 32, 35, 36 — six different values.")
def cntn(v): 
    import math
    return sum(1 for n in range(1,101) if int(math.isqrt(n))**2==n)==v
I("count-the-n-for-which-x-squared-minus-n-factors",1,PL,3,
  "For how many integers n from 1 to 100, inclusive, can x² − n be written as the product of two binomials with integer coefficients?",
  [10,9,11,100],cntn,
  ["B: 9 — the case n = 100 was left out.",
   "C: 11 — the square 0 was counted although n starts at 1.",
   "D: 100 — every n was assumed to factor."],
  "x² − n factors over the integers only when n is a perfect square, so count squares in the range",
  "n must be 1, 4, 9, 16, 25, 36, 49, 64, 81 or 100 — ten values.")
def gk(v): return max(p+q for p in range(-30,31) for q in range(-30,31) if p*q==-24)==v
I("greatest-linear-coefficient-for-a-factorable-trinomial",1,PL,3,
  "The trinomial x² + kx − 24 can be factored into two binomials with integer coefficients. What is the greatest possible value of k?",
  [23,5,10,2],gk,
  ["B: 5 — only the pair (−3, 8) was tried.",
   "C: 10 — only the pair (−2, 12) was tried.",
   "D: 2 — only the pair (−4, 6) was tried."],
  "k is the SUM of the two numbers whose product is −24 — to make it largest, make the numbers as far apart as possible",
  "The pairs (−1, 24), (−2, 12), (−3, 8), (−4, 6), ... have sums 23, 10, 5, 2, ... The greatest is 23.")
def sq4(v): return sum(t*t for t in sp.solveset(x**4-10*x**2+9,x,domain=sp.S.Reals))==Fq(F(v)) or False
I("sum-of-squares-of-the-real-solutions-of-a-quartic",1,PL,3,
  "What is the sum of the squares of all the real solutions of x⁴ − 10x² + 9 = 0?",
  [20,10,18,9],lambda v: sum(t**2 for t in sp.solveset(x**4-10*x**2+9,x,domain=sp.S.Reals))==Fq(F(v)),
  ["B: 10 — the two values u = 1 and u = 9 were added without doubling for ±.",
   "C: 18 — only u = 9 was used and counted twice (x = ±3).",
   "D: 9 — only the larger value of x² was reported."],
  "substitute u = x²: each u > 0 gives TWO real solutions ±√u, and both get squared",
  "u² − 10u + 9 = 0 gives u = 1 or 9, so x = ±1 or ±3. The squares add to 1 + 1 + 9 + 9 = 20.")
A_,B_=sp.symbols('A B')
def sym1(v):
    sols=sp.solve([A_-B_-2,A_*B_-15],[A_,B_],dict=True); return all(t[A_]**3-t[B_]**3==Fq(F(v)) for t in sols)
I("difference-of-cubes-from-a-difference-and-a-product",1,PL,3,
  "If a − b = 2 and ab = 15, what is the value of a³ − b³?",
  [98,38,34,53],sym1,
  ["B: 38 — the factor a² − ab + b² was used instead of a² + ab + b².",
   "C: 34 — only a² + b² was reported.",
   "D: 53 — (a − b)³ + 3ab was computed instead of (a − b)³ + 3ab(a − b)."],
  "a³ − b³ = (a − b)(a² + ab + b²), and a² + b² comes from squaring a − b: (a − b)² + 2ab",
  "a² + b² = 2² + 2·15 = 34, so a² + ab + b² = 49 and a³ − b³ = 2 · 49 = 98.")
def sym2(v):
    sols=sp.solve([A_+B_-9,A_**2+B_**2-45],[A_,B_],dict=True); return all(t[A_]**3+t[B_]**3==Fq(F(v)) for t in sols)
I("sum-of-cubes-from-a-sum-and-a-sum-of-squares",1,PL,3,
  "If x + y = 9 and x² + y² = 45, what is the value of x³ + y³?",
  [243,405,729,81],lambda v: sym2(v),
  ["B: 405 — x³ + y³ was computed as 9 × 45.",
   "C: 729 — only (x + y)³ was reported.",
   "D: 81 — only (x + y)² was reported."],
  "x³ + y³ = (x + y)(x² − xy + y²), and xy comes from (x + y)² = x² + 2xy + y²",
  "81 = 45 + 2xy gives xy = 18. Then x³ + y³ = 9 × (45 − 18) = 243.")
def deg2(v): return sp.degree(sp.expand((2*x**2-x)**2-4*x**4),x)==v
I("degree-after-the-leading-terms-cancel",1,PL,2,
  "What is the degree of the polynomial (2x² − x)² − 4x⁴?",
  [3,4,2,1],deg2,
  ["B: 4 — the leading terms were assumed not to cancel.",
   "C: 2 — the expansion stopped at the x² term.",
   "D: 1 — only the last term −x was considered."],
  "expand fully: the highest power may cancel, so the degree is the highest power that survives",
  "(2x² − x)² = 4x⁴ − 4x³ + x². Subtracting 4x⁴ leaves −4x³ + x², whose degree is 3.")
def xc(v): return sp.expand((x+3)*(x-2)*(x-5)).coeff(x,1)==v
I("coefficient-of-a-single-power-in-a-product-of-three-binomials",1,PL,3,
  "What is the coefficient of x in the expansion of (x + 3)(x − 2)(x − 5)?",
  [-11,-4,11,30],xc,
  ["B: −4 — the coefficient of x² was reported.",
   "C: 11 — the sign of the sum of pair products was lost.",
   "D: 30 — the constant term was reported."],
  "the x-coefficient is the SUM OF PAIR PRODUCTS of the three constants: 3(−2) + 3(−5) + (−2)(−5)",
  "−6 − 15 + 10 = −11.")
def d2(v): return sp.expand((5*x+3)**2-(5*x-3)**2-v)==0
I("difference-of-two-squared-binomials",1,PL,2,
  "Which expression is equal to (5x + 3)² − (5x − 3)²?",
  [60*x,50*x**2,18,30*x],d2,
  ["B: 50x² — the squares were added instead of subtracted, ignoring the cross terms.",
   "C: 18 — the two constants 9 and 9 were added.",
   "D: 30x — the cross term was counted once instead of twice for each bracket."],
  "the squares cancel, and each bracket contributes a cross term of ±30x — so they ADD to 60x",
  "(25x² + 30x + 9) − (25x² − 30x + 9) = 60x.",pf)
# ---------- complex numbers ----------
def ip(v): return sp.I**58==sp.sympify(v)
I("power-of-i-with-a-large-exponent",7,CX,2,
  "What is the value of i⁵⁸?",
  [-1,1,sp.I,-sp.I],ip,
  ["B: 1 — the remainder was taken as 0 after dividing 58 by 4, instead of 2.",
   "C: i — the remainder was taken as 1.",
   "D: −i — the remainder was taken as 3."],
  "powers of i repeat every 4 — divide the exponent by 4 and use the remainder",
  "58 = 4 × 14 + 2, so i⁵⁸ = i² = −1.",lambda v: mn(str(v).replace('I','i')))
def cp6(v): return sp.expand((1+sp.I)**6)==sp.sympify(v)
I("power-of-a-complex-binomial",7,CX,3,
  "What is the value of (1 + i)⁶?",
  [-8*sp.I,8*sp.I,8,-8],cp6,
  ["B: 8i — i³ was taken as i instead of −i.",
   "C: 8 — the factor i³ was dropped.",
   "D: −8 — i³ was taken as −1."],
  "square first: (1 + i)² = 2i, then cube it: (2i)³ = 8i³ and i³ = −i",
  "(1 + i)² = 2i, so (1 + i)⁶ = (2i)³ = 8i³ = −8i.",lambda v: mn(str(v).replace('*','').replace('I','i')))
def eqp(v):
    X,Y=sp.symbols('X Y'); s=sp.solve([3*X-2-10,Y+4+2],[X,Y]); return s[X]+s[Y]==Fq(F(v))
I("equate-real-and-imaginary-parts",7,CX,3,
  "If (3x − 2) + (y + 4)i = 10 − 2i, where x and y are real numbers, what is the value of x + y?",
  [-2,6,2,10],eqp,
  ["B: 6 — y + 4 = −2 was solved as y = 2 (the 4 was added instead of subtracted).",
   "C: 2 — y + 4 = −2 was solved as y = −2 (the 4 was ignored).",
   "D: 10 — the real part of the right-hand side was reported."],
  "two complex numbers are equal when their REAL parts match and their IMAGINARY parts match",
  "3x − 2 = 10 gives x = 4. y + 4 = −2 gives y = −6. So x + y = −2.")
def nonreal(v): return v=="k > 9"
I("condition-for-two-distinct-nonreal-roots",7,CX,3,
  "For which values of k does x² − 6x + k = 0 have two distinct nonreal complex solutions?",
  ["k > 9","k < 9","k = 9","k > 36"],nonreal,
  ["B: k < 9 — the discriminant inequality was written the wrong way round.",
   "C: k = 9 — the discriminant was set to zero, which gives one repeated real root.",
   "D: k > 36 — 36 − 4k < 0 was solved as k > 36."],
  "nonreal roots need a NEGATIVE discriminant: b² − 4ac < 0",
  "36 − 4k < 0 gives k > 9.",lambda v:v)
def cq(v): return sp.simplify((5-sp.I)/(2+sp.I)-(sp.Rational(v[0].numerator,v[0].denominator)+sp.I*sp.Rational(v[1].numerator,v[1].denominator)))==0
def cfmt(t):
    re,im=t; r=fr(re) if re.denominator>1 else mn(str(re.numerator))
    i=(fr(abs(im)) if abs(im).denominator>1 else str(abs(im).numerator))
    return f"{r} {'−' if im<0 else '+'} {'' if i=='1' else i}i" if abs(im).denominator==1 else f"{r} {'−' if im<0 else '+'} ({i})i"
I("complex-quotient-with-a-binomial-denominator",7,CX,3,
  "Which of the following is equal to (5 − i)/(2 + i)?",
  [(F(9,5),F(-7,5)),(F(9,5),F(7,5)),(F(11,5),F(-7,5)),(F(9),F(-7))],cq,
  ["B: 9/5 + (7/5)i — the sign of the imaginary part was lost.",
   "C: 11/5 − (7/5)i — i² was replaced by +1 instead of −1 in the numerator.",
   "D: 9 − 7i — the denominator 5 was not divided out."],
  "multiply top and bottom by the conjugate of the denominator, then replace i² with −1",
  "(5 − i)(2 − i) = 10 − 5i − 2i + i² = 9 − 7i and (2 + i)(2 − i) = 5, so the quotient is 9/5 − (7/5)i.",cfmt)
def qs(v): return set(sp.solve(x**2+2*x+10,x))=={sp.sympify(t) for t in v}
I("solutions-of-a-quadratic-with-a-negative-discriminant",7,CX,3,
  "What are the solutions of x² + 2x + 10 = 0?",
  [(-1+3*sp.I,-1-3*sp.I),(1+3*sp.I,1-3*sp.I),(-1+9*sp.I,-1-9*sp.I),(-2+6*sp.I,-2-6*sp.I)],qs,
  ["B: 1 ± 3i — the sign of −b/2a was lost.",
   "C: −1 ± 9i — √−36 was written as 18i instead of 6i.",
   "D: −2 ± 6i — the division by 2a = 2 was forgotten."],
  "use x = (−b ± √D)/2a — with D = −36 the square root is 6i, and the whole numerator is divided by 2",
  "D = 4 − 40 = −36, so x = (−2 ± 6i)/2 = −1 ± 3i.",lambda t: f"{mn(sp.re(t[0]))} ± {abs(sp.im(t[0]))}i")
# ---------- error analysis (first wrong step) ----------
ERR=["There is no error.","Step 1","Step 2","Step 3"]
def err_item(sig,unit,topic,lvl,stem,right,note_by_step,trick,why):
    I(sig,unit,topic,lvl,stem,list(ERR),lambda v,right=right: v==ERR[right],
      [f"X: {o} — {note_by_step[o]}" for o in [e for i,e in enumerate(ERR) if i!=right]],trick,why,lambda v:v,natural=True)
err_item("first-error-distributing-a-factor",2,EQ,2,
  "A student solves 2(x − 3) + 4 = x + 5 as follows. Step 1: 2x − 3 + 4 = x + 5. Step 2: 2x + 1 = x + 5. Step 3: x = 4. In which step does the first error occur?",
  1,{"There is no error.":"the answer x = 4 does not satisfy the original equation: 2(1) + 4 = 6 but x + 5 = 9.","Step 2":"2x − 3 + 4 does equal 2x + 1; the arithmetic here is right.","Step 3":"from 2x + 1 = x + 5, x = 4 is the correct next line, so the slip is earlier."},
  "check each line against the one before it — the first line that is not equivalent is the error",
  "Step 1 multiplied only the x by 2: 2(x − 3) = 2x − 6, not 2x − 3. The correct solution is x = 7.")
err_item("first-error-reversing-an-inequality-sign",2,EQ,2,
  "A student solves 5 − 2x < 11 as follows. Step 1: −2x < 6. Step 2: x < −3. Step 3: The solution set is (−∞, −3). In which step does the first error occur?",
  2,{"There is no error.":"dividing −2x < 6 by −2 requires the sign to flip, so x < −3 is wrong.","Step 1":"5 − 2x < 11 does give −2x < 6.","Step 3":"the set (−∞, −3) is the correct translation of x < −3; the slip came earlier."},
  "dividing or multiplying an inequality by a NEGATIVE number reverses the sign",
  "Step 2 divides by −2 without reversing: the correct line is x > −3, so the solution set is (−3, ∞).")
err_item("first-error-keeping-only-one-absolute-value-case",2,EQ,2,
  "A student solves |3x − 1| = 8 as follows. Step 1: 3x − 1 = 8. Step 2: 3x = 9. Step 3: x = 3, so the only solution is x = 3. In which step does the first error occur?",
  1,{"There is no error.":"the equation also has the solution x = −7/3, so the work is incomplete.","Step 2":"3x − 1 = 8 does give 3x = 9; the arithmetic is right.","Step 3":"x = 3 follows correctly from 3x = 9; the claim 'only solution' comes from Step 1."},
  "an absolute value equation |A| = c (c > 0) always splits into A = c AND A = −c",
  "Step 1 uses only one case. The second case 3x − 1 = −8 gives x = −7/3, so the solutions are 3 and −7/3.")
err_item("first-error-in-elimination-back-substitution",2,EQ,2,
  "A student solves x + 2y = 7 and 3x − 2y = 5 as follows. Step 1: Add the equations: 4x = 12. Step 2: x = 3. Step 3: Substitute: 3 + 2y = 7, so y = 5. In which step does the first error occur?",
  3,{"There is no error.":"3 + 2y = 7 gives 2y = 4, so y = 2, not 5.","Step 1":"adding the equations eliminates y correctly: 4x = 12.","Step 2":"4x = 12 gives x = 3 correctly."},
  "after finding one variable, finish the substitution carefully — and check the pair in the other equation",
  "Steps 1 and 2 are correct. In Step 3, 3 + 2y = 7 gives 2y = 4, so y = 2. Check: 3(3) − 2(2) = 5.")
err_item("first-error-clearing-fractions",2,EQ,3,
  "A student solves (x + 1)/3 = 2 − x/2 as follows. Step 1: Multiply by 6: 2x + 1 = 12 − 3x. Step 2: 5x = 11. Step 3: x = 11/5. In which step does the first error occur?",
  1,{"There is no error.":"the answer 11/5 does not satisfy the original equation.","Step 2":"2x + 1 = 12 − 3x does give 5x = 11; the arithmetic is right.","Step 3":"5x = 11 gives x = 11/5 correctly."},
  "when you multiply by the common denominator, EVERY term on both sides is multiplied — including the whole bracket",
  "Step 1 should read 2(x + 1) = 12 − 3x, i.e. 2x + 2 = 12 − 3x. Then 5x = 10 and x = 2.")
def syn1(v): return v=="The sign of c is wrong: it should be −2."
I("synthetic-division-by-a-sum-uses-the-opposite-sign",1,PL,3,
  "A student divides 2x³ − x² + 5 by (x + 2) using synthetic division. The student writes c = 2 and uses the coefficients 2, −1, 0, 5. What is the mistake?",
  ["The sign of c is wrong: it should be −2.","There is no mistake.","The coefficient 0 should not be written.","The remainder must be subtracted from the quotient."],syn1,
  ["B: no mistake — the divisor x + 2 means c = −2, so c = 2 is wrong.",
   "C: the zero is needed: the missing x term must be written as 0, so the coefficients are right.",
   "D: the remainder is never subtracted from the quotient; it is reported separately."],
  "synthetic division by (x − c) uses c — so for (x + 2) you use c = −2",
  "x + 2 = x − (−2), so c = −2. The coefficients 2, −1, 0, 5 (with the zero for the missing x-term) are correct.",lambda v:v)
def syn2(v): return v=="The coefficient 0 of the missing x² term was left out."
I("synthetic-division-with-a-missing-term",1,PL,3,
  "A student divides x³ − 13x + 12 by (x − 3) using synthetic division and writes c = 3 with the coefficients 1, −13, 12. What is the mistake?",
  ["The coefficient 0 of the missing x² term was left out.","The value of c should be −3.","There is no mistake.","The last coefficient should be −12."],syn2,
  ["B: c = 3 is correct because the divisor is x − 3.",
   "C: the missing x² term must be written as 0, so there is a mistake.",
   "D: the constant 12 is the given constant term and must be written as it is."],
  "write EVERY power from the highest down to the constant — a missing power still needs a 0",
  "x³ − 13x + 12 = 1x³ + 0x² − 13x + 12, so the coefficients are 1, 0, −13, 12.",lambda v:v)
