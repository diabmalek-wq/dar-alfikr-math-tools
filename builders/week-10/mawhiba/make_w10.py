"""Week 10 Mawhiba: Unit 3 Activity 2 Paired variables. Every dataset statistic and worked value asserted (numpy only)."""
import json, os
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from mathgen import render
# ---------------- datasets (model values)
D = {}
D["car"]=dict(x=list(range(0,90,10)), y=[280+0.8*d for d in range(0,90,10)], xl="Distance over 100 km (km)", yl="Cost of hire (SAR)", xr=(0,90,10), yr=(270,360,10))
D["spr"]=dict(x=list(range(50,550,50)), y=[12.2,13.8,16.3,17.7,20.4,21.9,24.2,26.1,27.8,30.3], xl="Mass added (g)", yl="Length of spring (cm)", xr=(0,550,50), yr=(0,34,4))
D["fer"]=dict(x=list(range(0,9)), y=[38,52,61,70,74,79,77,80,72], xl="Fertiliser per palm (kg per year)", yl="Dates harvested per palm (kg)", xr=(0,9,1), yr=(30,90,10))
D["chg"]=dict(x=[0,10,20,30,40,50,60], y=[8,23,38,52,66,78,87], xl="Charging time (min)", yl="Battery charge (%)", xr=(0,70,10), yr=(0,100,10))
for k in D: assert len(D[k]["x"])==len(D[k]["y"])
X={k:np.array(D[k]["x"],float) for k in D}; Y={k:np.array(D[k]["y"],float) for k in D}
# car: exact
assert np.allclose(Y["car"],280+0.8*X["car"]) and abs(np.corrcoef(X["car"],Y["car"])[0,1]-1)<1e-12
assert (328-288)/(60-10)==0.8 and 288-0.8*10==280 and 280+0.8*70==336 and 280+0.8*0==280 and 280+0.8*100==360
# spring: inexact but strong linear; ideal 10 + 0.04 m
ms,cs=np.polyfit(X["spr"],Y["spr"],1); rs=np.corrcoef(X["spr"],Y["spr"])[0,1]
assert rs>0.995 and abs(ms-0.04)<0.002 and abs(cs-10)<0.5 and np.abs(Y["spr"]-(10+0.04*X["spr"])).max()<=0.45 and not np.allclose(Y["spr"],10+0.04*X["spr"])
assert 10+0.04*5000==210 and 10+0.04*300==22 and 10+0.04*0==10
# fertiliser: inexact, levels off then falls
rf=np.corrcoef(X["fer"],Y["fer"])[0,1]; assert 0.7<rf<0.93 and Y["fer"].argmax()==7 and Y["fer"][-1]<Y["fer"].max()
qf=np.polyfit(X["fer"],Y["fer"],1); resf=Y["fer"]-np.polyval(qf,X["fer"]); assert resf[0]<0 and resf[4]>0 and resf[-1]<0   # curved residual pattern
# charging: line through first 5 points, then slows
for t,y in zip(D["chg"]["x"][:5],D["chg"]["y"][:5]): assert abs(y-(8+1.45*t))<=1
assert (52-23)/(30-10)==1.45 and 23-1.45*10==8.5 and abs(1.45*25+8.5-44.75)<1e-9 and abs(1.45*90+8.5-139)<1e-9 and 1.45*90+8.5>100
assert np.diff(Y["chg"])[-1]<np.diff(Y["chg"])[0] and 1.45*60+8.5>Y["chg"][-1]       # real data fall below the line later
assert abs(1.45*60+8.5-95.5)<1e-9
INK,WHITE="222E2D","FFFFFF"; E={}
def ex(k,t,c=INK): E[k]=(t,c)
def both(k,t): ex(k,t); ex(k+"_w",t,WHITE)
both("gm",r"m=\dfrac{y_2-y_1}{x_2-x_1}"); both("gc",r"c=y_1-mx_1"); both("gy",r"y=mx+c")
both("carL",r"C=0.8d+280"); both("sprL",r"y=0.04x+10"); both("chgL",r"y=1.45x+8.5")
ex("lab_pt1",r"(x_1,\ y_1)="); ex("lab_pt2",r"(x_2,\ y_2)="); ex("lab_m2",r"m=\dfrac{y_2-y_1}{x_2-x_1}="); ex("lab_c2",r"c=y_1-mx_1="); ex("lab_eqn",r"\text{my equation: }\ y=")
ex("x36",r"x=25"); ex("x90",r"x=90")
json.dump({k:v[0] for k,v in E.items()},open("exprs.json","w"),indent=0); render(E,"w10","mw10")
# ---------------- figures
os.makedirs("fig",exist_ok=True)
INKC,TEALC,NAVYC,GOLDC,ORC="#222E2D","#17A199","#1F3864","#F0B323","#E8762C"
plt.rcParams.update({"font.family":"serif","mathtext.fontset":"cm"})
def scatter(name,k,size=(5,3.8),transparent=False,lines=(),fs=8,tfs=9,dot=26,ticks=None,minor=None,xr=None,yr=None,pts=None):
    d=D[k]; xr=xr or d["xr"]; yr=yr or d["yr"]
    fig,ax=plt.subplots(figsize=size,constrained_layout=True)
    ax.set_xlim(xr[0],xr[1]); ax.set_ylim(yr[0],yr[1])
    ax.xaxis.set_major_locator(MultipleLocator(ticks[0] if ticks else xr[2])); ax.yaxis.set_major_locator(MultipleLocator(ticks[1] if ticks else yr[2]))
    if minor: ax.xaxis.set_minor_locator(MultipleLocator(minor[0])); ax.yaxis.set_minor_locator(MultipleLocator(minor[1]))
    ax.grid(True,which="major",color="#B9D0CD",lw=.7); ax.grid(True,which="minor",color="#DCE9E7",lw=.4); ax.set_axisbelow(True)
    for s in ("right","top"): ax.spines[s].set_color("none")
    ax.spines["left"].set_color(INKC); ax.spines["bottom"].set_color(INKC)
    ax.tick_params(labelsize=fs,colors=INKC,length=3,which="major"); ax.tick_params(length=0,which="minor")
    ax.plot(1,0,">",transform=ax.transAxes,color=INKC,clip_on=False,ms=4); ax.plot(0,1,"^",transform=ax.transAxes,color=INKC,clip_on=False,ms=4)
    ax.set_xlabel(d["xl"],fontsize=tfs,color=INKC,labelpad=3); ax.set_ylabel(d["yl"],fontsize=tfs,color=INKC,labelpad=3)
    xx=np.array([xr[0],xr[1]],float)
    for (m,c,col,lw) in lines: ax.plot(xx,m*xx+c,color=col,lw=lw,zorder=3,solid_capstyle="round")
    xs,ys=(np.array(d["x"]),np.array(d["y"])) if pts is None else pts
    ax.scatter(xs,ys,s=dot,color=NAVYC,edgecolor="white",linewidth=.6,zorder=4)
    fig.savefig(f"fig/{name}.png",dpi=300,transparent=transparent,facecolor=None if transparent else "white"); plt.close(fig)
