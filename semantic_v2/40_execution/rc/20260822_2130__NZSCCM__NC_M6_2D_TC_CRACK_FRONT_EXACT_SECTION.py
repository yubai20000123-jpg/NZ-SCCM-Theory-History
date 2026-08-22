from __future__ import annotations

"""NC-M6 coupled 2D TC crack-front execution for Swartz Panels 1/14/21.

Hard boundary:
- reuse the frozen source-waveform explicit structural front end verbatim;
- reuse the full two-independent-affine-slope section variables;
- change only the NC TC crack-front/current branch;
- no spatial quadrature, no material-point mesh, no Pf in root selection.

The formal section resultants and Jacobian are exact finite branch primitives.
Scalar root solves are used only to localize moving material branch fronts in z.
"""

from pathlib import Path
import importlib.util
import math
import numpy as np
from scipy.optimize import root, root_scalar, brentq

OLD_PATH = Path(__file__).with_name(
    "20260822_1927__NZSCCM__PANEL1_14_21_TWO_SLOPE_FULL2D_SECTION_DIAGNOSTIC.py"
)
spec = importlib.util.spec_from_file_location("full2d1927", OLD_PATH)
old = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(old)

base = old.base
NU, ES, FY = old.NU, old.ES, old.FY
ALPHA1 = 10.0
ALPHA2 = 0.3
SOFTEN_ONSET = 10.0 / 17.0


def tc_fcr(sc: float, panel: dict) -> tuple[float, float, str]:
    fc, ft = panel["fc"], 0.1 * panel["fc"]
    r = max(0.0, -sc) / fc
    if r <= 0.8:
        return ft * (1.0 - 0.5 * r), ft / (2.0 * fc), "A"
    return 3.0 * ft * (1.0 - r), 3.0 * ft / fc, "B"


def _front_root(a: float, b: float, L: float, z0: float, z1: float):
    if abs(b) < 1.0e-16:
        return None
    z = (L - a) / b
    return z if z0 + 1.0e-12 < z < z1 - 1.0e-12 else None


def _uniq(xs, tol=1.0e-10):
    out = []
    for x in sorted(xs):
        if not out or abs(x - out[-1]) > tol:
            out.append(x)
    return out


def _add_bracket_root(dst: list[float], f, lo: float, hi: float):
    fl, fh = f(lo), f(hi)
    if not (np.isfinite(fl) and np.isfinite(fh)):
        return
    if abs(fl) < 1.0e-12 or abs(fh) < 1.0e-12:
        return
    if fl * fh < 0.0:
        z = brentq(f, lo, hi, xtol=1.0e-13, rtol=1.0e-13, maxiter=100)
        if lo + 1.0e-10 < z < hi - 1.0e-10:
            dst.append(z)


def section_cuts(v: np.ndarray, panel: dict) -> list[float]:
    ax, ay, bx, by = map(float, v)
    h = panel["t"] / 2.0
    z0, z1 = -h, h
    K = panel["E0"] * panel["eps0"]
    xcr0 = 0.1 * panel["fc"] / K
    cuts = [z0, z1]
    for a, b in ((ax, bx), (ay, by)):
        for L in (-10.0, -1.0, 0.0, xcr0, 10.0 * xcr0, SOFTEN_ONSET):
            z = _front_root(a, b, L, z0, z1)
            if z is not None:
                cuts.append(z)
    cuts = _uniq(cuts)

    extra = []
    for lo, hi in zip(cuts[:-1], cuts[1:]):
        z = 0.5 * (lo + hi)
        lx, ly = ax + bx * z, ay + by * z
        if lx * ly < 0.0:
            ac, bc = (ay, by) if lx > 0.0 else (ax, bx)
            def g08(zz):
                sc, _ = old.scalar_stress_tangent(ac + bc * zz, panel)
                return -sc - 0.8 * panel["fc"]
            _add_bracket_root(extra, g08, lo, hi)
    cuts = _uniq(cuts + extra)

    extra = []
    for lo, hi in zip(cuts[:-1], cuts[1:]):
        z = 0.5 * (lo + hi)
        lx, ly = ax + bx * z, ay + by * z
        if lx * ly < 0.0:
            if lx > 0.0:
                at, bt, ac, bc = ax, bx, ay, by
            else:
                at, bt, ac, bc = ay, by, ax, bx
            def fcr_z(zz):
                sc, _ = old.scalar_stress_tangent(ac + bc * zz, panel)
                return tc_fcr(sc, panel)[0]
            def gcr(zz):
                return K * (at + bt * zz) - fcr_z(zz)
            def gres(zz):
                return K * (at + bt * zz) - ALPHA1 * fcr_z(zz)
            _add_bracket_root(extra, gcr, lo, hi)
            _add_bracket_root(extra, gres, lo, hi)
    return _uniq(cuts + extra)


