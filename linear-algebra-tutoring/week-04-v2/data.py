from h4 import *
WEEK=4
TITLE=r"Row Reduction, Solving Linear Systems \& Bases from RREF"
HEADT=r"Row Reduction, Solving Linear Systems \& Bases from RREF"
FILE="LA-Week-04"
SECS=[("A","Echelon Forms and Row Reduction"),("B","Solving Linear Systems"),("C","Column Spaces, Relations and Proofs")]
P=[]
def add(sec,lvl,st,sp,steps,ans): P.append((sec,lvl,st,sp,steps,ans))
def rr(A,ncoef=None):
    t,R,p=trace(A,ncoef); return t,R,p
def mm(rows,nc=None): return mat(M(rows),nc)
X3=['x','y','z']; X4=['x','y','z','w']
# ================= A
Ma=[[1,0,2],[0,1,-1],[0,0,0]]; Mb=[[1,0,2],[0,1,0],[0,0,1]]; Mc=[[0,1,3],[1,0,2],[0,0,0]]; Md=[[1,3,0,2],[0,0,1,-1],[0,0,0,0]]
assert is_rref(M(Ma)) and is_ref(M(Mb)) and not is_rref(M(Mb)) and not is_ref(M(Mc)) and is_rref(M(Md))
add("A",F,r"Classify each matrix as: in RREF, in REF but not RREF, or neither. For every matrix that is not in RREF, name the condition it violates. $$\text{(a) }%s\quad \text{(b) }%s\quad\text{(c) }%s\quad\text{(d) }%s$$"%(mm(Ma),mm(Mb),mm(Mc),mm(Md)),3.0,
[r"Recall the two lists of conditions. \emph{REF:} zero rows are at the bottom, and the first nonzero entry (the \emph{leading entry}) of each row lies strictly to the right of the leading entry of the row above. \emph{RREF:} REF, plus every leading entry equals $1$, plus each leading entry is the only nonzero entry in its column.",
 r"(a) Leading entries: row 1 in column 1, row 2 in column 2, row 3 is a zero row at the bottom. They move right, so it is REF. Both leading entries are $1$. Column 1 has only the entry $1$ (others $0$). Column 2 has only the entry $1$. So (a) is in RREF.",
 r"(b) Leading entries sit in columns $1,2,3$, moving right, so it is REF. All leading entries are $1$. But column 3 contains the leading entry $1$ of row 3 and also the entry $2$ above it in row 1. A leading entry must be the \emph{only} nonzero entry in its column, so (b) is REF but \emph{not} RREF.",
 r"(c) Row 1 has its leading entry in column 2; row 2 has its leading entry in column 1, which is to the \emph{left} of the one above. The leading entries do not move to the right, so (c) is not even REF.",
 r"(d) Row 1 leads in column 1, row 2 leads in column 3, row 3 is zero and at the bottom: REF. Leading entries are $1$. Column 1 has no other nonzero entry; column 3 has only the $1$ (the entry above it is $0$; the $3$ and $2$ lie in non-pivot columns, which is allowed). So (d) is in RREF."],
r"(a) RREF. (b) REF only: the entry $2$ above the pivot in column 3 is nonzero. (c) Neither: leading entries do not move to the right. (d) RREF.")
A2=[[1,2,1],[2,5,3],[1,3,4]]
t,R,p=rr(M(A2)); assert p==[0,1,2]
add("A",F,r"Use elementary row operations to reduce $%s$ to RREF. Write each operation in the form $R_i\to R_i-cR_j$ and state the pivot columns."%mm(A2),4.2,
[r"Strategy: take each column in turn from the left, make its pivot equal to $1$, then clear every other entry in that column using the pivot row."]+t+[r"The matrix is now in RREF. It has a pivot in each of columns $1,2,3$."],
r"RREF $=%s$; pivot columns $1,2,3$."%mat(R))
A3=[[1,2,-1,3],[2,4,0,2],[1,2,1,-1]]
t,R,p=rr(M(A3)); assert p==[0,2]
add("A",I_,r"Reduce $%s$ to RREF. State the pivot columns and explain why column 2 is not a pivot column."%mm(A3),4.6,
[r"Work column by column. Column 1 already has a $1$ in the top position, so use it to clear below."]+t+[r"After clearing column 1, column 2 below row 1 is entirely $0$, so there is no pivot in column 2 (nothing available to turn into a leading entry). Move on to column 3: it has a nonzero entry in row 2, which becomes the pivot.",r"The matrix is in RREF with pivot columns $1$ and $3$."],
r"RREF $=%s$. Pivot columns $1,3$; column 2 has no pivot because, once column 1 is cleared, every entry of column 2 in rows $2$ and $3$ is $0$."%mat(R))
A4=[[0,2,4],[1,1,1],[2,0,-2]]
t,R,p=rr(M(A4)); 
add("A",I_,r"Reduce $%s$ to RREF. A row swap is needed: say why, and state the pivot columns."%mm(A4),4.6,
[r"The entry in position $(1,1)$ is $0$, so it cannot serve as a pivot. We must bring up a row whose first entry is nonzero: swap row 1 with row 2 (or row 3). The swap is an allowed elementary row operation and does not change the solution set of a system."]+t+[r"The matrix is now in RREF."],
r"RREF $=%s$; pivot columns %s."%(mat(R),",".join(str(c+1) for c in p)))
A5=[[1,I,0],[2,2*I,1],[1,I,1]]
t,R,p=rr(M(A5)); assert p==[0,2]
add("A",C,r"Over $\mathbb{C}$, reduce $%s$ to RREF. State the pivot columns."%mm(A5),4.2,
[r"Arithmetic over $\mathbb{C}$ follows the same rules; the only new fact needed is $i^{2}=-1$. Column 1 has a $1$ at the top, so clear below it. The multiples of $i$ in column 2 will be cleared automatically along with column 1."]+t+[r"Column 2 is zero below row 1 (it is $i$ times column 1), so it holds no pivot. Column 3 gives the second pivot."],
r"RREF $=%s$; pivot columns $1,3$."%mat(R))
add("A",C,r"(Why row reduction works.) Let $S'$ be obtained from a system $S$ by one elementary row operation $R_i\to R_i+\lambda R_j$ ($i\neq j$). Prove that $S$ and $S'$ have the same solutions.",5.0,
[r"Let the equations of $S$ be $E_1,\dots,E_m$ (each equation is an expression $E_k$ equal to a number $\beta_k$). $S'$ has the same equations except that $E_i$ is replaced by $E_i+\lambda E_j$ (and $\beta_i$ by $\beta_i+\lambda\beta_j$).",
 r"($\Rightarrow$) Suppose $\mathbf x$ solves every equation of $S$. Then $E_i(\mathbf x)=\beta_i$ and $E_j(\mathbf x)=\beta_j$. Hence $(E_i+\lambda E_j)(\mathbf x)=\beta_i+\lambda\beta_j$, so $\mathbf x$ also satisfies the new equation. All other equations are unchanged, so $\mathbf x$ solves $S'$.",
 r"($\Leftarrow$) Suppose $\mathbf x$ solves $S'$. Then it satisfies $E_j=\beta_j$ (unchanged) and $E_i+\lambda E_j=\beta_i+\lambda\beta_j$. Subtract $\lambda$ times the first from the second: $E_i(\mathbf x)=\beta_i$. So $\mathbf x$ solves $S$.",
 r"Both directions hold, so the solution sets are equal. The same argument (or the observation that each operation can be undone by another operation of the same kind) covers swaps and scaling by $c\neq0$."],
r"Each solution of $S$ solves $S'$, and subtracting $\lambda E_j$ recovers $E_i$, so each solution of $S'$ solves $S$; the solution sets are equal.")
# ================= B
Ab=[[1,1],[2,-1]]; bb=V(3,0)
st,a=solve_steps(M(Ab),bb,['x','y'])
add("B",F,r"Solve by row reduction: $%s$"%sysbox(M(Ab),bb,['x','y']),3.6,st,a)
Ab=[[1,1,2],[2,-1,1],[1,2,-1]]; bb=V(5,4,3)
s=solve(M(Ab),bb); assert s is not None and not s[1]
st,a=solve_steps(M(Ab),bb,X3)
add("B",F,r"Solve by row reduction: $%s$"%sysbox(M(Ab),bb,X3),5.0,st,a)
Ab=[[1,2,-1],[2,5,1]]; bb=V(4,9)
st,a=solve_steps(M(Ab),bb,X3)
add("B",I_,r"Solve: $%s$ Describe the solution set in parametric vector form."%sysbox(M(Ab),bb,X3),4.6,st,a)
Ab=[[1,2,1],[2,4,3],[1,2,-1]]; bb=V(1,3,2)
assert solve(M(Ab),bb) is None
st,a=solve_steps(M(Ab),bb,X3)
add("B",I_,r"Decide whether the system is consistent: $%s$"%sysbox(M(Ab),bb,X3),4.8,st,a)
Ab=[[1,1,1,1],[1,2,0,3]]; bb=V(2,5)
st,a=solve_steps(M(Ab),bb,X4)
add("B",I_,r"Solve $%s$ and identify the basic and free variables."%sysbox(M(Ab),bb,X4),4.6,st,a)
Ah=[[1,2,0,-1],[2,4,1,1],[1,2,1,2]]; bh=V(0,0,0)
st,a=solve_steps(M(Ah),bh,X4)
add("B",I_,r"Solve the homogeneous system $%s$ and write the solution set as a span."%sysbox(M(Ah),bh,X4),5.0,st,
 a+r" Equivalently the solution set is the span of the vectors multiplying the parameters (a subspace of $\mathbb{R}^{4}$; it always contains $\mathbf 0$).")
