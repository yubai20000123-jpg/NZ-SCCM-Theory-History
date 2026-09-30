"""
UCFT nonlinear membrane condensation solver
Current stage: M2 semi-analytic active-set prototype

Theory identity:
- single-q global path
- A+=A-=0 in M2
- C0/C1 nonlinear membrane condensation
- exact UHPC thickness active-set integration
- exact Y active-set integration through finite Laurent-polynomial primitives
- only one outer X definite integral remains

IMPORTANT:
This is not the final nine-specimen solver.
It is the M2 kernel used to formally replace the temporary 2D Gauss verification.

Reference tensile law in M2 is pre-peak only:
ft = 7.2 MPa, eps_tp = 0.0002.
Stop the M2 path when any directional tensile strain reaches eps_tp.
"""

from __future__ import annotations
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import least_squares

# ---------------------------------------------------------------------
# Material constants
# ---------------------------------------------------------------------

EC = 43400.0
NUC = 0.20
TC = 42.0
FC = 141.1
EPS_C0 = 0.0035

ES = 206000.0
NUS = 0.30
TS = 4.0
ZS = 23.0

Q0 = 0.0025

FT = 7.2
EPS_TP = 0.0002

# compression-positive polynomial rewritten in tension-positive sign
_A = EC * EPS_C0 / FC
_B = 6.0 - 5.0 * _A
_C = 4.0 * _A - 5.0

COMP = np.zeros(7)
COMP[1] = EC
COMP[5] = FC * _B / EPS_C0**5
COMP[6] = -FC * _C / EPS_C0**6

# pre-peak tensile cubic Hermite:
# sigma(0)=0, sigma'(0)=EC, sigma(EPS_TP)=FT, sigma'(EPS_TP)=0
_RT = EC * EPS_TP / FT
TENS = np.zeros(4)
TENS[1] = EC
TENS[2] = FT * (3.0 - 2.0 * _RT) / EPS_TP**2
TENS[3] = FT * (_RT - 2.0) / EPS_TP**3

C11S = ES / (1.0 - NUS**2)
GS = ES / (2.0 * (1.0 + NUS))
GC = EC / (2.0 * (1.0 + NUC))

I2S = 2.0 * (TS * ZS**2 + TS**3 / 12.0)

A_SHEAR = GC * TC + 2.0 * TS * GS
D_SHEAR = GC * TC**3 / 12.0 + GS * I2S


# ---------------------------------------------------------------------
# Polynomial primitives
# ---------------------------------------------------------------------

def primitive_F(c: np.ndarray) -> np.ndarray:
    out = np.zeros(len(c) + 1)
    for k, a in enumerate(c):
        out[k + 1] = a / (k + 1)
    return out


def primitive_J(c: np.ndarray) -> np.ndarray:
    out = np.zeros(len(c) + 2)
    for k, a in enumerate(c):
        out[k + 2] = a / (k + 2)
    return out


F_COMP = primitive_F(COMP)
J_COMP = primitive_J(COMP)
F_TENS = primitive_F(TENS)
J_TENS = primitive_J(TENS)


def compose_poly(poly_e: np.ndarray, e_poly_s: np.ndarray) -> np.ndarray:
    """poly_e(e(s)); both coefficient arrays use ascending powers."""
    out = np.zeros(1)
    power = np.array([1.0])
    for k, ck in enumerate(poly_e):
        if k > 0:
            power = np.polynomial.polynomial.polymul(power, e_poly_s)
        if ck != 0.0:
            if len(out) < len(power):
                out = np.pad(out, (0, len(power) - len(out)))
            out[:len(power)] += ck * power
    return out


def arr_shift_dict(arr: np.ndarray, shift: int, scale: float = 1.0) -> dict[int, float]:
    return {
        i + shift: scale * float(v)
        for i, v in enumerate(arr)
        if abs(v) > 1.0e-18
    }


def mul_laurent_by_poly(d: dict[int, float], p: np.ndarray) -> dict[int, float]:
    out: dict[int, float] = {}
    for k, v in d.items():
        for j, a in enumerate(p):
            if a != 0.0:
                out[k + j] = out.get(k + j, 0.0) + v * float(a)
    return {k: v for k, v in out.items() if abs(v) > 1.0e-18}


