"""
Diagnostic-only nonlinear material-space screen for the proposed invariant A/B representation.

This script does NOT use Case21 Pu, Swartz24, spatial X/Y/zeta samples, element
integration, or material-point integration.  It uses the frozen NC current
operator only as a deliberately difficult nonlinear material oracle.

Goal: test whether a naive low/moderate total-degree global invariant surface
    s_i = A(mu,r2) + B(mu,r2) e_i
is sufficient as an ARCHITECTURE PROOF.  It is not a final material fit.
"""
from __future__ import annotations

import math
import numpy as np
from numpy.linalg import cond, lstsq
from numpy.polynomial.chebyshev import chebval

# Frozen Case21 NC parameters (benchmark/oracle only)
FC = 21.23
E0 = 20321.0
EPS0 = 0.00209
NU = 0.18
RHO = 0.1
KAPPA = E0*EPS0/FC
XCR = RHO/KAPPA
ETA = XCR/20.0
ETA_R = 0.05
MT = -7.0/90.0
ACC = 0.1072329249362415
AT = 1.0 - 2.0**(-1.0/8.0)


def Pi_eta(z):
    return z*z*(np.sqrt(z*z+ETA*ETA)+z)/(2.0*(z*z+ETA*ETA))


def H(r, r0):
    return (
        0.5*((r-r0)+np.sqrt((r-r0)**2+ETA_R**2))
        - 0.5*((-r0)+math.sqrt(r0**2+ETA_R**2))
    )


def principal_response(lam):
    c = Pi_eta(-lam)
    t = Pi_eta(lam)
    C = KAPPA*c/(1.0+(KAPPA-2.0)*c+c*c)
    rr = t/XCR
    T = rr + (MT-1.0)*H(rr, 1.0) - MT*H(rr, 10.0)
    U = KAPPA*lam - C + KAPPA*c + RHO*T - KAPPA*t
    return U, C, T


def frozen_nc_diag(e1, e2):
    """Normalized stresses s1,s2 for physical principal strains EPS0*(e1,e2)."""
    x1 = (e1 + NU*e2)/(1.0-NU**2)
    x2 = (NU*e1 + e2)/(1.0-NU**2)
    U1,C1,T1 = principal_response(x1)
    U2,C2,T2 = principal_response(x2)
    s1 = U1 - ACC*C1**2*C2 + C1*T2 - RHO*AT*T1*T2**8
    s2 = U2 - ACC*C2**2*C1 + C2*T1 - RHO*AT*T2*T1**8
    return float(s1), float(s2)


# Deliberately broad MATERIAL-space stress-test domain, not a frozen validity domain.
EMIN, EMAX = -2.0, 0.6
MC = 0.5*(EMIN+EMAX)
MS = 0.5*(EMAX-EMIN)
R2MAX = ((EMAX-EMIN)/2.0)**2


def Tn(n, x):
    c = np.zeros(n+1)
    c[n] = 1.0
    return chebval(x, c)


def features(e1, e2, degree):
    mu = 0.5*(e1+e2)
    r2 = (0.5*(e1-e2))**2
    xi = (mu-MC)/MS
    eta = 2.0*r2/R2MAX - 1.0
    terms = [(i,j) for i in range(degree+1) for j in range(degree+1-i)]
    tx = [Tn(i,xi) for i in range(degree+1)]
    ty = [Tn(j,eta) for j in range(degree+1)]
    phi = np.array([tx[i]*ty[j] for i,j in terms])
    return phi, terms


def fit_degree(degree, ntrain=35):
    grid = np.linspace(EMIN, EMAX, ntrain)
    rows, rhs = [], []
    for e1 in grid:
        for e2 in grid:
            s1,s2 = frozen_nc_diag(e1,e2)
            phi,terms = features(e1,e2,degree)
            rows.append(np.r_[phi, e1*phi]); rhs.append(s1)
            rows.append(np.r_[phi, e2*phi]); rhs.append(s2)
    mat = np.vstack(rows)
    vec = np.array(rhs)
    coef = lstsq(mat, vec, rcond=1e-12)[0]
    return coef, terms, cond(mat)


def test_degree(degree, ntrain=35, ntest=34):
    coef,terms,kappa = fit_degree(degree,ntrain)
    step = (EMAX-EMIN)/ntest
    test = np.linspace(EMIN+step/2.0, EMAX-step/2.0, ntest)
    errors = []
    for e1 in test:
        for e2 in test:
            s1,s2 = frozen_nc_diag(e1,e2)
            phi,_ = features(e1,e2,degree)
            n = len(phi)
            aa = coef[:n] @ phi
            bb = coef[n:] @ phi
            errors += [abs(aa+bb*e1-s1), abs(aa+bb*e2-s2)]
    errors = np.asarray(errors)
    return {
        "degree": degree,
        "ncoeff": 2*len(terms),
        "condition": kappa,
        "mae": errors.mean(),
        "p95": np.quantile(errors,0.95),
        "max": errors.max(),
    }


if __name__ == "__main__":
    print("degree,ncoeff,condition,mae,p95,max")
    for degree in (2,4,6,8,10,12):
        r = test_degree(degree)
        print(
            f"{r['degree']},{r['ncoeff']},{r['condition']:.6e},"
            f"{r['mae']:.6f},{r['p95']:.6f},{r['max']:.6f}"
        )
