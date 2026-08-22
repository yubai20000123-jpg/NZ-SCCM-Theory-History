from __future__ import annotations

"""NC-M6 reinforcement-dependent postcrack-tension source-closure diagnostic.

Hard boundary:
- imports and reuses the frozen 20260822_2130 NC-M6 explicit structural operator;
- source waveforms, P_phi(q), (a_x,a_y,b_x,b_y), Nx/Ny/Mx/My equilibrium unchanged;
- NC CC, TT and Vecchio-Collins gamma formulas unchanged;
- no formal spatial quadrature and no through-thickness material-point rule;
- Pf is comparison-only after theoretical event localization.

This diagnostic tests a continuity-preserving, source-anchored projection of Bentz
bond-dependent tension stiffening into the existing finite Foster grammar.
It is a project-derived diagnostic, not a literal Foster/Bentz production law.
"""

from pathlib import Path
import importlib.util
import cmath
import math
import numpy as np
from scipy.optimize import root, root_scalar
from scipy.signal import residue

M6_PATH = Path(__file__).with_name(
    "20260822_2130__NZSCCM__NC_M6_2D_TC_CRACK_FRONT_EXACT_SECTION.py"
)
spec = importlib.util.spec_from_file_location("m6_2130", M6_PATH)
m6 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(m6)

old, base = m6.old, m6.base
NU, ES, FY = m6.NU, m6.ES, m6.FY
SOFTEN_ONSET = m6.SOFTEN_ONSET
PANELS, PHI_COEFF = base.PANELS, base.PHI_COEFF

DB = 2.7  # mm; Swartz No.12 gage wire source
TD_MODIFIED_BENTZ = 0.6


def ptrim(p):
    p = np.asarray(p, float)
    while len(p) > 1 and abs(p[-1]) < 1.0e-14:
        p = p[:-1]
    return p


def padd(a, b):
    return np.polynomial.polynomial.polyadd(a, b)


def psub(a, b):
    return np.polynomial.polynomial.polysub(a, b)


def pmul(a, b):
    return np.polynomial.polynomial.polymul(a, b)


def pscale(a, c):
    return np.asarray(a, float) * float(c)


def ppow(a, n):
    out = np.array([1.0])
    for _ in range(int(n)):
        out = pmul(out, a)
    return out


def comp_rat(lam_poly, panel, branch, tangent=False):
    """Compression branch as numerator/denominator polynomials in z."""
    fc = panel["fc"]
    K = panel["E0"] * panel["eps0"]
    if branch == "C_RESIDUAL":
        return np.array([0.0 if tangent else -0.1 * fc]), np.array([1.0])
    if branch == "C_POSTPEAK":
        if tangent:
            return np.array([-0.1 * fc]), np.array([1.0])
        return padd(np.array([-1.1 * fc]), pscale(lam_poly, -0.1 * fc)), np.array([1.0])
    if branch == "C_SAENZ":
        kap = K / fc
        aa = kap - 2.0
        den = padd(psub(ppow(lam_poly, 2), pscale(lam_poly, aa)), np.array([1.0]))
        if tangent:
            return pscale(psub(np.array([1.0]), ppow(lam_poly, 2)), K), ppow(den, 2)
        return pscale(lam_poly, K), den
    raise ValueError(branch)


def ratint(num, den, x0, x1):
    """Evaluate a finite rational primitive by partial fractions; no quadrature."""
    num, den = ptrim(num), ptrim(den)
    r, p, k = residue(num[::-1], den[::-1], tol=1.0e-4)
    val = 0j
    if len(k):
        ki = np.polyint(k)
        val += np.polyval(ki, x1) - np.polyval(ki, x0)
    i = 0
    while i < len(p):
        pole = p[i]
        j = i
        while j < len(p) and abs(p[j] - pole) < 1.0e-5 * max(1.0, abs(pole)):
            order = j - i + 1
            rr = r[j]
            if order == 1:
                val += rr * (cmath.log(x1 - pole) - cmath.log(x0 - pole))
            else:
                val += rr / (1 - order) * (
                    (x1 - pole) ** (1 - order) - (x0 - pole) ** (1 - order)
                )
            j += 1
        i = j
    return float(val.real)


