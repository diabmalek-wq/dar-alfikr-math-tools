F,I,C='Foundational','Intermediate','Challenge'
WEEK=3
TITLE=r"Span, Linear Independence \& Setting Up Linear Systems"
HEADT=r"Span, Linear Independence \& Setting Up Linear Systems"
FILE="LA-Week-03"
SECS=[("A","Linear Combinations and Span"),("B","Linear Independence and Dependence"),("C","Setting Up Systems, Spanning Sets and Proofs")]
P=[]
def add(sec,lvl,st,sp,steps,ans): P.append((sec,lvl,st,sp,steps,ans))
# ---- A
add("A",F,r"Write $(5,-1)$ as a linear combination of $(1,1)$ and $(1,-1)$ in $\mathbb{R}^{2}$.",3.0,
 [r"Set $a(1,1)+b(1,-1)=(5,-1)$: $a+b=5$ and $a-b=-1$.",r"Add the equations: $2a=4$, so $a=2$. Then $b=5-2=3$.",r"Check: $2(1,1)+3(1,-1)=(2+3,\,2-3)=(5,-1)$."],
 r"$(5,-1)=2(1,1)+3(1,-1)$")
add("A",F,r"Decide whether $(2,3,4)\in\operatorname{span}\{(1,1,1),(0,1,2)\}$ in $\mathbb{R}^{3}$. If so, give the coefficients.",3.4,
 [r"$a(1,1,1)+b(0,1,2)=(a,\ a+b,\ a+2b)$. Set equal to $(2,3,4)$.",r"First coordinate: $a=2$. Second: $2+b=3$, so $b=1$.",r"Third coordinate check: $a+2b=2+2=4$ \checkmark."],
 r"Yes: $(2,3,4)=2(1,1,1)+1\,(0,1,2)$.")
add("A",F,r"Decide whether $(1,0,0)\in\operatorname{span}\{(1,1,0),(0,1,1)\}$ in $\mathbb{R}^{3}$.",3.4,
 [r"$x(1,1,0)+y(0,1,1)=(x,\ x+y,\ y)$. Set equal to $(1,0,0)$.",r"First coordinate: $x=1$. Third: $y=0$.",r"Second coordinate: $x+y=1\neq0$. Contradiction."],
 r"No, $(1,0,0)\notin\operatorname{span}\{(1,1,0),(0,1,1)\}$.")
add("A",I,r"Find $k$ such that $(1,2,k)\in\operatorname{span}\{(1,1,0),(1,-1,2)\}$.",3.6,
 [r"$a(1,1,0)+b(1,-1,2)=(a+b,\ a-b,\ 2b)$. Set equal to $(1,2,k)$.",r"$a+b=1$ and $a-b=2$: adding gives $2a=3$, so $a=\tfrac32$; then $b=-\tfrac12$.",r"Third coordinate: $k=2b=-1$.",r"Check: $\tfrac32(1,1,0)-\tfrac12(1,-1,2)=(1,\,2,\,-1)$ \checkmark."],
 r"$k=-1$")
add("A",I,r"In $\mathbb{C}^{2}$ over $\mathbb{C}$, write $(1+i,\;2)$ as a linear combination of $(1,i)$ and $(1,-i)$.",4.4,
 [r"Solve $a(1,i)+b(1,-i)=(1+i,2)$: \ $a+b=1+i$ \ and \ $ia-ib=2$.",r"Divide the second equation by $i$: $a-b=\dfrac{2}{i}=-2i$.",r"Add: $2a=1+i-2i=1-i$, so $a=\dfrac{1-i}{2}$. Subtract: $2b=1+i+2i=1+3i$, so $b=\dfrac{1+3i}{2}$.",r"Check: $a+b=\tfrac{2+2i}{2}=1+i$ \checkmark \ and \ $a-b=\tfrac{-4i}{2}=-2i$ \checkmark."],
 r"$a=\dfrac{1-i}{2},\ b=\dfrac{1+3i}{2}$")
