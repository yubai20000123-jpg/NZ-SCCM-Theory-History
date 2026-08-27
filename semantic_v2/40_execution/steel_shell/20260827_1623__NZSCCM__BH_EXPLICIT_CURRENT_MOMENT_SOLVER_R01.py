from __future__ import annotations

"""NZ-SCCM explicit BH/SSUHPC solver R01.

Purpose
-------
Reproduce the 2026-08-27 single-harmonic explicit route without spatial
quadrature or material points:

    initial full-composite Airy membrane skeleton
    -> q-derived common curvature
    -> qU-augmented R02/R06 steel faces
    -> exact UHPC directional N-M
    -> exact web resultant
    -> current normal moments in the same retained q harmonic
    -> finite terminal root

This code is intentionally BH-family specific in geometry registration.  It is
reusable for the self-similar BH005/BH010/BH020/BH032/BH050 family by changing
`B` and the raw specimen geometry/material inputs.  A different local PBL
registration must provide its own exact harmonic geometry backend.

Important execution identity
----------------------------
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
EFFECTIVE_WIDTH = 0
COMPARATOR_IN_ROOT_SELECTION = 0

The GL+LL local-Mises field is analytic.  This execution backend locates its
continuous stationary maximum with deterministic gradient-based optimization;
it does not integrate or sample the plate for resultants.  A formal production
certificate may replace that numerical stationary search by the finite
algebraic resultant backend without changing the theory or root equations.
"""

from dataclasses import dataclass, asdict
from collections import defaultdict
from fractions import Fraction as F
import cmath
import json
import math
from typing import Dict, Tuple

import mpmath as mp
import numpy as np
from scipy.optimize import brentq, least_squares, minimize

FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
EFFECTIVE_WIDTH = False
COMPARATOR_IN_ROOT_SELECTION = False


# ---------------------------------------------------------------------------
# S00 — raw specimen/material inputs
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class BHSpec:
    name: str = "BH050"
    B: float = 2500.0                 # mm, transverse width
    a_phys: float = 5000.0            # mm, physical loaded length = 2B
    ts: float = 4.0                   # mm, each external steel face
    tc: float = 42.0                  # mm, UHPC core thickness
    Aw: float = 1332.0                # mm2, nine longitudinal webs total area
    q0: float = 0.0025                # dimensionless global imperfection
    Es: float = 206000.0              # MPa
    nu_s: float = 0.30
    fy: float = 355.0                  # MPa
    Ec: float = 43400.0               # MPa
    nu_c: float = 0.20
    fc: float = 141.1                 # MPa
    eps_c0: float = 0.0035
    fct: float = 4.513133983249735    # MPa
    eps_t0: float = 0.001
    mt: float = 0.4418


@dataclass
class LedgerEntry:
    stage: str
    name: str
    value: object
    units: str
    method: str
    source: str


class ProvenanceLedger:
    def __init__(self):
        self.rows = []

    def add(self, stage, name, value, units, method, source):
        self.rows.append(LedgerEntry(stage, name, value, units, method, source))
        return value

    def as_jsonable(self):
        return [asdict(r) for r in self.rows]


# ---------------------------------------------------------------------------
# Exact finite-harmonic BH qU geometry backend, inherited from 1320 R01
# ---------------------------------------------------------------------------

def _add(a, b, scale=1.0):
    out = defaultdict(complex)
    out.update(a)
    for k, v in b.items():
        out[k] += scale * v
    return {k: v for k, v in out.items() if abs(v) > 1e-14}


def _mul(a, b):
    out = defaultdict(complex)
    for (ax, ay), ca in a.items():
        for (bx, by), cb in b.items():
            out[(ax + bx, ay + by)] += ca * cb
    return {k: v for k, v in out.items() if abs(v) > 1e-13}


def _deriv(f, dx=0, dy=0):
    return {
        (a, b): c * (1j * math.pi * float(a)) ** dx
        * (1j * math.pi * float(b)) ** dy
        for (a, b), c in f.items()
    }


def _scale(f, s):
    return {k: s * v for k, v in f.items()}


