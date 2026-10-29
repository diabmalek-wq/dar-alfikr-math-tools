"""TikZ figures for Session 9. Every figure is built from the SAME numbers as the stem (model units) and scaled to fit."""
import math
from figlib import FIGSTYLE
from lib import fig as _fig
D2R=math.radians
def _u(v):
    n=math.hypot(*v); return (v[0]/n,v[1]/n)
class Fg:
    def __init__(self,pts,W=4.6,H=3.6,extra_box=None):
        W=min(W,5.0); H=min(H,3.1)
        self.m=dict(pts)                       # model points
        xs=[p[0] for p in pts.values()]; ys=[p[1] for p in pts.values()]
        if extra_box: xs+= [extra_box[0],extra_box[2]]; ys+=[extra_box[1],extra_box[3]]
        self.x0,self.y0=min(xs),min(ys)
        bw=max(xs)-self.x0; bh=max(ys)-self.y0
        self.s=min(W/bw,H/bh)
        self.out=[]
    def c(self,p):
        if isinstance(p,str): p=self.m[p]
        return ((p[0]-self.x0)*self.s,(p[1]-self.y0)*self.s)
    def tp(self,p):
        x,y=self.c(p); return "(%.4f,%.4f)"%(x,y)
    def add(self,s): self.out.append(s)
    def line(self,*names,style='ln',close=False):
        self.add(r"\draw[%s] %s%s;"%(style," -- ".join(self.tp(n) for n in names)," -- cycle" if close else ""))
    def poly(self,*names,style='ln'): self.line(*names,style=style,close=True)
    def dash(self,a,b,col='GREY'): self.add(r"\draw[dashed,thick,%s] %s -- %s;"%(col,self.tp(a),self.tp(b)))
    def dot(self,n,col='ORANGE'): self.add(r"\fill[%s] %s circle (1.7pt);"%(col,self.tp(n)))
    def node(self,p,text,font=r'\small',extra=''):
        self.add(r"\node[font=%s,inner sep=1pt%s] at %s {%s};"%(font,extra,self.tp(p),text))
    def vlab(self,n,text,ref,d=0.28,font=r'\small'):
        x,y=self.c(n); rx,ry=self.c(ref); ux,uy=_u((x-rx,y-ry))
        self.add(r"\node[font=%s,inner sep=1pt] at (%.4f,%.4f) {%s};"%(font,x+d*ux,y+d*uy,text))
    def slab(self,a,b,text,ref,d=0.14,font=r'\small',t=0.5,fill=False):
        import re as _re
        plain=_re.sub(r'\\[a-zA-Z]+','x',text).replace('$','').replace('{','').replace('}','')
        w=0.14*len(plain)+0.1; h=0.28
        (x1,y1),(x2,y2)=self.c(a),self.c(b); mx,my=x1+t*(x2-x1),y1+t*(y2-y1)
        nx,ny=-(y2-y1),(x2-x1); nx,ny=_u((nx,ny)); rx,ry=self.c(ref)
        if (mx-rx)*nx+(my-ry)*ny<0: nx,ny=-nx,-ny
        off=d+0.5*(abs(nx)*w+abs(ny)*h)
        self.add(r"\node[font=%s,inner sep=1pt%s] at (%.4f,%.4f) {%s};"%(font,',fill=white' if fill else '',mx+off*nx,my+off*ny,text))
    def rmark(self,v,a,b,s=0.22):
        vx,vy=self.c(v); ax,ay=_u((self.c(a)[0]-vx,self.c(a)[1]-vy)); bx,by=_u((self.c(b)[0]-vx,self.c(b)[1]-vy))
        self.add(r"\draw[thin,INK] (%.4f,%.4f)--(%.4f,%.4f)--(%.4f,%.4f);"%(vx+s*ax,vy+s*ay,vx+s*(ax+bx),vy+s*(ay+by),vx+s*bx,vy+s*by))
    def amark(self,v,a,b,text=None,r=0.45,lr=None,font=r'\footnotesize'):
        vx,vy=self.c(v); a1=math.degrees(math.atan2(self.c(a)[1]-vy,self.c(a)[0]-vx)); a2=math.degrees(math.atan2(self.c(b)[1]-vy,self.c(b)[0]-vx))
        while a2-a1>180: a2-=360
        while a1-a2>180: a2+=360
        self.add(r"\draw[thin,ORANGE] (%.4f,%.4f) arc (%.3f:%.3f:%.3f);"%(vx+r*math.cos(D2R(a1)),vy+r*math.sin(D2R(a1)),a1,a2,r))
        if text:
            lr=lr if lr is not None else r+0.33; am=D2R((a1+a2)/2)
            self.add(r"\node[font=%s,inner sep=0.5pt] at (%.4f,%.4f) {%s};"%(font,vx+lr*math.cos(am),vy+lr*math.sin(am),text))
    def tick(self,a,b,n=1,L=0.09):
        (x1,y1),(x2,y2)=self.c(a),self.c(b); mx,my=(x1+x2)/2,(y1+y2)/2; ux,uy=_u((x2-x1,y2-y1)); nx,ny=-uy,ux
        for k in range(n):
            o=(k-(n-1)/2)*0.09
            self.add(r"\draw[thin,INK] (%.4f,%.4f)--(%.4f,%.4f);"%(mx+o*ux-L*nx,my+o*uy-L*ny,mx+o*ux+L*nx,my+o*uy+L*ny))
    def circle(self,center,r,style='ln'):
        x,y=self.c(center); self.add(r"\draw[%s] (%.4f,%.4f) circle (%.4f);"%(style,x,y,r*self.s))
    def arc(self,center,r,a1,a2,style='very thick,ORANGE'):
        x,y=self.c(center); R=r*self.s
        self.add(r"\draw[%s] (%.4f,%.4f) arc (%.3f:%.3f:%.3f);"%(style,x+R*math.cos(D2R(a1)),y+R*math.sin(D2R(a1)),a1,a2,R))
    def tex(self):
        return _fig("\n".join(self.out),xu=1,yu=1)