def scalar_integrals(a: float, b: float, lo: float, hi: float, panel: dict):
    N, M = old.affine_force_moment(a, b, lo, hi, panel)
    if abs(b) < 1.0e-12:
        _, D = old.scalar_stress_tangent(a, panel)
        D0 = D * (hi - lo)
        D1 = 0.5 * D * (hi**2 - lo**2)
        D2 = D * (hi**3 - lo**3) / 3.0
    else:
        s0, _ = old.scalar_stress_tangent(a + b * lo, panel)
        s1, _ = old.scalar_stress_tangent(a + b * hi, panel)
        D0 = (s1 - s0) / b
        D1 = (hi * s1 - lo * s0 - N) / b
        D2 = (hi**2 * s1 - lo**2 * s0 - 2.0 * M) / b
    return N, M, D0, D1, D2


def tc_linear_form(lt: float, lc: float, panel: dict):
    fc = panel["fc"]
    K = panel["E0"] * panel["eps0"]
    sc, _ = old.scalar_stress_tangent(lc, panel)
    fcr, _, seg = tc_fcr(sc, panel)
    xcrt = fcr / K
    if lt <= xcrt:
        return 0.0, 0.0, K, f"UNCRACKED_{seg}", False
    gamma_active = lt > SOFTEN_ONSET
    d = (1.0 - ALPHA2) / (ALPHA1 - 1.0)
    if seg == "A":
        F0, Bf = 0.1 * fc, 0.05
    else:
        F0, Bf = 0.3 * fc, 0.30
    if lt < ALPHA1 * xcrt:
        return (1.0 + d) * F0, (1.0 + d) * Bf, -d * K, f"SOFT_{seg}", gamma_active
    return ALPHA2 * F0, ALPHA2 * Bf, 0.0, f"RESID_{seg}", gamma_active


def point_map(lx: float, ly: float, panel: dict):
    if (lx < 0.0 and ly < 0.0) or (lx >= 0.0 and ly >= 0.0):
        sx, Dx = old.scalar_stress_tangent(lx, panel)
        sy, Dy = old.scalar_stress_tangent(ly, panel)
        return sx, sy, np.array([[Dx, 0.0], [0.0, Dy]]), False
    x_tension = lx >= 0.0
    lt, lc = (lx, ly) if x_tension else (ly, lx)
    sc, Dc = old.scalar_stress_tangent(lc, panel)
    A, Bc, C, _, gamma_active = tc_linear_form(lt, lc, panel)
    st = A + Bc * sc + C * lt
    dst_dlt, dst_dlc = C, Bc * Dc
    if gamma_active:
        gamma = 1.0 / (0.8 + 0.34 * lt)
        sc_eff = gamma * sc
        dsc_dlc = gamma * Dc
        dsc_dlt = -0.34 * sc / (0.8 + 0.34 * lt) ** 2
    else:
        sc_eff, dsc_dlc, dsc_dlt = sc, Dc, 0.0
    if x_tension:
        return st, sc_eff, np.array([[dst_dlt, dst_dlc], [dsc_dlt, dsc_dlc]]), gamma_active
    return sc_eff, st, np.array([[dsc_dlc, dsc_dlt], [dst_dlc, dst_dlt]]), gamma_active