add("A",F,r"Show that $\operatorname{span}\{(1,2),(2,4)\}\subseteq\mathbb{R}^{2}$ is a line, and give its equation.",3.4,
 [r"A general element is $a(1,2)+b(2,4)=(a+2b,\ 2a+4b)=(a+2b)(1,2)$.",r"Put $t=a+2b$; as $a,b$ vary, $t$ takes every real value.",r"So the span is $\{(t,2t):t\in\mathbb{R}\}$, i.e.\ all points with $y=2x$."],
 r"The line $y=2x$ through the origin.")
add("A",I,r"Describe $\operatorname{span}\{(1,0,2),(0,1,-1)\}\subseteq\mathbb{R}^{3}$ by a single linear equation in $x,y,z$.",4.0,
 [r"$a(1,0,2)+b(0,1,-1)=(a,\ b,\ 2a-b)$.",r"So $x=a$, $y=b$, $z=2a-b=2x-y$.",r"Rearrange: $2x-y-z=0$. Conversely every $(x,y,2x-y)$ is obtained with $a=x,\ b=y$."],
 r"$\{(x,y,z):2x-y-z=0\}$")
add("A",C,r"Prove that for any vectors $v_1,\dots,v_k$ in a vector space $V$, the set $\operatorname{span}\{v_1,\dots,v_k\}$ is a subspace of $V$.",5.0,
 [r"Zero vector: $\mathbf 0=0v_1+\dots+0v_k$, so $\mathbf 0\in\operatorname{span}$.",r"Addition: $\sum a_iv_i+\sum b_iv_i=\sum(a_i+b_i)v_i$, again a linear combination.",r"Scalars: $\lambda\sum a_iv_i=\sum(\lambda a_i)v_i$, again a linear combination.",r"All three subspace conditions hold."],
 r"$\operatorname{span}\{v_1,\dots,v_k\}$ is a subspace of $V$.")
# ---- B
add("B",F,r"Is $\{(1,2),(3,6)\}$ linearly independent in $\mathbb{R}^{2}$?",2.6,
 [r"Observe $(3,6)=3(1,2)$.",r"Hence $3(1,2)-1\,(3,6)=\mathbf 0$ is a nontrivial relation."],
 r"Linearly dependent.")
add("B",F,r"Is $\{(1,2),(2,3)\}$ linearly independent in $\mathbb{R}^{2}$?",3.0,
 [r"Solve $a(1,2)+b(2,3)=\mathbf 0$: $a+2b=0$ and $2a+3b=0$.",r"From the first, $a=-2b$. Substitute: $-4b+3b=-b=0$, so $b=0$ and $a=0$.",r"Only the trivial solution."],
 r"Linearly independent.")
add("B",I,r"Is $\{(1,0,1),(1,1,0),(0,1,1)\}$ linearly independent in $\mathbb{R}^{3}$?",4.0,
 [r"Solve $a(1,0,1)+b(1,1,0)+c(0,1,1)=\mathbf 0$: \ $a+b=0,\ \ b+c=0,\ \ a+c=0$.",r"So $a=-b$ and $c=-b$. Then $a+c=-2b=0$, giving $b=0$.",r"Hence $a=b=c=0$."],
 r"Linearly independent.")
add("B",I,r"Is $\{(1,2,3),(4,5,6),(7,8,9)\}$ linearly independent in $\mathbb{R}^{3}$? If not, give a nontrivial relation.",4.0,
 [r"Solve $a v_1+bv_2+cv_3=\mathbf 0$: $a+4b+7c=0,\ 2a+5b+8c=0,\ 3a+6b+9c=0$.",r"Eq.\,2 $-$ Eq.\,1: $a+b+c=0$. Eq.\,3 $-$ Eq.\,2: $a+b+c=0$ (same equation). So the system has a free variable.",r"Eq.\,1 $-$ $(a+b+c)$: $3b+6c=0$, so $b=-2c$; then $a=-b-c=c$. Take $c=1$: $(a,b,c)=(1,-2,1)$.",r"Check: $v_1-2v_2+v_3=(1-8+7,\ 2-10+8,\ 3-12+9)=(0,0,0)$ \checkmark."],
 r"Linearly dependent: $v_1-2v_2+v_3=\mathbf 0$.")
