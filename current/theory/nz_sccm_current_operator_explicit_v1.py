"""
NZ-SCCM explicit current material operators.
No compiler, no spatial quadrature, no hidden material-point grid.

Ordinary-concrete operator exactly matches the algebraic-Foster current target
used by the successful historical Case21 regression packages.
The later exploratory tanh tension-smoothing variant is intentionally excluded.
"""
from __future__ import annotations

import sympy as sp


def nc_parameters(fc, E0, eps0, nu):
    rho = sp.Rational(1, 10)
    kappa = E0 * eps0 / fc
    xcr = rho / kappa
    eta = xcr / 20
    return {
        "fc": fc, "E0": E0, "eps0": eps0, "nu": nu,
        "rho": rho, "kappa": kappa, "xcr": xcr, "eta": eta,
        "eta_r": sp.Rational(1, 20),
        "m_t": -sp.Rational(7, 90),
        "a_cc": sp.Float("0.1072329249362415", 30),
        "a_t": 1 - 2 ** (-sp.Rational(1, 8)),
    }


def Pi_eta(z, eta):
    return z**2 * (sp.sqrt(z**2 + eta**2) + z) / (2 * (z**2 + eta**2))


def foster_H(r, r0, eta_r=sp.Rational(1, 20)):
    return (
        sp.Rational(1, 2) * ((r-r0) + sp.sqrt((r-r0)**2 + eta_r**2))
        - sp.Rational(1, 2) * ((-r0) + sp.sqrt(r0**2 + eta_r**2))
    )


def nc_principal_response(lam, pars):
    rho = pars["rho"]
    kappa = pars["kappa"]
    xcr = pars["xcr"]
    eta = pars["eta"]
    eta_r = pars["eta_r"]
    m_t = pars["m_t"]

    c = Pi_eta(-lam, eta)
    t = Pi_eta(lam, eta)

    C = kappa*c / (1 + (kappa-2)*c + c**2)

    rr = t/xcr
    T = rr + (m_t-1)*foster_H(rr, 1, eta_r) - m_t*foster_H(rr, 10, eta_r)

    U = kappa*lam - C + kappa*c + rho*T - kappa*t
    return U, C, T, c, t


def M_NC(eps_x, eps_y, gamma_xy, fc, E0, eps0, nu):
    """
    Returns (sigma_x, sigma_y, tau_xy) using the exact explicit current operator.
    """
    p = nc_parameters(fc, E0, eps0, nu)

    X11 = (eps_x + nu*eps_y) / ((1-nu**2)*eps0)
    X22 = (nu*eps_x + eps_y) / ((1-nu**2)*eps0)
    X12 = gamma_xy / (2*(1+nu)*eps0)

    mu = (X11 + X22)/2
    delta = (X11 - X22)/2
    rad = sp.sqrt(delta**2 + X12**2)
    lp = mu + rad
    lm = mu - rad

    Up, Cp, Tp, cp, tp = nc_principal_response(lp, p)
    Um, Cm, Tm, cm, tm = nc_principal_response(lm, p)

    acc = p["a_cc"]
    at = p["a_t"]
    rho = p["rho"]

    sp_ = Up - acc*Cp**2*Cm + Cp*Tm - rho*at*Tp*Tm**8
    sm_ = Um - acc*Cm**2*Cp + Cm*Tp - rho*at*Tm*Tp**8

    Savg = (sp_ + sm_)/2
    Sdiff = (sp_ - sm_)/2

    # Continuous spectral extension at rad=0.
    Sxx = sp.Piecewise((Savg, sp.Eq(rad, 0)), (Savg + Sdiff*delta/rad, True))
    Syy = sp.Piecewise((Savg, sp.Eq(rad, 0)), (Savg - Sdiff*delta/rad, True))
    Sxy = sp.Piecewise((sp.Integer(0), sp.Eq(rad, 0)), (Sdiff*X12/rad, True))

    return fc*Sxx, fc*Syy, fc*Sxy


# Nguyen / Swartz reinforcement constants
ES_REBAR = sp.Integer(200000)       # MPa
EPSY_REBAR = sp.Rational(265, 100000)  # 0.00265
FY_REBAR = ES_REBAR * EPSY_REBAR   # 530 MPa
EPSF_REBAR = sp.Rational(4, 100)   # 0.04
EW_REBAR = sp.Integer(0)            # post-yield tangent modulus


def M_REBAR(eps_s):
    """
    Source-defined reinforcement law for |eps_s| <= 0.04.
    No post-failure branch is invented.
    """
    ae = sp.Abs(eps_s)
    return sp.Piecewise(
        (ES_REBAR*eps_s, ae <= EPSY_REBAR),
        (FY_REBAR*sp.sign(eps_s), ae <= EPSF_REBAR),
        (sp.nan, True),  # source-defined range exhausted
    )


def rebar_strain(eps_x, eps_y, gamma_xy, theta):
    c = sp.cos(theta)
    s = sp.sin(theta)
    return eps_x*c**2 + eps_y*s**2 + gamma_xy*s*c


CASE21 = {
    "fc": sp.Float("21.23"),
    "E0": sp.Float("20321.0"),
    "eps0": sp.Float("0.00209"),
    "nu": sp.Float("0.18"),
    "p_total": sp.Float("0.0075"),
    "n_layers": 1,
    "rho_s_x_per_layer": sp.Float("0.00375"),
    "rho_s_y_per_layer": sp.Float("0.00375"),
    "z_s_mm": sp.Float("0.0"),
}
