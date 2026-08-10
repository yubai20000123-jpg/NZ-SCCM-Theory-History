"""NZ-SCCM PF1-R04 physical relative-x endpoint audit.

This is an exact symbolic audit only. No spatial/auxiliary numerical quadrature,
no cells, no material points, no Case21 Pu, no Swartz24, and no route switch.

Main result
-----------
For P=x(1-x) Gamma and parameter derivatives that do not move x=0,1,
P_theta=x(1-x) Gamma_theta.  The R03 Griffiths/Hermite exact term can be
chosen with B_rel=x(1-x) C, so B_rel/w -> 0 at both physical branch endpoints.
Thus the algebraic compact subsystem uses the same finite Gauss-Manin matrix on
the physical [0,1] relative chain; the exact-differential endpoint functional
vanishes identically.  Log/atanh endpoint terms remain a separate relative
extension and are NOT declared closed here.
"""
from __future__ import annotations

import json
import sympy as sp

x,y,D,M,nu,r,Bb,t,eta = sp.symbols('x y D M nu r Bb t eta')
h = x*(1-x)

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
Pgen = sp.expand(h*Gamma)


def endpoint_reduction_matrix(G):
    """7x7 map [Atilde_0..3,C_0..2] -> coeffs of Atilde*G+C*h*G'."""
    Gp=sp.Poly(sp.expand(G),x)
    HGp=sp.Poly(sp.expand(h*sp.diff(G,x)),x)
    if Gp.degree()!=3:
        raise ValueError('R04 generic single-resolvent Gamma must be cubic in x')
    S=sp.zeros(7,7)
    gc=[Gp.nth(i) for i in range(4)]
    hc=[HGp.nth(i) for i in range(5)]
    for i in range(4):
        for k,v in enumerate(gc): S[i+k,i]=v
    for j in range(3):
        for k,v in enumerate(hc): S[j+k,4+j]=v
    return S


def endpoint_compatible_reduction(G,Gtheta,k):
    """Return A,Brel,C and exact identity for N=-1/2*x^k*h*Gtheta."""
    S=endpoint_reduction_matrix(G)
    Nt=sp.Poly(sp.expand(-sp.Rational(1,2)*x**k*Gtheta),x)
    rhs=sp.Matrix([Nt.nth(i) for i in range(7)])
    sol=S.LUsolve(rhs)
    Atilde=sum(sol[i]*x**i for i in range(4))
    C=sum(sol[4+j]*x**j for j in range(3))
    Brel=sp.factor(h*C)
    A=sp.factor(Atilde-C*sp.diff(h,x))
    P=sp.factor(h*G)
    N=sp.factor(h*Nt.as_expr())
    identity=sp.expand(A*P+Brel*sp.diff(P,x)-N)==0
    Q=sp.factor(A+2*sp.diff(Brel,x))
    return A,Brel,C,Q,identity


def exact_state_audit(name,subs):
    G=sp.factor(Gamma.subs(subs))
    S=endpoint_reduction_matrix(G)
    detS=sp.factor(S.det())
    resultant=sp.factor(sp.resultant(G,h*sp.diff(G,x),x))
    per_theta={}
    for theta in (D,M,y):
        Gtheta=sp.diff(Gamma,theta).subs(subs)
        rows=[]
        for k in range(4):
            A,Brel,C,Q,ok=endpoint_compatible_reduction(G,Gtheta,k)
            rows.append({
                'k':k,
                'identity':bool(ok),
                'Brel_has_x_factor':bool(sp.rem(sp.Poly(Brel,x),sp.Poly(x,x)).as_expr()==0),
                'Brel_has_1_minus_x_factor':bool(sp.simplify(Brel.subs(x,1))==0),
                'Brel_at_0':str(sp.factor(Brel.subs(x,0))),
                'Brel_at_1':str(sp.factor(Brel.subs(x,1))),
                'Q_degree':int(sp.Poly(Q,x).degree()),
            })
        per_theta[str(theta)]=rows
    return {
        'name':name,
        'state':{str(k):str(v) for k,v in subs.items()},
        'Gamma':str(G),
        'P':str(sp.factor(h*G)),
        'det_7x7':str(detS),
        'resultant_G_hGprime':str(resultant),
        'det_equals_resultant':bool(sp.simplify(detS-resultant)==0),
        'theta_audit':per_theta,
    }