Ac=[[1,I],[I,2]]; bc=V(Z(1,1),I)
st,a=solve_steps(M(Ac),bc,['x','y'])
add("B",I_,r"Over $\mathbb{C}$, solve $\begin{cases}x+iy=1+i\\ ix+2y=i\end{cases}$",4.6,st,a)
# parameter problem (hand)
Ak=lambda k:[[1,1,1],[1,2,3],[1,3,k]]; bk=V(1,2,4)
for k in range(-3,9):
    A=M(Ak(k)); s=solve(A,bk) if True else None
    assert (s is None)==(k==5) and (s is not None and not s[1])==(k!=5)
add("B",C,r"For which real $k$ does the system $\begin{cases}x+y+z=1\\ x+2y+3z=2\\ x+3y+kz=4\end{cases}$ have (i) a unique solution, (ii) no solution, (iii) infinitely many solutions?",5.6,
[r"Write the augmented matrix and reduce, keeping $k$ as a symbol: $\displaystyle\left(\begin{array}{ccc|c}1&1&1&1\\1&2&3&2\\1&3&k&4\end{array}\right)$.",
 r"Apply $R_2\to R_2-R_1,\ R_3\to R_3-R_1$: $\displaystyle\left(\begin{array}{ccc|c}1&1&1&1\\0&1&2&1\\0&2&k-1&3\end{array}\right)$.",
 r"Apply $R_3\to R_3-2R_2$: $\displaystyle\left(\begin{array}{ccc|c}1&1&1&1\\0&1&2&1\\0&0&k-5&1\end{array}\right)$.",
 r"Read the last row: $(k-5)z=1$. If $k\neq5$ we can divide by $k-5$, so $z=\dfrac{1}{k-5}$; then $y$ and $x$ follow by back-substitution. There are three pivots, so the solution is unique.",
 r"If $k=5$ the last row reads $0=1$, a contradiction: no solution.",
 r"Infinitely many solutions would need a free variable and a consistent system. For $k=5$ the system is inconsistent, and for $k\neq5$ there is no free variable. So this never happens.",
 r"Check one value: $k=6$ gives $z=1$, then $y+2=1$ so $y=-1$, then $x-1+1=1$ so $x=1$; test in equation 3: $1+3(-1)+6(1)=4$ \checkmark."],
r"(i) unique solution for every $k\neq5$; (ii) no solution when $k=5$; (iii) never infinitely many.")
add("B",C,r"A homogeneous system has $m$ equations and $n$ unknowns with $n>m$. Prove it has a nonzero solution.",4.2,
[r"Reduce the $m\times n$ coefficient matrix to RREF. Each pivot occupies its own row and its own column, so there are at most $m$ pivots (one per row).",
 r"The coefficient matrix has $n$ columns and $n>m\ge$ (number of pivots). So at least $n-m\ge1$ columns contain no pivot; the variables in those columns are free.",
 r"A homogeneous system is always consistent (the zero vector solves it). Give one free variable the value $1$ (others $0$) and solve for the basic variables from the RREF rows. The resulting solution has a coordinate equal to $1$, so it is nonzero."],
r"At most $m$ pivot columns, so at least $n-m\ge1$ free variables; setting a free variable to $1$ gives a nonzero solution of the always-consistent homogeneous system.")
# ================= C
Rc=[[1,0,3,0,-2],[0,1,-1,0,4],[0,0,0,1,5]]
Rm=M(Rc); assert is_rref(Rm)
bc0=V(0,0,0)
sc=solve(Rm,bc0)
add("C",F,r"The matrix $R=%s$ is the RREF of the coefficient matrix of a homogeneous system. State the pivot columns, the basic and free variables (use $x_1,\dots,x_5$), and the general solution of $R\mathbf x=\mathbf 0$."%mm(Rc),4.6,
[r"Pivot columns are the columns containing a leading $1$: columns $1$, $2$ and $4$. So $x_1,x_2,x_4$ are basic and $x_3,x_5$ are free; set $x_3=s$, $x_5=t$.",
 r"Read the rows: row 1: $x_1+3x_3-2x_5=0$, so $x_1=-3s+2t$. Row 2: $x_2-x_3+4x_5=0$, so $x_2=s-4t$. Row 3: $x_4+5x_5=0$, so $x_4=-5t$.",
 r"Vector form: $\mathbf x=\begin{pmatrix}-3s+2t\\ s-4t\\ s\\ -5t\\ t\end{pmatrix}=s\begin{pmatrix}-3\\1\\1\\0\\0\end{pmatrix}+t\begin{pmatrix}2\\-4\\0\\-5\\1\end{pmatrix}$.",
 r"Check the first vector in row 1: $(-3)+3(1)-2(0)=0$ \checkmark; in row 2: $1-1+0=0$ \checkmark; in row 3: $0+0=0$ \checkmark."],
r"Pivots: columns $1,2,4$. Free: $x_3,x_5$. $\mathbf x=s(-3,1,1,0,0)^{T}+t(2,-4,0,-5,1)^{T}$.")
# bases from RREF
def colbasis(A,nm):
    Am=M(A); t,R,p=trace(Am)
    return t,R,p
