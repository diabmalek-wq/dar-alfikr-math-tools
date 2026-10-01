from common import *

meta = dict(
 code="SAT-M \\textperiodcentered\\ W1-B", week="1", session="B",
 title="Lines, Slope \\& Linear Functions",
 topics="slope from points/graphs/tables \\textperiodcentered\\ forms of a line \\textperiodcentered\\ intercepts \\textperiodcentered\\ parallel \\& perpendicular \\textperiodcentered\\ translations \\textperiodcentered\\ meaning of slope/intercept \\textperiodcentered\\ linear function notation",
 skills=r"""
\begin{enumerate}[leftmargin=1.6em,itemsep=0pt,label=\textbf{S\arabic*.}]
\item Find slope from two points, a graph, a table, a standard-form equation, or a verbal rate.
\item Write and convert between slope-intercept, point-slope, standard and intercept forms.
\item Find $x$- and $y$-intercepts and use them (areas, conditions, context meaning).
\item Parallel and perpendicular lines, including directly from $Ax+By=C$.
\item Translate a line (up/down/left/right) and track slope and intercepts.
\item Interpret slope and intercept in context; build $f(x)=mx+b$ from data and solve for inputs.
\item Coordinate reasoning: collinearity, midpoint, perpendicular bisector, triangles cut by axes.
\item Parameter conditions on lines (a constant fixes slope, intercept, perpendicularity or area).
\end{enumerate}""",
 facts=r"""
\begin{itemize}[leftmargin=1.4em,itemsep=0pt]
\item Slope $=\dfrac{\text{rise}}{\text{run}}=$ constant rate of change; the $y$-intercept is the value at $x=0$; the $x$-intercept is where $y=0$.
\item Horizontal line $y=c$: slope $0$. Vertical line $x=c$: slope undefined.
\item Parallel $\iff$ equal slopes (different intercepts). Perpendicular $\iff$ slopes are negative reciprocals (product $-1$).
\item A function is linear if equal steps in $x$ give equal steps in $y$ (check every gap in a table).
\item Shifting a graph up $k$ adds $k$ to $y$; slope never changes under a translation.
\item Two points determine a line; on a graph read only points that sit exactly on grid intersections.
\end{itemize}""",
 formulas=r"""
\vspace{-4pt}\[
m=\dfrac{y_2-y_1}{x_2-x_1},\qquad y=mx+b,\qquad y-y_1=m(x-x_1),\qquad \dfrac xa+\dfrac yb=1
\]
\vspace{-8pt}\[
Ax+By=C:\ \ m=-\dfrac AB,\ \ \text{$x$-int }\dfrac CA,\ \ \text{$y$-int }\dfrac CB,\qquad \text{area with axes}=\dfrac12\left|\dfrac CA\cdot\dfrac CB\right|
\]
\vspace{-8pt}\[
\parallel:\ A_1B_2=A_2B_1,\qquad \perp:\ A_1A_2+B_1B_2=0,\qquad \text{midpoint}=\left(\dfrac{x_1+x_2}2,\dfrac{y_1+y_2}2\right),\qquad f(a+d)-f(a)=md
\]""",
 theory=r"""
\textbf{Choose the form by the data.}
\begin{center}\begin{tabular}{@{}ll@{}}\toprule
Given & Fastest route\\\midrule
two points & $m=\frac{\Delta y}{\Delta x}$, then point-slope with either point\\
slope and $y$-intercept & $y=mx+b$ directly\\
both intercepts $(a,0),(0,b)$ & $\frac xa+\frac yb=1$, or $m=-\frac ba$\\
$Ax+By=C$ & read $m=-\frac AB$; set $x=0$ or $y=0$ for intercepts\\
a table & $m$ from any two rows; confirm the rest have the same $m$\\\bottomrule\end{tabular}\end{center}
\textbf{Perpendicular in standard form.} Swap the coefficients and negate one: $\perp$ to $Ax+By=C$ is $Bx-Ay=C'$; find $C'$ from the given point.
\textbf{Parallel in standard form.} Keep $A,B$ (or scale both), change only $C$.
\textbf{Translation.} Down $k$: $b\to b-k$, and the $x$-intercept moves by $\frac km$. Same slope, always.
\textbf{Meaning.} In $y=mx+b$: $m$ = change in $y$ per $1$ unit of $x$; $b$ = starting value. Units of $m$ are (units of $y$)/(units of $x$).
\textbf{Constant conditions.} Turn the condition (slope, perpendicular, area, collinear) into one equation in the constant, then solve.
\textbf{Whole-number contexts.} Solve $f(x)=\text{target}$; if $x$ must be a whole day/trip/session, round to the first value that \emph{reaches} the target.""",
 strategy=r"""
\textbf{Shortcuts.} (1) Build slope as a fraction; never convert to a decimal until the end. (2) On a graph, use two lattice points far apart. (3) Verify any final equation by plugging both original points. (4) Perpendicular: swap and negate. (5) Intercept triangle: area $=\frac12|a||b|$, no integration of ideas needed.\\
\textbf{Traps.} $\frac{\Delta x}{\Delta y}$ inverted $\cdot$ sign lost in $y_2-y_1$ vs.\ $x_2-x_1$ order mismatch $\cdot$ reading the $y$-value of a point as the intercept $\cdot$ parallel vs.\ perpendicular confusion $\cdot$ ``what does the \emph{slope} mean'' answered with the intercept $\cdot$ forgetting the answer must be a whole day/trip.\\
\textbf{Calculator (Desmos).} Plot points as $(x,y)$, add \texttt{y\textasciitilde mx+b}, drag sliders to match; use a table to test integer inputs; type equations in standard form directly; click an intersection to read exact coordinates.\\
\textbf{Timing.} Easy $\le1.5$ min $\cdot$ Medium $\le3$ $\cdot$ Hard $\le4.5$ $\cdot$ Challenge $\le7$ (total $\approx80$ min).\\
\textbf{Pattern cues.} ``parallel'' $\to$ same $m$ $\cdot$ ``perpendicular'' $\to$ $-\frac1m$ $\cdot$ ``increases by \dots\ for every \dots'' $\to$ $m$ $\cdot$ ``bounded by the axes'' $\to$ intercepts $\cdot$ ``for all $a$: $f(a+d)-f(a)$'' $\to$ slope $\cdot$ ``first day/trip that \dots'' $\to$ round up.""")

