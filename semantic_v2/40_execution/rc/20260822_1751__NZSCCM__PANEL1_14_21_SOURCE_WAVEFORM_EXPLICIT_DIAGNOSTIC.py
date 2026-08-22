from __future__ import annotations

"""Source-waveform-conditioned explicit diagnostic for Swartz Panels 1, 14, 21.

This script does NOT predict a waveform and does NOT fit any coefficient to the
experimental failure load.  The normalized longitudinal waveform is digitized
from Nguyen Figs. 5.7a, 5.8a and 5.6a respectively, then frozen as a short finite
sine series.  The finite series is used only as an exogenous geometry input.

Formal structural integration is analytic: all Fourier products are reduced to
finite cosine coefficient dictionaries and exact orthogonality sums.  There is no
spatial quadrature or material-point integration in the structural operator.

The last section is deliberately a diagnostic only.  It shows the complete plate
resultants Mx, My, Mxy and the affine-through-thickness kinematic state at the
current 1D capacity control point.  It does NOT claim a final full-2D Pu because
the current TC-R2 section reduction has only one independent curvature slope.
"""

from collections import defaultdict
import math
import numpy as np
from scipy.optimize import root, minimize_scalar

A = 2440.0
B = 1220.0
NU = 0.18
ES = 200000.0
FY = 530.0
Q0 = 1.0 / 400.0

PANELS = {
    1: dict(t=25.40, fc=22.81, E0=21730.0, eps0=0.00210, p=0.0020,
            z=(0.0,), Pf=490.1940220017071),
    14: dict(t=32.26, fc=16.82, E0=17995.0, eps0=0.00187, p=0.0075,
             z=(-12.63, +12.63), Pf=716.1636800569404),
    21: dict(t=19.30, fc=21.23, E0=20321.0, eps0=0.00209, p=0.0075,
             z=(0.0,), Pf=368.3127497435694),
}

# Nine longitudinal stations y/a = 0,1/8,...,1 manually digitized from the
# Nguyen scanned FE surfaces.  Only normalized shape is used; the figures do not
# provide a metric deflection axis.
DIGITIZED_RAW = {
    1: np.array([0.0, 52.6, 88.3, 110.9, 123.5, 127.1, 111.8, 72.4, 0.0]),
    14: np.array([0.0, 54.8, 87.1, 108.4, 119.8, 116.1, 97.4, 58.7, 0.0]),
    21: np.array([0.0, -15.0, -63.0, -91.0, -24.0, 54.0, 71.0, 38.0, 0.0]),
}

# Frozen finite-series descriptions from those station ordinates.  Panel 1/14 use
# n=1..3; Panel 21 needs n=1..4 to retain its unequal two-lobe shape.
PHI_COEFF = {
    1: np.array([+1.04276809, -0.09582984, +0.08299371]),
    14: np.array([+1.05654776, -0.03901107, +0.06242867]),
    21: np.array([-0.12203066, -0.76471804, +0.18158893, +0.25675995]),
}


def rc_stiffness(panel: dict) -> dict:
    t, E0, p = panel["t"], panel["E0"], panel["p"]
    z = panel["z"]
    L = len(z)
    ax = [p * t / L] * L
    ay = [p * t / L] * L
    Q = E0 / (1.0 - NU**2)
    Q12 = NU * E0 / (1.0 - NU**2)
    Q66 = E0 / (2.0 * (1.0 + NU))
    t_conc = t - sum(np.asarray(ax) + np.asarray(ay))
    A11 = Q * t_conc + ES * sum(ax)
    A22 = Q * t_conc + ES * sum(ay)
    A12 = Q12 * t_conc
    A66 = Q66 * t_conc
    Ieff = t**3 / 12.0 - sum((ax[i] + ay[i]) * z[i] ** 2 for i in range(L))
    Dx = Q * Ieff + ES * sum(ax[i] * z[i] ** 2 for i in range(L))
    Dy = Q * Ieff + ES * sum(ay[i] * z[i] ** 2 for i in range(L))
    Dmu = Q12 * Ieff
    D66 = Q66 * Ieff
    H = Dmu + 2.0 * D66
    return locals()


def phi_values(c: np.ndarray, u: float) -> tuple[float, float, float]:
    n = np.arange(1, len(c) + 1, dtype=float)
    k = n * math.pi / A
    th = math.pi * u
    phi = float(np.sum(c * np.sin(n * th)))
    phip = float(np.sum(c * k * np.cos(n * th)))
    phipp = float(np.sum(-c * k**2 * np.sin(n * th)))
    return phi, phip, phipp


def product_cos_coeffs(c: np.ndarray) -> tuple[dict[int, float], dict[int, float]]:
    """Return exact finite cosine coefficients of
       f0 = Phi_y^2 + Phi Phi_yy,
       f2 = Phi_y^2 - Phi Phi_yy.
    """
    k0 = math.pi / A
    f0 = defaultdict(float)
    f2 = defaultdict(float)
    for n in range(1, len(c) + 1):
        for m in range(1, len(c) + 1):
            fac = 0.5 * c[n - 1] * c[m - 1] * k0**2
            kd, ks = abs(n - m), n + m
            f0[kd] += fac * (n * m - m**2)
            f0[ks] += fac * (n * m + m**2)
            f2[kd] += fac * (n * m + m**2)
            f2[ks] += fac * (n * m - m**2)
    return dict(f0), dict(f2)


