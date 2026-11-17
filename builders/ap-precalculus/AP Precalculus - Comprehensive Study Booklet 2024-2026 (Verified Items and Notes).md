[Math Department Logo] | Mr. Malek Thiab | [Dar Alfikr School Logo]

# AP Precalculus — Comprehensive Study Booklet 2024–2026: Verified Notes and Item Bank

**Added:** 17 Nov 2026. **Source:** "AP Precalculus Comprehensive Study Booklet (2024–2026)" (10 pp, teacher-supplied): 8 student-recalled hard MCQs (May 2024–2026), 12 free-response questions (FRQ 1–4 for 2024, 2025, 2026), a trap taxonomy and a scoring-rubric checklist.
**Status of the source:** the booklet is a third-party compilation. Its figures and exact wording are not College Board documents, so the items below are **booklet-reported**, restated in plain wording, and every answer was **recomputed by script**. Where the booklet was wrong or garbled the corrected version is used and logged in section 1.
**House rules kept:** English only, no Saudi context (AP), LaTeX for all maths, VANG language where it fits the AP Precalc guided-notes book, each item states its calculator tool.

## 1. Verification log (what the booklet got wrong)

| Where | Booklet says | Verified | Action |
|---|---|---|---|
| MCQ 1 | roots $x\approx\pm3.011$ | $x^4-9x^2=1\Rightarrow x^2=\frac{9+\sqrt{85}}{2}$, so $x\approx\pm3.018$ | corrected; distractor $3.104$ (from $x^2(x-3)=1$) confirmed |
| MCQ 2 | stem says $f$ "is concave up" and then asks which interval "guarantees" it | with the premise given, only $k<4$ is forced; $1<k<3$ is not forced (k = 3.5 also works) | stem rewritten (item M2) |
| MCQ 8 | option (C) $\lim_{x\to2}r(x)=\frac37$ | after cancelling one factor the value would be $\frac{7}{3}$, and the two-sided limit does not exist | option rewritten as the "cancel once and substitute" trap $\frac73$ |
| 2026 FRQ 2 | $V(t)=2$ at $t\approx22.463$ | $t=\dfrac{\ln(2/a)}{\ln b}\approx22.44$ | corrected |
| 2026 FRQ 3 | rubric text contradicts itself ("Wait—tracking…") and labels J both as midline and as the minimum | five quarter-points from the first maximum: F max, G midline (falling), J min, K midline (rising), P max | restated with the interval minimum → rising midline |
| 2025 FRQ 1 | $g(x)=-x^3+0.167x^2-1.834$ gives $h(1)=0.333$ | that form gives $-6.68$; the form $-0.167x^3+x^2-1.834$ gives $0.3335$ and zeros $-1.233,\ 1.578,\ 5.643$ | second form used |
| 2025 FRQ 4(B)(ii) | expression garbled | $\tan x\,(\csc^2x-1)=\tan x\cot^2x=\cot x=\dfrac1{\tan x}$ | restated |
| 2024 FRQ 3(C) | "rate of change is decreasing (concave down)" between $K$ and $P$ | $h''=-9\pi^2\sin(\pi(t-1))>0$ there: **concave up, rate of change increasing** | corrected |
| 2024 FRQ 4(B)(i) | "$\log_{10}(16x^2)$" | $\log_{10}\!\dfrac{16}{x^{2}}$ (the exponent is $-2$) | corrected |
| Exam format (Part I) | 42 MCQ (29 + 13), FRQ 35 + 35 min from May 2027 | **confirmed** on the College Board AP Central exam page and CED clarification | kept |

## 2. Notes

### 2.1 Exam architecture (confirmed on AP Central)
Section I, multiple choice: **42 questions, 105 minutes, 62.5%** of the score. Part A has 29 questions, 65 minutes, no calculator (43.75%). Part B has 13 questions, 40 minutes, graphing calculator required (18.75%).
Section II, free response: **4 questions, 70 minutes, 37.5%**. Part A has 2 questions, 35 minutes, graphing calculator (FRQ 1 Function Concepts, FRQ 2 Modeling a Non-Periodic Context). Part B has 2 questions, 35 minutes, no calculator (FRQ 3 Modeling a Periodic Context, FRQ 4 Symbolic Manipulations).
These numbers apply from the **May 2027** exam (the exam is Tue 11 May 2027, Session 1). The CED clarification says course content has not changed, and that FRQ 2 lost its part B(iii) (the secant-line explanation) with part C expanded. Treat the secant-versus-curve explanation below as strong practice, but not as a guaranteed FRQ 2 part in 2027.

