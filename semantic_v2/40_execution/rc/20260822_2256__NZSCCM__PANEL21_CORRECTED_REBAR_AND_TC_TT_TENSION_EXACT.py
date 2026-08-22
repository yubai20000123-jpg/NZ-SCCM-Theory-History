from __future__ import annotations

"""Panel21 source-input correction and continuous TC/TT tension audit.

This is a thin reproduction driver over the frozen 20260822_2130 NC-M6 exact
source-wave implementation.  It deliberately does NOT replace the explicit
structural path.

Changes relative to the 2130 script:
1. Nguyen Table 5.1 `p` is nominal TOTAL steel ratio, so the two orthogonal
   reinforcement directions each receive p/2 before layer splitting.
2. For the authorized postcrack-tension diagnostic, one alpha2 value is used in
   both the scalar TT tension branch and the NC-M6 TC tension branch.  This removes
   a TC->TT postcrack stress mismatch while retaining the same finite Foster grammar.

No formal spatial/thickness quadrature and no Pf-based root or parameter selection
are introduced.  The NC-M6 crack front, CC branch, Vecchio-Collins gamma law,
waveform, P_phi(q), and (a_x,a_y,b_x,b_y) section kinematics remain unchanged.
"""

from pathlib import Path
import importlib.util
import math
import numpy as np

M6_PATH = Path(__file__).with_name(
    "20260822_2130__NZSCCM__NC_M6_2D_TC_CRACK_FRONT_EXACT_SECTION.py"
)
spec = importlib.util.spec_from_file_location("m6_2130_corrected_driver", M6_PATH)
m6 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(m6)

base = m6.base
old = m6.old
NU, ES = m6.NU, m6.ES
CASE = 21
DB = 2.7  # mm, Swartz No.12 gage wire source used in the prior bond audit


# -----------------------------------------------------------------------------
# 1. SOURCE-CORRECT REINFORCEMENT MAPPING
# -----------------------------------------------------------------------------

def corrected_rc_stiffness(panel: dict) -> dict:
    """Same base stiffness formula; only p interpretation is corrected.

    Nguyen Table 5.1: p = nominal total steel ratio.
    Isotropic x/y mesh => rho_direction = p/2, then divide among layers.
    """
    t, E0, p_total = panel["t"], panel["E0"], panel["p"]
    z = panel["z"]
    n_layers = len(z)
    rho_direction = 0.5 * p_total
    ax = [rho_direction * t / n_layers] * n_layers
    ay = [rho_direction * t / n_layers] * n_layers

    Q = E0 / (1.0 - NU**2)
    Q12 = NU * E0 / (1.0 - NU**2)
    Q66 = E0 / (2.0 * (1.0 + NU))
    t_conc = t - sum(np.asarray(ax) + np.asarray(ay))

    A11 = Q * t_conc + ES * sum(ax)
    A22 = Q * t_conc + ES * sum(ay)
    A12 = Q12 * t_conc
    A66 = Q66 * t_conc

    Ieff = t**3 / 12.0 - sum((ax[i] + ay[i]) * z[i] ** 2 for i in range(n_layers))
    Dx = Q * Ieff + ES * sum(ax[i] * z[i] ** 2 for i in range(n_layers))
    Dy = Q * Ieff + ES * sum(ay[i] * z[i] ** 2 for i in range(n_layers))
    Dmu = Q12 * Ieff
    D66 = Q66 * Ieff
    H = Dmu + 2.0 * D66
    return locals()


# build_wave_operator resolves rc_stiffness dynamically from its source module.
base.rc_stiffness = corrected_rc_stiffness


# -----------------------------------------------------------------------------
# 2. ONE ALPHA2 ACROSS TC AND TT, WITH THE SAME EXACT SCALAR PRIMITIVES
# -----------------------------------------------------------------------------

def scalar_stress_tangent_common(lam: float, panel: dict) -> tuple[float, float]:
    fc, E0, eps0 = panel["fc"], panel["E0"], panel["eps0"]
    ft = 0.1 * fc
    K = E0 * eps0
    xcr = ft / K
    alpha2 = m6.ALPHA2

    if lam < -10.0:
        return -0.1 * fc, 0.0
    if lam < -1.0:
        return fc * (-0.1 * lam - 1.1), -0.1 * fc
    if lam < 0.0:
        kap = K / fc
        aa = kap - 2.0
        den = lam * lam - aa * lam + 1.0
        return K * lam / den, K * (1.0 - lam * lam) / (den * den)
    if lam <= xcr:
        return K * lam, K
    if lam < m6.ALPHA1 * xcr:
        d = (1.0 - alpha2) / (m6.ALPHA1 - 1.0)
        return ft * ((1.0 + d) - d * lam / xcr), -ft * d / xcr
    return alpha2 * ft, 0.0