def _sin_mode(r, axis):
    if axis == "x":
        return {(r, F(0)): 1 / (2j), (-r, F(0)): -1 / (2j)}
    return {(F(0), r): 1 / (2j), (F(0), -r): -1 / (2j)}


def _cos_shift(r, x0, axis):
    ph = cmath.exp(-1j * math.pi * float(r * x0))
    if axis == "x":
        return {(r, F(0)): 0.5 * ph, (-r, F(0)): 0.5 * ph.conjugate()}
    return {(F(0), r): 0.5 * ph, (F(0), -r): 0.5 * ph.conjugate()}


def _one_minus_cos(r, x0, axis):
    return _add({(F(0), F(0)): 1 + 0j}, _cos_shift(r, x0, axis), -1)


def _psi():
    return _mul(_sin_mode(F(1), "x"), _sin_mode(F(1), "y"))


def _phi(x0, y0):
    # BH self-similar ratios: kx/pi=80/9, ky/pi=9 in normalized x/B,y/B.
    return _mul(_one_minus_cos(F(80, 9), x0, "x"), _one_minus_cos(F(9), y0, "y"))


def _source_ll(p):
    K = _add(
        _mul(_deriv(p, 2, 0), _deriv(p, 0, 2)),
        _mul(_deriv(p, 1, 1), _deriv(p, 1, 1)),
        -1,
    )
    return _scale(K, -1)


def _source_gl(ps, p):
    C = _add(
        _mul(_deriv(ps, 2, 0), _deriv(p, 0, 2)),
        _mul(_deriv(p, 2, 0), _deriv(ps, 0, 2)),
    )
    C = _add(C, _mul(_deriv(ps, 1, 1), _deriv(p, 1, 1)), -2)
    return _scale(C, -1)


def _stress_from_source(S):
    sx, sy, tau = {}, {}, {}
    for (a, b), c in S.items():
        aa, bb = math.pi * float(a), math.pi * float(b)
        den = (aa * aa + bb * bb) ** 2
        if den < 1e-30:
            continue
        FF = c / den
        sx[(a, b)] = -bb * bb * FF
        sy[(a, b)] = -aa * aa * FF
        tau[(a, b)] = aa * bb * FF
    return sx, sy, tau


_PATTERN = {
    "TOP": (F(31, 80), F(4, 9)),
    "BOTTOM": (F(11, 40), F(4, 9)),
}

# Exact scale-free values emitted by 1320 exact rational-harmonic backend.
_SCALE_FREE = {
    "TOP": dict(
        hx=9.564070824135575,
        hy=9.564070824135571,
        hgamma=0.0,
        KA=103860.65999983741,
        KdDelta=2354.8943862105207,
        KDeltaDelta=57.07652449604563,
    ),
    "BOTTOM": dict(
        hx=8.972928383353008,
        hy=8.972928383353010,
        hgamma=1.1673861933222223,
        KA=103860.65999983740,
        KdDelta=2209.3415101552087,
        KDeltaDelta=50.67092721328501,
    ),
}


def _packed_harmonics(pattern):
    x0, y0 = _PATTERN[pattern]
    p, ps = _phi(x0, y0), _psi()
    ll = _stress_from_source(_source_ll(p))
    gl = _stress_from_source(_source_gl(ps, p))
    freqs = sorted(
        set().union(*[set(d.keys()) for d in ll + gl]),
        key=lambda z: (float(z[0]), float(z[1])),
    )
    arr = np.array([[float(a), float(b)] for a, b in freqs], dtype=float)
    lli = np.zeros((3, len(freqs)), dtype=complex)
    gli = np.zeros((3, len(freqs)), dtype=complex)
    index = {k: i for i, k in enumerate(freqs)}
    for j, d in enumerate(ll):
        for k, c in d.items():
            lli[j, index[k]] = c
    for j, d in enumerate(gl):
        for k, c in d.items():
            gli[j, index[k]] = c
    return arr, lli, gli


# ---------------------------------------------------------------------------
# S10/S20 — global initial full-composite ABD + Airy coefficients
# ---------------------------------------------------------------------------

