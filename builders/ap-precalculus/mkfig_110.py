import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"serif","mathtext.fontset":"cm"})
T,N,O,G,I,B="#17A199","#1F3864","#E8762C","#F0B323","#222E2D","#3B5BA9"
def base(ax,xl,yl,xt,yt):
    ax.set_xlim(*xl);ax.set_ylim(*yl);ax.grid(alpha=0.3,lw=0.6);ax.set_xticks(xt);ax.set_yticks(yt)
    for s in("top","right"):ax.spines[s].set_visible(False)
    ax.spines["left"].set_position(("data",0));ax.spines["bottom"].set_position(("data",0))
    ax.tick_params(labelsize=8,colors=I)
    ax.plot(1,0,">k",transform=ax.get_yaxis_transform(),clip_on=False,ms=4)
    ax.plot(0,1,"^k",transform=ax.get_xaxis_transform(),clip_on=False,ms=4)
# r(x)=(x+2)/(x-3) with hole at (1,-3/2)
r=lambda x:(x+2)/(x-3)
fig,ax=plt.subplots(figsize=(4.1,3.1));fig.patch.set_alpha(0);ax.patch.set_alpha(0)
x1=np.linspace(-6,2.85,400);x2=np.linspace(3.2,8,400)
for x in(x1,x2):ax.plot(x,r(x),color=N,lw=2.2)
ax.axvline(3,color=T,lw=1.4,ls=":");ax.axhline(1,color=O,lw=1.4,ls="--")
ax.plot([1],[r(1)],"o",mfc="white",mec=N,mew=1.8,ms=7,zorder=6)
base(ax,(-6,8),(-5,7),[-4,-2,2,4,6],[-4,-2,2,4,6])
ax.text(3.25,-4.4,r"$x=3$",color=T,fontsize=10.5)
ax.text(-5.8,1.45,r"$y=1$",color=O,fontsize=10.5)
ax.annotate(r"hole $\left(1,-\frac{3}{2}\right)$",xy=(1,r(1)),xytext=(3.45,-2.4),fontsize=10,color=N,
            arrowprops=dict(arrowstyle="->",color=I,lw=0.9,shrinkA=2,shrinkB=5))
ax.text(5.2,5.6,r"$r(x)$",color=N,fontsize=10.5)
fig.tight_layout();fig.savefig("/home/claude/fikr_pptx/prezi/figs/AP1-10_hole.png",dpi=300,transparent=True)