def primitive_pair_common(lam: float, panel: dict, branch: str) -> tuple[float, float]:
    fc, E0, eps0 = panel["fc"], panel["E0"], panel["eps0"]
    ft = 0.1 * fc
    K = E0 * eps0
    xcr = ft / K
    alpha2 = m6.ALPHA2

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
        I = old.saenz_i0(lam, kap)
        J = 0.5 * math.log(den) + 0.5 * aa * I
        return K * J, K * (lam + aa * J - I)
    if branch == "T_ELASTIC":
        return 0.5 * K * lam**2, K * lam**3 / 3.0
    if branch == "T_FOSTER_SOFTEN":
        d = (1.0 - alpha2) / (m6.ALPHA1 - 1.0)
        aa = 1.0 + d
        bb = d / xcr
        return (
            ft * (aa * lam - 0.5 * bb * lam**2),
            ft * (0.5 * aa * lam**2 - bb * lam**3 / 3.0),
        )
    s = alpha2 * ft
    return s * lam, 0.5 * s * lam**2


# old.affine_force_moment and all M6 exact derivative identities call these
# module globals at evaluation time; patching them retains the same finite exact
# primitive architecture while making TT and TC use the same alpha2.
old.scalar_stress_tangent = scalar_stress_tangent_common
old.primitive_pair = primitive_pair_common


# -----------------------------------------------------------------------------
# 3. EVENT HELPERS
# -----------------------------------------------------------------------------

def panel21_bond_target(modified: bool) -> tuple[float, float, float]:
    panel = base.PANELS[CASE]
    rho_direction = 0.5 * panel["p"]
    m = DB / (4.0 * rho_direction)
    td = 0.6 if modified else 1.0
    ct = 3.6 * td * m
    epscr0 = 0.1 * panel["fc"] / panel["E0"]
    alpha2 = 1.0 / (1.0 + math.sqrt(ct * m6.ALPHA1 * epscr0))
    return alpha2, m, ct


def stationary(case: int, alpha2: float, seed: np.ndarray) -> tuple[float, np.ndarray]:
    m6.ALPHA2 = float(alpha2)
    m6.SEED[case] = np.asarray(seed, float)
    return m6.stationary_event(case)


def event_record(alpha2: float, seed: np.ndarray) -> dict:
    panel = base.PANELS[CASE]
    op = base.build_wave_operator(panel, base.PHI_COEFF[CASE])
    u, X = stationary(CASE, alpha2, seed)
    v, q = X[:4], float(X[4])
    r = base.resultants(op, q, 1.0, u)
    R, J = m6.section_resultant_and_jac(v, panel, op["st"])
    _, _, Vh = np.linalg.svd(J)
    null = Vh[-1] / np.max(np.abs(Vh[-1]))

    h = panel["t"] / 2.0
    faces = []
    for z in (-h, +h):
        faces.append((z, v[0] + v[2] * z, v[1] + v[3] * z))

    lx0, ly0 = v[0], v[1]
    ex0 = panel["eps0"] * (lx0 - NU * ly0)
    ey0 = panel["eps0"] * (ly0 - NU * lx0)
    steel = (ES * ex0, ES * ey0)

    return {
        "alpha2": alpha2,
        "u": u,
        "q": q,
        "P_kN": r["P"] / 1000.0,
        "v": v,
        "singular_null": null,
        "faces": faces,
        "midplane_steel_MPa": steel,
        "rho_direction": 0.5 * panel["p"],
        "section_residual_norm": float(np.linalg.norm(R - m6.demand4(op, q, u))),
    }


def main() -> None:
    print("EXPLICIT_STRUCTURAL_PATH_CHANGED = FALSE")
    print("FORMAL_SPATIAL_QUADRATURE = 0")
    print("FORMAL_MATERIAL_POINTS = 0")
    print("Pf_IN_ROOT_SELECTION = 0")
    print("PANEL21_FULL_LENGTH_mm =", base.A)
    print("PANEL21_WIDTH_mm =", base.B)
    print("PANEL21_NOMINAL_HALFWAVE_mm =", base.A / 2.0)
    print("PANEL21_RHO_DIRECTION =", 0.5 * base.PANELS[CASE]["p"])

    # Corrected baseline NC-M6/F03.
    f03 = event_record(
        0.3,
        np.array([0.0497, -0.16734, -0.01615, -0.01116, 0.0013476]),
    )
    print("\nM6_F03_CORRECTED", f03)

    # Same bond-dependent alpha2 across TC and TT.
    for label, modified, seed in (
        ("B99_3P6M", False, np.array([0.08610, -0.17462, -0.02283, -0.01198, 0.0014349])),
        ("B03_TD0P6", True, np.array([0.10881, -0.17731, -0.02671, -0.01230, 0.0014688])),
    ):
        alpha2, m, ct = panel21_bond_target(modified)
        rec = event_record(alpha2, seed)
        print("\nVARIANT", label, "m_mm", m, "ct_mm", ct)
        print(rec)


if __name__ == "__main__":
    main()