# ---------- helpers for right triangles: C at origin ----------
def RT(C,A,B,**kw):
    return Fg({'C':C,'A':A,'B':B},**kw)

def F044():
    f=RT((0,0),(16,0),(0,30),H=4.4); f.poly('A','B','C'); f.rmark('C','A','B')
    f.vlab('A','$A$','C'); f.vlab('B','$B$','C'); f.vlab('C','$C$','A')
    f.slab('C','A','$16$','B'); f.slab('C','B','$30$','A'); return f.tex()
def F045():
    f=RT((0,0),(36,0),(0,48),H=4.0); f.poly('A','B','C'); f.rmark('C','A','B'); f.amark('A','C','B')
    f.vlab('A','$A$','C'); f.vlab('B','$B$','C'); f.vlab('C','$C$','A'); f.slab('C','A','$36$','B'); return f.tex()
def F046():
    y=18*math.tan(D2R(30)); f=Fg({'C':(0,0),'B':(18,0),'A':(0,y)},W=5.2,H=2.4)
    f.poly('A','B','C'); f.rmark('C','B','A'); f.amark('B','C','A','$30^\\circ$',r=0.7,lr=1.05)
    f.vlab('B','$B$','C'); f.vlab('A','$A$','C'); f.vlab('C','$C$','B'); f.slab('C','B','$18$','A'); return f.tex()
def F047():
    f=RT((0,0),(1,0),(0,1),W=2.6,H=2.6); f.poly('A','B','C'); f.rmark('C','A','B'); f.tick('C','A'); f.tick('C','B'); return f.tex()
def F066():
    f=RT((0,0),(9,0),(0,12),H=3.8); f.poly('A','B','C'); f.rmark('C','A','B'); f.amark('A','C','B')
    f.vlab('A','$A$','C'); f.vlab('B','$B$','C'); f.vlab('C','$C$','A'); f.slab('C','A','$9$','B'); f.slab('C','B','$12$','A'); return f.tex()
def F067():
    y=18*math.tan(D2R(35)); f=Fg({'F':(0,0),'D':(18,0),'E':(0,y)},W=5.2,H=3.2)
    f.poly('D','E','F'); f.rmark('F','D','E'); f.amark('D','F','E','$35^\\circ$',r=0.8,lr=1.2)
    f.vlab('D','$D$','F'); f.vlab('E','$E$','F'); f.vlab('F','$F$','D'); f.slab('F','D','$18$','E'); return f.tex()
def F068():
    f=Fg({'V':(0,0),'X':(80,0),'Y':(95*math.cos(D2R(62)),95*math.sin(D2R(62)))},W=5.0,H=3.8)
    f.poly('V','X','Y'); f.amark('V','X','Y','$62^\\circ$',r=0.55,lr=0.9)
    f.slab('V','X','$80$ m','Y'); f.slab('V','Y','$95$ m','X'); f.slab('X','Y','$?$','V'); return f.tex()
