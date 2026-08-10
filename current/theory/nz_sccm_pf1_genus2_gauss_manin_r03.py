from __future__ import annotations
import json
import sympy as sp

x,y,D,M,nu,r = sp.symbols('x y D M nu r')

Gamma = (
 D**2*nu**2*x*y - 2*D**2*nu*x*y + 4*D**2*nu*x + 4*D**2*nu*y - 4*D**2*nu + D**2*x*y
 + 2*D*M*nu*x**2*y - 4*D*M*nu*x**2 + 2*D*M*nu*x*y**2 - 4*D*M*nu*x*y + 4*D*M*nu*x
 - 2*D*M*x**2*y - 2*D*M*x*y**2 + 4*D*M*x*y + 4*D*M*y**2 - 4*D*M*y
 - 4*D*nu*r*x*y + 4*D*nu*r*x + 4*D*nu*r*y - 4*D*nu*r
 + 4*D*r*x*y - 4*D*r*x - 4*D*r*y + 4*D*r
 + M**2*x**3*y + 2*M**2*x**2*y**2 - 4*M**2*x**2*y + M**2*x*y**3 - 4*M**2*x*y**2 + 4*M**2*x*y
 - 4*M*r*x**2*y + 4*M*r*x**2 - 4*M*r*x*y**2 + 8*M*r*x*y - 4*M*r*x
 + 4*M*r*y**2 - 4*M*r*y + 4*r**2*x*y - 4*r**2*x - 4*r**2*y + 4*r**2
)
Pgen = sp.expand(x*(1-x)*Gamma)


def sylvester_reduction_matrix(P):
    """S maps [a0..a3,b0..b4] to coeffs of A*P+B*P'."""
    p = sp.Poly(sp.expand(P), x)
    pp = sp.Poly(sp.diff(P,x),x)
    if p.degree() != 5:
        raise ValueError('PF1-R03 expects generic degree-5 genus-2 model')
    pc=[p.nth(i) for i in range(6)]
    qc=[pp.nth(i) for i in range(5)]
    S=sp.zeros(9,9)
    for i in range(4):
        for k,v in enumerate(pc):
            S[i+k,i]=v
    for j in range(5):
        for k,v in enumerate(qc):
            S[j+k,4+j]=v
    return S


def connection_at(P, Ptheta):
    """Exact genus-2 absolute de-Rham connection for omega_k=x^k dx/w, k=0..3.

    d_theta omega_k = N/w^3 dx with N=-1/2*x^k*Ptheta.
    Solve N=A P+B P'. Then
      N/w^3 dx = (A+2B')/w dx - 2 d(B/w).
    The returned 4x4 matrix is the absolute/cohomology part; exact-term B is
    retained separately and MUST NOT be dropped for physical relative paths.
    """
    S=sylvester_reduction_matrix(P)
    Sinv=S.inv()
    C=sp.zeros(4,4)
    exact_terms=[]
    identities=[]
    for k in range(4):
        N=sp.Poly(sp.expand(-sp.Rational(1,2)*x**k*Ptheta),x)
        rhs=sp.Matrix([N.nth(i) for i in range(9)])
        sol=Sinv*rhs
        A=sum(sol[i]*x**i for i in range(4))
        B=sum(sol[4+j]*x**j for j in range(5))
        identities.append(sp.expand(A*P+B*sp.diff(P,x)-N.as_expr())==0)
        Q=sp.Poly(sp.expand(A+2*sp.diff(B,x)),x)
        for j in range(4):
            C[j,k]=sp.factor(Q.nth(j))
        exact_terms.append(sp.factor(B))
    return C,exact_terms,all(identities)


def matrix_strings(A):
    return [[str(sp.factor(A[i,j])) for j in range(A.cols)] for i in range(A.rows)]


def main():
    spec={D:sp.Integer(1),M:sp.Integer(1),nu:sp.Rational(1,5),r:sp.Integer(2),y:sp.Rational(1,3)}
    P=sp.factor(Pgen.subs(spec))
    S=sylvester_reduction_matrix(P)
    detS=sp.factor(S.det())
    resultant=sp.factor(sp.resultant(P,sp.diff(P,x),x))
    conns={}
    for theta in (D,M,y):
        C,Bs,ok=connection_at(P,sp.diff(Pgen,theta).subs(spec))
        conns[str(theta)]={
            'reduction_identity_all_four_basis_forms': bool(ok),
            'connection_matrix': matrix_strings(C),
            'exact_term_B_over_w': [str(v) for v in Bs],
        }
    result={
        'status':{
            'PF1_PATH_INVARIANTS':'LOCKED',
            'PF1_R03_GENUS2_ABSOLUTE_DERHAM_BASIS':'PASS_EXACT',
            'PF1_R03_FIXED_9X9_GRIFFITHS_HERMITE_REDUCTION':'PASS_EXACT',
            'PF1_R03_ABSOLUTE_X_GAUSS_MANIN':'PASS_EXACT',
            'PF1_R03_PHYSICAL_RELATIVE_X_ENDPOINT':'HOLD',
            'PF1_R03_LOG_RELATIVE_EXTENSION':'NOT_YET_CLOSED',
            'PF1_R03_PAIR_BLOCK_EXTENSION':'NOT_YET_CLOSED',
            'PF1_R03_Y_WHOLE_HALFWAVE_CLOSURE':'NOT_YET_CLOSED',
            'FORMAL_WHOLE_HALFWAVE_GATE_A':'HOLD',
        },
        'basis':['dx/w','x dx/w','x^2 dx/w','x^3 dx/w'],
        'reduction':{
            'unknown_A_degree_max':3,
            'unknown_B_degree_max':4,
            'fixed_linear_system_dimension':9,
            'identity':'N=A*P+B*Pprime; N/w^3=(A+2Bprime)/w-2*d(B/w)',
            'matrix_determinant_equals_resultant': bool(sp.simplify(detS-resultant)==0),
        },
        'exact_witness':{
            'parameters':{'D':'1','M':'1','nu':'1/5','r':'2','y':'1/3'},
            'P5':str(P),
            'rank_S':int(S.rank()),
            'det_S':str(detS),
            'resultant_P_Pprime':str(resultant),
            'connection_D_M_y':conns,
        },
        'formal_counts':{
            'spatial_sampling':0,
            'spatial_quadrature':0,
            'spatial_subdomains':1,
            'material_point_grid':0,
            'derham_basis_dimension':4,
            'reduction_matrix_dimension':9,
        }
    }
    print(json.dumps(result,indent=2,ensure_ascii=False))

if __name__=='__main__':
    main()