class BHSolver:
    def __init__(self, spec: BHSpec):
        self.s = spec
        self.L = ProvenanceLedger()
        self._introduce_raw_inputs()
        self._derive_global()
        self._derive_local()
        self._derive_harmonics()

    def _introduce_raw_inputs(self):
        for k, v in asdict(self.s).items():
            if k == "name":
                continue
            units = "-"
            if k in {"B", "a_phys", "ts", "tc"}:
                units = "mm"
            elif k == "Aw":
                units = "mm2"
            elif k in {"Es", "fy", "Ec", "fc", "fct"}:
                units = "MPa"
            self.L.add("S00_RAW", k, v, units, "direct specimen/material input", "BH current geometry/material contract")

    def _derive_global(self):
        s = self.s
        self.rho = self.L.add(
            "S10_GEOM", "rho_w", s.Aw / (s.B * s.tc), "-",
            "Aw/(B*tc)", "nine-web equivalent longitudinal steel fraction"
        )
        self.zf = self.L.add("S10_GEOM", "z_f", s.tc / 2 + s.ts / 2, "mm", "tc/2+ts/2", "gross face centroid")

        Qs11 = s.Es / (1 - s.nu_s ** 2)
        Qs12 = s.nu_s * Qs11
        Qs66 = s.Es / (2 * (1 + s.nu_s))
        Qc11 = s.Ec / (1 - s.nu_c ** 2)
        Qc12 = s.nu_c * Qc11
        Qc66 = s.Ec / (2 * (1 + s.nu_c))

        self.A11 = 2 * s.ts * Qs11 + (1 - self.rho) * s.tc * Qc11
        self.A22 = self.A11 + self.rho * s.tc * s.Es
        self.A12 = 2 * s.ts * Qs12 + (1 - self.rho) * s.tc * Qc12
        self.A66 = 2 * s.ts * Qs66 + (1 - self.rho) * s.tc * Qc66
        self.DeltaA = self.A11 * self.A22 - self.A12 ** 2

        If = 2 * (s.ts * self.zf ** 2 + s.ts ** 3 / 12)
        Ic = s.tc ** 3 / 12
        self.Dx = Qs11 * If + (1 - self.rho) * Qc11 * Ic
        self.Dy = self.Dx + self.rho * s.Es * Ic
        self.Dmu = Qs12 * If + (1 - self.rho) * Qc12 * Ic
        self.D66 = Qs66 * If + (1 - self.rho) * Qc66 * Ic
        self.H = self.Dmu + 2 * self.D66

        # BH family: a_phys=2B -> m*=2 -> representative halfwave ell=B.
        self.ell = s.B
        self.alpha = math.pi / s.B
        self.beta = math.pi / self.ell
        self.Kx = self.alpha ** 2 * s.B ** 2 * self.DeltaA / (8 * self.A22)
        self.Gairy = self.beta ** 2 * s.B ** 2 * self.DeltaA / (8 * self.A11)
        self.Km = self.DeltaA / 16 * (self.alpha ** 4 / self.A22 + self.beta ** 4 / self.A11)
        self.C = s.B ** 3 * self.Km / self.beta ** 2
        Kbglob = self.Dx * self.alpha ** 4 + 2 * self.H * self.alpha ** 2 * self.beta ** 2 + self.Dy * self.beta ** 4
        self.Pcr = s.B * Kbglob / self.beta ** 2

        for n, v, u in [
            ("A11", self.A11, "N/mm"), ("A22", self.A22, "N/mm"),
            ("A12", self.A12, "N/mm"), ("A66", self.A66, "N/mm"),
            ("DeltaA", self.DeltaA, "N2/mm2"),
            ("Dx", self.Dx, "N mm"), ("Dy", self.Dy, "N mm"),
            ("Dmu", self.Dmu, "N mm"), ("D66_0", self.D66, "N mm"),
            ("alpha", self.alpha, "1/mm"), ("beta", self.beta, "1/mm"),
            ("Kx", self.Kx, "N/mm"), ("G", self.Gairy, "N/mm"),
            ("Km", self.Km, "N/mm2"), ("C", self.C, "N"),
            ("Pcr_elastic_regression", self.Pcr, "N"),
        ]:
            self.L.add("S20_AIRY", n, v, u, "closed-form initial full-composite ABD/Airy evaluation", "1710 explicit harmonic theory")

    def _derive_local(self):
        s = self.s
        self.Lx = 0.225 * s.B
        self.Ly = 2 * s.B / 9
        self.A0 = self.Lx / 1600
        self.kx = 2 * math.pi / self.Lx
        self.ky = 2 * math.pi / self.Ly
        self.Qs = s.Es / (1 - s.nu_s ** 2)
        self.Gs = s.Es / (2 * (1 + s.nu_s))
        self.Ds = s.Es * s.ts ** 3 / (12 * (1 - s.nu_s ** 2))
        self.cx = 3 * self.kx ** 2 / 8
        self.cy = 3 * self.ky ** 2 / 8
        self.Kb_local = self.Ds * (0.75 * (self.kx ** 4 + self.ky ** 4) + 0.5 * self.kx ** 2 * self.ky ** 2)
        r = self.Ly / self.Lx
        kcr = 4 * (3 * r ** 4 + 2 * r ** 2 + 3) / (3 * r ** 2)
        csig = math.pi ** 2 * s.Es * s.ts ** 2 / (12 * (1 - s.nu_s ** 2) * self.Lx ** 2)
        self.sigma_cr_local = csig * kcr
        for n, v, u, m in [
            ("Lx", self.Lx, "mm", "0.225B"),
            ("Ly", self.Ly, "mm", "2B/9"),
            ("A0", self.A0, "mm", "Lx/1600"),
            ("cx", self.cx, "1/mm2", "3kx^2/8"),
            ("cy", self.cy, "1/mm2", "3ky^2/8"),
            ("Kb_local", self.Kb_local, "N/mm3", "R02 local bending coefficient"),
            ("sigma_cr_local", self.sigma_cr_local, "MPa", "Yun elastic local-buckling stress"),
        ]:
            self.L.add("S30_R02_GEOM", n, v, u, m, "BH PBL geometry contract")

    def _derive_harmonics(self):
        self.packed = {p: _packed_harmonics(p) for p in ("TOP", "BOTTOM")}
        self.geom = {}
        for p in ("TOP", "BOTTOM"):
            sf = _SCALE_FREE[p]
            self.geom[p] = dict(
                hx=sf["hx"] / self.s.B ** 2,
                hy=sf["hy"] / self.s.B ** 2,
                hgamma=sf["hgamma"] / self.s.B ** 2,
                KA=sf["KA"] / self.s.B ** 4,
                KdDelta=sf["KdDelta"] / self.s.B ** 4,
                KDeltaDelta=sf["KDeltaDelta"] / self.s.B ** 4,
            )
            for n, v in self.geom[p].items():
                self.L.add("S40_Q_U", f"{p}_{n}", v, "1/mm2" if n.startswith("h") else "1/mm4", "scale-free exact rational harmonic coefficient / B power", "1320 exact geometry backend")

    # ------------------------------------------------------------------
    # S50 — UHPC exact directional N-M primitives
    # ------------------------------------------------------------------
    def _uhpc_sigma(self, eps):
        s = self.s
        if eps < 0:
            xi = -eps / s.eps_c0
            nh = s.Ec * s.eps_c0 / s.fc
            return -s.fc * (nh * xi - xi * xi) / (1 + (nh - 2) * xi)
        if eps > 0:
            xi = eps / s.eps_t0
            return s.fct * math.exp(1 / s.mt) * xi * math.exp(-(xi ** s.mt) / s.mt)
        return 0.0

    def _S0(self, eps):
        s = self.s
        if abs(eps) < 1e-18:
            return 0.0
        if eps < 0:
            nh = s.Ec * s.eps_c0 / s.fc
            a = nh - 2
            xi = -eps / s.eps_c0
            F0 = -xi ** 2 / (2 * a) + (nh - 1) ** 2 / a ** 2 * xi - (nh - 1) ** 2 / a ** 3 * math.log(1 + a * xi)
            return s.fc * s.eps_c0 * F0
        xi = eps / s.eps_t0
        T0 = float(mp.e ** (1 / s.mt) * s.mt ** (2 / s.mt - 1) * mp.gammainc(2 / s.mt, 0, xi ** s.mt / s.mt))
        return s.fct * s.eps_t0 * T0

    def _S1(self, eps):
        s = self.s
        if abs(eps) < 1e-18:
            return 0.0
        if eps < 0:
            nh = s.Ec * s.eps_c0 / s.fc
            a = nh - 2
            xi = -eps / s.eps_c0
            F1 = -xi ** 3 / (3 * a) + (nh - 1) ** 2 / (2 * a ** 2) * xi ** 2 - (nh - 1) ** 2 / a ** 3 * xi + (nh - 1) ** 2 / a ** 4 * math.log(1 + a * xi)
            return -s.fc * s.eps_c0 ** 2 * F1
        xi = eps / s.eps_t0
        T1 = float(mp.e ** (1 / s.mt) * s.mt ** (3 / s.mt - 1) * mp.gammainc(3 / s.mt, 0, xi ** s.mt / s.mt))
        return s.fct * s.eps_t0 ** 2 * T1

    def uhpc_NM(self, A, Bcur):
        h = self.s.tc / 2
        if abs(Bcur) < 1e-14:
            return (1 - self.rho) * self.s.tc * self._uhpc_sigma(A), 0.0
        ep, em = A + Bcur * h, A - Bcur * h
        N = (1 - self.rho) * (self._S0(ep) - self._S0(em)) / Bcur
        M = (1 - self.rho) * ((self._S1(ep) - self._S1(em)) - A * (self._S0(ep) - self._S0(em))) / Bcur ** 2
        return N, M

    # ------------------------------------------------------------------
    # S60 — exact clipped-affine longitudinal web
    # ------------------------------------------------------------------
    def web_NM(self, A, Bcur):
        s = self.s
        ey = s.fy / s.Es
        zlo, zhi = -s.tc / 2, s.tc / 2
        pts = [zlo, zhi]
        if abs(Bcur) > 1e-16:
            for ec in (-ey, ey):
                z = (ec - A) / Bcur
                if zlo < z < zhi:
                    pts.append(z)
        pts = sorted(pts)
        N = M = 0.0
        for l, r in zip(pts[:-1], pts[1:]):
            e = A + Bcur * (l + r) / 2
            if e > ey:
                sig = s.fy
                N += self.rho * sig * (r - l)
                M += self.rho * sig * (r * r - l * l) / 2
            elif e < -ey:
                sig = -s.fy
                N += self.rho * sig * (r - l)
                M += self.rho * sig * (r * r - l * l) / 2
            else:
                N += self.rho * s.Es * (A * (r - l) + Bcur * (r * r - l * l) / 2)
                M += self.rho * s.Es * (A * (r * r - l * l) / 2 + Bcur * (r ** 3 - l ** 3) / 3)
        return N, M

    # ------------------------------------------------------------------
    # S70 — qU R02 cubic + nonnegative active-set minimum energy
    # ------------------------------------------------------------------
    def cubic_coeffs(self, q, epsx, epsy, pattern):
        s, g = self.s, self.geom[pattern]
        ex, ey, gamma = -epsx, -epsy, 0.0
        Ccc = self.Qs * (self.cx ** 2 + 2 * s.nu_s * self.cx * self.cy + self.cy ** 2)
        Cch = self.Qs * (self.cx * g["hx"] + s.nu_s * self.cx * g["hy"] + s.nu_s * self.cy * g["hx"] + self.cy * g["hy"])
        Chh = self.Qs * (g["hx"] ** 2 + 2 * s.nu_s * g["hx"] * g["hy"] + g["hy"] ** 2) + self.Gs * g["hgamma"] ** 2
        Lc = self.Qs * (self.cx * (ex + s.nu_s * ey) + self.cy * (ey + s.nu_s * ex))
        Lh = self.Qs * (g["hx"] * (ex + s.nu_s * ey) + g["hy"] * (ey + s.nu_s * ex)) + self.Gs * gamma * g["hgamma"]
        W, W0, a = s.B * (s.q0 + q), s.B * s.q0, self.A0
        B3 = 2 * s.ts * (2 * s.Es * g["KA"] + Ccc)
        B2 = 3 * W * s.ts * (2 * s.Es * g["KdDelta"] + Cch)
        B1 = self.Kb_local - B3 * a ** 2 - 2 * a * W0 * s.ts * (2 * s.Es * g["KdDelta"] + Cch) + W ** 2 * s.ts * (2 * s.Es * g["KDeltaDelta"] + Chh) - 2 * s.ts * Lc
        B0 = -a * self.Kb_local - a ** 2 * W * s.ts * (2 * s.Es * g["KdDelta"] + Cch) - a * W * W0 * s.ts * (2 * s.Es * g["KDeltaDelta"] + Chh) - W * s.ts * Lh
        return B3, B2, B1, B0

    def _amp_energy(self, q, epsx, epsy, pattern, U):
        s, g = self.s, self.geom[pattern]
        ex, ey = -epsx, -epsy
        d = U ** 2 - self.A0 ** 2
        Delta = s.B * ((s.q0 + q) * U - s.q0 * self.A0)
        mx = ex - self.cx * d - g["hx"] * Delta
        my = ey - self.cy * d - g["hy"] * Delta
        mg = -g["hgamma"] * Delta
        return (
            0.5 * self.Kb_local * (U - self.A0) ** 2
            + 0.5 * s.ts * self.Qs * (mx ** 2 + my ** 2 + 2 * s.nu_s * mx * my)
            + 0.5 * s.ts * self.Gs * mg ** 2
            + s.ts * s.Es * (g["KA"] * d ** 2 + 2 * g["KdDelta"] * d * Delta + g["KDeltaDelta"] * Delta ** 2)
        )

    def amplitude(self, q, epsx, epsy, pattern):
        coeff = self.cubic_coeffs(q, epsx, epsy, pattern)
        roots = np.roots(coeff)
        candidates = [0.0]
        candidates.extend(float(z.real) for z in roots if abs(z.imag) < 1e-8 and z.real > 1e-12)
        return min(candidates, key=lambda U: self._amp_energy(q, epsx, epsy, pattern, U))

    def mean_stress(self, q, epsx, epsy, pattern, U=None):
        s, g = self.s, self.geom[pattern]
        if U is None:
            U = self.amplitude(q, epsx, epsy, pattern)
        ex, ey = -epsx, -epsy
        d = U ** 2 - self.A0 ** 2
        Delta = s.B * ((s.q0 + q) * U - s.q0 * self.A0)
        mx = ex - self.cx * d - g["hx"] * Delta
        my = ey - self.cy * d - g["hy"] * Delta
        mg = -g["hgamma"] * Delta
        return np.array([-self.Qs * (mx + s.nu_s * my), -self.Qs * (my + s.nu_s * mx), self.Gs * mg]), U, d, Delta

    # ------------------------------------------------------------------
    # S80 — analytic GL+LL local stress field + R06 first local-Mises yield
    # ------------------------------------------------------------------
    def _stress_field(self, q, epsx, epsy, pattern, U=None):
        mean, U, d, Delta = self.mean_stress(q, epsx, epsy, pattern, U)
        freq, ll, gl = self.packed[pattern]
        coeff = self.s.Es / self.s.B ** 2 * (d * ll + Delta * gl)
        wx, wy = math.pi * freq[:, 0], math.pi * freq[:, 1]

        def evaluate(v):
            x, y = v
            ee = np.exp(1j * math.pi * (freq[:, 0] * x + freq[:, 1] * y))
            vals = (coeff @ ee).real + mean
            dx = (coeff @ (1j * wx * ee)).real
            dy = (coeff @ (1j * wy * ee)).real
            sx, sy, tt = vals
            Fv = sx * sx - sx * sy + sy * sy + 3 * tt * tt
            vm = math.sqrt(max(Fv, 0.0))
            Fx = 2 * sx * dx[0] - (dx[0] * sy + sx * dx[1]) + 2 * sy * dx[1] + 6 * tt * dx[2]
            Fy = 2 * sx * dy[0] - (dy[0] * sy + sx * dy[1]) + 2 * sy * dy[1] + 6 * tt * dy[2]
            grad = np.array([Fx, Fy]) / (2 * vm) if vm > 1e-14 else np.zeros(2)
            return vm, -grad

        return evaluate, U

    def _max_local_vm(self, q, epsx, epsy, pattern, seed=None):
        fg, U = self._stress_field(q, epsx, epsy, pattern)
        if pattern == "TOP":
            xb = (31 / 80, 49 / 80)
        else:
            xb = (11 / 40, 1 / 2)
        yb = (4 / 9, 6 / 9)
        xc, yc = sum(xb) / 2, sum(yb) / 2
        starts = [seed or (xc, yc), (xc, yc), (xb[0] + 0.02 * (xb[1] - xb[0]), yc), (xb[1] - 0.02 * (xb[1] - xb[0]), yc)]
        best = None
        for st in starts:
            r = minimize(lambda v: -fg(v)[0], st, jac=lambda v: fg(v)[1], method="L-BFGS-B", bounds=[xb, yb], options={"ftol": 1e-14, "gtol": 1e-10, "maxiter": 100})
            z = (-r.fun, float(r.x[0]), float(r.x[1]))
            if best is None or z[0] > best[0]:
                best = z
        return best, U

    def r06_face(self, q, epsx, epsy, pattern):
        s = self.s
        seed = None

        def f(eta):
            nonlocal seed
            m, U = self._max_local_vm(eta * q, eta * epsx, eta * epsy, pattern, seed)
            seed = (m[1], m[2])
            return m[0] - s.fy

        f1 = f(1.0)
        if f1 <= 0:
            mean, U, _, _ = self.mean_stress(q, epsx, epsy, pattern)
            return dict(eta=1.0, stress=mean, U=U, maxvm=f1 + s.fy, loc=seed)
        eta = brentq(f, 0.0, 1.0, xtol=1e-11, rtol=1e-11, maxiter=60)
        m, U = self._max_local_vm(eta * q, eta * epsx, eta * epsy, pattern, seed)
        mean, U, _, _ = self.mean_stress(eta * q, eta * epsx, eta * epsy, pattern, U)
        return dict(eta=eta, stress=mean, U=U, maxvm=m[0], loc=(m[1], m[2]))

    # ------------------------------------------------------------------
    # S90 — current section + explicit current-moment harmonic load
    # ------------------------------------------------------------------
    def section_state(self, q, Ax, Ay):
        s = self.s
        kappa = math.pi ** 2 * q / s.B
        NxU, MxU = self.uhpc_NM(Ax, kappa)
        NyU, MyU = self.uhpc_NM(Ay, kappa)
        Nw, Mw = self.web_NM(Ay, kappa)

        top = self.r06_face(q, Ax + self.zf * kappa, Ay + self.zf * kappa, "TOP")
        bot = self.r06_face(q, Ax - self.zf * kappa, Ay - self.zf * kappa, "BOTTOM")
        Nt, Nb = s.ts * top["stress"], s.ts * bot["stress"]

        Nx = NxU + Nt[0] + Nb[0]
        Ny = NyU + Nw + Nt[1] + Nb[1]
        Mx = MxU + self.zf * Nt[0] - self.zf * Nb[0]
        My = MyU + Mw + self.zf * Nt[1] - self.zf * Nb[1]

        Qq = q * (q + 2 * s.q0)
        twist = 4 * s.B * q * self.D66 * self.alpha ** 2
        P = (Mx + My + twist) / (q + s.q0) + self.C * Qq
        Nxd = self.Kx * Qq
        Nyd = -P / s.B + self.Gairy * Qq
        return dict(q=q, Ax=Ax, Ay=Ay, kappa=kappa, P=P, Qq=Qq, NxU=NxU, MxU=MxU, NyU=NyU, MyU=MyU, Nw=Nw, Mw=Mw, top=top, bottom=bot, Nx=Nx, Ny=Ny, Mx=Mx, My=My, twist=twist, Nxd=Nxd, Nyd=Nyd, Rx=Nx-Nxd, Ry=Ny-Nyd)

    # ------------------------------------------------------------------
    # S100 — BH governing y-bottom UHPC endpoint, two unknowns (q,Ax)
    # ------------------------------------------------------------------
    def endpoint_state(self, q, Ax):
        kappa = math.pi ** 2 * q / self.s.B
        Ay = -self.s.eps_c0 + self.s.tc / 2 * kappa
        return self.section_state(q, Ax, Ay)

    def solve_endpoint(self):
        # Deterministic theory-only seeds.  No FEM/test load is read here.
        seeds = [(0.010, 0.0005), (0.015, 0.0010), (0.020, 0.0035), (0.024, 0.0045)]
        roots = []

        def residual(x):
            q, Ax = float(x[0]), float(x[1])
            try:
                st = self.endpoint_state(q, Ax)
                return np.array([st["Rx"] / 1000.0, st["Ry"] / 5000.0])
            except Exception:
                return np.array([10.0, 10.0])

        for seed in seeds:
            sol = least_squares(residual, seed, bounds=([1e-5, -0.002], [0.04, 0.008]), xtol=1e-12, ftol=1e-12, gtol=1e-12, max_nfev=120)
            if np.linalg.norm(sol.fun) > 1e-7:
                continue
            st = self.endpoint_state(float(sol.x[0]), float(sol.x[1]))
            if st["q"] <= 0:
                continue
            # UHPC compressed endpoints must not have crossed -eps_c0 elsewhere.
            h = self.s.tc / 2
            core_eps = [st["Ax"] + h * st["kappa"], st["Ax"] - h * st["kappa"], st["Ay"] + h * st["kappa"], st["Ay"] - h * st["kappa"]]
            if min(core_eps) < -self.s.eps_c0 - 1e-8:
                continue
            if all(abs(st["q"] - r["q"]) > 1e-7 for r in roots):
                roots.append(st)

        if not roots:
            raise RuntimeError("No admissible BH UHPC endpoint root")
        roots.sort(key=lambda r: r["P"])
        root = roots[0]
        self.L.add("S100_ROOT", "q_u", root["q"], "-", "two-variable least_squares on Rx=Ry=0 after Ay(q) endpoint elimination; multi-seed, comparator-blind", "1710 terminal system + 1623 R02 active-set completion")
        self.L.add("S100_ROOT", "A_x", root["Ax"], "-", "same simultaneous root", "current section inverse")
        self.L.add("S100_ROOT", "A_y", root["Ay"], "-", "-eps_c0 + tc*pi^2*q/(2B)", "active UHPC y-bottom endpoint")
        self.L.add("S100_ROOT", "P_u", root["P"], "N", "explicit current-moment load after root", "1710 Section 8")
        return root


