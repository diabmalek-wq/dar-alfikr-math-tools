# SAAT part R — figure items. Every figure is drawn from the same coordinates the answer is computed from.
import math, numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, Polygon
plt.style.use('seaborn-v0_8-paper'); plt.rcParams.update({'font.family':'serif','mathtext.fontset':'cm','savefig.transparent':True})
INK='#1b2f55'; ACC='#b4412e'; SOFT='#cfd9ee'; DPI=460
def m(s): return str(s).replace('-', '−')
ITEMS=[]
def I(sig,fig,figW,unit,topic,lvl,stem,vals,pred,notes,trick,why,fmt=m):
    ITEMS.append(dict(sig=sig,fig=fig,figW=figW,unit=unit,topic=topic,lvl=lvl,stem=stem,vals=vals,pred=pred,notes=notes,trick=trick,why=why,fmt=fmt))
def fig_(w,h,axes=False):
    f,ax=plt.subplots(figsize=(w,h)); ax.set_aspect('equal')
    if not axes: ax.axis('off')
    return f,ax
def save(f,name): f.savefig(f"figs/{name}.png",dpi=DPI,bbox_inches='tight',pad_inches=0.06); plt.close(f)
def ang(P,Q,R):  # angle at Q between QP and QR, degrees
    a=np.array(P)-np.array(Q); b=np.array(R)-np.array(Q)
    return math.degrees(math.acos(np.dot(a,b)/np.linalg.norm(a)/np.linalg.norm(b)))
def arc(ax,Q,P,R,r,label=None,lr=1.7,fs=9,color=ACC):
    a1=math.degrees(math.atan2(P[1]-Q[1],P[0]-Q[0])); a2=math.degrees(math.atan2(R[1]-Q[1],R[0]-Q[0]))
    d=(a2-a1)%360
    if d>180: a1,a2=a2,a1; d=360-d
    ax.add_patch(Arc(Q,2*r,2*r,theta1=a1,theta2=a1+d,color=color,lw=1.1))
    if label:
        mid=math.radians(a1+d/2); ax.text(Q[0]+lr*r*math.cos(mid),Q[1]+lr*r*math.sin(mid),label,ha='center',va='center',fontsize=fs,color=color)
def poly(ax,pts,close=True,**k):
    p=list(pts)+([pts[0]] if close else []); ax.plot([a[0] for a in p],[a[1] for a in p],color=INK,lw=1.5,solid_joinstyle='round',**k)
def vlabel(ax,P,txt,dx,dy): ax.text(P[0]+dx,P[1]+dy,txt,fontsize=11,fontweight='bold',color=INK,ha='center',va='center')
def tick(ax,P,Q,n=1,L=0.07):
    mx,my=(P[0]+Q[0])/2,(P[1]+Q[1])/2; dx,dy=Q[0]-P[0],Q[1]-P[1]; n_=math.hypot(dx,dy); ux,uy=dx/n_,dy/n_
    for k in range(n):
        o=(k-(n-1)/2)*0.07; cx,cy=mx+ux*o,my+uy*o
        ax.plot([cx-uy*L,cx+uy*L],[cy+ux*L,cy-ux*L],color=ACC,lw=1.4)
def axes_graph(w,h,xr,yr,xt,yt,xl='x',yl='y'):
    f,ax=plt.subplots(figsize=(w,h))
    ax.set_xlim(*xr); ax.set_ylim(*yr); ax.set_xticks(xt); ax.set_yticks(yt); ax.grid(alpha=.3,lw=.5)
    for s in ('top','right'): ax.spines[s].set_visible(False)
    for s in ('left','bottom'): ax.spines[s].set_position('zero') if xr[0]<0<xr[1] and s=='left' or yr[0]<0<yr[1] and s=='bottom' else None
    ax.annotate('',xy=(xr[1],0 if yr[0]<0 else yr[0]),xytext=(xr[0],0 if yr[0]<0 else yr[0]),arrowprops=dict(arrowstyle='-|>',color='k',lw=1))
    ax.annotate('',xy=(0 if xr[0]<0 else xr[0],yr[1]),xytext=(0 if xr[0]<0 else xr[0],yr[0]),arrowprops=dict(arrowstyle='-|>',color='k',lw=1))
    ax.set_xlabel(xl,loc='right'); ax.set_ylabel(yl,loc='top',rotation=0)
    ax.tick_params(labelsize=8); return f,ax
