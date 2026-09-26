# Week 7 — Dot Products, Normal Forms & Projections

**Session length:** 3 hours
**Source:** Siefken, *MAT223 Workbook*, Module 4 (Dot Products & Normal Forms) and Module 5 (Projections & Vector Components)

---

## Page 1 — Introduction, Key Facts & Definitions

### Recap from Previous Weeks

You already know how to write a line or plane in **vector form**, $\vec x = t\vec d + \vec p$ (line) or $\vec x = t\vec d_1 + s\vec d_2 + \vec p$ (plane), using a base point and one or two direction vectors, and how to describe a set of vectors as a **span**. Vector form answers the question "how do I *walk along* this line/plane?" This week we build a second, completely different tool for describing the same objects — the **dot product** and the **normal form** it produces — which instead answers the question "which vectors point *straight into* this line/plane?" The two descriptions are complementary, and converting between them will become a routine skill.

### Why this matters

The dot product is the single most useful tool in this course besides matrix multiplication. It measures length, angle, and orthogonality all at once, it gives us a second way to describe lines and planes (normal form) that is often faster to write down than vector form, and it is the key ingredient in **projections** — finding the closest point in a line or plane to a given vector. Projections are what let us "flatten" a high-dimensional object onto a lower-dimensional one, which is a recurring theme for the rest of the course (and in applications, from 3D graphics to data science).

### Definition: Dot Product — Geometric and Algebraic (Module 4)

Let $\vec a$ and $\vec b$ be vectors rooted at the same point, and let $\theta$ denote the smaller angle between them ($0 \leq \theta \leq \pi$). The **geometric definition** of the dot product is
$$\vec a \cdot \vec b = \|\vec a\|\|\vec b\|\cos\theta.$$
The dot product is also called the **scalar product**, because the result is a scalar, not a vector.

Algebraically, in coordinates,
$$\begin{bmatrix}a_1\\a_2\\\vdots\\a_n\end{bmatrix} \cdot \begin{bmatrix}b_1\\b_2\\\vdots\\b_n\end{bmatrix} = a_1b_1 + a_2b_2 + \cdots + a_nb_n.$$
This is the **algebraic definition**. Because both definitions compute the *same* quantity, we can switch between them — using the algebraic formula (which needs only coordinates) to find the quantity $\vec a \cdot \vec b$, then using the geometric formula (which involves $\theta$) to extract angle information, or vice versa.

### Fact: The Dot Product Computes Length (Module 4)

Since the angle between $\vec a$ and itself is $0$, the geometric definition gives $\vec a \cdot \vec a = \|\vec a\|\|\vec a\|\cos 0 = \|\vec a\|^2$. Hence
$$\|\vec a\| = \sqrt{\vec a \cdot \vec a}.$$
This is called the **norm** of $\vec v = \begin{bmatrix}v_1\\ \vdots \\v_n\end{bmatrix}$; it can equivalently be computed directly from the Pythagorean formula $\|\vec v\| = \sqrt{v_1^2+\cdots+v_n^2}$.

**Related definitions.** The **distance** between two vectors $\vec u$ and $\vec v$ is $\|\vec u - \vec v\|$. A vector $\vec v$ is a **unit vector** if $\|\vec v\| = 1$.

### Key Fact: Algebraic Properties of the Dot Product (Module 4)

For any vectors $\vec a, \vec b, \vec c$ and scalar $k$:
$$(\vec a+\vec b)\cdot\vec c = \vec a\cdot\vec c + \vec b\cdot\vec c, \qquad \vec a\cdot(\vec b+\vec c) = \vec a\cdot\vec b + \vec a\cdot\vec c,$$
$$(k\vec a)\cdot\vec b = k(\vec a\cdot\vec b) = \vec a\cdot(k\vec b), \qquad \vec a\cdot\vec b = \vec b\cdot\vec a.$$

### Definition: Orthogonal (Module 4)