guided = r"""
\begin{cbox}[title={Example 1 \textemdash\ Two points $\to$ equation $\to$ intercepts}]{TEAL}
A line passes through $(-1,7)$ and $(3,-1)$. Find its equation and both intercepts.\\[2pt]
$m=\dfrac{-1-7}{3-(-1)}=\dfrac{-8}{4}=-2$. Point-slope: $y-7=-2(x+1)\Rightarrow y=-2x+5$.\\
$y$-intercept $5$; $x$-intercept: $0=-2x+5\Rightarrow x=\frac52$. \emph{Check:} $(3,-1)$: $-6+5=-1$. \checkmark
\end{cbox}
\begin{cbox}[title={Example 2 \textemdash\ Perpendicular through a point (standard form)}]{TEAL}
Line $\ell$: $4x-3y=12$. Write the line through $(2,-1)$ perpendicular to $\ell$.\\[2pt]
Swap and negate: $3x+4y=C'$. Plug in $(2,-1)$: $C'=3(2)+4(-1)=2$. Answer: $3x+4y=2$.\\
\emph{Check:} $A_1A_2+B_1B_2=4\cdot3+(-3)(4)=0$. \checkmark
\end{cbox}
\begin{cbox}[title={Example 3 \textemdash\ Meaning of slope and intercept}]{TEAL}
A gym plan costs $340$ SAR after $2$ months and $640$ SAR after $5$ months (linear). Write $C(m)$ and interpret its parts.\\[2pt]
$\text{slope}=\dfrac{640-340}{5-2}=100$. $C(m)=100m+b$; $340=200+b\Rightarrow b=140$. So $C(m)=100m+140$.\\
$100$ = SAR per month; $140$ = joining fee (cost at $m=0$).
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

# ---- EASY
add('E', r"What is the slope of the line in the $xy$-plane that passes through $(-2,5)$ and $(4,-7)$?",
    r"Subtract in the same order on top and bottom.",
    r"$m=\frac{-7-5}{4-(-2)}=\frac{-12}6=-2$.",
    opts=[r"$-2$", r"$-\tfrac12$", r"$\tfrac12$", r"$2$"], correct=0)
add('E', r"The graph of a line is shown in the $xy$-plane. Which equation represents the line?",
    r"Read the $y$-intercept, then count rise over run to the next lattice point.",
    r"$y$-intercept $2$. From $(0,2)$ to $(2,-1)$: rise $-3$, run $2$, so $m=-\frac32$. $y=-\frac32x+2$. (D) reuses $-1$ as the intercept.",
    opts=[r"$y=\tfrac32x+2$", r"$y=-\tfrac23x+2$", r"$y=-\tfrac32x+2$", r"$y=-\tfrac32x-1$"], correct=2,
    fig=fig(axes(-3,4,-3,5,1,1)+r"""
