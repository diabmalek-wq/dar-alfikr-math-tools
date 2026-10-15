from h4 import *
WEEK=5
TITLE=r"Bases and Dimension"
HEADT=r"Bases and Dimension"
FILE="LA-Week-05"
SECS=[("A","Standard Bases, Counting and Dimension"),("B","Bases of Subspaces Given by Constraints"),("C","Extracting, Extending and Coordinates"),("D","Proofs and Challenges")]
P=[]
def add(sec,lvl,st,sp,steps,ans): P.append((sec,lvl,st,sp,steps,ans))
def mm(rows,nc=None): return mat(M(rows),nc)
def zlist(v): return [zz(t) for t in v]
def pm(v,r,c):
    v=zlist(v)
    return r"\begin{pmatrix}"+r" \\ ".join(" & ".join(tx(v[i*c+j]) for j in range(c)) for i in range(r))+r"\end{pmatrix}"
def pm2(v): return pm(v,2,2)
def pol(v):
    v=zlist(v)
    return expr(v[0],[(v[k],("x" if k==1 else "x^{%d}"%k)) for k in range(1,len(v))])
def cv(v): return vec(zlist(v))
X3=['x','y','z']; X4=['x','y','z','w']; ABCD=['a','b','c','d']
def colsof(vecs): return [[zz(vecs[j][i]) for j in range(len(vecs))] for i in range(len(vecs[0]))]
def col(R,j): return [R[i][j] for i in range(len(R))]
def pivs(A):
    return trace(M(A) if not isinstance(A[0][0],Z) else A)[2]

def cs(A,vs,intro,fmt,wname="W"):
    """constraint subspace: A = constraint matrix over coordinates vs; fmt: coordinate vector -> LaTeX object."""
    Am=M(A); b=V(*([0]*len(A)))
    st,a=solve_steps(Am,b,vs)
    part,null,fr,pv=solve(Am,b)
    k=len(null)
    objs=[fmt(v) for v in null]
    post=[r"Translate each coordinate vector back into the original objects. Setting one parameter to $1$ and the others to $0$ in the vector form gives: %s."%(
            "; ".join(r"$%s\leftrightarrow %s$"%(cv(v),o) for v,o in zip(null,objs)))]
    post.append(r"These %d vectors \emph{span} $%s$: the vector form says every element of $%s$ equals $%s$ with the parameters free. They are \emph{linearly independent}: in this combination the entry in the position of the free variable%s %s equals the parameter%s %s (each basis vector has $1$ in its own free position and $0$ in the other free position%s), so a combination equal to $\mathbf 0$ forces every parameter to be $0$."%(k,wname,wname,
            "+".join("%s\\,\\mathbf b_%d"%("stuvw"[j],j+1) for j in range(k)),
            "" if k==1 else "s",", ".join("$%s$"%vs[f] for f in fr),
            "" if k==1 else "s",", ".join("$%s$"%"stuvw"[j] for j in range(k)),"" if k==1 else "s"))
    post.append(r"Hence the objects above form a basis of $%s$, and $\dim %s$ equals the number of free variables, namely $%d$."%(wname,wname,k))
    ans=r"Basis: $\left\{%s\right\}$; $\dim %s=%d$."%(",\ ".join(objs),wname,k)
    return intro+st+post,ans,null,fr

# ===================== PART A
add("A",F,r"State the standard basis and the dimension of each space: (a) $\mathbb{C}^{3}$ over $\mathbb{C}$; (b) $M_{2\times3}(\mathbb{R})$; (c) $P_{3}(\mathbb{R})$. Then write $A=\begin{pmatrix}2&-1&0\\5&3&4\end{pmatrix}$ and $p(x)=4-x+2x^{3}$ as combinations of the standard bases of (b) and (c).",3.6,
[r"(a) The standard basis of $\mathbb{C}^{3}$ is $\{e_1,e_2,e_3\}$ with $e_1=(1,0,0)$, $e_2=(0,1,0)$, $e_3=(0,0,1)$. It has $3$ elements, so $\dim\mathbb{C}^{3}=3$ over $\mathbb{C}$.",
 r"(b) Let $E_{ij}$ be the $2\times3$ matrix with $1$ in row $i$, column $j$ and $0$ elsewhere. The standard basis is $\{E_{11},E_{12},E_{13},E_{21},E_{22},E_{23}\}$: $2\cdot3=6$ matrices. So $\dim M_{2\times3}(\mathbb{R})=6$.",
 r"(c) The standard basis of $P_3(\mathbb{R})$ (polynomials of degree at most $3$) is $\{1,x,x^{2},x^{3}\}$. It has $4$ elements, so $\dim P_3(\mathbb{R})=4$ (always degree bound plus $1$).",
 r"Write $A$ entry by entry: $A=2E_{11}+(-1)E_{12}+0\,E_{13}+5E_{21}+3E_{22}+4E_{23}$. The coefficients are the entries of $A$ read row by row.",
 r"Write $p$ by its coefficients: $p=4\cdot1+(-1)\,x+0\,x^{2}+2\,x^{3}$."],
r"(a) $\{e_1,e_2,e_3\}$, dim $3$. (b) $\{E_{ij}\}$ (six matrices), dim $6$; $A=2E_{11}-E_{12}+5E_{21}+3E_{22}+4E_{23}$. (c) $\{1,x,x^{2},x^{3}\}$, dim $4$; $p=4\cdot1-x+2x^{3}$.")

add("A",F,r"For each statement decide whether it is true, using only a dimension count (state the dimension used and the theorem): (a) five matrices in $M_2(\mathbb{R})$ must be linearly dependent; (b) $\{(1,0,0),(0,1,0)\}$ spans $\mathbb{R}^{3}$; (c) any four polynomials in $P_2(\mathbb{R})$ are linearly dependent; (d) five matrices in $M_{3\times2}(\mathbb{R})$ can span $M_{3\times2}(\mathbb{R})$; (e) ten matrices in $M_3(\mathbb{R})$ can form a basis of $M_3(\mathbb{R})$; (f) three polynomials in $P_3(\mathbb{R})$ can span $P_3(\mathbb{R})$.",5.0,
[r"Tools. If $\dim V=n$ then $V$ is spanned by $n$ vectors, so (Dimension Bound) every linearly independent set in $V$ has at most $n$ elements; equivalently, more than $n$ vectors are linearly dependent. Also a spanning set needs at least $n$ vectors (a spanning set can be shrunk to a basis, which has exactly $n$). A basis has exactly $n$ elements.",
 r"(a) $\dim M_2(\mathbb{R})=4$. Five vectors is more than $4$, so they are linearly dependent. \textbf{True.}",
 r"(b) $\dim\mathbb{R}^{3}=3$ but the set has only $2<3$ vectors, and a spanning set needs at least $3$. \textbf{False.} (Concretely every combination has third coordinate $0$.)",
 r"(c) $\dim P_2(\mathbb{R})=3$, so $P_2(\mathbb{R})$ is spanned by $3$ vectors and every independent set has at most $3$ elements. Four polynomials in $P_2(\mathbb{R})$ therefore cannot be independent. \textbf{True.}",
 r"(d) $\dim M_{3\times2}(\mathbb{R})=3\cdot2=6$. Five vectors is fewer than $6$, so they cannot span. \textbf{False.}",
 r"(e) $\dim M_3(\mathbb{R})=9$. A basis has exactly $9$ elements, not $10$. \textbf{False.}",
 r"(f) $\dim P_3(\mathbb{R})=4$. Three vectors is fewer than $4$, so they cannot span. \textbf{False.}"],
r"(a) true; (b) false; (c) true; (d) false; (e) false; (f) false.")

A3=[[1,1,0],[1,2,1],[0,1,3]]   # columns are the vectors (1,1,0),(1,2,1),(0,1,3)
t,R,p=trace(M(A3)); assert p==[0,1,2] and R==M([[1,0,0],[0,1,0],[0,0,1]])
add("A",F,r"Is $\{(1,1,0),\ (1,2,1),\ (0,1,3)\}$ a basis of $\mathbb{R}^{3}$? Row reduce the matrix whose columns are these vectors.",4.2,
[r"Put the vectors in the columns: $A=%s$. The set is linearly independent exactly when $A\mathbf a=\mathbf 0$ has only $\mathbf a=\mathbf 0$, i.e.\ when every column has a pivot."%mat(M(A3))]+t+
[r"The RREF is the identity matrix, so every column has a pivot: the three vectors are linearly independent.",
 r"$\dim\mathbb{R}^{3}=3$ and we have $3$ linearly independent vectors, so they form a basis (an independent set with $\dim V$ elements is a basis). Equivalently, a pivot in every \emph{row} means $A\mathbf a=\mathbf b$ is solvable for every $\mathbf b$, so they span."],
r"Yes, it is a basis of $\mathbb{R}^{3}$ (RREF $=I_3$).")

