"""NZ-SCCM M1-R01 material-space screen.

Purpose
-------
Test a structured analytic material representation

    s_i = p(e_i) + A_c(mu,r2) + B_c(mu,r2) e_i

against the frozen Case21 NC current operator used only as a nonlinear
material oracle. No structural Pu, no spatial coordinates, no spatial
quadrature and no material-point history are used.

This script reproduces the R01 screen documented in
NZ_SCCM_M1_STRUCTURED_MATRIX_POLYNOMIAL_SCREEN_R01_20260810.md.
"""
from __future__ import annotations

import numpy as np
import scipy.linalg as la
from numpy.polynomial.chebyshev import chebvander

NU = 0.18
KAPPA = 2.0005129533678754
RHO = 0.1
XCR = 0.04998717945397425
ETA = XCR / 20.0
ETA_R = 0.05
MT = -7.0 / 90.0
ACC = 0.1072329249362415
AT = 1.0 - 2.0 ** (-1.0 / 8.0)
EMIN, EMAX = -2.0, 0.6
R2MAX = ((EMAX - EMIN) / 2.0) ** 2


def pi_eta(z):
    return z**2 * (np.sqrt(z*z + ETA*ETA) + z) / (2.0 * (z*z + ETA*ETA))


def foster_h(r, r0):
    return 0.5 * ((r-r0) + np.sqrt((r-r0)**2 + ETA_R**2)) - 0.5 * ((-r0) + np.sqrt(r0**2 + ETA_R**2))


def principal_response(lam):
    c = pi_eta(-lam)
    t = pi_eta(lam)
    C = KAPPA*c / (1.0 + (KAPPA-2.0)*c + c*c)
    rr = t / XCR
    T = rr + (MT-1.0)*foster_h(rr, 1.0) - MT*foster_h(rr, 10.0)
    U = KAPPA*lam - C + KAPPA*c + RHO*T - KAPPA*t
    return U, C, T


def frozen_oracle(e1, e2):
    """Return normalized principal stresses s_i=sigma_i/fc.

    e1,e2 are raw principal strains normalized by eps0.
    """
    x1 = (e1 + NU*e2) / (1.0 - NU**2)
    x2 = (NU*e1 + e2) / (1.0 - NU**2)
    U1,C1,T1 = principal_response(x1)
    U2,C2,T2 = principal_response(x2)
    s1 = U1 - ACC*C1**2*C2 + C1*T2 - RHO*AT*T1*T2**8
    s2 = U2 - ACC*C2**2*C1 + C2*T1 - RHO*AT*T2*T1**8
    return s1, s2


def scale_e(e):
    return 2.0*(e-EMIN)/(EMAX-EMIN) - 1.0


def scale_r2(r2):
    return 2.0*r2/R2MAX - 1.0


def correction_indices(d):
    return [(m,n) for m in range(d+1) for n in range(d+1-m) if (m,n)!=(0,0)]


def design_rows(e1, e2, pdeg, corrdeg):
    e1 = np.asarray(e1).ravel()
    e2 = np.asarray(e2).ravel()
    mu = (e1 + e2) / 2.0
    r2 = ((e1 - e2) / 2.0) ** 2

    Tp1 = chebvander(scale_e(e1), pdeg)
    Tp2 = chebvander(scale_e(e2), pdeg)

    idx = correction_indices(corrdeg)
    Tm = chebvander(scale_e(mu), corrdeg)
    Tr = chebvander(scale_r2(r2), corrdeg)
    C = np.column_stack([Tm[:,m]*Tr[:,n] for m,n in idx])

    F1 = np.hstack([Tp1, C, C*e1[:,None]])
    F2 = np.hstack([Tp2, C, C*e2[:,None]])
    return np.vstack([F1,F2])


def fit_model(pdeg=12, corrdeg=8, ngrid=45, rank_tol=1e-11):
    values = np.linspace(EMIN, EMAX, ngrid)
    E1,E2 = np.meshgrid(values, values, indexing="ij")
    e1,e2 = E1.ravel(),E2.ravel()
    s1,s2 = frozen_oracle(e1,e2)
    F = design_rows(e1,e2,pdeg,corrdeg)
    y = np.r_[s1,s2]

    Q,R,piv = la.qr(F, mode="economic", pivoting=True)
    diag = np.abs(np.diag(R))
    rank = int(np.sum(diag > rank_tol*diag[0]))
    selected = np.sort(piv[:rank])
    Fs = F[:,selected]
    coef_s, *_ = np.linalg.lstsq(Fs,y,rcond=None)
    coef = np.zeros(F.shape[1])
    coef[selected] = coef_s
    sing = np.linalg.svd(Fs,compute_uv=False)
    cond = float(sing[0]/sing[-1])
    return coef, rank, cond


def evaluate(coef,pdeg,corrdeg,ngrid=101):
    values = np.linspace(EMIN, EMAX, ngrid)
    E1,E2 = np.meshgrid(values, values, indexing="ij")
    e1,e2 = E1.ravel(),E2.ravel()
    s1,s2 = frozen_oracle(e1,e2)
    F = design_rows(e1,e2,pdeg,corrdeg)
    yp = F @ coef
    n = len(e1)
    err = np.r_[np.abs(yp[:n]-s1),np.abs(yp[n:]-s2)]
    return {
        "mean": float(np.mean(err)),
        "p95": float(np.quantile(err,0.95)),
        "max": float(np.max(err)),
        "rmse": float(np.sqrt(np.mean(err**2))),
    }


def main():
    for d in (4,8,10,12):
        coef,rank,cond = fit_model(12,d)
        stats = evaluate(coef,12,d)
        print({"pdeg":12,"corrdeg":d,"rank":rank,"cond":cond,**stats})


if __name__ == "__main__":
    main()