def build_wave_operator(panel: dict, c: np.ndarray) -> dict:
    st = rc_stiffness(panel)
    alpha = math.pi / B
    Delta = st["A11"] * st["A22"] - st["A12"] ** 2
    abar11 = st["A22"] / Delta
    abar22 = st["A11"] / Delta
    abar12 = -st["A12"] / Delta
    abar66 = 1.0 / st["A66"]
    k0 = math.pi / A

    f0, f2 = product_cos_coeffs(c)
    r0 = {k: alpha**2 * v / 2.0 for k, v in f0.items()}
    r2 = {k: alpha**2 * v / 2.0 for k, v in f2.items()}

    # theta_p = B^2 Q [sum t0_k cos(k*pi*y/a)
    #                   + cos(2 alpha x) sum t2_k cos(k*pi*y/a)]
    t0, t2 = {}, {}
    for k, rhs in r0.items():
        if k == 0:
            if abs(rhs) > 1e-12:
                raise RuntimeError("non-zero incompatible mean in f0")
            continue
        mu = k * k0
        t0[k] = rhs / (abar11 * mu**4)
    for k, rhs in r2.items():
        mu = k * k0
        eig = (abar22 * (2 * alpha) ** 4
               + (2 * abar12 + abar66) * (2 * alpha) ** 2 * mu**2
               + abar11 * mu**4)
        t2[k] = rhs / eig

    n = np.arange(1, len(c) + 1, dtype=float)
    I0 = A / 2.0 * float(np.sum(c**2))
    I1 = A / 2.0 * float(np.sum((n * k0) ** 2 * c**2))
    I2 = A / 2.0 * float(np.sum((n * k0) ** 4 * c**2))

    Pcr = B * (st["Dx"] * alpha**4 * I0
               + 2 * st["H"] * alpha**2 * I1
               + st["Dy"] * I2) / I1

    # Compatibility symmetry gives M0=-int[Theta,Phi]Phi=2 int Theta*R.
    integ = 0.0
    for k, tv in t0.items():
        Iy = A / 2.0 if k > 0 else A
        integ += tv * r0[k] * B * Iy
    for k, tv in t2.items():
        Iy = A / 2.0 if k > 0 else A
        integ += tv * r2[k] * (B / 2.0) * Iy
    M0 = 2.0 * integ
    L0 = B / 2.0 * I1
    C = B**3 * M0 / L0

    return dict(panel=panel, c=c, st=st, alpha=alpha, Pcr=Pcr, C=C,
                r0=r0, r2=r2, t0=t0, t2=t2, I0=I0, I1=I1, I2=I2)


def resultants(op: dict, q: float, s: float, u: float) -> dict:
    alpha = op["alpha"]
    x = math.asin(max(0.0, min(1.0, s))) / alpha
    cos2 = math.cos(2.0 * alpha * x)
    sin2 = math.sin(2.0 * alpha * x)
    cos1 = math.cos(alpha * x)
    xi = math.pi * u
    k0 = math.pi / A
    Qgeom = q * (q + 2.0 * Q0)
    P = op["Pcr"] * q / (q + Q0) + op["C"] * Qgeom

    Nx = 0.0
    Ny = -P / B
    Nxy = 0.0
    for k, tv in op["t0"].items():
        mu = k * k0
        Nx += B**2 * Qgeom * (-mu**2) * tv * math.cos(k * xi)
    for k, tv in op["t2"].items():
        mu = k * k0
        ck, sk = math.cos(k * xi), math.sin(k * xi)
        Nx += B**2 * Qgeom * cos2 * (-mu**2) * tv * ck
        Ny += B**2 * Qgeom * (-4.0 * alpha**2) * cos2 * tv * ck
        if k > 0:
            Nxy += B**2 * Qgeom * (-2.0 * alpha * mu) * sin2 * tv * sk

    phi, phip, phipp = phi_values(op["c"], u)
    st = op["st"]
    Mx = B * q * s * (st["Dx"] * alpha**2 * phi - st["Dmu"] * phipp)
    My = B * q * s * (st["Dmu"] * alpha**2 * phi - st["Dy"] * phipp)
    Mxy = -2.0 * st["D66"] * B * q * alpha * cos1 * phip
    return dict(P=P, Nx=Nx, Ny=Ny, Nxy=Nxy, Mx=Mx, My=My, Mxy=Mxy,
                phi=phi, phip=phip, phipp=phipp)


