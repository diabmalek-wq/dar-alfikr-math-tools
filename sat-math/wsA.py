from common import *

meta = dict(
 code="SAT-M \\textperiodcentered\\ W1-A", week="1", session="A",
 title="Linear Equations: Structure, Rearranging \\& Translating",
 topics="one-variable equations \\textperiodcentered\\ solution-count structure \\textperiodcentered\\ identities \\& coefficient matching \\textperiodcentered\\ literal equations \\textperiodcentered\\ word translation \\textperiodcentered\\ inequalities",
 skills=r"""
\begin{enumerate}[leftmargin=1.6em,itemsep=0pt,label=\textbf{S\arabic*.}]
\item Solve any linear equation (distribute, LCD for fractions/decimals, collect, divide).
\item Spot a repeated \emph{block} and solve for the block instead of the variable.
\item Decide \emph{one / none / infinitely many} solutions by comparing coefficients, before solving.
\item Match coefficients when an equation is true for every $x$; solve for constants.
\item Rearrange literal equations (make any letter the subject).
\item Translate words: ``less than'', consecutive integers, ratios, fixed-plus-rate.
\item Linear inequalities: sign flip, compound and \emph{or}-unions, integer counts, rounding to a feasible whole number.
\item Parameter equations: the solution depends on a constant; integer-solution and case-analysis conditions.
\end{enumerate}""",
 facts=r"""
\begin{itemize}[leftmargin=1.4em,itemsep=0pt]
\item Equal operations on both sides keep an equation true; \textbf{multiplying or dividing an inequality by a negative reverses it}.
\item ``$n$ less than $m$'' $=m-n$; ``at least'' $\ge$; ``at most'' / ``no more than'' $\le$; ``more than'' $>$.
\item Consecutive integers differ by $1$; consecutive \emph{even or odd} integers differ by $2$.
\item A ratio $a:b=m:n$ means $a=mt,\ b=nt$; the whole is $(m+n)t$.
\item Integers with $p\le x\le q$: $q-p+1$ of them; drop one for each open end.
\item Isosceles: two sides equal; every side must be $>0$ and satisfy $a+b>c$.
\item $\frac{p}{q}$ is an integer $\iff q\mid p$ (for integers $p,q$, $q\neq0$).
\end{itemize}""",
 formulas=r"""
\vspace{-4pt}\[
ax+b=cx+d\ \Longrightarrow\ (a-c)x=d-b,\qquad x=\dfrac{d-b}{a-c}\ \ (a\neq c)
\]
\vspace{-8pt}\[
P_{\text{rect}}=2(\ell+w),\qquad A_{\text{trap}}=\dfrac12h(b_1+b_2),\qquad F=\dfrac95C+32
\]
\vspace{-8pt}\[
n,\ n+2,\ n+4,\ n+6\ \ (\text{consecutive odd}),\qquad \text{sum of }k\text{ terms}=k\cdot\text{(mean)}
\]""",
 theory=r"""
\textbf{Master reduction.} Every linear equation collapses to $mx=n$. Then:
\begin{center}\begin{tabular}{@{}lll@{}}\toprule
$m\ne0$ & one solution & $x=\dfrac nm$\\
$m=0,\ n\ne0$ & no solution & $0=n$ is false\\
$m=0,\ n=0$ & infinitely many & $0=0$ is true for all $x$\\\bottomrule\end{tabular}\end{center}
\textbf{Two-parameter identity.} If $p(x+q)=rx+s$ holds for all $x$: coefficients of $x$ match ($p=r$) \emph{and} constants match ($pq=s$).
\textbf{Block rule.} If an expression $E$ occurs, $cE=k\Rightarrow E=\frac kc$; scale or shift the block, never expand it.
\textbf{Inequalities.} Same steps as equations; reverse only on $\times/\div$ by a negative. Compound: operate on all three parts. \emph{And} $=$ overlap, \emph{or} $=$ union. Closed dot $\le,\ge$; open dot $<,>$.
\textbf{Contexts.} Fixed + rate: $y=\text{fee}+\text{rate}\cdot n$. For ``at most'' counts solve, then \emph{round down}; for ``at least'' counts round up.
\textbf{Case analysis.} If a condition (isosceles, equal sums) can occur in several pairings, solve each pairing, then reject any that break positivity or the triangle inequality.
\textbf{Parameter solution.} Solve for $x$ in terms of the constant first; then impose the condition on that expression.""",
 strategy=r"""
\textbf{Shortcuts.} (1) \emph{Block}: if the target is a multiple of an expression you were given, scale---don't solve. (2) \emph{Structure first}: ``how many solutions'', ``no solution'', ``infinitely many'' $\Rightarrow$ compare coefficients, zero algebra. (3) \emph{Back-solve}: plug options into the original equation, middle values first.\\
\textbf{Traps.} Sign of a distributed negative $\cdot$ forgetting to reverse an inequality $\cdot$ ``less than'' written backwards $\cdot$ \emph{and} vs.\ \emph{or} $\cdot$ open vs.\ closed endpoints $\cdot$ answering for $x$ when the question asks for $k$, $x-3$, area, or a product $\cdot$ rounding the wrong way in counting contexts.\\
\textbf{Calculator (Desmos).} Enter each side as $y_1,\,y_2$: intersections = solutions; parallel = none; identical = infinite. Use a slider for a parameter. Keep fractions exact; never round mid-solution.\\
\textbf{Timing.} Easy $\le1.5$ min $\cdot$ Medium $\le3$ $\cdot$ Hard $\le4.5$ $\cdot$ Challenge $\le7$ (total $\approx80$ min, 10 min buffer). If stuck $>$ the limit, mark and return.\\
\textbf{Pattern cues.} ``for all $x$'' $\to$ match coefficients $\cdot$ ``true for infinitely many'' $\to$ same slope \emph{and} same constant $\cdot$ ``what is $(\text{expr})$?'' $\to$ block $\cdot$ ``greatest/least whole number'' $\to$ inequality then round.""")

