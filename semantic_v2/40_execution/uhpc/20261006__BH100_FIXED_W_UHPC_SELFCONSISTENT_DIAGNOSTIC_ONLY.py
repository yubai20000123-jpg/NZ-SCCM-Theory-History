"""
BH100 fixed-w UHPC W_E-W_P-d self-consistent closure.
DIAGNOSTIC VALIDATION ONLY.

Production contract is NOT this area quadrature.
Production must replace the area integration backend with:
  quartic level-set roots + finite 1-D algebraic/Abelian definite integrals.
The 3-scalar root system itself is the intended reduced-order structure.

Branch:
  diagnostic/20261006-bh100-uhpc-we-wp-d-self-consistency
"""

import math
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import root

# BH100
b = 5000.0
ah = 10000.0
tc = 42.0
Ec = 43400.0
nu = 0.30
ft = 7.3
fc = 141.1
w0 = 12.5
w_total = 82.2

alpha = math.pi / b
beta = math.pi / ah
AT = w0 + w_total

D0 = Ec * tc**3 / (12.0 * (1.0 - nu**2))
Kfac = (alpha**2 + beta**2)**2 / beta**2
Lfac = (alpha**4 + beta**4) / beta**2

# Final UHPC_UC141 Abaqus input.
c_sig = np.array([
119.49,132.75,141.1,138.58,132.28,123.94,114.85,112.11,108.49,105.83,
101.49,98.96,97.31,89.5,87.31,84.49,82.46,76.16,70.55,53.58,42.57,
35.06,29.67,25.65,22.56,20.11,19.99,16.49,15.12,12.5
], dtype=float)
c_in = np.array([
0,9.13521e-05,0.000248848,0.000656904,0.00115204,0.00169426,0.00225371,
0.00242185,0.00264516,0.00281164,0.00308658,0.00324981,0.00335783,
0.0038877,0.00404324,0.00424814,0.00439998,0.00489512,0.00537442,
0.00716538,0.00881905,0.0103923,0.0119163,0.0134089,0.0148802,
0.0163367,0.0164134,0.0192201,0.0206517,0.0242119
], dtype=float)
c_d = np.array([
0,0.014607,0.0362051,0.0892994,0.148118,0.207765,0.265113,0.28159,
0.302951,0.318494,0.34346,0.357869,0.367238,0.411269,0.42359,0.439408,
0.450827,0.486296,0.518103,0.616623,0.683619,0.731449,0.767066,
0.794518,0.816278,0.833927,0.834769,0.860772,0.871207,0.891565
], dtype=float)

t_sig = np.array([
5.57131,6.20338,6.63126,6.91944,7.10779,7.22269,7.2824,7.3,7.28516,
7.24514,7.18549,7.11054,7.02369,6.92762,6.82449,6.71603,6.60364,
6.48846,5.8981,5.3246,4.7937,4.31285,2.85138
], dtype=float)
t_ck = np.array([
0,0.000246,0.000333,0.000424,0.000517,0.000611,0.000707,0.000804,
0.000901,0.000999,0.001098,0.001197,0.001296,0.001396,0.001495,
0.001595,0.001695,0.001794,0.002294,0.002793,0.003292,0.003789,0.005766
], dtype=float)
t_d = np.array([
0,0.393674,0.439294,0.477144,0.509385,0.537378,0.562037,0.584009,
0.603772,0.621684,0.638025,0.653016,0.666835,0.679628,0.691516,
0.702599,0.712964,0.722682,0.763513,0.794881,0.819813,0.840127,0.893861
], dtype=float)

# Convert input strain measures to total strain.
c_tot = c_in + c_sig / Ec
t_tot = t_ck + t_sig / Ec

# CDP-compatible plastic strain used for permanent reference geometry.
c_pl = c_in - (c_d / (1.0 - c_d)) * c_sig / Ec
t_pl = t_ck - (t_d / (1.0 - t_d)) * t_sig / Ec

def interp_state(x, xp, fp):
    """Piecewise-linear material function; zero before first nonlinear node."""
    x = np.asarray(x)
    y = np.interp(x, xp, fp, left=fp[0], right=fp[-1])
    return np.where(x < xp[0], 0.0, y)

