# Week 3 — Systems of Linear Equations I & II

**Session length:** 3 hours
**Source:** Siefken, *MAT223 Workbook*, Appendix 1 (Systems of Linear Equations I) and Appendix 2 (Systems of Linear Equations II)

---

## Page 1 — Introduction, Key Facts & Definitions

### Why this matters

An equation encodes a precise relationship between quantities. A single linear equation rarely pins down its variables completely, but a **system** of several linear equations — several relationships holding simultaneously — often does. Vector equations (like "is $\vec w$ a linear combination of $\vec u$ and $\vec v$?") always translate, coordinate by coordinate, into a system of linear equations, and vice versa. Unlike general equations (there is no guarantee an arbitrary equation like $x^4 - e^x + 7 = 0$ has a solution), for systems of *linear* equations there is an algorithm — row reduction — that always tells us whether a solution exists and, if so, what it is. (Appendix 1)

### Definition: Linear Equation & System of Linear Equations (Appendix 1)

A **linear equation** in the variables $x_1, \ldots, x_n$ is one that can be expressed as
$$a_1 x_1 + a_2 x_2 + \cdots + a_n x_n = c$$
for constants $a_1, \ldots, a_n$ and $c$. A **system of linear equations** is a system of equations consisting of one or more linear equations.

Every vector equation, written in coordinates, corresponds to an equivalent system of linear equations, and every system of linear equations corresponds to a vector equation.

### Definition: Solution Set (Appendix 1)

A **solution** to an equation (or system of equations) is a particular choice of values for the variables that satisfies (makes true) the equation (or every equation in the system). The **solution set**, also called the **complete solution**, is the set of *all* possible solutions.

### Definition: Consistent & Inconsistent (Appendix 1)

A system of equations is **consistent** if it has at least one solution, i.e. its solution set is non-empty. Otherwise it is **inconsistent** (solution set is $\{\}$, the empty set).

### Definition: Equivalent Systems (Appendix 1)

Two equations or systems of equations are **equivalent** if they have the same solution set. "Doing algebra" to a system means manipulating it into an easier-to-read *equivalent* system.

### Definition: Augmented Matrix (Appendix 1)

An **augmented matrix** packages a system's information into a grid of numbers: the coefficients of the variables, together with the constants on the right-hand side of each equation, with an optional vertical line separating the two. For example,
$$\begin{cases} -2r + 2s + t = -15 \\ -5r + s + 2t = -21 \\ r - 4s + t = 18 \end{cases} \quad \longleftrightarrow \quad \begin{bmatrix} 1 & 2 & -2 & -15 \\ 2 & 1 & -5 & -21 \\ 1 & -4 & 1 & 18 \end{bmatrix}.$$
(Notice the columns list the coefficients of $r, s, t$ in that order, then the constants — the variable names themselves are dropped, since the column position tells us which variable a number belongs to.)

### The Three Elementary Row Operations (Appendix 1)

Row reduction (also called Gaussian elimination or Gauss–Jordan elimination) solves a system by manipulating its augmented matrix using the **elementary row operations**:

- **Swap** two rows: $R_i \leftrightarrow R_j$.
- **Scale** a row by a non-zero scalar: $R_i \leftarrow k R_i$ ($k \neq 0$).
- **Add a multiple of one row to another**: $R_i \leftarrow R_i + k R_j$.

Every elementary row operation can be undone (e.g. $R_i \leftarrow k R_i$ is undone by $R_i \leftarrow \dfrac{1}{k} R_i$), which is exactly why applying one to a system is guaranteed to produce an *equivalent* system.

### Strategy for Solving a System (Appendix 1)

1. Rewrite the system as an augmented matrix.
2. Use elementary row operations to zero out the lower triangle of the augmented matrix.
3. Convert the matrix back to a system of equations.
4. Read off the solution (substituting where necessary).

### Definition: Reduced Row Echelon Form — RREF (Appendix 2)

A matrix is in **reduced row echelon form (rref)** if:

- The first non-zero entry in every row is a $1$; these entries are called **pivots** or **leading ones**.
- Above and below each leading one are zeros.
- The leading ones form an echelon (staircase) pattern: if row $i$ has a leading one, every leading one in a row $j > i$ appears strictly to the right of row $i$'s leading one.
- All rows of zeros occur at the bottom of the matrix.

Columns containing pivots are called **pivot columns**. (If the matrix is augmented, the augmented column is *not* called a pivot column, even if it happens to contain a pivot in that last row.) Every matrix has a **unique** reduced row echelon form, written $\operatorname{rref}(M)$.

### The Row Reduction Algorithm (Appendix 2)

Given a matrix $M$:

1. If $M$'s first column is all zeros, apply the algorithm to the submatrix obtained by ignoring that column.
2. Otherwise, row-swap (if needed) so the upper-left entry is non-zero.
3. Let $\alpha$ be the upper-left entry. Apply $R_1 \leftarrow \dfrac{1}{\alpha} R_1$ so the upper-left entry becomes the pivot, $1$.
4. Use operations $R_i \leftarrow R_i + \beta R_1$ to zero every entry *below* the pivot.
5. Apply the algorithm to the remaining submatrix (ignoring the pivot row and pivot column).
6. Once every pivot is in place (this is called **pre**-reduced row echelon form), zero out every entry *above* each pivot using operations $R_i \leftarrow R_i + \beta R_j$. This last step produces full reduced row echelon form.

### Free Variables and the Complete Solution (Appendix 2)

Once a system's augmented matrix is in rref, every **non-pivot, non-augmented column** is called a **free variable column**. For each free variable column, introduce an arbitrary equation such as $x_i = t$ (the variable is now called a **free variable** and $t$ a **parameter** — it may be *any* real number and still yields a valid solution). Substituting back through the remaining rows expresses every other variable in terms of the parameter(s), giving the **complete solution** in vector form:
$$\vec x = t\,\vec d_1 + s\,\vec d_2 + \cdots + \vec p.$$
If a system needs a free variable/parameter to describe its complete solution, it necessarily has **infinitely many** solutions (one for every choice of the parameter).

### Theorem: The Number of Solutions (Appendix 2)

A system of linear equations always has **0, 1, or infinitely many** solutions — never, say, exactly two. Whether a system falls into each case is read off from its rref exactly as follows:

| Consistent? | Pivots | Number of Solutions |
|---|---|---|
| False | At least one (non-augmented) column lacks a pivot | $0$ |
| True | Every (non-augmented) column has a pivot | $1$ |
| True | At least one (non-augmented) column lacks a pivot | Infinitely many |

**Caution.** A missing pivot column does *not* by itself mean infinitely many solutions — you must first check the system is consistent. For example, $\begin{bmatrix} 1 & 2 & -1 \\ 0 & 0 & 0 \end{bmatrix}$ has infinitely many solutions (column 2 has no pivot, and the system is consistent), but $\begin{bmatrix} 1 & 2 & 0 \\ 0 & 0 & 1 \end{bmatrix}$ has *no* solutions at all: its second row reads $0x + 0y = 1$, which is never true, even though column 2 also lacks a pivot. Always check the augmented column for a row of the form $[0 \ 0 \ \cdots \ 0 \mid k]$ with $k \neq 0$ — that row alone makes the system inconsistent, regardless of any free variable columns elsewhere.

### The Geometry of Solution Sets (Appendix 2)

Each individual linear equation, viewed in isolation, specifies a geometric object called a **hyperplane** (a line in $\mathbb{R}^2$, a plane in $\mathbb{R}^3$, and so on — always one dimension less than the ambient space, with one exception: the trivial equation $0x_1 + \cdots + 0x_n = 0$, whose solution set is everything). A solution to a *system* of equations is a point lying in the intersection of all these hyperplanes simultaneously. In $\mathbb{R}^2$, two lines can only meet in a point, a (shared) line, or nowhere — matching exactly the three possible outcomes: one solution, infinitely many solutions, or no solution.

---

## Pages 2–3 — Solved Examples

**Example 1 (A $2\times2$ system with a unique solution).** Solve
$$\begin{cases} x - 2y = 0 \\ x + y = 3 \end{cases}.$$