\draw[ln,<->] (-2.2,5.3)--(3.2,-2.8);
\node[pt] at (0,2){};\node[pt] at (2,-1){};""", xu=0.55, yu=0.55))
add('E', r"What is the $x$-coordinate of the $x$-intercept of the line $5x+2y=30$?",
    r"At an $x$-intercept, $y=0$.",
    r"$5x=30\Rightarrow x=6$.",
    opts=[r"$6$", r"$12$", r"$15$", r"$30$"], correct=0)
add('E', r"A linear function $f$ satisfies $f(3)=7$, and $f(x)$ increases by $5$ for each increase of $1$ in $x$. What is $f(0)$?",
    r"Move from $x=3$ to $x=0$: three steps of $-5$.",
    r"$f(0)=7-3(5)=-8$.",
    ans="-8")
add('E', r"The equation $y=45x+120$ gives the total cost $y$, in Saudi riyals (SAR), of attending $x$ tutoring sessions. Which statement is the best interpretation of $45$?",
    r"Slope = change in cost per one more session.",
    r"$45$ is the slope: each additional session adds $45$ SAR. ($120$ is the registration fee.)",
    opts=[r"The number of sessions attended", r"The registration fee, in SAR", r"The cost, in SAR, of each session", r"The total cost, in SAR, of the first session"], correct=2)
add('E', r"Which equation represents the line that passes through $(1,2)$ and is parallel to $y=3x-5$?",
    r"Same slope; use point-slope with $(1,2)$.",
    r"$m=3$: $y-2=3(x-1)\Rightarrow y=3x-1$. (A) is perpendicular; (C) is the given line itself; (D) reuses $2$ as the intercept.",
    opts=[r"$y=-\tfrac13x+\tfrac73$", r"$y=3x-1$", r"$y=3x-5$", r"$y=3x+2$"], correct=1)

# ---- MEDIUM
add('M', r"In the $xy$-plane, the line $\ell$ is perpendicular to the line $2x+5y=10$ and passes through $(4,3)$. What is the $y$-coordinate of the $y$-intercept of $\ell$?",
    r"Slope of the given line is $-\frac25$; take the negative reciprocal.",
    r"$m_\perp=\frac52$. $y-3=\frac52(x-4)\Rightarrow y=\frac52x-7$. $y$-intercept: $-7$.",
    ans="-7")
add('M', r"The table shows three values of a linear function $f$. What is the value of $p$?\\[3pt]\begin{center}\begin{tabular}{c|ccc}$x$&$2$&$5$&$9$\\\hline $f(x)$&$11$&$20$&$p$\end{tabular}\end{center}",
    r"Get the slope from the two complete columns.",
    r"$m=\frac{20-11}{5-2}=3$. $p=20+3(9-5)=32$.",
    ans="32")
add('M', r"A line has $x$-intercept $-4$ and $y$-intercept $6$. Which of the following points lies on the line?",
    r"Slope $=-\frac{b}{a}$ with $a=-4,\ b=6$; then $y=mx+6$.",
    r"$m=\frac{6-0}{0-(-4)}=\frac32$, $y=\frac32x+6$. At $x=2$: $y=9$. So $(2,9)$.",
    opts=[r"$(2,3)$", r"$(2,6)$", r"$(2,9)$", r"$(2,12)$"], correct=2)
add('M', r"The graph of $y=-2x+7$ in the $xy$-plane is translated down $5$ units. What is the $x$-coordinate of the $x$-intercept of the new graph?",
    r"New equation: subtract $5$ from the right side.",
    r"$y=-2x+2$; set $y=0$: $x=1$.",
    ans="1")
add('M', r"A tank at a desalination plant is being drained. The graph shows the volume $V$ of water, in thousands of liters, $t$ minutes after draining begins. If the volume keeps decreasing at the same rate, after how many minutes will the tank be empty?",
    r"Rate $=\frac{\Delta V}{\Delta t}$ between the two labeled points; then solve $V=0$.",
    r"$m=\frac{54-90}{6-0}=-6$. $V=90-6t=0\Rightarrow t=15$ minutes.",
    ans="15",
    fig=fig(axes(0,9,0,10,1,1,xl='t',yl='V',lab_x=2,lab_y=2,ymult=10)+r"""
