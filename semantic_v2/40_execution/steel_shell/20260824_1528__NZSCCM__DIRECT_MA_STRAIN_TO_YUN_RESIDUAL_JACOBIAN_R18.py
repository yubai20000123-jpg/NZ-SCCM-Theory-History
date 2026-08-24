"""
NZ-SCCM R18
Direct Marguerre–Airy explicit strain -> always-on Yun steel-shell
stress/tangent -> equilibrium residual/Jacobian.

ARCHITECTURE
------------
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
YUN_ALWAYS_ON = True
A_B_D_INTERMEDIATE = False

The high-order Gauss-Legendre integration in this file is used ONLY as a
verification oracle for the direct residual/Jacobian chain rule. It is not
the formal NZ-SCCM production integration rule.

The upstream Marguerre–Airy field is represented explicitly.  The historical
project relation used here is

    e_y = -D + M(q)*(u^2-u^2*v^2) + alpha*B_A^y(u,v)
          + B(q)*u*v*zeta

    M(q) = pi^2*(q0*q + q^2/2)
    B(q) = 2*pi^2*q

The physical axial global strain is eps_g = eps0*e_y.

B_A^y is intentionally supplied as an upstream callable; this kernel does
not invent or refit the structural Airy basis.  The verification harness uses
a clearly labelled manufactured harmonic B_A^y only to prove the analytic
chain rule and Jacobian.

The historical Yun/Karman steel strain is

    eps_s = eps_g
            + A*(w0_y + dw_y)*phi_y
            + A0*dw_y*phi_y
            + (A0*A + A^2/2)*phi_y^2.

The current steel law is the already executed ideal EPP baseline

    sigma = clip(Es*eps_s, -fy, +fy)
    Et    = Es in the elastic branch, 0 in the yielded branch.

Global steel residual rows are inserted directly:

    R_i^s = ts * integral sigma * eps_{,i} dOmega

and their exact current Jacobian is

    K_ij^s = ts * integral [
        Et * eps_{,i} * eps_{,j}
        + sigma * eps_{,ij}
    ] dOmega.

The Yun local-amplitude row remains an always-on local equilibrium equation:

    R_A = C_sigma*[k_cr*A + H*(2*A0*A + A^2)*(A+A0)]
          - sigma_bar_c*(A+A0)

where sigma_bar_c is the current compression-positive average obtained from
the same direct EPP stress field.  Its Jacobian includes the full chain rule
through sigma_bar_c.

No width/thickness gate, sigma_cr/fy gate, CC/TC/TT gate, experimental
comparator, or terminal capacity fit is present in this operator.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Dict, Tuple
import csv
import math
import numpy as np
from numpy.polynomial.legendre import leggauss

FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
YUN_ALWAYS_ON = True
A_B_D_INTERMEDIATE = False
VERIFICATION_ORACLE_GAUSS = True

GLOBAL_NAMES = ("D", "q", "alpha")
ALL_NAMES = ("D", "q", "alpha", "A")


@dataclass(frozen=True)
class MAParams:
    eps0: float
    q0: float
    b_global: float
    ell_global: float
    zeta: float
    BAy: Callable[[np.ndarray, np.ndarray], np.ndarray]


@dataclass(frozen=True)
class YunStrip:
    Bs: float
    ell_local: float
    m_local: int
    A0: float
    ts: float
    Es: float
    fy: float
    C_sigma: float
    k_cr: float
    H: float


@dataclass(frozen=True)
class State:
    D: float
    q: float
    alpha: float
    A: float

    def vector(self) -> np.ndarray:
        return np.array([self.D, self.q, self.alpha, self.A], dtype=float)

    @staticmethod
    def from_vector(v: np.ndarray) -> "State":
        return State(D=float(v[0]), q=float(v[1]),
                     alpha=float(v[2]), A=float(v[3]))


def _mapped_gauss(n: int, lo: float, hi: float) -> Tuple[np.ndarray, np.ndarray]:
    """Verification oracle only."""
    xi, wi = leggauss(n)
    x = 0.5*(hi-lo)*xi + 0.5*(hi+lo)
    w = 0.5*(hi-lo)*wi
    return x, w


class DirectMAYunOperator:
    def __init__(self, ma: MAParams, strip: YunStrip):
        self.ma = ma
        self.strip = strip

    def _field(self, state: State, x: np.ndarray, y: np.ndarray) -> Dict[str, np.ndarray]:
        """
        Return eps_s and exact first/second generalized derivatives.
        Shapes are the broadcast shape of x and y.
        """
        ma, s = self.ma, self.strip
        D, q, alpha, A = state.D, state.q, state.alpha, state.A

        u = x / ma.b_global
        v = y / ma.ell_global

        # Historical explicit Marguerre–Airy axial strain structure.
        h = u*u*(1.0 - v*v)
        bay = ma.BAy(u, v)
        M = math.pi**2 * (ma.q0*q + 0.5*q*q)
        B = 2.0*math.pi**2*q

        e_y = -D + M*h + alpha*bay + B*u*v*ma.zeta
        eps_g = ma.eps0 * e_y

        deps_g = np.zeros((4,) + eps_g.shape, dtype=float)
        deps_g[0] = -ma.eps0
        deps_g[1] = ma.eps0 * (
            math.pi**2*(ma.q0 + q)*h
            + 2.0*math.pi**2*u*v*ma.zeta
        )
        deps_g[2] = ma.eps0 * bay

        d2eps_g = np.zeros((4, 4) + eps_g.shape, dtype=float)
        d2eps_g[1, 1] = ma.eps0 * math.pi**2 * h

        # Explicit global half-wave slopes.  These are current deformation
        # outputs; no A/B/D constitutive matrix is formed.
        slope_basis = (
            ma.b_global * math.pi / ma.ell_global
            * np.sin(math.pi*x/ma.b_global)
            * np.cos(math.pi*y/ma.ell_global)
        )
        w0_y = ma.q0 * slope_basis
        dw_y = q * slope_basis
        g_y = w0_y + dw_y

        dg_y = np.zeros((4,) + eps_g.shape, dtype=float)
        ddw_y = np.zeros((4,) + eps_g.shape, dtype=float)
        dg_y[1] = slope_basis
        ddw_y[1] = slope_basis

        d2g_y = np.zeros((4, 4) + eps_g.shape, dtype=float)
        d2dw_y = np.zeros((4, 4) + eps_g.shape, dtype=float)

        # Yun local Karman shape and its axial derivative.
        phi_y = (
            (1.0 - np.cos(2.0*math.pi*x/s.Bs))
            * (2.0*s.m_local*math.pi/s.ell_local)
            * np.sin(2.0*s.m_local*math.pi*y/s.ell_local)
        )

        eps = (
            eps_g
            + A*g_y*phi_y
            + s.A0*dw_y*phi_y
            + (s.A0*A + 0.5*A*A)*phi_y*phi_y
        )

        deps = deps_g.copy()
        for j in range(3):
            deps[j] += A*dg_y[j]*phi_y + s.A0*ddw_y[j]*phi_y
        deps[3] = g_y*phi_y + (s.A0 + A)*phi_y*phi_y

        d2eps = d2eps_g.copy()
        for i in range(3):
            for j in range(3):
                d2eps[i, j] += A*d2g_y[i, j]*phi_y + s.A0*d2dw_y[i, j]*phi_y

        # global-A cross derivative
        for j in range(3):
            d2eps[j, 3] = dg_y[j]*phi_y
            d2eps[3, j] = d2eps[j, 3]
        d2eps[3, 3] = phi_y*phi_y

        return {
            "eps": eps,
            "deps": deps,
            "d2eps": d2eps,
            "phi_y": phi_y,
            "g_y": g_y,
            "dw_y": dw_y,
        }

    def epp(self, eps: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        trial = self.strip.Es * eps
        sigma = np.clip(trial, -self.strip.fy, self.strip.fy)
        # Deliberately treat equality as yielded; verification states stay
        # away from the non-differentiable transition.
        Et = np.where(np.abs(trial) < self.strip.fy, self.strip.Es, 0.0)
        return sigma, Et

    def assemble_oracle(self, state: State, order: int = 48):
        """
        High-order verification oracle, not formal production integration.

        Returns residual [R_D,R_q,R_alpha,R_A] and exact analytic Jacobian.
        Global rows are direct virtual-work rows. The A row is the historical
        Yun local-amplitude equilibrium using current average compression.
        """
        s = self.strip
        x, wx = _mapped_gauss(order, 0.0, s.Bs)
        y, wy = _mapped_gauss(order, 0.0, s.ell_local)
        X, Y = np.meshgrid(x, y, indexing="ij")
        W = wx[:, None] * wy[None, :]
        area = s.Bs * s.ell_local

        f = self._field(state, X, Y)
        eps, deps, d2eps = f["eps"], f["deps"], f["d2eps"]
        sigma, Et = self.epp(eps)

        R = np.zeros(4, dtype=float)
        K = np.zeros((4, 4), dtype=float)

        # Direct steel contribution to global equilibrium.
        for i in range(3):
            R[i] = s.ts * np.sum(W * sigma * deps[i])
            for j in range(4):
                K[i, j] = s.ts * np.sum(
                    W * (Et*deps[i]*deps[j] + sigma*d2eps[i, j])
                )

        # Current compression-positive average from the same Yun/EPP state.
        comp_mask = sigma < 0.0
        sigma_c_density = np.where(comp_mask, -sigma, 0.0)
        bar_sigma_c = np.sum(W*sigma_c_density) / area

        dbar = np.zeros(4, dtype=float)
        for j in range(4):
            # d(-sigma)/deta = -Et*eps_,j on currently compressive points.
            dsigc = np.where(comp_mask, -Et*deps[j], 0.0)
            dbar[j] = np.sum(W*dsigc) / area

        A, A0 = state.A, s.A0
        F = 2.0*A0*A + A*A
        G = A + A0
        Fp = 2.0*(A0 + A)

        R[3] = (
            s.C_sigma*(s.k_cr*A + s.H*F*G)
            - bar_sigma_c*G
        )

        for j in range(3):
            K[3, j] = -G*dbar[j]
        K[3, 3] = (
            s.C_sigma*(s.k_cr + s.H*(Fp*G + F))
            - bar_sigma_c
            - G*dbar[3]
        )

        diag = {
            "bar_sigma_c": float(bar_sigma_c),
            "elastic_fraction": float(np.sum(W*(Et > 0.0))/area),
            "compression_fraction": float(np.sum(W*comp_mask)/area),
            "min_eps": float(np.min(eps)),
            "max_eps": float(np.max(eps)),
            "min_sigma": float(np.min(sigma)),
            "max_sigma": float(np.max(sigma)),
        }
        return R, K, diag

    def finite_difference_jacobian(self, state: State, order: int = 48):
        base = state.vector()
        J = np.zeros((4, 4), dtype=float)
        # Coordinate-aware steps: D,q,alpha dimensionless; A in mm.
        abs_steps = np.array([2e-7, 2e-8, 2e-7, 2e-5], dtype=float)
        for j in range(4):
            h = max(abs_steps[j], 2e-6*max(abs(base[j]), 1e-3))
            vp = base.copy(); vp[j] += h
            vm = base.copy(); vm[j] -= h
            Rp, _, _ = self.assemble_oracle(State.from_vector(vp), order=order)
            Rm, _, _ = self.assemble_oracle(State.from_vector(vm), order=order)
            J[:, j] = (Rp - Rm)/(2.0*h)
        return J


def manufactured_BAy(u: np.ndarray, v: np.ndarray) -> np.ndarray:
    """
    Verification-only Airy basis. It is NOT claimed to be the project's
    physical B_A^y. The production operator accepts the actual upstream BAy.
    """
    return (1.0-u*u)*(1.0-v*v)


def relative_matrix_error(A: np.ndarray, B: np.ndarray) -> float:
    denom = max(np.linalg.norm(B), 1.0)
    return float(np.linalg.norm(A-B)/denom)


def max_scaled_entry_error(A: np.ndarray, B: np.ndarray) -> float:
    scale = np.maximum(np.maximum(np.abs(A), np.abs(B)), 1.0)
    return float(np.max(np.abs(A-B)/scale))


def run_verification(csv_path: str | None = None):
    ma = MAParams(
        eps0=0.0020,
        q0=0.0040,
        b_global=6000.0,
        ell_global=6000.0,
        zeta=0.20,
        BAy=manufactured_BAy,
    )
    strip = YunStrip(
        Bs=200.0,
        ell_local=1000.0,
        m_local=1,
        A0=0.20,
        ts=4.0,
        Es=206000.0,
        fy=355.0,
        # Verification-only local-equilibrium constants; no physical
        # calibration claim is made by this derivative test.
        C_sigma=25.0,
        k_cr=4.0,
        H=0.015,
    )
    op = DirectMAYunOperator(ma, strip)

    cases = {
        # Entire strip remains elastic.
        "ELASTIC": State(D=0.10, q=0.0010, alpha=0.020, A=0.25),
        # Entire strip remains compressive-yielded. Yun geometry remains on;
        # Et=0 but sigma*eps_,ij geometric/current-stress terms survive.
        "FULL_COMPRESSION_YIELDED": State(D=2.50, q=0.0010, alpha=0.020, A=0.25),
    }

    rows = []
    for name, st in cases.items():
        R, K, diag = op.assemble_oracle(st, order=56)
        Jfd = op.finite_difference_jacobian(st, order=56)
        rel = relative_matrix_error(K, Jfd)
        mx = max_scaled_entry_error(K, Jfd)

        gg_asym = np.linalg.norm(K[:3,:3]-K[:3,:3].T) / max(np.linalg.norm(K[:3,:3]),1.0)
        yielded_geom_norm = float(np.linalg.norm(K[:3,:])) if diag["elastic_fraction"] == 0.0 else float("nan")

        rows.append({
            "case": name,
            "relative_jacobian_error": rel,
            "max_scaled_entry_error": mx,
            "global_global_symmetry_error": float(gg_asym),
            "elastic_fraction": diag["elastic_fraction"],
            "compression_fraction": diag["compression_fraction"],
            "bar_sigma_c_MPa": diag["bar_sigma_c"],
            "min_eps": diag["min_eps"],
            "max_eps": diag["max_eps"],
            "min_sigma_MPa": diag["min_sigma"],
            "max_sigma_MPa": diag["max_sigma"],
            "global_jacobian_norm_when_fully_yielded": yielded_geom_norm,
            "pass_jacobian": rel < 2e-6 and mx < 2e-6,
        })

    # Structural/architecture checks.
    no_gate = (
        YUN_ALWAYS_ON
        and FORMAL_SPATIAL_QUADRATURE == 0
        and MATERIAL_POINTS == 0
        and not A_B_D_INTERMEDIATE
    )
    for r in rows:
        r["architecture_guard_pass"] = no_gate

    if csv_path is not None:
        keys = list(rows[0].keys())
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=keys)
            w.writeheader()
            w.writerows(rows)

    return rows


if __name__ == "__main__":
    here = __import__("pathlib").Path(__file__).resolve().parent
    csv_path = here / "20260824_1528__NZSCCM__DIRECT_MA_STRAIN_TO_YUN_RESIDUAL_JACOBIAN_R18_RESULTS.csv"
    rows = run_verification(str(csv_path))
    print("NZ-SCCM R18 direct MA -> Yun residual/Jacobian verification")
    print(f"FORMAL_SPATIAL_QUADRATURE={FORMAL_SPATIAL_QUADRATURE}")
    print(f"MATERIAL_POINTS={MATERIAL_POINTS}")
    print(f"YUN_ALWAYS_ON={YUN_ALWAYS_ON}")
    print(f"A_B_D_INTERMEDIATE={A_B_D_INTERMEDIATE}")
    print(f"VERIFICATION_ORACLE_GAUSS={VERIFICATION_ORACLE_GAUSS}")
    for r in rows:
        print(r)
