import sys,os,shutil
sys.path.insert(0,"/home/claude/w8ap")
os.chdir("/home/claude/w8ap/ws110")
exec(open("/home/claude/w8ap/wsbase.py").read().replace("for x in o)>34","for x in o)>58"))
M10=[
(r"Let $r(x)=\dfrac{x^2+2x-8}{x^2-3x+2}$. What are the coordinates of the hole in the graph of $r$?",
 r"$(2,6)$",[r"$(2,0)$",r"$(-2,6)$",r"$\left(2,\dfrac16\right)$"],0,
 r"$r(x)=\dfrac{(x+4)(x-2)}{(x-1)(x-2)}$: the factor $x-2$ is in both parts, so the hole is at $x=2$, and the reduced value is $\dfrac{2+4}{2-1}=6$. {d0}: used the original numerator, which is $0$ at $x=2$. {d1}: sign error, reading $x-2$ as $x=-2$. {d2}: inverted the reduced fraction."),
(r"Which statement about the graph of $r(x)=\dfrac{x^2-9}{x^2-6x+9}$ is true?",
 r"A vertical asymptote at $x=3$ and no hole",[r"A hole at $x=3$ and no vertical asymptote",r"A hole at $x=3$ and a vertical asymptote at $x=-3$",r"A hole at $x=-3$ and a vertical asymptote at $x=3$"],1,
 r"$r(x)=\dfrac{(x-3)(x+3)}{(x-3)^2}$. At $x=3$ the numerator has multiplicity $1$ and the denominator multiplicity $2$; since $1<2$ there is no hole, and $r(x)=\dfrac{x+3}{x-3}$ is undefined with unbounded outputs at $x=3$. {d0}: cancelled one factor and stopped, without comparing multiplicities. {d1}: treated $x+3$ as an asymptote factor, although it is in the numerator only. {d2}: sign error and swapped the two roles."),
(r"What is the value of $\displaystyle\lim_{x\to-3}\dfrac{x^2+2x-3}{x+3}$?",
 r"$-4$",[r"$0$",r"$2$",r"The limit does not exist"],2,
 r"$\dfrac{(x+3)(x-1)}{x+3}=x-1$ for $x\ne-3$, so the limit is $-3-1=-4$. {d0}: substituted $x=-3$ into the numerator, which is $0$. {d1}: evaluated $x-1$ at $x=3$. {d2}: concluded the limit fails because the denominator is $0$ at $x=-3$."),
(r"For a rational function $r$, the outputs for inputs near $2$ are shown. Which statement is supported by the table? \par\medskip\noindent\hspace{18pt}$\begin{array}{c|cccccc}x&1.9&1.99&1.999&2.001&2.01&2.1\\\hline r(x)&4.9&4.99&4.999&5.001&5.01&5.1\end{array}$",
 r"The graph of $r$ has a hole at $(2,5)$",[r"The graph of $r$ has a vertical asymptote at $x=2$",r"The graph of $r$ has a hole at $(5,2)$",r"The graph of $r$ has a zero at $x=2$"],3,
 r"The outputs approach $5$ from both sides as $x\to2$, so $\displaystyle\lim_{x\to2}r(x)=5$ and the hole is at $(2,5)$ (here $r(x)=x+3$ with $x\ne2$). {d0}: confused a hole with an asymptote (outputs would be unbounded). {d1}: swapped the coordinates. {d2}: read the input $2$ as a zero."),
(r"Which function has a hole at $x=1$ and a vertical asymptote at $x=-2$?",
 r"$r(x)=\dfrac{(x-1)(x+3)}{(x-1)(x+2)}$",[r"$r(x)=\dfrac{(x+1)(x+3)}{(x+1)(x-2)}$",r"$r(x)=\dfrac{(x+2)(x+3)}{(x-1)(x+2)}$",r"$r(x)=\dfrac{x+3}{(x-1)(x+2)}$"],0,
 r"The hole needs the factor $x-1$ in both numerator and denominator; the asymptote needs $x+2$ in the denominator only. {d0}: sign errors (hole at $-1$, asymptote at $2$). {d1}: swapped the roles (hole at $-2$, asymptote at $1$). {d2}: no common factor, so both denominator zeros are asymptotes."),
(r"Let $r(x)=\dfrac{(x-2)^3(x+1)}{(x-2)^2(x-5)}$. What are the coordinates of the hole in the graph of $r$?",
 r"$(2,0)$",[r"$(2,3)$",r"$(-1,0)$",r"$(5,0)$"],1,
 r"At $x=2$ the multiplicities are $3\ge2$, so there is a hole. The reduced function is $\dfrac{(x-2)(x+1)}{x-5}$, which is $0$ at $x=2$. {d0}: evaluated only the factor $x+1$ at $x=2$, ignoring the rest of the reduced function. {d1}: gave a zero of the numerator instead of the hole. {d2}: gave the asymptote's input with the $y$-value $0$."),
(r"How many holes and how many vertical asymptotes does the graph of $r(x)=\dfrac{(x+1)(x-2)(x-4)}{(x-2)(x-4)(x+5)}$ have?",
 r"$2$ holes and $1$ vertical asymptote",[r"$0$ holes and $3$ vertical asymptotes",r"$1$ hole and $2$ vertical asymptotes",r"$3$ holes and $0$ vertical asymptotes"],2,
 r"The factors $x-2$ and $x-4$ are in both parts, giving holes at $x=2$ and $x=4$; the factor $x+5$ stays in the denominator, giving the asymptote $x=-5$. {d0}: treated every zero of the denominator as an asymptote. {d1}: cancelled only one common factor. {d2}: counted every factor of the numerator as a hole."),
(r"What are the coordinates of the hole in the graph of $r(x)=\dfrac{2x^2-8}{x^2-x-2}$?",
 r"$\left(2,\dfrac83\right)$",[r"$(2,2)$",r"$\left(2,\dfrac43\right)$",r"$\left(2,\dfrac38\right)$"],3,
 r"$r(x)=\dfrac{2(x-2)(x+2)}{(x-2)(x+1)}$, so the hole is at $x=2$ with reduced value $\dfrac{2(2+2)}{2+1}=\dfrac83$. {d0}: used the ratio of leading coefficients, the horizontal asymptote. {d1}: dropped the constant factor $2$. {d2}: inverted the reduced fraction."),
]
F10=[
 dict(tag="Calculator allowed",dok=3,pts=6,
 ctx=r"A sprinter's distance from the start, in metres, is $s(t)=t^2+3t$ for $t$ seconds after the start. The average speed between $1$ second and $t$ seconds is $v(t)=\dfrac{s(t)-s(1)}{t-1}=\dfrac{t^2+3t-4}{t-1}$, for $t>0$ and $t\ne1$.",
 parts=[(r"Factor the numerator, write $v(t)$ in simplified form and give the coordinates of the hole in the graph of $v$.",2,
         r"$t^2+3t-4=(t+4)(t-1)$, so $v(t)=t+4$ for $t\ne1$. Hole at $(1,5)$.",3.0),
        (r"Use limit notation to describe the behaviour of $v(t)$ near $t=1$, and interpret the result in context.",2,
         r"$\displaystyle\lim_{t\to1}v(t)=5$. The average speed over shorter and shorter intervals around $1$ second approaches $5$ metres per second.",3.4),
        (r"Find the time at which the average speed is $7.5$ metres per second. Explain why no time gives an average speed of exactly $5$ metres per second.",2,
         r"$t+4=7.5$, so $t=3.5$ seconds. $v(t)=5$ only for $t=1$, which is the hole: $v(1)$ is undefined, so $5$ is approached but never reached.",3.8)]),
 dict(tag="No calculator",dok=3,pts=6,
 ctx=r"Let $r(x)=\dfrac{(x-3)^2(x+1)(x-2)}{(x-3)(x-2)^2(x+4)}$.",
 parts=[(r"For each of the inputs $x=3$ and $x=2$, compare the multiplicity of the zero in the numerator with its multiplicity in the denominator, and state whether the graph has a hole or not.",2,
         r"$x=3$: numerator multiplicity $2$, denominator multiplicity $1$; $2\ge1$, so the graph has a hole at $x=3$. $x=2$: numerator multiplicity $1$, denominator multiplicity $2$; $1<2$, so there is no hole (a vertical asymptote).",3.8),
        (r"Find the coordinates of the hole.",2,
         r"Reduced function $\dfrac{(x-3)(x+1)}{(x-2)(x+4)}$. At $x=3$ the value is $0$, so $\displaystyle\lim_{x\to3}r(x)=0$ and the hole is $(3,0)$.",3.0),
        (r"State the equations of all vertical asymptotes and the $x$-intercepts of the graph of $r$.",2,
         r"Vertical asymptotes: $x=2$ and $x=-4$. The only $x$-intercept is $(-1,0)$; $x=3$ is a hole, not an intercept.",3.0)]),
]
if __name__=="__main__":
    OUT="/home/claude/deliver/ap_new/L1-10_RationalFunctionsAndHoles"; os.makedirs(OUT,exist_ok=True)
    top="AP PRECALCULUS · TOPIC 1.10"; title="Rational Functions and Holes"
    build("w110",top,title,M10,F10,None,False); build("w110s",top,title,M10,F10,None,True)
    shutil.copy("w110.pdf",OUT+"/AP_Precalculus_L1-10_RationalFunctionsAndHoles_Worksheet.pdf")
    shutil.copy("w110s.pdf",OUT+"/AP_Precalculus_L1-10_RationalFunctionsAndHoles_SOLVED.pdf")
