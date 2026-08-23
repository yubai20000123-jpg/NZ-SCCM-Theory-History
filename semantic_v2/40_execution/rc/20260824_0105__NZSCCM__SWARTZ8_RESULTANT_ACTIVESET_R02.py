from __future__ import annotations

"""Optimizer-free resultant-only active-set driver for Swartz common-8.

This supersedes only the R01 SLSQP numerical table. The Marguerre-Air y front
end and resultant-only Brondum-Nielsen-family terminal architecture are unchanged.

No concrete point stress/strain law, thickness integration, material points,
or experimental load enters the solver. Pf is comparator-only.
"""

import math
import numpy as np
from scipy.optimize import brentq

B = 1220.0
NU = 0.18
ES = 200000.0
FY = 530.0
Q0 = 1.0 / 400.0

CASES = {
    4: dict(t=25.40, fc=23.63, E0=23772., p=.0050, hr=9.20, L=2, ell=2440./3., Pf=534.231415992786),
    5: dict(t=25.40, fc=22.72, E0=21460., p=.0075, hr=9.20, L=2, ell=2440./3., Pf=623.640670459522),
    6: dict(t=26.40, fc=24.43, E0=18058., p=.0075, hr=9.70, L=2, ell=2440./3., Pf=691.6984611730078),
    8: dict(t=24.64, fc=22.05, E0=20830., p=.0100, hr=8.82, L=2, ell=610., Pf=455.0530712411491),
    9: dict(t=31.75, fc=17.67, E0=15480., p=.0020, hr=0., L=1, ell=2440./3., Pf=625.8647812671522),
    14:dict(t=32.26, fc=19.79, E0=17995., p=.0075, hr=12.63, L=2, ell=2440., Pf=716.1636800569404),
    21:dict(t=19.30, fc=24.98, E0=20321., p=.0075, hr=0., L=1, ell=1220., Pf=368.3127497435694),
    23:dict(t=19.38, fc=23.40, E0=23818., p=.0100, hr=0., L=1, ell=2440./3., Pf=346.96128599031897),
}


def structural(c):
    t, E0, p, hr, L, ell = c['t'], c['E0'], c['p'], c['hr'], c['L'], c['ell']
    As_dir_total = p * t / 2.0
    As_layer = As_dir_total / L
    zs = np.array([0.0]) if L == 1 else np.array([-hr, +hr], dtype=float)
    den = 1.0 - NU**2
    Q = E0 / den
    Q12 = NU * E0 / den
    Q66 = E0 / (2.0 * (1.0 + NU))
    tconc = t - 2.0 * As_dir_total
    A11 = Q * tconc + ES * As_dir_total
    A22 = A11
    A12 = Q12 * tconc
    Ig = t**3 / 12.0
    Iconc = Ig - np.sum(2.0 * As_layer * zs**2)
    Dx = Q * Iconc + ES * np.sum(As_layer * zs**2)
    Dy = Dx
    Dmu = Q12 * Iconc
    D66 = Q66 * Iconc
    H = Dmu + 2.0 * D66
    alpha = math.pi / B
    beta = math.pi / ell
    Delta = A11 * A22 - A12 * A12
    Pcr = B * (Dx * alpha**4 + 2.0 * H * alpha**2 * beta**2 + Dy * beta**4) / beta**2 / 1000.0
    Kx = B**2 * alpha**2 * Delta / (8.0 * A22)
    Ky = B**2 * beta**2 * Delta / (8.0 * A11)
    C = B / 2.0 * (Ky + Kx * alpha**2 / beta**2) / 1000.0
    Jx = B * (Dx * alpha**2 + Dmu * beta**2)
    Jy = B * (Dmu * alpha**2 + Dy * beta**2)
    d = np.array([alpha**2, beta**2], dtype=float)
    d /= np.linalg.norm(d)
    return dict(As=As_layer, zs=zs, Pcr=Pcr, Kx=Kx, Ky=Ky, C=C,
                Jx=Jx, Jy=Jy, d=d, alpha=alpha, beta=beta)