Two vectors $\vec u$ and $\vec v$ are **orthogonal** to each other if $\vec u \cdot \vec v = 0$. "Orthogonal" is synonymous with "perpendicular." Note that $\vec u \cdot \vec v = 0$ can hold for two reasons: either $\vec u = \vec 0$, $\vec v = \vec 0$, or both; **or** $\vec u$ and $\vec v$ meet at $90^\circ$. The definition deliberately includes the zero-vector case, because doing so simplifies later theory.

### Definition: Direction (Module 4)

The vector $\vec u$ **points in the direction of** $\vec v$ if $\vec u = k\vec v$ for some scalar $k$. It points in the **positive direction** of $\vec v$ if $k > 0$. Since $\cos\theta = \dfrac{\vec p \cdot \vec q}{\|\vec p\|\|\vec q\|}$ (equating the two definitions of the dot product), the closer $\cos\theta$ is to $1$, the closer $\vec p$'s direction is to $\vec q$'s.

### Definition: Normal Vector (Module 4)

A **normal vector** to a line (or plane, or hyperplane) is a non-zero vector that is orthogonal to *all* direction vectors for that line/plane/hyperplane.

### Definition: Normal Form of a Line or Plane (Module 4)

A line $\ell \subseteq \mathbb{R}^2$ (or a plane $P \subseteq \mathbb{R}^3$) is expressed in **normal form** if there exist vectors $\vec n \neq \vec 0$ and $\vec p$ so that the line/plane is exactly the solution set of
$$\vec n \cdot (\vec x - \vec p) = 0.$$
If a line/plane is expressed this way, $\vec n$ is necessarily a normal vector for it. (If $\vec n$ were $\vec 0$, the equation would be satisfied by *every* $\vec x$, which is not a line or plane.) In $\mathbb{R}^n$, an object with a normal form is called a **hyperplane**; hyperplanes always have dimension one less than the surrounding space (lines in $\mathbb{R}^2$, planes in $\mathbb{R}^3$).

### Key Fact: Normal Form $\leftrightarrow$ Scalar (Cartesian) Form (Module 4)

Expanding $\vec n \cdot (\vec x - \vec p) = 0$ gives $\vec n \cdot \vec x = \vec n \cdot \vec p = \alpha$, a constant since $\vec n, \vec p$ are fixed. Writing $\vec n = \begin{bmatrix}n_x\\n_y\\n_z\end{bmatrix}$, this becomes the familiar **scalar (Cartesian) equation**
$$n_x x + n_y y + n_z z = \alpha.$$
Going the other way — from a scalar equation back to vector form — you row-reduce the corresponding augmented matrix and read off the complete solution, exactly as you did with systems of equations.

**Finding a normal vector when you already have direction vectors:** if $\vec d_1, \vec d_2$ are direction vectors for a plane, a normal vector $\vec n$ must satisfy *both* $\vec n \cdot \vec d_1 = 0$ and $\vec n \cdot \vec d_2 = 0$ — sometimes you can spot $\vec n$ by inspection, and otherwise you solve this small system.

### Definition: Projection (Module 5)

Let $X \subseteq \mathbb{R}^n$ be a set. The **projection** of $\vec v \in \mathbb{R}^n$ onto $X$, written $\operatorname{proj}_X \vec v$, is the **closest point in $X$ to $\vec v$**. (This is sometimes called the *orthogonal* projection, to distinguish it from other kinds of projections.) If $\vec v$ is equidistant from two closest points of $X$, or $X$ has no closest point at all, $\operatorname{proj}_X \vec v$ is simply undefined — but for lines and planes in $\mathbb{R}^n$, the projection is always defined.

### Key Fact: Projections Onto Lines/Planes and Normal Vectors (Module 5)

If $X$ is a line or a plane and $\vec v \notin X$, then $\vec v - \operatorname{proj}_X \vec v$ is a **normal vector for $X$**. This is extremely useful: it means you can find $\operatorname{proj}_X\vec v$ by setting up orthogonality equations (dot products equal to zero) instead of literally minimizing a distance formula.

### Definition: Vector Component (Module 5)

