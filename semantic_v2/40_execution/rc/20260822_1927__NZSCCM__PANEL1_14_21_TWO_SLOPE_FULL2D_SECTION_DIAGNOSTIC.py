from __future__ import annotations

"""Two-independent-slope full-2D section diagnostic for Swartz Panels 1/14/21.

This script keeps the frozen source-waveform structural operator and the current
NC scalar/Foster-Saenz material functions unchanged.  The only theory-interface
change is

    lambda_x(z) = a_x + b_x z
    lambda_y(z) = a_y + b_y z

so that Nx, Ny, Mx and My are all matched simultaneously.

No spatial quadrature is used.  Concrete force/moment resultants are evaluated
from exact finite branch primitives.  The section Jacobian is the exact same-law
derivative, using endpoint identities for an affine material coordinate.

The experimental failure load is read only after each theoretical event is fixed.
It never enters waveform coefficients, root selection or any material parameter.
"""

from pathlib import Path
import importlib.util
import math
import numpy as np
from scipy.optimize import root, root_scalar

# Reuse the already-frozen source-waveform structural front end verbatim.
BASE_PATH = Path(__file__).with_name(
    "20260822_1751__NZSCCM__PANEL1_14_21_SOURCE_WAVEFORM_EXPLICIT_DIAGNOSTIC.py"
)
spec = importlib.util.spec_from_file_location("sourcewave1751", BASE_PATH)
base = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(base)

NU = base.NU
ES = base.ES
FY = base.FY
SOFTEN_ONSET = 10.0 / 17.0


def branch_limits(panel: dict) -> list[float]:
    ft = 0.1 * panel["fc"]
    xcr = ft / (panel["E0"] * panel["eps0"])
    return [-10.0, -1.0, 0.0, xcr, 10.0 * xcr]


def branch_id(lam: float, panel: dict) -> str:
    ft = 0.1 * panel["fc"]
    xcr = ft / (panel["E0"] * panel["eps0"])
    if lam < -10.0:
        return "C_RESIDUAL"
    if lam < -1.0:
        return "C_POSTPEAK"
    if lam < 0.0:
        return "C_SAENZ"
    if lam <= xcr:
        return "T_ELASTIC"
    if lam < 10.0 * xcr:
        return "T_FOSTER_SOFTEN"
    return "T_RESIDUAL"


def saenz_i0(lam: float, kappa: float) -> float:
    a = kappa - 2.0
    h2 = 1.0 - 0.25 * a * a
    x = lam - 0.5 * a
    if h2 > 1.0e-14:
        h = math.sqrt(h2)
        return math.atan(x / h) / h
    if h2 < -1.0e-14:
        h = math.sqrt(-h2)
        return 0.5 / h * math.log(abs((x - h) / (x + h)))
    return -1.0 / x


def scalar_stress_tangent(lam: float, panel: dict) -> tuple[float, float]:
    fc, E0, eps0 = panel["fc"], panel["E0"], panel["eps0"]
    ft = 0.1 * fc
    K = E0 * eps0
    xcr = ft / K
    if lam < -10.0:
        return -0.1 * fc, 0.0
    if lam < -1.0:
        return fc * (-0.1 * lam - 1.1), -0.1 * fc
    if lam < 0.0:
        kap = K / fc
        aa = kap - 2.0
        den = lam * lam - aa * lam + 1.0
        sig = K * lam / den
        ds = K * (1.0 - lam * lam) / (den * den)
        return sig, ds
    if lam <= xcr:
        return K * lam, K
    if lam < 10.0 * xcr:
        aa = 1.0 + 0.7 / 9.0
        bb = 0.7 / (9.0 * xcr)
        return ft * (aa - bb * lam), -ft * bb
    return 0.3 * ft, 0.0


def primitive_pair(lam: float, panel: dict, branch: str) -> tuple[float, float]:
    """Return local primitives S0'=sigma and S1'=lambda*sigma."""
    fc, E0, eps0 = panel["fc"], panel["E0"], panel["eps0"]
    ft = 0.1 * fc
    K = E0 * eps0
    xcr = ft / K
    if branch == "C_RESIDUAL":
        s = -0.1 * fc
        return s * lam, 0.5 * s * lam * lam
    if branch == "C_POSTPEAK":
        return (
            fc * (-0.05 * lam**2 - 1.1 * lam),
            fc * (-lam**3 / 30.0 - 0.55 * lam**2),
        )
    if branch == "C_SAENZ":
        kap = K / fc
        aa = kap - 2.0
        den = lam * lam - aa * lam + 1.0
        I = saenz_i0(lam, kap)
        J = 0.5 * math.log(den) + 0.5 * aa * I
        return K * J, K * (lam + aa * J - I)
    if branch == "T_ELASTIC":
        return 0.5 * K * lam**2, K * lam**3 / 3.0
    if branch == "T_FOSTER_SOFTEN":
        aa = 1.0 + 0.7 / 9.0
        bb = 0.7 / (9.0 * xcr)
        return (
            ft * (aa * lam - 0.5 * bb * lam**2),
            ft * (0.5 * aa * lam**2 - bb * lam**3 / 3.0),
        )
    s = 0.3 * ft
    return s * lam, 0.5 * s * lam**2


