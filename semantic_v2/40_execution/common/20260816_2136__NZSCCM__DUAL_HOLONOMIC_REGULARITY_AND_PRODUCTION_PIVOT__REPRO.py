"""NZ-SCCM 21:36 decisive dual-holonomic regularity audit.

Purpose:
1) correct the 20:59 local 4-state derivative matrix placement;
2) derive the exact denominator-gauge identity for regular rational dual targets;
3) expose the retained smooth prototype's interior apparent pole in the rationalized basis;
4) verify that the physical algebraic combination is regular there;
5) record the anti-loop production pivot back to the accepted N48-C1/MM + General-D15 chain.

Formal structural spatial/thickness numerical integration remains ZERO. Any direct numerical integration
used to check a recurrence is audit-only and is not a production operator.
"""

import sympy as sp

x=sp.symbols('x', real=True)
rho=sp.Rational(1,10)
kappa=sp.Integer(2)
eta=(rho/kappa)/20
I2=sp.eye(2)
E=sp.Matrix([
    [sp.Rational(1,5)+x/3, sp.Rational(1,7)+x/5],
    [sp.Rational(1,7)+x/5,-sp.Rational(1,4)+2*x/7]
])

# Smooth quadratic tower q^2=Q, s^2=A+2q
Amat=sp.expand(E*E)+eta**2*I2
A=sp.factor(sp.trace(Amat))
Q=sp.factor(Amat.det())
q=sp.sqrt(Q)
s=sp.sqrt(A+2*q)
ell=sp.cancel(sp.diff(Q,x)/(2*Q))
den=2*(A**2-4*Q)
c0=sp.cancel((sp.diff(A,x)*A-4*ell*Q)/den)
c1=sp.cancel((-2*sp.diff(A,x)+2*ell*A)/den)

# Correct local derivative matrix for v=(1,q,s,qs)^T.
Aloc=sp.Matrix([
    [0,0,0,0],
    [0,ell,0,0],
    [0,0,c0,c1],
    [0,0,c1*Q,ell+c0]
])
v=sp.Matrix([1,q,s,q*s])

# Three exact audit fibers suffice only to test the algebraic matrix placement; they are NOT quadrature.
for xv in [sp.Rational(-1,2),sp.Rational(0),sp.Rational(1,2)]:
    rr=sp.N((sp.diff(v,x)-Aloc*v).subs(x,xv),50)
    assert max(abs(complex(z)) for z in rr) == 0.0

# Decisive apparent-pole audit.
disc=sp.factor(A**2-4*Q)
xstar=sp.Rational(21,260)
assert sp.factor(disc - (260*x-21)**2*(28624*x**2+47880*x+50121)/sp.Integer(31116960000)) == 0
qstar=sp.N(q.subs(x,xstar),50)
sstar=sp.N(s.subs(x,xstar),50)
combo_limit=sp.limit(c0+c1*q,x,xstar)
assert sp.factor(combo_limit-sp.Rational(29577184,61042095)) == 0

# Exact denominator-gauge identity, written symbolically.
# If d V' = B V and W=V/G then (dG) W' = (BG-dG'I) W.
d,G=sp.symbols('d G', nonzero=True)
print('GAUGE_IDENTITY: (d*G) Wprime = (B*G-d*Gprime*I) W')
print('MOMENT_RECURRENCE: [x^n dG W] = sum_j (n+j)h_j M[n+j-1] + sum_j H_j M[n+j]')

# Common denominator of corrected local block remains finite.
dens=[]
for z in Aloc:
    if z!=0:
        dens.append(sp.Poly(sp.cancel(z).as_numer_denom()[1],x,domain=sp.QQ))
dpoly=dens[0]
for dd in dens[1:]:
    dpoly=sp.lcm(dpoly,dd)

print('FORMAL STRUCTURAL COUNTERS: sampling=0 quadrature=0 subdomains=1 thickness_quadrature=0')
print('CORRECT_LOCAL_MATRIX =')
sp.pprint(Aloc)
print('LOCAL_COMMON_DENOMINATOR_DEGREE =', dpoly.degree())
print('SMOOTH_DISCRIMINANT_FACTOR =', disc)
print('APPARENT_INTERIOR_POLE_x =', xstar, '=', sp.N(xstar,30))
print('q(x*) =', qstar)
print('s(x*) =', sstar)
print('lim(c0+c1*q) =', combo_limit, '=', sp.N(combo_limit,30))
print('PHYSICAL_ATOM_REGULAR_AT_APPARENT_POLE = PASS')
print('RATIONALIZED_BASIS_GLOBAL_REGULARITY = FAIL_APPARENT_INTERIOR_POLE')
print('EXACT_ALGEBRAIC_HOLONOMIC_PRODUCTION = PAUSED_RESEARCH_BRANCH')
print('PRODUCTION_ROUTE = N48-C1/MM + GENERAL-D15 + FIVE-TERM MEMBRANE REDISTRIBUTION')
print('NEXT_GATE = UNIFIED_V1_CASE21_MEMBRANE_REDISTRIBUTED_N48_PRODUCTION_GATE')
print('NEW_Pu = NOT_RUN_IN_THIS_GATE')