guided = r"""
\begin{cbox}[title={Example 1 \textemdash\ Structure first (parameter)}]{TEAL}
For what value of $k$ does $4(x-2)+k=4x-3$ have \textbf{(a)} no solution, \textbf{(b)} infinitely many solutions?\\[2pt]
Expand: $4x-8+k=4x-3$. The $x$-coefficients agree ($4=4$), so only the constants decide: compare $k-8$ with $-3$.\\
(b) infinitely many iff $k-8=-3$, so $k=5$. (a) none iff $k-8\ne-3$, i.e.\ \textbf{every} $k\ne5$.\\
\emph{Check:} $k=5$ gives $4x-3=4x-3$ (true always). $k=0$ gives $4x-8=4x-3$ (false always).
\end{cbox}
\begin{cbox}[title={Example 2 \textemdash\ Fractions: clear with the LCD}]{TEAL}
Solve $\dfrac{x+1}{2}-\dfrac{x-3}{5}=2$.\\[2pt]
LCD $=10$: $5(x+1)-2(x-3)=20\ \Rightarrow\ 5x+5-2x+6=20\ \Rightarrow\ 3x+11=20\ \Rightarrow\ x=3$.\\
\emph{Check:} $\frac{4}{2}-\frac{0}{5}=2$. \checkmark\quad (Note the minus sign distributes to \emph{both} terms of $x-3$.)
\end{cbox}
\begin{cbox}[title={Example 3 \textemdash\ Words $\to$ equation (consecutive integers)}]{TEAL}
The sum of three consecutive even integers is $54$. What is the largest?\\[2pt]
Let them be $n,\ n+2,\ n+4$: $3n+6=54\Rightarrow n=16$. Integers: $16,\,18,\,20$. Largest $=\mathbf{20}$.\\
\emph{Shortcut:} $54\div3=18$ is the middle term; add $2$.
\end{cbox}"""

P = []
def add(lv, q, hint, sol, ans=None, opts=None, correct=None, fig=None, lines=None):
    d = dict(lv=lv, q=q, hint=hint, sol=sol)
    if opts is not None:
        d['opts'] = opts; d['correct'] = correct
    else:
        d['ans'] = ans
    if fig: d['fig'] = fig
    if lines: d['lines'] = lines
    P.append(d)