### 2.2 The four FRQ slots and what they always ask
| FRQ | Slot | Recurring parts |
|---|---|---|
| 1 | Function concepts (calc) | composition $h=g\circ f$ from a graph and a formula; solve $g(x)=c$ numerically; a one-sided or end-behaviour limit; invertibility of $f$ with a reason |
| 2 | Non-periodic model (calc) | write equations for the parameters from two or three data points; average rate of change; secant-line estimate; concavity explanation; domain limit from context |
| 3 | Periodic model (no calc) | five quarter-period points from the first maximum; write $h(t)=a\sin(b(t+c))+d$; sign, concavity and rate of change on an interval |
| 4 | Symbolic (no calc) | solve exponential and logarithmic equations exactly; rewrite with one base or one trig function; solve a trig equation on an interval or in general |

### 2.3 Author-trap taxonomy (from the booklet, checked)
1. **Hidden symmetry:** an even polynomial with a stated zero at $3$ also has a zero at $-3$; typing only the given factors into the calculator gives the wrong root.
2. **Concavity from a table:** equal input steps, so concave up $\Leftrightarrow$ average rates of change increase; compare the two slopes, do not eyeball "between the neighbours".
3. **Polar quadrant:** $\arctan\frac{b}{a}$ does not choose the quadrant; plot $(a,b)$ first.
4. **Hidden quadratic:** $e^{2x}-e^x-12=0$ is $u^2-u-12=0$ with $u=e^x>0$, so the root $u=-3$ is rejected and the sum of real solutions is $\ln4$, not Vieta's $1$.
5. **Polar distance:** the distance from the pole is $|r|$, not $r$; when $r<0$ and decreasing, $|r|$ increases.
6. **Reflection reverses both monotonicity and concavity:** $-\frac12\ln(x-3)$ is decreasing and concave up.
7. **Reciprocal functions:** $\sec$ has a vertical asymptote wherever $\cos$ is zero, so count zeros of $\cos(bx)$ on the interval.
8. **Hole versus asymptote:** cancel one factor, then check what remains in the denominator.

### 2.4 Scoring-rubric checklist (booklet, with the one correction noted)
| Component | Mandatory phrasing or requirement |
|---|---|
| Secant versus curve | State the concavity first: a secant line lies **above** a concave-up curve and **below** a concave-down curve. |
| Function-type proof | Never cite regression $r^2$. Compare equal input steps: constant first differences mean linear, constant second differences mean quadratic, constant output ratios mean exponential. |
| Asymptote limits | Use a one-sided limit when a log or rational function exists on one side of the vertical asymptote (for example $\lim_{x\to1^+}$). A two-sided limit forfeits the point. |
| Sinusoidal parameters | $a=\dfrac{\max-\min}{2}$, $d=\dfrac{\max+\min}{2}$, $b=\dfrac{2\pi}{\text{period}}$, and $c$ chosen so that $t=-c$ is a rising midline crossing. |
| Exact symbolic form | Radians only, $\pm$ roots for even roots, general solutions $+\pi k$ (tan, cot) or $+2\pi k$ (sin, cos) when no interval is given, no negative exponents inside a logarithm. |
| Decimals | Three decimal places, truncated or rounded, unless the question says otherwise. |

### 2.5 Link to the guided-notes book (standing rule, 3 Nov 2026)
M1 and M8 belong with Topics 1.5 and 1.9–1.10; M2 with 1.2–1.3; M3 with 3.13; M4 and M6 with 2.4, 2.11–2.12; M5 with 3.15; M7 with 3.11. FRQ 1 maps to 1.14, 2.6 and 2.9; FRQ 2 to 1.13–1.14 and 2.6; FRQ 3 to 3.4–3.5; FRQ 4 to 2.4, 2.12, 3.9–3.11.