def F069():
    f=RT((0,0),(12,0),(0,5),W=5.0,H=2.4); f.poly('A','B','C'); f.rmark('C','A','B')
    f.vlab('A','$A$','C'); f.vlab('B','$B$','C'); f.vlab('C','$C$','A'); f.slab('A','B','$13$','C'); f.slab('C','B','$5$','A'); return f.tex()
def F070():
    h=40*math.tan(D2R(58)); f=Fg({'O':(0,0),'T':(40,0),'K':(40,h)},W=3.4,H=4.2)
    f.poly('O','T','K'); f.line('T','K',style='ln,line width=2.2pt'); f.rmark('T','O','K'); f.amark('O','T','K','$58^\\circ$',r=0.9,lr=1.3)
    f.slab('O','T','$40$ m','K'); f.node(('T',),'') if False else None
    x,y=f.c('K'); f.add(r"\node[font=\small,anchor=west] at (%.3f,%.3f) {top of tower};"%(x+0.12,y)); 
    x,y=f.c(((40+0),h/2)); f.add(r"\node[font=\small,anchor=west] at (%.3f,%.3f) {tower};"%(x+0.12,y)); return f.tex()
def F071():
    Dp=(0,0);Ep=(22,0)
    # F by law of sines (drawing only)
    DF=22*math.sin(D2R(65))/math.sin(D2R(75)); Fp=(DF*math.cos(D2R(40)),DF*math.sin(D2R(40)))
    f=Fg({'D':Dp,'E':Ep,'F':Fp},W=5.2,H=3.4); f.poly('D','E','F')
    f.amark('D','E','F','$40^\\circ$',r=0.9,lr=1.25); f.amark('E','F','D','$65^\\circ$',r=0.55,lr=0.9)
    f.vlab('D','$D$','F'); f.vlab('E','$E$','F'); f.vlab('F','$F$','E'); f.slab('D','E','$22$','F'); return f.tex()
def F072():
    f=RT((0,0),(24,0),(0,7),W=5.2,H=2.0); f.poly('P' if False else 'A','B','C') if False else None
    f=Fg({'R':(0,0),'P':(24,0),'Q':(0,7)},W=5.2,H=2.0); f.poly('P','Q','R'); f.rmark('R','P','Q')
    f.vlab('P','$P$','R'); f.vlab('Q','$Q$','R'); f.vlab('R','$R$','P'); return f.tex()
def F088():
    f=Fg({'Q':(0,0),'R':(10,0),'P':(8*math.cos(D2R(60)),8*math.sin(D2R(60)))},W=5.0,H=3.4); f.poly('P','Q','R')
    f.amark('Q','R','P','$60^\\circ$',r=0.6,lr=0.95); f.vlab('P','$P$','Q',d=0.25); f.vlab('Q','$Q$','R'); f.vlab('R','$R$','Q')
    f.slab('Q','P','$8$','R'); f.slab('Q','R','$10$','P'); return f.tex()
def F100():
    f=RT((0,0),(12,0),(0,5),W=5.2,H=2.2); f.poly('A','B','C'); f.rmark('C','A','B')
    f.slab('C','A','$x+8$','B'); f.slab('C','B','$x+1$','A'); f.slab('A','B','$x+9$','C'); return f.tex()
def F101():
    f=Fg({'C':(0,0),'A':(math.sqrt(3),0),'B':(0,1)},W=4.2,H=2.6); f.poly('A','B','C'); f.rmark('C','A','B')
    f.amark('A','C','B','$30^\\circ$',r=0.75,lr=1.1); f.amark('B','A','C','$60^\\circ$',r=0.45,lr=0.85); return f.tex()
def F102():
    f=Fg({'B':(0,0),'A':(5,0),'C':(0,5*math.sqrt(3))},W=3.6,H=4.0); f.poly('A','B','C'); f.rmark('B','A','C')
    f.vlab('A','$A$','B'); f.vlab('B','$B$','A'); f.vlab('C','$C$','B'); f.slab('A','B','$5$','C'); return f.tex()
def F107():
    f=Fg({'A':(0,0),'C':(15,0),'D':(3,0),'B':(3,6)},W=5.4,H=2.4); f.poly('A','B','C'); f.dash('B','D')
    f.rmark('B','A','C'); f.rmark('D','C','B'); f.vlab('A','$A$','B',d=0.25); f.vlab('C','$C$','B',d=0.25); f.vlab('B','$B$','D'); f.vlab('D','$D$','B')
    f.slab('A','D','$3$','B'); f.slab('D','C','$12$','B'); return f.tex()
