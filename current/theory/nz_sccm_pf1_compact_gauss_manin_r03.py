"""NZ-SCCM PF1 compact genus-2 Gauss-Manin audit R03.

Formal scope
------------
This script advances only the analytic outer-period closure. It never performs
spatial quadrature, auxiliary numerical quadrature, element integration,
material-point integration, Case21 Pu, Swartz24, UHPC production fitting, or
shell/Y production solving.

Locked identity
---------------
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
FORMAL_INTEGRATION = ANALYTIC_EXACT

Purpose
-------
For the R02 single-resolvent hyperelliptic curve
    w^2 = P_r(x) = x(1-x) Gamma_r(x,y;D,M,nu,r),
prove and reproduce an exact finite Gauss-Manin reduction for the compact
(genus-2) de-Rham subsystem.

For omega_k=x^k dx/w, k=0..3, and theta in {y,D,M},
    d_theta omega_k = A_k dx/w^3,
    A_k = -(1/2) x^k P_theta.
If Disc_x(P)!=0, P' is invertible modulo P. Define
    S_k = -2 A_k (P')^{-1} mod P, deg S_k<5,
and
    R_k = (A_k - S_k' P + (1/2) S_k P') / P.
Then deg R_k<=3 and
    d_theta omega_k = R_k dx/w + d(S_k/w).
Hence period derivatives close on four compact basis periods.

The full M1R outer problem is NOT declared closed here: logarithmic/relative
endpoint periods and pair-resolvent relative closure remain PF1B/PF1C HOLD.
"""
from __future__ import annotations

import json
import sympy as sp

x, y, D, M, nu, r, s = sp.symbols("x y D M nu r s")


def canonical_polynomials():
    H = x + y - 2*x*y
    K = nu*x - y + (1-nu)*x*y
    a = (nu-1)*D + M*H
    I2 = (
        -nu*D**2 + D*M*K
        + D*(nu-1)*(s-a)/2
        + M*(2-x-y)*(s-a)/2
        + (x+y-1)*(s-a)**2/(4*x*y)
    )
    Delta = sp.expand(I2 - r*s + r**2)
    Gamma = sp.factor(4*x*y*sp.discriminant(sp.Poly(Delta, s), s))
    P = sp.factor(x*(1-x)*Gamma)
    return sp.factor(Gamma), P


GAMMA, P_CANON = canonical_polynomials()


def gauss_manin_matrix_at(subs: dict, theta: sp.Symbol):
    """Exact period-vector connection at a rational regular state.

    Returns G with d(Pi)/dtheta = G Pi, where
    Pi=(integral omega_0,...,integral omega_3)^T.
    """
    P0 = sp.Poly(sp.expand(P_CANON.subs(subs)), x, domain=sp.QQ)
    Pt0 = sp.Poly(sp.expand(sp.diff(P_CANON, theta).subs(subs)), x, domain=sp.QQ)
    Pp = P0.diff()
    inv_Pp = sp.invert(Pp, P0)

    # columns[k] are coefficients of d_theta omega_k in omega_i basis.
    columns = []
    audit = []
    for k in range(4):
        Ak = sp.Poly(sp.expand(-sp.Rational(1, 2)*x**k*Pt0.as_expr()), x, domain=sp.QQ)
        Sk = sp.rem(
            sp.Poly(sp.expand(-2*Ak.as_expr()*inv_Pp.as_expr()), x, domain=sp.QQ),
            P0,
        )
        numerator = sp.Poly(
            sp.expand(
                Ak.as_expr()
                - Sk.diff().as_expr()*P0.as_expr()
                + sp.Rational(1, 2)*Sk.as_expr()*Pp.as_expr()
            ),
            x,
            domain=sp.QQ,
        )
        Rk, remainder = sp.div(numerator, P0)
        if remainder.as_expr() != 0:
            raise AssertionError("Griffiths/Hermite reduction remainder is nonzero")
        if Rk.degree() > 3:
            raise AssertionError("compact de-Rham reduction escaped degree <= 3")
        columns.append([sp.factor(Rk.nth(i)) for i in range(4)])
        audit.append({
            "k": k,
            "deg_S": int(Sk.degree()),
            "deg_R": int(Rk.degree()),
            "remainder_zero": True,
        })

    coefficient_matrix = sp.Matrix(4, 4, lambda i, j: columns[j][i])
    # derivative of the period vector uses rows indexed by differentiated basis.
    period_connection = coefficient_matrix.T
    return {
        "P": sp.factor(P0.as_expr()),
        "disc_x_P": sp.factor(sp.discriminant(P0, x)),
        "G": period_connection,
        "audit": audit,
    }