Let $\vec u$ and $\vec v \neq \vec 0$ be vectors. The **vector component of $\vec u$ in the $\vec v$ direction**, written $\operatorname{vcomp}_{\vec v}\vec u$, is the vector in the direction of $\vec v$ so that $\vec u - \operatorname{vcomp}_{\vec v}\vec u$ is orthogonal to $\vec v$. By definition,
$$\vec u = \operatorname{vcomp}_{\vec v}\vec u + \big(\vec u - \operatorname{vcomp}_{\vec v}\vec u\big)$$
decomposes $\vec u$ into a piece parallel to $\vec v$ and a piece orthogonal to $\vec v$.

### Key Fact: Formula for the Vector Component (Module 5)

Since $\operatorname{vcomp}_{\vec v}\vec u = k\vec v$ for some scalar $k$, and $\vec v \cdot (\vec u - k\vec v) = 0$, solving for $k$ (using $\vec v \cdot \vec v \neq 0$ since $\vec v \neq \vec 0$) gives $k = \dfrac{\vec v \cdot \vec u}{\vec v \cdot \vec v}$, and so
$$\operatorname{vcomp}_{\vec v}\vec u = \left(\dfrac{\vec v \cdot \vec u}{\vec v \cdot \vec v}\right)\vec v.$$

### Theorem: Projection Onto a Span Equals Vector Component (Module 5)

For vectors $\vec u$ and $\vec v \neq \vec 0$,
$$\operatorname{proj}_{\operatorname{span}\{\vec v\}} \vec u = \operatorname{vcomp}_{\vec v} \vec u.$$
This is only true when the target set is a **span through the origin** — it is a computational shortcut for that one special case, not a general fact about projections. If the line does *not* pass through the origin (e.g. $\ell = \operatorname{span}\{\vec v\}+\{\vec p\}$ with $\vec p \notin \operatorname{span}\{\vec v\}$), $\operatorname{proj}_\ell \vec u$ and $\operatorname{vcomp}_{\vec v}\vec u$ are generally **different** vectors, and you must fall back on the orthogonality method (Key Fact above) instead.

---

## Pages 2–3 — Solved Examples

**Example 1 (Compute dot products and test orthogonality).** Let $\vec u = \begin{bmatrix}3\\-1\\2\end{bmatrix}$, $\vec v = \begin{bmatrix}4\\10\\1\end{bmatrix}$, and $\vec w = \begin{bmatrix}1\\3\\0\end{bmatrix}$. Compute $\vec u \cdot \vec v$ and $\vec u \cdot \vec w$, and determine which pair, if either, is orthogonal.

Using the algebraic definition (multiply matching coordinates, then add):
$$\vec u \cdot \vec v = 3(4)+(-1)(10)+2(1) = 12-10+2 = 4.$$
$$\vec u \cdot \vec w = 3(1)+(-1)(3)+2(0) = 3-3+0 = 0.$$
Since $\vec u \cdot \vec v = 4 \neq 0$, $\vec u$ and $\vec v$ are **not** orthogonal. Since $\vec u \cdot \vec w = 0$ and neither vector is $\vec 0$, $\vec u$ and $\vec w$ **are** orthogonal. $\blacksquare$

---

**Example 2 (Find the angle between two vectors).** Find the angle between $\vec v = (1,2,3)$ and $\vec w = (1,1,-2)$.

From the algebraic definition,
$$\vec v \cdot \vec w = 1(1)+2(1)+3(-2) = -3.$$
From the geometric definition,
$$\vec v \cdot \vec w = \|\vec v\|\|\vec w\|\cos\theta = \sqrt{14}\sqrt{6}\cos\theta = 2\sqrt{21}\cos\theta.$$
Equating the two definitions of $\vec v \cdot \vec w$,
$$\cos\theta = \dfrac{-3}{2\sqrt{21}} \qquad \text{so} \qquad \theta = \arccos\left(\dfrac{-3}{2\sqrt{21}}\right).$$
This is the whole strategy for using dot products to find angles: compute the dot product algebraically (fast), then solve for $\theta$ using the geometric formula.