add("A",I_,r"(Dimension depends on the scalars.) (a) Find a basis and the dimension of $\mathbb{C}^{2}$ regarded as a vector space over $\mathbb{R}$, and prove your set is a basis. (b) What is $\dim\mathbb{C}^{2}$ over $\mathbb{C}$? (c) Why is $\{(1,0),(i,0)\}$ linearly independent over $\mathbb{R}$ but linearly dependent over $\mathbb{C}$?",5.4,
[r"(a) Candidate: $\mathcal B=\{(1,0),(i,0),(0,1),(0,i)\}$. Over $\mathbb{R}$ the scalars are real numbers only.",
 r"\emph{Spanning.} Any $(z,w)\in\mathbb{C}^{2}$ has $z=a+bi$ and $w=c+di$ with $a,b,c,d\in\mathbb{R}$. Then $(z,w)=a(1,0)+b(i,0)+c(0,1)+d(0,i)$, a combination with real coefficients.",
 r"\emph{Independence.} Suppose $a(1,0)+b(i,0)+c(0,1)+d(0,i)=(0,0)$ with $a,b,c,d\in\mathbb{R}$. First coordinate: $a+bi=0$; a complex number $a+bi$ with $a,b$ real is $0$ only when $a=0$ and $b=0$. Second coordinate: $c+di=0$, so $c=d=0$. Only the trivial combination gives $\mathbf 0$.",
 r"So $\mathcal B$ is a basis with $4$ elements: $\dim_{\mathbb{R}}\mathbb{C}^{2}=4$.",
 r"(b) Over $\mathbb{C}$, $(z,w)=z(1,0)+w(0,1)$ with \emph{complex} coefficients $z,w$, and $\{(1,0),(0,1)\}$ is independent (if $z(1,0)+w(0,1)=\mathbf 0$ then $z=w=0$). So $\dim_{\mathbb{C}}\mathbb{C}^{2}=2$.",
 r"(c) Over $\mathbb{R}$: $a(1,0)+b(i,0)=(a+bi,0)=\mathbf 0$ forces $a=b=0$ (part (a)), so independent. Over $\mathbb{C}$: $i\cdot(1,0)-1\cdot(i,0)=(i,0)-(i,0)=\mathbf 0$ is a combination with coefficients $i$ and $-1$, not both zero, so dependent. The allowed scalars decide independence, so the dimension depends on the field."],
r"(a) Basis $\{(1,0),(i,0),(0,1),(0,i)\}$, $\dim_{\mathbb{R}}=4$. (b) $\dim_{\mathbb{C}}=2$. (c) $i(1,0)-(i,0)=\mathbf 0$ is a nontrivial \emph{complex} relation, but no nontrivial real one exists.")

# ===================== PART B
st,a,nl,fr=cs([[1,-2,0]],X3,[r"A vector $(x,y,z)$ lies in $W$ exactly when it satisfies the one linear equation $x-2y=0$, i.e.\ $x-2y+0z=0$. So $W$ is the solution set of the homogeneous system $%s$ with coefficient matrix $\begin{pmatrix}1&-2&0\end{pmatrix}$."%sysbox(M([[1,-2,0]]),V(0),X3)],lambda v:r"(%s)"%",".join(tx(t) for t in v))
add("B",F,r"Let $W=\{(x,y,z)\in\mathbb{R}^{3}:\ x=2y\}$. Show that $W$ is a subspace by exhibiting a basis, and state $\dim W$.",4.0,st,a)

st,a,nl,fr=cs([[1,0,0,1]],ABCD,[r"A matrix $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ has coordinate vector $(a,b,c,d)$ with respect to $E_{11},E_{12},E_{21},E_{22}$. The condition $\operatorname{tr}A=0$ reads $a+d=0$: the homogeneous system $%s$ with coefficient matrix $\begin{pmatrix}1&0&0&1\end{pmatrix}$."%sysbox(M([[1,0,0,1]]),V(0),ABCD)],pm2)
add("B",F,r"Find a basis and the dimension of $W=\{A\in M_2(\mathbb{R}):\ \operatorname{tr}A=0\}$.",4.0,st,a)
assert nl==[zlist([0,1,0,0]),zlist([0,0,1,0]),zlist([-1,0,0,1])]

st,a,nl,fr=cs([[1,0,0,0],[1,1,1,1]],ABCD,[r"Write $f(x)=a+bx+cx^{2}+dx^{3}$; its coordinate vector is $(a,b,c,d)$ with respect to $1,x,x^{2},x^{3}$. Then $f(0)=a$ and $f(1)=a+b+c+d$, so the conditions are $a=0$ and $a+b+c+d=0$: the homogeneous system $%s$."%sysbox(M([[1,0,0,0],[1,1,1,1]]),V(0,0),ABCD)],pol)
assert nl==[zlist([0,-1,1,0]),zlist([0,-1,0,1])]
add("B",I_,r"Find a basis and the dimension of $W=\{f\in P_3(\mathbb{R}):\ f(0)=f(1)=0\}$.",5.0,st,a)

st,a,nl,fr=cs([[0,1,1,1],[1,2,4,8]],ABCD,[r"Write $p(x)=a+bx+cx^{2}+dx^{3}$. Then $p(0)=a$, $p(1)=a+b+c+d$ and $p(2)=a+2b+4c+8d$. The condition $p(0)=p(1)$ becomes $b+c+d=0$ (subtract $a$ from both sides), and $p(2)=0$ becomes $a+2b+4c+8d=0$. So we solve the homogeneous system $%s$."%sysbox(M([[0,1,1,1],[1,2,4,8]]),V(0,0),ABCD)],pol)
assert nl==[zlist([-2,-1,1,0]),zlist([-6,-1,0,1])]
for v in nl:
    pv=lambda t:sum((v[k]*Z(t)**k if False else v[k]*Z(t**k) for k in range(4)),Z(0))
    assert pv(0)==pv(1) and pv(2)==0
add("B",I_,r"Find a basis and the dimension of $W=\{p\in P_3(\mathbb{R}):\ p(0)=p(1),\ p(2)=0\}$.",5.2,
 st[:1]+[st[1]]+st[2:]+[r"Check the first basis polynomial $q=-2-x+x^{2}$: $q(0)=-2$, $q(1)=-2-1+1=-2$, so $q(0)=q(1)$; and $q(2)=-2-2+4=0$ \checkmark. Check the second $r=-6-x+x^{3}$: $r(0)=-6$, $r(1)=-6-1+1=-6$, and $r(2)=-6-2+8=0$ \checkmark."],a)

st,a,nl,fr=cs([[1,1,-1,0],[0,1,0,1]],X4,[r"A vector $(x,y,z,w)$ lies in $W$ exactly when $x+y-z=0$ and $y+w=0$: the homogeneous system $%s$."%sysbox(M([[1,1,-1,0],[0,1,0,1]]),V(0,0),X4)],lambda v:r"(%s)"%",".join(tx(t) for t in v))
assert nl==[zlist([1,0,1,0]),zlist([1,-1,0,1])]
add("B",I_,r"Find a basis and the dimension of $W=\{(x,y,z,w)\in\mathbb{R}^{4}:\ x+y-z=0,\ y+w=0\}$.",5.0,st,a)

st,a,nl,fr=cs([[1,I,0,0],[0,0,1,Z(-1,-1)]],ABCD,[r"Let $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in M_2(\mathbb{C})$. The condition $a_{11}+i\,a_{12}=0$ reads $a+ib=0$. The condition $a_{21}=(1+i)a_{22}$ reads $c-(1+i)d=0$, i.e.\ $c+(-1-i)d=0$. The coefficient matrix of this homogeneous system over $\mathbb{C}$ is $\begin{pmatrix}1&i&0&0\\0&0&1&-1-i\end{pmatrix}$, which is already in RREF."],pm2)
assert nl==[zlist([Z(0,-1),1,0,0]),zlist([0,0,Z(1,1),1])]
add("B",I_,r"Let $W=\{A\in M_2(\mathbb{C}):\ a_{11}+i\,a_{12}=0,\ a_{21}=(1+i)\,a_{22}\}$, a subset of $M_2(\mathbb{C})$ over $\mathbb{C}$. Find a basis of $W$ and $\dim W$.",5.2,
 st+[r"Check the first basis matrix $\begin{pmatrix}-i&1\\0&0\end{pmatrix}$: $a_{11}+ia_{12}=-i+i\cdot1=0$ \checkmark and $a_{21}=0=(1+i)\cdot0$ \checkmark. Check the second $\begin{pmatrix}0&0\\1+i&1\end{pmatrix}$: $a_{11}+ia_{12}=0$ \checkmark and $a_{21}=1+i=(1+i)\cdot1$ \checkmark."],a)