# ---------------- EASY ----------------
add('E', r"If $4x+3=27$, what is the value of $8x+6$?",
    r"$8x+6$ is a multiple of $4x+3$.",
    r"$8x+6=2(4x+3)=2(27)=54$. (Solving: $x=6$, $8(6)+6=54$.)",
    opts=[r"$33$", r"$48$", r"$54$", r"$60$"], correct=2)
add('E', r"What is the solution to $-2(3x-5)=4x-10$?",
    r"Distribute the $-2$ to \emph{both} terms.",
    r"$-6x+10=4x-10\Rightarrow 20=10x\Rightarrow x=2$.",
    opts=[r"$-2$", r"$0$", r"$2$", r"$20$"], correct=2)
add('E', r"What is the solution to $\dfrac{2x+1}{3}=\dfrac{x-4}{2}$?",
    r"Cross-multiply.",
    r"$2(2x+1)=3(x-4)\Rightarrow4x+2=3x-12\Rightarrow x=-14$.",
    opts=[r"$-14$", r"$-2$", r"$2$", r"$14$"], correct=0)
add('E', r"The formula $F=\dfrac95C+32$ converts a temperature from degrees Celsius $C$ to degrees Fahrenheit $F$. Which equation gives $C$ in terms of $F$?",
    r"Undo $+32$ first, then undo $\times\frac95$.",
    r"$F-32=\frac95C\Rightarrow C=\frac59(F-32)$.",
    opts=[r"$C=\dfrac59(F-32)$", r"$C=\dfrac59F-32$", r"$C=\dfrac95(F-32)$", r"$C=\dfrac59F+32$"], correct=0)
add('E', r"Three less than twice a number is five more than the number. What is the number?",
    r"``Three less than $2n$'' is $2n-3$.",
    r"$2n-3=n+5\Rightarrow n=8$.",
    ans="8")
add('E', r"What is the least integer $x$ that satisfies $-3x+7\le 22$?",
    r"Dividing by $-3$ reverses the inequality.",
    r"$-3x\le15\Rightarrow x\ge-5$. Least integer: $-5$.",
    ans="-5")

# ---------------- MEDIUM ----------------
add('M', r"For what value of $k$ does the equation $\dfrac12(6x+k)=3x+7$ have infinitely many solutions?",
    r"After distributing, the $x$-terms already match; make the constants match.",
    r"$3x+\frac k2=3x+7$. Infinitely many iff $\frac k2=7$, so $k=14$.",
    ans="14")
add('M', r"In the equation $(a-2)x+3=5x+7$, $a$ is a constant. If the equation has no solution, what is the value of $a$?",
    r"No solution: equal $x$-coefficients, different constants.",
    r"Need $a-2=5\Rightarrow a=7$. Constants $3\ne7$, so the statement is false for every $x$: no solution. ($a\ne7$ gives exactly one solution.)",
    opts=[r"$2$", r"$3$", r"$5$", r"$7$"], correct=3)
add('M', r"If $3(2x+a)=bx+21$ is true for all values of $x$, where $a$ and $b$ are constants, what is $a+b$?",
    r"Expand the left side, then match $x$-coefficients and constants.",
    r"$6x+3a=bx+21$: $b=6$, $3a=21\Rightarrow a=7$. $a+b=13$.",
    ans="13")
add('M', r"The Dar Alfikr robotics club has girls and boys in the ratio $3:5$. There are $96$ members. How many more boys than girls are in the club?",
    r"Total parts $=8$; find one part.",
    r"$8t=96\Rightarrow t=12$: girls $36$, boys $60$; difference $24$ (equivalently $2t$).",
    opts=[r"$12$", r"$24$", r"$36$", r"$60$"], correct=1)
add('M', r"The area of a trapezoid is $A=\dfrac12h(b_1+b_2)$. Which expression equals $b_1$?",
    r"Clear the $\frac12$ and the $h$ first.",
    r"$2A=h(b_1+b_2)\Rightarrow\frac{2A}h=b_1+b_2\Rightarrow b_1=\frac{2A}h-b_2$.",
    opts=[r"$\dfrac{2A-b_2}{h}$", r"$\dfrac{A}{2h}-b_2$", r"$\dfrac{2A}{h+b_2}$", r"$\dfrac{2A}{h}-b_2$"], correct=3)