---

**Example 3 (Use the dot product to find the closest direction).** Let $\vec a = \begin{bmatrix}1\\2\end{bmatrix}$, $\vec b = \begin{bmatrix}3\\3\end{bmatrix}$, $\vec c = \begin{bmatrix}2\\1\end{bmatrix}$, and $\vec v = \begin{bmatrix}3\\4\end{bmatrix}$. Which of $\vec a, \vec b, \vec c$ points in a direction closest to $\vec v$?

The angle $\theta$ between two vectors is smallest exactly when $\cos\theta$ is closest to $1$ (since $\cos 0 = 1$). From $\cos\theta = \dfrac{\vec p \cdot \vec q}{\|\vec p\|\|\vec q\|}$, let $\alpha, \beta, \gamma$ be the angles between $\vec v$ and $\vec a, \vec b, \vec c$ respectively:
$$\cos\alpha = \dfrac{3+8}{5\sqrt 5} = \dfrac{11\sqrt5}{25} \approx 0.9839, \qquad \cos\beta = \dfrac{9+12}{5\sqrt{18}} = \dfrac{7\sqrt2}{10} \approx 0.9899,$$
$$\cos\gamma = \dfrac{6+4}{5\sqrt 5} = \dfrac{2\sqrt5}{5} \approx 0.8944.$$
Since $\cos\beta$ is closest to $1$, $\vec b$ points in the direction closest to $\vec v$. $\blacksquare$

---