st,a,nl,fr=cs([[1,0,0,1],[0,1,-1,0]],ABCD,[r"Write $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$. The condition $\operatorname{tr}A=0$ is $a+d=0$. The condition $A=A^{T}$ means $\begin{pmatrix}a&b\\c&d\end{pmatrix}=\begin{pmatrix}a&c\\b&d\end{pmatrix}$, i.e.\ $b=c$, i.e.\ $b-c=0$. So we solve the homogeneous system $%s$."%sysbox(M([[1,0,0,1],[0,1,-1,0]]),V(0,0),ABCD)],pm2)
assert nl==[zlist([0,1,1,0]),zlist([-1,0,0,1])]
add("B",I_,r"Find a basis and the dimension of $W=\{A\in M_2(\mathbb{R}):\ \operatorname{tr}A=0\ \text{and}\ A=A^{T}\}$.",5.0,st,a)

# ===================== PART C
V12=[[1,2,1],[2,4,2],[1,1,0]]
A12=colsof(V12)
t,R,p=trace(M(A12)); assert p==[0,2]
add("C",F,r"Find a linearly independent subset of $S=\{(1,2,1),\ (2,4,2),\ (1,1,0)\}\subseteq\mathbb{R}^{3}$ with the same span as $S$. State $\dim\operatorname{span}S$.",4.6,
[r"Put the vectors in the columns of $A=%s$ and row reduce. The pivot columns of the \emph{original} $A$ give an independent set with the same span as the columns."%mat(M(A12))]+t+
[r"The pivot columns are $1$ and $3$. So $\{v_1,v_3\}=\{(1,2,1),(1,1,0)\}$ is linearly independent and spans the same space as $S$.",
 r"Column $2$ of the RREF is $%s$, so $v_2=2v_1$: $2(1,2,1)=(2,4,2)$ \checkmark. Hence $v_2$ adds nothing to the span."%vec(col(R,1))+r" The span has $2$ vectors in a basis: $\dim\operatorname{span}S=2$."],
r"$\{(1,2,1),(1,1,0)\}$ (columns $1$ and $3$); $v_2=2v_1$; $\dim\operatorname{span}S=2$.")

V13=[[1,1,0],[2,2,0],[0,1,1],[1,2,1],[0,0,1]]   # coordinates wrt 1,x,x^2
A13=colsof(V13)
t,R,p=trace(M(A13)); assert p==[0,2,4]
assert [R[0][3],R[1][3]]==[1,1] and R[0][1]==2
add("C",I_,r"In $P_2(\mathbb{R})$ let $S=\{1+x,\ 2+2x,\ x+x^{2},\ 1+2x+x^{2},\ x^{2}\}$. Find a linearly independent subset of $S$ with the same span as $S$, express each remaining polynomial through it, and decide whether $S$ spans $P_2(\mathbb{R})$.",6.2,
[r"Take coordinates with respect to $1,x,x^{2}$: $1+x\leftrightarrow(1,1,0)$, $2+2x\leftrightarrow(2,2,0)$, $x+x^{2}\leftrightarrow(0,1,1)$, $1+2x+x^{2}\leftrightarrow(1,2,1)$, $x^{2}\leftrightarrow(0,0,1)$. Coordinates turn linear combinations of polynomials into linear combinations of vectors, so we may row reduce the matrix of these columns.",
 r"$A=%s$."%mat(M(A13))]+t+
[r"The pivot columns are $1,3,5$. So a linearly independent subset with the same span is $\{1+x,\ x+x^{2},\ x^{2}\}$ (columns $1,3,5$ of the \emph{original} matrix).",
 r"Non-pivot columns: column $2$ of $R$ is $(2,0,0)^{T}$, so $2+2x=2(1+x)$. Column $4$ of $R$ is $(1,1,0)^{T}$, so $1+2x+x^{2}=1\cdot(1+x)+1\cdot(x+x^{2})$. Check: $(1+x)+(x+x^{2})=1+2x+x^{2}$ \checkmark.",
 r"The span of $S$ has a basis with $3$ elements, so $\dim\operatorname{span}S=3=\dim P_2(\mathbb{R})$. A subspace of dimension $3$ in a $3$-dimensional space is the whole space (an independent set of $\dim V$ elements is a basis), so $S$ spans $P_2(\mathbb{R})$."],
r"Independent subset $\{1+x,\ x+x^{2},\ x^{2}\}$; $2+2x=2(1+x)$ and $1+2x+x^{2}=(1+x)+(x+x^{2})$. Yes, $S$ spans $P_2(\mathbb{R})$ (and $\{1+x,x+x^{2},x^{2}\}$ is a basis of it).")


V14=[[1,2,3],[3,2,1],[1,1,1]]
A14=colsof(V14)
t,R,p=trace(M(A14)); assert p==[0,1]
assert col(R,2)[:2]==[Z(1,0)/4,Z(1,0)/4]
rel=[Z(1),Z(1),Z(-4)]
assert all(sum((rel[j]*zz(V14[j][i]) for j in range(3)),Z(0)).iszero() for i in range(3))
add("C",I_,r"Let $S=\{v_1,v_2,v_3\}=\{(1,2,3),\ (3,2,1),\ (1,1,1)\}\subseteq\mathbb{R}^{3}$. (a) Write the system that tests linear independence and row reduce it. (b) Decide whether $S$ is linearly independent; if not, find an explicit relation. (c) Give a linearly independent subset of $S$ that is a basis of $\operatorname{span}S$, and decide whether $S$ spans $\mathbb{R}^{3}$.",6.6,
[r"(a) $S$ is independent iff $a_1v_1+a_2v_2+a_3v_3=\mathbf 0$ forces $a_1=a_2=a_3=0$. In coordinates this is the homogeneous system $%s$, whose coefficient matrix has columns $v_1,v_2,v_3$: $A=%s$."%(sysbox(M([[1,3,1],[2,2,1],[3,1,1]]),V(0,0,0),['a_1','a_2','a_3']),mat(M(A14))),
 r"Row reduce $A$."]+t+
[r"(b) The RREF has pivots in columns $1,2$ only, so $a_3$ is free and the system has nonzero solutions: $S$ is \emph{linearly dependent}.",
 r"Column $3$ of the RREF is $%s$, so $a_1=-\tfrac14a_3$ and $a_2=-\tfrac14a_3$. Choose $a_3=-4$ (to clear fractions): $(a_1,a_2,a_3)=(1,1,-4)$, giving the relation $v_1+v_2-4v_3=\mathbf 0$."%cv([R[0][2],R[1][2]]),
 r"Check: $(1,2,3)+(3,2,1)-4(1,1,1)=(4,4,4)-(4,4,4)=(0,0,0)$ \checkmark.",
 r"(c) The pivot columns of $A$ are $1$ and $2$, so $\{v_1,v_2\}=\{(1,2,3),(3,2,1)\}$ is linearly independent and spans $\operatorname{span}S$ (indeed $v_3=\tfrac14v_1+\tfrac14v_2$). So $\dim\operatorname{span}S=2$.",
 r"Since $\dim\operatorname{span}S=2<3=\dim\mathbb{R}^{3}$, $S$ does not span $\mathbb{R}^{3}$ (a spanning set of $\mathbb{R}^{3}$ needs at least $3$ vectors)."],
r"Dependent: $v_1+v_2-4v_3=\mathbf 0$. Basis of $\operatorname{span}S$: $\{(1,2,3),(3,2,1)\}$, $\dim\operatorname{span}S=2$, so $S$ does not span $\mathbb{R}^{3}$.")

