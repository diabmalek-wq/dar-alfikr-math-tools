import sys,os,shutil
M19=[
(r"Which of the following gives all vertical asymptotes of $r(x)=\dfrac{x+4}{x^2-x-12}$?",
 r"$x=-3$ and $x=4$",[r"$x=3$ and $x=-4$",r"$x=-4$",r"$x=-4$, $x=-3$ and $x=4$"],0,
 r"$r(x)=\dfrac{x+4}{(x-4)(x+3)}$; the denominator is $0$ at $x=4$ and $x=-3$ and the numerator is not $0$ at either. {d0}: sign error, reading each factor $x-a$ as $x=-a$. {d1}: set the numerator equal to $0$ (that gives the zero, not an asymptote). {d2}: also counted the zero of the numerator as an asymptote."),
(r"Which of the following gives all vertical asymptotes of $r(x)=\dfrac{x^2-9}{x^2-x-6}$?",
 r"$x=-2$ only",[r"$x=-2$ and $x=3$",r"$x=3$ only",r"$x=-3$ and $x=2$"],1,
 r"$r(x)=\dfrac{(x-3)(x+3)}{(x-3)(x+2)}$; the factor $x-3$ cancels (a hole at $x=3$) and $x+2$ remains. {d0}: treated every zero of the denominator as an asymptote. {d1}: swapped the roles of the two denominator factors. {d2}: sign error, reading $x-a$ as $x=-a$."),
(r"The graph of the rational function $f$ is shown, with vertical asymptotes at $x=-1$ and $x=2$. Which statement is true?",
 r"$\displaystyle\lim_{x\to-1^{+}}f(x)=-\infty$ and $\displaystyle\lim_{x\to2^{+}}f(x)=-\infty$",
 [r"$\displaystyle\lim_{x\to-1^{+}}f(x)=\infty$ and $\displaystyle\lim_{x\to2^{+}}f(x)=-\infty$",
  r"$\displaystyle\lim_{x\to-1^{+}}f(x)=-\infty$ and $\displaystyle\lim_{x\to2^{+}}f(x)=\infty$",
  r"$\displaystyle\lim_{x\to-1^{+}}f(x)=0$ and $\displaystyle\lim_{x\to2^{+}}f(x)=0$"],2,
 r"Right of $x=-1$ the branch falls without bound; right of $x=2$ the branch also falls without bound. {d0}: used the branch on the left of $x=-1$. {d1}: assumed the two sides of $x=2$ differ, as at $x=-1$. {d2}: read the end behavior (the $x$-axis) as the behavior at the asymptotes."),
(r"What is the value of $\displaystyle\lim_{x\to3^{-}}\dfrac{x+1}{x-3}$?",
 r"$-\infty$",[r"$\infty$",r"$0$",r"$4$"],3,
 r"The numerator tends to $4$ and $x-3$ is a tiny negative number, so the quotient decreases without bound. {d0}: ignored the sign of $x-3$ on the left. {d1}: thought a tiny denominator gives a tiny value. {d2}: substituted $x=3$ into the numerator only."),
(r"Let $g(x)=\dfrac{5}{(x+2)^2(x-1)}$. Which statement is true?",
 r"$\displaystyle\lim_{x\to-2^{-}}g(x)=-\infty$ and $\displaystyle\lim_{x\to-2^{+}}g(x)=-\infty$",
 [r"$\displaystyle\lim_{x\to-2^{-}}g(x)=-\infty$ and $\displaystyle\lim_{x\to-2^{+}}g(x)=\infty$",
  r"$\displaystyle\lim_{x\to-2^{-}}g(x)=\infty$ and $\displaystyle\lim_{x\to-2^{+}}g(x)=\infty$",
  r"$\displaystyle\lim_{x\to-2^{-}}g(x)=\infty$ and $\displaystyle\lim_{x\to-2^{+}}g(x)=-\infty$"],1,
 r"$(x+2)^2$ is positive on both sides and $x-1$ is near $-3$, so the quotient is negative on both sides. {d0}: treated the even multiplicity as odd, so the sides differ. {d1}: ignored the negative factor $x-1$. {d2}: odd-multiplicity pattern with the signs reversed."),
(r"A rational function has vertical asymptotes at $x=-2$ and $x=5$, a zero at $x=1$, and no other zeros. Which could be its equation?",
 r"$r(x)=\dfrac{x-1}{(x+2)(x-5)}$",[r"$r(x)=\dfrac{x+1}{(x-2)(x+5)}$",r"$r(x)=\dfrac{(x+2)(x-5)}{x-1}$",r"$r(x)=\dfrac{x-1}{(x-2)(x+5)}$"],2,
 r"Factors $x+2$ and $x-5$ in the denominator give asymptotes at $-2$ and $5$; the factor $x-1$ in the numerator gives the zero at $1$. {d0}: sign errors on every factor. {d1}: swapped the numerator and the denominator. {d2}: sign errors on the denominator factors only."),
(r"The cost, in thousands of dollars, of removing $p$ percent of a pollutant is $C(p)=\dfrac{50p}{100-p}$ for $0\le p<100$. Which is the best interpretation of $\displaystyle\lim_{p\to100^{-}}C(p)=\infty$?",
 r"As the percentage removed gets close to $100$, the cost increases without bound",[r"Removing $100\%$ of the pollutant costs exactly $100$ thousand dollars",r"The cost never exceeds $50$ thousand dollars",r"The cost decreases toward $0$ as the percentage removed approaches $100$"],3,
 r"The denominator $100-p$ is a tiny positive number and the numerator is near $5000$, so $C$ increases without bound. {d0}: read $100$ as the value of the function. {d1}: used the coefficient $50$ as a maximum. {d2}: thought a small denominator gives a small output."),
(r"Which gives all vertical asymptotes of $r(x)=\dfrac{(x-2)^2(x+1)}{(x-2)^3(x+4)}$?",
 r"$x=-4$ and $x=2$",[r"$x=-4$ only",r"$x=-4$, $x=-1$ and $x=2$",r"$x=4$ and $x=-2$"],0,
 r"The zero $2$ has multiplicity $3$ in the denominator and $2$ in the numerator; $3>2$, so one factor $x-2$ remains: an asymptote. $x+4$ gives $x=-4$. {d0}: cancelled the whole factor and called $x=2$ a hole. {d1}: also counted the numerator zero $x=-1$. {d2}: sign errors on both factors."),
]
F19=[
 dict(tag="Calculator allowed",dok=3,pts=6,
 ctx=r"For a thin lens with focal length $10$ cm, an object placed $u$ cm from the lens ($u>10$) forms an image $v$ cm from the lens, where $v(u)=\dfrac{10u}{u-10}$.",
 parts=[(r"Find the equation of the vertical asymptote of the graph of $v$ and justify your answer.",2,
         r"$u-10=0$ at $u=10$ and the numerator is $100\ne0$ there, so the vertical asymptote is $u=10$.",1.5),
        (r"Write a limit statement describing the behavior of $v(u)$ as $u$ approaches $10$ from the right, and interpret it in context.",2,
         r"$\displaystyle\lim_{u\to10^{+}}v(u)=\infty$. As the object gets closer to the focal point, the image distance increases without bound.",1.8),
        (r"Find the object distance $u$ for which the image distance is $25$ cm. Give your answer to three decimal places.",2,
         r"$10u=25(u-10)\Rightarrow15u=250\Rightarrow u=\dfrac{50}{3}\approx16.667$ cm.",1.7)]),
 dict(tag="No calculator",dok=3,pts=6,
 ctx=r"Let $r(x)=\dfrac{x^2-2x-3}{x^2-2x}$.",
 parts=[(r"Factor the numerator and the denominator of $r$. Give the zeros and the equations of all vertical asymptotes.",2,
         r"$r(x)=\dfrac{(x-3)(x+1)}{x(x-2)}$. Zeros: $x=3$ and $x=-1$. No factor cancels, so the vertical asymptotes are $x=0$ and $x=2$.",1.6),
        (r"Find $\displaystyle\lim_{x\to2^{-}}r(x)$ and $\displaystyle\lim_{x\to2^{+}}r(x)$. Show the sign of each factor.",2,
         r"Near $x=2$ the numerator is near $-3$ and $x$ is near $2>0$. From the left $x-2<0$, so the quotient is $\dfrac{-3}{0^{-}}$: $\displaystyle\lim_{x\to2^{-}}r(x)=\infty$. From the right $x-2>0$: $\displaystyle\lim_{x\to2^{+}}r(x)=-\infty$.",1.9),
        (r"Write an equation for a rational function $q$ with vertical asymptotes at $x=0$ and $x=2$ whose graph goes to the same infinity on both sides of $x=0$. Justify your answer.",2,
         r"For example $q(x)=\dfrac{1}{x^2(x-2)}$. The factor $x^2$ has even multiplicity and is positive on both sides of $0$, and $x-2$ is near $-2$, so $q\to-\infty$ from both sides of $x=0$.",1.9)]),
]
if __name__=="__main__":
    os.makedirs("/home/claude/w8ap/ws19",exist_ok=True)
    os.chdir("/home/claude/w8ap/ws19")
    for f in os.listdir("/home/claude/w8ap/ws"):
        if f.endswith(".png") and not os.path.exists(f): shutil.copy("/home/claude/w8ap/ws/"+f,f)
    exec(open("/home/claude/w8ap/wsbase_19.py").read())
    OUT="/home/claude/deliver/ap_new/L1-9_RationalFunctionsVerticalAsymptotes"; os.makedirs(OUT,exist_ok=True)
    top="AP PRECALCULUS · TOPIC 1.9"; title="Rational Functions and Vertical Asymptotes"
    build("w19",top,title,M19,F19,"ws19_fig.png",False); build("w19s",top,title,M19,F19,"ws19_fig.png",True)
    shutil.copy("w19.pdf",OUT+"/AP_Precalculus_L1-9_RationalFunctionsVerticalAsymptotes_Worksheet.pdf")
    shutil.copy("w19s.pdf",OUT+"/AP_Precalculus_L1-9_RationalFunctionsVerticalAsymptotes_SOLVED.pdf")