Acb=[[1,2,0,1],[2,4,1,3],[1,2,1,2]]
t,R,p=colbasis(Acb,"A"); assert p==[0,2]
col=lambda A,j:[A[i][j] for i in range(len(A))]
Am=M(Acb); c1,c2,c3,c4=[col(Am,j) for j in range(4)]
a4=[R[0][3],R[1][3]]; assert [a4[0]*c1[i]+a4[1]*c3[i] for i in range(3)]==c4
assert [R[0][1]*c1[i] for i in range(3)]==c2
add("C",I_,r"Let $A=%s$. (a) Reduce $A$ to RREF. (b) Give a basis of the column space $\operatorname{col}(A)$ made of columns of $A$ itself. (c) Express each non-pivot column of $A$ as a linear combination of the pivot columns."%mm(Acb),6.0,
[r"(a) Row reduce."]+t+[r"The RREF has pivots in columns $1$ and $3$.",
 r"(b) Rule: the pivot columns of the \emph{original} matrix $A$ (not of the RREF) form a basis of $\operatorname{col}(A)$. So a basis is $\left\{%s,\ %s\right\}$."%(vec(c1),vec(c3)),
 r"(c) The entries of a non-pivot column of the RREF are the coefficients: column 2 of the RREF is $%s$, so $\text{col}_2=%s\,\text{col}_1$; column 4 of the RREF is $%s$, so $\text{col}_4=%s\,\text{col}_1+%s\,\text{col}_3$."%(vec(col(R,1)[:2]),tx(R[0][1]),vec(a4),tx(a4[0]),tx(a4[1])),
 r"Check column 4: $%s\cdot%s+%s\cdot%s=%s$ \checkmark."%(tx(a4[0]),vec(c1),tx(a4[1]),vec(c3),vec(c4))],
r"RREF $=%s$. Basis of $\operatorname{col}(A)$: $\{%s,%s\}$ (columns $1$ and $3$ of $A$); $\text{col}_2=2\,\text{col}_1$, $\text{col}_4=\text{col}_1+\text{col}_3$."%(mat(R),vec(c1),vec(c3)))
# row space basis
Ars=[[1,2,3],[2,4,7],[3,6,10]]
t,R,p=trace(M(Ars)); nz=[r for r in R if any(not z.iszero() for z in r)]
add("C",I_,r"For $A=%s$, reduce to RREF and give a basis of the row space $\operatorname{row}(A)$ and the number of pivots."%mm(Ars),5.0,
[r"Row operations replace each row by a combination of rows, and they can be reversed, so they do not change the span of the rows. Hence $\operatorname{row}(A)=\operatorname{row}(R)$ where $R$ is the RREF."]+t+[r"The nonzero rows of the RREF are linearly independent (each has a $1$ in a pivot column where all the others have $0$) and span the row space. So they form a basis."],
r"RREF $=%s$; basis of $\operatorname{row}(A)$: %s; the rank (number of pivots) is $%d$."%(mat(R),", ".join("$(%s)$"%",".join(tx(z) for z in r) for r in nz),len(nz)))
# span membership
vs=[[1,0,1],[2,1,0],[0,1,-2]]; w=[3,2,1]
Am=M([[vs[j][i] for j in range(3)] for i in range(3)])
s=solve(Am,V(*w))
add("C",I_,r"Decide whether $\mathbf w=(3,2,1)$ lies in $\operatorname{span}\{(1,0,1),(2,1,0),(0,1,-2)\}\subseteq\mathbb{R}^{3}$ by row reducing one augmented matrix. Give the coefficients if it does.",5.2,
solve_steps(Am,V(*w),['a','b','c'])[0][:1]+[r"(The columns are the three vectors; the right-hand side is $\mathbf w$.)"]+solve_steps(Am,V(*w),['a','b','c'])[0][1:],
(r"No: the system is inconsistent, so $\mathbf w\notin\operatorname{span}$." if s is None else solve_steps(Am,V(*w),['a','b','c'])[1]))
v4=[[1,2,1,0],[1,0,1,1],[2,1,0,1]]
Am=M([[1,1,2],[2,0,1],[1,1,0],[0,1,1]]); 
add("C",I_,r"Place the vectors $(1,2,1,0),\ (1,0,1,1),\ (2,1,0,1)$ of $\mathbb{R}^{4}$ as columns of a matrix. Use RREF to decide whether they are linearly independent.",5.0,
[r"Put the vectors in the columns of $A$; independence means $A\mathbf a=\mathbf 0$ has only the zero solution.",
 r"$A=%s$. Reduce it."%mat(Am)]+trace(Am)[0]+[r"Every column holds a pivot, so there are no free variables: the only solution of $A\mathbf a=\mathbf 0$ is $\mathbf a=\mathbf 0$."],
r"Linearly independent (a pivot in every column).")
assert trace(Am)[2]==[0,1,2]
# dependent four vectors in R^3 with relation
v=[[1,0,1],[1,1,0],[0,1,1],[2,3,1]]
Am=M([[v[j][i] for j in range(4)] for i in range(3)])
t,R,p=trace(Am); sol=solve(Am,V(0,0,0)); part,null,fr,pv=sol
assert len(null)==1
add("C",I_,r"Show that $(1,0,1),(1,1,0),(0,1,1),(2,3,1)$ in $\mathbb{R}^{3}$ are linearly dependent, and use RREF to find an explicit relation among them.",5.4,
[r"Four vectors in $\mathbb{R}^{3}$: the matrix with these columns is $3\times4$, so it cannot have a pivot in every column. Dependence is guaranteed; we now find a relation.",
 r"$A=%s$. Reduce it."%mat(Am)]+t+[r"Column %d has no pivot, so $a_%d$ is free: set $a_%d=1$. Solving the RREF rows gives the vector $%s$."%(fr[0]+1,fr[0]+1,fr[0]+1,vec(null[0])),
 r"So the relation is $(%s)v_1+(%s)v_2+(%s)v_3+(%s)v_4=\mathbf 0$. Check: $%s=%s$ \checkmark."%tuple([tx(z) for z in null[0]]+["+".join("(%s)%s"%(tx(null[0][j]),vec(v[j])) for j in range(4)),vec(matvec(Am,null[0]))])],
r"Dependent: $(%s)v_1+(%s)v_2+(%s)v_3+(%s)v_4=\mathbf 0$."%tuple(tx(z) for z in null[0]))
# poly/matrix set-up
add("C",I_,r"In $P_{2}(\mathbb{R})$, decide whether $q(x)=2+3x+x^{2}\in\operatorname{span}\{1+x,\ x+x^{2},\ 1+x^{2}\}$. Set up the system, reduce, and conclude.",5.4,
(lambda A,b:[r"We need $a,b,c$ with $a(1+x)+b(x+x^{2})+c(1+x^{2})=2+3x+x^{2}$. Expand and collect powers: $(a+c)+(a+b)x+(b+c)x^{2}$.",
 r"A polynomial equality means equal coefficients: constant $a+c=2$; $x$: $a+b=3$; $x^{2}$: $b+c=1$. In matrix form (columns are the coordinate vectors with respect to $1,x,x^{2}$)."]+solve_steps(M(A),V(*b),['a','b','c'])[0])([[1,0,1],[1,1,0],[0,1,1]],[2,3,1]),
solve_steps(M([[1,0,1],[1,1,0],[0,1,1]]),V(2,3,1),['a','b','c'])[1].replace("Unique solution","Yes, $q$ is in the span; the coefficients are")+r" That is, $q=2(1+x)+1(x+x^{2})+0(1+x^{2})$.")
# solution as p + null
add("C",C,r"Let $A\mathbf x=\mathbf b$ be consistent and let $\mathbf p$ be one solution. Prove that the solution set is exactly $\{\mathbf p+\mathbf h:\ A\mathbf h=\mathbf 0\}$.",4.8,
[r"Two inclusions. ($\supseteq$) Let $A\mathbf h=\mathbf 0$. Then $A(\mathbf p+\mathbf h)=A\mathbf p+A\mathbf h=\mathbf b+\mathbf 0=\mathbf b$, so $\mathbf p+\mathbf h$ is a solution.",
 r"($\subseteq$) Let $\mathbf x$ be any solution of $A\mathbf x=\mathbf b$. Put $\mathbf h=\mathbf x-\mathbf p$. Then $A\mathbf h=A\mathbf x-A\mathbf p=\mathbf b-\mathbf b=\mathbf 0$, and $\mathbf x=\mathbf p+\mathbf h$.",
 r"Both inclusions hold, so the sets are equal. (This is why the general solution always has the shape ``particular solution $+$ solution of the homogeneous system''.)"],
r"$A(\mathbf p+\mathbf h)=\mathbf b$ for each $\mathbf h$ in the null set, and any solution $\mathbf x$ equals $\mathbf p+(\mathbf x-\mathbf p)$ with $A(\mathbf x-\mathbf p)=\mathbf 0$.")
# consistency condition
Ac=[[1,2,-1],[2,3,1],[1,1,2]]
import random
for _ in range(30):
    a_,b_=random.randint(-5,5),random.randint(-5,5); c_=b_-a_+ (0 if random.random()<.5 else random.randint(1,3))
    s=solve(M(Ac),V(a_,b_,c_)); assert (s is not None)==(a_-b_+c_==0)