def section_capacity(panel: dict, st: dict, cna: float) -> tuple[float, float]:
    t, fc, eps0 = panel["t"], panel["fc"], panel["eps0"]
    h = t / 2.0
    if cna <= t:
        Nc = 2.0 / 3.0 * fc * cna
        Mc = 2.0 / 3.0 * fc * h * cna - 0.25 * fc * cna**2
    else:
        Nc = fc * (t - t**3 / (3.0 * cna**2))
        Mc = fc * t**4 / (12.0 * cna**2)
    Nu, Mu = Nc, Mc
    for ax, ay, z in zip(st["ax"], st["ay"], st["z"]):
        yl = h - z
        epss = eps0 * (1.0 - yl / cna)
        sigs = float(np.clip(ES * epss, -FY, FY))
        if yl < cna:
            sigc = fc * (1.0 - yl**2 / cna**2)
            Nu -= (ax + ay) * sigc
            Mu -= (ax + ay) * sigc * z
        Nu += ay * sigs
        Mu += ay * sigs * z
    return Nu, Mu


def local_capacity_root(op: dict, s: float, u: float) -> tuple[float, float, float] | None:
    panel, st = op["panel"], op["st"]

    def eq(x):
        q, cna = x
        if q <= 0.0 or cna <= 0.0:
            return np.array([1e6, 1e6])
        r = resultants(op, q, s, u)
        Nu, Mu = section_capacity(panel, st, cna)
        return np.array([-r["Ny"] - Nu, abs(r["My"]) - Mu])

    roots = []
    for qg in (1e-4, 5e-4, 1e-3, 2e-3, 4e-3, 8e-3, 1.5e-2):
        for cg in (0.4 * panel["t"], 0.8 * panel["t"], 1.5 * panel["t"],
                   2.5 * panel["t"], 4.0 * panel["t"]):
            sol = root(eq, [qg, cg])
            if not sol.success:
                continue
            q, cna = map(float, sol.x)
            if q <= 0 or cna <= 0 or np.linalg.norm(eq([q, cna])) > 1e-5:
                continue
            P = resultants(op, q, s, u)["P"]
            if P > 0:
                roots.append((q, cna, P))
    return min(roots) if roots else None


def control_root(op: dict, bracket: tuple[float, float]) -> tuple[float, float, float, float]:
    # All three representative runs localize to the transverse centre s=1.  The
    # remaining longitudinal coordinate is minimized continuously; this is not a
    # spatial quadrature/material grid.
    def obj(u):
        rr = local_capacity_root(op, 1.0, float(u))
        return rr[0] if rr else 1e3
    opt = minimize_scalar(obj, bounds=bracket, method="bounded", options={"xatol": 1e-12})
    rr = local_capacity_root(op, 1.0, float(opt.x))
    if rr is None:
        raise RuntimeError("no positive capacity root")
    q, cna, P = rr
    return q, cna, P, float(opt.x)


def material_coordinate_diagnostic(op: dict, q: float, u: float) -> list[dict]:
    panel, st = op["panel"], op["st"]
    r = resultants(op, q, 1.0, u)
    Delta = st["A11"] * st["A22"] - st["A12"]**2
    ex0 = (st["A22"] * r["Nx"] - st["A12"] * r["Ny"]) / Delta
    ey0 = (-st["A12"] * r["Nx"] + st["A11"] * r["Ny"]) / Delta
    phi, _, phipp = phi_values(op["c"], u)
    kx = B * q * op["alpha"]**2 * phi
    ky = -B * q * phipp
    out = []
    for z in (-panel["t"] / 2.0, 0.0, panel["t"] / 2.0):
        ex = ex0 + z * kx
        ey = ey0 + z * ky
        lt = (ex + NU * ey) / (panel["eps0"] * (1.0 - NU**2))
        lc = (ey + NU * ex) / (panel["eps0"] * (1.0 - NU**2))
        out.append(dict(z=z, ex=ex, ey=ey, lambda_t=lt, lambda_c=lc))
    return out


def main() -> None:
    brackets = {1: (0.60, 0.90), 14: (0.60, 0.90), 21: (0.25, 0.50)}
    for case in (1, 14, 21):
        panel = PANELS[case]
        c = PHI_COEFF[case]
        op = build_wave_operator(panel, c)
        q, cna, P, u = control_root(op, brackets[case])
        r = resultants(op, q, 1.0, u)
        err = 100.0 * (P / 1000.0 / panel["Pf"] - 1.0)
        raw = DIGITIZED_RAW[case] / np.max(np.abs(DIGITIZED_RAW[case]))
        us = np.arange(9, dtype=float) / 8.0
        fit = np.array([phi_values(c, uu)[0] for uu in us])
        rmse = float(np.sqrt(np.mean((fit - raw)**2)))
        print(f"\nPANEL {case}")
        print("phi_coeff =", c.tolist(), "station_RMSE =", rmse)
        print("Pcr_kN =", op["Pcr"] / 1000.0, "C_kN =", op["C"] / 1000.0)
        print("q =", q, "c_mm =", cna, "u =", u)
        print("Pu_kN =", P / 1000.0, "Pf_kN =", panel["Pf"], "error_pct =", err)
        print("resultants =", {k: r[k] for k in ("Nx", "Ny", "Nxy", "Mx", "My", "Mxy")})
        print("thickness_material_coordinates =", material_coordinate_diagnostic(op, q, u))


if __name__ == "__main__":
    main()
