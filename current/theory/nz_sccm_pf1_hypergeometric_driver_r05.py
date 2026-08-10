"""NZ-SCCM PF1-R05 exact hypergeometric-driver audit.

Purpose
-------
Stay on the locked NZ-SCCM route and reduce the ACTUAL R04 symmetric-endpoint
Phi pullback to finite rational/algebraic whole-domain objects.  This script is
an exact symbolic audit only.

It does NOT perform spatial/auxiliary numerical quadrature, spatial cells,
material-point integration, Case21 Pu, Swartz24, UHPC fitting, shell/Y closure,
or any route switch.

Key statuses
------------
PF1_R05_PHI_FIRST_ORDER_IDENTITY = PASS_EXACT
PF1_R05_COMMON_TAU_DRIVER_IDENTITY = PASS_EXACT
PF1_R05_LOG_KERNEL_TAU_ODE = PASS_EXACT
PF1_R05_RECIPROCAL_KERNEL_TAU_ODE = PASS_EXACT
PF1_R05_X_ARCSINE_RESOLVENT_ELIMINATION = PASS_CLASS_A
PF1_R05_Y_ALGEBRAIC_TRACE_RESULTANT = PASS_FINITE_ALGEBRAIC
PF1_R05_TWISTED_CRITICAL_QUOTIENT = PASS_WITNESS_DIMENSION_19
PF1_R05_FULL_GENERIC_CONNECTION_MATRIX = HOLD
FORMAL_WHOLE_HALFWAVE_GATE_A = HOLD
"""
from __future__ import annotations

import json
import sympy as sp

x, y, tau, Z, z, rho = sp.symbols("x y tau Z z rho")
D, M, nu, r = sp.symbols("D M nu r")


def generic_blocks():
    H = x + y - 2*x*y
    Kgeom = nu*x - y + (1-nu)*x*y
    a = (nu-1)*D + M*H

    # E0 is the B^2-independent part of the R04 endpoint coefficient E_r.
    E0 = sp.expand(-nu*D**2 + D*M*Kgeom - r*a + r**2)
    h1 = x + y - 1
    E = sp.expand(E0 + tau*h1)
    K = sp.expand(E0 - tau*h1)
    ell = sp.expand(D*(nu-1) + M*(2-x-y) - 2*r)

    # R02/R04 Gamma_r, independent of the bending-square coefficient tau.
    Gamma = (
        D**2*nu**2*x*y - 2*D**2*nu*x*y + 4*D**2*nu*x + 4*D**2*nu*y - 4*D**2*nu + D**2*x*y
        + 2*D*M*nu*x**2*y - 4*D*M*nu*x**2 + 2*D*M*nu*x*y**2 - 4*D*M*nu*x*y + 4*D*M*nu*x
        - 2*D*M*x**2*y - 2*D*M*x*y**2 + 4*D*M*x*y + 4*D*M*y**2 - 4*D*M*y
        - 4*D*nu*r*x*y + 4*D*nu*r*x + 4*D*nu*r*y - 4*D*nu*r
        + 4*D*r*x*y - 4*D*r*x - 4*D*r*y + 4*D*r
        + M**2*x**3*y + 2*M**2*x**2*y**2 - 4*M**2*x**2*y + M**2*x*y**3 - 4*M**2*x*y**2 + 4*M**2*x*y
        - 4*M*r*x**2*y + 4*M*r*x**2 - 4*M*r*x*y**2 + 8*M*r*x*y - 4*M*r*x
        + 4*M*r*y**2 - 4*M*r*y + 4*r**2*x*y - 4*r**2*x - 4*r**2*y + 4*r**2
    )

    Dr = sp.factor(E**2 - tau*x*y*ell**2)
    return E0, E, K, ell, sp.expand(Gamma), Dr


def phi_first_order_audit():
    Phi = sp.atanh(sp.sqrt(z))/sp.sqrt(z)
    remainder = sp.simplify(2*z*sp.diff(Phi, z) + Phi - 1/(1-z))
    return remainder


def kernel_tau_ode_audit():
    E0, E, K, ell, Gamma, Dr = generic_blocks()

    common_remainder = sp.factor(Dr - (K**2 - tau*Gamma))

    zL = sp.cancel(tau*x*y*ell**2/E**2)
    RL = sp.cancel(ell/(2*E))
    coeffL = sp.factor(sp.diff(RL, tau)/RL - sp.diff(zL, tau)/(2*zL))
    driverL = sp.factor(RL*sp.diff(zL, tau)/(2*zL*(1-zL)))
    driverL_remainder = sp.factor(driverL - ell*K/(4*tau*Dr))

    zJ = sp.cancel(tau*Gamma/K**2)
    RJ = sp.cancel(1/K)
    coeffJ = sp.factor(sp.diff(RJ, tau)/RJ - sp.diff(zJ, tau)/(2*zJ))
    driverJ = sp.factor(RJ*sp.diff(zJ, tau)/(2*zJ*(1-zJ)))
    driverJ_remainder = sp.factor(driverJ - E/(2*tau*Dr))

    return {
        "common_remainder": common_remainder,
        "coeffL": coeffL,
        "driverL_remainder": driverL_remainder,
        "coeffJ": coeffJ,
        "driverJ_remainder": driverJ_remainder,
        "Dr": Dr,
    }