We rewrite the system as an augmented matrix and row reduce.
$$\begin{bmatrix} 1 & -2 & 0 \\ 1 & 1 & 3 \end{bmatrix} \xrightarrow[\text{(eliminate } x \text{ below row 1)}]{R_2 \leftarrow R_2 - R_1} \begin{bmatrix} 1 & -2 & 0 \\ 0 & 3 & 3 \end{bmatrix} \xrightarrow[\text{(make the row-2 pivot a 1)}]{R_2 \leftarrow \frac{1}{3}R_2} \begin{bmatrix} 1 & -2 & 0 \\ 0 & 1 & 1 \end{bmatrix} \xrightarrow[\text{(zero above the row-2 pivot)}]{R_1 \leftarrow R_1 + 2R_2} \begin{bmatrix} 1 & 0 & 2 \\ 0 & 1 & 1 \end{bmatrix}.$$

Every column (other than the augmented column) has a pivot, so this system has a unique solution: $x = 2$, $y = 1$. Geometrically, this is exactly the point where the lines $x - 2y = 0$ and $x + y = 3$ cross.

**Example 2 (A $3\times3$ system with a unique solution, carried all the way to rref).** Solve
$$\begin{cases} a + 3b + 2c = 1 \\ 2a + 7b + 5c = 2 \\ -a - 4b = 11 \end{cases}.$$

$$\begin{bmatrix} 1 & 3 & 2 & 1 \\ 2 & 7 & 5 & 2 \\ -1 & -4 & 0 & 11 \end{bmatrix} \xrightarrow[\text{(eliminate }a\text{ from row 2)}]{R_2 \leftarrow R_2 - 2R_1} \begin{bmatrix} 1 & 3 & 2 & 1 \\ 0 & 1 & 1 & 0 \\ -1 & -4 & 0 & 11 \end{bmatrix} \xrightarrow[\text{(eliminate }a,b\text{ from row 3)}]{R_3 \leftarrow R_3 + R_1 + R_2} \begin{bmatrix} 1 & 3 & 2 & 1 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 3 & 12 \end{bmatrix}.$$

At this point every row is easy to solve by substitution, but let's continue to full rref instead.
$$\xrightarrow[\text{(make the row-3 pivot a 1)}]{R_3 \leftarrow \frac{1}{3}R_3} \begin{bmatrix} 1 & 3 & 2 & 1 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 4 \end{bmatrix} \xrightarrow[\text{(zero above the row-3 pivot in row 2)}]{R_2 \leftarrow R_2 - R_3} \begin{bmatrix} 1 & 3 & 2 & 1 \\ 0 & 1 & 0 & -4 \\ 0 & 0 & 1 & 4 \end{bmatrix} \xrightarrow[\text{(zero above the remaining pivots in row 1)}]{R_1 \leftarrow R_1 - 3R_2 - 2R_3} \begin{bmatrix} 1 & 0 & 0 & 5 \\ 0 & 1 & 0 & -4 \\ 0 & 0 & 1 & 4 \end{bmatrix}.$$

Every column has a pivot, so the solution is unique and can be read off directly: $a = 5$, $b = -4$, $c = 4$. The solution set is $\left\{\begin{bmatrix} 5 \\ -4 \\ 4 \end{bmatrix}\right\}$.

**Example 3 (A $4$-equation, $3$-unknown system — a redundant row does not spoil uniqueness).** Solve
$$\begin{cases} 13r + s + 3t = -2 \\ 5r + t = 1 \\ -6r + s - t = -8 \\ 4r + s + t = -6 \end{cases}.$$

