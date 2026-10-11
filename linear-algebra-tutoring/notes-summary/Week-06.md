# Week 6: Linear Transformations, Coordinate Vectors and Matrix Representations

## Big idea
A linear transformation $T:V\to W$ is a map that preserves addition and scalar multiplication. Once bases are fixed, $T$ is encoded by a matrix, so computing $T(v)$ becomes multiplying coordinate vectors by that matrix.

## Definitions
- **Linear transformation**: $T(u+v)=T(u)+T(v)$ and $T(av)=aT(v)$ for all $u,v\in V$, $a\in F$ (operations of $V$ on the left, of $W$ on the right).
- **Coordinate vector**: for a basis $\alpha=\{v_1,\dots,v_n\}$ and $v=\sum_i b_iv_i$, $[v]_\alpha=\begin{pmatrix}b_1\\ \vdots\\ b_n\end{pmatrix}$.
- **Matrix of $T$**: for bases $\alpha$ of $V$ and $\beta$ of $W$, $[T]^\beta_\alpha$ has $i$-th column $[T(v_i)]_\beta$.
- **Standard inner product**: $\langle u,v\rangle=\sum_i u_iv_i$; **length** $\|v\|=\sqrt{\langle v,v\rangle}$.
- **Orthogonal**: nonzero $u,v$ with $\langle u,v\rangle=0$.
- **Projection onto** $L=\operatorname{span}\{a\}$: $P_a(v)=\dfrac{\langle a,v\rangle}{\langle a,a\rangle}\,a$.

## Theorems and results
- For linear $T$: $T(0_V)=0_W$. *Idea:* $T(0_V)=T(0\cdot 0_V)=0\cdot T(0_V)=0_W$.
- $T$ is linear iff $T(au+bv)=aT(u)+bT(v)$ for all $u,v\in V$, $a,b\in F$.
- The zero and identity transformations are linear.
- If $S,T:V\to W$ are linear and agree on a basis, then $S=T$. *Idea:* write $v=\sum a_iv_i$ and apply linearity to both maps.
- A linear $T:V\to W$ with $\dim V=n$, $\dim W=k$ is uniquely determined by $nk$ scalars.
- For nonzero $u,v\in\mathbb R^n$: $\cos\theta=\dfrac{\langle u,v\rangle}{\|u\|\,\|v\|}$. *Idea:* expand $\|u-v\|^2$ with the inner product and compare with the law of cosines. Hence $u\perp v$ iff $\langle u,v\rangle=0$.
- **Coordinate formula**: $[T(v)]_\beta=[T]^\beta_\alpha[v]_\alpha$. *Idea:* expand $v=\sum_j a_jv_j$, apply linearity, and reorder finite sums.
- **Fundamental theorem** (proof postponed to the textbook): for $M\in M_{k\times n}(\mathbb R)$, $T_M(v)=w \iff M[v]_\alpha=[w]_\beta$ defines a linear map; every linear $T$ satisfies $T=T_{[T]}$, and $M=[T_M]$.

## Techniques / procedures
1. Prove linearity: check additivity and homogeneity separately, or check $T(au+bv)=aT(u)+bT(v)$ directly.
2. Build $[T]^\beta_\alpha$: compute each $T(v_i)$, write it in basis $\beta$, and place its coordinates in column $i$.
3. Find $[v]_\alpha$: solve $v=\sum_i b_iv_i$; the $b_i$ are the entries.
4. Compute $[T(v)]_\beta$ as $[T]^\beta_\alpha[v]_\alpha$: multiply each row of $[T]$ by the column $[v]_\alpha$.
5. Projection: solve $\langle a,\,v-ca\rangle=0$ for $c$, giving $c=\dfrac{\langle a,v\rangle}{\langle a,a\rangle}$.
6. Rotation: $R_\theta(e_1)=(\cos\theta,\sin\theta)$ and $R_\theta(e_2)=(-\sin\theta,\cos\theta)$ are the columns.

## Worked examples in the notes
- $T(x)=7x$ on $\mathbb R$ $\to$ check $T(u+v)$ and $T(au)$ separately using distributivity and commutativity $\to$ linear.
- $v=(2,0)$, $\alpha$ standard, $\beta=\{(1,1),(1,-1)\}$ $\to$ $[v]_\alpha=(2,0)^T$, $[v]_\beta=(1,1)^T$ (printed expansion garbled: [unclear in scan]).
- Identity from $\alpha=\{(0,1),(1,0)\}$ to $\beta=\{(1,1),(1,-1)\}$ $\to$ express each $\alpha$-vector in $\beta$ $\to$ columns $(\tfrac12,-\tfrac12)^T$ and $(\tfrac12,\tfrac12)^T$ (scan partly unclear).
- Rotation $R_\theta$ on $\mathbb R^2$ $\to$ columns from step 6 $\to$ $[R_\theta]=\begin{pmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{pmatrix}$ (printed matrix partly unclear; columns legible).
- Projection of $(4,3)$ onto $\operatorname{span}\{(1,0)\}$ $\to$ $\dfrac{\langle(1,0),(4,3)\rangle}{\langle(1,0),(1,0)\rangle}(1,0)$ $\to$ $(4,0)$.
- $T(x,y,z)=(x+y+z,\ y+z,\ z)$ on $\mathbb R^3$ $\to$ columns $[T(e_i)]$ $\to$ check $[T(1,2,3)]=[T]\,[(1,2,3)]$ $\to$ notes report agreement (some entries [unclear in scan]).
- $M=\begin{pmatrix}1&2&1\\0&1&0\\1&2&3\end{pmatrix}$ from $P_2(\mathbb R)$ (basis $1,x,x^2$) to $\mathbb R^3$ $\to$ $T_M(a_1+a_2x+a_3x^2)=(a_1+2a_2+a_3,\ a_2,\ a_1+2a_2+3a_3)$.

## Common pitfalls
- Writing $T(u+v)=T(u)+T(v)$ hides the fact that $V$ and $W$ may have different operations; track them separately.
- Coordinate vectors depend on the basis: $[v]_\alpha$ and $[v]_\beta$ are generally different.
