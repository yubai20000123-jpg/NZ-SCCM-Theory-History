"""NZ-SCCM M1R source-shaped rational primitive screen R01.

Purpose
-------
Material-space architecture/regression screen only.  This script does NOT use
Case21 Pu, Swartz24, spatial quadrature, element integration or material points.
It treats the frozen Nguyen/Foster ordinary-concrete current operator as a
strong nonlinear MATERIAL oracle and tests a source-shaped 1D rational compiler.

Formal status
-------------
M1R_R01_FROZEN_NC_ORACLE_REGRESSION = PASS_SCREEN
FINAL_NC_SOURCE_CALIBRATION = NOT_YET_DONE
FINAL_GATE_B = NOT_YET_FROZEN
M1R_R01_S_INNER_INTEGRATION = PASS_CLASS_A
M1R_R01_OUTER_XY = CLASS_B_CANDIDATE / NOT_YET_CLOSED
"""
from __future__ import annotations

import math
import numpy as np

# Frozen NC benchmark/oracle parameters.
FC = 21.23
E0 = 20321.0
EPS0 = 0.00209
NU = 0.18
RHO = 0.1
KAPPA = E0 * EPS0 / FC
XCR = RHO / KAPPA
ETA = XCR / 20.0
ETA_R = 0.05
MT = -7.0 / 90.0
ACC = 0.1072329249362415
AT = 1.0 - 2.0 ** (-1.0 / 8.0)

EMIN, EMAX = -2.0, 0.6
LAM_MIN = EMIN / (1.0 - NU)
LAM_MAX = EMAX / (1.0 - NU)
LAM_C = 0.5 * (LAM_MIN + LAM_MAX)
LAM_S = 0.5 * (LAM_MAX - LAM_MIN)

# R01 fixed rational coefficients.
# U: [n1,n2,n3,d1,d2,d3,d4], with exact origin slope KAPPA.
U_COEF = np.array([
    -9.786990860138413,
    20.2150042396063,
    -10.648551770753837,
    -2.1990006614651056,
    27.740854104357723,
    21.454401259317827,
    32.84751931776155,
])

# Generic zero-rational arrays are [n0..nm,d1..dd].
C_COEF = np.array([
    -0.9442135131854792,
    8.475283733893267,
    -19.155032651471718,
    11.717171611700422,
    2.502734679618874,
    36.42244419918754,
    31.105995105744704,
    36.19639777683384,
])

C2_COEF = np.array([
    -0.22001900119107273,
    1.235734615177478,
    -1.4750318560416769,
    0.02930272701903502,
    2.4695146543890787,
    6.3090038864234,
    4.550686012252086,
    2.6723789248563734,
])

T_COEF = np.array([
    5.2832456515727308e+00,
    5.9036380076624050e+02,
    1.6827160529299152e+04,
    3.4424484696375992e+05,
    2.3654301901438353e+06,
    -5.3855760768061061e+05,
    -1.9558929506678067e+07,
    4.6747916139120964e+05,
    3.6048668340100557e+07,
    1.6064437897170084e+07,
    -1.4488932046500764e+02,
    1.5542658904204591e+04,
    -5.2992374395863095e+05,
    9.7304263129297085e+06,
    -8.4085213382741570e+07,
    4.6193321040738773e+08,
    -1.4278058956538005e+09,
    2.5022789964268451e+09,
    -2.4676258484463243e+09,
    1.1691624735294776e+09,
])

V_COEF = np.array([
    -2.6397090716844929e+00,
    8.5521709459697178e+01,
    4.7435950866466396e+02,
    -7.6967479847511470e+02,
    -7.2653855232676938e+02,
    -4.5562216690418325e+01,
    9.5670115797598226e+02,
    -1.0491501141642168e+04,
    6.6993892415682218e+04,
    -3.1190274492658256e+04,
])


def Pi_eta(z):
    return z * z * (np.sqrt(z * z + ETA * ETA) + z) / (2.0 * (z * z + ETA * ETA))


