# Week 5 — Sets of Vectors, Lines & Planes

**Session length:** 3 hours
**Source:** Siefken, *MAT223 Workbook*, Module 2 (Sets of Vectors, Lines & Planes)

---

## Page 1 — Introduction, Key Facts & Definitions

### Recap from Week 4 (Module 1)

Last week you worked with **linear combinations**: a vector $\vec w = \alpha_1 \vec v_1 + \alpha_2 \vec v_2 + \cdots + \alpha_n \vec v_n$, and with **set-builder notation** for describing a set of vectors satisfying some property. This week we use exactly those two tools to describe two of the most important geometric objects in linear algebra: **lines** and **planes**.

### Why this matters

In $\mathbb{R}^2$, a line can be described by $y = mx+b$ — but this fails for vertical lines, and it has no good analogue in $\mathbb{R}^3$ (where a line is the *intersection* of two planes, not the graph of one equation). Vectors fix this: every line and every plane, in any dimension, can be written as a **translated set of linear combinations** of one or two direction vectors. This shorthand is called **vector form**.

### Definition: Vector Form of a Line (Module 2, "Lines")

Consider the line $\ell$ through points $P$ and $Q$, and let $\vec d = \overrightarrow{PQ}$. The set of points reachable by starting at $P$ and displacing by some multiple of $\vec d$,
$$\ell = \{\vec x : \vec x = t\vec d + P \text{ for some } t \in \mathbb{R}\},$$
is exactly the line $\ell$. In set-builder notation, we must write **"for some $t \in \mathbb{R}$"** — replacing this with "for all $t \in \mathbb{R}$" turns the description into a (usually false) logical statement about a *single* vector $\vec x$, not a specification of the set $\ell$.