def gamma_comp_integrals(ac, bc, at, bt, lo, hi, panel):
    """Exact rational primitive for the unchanged VC gamma branch."""
    zm = 0.5 * (lo + hi)
    cbr = old.branch_id(ac + bc * zm, panel)
    if not cbr.startswith("C_"):
        raise RuntimeError(cbr)
    lcp = np.array([ac, bc])
    ltp = np.array([at, bt])
    scn, scd = comp_rat(lcp, panel, cbr, False)
    Dcn, Dcd = comp_rat(lcp, panel, cbr, True)
    g = padd(np.array([0.8]), pscale(ltp, 0.34))

    def zpow(k):
        return np.array([0.0] * k + [1.0])

    Nc = ratint(scn, pmul(scd, g), lo, hi)
    Mc = ratint(pmul(scn, zpow(1)), pmul(scd, g), lo, hi)
    Clc, Clt = [], []
    for k in range(3):
        Clc.append(ratint(pmul(Dcn, zpow(k)), pmul(Dcd, g), lo, hi))
        Clt.append(ratint(pscale(pmul(scn, zpow(k)), -0.34),
                          pmul(scd, ppow(g, 2)), lo, hi))
    return Nc, Mc, Clc, Clt


def bond_alpha_target(panel, modified=False):
    """Bentz retention evaluated at the Foster alpha1=10 endpoint.

    This is a source-to-source projection used only as a diagnostic target.
    """
    rho = panel["p"]
    m = DB / (4.0 * rho)
    ct = (3.6 * TD_MODIFIED_BENTZ * m) if modified else (3.6 * m)
    epscr0 = 0.1 * panel["fc"] / panel["E0"]
    alpha = 1.0 / (1.0 + math.sqrt(ct * 10.0 * epscr0))
    return min(0.7, max(0.3, alpha)), m, ct


def blend_point_coeffs(sc, Dc, lt, panel, alphaB):
    """Continuity-preserving TC-only bond target.

    w_TC = 1 - fcr_TC/ft vanishes exactly at p0=0, hence the locked TT
    postcrack law is recovered at the TC->TT boundary.
    """
    fc = panel["fc"]
    ft = 0.1 * fc
    K = panel["E0"] * panel["eps0"]
    fcr, Bf, seg = m6.tc_fcr(sc, panel)
    xcr = fcr / K
    w = 1.0 - fcr / ft
    alpha = 0.3 + (alphaB - 0.3) * w
    dalpha_dlc = -(alphaB - 0.3) / ft * Bf * Dc

    if lt <= xcr:
        return K * lt, K, 0.0, fcr, alpha, "UNCR"
    if lt < 10.0 * xcr:
        d = (1.0 - alpha) / 9.0
        dd = -dalpha_dlc / 9.0
        st = fcr + d * (fcr - K * lt)
        dstlt = -d * K
        dstlc = (1.0 + d) * Bf * Dc + dd * (fcr - K * lt)
        return st, dstlt, dstlc, fcr, alpha, "SOFT"

    st = alpha * fcr
    dstlt = 0.0
    dstlc = dalpha_dlc * fcr + alpha * Bf * Dc
    return st, dstlt, dstlc, fcr, alpha, "RESID"


def scalar_extended(ac, bc, lo, hi, panel):
    """Exact moments needed by the blended law."""
    S0, S1, D0, D1, D2 = m6.scalar_integrals(ac, bc, lo, hi, panel)
    zm = 0.5 * (lo + hi)
    br = old.branch_id(ac + bc * zm, panel)

    if abs(bc) < 1.0e-12:
        sc, Dc = old.scalar_stress_tangent(ac, panel)
        I = [(hi ** (k + 1) - lo ** (k + 1)) / (k + 1) for k in range(5)]
        return (
            [sc * I[k] for k in range(3)],
            [Dc * I[k] for k in range(4)],
            [sc * sc * I[k] for k in range(2)],
            [sc * Dc * I[k] for k in range(3)],
        )

    lcp = np.array([ac, bc])
    scn, scd = comp_rat(lcp, panel, br, False)
    z2 = np.array([0.0, 0.0, 1.0])
    S2 = ratint(pmul(scn, z2), scd, lo, hi)
    S = [S0, S1, S2]

    s_lo, _ = old.scalar_stress_tangent(ac + bc * lo, panel)
    s_hi, _ = old.scalar_stress_tangent(ac + bc * hi, panel)
    D3 = (hi**3 * s_hi - lo**3 * s_lo - 3.0 * S2) / bc
    D = [D0, D1, D2, D3]

    qnum, qden = pmul(scn, scn), pmul(scd, scd)
    Q0 = ratint(qnum, qden, lo, hi)
    Q1 = ratint(pmul(qnum, [0.0, 1.0]), qden, lo, hi)
    Q = [Q0, Q1]

    SD0 = (s_hi**2 - s_lo**2) / (2.0 * bc)
    SD1 = (hi * s_hi**2 - lo * s_lo**2 - Q0) / (2.0 * bc)
    SD2 = (hi**2 * s_hi**2 - lo**2 * s_lo**2 - 2.0 * Q1) / (2.0 * bc)
    return S, D, Q, [SD0, SD1, SD2]