add("B",C,r"Find all real $k$ for which $\{(1,1,1),(1,2,3),(1,3,k)\}$ is linearly dependent.",4.6,
 [r"Solve $a(1,1,1)+b(1,2,3)+c(1,3,k)=\mathbf 0$: $a+b+c=0,\ \ a+2b+3c=0,\ \ a+3b+kc=0$.",r"Eq.\,2 $-$ Eq.\,1: $b+2c=0$. Eq.\,3 $-$ Eq.\,2: $b+(k-3)c=0$.",r"Subtract these two: $(k-5)c=0$.",r"If $k\ne5$: $c=0$, then $b=0,\ a=0$ (independent). If $k=5$: $c$ is free, e.g.\ $c=1,\ b=-2,\ a=1$ (dependent)."],
 r"Dependent exactly when $k=5$.")
add("B",F,r"In $P_{2}(\mathbb{R})$, is $\{1+x,\ 1-x,\ 2\}$ linearly independent?",3.0,
 [r"Add the first two: $(1+x)+(1-x)=2$.",r"So $(1+x)+(1-x)-1\cdot2=\mathbf 0$ is a nontrivial relation."],
 r"Linearly dependent.")
add("B",I,r"In $\mathbb{C}^{2}$, consider $\{(1,i),\ (1+i,\ i-1)\}$. (a) Is it linearly independent over $\mathbb{C}$? (b) Is it linearly independent over $\mathbb{R}$?",5.0,
 [r"(a) Compute $(1+i)(1,i)=(1+i,\ i+i^{2})=(1+i,\ i-1)$, which is the second vector.",r"So $(1+i)\,v_1-v_2=\mathbf 0$: dependent over $\mathbb{C}$.",r"(b) Take real $a,b$ with $a(1,i)+b(1+i,\,i-1)=\mathbf 0$. First coordinate: $a+b+bi=0$.",r"Imaginary part gives $b=0$; then real part gives $a=0$. Only the trivial solution over $\mathbb{R}$."],
 r"(a) dependent over $\mathbb{C}$; (b) independent over $\mathbb{R}$.")
add("B",C,r"Let $u,v,w$ be linearly independent in a real vector space. Prove that $u+v,\ v+w,\ u+w$ are linearly independent.",5.0,
 [r"Suppose $a(u+v)+b(v+w)+c(u+w)=\mathbf 0$.",r"Regroup: $(a+c)u+(a+b)v+(b+c)w=\mathbf 0$.",r"By independence of $u,v,w$: $a+c=0,\ a+b=0,\ b+c=0$.",r"Adding: $2(a+b+c)=0$, so $a+b+c=0$. Then $a=(a+b+c)-(b+c)=0$, and similarly $b=0$, $c=0$."],
 r"Only the trivial relation exists, so they are linearly independent.")
# ---- C
add("C",F,r"Set up and solve the system that decides whether $(1,2,3)\in\operatorname{span}\{(1,0,1),(2,1,0),(0,1,1)\}$.",4.6,
 [r"Seek $a,b,c$ with $a(1,0,1)+b(2,1,0)+c(0,1,1)=(1,2,3)$. Coordinatewise: $a+2b=1,\ \ b+c=2,\ \ a+c=3$.",r"Augmented matrix (columns are the three vectors, last column is the target): $\left(\begin{array}{ccc|c}1&2&0&1\\0&1&1&2\\1&0&1&3\end{array}\right)$.",r"From Eq.\,1: $a=1-2b$. From Eq.\,2: $c=2-b$. Substitute into Eq.\,3: $3-3b=3$, so $b=0$, $a=1$, $c=2$.",r"Check: $1(1,0,1)+0(2,1,0)+2(0,1,1)=(1,2,3)$ \checkmark."],
 r"Yes: $(1,2,3)=1(1,0,1)+0(2,1,0)+2(0,1,1)$.")