Following Siefken's own presentation, we order the augmented matrix's columns as $t, s, r$ (rather than $r,s,t$) purely because this ordering happens to put a coefficient of $1$ in an early row, saving work — the system itself is unchanged.
$$\begin{bmatrix} 3 & 1 & 13 & -2 \\ 1 & 0 & 5 & 1 \\ -1 & 1 & -6 & -8 \\ 1 & 1 & 4 & -6 \end{bmatrix} \xrightarrow[\text{(bring a leading 1 to the top)}]{R_1 \leftrightarrow R_2} \begin{bmatrix} 1 & 0 & 5 & 1 \\ 3 & 1 & 13 & -2 \\ -1 & 1 & -6 & -8 \\ 1 & 1 & 4 & -6 \end{bmatrix} \xrightarrow[\text{(eliminate col. 1 from row 2)}]{R_2 \leftarrow R_2 - 3R_1} \begin{bmatrix} 1 & 0 & 5 & 1 \\ 0 & 1 & -2 & -5 \\ -1 & 1 & -6 & -8 \\ 1 & 1 & 4 & -6 \end{bmatrix}.$$

$$\xrightarrow[\text{(eliminate col. 1–2 from row 3)}]{R_3 \leftarrow R_3 + R_1 - R_2} \begin{bmatrix} 1 & 0 & 5 & 1 \\ 0 & 1 & -2 & -5 \\ 0 & 0 & 1 & -2 \\ 1 & 1 & 4 & -6 \end{bmatrix} \xrightarrow[\text{(eliminate col. 1–2 from row 4)}]{R_4 \leftarrow R_4 - R_1 - R_2} \begin{bmatrix} 1 & 0 & 5 & 1 \\ 0 & 1 & -2 & -5 \\ 0 & 0 & 1 & -2 \\ 0 & 0 & 1 & -2 \end{bmatrix} \xrightarrow[\text{(row 4 is now a repeat of row 3)}]{R_4 \leftarrow R_4 - R_3} \begin{bmatrix} 1 & 0 & 5 & 1 \\ 0 & 1 & -2 & -5 \\ 0 & 0 & 1 & -2 \\ 0 & 0 & 0 & 0 \end{bmatrix}.$$

The bottom row reads $0 = 0$ — it is *redundant* (it carried no new information), not a sign of inconsistency, because the augmented entry in that row is also $0$. Every remaining (non-augmented) column has a pivot, so the system is consistent with a unique solution. Reading off: $r = -2$; substituting into row 2 gives $s - 2(-2) = -5 \Rightarrow s = -9$; substituting into row 1 gives $t + 5(-2) = 1 \Rightarrow t = 11$. The solution set is $\left\{\begin{bmatrix} t \\ s \\ r\end{bmatrix} = \begin{bmatrix} 11 \\ -9 \\ -2 \end{bmatrix}\right\}$.

**Example 4 (An inconsistent $2\times2$ system).** Solve
$$\begin{cases} x + y = 1 \\ 4x + 4y = 7 \end{cases}.$$

$$\begin{bmatrix} 1 & 1 & 1 \\ 4 & 4 & 7 \end{bmatrix} \xrightarrow[\text{(eliminate }x\text{ from row 2)}]{R_2 \leftarrow R_2 - 4R_1} \begin{bmatrix} 1 & 1 & 1 \\ 0 & 0 & 3 \end{bmatrix}.$$

The second row corresponds to $0x + 0y = 3$, which is true for *no* choice of $x$ and $y$. The system is **inconsistent**; its solution set is $\{\}$, the empty set. (This makes sense: $4x+4y=7$ says $x+y = 1.75$, which directly contradicts $x+y=1$.)

**Example 5 (An inconsistent $3\times3$ system).** Solve
$$\begin{cases} x + z = 4 \\ x + y + 2z = -8 \\ x + 3y + 4z = -18 \end{cases}.$$

