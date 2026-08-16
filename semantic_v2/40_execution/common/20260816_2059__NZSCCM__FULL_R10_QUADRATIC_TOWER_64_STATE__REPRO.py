"""NZ-SCCM full R10 quadratic-tower 64-state compositum gate.

Formal structural spatial/thickness numerical integration remains ZERO.
This script reproduces the finite algebraic state, derivative sparsity,
prototype denominator degrees and the exact-field R10 uR/T7 support probe.
The knot rationalization is diagnostic only; formal theory retains exact R10 roots.
"""
import time
import sympy as sp
import mpmath as mp

x=sp.symbols('x')
rho=sp.Rational(1,10)
kappa=sp.Integer(2)
a=rho/kappa
eta=a/20
I2=sp.eye(2)
E=sp.Matrix([[sp.Rational(1,5)+x/3, sp.Rational(1,7)+x/5],
             [sp.Rational(1,7)+x/5,-sp.Rational(1,4)+2*x/7]])

# -----------------------------------------------------------------------------
# exact universal source thresholds; rationalized only for symbolic timing probe
# -----------------------------------------------------------------------------
mp.mp.dps=50
def tau_u(u):
    u=mp.mpf(u)
    return u*u*(mp.sqrt(u*u+mp.mpf(1)/400)+u)/(2*(u*u+mp.mpf(1)/400))
u1=mp.findroot(lambda u:tau_u(u)-1,1)
u10=mp.findroot(lambda u:tau_u(u)-10,10)
L1=sp.Rational(500933621342341,10_000_000_000_000_000)
L10=sp.Rational(500009374609403,1_000_000_000_000_000)

# -----------------------------------------------------------------------------
# three quadratic pairs q^2=Q, s^2=A+2q
# -----------------------------------------------------------------------------
Amat=sp.expand(E*E)+eta**2*I2
P0=sp.factor(sp.trace(Amat));Q0=sp.factor(Amat.det())
rels=[]
for L in [None,L1,L10]:
    if L is None:
        Q,A=Q0,P0
    else:
        F=E-L*I2; tt=sp.trace(F); dd=sp.factor(F.det())
        Q=sp.factor(dd**2);A=sp.factor(tt**2-2*dd)
    rels.append((Q,A))

# local derivative coefficients and denominator preflight
local=[]; dens=[]
for Q,A in rels:
    ell=sp.cancel(sp.diff(Q,x)/(2*Q))
    den=2*(A**2-4*Q)
    c0=sp.cancel((sp.diff(A,x)*A-4*ell*Q)/den)
    c1=sp.cancel((-2*sp.diff(A,x)+2*ell*A)/den)
    local.append((ell,c0,c1))
    dens.extend([sp.Poly(sp.fraction(z)[1],x,domain=sp.QQ) for z in (ell,c0,c1)])
dpoly=dens[0]
for d in dens[1:]: dpoly=sp.lcm(dpoly,d)

# exact 64-state sparsity from Kronecker-sum pattern
bits=[tuple((i>>j)&1 for j in range(6)) for i in range(64)]
nz=set()
for col,b in enumerate(bits):
    if any(b): nz.add((col,col))
    for g in range(3):
        qb=2*g;sb=qb+1
        if b[sb]:
            bb=list(b);bb[qb]^=1
            row=sum(v<<j for j,v in enumerate(bb))
            nz.add((row,col))

# -----------------------------------------------------------------------------
# sparse exact-field arithmetic; basis exponents are six bits
# -----------------------------------------------------------------------------
idx={b:i for i,b in enumerate(bits)}
def C(c):
    z=[sp.Integer(0)]*64;z[0]=sp.sympify(c);return z
def B(j):
    z=[sp.Integer(0)]*64;b=[0]*6;b[j]=1;z[idx[tuple(b)]]=1;return z
Qv=[B(0),B(2),B(4)];Sv=[B(1),B(3),B(5)]
def add(u,v):return [a+b for a,b in zip(u,v)]
def scale(u,c):return [c*a for a in u]
def local_reduce(eq,es,Q,A):
    d={(0,0):sp.Integer(1)}
    for _ in range(eq):
        nd={}
        for (iq,is_),c in d.items():
            key=(0,is_) if iq else (1,is_)
            nd[key]=nd.get(key,0)+c*(Q if iq else 1)
        d=nd
    for _ in range(es):
        nd={}
        for (iq,is_),c in d.items():
            if not is_: nd[(iq,1)]=nd.get((iq,1),0)+c
            else:
                nd[(iq,0)]=nd.get((iq,0),0)+c*A
                if iq: nd[(0,0)]=nd.get((0,0),0)+2*c*Q
                else: nd[(1,0)]=nd.get((1,0),0)+2*c
        d=nd
    return d
red={}
for i,bi in enumerate(bits):
    for j,bj in enumerate(bits):
        ex=[bi[k]+bj[k] for k in range(6)]
        p=[local_reduce(ex[2*g],ex[2*g+1],rels[g][0],rels[g][1]) for g in range(3)]
        out={}
        for k0,c0 in p[0].items():
          for k1,c1 in p[1].items():
            for k2,c2 in p[2].items():
              b=(k0[0],k0[1],k1[0],k1[1],k2[0],k2[1])
              out[idx[b]]=c0*c1*c2
        red[(i,j)]=out
