"""NZ-SCCM 2026-08-17 01:00 source-level regularization + real-target preflight.

Formal structural spatial/thickness quadrature = ZERO.
This reproducer does not compute Pu.
"""
import time
import sympy as sp

x,Y=sp.symbols('x Y', real=True)
I=sp.eye(2)
E=sp.Matrix([
    [sp.Rational(1,5)+x/3, sp.Rational(1,7)+x/5],
    [sp.Rational(1,7)+x/5, -sp.Rational(1,4)+2*x/7],
])
xstar=sp.Rational(21,260)


def smooth_regularization(eta):
    M=sp.expand(E*E)+eta**2*I
    A=sp.factor(sp.trace(M)); Q=sp.factor(M.det())
    disc=sp.factor(A**2-4*Q)
    Ms=sp.simplify(M.subs(x,xstar))
    r=sp.sqrt(sp.factor(Ms[0,0]))
    Mp=sp.diff(M,x).subs(x,xstar)
    Rp=sp.simplify(Mp/(2*r))  # Sylvester RR'+R'R=M'; R=rI at xstar
    return M,A,Q,disc,Ms,r,Rp


# ---------------------------------------------------------------------------
# Old four-state field, used only to prove a REAL compression target has
# algebraic degree <=4. Production is not authorized to canonicalize all
# rational coefficients of this representation.
# ---------------------------------------------------------------------------
def build_four_state(Q,A):
    basis=[(0,0),(1,0),(0,1),(1,1)]
    idx={b:i for i,b in enumerate(basis)}
    red={}
    def monomial(eq,es):
        d={(0,0):sp.Integer(1)}
        for _ in range(eq):
            nd={}
            for (iq,is_),c in d.items():
                if iq: key=(0,is_); f=Q
                else:  key=(1,is_); f=1
                nd[key]=nd.get(key,0)+c*f
            d=nd
        for _ in range(es):
            nd={}
            for (iq,is_),c in d.items():
                if not is_:
                    nd[(iq,1)]=nd.get((iq,1),0)+c
                else:
                    nd[(iq,0)]=nd.get((iq,0),0)+c*A
                    if iq: nd[(0,0)]=nd.get((0,0),0)+2*c*Q
                    else:  nd[(1,0)]=nd.get((1,0),0)+2*c
            d=nd
        return d
    for i,bi in enumerate(basis):
        for j,bj in enumerate(basis):
            rr=monomial(bi[0]+bj[0],bi[1]+bj[1])
            red[i,j]={idx[k]:v for k,v in rr.items()}
    e=[]
    for i in range(4):
        v=[0]*4; v[i]=1; e.append(v)
    def add(a,b): return [a[i]+b[i] for i in range(4)]
    def scale(a,c): return [c*z for z in a]
    def mul(a,b,canon=False):
        out=[0]*4
        for i,ai in enumerate(a):
            if ai==0: continue
            for j,bj in enumerate(b):
                if bj==0: continue
                for k,r in red[i,j].items(): out[k]+=ai*bj*r
        return [sp.cancel(z) for z in out] if canon else out
    def inv(a):
        MM=sp.Matrix.hstack(*[sp.Matrix(mul(a,e[j])) for j in range(4)])
        return [sp.cancel(z) for z in MM.inv()[:,0]]
    return e,add,scale,mul,inv