def section_resultant_and_jac(v: np.ndarray, panel: dict, st: dict, lower_y_bar_tangent=None):
    ax, ay, bx, by = map(float, v)
    R = np.zeros(4, float)
    J = np.zeros((4, 4), float)
    cuts = section_cuts(v, panel)

    for lo, hi in zip(cuts[:-1], cuts[1:]):
        z = 0.5 * (lo + hi)
        lx, ly = ax + bx * z, ay + by * z
        I0 = hi - lo
        I1 = 0.5 * (hi**2 - lo**2)
        I2 = (hi**3 - lo**3) / 3.0

        if (lx < 0.0 and ly < 0.0) or (lx >= 0.0 and ly >= 0.0):
            for a, b, rN, rM, cA, cB in ((ax, bx, 0, 2, 0, 2), (ay, by, 1, 3, 1, 3)):
                N, M, D0, D1, D2 = scalar_integrals(a, b, lo, hi, panel)
                R[rN] += N; R[rM] += M
                J[rN, cA] += D0; J[rN, cB] += D1
                J[rM, cA] += D1; J[rM, cB] += D2
            continue

        x_tension = lx >= 0.0
        if x_tension:
            at, bt, ac, bc = ax, bx, ay, by
            tN, tM, tA, tB = 0, 2, 0, 2
            cN, cM, cA, cB = 1, 3, 1, 3
            lt, lc = lx, ly
        else:
            at, bt, ac, bc = ay, by, ax, bx
            tN, tM, tA, tB = 1, 3, 1, 3
            cN, cM, cA, cB = 0, 2, 0, 2
            lt, lc = ly, lx

        Nc, Mc, D0c, D1c, D2c = scalar_integrals(ac, bc, lo, hi, panel)
        A0, Bcoup, Ct, _, ga = tc_linear_form(lt, lc, panel)
        if ga:
            raise RuntimeError("gamma-active TC interval reached before exact gamma primitive is installed")

        Nlt = at * I0 + bt * I1
        Mlt = at * I1 + bt * I2
        Nt = A0 * I0 + Bcoup * Nc + Ct * Nlt
        Mt = A0 * I1 + Bcoup * Mc + Ct * Mlt
        R[cN] += Nc; R[cM] += Mc; R[tN] += Nt; R[tM] += Mt
        J[cN, cA] += D0c; J[cN, cB] += D1c
        J[cM, cA] += D1c; J[cM, cB] += D2c
        J[tN, tA] += Ct * I0; J[tN, tB] += Ct * I1
        J[tM, tA] += Ct * I1; J[tM, tB] += Ct * I2
        J[tN, cA] += Bcoup * D0c; J[tN, cB] += Bcoup * D1c
        J[tM, cA] += Bcoup * D1c; J[tM, cB] += Bcoup * D2c

    for arx, ary, z in zip(st["ax"], st["ay"], st["z"]):
        lx, ly = ax + bx * z, ay + by * z
        sx, sy, T, ga = point_map(lx, ly, panel)
        if ga:
            raise RuntimeError("gamma-active reinforcement point reached before exact gamma primitive is installed")
        ex = panel["eps0"] * (lx - NU * ly)
        ey = panel["eps0"] * (ly - NU * lx)
        tx, ty = ES * ex, ES * ey
        ssx, ssy = float(np.clip(tx, -FY, FY)), float(np.clip(ty, -FY, FY))
        Dsteel_x = ES if abs(tx) < FY else 0.0
        if lower_y_bar_tangent is not None and abs(z + 12.63) < 1.0e-9:
            Dsteel_y = float(lower_y_bar_tangent)
        else:
            Dsteel_y = ES if abs(ty) < FY else 0.0
        atot = arx + ary
        Rx, Ry = -atot * sx + arx * ssx, -atot * sy + ary * ssy
        R += np.array([Rx, Ry, z * Rx, z * Ry])
        dlx = np.array([1.0, 0.0, z, 0.0]); dly = np.array([0.0, 1.0, 0.0, z])
        dsx = T[0, 0] * dlx + T[0, 1] * dly
        dsy = T[1, 0] * dlx + T[1, 1] * dly
        dex = panel["eps0"] * (dlx - NU * dly)
        dey = panel["eps0"] * (dly - NU * dlx)
        dRx = -atot * dsx + arx * Dsteel_x * dex
        dRy = -atot * dsy + ary * Dsteel_y * dey
        J[0] += dRx; J[1] += dRy; J[2] += z * dRx; J[3] += z * dRy
    return R, J


def demand4(op: dict, q: float, u: float) -> np.ndarray:
    r = base.resultants(op, q, 1.0, u)
    return np.array([r["Nx"], r["Ny"], r["Mx"], r["My"]], float)