def tc_blend_moments(at, bt, ac, bc, lo, hi, panel, alphaB):
    zm = 0.5 * (lo + hi)
    lt, lc = at + bt * zm, ac + bc * zm
    sc, _ = old.scalar_stress_tangent(lc, panel)
    fcr, Bf, seg = m6.tc_fcr(sc, panel)
    K = panel["E0"] * panel["eps0"]
    ft = 0.1 * panel["fc"]
    mode = "UNCR" if K * lt <= fcr else ("SOFT" if K * lt < 10.0 * fcr else "RESID")
    I = [(hi ** (k + 1) - lo ** (k + 1)) / (k + 1) for k in range(4)]

    if mode == "UNCR":
        L = [at * I[k] + bt * I[k + 1] for k in range(3)]
        return K * L[0], K * L[1], [K * I[k] for k in range(3)], [0.0] * 3

    S, D, Q, SD = scalar_extended(ac, bc, lo, hi, panel)
    F0 = 0.1 * panel["fc"] if seg == "A" else 0.3 * panel["fc"]
    F = [F0 * I[k] + Bf * S[k] for k in range(3)]
    G = [F0**2 * I[k] + 2.0 * F0 * Bf * S[k] + Bf**2 * Q[k] for k in range(2)]
    L = [at * I[k] + bt * I[k + 1] for k in range(3)]
    H = [F0 * L[k] + Bf * (at * S[k] + bt * S[k + 1]) for k in range(2)]
    delta = alphaB - 0.3

    if mode == "SOFT":
        d0 = (1.0 - 0.3) / 9.0
        c = delta / 9.0
        Nt = ((1.0 + d0) * F[0] - d0 * K * L[0]
              - c * (F[0] - K * L[0]) + c / ft * (G[0] - K * H[0]))
        Mt = ((1.0 + d0) * F[1] - d0 * K * L[1]
              - c * (F[1] - K * L[1]) + c / ft * (G[1] - K * H[1]))
        Tlt = [K * ((-d0 + c) * I[k] - c / ft * F[k]) for k in range(3)]
        Tlc = []
        for k in range(3):
            fD = F0 * D[k] + Bf * SD[k]
            ltD = at * D[k] + bt * D[k + 1]
            Tlc.append(Bf * ((1.0 + d0 - c) * D[k] + c / ft * (2.0 * fD - K * ltD)))
    else:
        Nt = alphaB * F[0] - delta / ft * G[0]
        Mt = alphaB * F[1] - delta / ft * G[1]
        Tlt = [0.0, 0.0, 0.0]
        Tlc = []
        for k in range(3):
            fD = F0 * D[k] + Bf * SD[k]
            Tlc.append(Bf * (alphaB * D[k] - 2.0 * delta / ft * fD))

    return Nt, Mt, Tlt, Tlc