def F112():
    r=math.sqrt(30**2-18**2); P=(0,18);Rr=(r,0)
    t=((0)*(Rr[0]-P[0])+(0-P[1])*(Rr[1]-P[1]))/((Rr[0]-P[0])**2+(Rr[1]-P[1])**2); Sf=(P[0]+t*(Rr[0]-P[0]),P[1]+t*(Rr[1]-P[1]))
    f=Fg({'Q':(0,0),'P':P,'R':Rr,'S':Sf},W=4.6,H=3.8); f.poly('P','Q','R'); f.dash('Q','S'); f.rmark('Q','R','P'); f.rmark('S','Q','R')
    f.vlab('P','$P$','Q'); f.vlab('Q','$Q$','S'); f.vlab('R','$R$','Q'); f.vlab('S','$S$','Q',d=0.25); f.slab('Q','P','$18$','R'); f.slab('P','R','$30$','Q'); return f.tex()
def F118():
    f=Fg({'A':(0,0),'B':(26,0),'D':(8,0),'C':(8,12)},W=5.6,H=3.0); f.poly('A','B','C'); f.dash('C','D'); f.rmark('C','A','B'); f.rmark('D','B','C')
    f.vlab('A','$A$','C',d=0.25); f.vlab('B','$B$','C',d=0.25); f.vlab('C','$C$','D'); f.vlab('D','$D$','C')
    x,y=f.c((5.2,3.0)); f.add(r"\node[font=\scriptsize] at (%.3f,%.3f) {$48$};"%(x,y))
    x,y=f.c((15.5,3.0)); f.add(r"\node[font=\scriptsize] at (%.3f,%.3f) {$108$};"%(x,y)); return f.tex()
def F121():
    f=Fg({'P':(0,0),'R':(25,0),'S':(16,0),'Q':(16,12)},W=5.6,H=2.8); f.poly('P','Q','R'); f.dash('Q','S'); f.rmark('Q','P','R'); f.rmark('S','R','Q')
    f.amark('R','S','Q',r=0.7); f.vlab('P','$P$','Q',d=0.25); f.vlab('R','$R$','Q',d=0.25); f.vlab('Q','$Q$','S'); f.vlab('S','$S$','Q'); f.slab('P','S','$16$','Q'); return f.tex()
def F125():
    s=48/7; f=Fg({'C':(0,0),'B':(16,0),'A':(0,12),'D':(s,0),'F':(0,s),'E':(s,s)},W=4.8,H=3.9)
    f.poly('A','B','C'); f.line('D','E','F',style='ln,TEAL'); f.rmark('C','B','A',s=0.2)
    f.vlab('C','$C$','E'); f.vlab('B','$B$','C'); f.vlab('A','$A$','C'); f.vlab('D','$D$','E'); f.vlab('F','$F$','E'); f.vlab('E','$E$','C',d=0.26); f.slab('A','B','$20$','C',t=0.78); return f.tex()
def F133():
    f=Fg({'A':(0,0),'B':(10,0),'D':(8,0),'C':(8,4)},W=5.4,H=2.2); f.poly('A','B','C'); f.dash('C','D'); f.rmark('C','A','B'); f.rmark('D','B','C')
    f.vlab('A','$A$','C',d=0.25); f.vlab('B','$B$','C',d=0.25); f.vlab('C','$C$','D'); f.vlab('D','$D$','C'); f.slab('C','D','$4$','B',d=0.2); f.slab('A','B','$10$','C'); return f.tex()
def F136():
    b=5+5*math.sqrt(3); a=b*math.sqrt(3); f=Fg({'C':(0,0),'A':(a,0),'B':(0,b)},W=5.4,H=3.6)
    f.poly('A','B','C'); f.rmark('C','A','B',s=0.2); f.circle((5,5),5,style='thick,TEAL'); f.dash((5,5),(5,0)) if False else None
    f.add(r"\draw[dashed,thick,GREY] %s -- %s;"%(f.tp((5,5)),f.tp((5,0)))); f.add(r"\fill[TEAL] %s circle (1.5pt);"%f.tp((5,5)))
    x,y=f.c((5,2.5)); f.add(r"\node[font=\small,anchor=west,inner sep=1.5pt] at (%.3f,%.3f) {$5$};"%(x,y))
    f.amark('A','C','B','$30^\\circ$',r=1.0,lr=1.45); f.vlab('A','$A$','C'); f.vlab('B','$B$','C'); f.vlab('C','$C$','A'); return f.tex()