add('M', r"A tutoring academy charges a one-time registration fee of $150$ SAR plus $45$ SAR per session. Ahmad paid a total of $690$ SAR. How many sessions did he attend?",
    r"Subtract the fee \emph{before} dividing by the rate.",
    r"$150+45n=690\Rightarrow45n=540\Rightarrow n=12$.",
    opts=[r"$12$", r"$15$", r"$19$", r"$540$"], correct=0)
add('M', r"A Riyadh Metro card holds $60$ SAR. Each trip costs $4.5$ SAR. Sara wants at least $5$ SAR to remain on the card. What is the greatest number of trips she can take?",
    r"$60-4.5t\ge5$; the count of trips must be a whole number.",
    r"$4.5t\le55\Rightarrow t\le12.\overline{2}$. Whole trips: $12$ (check: $60-54=6\ge5$; $13$ trips leave $1.5<5$).",
    opts=[r"$11$", r"$12$", r"$13$", r"$14$"], correct=1)
add('M', r"How many integers $x$ satisfy $-7<3-2x\le9$?",
    r"Subtract $3$ from all three parts, then divide by $-2$ and flip \emph{both} signs.",
    r"$-10<-2x\le6\Rightarrow5>x\ge-3$, i.e.\ $-3\le x<5$: $-3,\dots,4$, which is $8$ integers.",
    opts=[r"$7$", r"$8$", r"$9$", r"$10$"], correct=1)
add('M', r"What is the solution to $0.4(x+10)=0.25x+7.6$?",
    r"Distribute, then collect the $x$-terms on the left.",
    r"$0.4x+4=0.25x+7.6\Rightarrow0.15x=3.6\Rightarrow x=24$.",
    ans="24")
add('M', r"The figure shows a rectangular school garden with width $w$ meters and length $(2w-3)$ meters. Its perimeter is $54$ meters. What is its area, in square meters?",
    r"Write the perimeter equation, find $w$, then the area.",
    r"$2\big(w+(2w-3)\big)=54\Rightarrow3w-3=27\Rightarrow w=10$. Length $17$. Area $=10\cdot17=170$.",
    ans="170",
    fig=fig(r"""\draw[very thick,NAVY,fill=BLUE!8] (0,0) rectangle (10,4);
\node[below] at (5,0) {$(2w-3)$ m};\node[left] at (0,2) {$w$ m};
\node at (5,2) {\small garden};""", xu=0.5, yu=0.5))

# ---------------- HARD ----------------
add('H', r"The equation $(a^2-9)x=a+3$ has a real constant $a$. For how many real values of $a$ does the equation \emph{not} have exactly one solution?",
    r"Exactly one solution needs the $x$-coefficient $\ne0$. Test each value that makes it $0$.",
    r"$a^2-9=0\Rightarrow a=\pm3$. $a=3$: $0=6$, no solution. $a=-3$: $0=0$, infinitely many. Other $a$: exactly one. So $2$ values.",
    opts=[r"$0$", r"$1$", r"$2$", r"$3$"], correct=2)
add('H', r"If $\dfrac{a+b}{a-b}=3$ and $b\neq0$, what is the value of $\dfrac ab$?",
    r"Clear the denominator, then divide by $b$.",
    r"$a+b=3a-3b\Rightarrow4b=2a\Rightarrow\frac ab=2$.",
    opts=[r"$1$", r"$\dfrac32$", r"$2$", r"$3$"], correct=2)
add('H', r"The sum of four consecutive odd integers is $18$ more than twice the largest of the four. What is the product of the two middle integers?",
    r"Let the integers be $n,\,n+2,\,n+4,\,n+6$.",
    r"$4n+12=2(n+6)+18\Rightarrow2n=18\Rightarrow n=9$: $9,11,13,15$ (sum $48=30+18$). Middle product $11\cdot13=143$.",
    ans="143")
add('H', r"What is the solution to $\dfrac{2x-1}{3}-\dfrac{x+2}{4}=\dfrac x6-\dfrac12$?",
    r"LCD is $12$; multiply every term, including $\frac12$.",
    r"$4(2x-1)-3(x+2)=2x-6\Rightarrow8x-4-3x-6=2x-6\Rightarrow5x-10=2x-6\Rightarrow x=\frac43$.",
    ans=r"\tfrac{4}{3}")