def inlab(ax,V,P,Q,txt,d=.42,fs=8.5):
    a=np.array(P)-np.array(V); b=np.array(Q)-np.array(V); a=a/np.linalg.norm(a); b=b/np.linalg.norm(b); u=a+b; u=u/np.linalg.norm(u)
    ax.text(V[0]+d*u[0],V[1]+d*u[1],txt,fontsize=fs,color=ACC,ha='center',va='center',bbox=dict(boxstyle='round,pad=0.12',fc='white',ec='none',alpha=.85))
T="Triangles, polygons & quadrilaterals"; C_="Circles"

# ---------- R1 smallest angle from labelled sides
B=(0,0); Cc=(9,0); x=(81+36-49)/18; A=(x,math.sqrt(36-x*x))
sides={"AB":math.dist(A,B),"BC":math.dist(B,Cc),"CA":math.dist(Cc,A)}
assert [round(v) for v in sides.values()]==[6,9,7]
angs={"∠A":ang(B,A,Cc),"∠B":ang(A,B,Cc),"∠C":ang(A,Cc,B)}
f,ax=fig_(3.4,2.5); poly(ax,[A,B,Cc])
vlabel(ax,A,'A',0,.45); vlabel(ax,B,'B',-.4,-.3); vlabel(ax,Cc,'C',.4,-.3)
ax.text((A[0]+B[0])/2-.95,(A[1]+B[1])/2+.1,'6 cm',fontsize=9,ha='center'); ax.text(4.5,-.55,'9 cm',fontsize=9,ha='center'); ax.text((A[0]+Cc[0])/2+.95,(A[1]+Cc[1])/2+.1,'7 cm',fontsize=9,ha='center')
ax.set_xlim(-2.2,11.2); ax.set_ylim(-1,5.6); save(f,'r_tri_sides')
I("smallest-angle-from-a-labelled-triangle","r_tri_sides",1.9,4,T,2,
  "Triangle ABC is drawn with its side lengths marked. Which angle is the smallest?",
  ["∠C","∠A","∠B","∠B and ∠C are equal"],
  lambda v: v in angs and angs[v]==min(angs.values()),
  ["B: the angle facing the longest side (BC) is the LARGEST, not the smallest.",
   "C: the middle side, CA, faces this angle; it is neither smallest nor largest.",
   "D: the two sides facing them, 7 cm and 6 cm, are different, so the angles differ."],
  "the smallest angle sits opposite the SHORTEST side — find the side first, then read across the triangle to the vertex that faces it",
  "The shortest side is AB = 6 cm; the vertex facing it is C, so ∠C is the smallest (about 41°).")

# ---------- R2 isosceles with ticks, algebraic angles
base=66; h=math.tan(math.radians(base)); A=(0,h); B=(-1,0); Cc=(1,0)
assert round(ang(B,A,Cc))==48
f,ax=fig_(3.0,2.8); poly(ax,[A,B,Cc]); tick(ax,A,B); tick(ax,A,Cc)
vlabel(ax,A,'A',0,.22); vlabel(ax,B,'B',-.15,-.18); vlabel(ax,Cc,'C',.15,-.18)
arc(ax,A,B,Cc,.55,'48°',1.55,9); arc(ax,B,A,Cc,.32,'(3x)°',2.5,9)
ax.set_xlim(-1.6,1.4); ax.set_ylim(-.4,2.7); save(f,'r_iso_ticks')
I("isosceles-base-angle-with-an-algebraic-label","r_iso_ticks",1.7,4,T,2,
  "In the figure, the tick marks show that AB = AC. The angle at A measures 48° and the angle at B measures (3x)°. What is the value of x?",
  [22,16,44,66], lambda v: 48+2*(3*v)==180,
  ["B: the base angle was set equal to the apex angle, 3x = 48.",
   "C: x was doubled after finding it, as if both base angles were added in.",
   "D: this is the size of one base angle, 3x, not the value of x."],
  "equal sides mean equal BASE angles — two of them — so the 180° sum is 48 + 3x + 3x, and 3x is not yet x",
  "48 + 3x + 3x = 180 gives 6x = 132, so x = 22 (each base angle is 66°).")