$$\begin{bmatrix} 1 & 0 & 1 & 4 \\ 1 & 1 & 2 & -8 \\ 1 & 3 & 4 & -18 \end{bmatrix} \xrightarrow[\text{(eliminate row 3's leading term using row 2)}]{R_3 \leftarrow R_3 - R_2} \begin{bmatrix} 1 & 0 & 1 & 4 \\ 1 & 1 & 2 & -8 \\ 0 & 2 & 2 & -10 \end{bmatrix} \xrightarrow[\text{(eliminate }x\text{ from row 2)}]{R_2 \leftarrow R_2 - R_1} \begin{bmatrix} 1 & 0 & 1 & 4 \\ 0 & 1 & 1 & -12 \\ 0 & 2 & 2 & -10 \end{bmatrix} \xrightarrow[\text{(eliminate }y\text{ from row 3)}]{R_3 \leftarrow R_3 - 2R_2} \begin{bmatrix} 1 & 0 & 1 & 4 \\ 0 & 1 & 1 & -12 \\ 0 & 0 & 0 & 14 \end{bmatrix}.$$

The last row says $0x + 0y + 0z = 14$, never true. The system is **inconsistent**; its solution set is $\{\}$. Note the trap: column 3 also lacks a pivot, but that is irrelevant here — the augmented entry $14$ in an all-zero row is what actually decides the outcome (see the Caution on Page 1).

**Example 6 (Infinitely many solutions — one free variable).** Solve
$$\begin{cases} x + 3y = 2 \\ 2x + 6y = 4 \end{cases}.$$

$$\begin{bmatrix} 1 & 3 & 2 \\ 2 & 6 & 4 \end{bmatrix} \xrightarrow[\text{(row 2 is exactly } 2\times\text{ row 1)}]{R_2 \leftarrow R_2 - 2R_1} \begin{bmatrix} 1 & 3 & 2 \\ 0 & 0 & 0 \end{bmatrix}.$$

The system is consistent ($0=0$ carries no contradiction), but column 2 has no pivot — a free variable column. Introduce the arbitrary equation $y = t$ (any real number $t$). Substituting into row 1: $x = 2 - 3t$. The complete solution, in vector form, is
$$\vec x = \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 2 - 3t \\ t \end{bmatrix} = t\begin{bmatrix} -3 \\ 1 \end{bmatrix} + \begin{bmatrix} 2 \\ 0 \end{bmatrix},$$
which traces out the line $x + 3y = 2$ as $t$ ranges over all of $\mathbb{R}$.

**Example 7 (Infinitely many solutions — two free variables, one variable that never appears).** Consider the system in the variables $x, y, z, w$:
$$\begin{cases} -2w = -2 \\ 3w + y + 2z = 2 \\ 5w + 2y + 4z = 3 \end{cases}.$$

Notice $x$ has coefficient $0$ in every equation, so the augmented matrix's first column (ordering variables as $x,y,z,w$) is entirely zero from the start:
$$M = \begin{bmatrix} 0 & 0 & 0 & -2 & -2 \\ 0 & 1 & 2 & 3 & 2 \\ 0 & 2 & 4 & 5 & 3 \end{bmatrix}.$$

Per the row reduction algorithm, a zero column is simply skipped, so we work on the submatrix starting at column 2.
$$\xrightarrow[\text{(bring a non-zero entry to the working corner)}]{R_1 \leftrightarrow R_2} \begin{bmatrix} 0 & 1 & 2 & 3 & 2 \\ 0 & 0 & 0 & -2 & -2 \\ 0 & 2 & 4 & 5 & 3 \end{bmatrix} \xrightarrow[\text{(eliminate col. 2 from row 3)}]{R_3 \leftarrow R_3 - 2R_1} \begin{bmatrix} 0 & 1 & 2 & 3 & 2 \\ 0 & 0 & 0 & -2 & -2 \\ 0 & 0 & 0 & -1 & -1 \end{bmatrix}.$$

Column 3 is now all zero in the remaining submatrix, so we skip to column 4:
$$\xrightarrow[\text{(make the row-2 pivot a 1)}]{R_2 \leftarrow -\frac{1}{2}R_2} \begin{bmatrix} 0 & 1 & 2 & 3 & 2 \\ 0 & 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & -1 & -1 \end{bmatrix} \xrightarrow[\text{(eliminate col. 4 from row 3)}]{R_3 \leftarrow R_3 + R_2} \begin{bmatrix} 0 & 1 & 2 & 3 & 2 \\ 0 & 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix} \xrightarrow[\text{(zero above the row-2 pivot)}]{R_1 \leftarrow R_1 - 3R_2} \begin{bmatrix} 0 & 1 & 2 & 0 & -1 \\ 0 & 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix} = \operatorname{rref}(M).$$

The pivot columns are column 2 ($y$) and column 4 ($w$); columns 1 ($x$) and 3 ($z$) are free variable columns. Introduce $x = t$ and $z = s$. Row 1 gives $y + 2z = -1 \Rightarrow y = -1-2s$; row 2 gives $w = 1$. The complete solution is
$$\begin{bmatrix} x \\ y \\ z \\ w \end{bmatrix} = \begin{bmatrix} t \\ -1-2s \\ s \\ 1 \end{bmatrix} = t\begin{bmatrix} 1 \\ 0 \\ 0 \\ 0 \end{bmatrix} + s\begin{bmatrix} 0 \\ -2 \\ 1 \\ 0 \end{bmatrix} + \begin{bmatrix} 0 \\ -1 \\ 0 \\ 1 \end{bmatrix}, \qquad s,t \in \mathbb{R}.$$

---

## Pages 4–5 — Practice Problems (unsolved)

**Setting Up Systems (Translating Equations)**

1. Convert the vector equation $x\begin{bmatrix} 1 \\ -1 \\ 0 \end{bmatrix} + y\begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} + z\begin{bmatrix} 4 \\ 6 \\ 1 \end{bmatrix} = \begin{bmatrix} 2 \\ -5 \\ 2 \end{bmatrix}$ into a system of linear equations, then solve it by row reduction.