# 15 extension
A1_,A2_,A3_=[1,0,0,0],[0,1,1,0],[0,1,0,1]
E=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
A15=colsof([A1_,A2_,A3_]+E)
t,R,p=trace(M(A15),bar=3); assert p==[0,1,2,4]
add("C",I_,r"Extend the linearly independent set $\left\{\begin{pmatrix}1&0\\0&0\end{pmatrix},\begin{pmatrix}0&1\\1&0\end{pmatrix},\begin{pmatrix}0&1\\0&1\end{pmatrix}\right\}$ to a basis of $M_2(\mathbb{R})$ by adding one of $E_{11},E_{12},E_{21},E_{22}$. Justify your choice and say which of the four would \emph{not} work.",7.0,
[r"Use coordinates $(a_{11},a_{12},a_{21},a_{22})$: the three matrices are $A_1=(1,0,0,0)$, $A_2=(0,1,1,0)$, $A_3=(0,1,0,1)$, and $E_{11},E_{12},E_{21},E_{22}$ are the standard vectors. $\dim M_2(\mathbb{R})=4$, so we need exactly one more vector $x$ with $x\notin\operatorname{span}\{A_1,A_2,A_3\}$ (Extension Lemma: $\{A_1,A_2,A_3,x\}$ is then independent, and $4$ independent vectors in a $4$-dimensional space form a basis).",
 r"Find $\operatorname{span}\{A_1,A_2,A_3\}$: $\alpha A_1+\beta A_2+\gamma A_3$ has coordinates $(\alpha,\ \beta+\gamma,\ \beta,\ \gamma)$. So a matrix $\begin{pmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{pmatrix}$ lies in the span exactly when $a_{12}=a_{21}+a_{22}$ (the span is $\{(\alpha,\beta+\gamma,\beta,\gamma)\}$; given such coordinates take $\alpha=a_{11}$, $\beta=a_{21}$, $\gamma=a_{22}$).",
 r"Test each standard matrix against $a_{12}=a_{21}+a_{22}$: $E_{11}$: $0=0+0$ holds, so $E_{11}\in\operatorname{span}$ (indeed $E_{11}=A_1$). $E_{12}$: $1=0+0$ fails, so $E_{12}\notin\operatorname{span}$. $E_{21}$: $0=1+0$ fails, so not in the span. $E_{22}$: $0=0+1$ fails, so not in the span.",
 r"Same result by row reduction: put $A_1,A_2,A_3,E_{11},E_{12},E_{21},E_{22}$ as columns of one matrix and reduce; the pivot columns tell which vectors to keep from left to right. $B=%s$."%mat(M(A15),3)]+t+
[r"The pivot columns are $1,2,3$ and $5$. Column $4$ ($E_{11}$) has no pivot because it equals column $1$; column $5$ ($E_{12}$) is the first standard vector that adds a new direction, so $\{A_1,A_2,A_3,E_{12}\}$ is a basis.",
 r"Conclusion: $E_{12}$, $E_{21}$ and $E_{22}$ each extend the set to a basis; $E_{11}$ does not, since it already lies in the span of the given set."],
r"A basis is $\{A_1,A_2,A_3,E_{12}\}$ (also $E_{21}$ or $E_{22}$ would work); $E_{11}$ fails because $E_{11}=A_1$ is already in the span.")

# 16 coordinates
B16=[[1,-1,0],[2,0,1],[0,1,2]]; p16=[5,2,8]
A16=colsof(B16)
s=solve(M(A16),V(*p16)); assert s[0]==zlist([1,2,3]) and not s[1]
st,a=solve_steps(M(A16),V(*p16),['a','b','c'])
add("C",I_,r"Show that $\beta=\{1-x,\ 2+x^{2},\ x+2x^{2}\}$ is a basis of $P_2(\mathbb{R})$ and find the coordinate vector $[p]_\beta$ of $p(x)=5+2x+8x^{2}$.",6.6,
[r"With respect to $1,x,x^{2}$ the three polynomials have coordinate vectors $(1,-1,0)$, $(2,0,1)$, $(0,1,2)$, and $p\leftrightarrow(5,2,8)$. We need $a(1-x)+b(2+x^{2})+c(x+2x^{2})=p$, i.e.\ the system with these vectors as columns and $(5,2,8)$ on the right: $a+2b=5$, $-a+c=2$, $b+2c=8$ (equating coefficients of $1$, $x$, $x^{2}$)."]+st+
[r"The reduction used only the coefficient part, and that part became $I_3$ (a pivot in every column and every row). So for \emph{every} right-hand side the system has exactly one solution: existence of a solution for every polynomial means $\beta$ spans $P_2(\mathbb{R})$, and uniqueness (right-hand side $\mathbf 0$ gives only $\mathbf 0$) means $\beta$ is linearly independent. So $\beta$ is a basis and the coordinates are unique.",
 r"Therefore $[p]_\beta=(1,2,3)^{T}$; check: $1(1-x)+2(2+x^{2})+3(x+2x^{2})=(1+4)+(-1+3)x+(2+6)x^{2}=5+2x+8x^{2}$ \checkmark."],
r"$\beta$ is a basis, and $[p]_\beta=%s$."%vec(zlist([1,2,3])))

# 17 M2(C) over C and over R
S17=[[1,I,0,1],[I,-1,0,I],[0,1,1,0]]
A17=colsof(S17)
t,R,p=trace(M(A17)); assert p==[0,2] and col(R,1)==zlist([I,0,0,0])
add("C",I_,r"Let $A_1=\begin{pmatrix}1&i\\0&1\end{pmatrix}$, $A_2=\begin{pmatrix}i&-1\\0&i\end{pmatrix}$, $A_3=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ in $M_2(\mathbb{C})$. (a) Over $\mathbb{C}$, decide whether $\{A_1,A_2,A_3\}$ is linearly independent by row reducing, and give a basis of its span. (b) Regard $M_2(\mathbb{C})$ as a vector space over $\mathbb{R}$. Is $\{A_1,A_2,A_3\}$ linearly independent over $\mathbb{R}$? Prove your answer.",7.2,
[r"(a) Coordinates $(a_{11},a_{12},a_{21},a_{22})$: $A_1=(1,i,0,1)$, $A_2=(i,-1,0,i)$, $A_3=(0,1,1,0)$. Over $\mathbb{C}$ independence means $\alpha_1A_1+\alpha_2A_2+\alpha_3A_3=\mathbf 0$ forces $\alpha_1=\alpha_2=\alpha_3=0$, so put them as columns of $A=%s$ and reduce (arithmetic over $\mathbb{C}$, using $i^{2}=-1$)."%mat(M(A17))]+t+
[r"Column $2$ has no pivot (pivot columns $1$ and $3$). Column $2$ of the RREF is $%s$, so $A_2=i\,A_1$. Check: $i\begin{pmatrix}1&i\\0&1\end{pmatrix}=\begin{pmatrix}i&i^{2}\\0&i\end{pmatrix}=\begin{pmatrix}i&-1\\0&i\end{pmatrix}=A_2$ \checkmark."%cv([R[0][1],R[1][1],R[2][1],R[3][1]]),
 r"So over $\mathbb{C}$ the set is linearly dependent ($iA_1-A_2=0$), and $\{A_1,A_3\}$ (pivot columns $1,3$) is a basis of the span, of dimension $2$.",
 r"(b) Over $\mathbb{R}$ the scalars $x,y,z$ are real. Suppose $xA_1+yA_2+zA_3=0$ with $x,y,z\in\mathbb{R}$. The $(1,1)$ entry gives $x+iy=0$. A complex number $x+iy$ with $x,y$ real is $0$ only if $x=y=0$ (compare real and imaginary parts).",
 r"The $(2,1)$ entry gives $z=0$. So only the trivial combination works: $\{A_1,A_2,A_3\}$ is linearly independent over $\mathbb{R}$."],
r"(a) Dependent over $\mathbb{C}$: $A_2=iA_1$; basis $\{A_1,A_3\}$ of the span. (b) Independent over $\mathbb{R}$: $x+iy=0$ with $x,y$ real forces $x=y=0$, and the $(2,1)$ entry forces $z=0$.")

# ===================== PART D
add("D",I_,r"Let $V$ be a vector space with $\dim V=n$ and let $W$ be a subspace of $V$. Prove: (a) $W$ is finite-dimensional with $\dim W\le n$; (b) if $\dim W=n$ then $W=V$.",6.2,
[r"Tools: Dimension Bound (a linearly independent subset of $V$ has at most $n$ elements, since $V$ is spanned by $n$ vectors); Extension Lemma ($S$ independent, $x\notin\operatorname{span}S\Rightarrow S\cup\{x\}$ independent); an independent set of $n$ elements in $V$ is a basis.",
 r"(a) Any linearly independent subset of $W$ is a linearly independent subset of $V$, so it has at most $n$ elements. So the sizes of independent subsets of $W$ are bounded; choose an independent subset $S=\{w_1,\dots,w_m\}\subseteq W$ with $m$ as large as possible, $m\le n$ (the empty set is independent, so such $S$ exists).",
 r"Claim: $S$ spans $W$. If not, there is $x\in W$ with $x\notin\operatorname{span}S$. By the Extension Lemma $S\cup\{x\}$ is linearly independent, lies in $W$, and has $m+1$ elements, contradicting the maximality of $m$.",
 r"So $S$ is a basis of $W$: $W$ is finite-dimensional and $\dim W=m\le n$.",
 r"(b) If $\dim W=n$ then $S$ has $n$ elements and is linearly independent in $V$. Since $\dim V=n$, an independent set of $n$ elements is a basis of $V$, so $\operatorname{span}S=V$. But $\operatorname{span}S=W$. Hence $W=V$."],
r"Maximal independent subsets of $W$ have size $m\le n$ and are bases of $W$, so $\dim W\le n$; if $m=n$ the basis of $W$ is an independent $n$-set in $V$, hence a basis of $V$, so $W=V$.")