def summarize(root):
    Ny_faces = root["top"]["stress"][1] * 4 + root["bottom"]["stress"][1] * 4
    shares = {
        "UHPC_pct": 100 * root["NyU"] / root["Ny"],
        "steel_faces_pct": 100 * Ny_faces / root["Ny"],
        "web_pct": 100 * root["Nw"] / root["Ny"],
    }
    return {
        "q_u": root["q"],
        "P_u_MN": root["P"] / 1e6,
        "A_x": root["Ax"],
        "A_y": root["Ay"],
        "kappa_per_mm": root["kappa"],
        "Rx_N_per_mm": root["Rx"],
        "Ry_N_per_mm": root["Ry"],
        "Nx_sec": root["Nx"],
        "Nx_d": root["Nxd"],
        "Ny_sec": root["Ny"],
        "Ny_d": root["Nyd"],
        "Mx_sec_N": root["Mx"],
        "My_sec_N": root["My"],
        "top_U_mm": root["top"]["U"],
        "bottom_U_mm": root["bottom"]["U"],
        "top_eta": root["top"]["eta"],
        "bottom_eta": root["bottom"]["eta"],
        "top_stress_MPa": root["top"]["stress"].tolist(),
        "bottom_stress_MPa": root["bottom"]["stress"].tolist(),
        "load_shares": shares,
    }


if __name__ == "__main__":
    solver = BHSolver(BHSpec())
    root = solver.solve_endpoint()
    print(json.dumps({"result": summarize(root), "parameter_provenance": solver.L.as_jsonable()}, indent=2, ensure_ascii=False))