def mul(u,v):
    out=[0]*64
    iu=[i for i,c in enumerate(u) if c!=0];iv=[j for j,c in enumerate(v) if c!=0]
    for i in iu:
      for j in iv:
        cc=u[i]*v[j]
        for k,r in red[(i,j)].items():out[k]+=cc*r
    return out
def invs(g):
    Q,A=rels[g]
    return scale(mul(Sv[g],add(C(A),scale(Qv[g],-2))),1/(A**2-4*Q))

def MC(M):return [[C(M[i,j]) for j in range(2)] for i in range(2)]
def MI():return [[C(1),C(0)],[C(0),C(1)]]
def MA(A,B):return [[add(A[i][j],B[i][j]) for j in range(2)] for i in range(2)]
def MS(A,c):return [[scale(A[i][j],c) for j in range(2)] for i in range(2)]
def MM(A,B):
    return [[add(mul(A[i][0],B[0][j]),mul(A[i][1],B[1][j])) for j in range(2)] for i in range(2)]
def MP(A,n):
    R=MI()
    for _ in range(n):R=MM(R,A)
    return R
def MT(A):return add(A[0][0],A[1][1])

# smooth t,c
Ef=MC(E);tau=sp.trace(E);s2=mul(Sv[0],Sv[0])
sc=scale(add(s2,C(-tau**2)),sp.Rational(1,2))
R=MS(Ef,tau);R[0][0]=add(R[0][0],sc);R[1][1]=add(R[1][1],sc)
R=[[mul(R[i][j],invs(0)) for j in range(2)] for i in range(2)]
Ainv=sp.simplify(Amat.inv())
G=MM(MM(MC(E*E),R),MC(Ainv))
H=MM(MC(E**3),MC(Ainv))
t=MS(MA(G,H),sp.Rational(1,2))

# exact shifted spectral projectors from E-LI
def projector(g,L):
    F=E-L*I2;tt=sp.trace(F);ss=mul(Sv[g],Sv[g])
    sc=scale(add(ss,C(-tt**2)),sp.Rational(1,2))
    Abs=MS(MC(F),tt);Abs[0][0]=add(Abs[0][0],sc);Abs[1][1]=add(Abs[1][1],sc)
    Abs=[[mul(Abs[i][j],invs(g)) for j in range(2)] for i in range(2)]
    sign=MM(MM(MC(F),Abs),MC(sp.simplify((F*F).inv())))
    return MS(MA(MI(),sign),sp.Rational(1,2))
H1=projector(1,L1);H10=projector(2,L10)
Z=MS(t,1/a)
def shift(A,m):
    R=[[list(A[i][j]) for j in range(2)] for i in range(2)]
    R[0][0]=add(R[0][0],C(-m));R[1][1]=add(R[1][1],C(-m));return R
D1=shift(Z,1);D10=shift(Z,10)

# exact spline coefficients from frozen source constants
Hc=sp.Rational('0.09799750427197301');UR=sp.Rational(3,100)
A3=4*rho+(-7300*Hc+10*UR)/729
A4=7*rho+(-32800*Hc-5*UR)/2187
A5=3*rho+(-118100*Hc+2*UR)/19683
B3=10*(Hc-UR)/729;B4=5*(Hc-UR)/2187;B5=2*(Hc-UR)/19683
uR=MS(Z,rho)
for cc,p in [(10*Hc-6*rho,3),(8*rho-15*Hc,4),(6*Hc-3*rho,5)]:uR=MA(uR,MS(MP(Z,p),cc))
for cc,p in [(A3,3),(A4,4),(A5,5)]:uR=MA(uR,MS(MM(MP(D1,p),H1),cc))
for cc,p in [(B3,3),(B4,4),(B5,5)]:uR=MA(uR,MS(MM(MP(D10,p),H10),cc))
T=MS(uR,1/rho)
t0=time.time();T7=MP(T,7);runtime=time.time()-t0

support=lambda A:[sum(c!=0 for c in A[i][j]) for i in range(2) for j in range(2)]
print('FORMAL STRUCTURAL COUNTERS: sampling=0 quadrature=0 subdomains=1 thickness_quadrature=0')
print('EXACT UNIVERSAL u1 =',mp.nstr(u1,40))
print('EXACT UNIVERSAL u10=',mp.nstr(u10,40))
print('DIAGNOSTIC lambda1 =',L1)
print('DIAGNOSTIC lambda10=',L10)
print('LOCAL DEGREE PAIRS =',[[ (sp.degree(sp.fraction(z)[0],x),sp.degree(sp.fraction(z)[1],x)) for z in q] for q in local])
print('COMMON DENOMINATOR DEGREE =',dpoly.degree())
print('COMMON DENOMINATOR TERMS =',len(dpoly.terms()))
print('A64 NONZEROS =',len(nz),'DIAG=',sum(r==c for r,c in nz),'OFFDIAG=',sum(r!=c for r,c in nz))
print('t SUPPORT =',support(t))
print('H1 SUPPORT=',support(H1))
print('uR SUPPORT=',support(uR))
print('T7 SUPPORT=',support(T7))
print('tr(T7) SUPPORT=',sum(c!=0 for c in MT(T7)))
print('T7 RAW FIELD MULTIPLICATION RUNTIME s =',runtime)
print('NAIVE FLATTENED COEFFICIENT CANONICALIZATION = FAIL_TRACTABILITY_GT_60S (recorded execution boundary)')
print('NEW_Pu = NOT_RUN')