add("D",I_,r"Let $W_1,W_2$ be subspaces of a vector space $V$. (a) Prove that $W_1\cap W_2$ is a subspace of $V$. (b) Prove that $W_1\cup W_2$ is a subspace of $V$ if and only if $W_1\subseteq W_2$ or $W_2\subseteq W_1$.",6.4,
[r"(a) \emph{Zero:} $\mathbf 0\in W_1$ and $\mathbf 0\in W_2$ (both are subspaces), so $\mathbf 0\in W_1\cap W_2$.",
 r"\emph{Sums:} if $u,v\in W_1\cap W_2$ then $u,v\in W_1$, so $u+v\in W_1$; likewise $u+v\in W_2$. So $u+v\in W_1\cap W_2$. \emph{Scalars:} for $c$ in the field, $cu\in W_1$ and $cu\in W_2$, so $cu\in W_1\cap W_2$. Hence $W_1\cap W_2$ is a subspace.",
 r"(b) ($\Leftarrow$) If $W_1\subseteq W_2$ then $W_1\cup W_2=W_2$, a subspace. Similarly if $W_2\subseteq W_1$.",
 r"($\Rightarrow$) Suppose $W_1\cup W_2$ is a subspace and $W_1\not\subseteq W_2$. Then pick $u\in W_1$ with $u\notin W_2$. We show $W_2\subseteq W_1$. Let $w\in W_2$ be arbitrary.",
 r"Both $u$ and $w$ lie in $W_1\cup W_2$, a subspace, so $u+w\in W_1\cup W_2$. If $u+w\in W_2$, then $u=(u+w)-w\in W_2$ (as $w\in W_2$ and $W_2$ is a subspace), contradicting $u\notin W_2$. So $u+w\in W_1$.",
 r"Then $w=(u+w)-u\in W_1$ (as $u\in W_1$). Since $w\in W_2$ was arbitrary, $W_2\subseteq W_1$."],
r"(a) closure of $W_1,W_2$ gives closure of $W_1\cap W_2$ and $\mathbf 0\in W_1\cap W_2$. (b) $\Leftarrow$ trivial; $\Rightarrow$: if $u\in W_1\setminus W_2$ and $w\in W_2$ then $u+w\in W_1$, hence $w\in W_1$; so $W_2\subseteq W_1$.")

add("D",I_,r"Let $S_3$ be the set of symmetric matrices in $M_3(\mathbb{R})$ ($A^{T}=A$) and $K_3$ the set of skew-symmetric matrices ($A^{T}=-A$). Find a basis and the dimension of each, proving that your sets are bases.",7.4,
[r"\emph{Symmetric.} $A\in S_3$ means $a_{ij}=a_{ji}$ for all $i,j$. So $A$ is determined by $a_{11},a_{22},a_{33},a_{12},a_{13},a_{23}$ and $A=a_{11}E_{11}+a_{22}E_{22}+a_{33}E_{33}+a_{12}(E_{12}+E_{21})+a_{13}(E_{13}+E_{31})+a_{23}(E_{23}+E_{32})$.",
 r"So the six matrices $E_{11},E_{22},E_{33},E_{12}+E_{21},E_{13}+E_{31},E_{23}+E_{32}$ (each symmetric) span $S_3$. They are independent: in a combination equal to $0$, the entry in position $(1,1)$ is the coefficient of $E_{11}$, which must be $0$; likewise for $(2,2),(3,3)$; position $(1,2)$ is the coefficient of $E_{12}+E_{21}$, and $(1,3)$, $(2,3)$ give the other two. All six coefficients are $0$. So $\dim S_3=6$.",
 r"\emph{Skew-symmetric.} $a_{ij}=-a_{ji}$. For $i=j$: $a_{ii}=-a_{ii}$, so $2a_{ii}=0$ and $a_{ii}=0$ (we are over $\mathbb{R}$, where $2\neq0$). So $A$ is determined by $a_{12},a_{13},a_{23}$ and $A=a_{12}(E_{12}-E_{21})+a_{13}(E_{13}-E_{31})+a_{23}(E_{23}-E_{32})$.",
 r"So $E_{12}-E_{21},\ E_{13}-E_{31},\ E_{23}-E_{32}$ (each skew-symmetric) span $K_3$. They are independent: in a combination equal to $0$ the entries in positions $(1,2),(1,3),(2,3)$ are the three coefficients, so all are $0$. So $\dim K_3=3$.",
 r"Consistency check: $\dim S_3+\dim K_3=6+3=9=\dim M_3(\mathbb{R})$."],
r"$S_3$: basis $E_{11},E_{22},E_{33},E_{12}+E_{21},E_{13}+E_{31},E_{23}+E_{32}$, $\dim=6$. $K_3$: basis $E_{12}-E_{21},E_{13}-E_{31},E_{23}-E_{32}$, $\dim=3$.")

add("D",C,r"Let $W=\{A\in M_2(\mathbb{C}):\ A^{*}=A\}$ (here $A^{*}=\overline{A}^{\,T}$ is the conjugate transpose). (a) Show that $W$ is a vector space over $\mathbb{R}$ and find a basis and $\dim_{\mathbb{R}}W$. (b) Show that $W$ is \emph{not} a subspace of $M_2(\mathbb{C})$ over $\mathbb{C}$.",7.6,
[r"(a) Write $A=\begin{pmatrix}p&q\\r&s\end{pmatrix}$ with $p,q,r,s\in\mathbb{C}$. Then $A^{*}=\begin{pmatrix}\overline p&\overline r\\ \overline q&\overline s\end{pmatrix}$. So $A^{*}=A$ means $p=\overline p$, $s=\overline s$ and $q=\overline r$ (the $(2,1)$ condition $r=\overline q$ is the same). Hence $p,s\in\mathbb{R}$ and $r=\overline q$.",
 r"Subspace over $\mathbb{R}$: $(A+B)^{*}=A^{*}+B^{*}=A+B$ and, for real $c$, $(cA)^{*}=\overline cA^{*}=cA$, and $0^{*}=0$. So $W$ is closed under addition and real scalars and contains $0$.",
 r"Parametrize: $p=a$, $s=d$, $q=b+ci$ with $a,b,c,d\in\mathbb{R}$, so $r=\overline q=b-ci$. Then $A=\begin{pmatrix}a&b+ci\\ b-ci&d\end{pmatrix}=a\begin{pmatrix}1&0\\0&0\end{pmatrix}+d\begin{pmatrix}0&0\\0&1\end{pmatrix}+b\begin{pmatrix}0&1\\1&0\end{pmatrix}+c\begin{pmatrix}0&i\\-i&0\end{pmatrix}$.",
 r"So $H_1=\begin{pmatrix}1&0\\0&0\end{pmatrix}$, $H_2=\begin{pmatrix}0&0\\0&1\end{pmatrix}$, $H_3=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, $H_4=\begin{pmatrix}0&i\\-i&0\end{pmatrix}$ (all in $W$) span $W$ over $\mathbb{R}$.",
 r"Independence over $\mathbb{R}$: if $aH_1+dH_2+bH_3+cH_4=0$ with $a,b,c,d$ real, the diagonal gives $a=0$, $d=0$, and the $(1,2)$ entry gives $b+ci=0$, so $b=c=0$ (real and imaginary parts). So $\{H_1,H_2,H_3,H_4\}$ is a basis and $\dim_{\mathbb{R}}W=4$.",
 r"(b) $I_2\in W$ since $I_2^{*}=I_2$. But $i\,I_2=\begin{pmatrix}i&0\\0&i\end{pmatrix}$ has $(iI_2)^{*}=\begin{pmatrix}-i&0\\0&-i\end{pmatrix}=-iI_2\neq iI_2$. So $iI_2\notin W$: $W$ is not closed under multiplication by the complex scalar $i$, so it is not a complex subspace."],
r"(a) $W$ is a real vector space with basis $\begin{pmatrix}1&0\\0&0\end{pmatrix},\begin{pmatrix}0&0\\0&1\end{pmatrix},\begin{pmatrix}0&1\\1&0\end{pmatrix},\begin{pmatrix}0&i\\-i&0\end{pmatrix}$, $\dim_{\mathbb{R}}W=4$. (b) $I_2\in W$ but $(iI_2)^{*}=-iI_2\neq iI_2$.")