# ---------- R3 inscribed angle in a semicircle with algebraic labels
t=math.radians(76); A=(-1,0); Bp=(1,0); Cc=(math.cos(t),math.sin(t))
assert round(ang(Bp,A,Cc))==38 and round(ang(A,Bp,Cc))==52 and round(ang(A,Cc,Bp))==90
f,ax=fig_(3.1,2.5); ax.add_patch(Circle((0,0),1,fill=False,color=INK,lw=1.5)); poly(ax,[A,Bp,Cc]); ax.plot(0,0,'o',color=ACC,ms=3)
vlabel(ax,A,'A',-.15,-.12); vlabel(ax,Bp,'B',.15,-.12); vlabel(ax,Cc,'C',.08,.14); ax.text(0,-.14,'O',fontsize=9,color=ACC,ha='center')
inlab(ax,A,Bp,Cc,'(2x+4)°',.7,8); inlab(ax,Bp,A,Cc,'(3x+1)°',.66,8)
ax.set_xlim(-1.4,1.4); ax.set_ylim(-1.15,1.3); save(f,'r_thales')
I("angle-in-a-semicircle-with-algebraic-angles","r_thales",1.8,4,C_,3,
  "In the figure, O is the centre of the circle and AB is a diameter. The angles at A and B of triangle ABC measure (2x + 4)° and (3x + 1)°. What is the value of x?",
  [17,18,35,38], lambda v: (2*v+4)+(3*v+1)==90,
  ["B: the constants 4 and 1 were left out, so 5x = 90.",
   "C: the two angles were set to add to 180°, giving 5x + 5 = 180.",
   "D: this is the size of the angle at A, 2x + 4, not x."],
  "an angle in a semicircle is 90°, so the other two angles add to 90° — not 180° — before the constants are handled",
  "∠C = 90° because AB is a diameter, so (2x + 4) + (3x + 1) = 90, 5x = 85 and x = 17.")

# ---------- R4 trapezoid with crossing diagonals
E=np.array([0.,0.]); Bq=np.array([4.,0.]); a=4*math.sin(math.radians(40))/math.sin(math.radians(30))
Aq=a*np.array([math.cos(math.radians(110)),math.sin(math.radians(110))]); Cq=-0.7*Aq; Dq=-0.7*Bq
def par(P,Q,R,S): u=np.array(Q)-np.array(P); v=np.array(S)-np.array(R); return abs(u[0]*v[1]-u[1]*v[0])<1e-9
assert par(Aq,Bq,Dq,Cq)
trueC=ang(Aq,Cq,Dq)
f,ax=fig_(3.4,3.0); poly(ax,[Aq,Bq,Cq,Dq]); ax.plot([Aq[0],Cq[0]],[Aq[1],Cq[1]],color=INK,lw=1.2); ax.plot([Bq[0],Dq[0]],[Bq[1],Dq[1]],color=INK,lw=1.2)
for P,s,dx,dy in ((Aq,'A',-.3,.2),(Bq,'B',.3,.1),(Cq,'C',.25,-.3),(Dq,'D',-.35,-.05),(E,'E',-.5,.3)): vlabel(ax,P,s,dx,dy)
arc(ax,E,Aq,Bq,.7,'110°',2.0,8.5); arc(ax,Bq,Aq,Dq,.8,'40°',1.9,8.5)
for P,Q in ((Aq,Bq),(Dq,Cq)):
    c=(np.array(P)+np.array(Q))/2; u=(np.array(Q)-np.array(P)); u/=np.linalg.norm(u); n=np.array([-u[1],u[0]])
    ax.plot([c[0]-.12*u[0]+.1*n[0],c[0]+.12*u[0]],[c[1]-.12*u[1]+.1*n[1],c[1]+.12*u[1]],color=ACC,lw=1.3); ax.plot([c[0]-.12*u[0]-.1*n[0],c[0]+.12*u[0]],[c[1]-.12*u[1]-.1*n[1],c[1]+.12*u[1]],color=ACC,lw=1.3)