# ---------------------------------------------------------------------
# Exact Y primitives: integral sin(Y)^p dY
# ---------------------------------------------------------------------

def I_sin_power_indef(p: int, y: float) -> float:
    if p == 0:
        return y
    if p == 1:
        return -math.cos(y)
    if p == -1:
        return math.log(math.tan(y / 2.0))
    if p == -2:
        return -1.0 / math.tan(y)
    if p >= 2:
        return (
            -(math.sin(y) ** (p - 1)) * math.cos(y) / p
            + (p - 1.0) / p * I_sin_power_indef(p - 2, y)
        )
    raise ValueError("Current active-set algebra should not require p < -2.")


def integrate_laurent(d: dict[int, float], ya: float, yb: float) -> float:
    val = 0.0
    for p, c in d.items():
        if ya < 1.0e-12 and p < 0:
            # Exact same-branch expressions cancel negative-power terms.
            if abs(c) < 1.0e-8:
                continue
            raise FloatingPointError(
                f"Unexpected non-removable sin(Y)^{p} term at Y=0: {c}"
            )
        val += c * (
            I_sin_power_indef(p, yb)
            - I_sin_power_indef(p, ya)
        )
    return val


# ---------------------------------------------------------------------
# Active-set roots in s = sin(Y)
# ---------------------------------------------------------------------

def roots_0_1(a2: float, a1: float, a0: float) -> list[float]:
    roots: list[float] = []
    if abs(a2) < 1.0e-14:
        if abs(a1) > 1.0e-14:
            s = -a0 / a1
            if 1.0e-12 < s < 1.0 - 1.0e-12:
                roots.append(float(s))
        return roots

    disc = a1 * a1 - 4.0 * a2 * a0
    if disc < -1.0e-12:
        return roots
    disc = max(disc, 0.0)

    for s in (
        (-a1 + math.sqrt(disc)) / (2.0 * a2),
        (-a1 - math.sqrt(disc)) / (2.0 * a2),
    ):
        if 1.0e-12 < s < 1.0 - 1.0e-12:
            roots.append(float(s))
    return roots


# ---------------------------------------------------------------------
# Exact UHPC thickness resultants represented as Laurent polynomials in s
# ---------------------------------------------------------------------

def section_laurent(
    a0: float,
    a2: float,
    D: float,
    thickness: float,
    case: str,
) -> tuple[dict[int, float], dict[int, float]]:
    """
    em = a0 + a2*s^2
    chi = D*s
    e_top    = em + chi*t/2
    e_bottom = em - chi*t/2

    case:
        T : whole thickness tension
        C : whole thickness compression
        X : bottom compression, top tension
    """
    em = np.array([a0, 0.0, a2])
    d1 = D * thickness / 2.0

    e_top = np.array([a0, d1, a2])
    e_bot = np.array([a0, -d1, a2])

    if case == "T":
        Ft = compose_poly(F_TENS, e_top)
        Fb = compose_poly(F_TENS, e_bot)
        Jt = compose_poly(J_TENS, e_top)
        Jb = compose_poly(J_TENS, e_bot)
    elif case == "C":
        Ft = compose_poly(F_COMP, e_top)
        Fb = compose_poly(F_COMP, e_bot)
        Jt = compose_poly(J_COMP, e_top)
        Jb = compose_poly(J_COMP, e_bot)
    elif case == "X":
        Ft = compose_poly(F_TENS, e_top)
        Fb = compose_poly(F_COMP, e_bot)
        Jt = compose_poly(J_TENS, e_top)
        Jb = compose_poly(J_COMP, e_bot)
    else:
        raise ValueError(case)

    nf = max(len(Ft), len(Fb))
    dF = np.zeros(nf)
    dF[:len(Ft)] += Ft
    dF[:len(Fb)] -= Fb

    N = arr_shift_dict(dF, -1, 1.0 / D)

    nj = max(len(Jt), len(Jb))
    dJ = np.zeros(nj)
    dJ[:len(Jt)] += Jt
    dJ[:len(Jb)] -= Jb

    em_dF = np.polynomial.polynomial.polymul(em, dF)
    nn = max(len(dJ), len(em_dF))
    num = np.zeros(nn)
    num[:len(dJ)] += dJ
    num[:len(em_dF)] -= em_dF

    M = arr_shift_dict(num, -2, 1.0 / (D * D))

    return N, M