## 3. Multiple-choice items (booklet-reported, corrected)

### AP-BK-M1 — Even polynomial, reconstruct the factor
**Topic:** 1.5 and 1.6 · **Section I Part B (graphing calculator)** · Hard
**Question:** The even polynomial $p$ has degree $4$ and leading coefficient $1$, and $x^{2}(x-3)$ is a factor of $p(x)$. Which of the following gives all real solutions to $p(x)=1$?
(A) $x\approx3.104$ only
(B) $x\approx-3.018$ and $x\approx3.018$
(C) $x\approx-3.104$ and $x\approx3.104$
(D) $x\approx-3.018,\ x=0$ and $x\approx3.018$
**Key:** (B)
**Solution:** $p$ is even and has a zero at $3$, so it also has a zero at $-3$: $p(x)=x^{2}(x-3)(x+3)=x^{4}-9x^{2}$. Solving $x^{4}-9x^{2}=1$ gives $x^{2}=\frac{9+\sqrt{85}}{2}$, so $x\approx\pm3.018$ (the other value of $x^2$ is negative). At $x=0$, $p(0)=0\ne1$.
**Trap:** solving $x^{2}(x-3)=1$ gives only $x\approx3.104$ (A) because the symmetric factor was never restored.

### AP-BK-M2 — Concave up from a table (restated)
**Topic:** 1.2, 1.3 · **Part B (calculator)** · Hard
**Question:** The function $f$ is continuous and concave up on $[1,5]$, with $f(1)=2$, $f(3)=k$ and $f(5)=6$. Which of the following must be true about $k$?
(A) $k<4$
(B) $k>4$
(C) $4<k<6$
(D) $k<2$
**Key:** (A)
**Solution:** Over equal steps $\Delta x=2$, concave up means the average rate of change increases: $\dfrac{k-2}{2}<\dfrac{6-k}{2}\Rightarrow 2k<8\Rightarrow k<4$. Values such as $k=3.5$ are allowed, so (D) is not forced, and (B), (C) are impossible.
**Trap:** assuming "increasing and concave up" puts $k$ between $2$ and $6$ without testing the midpoint value $4$.

### AP-BK-M3 — Complex number to polar form
**Topic:** 3.13 · **Part A (no calculator)** · Medium
**Question:** Which of the following is $z=-4+4i$ in the form $r(\cos\theta+i\sin\theta)$ with $r>0$ and $0\le\theta<2\pi$?
(A) $4\sqrt2\left(\cos\frac{\pi}{4}+i\sin\frac{\pi}{4}\right)$
(B) $4\sqrt2\left(\cos\frac{3\pi}{4}+i\sin\frac{3\pi}{4}\right)$
(C) $4\sqrt2\left(\cos\frac{7\pi}{4}+i\sin\frac{7\pi}{4}\right)$
(D) $8\left(\cos\frac{3\pi}{4}+i\sin\frac{3\pi}{4}\right)$
**Key:** (B)
**Solution:** The point $(-4,4)$ is in Quadrant II. $r=\sqrt{16+16}=4\sqrt2$, reference angle $\frac{\pi}{4}$, so $\theta=\pi-\frac{\pi}{4}=\frac{3\pi}{4}$.
**Trap:** $\arctan\frac{4}{-4}=-\frac{\pi}{4}$, adding $2\pi$ gives $\frac{7\pi}{4}$ in Quadrant IV (C); (D) forgets that $r=\sqrt{32}$.

### AP-BK-M4 — Hidden quadratic in $e^x$
**Topic:** 2.4, 2.12 · **Part A (no calculator)** · Hard
**Question:** What is the sum of all real solutions of $e^{2x}-e^{x}-12=0$?
(A) $\ln4$ (B) $\ln12$ (C) $\ln4+\ln3$ (D) $1$
**Key:** (A)
**Solution:** $(e^{x}-4)(e^{x}+3)=0$. Since $e^{x}>0$, only $e^{x}=4$ works, so $x=\ln4$ and the sum is $\ln4$.
**Trap:** Vieta on $u^2-u-12=0$ gives $1$ (D); keeping $e^x=-3$ leads to (C).