def real_compression_target_charpoly():
    # Retained rational exact prototype: kappa=2, eta=1/400.
    eta=sp.Rational(1,400); kappa=sp.Integer(2)
    M,A,Q,_,_,_,_=smooth_regularization(eta)
    e,add,scale,mul,inv=build_four_state(Q,A)
    one,q,s,qs=e
    invs=inv(s)
    def cst(z): return [z,0,0,0]
    def CM(Mat): return [[cst(Mat[i,j]) for j in range(2)] for i in range(2)]
    def MA(X,Z): return [[add(X[i][j],Z[i][j]) for j in range(2)] for i in range(2)]
    def MS(X,c): return [[scale(X[i][j],c) for j in range(2)] for i in range(2)]
    def MM(X,Z):
        out=[[None]*2 for _ in range(2)]
        for i in range(2):
            for j in range(2):
                w=cst(0)
                for k in range(2): w=add(w,mul(X[i][k],Z[k][j],True))
                out[i][j]=[sp.cancel(v) for v in w]
        return out
    def MI(): return [[cst(1 if i==j else 0) for j in range(2)] for i in range(2)]
    def DET(X): return [sp.cancel(z) for z in add(mul(X[0][0],X[1][1]),scale(mul(X[0][1],X[1][0]),-1))]
    def INV2(X):
        d=DET(X); di=inv(d)
        return [[mul(X[1][1],di,True),scale(mul(X[0][1],di,True),-1)],
                [scale(mul(X[1][0],di,True),-1),mul(X[0][0],di,True)]]

    Mc=CM(M); Ec=CM(E); E2=CM(sp.expand(E*E))
    qI=[[q if i==j else cst(0) for j in range(2)] for i in range(2)]
    Rnum=MA(Mc,qI)
    R=[[mul(Rnum[i][j],invs,True) for j in range(2)] for i in range(2)]
    RmE=MA(R,MS(Ec,-1))
    Minv=CM(sp.simplify(M.inv()))
    cmat=MS(MM(MM(E2,RmE),Minv),sp.Rational(1,2))
    c2=MM(cmat,cmat)
    Den=MA(MI(),c2)               # kappa-2=0 in retained prototype
    C=MS(MM(cmat,INV2(Den)),kappa)
    detC=DET(C)
    target=mul(detC,C[1][1],True) # actual Syy subtarget det(C)*Cyy
    Mtarget=sp.Matrix.hstack(*[sp.Matrix(mul(target,e[j])) for j in range(4)])
    t0=time.time(); cp=Mtarget.charpoly(Y).as_expr(); dt=time.time()-t0
    P=sp.Poly(cp,Y)
    return target,P,dt


def source_spline_c2():
    z,rho,H,U=sp.symbols('z rho H U')
    p1=rho*z+(10*H-6*rho)*z**3+(8*rho-15*H)*z**4+(6*H-3*rho)*z**5
    s=(z-1)/9
    p2=H+(U-H)*(10*s**3-15*s**4+6*s**5)
    j1=[sp.simplify(sp.diff(p1,z,n).subs(z,1)-sp.diff(p2,z,n).subs(z,1)) for n in range(3)]
    j10=[sp.simplify(sp.diff(p2,z,n).subs(z,10)-(U if n==0 else 0)) for n in range(3)]
    return j1,j10


def main():
    M,A,Q,disc,Ms,r,Rp=smooth_regularization(sp.Rational(1,400))
    print('FORMAL_COUNTERS sampling=0 quadrature=0 subdomains=1 thickness_quadrature=0')
    print('Z6_BOUNDARY=SSSS')
    print('xstar=',xstar)
    print('A^2-4Q=',disc)
    print('M(xstar)=',Ms)
    print('R_scalar=',sp.N(r,20))
    print('Sylvester_eigenvalues=',[sp.N(2*r,20)]*4)
    print('Sylvester_cond2=1 exactly')
    print('Rprime=',sp.N(Rp,18))

    # Actual Case21 eta at the same algebraic repeated-eigenvalue point.
    kappa=sp.Rational(386099,193000); eta=sp.Rational(965,386099)
    _,_,_,_,Mcase,rcase,_=smooth_regularization(eta)
    print('Case21_kappa=',kappa,sp.N(kappa,20))
    print('Case21_eta=',eta,sp.N(eta,20))
    print('Case21_R_scalar_at_xstar=',sp.N(rcase,20))
    print('Case21_Sylvester_eigenvalue=',sp.N(2*rcase,20))

    j1,j10=source_spline_c2()
    print('SOURCE_SPLINE_C2_JUMP_AT_1=',j1)
    print('SOURCE_SPLINE_C2_JUMP_AT_10=',j10)
    print('PROJECTOR_FREE_POSITIVE_PART= ((D+sqrt(D^2))/2)^p, p=3,4,5')

    target,P,dt=real_compression_target_charpoly()
    print('REAL_TARGET=det(C)*Cyy')
    print('REAL_TARGET_FIELD_SUPPORT=',sum(z!=0 for z in target),'/4')
    print('REAL_TARGET_CHARPOLY_DEGREE_Y=',P.degree())
    print('REAL_TARGET_CHARPOLY_BUILD_SECONDS=',dt)
    print('REAL_TARGET_CHARPOLY_COEFF_OPS=',[sp.count_ops(c) for c in P.all_coeffs()])
    print('EXPLICIT_RATIONAL_ANNIHILATOR_CANONICALIZATION=REJECTED_AFTER_60S_FAIL_FAST')
    print('NEW_Pu=NOT_RUN')

if __name__=='__main__':
    main()