ax.set_xlim(-3.6,5.0); ax.set_ylim(-4.0,5.4); save(f,'r_trap_diag')
I("alternate-angles-in-a-trapezoid-with-crossing-diagonals","r_trap_diag",2.0,4,T,3,
  "In trapezoid ABCD, AB ∥ DC (marked with arrows) and the diagonals AC and BD meet at E. If ∠AEB = 110° and ∠ABD = 40°, what is the measure of ∠ACD?",
  [30,40,70,110], lambda v: abs(v-trueC)<1e-6,
  ["B: this is ∠BDC, which equals ∠ABD, but the question asks for the angle at C.",
   "C: this is the supplement of ∠AEB, 180° − 110°, a linear-pair angle.",
   "D: this is ∠DEC, which is vertical to ∠AEB, not an angle at C."],
  "parallel sides give alternate angles that carry the 40° across to D; then the vertical angle at E lets triangle DEC be closed",
  "∠BDC = ∠ABD = 40° (alternate angles) and ∠DEC = ∠AEB = 110° (vertical), so ∠DCE = 180° − 110° − 40° = 30°, which is ∠ACD.")

# ---------- R5 decreasing intervals with a flat piece
V=[(-5,1),(-3,-2),(0,3),(2,3),(4,-1),(6,2)]
f,ax=axes_graph(4.2,2.8,(-6.4,7.4),(-3.4,4.6),range(-6,8),range(-3,5))
ax.plot([p[0] for p in V],[p[1] for p in V],color=INK,lw=1.8); ax.plot([p[0] for p in V],[p[1] for p in V],'o',color=ACC,ms=4); save(f,'r_decreasing')
dec=[(V[i][0],V[i+1][0]) for i in range(len(V)-1) if V[i+1][1]<V[i][1]]
inc=[(V[i][0],V[i+1][0]) for i in range(len(V)-1) if V[i+1][1]>V[i][1]]
flat=[(V[i][0],V[i+1][0]) for i in range(len(V)-1) if V[i+1][1]==V[i][1]]
def f5(v): return " and ".join(m(f"({a}, {b})") for a,b in v)
I("intervals-of-decrease-with-a-flat-segment","r_decreasing",2.5,3,"Functions & graphs",2,
  "The graph of a piecewise-linear function f is shown. On which intervals is f decreasing?",
  [dec,inc,sorted(dec+flat),[(-3,4)]], lambda v: sorted(v)==sorted(dec),
  ["B: these are the intervals where the graph rises, so the direction was reversed.",
   "C: the flat segment from x = 0 to x = 2 was counted as decreasing; a level piece neither rises nor falls.",
   "D: the single stretch from the low point to the next low point was taken, ignoring that the graph rises in between."],
  "'decreasing' means the graph FALLS as x increases — a flat piece does not count, and every falling piece must be listed",
  "The graph falls from (−5, 1) to (−3, −2) and from (2, 3) to (4, −1), and is level on (0, 2), so f is decreasing on (−5, −3) and (2, 4).", f5)

# ---------- R6 distance-time slope
f,ax=axes_graph(3.6,2.7,(0,7),(0,60),range(0,8),range(0,61,12),'t (hours)','d (km)')
ax.plot([0,6],[48,0],color=INK,lw=1.8); ax.plot([0,6],[48,0],'o',color=ACC,ms=4)
ax.text(.2,50.5,'(0, 48)',fontsize=8.5); ax.text(5.3,11,'(6, 0)',fontsize=8.5); save(f,'r_dist_time')
I("slope-from-a-labelled-distance-time-graph","r_dist_time",2.2,3,"Functions & graphs",2,
  "The graph shows a cyclist's distance d from home (in km) against time t (in hours). The line passes through the two labelled points. What is the slope of the line?",
  [-8,8,-6,48], lambda v: (0-48)/(6-0)==v,
  ["B: the sign was dropped, but d falls as t rises, so the slope is negative.",
   "C: the elapsed time was reported instead of the rate.",
   "D: the starting distance, the d-intercept, was reported instead of the slope."],
  "slope is rise over run with its sign — a distance that shrinks over time gives a negative slope, and the intercept is not the slope",
  "(0 − 48) ÷ (6 − 0) = −8, so the slope is −8 km per hour.")

