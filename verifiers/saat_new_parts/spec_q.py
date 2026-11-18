# SAAT part Q — skills read (skill+trap only) from nine leak/trial PDFs (Nov 2026). New stems, numbers, options.
import math, numpy as np
def m(s): return str(s).replace('-', '−')
def s_(v): return m(v)
ITEMS=[]
def I(sig,unit,topic,lvl,stem,vals,pred,notes,trick,why,fmt=s_):
    ITEMS.append(dict(sig=sig,unit=unit,topic=topic,lvl=lvl,stem=stem,vals=vals,pred=pred,notes=notes,trick=trick,why=why,fmt=fmt))
T="Triangles, polygons & quadrilaterals"

# 1 largest angle opposite longest side
opp={"∠A":14,"∠B":11,"∠C":9}   # AB=9, BC=14, CA=11
I("largest-angle-is-opposite-the-longest-side",4,T,2,
  "In triangle ABC, AB = 9 cm, BC = 14 cm and CA = 11 cm. Which angle is the largest?",
  ["∠A","∠B","∠C","They are all equal"],
  lambda v: v in opp and opp[v]==max(opp.values()),
  ["B: the angle was matched to the side that ends at it (CA) instead of the side opposite it.",
   "C: the angle at the end of the shortest side was chosen.",
   "D: equal angles need equal sides, and these three sides all differ."],
  "the largest angle faces the longest side — it is NOT the angle where the longest side ends",
  "BC = 14 cm is the longest side and it lies opposite vertex A, so ∠A is the largest.")

# 2 equilateral: solve x then side
def eq_side():
    x=(6+4)/(3-1); a=3*x-4; b=x+6; c=2*x+1
    assert a==b==c; return a
I("equilateral-triangle-solve-then-find-the-perimeter",4,T,2,
  "A triangle is equilateral. Its sides measure (3x − 4), (x + 6) and (2x + 1) cm. What is its perimeter?",
  [33,15,11,21],
  lambda v: v==3*eq_side(),
  ["B: x = 5 was reported as if it were the answer to the question asked.",
   "C: a single side was reported instead of the perimeter.",
   "D: x = 3 was substituted by mistake, giving 5 + 9 + 7."],
  "solving for x is only the middle step — the question asks for the perimeter, which is three sides",
  "3x − 4 = x + 6 gives x = 5. Each side is 11 cm (2x + 1 = 11 agrees), so the perimeter is 33 cm.")

# 3 measure of centre with an outlier
data=[12,13,14,15,15,16,17,58]
def shift(f): return abs(f(data)-f(data[:-1]))
cent={"Mean":lambda d:sum(d)/len(d),"Median":lambda d:float(np.median(d))}
I("typical-value-when-an-outlier-is-present",5,"Statistics",2,
  "A shop records its daily sales of an item over eight days: 12, 13, 14, 15, 15, 16, 17 and 58. Which measure best describes a typical day?",
  ["Median","Mean","Range","Standard deviation"],
  lambda v: v in cent and shift(cent[v])==min(shift(c) for c in cent.values()),
  ["B: the mean is dragged upward by the single extreme day.",
   "C: the range measures spread, not a typical value.",
   "D: the standard deviation also measures spread and is inflated by the extreme day."],
  "an extreme value pulls the mean but barely moves the median — and spread measures are not measures of the centre at all",
  "The median is 15 and ignores the size of 58, while the mean is 20 and is pulled toward it.")

# 4 x - 1/x squared
def sq_val():
    rs=np.roots([1,-3,-1]); return {round(float(r*r+1/(r*r))) for r in rs}
I("square-an-expression-to-find-a-sum-of-squares",1,"Number & algebra",3,
  "If x − 1/x = 3, what is the value of x² + 1/x²?",
  [11,9,7,13], lambda v: sq_val()=={v},
  ["B: the −2 from the cross term was dropped when squaring, giving 3².",
   "C: the cross term was subtracted twice instead of added back.",
   "D: the cross term 2 was added twice."],
  "squaring (x − 1/x) produces a middle term of −2, which has to be ADDED back to isolate x² + 1/x²",
  "(x − 1/x)² = x² − 2 + 1/x² = 9, so x² + 1/x² = 9 + 2 = 11.")

