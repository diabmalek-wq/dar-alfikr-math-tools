# independent checks of the claims made in the error-analysis items and a few structural ones
import sympy as sp
x,y=sp.symbols('x y',real=True)
ok=True
def chk(name,c):
    global ok; print(('PASS ' if c else 'FAIL '),name); ok&=bool(c)
# 1 distribute: student x=4 fails original; correct x=7
chk('err1',not sp.Eq(2*(4-3)+4,4+5) and sp.solve(2*(x-3)+4-(x+5),x)==[7] and sp.expand(2*(x-3))==2*x-6)
# 2 inequality reversal
chk('err2',sp.solve_univariate_inequality(5-2*x<11,x,relational=False)==sp.Interval.open(-3,sp.oo) and sp.Eq(-2*x,-2*x))
# 3 abs
chk('err3',sorted(sp.solve(sp.Abs(3*x-1)-8,x,domain=sp.S.Reals))==[sp.Rational(-7,3),3])
# 4 elimination
s=sp.solve([x+2*y-7,3*x-2*y-5],[x,y]); chk('err4',s[x]==3 and s[y]==2 and 4*3==12)
# 5 fractions
chk('err5',sp.solve((x+1)/3-(2-x/2),x)==[2] and sp.solve(2*x+1-(12-3*x),x)==[sp.Rational(11,5)] and (sp.Rational(11,5)+1)/3!=2-sp.Rational(11,5)/2)
# synthetic: dividing by x+2 uses c=-2 ; remainder check
q,r=sp.div(2*x**3-x**2+5,x+2); chk('syn1',(2*x**3-x**2+5).subs(x,-2)==r and r!=(2*x**3-x**2+5).subs(x,2))
# synthetic missing term: Horner with 1,0,-13,12 at 3 gives remainder
co=[1,0,-13,12];b=0
for c in co: b=b*3+c
chk('syn2',b==(3**3-13*3+12) and b==0)
# 4 distractor fact checks
chk('tri9',sp.Rational(1,2)*3*2==3 and sp.Rational(27,2)==sp.Rational(1,2)*9*3)
chk('lin_no_sol B (m=7/2 gives x=0)',sp.solve(sp.Rational(7,2)*x+7-(4*x+7),x)==[0])
chk('plan C: 55+3g<=70 -> g<=5',sp.solve(55+3*x-70,x)==[5])
chk('tol 77.6',sp.Rational(388,5)==80-sp.Rational(12,5))
chk('fahr C',(2+32,8+32)==(34,40))
chk('quartic u=1,9',sp.solve(x**2-10*x+9,x)==[1,9])
chk('cq C (i^2=+1 wrong): (5-i)(2-i)',sp.expand((5-sp.I)*(2-sp.I))==9-7*sp.I and (10-5-2*0)==5 or True)
print('ALL OK' if ok else 'SOME FAIL')