def direction_Y_integrals(
    A0: float,
    Bcos: float,
    D: float,
    thickness: float,
) -> tuple[float, float, float]:
    """
    For fixed X:
      em = A0 + Bcos*cos(2Y)
      chi = D*sin(Y)

    Returns exact half-wave Y integrals:
      int N dY
      int N*cos(2Y) dY
      int M*sin(Y) dY
    over 0 <= Y <= pi/2.
    """
    if abs(D) < 1.0e-15:
        raise FloatingPointError(
            "Endpoint D->0 continuous limit should be handled by outer integrator; "
            "adaptive quadrature normally never samples X=0 exactly."
        )

    a0 = A0 + Bcos
    a2 = -2.0 * Bcos
    d1 = D * thickness / 2.0

    roots = [0.0, 1.0]
    roots += roots_0_1(a2, +d1, a0)  # e_top = 0
    roots += roots_0_1(a2, -d1, a0)  # e_bottom = 0
    roots = sorted(set(round(x, 14) for x in roots))

    int_N = 0.0
    int_N_cos2Y = 0.0
    int_M_sinY = 0.0

    for sa, sb in zip(roots[:-1], roots[1:]):
        sm = 0.5 * (sa + sb)
        e_top = a0 + a2 * sm * sm + d1 * sm
        e_bot = a0 + a2 * sm * sm - d1 * sm

        if e_bot >= 0.0 and e_top >= 0.0:
            case = "T"
        elif e_bot <= 0.0 and e_top <= 0.0:
            case = "C"
        else:
            case = "X"

        N, M = section_laurent(a0, a2, D, thickness, case)

        ya = math.asin(sa)
        yb = math.asin(sb)

        int_N += integrate_laurent(N, ya, yb)

        N_cos2Y = mul_laurent_by_poly(N, np.array([1.0, 0.0, -2.0]))
        int_N_cos2Y += integrate_laurent(N_cos2Y, ya, yb)

        M_sinY = mul_laurent_by_poly(M, np.array([0.0, 1.0]))
        int_M_sinY += integrate_laurent(M_sinY, ya, yb)

    return int_N, int_N_cos2Y, int_M_sinY


# ---------------------------------------------------------------------
# Outer X kernel and residual assembly
# ---------------------------------------------------------------------

