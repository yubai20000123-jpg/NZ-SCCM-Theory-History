"""NZ-SCCM RC1 adjoint-Clenshaw / General-D15 target gate reproducer.

No structural spatial/thickness numerical quadrature is used.
The low-order identity uses exact SymPy rational algebra and the closed D15
moment int_0^pi sin^(2m)X dX = pi*C(2m,m)/4^m.
The active Z0-Z6 part is a deterministic nested-composition degree preflight.
It intentionally does not allocate the forbidden giant flattened polynomial.
"""
import time
import sympy as sp

z=sp.symbols('z', real=True)


def beta_lens_poly(p,q,alpha,x):
    t=sp.symbols('t')
    bmax=sp.Rational(p,p+q)**p*sp.Rational(q,p+q)**q
    B=sp.expand(t**p*(1-t)**q/bmax)
    I=sp.integrate(B,(t,0,x))
    I1=sp.simplify(I.subs(x,1))
    return sp.expand(-1+2*(x+sp.Rational(alpha)*I)/(1+sp.Rational(alpha)*I1))


def cheb_comp(coeffs,g):
    if len(coeffs)==1:
        return sp.expand(coeffs[0])
    T0=sp.Integer(1); T1=sp.expand(g)
    out=coeffs[0]+coeffs[1]*T1
    for n in range(1,len(coeffs)-1):
        T2=sp.expand(2*g*T1-T0)
        out=sp.expand(out+coeffs[n+1]*T2)
        T0,T1=T1,T2
    return sp.expand(out)


def d15_exact(poly):
    """Exact one-coordinate D15 oracle for poly(z), z=sin^2 X."""
    P=sp.Poly(sp.expand(poly),z)
    ans=sp.Integer(0)
    for (m,),c in P.terms():
        ans += c*sp.pi*sp.binomial(2*m,m)/sp.Integer(4)**m
    return sp.simplify(ans)


def adjoint_cheb_target(coeffs,g,K,L):
    """Transpose of backward Clenshaw, acting on the target kernel."""
    N=len(coeffs)-1
    A=[sp.Integer(0) for _ in range(N+3)]
    ans=coeffs[0]*L(K)
    if N>=1:
        A[1]=sp.expand(g*K)
        A[2]=sp.expand(-K)
    for k in range(1,N+1):
        ans += coeffs[k]*L(A[k])
        A[k+1]=sp.expand(A[k+1]+2*g*A[k])
        A[k+2]=sp.expand(A[k+2]-A[k])
    return sp.simplify(ans),A


def low_order_exact_gate():
    # Deliberately small exact nested graph; all numbers are rational.
    s=sp.Rational(1,3)+sp.Rational(1,5)*z
    gate=beta_lens_poly(2,1,3,s)
    ccoef=[sp.Rational(1,7),-sp.Rational(2,5),sp.Rational(3,11),
           sp.Rational(1,13),-sp.Rational(1,17)]
    chat=cheb_comp(ccoef,gate)
    tcoord=sp.Rational(1,2)+sp.Rational(1,8)*chat
    twarp=beta_lens_poly(1,2,2,tcoord)
    ucoef=[sp.Rational(2,9),-sp.Rational(1,8),sp.Rational(1,10),sp.Rational(1,14)]
    u=cheb_comp(ucoef,twarp)
    K=1+2*z
    direct=d15_exact(K*u)
    adj,A=adjoint_cheb_target(ucoef,twarp,K,d15_exact)
    contributing=[int(sp.degree(A[k],z)) for k in range(1,len(ucoef))]
    return {
        'gate_degree':int(sp.degree(gate,z)),
        'chat_degree':int(sp.degree(chat,z)),
        'tension_warp_degree':int(sp.degree(twarp,z)),
        'final_nested_degree':int(sp.degree(u,z)),
        'direct_minus_adjoint':sp.simplify(direct-adj),
        'functional_over_pi':float(sp.N(direct/sp.pi,17)),
        'adjoint_contributing_target_degrees':contributing,
    }


CASES={
 'Z0':dict(level='L2',Ng=512,Nc=14,Nt=256,gate=(23,5),lenses=[(3,29),(29,2)]),
 'Z1':dict(level='L3',Ng=640,Nc=14,Nt=320,gate=(11,2),lenses=[(3,23)]),
 'Z2':dict(level='L2',Ng=512,Nc=14,Nt=256,gate=(23,5),lenses=[(3,29),(29,2)]),
 'Z3':dict(level='L2',Ng=512,Nc=14,Nt=256,gate=(17,3),lenses=[(3,22)]),
 'Z4':dict(level='L2',Ng=512,Nc=14,Nt=256,gate=(25,6),lenses=[(2,23),(22,5)]),
 'Z5':dict(level='L6',Ng=1024,Nc=14,Nt=512,gate=(16,7),lenses=[(1,27),(5,9)]),
 'Z6':dict(level='L7',Ng=1152,Nc=16,Nt=576,gate=(14,11),lenses=[(1,31),(4,15)]),
}


def complexity_row(name,c):
    dg=sum(c['gate'])+1
    dt=max(p+q+1 for p,q in c['lenses'])
    Dg=c['Ng']*dg
    DC=c['Nc']*Dg
    Dt=c['Nt']*dt
    Du=Dg*Dt
    DCC=3*DC
    DTC=DC+Du
    DTT=3*Du
    return dict(case=name,level=c['level'],Ng=c['Ng'],Nc=c['Nc'],Nt=c['Nt'],
                dg=dg,dt=dt,Dg=Dg,DC=DC,Dt_natural=Dt,DuR_DT7=Du,
                DCC=DCC,DTC=DTC,DTT=DTT,
                uR_1D_float64_GB=8*(Du+1)/1e9,
                DTT_1D_float64_GB=8*(DTT+1)/1e9)


if __name__=='__main__':
    print('FORMAL STRUCTURAL SPATIAL SAMPLING/QUADRATURE = 0')
    print('FORMAL THICKNESS QUADRATURE = 0')
    t0=time.perf_counter(); low=low_order_exact_gate(); dt=time.perf_counter()-t0
    print('LOW ORDER EXACT IDENTITY:',low)
    print('runtime_s=',dt)
    assert low['direct_minus_adjoint']==0
    print('\nACTIVE RC1 COMPOSITION PREFLIGHT')
    for name,c in CASES.items():
        print(complexity_row(name,c))
    print('\nDECISION: ADJOINT_CLENSHAW_LOW_ORDER=PASS_EXACT')
    print('DECISION: ACTIVE_RC1_TARGET_RUNTIME=FAIL_PREFLIGHT')
    print('DECISION: NEW_Pu=NOT_RUN')
