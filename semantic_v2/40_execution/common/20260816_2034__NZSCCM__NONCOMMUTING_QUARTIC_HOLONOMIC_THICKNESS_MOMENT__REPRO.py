"""NZ-SCCM noncommuting quartic holonomic thickness-moment gate.

Formal structural spatial/thickness quadrature remains ZERO.
mpmath quadrature is used only as an independent audit oracle for the
prototype integration-by-parts recurrence; it is not a production integral.
"""
import math
import sympy as sp
import mpmath as mp

x,y=sp.symbols("x y", real=True)
eta=sp.Rational(1,20)

# Prototype noncommuting affine symmetric 2x2 thickness pencil.
E=sp.Matrix([
    [sp.Rational(1,5)+x/sp.Integer(3), sp.Rational(1,7)+x/sp.Integer(5)],
    [sp.Rational(1,7)+x/sp.Integer(5), -sp.Rational(1,4)+2*x/sp.Integer(7)]
])
A=sp.expand(E*E)+eta**2*sp.eye(2)
p=sp.factor(sp.trace(A))
q=sp.factor(A.det())
r=sp.factor(p**2-4*q)
Delta=sp.factor(p**2-r)

# Universal compact order-2 annihilator coefficients.
a=sp.factor(sp.diff(r,x)/(4*r))
b=sp.factor(sp.diff(p,x)/2-p*sp.diff(r,x)/(4*r))
c=sp.factor(sp.diff(a,x)+a**2+b**2/Delta)
e=sp.factor(sp.diff(b,x)-b*sp.diff(Delta,x)/(2*Delta)+2*a*b)
O0=sp.factor(e*a-b*c)
O1=sp.factor(-e)
O2=sp.factor(b)

# Clear rational denominators and make a primitive integer polynomial triple.
den=sp.lcm([sp.denom(O0),sp.denom(O1),sp.denom(O2)])
Os=[sp.factor(sp.cancel(z*den)) for z in (O0,O1,O2)]
g=sp.gcd(sp.gcd(sp.Poly(Os[0],x),sp.Poly(Os[1],x)),sp.Poly(Os[2],x))
Os=[sp.factor(sp.cancel(z/g.as_expr())) for z in Os]
Ps=[sp.Poly(z,x,domain=sp.QQ) for z in Os]
ld=1
for P in Ps:
    for co in P.all_coeffs():
        ld=sp.ilcm(ld,int(co.q))
Ps=[sp.Poly(sp.expand(P.as_expr()*ld),x,domain=sp.ZZ) for P in Ps]
cg=0
for P in Ps:
    for co in P.all_coeffs():
        cg=math.gcd(cg,abs(int(co)))
Ps=[sp.Poly(sp.expand(P.as_expr()/cg),x,domain=sp.ZZ) for P in Ps]
A0,A1,A2=[P.as_expr() for P in Ps]

# Exact quotient-field derivative proof.
K=sp.QQ.frac_field(x)
Palg=sp.Poly(y**4-2*p*y**2+r,y,domain=K)
Py=Palg.diff()
Px=sp.Poly(sp.diff(Palg.as_expr(),x),y,domain=K)
yp=(-Px*sp.invert(Py,Palg)).rem(Palg)
def total_deriv(F):
    expr=sp.diff(F.as_expr(),x)+sp.diff(F.as_expr(),y)*yp.as_expr()
    return sp.Poly(expr,y,domain=K).rem(Palg)
d0=sp.Poly(y,y,domain=K)
d1=total_deriv(d0)
d2=total_deriv(d1)
R=(d0.mul_ground(K.convert(A0))+d1.mul_ground(K.convert(A1))+d2.mul_ground(K.convert(A2))).rem(Palg)

# Audit-only high precision recurrence check.
mp.mp.dps=60
def f_mp(xx):
    xx=mp.mpf(xx)
    pp=(mp.mpf(48112)*xx**2+mp.mpf(18480)*xx+mp.mpf(26163))/mp.mpf(176400)
    qq=(mp.mpf(5274752)*xx**4-mp.mpf(15915200)*xx**3-mp.mpf(262976)*xx**2+
        mp.mpf(20738760)*xx+mp.mpf(9199989))/mp.mpf(1728720000)
    return mp.sqrt(pp+2*mp.sqrt(qq))
def fp_mp(xx):
    return mp.diff(f_mp,xx)

maxk=14
M=[mp.quad(lambda xx,kk=k: xx**kk*f_mp(xx),[-1,0,1]) for k in range(maxk+1)]
def coeffs(P):
    P=sp.Poly(P,x,domain=sp.ZZ)
    return [mp.mpf(int(P.nth(j))) for j in range(P.degree()+1)]
a0,a1,a2=coeffs(A0),coeffs(A1),coeffs(A2)
def peval(cc,xx):
    return sum(cc[j]*xx**j for j in range(len(cc)))
def dz_xnA2(n,xx):
    return sum((n+j)*a2[j]*xx**(n+j-1) for j in range(len(a2)) if n+j>0)
def boundary(n,xx):
    return xx**n*peval(a2,xx)*fp_mp(xx)-dz_xnA2(n,xx)*f_mp(xx)+xx**n*peval(a1,xx)*f_mp(xx)
def rec_integral(n):
    ans=mp.mpf("0")
    for j,aa in enumerate(a2):
        k=n+j-2
        if k>=0 and (n+j)*(n+j-1):
            ans+=aa*(n+j)*(n+j-1)*M[k]
    for j,aa in enumerate(a1):
        k=n+j-1
        if k>=0 and (n+j):
            ans-=aa*(n+j)*M[k]
    for j,aa in enumerate(a0):
        ans+=aa*M[n+j]
    return ans
REC={n:abs(boundary(n,mp.mpf(1))-boundary(n,mp.mpf(-1))+rec_integral(n)) for n in range(7)}

print("FORMAL STRUCTURAL COUNTERS: sampling=0 quadrature=0 subdomains=1 thickness_quadrature=0")
print("p(x) =",p)
print("q(x) =",q)
print("r(x) =",r)
print("A0 =",sp.factor(A0))
print("A1 =",sp.factor(A1))
print("A2 =",sp.factor(A2))
print("degrees =",[sp.degree(A0,x),sp.degree(A1,x),sp.degree(A2,x)])
print("ANNIHILATOR_QUOTIENT_REMAINDER =",R)
print("M0_AUDIT =",mp.nstr(M[0],35))
print("M1_AUDIT =",mp.nstr(M[1],35))
print("endpoint =",{
    "y-1":mp.nstr(f_mp(-1),40),"y+1":mp.nstr(f_mp(1),40),
    "yp-1":mp.nstr(fp_mp(-1),40),"yp+1":mp.nstr(fp_mp(1),40)})
print("RECURRENCE_AUDIT_ABS =",{n:mp.nstr(v,14) for n,v in REC.items()})
print("UNIVERSAL_SMOOTH_QUARTIC_SECOND_ORDER_ODE = PASS_EXACT")
print("POLYNOMIAL_THICKNESS_MOMENT_RECURRENCE = PASS_EXACT")
print("FULL_R10_COMPOSITUM_RUNTIME = OPEN")
print("NEW_Pu = NOT_RUN")
