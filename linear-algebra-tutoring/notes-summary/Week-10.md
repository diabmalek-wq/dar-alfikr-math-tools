# Week 10: Determinants and Change of Bases

## Big idea
The determinant is the unique alternating, multilinear function of the rows of a square matrix with value $1$ at $I$, and it decides invertibility. It also measures signed area and volume scaling and gives Cramer's rule for solving systems.

## Definitions
- **Multilinear**: linear in each of its $n$ inputs.
- **Alternating**: swapping two entries changes the sign of the output.
- **Diagonal matrix**: $D=[d_{ij}]$ with $d_{ij}=0$ whenever $i\neq j$.
- **$ij$-minor $M_{ij}$**: the $(n-1)\times(n-1)$ matrix obtained by deleting row $i$ and column $j$ of $M$.
- **Determinant**: the alternating, multilinear function $\det:M_{n\times n}(\mathbb R)\to\mathbb R$ (inputs are rows $R_1,\dots,R_n$) with $\det(I)=1$.
- **$n$-area / $n$-volume**: the size of the parallelotope spanned by $n$ vectors. For $\vec v_1,\dots,\vec v_n\in\mathbb R^n$ it equals $|\det(\vec v_1,\dots,\vec v_n)|$.
- **Determinant of a linear map**: the determinant of any matrix representation of $T$.

## Theorems and results
- **Dependent or repeated inputs.** An alternating multilinear function outputs $0$ if two inputs are equal, and also if the inputs are linearly dependent. *Idea:* swapping equal entries gives $T=-T$, so $2T=0$. For dependence, expand the redundant vector by multilinearity; every term has a repeated input.
- **Diagonal.** $\det D=d_{11}d_{22}\cdots d_{nn}$.
- **Row operations.** Scaling a row by $\lambda$ multiplies $\det$ by $\lambda$. Swapping two rows multiplies $\det$ by $-1$. Adding a multiple of one row to another leaves $\det$ unchanged.
- **Invertibility.** $M$ is invertible iff $\det M\neq 0$. If $M$ is not invertible, its rows are dependent and $\det M=0$. If $M$ is invertible, Gauss–Jordan reduction gives $\det M\neq 0$.
- **Expansion.** For any fixed row $i$: $\det M=\sum_j(-1)^{i+j}m_{ij}\det M_{ij}$. The column version also holds, and every choice of row or column gives the same value.
- **Transpose.** $\det A=\det A^T$ (proof left as exercise).
- **Area scaling.** For $T:\mathbb R^n\to\mathbb R^n$, $|\det(T\vec v_1,\dots,T\vec v_n)|=|\det[T]|\cdot|\det(\vec v_1,\dots,\vec v_n)|$. In $\mathbb R^2$ the signed area of the parallelogram on $(a,c)$ and $(b,d)$ is $ad-bc$ (proved in the notes for a special case).
- **Cramer's rule.** If $\det A\neq 0$, the solution of $A\vec x=\vec b$ has $x_j=\dfrac{\det A_j}{\det A}$, where $A_j$ is $A$ with column $j$ replaced by $\vec b$.

## Techniques / procedures
1. **Row expansion:** choose a row, compute $\sum_j(-1)^{i+j}m_{ij}\det M_{ij}$, and recurse on the minors.
2. **Row reduction:** reduce $M$ toward $I$, track the scalar each operation contributes, and combine them with $\det I=1$.
3. **Small cases:** $\det[a]=a$ and $\det\begin{pmatrix}a&b\\c&d\end{pmatrix}=ad-bc$.
4. **Cramer's rule:** compute $\det A$; for each $j$ form $A_j$; set $x_j=\det A_j/\det A$.
5. **Area of a parallelotope:** take $|\det|$ of the matrix whose columns are the edge vectors.

## Worked examples in the notes
- $\det\begin{pmatrix}1&0&-1\\2&2&3\\3&1&4\end{pmatrix}$ $\to$ expand along row 1 $\to$ $5+4=9$ $\to$ nonzero, so invertible.
- $\det\begin{pmatrix}a&b\\c&d\end{pmatrix}$ $\to$ multilinearity on $\vec e_1,\vec e_2$ $\to$ $ad-bc$.
- $T(x,y)=(x+2y,2x+y)$ (matrix as read from scan) $\to$ $|\det|=|-3|=3$, so the unit square maps to area $3$.
- $T(x,y)=(x,0)$ $\to$ the square collapses to a segment $\to$ area $0$ and $\det=0$.
- A $2\times2$ system solved by Cramer's rule $\to$ $[x,y]^T=[0,-\tfrac12]^T$ (coefficients partly [unclear in scan]).

## Common pitfalls
- The determinant does change under row operations; "row operation invariance" is "not quite right", but the changes are simple and predictable.
- Row reduction and recursive expansion are costly and numerically unstable.
- Cramer's rule applies only when $\det A\neq 0$.
- The determinant of a linear map is computed from a matrix representation of it.