add("C",I,r"Find the condition on $(a,b,c)$ for $(a,b,c)\in\operatorname{span}\{(1,2,0),(0,1,1)\}$.",4.4,
 [r"$x(1,2,0)+y(0,1,1)=(x,\ 2x+y,\ y)$.",r"Matching $(a,b,c)$: $x=a$, $y=c$, and $b=2x+y=2a+c$.",r"The condition is $2a-b+c=0$; conversely, if it holds take $x=a,\ y=c$."],
 r"$2a-b+c=0$")
add("C",I,r"Find a finite spanning set for $W=\{(x,y,z)\in\mathbb{R}^{3}:x+y+z=0\}$.",4.4,
 [r"Solve for $x$: $x=-y-z$, so every element is $(-y-z,\ y,\ z)$.",r"Split: $(-y-z,y,z)=y(-1,1,0)+z(-1,0,1)$.",r"Hence $W\subseteq\operatorname{span}\{(-1,1,0),(-1,0,1)\}$; both vectors satisfy $x+y+z=0$, so equality holds."],
 r"$W=\operatorname{span}\{(-1,1,0),(-1,0,1)\}$")
add("C",I,r"(a) Show that $\{(1,1),(1,2),(2,1)\}$ spans $\mathbb{R}^{2}$. (b) Is it linearly independent?",5.0,
 [r"(a) For a target $(x,y)$ use only the first two: $a+b=x$, $a+2b=y$. Subtract: $b=y-x$, then $a=2x-y$. Every $(x,y)$ is reached.",r"(b) Look for a relation among all three. Try $(2,1)=a(1,1)+b(1,2)$: $a+b=2,\ a+2b=1$ give $b=-1,\ a=3$.",r"Check: $3(1,1)-(1,2)=(2,1)$ \checkmark, so $3(1,1)-(1,2)-(2,1)=\mathbf 0$."],
 r"(a) Yes it spans. (b) No, it is linearly dependent.")
add("C",I,r"Show that $\{1,\ 1+x,\ 1+x+x^{2}\}$ spans $P_{2}(\mathbb{R})$.",4.6,
 [r"Let $a+bx+cx^{2}$ be arbitrary. Seek $\alpha,\beta,\gamma$ with $a+bx+cx^{2}=\alpha\cdot1+\beta(1+x)+\gamma(1+x+x^{2})$.",r"Compare coefficients: $x^{2}$: $\gamma=c$. $x$: $\beta+\gamma=b$, so $\beta=b-c$. Constant: $\alpha+\beta+\gamma=a$, so $\alpha=a-b$.",r"Such $\alpha,\beta,\gamma$ exist for every $a,b,c$."],
 r"$a+bx+cx^{2}=(a-b)\cdot1+(b-c)(1+x)+c(1+x+x^{2})$; spans.")
add("C",C,r"Show that $\left\{\begin{pmatrix}1&0\\0&1\end{pmatrix},\begin{pmatrix}0&1\\1&0\end{pmatrix},\begin{pmatrix}0&1\\-1&0\end{pmatrix},\begin{pmatrix}1&0\\0&-1\end{pmatrix}\right\}$ spans $M_{2\times2}(\mathbb{R})$ and is linearly independent.",6.0,
 [r"Let $\begin{pmatrix}p&q\\r&s\end{pmatrix}=\alpha I+\beta\begin{pmatrix}0&1\\1&0\end{pmatrix}+\gamma\begin{pmatrix}0&1\\-1&0\end{pmatrix}+\delta\begin{pmatrix}1&0\\0&-1\end{pmatrix}$.",r"Entries give: $p=\alpha+\delta$, \ $s=\alpha-\delta$, \ $q=\beta+\gamma$, \ $r=\beta-\gamma$.",r"Solve: $\alpha=\tfrac{p+s}{2},\ \delta=\tfrac{p-s}{2},\ \beta=\tfrac{q+r}{2},\ \gamma=\tfrac{q-r}{2}$. So every matrix is reached: spanning.",r"Independence: if the matrix is $\mathbf 0$ then $p=q=r=s=0$, so the formulas give $\alpha=\beta=\gamma=\delta=0$."],
 r"The set spans $M_{2\times2}(\mathbb{R})$ and is linearly independent.")