### AP-BK-M5 — Polar distance and rate of change
**Topic:** 3.15 · **Part B (calculator)** · Hard
**Question:** For the polar function $r=f(\theta)=1+2\cos\theta$ on $\frac{2\pi}{3}<\theta<\pi$, how is the distance between the point $(f(\theta),\theta)$ and the origin changing?
(A) Decreasing, because $f(\theta)<0$ and $f$ is decreasing.
(B) Increasing, because $f(\theta)<0$ and $f$ is decreasing.
(C) Decreasing, because $f(\theta)>0$ and $f$ is decreasing.
(D) Increasing, because $f(\theta)>0$ and $f$ is increasing.
**Key:** (B)
**Solution:** $f\!\left(\frac{2\pi}{3}\right)=1+2\left(-\frac12\right)=0$ and $f(\pi)=-1$, so $f<0$ and $f$ is decreasing. The distance from the pole is $|f(\theta)|$, which rises from $0$ to $1$.
**Trap:** "$f$ decreasing means the point moves closer to the pole."

### AP-BK-M6 — Reflected logarithm: monotonicity and concavity
**Topic:** 2.11, 2.12 · **Part A (no calculator)** · Medium
**Question:** Which describes $g(x)=-\frac12\ln(x-3)$ on $(3,\infty)$?
(A) Decreasing and concave down (B) Decreasing and concave up (C) Increasing and concave down (D) Increasing and concave up
**Key:** (B)
**Solution:** $y=\ln(x-3)$ is increasing and concave down. Multiplying by $-\frac12$ reflects it across the $x$-axis, reversing both, so $g$ is decreasing and concave up.

### AP-BK-M7 — Vertical asymptotes of a secant
**Topic:** 3.11 · **Part A (no calculator)** · Medium
**Question:** How many vertical asymptotes does $y=3\sec(2x)$ have on $(0,2\pi)$?
(A) $2$ (B) $3$ (C) $4$ (D) $5$
**Key:** (C)
**Solution:** Asymptotes occur where $\cos(2x)=0$, with $0<2x<4\pi$: $2x=\frac{\pi}{2},\frac{3\pi}{2},\frac{5\pi}{2},\frac{7\pi}{2}$, so $x=\frac{\pi}{4},\frac{3\pi}{4},\frac{5\pi}{4},\frac{7\pi}{4}$.
**Trap:** forgetting that $2x$ runs over two periods of $\cos$ (answer $2$).

### AP-BK-M8 — Hole versus vertical asymptote
**Topic:** 1.9, 1.10 · **Part A (no calculator)** · Medium
**Question:** Let $r(x)=\dfrac{(x-2)(x+5)}{(x-2)^{2}(x+1)}$. Which statement about $r$ near $x=2$ is correct?
(A) $r$ has a hole at $x=2$ because $(x-2)$ is a factor of both numerator and denominator.
(B) $r$ has a vertical asymptote at $x=2$ because $(x-2)$ has greater multiplicity in the denominator than in the numerator.
(C) $\lim_{x\to2}r(x)=\dfrac73$.
(D) $r$ has a horizontal asymptote at $y=2$.
**Key:** (B)
**Solution:** For $x\ne2$, $r(x)=\dfrac{x+5}{(x-2)(x+1)}$. A factor $(x-2)$ remains in the denominator, so $x=2$ is a vertical asymptote ($r\to-\infty$ from the left, $+\infty$ from the right). The horizontal asymptote is $y=0$.
**Trap:** cancelling one factor and substituting $x=2$ in what is left, $\frac{7}{3}$ (C).

## 4. Free-response items (booklet-reported, corrected and verified)

Each part is answered and checked. "Calc" means graphing calculator. Where the booklet gave no figure, only the data it states are used.

