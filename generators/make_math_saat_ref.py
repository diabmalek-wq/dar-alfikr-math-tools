"""LaTeX for the SAAT (Tahsili) FACTS, FORMULAS AND SKILLS reference.

One image per CARD — each card is a short array of related formulas, so the
document needs sixty images rather than three hundred, and every line on the
page is typeset rather than typed.

Facts and formulas follow the department's Tahsili revision source, section by
section, across the whole examined syllabus. The arrangement, the wording and
the emphasis are ours.
"""
import json, os, shutil, subprocess, tempfile
from PIL import Image

INK = "222E2D"

A = lambda body, cols="ll": r"\begin{array}{%s}%s\end{array}" % (cols, body)

E = {
# ================================================== 1 · LOGIC AND REASONING
"r_log_stmt": A(r"""
\sim p & \text{negation — the opposite truth value}\\[2pt]
p\wedge q & \text{AND: true only when BOTH are true}\\[2pt]
p\vee q & \text{OR: true when AT LEAST one is true}\\[2pt]
p\to q & \text{false ONLY when }p\text{ true, }q\text{ false}\\[2pt]
p\leftrightarrow q & \text{true when both have the SAME value}"""),

"r_log_cond": A(r"""
\text{conditional} & p\to q\\[2pt]
\text{converse} & q\to p\\[2pt]
\text{inverse} & \sim p\to\ \sim q\\[2pt]
\text{contrapositive} & \sim q\to\ \sim p"""),

"r_log_eq": A(r"""
p\to q &\equiv\ \sim q\to\ \sim p & \text{(contrapositive)}\\[2pt]
q\to p &\equiv\ \sim p\to\ \sim q & \text{(converse}\equiv\text{inverse)}\\[2pt]
\sim(p\wedge q) &\equiv\ \sim p\ \vee \sim q &\\[2pt]
\sim(p\vee q) &\equiv\ \sim p\ \wedge \sim q &""", "rll"),

"r_log_syl": A(r"""
\text{syllogism} & (p\to q)\ \wedge\ (q\to r)\ \Rightarrow\ p\to r\\[2pt]
\text{disproof} & \text{ONE counterexample is enough}"""),

# =========================== 2 · LINES, ANGLES AND THE COORDINATE PLANE
"r_ang_pairs": A(r"""
\text{complementary} & m\angle 1+m\angle 2=90^{\circ}\\[2pt]
\text{supplementary} & m\angle 1+m\angle 2=180^{\circ}\\[2pt]
\text{vertical} & \angle 1\cong\angle 3\\[2pt]
\text{linear pair} & \text{adjacent, and supplementary}"""),

"r_par": A(r"""
\text{corresponding} & \cong\\[2pt]
\text{alternate interior} & \cong\\[2pt]
\text{alternate exterior} & \cong\\[2pt]
\text{co-interior} & \text{supplementary}"""),

"r_slope": A(r"""
m=\dfrac{y_{2}-y_{1}}{x_{2}-x_{1}} & \text{parallel: } m_{1}=m_{2}\\[8pt]
\text{horizontal: } m=0 & \text{perpendicular: } m_{1}m_{2}={-1}\\[4pt]
\text{vertical: } m \text{ undefined} &"""),

"r_line": A(r"""
y=mx+b & \text{slope and }y\text{-intercept}\\[2pt]
y-y_{1}=m(x-x_{1}) & \text{a point and the slope}\\[2pt]
y=b & \text{horizontal}\\[2pt]
x=a & \text{vertical}"""),

"r_dist": A(r"""
d=\sqrt{(x_{2}-x_{1})^{2}+(y_{2}-y_{1})^{2}}\\[4pt]
M=\left(\dfrac{x_{1}+x_{2}}{2},\ \dfrac{y_{1}+y_{2}}{2}\right)\\[8pt]
d_{3D}=\sqrt{(\Delta x)^{2}+(\Delta y)^{2}+(\Delta z)^{2}}""", "l"),

# ================================== 3 · POLYGONS AND QUADRILATERALS
"r_poly": A(r"""
\text{interior sum} & S=180^{\circ}(n-2)\\[3pt]
\text{one interior} & m=\dfrac{180^{\circ}(n-2)}{n}\\[8pt]
\text{exterior sum} & 360^{\circ}\ \text{for every polygon}\\[3pt]
\text{one exterior} & \dfrac{360^{\circ}}{n}\ ,\qquad n=\dfrac{360^{\circ}}{180^{\circ}-m}"""),

"r_quad_par": A(r"""
\text{opposite sides} & \cong\ \text{and parallel}\\[2pt]
\text{opposite angles} & \cong\\[2pt]
\text{co-interior angles} & \text{supplementary}\\[2pt]
\text{diagonals} & \text{bisect each other}"""),

"r_quad_spec": A(r"""
\text{rectangle} & \text{diagonals}\ \cong\\[2pt]
\text{rhombus} & \text{diagonals}\ \perp\ \text{and bisect the angles}\\[2pt]
\text{square} & \text{both of the above}\\[2pt]
\text{kite} & \text{diagonals}\ \perp,\ \text{one pair of}\ \cong\ \text{angles}"""),

"r_trap": A(r"""
\text{trapezoid} & \text{exactly one pair of parallel sides}\\[2pt]
\text{isosceles} & \text{base angles}\ \cong,\ \text{diagonals}\ \cong\\[2pt]
\text{midsegment} & EF=\dfrac{1}{2}\left(AB+CD\right)"""),

# ================================================= 4 · TRIANGLES
"r_tri_ang": A(r"""
\text{angle sum} & 180^{\circ}\\[2pt]
\text{exterior angle} & =\ \text{the two remote interior angles}\\[2pt]
\text{right triangle} & \text{the two acute angles are complementary}\\[2pt]
\text{equilateral} & \text{every angle is }60^{\circ}"""),

"r_tri_cong": A(r"""
\text{any triangle} & \text{SSS}\quad \text{SAS}\quad \text{ASA}\quad \text{AAS}\\[3pt]
\text{right triangle} & \text{LL}\quad \text{HA}\quad \text{LA}\quad \text{HL}\\[3pt]
\text{never} & \text{SSA}\quad \text{AAA (that is similarity)}"""),

"r_tri_seg": A(r"""
\text{perpendicular bisector} & \text{equidistant from the two endpoints}\\[2pt]
\text{angle bisector} & \text{equidistant from the two sides}\\[2pt]
\text{median}\ \to\ \text{centroid} & \text{vertex to centroid}=\dfrac{2}{3}\ \text{of the median}\\[6pt]
\text{altitude} & \perp\ \text{to the opposite side, may fall outside}"""),

"r_tri_ineq": A(r"""
a+b>c\ \text{for every pair}\\[3pt]
\lvert a-b\rvert<c<a+b\\[3pt]
\text{the longest side faces the largest angle}""", "l"),

# ================================================ 5 · SIMILARITY
"r_sim": A(r"""
\text{similar by} & \text{AA}\quad \text{SSS}\quad \text{SAS}\\[3pt]
\text{perimeters} & \text{in the ratio } k\\[2pt]
\text{areas} & \text{in the ratio } k^{2}\\[2pt]
\text{parallel to a side} & \dfrac{AD}{DC}=\dfrac{AF}{FB}\\[7pt]
\text{angle bisector} & \dfrac{CA}{CD}=\dfrac{BA}{BD}\\[7pt]
\text{midsegment} & \text{parallel, and half the side}"""),

# ============================================ 6 · TRANSFORMATIONS
"r_trans": A(r"""
\text{reflect in }x & (x,y)\to(x,{-y})\\[2pt]
\text{reflect in }y & (x,y)\to({-x},y)\\[2pt]
\text{reflect in }y=x & (x,y)\to(y,x)\\[2pt]
\text{about the origin} & (x,y)\to({-x},{-y})\\[2pt]
\text{translate} & (x,y)\to(x+a,\ y+b)"""),

"r_rot": A(r"""
90^{\circ} & (x,y)\to({-y},x)\\[2pt]
180^{\circ} & (x,y)\to({-x},{-y})\\[2pt]
270^{\circ} & (x,y)\to(y,{-x})\\[2pt]
\text{dilation }k & (x,y)\to(kx,ky)\\[2pt]
\text{rotational symmetry} & \dfrac{360^{\circ}}{n}\ \text{for a regular }n\text{-gon}"""),

# ================================================== 7 · CIRCLES
"r_cir_basic": A(r"""
C=2\pi r=\pi d & A=\pi r^{2}\\[4pt]
\text{arc } s=\dfrac{\theta}{360^{\circ}}\,2\pi r & s=r\theta\ \ (\theta\ \text{in radians})\\[8pt]
\text{sector } =\dfrac{\theta}{360^{\circ}}\,\pi r^{2} & =\dfrac{1}{2}r^{2}\theta"""),

"r_cir_ang": A(r"""
\text{central angle} & =\ \text{its arc}\\[2pt]
\text{inscribed angle} & =\ \tfrac{1}{2}\ \text{its arc}\\[2pt]
\text{angle in a semicircle} & =90^{\circ}\\[2pt]
\text{same arc} & \text{equal inscribed angles}\\[2pt]
\text{cyclic quadrilateral} & \text{opposite angles supplementary}"""),

"r_cir_tan": A(r"""
\text{tangent} & \perp\ \text{radius at the point of contact}\\[2pt]
\text{two tangents} & \text{from one point are equal}\\[2pt]
\text{tangent-chord} & m\angle=\tfrac{1}{2}\ \text{intercepted arc}\\[2pt]
\text{two chords} & AB\cdot BC=DB\cdot BE\\[2pt]
\text{tangent-secant} & (JK)^{2}=JL\cdot JM"""),

"r_cir_eq": A(r"""
(x-h)^{2}+(y-k)^{2}=r^{2} & \text{centre }(h,k)\\[3pt]
x^{2}+y^{2}=r^{2} & \text{centre at the origin}\\[3pt]
\text{touches an axis} & \text{when a coordinate of the centre}=r"""),

# ============================================== 8 · TRIGONOMETRY
"r_trig_ratio": A(r"""
\sin\theta=\dfrac{\text{opp}}{\text{hyp}} & \csc\theta=\dfrac{1}{\sin\theta}\\[7pt]
\cos\theta=\dfrac{\text{adj}}{\text{hyp}} & \sec\theta=\dfrac{1}{\cos\theta}\\[7pt]
\tan\theta=\dfrac{\text{opp}}{\text{adj}} & \cot\theta=\dfrac{1}{\tan\theta}"""),

"r_trig_special": A(r"""
\theta & 0^{\circ} & 30^{\circ} & 45^{\circ} & 60^{\circ} & 90^{\circ}\\[3pt]
\sin & 0 & \tfrac{1}{2} & \tfrac{\sqrt{2}}{2} & \tfrac{\sqrt{3}}{2} & 1\\[5pt]
\cos & 1 & \tfrac{\sqrt{3}}{2} & \tfrac{\sqrt{2}}{2} & \tfrac{1}{2} & 0\\[5pt]
\tan & 0 & \tfrac{\sqrt{3}}{3} & 1 & \sqrt{3} & \text{---}""", "r|ccccc"),

"r_trig_quad": A(r"""
\text{I} & \text{all positive}\\[2pt]
\text{II} & \sin\ \text{and}\ \csc\ \text{only}\\[2pt]
\text{III} & \tan\ \text{and}\ \cot\ \text{only}\\[2pt]
\text{IV} & \cos\ \text{and}\ \sec\ \text{only}\\[3pt]
\text{on a point} & \sin=\dfrac{y}{r},\ \cos=\dfrac{x}{r},\ r=\sqrt{x^{2}+y^{2}}"""),

"r_trig_rad": A(r"""
\text{degrees}\to\text{radians} & \times\dfrac{\pi}{180^{\circ}}\\[7pt]
\text{radians}\to\text{degrees} & \times\dfrac{180^{\circ}}{\pi}\\[7pt]
\text{reference angle} & \theta'=180^{\circ}-\theta,\ \theta-180^{\circ},\ 360^{\circ}-\theta"""),

"r_trig_id": A(r"""
\sin^{2}\theta+\cos^{2}\theta=1 & \tan\theta=\dfrac{\sin\theta}{\cos\theta}\\[7pt]
1+\tan^{2}\theta=\sec^{2}\theta & \cot\theta=\dfrac{\cos\theta}{\sin\theta}\\[7pt]
1+\cot^{2}\theta=\csc^{2}\theta & \sin({-\theta})={-\sin\theta}\\[4pt]
\sin\!\left(\tfrac{\pi}{2}-\theta\right)=\cos\theta & \cos({-\theta})=\cos\theta"""),

"r_trig_sum": A(r"""
\sin(A\pm B)=\sin A\cos B\pm\cos A\sin B\\[3pt]
\cos(A\pm B)=\cos A\cos B\mp\sin A\sin B\\[3pt]
\tan(A\pm B)=\dfrac{\tan A\pm\tan B}{1\mp\tan A\tan B}\\[8pt]
\sin 2\theta=2\sin\theta\cos\theta\\[3pt]
\cos 2\theta=\cos^{2}\theta-\sin^{2}\theta=2\cos^{2}\theta-1=1-2\sin^{2}\theta\\[3pt]
\tan 2\theta=\dfrac{2\tan\theta}{1-\tan^{2}\theta}""", "l"),

"r_trig_laws": A(r"""
\dfrac{\sin A}{a}=\dfrac{\sin B}{b}=\dfrac{\sin C}{c}\\[8pt]
c^{2}=a^{2}+b^{2}-2ab\cos C\\[4pt]
\cos A=\dfrac{b^{2}+c^{2}-a^{2}}{2bc}\\[8pt]
K=\dfrac{1}{2}ab\sin C""", "l"),

"r_trig_graph": A(r"""
y=a\sin b\theta & \text{amplitude }\lvert a\rvert,\ \text{period }\dfrac{360^{\circ}}{\lvert b\rvert}\\[7pt]
y=a\cos b\theta & \text{amplitude }\lvert a\rvert,\ \text{period }\dfrac{360^{\circ}}{\lvert b\rvert}\\[7pt]
y=a\tan b\theta & \text{no amplitude, period }\dfrac{180^{\circ}}{\lvert b\rvert}"""),

# ================================================== 9 · VECTORS
"r_vec_plane": A(r"""
\overrightarrow{AB}=\langle x_{2}-x_{1},\ y_{2}-y_{1}\rangle\\[3pt]
\lvert v\rvert=\sqrt{x^{2}+y^{2}}\\[3pt]
u=\dfrac{v}{\lvert v\rvert}\quad\text{(unit vector)}\\[7pt]
v=\langle a,b\rangle=a\,\mathbf{i}+b\,\mathbf{j}\\[3pt]
v=\langle\lvert v\rvert\cos\theta,\ \lvert v\rvert\sin\theta\rangle""", "l"),

"r_vec_dot": A(r"""
a\cdot b=a_{1}b_{1}+a_{2}b_{2}\ (+a_{3}b_{3})\\[3pt]
\cos\theta=\dfrac{a\cdot b}{\lvert a\rvert\lvert b\rvert}\\[8pt]
a\perp b\ \Longleftrightarrow\ a\cdot b=0""", "l"),

"r_vec_space": A(r"""
a\times b=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\a_{1}&a_{2}&a_{3}\\b_{1}&b_{2}&b_{3}\end{vmatrix}\\[14pt]
\lvert a\times b\rvert=\text{area of the parallelogram}\\[3pt]
\lvert t\cdot(u\times v)\rvert=\text{volume}""", "l"),

# ================================= 10 · POLAR AND COMPLEX NUMBERS
"r_pol": A(r"""
x=r\cos\theta & y=r\sin\theta\\[3pt]
r=\sqrt{x^{2}+y^{2}} & \theta=\tan^{-1}\dfrac{y}{x}\\[8pt]
\multicolumn{2}{l}{(r,\theta)=(r,\theta\pm 360^{\circ})=({-r},\theta\pm 180^{\circ})}"""),

"r_cplx": A(r"""
i^{2}={-1},\quad i^{3}={-i},\quad i^{4}=1\\[3pt]
\dfrac{1}{a+bi}\times\dfrac{a-bi}{a-bi},\qquad (a+bi)(a-bi)=a^{2}+b^{2}\\[8pt]
\lvert z\rvert=\sqrt{a^{2}+b^{2}},\qquad z=r(\cos\theta+i\sin\theta)\\[4pt]
z^{n}=r^{n}\left(\cos n\theta+i\sin n\theta\right)\\[4pt]
z_{1}z_{2}=r_{1}r_{2}\bigl(\cos(\theta_{1}+\theta_{2})+i\sin(\theta_{1}+\theta_{2})\bigr)""", "l"),

# ==================================== 11 · REAL NUMBERS AND ALGEBRA
"r_sets": A(r"""
\mathbb{N} & 1,2,3,\dots\\[2pt]
\mathbb{W} & 0,1,2,3,\dots\\[2pt]
\mathbb{Z} & \dots,{-1},0,1,\dots\\[2pt]
\mathbb{Q} & \dfrac{a}{b}\ \text{— terminating or repeating}\\[7pt]
\mathbb{I} & \text{never ends, never repeats}\\[2pt]
\mathbb{R} & \mathbb{Q}\cup\mathbb{I}"""),

"r_props": A(r"""
\text{commutative} & a+b=b+a,\quad ab=ba\\[2pt]
\text{associative} & (a+b)+c=a+(b+c)\\[2pt]
\text{distributive} & a(b+c)=ab+ac\\[2pt]
\text{identity} & a+0=a,\quad a\cdot 1=a\\[2pt]
\text{inverse} & a+({-a})=0,\quad a\cdot\dfrac{1}{a}=1"""),

"r_idx": A(r"""
a^{m}a^{n}=a^{m+n} & \dfrac{a^{m}}{a^{n}}=a^{m-n}\\[7pt]
\left(a^{m}\right)^{n}=a^{mn} & a^{-n}=\dfrac{1}{a^{n}}\\[7pt]
a^{0}=1 & \sqrt[n]{a^{m}}=a^{\frac{m}{n}}"""),

"r_rad": A(r"""
\sqrt{ab}=\sqrt{a}\sqrt{b} & \sqrt{\dfrac{a}{b}}=\dfrac{\sqrt{a}}{\sqrt{b}}\\[8pt]
\sqrt[2k]{x^{2k}}=\lvert x\rvert & \dfrac{c}{\sqrt{a}+b}\times\dfrac{\sqrt{a}-b}{\sqrt{a}-b}"""),

"r_abs": A(r"""
\lvert x\rvert<c & \Longleftrightarrow\ {-c}<x<c\\[2pt]
\lvert x\rvert>c & \Longleftrightarrow\ x<{-c}\ \text{or}\ x>c\\[2pt]
\lvert x\rvert=\text{negative} & \text{has no solution}\\[2pt]
f(x)=\lvert x-a\rvert+b & \text{vertex }(a,b),\ \text{range } y\geq b"""),

"r_sci": A(r"""
a\times 10^{n},\qquad 1\leq a<10\\[3pt]
\text{multiply: multiply } a,\ \text{add } n\ \text{— then renormalise}""", "l"),

# ================================================= 12 · MATRICES
"r_mat": A(r"""
A_{m\times r}\cdot B_{r\times t}=C_{m\times t} & \text{inner must match}\\[3pt]
\begin{vmatrix}a&b\\c&d\end{vmatrix}=ad-bc & A^{-1}=\dfrac{1}{ad-bc}\begin{pmatrix}d&{-b}\\{-c}&a\end{pmatrix}\\[12pt]
\det=0 & \text{no inverse (singular)}\\[3pt]
\text{area}=\tfrac{1}{2}\lvert\det\rvert & \text{from three vertices}"""),

# =================================== 13 · POLYNOMIALS AND QUADRATICS
"r_fact": A(r"""
a^{2}-b^{2} & =(a-b)(a+b)\\[2pt]
a^{3}\pm b^{3} & =(a\pm b)(a^{2}\mp ab+b^{2})\\[2pt]
x^{2}+bx+c & \text{two numbers: product } c,\ \text{sum } b\\[2pt]
\text{grouping} & \text{the bracket left behind must match}"""),

"r_quad": A(r"""
x=\dfrac{{-b}\pm\sqrt{b^{2}-4ac}}{2a}\\[9pt]
b^{2}-4ac>0\ \text{two real}\quad =0\ \text{one repeated}\quad <0\ \text{two complex}\\[3pt]
\text{a perfect square discriminant}\ \Rightarrow\ \text{rational roots}\\[3pt]
\text{vertex } x=\dfrac{{-b}}{2a},\qquad y=a(x-h)^{2}+k\\[8pt]
\text{sum}=\dfrac{{-b}}{a},\qquad \text{product}=\dfrac{c}{a}""", "l"),

"r_poly_th": A(r"""
\text{remainder} & f(x)\div(x-r)\ \Rightarrow\ f(r)\\[3pt]
\text{factor} & f(r)=0\ \Longleftrightarrow\ (x-r)\ \text{is a factor}\\[3pt]
\text{degree }n & \text{exactly } n \text{ complex roots}\\[3pt]
\text{real coefficients} & a+bi\ \text{a root}\ \Rightarrow\ a-bi\ \text{a root}"""),

# ============================= 14 · RATIONAL AND RADICAL EXPRESSIONS
"r_rat": A(r"""
\text{domain} & \text{denominator}\neq 0\\[3pt]
\text{vertical asymptote} & \text{at a zero of the denominator}\\[3pt]
\deg N<\deg D & y=0\\[3pt]
\deg N=\deg D & y=\dfrac{\text{leading }N}{\text{leading }D}\\[8pt]
\deg N>\deg D & \text{no horizontal asymptote}\\[3pt]
\text{cancelled factor} & \text{a HOLE, not an asymptote}"""),

"r_radeq": A(r"""
\sqrt{A}=B\ \Rightarrow\ A=B^{2},\ \text{then TEST every root}\\[3pt]
\text{an even index needs the radicand}\ \geq 0\\[3pt]
\text{squaring can invent a root the original rejects}""", "l"),

# ============================== 15 · SEQUENCES, SERIES AND BINOMIAL
"r_arith": A(r"""
a_{n}=a_{1}+(n-1)d\\[3pt]
S_{n}=\dfrac{n}{2}\left[2a_{1}+(n-1)d\right]=n\left(\dfrac{a_{1}+a_{n}}{2}\right)""", "l"),

"r_geo": A(r"""
a_{n}=a_{1}r^{\,n-1}\\[3pt]
S_{n}=\dfrac{a_{1}\left(1-r^{n}\right)}{1-r}\\[9pt]
S_{\infty}=\dfrac{a_{1}}{1-r}\ ,\qquad \lvert r\rvert<1""", "l"),

"r_sigma": A(r"""
\displaystyle\sum_{k=a}^{b}f(k) & n=b-a+1\ \text{terms}\\[8pt]
\text{first} & f(a)\\[2pt]
\text{last} & f(b)"""),

"r_binom": A(r"""
{}_{n}C_{r}=\dfrac{n!}{(n-r)!\,r!}\\[9pt]
(a+b)^{n}\ \text{has } n+1\ \text{terms}\\[3pt]
\text{term } r+1={}_{n}C_{r}\,a^{\,n-r}b^{\,r}""", "l"),

# ================================================= 16 · FUNCTIONS
"r_fun": A(r"""
\text{a function} & \text{each domain value has ONE image}\\[3pt]
\text{vertical line test} & \text{cuts the graph once}\\[3pt]
\text{one-to-one} & \text{horizontal line test}\\[3pt]
\text{even} & f({-x})=f(x)\ \text{— symmetric in } y\\[3pt]
\text{odd} & f({-x})={-f(x)}\ \text{— symmetric in the origin}"""),

"r_comp": A(r"""
(f\circ g)(x)=f\bigl(g(x)\bigr)\ \text{— inner function FIRST}\\[3pt]
\text{inverse: swap } x\ \text{and } y,\ \text{then solve for } y\\[3pt]
(f\circ f^{-1})(x)=x\\[3pt]
\text{domain of } f^{-1}=\text{range of } f""", "l"),

"r_parent": A(r"""
g(x)=a\,f(x-h)+k\\[3pt]
h>0\ \text{right},\quad h<0\ \text{left}\\[2pt]
k>0\ \text{up},\quad k<0\ \text{down}\\[2pt]
{-f(x)}\ \text{reflects in } x,\qquad f({-x})\ \text{reflects in } y\\[2pt]
\lvert a\rvert>1\ \text{stretch},\quad 0<\lvert a\rvert<1\ \text{compress}""", "l"),

# ================================== 17 · EXPONENTIAL AND LOGARITHMIC
"r_exp": A(r"""
f(x)=b^{x} & \text{domain }\mathbb{R},\ \text{range } y>0\\[3pt]
b>1 & \text{increasing};\qquad 0<b<1\ \text{decreasing}\\[3pt]
\text{asymptote} & y=0\ \text{(shifts with } k)\\[3pt]
b^{x}=b^{y} & \Longleftrightarrow\ x=y"""),

"r_log": A(r"""
y=\log_{b}x\ \Longleftrightarrow\ b^{y}=x\\[3pt]
\log_{b}(xy)=\log_{b}x+\log_{b}y\\[2pt]
\log_{b}\dfrac{x}{y}=\log_{b}x-\log_{b}y\\[7pt]
\log_{b}x^{p}=p\log_{b}x,\qquad \log_{b}a=\dfrac{\log_{c}a}{\log_{c}b}\\[8pt]
\text{domain } x>0,\qquad \text{vertical asymptote } x=0""", "l"),

# ============================= 18 · PROBABILITY AND STATISTICS
"r_count": A(r"""
\text{counting principle} & \text{multiply the stages}\\[3pt]
{}_{n}P_{r}=\dfrac{n!}{(n-r)!} & \text{order MATTERS}\\[8pt]
{}_{n}C_{r}=\dfrac{n!}{(n-r)!\,r!} & \text{order does not}\\[8pt]
\text{circular} & (n-1)!\ \text{with no fixed seat}\\[3pt]
\text{repeated letters} & \dfrac{n!}{r_{1}!\,r_{2}!\cdots}"""),

"r_prob": A(r"""
P(E)=\dfrac{\text{favourable}}{\text{total}},\qquad P(E')=1-P(E)\\[8pt]
\text{mutually exclusive}\ \Rightarrow\ P(A\cup B)=P(A)+P(B)\\[3pt]
\text{otherwise}\ P(A\cup B)=P(A)+P(B)-P(A\cap B)\\[3pt]
\text{independent}\ \Rightarrow\ P(A\cap B)=P(A)\cdot P(B)\\[3pt]
P(B\mid A)=\dfrac{P(A\cap B)}{P(A)}""", "l"),

"r_stat": A(r"""
\text{outlier present} & \text{use the median}\\[3pt]
\sigma^{2}=\dfrac{\sum (x_{k}-\mu)^{2}}{n} & \sigma=\sqrt{\sigma^{2}}\\[9pt]
\text{normal} & 68\%\ \ 95\%\ \ 99.7\%\ \text{within }1,2,3\sigma\\[3pt]
\text{binomial} & \mu=np,\ \ \sigma=\sqrt{npq}\\[3pt]
\text{margin of error} & \approx\dfrac{1}{\sqrt{n}}"""),

# ================================================= 19 · LIMITS
"r_lim": A(r"""
\text{substitute first}\\[2pt]
\dfrac{0}{0}\ \Rightarrow\ \text{factor and cancel, or use the conjugate}\\[7pt]
\dfrac{k}{0}\ \Rightarrow\ \text{the limit does not exist}\\[7pt]
\text{the limit exists only when both one-sided limits agree}""", "l"),

"r_cont": A(r"""
f(a)\ \text{is defined},\quad \lim_{x\to a}f(x)\ \text{exists},\quad \text{they are equal}\\[4pt]
\text{removable — a hole}\qquad \text{jump}\qquad \text{infinite — an asymptote}""", "l"),

"r_liminf": A(r"""
\deg N<\deg D & \text{limit }=0\\[3pt]
\deg N=\deg D & \text{ratio of the leading coefficients}\\[3pt]
\deg N>\deg D & \pm\infty"""),

# ============================================ 20 · DIFFERENTIATION
"r_der": A(r"""
\dfrac{d}{dx}\,x^{n}=nx^{\,n-1} & \dfrac{d}{dx}\,c=0\\[8pt]
(uv)'=u'v+uv' & \left(\dfrac{u}{v}\right)'=\dfrac{u'v-uv'}{v^{2}}\\[10pt]
\multicolumn{2}{l}{\bigl[f(g(x))\bigr]'=f'\bigl(g(x)\bigr)\cdot g'(x)}"""),

"r_der2": A(r"""
(\sin x)'=\cos x & (\cos x)'={-\sin x}\\[3pt]
(\tan x)'=\sec^{2}x & \left(e^{x}\right)'=e^{x}\\[4pt]
(\ln x)'=\dfrac{1}{x} & \left(b^{x}\right)'=b^{x}\ln b"""),

"r_app": A(r"""
\text{tangent} & \text{slope}=f'(a)\ \text{at}\ \bigl(a,f(a)\bigr)\\[3pt]
f'>0\ \text{increasing} & f'<0\ \text{decreasing}\\[3pt]
\text{critical point} & f'=0\ \text{or undefined}\\[3pt]
f''<0\ \text{maximum} & f''>0\ \text{minimum}\\[3pt]
f''=0\ \text{and changes sign} & \text{point of inflection}\\[3pt]
\text{closed interval} & \text{test the ENDPOINTS as well}\\[3pt]
s(t)\to v(t)=s' & \to a(t)=s''"""),

# ============================================== 21 · INTEGRATION
"r_int": A(r"""
\displaystyle\int x^{n}\,dx=\dfrac{x^{\,n+1}}{n+1}+C,\qquad n\neq{-1}\\[9pt]
\displaystyle\int a\,dx=ax+C\\[8pt]
\displaystyle\int_{a}^{b}f(x)\,dx=F(b)-F(a)""", "l"),

"r_intprop": A(r"""
\displaystyle\int_{a}^{a}f=0,\qquad \int_{a}^{b}f={-\int_{b}^{a}}f\\[9pt]
\displaystyle\int_{a}^{b}f=\int_{a}^{c}f+\int_{c}^{b}f\\[9pt]
\text{area}=\displaystyle\int_{a}^{b}\bigl(\text{upper}-\text{lower}\bigr)dx""", "l"),
}