add("C",C,r"Prove: if $w\in\operatorname{span}\{v_1,\dots,v_k\}$ then $\operatorname{span}\{v_1,\dots,v_k,w\}=\operatorname{span}\{v_1,\dots,v_k\}$.",5.0,
 [r"($\supseteq$) Any combination of $v_1,\dots,v_k$ is a combination of $v_1,\dots,v_k,w$ with coefficient $0$ on $w$.",r"Write $w=\sum c_iv_i$. ($\subseteq$) Take $\sum a_iv_i+bw$.",r"Substitute: $\sum a_iv_i+b\sum c_iv_i=\sum(a_i+bc_i)v_i$, a combination of $v_1,\dots,v_k$.",r"Both inclusions hold."],
 r"The two spans are equal.")
add("C",C,r"Let $v_1,\dots,v_k$ be linearly independent and $v_{k+1}\notin\operatorname{span}\{v_1,\dots,v_k\}$. Prove that $v_1,\dots,v_{k+1}$ are linearly independent.",5.4,
 [r"Suppose $a_1v_1+\dots+a_kv_k+a_{k+1}v_{k+1}=\mathbf 0$.",r"If $a_{k+1}\neq0$: $v_{k+1}=-\sum_{i\le k}\dfrac{a_i}{a_{k+1}}v_i\in\operatorname{span}\{v_1,\dots,v_k\}$, a contradiction.",r"So $a_{k+1}=0$, leaving $a_1v_1+\dots+a_kv_k=\mathbf 0$.",r"By independence of $v_1,\dots,v_k$: $a_1=\dots=a_k=0$."],
 r"All coefficients vanish, so $v_1,\dots,v_{k+1}$ are linearly independent.")