### AP-BK-F1 — 2026 FRQ 1 (calc): composition, logarithm, invertibility · 6 points
**Setup:** $f$ is increasing on $-3\le x\le3$ and passes through $(-3,-2),(-2,0),(0,2),(1,3),(2,5),(3,9)$. $g(x)=-4.792+\ln(6x-6)$.
(A)(i) Find $h(2)$ where $h=g\circ f$. (ii) Find all $x$ with $f(x)=3$.
(B)(i) Find all $x$ with $g(x)=-1.5$. (ii) Describe the behaviour of $g$ as $x$ decreases toward $1$, in limit notation.
(C)(i) Is $f$ invertible? (ii) Give a reason.
**Solution:** (A)(i) $h(2)=g(5)=-4.792+\ln24\approx-1.614$. (ii) $x=1$. (B)(i) $\ln(6x-6)=3.292\Rightarrow x\approx5.483$. (ii) $\lim_{x\to1^{+}}g(x)=-\infty$ (one-sided only; $g$ exists only for $x>1$). (C) Yes: $f$ is strictly increasing, so no two inputs share an output.

### AP-BK-F2 — 2026 FRQ 2 (calc): exponential depreciation · 6 points
**Setup:** $V(t)=ab^{t}$; $V(1)=27.2$ and $V(6)=14.8$ (thousand dollars, $t$ in years after end of 2019).
(A)(i) Write two equations for $a$ and $b$. (ii) Find $a$ and $b$. (B)(i) Average rate of change from $t=1$ to $t=6$. (ii) Estimate $V(3)$ with it. (iii) Explain why this secant estimate exceeds $V(t)$ on $1<t<6$. (C) The car is donated when $V=2$; explain the domain limit.
**Solution:** (A) $ab=27.2$, $ab^{6}=14.8$; $b=(14.8/27.2)^{1/5}\approx0.885$, $a\approx30.721$. (B)(i) $\dfrac{14.8-27.2}{5}=-2.48$ thousand dollars per year. (ii) $27.2-2.48(2)=22.24$. (iii) $V$ is exponential decay, concave up, so the secant lies above the curve. (C) $V(t)=2\Rightarrow t\approx22.44$ (booklet said $22.463$), so the model applies for $0\le t\le22.44$.

### AP-BK-F3 — 2026 FRQ 3 (no calc): waterwheel · 6 points
**Setup:** A wheel turns counterclockwise, one revolution per $10$ seconds. At $t=0$ point $W$ is $6$ ft directly above the centre; $h(t)$ is its height above the horizontal line through the centre.
(A) Give $(t,h(t))$ for the five consecutive quarter-period points $F,G,J,K,P$ starting at the first maximum. (B) Write $h(t)=a\sin(b(t+c))+d$. (C) On the interval from $J$ (minimum) to $K$ (rising midline), is $h$ positive or negative, increasing or decreasing, concave up or down, and is its rate of change increasing or decreasing?
**Solution:** (A) $F(0,6),\ G(2.5,0),\ J(5,-6),\ K(7.5,0),\ P(10,6)$. (B) $a=6$, $b=\frac{2\pi}{10}=\frac{\pi}{5}$, $d=0$, $c=\frac52$: $h(t)=6\sin\!\left(\frac{\pi}{5}\left(t+\frac52\right)\right)$. (C) negative, increasing, concave up, and the rate of change is increasing ($h=6\cos\frac{\pi t}{5}$, $h''>0$ here).

### AP-BK-F4 — 2026 FRQ 4 (no calc): exact solving and identities · 6 points
(A)(i) Solve $e^{2x}=e^{-6}$. (ii) Solve $\log_2(5x)=3$. (B)(i) Write $j(x)=7^{x}\cdot7^{3x+1}$ as $7^{\text{expression}}$. (ii) Write $k(x)=\sin(2x)\sec x$ with $\sin x$ appearing once and no other trig function. (C) Find all $x$ in $\left[0,\frac{\pi}{2}\right]$ with $\tan(3x)=1$.
**Solution:** (A)(i) $x=-3$. (ii) $5x=8$, $x=\frac85$. (B)(i) $7^{4x+1}$. (ii) $2\sin x\cos x\cdot\frac{1}{\cos x}=2\sin x$. (C) $0\le3x\le\frac{3\pi}{2}$, so $3x=\frac{\pi}{4}$ or $\frac{5\pi}{4}$, giving $x=\frac{\pi}{12}$ and $\frac{5\pi}{12}$.
**Note:** the exponent in (A)(i) is printed unclearly in the booklet; the rubric answer $x=-3$ requires $e^{-6}$.

