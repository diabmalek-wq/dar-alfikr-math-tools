import numpy as np, itertools, re, subprocess
rk=lambda M:np.linalg.matrix_rank(np.array(M,dtype=complex),tol=1e-9)
def nullity(M): M=np.array(M,dtype=complex); return M.shape[1]-rk(M)
ok=[]
def chk(name,c):
    ok.append(c); print(("PASS " if c else "FAIL ")+name)
# P3
chk("3 det=2 basis",abs(np.linalg.det(np.array([[1,1,0],[1,2,1],[0,1,3]]))-2)<1e-9)
# P4 dim_R C^2 =4: real embedding
def realify(vs): return [[z.real for z in v]+[z.imag for z in v] for v in vs]
B=[(1,0),(1j,0),(0,1),(0,1j)]
chk("4 real-indep rank 4",rk(realify(B))==4)
chk("4 {(1,0),(i,0)} complex dep rank1",rk([[1,0],[1j,0]])==1)
chk("4 {(1,0),(i,0)} real indep",rk(realify([(1,0),(1j,0)]))==2)
# B problems: constraint matrices & bases
def inb(cons,basis,n,dim):
    C=np.array(cons,dtype=complex); Bm=np.array(basis,dtype=complex)
    return np.allclose(C@Bm.T,0) and rk(Bm)==len(basis) and nullity(C)==dim==len(basis)
chk("5",inb([[1,-2,0]],[[2,1,0],[0,0,1]],3,2))
chk("6",inb([[1,0,0,1]],[[0,1,0,0],[0,0,1,0],[-1,0,0,1]],4,3))
chk("7",inb([[1,0,0,0],[1,1,1,1]],[[0,-1,1,0],[0,-1,0,1]],4,2))
chk("8",inb([[0,1,1,1],[1,2,4,8]],[[-2,-1,1,0],[-6,-1,0,1]],4,2))
chk("9",inb([[1,1,-1,0],[0,1,0,1]],[[1,0,1,0],[1,-1,0,1]],4,2))
chk("10",inb([[1,1j,0,0],[0,0,1,-1-1j]],[[-1j,1,0,0],[0,0,1+1j,1]],4,2))
chk("11",inb([[1,0,0,1],[0,1,-1,0]],[[0,1,1,0],[-1,0,0,1]],4,2))
# direct semantic checks of 7,8 as functions
p=lambda c,t:sum(ci*t**i for i,ci in enumerate(c))
chk("7 sem",all(abs(p(b,0))<1e-9 and abs(p(b,1))<1e-9 for b in [[0,-1,1,0],[0,-1,0,1]]))
chk("8 sem",all(abs(p(b,0)-p(b,1))<1e-9 and abs(p(b,2))<1e-9 for b in [[-2,-1,1,0],[-6,-1,0,1]]))
# polys: evaluate-functional rank independent of my cons matrices
ev=lambda t:[t**i for i in range(4)]
chk("7 dim via evals",nullity([ev(0),ev(1)])==2)
chk("8 dim via evals",nullity([np.array(ev(0))-np.array(ev(1)),ev(2)])==2)
# 12
A=np.array([[1,2,1],[2,4,2],[1,1,0]]).T
chk("12 rank2, v2=2v1, indep {v1,v3}",rk(A)==2 and np.allclose(A[:,1],2*A[:,0]) and rk(A[:,[0,2]])==2)
# 13
S=[[1,1,0],[2,2,0],[0,1,1],[1,2,1],[0,0,1]]; A=np.array(S).T
chk("13 rank3; cols1,3,5 indep; c4=c1+c3; c2=2c1",rk(A)==3 and rk(A[:,[0,2,4]])==3 and np.allclose(A[:,3],A[:,0]+A[:,2]) and np.allclose(A[:,1],2*A[:,0]))
# 14
A=np.array([[1,2,3],[3,2,1],[1,1,1]]).T
chk("14 rank2, v1+v2-4v3=0, {v1,v2} indep",rk(A)==2 and np.allclose(A[:,0]+A[:,1]-4*A[:,2],0) and rk(A[:,[0,1]])==2)
# 15
A1,A2,A3=[1,0,0,0],[0,1,1,0],[0,1,0,1]
E=np.eye(4)
res=[rk([A1,A2,A3,list(E[i])])==4 for i in range(4)]
chk("15 E11 fails, E12,E21,E22 work",res==[False,True,True,True])
chk("15 span constraint a12=a21+a22",all(abs(v[1]-v[2]-v[3])<1e-12 for v in [A1,A2,A3]))
# 16
Bm=np.array([[1,-1,0],[2,0,1],[0,1,2]]).T; sol=np.linalg.solve(Bm,[5,2,8])
chk("16 coords 1,2,3 and det!=0",np.allclose(sol,[1,2,3]) and abs(np.linalg.det(Bm))>1e-9)
# 17
A1=[1,1j,0,1];A2=[1j,-1,0,1j];A3=[0,1,1,0]
chk("17 complex rank 2, A2=iA1",rk([A1,A2,A3])==2 and np.allclose(np.array(A2),1j*np.array(A1)))
chk("17 real rank 3",rk(realify([A1,A2,A3]))==3)
# 20
def lin_nullity(f,n):
    cols=[]
    for k in range(n*n):
        X=np.zeros(n*n);X[k]=1;cols.append(f(X.reshape(n,n)).ravel())
    return n*n-np.linalg.matrix_rank(np.array(cols).T)