EX=[
("Membership in a span",r"Is $(4,7)\in\operatorname{span}\{(1,2),(3,5)\}$ in $\mathbb{R}^{2}$?",
 [r"Solve $a(1,2)+b(3,5)=(4,7)$: $a+3b=4$, $2a+5b=7$.",r"From the first, $a=4-3b$. Substitute: $8-6b+5b=7$, so $b=1$, $a=1$.",r"Check: $(1,2)+(3,5)=(4,7)$."],
 r"Yes: $(4,7)=1(1,2)+1(3,5)$."),
("Membership (positive)",r"Is $(1,2,3)\in\operatorname{span}\{(1,0,1),(0,1,1)\}$?",
 [r"$a(1,0,1)+b(0,1,1)=(a,\ b,\ a+b)$.",r"Match: $a=1$, $b=2$; third coordinate $a+b=3$ \checkmark."],
 r"Yes: $(1,2,3)=1(1,0,1)+2(0,1,1)$."),
("Membership (negative)",r"Is $(1,2,4)\in\operatorname{span}\{(1,0,1),(0,1,1)\}$?",
 [r"As before the combination is $(a,b,a+b)$.",r"Match: $a=1$, $b=2$, but then $a+b=3\neq4$."],
 r"No."),
("Dependence, finding a relation",r"Test $\{(1,2,1),(2,1,0),(1,-1,-1)\}$ for independence.",
 [r"Solve $a(1,2,1)+b(2,1,0)+c(1,-1,-1)=\mathbf 0$: $a+2b+c=0,\ 2a+b-c=0,\ a-c=0$.",r"Third: $c=a$. First: $2a+2b=0$, so $b=-a$. Second: $2a-a-a=0$ \checkmark (automatically).",r"So $(a,b,c)=(1,-1,1)$ is a nontrivial solution. Check: $v_1-v_2+v_3=(1-2+1,\ 2-1-1,\ 1-0-1)=\mathbf 0$."],
 r"Linearly dependent: $v_1-v_2+v_3=\mathbf 0$."),
("Independence in $P_{2}$",r"Show $\{1+x,\ x+x^{2},\ 1+x^{2}\}$ is linearly independent in $P_{2}(\mathbb{R})$.",
 [r"Suppose $a(1+x)+b(x+x^{2})+c(1+x^{2})=\mathbf 0$. Compare coefficients.",r"Constant: $a+c=0$. $x$: $a+b=0$. $x^{2}$: $b+c=0$.",r"So $a=-c$ and $b=-a=c$; then $b+c=2c=0$, so $c=0$, hence $a=b=0$."],
 r"Linearly independent."),
("The field matters",r"Is $\{(1,i),(i,-1)\}$ linearly independent in $\mathbb{C}^{2}$ over $\mathbb{C}$? Over $\mathbb{R}$?",
 [r"Note $i\cdot(1,i)=(i,\,i^{2})=(i,-1)$.",r"Over $\mathbb{C}$: $i\,v_1-v_2=\mathbf 0$, a nontrivial relation, so dependent.",r"Over $\mathbb{R}$: $a(1,i)+b(i,-1)=\mathbf 0$ with real $a,b$ gives first coordinate $a+bi=0$, so $a=b=0$: independent."],
 r"Dependent over $\mathbb{C}$; independent over $\mathbb{R}$."),
("Proof: dependence means one vector is redundant",r"Prove: if $v_1,\dots,v_k$ are linearly dependent, then some $v_j$ is a linear combination of the others.",
 [r"Take a nontrivial relation $a_1v_1+\dots+a_kv_k=\mathbf 0$ and pick $j$ with $a_j\neq0$.",r"Isolate: $a_jv_j=-\sum_{i\neq j}a_iv_i$.",r"Divide by $a_j$ (allowed because $a_j\ne0$ in a field): $v_j=-\sum_{i\ne j}\dfrac{a_i}{a_j}v_i$."],
 r"$v_j\in\operatorname{span}\{v_i:i\neq j\}$."),
("Describing a span by an equation",r"Find the condition on $(a,b,c)$ for $(a,b,c)\in\operatorname{span}\{(1,1,0),(0,1,1)\}$.",
 [r"$x(1,1,0)+y(0,1,1)=(x,\ x+y,\ y)$.",r"Matching: $x=a$, $y=c$, and $b=x+y=a+c$."],
 r"$a-b+c=0$"),
]
FACTS=r"""
\begin{tcolorbox}[colback=soft,colframe=ink,title={\bfseries Key Facts}]
\textbf{Linear combination and span.} A linear combination of $v_1,\dots,v_k\in V$ is $a_1v_1+\dots+a_kv_k$ with $a_i\in\mathbb{F}$. $\operatorname{span}\{v_1,\dots,v_k\}$ is the set of all of them; $\operatorname{span}\varnothing=\{\mathbf 0\}$. It is a subspace, and the smallest subspace containing $v_1,\dots,v_k$.

\textbf{Setting up the system.} To test $w\in\operatorname{span}\{v_1,\dots,v_k\}$ in $\mathbb{F}^{n}$, solve $a_1v_1+\dots+a_kv_k=w$. Coordinatewise this is $n$ equations in $k$ unknowns, with augmented matrix whose columns are $v_1,\dots,v_k\mid w$. Solution exists $\iff w\in$ span.

\textbf{Linear independence.} $v_1,\dots,v_k$ are \emph{independent} if $a_1v_1+\dots+a_kv_k=\mathbf 0$ forces $a_1=\dots=a_k=0$; otherwise \emph{dependent}. Test: solve the homogeneous system; only $\mathbf 0$ $\Rightarrow$ independent, a nonzero solution $\Rightarrow$ dependent (and it gives a relation).

\textbf{Useful facts.} A set containing $\mathbf 0$ is dependent. One vector is independent iff it is nonzero. Two vectors are independent iff neither is a scalar multiple of the other. $v_1,\dots,v_k$ dependent $\iff$ some $v_j\in\operatorname{span}$ of the others. If $w\in\operatorname{span}\{v_1,\dots,v_k\}$, adding $w$ does not enlarge the span. Independence and span depend on the field: $\{(1,i),(i,-1)\}$ is dependent over $\mathbb{C}$ but independent over $\mathbb{R}$.

\textbf{Counting.} More homogeneous unknowns than equations forces a nonzero solution; so more than $n$ vectors in $\mathbb{F}^{n}$ are dependent.
\end{tcolorbox}
"""