add("C",C,r"Find the condition on $a,b,c$ for the system $\begin{cases}x+2y-z=a\\ 2x+3y+z=b\\ x+y+2z=c\end{cases}$ to be consistent.",5.6,
[r"Row reduce the augmented matrix, carrying $a,b,c$ along: $\displaystyle\left(\begin{array}{ccc|c}1&2&-1&a\\2&3&1&b\\1&1&2&c\end{array}\right)$.",
 r"$R_2\to R_2-2R_1,\ R_3\to R_3-R_1$: $\displaystyle\left(\begin{array}{ccc|c}1&2&-1&a\\0&-1&3&b-2a\\0&-1&3&c-a\end{array}\right)$.",
 r"$R_3\to R_3-R_2$: $\displaystyle\left(\begin{array}{ccc|c}1&2&-1&a\\0&-1&3&b-2a\\0&0&0&(c-a)-(b-2a)\end{array}\right)$. The last right-hand side simplifies to $a-b+c$.",
 r"The last row says $0=a-b+c$. If $a-b+c\neq0$ this is a contradiction (inconsistent). If $a-b+c=0$ the row is $0=0$ and the system is consistent, with a free variable (infinitely many solutions).",
 r"Check: take $(a,b,c)=(1,3,2)$, which satisfies $1-3+2=0$. Then $x=1-2y+z$ from equation 1; with $z=0$: $x=1-2y$, equation 2: $2-4y+3y=3$, so $y=-1$, $x=3$; equation 3: $3-1+0=2$ \checkmark."],
r"Consistent if and only if $a-b+c=0$ (then infinitely many solutions); otherwise no solution.")
add("C",C,r"Let $R$ be the RREF of $A$. Prove that every non-pivot column of $R$ is a linear combination of the pivot columns of $R$, and explain why the same relation holds among the corresponding columns of $A$.",5.4,
[r"Let the pivot columns of $R$ be $j_1<\dots<j_r$. Column $j_k$ of $R$ is the standard vector $\mathbf e_k$ (a $1$ in row $k$, zeros elsewhere), because each pivot is $1$ and is the only nonzero entry in its column.",
 r"Any column $\mathbf c$ of $R$ has nonzero entries only in rows $1,\dots,r$ (rows below the last pivot are zero rows). So $\mathbf c=c_1\mathbf e_1+\dots+c_r\mathbf e_r=c_1R_{j_1}+\dots+c_rR_{j_r}$, where $c_k$ is the $k$-th entry of $\mathbf c$.",
 r"So a non-pivot column is the combination of pivot columns with its own entries as coefficients. Rewrite as a vector equation $\lambda_1 R_{1}+\dots+\lambda_n R_{n}=\mathbf 0$ (with a coefficient $-1$ on the non-pivot column): this is a solution of $R\boldsymbol\lambda=\mathbf 0$.",
 r"$A\boldsymbol\lambda=\mathbf 0$ and $R\boldsymbol\lambda=\mathbf 0$ have the same solutions, because row operations preserve solution sets (Problem 6). So the same coefficients give the same relation among the columns of $A$."],
r"Each non-pivot column of $R$ equals $\sum_k c_k\,\mathbf e_k$ with $\mathbf e_k$ a pivot column; the relation is a solution of $R\boldsymbol\lambda=\mathbf 0$, hence of $A\boldsymbol\lambda=\mathbf 0$.")
# ============== examples
def ex(title,stmt,steps,ans): return (title,stmt,steps,ans)
EX=[]
t,R,p=rr(M([[1,2,1],[2,5,3],[1,3,4]]))
EX.append(ex("Reducing a matrix to RREF",r"Reduce $%s$ to RREF."%mm([[1,2,1],[2,5,3],[1,3,4]]),
 [r"Go column by column. Column 1: the top entry is already $1$, so use it as the pivot and clear the entries below."]+t+[r"Every column has a pivot; the result is the identity matrix, which is in RREF."],r"RREF $=%s$."%mat(R)))