**Example 4 (Find a normal vector and write a line's normal form).** Let $\vec n = \begin{bmatrix}1\\2\end{bmatrix}$. Find the line $\ell$ consisting of all vectors orthogonal to $\vec n$, then write the normal form of $\ell$ and of its translate $\ell_2$ through $\vec p = \begin{bmatrix}1\\1\end{bmatrix}$.

If $\vec v = \begin{bmatrix}v_1\\v_2\end{bmatrix}$ is orthogonal to $\vec n$, then $\vec n \cdot \vec v = v_1+2v_2 = 0$, so $v_1 = -2v_2$. Thus $\vec v \in \operatorname{span}\left\{\begin{bmatrix}-2\\1\end{bmatrix}\right\}$, and the set of all vectors orthogonal to $\vec n$ is exactly the line $\ell = \operatorname{span}\left\{\begin{bmatrix}-2\\1\end{bmatrix}\right\}$. Since every vector of $\ell$ is orthogonal to $\vec n$, $\vec n$ is a normal vector for $\ell$, and $\ell$'s normal form is
$$\vec n \cdot \vec x = 0.$$
Translating $\ell$ by $\vec p$ gives $\ell_2 = \operatorname{span}\left\{\begin{bmatrix}-2\\1\end{bmatrix}\right\} + \left\{\begin{bmatrix}1\\1\end{bmatrix}\right\}$, and since $\vec n$ is still orthogonal to every direction vector of $\ell_2$ (translating doesn't change directions), $\vec n$ is also a normal vector for $\ell_2$, with normal form
$$\vec n \cdot (\vec x - \vec p) = 0.$$

---

**Example 5 (Normal form of a plane through three points).** Find vector form and normal form of the plane $P$ through $A=(1,0,0)$, $B=(0,1,0)$, $C=(0,0,1)$.

*Vector form.* Using $A$ as base point, $\vec d_1 = \overrightarrow{AB} = \begin{bmatrix}-1\\1\\0\end{bmatrix}$ and $\vec d_2 = \overrightarrow{AC} = \begin{bmatrix}-1\\0\\1\end{bmatrix}$, so
$$\vec x = t\begin{bmatrix}-1\\1\\0\end{bmatrix} + s\begin{bmatrix}-1\\0\\1\end{bmatrix} + \begin{bmatrix}1\\0\\0\end{bmatrix}.$$
*Normal form.* We need $\vec n$ with $\vec n \cdot \vec d_1 = 0$ and $\vec n \cdot \vec d_2 = 0$. By inspection, $\vec n = \begin{bmatrix}1\\1\\1\end{bmatrix}$ works ($-1+1+0=0$ and $-1+0+1=0$). (If we weren't so lucky at guessing, we would instead solve the system $\vec n \cdot \vec d_1 = 0$, $\vec n \cdot \vec d_2=0$ directly.) So
$$\begin{bmatrix}1\\1\\1\end{bmatrix} \cdot \left(\begin{bmatrix}x\\y\\z\end{bmatrix} - \begin{bmatrix}1\\0\\0\end{bmatrix}\right) = 0$$
is $P$ in normal form.

---

**Example 6 (Normal form $\to$ scalar form $\to$ vector form).** Let $Q \subseteq \mathbb{R}^3$ be the plane through $\vec p = \begin{bmatrix}1\\1\\0\end{bmatrix}$ with normal vector $\vec n = \begin{bmatrix}1\\1\\1\end{bmatrix}$. Write $Q$ in vector form.

$Q$'s normal form is $\vec n \cdot (\vec x - \vec p) = 0$. Expanding into scalar form,
$$\vec n \cdot \vec x - \vec n \cdot \vec p = x+y+z - 2 = 0 \quad \Longrightarrow \quad x+y+z=2.$$
This corresponds to the (already row-reduced) augmented matrix $\begin{bmatrix}1 & 1 & 1 & \vert & 2\end{bmatrix}$. Solving for the complete solution (letting $y=t$, $z=s$ be free, so $x = 2-t-s$):
$$\vec x = t\begin{bmatrix}-1\\1\\0\end{bmatrix} + s\begin{bmatrix}-1\\0\\1\end{bmatrix} + \begin{bmatrix}2\\0\\0\end{bmatrix}.$$

---

**Example 7 (Vector projection onto a line, using the definition).** Let $\ell$ be given in vector form by $\vec x = t\begin{bmatrix}1\\1\end{bmatrix}+\begin{bmatrix}3\\-2\end{bmatrix}$, and let $\vec v = \begin{bmatrix}-1\\-1\end{bmatrix}$. Use the definition of projection (closest point) to find $\operatorname{proj}_\ell \vec v$.

Let $\vec u_t = t\begin{bmatrix}1\\1\end{bmatrix}+\begin{bmatrix}3\\-2\end{bmatrix}$ be a generic point of $\ell$. The distance from $\vec v$ to $\vec u_t$ is
$$\|\vec u_t - \vec v\| = \left\|\begin{bmatrix}t+4\\t-1\end{bmatrix}\right\| = \sqrt{2t^2+6t+17}.$$
This is minimized exactly where $2t^2+6t+17$ is minimized, which (using the vertex formula $t=-\dfrac{b}{2a}$) occurs at $t = -\dfrac{6}{2(2)} = -\dfrac32$. So the closest point of $\ell$ to $\vec v$ is $\vec u_{-3/2}$:
$$\operatorname{proj}_\ell \vec v = -\dfrac32\begin{bmatrix}1\\1\end{bmatrix}+\begin{bmatrix}3\\-2\end{bmatrix} = \begin{bmatrix}3/2\\-7/2\end{bmatrix}.$$

---

**Example 8 (The same projection, using the orthogonality shortcut).** Redo Example 7 using the fact that $\vec v - \operatorname{proj}_\ell \vec v$ is a normal vector for $\ell$, and confirm the two methods agree.

Since $\vec v - \operatorname{proj}_\ell \vec v$ is orthogonal to $\ell$'s direction vector $\vec d = \begin{bmatrix}1\\1\end{bmatrix}$, write $\begin{bmatrix}x\\y\end{bmatrix} = \operatorname{proj}_\ell \vec v$ for unknown $x,y$. Then
$$(\vec v - \operatorname{proj}_\ell\vec v)\cdot \vec d = \begin{bmatrix}-1-x\\-1-y\end{bmatrix}\cdot\begin{bmatrix}1\\1\end{bmatrix} = -2-x-y = 0 \quad\Longrightarrow\quad x+y=-2. \tag{i}$$
Also, since $\operatorname{proj}_\ell\vec v \in \ell$, $\begin{bmatrix}x\\y\end{bmatrix} = t\begin{bmatrix}1\\1\end{bmatrix}+\begin{bmatrix}3\\-2\end{bmatrix}$ for some $t$, giving $x-t=3$ and $y-t=-2$. Combined with (i), we get three equations in three unknowns $x,y,t$:
$$\begin{cases}x+y=-2\\ x-t=3\\ y-t=-2\end{cases}$$
Solving, $x=3/2$, $y=-7/2$ (the value of $t$ is not needed). So $\operatorname{proj}_\ell \vec v = \begin{bmatrix}3/2\\-7/2\end{bmatrix}$, which **matches Example 7**. $\blacksquare$

Note that this line does not pass through the origin, so $\operatorname{vcomp}_{\vec d}\vec v$ would **not** give the right answer here — only the orthogonality method works for a line that isn't a span.

---

**Example 9 (Vector component formula and orthogonal decomposition).** Let $\vec a = \begin{bmatrix}1\\2\end{bmatrix}$ and $\vec b = \begin{bmatrix}1\\1\end{bmatrix}$. Find $\operatorname{vcomp}_{\vec b}\vec a$, and decompose $\vec a$ into a piece parallel to $\vec b$ and a piece orthogonal to $\vec b$.

By the formula, $k = \dfrac{\vec b \cdot \vec a}{\vec b \cdot \vec b} = \dfrac{1(1)+1(2)}{1(1)+1(1)} = \dfrac{3}{2}$, so
$$\operatorname{vcomp}_{\vec b}\vec a = \dfrac32\begin{bmatrix}1\\1\end{bmatrix} = \begin{bmatrix}3/2\\3/2\end{bmatrix}.$$
The orthogonal piece is $\vec a - \operatorname{vcomp}_{\vec b}\vec a = \begin{bmatrix}1-3/2\\2-3/2\end{bmatrix} = \begin{bmatrix}-1/2\\1/2\end{bmatrix}$. **Check:** $\begin{bmatrix}-1/2\\1/2\end{bmatrix}\cdot\begin{bmatrix}1\\1\end{bmatrix} = -\dfrac12+\dfrac12=0$, confirming orthogonality, and $\begin{bmatrix}3/2\\3/2\end{bmatrix}+\begin{bmatrix}-1/2\\1/2\end{bmatrix} = \begin{bmatrix}1\\2\end{bmatrix} = \vec a$, confirming the decomposition adds back up. $\blacksquare$

---

## Pages 4–5 — Practice Problems (unsolved)

**Dot Products & Orthogonality**

1. Compute $\begin{bmatrix}9\\4\end{bmatrix}\cdot\begin{bmatrix}10\\-3\end{bmatrix}$.
2. Compute the length $\|\vec v\|$ of $\vec v = \begin{bmatrix}1\\2\\3\end{bmatrix}$ using $\|\vec v\| = \sqrt{\vec v \cdot \vec v}$.
3. Determine whether the angle between $\begin{bmatrix}1\\0\\1\end{bmatrix}$ and $\begin{bmatrix}-5\\4\\-3\end{bmatrix}$ is greater than, less than, or equal to $90^\circ$.
4. Find two unit vectors orthogonal to $\begin{bmatrix}1\\2\end{bmatrix}$.

**Normal Vectors & Normal Form**

5. Let $\vec d = \begin{bmatrix}1\\2\end{bmatrix}$ and $\vec p = \begin{bmatrix}1\\-1\end{bmatrix}$, and let $\ell_1 = \operatorname{span}\{\vec d\}$ and $\ell_2 = \operatorname{span}\{\vec d\}+\{\vec p\}$. Find a normal vector $\vec n$ that works for **both** $\ell_1$ and $\ell_2$, then write both lines in normal form.
6. Express the plane $P \subseteq \mathbb{R}^3$ through $A=(2,0,0)$, $B=(0,3,0)$, $C=(0,0,-1)$ in both vector form and normal form.
7. Let $B \subseteq \mathbb{R}^3$ be the plane through $\begin{bmatrix}1\\2\\3\end{bmatrix}$ with normal vector $\begin{bmatrix}1\\-1\\0\end{bmatrix}$. Write $B$'s normal form, then convert it to scalar (Cartesian) form and to vector form.

**Projections**

8. Let $\ell = \operatorname{span}\left\{\begin{bmatrix}2\\1\end{bmatrix}\right\}$ and $\vec v = \begin{bmatrix}1\\0\end{bmatrix}$. Find $\operatorname{proj}_\ell \vec v$.
9. Let $K$ be given in vector form by $\vec x = t\begin{bmatrix}1\\2\end{bmatrix}+\begin{bmatrix}1\\0\end{bmatrix}$, and let $\vec c = \begin{bmatrix}1\\3\end{bmatrix}$. Find $\operatorname{proj}_K \vec c$ using the fact that $\vec c - \operatorname{proj}_K \vec c$ is orthogonal to $K$'s direction vector.

**Vector Components**

10. Let $\vec a, \vec b \in \mathbb{R}^3$ be unknown vectors with $\vec b \neq \vec 0$. (a) State the two defining conditions $\operatorname{vcomp}_{\vec b}\vec a$ must satisfy. (b) Using those two conditions, derive the formula for $\operatorname{vcomp}_{\vec b}\vec a$.
11. Let $\vec d = \begin{bmatrix}3\\3\end{bmatrix}$ and $\vec u = \begin{bmatrix}1\\2\end{bmatrix}$. Compute $\operatorname{proj}_{\operatorname{span}\{\vec d\}}\vec u$ and $\operatorname{vcomp}_{\vec d}\vec u$ and confirm they are equal. Then compute $\operatorname{vcomp}_{-\vec d}\vec u$: is it the same as or different from $\operatorname{vcomp}_{\vec d}\vec u$? Explain.
12. Decompose $\vec u = \begin{bmatrix}4\\1\end{bmatrix}$ into a component parallel to $\vec v = \begin{bmatrix}1\\3\end{bmatrix}$ and a component orthogonal to $\vec v$. Verify that the two components sum to $\vec u$ and that the orthogonal piece really is orthogonal to $\vec v$.

---

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|---|---|
| 1 | $90-12=78$ | Multiplying corresponding entries but then multiplying the two results together (or adding the wrong pairs) instead of summing the products. |
| 2 | $\|\vec v\| = \sqrt{1+4+9} = \sqrt{14}$ | Forgetting the square root at the end and reporting $14$; or writing $\vec v \cdot \vec v$ as a vector instead of a scalar. |
| 3 | Dot product $= -5+0-3=-8 < 0$, so the angle is **greater than** $90^\circ$ | Assuming a negative dot product means the vectors are orthogonal (rather than obtuse) — orthogonal specifically requires the dot product to equal exactly $0$, not merely be negative. |
| 4 | $\pm\left(\dfrac{2}{\sqrt5},\dfrac{-1}{\sqrt5}\right)$ | Finding a correct orthogonal vector (e.g. $(2,-1)$ or $(-2,1)$) but forgetting to divide by its length to make it a *unit* vector. |
| 5 | $\vec n = \begin{bmatrix}-2\\1\end{bmatrix}$ (or any nonzero scalar multiple); $\ell_1: \vec n\cdot\vec x=0$; $\ell_2: \vec n\cdot(\vec x-\vec p)=0$ | Using a different normal vector for $\ell_1$ than for $\ell_2$, not realizing that translating a line does not change its normal vector — only the $\vec p$ in the normal-form equation changes. |
| 6 | $\vec d_1=(-2,3,0)$, $\vec d_2=(-2,0,-1)$; vector form $\vec x=t(-2,3,0)+s(-2,0,-1)+(2,0,0)$; normal vector $\vec n=(3,2,-6)$; normal form $(3,2,-6)\cdot(\vec x-(2,0,0))=0$ (equivalently $3x+2y-6z=6$) | Trying to spot the normal vector "by inspection" without checking it against *both* direction vectors — a guessed vector that is only orthogonal to $\vec d_1$ (not $\vec d_2$) is not a valid normal vector. |
| 7 | Normal form $(1,-1,0)\cdot(\vec x-(1,2,3))=0$; scalar form $x-y=-1$; vector form $\vec x=t(1,1,0)+s(0,0,1)+(1,2,3)$ | After expanding to scalar form, forgetting the plane has only *one* linear equation in three unknowns (so two free parameters are needed for vector form), and instead treating it like a line with a single parameter. |
| 8 | $\operatorname{proj}_\ell\vec v = \dfrac{2}{5}\begin{bmatrix}2\\1\end{bmatrix}=\begin{bmatrix}4/5\\2/5\end{bmatrix}$ | Using the vector component shortcut correctly here (fine, since $\ell$ is a span) but then trying to reuse the exact same shortcut in Problem 9, where the line does not pass through the origin. |
| 9 | Solving $(\vec c-\operatorname{proj}_K\vec c)\cdot(1,2)=0$ together with $\operatorname{proj}_K\vec c \in K$ gives $t=6/5$ and $\operatorname{proj}_K\vec c = \begin{bmatrix}11/5\\12/5\end{bmatrix}$ | Applying $\operatorname{vcomp}_{(1,2)}\vec c$ directly as if it were the projection, without noticing $K$ is translated away from the origin by $(1,0)$ — the vector-component shortcut only applies to spans. |
| 10 | (a) $\operatorname{vcomp}_{\vec b}\vec a$ must be (i) a scalar multiple of $\vec b$, and (ii) such that $\vec a - \operatorname{vcomp}_{\vec b}\vec a$ is orthogonal to $\vec b$. (b) Writing $\operatorname{vcomp}_{\vec b}\vec a = k\vec b$ and solving $\vec b\cdot(\vec a-k\vec b)=0$ for $k$ gives $k=\dfrac{\vec b\cdot\vec a}{\vec b\cdot\vec b}$, so $\operatorname{vcomp}_{\vec b}\vec a = \left(\dfrac{\vec b\cdot\vec a}{\vec b\cdot\vec b}\right)\vec b$ | Stating only one of the two conditions (usually just "it's a multiple of $\vec b$") and forgetting the orthogonality condition is what actually pins down the scalar $k$. |
| 11 | $\operatorname{proj}_{\operatorname{span}\{\vec d\}}\vec u = \operatorname{vcomp}_{\vec d}\vec u = \dfrac{9}{18}\begin{bmatrix}3\\3\end{bmatrix}=\begin{bmatrix}3/2\\3/2\end{bmatrix}$; $\operatorname{vcomp}_{-\vec d}\vec u = \begin{bmatrix}3/2\\3/2\end{bmatrix}$, the **same** vector, because $\operatorname{span}\{\vec d\}=\operatorname{span}\{-\vec d\}$ and the two sign flips in the formula $\left(\dfrac{(-\vec d)\cdot\vec u}{(-\vec d)\cdot(-\vec d)}\right)(-\vec d)$ cancel out | Assuming that flipping the sign of the vector you're projecting onto must flip the sign of the answer, without actually tracking how the $(-1)$ appears three times in the formula and cancels. |
| 12 | $\operatorname{vcomp}_{\vec v}\vec u = \dfrac{7}{10}\begin{bmatrix}1\\3\end{bmatrix}=\begin{bmatrix}7/10\\21/10\end{bmatrix}$; orthogonal piece $=\begin{bmatrix}33/10\\-11/10\end{bmatrix}$; both check out ($\vec v\cdot(\text{orthogonal piece})=0$ and the two pieces sum to $(4,1)$) | Computing $\operatorname{vcomp}_{\vec v}\vec u$ correctly but then subtracting in the wrong order ($\vec v - \vec u$ style, or subtracting $\vec v$ instead of $\vec u$) when finding the orthogonal piece, instead of $\vec u - \operatorname{vcomp}_{\vec v}\vec u$. |