### AP-BK-F5 — 2025 FRQ 1 (calc): table, composition, cubic · 6 points
**Setup:** $f$ is decreasing with $(-2,14),(-1,7),(0,3.5),(1,1.75),(2,0.875)$. $g(x)=-0.167x^{3}+x^{2}-1.834$.
(A)(i) Find $h(1)=g(f(1))$. (ii) Find $f^{-1}(3.5)$. (B)(i) Find all real zeros of $g$. (ii) Find $\lim_{x\to\infty}g(x)$. (C) Which model type (linear, quadratic, exponential, logarithmic) fits $f$? Justify with the table.
**Solution:** (A)(i) $g(1.75)\approx0.333$. (ii) $f(0)=3.5$, so $f^{-1}(3.5)=0$. (B)(i) $x\approx-1.233,\ 1.578,\ 5.643$. (ii) $-\infty$. (C) Exponential: for equal input steps of $1$ the outputs have a constant ratio $0.5$.

### AP-BK-F6 — 2025 FRQ 2 (calc): quadratic streams model · 6 points
**Setup:** $D(t)=at^{2}+bt+c$ thousand plays; $D(0)=25$, $D(2)=30$, $D(4)=34$.
(A) Write three equations, then find $a,b,c$. (B)(i) Average rate of change on $[0,4]$. (ii) Estimate $D(1.5)$ with it. (iii) Explain why the secant estimate is below $D(t)$ on $0<t<4$. (C) Explain how the maximum of $D$ limits the domain.
**Solution:** (A) $c=25$, $4a+2b+c=30$, $16a+4b+c=34$, so $a=-0.125$, $b=2.75$, $c=25$. (B)(i) $\frac{34-25}{4}=2.25$. (ii) $25+2.25(1.5)=28.375$. (iii) $a<0$, concave down, secant below the curve. (C) Total plays cannot decrease; the vertex is at $t=-\frac{b}{2a}=11$, so the model is valid for $0\le t\le11$.

### AP-BK-F7 — 2025 FRQ 3 (no calc): vibrating string · 6 points
**Setup:** Point $X$ starts at its highest position, $2$ mm above rest, moves to $-2$ mm and back, repeating $200$ times per second.
(A) The five quarter-period points from the first maximum. (B) $h(t)=a\sin(b(t+c))+d$. (C) Between the midline crossing $G$ and the minimum $J$, describe sign, monotonicity, concavity and rate of change.
**Solution:** Period $\frac{1}{200}$ s, quarter-period $\frac{1}{800}$ s. (A) $F(0,2),\ G\!\left(\frac1{800},0\right),\ J\!\left(\frac1{400},-2\right),\ K\!\left(\frac3{800},0\right),\ P\!\left(\frac1{200},2\right)$. (B) $a=2$, $b=400\pi$, $c=\frac1{800}$, $d=0$. (C) $h$ is negative and decreasing, concave up, and its rate of change is increasing.

### AP-BK-F8 — 2025 FRQ 4 (no calc): logs, identities, exponential zeros · 6 points
(A)(i) Solve $2\log_3x=4$. (ii) Solve $4\cos^{2}x=3$ on $\left[0,\frac{\pi}{2}\right)$. (B)(i) Write $\log_2x+3\log_2 2$ as one base-2 logarithm. (ii) Write $k(x)=\tan x\,(\csc^{2}x-1)$ using $\tan x$ once. (C) Find all zeros of $m(x)=e^{2x}-e^{x}-12$.
**Solution:** (A)(i) $x=9$. (ii) $\cos x=\frac{\sqrt3}{2}$, $x=\frac{\pi}{6}$. (B)(i) $\log_2(8x)$. (ii) $\tan x\cot^{2}x=\cot x=\dfrac{1}{\tan x}$. (C) $(e^{x}-4)(e^{x}+3)=0$, $x=\ln4$ only.