def F143():
    f=Fg({'C':(0,0),'A':(24,0),'B':(0,10),'D':(24*10**2/(24**2+10**2)*0+ (10**2*24)/(24**2+10**2)*0,0)},W=5.4,H=2.4)
    # foot of altitude from C on AB: D = A + t(B-A), t = (C-A).(B-A)/|B-A|^2
    A=(24,0);B=(0,10); t=((0-A[0])*(B[0]-A[0])+(0-A[1])*(B[1]-A[1]))/((B[0]-A[0])**2+(B[1]-A[1])**2); Dp=(A[0]+t*(B[0]-A[0]),A[1]+t*(B[1]-A[1]))
    f=Fg({'C':(0,0),'A':A,'B':B,'D':Dp},W=5.4,H=2.4); f.poly('A','B','C'); f.dash('C','D'); f.rmark('C','A','B'); f.rmark('D','C','A',s=0.2)
    f.amark('A','C','B',r=0.9); f.vlab('A','$A$','C'); f.vlab('B','$B$','C'); f.vlab('C','$C$','D'); f.vlab('D','$D$','C',d=0.25); return f.tex()
def F154():
    f=Fg({'A':(0,0),'B':(13,0),'D':(4,0),'C':(4,6)},W=5.4,H=2.6); f.poly('A','B','C'); f.dash('C','D'); f.rmark('C','A','B'); f.rmark('D','B','C')
    f.vlab('A','$A$','C',d=0.25); f.vlab('B','$B$','C',d=0.25); f.vlab('C','$C$','D'); f.vlab('D','$D$','C'); f.slab('C','D','$6$','B',d=0.2); return f.tex()
def F174():
    f=RT((0,0),(45,0),(0,24),W=5.2,H=2.8); f.poly('A','B','C'); f.rmark('C','A','B'); f.amark('A','C','B',r=0.9)
    f.vlab('A','$A$','C'); f.vlab('B','$B$','C'); f.vlab('C','$C$','A'); f.slab('A','B','$51$','C'); return f.tex()
def F175():
    P=(7,0);R=(0,24); t=((0-P[0])*(R[0]-P[0])+(0-P[1])*(R[1]-P[1]))/((R[0]-P[0])**2+(R[1]-P[1])**2); Sf=(P[0]+t*(R[0]-P[0]),P[1]+t*(R[1]-P[1]))
    f=Fg({'Q':(0,0),'P':P,'R':R,'S':Sf},W=3.4,H=4.6); f.poly('P','Q','R'); f.dash('Q','S'); f.rmark('Q','P','R',s=0.2); f.rmark('S','Q','R',s=0.17)
    f.vlab('P','$P$','Q'); f.vlab('R','$R$','Q'); f.vlab('Q','$Q$','S'); f.slab('Q','P','$7$','R'); f.slab('Q','R','$24$','P')
    x,y=f.c((0.9,2.0)); f.add(r"\node[font=\small,inner sep=1pt] at (%.3f,%.3f) {$h$};"%(x-0.02,y+0.1)); return f.tex()
def F176():
    f=Fg({'C':(0,0),'A':(1,0),'B':(0,1)},W=3.0,H=3.0); f.poly('A','B','C'); f.rmark('C','A','B'); f.tick('C','A'); f.tick('C','B'); f.slab('A','B','$14$','C'); return f.tex()
def F177():
    h=math.sqrt(3)/2; f=Fg({'A':(0,0),'B':(1,0),'C':(0.5,h),'M':(0.5,0)},W=3.6,H=3.2); f.poly('A','B','C'); f.dash('C','M'); f.rmark('M','B','C',s=0.2)
    x,y=f.c((0.5,0.55*h)); f.add(r"\node[font=\small,fill=white,inner sep=1.5pt] at (%.3f,%.3f) {$6\sqrt{3}$};"%(x,y)); return f.tex()