def fold_system(X: np.ndarray, op: dict, u: float) -> np.ndarray:
    v, q = X[:4], float(X[4])
    sec, J = section_resultant_and_jac(v, op["panel"], op["st"])
    res = (sec - demand4(op, q, u)) / np.array([100.0, 600.0, 600.0, 600.0])
    row = np.linalg.norm(J, axis=1); row[row == 0.0] = 1.0
    Jn = J / row[:, None]
    col = np.linalg.norm(Jn, axis=0); col[col == 0.0] = 1.0
    Jn /= col
    return np.r_[res, np.linalg.det(Jn)]


def panel14_yield_system(X: np.ndarray, op: dict, u: float) -> np.ndarray:
    v, q = X[:4], float(X[4])
    sec, _ = section_resultant_and_jac(v, op["panel"], op["st"])
    res = (sec - demand4(op, q, u)) / np.array([100.0, 600.0, 600.0, 600.0])
    z = -12.63
    lx, ly = v[0] + v[2] * z, v[1] + v[3] * z
    ey = op["panel"]["eps0"] * (ly - NU * lx)
    return np.r_[res, (ES * ey + FY) / FY]


SEED = {
    1: np.array([0.0520240, -0.5175504, 0.0141352, 0.00585784, 0.00152806]),
    14: np.array([-0.0155567, -1.1802128, 0.00419654, 0.01973398, 0.000934579]),
    21: np.array([0.0857082, -0.1805669, -0.0245850, -0.0133694, 0.00158511]),
}


def event_at_u(case: int, u: float, seed: np.ndarray) -> np.ndarray:
    op = base.build_wave_operator(base.PANELS[case], base.PHI_COEFF[case])
    fun = (lambda X: panel14_yield_system(X, op, u)) if case == 14 else (lambda X: fold_system(X, op, u))
    sol = root(fun, seed)
    if (not sol.success) or np.linalg.norm(fun(sol.x)) > 1.0e-6:
        raise RuntimeError(f"event root failed for panel {case} at u={u}")
    return sol.x


def stationary_event(case: int) -> tuple[float, np.ndarray]:
    seed = SEED[case]
    def dqdu(u: float) -> float:
        h = 2.0e-5
        qm = event_at_u(case, u - h, seed)[4]
        qp = event_at_u(case, u + h, seed)[4]
        return (qp - qm) / (2.0 * h)
    bracket = {1: (0.60, 0.67), 14: (0.72, 0.79), 21: (0.33, 0.38)}[case]
    u = root_scalar(dqdu, bracket=bracket, xtol=1.0e-11).root
    return u, event_at_u(case, u, seed)


def main():
    print("EXPLICIT_STRUCTURAL_PATH_CHANGED = FALSE")
    print("FORMAL_SPATIAL_QUADRATURE = 0")
    print("FORMAL_MATERIAL_POINTS = 0")
    print("Pf_IN_ROOT_SELECTION = 0")
    print("NC_M6_ALPHA2 =", ALPHA2)
    for case in (1, 14, 21):
        panel = base.PANELS[case]
        op = base.build_wave_operator(panel, base.PHI_COEFF[case])
        u, X = stationary_event(case)
        v, q = X[:4], X[4]
        r = base.resultants(op, q, 1.0, u)
        PkN = r["P"] / 1000.0
        _, J = section_resultant_and_jac(v, panel, op["st"])
        h = panel["t"] / 2.0
        lam_x = (v[0] - v[2] * h, v[0] + v[2] * h)
        lam_y = (v[1] - v[3] * h, v[1] + v[3] * h)
        err = 100.0 * (PkN / panel["Pf"] - 1.0)
        print("\nPANEL", case)
        print("u =", u, "q =", q, "P_event_kN =", PkN)
        print("event =", "Y_REBAR_ACTIVE_SET_TERMINAL" if case == 14 else "CURRENT_MAP_SECTION_FOLD")
        print("lambda_x_faces =", lam_x, "lambda_y_faces =", lam_y)
        print("same_law_singular_values =", np.linalg.svd(J, compute_uv=False))
        print("post_solution_Pf_kN =", panel["Pf"], "post_solution_error_pct =", err)


if __name__ == "__main__":
    main()