### AP-BK-F9 — 2024 FRQ 1 (calc): non-invertible graph, exponential decay · 6 points
**Setup:** $f$ on $[-3.5,3.5]$ passes through $(-3,-1),(0,1),(3,1)$. $g(x)=2.916(0.7)^{x}$.
(A)(i) $h(3)=g(f(3))$. (ii) All $x$ with $f(x)=1$. (B)(i) Solve $g(x)=2$. (ii) $\lim_{x\to\infty}g(x)$. (C) Does $f$ have an inverse? Justify.
**Solution:** (A)(i) $g(1)=2.041$. (ii) $x=0$ and $x=3$ (from the listed points). (B)(i) $x=\dfrac{\ln(2/2.916)}{\ln0.7}\approx1.057$. (ii) $0$. (C) No: the output $1$ comes from two inputs, $f(0)=f(3)=1$, so the inverse relation would give one input two outputs.

### AP-BK-F10 — 2024 FRQ 2 (calc): logarithmic sales model · 6 points
**Setup:** $G(t)=a+b\ln(t+1)$ thousand per day, $G(0)=40$, $G(91)=76$.
(A) Find $a$ and $b$. (B) Average rate of change on $[0,91]$; use it for a linear estimate of $G(50)$; explain whether it is an under- or overestimate. (C) Explain what happens to the model error after $t=91$ if actual sales decline.
**Solution:** (A) $a=40$, $b=\dfrac{36}{\ln92}\approx7.961$. (B) $\frac{36}{91}\approx0.396$; estimate $40+\frac{36}{91}(50)\approx59.780$; $G$ is concave down, so the secant lies below and the estimate is an **underestimate**. (C) $G$ keeps increasing while actual sales fall, so the difference grows.

### AP-BK-F11 — 2024 FRQ 3 (no calc): rolling tire · 6 points
**Setup:** A tire of radius $9$ in. rolls at a constant rate. Point $W$ is on the ground at $t=\frac12$ s and again at $t=\frac52$ s; its maximum height is $18$ in.
(A) The five quarter-period points from the first ground contact. (B) $h(t)=a\sin(b(t+c))+d$. (C) Between $K$ (midline, falling) and $P$ (next ground contact), describe $h$.
**Solution:** Period $2$ s, quarter-period $\frac12$ s. (A) $F\!\left(\frac12,0\right),\ G(1,9),\ J\!\left(\frac32,18\right),\ K(2,9),\ P\!\left(\frac52,0\right)$. (B) $h(t)=9\sin(\pi(t-1))+9$ ($a=9$, $b=\pi$, $c=-1$, $d=9$). (C) $h$ is positive and decreasing, **concave up**, and its rate of change is **increasing** (the booklet's "concave down" is wrong).

### AP-BK-F12 — 2024 FRQ 4 (no calc): inverse trig and log rules · 6 points
(A)(i) Solve $e^{x+3}=10$. (ii) Solve $\arcsin(2x)=\frac{\pi}{4}$. (B)(i) Write $\log_{10}(8x^{5})+\log_{10}(2x^{2})-9\log_{10}x$ as one logarithm without negative exponents. (ii) Write $k(x)=\dfrac{1-\sin^{2}x}{\sin x}\sec x$ as one term in $\tan x$. (C) For $m(x)=\cos^{-1}(\tan(2x))$ find all $x$ in the domain with $m(x)=0$.
**Solution:** (A)(i) $x=\ln10-3$. (ii) $2x=\frac{\sqrt2}{2}$, $x=\frac{\sqrt2}{4}$. (B)(i) $\log_{10}\!\dfrac{16}{x^{2}}$. (ii) $\dfrac{\cos^{2}x}{\sin x\cos x}=\dfrac{1}{\tan x}$. (C) $\tan(2x)=1\Rightarrow x=\dfrac{\pi}{8}+\dfrac{\pi k}{2}$, $k$ an integer.

## 5. How to use these in the weekly workflow
- **Unit 1 checkpoint and Topic 1.5:** M1, M2, M8, F1, F5 (zeros, composition, rational behaviour, invertibility).
- **Unit 2:** M4, M6, F2, F4, F8, F9, F10, F12 (exponential and logarithmic equations, modelling, secant versus curve).
- **Unit 3:** M3, M5, M7, F3, F7, F11 (polar, secant, sinusoidal construction; the same "five points, then parameters, then interval behaviour" structure repeats in three of the twelve FRQs).
- Scoring practice: use section 2.4 as the rubric checklist on every FRQ attempt.