**Vector Form of a Line.** Let $\ell$ be a line and let $\vec d$ and $\vec p$ be vectors. If $\ell = \{\vec x : \vec x = t\vec d + \vec p \text{ for some } t \in \mathbb{R}\}$, we say the vector equation
$$\vec x = t\vec d + \vec p$$
is $\ell$ expressed in **vector form**. The vector $\vec d$ is called a **direction vector** for $\ell$. Since $t$ is playing the role of a *parameter variable* (a dummy variable — not the same quantity every time it's used), vector form is also called **parametric form**.

**Takeaway.** Vector form is a specific shorthand for a set. Writing $\vec x = t\vec d + \vec p$ (or the same thing with "where $t \in \mathbb{R}$" attached) means the set $\{\vec x : \vec x = t\vec d + \vec p \text{ for some } t \in \mathbb{R}\}$. Adding or removing words changes the meaning — and writing $\ell = t\vec d + \vec p$ is nonsensical (a set cannot equal a vector).

### Key Fact: Direction Vector $\neq$ Vector in the Line

A **direction vector** for $\ell$ tells you which way $\ell$ points; it is generally *not itself a point on $\ell$* (unless $\vec p = \vec 0$). Don't confuse "a direction vector for $\ell$" with "a vector in $\ell$."

### Key Fact: Vector Form Is Not Unique

Every line has infinitely many correct vector forms: any point on the line may be used as $\vec p$, and any nonzero scalar multiple of a direction vector is still a direction vector. For example,
$$\vec x = t\begin{bmatrix}1\\2\end{bmatrix}+\begin{bmatrix}0\\3\end{bmatrix}, \qquad \vec x = t\begin{bmatrix}2\\4\end{bmatrix}+\begin{bmatrix}0\\3\end{bmatrix}, \qquad \vec x = t\begin{bmatrix}1\\2\end{bmatrix}+\begin{bmatrix}1\\5\end{bmatrix}$$
all describe the *same* line. Because of this, you cannot decide whether two vector forms describe the same line just by comparing them visually — you must compare the **sets** they define (see the worked examples).

### Key Fact: Converting Between Cartesian and Vector Form

- **Cartesian $\to$ vector:** find *any* two points $A, B$ satisfying the Cartesian equation (guess-and-check works fine), then use $\vec d = \overrightarrow{AB}$ and $\vec p = A$.
- **Vector $\to$ Cartesian:** solve the parametric equations for the parameter(s) in terms of some coordinates, then substitute into the remaining coordinate equation(s) to eliminate the parameter(s).

### Key Fact: Determining Whether Two Lines Coincide or Intersect

Vector forms use a dummy parameter variable, so when comparing **two different lines**, always rename the parameters (e.g. $t$ and $s$) before setting the equations equal to each other. Solve the resulting system coordinate-by-coordinate:

- **Infinitely many solutions $(t,s)$** $\Rightarrow$ the lines coincide (same line).
- **Exactly one solution** $\Rightarrow$ the lines intersect at one point.
- **No solution, but directions proportional** $\Rightarrow$ the lines are parallel and distinct.
- **No solution, directions not proportional** (only possible in $\mathbb{R}^3$ and higher) $\Rightarrow$ the lines are **skew**: they point in different directions yet never meet.

### Definition: Vector Form of a Plane (Module 2, "Planes")

Three points $A,B,C \in \mathbb{R}^3$ that are **not collinear** determine a plane $P$. Both $\vec d_1 = \overrightarrow{AB}$ and $\vec d_2 = \overrightarrow{AC}$ are direction vectors for $P$; since a plane is two-dimensional, two non-parallel direction vectors suffice to describe it.

**Vector Form of a Plane.** A plane $P$ is written in vector form if it is expressed as
$$\vec x = t\vec d_1 + s\vec d_2 + \vec p$$
for some vectors $\vec d_1,\vec d_2$ and point $\vec p$; that is, $P = \{\vec x : \vec x = t\vec d_1+s\vec d_2+\vec p \text{ for some } t,s\in\mathbb{R}\}$. The vectors $\vec d_1,\vec d_2$ are called **direction vectors** for $P$.

Just as with lines, vector form of a plane is not unique — different point choices and different (non-parallel) direction vectors can describe the same plane.

### Key Fact: Intersecting Lines and Planes

The same "rename the parameters, set the equations equal, solve the system" strategy from lines works for planes too:

- **Line $\cap$ plane:** substitute the line's parametric coordinates directly into the plane's Cartesian equation and solve for the one parameter, **or** set the plane's vector form equal to the line's vector form (with a fresh parameter) and solve.
- **Plane $\cap$ plane:** generically a *line*. Set the two vector forms equal (four parameters total), solve the resulting (usually underdetermined) system, then substitute the free parameter back into either plane's equation to get the line of intersection in vector form.
- **Is a given point on a line/plane?** Substitute the point's coordinates into the vector equation and check whether *a single value of each parameter* makes **every** coordinate equation true simultaneously. It is not enough for one coordinate to match — all of them must match for the *same* $t$ (and $s$, for a plane).

---

## Pages 2–3 — Solved Examples

**Example 1 (Cartesian line $\to$ vector form, $\mathbb{R}^2$).** Find vector form of the line $\ell \subseteq \mathbb{R}^2$ with equation $y = 2x+3$.

*Reasoning.* Vector form needs one point on $\ell$ and one direction vector. We find two points by guess-and-check, then subtract.

By guess-and-check, $P=(0,3)$ and $Q=(1,5)$ both satisfy $y=2x+3$. A direction vector is
$$\vec d = \begin{bmatrix}1\\5\end{bmatrix}-\begin{bmatrix}0\\3\end{bmatrix}=\begin{bmatrix}1\\2\end{bmatrix}.$$
Hence
$$\vec x = t\begin{bmatrix}1\\2\end{bmatrix}+\begin{bmatrix}0\\3\end{bmatrix}$$
is $\ell$ in vector form. (Any other pair of points on $\ell$ would give an equally correct, but different-looking, vector form.)

---

**Example 2 (Vector form of a line through two given points, $\mathbb{R}^3$).** Find vector form of the line $\ell$ through $P=(3,-1,2)$ and $Q=(1,4,-2)$.

*Reasoning.* We're already handed two points, so no guessing is needed — the direction vector is simply the displacement from one point to the other, and either point can serve as $\vec p$.

$$\vec d = \overrightarrow{PQ} = \begin{bmatrix}1\\4\\-2\end{bmatrix}-\begin{bmatrix}3\\-1\\2\end{bmatrix}=\begin{bmatrix}-2\\5\\-4\end{bmatrix}.$$
Using $P$ as the base point,
$$\vec x = t\begin{bmatrix}-2\\5\\-4\end{bmatrix}+\begin{bmatrix}3\\-1\\2\end{bmatrix}.$$
Equally valid: using $Q$ as the base point, or using $\overrightarrow{QP}=\begin{bmatrix}2\\-5\\4\end{bmatrix}$ as the direction vector — the underlying set of points is identical either way.

---

**Example 3 (Do two vector forms describe the same line?).** Determine whether
$$\vec x = t\begin{bmatrix}1\\1\end{bmatrix}+\begin{bmatrix}2\\1\end{bmatrix} \qquad \text{and} \qquad \vec x = s\begin{bmatrix}2\\2\end{bmatrix}+\begin{bmatrix}4\\3\end{bmatrix}$$
are the same line.

*Reasoning.* The direction vectors are parallel ($\begin{bmatrix}2\\2\end{bmatrix}=2\begin{bmatrix}1\\1\end{bmatrix}$), so the lines are either identical or strictly parallel. We already renamed the parameters $t$ and $s$; now we check whether the systems is solvable for *every* choice of the other parameter, coordinate by coordinate.

$$t\begin{bmatrix}1\\1\end{bmatrix}+\begin{bmatrix}2\\1\end{bmatrix} = s\begin{bmatrix}2\\2\end{bmatrix}+\begin{bmatrix}4\\3\end{bmatrix} \;\Longrightarrow\; \begin{cases}t+2 = 2s+4\\ t+1 = 2s+3\end{cases} \;\Longrightarrow\; \begin{cases}t = 2s+2\\ t = 2s+2.\end{cases}$$

Both equations reduce to the *same* relation $t = 2s+2$. This has a solution for every $s$ (and every $t$), so every point of one line is a point of the other — the lines coincide. $\blacksquare$

---

**Example 4 (Do two lines in $\mathbb{R}^3$ intersect?).** Determine whether the lines
$$\vec x = t(1,3,-2)+(1,2,1) \qquad \text{and} \qquad \vec x = s(0,2,3)+(0,3,9)$$
intersect, and if so, find the point of intersection.

*Reasoning.* The direction vectors $(1,3,-2)$ and $(0,2,3)$ are not parallel (neither is a scalar multiple of the other), so the lines are *not* parallel — but in $\mathbb{R}^3$ that does not guarantee they intersect; they could be skew. We set the equations equal with different parameter names and read off a coordinate-by-coordinate system, which is now **overdetermined** (3 equations, 2 unknowns) — it may or may not be consistent.

$$t(1,3,-2)+(1,2,1) = s(0,2,3)+(0,3,9) \;\Longrightarrow\; (t+1,\,3t+2,\,-2t+1) = (0,\,2s+3,\,3s+9)$$

$$\begin{cases} t+1 = 0 \\ 3t+2 = 2s+3 \\ -2t+1 = 3s+9\end{cases}$$

From the first equation, $t=-1$. Substituting into the second: $-3+2=2s+3 \Rightarrow -1=2s+3 \Rightarrow s=-2$. **Check** the third (unused) equation with both values: $-2(-1)+1 = 3$ and $3(-2)+9=3$ — they agree, so the system is consistent and the lines really do intersect (had they disagreed, the lines would be skew).

Substituting $t=-1$ into the first line's equation gives the intersection point $(0,-1,3)$. $\blacksquare$

---

**Example 5 (Cartesian plane $\to$ vector form, then back again).** *(a)* Find vector form of the plane $P \subseteq \mathbb{R}^3$ with equation $z=2x+y+3$. *(b)* Then convert your answer back to Cartesian form, to confirm the round trip works.

*Reasoning for (a).* We need one point and *two* non-parallel direction vectors, so we need three points on $P$ that are not collinear.

By guess-and-check,
$$A=\begin{bmatrix}0\\0\\3\end{bmatrix}, \quad B=\begin{bmatrix}1\\0\\5\end{bmatrix}, \quad C=\begin{bmatrix}0\\1\\4\end{bmatrix}$$
all satisfy $z=2x+y+3$. Then
$$\vec d_1 = B - A = \begin{bmatrix}1\\0\\2\end{bmatrix}, \qquad \vec d_2 = C-A = \begin{bmatrix}0\\1\\1\end{bmatrix}$$
are direction vectors for $P$ (they are not parallel, so they genuinely span the plane), and
$$\vec x = t\begin{bmatrix}1\\0\\2\end{bmatrix}+s\begin{bmatrix}0\\1\\1\end{bmatrix}+\begin{bmatrix}0\\0\\3\end{bmatrix}.$$

*Reasoning for (b).* Reading off coordinates from the vector form, $x=t$, $y=s$, $z=2t+s+3$. Since $t=x$ and $s=y$ directly, substitute:
$$z = 2x+y+3,$$
which is exactly the equation we started with — confirming the conversion is reversible. $\blacksquare$

---

**Example 6 (Vector form of a plane through three explicitly given points).** Find vector form of the plane through $A=(2,0,1)$, $B=(3,2,1)$, $C=(1,1,4)$.

*Reasoning.* Unlike Example 5, we are handed the three points directly, so no guessing is required — just subtract to get two direction vectors from a common base point $A$.

$$\vec d_1 = \overrightarrow{AB} = \begin{bmatrix}1\\2\\0\end{bmatrix}, \qquad \vec d_2 = \overrightarrow{AC} = \begin{bmatrix}-1\\1\\3\end{bmatrix}.$$
These are not parallel, so they are valid direction vectors, and
$$\vec x = t\begin{bmatrix}1\\2\\0\end{bmatrix}+s\begin{bmatrix}-1\\1\\3\end{bmatrix}+\begin{bmatrix}2\\0\\1\end{bmatrix}$$
is $P$ in vector form. (We could equally well have used $\overrightarrow{BC}$ paired with $\overrightarrow{AB}$, and $B$ or $C$ as the base point.)

---

**Example 7 (Does a given point lie on a given line?).** Is $(4,7,-1)$ on the line $L: \vec x = t(1,3,-2)+(1,2,1)$?

*Reasoning.* A point lies on $L$ only if there is a **single** value of $t$ that makes *every* coordinate match simultaneously — it is not enough to check one coordinate.

From the first coordinate: $4 = 1+t \Rightarrow t=3$. Check the second coordinate at $t=3$: $2+3(3) = 11 \neq 7$. Since no single $t$ can satisfy all three coordinate equations at once, $(4,7,-1)$ is **not** on $L$. $\blacksquare$

---

**Example 8 (Where does a line meet a plane?).** Find the intersection of $P_1: x - y + 2z = 4$ and $\ell: \vec x = t(1,0,-1)+(2,1,0)$.

*Reasoning.* $\ell$ is already parametrized, so the fastest route is to substitute its coordinates directly into $P_1$'s Cartesian equation and solve for the single unknown $t$.

Coordinates of $\ell$: $x = 2+t,\; y=1,\; z=-t$. Substituting into $P_1$:
$$(2+t) - (1) + 2(-t) = 4 \;\Longrightarrow\; 1 - t = 4 \;\Longrightarrow\; t = -3.$$
The intersection point is $(2+(-3),\,1,\,-(-3)) = (-1,1,3)$. **Check:** $-1-1+2(3) = 4$. ✓ $\blacksquare$

---

## Pages 4–5 — Practice Problems (unsolved)

**Lines**

1. Express $\ell_1 \subseteq \mathbb{R}^2$ with equation $4x-3y=-10$ in vector form.
2. Express $\ell_4 \subseteq \mathbb{R}^3$, the line through $A=(-1,-1,0)$ and $B=(2,3,5)$, in vector form.
3. Express $\ell_3 \subseteq \mathbb{R}^2$, the line through the origin parallel to $\ell_1$ from Problem 1, in vector form.
4. Let $L: \vec x = t(1,3,-2)+(1,2,1)$. Determine whether the point $(3,8,-3)$ lies on $L$.

**Planes**

5. Express $P_2 \subseteq \mathbb{R}^3$, the plane through $A=(-1,-1,0)$, $B=(2,3,5)$, and $C=(3,3,3)$, in vector form.
6. Let $Q \subseteq \mathbb{R}^3$ be the plane with equation $x+y+z=1$. Find three points in $Q$, find two direction vectors for $Q$, and write $Q$ in vector form.
7. Determine whether the point $(2,-1,3)$ lies on the plane $\vec x = t(1,0,2)+s(0,1,1)+(0,0,4)$.

**Converting Between Forms**

8. Express $P_1 \subseteq \mathbb{R}^3$ with equation $4x - z = 0$ in vector form.
9. Express $P_4 \subseteq \mathbb{R}^3$, the plane parallel to the $yz$-plane passing through $X=(1,-1,1)$, in vector form.
10. Convert the plane $\vec x = t(1,-1,0)+s(2,0,1)+(1,1,-2)$ into a scalar (Cartesian) equation by eliminating the parameters $t$ and $s$.

**Intersections**

11. Let $A$ and $C$ be given in vector form by
$$A: \vec x = t\begin{bmatrix}1\\2\\3\end{bmatrix}+\begin{bmatrix}0\\0\\1\end{bmatrix}, \qquad B: \vec x = t\begin{bmatrix}-1\\1\\1\end{bmatrix}+\begin{bmatrix}-1\\1\\2\end{bmatrix}, \qquad C: \vec x = t\begin{bmatrix}2\\-1\\1\end{bmatrix}+\begin{bmatrix}1\\1\\1\end{bmatrix}.$$
    (a) Do the lines $A$ and $B$ intersect? Justify your conclusion. (b) Do the lines $A$ and $C$ intersect? Justify your conclusion.
12. Let $P_1 \subseteq \mathbb{R}^3$ be the plane with equation $x+2y-z=3$, and let $\ell: \vec x = t(1,3,1)+(1,1,0)$. Find $P_1 \cap \ell$.
13. Let $\ell_1, \ell_2, \ell_3$ be described in vector form by
$$\ell_1: \vec x = t\begin{bmatrix}1\\1\end{bmatrix}+\begin{bmatrix}1\\3\end{bmatrix}, \qquad \ell_2: \vec x = t\begin{bmatrix}1\\3\end{bmatrix}+\begin{bmatrix}1\\1\end{bmatrix}, \qquad \ell_3: \vec x = t\begin{bmatrix}2\\2\end{bmatrix}+\begin{bmatrix}2\\4\end{bmatrix}.$$
    (a) Determine which pairs of the lines intersect, coincide, or are parallel. (b) Find $\ell_1 \cap \ell_2 \cap \ell_3$.

---

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|---|---|
| 1 | $\vec x = t\begin{bmatrix}3\\4\end{bmatrix}+\begin{bmatrix}-1\\2\end{bmatrix}$ (e.g. via points $(-1,2)$ and $(2,6)$) | Solving $4x-3y=-10$ for a slope and writing $y=mx+b$ form instead of finding two points and subtracting; also forgetting that any two points on the line give an equally valid (if different-looking) answer. |
| 2 | $\vec x = t\begin{bmatrix}3\\4\\5\end{bmatrix}+\begin{bmatrix}-1\\-1\\0\end{bmatrix}$ | Computing $\overrightarrow{AB}$ as $A-B$ instead of $B-A$, which just flips the direction's sign but is easy to do inconsistently partway through a longer problem. |
| 3 | $\vec x = t\begin{bmatrix}3\\4\end{bmatrix}$ | Forgetting that "parallel" only constrains the direction vector — re-deriving a whole new direction vector from scratch instead of reusing the one already found for $\ell_1$, and/or forgetting the base point is $\vec 0$ so the $+\vec p$ term is simply dropped. |
| 4 | Yes; $t=2$ gives $(1+2,\,2+6,\,1-4)=(3,8,-3)$ | Checking only the $x$-coordinate for a matching $t$ and declaring the point "on the line" without verifying the $y$- and $z$-coordinates give the *same* $t$. |
| 5 | $\vec x = t\begin{bmatrix}3\\4\\5\end{bmatrix}+s\begin{bmatrix}4\\4\\3\end{bmatrix}+\begin{bmatrix}-1\\-1\\0\end{bmatrix}$ (using $\vec d_1=\overrightarrow{AB}$, $\vec d_2=\overrightarrow{AC}$) | Using two direction vectors that turn out to be parallel (e.g. picking $\overrightarrow{AB}$ and $2\overrightarrow{AB}$ by accident), which only describes a line, not the full plane. |
| 6 | Points e.g. $(1,0,0),(0,1,0),(0,0,1)$; $\vec d_1=(-1,1,0)$, $\vec d_2=(-1,0,1)$; $\vec x=t(-1,1,0)+s(-1,0,1)+(1,0,0)$ | Choosing three points that happen to be collinear (e.g. all with $z=0$ satisfying a coincidental linear relation) and not noticing the two "direction vectors" are actually parallel. |
| 7 | No — plugging in gives $t=2,\ s=-1$, so $z$ should be $2(2)+(-1)+4=7 \neq 3$ | Only checking that $t$ and $s$ exist matching the $x$- and $y$-coordinates, and forgetting to verify the *third* coordinate equation with those same values. |
| 8 | $\vec x = t\begin{bmatrix}1\\0\\4\end{bmatrix}+s\begin{bmatrix}0\\1\\0\end{bmatrix}$ (through the origin) | Forgetting the plane passes through $\vec 0$ (since $(0,0,0)$ satisfies $4x-z=0$), and instead guessing an unnecessary nonzero base point. |
| 9 | $\vec x = t\begin{bmatrix}0\\1\\0\end{bmatrix}+s\begin{bmatrix}0\\0\\1\end{bmatrix}+\begin{bmatrix}1\\-1\\1\end{bmatrix}$ (equivalently the plane $x=1$) | Not realizing "parallel to the $yz$-plane" means the direction vectors are just $\vec e_2,\vec e_3$ unchanged — instead trying to compute new direction vectors from scratch, or mistakenly changing the $x$-component of the direction vectors. |
| 10 | $x+y-2z=6$ | Sign errors while isolating $t$ and $s$ (e.g. writing $t=y-1$ instead of $t=1-y$) that silently flip the sign of a term when substituted back in. |
| 11 | (a) Yes, at $(0,0,1)$ ($t=0$, $s=-1$). (b) No — directions not proportional and the system is inconsistent, so $A$ and $C$ are skew. | Concluding two $\mathbb{R}^3$ lines "don't intersect" $\Rightarrow$ "parallel," forgetting that non-parallel lines in $\mathbb{R}^3$ can simply be skew; also forgetting to use a fresh parameter name for the second line before setting the equations equal. |
| 12 | $P_1 \cap \ell = \{(1,1,0)\}$ (at $t=0$) | Substituting $\ell$'s parametric coordinates into $P_1$ correctly but then forgetting to plug the solved $t$ back into $\ell$'s equation to report an actual point, leaving the answer as just "$t=0$." |
| 13 | (a) $\ell_1$ and $\ell_3$ coincide (same line); $\ell_2$ crosses both at $(2,4)$. (b) $\ell_1 \cap \ell_2 \cap \ell_3 = \{(2,4)\}$. | Seeing that $\ell_1$'s and $\ell_3$'s direction vectors are parallel and stopping at "parallel," without checking whether $\ell_3$'s point actually lies on $\ell_1$ (which is what makes them coincide rather than merely parallel-and-distinct). |