chk("20 dim sym 6, skew 3",lin_nullity(lambda X:X-X.T,3)==6 and lin_nullity(lambda X:X+X.T,3)==3)
# 21 hermitian real dim of 2x2
def herm(X):
    # X real 8-vector
    return None
cols=[]
for k in range(8):
    x=np.zeros(8);x[k]=1
    Z=(x[:4]+1j*x[4:]).reshape(2,2)
    D=Z-Z.conj().T
    cols.append(np.concatenate([D.real.ravel(),D.imag.ravel()]))
chk("21 real dim hermitian 2x2 =4",8-np.linalg.matrix_rank(np.array(cols).T)==4)
H=[np.array(m,dtype=complex) for m in ([[1,0],[0,0]],[[0,0],[0,1]],[[0,1],[1,0]],[[0,1j],[-1j,0]])]
chk("21 H_i hermitian & real-indep",all(np.allclose(h,h.conj().T) for h in H) and rk([[*h.ravel().real,*h.ravel().imag] for h in H])==4)
chk("21 iI not hermitian",not np.allclose(1j*np.eye(2),(1j*np.eye(2)).conj().T))
# 22
good=[]
for k in np.linspace(-6,6,241):
    M=np.array([[1,1,k],[1,k,1],[k,1,1]])
    d=np.linalg.det(M); pred=-(k-1)**2*(k+2)
    assert abs(d-pred)<1e-8
    good.append((abs(d)>1e-9)==(abs(k-1)>1e-9 and abs(k+2)>1e-9))
chk("22 det formula and basis iff k!=1,-2",all(good))
# 25 numeric check of equivalence over C for random vectors; and F2 counter
rng=np.random.default_rng(1)
okc=True
for _ in range(200):
    n=4; U=rng.integers(-2,3,(3,n)).astype(float)
    if rng.random()<.5: U[2]=U[0]*rng.integers(-2,3)+U[1]*rng.integers(-2,3)
    u,v,w=U; W=np.array([u+v,u+w,v+w])
    okc&=(rk(U)==3)==(rk(W)==3)
chk("25 random equivalence over R/C",okc)
e=np.eye(3,dtype=int)
chk("25 F2 counterexample",((e[0]+e[1])+(e[0]+e[2])+(e[1]+e[2]))%2 .tolist()==[0,0,0] if False else np.all(((e[0]+e[1])+(e[0]+e[2])+(e[1]+e[2]))%2==0))
# Examples
A=np.array([[1,2,0],[0,1,1],[1,0,-2]]).T
chk("Ex2 rank2 v3=v1-2v2",rk(A)==2 and np.allclose(A[:,2],A[:,0]-2*A[:,1]))
chk("Ex3 dim 2, basis -1+x^2, -x+x^3",inb([ev(1),ev(-1)],[[-1,0,1,0],[0,-1,0,1]],4,2))
A=np.array([[1,1,0],[0,1,1],[1,2,1],[1,0,-1]]).T
chk("Ex4 rank2, v3=v1+v2, v4=v1-v2",rk(A)==2 and np.allclose(A[:,2],A[:,0]+A[:,1]) and np.allclose(A[:,3],A[:,0]-A[:,1]))
chk("Ex5 basis incl e1, e1 not in span",rk([[1,1,1],[1,2,3],[1,0,0]])==3)
Bm=np.array([[1,1j],[1,-1j]]).T; w=np.linalg.solve(Bm,[3,1+1j])
chk("Ex6 coords 2-i/2, 1+i/2",np.allclose(w,[2-.5j,1+.5j]))
print("ALL OK" if all(ok) else "SOME FAILED")
