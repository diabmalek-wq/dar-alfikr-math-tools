import sys,os,shutil
os.makedirs("/home/claude/w8ap/ws18",exist_ok=True)
os.chdir("/home/claude/w8ap/ws18")
sys.path.insert(0,"/home/claude/w8ap")
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"serif","mathtext.fontset":"cm"})
T,N,O,I="#17A199","#1F3864","#E8762C","#222E2D"
# ---- figure for MCQ 3: s(x)=(x+1)(x-3)/(x-1) with hole at x=-3
s=lambda x:(x+1)*(x-3)/(x-1)
fig,ax=plt.subplots(figsize=(4.0,3.0));fig.patch.set_alpha(0);ax.patch.set_alpha(0)
for xs in (np.linspace(-8,0.62,400),np.linspace(1.38,8,400)):
    ax.plot(xs,s(xs),color=N,lw=2)
ax.axvline(1,color=O,lw=1.3,ls="--")
ax.scatter([-1,3],[0,0],color=T,s=28,zorder=6)
ax.scatter([-3],[s(-3)],facecolor="white",edgecolor=N,s=34,zorder=7,lw=1.4)
ax.set_xlim(-8,8.6);ax.set_ylim(-8,10);ax.set_xticks([-8,-6,-4,-2,2,4,6,8]);ax.set_yticks([-6,-3,3,6,9])
ax.grid(alpha=0.3,lw=0.6)
for sp in("top","right"):ax.spines[sp].set_visible(False)
ax.spines["left"].set_position(("data",0));ax.spines["bottom"].set_position(("data",0))
ax.tick_params(labelsize=8,colors=I)
ax.plot(1,0,">k",transform=ax.get_yaxis_transform(),clip_on=False,ms=4)
ax.plot(0,1,"^k",transform=ax.get_xaxis_transform(),clip_on=False,ms=4)
ax.text(1.3,9.2,r"$x=1$",color=O,fontsize=9.5,va="top")
ax.text(5.2,-5.5,r"$y=r(x)$",color=N,fontsize=9.5)
fig.tight_layout();fig.savefig("fig_q3.png",dpi=300,transparent=True)
_src=open("/home/claude/w8ap/wsbase.py").read().replace(r"\includegraphics[height=3.1cm]",r"\includegraphics[height=3.5cm]").replace(r"0.64\linewidth",r"0.62\linewidth").replace(r"0.33\linewidth",r"0.35\linewidth")
exec(_src)
M18=[
(r"Let $r(x)=\dfrac{(x-3)(x+4)}{(x+1)(x-2)}$. What are all of the real zeros of $r$?",
 r"$-4,\ 3$",[r"$-3,\ 4$",r"$-4,\ -1,\ 2,\ 3$",r"$-1,\ 2$"],0,
 r"The numerator is zero at $x=3$ and $x=-4$, and the denominator is not zero at either. {d0}: sign error, reading each factor $x-a$ as $x=-a$. {d1}: listed the zeros of the denominator as well. {d2}: gave only the zeros of the denominator."),
(r"What are all of the real zeros of $f(x)=\dfrac{x^2-9}{x^2-x-6}$?",
 r"$-3$",[r"$-3,\ 3$",r"$3$",r"$-2$"],1,
 r"$f(x)=\dfrac{(x-3)(x+3)}{(x-3)(x+2)}$. At $x=3$ the denominator is $0$, so $3$ is not in the domain (hole). Only $x=-3$ remains. {d0}: counted the hole $x=3$ as a zero. {d1}: kept only the excluded value. {d2}: used the remaining denominator factor."),
(r"The graph of the rational function $r$ is shown. It has $x$-intercepts at $x=-1$ and $x=3$, a vertical asymptote at $x=1$, and a hole at $(-3,-3)$. Which is the solution set of $r(x)\le0$?",
 r"$(-\infty,-3)\cup(-3,-1]\cup(1,3]$",[r"$(-\infty,-1]\cup(1,3]$",r"$(-\infty,-3)\cup(-3,-1]\cup[1,3]$",r"$[-1,1)\cup[3,\infty)$"],2,
 r"The graph is on or below the $x$-axis for $x\le-1$ and for $1<x\le3$, but the hole at $x=-3$ is not in the domain. {d0}: ignored the hole at $x=-3$. {d1}: included the asymptote $x=1$ as a closed endpoint. {d2}: gave the intervals where $r(x)\ge0$ instead."),
(r"Which list gives all of the real zeros of $g(x)=\dfrac{x^3-x}{x^2+4}$?",
 r"$-1,\ 0,\ 1$",[r"$-1,\ 1$",r"There are no real zeros",r"$-2,\ 2$"],3,
 r"$g(x)=\dfrac{x(x-1)(x+1)}{x^2+4}$ and $x^2+4\ne0$ for every real $x$. {d0}: divided out $x$ and lost the zero at $0$. {d1}: thought a denominator with no real zeros means the function has no zeros. {d2}: took the zeros of the denominator's factor $x^2-4$ by mistake."),
(r"What is the real zero of $r(x)=\dfrac{1}{x-2}-\dfrac{3}{x+4}$?",
 r"$5$",[r"$-7$",r"$-5$",r"$r$ has no real zeros"],1,
 r"$r(x)=\dfrac{(x+4)-3(x-2)}{(x-2)(x+4)}=\dfrac{10-2x}{(x-2)(x+4)}$, zero at $x=5$. {d0}: set $x-2=3(x+4)$, cross-multiplying with the wrong sides. {d1}: sign error in the numerator, solving $2x+10=0$. {d2}: subtracted the numerators $1-3$ only and concluded the numerator is never zero."),
(r"Which is the solution set of $\dfrac{x+2}{x-3}\le0$?",
 r"$[-2,3)$",[r"$[-2,3]$",r"$(-\infty,-2]\cup(3,\infty)$",r"$(-2,3)$"],3,
 r"Boundaries $-2$ (zero) and $3$ (asymptote); the quotient is negative between them. {d0}: included $x=3$, where the denominator is zero. {d1}: gave the intervals where the quotient is positive. {d2}: dropped the zero $x=-2$ although $\le$ includes it."),
(r"Which function has exactly one real zero?",
 r"$f(x)=\dfrac{x^2-4}{x-2}$",[r"$f(x)=\dfrac{x^2-4}{x^2+1}$",r"$f(x)=\dfrac{(x-2)(x+1)}{x+3}$",r"$f(x)=\dfrac{x^2+4}{x-1}$"],0,
 r"For the correct choice, $f(x)=x+2$ for $x\ne2$, so the only zero is $-2$ ($x=2$ is a hole). {d0}: has two zeros, $\pm2$, since $x^2+1$ is never $0$. {d1}: has two zeros, $2$ and $-1$, neither excluded. {d2}: has no real zeros, because $x^2+4>0$."),
(r"Let $f(x)=\dfrac{(x-4)^2(x+1)}{(x-4)(x+2)}$. Which statement is true?",
 r"$f$ has exactly one zero, $x=-1$, and a hole at $(4,0)$",[r"$f$ has zeros at $x=-1$ and $x=4$",r"$f$ has a zero at $x=4$ only",r"$f$ has zeros at $x=-2$ and $x=-1$"],2,
 r"Cancel one factor $x-4$: $f(x)=\dfrac{(x-4)(x+1)}{x+2}$ for $x\ne4$. $f$ is undefined at $4$, so $4$ is not a zero, and the graph has a hole at $(4,0)$. {d0}: counted the hole on the $x$-axis as a zero. {d1}: used only the squared factor. {d2}: used the zero of the denominator $x=-2$ as a zero."),
]
F18=[
 dict(tag="Calculator allowed",dok=3,pts=6,
 ctx=r"A biologist models the rate of change of the fish population in a lake, in hundreds of fish per month, by $R(t)=\dfrac{2(t-6)(t+1)}{t+3}$, where $t\ge0$ is the time in months since the study began.",
 parts=[(r"Find the zero of $R$ in the context of the problem. Explain why the other zero of the numerator is not used.",2,
         r"$2(t-6)(t+1)=0$ gives $t=6$ and $t=-1$. The denominator is nonzero at both, but $t=-1$ is outside the domain $t\ge0$. The zero is $t=6$ months.",4.0),
        (r"Solve $R(t)\ge0$ for $t\ge0$ and interpret your answer in context.",2,
         r"On $t\ge0$ the denominator is positive and $t+1>0$, so the sign of $R$ is the sign of $t-6$. $R(t)\ge0$ for $t\ge6$. After $6$ months the population is not decreasing; before then it is decreasing (e.g. $R(0)=-4$).",4.6),
        (r"Find the time at which the rate of change is exactly $4$ hundred fish per month. Give your answer to three decimal places.",2,
         r"$2(t-6)(t+1)=4(t+3)\Rightarrow t^2-7t-12=0\Rightarrow t=\dfrac{7+\sqrt{97}}{2}\approx8.424$ months (the root $\dfrac{7-\sqrt{97}}{2}<0$ is rejected).",4.6)]),
 dict(tag="No calculator",dok=3,pts=6,
 ctx=r"Let $r(x)=\dfrac{x^3-4x^2-5x}{x^2-2x-15}$.",
 parts=[(r"Factor the numerator and the denominator, and state the real zeros of $r$.",2,
         r"$r(x)=\dfrac{x(x-5)(x+1)}{(x-5)(x+3)}$. The numerator is zero at $0,\ 5,\ -1$, but $x=5$ makes the denominator $0$, so it is not in the domain. Zeros: $x=-1$ and $x=0$.",4.6),
        (r"Find the coordinates of the hole in the graph of $r$.",2,
         r"The cancelled factor is $x-5$. The reduced function is $\dfrac{x(x+1)}{x+3}$; at $x=5$: $\dfrac{5\cdot6}{8}=\dfrac{15}{4}$. Hole at $\left(5,\dfrac{15}{4}\right)$.",3.8),
        (r"Solve $r(x)\ge0$. Write your answer in interval notation.",2,
         r"Boundaries from $\dfrac{x(x+1)}{x+3}$: $-3,\ -1,\ 0$. Signs on $(-\infty,-3),\ (-3,-1),\ (-1,0),\ (0,\infty)$: $-,\ +,\ -,\ +$. Include the zeros $-1$ and $0$, exclude $-3$ and the hole $x=5$: $(-3,-1]\cup[0,5)\cup(5,\infty)$.",5.4)]),
]
if __name__=="__main__":
    OUT="/home/claude/deliver/ap_new/L1-8_RationalFunctionsAndZeros";os.makedirs(OUT,exist_ok=True)
    top="AP PRECALCULUS · TOPIC 1.8";title="Rational Functions and Zeros"
    # figure goes to question 3 in both versions
    build("w18",top,title,M18,F18,"fig_q3.png",False); build("w18s",top,title,M18,F18,"fig_q3.png",True)
    shutil.copy("w18.pdf",OUT+"/AP_Precalculus_L1-8_RationalFunctionsAndZeros_Worksheet.pdf")
    shutil.copy("w18s.pdf",OUT+"/AP_Precalculus_L1-8_RationalFunctionsAndZeros_SOLVED.pdf")