for k in ("car","spr","fer"):
    scatter(f"th_{k}_doc",k,size=(3.4,2.5),fs=6.5,tfs=6.8,dot=14); scatter(f"th_{k}_s",k,size=(4.0,2.9),transparent=True,fs=8.5,tfs=9,dot=30)
scatter("spr_fit_s","spr",size=(5.6,4.2),transparent=True,fs=10,tfs=11,dot=40,lines=[(0.04,10,ORC,2.0)])
scatter("chg_doc","chg",size=(4.3,3.0),fs=7,tfs=8,dot=22,minor=(5,5)); scatter("chg_s","chg",size=(5.9,4.2),transparent=True,fs=10,tfs=11,dot=34,minor=(5,5))
fig,ax=plt.subplots(figsize=(3.9,3.0)); ax.axis("off")
ax.plot([0,10],[10,40],color="#F0B323",lw=3,solid_capstyle="round"); ax.scatter([1,2,3,4,5,6,7,8,9],[11,17,19,24,25,31,34,36,40],s=70,color="white",edgecolor="#0E4F4C",lw=1.2,zorder=3)
ax.set_xlim(-.5,10.5); ax.set_ylim(5,45); fig.tight_layout(pad=.1); fig.savefig("fig/title_s.png",dpi=300,transparent=True); plt.close(fig)
print("OK")