# 22 parameter k
for k in range(-6,7):
    G=M([[1,1,k],[1,k,1],[k,1,1]])
    pv=trace(G)[2]
    assert (len(pv)==3)==(k not in (1,-2))
add("D",C,r"For which real numbers $k$ is $\{(1,1,k),\ (1,k,1),\ (k,1,1)\}$ a basis of $\mathbb{R}^{3}$?",6.6,
[r"Three vectors in $\mathbb{R}^{3}$ form a basis exactly when they are linearly independent (an independent set of $\dim V=3$ elements is a basis), i.e.\ when the matrix with these columns has a pivot in every column. Row reduce, keeping $k$ as a symbol: $A=%s$."%r"\begin{pmatrix}1&1&k\\1&k&1\\k&1&1\end{pmatrix}",
 r"$R_2\to R_2-R_1,\ R_3\to R_3-kR_1$: $\begin{pmatrix}1&1&k\\0&k-1&1-k\\0&1-k&1-k^{2}\end{pmatrix}$.",
 r"$R_3\to R_3+R_2$: the $(3,3)$ entry becomes $(1-k^{2})+(1-k)=(1-k)\bigl((1+k)+1\bigr)=(1-k)(k+2)$, and the $(3,2)$ entry becomes $(1-k)+(k-1)=0$. So $\begin{pmatrix}1&1&k\\0&k-1&1-k\\0&0&(1-k)(k+2)\end{pmatrix}$.",
 r"Case $k=1$: the vectors are all $(1,1,1)$, so they are dependent (the matrix above has two zero rows). Not a basis.",
 r"Case $k\neq1$: the pivot $k-1$ in column $2$ is nonzero. Column $3$ has a pivot iff $(1-k)(k+2)\neq0$, i.e.\ iff $k\neq1$ and $k\neq-2$. So for $k\neq1$ there are three pivots iff $k\neq-2$.",
 r"Case $k=-2$: the third row is zero, so only two pivots. Directly, $(1,1,-2)+(1,-2,1)+(-2,1,1)=(0,0,0)$, a nontrivial relation, so they are dependent.",
 r"Check one value, $k=0$: the vectors $(1,1,0),(1,0,1),(0,1,1)$; the matrix above becomes $\begin{pmatrix}1&1&0\\0&-1&1\\0&0&2\end{pmatrix}$ with three pivots, a basis \checkmark."],
r"A basis exactly when $k\neq1$ and $k\neq-2$ (the pivots are $1,\ k-1,\ (1-k)(k+2)$).")

add("D",C,r"Let $V$ be a vector space with $\dim V=n$ and let $S\subseteq V$ have exactly $n$ elements. Prove: (a) if $S$ is linearly independent then $S$ is a basis of $V$; (b) if $S$ spans $V$ then $S$ is a basis of $V$. You may use: the Extension Lemma, the Dimension Bound, and that every basis of $V$ has exactly $n$ elements.",8.0,
[r"(a) Suppose $S$ is independent and, for contradiction, does not span $V$. Choose $x\in V$ with $x\notin\operatorname{span}S$.",
 r"By the Extension Lemma, $S\cup\{x\}$ is linearly independent. It has $n+1$ elements (note $x\notin S$ because $S\subseteq\operatorname{span}S$).",
 r"But $V$ is spanned by a basis, which has $n$ elements, so by the Dimension Bound every independent set in $V$ has at most $n$ elements. This contradicts $n+1$ elements. Hence $S$ spans $V$, and being independent, $S$ is a basis.",
 r"(b) Suppose $S=\{v_1,\dots,v_n\}$ spans $V$ and, for contradiction, is linearly dependent: $c_1v_1+\dots+c_nv_n=\mathbf 0$ with some $c_j\neq0$.",
 r"Since $c_j\neq0$ in a field we may divide: $v_j=-c_j^{-1}\sum_{i\neq j}c_iv_i$, so $v_j\in\operatorname{span}(S\setminus\{v_j\})$. Therefore $\operatorname{span}(S\setminus\{v_j\})=\operatorname{span}S=V$ (any combination using $v_j$ can be rewritten without it).",
 r"So $V$ is spanned by $n-1$ vectors. Then by the Dimension Bound every independent set in $V$ has at most $n-1$ elements; but a basis of $V$ is independent with $n$ elements. Contradiction. Hence $S$ is independent, and being spanning, a basis."],
r"(a) A non-spanning independent $n$-set extends to an independent $(n+1)$-set, exceeding the bound $n$. (b) A dependent spanning $n$-set can drop a vector and still span, so $V$ would be spanned by $n-1$ vectors, forcing independent sets to have at most $n-1$ elements, contradicting a basis of size $n$.")

add("D",C,r"Let $S$ be a linearly independent subset of a vector space $V$ and let $S'\subsetneq S$ be a proper subset. Prove that $\operatorname{span}(S')\neq\operatorname{span}(S)$.",5.4,
[r"Since $S'\neq S$ and $S'\subseteq S$, pick $v\in S$ with $v\notin S'$. Then $v\in\operatorname{span}(S)$.",
 r"Claim: $v\notin\operatorname{span}(S')$. Suppose instead $v=c_1s_1+\dots+c_ms_m$ with $s_1,\dots,s_m\in S'$ distinct (a combination of finitely many elements of $S'$; if $S'=\varnothing$ then $\operatorname{span}S'=\{\mathbf 0\}$ and $v=\mathbf 0$ is the empty combination).",
 r"Then $1\cdot v-c_1s_1-\dots-c_ms_m=\mathbf 0$ is a linear combination of distinct elements $v,s_1,\dots,s_m$ of $S$ (they are distinct because $v\notin S'$), and the coefficient of $v$ is $1\neq0$. This contradicts the linear independence of $S$. (If $S'=\varnothing$ the relation reads $v=\mathbf 0$, impossible because an independent set contains no zero vector.)",
 r"So $v\in\operatorname{span}(S)$ but $v\notin\operatorname{span}(S')$, hence the two spans differ."],
r"An element $v\in S\setminus S'$ lies in $\operatorname{span}S$; if it were in $\operatorname{span}S'$ we would get a nontrivial relation among elements of $S$, contradicting independence.")

add("D",C,r"Let $V$ be a vector space over $\mathbb{C}$ and $u,v,w\in V$. (a) Prove $\{u,v,w\}$ is linearly independent if and only if $\{u+v,\ u+w,\ v+w\}$ is. (b) Where did you use $2\neq0$? (c) Show that the statement fails over the field $\mathbb{F}_2=\{0,1\}$ (where $1+1=0$): give $u,v,w\in\mathbb{F}_2^{3}$.",8.6,
[r"Put $x=u+v$, $y=u+w$, $z=v+w$.",
 r"(a) ($\Rightarrow$) Assume $\{u,v,w\}$ independent. Suppose $\alpha x+\beta y+\gamma z=\mathbf 0$. Expand: $\alpha(u+v)+\beta(u+w)+\gamma(v+w)=(\alpha+\beta)u+(\alpha+\gamma)v+(\beta+\gamma)w=\mathbf 0$.",
 r"By independence of $u,v,w$: $\alpha+\beta=0$, $\alpha+\gamma=0$, $\beta+\gamma=0$. Subtracting the first two gives $\beta=\gamma$; then the third gives $2\beta=0$, so $\beta=0$ (here $2\neq0$ is used), hence $\gamma=0$ and $\alpha=0$. So $\{x,y,z\}$ is independent.",
 r"($\Leftarrow$) Assume $\{x,y,z\}$ independent. Solve for $u,v,w$: $x+y-z=(u+v)+(u+w)-(v+w)=2u$, so $u=\tfrac12(x+y-z)$; similarly $v=\tfrac12(x-y+z)$ and $w=\tfrac12(-x+y+z)$ (division by $2$ is allowed since $2\neq0$).",
 r"Suppose $au+bv+cw=\mathbf 0$. Substitute: $\tfrac12\bigl[(a+b-c)x+(a-b+c)y+(-a+b+c)z\bigr]=\mathbf 0$. By independence of $x,y,z$: $a+b-c=0$, $a-b+c=0$, $-a+b+c=0$. Adding the first two: $2a=0$, so $a=0$; adding the first and third: $2b=0$, so $b=0$; adding the last two: $2c=0$, so $c=0$. So $\{u,v,w\}$ is independent.",
 r"(b) $2\neq0$ was used to conclude $2\beta=0\Rightarrow\beta=0$ in ($\Rightarrow$), and to divide by $2$ and to cancel $2a=0$ in ($\Leftarrow$). In $\mathbb{C}$ (or $\mathbb{R}$) $2\neq0$ holds.",
 r"(c) In $\mathbb{F}_2^{3}$ take $u=e_1=(1,0,0)$, $v=e_2=(0,1,0)$, $w=e_3=(0,0,1)$: independent. Then $u+v=(1,1,0)$, $u+w=(1,0,1)$, $v+w=(0,1,1)$ and their sum is $(2,2,2)=(0,0,0)$ in $\mathbb{F}_2^{3}$. So $(u+v)+(u+w)+(v+w)=\mathbf 0$ is a nontrivial relation: $\{u+v,u+w,v+w\}$ is dependent although $\{u,v,w\}$ is independent."],
r"True over $\mathbb{C}$ (both directions need $2\neq0$). Over $\mathbb{F}_2$: $e_1,e_2,e_3$ are independent but $(e_1+e_2)+(e_1+e_3)+(e_2+e_3)=\mathbf 0$.")