def demand(c, q):
    s = structural(c)
    Qg = q * (q + 2.0 * Q0)
    P = s['Pcr'] * q / (q + Q0) + s['C'] * Qg
    Nx = s['Kx'] * Qg
    Ny = -(P * 1000.0 / B - s['Ky'] * Qg)
    Mx = s['Jx'] * q
    My = s['Jy'] * q
    return P, Nx, Ny, Mx, My


def positive_roots(fun, qmin=1e-7, qmax=0.03, n=2000):
    qs = np.geomspace(qmin, qmax, n)
    vals = [float(fun(q)) for q in qs]
    roots = []
    for a, b, fa, fb in zip(qs[:-1], qs[1:], vals[:-1], vals[1:]):
        if fa == 0.0:
            roots.append(a)
        elif fa * fb < 0.0:
            roots.append(brentq(fun, a, b, xtol=1e-13, rtol=1e-12))
    out = []
    for q in roots:
        if q > 0 and all(abs(q-r) > 1e-9 for r in out):
            out.append(q)
    return out


def solve_family_bottom_upper(c):
    """Cases 4/5/6/8/9/23 controlling family."""
    st = structural(c)
    h, fc = c['t']/2.0, c['fc']
    Fs = st['As'] * FY
    zplus = c['hr'] if c['L'] == 2 else 0.0
    Ty = Fs if c['L'] == 2 else 0.0
    Tx = Fs
    d = st['d']

    def residual(q):
        _, Nx, Ny, Mxd, Myd = demand(c, q)
        cb = (Ty - Ny) / fc
        zb = -h + cb / 2.0
        Cxb = Nx - Tx
        Cyb = -fc * cb
        Mxu = zb * Cxb + zplus * Tx
        Myu = zb * Cyb + zplus * Ty
        return d[0]*Mxu + d[1]*Myu - (d[0]*Mxd + d[1]*Myd)

    roots = positive_roots(residual)
    admissible = []
    for q in roots:
        _, Nx, Ny, _, _ = demand(c, q)
        cb = (Ty - Ny) / fc
        Cxb = Nx - Tx
        if 0.0 <= cb <= c['t'] and -fc*cb <= Cxb <= 0.0:
            admissible.append(q)
    if not admissible:
        raise RuntimeError('no admissible bottom+upper active root')
    return max(admissible)


def solve_case21(c):
    st = structural(c)
    h, fc = c['t']/2.0, c['fc']
    Fs = st['As'] * FY
    d = st['d']

    def cb_stationary(q):
        _, Nx, _, _, _ = demand(c, q)
        return h + d[0] * (Nx - Fs) / (2.0 * d[1] * fc)

    def residual(q):
        _, Nx, _, Mxd, Myd = demand(c, q)
        cb = cb_stationary(q)
        zb = -h + cb / 2.0
        Mpu = zb * (d[0]*(Nx-Fs) - d[1]*fc*cb)
        return Mpu - (d[0]*Mxd + d[1]*Myd)

    roots = positive_roots(residual)
    admissible = []
    for q in roots:
        _, Nx, Ny, _, _ = demand(c, q)
        cb = cb_stationary(q)
        Sy = Ny + fc * cb
        Cxb = Nx - Fs
        if 0.0 <= cb <= c['t'] and 0.0 <= Sy <= Fs and -fc*cb <= Cxb <= 0.0:
            admissible.append(q)
    if not admissible:
        raise RuntimeError('no admissible Case21 stationary root')
    return max(admissible)