def section_resultant_and_jac(v, panel, st, alphaB, lower_y_bar_tangent=None):
    ax, ay, bx, by = map(float, v)
    R = np.zeros(4)
    J = np.zeros((4, 4))
    cuts = m6.section_cuts(v, panel)

    for lo, hi in zip(cuts[:-1], cuts[1:]):
        zm = 0.5 * (lo + hi)
        lx, ly = ax + bx * zm, ay + by * zm

        if (lx < 0.0 and ly < 0.0) or (lx >= 0.0 and ly >= 0.0):
            for a, b, rN, rM, cA, cB in (
                (ax, bx, 0, 2, 0, 2), (ay, by, 1, 3, 1, 3)
            ):
                N, M, D0, D1, D2 = m6.scalar_integrals(a, b, lo, hi, panel)
                R[rN] += N; R[rM] += M
                J[rN, cA] += D0; J[rN, cB] += D1
                J[rM, cA] += D1; J[rM, cB] += D2
            continue

        xt = lx >= 0.0
        if xt:
            at, bt, ac, bc = ax, bx, ay, by
            tN, tM, tA, tB = 0, 2, 0, 2
            cN, cM, cA, cB = 1, 3, 1, 3
            lt = lx
        else:
            at, bt, ac, bc = ay, by, ax, bx
            tN, tM, tA, tB = 1, 3, 1, 3
            cN, cM, cA, cB = 0, 2, 0, 2
            lt = ly

        Nt, Mt, Tlt, Tlc = tc_blend_moments(at, bt, ac, bc, lo, hi, panel, alphaB)
        R[tN] += Nt; R[tM] += Mt
        J[tN, tA] += Tlt[0]; J[tN, tB] += Tlt[1]
        J[tM, tA] += Tlt[1]; J[tM, tB] += Tlt[2]
        J[tN, cA] += Tlc[0]; J[tN, cB] += Tlc[1]
        J[tM, cA] += Tlc[1]; J[tM, cB] += Tlc[2]

        Nc0, Mc0, D0c, D1c, D2c = m6.scalar_integrals(ac, bc, lo, hi, panel)
        if lt > SOFTEN_ONSET:
            Nc, Mc, Clc, Clt = gamma_comp_integrals(ac, bc, at, bt, lo, hi, panel)
            R[cN] += Nc; R[cM] += Mc
            J[cN, cA] += Clc[0]; J[cN, cB] += Clc[1]
            J[cM, cA] += Clc[1]; J[cM, cB] += Clc[2]
            J[cN, tA] += Clt[0]; J[cN, tB] += Clt[1]
            J[cM, tA] += Clt[1]; J[cM, tB] += Clt[2]
        else:
            R[cN] += Nc0; R[cM] += Mc0
            J[cN, cA] += D0c; J[cN, cB] += D1c
            J[cM, cA] += D1c; J[cM, cB] += D2c

    # Reinforcement is still the same explicit bare EPP law; only displaced
    # concrete uses the new current-map stress/tangent.
    for arx, ary, z in zip(st["ax"], st["ay"], st["z"]):
        lx, ly = ax + bx * z, ay + by * z
        if (lx < 0.0 and ly < 0.0) or (lx >= 0.0 and ly >= 0.0):
            sx, Dx = old.scalar_stress_tangent(lx, panel)
            sy, Dy = old.scalar_stress_tangent(ly, panel)
            T = np.array([[Dx, 0.0], [0.0, Dy]])
        else:
            xt = lx >= 0.0
            lt, lc = (lx, ly) if xt else (ly, lx)
            sc, Dc = old.scalar_stress_tangent(lc, panel)
            stt, dt, dc, _, _, _ = blend_point_coeffs(sc, Dc, lt, panel, alphaB)
            if lt > SOFTEN_ONSET:
                gam = 1.0 / (0.8 + 0.34 * lt)
                scc = gam * sc
                dcc = gam * Dc
                dct = -0.34 * sc / (0.8 + 0.34 * lt) ** 2
            else:
                scc, dcc, dct = sc, Dc, 0.0
            if xt:
                sx, sy = stt, scc
                T = np.array([[dt, dc], [dct, dcc]])
            else:
                sx, sy = scc, stt
                T = np.array([[dcc, dct], [dc, dt]])

        ex = panel["eps0"] * (lx - NU * ly)
        ey = panel["eps0"] * (ly - NU * lx)
        tx, ty = ES * ex, ES * ey
        ssx, ssy = float(np.clip(tx, -FY, FY)), float(np.clip(ty, -FY, FY))
        Dsx = ES if abs(tx) < FY else 0.0
        Dsy = ES if abs(ty) < FY else 0.0
        if lower_y_bar_tangent is not None and abs(z + 12.63) < 1.0e-9:
            Dsy = float(lower_y_bar_tangent)

        atot = arx + ary
        Rx, Ry = -atot * sx + arx * ssx, -atot * sy + ary * ssy
        R += np.array([Rx, Ry, z * Rx, z * Ry])

        dlx = np.array([1.0, 0.0, z, 0.0])
        dly = np.array([0.0, 1.0, 0.0, z])
        dsx = T[0, 0] * dlx + T[0, 1] * dly
        dsy = T[1, 0] * dlx + T[1, 1] * dly
        dex = panel["eps0"] * (dlx - NU * dly)
        dey = panel["eps0"] * (dly - NU * dlx)
        dRx = -atot * dsx + arx * Dsx * dex
        dRy = -atot * dsy + ary * Dsy * dey
        J[0] += dRx; J[1] += dRy
        J[2] += z * dRx; J[3] += z * dRy

    return R, J