def F179():
    h1=12; h2=math.sqrt(13**2-7**2); f=Fg({'W0':(0,0),'g1':(5,0),'g2':(7,0),'t1':(0,h1),'t2':(0,h2)},W=4.6,H=3.8)
    f.add(r"\draw[very thick,INK] %s -- %s;"%(f.tp((-0.3,0)),f.tp((8,0)))); f.add(r"\draw[very thick,INK] %s -- %s;"%(f.tp((0,0)),f.tp((0,13))))
    f.add(r"\fill[LINE!70] %s rectangle %s;"%(f.tp((-1.1,0)),f.tp((0,13))))
    f.line('g1','t1',style='dashed,thick,GREY'); f.line('g2','t2',style='ln')
    f.add(r"\draw[<->,thin,INK] %s -- %s;"%(f.tp((0,-1.4)),f.tp((5,-1.4)))); f.node((2.5,-2.3),'$5$'); 
    f.add(r"\draw[<->,thin,INK] %s -- %s;"%(f.tp((5,-1.4)),f.tp((7,-1.4)))); f.node((6,-2.3),'$2$')
    f.dot('t2'); x,y=f.c('t2'); f.add(r"\node[font=\small,anchor=east] at (%.3f,%.3f) {$?$};"%(x-0.1,y))
    f.node((4.2,6.2),'$13$ ft',extra=',rotate=%d'%(-round(math.degrees(math.atan2(h2,7))))); return f.tex()
def F180():
    P=(8,0);R=(0,15); t=((0-P[0])*(R[0]-P[0])+(0-P[1])*(R[1]-P[1]))/((R[0]-P[0])**2+(R[1]-P[1])**2); Sf=(P[0]+t*(R[0]-P[0]),P[1]+t*(R[1]-P[1]))
    f=Fg({'Q':(0,0),'P':P,'R':R,'S':Sf},W=3.6,H=4.2); f.poly('P','Q','R'); f.dash('Q','S'); f.rmark('Q','P','R',s=0.2); f.rmark('S','Q','R',s=0.2)
    f.vlab('P','$P$','Q'); f.vlab('R','$R$','Q'); f.vlab('Q','$Q$','S'); f.vlab('S','$S$','Q',d=0.25); f.slab('Q','P','$8$','R'); f.slab('Q','R','$15$','P'); return f.tex()
def F182():
    K=(80*math.cos(D2R(38)),80*math.sin(D2R(38))); f=Fg({'O':(0,0),'K':K,'G':(K[0],0)},W=5.2,H=3.6)
    f.add(r"\draw[very thick,INK] %s -- %s;"%(f.tp((-4,0)),f.tp((K[0]+8,0)))); f.line('O','K',style='ln'); f.dash('K','G'); f.rmark('G','O','K',s=0.2)
    f.amark('O','G','K','$38^\\circ$',r=1.1,lr=1.55); f.slab('O','K','$80$ m','G'); f.dot('K'); x,y=f.c('K'); f.add(r"\node[font=\small,anchor=south west] at (%.3f,%.3f) {kite};"%(x,y)); return f.tex()
def F183():
    f=RT((0,0),(8,0),(0,6),W=4.4,H=3.3); f.poly('A','B','C'); f.rmark('C','A','B'); f.node((2.7,2.0),'area $=24$',font=r'\small') if False else None
    x,y=f.c((2.3,1.7)); f.add(r"\node[font=\small] at (%.3f,%.3f) {area $=24$};"%(x,y)); return f.tex()
def F184():
    f=RT((0,0),(14,0),(0,48),W=2.6,H=4.4); f.poly('A','B','C'); f.rmark('C','A','B'); f.amark('A','C','B','$\\theta$',r=0.8,lr=1.1); f.slab('A','B','$50$','C'); return f.tex()
def F185():
    f=RT((0,0),(20,0),(0,15),W=4.8,H=3.6); f.poly('A','B','C'); f.rmark('C','A','B'); f.slab('C','A','$x+5$','B'); f.slab('C','B','$x$','A'); f.slab('A','B','$25$','C'); return f.tex()
def F186():
    f=Fg({'a':(0,0),'b':(70,0),'c':(70,24),'d':(0,24)},W=5.0,H=1.9); f.poly('a','b','c','d'); f.dash('a','c'); f.slab('a','c','$74$','b',d=0.0) if False else None
    x,y=f.c((35,12)); f.add(r"\node[font=\small,fill=white,inner sep=1.5pt] at (%.3f,%.3f) {$74$};"%(x,y)); return f.tex()