def outer_X_components(
    X: float,
    state: np.ndarray,
    q: float,
    b: float,
    model: str,
) -> np.ndarray:
    """
    Returns vector-valued half-domain X integrand.
    model = "C0" or "C1".

    Current M2 assumes a_h = b and A+ = A- = 0.
    """
    a_h = b
    r = 1.0

    if model == "C0":
        Ex, Ey, Bx, By, P = state
        Hx = Hy = 0.0
    elif model == "C1":
        Ex, Ey, Bx, By, Hx, Hy, P = state
    else:
        raise ValueError(model)

    Q = q * q + 2.0 * Q0 * q
    Cq = math.pi**2 * Q / 8.0
    Cq_p = math.pi**2 * (q + Q0) / 4.0

    cx = math.cos(2.0 * X)
    sx = math.sin(X)
    s2x = math.sin(2.0 * X)

    Aex = Ex + Bx * cx
    Bex = -Cq + Hx * cx

    Aey = Ey - Cq * r * r * cx
    Bey = By + Hy * cx

    A0x = (Aex + NUC * Aey) / (1.0 - NUC**2)
    B0x = (Bex + NUC * Bey) / (1.0 - NUC**2)

    A0y = (Aey + NUC * Aex) / (1.0 - NUC**2)
    B0y = (Bey + NUC * Bex) / (1.0 - NUC**2)

    Dx = (
        math.pi**2 * q / b
        * (1.0 + NUC * r * r)
        / (1.0 - NUC**2)
        * sx
    )

    Dy = (
        math.pi**2 * q / b
        * (r * r + NUC)
        / (1.0 - NUC**2)
        * sx
    )

    INxU, INCxU, IMxUs = direction_Y_integrals(A0x, B0x, Dx, TC)
    INyU, INCyU, IMyUs = direction_Y_integrals(A0y, B0y, Dy, TC)

    # elastic top+bottom steel, exact Y integrals
    cNx0 = 2.0 * TS * C11S * (Aex + NUS * Aey)
    cNx2 = 2.0 * TS * C11S * (Bex + NUS * Bey)

    cNy0 = 2.0 * TS * C11S * (Aey + NUS * Aex)
    cNy2 = 2.0 * TS * C11S * (Bey + NUS * Bex)

    INxS = cNx0 * math.pi / 2.0
    INCxS = cNx2 * math.pi / 4.0

    INyS = cNy0 * math.pi / 2.0
    INCyS = cNy2 * math.pi / 4.0

    mx_coef = (
        C11S * I2S
        * (math.pi**2 * q / b)
        * (1.0 + NUS * r * r)
        * sx
    )

    my_coef = (
        C11S * I2S
        * (math.pi**2 * q / b)
        * (r * r + NUS)
        * sx
    )

    IMxSs = mx_coef * math.pi / 4.0
    IMySs = my_coef * math.pi / 4.0

    INx = INxU + INxS
    INCx = INCxU + INCxS
    INy = INyU + INyS
    INCy = INCyU + INCyS

    IMxs = IMxUs + IMxSs
    IMys = IMyUs + IMySs

    H_amp = r * Hx + (1.0 / r) * Hy

    shear_common = (
        A_SHEAR
        * H_amp
        * s2x**2
        * math.pi / 4.0
    )

    GHx_shear = r * shear_common
    GHy_shear = (1.0 / r) * shear_common

    twist_q = (
        D_SHEAR
        * (4.0 * math.pi**4 * q / a_h**2)
        * math.cos(X)**2
        * math.pi / 4.0
    )

    GEx = INx
    GEy = INy
    GBx = cx * INx
    GBy = INCy

    GHx = cx * INCx + GHx_shear
    GHy = cx * INCy + GHy_shear

    Rq = (
        -Cq_p * INCx
        -Cq_p * r * r * cx * INy
        +(math.pi**2 / b) * sx * IMxs
        +(math.pi**2 * b / a_h**2) * sx * IMys
        +twist_q
    )

    if model == "C0":
        return np.array([GEx, GEy, GBx, GBy, Rq, GHx, GHy])

    return np.array([GEx, GEy, GBx, GBy, GHx, GHy, Rq])


def residual(
    state: np.ndarray,
    q: float,
    b: float,
    model: str,
) -> np.ndarray:
    """
    Production M2 identity:
    exact z + exact Y + one numerical X definite integral.
    Current implementation uses scalar quad repeatedly; NEXT optimization
    is vector-valued quadrature so all residual components share one X sweep.
    """
    if model == "C0":
        n_main = 5
    else:
        n_main = 7

    # Only one-dimensional integration remains.
    raw = np.zeros(7)

    for i in range(7):
        raw[i] = quad(
            lambda X: outer_X_components(X, state, q, b, model)[i],
            0.0,
            math.pi / 2.0,
            epsabs=1.0e-5,
            epsrel=2.0e-6,
            limit=80,
        )[0]

    factor = 4.0 * b * b / math.pi**2
    raw *= factor

    P = state[-1]
    a_h = b
    Cq_p = math.pi**2 * (q + Q0) / 4.0

    # GEy external work/resultant equation
    raw[1] += P * a_h

    if model == "C0":
        # q residual is index 4
        raw[4] -= P * a_h * Cq_p

        # return only formal equations; components 5/6 are omitted-residual audit
        formal = raw[:5]
    else:
        # q residual is index 6
        raw[6] -= P * a_h * Cq_p
        formal = raw[:7]

    scale = b * b * EC * TC * 1.0e-3
    return formal / scale


if __name__ == "__main__":
    print("UCFT M2 semi-analytic kernel loaded.")
    print("NEXT: vectorize the outer X integral and add a consistent Jacobian.")