A_=[[1,1],[2,-1]]; b_=V(3,0)
st,a=solve_steps(M(A_),b_,['x','y'])
EX.append(ex("A system with a unique solution",r"Solve $%s$"%sysbox(M(A_),b_,['x','y']),st,a))
A_=[[1,2,-1,3],[1,3,0,5]]; b_=V(1,2)
st,a=solve_steps(M([r[:3] for r in [[1,1,1],[2,1,0]]]),V(3,3),X3)
EX.append(ex("A system with infinitely many solutions",r"Solve $%s$"%sysbox(M([[1,1,1],[2,1,0]]),V(3,3),X3),st,a))
Ai=[[1,1,2],[2,2,5],[1,1,0]]; bi=V(1,3,2)
assert solve(M(Ai),bi) is None
st,a=solve_steps(M(Ai),bi,X3)
EX.append(ex("An inconsistent system",r"Solve $%s$"%sysbox(M(Ai),bi,X3),st,a))
Ah2=[[1,1,0,2],[2,2,1,5]]
st,a=solve_steps(M(Ah2),V(0,0),X4)
EX.append(ex("A homogeneous system",r"Solve $%s$ and write the solution set as a span."%sysbox(M(Ah2),V(0,0),X4),st,a+r" The solution set is $\operatorname{span}$ of the two vectors above."))
Ae=[[1,3,0,2],[2,6,1,5],[1,3,1,3]]
t,R,p=trace(M(Ae)); Am=M(Ae)
c=lambda j:[Am[i][j] for i in range(3)]
rel=[R[0][1],R[0][3],R[1][3]]
assert [rel[0]*c(0)[i] for i in range(3)]==c(1) and [R[0][3]*c(0)[i]+R[1][3]*c(2)[i] for i in range(3)]==c(3)
EX.append(ex("Column space basis and column relations",r"For $A=%s$ find a basis of $\operatorname{col}(A)$ and express the other columns using it."%mm(Ae),
 [r"Reduce $A$ to RREF."]+t+[r"Pivot columns: %s. By the pivot-column rule, a basis of $\operatorname{col}(A)$ is formed by columns %s \emph{of the original $A$}: $\left\{%s,\ %s\right\}$."%(",".join(str(q+1) for q in p),",".join(str(q+1) for q in p),vec(c(p[0])),vec(c(p[1]))),
  r"The non-pivot columns of the RREF give the coefficients: column 2 of $R$ is $%s$, so $\text{col}_2=%s\,\text{col}_1$; column 4 of $R$ is $%s$, so $\text{col}_4=%s\,\text{col}_1+%s\,\text{col}_3$."%(vec(col(R,1)[:2]),tx(R[0][1]),vec([R[0][3],R[1][3]]),tx(R[0][3]),tx(R[1][3])) if p==[0,2] else ""],
 r"Basis $\{%s,%s\}$."%(vec(c(p[0])),vec(c(p[1])))))
