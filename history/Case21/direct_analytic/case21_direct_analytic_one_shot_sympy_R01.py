"""NZ-SCCM Case21 direct-analytic one-shot CAS test R01.

Purpose
-------
Build the fully explicit Case21 concrete current-operator integrand at a fixed
reference state and ask SymPy to integrate the thickness coordinate directly.
No spatial quadrature, material-point sum, compiler, Chebyshev coefficient,
or support mask is used.

The source material variant used here is the algebraic Foster smoothing found
in the earlier Case21 regression package build_material_coeffs.py:
    H(r,r0;eta_r=0.05)
not the later exploratory tanh-sigmoid variant.
"""
import sympy as sp
import time

X, Y, zeta = sp.symbols("X Y zeta", real=True)
D = sp.Float("0.7955", 30)
q = sp.Float("0.001974", 30)
nu = sp.Float("0.18", 30)
eps0 = sp.Float("0.00209", 30)
fc = sp.Float("21.23", 30)
E0 = sp.Float("20321", 30)
b = sp.Float("1220", 30)
t = sp.Float("19.30", 30)
q0 = sp.Rational(1, 400)

kappa = E0 * eps0 / fc
rho = sp.Rational(1, 10)
xcr = rho / kappa
eta = xcr / 20
msoft = -sp.Rational(7, 90)
a_cc = sp.Float("0.1072329249362415", 30)
a_t = 1 - 2 ** (-sp.Rational(1, 8))

Cm = sp.pi**2 / eps0 * (q0*q + q*q/2)
Cb = sp.pi**2 / (2*eps0) * (t/b) * q
sX, cX = sp.sin(X), sp.cos(X)
sY, cY = sp.sin(Y), sp.cos(Y)

ex = nu*D + Cm*cX**2*sY**2 + Cb*sX*sY*zeta
ey = -D + Cm*sX**2*cY**2 + Cb*sX*sY*zeta
gxy = 2*Cm*sX*cX*sY*cY - 2*Cb*cX*cY*zeta

den = 1 - nu**2
X11 = (ex + nu*ey) / den
X22 = (nu*ex + ey) / den
X12 = gxy / (2*(1+nu))
mu = (X11 + X22) / 2
delta = (X11 - X22) / 2
rad = sp.sqrt(delta**2 + X12**2)
lam_p = mu + rad
lam_m = mu - rad


def Pi(v):
    return v**2 * (sp.sqrt(v**2 + eta**2) + v) / (2*(v**2 + eta**2))


def H(r, r0, eta_r=sp.Rational(1, 20)):
    return (sp.Rational(1, 2)*((r-r0) + sp.sqrt((r-r0)**2 + eta_r**2))
            - sp.Rational(1, 2)*((-r0) + sp.sqrt(r0**2 + eta_r**2)))


def principal_response(lam):
    c = Pi(-lam)
    tt = Pi(lam)
    C = kappa*c / (1 + (kappa-2)*c + c**2)
    rr = tt/xcr
    T = rr + (msoft-1)*H(rr, 1) - msoft*H(rr, 10)
    U = kappa*lam - C + kappa*c + rho*T - kappa*tt
    return U, C, T


Up, Cp, Tp = principal_response(lam_p)
Um, Cm_, Tm = principal_response(lam_m)
sp_ = Up - a_cc*Cp**2*Cm_ + Cp*Tm - rho*a_t*Tp*Tm**8
sm_ = Um - a_cc*Cm_**2*Cp + Cm_*Tp - rho*a_t*Tm*Tp**8

# sigma_y/fc = spectral projection; explicit, not a placeholder.
Syy = (sp_ + sm_)/2 - ((sp_ - sm_)/2) * delta/rad

# R_q integrand can be built from Sxx,Syy,Txy and explicit strain derivatives;
# if the simpler Syy thickness primitive cannot be obtained directly, the full
# one-shot Pc/Rq request is already disproved for this CAS route.
print("Syy operation count:", sp.count_ops(Syy), flush=True)
print("Attempting direct SymPy thickness integration with X,Y symbolic...", flush=True)
t0 = time.time()
Iz = sp.integrate(Syy, (zeta, -1, 1), risch=None)
print("elapsed_s:", time.time()-t0, flush=True)
print("contains_unevaluated_Integral:", Iz.has(sp.Integral), flush=True)
print("result_operation_count:", sp.count_ops(Iz), flush=True)
print(Iz)
