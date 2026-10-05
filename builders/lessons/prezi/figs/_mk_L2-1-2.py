import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"serif","mathtext.fontset":"cm"})
T,N,O,G,I="#17A199","#1F3864","#E8762C","#F0B323","#222E2D"
fig,ax=plt.subplots(figsize=(4.1,3.1)); fig.patch.set_alpha(0); ax.patch.set_alpha(0)
f=lambda x:2*(x-3)**2-1
x=np.linspace(0.55,5.45,300); ax.plot(x,f(x),color=N,lw=2.4)
ax.plot([3,3],[-1,9.4],color=O,ls="--",lw=1.6)
pts=[(1,7),(2,1),(4,1),(5,7)]
ax.scatter(*zip(*pts),color=T,s=34,zorder=5)
ax.scatter([3],[-1],color=O,s=60,zorder=6)
ax.annotate(r"vertex $(3,-1)$",(3,-1),xytext=(3.4,-2.2),color=O,fontsize=10,arrowprops=dict(arrowstyle="-",color=O,lw=0.8))
ax.text(3.12,8.2,"axis of\nsymmetry\n$x=3$",color=O,fontsize=9.5,va="center",linespacing=1.3)
for px,py in pts:
    ax.text(px+(-0.12 if px<3 else 0.12),py+(0.0),f"$({px},{py})$",color=I,fontsize=8.5,ha="right" if px<3 else "left",va="center")
ax.text(3.2,-3.4,r"$f(x)=2(x-3)^{2}-1$",color=N,fontsize=10.5)
ax.set_xlim(-0.3,6.3); ax.set_ylim(-4.2,9.8)
ax.grid(alpha=0.3,lw=0.6); ax.set_xticks([1,2,4,5,6]); ax.set_yticks([-2,2,4,6,8])
for s in ("top","right"): ax.spines[s].set_visible(False)
for s in ("left","bottom"): ax.spines[s].set_position("zero") if False else None
ax.spines["left"].set_position(("data",0)); ax.spines["bottom"].set_position(("data",0))
ax.tick_params(labelsize=8,colors=I)
ax.plot(1,0,">k",transform=ax.get_yaxis_transform(),clip_on=False,ms=4)
ax.plot(0,1,"^k",transform=ax.get_xaxis_transform(),clip_on=False,ms=4)
ax.set_xlabel("$x$",loc="right",fontsize=10); ax.set_ylabel("$f(x)$",loc="top",rotation=0,fontsize=10)
fig.tight_layout(); fig.savefig("figs/L2-1-2_vertex.png",dpi=300,transparent=True)