\draw[ln,-{Stealth[length=2.2mm]}] (0,9)--(8,4.2);
\node[pt] at (0,9){};\node[pt] at (6,5.4){};
\node[right,font=\small] at (0.15,9.35) {$(0,90)$};\node[above right,font=\small] at (6.05,5.5) {$(6,54)$};""", xu=0.6, yu=0.45))
add('M', r"For the line $kx+3y=12$ in the $xy$-plane, $k$ is a constant. If the slope of the line is $-2$, what is the value of $k$?",
    r"Solve for $y$, or use $m=-\frac AB$.",
    r"$3y=-kx+12\Rightarrow m=-\frac k3=-2\Rightarrow k=6$.",
    opts=[r"$-6$", r"$-2$", r"$2$", r"$6$"], correct=3)
add('M', r"A line in the $xy$-plane passes through $(-1,4)$ and $(3,12)$. What is the $y$-coordinate of the point on the line with $x$-coordinate $10$?",
    r"Slope first; then move $11$ units in $x$ from $x=-1$.",
    r"$m=\frac{12-4}{3+1}=2$. $y=4+2(10-(-1))=26$.",
    ans="26")
add('M', r"In the $xy$-plane, the line $2x+3y=12$ and the coordinate axes bound a triangle. What is the area of the triangle?",
    r"Find both intercepts; they are the legs.",
    r"Intercepts $6$ and $4$. Area $=\frac12(6)(4)=12$.",
    opts=[r"$6$", r"$12$", r"$24$", r"$36$"], correct=1)
add('M', r"The points $(1,2)$, $(4,8)$, and $(k,20)$ lie on the same line in the $xy$-plane. What is the value of $k$?",
    r"Equal slopes between any two pairs.",
    r"$m=\frac{8-2}{4-1}=2$; $\frac{20-2}{k-1}=2\Rightarrow k-1=9\Rightarrow k=10$.",
    ans="10")
add('M', r"The functions $f$ and $g$ are defined by $f(x)=5x+12$ and $g(x)=2x-9$. The function $h$ is defined by $h(x)=f(x)-g(x)$. What is the $x$-coordinate of the $x$-intercept of the graph of $y=h(x)$?",
    r"Simplify $h(x)$ first; its $x$-intercept is where $h(x)=0$.",
    r"$h(x)=3x+21=0\Rightarrow x=-7$.",
    ans="-7")

# ---- HARD
add('H', r"In the $xy$-plane, points $P(-2,1)$ and $Q(6,5)$ are the endpoints of a segment. Which equation represents the perpendicular bisector of $\overline{PQ}$?",
    r"Midpoint first; then the negative reciprocal of the segment's slope.",
    r"Midpoint $(2,3)$; slope of $PQ=\frac{4}{8}=\frac12$; perpendicular slope $-2$. $y=-2x+7$. (A) is line $PQ$; (B) drops the reciprocal; (C) drops the negative.",
    opts=[r"$y=\tfrac12x+2$", r"$y=-\tfrac12x+4$", r"$y=2x-1$", r"$y=-2x+7$"], correct=3)
add('H', r"In the $xy$-plane, line $\ell$ is shown. Line $m$ is perpendicular to $\ell$ and passes through the $y$-intercept of $\ell$. What is the area of the triangle bounded by $\ell$, $m$, and the $x$-axis?",
    r"Read the two labeled points; get $\ell$, then $m$; the $x$-axis chord is the base.",
    r"$\ell$: $m=\frac{6-0}{4+4}=\frac34$, $y=\frac34x+3$. $m\perp\ell$ through $(0,3)$: $y=-\frac43x+3$, $x$-intercept $\frac94$. Vertices $(-4,0),(\frac94,0),(0,3)$: base $\frac{25}4$, height $3$; area $=\frac12\cdot\frac{25}4\cdot3=\frac{75}8=9.375$.",
    ans=r"\tfrac{75}{8}",
    fig=fig(axes(-6,6,-3,8,1,1,lab_x=2,lab_y=2)+r"""