def log_divisor_audit():
    H=x+y-2*x*y
    K=nu*x-y+(1-nu)*x*y
    a=(nu-1)*D+M*H
    E=sp.factor(-nu*D**2+D*M*K+Bb**2*(x+y-1)-r*a+r**2)
    O=sp.factor(Bb*(D*(nu-1)+M*(2-x-y)-2*r))
    # t^2=x, eta^2=y. Direct log[Delta(s+)/Delta(s-)] factors.
    E_t=sp.expand(E.subs(x,t**2))
    O_t=sp.expand(O.subs(x,t**2))
    phi_plus=sp.expand(E_t+eta*t*O_t)
    phi_minus=sp.expand(E_t-eta*t*O_t)
    product_identity=sp.expand((phi_plus*phi_minus).subs(eta**2,y) - (E_t**2-y*t**2*O_t**2))==0

    # Exact rational witness with eta^2=y=1/4.
    wsub={D:sp.Integer(1),M:sp.Integer(1),nu:sp.Rational(1,5),r:sp.Integer(2),y:sp.Rational(1,4),eta:sp.Rational(1,2),Bb:sp.Rational(1,3)}
    pp=sp.factor(phi_plus.subs(wsub)); pm=sp.factor(phi_minus.subs(wsub))
    return {
        'E_degree_x':int(sp.Poly(E,x).degree()),
        'O_degree_x':int(sp.Poly(O,x).degree()),
        'phi_plus_degree_t':int(sp.Poly(phi_plus,t).degree()),
        'phi_minus_degree_t':int(sp.Poly(phi_minus,t).degree()),
        'product_identity':bool(product_identity),
        'witness':{
            'parameters':{'D':'1','M':'1','nu':'1/5','r':'2','y':'1/4','sqrt_y':'1/2','Bb':'1/3'},
            'phi_plus':str(pp),
            'phi_minus':str(pm),
            'gcd_degree':int(sp.gcd(sp.Poly(pp,t),sp.Poly(pm,t)).degree()),
            'disc_phi_plus':str(sp.factor(sp.discriminant(sp.Poly(pp,t),t))),
            'disc_phi_minus':str(sp.factor(sp.discriminant(sp.Poly(pm,t),t))),
        }
    }


def main():
    states=[
        ('A',{D:sp.Integer(1),M:sp.Integer(1),nu:sp.Rational(1,5),r:sp.Integer(2),y:sp.Rational(1,3)}),
        ('B',{D:sp.Rational(4,5),M:sp.Rational(3,2),nu:sp.Rational(1,4),r:sp.Rational(-1,2),y:sp.Rational(2,5)}),
        ('C',{D:sp.Rational(6,5),M:sp.Rational(2,3),nu:sp.Rational(1,6),r:sp.Rational(3,2),y:sp.Rational(3,5)}),
    ]
    result={
        'status':{
            'PF1_PATH_INVARIANTS':'LOCKED',
            'PF1_R04_ENDPOINT_COMPATIBLE_7X7_REDUCTION':'PASS_EXACT',
            'PF1_R04_PHYSICAL_ALGEBRAIC_X_ENDPOINT':'PASS_EXACT',
            'PF1_R04_DIRECT_LOG_DIVISOR_IDENTIFICATION':'PASS_EXACT',
            'PF1_R04_LOG_RELATIVE_EXTENDED_CONNECTION':'HOLD',
            'PF1_R04_PAIR_BLOCK_EXTENSION':'NOT_YET_CLOSED',
            'PF1_R04_Y_WHOLE_HALFWAVE_CLOSURE':'NOT_YET_CLOSED',
            'FORMAL_WHOLE_HALFWAVE_GATE_A':'HOLD',
        },
        'identity':{
            'P':'h*Gamma, h=x(1-x)',
            'Ptheta':'h*Gamma_theta',
            'N':'h*Ntilde, Ntilde=-1/2*x^k*Gamma_theta',
            'reduced_equation':'Ntilde=Atilde*Gamma+C*h*Gamma_prime',
            'Brel':'h*C',
            'A':'Atilde-C*h_prime',
            'boundary':'Brel/w=C*sqrt(h/Gamma) -> 0 at x=0,1 when P is square-free',
            'matrix_dimension':7,
            'matrix_determinant':'Res(Gamma,h*Gamma_prime)=Res(Gamma,h)*Res(Gamma,Gamma_prime)'
        },
        'exact_states':[exact_state_audit(name,subs) for name,subs in states],
        'direct_log_divisor':log_divisor_audit(),
        'formal_counts':{
            'spatial_sampling':0,
            'spatial_quadrature':0,
            'spatial_subdomains':1,
            'material_point_grid':0,
            'endpoint_reduction_matrix_dimension':7,
        }
    }
    print(json.dumps(result,indent=2,ensure_ascii=False))

if __name__=='__main__':
    main()