def bounded_moment_interval(N, c, ct, cb):
    """Exact finite allocation theorem; used only as a feasibility witness."""
    st = structural(c)
    h, fc = c['t']/2.0, c['fc']
    Fs = st['As'] * FY
    items = [
        (h-ct/2.0, -fc*ct, 0.0),
        (-h+cb/2.0, -fc*cb, 0.0),
    ]
    for z in st['zs']:
        items.append((float(z), 0.0, Fs))
    L = sum(lo for _, lo, _ in items)
    U = sum(hi for _, _, hi in items)
    if not (L-1e-10 <= N <= U+1e-10):
        return None

    def extreme(desc):
        M = sum(z*lo for z, lo, _ in items)
        delta = N - L
        for z, lo, hi in sorted(items, key=lambda a: a[0], reverse=desc):
            inc = min(max(delta, 0.0), hi-lo)
            M += z * inc
            delta -= inc
        return M

    return extreme(False), extreme(True)


def solve_case14(c):
    fc, t = c['fc'], c['t']
    roots = positive_roots(lambda q: demand(c, q)[2] + fc*t)
    if not roots:
        raise RuntimeError('no Case14 Ny force-floor root')
    q = max(roots)
    st = structural(c)
    _, Nx, _, Mxd, Myd = demand(c, q)
    d = st['d']
    # Symmetric ct=cb=t/2 gives full-depth y compression and Myu=0.
    ct = cb = t/2.0
    interval = bounded_moment_interval(Nx, c, ct, cb)
    if interval is None:
        raise RuntimeError('Case14 x force not feasible at force-floor root')
    req_Mx = (d[0]*Mxd + d[1]*Myd) / d[0]
    if not (interval[0]-1e-8 <= req_Mx <= interval[1]+1e-8):
        raise RuntimeError('Case14 projected moment not feasible at force-floor root')
    return q


def solve_full(case, c):
    if case in (4,5,6,8,9,23):
        return solve_family_bottom_upper(c)
    if case == 21:
        return solve_case21(c)
    if case == 14:
        return solve_case14(c)
    raise KeyError(case)


def solve_uniaxial(c):
    """Controlled ablation: same resultant capacity, enforce Ny-My only."""
    st = structural(c)
    h, fc = c['t']/2.0, c['fc']
    Fs = st['As'] * FY
    zplus = c['hr'] if c['L'] == 2 else 0.0

    def env(q):
        _, _, Ny, _, Myd = demand(c, q)
        # Active family valid for the eight roots: bottom compression + highest
        # positive-ordinate tension layer (or mid-plane steel at z=0).
        lo = max(0.0, -Ny/fc)
        hi = min(c['t'], (Fs-Ny)/fc)
        if lo > hi:
            return -1e12
        cb = min(max(h+zplus, lo), hi)
        Ty = Ny + fc*cb
        zb = -h + cb/2.0
        Myu = zb*(-fc*cb) + zplus*Ty
        return Myu - Myd

    roots = positive_roots(env)
    if not roots:
        raise RuntimeError('no uniaxial resultant root')
    return max(roots)


def main():
    efull, euni = [], []
    print('case,ell_mm,q_full,Pu_full_kN,q_uni,Pu_uni_kN,Pf_kN,error_full_pct,error_uni_pct')
    for case, c in CASES.items():
        qf = solve_full(case, c)
        qu = solve_uniaxial(c)
        Pf = c['Pf']
        Pfull = float(demand(c, qf)[0])
        Puni = float(demand(c, qu)[0])
        e1 = (Pfull/Pf-1.0)*100.0
        e2 = (Puni/Pf-1.0)*100.0
        efull.append(e1); euni.append(e2)
        print(f'{case},{c["ell"]:.10f},{qf:.12f},{Pfull:.9f},{qu:.12f},{Puni:.9f},{Pf:.9f},{e1:.8f},{e2:.8f}')
    for name, arr in [('FULL', np.asarray(efull)), ('UNI', np.asarray(euni))]:
        print(name, 'mean_signed', arr.mean(), 'MAE', np.abs(arr).mean(), 'RMSE', np.sqrt(np.mean(arr*arr)))


if __name__ == '__main__':
    main()