def residual_and_state(x, n=180):
    e, rhoA, rhoD = map(float, x)
    Q = 2.0 * AT * e - e * e

    Ny = (
        rhoD * D0 * Kfac * e / AT
        + rhoA * Ec * tc / 16.0 * Lfac * Q
    )

    # Diagnostic symmetric quadrature on theta,phi in [0,pi/2]^2.
    # DO NOT use as production backend.
    g, wg = leggauss(n)
    th = (g + 1.0) * math.pi / 4.0
    wt = wg * math.pi / 4.0
    TH, PH = np.meshgrid(th, th, indexing="ij")
    WGT = np.outer(wt, wt)

    sT = np.sin(TH); sP = np.sin(PH)
    cT = np.cos(TH); cP = np.cos(PH)
    c2T = np.cos(2.0 * TH); c2P = np.cos(2.0 * PH)

    ex0 = (
        nu * Ny / (rhoA * Ec * tc)
        - alpha**2 * Q / 8.0 * c2P
        + nu * beta**2 * Q / 8.0 * c2T
    )
    ey0 = (
        -Ny / (rhoA * Ec * tc)
        - beta**2 * Q / 8.0 * c2T
        + nu * alpha**2 * Q / 8.0 * c2P
    )

    faces = []
    for sgn in (+1.0, -1.0):
        z = sgn * tc / 2.0
        ex = ex0 + z * alpha**2 * e * sT * sP
        ey = ey0 + z * beta**2 * e * sT * sP
        gam = 2.0 * z * alpha * beta * e * cT * cP

        disc = np.sqrt((ex - ey)**2 + gam**2)
        e1 = 0.5 * (ex + ey + disc)
        e2 = 0.5 * (ex + ey - disc)

        et = np.maximum(e1, 0.0)
        ec = np.maximum(-e2, 0.0)

        dt = interp_state(et, t_tot, t_d)
        dc = interp_state(ec, c_tot, c_d)
        pt = interp_state(et, t_tot, t_pl)
        pc = interp_state(ec, c_tot, c_pl)

        # Eigenprojector of major principal direction.
        den = np.maximum(disc, 1e-30)
        P1xx = 0.5 * (1.0 + (ex - ey) / den)
        P1yy = 1.0 - P1xx

        exp = pt * P1xx - pc * P1yy
        eyp = pt * P1yy - pc * P1xx

        faces.append({
            "et": et, "ec": ec,
            "d": np.maximum(dt, dc),
            "pt": pt, "pc": pc,
            "exp": exp, "eyp": eyp
        })

    top, bottom = faces

    kxp = (top["exp"] - bottom["exp"]) / tc
    kyp = (top["eyp"] - bottom["eyp"]) / tc

    H = alpha**4 + beta**4 + 2.0 * nu * alpha**2 * beta**2

    wp_integrand = sT * sP * (
        (alpha**2 + nu * beta**2) * kxp
        + (beta**2 + nu * alpha**2) * kyp
    )

    wP_mat = 16.0 / (math.pi**2 * H) * np.sum(WGT * wp_integrand)

    dplus = top["d"]
    dminus = bottom["d"]
    d0 = 0.5 * (dplus + dminus)
    d1 = 0.5 * (dplus - dminus)

    rhoA_loc = 1.0 - d0
    rhoD_loc = (1.0 - d0) - d1**2 / (3.0 * np.maximum(1.0 - d0, 1e-12))

    PsiA = (
        alpha**4 * c2P**2
        + beta**4 * c2T**2
        - 2.0 * nu * alpha**2 * beta**2 * c2T * c2P
    )
    PsiD = (
        H * (sT * sP)**2
        + 2.0 * (1.0 - nu) * alpha**2 * beta**2 * (cT * cP)**2
    )

    IA = 4.0 / (alpha * beta) * np.sum(WGT * rhoA_loc * PsiA)
    ID = 4.0 / (alpha * beta) * np.sum(WGT * rhoD_loc * PsiD)

    denA = b * ah / 2.0 * (alpha**4 + beta**4)
    denD = b * ah / 4.0 * (alpha**2 + beta**2)**2

    rhoA_mat = IA / denA
    rhoD_mat = ID / denD

    R = np.array([
        w_total - e - wP_mat,
        rhoA - rhoA_mat,
        rhoD - rhoD_mat
    ])

    state = {
        "e": e,
        "wP": w_total - e,
        "wP_mat": wP_mat,
        "rhoA": rhoA,
        "rhoD": rhoD,
        "rhoA_mat": rhoA_mat,
        "rhoD_mat": rhoD_mat,
        "Q": Q,
        "Ny_N_per_mm": Ny,
        "PU_MN": b * Ny / 1.0e6,
        "max_tension_total_strain": max(top["et"].max(), bottom["et"].max()),
        "max_compression_total_strain": max(top["ec"].max(), bottom["ec"].max()),
        "max_raw_damage": max(top["d"].max(), bottom["d"].max()),
    }
    return R, state

if __name__ == "__main__":
    x0 = np.array([54.0, 0.78, 0.72])
    sol = root(lambda x: residual_and_state(x, n=180)[0], x0, method="hybr", tol=1e-10)
    R, s = residual_and_state(sol.x, n=180)

    print("success =", sol.success)
    print("x =", sol.x)
    print("R =", R)
    for k, v in s.items():
        print(k, "=", v)

    # Reference diagnostic result at n=180:
    # e       = 54.05826765 mm
    # wP      = 28.14173235 mm
    # rhoA    = 0.78174116
    # rhoD    = 0.72154674
    # PU      = 6.96255384 MN
    # max et  = 0.00107530553
    # max ec  = 0.00119318767
    # max d   = 0.60496112