# ----- circles -----
def F006():
    f=Fg({'o':(0,0)},W=3.6,H=3.6,extra_box=(-45,-45,45,45)); f.circle('o',45,style='thick,BLUE'); f.arc('o',45,15,165)
    A=(45*math.cos(D2R(15)),45*math.sin(D2R(15)));B=(45*math.cos(D2R(165)),45*math.sin(D2R(165)))
    f.m['A']=A;f.m['B']=B; f.line('o','A',style='thick,INK'); f.line('o','B',style='thick,INK'); f.dot('o','INK')
    f.node((0,-6),'$O$'); f.slab('o','A','$45$ m','B',d=0.22); f.amark('o','A','B','$\\dfrac{5\\pi}{6}$',r=0.55,lr=1.05,font=r'\scriptsize'); return f.tex()
def F021():
    f=Fg({'o':(0,0)},W=3.8,H=3.8,extra_box=(-1,-1,1,1)); f.circle('o',1,style='thick,BLUE')
    A=(math.cos(D2R(40)),math.sin(D2R(40)));B=(math.cos(D2R(140)),math.sin(D2R(140)));C=(0,-1); f.m.update(A=A,B=B,C=C)
    f.line('o','A',style='thick,INK'); f.line('o','B',style='thick,INK'); f.line('A','C',style='thick,INK'); f.line('B','C',style='thick,INK'); f.line('A','B',style='thick,INK')
    f.amark('o','A','B','$100^\\circ$',r=0.45,lr=0.78,font=r'\scriptsize'); f.dot('o','INK')
    f.vlab('A','$A$','o'); f.vlab('B','$B$','o'); f.vlab('C','$C$','o'); f.node((0.03,-0.14),'$O$',font=r'\scriptsize') if False else None
    x,y=f.c((0,0)); f.add(r"\node[font=\scriptsize,anchor=north] at (%.3f,%.3f) {$O$};"%(x,y-0.04)); return f.tex()
def F028():
    f=Fg({'o':(0,0)},W=3.6,H=3.6,extra_box=(-10,-10,10,10)); f.circle('o',10,style='thick,BLUE')
    A=(10*math.cos(D2R(240)),10*math.sin(D2R(240)));B=(10*math.cos(D2R(300)),10*math.sin(D2R(300))); f.m.update(A=A,B=B)
    f.line('o','A',style='thick,INK'); f.line('o','B',style='thick,INK'); f.line('A','B',style='thick,ORANGE'); f.dot('o','INK')
    f.amark('o','A','B','$60^\\circ$',r=0.55,lr=0.95,font=r'\scriptsize'); f.node((0.2,0.2) if False else (0,0),'')
    f.slab('o','A','$10$','B',d=0.2); f.slab('A','B','chord','o',d=0.25,font=r'\scriptsize'); x,y=f.c((0,0)); f.add(r"\node[font=\scriptsize,anchor=south] at (%.3f,%.3f) {$O$};"%(x,y+0.04)); return f.tex()
def F029():
    f=Fg({'o':(0,0),'P':(0,-9),'Q':(12,-9),'L1':(-6,-9),'L2':(16,-9)},W=5.2,H=3.6,extra_box=(-9,-9,9,9)); f.circle('o',9,style='thick,BLUE')
    f.line('L1','L2',style='thick,INK'); f.line('o','P',style='thick,INK'); f.line('o','Q',style='thick,INK'); f.rmark('P','o','Q',s=0.2); f.dot('o','INK'); f.dot('P','INK'); f.dot('Q','INK')
    x,y=f.c('o'); f.add(r"\node[font=\small,anchor=south] at (%.3f,%.3f) {$O$};"%(x,y+0.04)); f.vlab('P','$P$','o',d=0.25); f.vlab('Q','$Q$','o',d=0.25)
    x,y=f.c('L2'); f.add(r"\node[font=\small,anchor=west] at (%.3f,%.3f) {$\ell$};"%(x+0.05,y))
    f.slab('o','P','$9$','Q',d=0.2); f.slab('o','Q','$15$','P',d=0.2); return f.tex()