def render(out_dir="ref_math", dpi=300):
    shutil.rmtree(out_dir, ignore_errors=True)
    os.makedirs(out_dir)
    tmp = tempfile.mkdtemp()
    keys = list(E)
    doc = [r"\documentclass[12pt]{article}",
           r"\usepackage[active,tightpage]{preview}",
           r"\usepackage{amsmath,amssymb}",
           r"\usepackage[T1]{fontenc}",
           r"\usepackage[dvipsnames]{xcolor}",
           r"\setlength\PreviewBorder{1.5pt}",
           r"\definecolor{ink}{HTML}{%s}" % INK,
           r"\begin{document}"]
    for k in keys:
        doc.append(r"\begin{preview}$\color{ink}\displaystyle %s$\end{preview}" % E[k])
    doc.append(r"\end{document}")
    tex = os.path.join(tmp, "ref.tex")
    open(tex, "w").write("\n".join(doc))
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                        "-output-directory", tmp, tex], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-4000:])
        raise SystemExit("pdflatex failed")
    subprocess.run(["pdftocairo", "-png", "-transp", "-r", str(dpi),
                    os.path.join(tmp, "ref.pdf"), os.path.join(tmp, "p")], check=True)
    pages = sorted(f for f in os.listdir(tmp) if f.startswith("p-") and f.endswith(".png"))
    assert len(pages) == len(keys), f"{len(pages)} pages vs {len(keys)} cards"
    idx = {}
    for k, p in zip(keys, pages):
        im = Image.open(os.path.join(tmp, p)).convert("RGBA")
        dst = os.path.join(out_dir, k + ".png")
        im.save(dst)
        idx[k] = {"file": dst, "win": im.width / dpi, "hin": im.height / dpi,
                  "aspect": im.width / im.height}
    json.dump(idx, open(os.path.join(out_dir, "_index.json"), "w"), indent=1)
    print(f"{len(idx)} reference cards -> {out_dir} @ {dpi} dpi")


if __name__ == "__main__":
    render()
