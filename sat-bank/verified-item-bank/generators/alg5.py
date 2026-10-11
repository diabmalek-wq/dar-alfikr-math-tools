import sys; sys.path.insert(0,'/home/claude/cb')
exec(open('/home/claude/cb/alg4.py').read())
_keep={2,6,10,12,15,18,21,22,30,34,37,38,39,41}
I[:]=[it for n,it in enumerate(I,1) if n in _keep]
assert len(I)==14
# ---- new archetypes ----
f=lambda x:Fr(2,3)*x+4; assert f(12)==12
S(LF,M_,"The linear function $f$ is defined by $f(x)=\\dfrac23x+4$. For what value of $x$ is $f(x)=x$?","$12$","Set $\\dfrac23x+4=x$. Then $4=x-\\dfrac23x=\\dfrac13x$, so $x=12$. Check: $f(12)=8+4=12$.","Students solve $f(x)=0$ ($x=-6$) or compute $f(4)$ instead of equating $f(x)$ with $x$.")
k=7; assert Fr(-3+k,2)==Fr(5+(-1),2)==2
S(LE2,M_,"The segment with endpoints $(-3,5)$ and $(k,-1)$ has its midpoint on the line $y=x$. What is the value of $k$?","$7$","The midpoint is $\\left(\\dfrac{k-3}{2},\\ \\dfrac{5+(-1)}{2}\\right)=\\left(\\dfrac{k-3}{2},\\ 2\\right)$. On $y=x$ the coordinates are equal, so $\\dfrac{k-3}{2}=2$ and $k=7$.","Students average only one coordinate pair incorrectly or set the endpoints' coordinates equal instead of the midpoint's.")
a_,b_=-8,12; assert 2*4+a_==0 and -3*4+b_==0 and a_-b_==-20
S(LE2,H,"The lines $y=2x+a$ and $y=-3x+b$ intersect at the point $(4,0)$ on the $x$-axis. What is the value of $a-b$?","$-20$","Substituting $(4,0)$ into the first line: $0=8+a$, so $a=-8$. In the second: $0=-12+b$, so $b=12$. Then $a-b=-8-12=-20$.","Students compute $b-a=20$ or use $x=0$ instead of the point's coordinates.")
k=Fr(7,4); assert (5+k)/3==Fr(2*5-1,4)
S(LE1,H,"$$\\frac{x+k}{3}=\\frac{2x-1}{4}$$ In the equation above, $k$ is a constant. If $x=5$ is a solution, what is the value of $k$? (Enter as a decimal.)","$1.75$ (or $\\dfrac74$)","Substituting $x=5$: $\\dfrac{5+k}{3}=\\dfrac94$. Cross-multiplying gives $4(5+k)=27$, so $5+k=6.75$ and $k=1.75$.","Students compute $2x-1$ as $2(5-1)=8$, or cross-multiply as $3(5+k)=4\\cdot9$ with the denominators swapped.")
x,y=Fr(10,3),0
# 9x-2y from 3x-4y=10 and 6x+2y=5 : (3x-4y)+(6x+2y)=9x-2y
S(LE2,M_,"If $3x-4y=10$ and $6x+2y=5$, what is the value of $9x-2y$?","$15$","Add the two equations: $(3x-4y)+(6x+2y)=9x-2y$, and the right sides give $10+5=15$. There is no need to solve for $x$ and $y$.","Students solve the system fully, then slip on the fractional values of $x$ and $y$.")
assert [w for w in range(1,40) if (30-w)>=2*w][-1]==10
S(LI,M_,"A rectangular garden has a perimeter of at most $60$ meters, and its length is at least twice its width. What is the greatest possible whole-number width of the garden, in meters?","$10$","Let the width be $w$ and the length $\\ell$. The perimeter gives $\\ell+w\\le30$ and the length condition gives $\\ell\\ge2w$. Then $3w\\le2w+w\\le\\ell+w\\le30$, so $w\\le10$. A width of $10$ with length $20$ works.","Students forget the length condition and take $w=15$ (a square), or use $2\\ell+w\\le60$.")
x,y=9,15; assert Fr(x+y,2)==12 and 2*x-y==3
S(LE2,M_,"The average (arithmetic mean) of two numbers $x$ and $y$ is $12$, and $2x-y=3$. What is the value of $x$?","$9$","The average gives $x+y=24$. Adding $2x-y=3$ eliminates $y$: $3x=27$, so $x=9$.","Students use $x+y=12$ (the average instead of the sum) or report $y=15$.")
T=72; assert Fr(T,4)-Fr(T,6)==6
S(LE1,H,"A group of friends splits a restaurant bill equally. If $2$ more friends had joined, every person would have paid $\\$6$ less. The group originally had $4$ friends. What was the total bill, in dollars?","$72$","With the total $T$: $\\dfrac T4-\\dfrac T6=6$, so $\\dfrac{T}{12}=6$ and $T=72$. Check: $\\dfrac{72}{4}=18$ and $\\dfrac{72}{6}=12$.","Students use $4\\cdot6=24$ (assuming each originally paid $\\$6$) or forget the group grows to $6$ people.")
tab=[(0,5),(3,11),(7,19)]; assert all(Fr(y2-y1,x2-x1)==2 for (x1,y1),(x2,y2) in zip(tab,tab[1:]))
C(LF,M_,"$$\\begin{array}{c|c|c|c}x&0&3&7\\\\\\hline h(x)&5&11&k\\end{array}$$ The table shows some values of the linear function $h$. What is the value of $k$?",["$19$","$17$","$23$","$13$"],"From $x=0$ to $x=3$, $h$ rises by $6$, so the slope is $2$. From $x=3$ to $x=7$ the change in $x$ is $4$, so $k=11+2(4)=19$.","Students add the slope to the last output ($11+2$) or treat the step from $3$ to $7$ as $1$ unit.")
y=Fr(7,2)