add("D",I_,r"Let $S=\{v_1,\dots,v_n\}$ be a set of $n$ distinct vectors in a vector space $V$. Prove that $S$ is a basis of $V$ if and only if every vector of $V$ can be written \emph{uniquely} as $a_1v_1+\dots+a_nv_n$.",6.6,
[r"($\Rightarrow$) Let $S$ be a basis and $x\in V$. Since $S$ spans $V$, there are scalars with $x=\sum a_iv_i$ (existence).",
 r"Uniqueness: if also $x=\sum b_iv_i$, subtract: $\sum(a_i-b_i)v_i=\mathbf 0$. By linear independence every coefficient is $0$: $a_i=b_i$ for all $i$.",
 r"($\Leftarrow$) Assume every $x\in V$ has a unique representation. Existence of a representation for every $x$ says $\operatorname{span}S=V$, so $S$ spans.",
 r"Independence: $\mathbf 0=0\cdot v_1+\dots+0\cdot v_n$ is one representation of $\mathbf 0$. If $\sum c_iv_i=\mathbf 0$ is another, uniqueness gives $c_i=0$ for all $i$. So the only relation is the trivial one: $S$ is independent.",
 r"So $S$ spans and is independent: it is a basis."],
r"Spanning gives existence, independence gives uniqueness (subtract two representations); conversely existence is spanning, and uniqueness of the representation of $\mathbf 0$ is independence.")

add("D",C,r"Let $P(\mathbb{R})$ be the vector space of all real polynomials (of any degree). Prove that $P(\mathbb{R})$ is not finite-dimensional.",5.4,
[r"Suppose $P(\mathbb{R})$ has a finite basis with $m$ elements, so it is spanned by $m$ vectors.",
 r"Consider $T=\{1,x,x^{2},\dots,x^{m}\}\subseteq P(\mathbb{R})$, a set of $m+1$ polynomials.",
 r"$T$ is linearly independent: suppose $c_0+c_1x+\dots+c_mx^{m}=0$ as a polynomial. A nonzero polynomial of degree at most $m$ has at most $m$ roots, but the zero polynomial vanishes at every real number (infinitely many); so all $c_k=0$.",
 r"By the Dimension Bound, a linearly independent subset of a space spanned by $m$ vectors has at most $m$ elements. But $T$ is independent with $m+1$ elements. Contradiction.",
 r"Hence $P(\mathbb{R})$ is infinite-dimensional."],
r"$\{1,\dots,x^{m}\}$ is independent with $m+1>m$ elements: contradiction.")

# ============== examples
def ex(title,stmt,steps,ans): return (title,stmt,steps,ans)
EX=[]
EX.append(ex("Standard bases and dimensions",r"Prove that $\{1,x,x^{2}\}$ is a basis of $P_2(F)$ and that $\{E_{11},E_{12},E_{21},E_{22}\}$ is a basis of $M_2(F)$, for any field $F$. State the dimensions.",
 [r"$P_2(F)$ consists of the polynomials $a+bx+cx^{2}$ with $a,b,c\in F$. \emph{Spanning:} each such polynomial is $a\cdot1+b\cdot x+c\cdot x^{2}$, a combination of $1,x,x^{2}$.",
  r"\emph{Independence:} if $a\cdot1+b\,x+c\,x^{2}$ is the zero polynomial, all its coefficients are $0$, so $a=b=c=0$. Hence $\{1,x,x^{2}\}$ is a basis and $\dim P_2(F)=3$. In general $\dim P_n(F)=n+1$.",
  r"$M_2(F)$: $\begin{pmatrix}a&b\\c&d\end{pmatrix}=aE_{11}+bE_{12}+cE_{21}+dE_{22}$, so the four matrices span. If $aE_{11}+bE_{12}+cE_{21}+dE_{22}=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ is the zero matrix, then $a=b=c=d=0$, so they are independent.",
  r"So $\dim M_2(F)=4$. In general $\dim M_{m\times n}(F)=mn$, $\dim F^{n}=n$. None of these dimensions depends on which field $F$ is used (as long as the scalars are $F$)."],
 r"$\dim P_2(F)=3$ with basis $\{1,x,x^{2}\}$; $\dim M_2(F)=4$ with basis $\{E_{ij}\}$."))

Se=[[1,2,0],[0,1,1],[1,0,-2]]; Ae=colsof(Se)
t,R,p=trace(M(Ae)); assert p==[0,1] and col(R,2)[:2]==zlist([1,-2])
EX.append(ex("Is a set a basis of $\\mathbb{R}^{3}$?",r"Decide whether $\{(1,2,0),(0,1,1),(1,0,-2)\}$ is a basis of $\mathbb{R}^{3}$. If not, describe what it spans.",
 [r"Put the vectors in the columns: $A=%s$. Reduce."%mat(M(Ae))]+t+
 [r"Pivots are in columns $1$ and $2$ only; column $3$ has no pivot, so the vectors are linearly dependent. Column $3$ of the RREF is $%s$, so $v_3=1\cdot v_1-2\cdot v_2$. Check: $(1,2,0)-2(0,1,1)=(1,0,-2)$ \checkmark."%cv(col(R,2)[:2]),
  r"Three vectors that are dependent cannot be a basis. Since $v_1,v_2$ are independent (pivot columns) and span the same space, the set spans a $2$-dimensional subspace (a plane) of $\mathbb{R}^{3}$, with basis $\{(1,2,0),(0,1,1)\}$."],
 r"Not a basis: $v_3=v_1-2v_2$. The span is a plane with basis $\{(1,2,0),(0,1,1)\}$."))

st,a,nl,fr=cs([[1,1,1,1],[1,-1,1,-1]],ABCD,[r"Write $p(x)=a+bx+cx^{2}+dx^{3}$, coordinates $(a,b,c,d)$. Then $p(1)=a+b+c+d$ and $p(-1)=a-b+c-d$. The conditions give the homogeneous system $%s$."%sysbox(M([[1,1,1,1],[1,-1,1,-1]]),V(0,0),ABCD)],pol)
assert nl==[zlist([-1,0,1,0]),zlist([0,-1,0,1])]
EX.append(ex("Basis of a constraint subspace",r"Find a basis and the dimension of $W=\{p\in P_3(\mathbb{R}):\ p(1)=0,\ p(-1)=0\}$.",
 st+[r"Check: $q=-1+x^{2}$ has $q(1)=0$ and $q(-1)=0$ \checkmark; $r=-x+x^{3}$ has $r(1)=0$ and $r(-1)=0$ \checkmark."],a))

Sx=[[1,1,0],[0,1,1],[1,2,1],[1,0,-1]]; Ax=colsof(Sx)
t,R,p=trace(M(Ax)); assert p==[0,1] and col(R,2)[:2]==zlist([1,1]) and col(R,3)[:2]==zlist([1,-1])
EX.append(ex("Extracting a basis from a spanning set",r"The set $S=\{(1,1,0),(0,1,1),(1,2,1),(1,0,-1)\}$ spans a subspace $U$ of $\mathbb{R}^{3}$. Find a basis of $U$ chosen from $S$, and write the other vectors through it.",
 [r"The columns of $A=%s$ are the vectors of $S$. Reduce."%mat(M(Ax))]+t+
 [r"Pivot columns $1$ and $2$. Rule: the corresponding columns of the \emph{original} matrix form a basis of the span. So $\{(1,1,0),(0,1,1)\}$ is a basis of $U$ and $\dim U=2$.",
  r"Column $3$ of the RREF is $%s$: $v_3=v_1+v_2$; column $4$ is $%s$: $v_4=v_1-v_2$. Check: $(1,1,0)+(0,1,1)=(1,2,1)$ \checkmark and $(1,1,0)-(0,1,1)=(1,0,-1)$ \checkmark."%(cv(col(R,2)[:2]),cv(col(R,3)[:2]))],
 r"Basis $\{(1,1,0),(0,1,1)\}$, $\dim U=2$; $v_3=v_1+v_2$, $v_4=v_1-v_2$."))