def H(r, r0):
    return (
        0.5 * ((r - r0) + np.sqrt((r - r0) ** 2 + ETA_R ** 2))
        - 0.5 * ((-r0) + math.sqrt(r0 ** 2 + ETA_R ** 2))
    )


def exact_primitives(lam):
    """Frozen benchmark scalar primitives U,C,C^2,T,T^8."""
    c = Pi_eta(-lam)
    t = Pi_eta(lam)
    C = KAPPA * c / (1.0 + (KAPPA - 2.0) * c + c * c)
    r = t / XCR
    T = r + (MT - 1.0) * H(r, 1.0) - MT * H(r, 10.0)
    U = KAPPA * lam - C + KAPPA * c + RHO * T - KAPPA * t
    return U, C, C * C, T, T ** 8


def rational_zero(lam, coef, m, d):
    """lambda*(n0+...+nm lambda^m)/(1+d1 lambda+...+dd lambda^d)."""
    num_coef = coef[: m + 1]
    den_coef = coef[m + 1 :]
    num = lam * sum(num_coef[k] * lam ** k for k in range(m + 1))
    den = 1.0 + sum(den_coef[k - 1] * lam ** k for k in range(1, d + 1))
    return num / den


def rational_U(lam):
    n1, n2, n3, d1, d2, d3, d4 = U_COEF
    num = lam * (KAPPA + n1 * lam + n2 * lam ** 2 + n3 * lam ** 3)
    den = 1.0 + d1 * lam + d2 * lam ** 2 + d3 * lam ** 3 + d4 * lam ** 4
    return num / den


def compiled_primitives(lam):
    return (
        rational_U(lam),
        rational_zero(lam, C_COEF, 3, 4),
        rational_zero(lam, C2_COEF, 3, 4),
        rational_zero(lam, T_COEF, 9, 10),
        rational_zero(lam, V_COEF, 4, 5),
    )


def equivalent_lambdas(e1, e2):
    den = 1.0 - NU ** 2
    return (e1 + NU * e2) / den, (NU * e1 + e2) / den


def source_shaped_response(p1, p2):
    U1, C1, C21, T1, V1 = p1
    U2, C2, C22, T2, V2 = p2
    s1 = U1 - ACC * C21 * C2 + C1 * T2 - RHO * AT * T1 * V2
    s2 = U2 - ACC * C22 * C1 + C2 * T1 - RHO * AT * T2 * V1
    return float(s1), float(s2)


def frozen_nc(e1, e2):
    l1, l2 = equivalent_lambdas(e1, e2)
    return source_shaped_response(exact_primitives(l1), exact_primitives(l2))


def m1r_nc(e1, e2):
    l1, l2 = equivalent_lambdas(e1, e2)
    return source_shaped_response(compiled_primitives(l1), compiled_primitives(l2))


def metrics(errors):
    a = np.asarray(errors, dtype=float)
    return {
        "mean": float(np.mean(a)),
        "p95": float(np.quantile(a, 0.95)),
        "max": float(np.max(a)),
    }


def full_domain_screen(n=101):
    grid = np.linspace(EMIN, EMAX, n)
    errors = []
    for e1 in grid:
        for e2 in grid:
            se = frozen_nc(e1, e2)
            sa = m1r_nc(e1, e2)
            errors.extend((abs(sa[0] - se[0]), abs(sa[1] - se[1])))
    return metrics(errors)