**Systems with a Unique Solution**

2. Solve by row reduction: $\begin{cases} x + 2y = 8 \\ 3x - y = 3 \end{cases}$.
3. Write down the augmented matrix, use the row reduction algorithm to check consistency, and give the complete solution: $\begin{cases} -10x_1 - 4x_2 + 4x_3 = 28 \\ 3x_1 + x_2 - x_3 = -8 \\ x_1 + x_2 - \dfrac{1}{2}x_3 = -3 \end{cases}$.

**Systems with No Solution**

4. Solve by row reduction and identify the outcome: $\begin{cases} 2x - y = 4 \\ 6x - 3y = 5 \end{cases}$.
5. Solve by row reduction and identify the outcome: $\begin{cases} x + y + z = 2 \\ 2x + 2y + 2z = 5 \\ x - y + z = 0 \end{cases}$.

**Systems with Infinitely Many Solutions (write the parametric/vector-form answer)**

6. Find the complete solution of the single equation $2x - 4y = 6$ by introducing a free variable.
7. Find the complete solution: $\begin{cases} x + y + z = 1 \\ y - z = 2 \end{cases}$.
8. Find the complete solution: $\begin{cases} 0x + 0y + 0z = 0 \\ x + y + z = 3 \end{cases}$. (There should be *two* free variables here — think about why.)

**Applied Problem**

9. On Kokoro's farm there is a cage with $35$ animals, some chickens and some rabbits (each chicken has $2$ legs, each rabbit has $4$ legs). Kokoro counts $94$ legs in total. Set up a system of linear equations and solve it to find the number of chickens and the number of rabbits.
10. Kokoro now wants a cage with cats and dogs (each cat has $4$ legs and each dog has $4$ legs) so that there are $35$ animals in total and $94$ legs in total. Set up the corresponding system, and explain — using linear algebra, in complete sentences — whether such a cage is possible.

**Conceptual (True or False — justify every answer)**

11. "A system of linear equations with $4$ variables and $3$ equations is always consistent." True or false? Justify with an example or a short argument.
12. "There are $m, c \in \mathbb{R}$ so that the $y$-axis is the solution set of the equation $y = mx + c$." True or false? Justify your answer.

---

## Answer Key & Misconception Notes (for tutor use — do not show student until after attempt)

