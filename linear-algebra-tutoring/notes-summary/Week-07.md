# Week 7: Kernel, Image and Inverse Image

## Big idea
The kernel, image and inverse image are natural subspaces attached to a linear map, and in finite dimensions they are computed by solving linear systems for the matrix representation. Rank-nullity links their dimensions: $\dim\ker T+\dim\operatorname{image}T=\dim V$.

## Definitions
- **Kernel**: $\ker(T)=\{v\in V : T(v)=0_W\}$.
- **Nullspace**: $\operatorname{nullspace}(A)=\{x : Ax=0\}$.
- **Image**: $\operatorname{image}(T)=\{w\in W : w=T(v)\text{ for some } v\in V\}$.
- **Column space**: $\operatorname{col}(A)=\operatorname{span}\{a_1,\dots,a_n\}$, where $a_i$ are the columns of $A$.
- **Inverse image**: $T^{-1}(S)=\{v\in V : T(v)\in S\}$; $T^{-1}(w)$ means $T^{-1}(\{w\})$.

## Theorems and results
- $\ker(T)$ and $\operatorname{image}(T)$ are subspaces (closure test). *Idea:* linearity gives $T(x+y)=0$ and $T(cx)=0$ for $x,y\in\ker T$; similarly for images.
- **Matrix form**: $v\in\ker T \iff [T]^\beta_\alpha[v]_\alpha=[0]_\beta$, so $\ker T$ corresponds to $\operatorname{nullspace}([T]^\beta_\alpha)$.
- If $\{v_i\}$ spans $V$, then $\{T(v_i)\}$ spans $\operatorname{image}(T)$. *Idea:* write $v=\sum a_iv_i$ and apply linearity.
- $\{[w_i]_\beta\}$ is a basis of $\operatorname{col}([T]^\beta_\alpha)$ iff $\{w_i\}$ is a basis of $\operatorname{image}(T)$ (proof left as exercise).
- Pivot columns of $A$ (the original columns, at positions of pivots in RREF) form a basis of $\operatorname{col}(A)$ (proof left as exercise).
- **Rank-nullity**: $\dim\ker T+\dim\operatorname{image}T=\dim V$. *Idea:* extend a basis of $\ker T$ to a basis of $V$; the images of the added vectors form a basis of $\operatorname{image}T$.
- If $Ax=b$ has a solution $x_p$, its full solution set is $x_p+\operatorname{nullspace}(A)$. *Idea:* the difference of two solutions lies in the nullspace.
- The solution set of $Ax=b$ is a subspace iff $b=0$. *Idea:* $0$ in the set forces $b=0$; if $b=0$ the set is the nullspace.

## Techniques / procedures
1. Show a set is a subspace: contains $0$ and is closed under addition and scalar multiplication.
2. Kernel: form $[T]^\beta_\alpha$; row-reduce $[\,[T]\mid 0\,]$; set each free variable to a parameter; write the solution as a combination; convert $(b_i)$ to $v=\sum b_iv_i$.
3. Image: take the pivot columns of $[T]$ and map them back to $W$ through $\beta$.
4. Solve $T(v)=w$: row-reduce $[\,[T]\mid[w]_\beta\,]$; then $T^{-1}(w)=\{v_p\}+\ker T$.
5. Check with rank-nullity: free variables count $\dim\ker T$, pivots count $\dim\operatorname{image}T$.

## Worked examples in the notes
- Projection onto the $z$-axis, $T_1:\mathbb R^3\to\mathbb R^3$ $\to$ $\ker T_1=\{(x,y,0)\}$, $\operatorname{image}T_1=\{(0,0,z)\}$ $\to$ $2+1=3$.
- Rotation by $\pi/2$, $R(x,y)=(-y,x)$, on $\mathbb R^2$ $\to$ $\ker=\{(0,0)\}$, image $=\mathbb R^2$ $\to$ $0+2=2$.
- $T:M_{2\times 2}(\mathbb R)\to P_2(\mathbb R)$ (formula partly [unclear in scan]) $\to$ reduced system $x_1+x_4=0$, $x_2-x_3=0$ $\to$ $\ker T$ basis $\{-E_{11}+E_{22},\ E_{12}+E_{21}\}$.
- Differentiation $D:P_3(\mathbb R)\to P_2(\mathbb R)$ $\to$ $[D]$ has pivots in the columns for $x,x^2,x^3$ $\to$ image basis $\{1,2x,3x^2\}$, kernel basis $\{1\}$.
- $T(x,y)=(x-y,\ x-y)$ on $\mathbb R^2$ $\to$ $\ker T=\operatorname{span}\{(1,1)\}$; $T^{-1}(2,2)=(2,0)+\operatorname{span}\{(1,1)\}$; $T^{-1}(2,0)=\varnothing$ (inconsistent system).
- $T:P_2(\mathbb R)\to\mathbb R^3$, $T(p)=(p(0),p(1),p(2))$ $\to$ solve $[T][p]=[(1,2,4)]$ $\to$ unique solution $p(x)=1+\tfrac12x+\tfrac12x^2$.
- $A=\begin{pmatrix}1&1&1\\0&0&1\end{pmatrix}$, $b=(1,3)^T$ $\to$ $x_p=(-2,0,3)^T$, $\operatorname{nullspace}(A)=\operatorname{span}\{(-1,1,0)^T\}$ (scan partly unclear).

## Common pitfalls
- $T^{-1}(S)$ is not an inverse function: if $T(1,1)=T(2,2)=(0,0)$, then $T^{-1}(0,0)$ is not a single vector, and the notation does not imply an inverse map exists.
- The solution set of $Ax=b$ is a subspace only when $b=0$.
- For a basis of the column space, use the columns of the original matrix that match RREF pivot columns, not the RREF columns themselves.
