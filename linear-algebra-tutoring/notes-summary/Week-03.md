# Week 3: Systems of Linear Equations, Augmented Matrices, Row Echelon Form and Row Reduced Echelon Form

## Big idea
Linear systems are encoded as augmented matrices and solved by elementary row operations, which preserve the solution set and produce REF or RREF. The solution set is empty, a single point, or an affine set $p+\operatorname{span}(S)$.

## Definitions
- Linear system: $n$ equations in $k$ variables. A solution is a $k$-tuple satisfying all equations simultaneously. Equivalent systems have the same solution set.
- Homogeneous: every right-hand constant is zero.
- Augmented matrix: $[A\mid b]$.
- Elementary row operations: $R_i+\lambda R_j\to R_i$ ($i\neq j$); $\lambda R_i\to R_i$ ($\lambda\neq0$); $R_i\leftrightarrow R_j$.
- REF: (1) the first nonzero entry of each nonzero row is its pivot, in column $j(i)$; (2) zeros lie below each pivot; (3) $j(i)<j(i+1)$ for consecutive nonzero rows (staircase).
- RREF: REF, with every pivot equal to $1$ and zeros above each pivot too.
- Basic variables: variables in pivot columns. Free variables: all others.
- Affine set: $p+\operatorname{span}(S)$ for a fixed vector $p$.

## Theorems and results
- Finitely many elementary row operations produce an equivalent system.
- Every linear system has a unique RREF (proof left as an exercise).
- A homogeneous system always has the trivial solution $0$.
- If $n<k$, every homogeneous system with $k$ variables and $n$ equations has a nontrivial solution. Proof idea: basic variables number at most $n$, so at least $k-n\geq1$ variables are free.
- If $v_p$ solves $[A\mid b]$, the solution set is $\{v_p+\theta:\theta\text{ solves }[A\mid0]\}$ (accepted as fact this week).
- A system has no solution, exactly one, or infinitely many.

## Techniques / procedures
1. Gaussian elimination: for each column, bring a nonzero entry at or below the current row into the pivot position, then clear the entries below it.
2. Gauss–Jordan: as above, also scale each pivot to $1$ and clear the entries above it.
3. Back substitution: solve the last nonzero equation first, with free variables as parameters $s_i$.
4. Particular plus homogeneous: reduce to $[A'\mid b']$; set free variables to $0$ for $v_p$; solve $[A'\mid0]$ for the homogeneous set.
5. Dependence test: put the vectors as columns of a homogeneous system; only the trivial solution means independent.
6. Writing $W$ as a span: write the constraints as a homogeneous system, reduce to RREF, solve for basic variables, and factor out the free parameters.

## Worked examples in the notes
- $\begin{pmatrix}1&0&1\\2&-1&1\\3&0&0\end{pmatrix}$ (columns $(1,2,3),(0,-1,0),(1,1,0)$) $\to$ row reduce to $I_3$ $\to$ independent.
- Is $f=2x+2\in\operatorname{span}\{x^2+1,\,x^2-1\}$? $\to$ coefficient matching gives $c_1+c_2=0$, $0=2$, $c_1-c_2=2$ $\to$ inconsistent $\to$ $f\notin\operatorname{span}$.
- $\begin{pmatrix}1&2&0&3\mid3\\2&4&0&6\mid6\\1&1&4&3\mid5\end{pmatrix}$ $\to$ Gauss–Jordan to $\begin{pmatrix}1&0&8&3\mid7\\0&1&-4&0\mid-2\end{pmatrix}$ $\to$ $(7,-2,0,0)+s_1(-8,4,1,0)+s_2(-3,0,0,1)$.
- $W=\left\{\begin{pmatrix}a&b\\c&d\end{pmatrix}: a+2b+3c=0,\ a+b+c=0\right\}$ $\to$ RREF gives $a-c=0$, $b+2c=0$ $\to$ $W=\operatorname{span}\left\{\begin{pmatrix}1&-2\\1&0\end{pmatrix},\begin{pmatrix}0&0\\0&1\end{pmatrix}\right\}$.
- $a+b=3$, $b+2c+d=6$, $d=5$ $\to$ back substitution $\to$ $(2,1,0,5)+s(2,-2,1,0)$.
- Is $(1,i)\in\operatorname{span}\{(1,1),(1,2)\}$ over $\mathbb{C}$? (Target OCR-garbled; read as $(1,i)$.) $\to$ $x_1+x_2=1$, $x_1+2x_2=i$ $\to$ $(2-i,\,i-1)$ $\to$ yes.

## Common pitfalls
- Swapping rows gives an equivalent system; swapping columns (variables) generally does not.
- The homogeneous solution set decides uniqueness; existence needs a particular solution.
- For $b\neq0$, the graph of $y=mx+b$ is affine, not a subspace; for $b=0$ it is $\operatorname{span}\{(1,m)\}$.
- Affine representations $p+\operatorname{span}(S)$ are not unique.