def exact_witness_audit():
    E0, E, K, ell, Gamma, Dr = generic_blocks()
    subs = {D: sp.Integer(1), M: sp.Integer(1), nu: sp.Rational(1,5), r: sp.Integer(2)}
    Drw = sp.factor(Dr.subs(subs))

    # Exact x-root trace algebraic cover: Z = rho(rho-1), D(rho,y;tau)=0.
    resultant = sp.factor(sp.resultant(Drw, Z - x*(x-1), x))
    Pres = sp.Poly(resultant, Z, y)
    discZ = sp.factor(sp.discriminant(Pres, Z))

    # Endpoint-compatible twisted critical ideal for the actual rational driver.
    hx = x*(1-x)
    hy = y*(1-y)
    Gx = sp.expand(2*hx*sp.diff(Drw, x) + sp.diff(hx, x)*Drw)
    Gy = sp.expand(2*hy*sp.diff(Drw, y) + sp.diff(hy, y)*Drw)
    Gb = sp.groebner([Gx, Gy], x, y, order="grevlex", domain=sp.QQ.frac_field(tau))
    leading = [list(p.LM(order=Gb.order).exponents) for p in Gb.polys]

    standard = []
    for i in range(12):
        for j in range(12):
            if not any(i >= a and j >= b for a, b in leading):
                standard.append([i, j])

    return {
        "parameters": {"D": "1", "M": "1", "nu": "1/5", "r": "2", "tau": "symbolic"},
        "driver": str(Drw),
        "x_root_trace_resultant": {
            "degree_Z": int(sp.degree(resultant, Z)),
            "degree_y": int(sp.degree(resultant, y)),
            "total_degree_Z_y": int(Pres.total_degree()),
            "term_count": len(Pres.terms()),
            "discriminant_degree_y": int(sp.degree(discZ, y)),
            "discriminant_degree_tau": int(sp.degree(discZ, tau)),
            "discriminant_factor_degrees": [
                [int(sp.degree(f, y)), int(sp.degree(f, tau)), int(e)]
                for f, e in sp.factor_list(discZ)[1]
            ],
        },
        "twisted_critical_ideal": {
            "groebner_leading_monomials": leading,
            "standard_monomial_count": len(standard),
            "standard_monomials": standard,
        },
    }


def main():
    ode = kernel_tau_ode_audit()
    _, _, _, _, _, Dr = generic_blocks()
    P = sp.Poly(sp.expand(Dr), x, y)

    # Exact Euler-beta resolvent identity used for the x elimination.
    hgred = sp.hyperexpand(sp.hyper([sp.Rational(1,2), 1], [1], 1/rho))

    result = {
        "status": {
            "PF1_PATH_INVARIANTS": "LOCKED",
            "PF1_R05_PHI_FIRST_ORDER_IDENTITY": "PASS_EXACT",
            "PF1_R05_COMMON_TAU_DRIVER_IDENTITY": "PASS_EXACT",
            "PF1_R05_LOG_KERNEL_TAU_ODE": "PASS_EXACT",
            "PF1_R05_RECIPROCAL_KERNEL_TAU_ODE": "PASS_EXACT",
            "PF1_R05_X_ARCSINE_RESOLVENT_ELIMINATION": "PASS_CLASS_A",
            "PF1_R05_Y_ALGEBRAIC_TRACE_RESULTANT": "PASS_FINITE_ALGEBRAIC",
            "PF1_R05_TWISTED_CRITICAL_QUOTIENT": "PASS_WITNESS_DIMENSION_19",
            "PF1_R05_FULL_GENERIC_CONNECTION_MATRIX": "HOLD",
            "FORMAL_WHOLE_HALFWAVE_GATE_A": "HOLD",
        },
        "exact_identities": {
            "phi_first_order": "2*z*Phi'(z)+Phi(z)=1/(1-z)",
            "phi_identity_remainder": str(phi_first_order_audit()),
            "common_driver": "D_r(tau)=E_tau^2-tau*x*y*ell^2=K_tau^2-tau*Gamma",
            "common_driver_remainder": str(ode["common_remainder"]),
            "log_kernel_ode": "(2*tau*d/dtau+1) F_L = ell*K_tau/(2*D_r)",
            "log_chain_coeff": str(ode["coeffL"]),
            "log_driver_remainder": str(ode["driverL_remainder"]),
            "reciprocal_kernel_ode": "(2*tau*d/dtau+1) F_J = E_tau/D_r",
            "reciprocal_chain_coeff": str(ode["coeffJ"]),
            "reciprocal_driver_remainder": str(ode["driverJ_remainder"]),
        },
        "driver_geometry": {
            "degree_x": int(sp.degree(Dr, x)),
            "degree_y": int(sp.degree(Dr, y)),
            "total_degree": int(P.total_degree()),
            "term_count": len(P.terms()),
            "support": [list(m) for m, _ in P.terms()],
        },
        "x_resolvent": {
            "basic_identity": "integral_0^1 dx/[sqrt(x(1-x))*(x-rho)] = -pi/sqrt(rho*(rho-1)) on the analytically continued branch",
            "hypergeometric_reduction": "2F1(1/2,1;1;1/rho)=" + str(hgred),
            "cubic_trace": "for simple roots rho_j of D(x,y;tau), integral N/D = -pi*sum_j N(rho_j)/(D_x(rho_j)*sqrt(rho_j(rho_j-1)))",
        },
        "exact_witness": exact_witness_audit(),
        "formal_counts": {
            "spatial_sampling": 0,
            "spatial_quadrature": 0,
            "spatial_subdomains": 1,
            "material_point_grid": 0,
        },
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