Aq=[[1,I],[I,2]]; bq=V(Z(1,1),I)
st,a=solve_steps(M(Aq),bq,['x','y'])
EX.append(ex("A system over $\\mathbb{C}$",r"Solve $\begin{cases}x+iy=1+i\\ ix+2y=i\end{cases}$ over $\mathbb{C}$.",st,a))
EX.append(ex("Proof: row reduction does not change the solutions",r"Prove: swapping two equations, scaling an equation by $c\neq0$, or adding a multiple of one equation to another does not change the solution set.",
 [r"Swapping: the system is the same list of equations in a different order, and a vector solves a list of equations regardless of order.",
  r"Scaling $E_i$ by $c\neq0$: if $E_i(\mathbf x)=\beta_i$ then $(cE_i)(\mathbf x)=c\beta_i$. Conversely, if $(cE_i)(\mathbf x)=c\beta_i$, multiply both sides by $c^{-1}$ (possible because $c\neq0$ in a field) to recover $E_i(\mathbf x)=\beta_i$.",
  r"Adding $\lambda E_j$ to $E_i$: if $\mathbf x$ solves both $E_i,E_j$ it solves $E_i+\lambda E_j$. Conversely, if $\mathbf x$ solves $E_j$ and $E_i+\lambda E_j$, then $E_i(\mathbf x)=(E_i+\lambda E_j)(\mathbf x)-\lambda E_j(\mathbf x)=\beta_i$.",
  r"Each operation is undone by an operation of the same kind, so solutions are preserved in both directions."],
 r"The three operations preserve the solution set, so a system and its RREF have the same solutions."))
