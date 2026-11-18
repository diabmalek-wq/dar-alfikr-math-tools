import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, numpy as np, io, base64
from PIL import Image
plt.rcParams.update({'font.family':'serif','font.size':13,'mathtext.fontset':'cm'})
B='#2a54d4'; R='#c8102e'; G='#1b7f45'; K='#0f1b3d'
def axes(ax,xl,yl):
    ax.grid(alpha=.3); ax.spines[['top','right']].set_visible(False)
    ax.spines['left'].set_position('zero'); ax.spines['bottom'].set_position('zero')
    ax.plot(1,0,'>k',transform=ax.get_yaxis_transform(),clip_on=False,ms=6); ax.plot(0,1,'^k',transform=ax.get_xaxis_transform(),clip_on=False,ms=6)
def pitick(ax,lim,step=0.5):
    t=np.arange(lim[0],lim[1]+1e-9,step)
    def lab(v):
        f=__import__('fractions').Fraction(v).limit_denominator(4)
        if f==0: return '0'
        n,d=f.numerator,f.denominator
        s='-' if n<0 else ''; n=abs(n)
        num=('' if n==1 else str(n))+'\\pi'
        return '$%s%s$'%(s,num if d==1 else '\\frac{%s}{%d}'%(num,d))
    ax.set_xticks(t*np.pi); ax.set_xticklabels([lab(v) for v in t])
def enc(fig):
    b=io.BytesIO(); fig.savefig(b,format='png',dpi=200,bbox_inches='tight',facecolor='white'); plt.close(fig)
    im=Image.open(io.BytesIO(b.getvalue())).convert('RGB'); o=io.BytesIO(); im.save(o,'WEBP',quality=88)
    return {'d':base64.b64encode(o.getvalue()).decode(),'w':im.width,'h':im.height}
def f3_4():
    fig,ax=plt.subplots(figsize=(7.5,3.2)); x=np.linspace(0,2*np.pi,400)
    ax.plot(x,np.sin(x),color=B,lw=2.4,label=r'$y=\sin\theta$'); ax.plot(x,np.cos(x),color=R,lw=2.4,ls='--',label=r'$y=\cos\theta$')
    axes(ax,'',''); pitick(ax,(0,2)); ax.set_yticks([-1,0,1]); ax.set_ylim(-1.3,1.3); ax.legend(loc='lower left',frameon=False)
    return enc(fig)
def f3_5():
    fig,ax=plt.subplots(figsize=(7.5,3.4)); x=np.linspace(-0.2,2*np.pi+.2,400)
    ax.plot(x,3*np.sin(x),color=B,lw=2.4,label=r'$y=3\sin\theta$'); ax.plot(x,-2*np.cos(x),color=G,lw=2.4,ls='--',label=r'$y=-2\cos\theta$')
    axes(ax,'',''); pitick(ax,(0,2)); ax.set_yticks([-3,-2,-1,1,2,3]); ax.legend(loc='upper right',frameon=False,ncol=2); ax.set_ylim(-3.6,4.2)
    return enc(fig)
def f3_8():
    fig,ax=plt.subplots(figsize=(7.5,3.6))
    for k in (-1,0,1):
        x=np.linspace(k*np.pi-np.pi/2+.06,k*np.pi+np.pi/2-.06,300); ax.plot(x,np.tan(x),color=B,lw=2.4)
    for a in (-1.5,-.5,.5,1.5): ax.axvline(a*np.pi,color=R,ls='--',lw=1.3)
    axes(ax,'',''); pitick(ax,(-1.5,1.5)); ax.set_ylim(-5,5); ax.set_yticks([-4,-2,2,4]); ax.set_title(r'$y=\tan\theta$: period $\pi$, asymptotes at $\theta=\frac{\pi}{2}+k\pi$',fontsize=12)
    return enc(fig)
def f3_14():
    fig,axs=plt.subplots(1,3,subplot_kw={'projection':'polar'},figsize=(10.5,3.6)); t=np.linspace(0,2*np.pi,1600); fig.subplots_adjust(wspace=.45)
    for ax,(r,tt,c) in zip(axs,[(4*np.cos(3*t),r'$r=4\cos(3\theta)$',B),(5*np.sin(4*t),r'$r=5\sin(4\theta)$',G),(1+3*np.cos(t),r'$r=1+3\cos\theta$',R)]):
        tt2=np.where(r<0,t+np.pi,t); ax.plot(tt2,np.abs(r),color=c,lw=2); ax.set_title(tt,fontsize=12,pad=12); ax.set_rticks([]); ax.grid(alpha=.3)
        ax.set_thetagrids(range(0,360,45),fontsize=8)
    return enc(fig)
def f3_3():
    fig,ax=plt.subplots(figsize=(5.4,5.4)); t=np.linspace(0,2*np.pi,400); ax.plot(np.cos(t),np.sin(t),color=K,lw=1.6)
    import sympy as sp
    for k in range(24):
        a=k*np.pi/12
        if k%2 and k%3: continue
        x,y=np.cos(a),np.sin(a); ax.plot([0,x],[0,y],color='#9aa6c4',lw=.6); ax.plot(x,y,'o',color=B,ms=5)
        s=sp.nsimplify(sp.Rational(k,12)*sp.pi); ax.text(1.17*x,1.17*y,'$%s$'%sp.latex(s),ha='center',va='center',fontsize=10)
    ax.set_aspect('equal'); ax.set_xlim(-1.45,1.45); ax.set_ylim(-1.45,1.45); axes(ax,'',''); ax.set_xticks([]); ax.set_yticks([])
    return enc(fig)
def f1_6():
    fig,axs=plt.subplots(1,4,figsize=(10,2.7)); x=np.linspace(-2,2,300)
    for ax,(f,tt) in zip(axs,[(x**4-3*x**2,r'even, $a>0$'),(-(x**4)+3*x**2,r'even, $a<0$'),(x**3-2*x,r'odd, $a>0$'),(-(x**3)+2*x,r'odd, $a<0$')]):
        ax.plot(x,f,color=B,lw=2.2); ax.set_title(tt,fontsize=12); ax.set_xticks([]); ax.set_yticks([]); ax.set_ylim(-5,5)
        for s in ('top','right'): ax.spines[s].set_visible(False)
        ax.spines['left'].set_position('zero'); ax.spines['bottom'].set_position('zero')
    return enc(fig)
FIGS={k:v() for k,v in {'f3_4':f3_4,'f3_5':f3_5,'f3_8':f3_8,'f3_14':f3_14,'f3_3':f3_3,'f1_6':f1_6}.items()}
if __name__=='__main__':
    for k,v in FIGS.items():
        open('/tmp/claude-0/'+k+'.webp','wb').write(base64.b64decode(v['d'])); print(k,v['w'],v['h'],len(v['d'])//1024,'KB')