# ---------- R7 system from a shaded wedge
f,ax=axes_graph(3.6,3.3,(-3,9),(-3,8),range(-2,9,2),[v for v in range(-2,8,2) if v])
gx,gy=np.meshgrid(np.linspace(-3,9,400),np.linspace(-3,8,400)); mask=(gy>=gx-1)&(gy<=-gx+5)
ax.contourf(gx,gy,mask.astype(float),levels=[.5,1.5],colors=[SOFT],alpha=.9)
xs=np.array([-3,9]); ax.plot(xs,xs-1,color=INK,lw=1.6); ax.plot(xs,-xs+5,color=ACC,lw=1.6)
ax.text(5.4,7.0,'y = x − 1',fontsize=8.5,color=INK,ha='center',bbox=dict(fc='white',ec='none',alpha=.85)); ax.text(7.4,1.0,'y = −x + 5',fontsize=8.5,color=ACC,ha='center',bbox=dict(fc='white',ec='none',alpha=.85)); save(f,'r_system_wedge')
GX,GY=np.meshgrid(np.arange(-3,9),np.arange(-3,8)); GX=GX.ravel()+.5; GY=GY.ravel()+.5  # half-integer points avoid every boundary
true_mask=(GY>=GX-1)&(GY<=-GX+5)
opts7={"y ≥ x − 1  and  y ≤ −x + 5":lambda x,y:(y>=x-1)&(y<=-x+5),"y ≤ x − 1  and  y ≤ −x + 5":lambda x,y:(y<=x-1)&(y<=-x+5),
       "y ≥ x − 1  and  y ≥ −x + 5":lambda x,y:(y>=x-1)&(y>=-x+5),"y ≤ x − 1  and  y ≥ −x + 5":lambda x,y:(y<=x-1)&(y>=-x+5)}
I("system-of-inequalities-from-a-shaded-wedge","r_system_wedge",2.1,2,"Equations & inequalities",3,
  "The shaded region is bounded by the two lines shown, with both boundaries included. Which system of inequalities describes it?",
  list(opts7), lambda v: bool((opts7[v](GX,GY)==true_mask).all()),
  ["B: the region below BOTH lines is the wedge opening downward, not the one shown.",
   "C: the region above BOTH lines is the wedge opening upward.",
   "D: the region above y = −x + 5 and below y = x − 1 is the wedge opening to the right."],
  "test one point inside the shaded region in each inequality — a point such as (1, 2) is above y = x − 1 and below y = −x + 5",
  "The shading is above the rising line y = x − 1 and below the falling line y = −x + 5, so y ≥ x − 1 and y ≤ −x + 5.")

# ---------- R8 inscribed angles on the same arc
def P(d): return (math.cos(math.radians(d)),math.sin(math.radians(d)))
A=P(235); Bc=P(305); Cc=P(40); D=P(120)
assert round(ang(A,Cc,Bc))==35 and round(ang(A,D,Bc))==35
f,ax=fig_(3.2,3.2); ax.add_patch(Circle((0,0),1,fill=False,color=INK,lw=1.5))
for X,Y in ((A,Bc),(A,Cc),(Bc,Cc),(A,D),(Bc,D)): ax.plot([X[0],Y[0]],[X[1],Y[1]],color=INK,lw=1.3)
vlabel(ax,A,'A',-.14,-.12); vlabel(ax,Bc,'B',.14,-.12); vlabel(ax,Cc,'C',.14,.1); vlabel(ax,D,'D',-.12,.14)
inlab(ax,Cc,A,Bc,'(3x+5)°',.62,8); inlab(ax,D,A,Bc,'(5x−15)°',.78,8)
ax.set_xlim(-1.4,1.4); ax.set_ylim(-1.3,1.3); save(f,'r_same_arc')
I("inscribed-angles-on-the-same-arc-are-equal","r_same_arc",1.9,4,C_,3,
  "In the circle shown, ∠ACB = (3x + 5)° and ∠ADB = (5x − 15)°. Both angles stand on the same chord AB. What is the measure of ∠ADB?",
  [35,10,70,145], lambda v: abs(5*(v-5)/3-15-v)<1e-9,
  ["B: this is the value of x, not the angle.",
   "C: this is the size of arc AB, double the inscribed angle.",
   "D: this is the supplement of the angle, as if the two angles were on opposite sides of the chord."],
  "two inscribed angles on the same arc are equal — set the two expressions equal, then substitute back to get the ANGLE, not x",
  "3x + 5 = 5x − 15 gives x = 10, so ∠ADB = 5(10) − 15 = 35°.")