Be=[[1,1,1,0,0],[1,2,3,0,0]]  # placeholder
v1_,v2_=[1,1,1],[1,2,3]
Aext=colsof([v1_,v2_,[1,0,0],[0,1,0],[0,0,1]])
t,R,p=trace(M(Aext),bar=2); assert p==[0,1,2]
EX.append(ex("Extending an independent set to a basis",r"Extend the linearly independent set $\{(1,1,1),(1,2,3)\}$ to a basis of $\mathbb{R}^{3}$ using standard basis vectors.",
 [r"Put $v_1,v_2$ followed by $e_1,e_2,e_3$ in the columns and reduce; keep the pivot columns (Extension Lemma: each kept vector is outside the span of those before it). $B=%s$."%mat(M(Aext),2)]+t+
 [r"The pivot columns are $1,2,3$. Column $3$ is $e_1$, so $\{(1,1,1),(1,2,3),(1,0,0)\}$ is a basis (three independent vectors in $\mathbb{R}^{3}$). Columns $4$ and $5$ ($e_2,e_3$) have no pivot: each is already in the span of the previous vectors.",
  r"Direct check that $e_1\notin\operatorname{span}\{v_1,v_2\}$: $a(1,1,1)+b(1,2,3)=(1,0,0)$ needs $a+2b=0$ and $a+3b=0$, so $b=0$, $a=0$, but then the first coordinate is $0\neq1$. Not in the span \checkmark."],
 r"$\{(1,1,1),(1,2,3),(1,0,0)\}$ is a basis of $\mathbb{R}^{3}$."))

Bc=[[1,1],[I,-I]]; bc=V(3,Z(1,1))
s=solve(M(Bc),bc); assert s[0]==[Z(2,Fr(-1,2)),Z(1,Fr(1,2))]
st,a=solve_steps(M(Bc),bc,['a','b'])
EX.append(ex("Coordinates in $\\mathbb{C}^{2}$",r"Show that $\beta=\{(1,i),(1,-i)\}$ is a basis of $\mathbb{C}^{2}$ over $\mathbb{C}$ and find $[w]_\beta$ for $w=(3,1+i)$.",
 [r"We need $a(1,i)+b(1,-i)=(3,1+i)$, i.e.\ $a+b=3$ and $ia-ib=1+i$. The matrix has the basis vectors as columns."]+st+
 [r"The coefficient part reduced to $I_2$ (a pivot in every row and column), so for every $w$ there is exactly one solution: $\beta$ spans and is independent, hence is a basis, and coordinates are unique.",
  r"So $[w]_\beta=(2-\tfrac12 i,\ 1+\tfrac12 i)^{T}$. Check: $a+b=3$ \checkmark and $i(a-b)=i(1-i)=i+1$ \checkmark."],
 r"$\beta$ is a basis and $[w]_\beta=\begin{pmatrix}2-\frac12 i\\ 1+\frac12 i\end{pmatrix}$."))

EX.append(ex("Counting arguments",r"Decide using dimensions only: (a) can $\{1,x\}$ span $P_2(\mathbb{R})$? (b) are three vectors in $\mathbb{C}^{2}$ (over $\mathbb{C}$) necessarily dependent? (c) can a set of $6$ vectors be a basis of $M_{2\times3}(\mathbb{R})$? (d) can $4$ independent vectors lie in a subspace of $\mathbb{R}^{5}$ of dimension $3$?",
 [r"(a) $\dim P_2(\mathbb{R})=3$ and a spanning set has at least $3$ vectors. $\{1,x\}$ has $2$, so it cannot span.",
  r"(b) $\dim_{\mathbb{C}}\mathbb{C}^{2}=2$, so $\mathbb{C}^{2}$ is spanned by $2$ vectors and every independent set has at most $2$ elements. So any $3$ vectors are dependent: yes.",
  r"(c) $\dim M_{2\times3}(\mathbb{R})=6$, so a basis has exactly $6$ elements. A set of $6$ vectors \emph{can} be a basis (it is a basis iff it is independent, or iff it spans); the count alone does not decide it.",
  r"(d) A subspace $U$ with $\dim U=3$ is spanned by $3$ vectors, so every independent set in $U$ has at most $3$ elements. $4$ independent vectors cannot lie in $U$: no."],
 r"(a) No. (b) Yes. (c) Possibly (count is consistent; check independence). (d) No."))

EX.append(ex("Proof: the Extension Lemma",r"Let $S$ be linearly independent in $V$ and $x\in V$ with $x\notin S$. Prove: $S\cup\{x\}$ is linearly independent if and only if $x\notin\operatorname{span}(S)$.",
 [r"($\Rightarrow$) We prove the contrapositive. Suppose $x\in\operatorname{span}(S)$: $x=c_1s_1+\dots+c_ms_m$ with $s_i\in S$. Then $1\cdot x-c_1s_1-\dots-c_ms_m=\mathbf 0$ is a relation among distinct elements of $S\cup\{x\}$ with coefficient $1\neq0$ on $x$. So $S\cup\{x\}$ is dependent.",
  r"($\Leftarrow$) Suppose $x\notin\operatorname{span}(S)$ and $\alpha x+c_1s_1+\dots+c_ms_m=\mathbf 0$ with $s_i\in S$ distinct. If $\alpha\neq0$, divide by $\alpha$ (possible in a field): $x=-\alpha^{-1}(c_1s_1+\dots+c_ms_m)\in\operatorname{span}(S)$, contradicting $x\notin\operatorname{span}(S)$.",
  r"So $\alpha=0$, leaving $c_1s_1+\dots+c_ms_m=\mathbf 0$. Since $S$ is independent, every $c_i=0$. All coefficients are $0$, so $S\cup\{x\}$ is independent."],
 r"A relation involving $x$ with $\alpha\neq0$ would put $x$ in $\operatorname{span}S$; if $x\notin\operatorname{span}S$ then $\alpha=0$ and independence of $S$ kills the rest."))

FACTS=r"""
\begin{tcolorbox}[colback=soft,colframe=ink,title={\bfseries Key Facts}]
\textbf{Basis.} A subset $S$ of a vector space $V$ is a \emph{basis} if it is linearly independent and spans $V$. Equivalently, every vector of $V$ can be written \emph{uniquely} as a linear combination of the vectors of $S$ (spanning gives existence, independence gives uniqueness). Independence and dimension depend on the field $F$ of scalars ($\mathbb{C}^{2}$ has dimension $2$ over $\mathbb{C}$ but $4$ over $\mathbb{R}$).

\textbf{Dimension.} $V$ is \emph{finite-dimensional} if it has a finite basis; then every basis has the same number of elements, called $\dim V$. Standard bases: $\{e_1,\dots,e_n\}$ for $F^{n}$ (dim $n$); $\{E_{ij}\}$ for $M_{m\times n}(F)$ (dim $mn$); $\{1,x,\dots,x^{n}\}$ for $P_n(F)$ (dim $n+1$). $P(\mathbb{R})$, all polynomials, is not finite-dimensional.

\textbf{Dimension Bound.} If $V$ is spanned by $n$ vectors, every linearly independent set in $V$ has at most $n$ elements. So in a space with $\dim V=n$: more than $n$ vectors are linearly dependent; fewer than $n$ vectors cannot span.

\textbf{Extension Lemma.} If $S$ is linearly independent and $x\notin S$, then $S\cup\{x\}$ is linearly independent iff $x\notin\operatorname{span}(S)$. A linearly independent set can be extended to a basis by adding vectors from a spanning set one at a time, each outside the current span; a finite spanning set can be shrunk to a basis by discarding vectors lying in the span of the others.

\textbf{Basis criterion.} If $\dim V=n$ and $S$ has $n$ elements, then $S$ is a basis iff $S$ is linearly independent iff $S$ spans $V$. If $W$ is a subspace of $V$ then $\dim W\le\dim V$, with equality only if $W=V$.

\textbf{Computing.} Translate vectors, polynomials and matrices into coordinate vectors with respect to a standard basis, then row reduce. The pivot columns of the \emph{original} matrix are a basis of the span of the columns; each non-pivot column of the RREF gives the coefficients of that column in terms of the pivot columns. A subspace defined by linear conditions on the coordinates is the solution set of a homogeneous system: its dimension is the number of free variables, and the vectors multiplying the free parameters form a basis.
\end{tcolorbox}
"""
if __name__=="__main__":
    from collections import Counter
    print(len(P),Counter(p[1] for p in P),len(EX))
    for i,p in enumerate(P,1): print(i,p[0],p[1][:3],"|",p[5][:110])