| # | Answer | Common misconception |
|---|---|---|
| 1 | System: $x + 4z = 2,\ -x+y+6z=-5,\ z=2$. Solving: $z=2 \Rightarrow x = -6 \Rightarrow y = -23$. Solution: $(x,y,z)=(-6,-23,2)$. | Reading coordinates off the vectors in the wrong order (row vs. column index), producing a transposed or scrambled system. |
| 2 | $\begin{bmatrix} 1 & 2 & 8 \\ 3 & -1 & 3 \end{bmatrix} \to \begin{bmatrix} 1 & 2 & 8 \\ 0 & -7 & -21 \end{bmatrix} \to (x,y) = (2,3)$. | Sign error performing $R_2 \leftarrow R_2 - 3R_1$: forgetting to distribute the $-3$ across every entry of $R_1$, including the constant column. |
| 3 | $\operatorname{rref}$ gives $(x_1,x_2,x_3) = (-2, 0, 2)$. | Mis-clearing a fraction like $-\dfrac{1}{2}x_3$: multiplying only the $x_3$ term by $2$ and forgetting to also double the other coefficients and the constant in that row. |
| 4 | Row reduces to $\begin{bmatrix} 2 & -1 & 4 \\ 0 & 0 & -7 \end{bmatrix}$: inconsistent, solution set $\{\}$. | Seeing the zero row of *coefficients* and concluding "infinitely many solutions" without checking that the augmented entry ($-7$) is non-zero. |
| 5 | Row reduces to a row $[0\ 0\ 0 \mid 1]$ (from $R_2 - 2R_1$): inconsistent, solution set $\{\}$, regardless of the third equation. | Trying to use the third equation to "rescue" the system, not realizing the first two equations alone already contradict each other. |
| 6 | Pivot on $x$: $x = 3 + 2t$, $y = t$, i.e. $\begin{bmatrix} x\\y\end{bmatrix} = t\begin{bmatrix}2\\1\end{bmatrix}+\begin{bmatrix}3\\0\end{bmatrix}$. | Forgetting to assign the free variable a parameter name at all, and instead leaving the answer as the single equation $2x-4y=6$ (that is a relationship, not a complete parametrized solution). |
| 7 | $\begin{bmatrix} x\\y\\z\end{bmatrix} = t\begin{bmatrix}-2\\1\\1\end{bmatrix}+\begin{bmatrix}-1\\2\\0\end{bmatrix}$. | Picking $y$ (a pivot column variable) as the "free" one instead of $z$ (the true non-pivot column), which produces an answer that looks plausible but doesn't match the rref's actual pivot structure. |
| 8 | Pivot on $x$ only; $y=s$, $z=t$ free: $\begin{bmatrix} x\\y\\z\end{bmatrix} = s\begin{bmatrix}-1\\1\\0\end{bmatrix}+t\begin{bmatrix}-1\\0\\1\end{bmatrix}+\begin{bmatrix}3\\0\\0\end{bmatrix}$. | Treating the trivial equation $0x+0y+0z=0$ as if it disqualifies the system or must be "solved," instead of recognizing it adds no information and should simply be dropped after noting it's consistent. |
| 9 | $c + r = 35,\ 2c+4r=94 \Rightarrow$ $23$ chickens, $12$ rabbits. | Swapping which variable gets the $2$ and which gets the $4$ in the legs equation, e.g. writing $4c+2r=94$. |
| 10 | $c+d=35,\ 4c+4d=94 \Rightarrow 4(35)=140 \neq 94$: inconsistent, **not possible**, no matter how the $35$ animals are split. | Trying to solve for specific values of $c$ and $d$ instead of noticing the two equations are proportional in their left-hand sides but not their right-hand sides, which is the actual source of inconsistency. |
| 11 | **False.** E.g. $x_1+x_2+x_3+x_4=0,\ x_1+x_2+x_3+x_4=1,\ 0=0$ has $4$ variables, $3$ equations, but the first two directly contradict each other. | Assuming "more variables than equations always means consistent, often with free variables" — that intuition only applies once you already know the system is consistent; it says nothing about consistency itself. |
| 12 | **False.** The equation $y=mx+c$ assigns exactly one $y$-value to each $x$-value, so its graph can never be a vertical line; the $y$-axis is the vertical line $x=0$ together with *every* $y$-value. | Confusing "the $y$-axis passes through $y$-values" with "the $y$-axis is a graph of the form $y=mx+c$" — missing that $y=mx+c$ form can only ever produce non-vertical lines. |