def path_screen(path, n=401):
    errors = []
    if path == "e2=0":
        for e1 in np.linspace(EMIN, EMAX, n):
            e2 = 0.0
            se, sa = frozen_nc(e1, e2), m1r_nc(e1, e2)
            errors.extend((abs(sa[0] - se[0]), abs(sa[1] - se[1])))
    elif path == "equal_CC":
        for e in np.linspace(-2.0, 0.0, n):
            se, sa = frozen_nc(e, e), m1r_nc(e, e)
            errors.extend((abs(sa[0] - se[0]), abs(sa[1] - se[1])))
    elif path == "equal_TT":
        for e in np.linspace(0.0, 0.6, n):
            se, sa = frozen_nc(e, e), m1r_nc(e, e)
            errors.extend((abs(sa[0] - se[0]), abs(sa[1] - se[1])))
    elif path == "TC_ratio":
        for t in np.linspace(0.0, 2.0, n):
            e1, e2 = -t, 0.25 * t
            se, sa = frozen_nc(e1, e2), m1r_nc(e1, e2)
            errors.extend((abs(sa[0] - se[0]), abs(sa[1] - se[1])))
    else:
        raise ValueError(path)
    return metrics(errors)


def denominator_roots():
    """Return scalar-denominator roots in lambda coordinates."""
    out = {}
    # np.roots expects descending powers.
    u_den = [U_COEF[6], U_COEF[5], U_COEF[4], U_COEF[3], 1.0]
    out["U"] = np.roots(u_den)
    for name, coef, m, d in (
        ("C", C_COEF, 3, 4),
        ("C2", C2_COEF, 3, 4),
        ("T", T_COEF, 9, 10),
        ("V", V_COEF, 4, 5),
    ):
        dc = coef[m + 1 :]
        out[name] = np.roots(list(dc[::-1]) + [1.0])
    return out


def poles_on_material_domain(tol=1e-9):
    bad = {}
    for name, roots in denominator_roots().items():
        real = [float(r.real) for r in roots if abs(r.imag) <= tol]
        bad[name] = [r for r in real if LAM_MIN <= r <= LAM_MAX]
    return bad


def symbolic_degree_audit():
    """Exact SymPy audit of denominator/structural-weight degrees in s."""
    import sympy as sp

    s = sp.symbols("s")
    p, q = sp.symbols("p q")
    a0, a1, a2 = sp.symbols("a0 a1 a2")
    I2 = a0 + a1 * s + a2 * s ** 2

    Delta2 = 1 + p*s + q*s**2 + (p**2 - 2*q)*I2 + p*q*s*I2 + q**2*I2**2
    Delta1 = 1 + p*s + p**2*I2

    # Generic Case21 post-transform structural degrees.
    x0, x1 = sp.symbols("x0 x1")
    r0, r1 = sp.symbols("r0 r1")
    i20, i21, i22 = sp.symbols("i20 i21 i22")
    Xyy = x0 + x1*s
    I1q = r0 + r1*s
    I2q = i20 + i21*s + i22*s**2
    Gq = sp.expand(s*I1q - I2q)

    return {
        "quadratic_scalar_factor_matrix_det_degree_s": sp.Poly(sp.expand(Delta2), s).degree(),
        "linear_scalar_factor_matrix_det_degree_s": sp.Poly(sp.expand(Delta1), s).degree(),
        "Xyy_degree_s": sp.Poly(Xyy, s).degree(),
        "I1q_degree_s": sp.Poly(I1q, s).degree(),
        "Gq_degree_s": sp.Poly(Gq, s).degree(),
    }


if __name__ == "__main__":
    print("M1R R01 material domain")
    print("e in", (EMIN, EMAX))
    print("lambda in", (LAM_MIN, LAM_MAX))
    print("free coefficients =", 7 + 8 + 8 + 20 + 10)

    print("\n101x101 frozen-NC oracle regression")
    print(full_domain_screen(101))

    print("\nrepresentative paths")
    for p in ("e2=0", "equal_CC", "equal_TT", "TC_ratio"):
        print(p, path_screen(p, 401))

    print("\npoles on diagnostic lambda interval")
    print(poles_on_material_domain())
    all_roots = denominator_roots()
    v_real = sorted(float(r.real) for r in all_roots["V"] if abs(r.imag) <= 1e-9)
    print("V real roots =", v_real)

    print("\nexact s-degree audit")
    print(symbolic_degree_audit())