def affine_force_moment(a: float, b: float, z0: float, z1: float, panel: dict) -> tuple[float, float]:
    """Exact integral of sigma(a+bz) and z*sigma(a+bz)."""
    if abs(b) < 1.0e-14:
        sig, _ = scalar_stress_tangent(a, panel)
        return sig * (z1 - z0), 0.5 * sig * (z1**2 - z0**2)
    cuts = [z0, z1]
    for L in branch_limits(panel):
        z = (L - a) / b
        if z0 + 1.0e-12 < z < z1 - 1.0e-12:
            cuts.append(z)
    cuts.sort()
    N = M = 0.0
    for lo, hi in zip(cuts[:-1], cuts[1:]):
        br = branch_id(a + b * 0.5 * (lo + hi), panel)
        l0, l1 = a + b * lo, a + b * hi
        P00, P10 = primitive_pair(l0, panel, br)
        P01, P11 = primitive_pair(l1, panel, br)
        d0, d1 = P01 - P00, P11 - P10
        N += d0 / b
        M += (d1 - a * d0) / (b * b)
    return N, M


def concrete_block_jac(a: float, b: float, N: float, M: float, h: float, panel: dict):
    """Exact same-law derivatives for affine lambda.

    N_a = (sigma+ - sigma-)/b
    N_b = [h(sigma+ + sigma-) - N]/b
    M_a = N_b
    M_b = [h^2(sigma+ - sigma-) - 2M]/b
    """
    if abs(b) < 1.0e-12:
        _, D = scalar_stress_tangent(a, panel)
        return 2.0 * h * D, 0.0, 0.0, 2.0 * h**3 * D / 3.0
    sm, _ = scalar_stress_tangent(a - b * h, panel)
    sp, _ = scalar_stress_tangent(a + b * h, panel)
    Na = (sp - sm) / b
    Nb = (h * (sp + sm) - N) / b
    Ma = Nb
    Mb = (h * h * (sp - sm) - 2.0 * M) / b
    return Na, Nb, Ma, Mb


def section_resultant_and_jac(v: np.ndarray, panel: dict, st: dict, lower_y_bar_tangent=None):
    ax0, ay0, bx, by = map(float, v)
    h = panel["t"] / 2.0
    Nx, Mx = affine_force_moment(ax0, bx, -h, h, panel)
    Ny, My = affine_force_moment(ay0, by, -h, h, panel)
    J = np.zeros((4, 4), float)
    Na, Nb, Ma, Mb = concrete_block_jac(ax0, bx, Nx, Mx, h, panel)
    J[0, 0], J[0, 2], J[2, 0], J[2, 2] = Na, Nb, Ma, Mb
    Na, Nb, Ma, Mb = concrete_block_jac(ay0, by, Ny, My, h, panel)
    J[1, 1], J[1, 3], J[3, 1], J[3, 3] = Na, Nb, Ma, Mb

    for arx, ary, z in zip(st["ax"], st["ay"], st["z"]):
        lx, ly = ax0 + bx * z, ay0 + by * z
        sx, Dsx = scalar_stress_tangent(lx, panel)
        sy, Dsy = scalar_stress_tangent(ly, panel)
        ex = panel["eps0"] * (lx - NU * ly)
        ey = panel["eps0"] * (ly - NU * lx)
        tx, ty = ES * ex, ES * ey
        ssx, ssy = float(np.clip(tx, -FY, FY)), float(np.clip(ty, -FY, FY))
        Dsteel_x = ES if abs(tx) < FY else 0.0
        if lower_y_bar_tangent is not None and abs(z + 12.63) < 1.0e-9:
            Dsteel_y = float(lower_y_bar_tangent)
        else:
            Dsteel_y = ES if abs(ty) < FY else 0.0
        at = arx + ary
        Rx, Ry = -at * sx + arx * ssx, -at * sy + ary * ssy
        Nx, Ny, Mx, My = Nx + Rx, Ny + Ry, Mx + Rx * z, My + Ry * z
        dlx = np.array([1.0, 0.0, z, 0.0])
        dly = np.array([0.0, 1.0, 0.0, z])
        dex = panel["eps0"] * (dlx - NU * dly)
        dey = panel["eps0"] * (dly - NU * dlx)
        dRx = -at * Dsx * dlx + arx * Dsteel_x * dex
        dRy = -at * Dsy * dly + ary * Dsteel_y * dey
        J[0] += dRx
        J[1] += dRy
        J[2] += z * dRx
        J[3] += z * dRy
    return np.array([Nx, Ny, Mx, My]), J


