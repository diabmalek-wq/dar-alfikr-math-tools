import sys; sys.path.insert(0,'/home/claude/cb')
from alg_lib import *
G="Geometry and Trigonometry — "
RT=G+"Right triangles and trigonometry";CI=G+"Circles";AV=G+"Area and volume";LAT=G+"Lines, angles, and triangles"
def close(a,b,e=1e-9): assert abs(a-b)<e,(a,b)
R=math.sqrt
# ---------- RT ----------
x=25; assert x+(3*x-10)==90
add(RT,"Hard","$$\\sin(x^\\circ)=\\cos\\left((3x-10)^\\circ\\right)$$ In the equation above, $x$ is between $0$ and $30$. What is the value of $x$?",None,None,"$25$","Sine and cosine of complementary angles are equal, so $x+(3x-10)=90$, giving $4x=100$ and $x=25$. Check: $3(25)-10=65$ and $25+65=90$.","Students set the angles equal ($x=3x-10$, so $x=5$).")
assert 5*3==15 and 12*3==36 and 13*3==39 and 15+36+39==90
add(RT,"Hard","In right triangle $ABC$, the right angle is at $C$, $\\tan A=\\dfrac{5}{12}$, and $AB=39$. What is the perimeter of triangle $ABC$?",None,None,"$90$","$\\tan A=\\dfrac{BC}{AC}=\\dfrac5{12}$, so the sides are $5k$, $12k$ and $13k$. With $13k=39$, $k=3$, and the legs are $15$ and $36$. The perimeter is $15+36+39=90$.","Students treat $5$ and $12$ as the legs and use $AB=39$ as a leg.")
alt=9*12/15; assert abs(alt-7.2)<1e-12 and 9*9+12*12==15*15
add(RT,"Hard","In right triangle $PQR$, the right angle is at $Q$, $PQ=9$ and $QR=12$. The altitude from $Q$ to hypotenuse $\\overline{PR}$ has length $h$. What is the value of $h$? (Enter as a decimal.)",None,None,"$7.2$","$PR=\\sqrt{81+144}=15$. Equating two expressions for the area: $\\dfrac12(9)(12)=\\dfrac12(15)h$, so $h=\\dfrac{108}{15}=7.2$.","Students average the legs ($10.5$) or use $h=\\dfrac{PQ\\cdot QR}{2}$.")
hyp=14; leg=hyp/R(2)
opts=["$14+14\\sqrt2$","$14+7\\sqrt2$","$28$","$14+7\\sqrt3$"]
close(2*leg+hyp,14+14*R(2)); assert abs((14+7*R(2))-(2*leg+hyp))>1
add(RT,"Hard","An isosceles right triangle has a hypotenuse of length $14$. What is the perimeter of the triangle?",opts,0,"","Each leg is $\\dfrac{14}{\\sqrt2}=7\\sqrt2$. The perimeter is $14+7\\sqrt2+7\\sqrt2=14+14\\sqrt2$.","Students add only one leg ($14+7\\sqrt2$) or use the $30$-$60$-$90$ ratio ($\\sqrt3$).")
s=12; close(s*R(3)/2,6*R(3)); assert 3*s==36
add(RT,"Hard","The height of an equilateral triangle is $6\\sqrt3$. What is the perimeter of the triangle?",None,None,"$36$","For an equilateral triangle with side $s$, the height is $\\dfrac{s\\sqrt3}{2}=6\\sqrt3$, so $s=12$ and the perimeter is $36$.","Students take the height as the side, or use $s=\\dfrac{h}{\\sqrt3}\\cdot2$ incorrectly.")
sin=Fr(3,5); assert Fr(3,5)**2+Fr(4,5)**2==1
add(RT,"Hard","In a right triangle, angle $\\theta$ is acute and $\\sin\\theta=0.6$. What is the value of $\\cos(90^\\circ-\\theta)+\\tan\\theta$?",["$1.35$","$1.6$","$0.75$","$1.2$"],0,"","$\\cos(90^\\circ-\\theta)=\\sin\\theta=0.6$. With $\\sin\\theta=\\dfrac35$, $\\cos\\theta=\\dfrac45$, so $\\tan\\theta=\\dfrac34=0.75$. The sum is $1.35$.","Students use $\\cos(90^\\circ-\\theta)=\\cos\\theta=0.8$ (total $1.55$) or leave out the $\\tan$ term.")
h=R(13**2-7**2); assert abs(h-10.954451)<1e-6
add(RT,"Hard","A $13$-foot ladder leans against a vertical wall. Its base is $5$ feet from the wall. The base is then pulled $2$ feet farther from the wall, so the ladder is $7$ feet from the wall. To the nearest tenth of a foot, how high up the wall does the ladder reach now?",None,None,"$11.0$","Originally $\\sqrt{169-25}=12$ feet. After the move, $\\sqrt{169-49}=\\sqrt{120}\\approx10.95$, which is $11.0$ to the nearest tenth.","Students subtract $2$ from the original height ($10$) instead of recomputing with the Pythagorean theorem.")
q=Fr(120,17); assert abs(8*15/17-120/17)<1e-12 and 8*8+15*15==17*17
add(RT,"Hard","In right triangle $PQR$, the right angle is at $Q$, $PQ=8$ and $QR=15$. Point $S$ is on $\\overline{PR}$ such that $\\overline{QS}$ is perpendicular to $\\overline{PR}$. What is the length of $\\overline{QS}$? (Enter as a fraction.)",None,None,"$\\dfrac{120}{17}$","$PR=\\sqrt{64+225}=17$. The area is $\\dfrac12(8)(15)=60=\\dfrac12(17)(QS)$, so $QS=\\dfrac{120}{17}$.","Students use $QS=\\dfrac{8+15}{2}$ or $\\dfrac{8\\cdot15}{2}$.")
close(math.cos(5*math.pi/3),0.5)
add(RT,"Hard","What is the value of $\\cos\\dfrac{5\\pi}{3}$?",["$\\dfrac12$","$-\\dfrac12$","$\\dfrac{\\sqrt3}{2}$","$-\\dfrac{\\sqrt3}{2}$"],0,"","$\\dfrac{5\\pi}{3}=2\\pi-\\dfrac\\pi3$ is in the fourth quadrant, where cosine is positive. The reference angle is $\\dfrac\\pi3$, and $\\cos\\dfrac\\pi3=\\dfrac12$.","Students give the sine value ($-\\dfrac{\\sqrt3}2$) or ignore the quadrant sign.")
hh=40*math.tan(math.radians(62)); assert round(hh)==75
add(RT,"Hard","From a point on level ground $40$ meters from the base of a tower, the angle of elevation to the top of the tower is $62^\\circ$. To the nearest meter, what is the height of the tower?",None,None,"$75$","$\\tan62^\\circ=\\dfrac{h}{40}$, so $h=40\\tan62^\\circ\\approx75.2$, which rounds to $75$.","Students use $\\sin$ or $\\cos$ ($40\\sin62^\\circ\\approx35$), or leave the calculator in radian mode.")
k=2; assert 3*k==6 and 4*k==8 and 5*k==10 and Fr(1,2)*6*8==24
add(RT,"Hard","In a right triangle, the sine of one acute angle is $\\dfrac35$ and the area of the triangle is $24$. What is the length of the hypotenuse?",None,None,"$10$","The sides are $3k$, $4k$ and $5k$. The area is $\\dfrac12(3k)(4k)=6k^2=24$, so $k=2$ and the hypotenuse is $5k=10$.","Students use $3$ or $4$ as the hypotenuse, or treat the area as one leg.")
assert 14**2+48**2==50**2 and Fr(1,2)*14*48==336
add(RT,"Hard","In a right triangle, the hypotenuse is $50$ and the cosine of an acute angle $\\theta$ is $\\dfrac{7}{25}$. What is the area of the triangle?",None,None,"$336$","The adjacent leg is $50\\cdot\\dfrac7{25}=14$. The opposite leg is $\\sqrt{50^2-14^2}=48$. The area is $\\dfrac12(14)(48)=336$.","Students use $7$ and $25$ as the legs or forget the factor $\\dfrac12$.")
xx=5; assert xx**2+(xx+7)**2==13**2 and Fr(1,2)*5*12==30
add(RT,"Hard","The legs of a right triangle have lengths $x$ and $x+7$, and the hypotenuse is $13$. What is the area of the triangle?",None,None,"$30$","$x^2+(x+7)^2=169$ gives $2x^2+14x-120=0$, so $x^2+7x-60=0$ and $x=5$. The legs are $5$ and $12$, so the area is $30$.","Students accept $x=-12$ or compute the perimeter.")
assert (5*2)*(12*2)==240 and (5*2)**2+(12*2)**2==26**2
add(RT,"Hard","The diagonal of a rectangle is $26$ and the ratio of its two side lengths is $5:12$. What is the area of the rectangle?",None,None,"$240$","The sides are $5k$ and $12k$ and the diagonal is $13k=26$, so $k=2$. The sides are $10$ and $24$ and the area is $240$.","Students take $26$ as a side or compute the perimeter ($68$).")
# ---------- CI ----------
close(72/360*2*math.pi*15,6*math.pi)
add(CI,"Hard","A circle has radius $15$. An arc of the circle subtends a central angle of $72^\\circ$. What is the length of the arc?",["$6\\pi$","$3\\pi$","$12\\pi$","$30\\pi$"],0,"","The arc is $\\dfrac{72}{360}=\\dfrac15$ of the circumference $2\\pi(15)=30\\pi$, so the length is $6\\pi$.","Students use the area formula or $\\dfrac{72}{360}\\pi r^2=45\\pi$.")
close(120/360*math.pi*36,12*math.pi)
add(CI,"Hard","A sector of a circle with radius $6$ has area $12\\pi$. What is the measure, in degrees, of the central angle of the sector?",None,None,"$120$","The full circle has area $36\\pi$. The sector is $\\dfrac{12\\pi}{36\\pi}=\\dfrac13$ of the circle, so the angle is $\\dfrac13(360^\\circ)=120^\\circ$.","Students use arc-length thinking ($\\dfrac{12\\pi}{12\\pi}$ gives $360$) or answer in radians.")
r2=(5**2+12**2); assert r2==169 and 26==2*13
add(CI,"Hard","$$x^2+y^2+10x-24y=0$$ In the $xy$-plane, the graph of the equation above is a circle. What is the diameter of the circle?",None,None,"$26$","Complete the square: $(x+5)^2+(y-12)^2=25+144=169$. The radius is $13$, so the diameter is $26$.","Students answer the radius ($13$) or read the constant term as $r^2$ (giving $0$).")
h=4; assert (0-h)**2+4**2==(8-h)**2+4**2 and h**2+16==32
add(CI,"Hard","In the $xy$-plane, a circle has its center on the $x$-axis and passes through the points $(0,4)$ and $(8,4)$. What is the square of the radius of the circle?",None,None,"$32$","The center is $(h,0)$ with equal distances to both points: $h^2+16=(8-h)^2+16$, so $h=4$. Then $r^2=4^2+4^2=32$.","Students take the center as $(4,4)$ (midpoint) giving $r=4$.")
sl=-Fr(4,3); assert Fr(2+1,6-2)==Fr(3,4) and Fr(3,4)*sl==-1
add(CI,"Hard","In the $xy$-plane, the circle $(x-2)^2+(y+1)^2=25$ passes through the point $(6,2)$. What is the slope of the line tangent to the circle at $(6,2)$?",["$-\\dfrac43$","$\\dfrac34$","$-\\dfrac34$","$\\dfrac43$"],0,"","The radius to $(6,2)$ has slope $\\dfrac{2-(-1)}{6-2}=\\dfrac34$. The tangent is perpendicular to the radius, so its slope is $-\\dfrac43$.","Students use the radius slope itself or its negative without taking the reciprocal.")
assert 2*R(13**2-5**2)==24
add(CI,"Hard","A chord of a circle with radius $13$ is $5$ units from the center of the circle. What is the length of the chord?",None,None,"$24$","The perpendicular from the center bisects the chord, forming a right triangle with hypotenuse $13$ and leg $5$. The other leg is $12$, so the chord is $2(12)=24$.","Students answer $12$ (half the chord) or $\\sqrt{169-25}$ without doubling.")
assert 28+62==90
add(CI,"Hard","Points $A$ and $B$ are the endpoints of a diameter of a circle, and point $C$ is on the circle. The measure of angle $CAB$ is $28^\\circ$. What is the measure, in degrees, of angle $ABC$?",None,None,"$62$","An angle inscribed in a semicircle is a right angle, so angle $ACB=90^\\circ$. Then angle $ABC=180-90-28=62^\\circ$.","Students answer $56$ (doubling) or $152$ (forgetting the right angle).")
assert 6*8==48 and 6**2+8**2==10**2
add(CI,"Hard","Point $P$ is $10$ units from the center $O$ of a circle with radius $6$. Segments $\\overline{PA}$ and $\\overline{PB}$ are tangent to the circle at $A$ and $B$. What is the area of quadrilateral $PAOB$?",None,None,"$48$","Each tangent is perpendicular to its radius, so $PA=\\sqrt{100-36}=8$. Triangle $PAO$ has area $\\dfrac12(8)(6)=24$, and quadrilateral $PAOB$ is two such triangles: $48$.","Students use only one triangle ($24$) or $PA\\cdot OA$ only.")
add(CI,"Hard","In the $xy$-plane, a circle has center $(-3,5)$ and is tangent to the $x$-axis. Which of the following is an equation of the circle?",["$(x+3)^2+(y-5)^2=25$","$(x+3)^2+(y-5)^2=9$","$(x-3)^2+(y+5)^2=25$","$(x+3)^2+(y-5)^2=5$"],0,"","The distance from the center to the $x$-axis is $5$, so the radius is $5$ and $r^2=25$. The equation is $(x+3)^2+(y-5)^2=25$.","Students use the $x$-coordinate ($3$) as the radius or flip the signs of the center.")
assert 6**2+8**2==100 and 2*8==16
add(CI,"Hard","In the $xy$-plane, the line $y=6$ intersects the circle $x^2+y^2=100$ at two points. What is the distance between the two points?",None,None,"$16$","Substituting: $x^2+36=100$, so $x=\\pm8$. The points are $(-8,6)$ and $(8,6)$, which are $16$ units apart.","Students give $8$ (one $x$-value) or $20$ (the diameter).")
close(10*math.pi/(2*math.pi/3),15)
add(CI,"Hard","An arc of a circle has length $10\\pi$ centimeters and subtends a central angle of $\\dfrac{2\\pi}{3}$ radians. What is the radius of the circle, in centimeters?",None,None,"$15$","Arc length $s=r\\theta$, so $r=\\dfrac{10\\pi}{2\\pi/3}=15$.","Students multiply instead of divide ($r=\\dfrac{20\\pi^2}{3}$) or treat the angle as degrees.")
assert 49-1==48
add(CI,"Hard","Two concentric circles have the same center. The outer circle has radius $7$, and the area of the region between the two circles is $48\\pi$. What is the radius of the inner circle?",None,None,"$1$","The ring area is $\\pi(49-r^2)=48\\pi$, so $r^2=1$ and $r=1$.","Students subtract radii ($7-48$) or use circumference.")
per=2*12+12*math.pi/3; close(per,24+4*math.pi)
add(CI,"Hard","A sector of a circle has radius $12$ and a central angle of $60^\\circ$. What is the perimeter of the sector?",["$24+4\\pi$","$4\\pi$","$12+4\\pi$","$24+24\\pi$"],0,"","The curved edge is $\\dfrac{60}{360}(2\\pi\\cdot12)=4\\pi$. The perimeter adds the two radii: $24+4\\pi$.","Students leave out the two straight edges ($4\\pi$) or add only one radius.")
close(10**2+10**2,(2*R(50))**2,1e-9); assert 10*10==100
add(CI,"Hard","A circle has area $50\\pi$. A square is inscribed in the circle so that all four vertices lie on the circle. What is the area of the square?",None,None,"$100$","$r^2=50$, so the diameter is $2\\sqrt{50}=10\\sqrt2$. The diameter is the square's diagonal, so the side is $10$ and the area is $100$.","Students use the diameter as the side or the radius as the diagonal.")
# ---------- AV ----------
assert 90==9*10 and 2*math.pi*3*10==60*math.pi
add(AV,"Hard","A right circular cylinder has volume $90\\pi$ and height $10$. The lateral surface area (excluding the bases) of the cylinder is $k\\pi$. What is the value of $k$?",None,None,"$60$","$\\pi r^2(10)=90\\pi$ gives $r=3$. Lateral area $=2\\pi r h=2\\pi(3)(10)=60\\pi$.","Students include the bases ($78$) or use the wrong radius.")
assert math.sqrt(100-36)==8 and Fr(1,3)*36*8==96
add(AV,"Hard","A right circular cone has base radius $6$ and slant height $10$. The volume of the cone is $k\\pi$. What is the value of $k$?",None,None,"$96$","The height is $\\sqrt{10^2-6^2}=8$. Volume $=\\dfrac13\\pi(36)(8)=96\\pi$.","Students use the slant height as the height ($120$) or omit the $\\dfrac13$ ($288$).")
r=6; assert 4*math.pi*r*r==144*math.pi and Fr(4,3)*216==288
add(AV,"Hard","A sphere has surface area $144\\pi$. The volume of the sphere is $k\\pi$. What is the value of $k$?",None,None,"$288$","$4\\pi r^2=144\\pi$ gives $r=6$. Volume $=\\dfrac43\\pi(6)^3=288\\pi$.","Students use $\\pi r^2=144\\pi$ ($r=12$) or confuse the formulas.")
assert Fr(40)*Fr(27,8)**Fr(2,3)*0 or True
# surface area ratio from volume ratio 8:27 -> linear 2:3 -> area ratio 4:9 ; 40*9/4=90
assert 40*Fr(9,4)==90
add(AV,"Hard","Two similar rectangular prisms have volumes in the ratio $8:27$. The smaller prism has a surface area of $40$. What is the surface area of the larger prism?",None,None,"$90$","The volume ratio $8:27$ means a linear ratio $2:3$. Surface areas scale by $\\left(\\dfrac32\\right)^2=\\dfrac94$, so $40\\cdot\\dfrac94=90$.","Students scale the area by the volume ratio ($\\dfrac{27}{8}$, giving $135$) or by the linear ratio ($60$).")
h=24; assert 36+64+h*h==26*26
add(AV,"Hard","A rectangular box has a base that measures $6$ by $8$. The distance from one corner of the box to the opposite corner (the space diagonal) is $26$. What is the height of the box?",None,None,"$24$","The space diagonal satisfies $6^2+8^2+h^2=26^2$, so $h^2=676-100=576$ and $h=24$.","Students use $\\sqrt{26^2-8^2}$ or the base diagonal ($10$) with only $2$D reasoning.")
rise=12**3/(40*30); close(rise,1.44)
add(AV,"Hard","A rectangular tank has a base that is $40$ centimeters by $30$ centimeters. A solid cube with edge $12$ centimeters is placed in the tank and sinks to the bottom, fully under water. By how many centimeters does the water level rise?",None,None,"$1.44$","The cube displaces its volume, $12^3=1728$ cm$^3$. The rise is $\\dfrac{1728}{40\\cdot30}=1.44$ cm.","Students divide by the cube's base area ($144$) or use the tank volume.")
assert 4*Fr(1,2)*12*10==240 and 6**2+8**2==10**2
add(AV,"Hard","A square pyramid has a base with side length $12$ and a height of $8$. What is the lateral surface area of the pyramid (the four triangular faces, excluding the base)?",None,None,"$240$","The slant height of each face is $\\sqrt{6^2+8^2}=10$. Each face has area $\\dfrac12(12)(10)=60$, so four faces give $240$.","Students use the pyramid height ($8$) as the slant height ($192$).")
e=9; close(e*R(3),9*R(3)); assert e**3==729
add(AV,"Hard","The space diagonal of a cube (the segment joining opposite vertices) has length $9\\sqrt3$. What is the volume of the cube?",None,None,"$729$","For edge $e$ the space diagonal is $e\\sqrt3$, so $e=9$ and the volume is $9^3=729$.","Students use the face diagonal $e\\sqrt2$ or the edge as the diagonal.")
assert (10//2)*(12//2)*(16//2)==240
add(AV,"Hard","A box has interior dimensions $10$ cm by $12$ cm by $16$ cm. Cubes with edge length $2$ cm are packed into the box with no gaps. How many cubes fit?",None,None,"$240$","Along each dimension: $\\dfrac{10}{2}=5$, $\\dfrac{12}{2}=6$, $\\dfrac{16}{2}=8$. The total is $5\\cdot6\\cdot8=240$.","Students divide volumes by $2$ instead of by $2^3=8$ ($960$).")
cyl=math.pi*25*12; cone=math.pi*25*12/3; assert round(cyl/cone)==3
add(AV,"Hard","A cone and a cylinder each have radius $5$ and height $12$. The cone is filled with water and the water is poured into the cylinder, repeatedly, until the cylinder is full. How many full cones of water does it take to fill the cylinder?",None,None,"$3$","The cylinder's volume is $\\pi(25)(12)=300\\pi$ and the cone's is $\\dfrac13$ of that, $100\\pi$. So it takes $3$ cones.","Students answer $\\dfrac13$ or compare surface areas.")
assert round((1.2**3-1)*100,1)==72.8
add(AV,"Hard","The radius of a sphere is increased by $20\\%$. By what percent does the volume of the sphere increase? (Enter as a decimal.)",None,None,"$72.8$","Volume scales with the cube of the radius: $(1.2)^3=1.728$, an increase of $72.8\\%$.","Students give $20\\%$ or $44\\%$ (squared).")
assert 63+18==81
add(AV,"Hard","A solid is formed by placing a hemisphere of radius $3$ on top of a right circular cylinder of radius $3$ and height $7$. The volume of the solid is $k\\pi$. What is the value of $k$?",None,None,"$81$","Cylinder: $\\pi(9)(7)=63\\pi$. Hemisphere: $\\dfrac23\\pi(27)=18\\pi$. Total $81\\pi$.","Students use a full sphere ($36\\pi$, total $99\\pi$) or forget the cylinder.")
# ---------- LAT ----------
x=20; assert 3*x+10==5*x-30 and 3*x+10==70
add(LAT,"Hard","Two parallel lines are cut by a transversal. A pair of alternate interior angles measure $(3x+10)^\\circ$ and $(5x-30)^\\circ$. What is the measure, in degrees, of each of these angles?",None,None,"$70$","Alternate interior angles are equal: $3x+10=5x-30$, so $x=20$ and each angle is $3(20)+10=70^\\circ$.","Students treat the angles as supplementary or answer $x=20$.")
x=14; assert 7*x-4==(2*x+15)+(3*x+9) and 7*x-4==94
add(LAT,"Hard","An exterior angle of a triangle measures $(7x-4)^\\circ$. The two remote interior angles measure $(2x+15)^\\circ$ and $(3x+9)^\\circ$. What is the measure, in degrees, of the exterior angle?",None,None,"$94$","An exterior angle equals the sum of the two remote interior angles: $7x-4=5x+24$, so $x=14$ and the exterior angle is $7(14)-4=94^\\circ$.","Students use the angle sum $180$ for the three listed angles or give $x$.")
x=25; assert (4*x-10)+2*(x+20)==180 and 4*x-10==90
add(LAT,"Hard","In an isosceles triangle, the two base angles each measure $(x+20)^\\circ$ and the vertex angle measures $(4x-10)^\\circ$. What is the measure, in degrees, of the vertex angle?",None,None,"$90$","The angles sum to $180$: $(4x-10)+2(x+20)=180$, so $6x+30=180$ and $x=25$. The vertex angle is $4(25)-10=90^\\circ$.","Students give $x=25$ or forget there are two base angles.")
AC=10*9/6; assert AC==15 and AC-9==6
add(LAT,"Hard","In triangle $ABC$, point $D$ lies on $\\overline{AB}$ and point $E$ lies on $\\overline{AC}$ such that $\\overline{DE}$ is parallel to $\\overline{BC}$. If $AD=6$, $DB=4$ and $AE=9$, what is the length of $\\overline{EC}$?",None,None,"$6$","Since $DE\\parallel BC$, $\\dfrac{AD}{AB}=\\dfrac{AE}{AC}$: $\\dfrac{6}{10}=\\dfrac{9}{AC}$, so $AC=15$ and $EC=15-9=6$.","Students answer $AC=15$ or set $\\dfrac{AD}{DB}=\\dfrac{AE}{AC}$.")
assert 12*20//(12+18)==8 and 20-8==12
add(LAT,"Hard","In triangle $ABC$, $AB=12$ and $AC=18$. The bisector of angle $A$ meets $\\overline{BC}$ at $D$, and $BC=20$. What is the length of the longer of the two segments $BD$ and $DC$?",None,None,"$12$","By the angle bisector theorem $\\dfrac{BD}{DC}=\\dfrac{12}{18}=\\dfrac23$, so $BD=8$ and $DC=12$. The longer segment is $12$.","Students split $20$ in half or assign the larger part to the shorter side.")
n=9; assert (n-2)*180/n==140
add(LAT,"Hard","Each interior angle of a regular polygon measures $140^\\circ$. How many sides does the polygon have?",None,None,"$9$","Each exterior angle is $40^\\circ$, and the exterior angles sum to $360^\\circ$, so $n=\\dfrac{360}{40}=9$.","Students use $\\dfrac{360}{140}$ or $\\dfrac{180}{140}$.")
add(LAT,"Hard","A trapezoid has parallel sides of length $10$ and $24$. A segment joins the midpoints of the two non-parallel sides. What is the length of this segment?",["$17$","$14$","$34$","$7$"],0,"","The midsegment of a trapezoid is parallel to the bases and equals their average: $\\dfrac{10+24}{2}=17$.","Students subtract ($14$) or add ($34$) the bases.")
cnt=sum(1 for t in range(1,40) if 7+t>12 and 7+12>t and 12+t>7); assert cnt==13
add(LAT,"Hard","Two sides of a triangle have lengths $7$ and $12$. The third side has an integer length. How many different integer lengths are possible for the third side?",None,None,"$13$","The third side $t$ satisfies $12-7<t<12+7$, i.e. $5<t<19$. The integers are $6$ through $18$: thirteen values.","Students include the endpoints ($15$) or subtract wrongly ($t<5$).")
k=5; assert Fr(1,2)*8*k==20
add(LAT,"Hard","In the $xy$-plane, a triangle has vertices $(0,0)$, $(8,0)$ and $(3,k)$, where $k>0$. The area of the triangle is $20$. What is the value of $k$?",None,None,"$5$","The base along the $x$-axis is $8$ and the height is $k$, so $\\dfrac12(8)k=20$ and $k=5$. The $x$-coordinate $3$ does not matter.","Students use $3$ as the base or compute $\\dfrac12(3)k=20$.")
a=(180-40)/2; assert a==70 and 180-70-70==40 and 70-40==30
add(LAT,"Hard","In triangle $ABC$, $AB=AC$ and angle $A$ measures $40^\\circ$. Point $D$ lies on $\\overline{AC}$ such that $BD=BC$. What is the measure, in degrees, of angle $ABD$?",None,None,"$30$","The base angles of triangle $ABC$ are $70^\\circ$. In isosceles triangle $BCD$ with $BD=BC$, angle $BDC=\\angle C=70^\\circ$, so angle $CBD=40^\\circ$. Then angle $ABD=70-40=30^\\circ$.","Students assume $BD$ bisects angle $B$ ($35$) or treat angle $BDC$ as $40$.")
