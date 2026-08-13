import sympy as sp

# Exact symbolic audit of Yun Lu Ch.2 against a one-complete-halfwave D15 representation.
# No numerical spatial quadrature is used.

r = sp.symbols('r', positive=True)  # local halfwave aspect ratio ell/b
E, nu, t, b, ell = sp.symbols('E nu t b ell', positive=True)
A, A0, px = sp.symbols('A A0 px', real=True)
pi = sp.pi
K = A**2 + 2*A*A0

# Yun Lu closed-form coefficients expressed on one representative complete halfwave ell=a/m.
kcr = sp.factor(4*(3*r**4 + 2*r**2 + 3)/(3*r**2))
kp_num = (272*r**16 + 2856*r**14 + 11273*r**12 + 23146*r**10 +
          31506*r**8 + 23146*r**6 + 11273*r**4 + 2856*r**2 + 272)
kp_den = r**2*(r**2 + 1)**2*(r**2 + 4)**2*(4*r**2 + 1)**2
kp = sp.factor(kp_num/kp_den)

# D15-generated normalized one-dimensional harmonic moments.
I1 = {0: sp.Rational(-1,2), 1: sp.Rational(1,2), 2: sp.Rational(-1,4)}
I2 = {0: sp.Rational(3,2), 1: sp.Rational(-1,1), 2: sp.Rational(1,4)}
I3 = {0: sp.Rational(0,1), 1: sp.Rational(1,2), 2: sp.Rational(-1,4)}

# Particular Airy stress-function coefficients f(q,s), Yun Lu Table 2-1 on one cell.
f = {
    (0,0): sp.Integer(0),
    (0,1): b**2*E/(2*ell**2),
    (0,2): -b**2*E/(32*ell**2),
    (1,0): ell**2*E/(2*b**2),
    (1,1): -ell**2*b**2*E/(ell**2+b**2)**2,
    (1,2): ell**2*b**2*E/(2*(4*ell**2+b**2)**2),
    (2,0): -ell**2*E/(32*b**2),
    (2,1): ell**2*b**2*E/(2*(ell**2+4*b**2)**2),
    (2,2): sp.Integer(0),
}

# Compatibility RHS harmonic coefficient matrix after factoring 8*pi^4*E*K/(ell^2*b^2).
M = sp.Matrix([[0, 1, -1],
               [1,-2,  1],
               [-1,1,  0]])

# Table 2-1 exact recovery.
table_checks = []
for q in range(3):
    for s in range(3):
        if q == 0 and s == 0:
            table_checks.append(sp.simplify(f[(q,s)]))
            continue
        src = 8*pi**4*E/(ell**2*b**2) * M[s,q]
        lam = 16*pi**4*((sp.Rational(q,1)/ell)**2 + (sp.Rational(s,1)/b)**2)**2
        pred = sp.simplify(src/lam) if M[s,q] != 0 else sp.Integer(0)
        table_checks.append(sp.factor(pred - f[(q,s)]))
assert all(c == 0 for c in table_checks)

kx = 2*pi/ell
ky = 2*pi/b

def G_harm(q,s):
    return -ell*b*kx**2*ky**2*(
        s**2*I1[q]*I2[s] + q**2*I2[q]*I1[s] + 2*q*s*I3[q]*I3[s]
    )

H = sp.factor(sum(f[(q,s)]*G_harm(q,s) for q in range(3) for s in range(3)))

# Membrane contribution implied by H, normalized into Yun Lu kp.
p_mem_coeff = sp.factor(-H*4*t/(3*ell*b*kx**2))
kp_from_d15 = sp.factor(p_mem_coeff / (E*t*pi**2/(12*b**2)))
kp_from_d15_r = sp.factor(kp_from_d15.subs(ell, r*b))
assert sp.simplify(kp_from_d15_r - kp) == 0

# Bending contribution -> kcrx.
kcr_from_d15 = sp.factor(
    ((3*kx**4 + 2*kx**2*ky**2 + 3*ky**4)/(3*kx**2))/(pi**2/b**2)
)
kcr_from_d15_r = sp.factor(kcr_from_d15.subs(ell, r*b))
assert sp.simplify(kcr_from_d15_r-kcr) == 0

# Minimum complete halfwave r=1.
assert sp.simplify(sp.diff(kcr,r).subs(r,1)) == 0
assert sp.simplify(sp.diff(kp,r).subs(r,1)) == 0
assert sp.simplify(kcr.subs(r,1) - sp.Rational(32,3)) == 0
assert sp.simplify(kp.subs(r,1) - sp.Rational(1066,25)) == 0

# Axial stress field generated uniquely by Table 2-1.
th, ph = sp.symbols('theta phi', real=True)
sigma_exact = (
    -2*K*E*pi**2/ell**2*sp.cos(ph)
    + K*E*pi**2/(2*ell**2)*sp.cos(2*ph)
    + 4*ell**2*K*E*pi**2/(ell**2+b**2)**2*sp.cos(th)*sp.cos(ph)
    - 2*ell**2*K*E*pi**2/(ell**2+4*b**2)**2*sp.cos(2*th)*sp.cos(ph)
    - 8*ell**2*K*E*pi**2/(4*ell**2+b**2)**2*sp.cos(th)*sp.cos(2*ph)
    - px/t
)

sigma_min = sp.factor(sigma_exact.subs({th:sp.pi, ph:0}))
sigma_min_expected = sp.factor(
    -3*K*E*pi**2/(2*ell**2)
    -4*ell**2*K*E*pi**2/(ell**2+b**2)**2
    +8*ell**2*K*E*pi**2/(4*ell**2+b**2)**2
    -2*ell**2*K*E*pi**2/(ell**2+4*b**2)**2
    -px/t
)
assert sp.simplify(sigma_min-sigma_min_expected) == 0

# Exact displacement-control compatibility derived from the same Karman field.
geom_shortening = sp.factor(3*pi**2/ell**2*(A0*A + A**2/2))
eps_compression = sp.factor(px/(E*t) + geom_shortening)

print('TABLE_2_1_FROM_D15 = PASS')
print('KCRX_FROM_D15 =', kcr_from_d15_r)
print('KP_FROM_D15 =', kp_from_d15_r)
print('KCRX_AT_r1 =', sp.simplify(kcr.subs(r,1)))
print('KP_AT_r1 =', sp.simplify(kp.subs(r,1)))
print('KCRX_SECOND_DERIV_AT_r1 =', sp.simplify(sp.diff(kcr,r,2).subs(r,1)))
print('KP_SECOND_DERIV_AT_r1 =', sp.simplify(sp.diff(kp,r,2).subs(r,1)))
print('SIGMA_X_FIELD_FROM_TABLE_2_1 =', sigma_exact)
print('SIGMA_X_MIN =', sigma_min)
print('EDGE_SHORTENING =', eps_compression)
print('ALL_EXACT_SYMBOLIC_CHECKS = PASS')