def demand4(op: dict, q: float, u: float) -> np.ndarray:
    r = base.resultants(op, q, 1.0, u)
    return np.array([r["Nx"], r["Ny"], r["Mx"], r["My"]], float)


def fold_system(X: np.ndarray, op: dict, u: float) -> np.ndarray:
    v, q = X[:4], float(X[4])
    sec, J = section_resultant_and_jac(v, op["panel"], op["st"])
    res = (sec - demand4(op, q, u)) / np.array([100.0, 600.0, 600.0, 600.0])
    row = np.linalg.norm(J, axis=1)
    row[row == 0.0] = 1.0
    Jn = J / row[:, None]
    col = np.linalg.norm(Jn, axis=0)
    col[col == 0.0] = 1.0
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


# Seeds are calculation seeds only, not fitted parameters and contain no Pf.
SEED = {
    1: np.array([0.0520240, -0.5175504, 0.0141352, 0.00585784, 0.00152806]),
    14: np.array([-0.0155567, -1.1802128, 0.00419654, 0.01973398, 0.000934579]),
    21: np.array([0.0857082, -0.1805669, -0.0245850, -0.0133694, 0.00158511]),
}
U0 = {1: 0.6378326, 14: 0.7455824, 21: 0.3572658}


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
    bracket = {1: (0.62, 0.66), 14: (0.73, 0.78), 21: (0.34, 0.375)}[case]
    u = root_scalar(dqdu, bracket=bracket, xtol=1.0e-11).root
    return u, event_at_u(case, u, seed)


def tc_source_util_at_crack_front(v: np.ndarray, panel: dict):
    ft = 0.1 * panel["fc"]
    xcr = ft / (panel["E0"] * panel["eps0"])
    z = (xcr - v[0]) / v[2]
    lx, ly = v[0] + v[2] * z, v[1] + v[3] * z
    sx, _ = scalar_stress_tangent(lx, panel)
    sy, _ = scalar_stress_tangent(ly, panel)
    t, p = max(sx, sy), max(-sx, -sy)
    phiA = p / panel["fc"] + t / (3.0 * ft)
    phiB = p / (2.0 * panel["fc"]) + t / ft
    return z, max(phiA, phiB), phiA, phiB


def main() -> None:
    for case in (1, 14, 21):
        panel = base.PANELS[case]
        op = base.build_wave_operator(panel, base.PHI_COEFF[case])
        u, X = stationary_event(case)
        v, q = X[:4], X[4]
        r = base.resultants(op, q, 1.0, u)
        PkN = r["P"] / 1000.0
        err = 100.0 * (PkN / panel["Pf"] - 1.0)
        h = panel["t"] / 2.0
        lam_x = (v[0] - v[2] * h, v[0] + v[2] * h)
        lam_y = (v[1] - v[3] * h, v[1] + v[3] * h)
        max_positive = max(0.0, *lam_x, *lam_y)
        zcr, tcutil, phiA, phiB = tc_source_util_at_crack_front(v, panel)
        sec, J = section_resultant_and_jac(v, panel, op["st"])
        sv = np.linalg.svd(J, compute_uv=False)
        _, _, Vh = np.linalg.svd(J)
        null = Vh[-1] / np.max(np.abs(Vh[-1]))
        print(f"\nPANEL {case}")
        print("u =", u, "q =", q, "P_event_kN =", PkN, "Pf_kN =", panel["Pf"], "error_pct =", err)
        print("event =", "Y_REBAR_ACTIVE_SET_TERMINAL" if case == 14 else "CURRENT_MAP_SECTION_FOLD")
        print("lambda_x_faces =", lam_x, "lambda_y_faces =", lam_y)
        print("max_positive_lambda =", max_positive, "softening_onset =", SOFTEN_ONSET)
        print("TC_source_util_at_lambda_x_crack_front =", tcutil, "z =", zcr, "PhiA =", phiA, "PhiB =", phiB)
        print("singular_values =", sv, "null_vector =", null)
        print("demand =", {k: r[k] for k in ("Nx", "Ny", "Mx", "My")})

        if case == 14:
            # One-sided active-set audit at the lower y-rebar compression yield event.
            zbar = -12.63
            dq = 1.0e-8
            dd = (demand4(op, q + dq, u) - demand4(op, q - dq, u)) / (2.0 * dq)
            grad_h = -ES * panel["eps0"] * (
                np.array([0.0, 1.0, 0.0, zbar]) - NU * np.array([1.0, 0.0, zbar, 0.0])
            )
            for label, tangent in (("elastic_side", ES), ("capped_side", 0.0)):
                _, JJ = section_resultant_and_jac(v, panel, op["st"], lower_y_bar_tangent=tangent)
                dv_dq = np.linalg.solve(JJ, dd)
                print(label, "dh_dq =", float(grad_h @ dv_dq))

        if not (max_positive < SOFTEN_ONSET):
            raise RuntimeError("TC-R2 gamma softening became active; this compact branch script is no longer sufficient")


if __name__ == "__main__":
    main()