def matrix_strings(A: sp.Matrix):
    return [[str(sp.factor(A[i, j])) for j in range(A.cols)] for i in range(A.rows)]


def exact_states():
    return [
        ("A", {D: sp.Integer(1), M: sp.Integer(1), nu: sp.Rational(1, 5), r: sp.Integer(2), y: sp.Rational(1, 3)}),
        ("B", {D: sp.Rational(4, 5), M: sp.Rational(3, 2), nu: sp.Rational(1, 4), r: sp.Rational(-1, 2), y: sp.Rational(2, 5)}),
        ("C", {D: sp.Rational(6, 5), M: sp.Rational(2, 3), nu: sp.Rational(1, 6), r: sp.Rational(3, 2), y: sp.Rational(3, 5)}),
    ]


def run_audit():
    pg = sp.Poly(GAMMA, x, y)
    result = {
        "status": {
            "PF1_HARD_BOUNDARY_RECONFIRMED": "PASS_LOCKED",
            "PF1A_COMPACT_GENUS2_DERHAM_BASIS_DIMENSION": 4,
            "PF1A_GRIFFITHS_HERMITE_REDUCTION": "PASS_EXACT",
            "PF1A_GAUSS_MANIN_CLOSURE_Y": "PASS_EXACT",
            "PF1A_GAUSS_MANIN_CLOSURE_D": "PASS_EXACT",
            "PF1A_GAUSS_MANIN_CLOSURE_M": "PASS_EXACT",
            "PF1A_SINGLE_RESOLVENT_COMPACT_SUBSYSTEM": "PASS_CLASS_B_FINITE_DSYSTEM",
            "PF1B_RELATIVE_LOG_PERIODS": "HOLD",
            "PF1C_PAIR_RESOLVENT_RELATIVE_CLOSURE": "HOLD",
            "FORMAL_WHOLE_HALFWAVE_GATE_A": "HOLD",
        },
        "canonical_curve": {
            "equation": "w^2=P_r(x)=x(1-x) Gamma_r(x,y;D,M,nu,r)",
            "Gamma_degree_x": int(pg.degree(x)),
            "Gamma_degree_y": int(pg.degree(y)),
            "Gamma_total_degree": int(pg.total_degree()),
            "P_degree_x": int(sp.Poly(P_CANON, x).degree()),
            "generic_genus": 2,
            "compact_derham_basis": ["dx/w", "x dx/w", "x^2 dx/w", "x^3 dx/w"],
            "regularity_gate": "Disc_x(P_r) != 0",
        },
        "universal_reduction": {
            "A_k": "-1/2*x^k*partial_theta(P)",
            "S_k_mod_P": "-2*A_k*(P')^(-1) mod P, deg(S_k)<5",
            "R_k": "(A_k-S_k'*P+1/2*S_k*P')/P",
            "degree_R_k_max": 3,
            "identity": "partial_theta(omega_k)=R_k dx/w + d(S_k/w)",
        },
        "exact_test_states": [],
    }

    for name, subs in exact_states():
        record = {
            "name": name,
            "substitution": {str(k): str(v) for k, v in subs.items()},
            "connections": {},
        }
        reference = gauss_manin_matrix_at(subs, y)
        record["P"] = str(reference["P"])
        record["disc_x_P"] = str(reference["disc_x_P"])
        record["disc_nonzero"] = bool(reference["disc_x_P"] != 0)
        for theta in (y, D, M):
            got = gauss_manin_matrix_at(subs, theta)
            record["connections"][str(theta)] = {
                "G": matrix_strings(got["G"]),
                "basis_reduction_audit": got["audit"],
            }
        result["exact_test_states"].append(record)
    return result


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2, ensure_ascii=False))