add('H', r"The graph shows the solution set of a compound inequality on the number line. Which of the following has this solution set?",
    r"Find each piece's solution set; \emph{or} means union.",
    r"(D): $x\le-2$ or $x>1$. (A) covers all reals ($x\ge-2$ or $x<1$). (B) is empty ($x\le-2$ \emph{and} $x>1$). (C) has open/closed endpoints swapped ($x<-2$ or $x\ge1$).",
    opts=[r"$3x+1\ge-5$ \ \textbf{or}\ \ $x-4<-3$", r"$3x+1\le-5$ \ \textbf{and}\ \ $x-4>-3$", r"$3x+1<-5$ \ \textbf{or}\ \ $x-4\ge-3$", r"$3x+1\le-5$ \ \textbf{or}\ \ $x-4>-3$"], correct=3,
    fig=fig(r"""\draw[<->,thick,INK] (-5.6,0)--(4.6,0);
\foreach \x in {-5,...,4}{\draw (\x,0.1)--(\x,-0.1) node[below,font=\scriptsize]{$\x$};}
\draw[line width=2.4pt,BLUE,-{Latex[length=2.6mm]}] (-2,0)--(-5.5,0);
\draw[line width=2.4pt,BLUE,-{Latex[length=2.6mm]}] (1,0)--(4.5,0);
\filldraw[fill=BLUE,draw=BLUE] (-2,0) circle (0.13);\filldraw[fill=white,draw=BLUE,thick] (1,0) circle (0.13);""", xu=0.9, yu=0.9))
add('H', r"The solution to $\dfrac{x+k}{4}=3$ is equal to $2k$. What is the value of the constant $k$?",
    r"Solve for $x$ in terms of $k$, then set it equal to $2k$.",
    r"$x+k=12\Rightarrow x=12-k$. Set $12-k=2k\Rightarrow k=4$.",
    ans="4")

# ---------------- CHALLENGE ----------------
add('C', r"For each integer $k\neq1$, the equation $(k+1)x+3=2x+k$ has exactly one solution $x$. What is the sum of all integer values of $k$ for which $x$ is also an integer?",
    r"Solve for $x$ as a fraction in $k$, split off a whole number, then use divisibility. Check $k=1$ separately.",
    r"$(k-1)x=k-3\Rightarrow x=\frac{k-3}{k-1}=1-\frac2{k-1}$. Integer iff $(k-1)\mid2$: $k-1\in\{\pm1,\pm2\}\Rightarrow k\in\{2,0,3,-1\}$ ($x=-1,3,0,2$). Sum $=2+0+3-1=4$. ($k=1$ gives $0=-2$, no solution, excluded.)",
    ans="4")
add('C', r"In the triangle shown (not drawn to scale), the side lengths are $x+2$, $3x-2$, and $5x-16$. The triangle is isosceles. What is the sum of all possible perimeters?",
    r"Three pairings. Solve each, then reject any with a non-positive side or a violated triangle inequality.",
    r"$(x+2)=(3x-2)$: $x=2$, sides $4,4,-6$: \textbf{invalid}. $(x+2)=(5x-16)$: $x=4.5$, sides $6.5,11.5,6.5$: valid ($13>11.5$), perimeter $24.5$. $(3x-2)=(5x-16)$: $x=7$, sides $9,19,19$: valid, perimeter $47$. Sum $=71.5$.",
    ans="71.5",
    fig=fig(r"""\draw[very thick,NAVY,fill=BLUE!8] (0,0)--(8,0)--(3,5)--cycle;
\node[below] at (4,0) {$3x-2$};\node[above left] at (1.5,2.5) {$x+2$};\node[above right] at (5.5,2.5) {$5x-16$};""", xu=0.5, yu=0.5))

problems = P
for _p,_t in zip(P,'NNNNNNNDNNNCCNCNDNNCNNNC'): _p['tool']=_t

if __name__ == "__main__":
    build(meta, guided, problems, "W1A.tex")