\draw[ln,<->] (-5.6,-1.2)--(5.2,6.9);
\node[pt] at (-4,0){};\node[pt] at (4,6){};
\node[above left,font=\small] at (-4,0.05){$(-4,0)$};\node[below right,font=\small] at (4,5.95){$(4,6)$};
\node[BLUE,font=\small] at (-3.6,-1.4){$\ell$};""", xu=0.5, yu=0.45))
add('H', r"A line in the $xy$-plane passes through $(2,3)$. Its $x$-intercept is twice its $y$-intercept, and neither intercept is $0$. What is the $x$-intercept of the line?",
    r"If the $y$-intercept is $b$, the $x$-intercept is $2b$; use $\frac{x}{2b}+\frac yb=1$.",
    r"$\frac{2}{2b}+\frac3b=1\Rightarrow\frac4b=1\Rightarrow b=4$. $x$-intercept $=8$. ($y=-\frac12x+4$ passes through $(2,3)$.)",
    ans="8")
add('H', r"For a linear function $f$, $f(a+2)-f(a)=6$ for every real number $a$, and $f(0)=-1$. What is $f(5)$?",
    r"The difference over an $x$-step of $2$ is $2m$.",
    r"$2m=6\Rightarrow m=3$, $f(x)=3x-1$, $f(5)=14$. (Not $29$: that uses $m=6$.)",
    opts=[r"$11$", r"$14$", r"$29$", r"$30$"], correct=1)
add('H', r"Nora's savings grow linearly. On day $3$ she has $250$ SAR and on day $9$ she has $490$ SAR. On what is the first day on which she has at least $1000$ SAR?",
    r"Model $f(d)$, solve $f(d)\ge1000$, then choose the first whole day.",
    r"$m=\frac{490-250}{9-3}=40$; $f(d)=40d+130$. $40d+130\ge1000\Rightarrow d\ge21.75$. First whole day: $22$.",
    ans="22")
add('H', r"In the $xy$-plane, the lines $(k+1)x+6y=5$ and $2x+ky=9$ are perpendicular. What is the value of $k$?",
    r"For $A_1x+B_1y=C_1$ and $A_2x+B_2y=C_2$, perpendicular means $A_1A_2+B_1B_2=0$.",
    r"$2(k+1)+6k=0\Rightarrow8k=-2\Rightarrow k=-\frac14$. (Check by slopes: $-\frac{k+1}{6}\cdot\left(-\frac2k\right)=\frac{k+1}{3k}=-1$.)",
    ans=r"-\tfrac{1}{4}")

# ---- CHALLENGE
add('C', r"In the $xy$-plane, a line with negative slope passes through the point $P(4,3)$ shown. Together with the positive $x$- and $y$-axes it forms a right triangle of area $24$. What is the slope of the line?",
    r"With intercepts $a,b$: $ab=48$ and $\frac4a+\frac3b=1$. Eliminate one unknown.",
    r"$\frac4a+\frac3b=1\Rightarrow4b+3a=ab=48$. With $b=\frac{48}a$: $\frac{192}a+3a=48\Rightarrow3a^2-48a+192=0\Rightarrow(a-8)^2=0$, so $a=8$, $b=6$. Slope $=-\frac ba=-\frac34$. (The double root shows $24$ is the \emph{smallest} possible area for a line through $P$.)",
    ans=r"-\tfrac{3}{4}",
    fig=fig(axes(0,10,0,8,1,1)+r"""
\node[pt] at (4,3){};\node[above right,font=\small] at (4.05,3.05){$P(4,3)$};""", xu=0.5, yu=0.45))
add('C', r"The linear function $f(x)=ax+b$ satisfies $f(f(x))=9x+8$ for all real $x$. What is the greatest possible value of $f(1)$?",
    r"Expand $f(f(x))$ and match coefficients: two equations, two cases for $a$.",
    r"$f(f(x))=a^2x+ab+b$. So $a^2=9$ and $b(a+1)=8$. $a=3\Rightarrow b=2$, $f(1)=5$. $a=-3\Rightarrow b=-4$, $f(1)=-7$. Greatest: $5$.",
    ans="5")

problems = P
for _p,_t in zip(P,'NDNNNNDNNDCNNNNNDDDNCDDN'): _p['tool']=_t
if __name__ == "__main__":
    build(meta, guided, problems, "W1B.tex")