def F038():
    r=20*math.sqrt(3); phi=D2R(30); D=(r*math.cos(phi),r*math.sin(phi)); Cc=(r/math.cos(phi),0); B=(r,0)
    f=Fg({'A':(0,0),'B':B,'C':Cc,'D':D},W=5.6,H=3.6,extra_box=(-4,-6,Cc[0]+2,r*0.72))
    f.add(r"\draw[thick,BLUE] %s arc (-10:80:%.4f);"%(f.tp((r*math.cos(D2R(-10)),r*math.sin(D2R(-10)))),r*f.s)) if False else None
    x,y=f.c('A'); R=r*f.s
    f.add(r"\draw[thick,BLUE] (%.4f,%.4f) arc (-12:50:%.4f);"%(x+R*math.cos(D2R(-12)),y+R*math.sin(D2R(-12)),R))
    f.arc('A',r,0,30)
    f.line('A','C',style='thick,INK'); f.line('A','D',style='thick,INK'); f.line('C','D',style='thick,INK'); f.rmark('D','A','C',s=0.2)
    for n in 'ABCD': f.dot(n,'INK')
    f.vlab('A','$A$','D',d=0.25); f.vlab('D','$D$','A',d=0.25)
    xb,yb=f.c('B'); xc,yc=f.c('C'); f.add(r"\node[font=\small,inner sep=1pt] at (%.3f,%.3f) {$B$};"%(xb-0.12,yb-0.27)); f.add(r"\node[font=\small,inner sep=1pt] at (%.3f,%.3f) {$C$};"%(xc+0.12,yc-0.27))
    lx,ly=f.c((0.74*r*math.cos(D2R(15)),0.74*r*math.sin(D2R(15)))); f.add(r"\node[font=\scriptsize,ORANGE!80!black,inner sep=1pt] at (%.3f,%.3f) {$\dfrac{10\sqrt{3}}{3}\pi$};"%(lx,ly))
    f.slab('A','D','$20\\sqrt{3}$','C',d=0.12,font=r'\scriptsize'); return f.tex()
def F039():
    r=18; d=r/math.sin(D2R(50)); al=math.acos(r/d); A=(r*math.cos(al),r*math.sin(al)); B=(r*math.cos(al),-r*math.sin(al)); P=(d,0)
    f=Fg({'o':(0,0),'A':A,'B':B,'P':P},W=5.2,H=3.4,extra_box=(-r,-r,d,r)); f.circle('o',r,style='thick,BLUE'); f.arc('o',r,-math.degrees(al),math.degrees(al))
    f.line('o','A',style='thick,INK'); f.line('o','B',style='thick,INK'); f.line('P','A',style='thick,INK'); f.line('P','B',style='thick,INK'); f.dot('o','INK')
    f.rmark('A','o','P',s=0.2); f.rmark('B','o','P',s=0.2); f.amark('P','A','B','$100^\\circ$',r=0.9,lr=1.45,font=r'\scriptsize')
    f.vlab('A','$A$','o',d=0.25); f.vlab('B','$B$','o',d=0.25); f.vlab('P','$P$','o',d=0.25)
    x,y=f.c('o'); f.add(r"\node[font=\small,anchor=east] at (%.3f,%.3f) {$O$};"%(x-0.08,y)); return f.tex()

def F265():
    r3=6*math.sqrt(3); f=Fg({'M':(0,0),'T':(0,6),'L':(-6,0),'R':(r3,0)},W=5.4,H=3.0)
    f.poly('L','T','R'); f.line('M','T',style='ln,line width=2.2pt'); f.rmark('M','L','T')
    f.amark('L','M','T','$45^\\circ$',r=0.6,lr=1.0); f.amark('R','M','T','$30^\\circ$',r=1.1,lr=1.5)
    f.slab('M','T','$6$ m','R'); return f.tex()
def F194():
    r=5; d=13; al=math.acos(r/d); A=(r*math.cos(al),r*math.sin(al)); B=(r*math.cos(al),-r*math.sin(al)); P=(d,0)
    f=Fg({'o':(0,0),'A':A,'B':B,'P':P},W=5.4,H=3.0,extra_box=(-r,-r,d,r)); f.circle('o',r,style='thick,BLUE')
    f.line('o','A',style='thick,INK'); f.line('o','B',style='thick,INK'); f.line('P','A',style='thick,INK'); f.line('P','B',style='thick,INK'); f.line('o','P',style='dashed,GREY'); f.dot('o','INK')
    f.rmark('A','o','P',s=0.2); f.rmark('B','o','P',s=0.2)
    f.vlab('A','$A$','o',d=0.25); f.vlab('B','$B$','o',d=0.25); f.vlab('P','$P$','o',d=0.25)
    x,y=f.c('o'); f.add(r"\node[font=\small,anchor=east] at (%.3f,%.3f) {$O$};"%(x-0.08,y)); 
    f.slab('o','P','$13$','A'); return f.tex()
FIG={k[1:]:v for k,v in dict(globals()).items() if re.match(r'^F\d\d\d$',k)} if False else None
import re
FIG={('GT-'+k[1:]):v for k,v in dict(globals()).items() if re.match(r'^F\d\d\d$',k)}
FIG['GT-194-2']=F194