def fold_system(X, op, u, alphaB):
    v, q = X[:4], float(X[4])
    sec, J = section_resultant_and_jac(v, op["panel"], op["st"], alphaB)
    res = (sec - m6.demand4(op, q, u)) / np.array([100.0, 600.0, 600.0, 600.0])
    row = np.linalg.norm(J, axis=1); row[row == 0.0] = 1.0
    Jn = J / row[:, None]
    col = np.linalg.norm(Jn, axis=0); col[col == 0.0] = 1.0
    Jn /= col
    return np.r_[res, np.linalg.det(Jn)]


def panel14_yield_system(X, op, u, alphaB):
    v, q = X[:4], float(X[4])
    sec, _ = section_resultant_and_jac(v, op["panel"], op["st"], alphaB)
    res = (sec - m6.demand4(op, q, u)) / np.array([100.0, 600.0, 600.0, 600.0])
    z = -12.63
    lx, ly = v[0] + v[2] * z, v[1] + v[3] * z
    ey = op["panel"]["eps0"] * (ly - NU * lx)
    return np.r_[res, (ES * ey + FY) / FY]


SEED = {
    1: np.array([0.0384, -0.366, 0.0102, 0.00275, 0.00108]),
    14: np.array([0.0505, -1.1702, 0.0109, 0.0208, 0.000935]),
    21: np.array([0.0800, -0.169, -0.0226, -0.0120, 0.00144]),
}


def event_at_u(case, u, seed, alphaB):
    op = base.build_wave_operator(PANELS[case], PHI_COEFF[case])
    fun = (lambda X: panel14_yield_system(X, op, u, alphaB)) if case == 14 \
          else (lambda X: fold_system(X, op, u, alphaB))
    sol = root(fun, seed, options={"xtol": 1.0e-10, "maxfev": 3000})
    if (not sol.success) or np.linalg.norm(fun(sol.x)) > 1.0e-6:
        raise RuntimeError(f"event root failed panel={case}, u={u}, norm={np.linalg.norm(fun(sol.x))}")
    return sol.x


def stationary_event(case, alphaB):
    bracket = {1: (0.60, 0.67), 14: (0.72, 0.79), 21: (0.33, 0.38)}[case]
    seed = SEED[case]

    def dqdu(u):
        h = 2.0e-5
        qm = event_at_u(case, u - h, seed, alphaB)[4]
        qp = event_at_u(case, u + h, seed, alphaB)[4]
        return (qp - qm) / (2.0 * h)

    u = root_scalar(dqdu, bracket=bracket, xtol=1.0e-10).root
    return u, event_at_u(case, u, seed, alphaB)


def main():
    print("EXPLICIT_STRUCTURAL_PATH_CHANGED = FALSE")
    print("FORMAL_SPATIAL_QUADRATURE = 0")
    print("FORMAL_MATERIAL_POINTS = 0")
    print("Pf_IN_ROOT_SELECTION = 0")
    for label, modified in (("B99_3P6M", False), ("B03_TD0P6", True)):
        print("\nVARIANT", label)
        for case in (1, 14, 21):
            alphaB, m, ct = bond_alpha_target(PANELS[case], modified=modified)
            u, X = stationary_event(case, alphaB)
            op = base.build_wave_operator(PANELS[case], PHI_COEFF[case])
            P = base.resultants(op, X[4], 1.0, u)["P"] / 1000.0
            err = 100.0 * (P / PANELS[case]["Pf"] - 1.0)
            print(case, "alphaB", alphaB, "m_mm", m, "ct", ct,
                  "u", u, "q", X[4], "P_event_kN", P,
                  "post_solution_error_pct", err)


if __name__ == "__main__":
    main()