FACTS=r"""
\begin{tcolorbox}[colback=soft,colframe=ink,title={\bfseries Key Facts}]
\textbf{Elementary row operations.} (i) swap two rows $R_i\leftrightarrow R_j$; (ii) scale a row $R_i\to cR_i$ with $c\neq0$; (iii) add a multiple of one row to another $R_i\to R_i+\lambda R_j$. They do not change the solution set of a system, and they can be undone, so they do not change the span of the rows.

\textbf{REF and RREF.} A matrix is in \emph{row echelon form} (REF) if the zero rows are at the bottom and the first nonzero entry (the \emph{leading entry}) of each row lies strictly to the right of the leading entry of the row above. It is in \emph{reduced} row echelon form (RREF) if moreover every leading entry is $1$ and is the only nonzero entry in its column. The RREF of a matrix is unique. A \emph{pivot column} is a column containing a leading entry.

\textbf{Solving $A\mathbf x=\mathbf b$.} Reduce $\bigl(A\mid\mathbf b\bigr)$ to RREF. If a row reads $(0\ \cdots\ 0\mid1)$ the system is \emph{inconsistent}. Otherwise variables in pivot columns are \emph{basic}, the others are \emph{free}. No free variable: a unique solution. At least one free variable: infinitely many solutions, written as $\mathbf p+s\,\mathbf v_1+t\,\mathbf v_2+\cdots$ (parametric vector form).

\textbf{Homogeneous systems.} $A\mathbf x=\mathbf 0$ is always consistent ($\mathbf x=\mathbf 0$). Its solution set is a subspace, the span of the vectors multiplying the free parameters. If there are more unknowns than equations there is a free variable, hence a nonzero solution. If $\mathbf p$ solves $A\mathbf x=\mathbf b$, every solution is $\mathbf p+\mathbf h$ with $A\mathbf h=\mathbf 0$.

\textbf{Columns, rows and RREF.} The columns of $A$ at the pivot positions of its RREF form a basis of $\operatorname{col}(A)$ (take them from the original $A$, not from the RREF). The nonzero rows of the RREF form a basis of $\operatorname{row}(A)$. The entries of a non-pivot column of the RREF are the coefficients expressing that column of $A$ through the pivot columns. Vectors $v_1,\dots,v_k$ are independent exactly when the matrix with these columns has a pivot in every column.
\end{tcolorbox}
"""
if __name__=="__main__":
    from collections import Counter
    print(len(P),Counter((p[0],p[1]) for p in P),len(EX))
    for i,p in enumerate(P,1): print(i,p[0],p[1][:3],"|",p[5][:110])