# 5 compound-angle recognition
cr=lambda a,b: math.cos(math.radians(a))*math.cos(math.radians(b))+math.sin(math.radians(a))*math.sin(math.radians(b))
opts5={"cos 50°":math.cos(math.radians(50)),"cos 90°":0.0,"sin 50°":math.sin(math.radians(50)),"sin 90°":1.0}
I("recognise-the-cosine-difference-formula",9,"Trigonometry II",2,
  "What is the exact value form of cos 70° cos 20° + sin 70° sin 20°?",
  ["cos 50°","cos 90°","sin 50°","sin 90°"],
  lambda v: abs(opts5[v]-cr(70,20))<1e-9,
  ["B: the pattern was read as the sum formula, which has a minus sign, giving cos(70° + 20°).",
   "C: the cosine pattern was converted to a sine of the same difference.",
   "D: the sum of the angles was used with sine."],
  "cos A cos B + sin A sin B (a PLUS sign) is cos(A − B) — the sum formula has a minus sign",
  "The expression has the form cos A cos B + sin A sin B = cos(A − B), so it equals cos(70° − 20°) = cos 50°.")

# 6 sign of sin/tan
def neg_quads():
    q=set()
    for d in range(1,360):
        if d in (90,180,270): continue
        r=math.sin(math.radians(d))/math.tan(math.radians(d))
        if r<0: q.add(d//90+1)
    return q
qs={"II and III":{2,3},"III and IV":{3,4},"II and IV":{2,4},"I and IV":{1,4}}
I("sign-of-a-simplified-trig-ratio",8,"Trigonometry I",3,
  "For 0° < x < 360° (x ≠ 90°, 180°, 270°), in which quadrants is sin x ÷ tan x negative?",
  ["II and III","III and IV","II and IV","I and IV"],
  lambda v: qs[v]==neg_quads(),
  ["B: only the sign of sin x was tracked, which is negative in III and IV.",
   "C: only the sign of tan x was tracked, which is negative in II and IV.",
   "D: the quadrants where cos x is positive were chosen."],
  "simplify first: sin x ÷ tan x = cos x, so the question is only where cosine is negative",
  "Since tan x = sin x ÷ cos x, the ratio equals cos x, which is negative in quadrants II and III.")

# 7 unit conversion sci notation
def f7(v): return m(f"{v[0]:g} × 10"+{1:"¹",2:"²",3:"³"}[v[1]])
I("minutes-to-seconds-in-scientific-notation",1,"Number & algebra",1,
  "A reaction takes 4 minutes. Write its duration in seconds in scientific notation.",
  [(2.4,2),(2.4,1),(2.4,3),(0.24,3)],
  lambda v: 1<=v[0]<10 and abs(v[0]*10**v[1]-240)<1e-9,
  ["B: the power of ten is one too small, which describes 24 seconds.",
   "C: the power of ten is one too large, which describes 2 400 seconds.",
   "D: the value is 240, but the coefficient is not between 1 and 10 so it is not scientific notation."],
  "after converting to 240 s, the coefficient must lie between 1 and 10 — 0.24 × 10³ is the right number in the wrong form",
  "4 × 60 = 240 s = 2.4 × 10² s.", f7)

# 8 derivative of a constant
lab={"0":0.0,"3e²":3*math.e**2,"e³":math.e**3,"3":3.0}
def numd(): h=1e-6; f=lambda x: math.e**3; return (f(1+h)-f(1))/h
I("derivative-of-a-constant-power",11,"Limits & calculus",1,
  "If f(x) = e³, what is f′(x)?",
  ["0","3e²","e³","3"], lambda v: abs(lab[v]-numd())<1e-6,
  ["B: the power rule was applied to e³ as if e were the variable.",
   "C: the constant was left unchanged by the derivative.",
   "D: the exponent was treated as the derivative."],
  "e³ is just a number — a constant — so its derivative is 0; e is not the variable here",
  "f(x) = e³ does not change with x, so its rate of change is 0.")

# 9 budget inequality
feas=[(6,4,True),(4,8,True),(1,10,True),(10,0,False)]
opt9={"7x + 4y ≤ 60":lambda x,y:7*x+4*y<=60,"7x + 4y ≥ 60":lambda x,y:7*x+4*y>=60,
      "7x + 4y < 60":lambda x,y:7*x+4*y<60,"4x + 7y ≤ 60":lambda x,y:4*x+7*y<=60}
I("at-most-budget-as-an-inequality",2,"Equations & inequalities",1,
  "A student buys x notebooks at SAR 7 each and y pens at SAR 4 each and may spend at most SAR 60 in total. Which inequality models this?",
  ["7x + 4y ≤ 60","7x + 4y ≥ 60","7x + 4y < 60","4x + 7y ≤ 60"],
  lambda v: all(opt9[v](x,y)==ok for x,y,ok in feas),
  ["B: 'at most' was reversed, so the total would have to reach SAR 60.",
   "C: the strict sign excludes spending exactly SAR 60, which is allowed.",
   "D: the two prices were attached to the wrong items."],
  "'at most' allows the limit itself, so it is ≤ — and each price must stay with its own item",
  "Total cost 7x + 4y must not exceed 60, so 7x + 4y ≤ 60.")

# 10 self-inverse matrix
mats={"rows (0, 1) and (1, 0)":np.array([[0,1],[1,0]]),"rows (1, 1) and (0, 1)":np.array([[1,1],[0,1]]),
      "rows (2, 0) and (0, 2)":np.array([[2,0],[0,2]]),"rows (0, −1) and (1, 0)":np.array([[0,-1],[1,0]])}
I("matrix-that-is-its-own-inverse",2,"Equations, matrices & systems",3,
  "Which of these 2 × 2 matrices is equal to its own inverse?",
  list(mats), lambda v: (mats[v]@mats[v]==np.eye(2)).all(),
  ["B: it has determinant 1, but its inverse has −1 in the corner, so it differs from itself.",
   "C: it is a multiple of the identity, but its inverse has entries ½, not 2.",
   "D: it is a quarter-turn, whose inverse is the opposite quarter-turn."],
  "a matrix equals its own inverse when squaring it gives the identity — having determinant 1 or being diagonal is not enough",
  "The swap matrix squared is the identity, so A × A = I and A⁻¹ = A.")

# 11 solve exponent
I("solve-for-an-exponent-after-dividing-the-coefficient",6,"Exponentials & logarithms",2,
  "If 5 · 2^m = 80, what is the value of m?",
  [4,16,8,5], lambda v: 5*2**v==80,
  ["B: this is the value of 2^m, not of m.",
   "C: the coefficient 5 was multiplied into the base, giving 10^m = 80, and then m was guessed.",
   "D: the coefficient 5 was read as the exponent."],
  "divide by the coefficient first — then 2^m = 16 is a power of 2, and m is its exponent, not 16",
  "5 · 2^m = 80 gives 2^m = 16 = 2⁴, so m = 4.")

# 12 polynomial roots incl complex
def rts(): return {complex(round(r.real,6),round(r.imag,6)) for r in np.roots([1,0,0,0,-81,0])}
sets={"0, ±3, ±3i":{0,3,-3,3j,-3j},"0, ±3":{0,3,-3},"0, ±9, ±9i":{0,9,-9,9j,-9j},"±3, ±3i":{3,-3,3j,-3j}}
I("complete-roots-of-a-quintic-over-the-complex-numbers",7,"Sequences, series & complex numbers",3,
  "What is the complete solution set of x⁵ − 81x = 0 over the complex numbers?",
  list(sets), lambda v: {complex(z) for z in sets[v]}==rts(),
  ["B: only the real roots were kept and the pair from x² + 9 = 0 was dropped.",
   "C: 81 was used where 9 belongs, so the fourth root of 81 was not taken.",
   "D: the common factor x was lost when factoring, so the root 0 disappeared."],
  "factor out x first, then x² − 9 and x² + 9 — the second factor supplies the imaginary pair and the first gives the root 0",
  "x(x⁴ − 81) = x(x² − 9)(x² + 9) = 0 gives 0, ±3 and ±3i — five roots in all.")

# 13 slope from a distance-time line
I("slope-of-a-distance-time-line-is-signed-velocity",3,"Functions & graphs",2,
  "A cyclist's distance from home is 60 km at t = 0 hours and 0 km at t = 4 hours, and the graph is a straight line. What is the slope of this line?",
  [-15,15,-4,60], lambda v: (0-60)/(4-0)==v,
  ["B: the sign was lost; the cyclist is moving toward home, so the slope is negative.",
   "C: the elapsed time was reported instead of the rate.",
   "D: the starting distance was reported instead of the rate."],
  "slope is rise over run with the sign kept — a distance that falls over time gives a negative velocity",
  "(0 − 60) ÷ (4 − 0) = −15, so the slope is −15 km per hour.")
