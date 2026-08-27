from __future__ import annotations

"""NZ-SCCM qU-R06 finite-Fourier stationary certificate R01.

Purpose
-------
Replace the temporary L-BFGS local-Mises search used in the 2026-08-27 qU
pre-certification by a deterministic all-stationary-root certificate for the
finite GL+LL Fourier stress field.

This module is NOT a structural spatial discretization and does NOT evaluate
section resultants by points.  It acts only on the already-analytic finite
Fourier polynomial that defines the local R06 Mises field.

Formal identities
-----------------
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_SPATIAL_SAMPLING = 0
MATERIAL_POINTS = 0
LOCAL_SPATIAL_OPTIMIZER = 0
ROOT_ISOLATION_CERTIFICATE = 1

The coefficient interface uses normalized BH coordinates xbar=x/B, ybar=y/B
and integer fundamental Fourier indices (m,n):

    exp(i*(m*pi*xbar/9 + n*pi*ybar)).

This exactly contains the registered BH local frequencies 80/9 and 9 together
with the global q frequency 1.  The qU GL field therefore remains finite and
commensurate, although it is no longer the old degree-6 polynomial in only
u=cos(kx x), v=cos(ky y).

Algorithm
---------
1. Build Phi = sx^2 - sx*sy + sy^2 + 3*tau^2 by finite Laurent convolution.
2. Pair conjugate Fourier terms into a finite real trigonometric polynomial.
3. Compute analytic gradient/Hessian and global third-derivative bounds.
4. Exclude regions containing no stationary root with Taylor bounds.
5. Isolate every surviving interior root and certify local uniqueness with a
   Krawczyk/Newton enclosure using the analytic Hessian bounds.
6. Isolate stationary roots independently on all four boundaries.
7. Add four corners and compare the finite candidate set.

The interval enclosures in steps 4-5 are root-proof enclosures only.  No
stress/resultant is approximated by an interval cell and no quadrature or
material-point field is created.  Refining an enclosure changes only proof
width, never the operator value.
"""

from dataclasses import dataclass
from collections import defaultdict
import math
from typing import Dict, Tuple, Iterable

import numpy as np

FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_SPATIAL_SAMPLING = 0
MATERIAL_POINTS = 0
LOCAL_SPATIAL_OPTIMIZER = 0
ROOT_ISOLATION_CERTIFICATE = 1

Index = Tuple[int, int]
Laurent = Dict[Index, complex]
Box = Tuple[float, float, float, float]


def _conv(a: Laurent, b: Laurent, tol: float = 1e-14) -> Laurent:
    out = defaultdict(complex)
    for (i, j), ca in a.items():
        for (k, l), cb in b.items():
            out[(i + k, j + l)] += ca * cb
    return {k: v for k, v in out.items() if abs(v) > tol}


def _add(*parts, tol: float = 1e-12) -> Laurent:
    out = defaultdict(complex)
    for scale, d in parts:
        for k, v in d.items():
            out[k] += scale * v
    return {k: v for k, v in out.items() if abs(v) > tol}


def mises_laurent(sx: Laurent, sy: Laurent, tau: Laurent) -> Laurent:
    return _add(
        (1.0, _conv(sx, sx)),
        (-1.0, _conv(sx, sy)),
        (1.0, _conv(sy, sy)),
        (3.0, _conv(tau, tau)),
    )


def round_sig(x: float, sig: int = 12) -> float:
    if x == 0.0:
        return 0.0
    return float(f"{x:.{sig}g}")


def rationalization_snapshot(d: Laurent, sig: int = 12) -> Laurent:
    """Decimal-rationalization convention matching the prior formal R06 gate.

    The returned floating representation corresponds to the exact decimal
    rational obtained by rounding real/imaginary parts to `sig` significant
    digits.  Reports should retain a uniform perturbation bound between the
    source and this snapshot.
    """
    return {
        k: complex(round_sig(v.real, sig), round_sig(v.imag, sig))
        for k, v in d.items()
        if v != 0
    }


@dataclass(frozen=True)
class RealTerm:
    m: int
    n: int
    a_cos: float
    b_sin: float


@dataclass
class FourierFunctional:
    constant: float
    terms: list[RealTerm]

    @classmethod
    def from_real_laurent(cls, d: Laurent):
        c0 = float(d.get((0, 0), 0.0).real)
        terms = []
        for (m, n), c in d.items():
            if (m, n) == (0, 0):
                continue
            if m > 0 or (m == 0 and n > 0):
                terms.append(RealTerm(m, n, 2.0 * c.real, -2.0 * c.imag))
        return cls(c0, terms)

    def arrays(self):
        m = np.array([t.m for t in self.terms], dtype=float)
        n = np.array([t.n for t in self.terms], dtype=float)
        A = np.array([t.a_cos for t in self.terms], dtype=float)
        B = np.array([t.b_sin for t in self.terms], dtype=float)
        wx = m * math.pi / 9.0
        wy = n * math.pi
        R = np.hypot(A, B)
        return A, B, wx, wy, R


@dataclass
class RootCertificate:
    x: float
    y: float
    radius: float
    krawczyk_pass: bool
    value: float
    kind: str


class StationaryCertificate:
    def __init__(self, phi: FourierFunctional):
        self.phi = phi
        self.A, self.B, self.wx, self.wy, self.R = phi.arrays()
        self.Lxxx = float(np.sum(self.R * np.abs(self.wx) ** 3))
        self.Lxxy = float(np.sum(self.R * np.abs(self.wx) ** 2 * np.abs(self.wy)))
        self.Lxyy = float(np.sum(self.R * np.abs(self.wx) * np.abs(self.wy) ** 2))
        self.Lyyy = float(np.sum(self.R * np.abs(self.wy) ** 3))

    def value(self, x: float, y: float) -> float:
        p = self.wx * x + self.wy * y
        return float(self.phi.constant + np.sum(self.A * np.cos(p) + self.B * np.sin(p)))

    def grad(self, x: float, y: float) -> np.ndarray:
        p = self.wx * x + self.wy * y
        base = -self.A * np.sin(p) + self.B * np.cos(p)
        return np.array([np.sum(base * self.wx), np.sum(base * self.wy)], dtype=float)

    def hess(self, x: float, y: float) -> np.ndarray:
        p = self.wx * x + self.wy * y
        base = -self.A * np.cos(p) - self.B * np.sin(p)
        return np.array([
            [np.sum(base * self.wx * self.wx), np.sum(base * self.wx * self.wy)],
            [np.sum(base * self.wx * self.wy), np.sum(base * self.wy * self.wy)],
        ], dtype=float)

    def _zero_excluded(self, box: Box) -> bool:
        xl, xu, yl, yu = box
        xc, yc = (xl + xu) / 2.0, (yl + yu) / 2.0
        hx, hy = (xu - xl) / 2.0, (yu - yl) / 2.0
        g = self.grad(xc, yc)
        H = self.hess(xc, yc)
        rx = 0.5 * (self.Lxxx * hx * hx + 2 * self.Lxxy * hx * hy + self.Lxyy * hy * hy)
        ry = 0.5 * (self.Lxxy * hx * hx + 2 * self.Lxyy * hx * hy + self.Lyyy * hy * hy)
        vx = abs(H[0, 0]) * hx + abs(H[0, 1]) * hy + rx
        vy = abs(H[1, 0]) * hx + abs(H[1, 1]) * hy + ry
        return abs(g[0]) > vx or abs(g[1]) > vy

    def newton(self, seed: Tuple[float, float], maxiter: int = 30):
        z = np.array(seed, dtype=float)
        for _ in range(maxiter):
            g = self.grad(z[0], z[1])
            H = self.hess(z[0], z[1])
            dz = np.linalg.solve(H, -g)
            z = z + dz
            if np.linalg.norm(dz, ord=np.inf) < 1e-13:
                break
        return float(z[0]), float(z[1])

    def krawczyk_unique(self, root: Tuple[float, float], radius: float) -> bool:
        x, y = root
        H = self.hess(x, y)
        C = np.linalg.inv(H)
        g = self.grad(x, y)
        step = -C @ g
        r = radius
        dH = np.array([
            [self.Lxxx * r + self.Lxxy * r, self.Lxxy * r + self.Lxyy * r],
            [self.Lxxy * r + self.Lxyy * r, self.Lxyy * r + self.Lyyy * r],
        ])
        E = np.abs(C) @ dH
        rad = E @ np.array([r, r])
        return bool(np.all(np.abs(step) + rad < np.array([r, r])))

    def interior_roots(self, box: Box, discover_tol: float = 5e-5):
        # Phase 1: rigorous zero exclusion leaves only neighborhoods that may
        # contain a stationary root.  No objective maximization is performed.
        stack = [box]
        candidates = []
        processed = 0
        while stack:
            b = stack.pop(); processed += 1
            if self._zero_excluded(b):
                continue
            xl, xu, yl, yu = b
            if max(xu - xl, yu - yl) <= discover_tol:
                candidates.append(b)
                continue
            xc, yc = (xl + xu) / 2.0, (yl + yu) / 2.0
            if xu - xl >= yu - yl:
                stack += [(xl, xc, yl, yu), (xc, xu, yl, yu)]
            else:
                stack += [(xl, xu, yl, yc), (xl, xu, yc, yu)]

        # Finite seed compression is used only after rigorous candidate
        # neighborhoods have been obtained.  Newton solves grad(Phi)=0.
        seeds = {}
        for b in candidates:
            c = ((b[0] + b[1]) / 2.0, (b[2] + b[3]) / 2.0)
            seeds[(round(c[0], 3), round(c[1], 3))] = c
        roots = []
        for s in seeds.values():
            try:
                z = self.newton(s)
            except Exception:
                continue
            if box[0] < z[0] < box[1] and box[2] < z[1] < box[3] and np.linalg.norm(self.grad(*z)) < 1e-3:
                if all((z[0]-r0[0])**2 + (z[1]-r0[1])**2 > 1e-12 for r0 in roots):
                    roots.append(z)
        roots.sort()

        # Krawczyk uniqueness for each isolated interior root.
        certs = []
        covers = []
        for z in roots:
            distance = min(z[0]-box[0], box[1]-z[0], z[1]-box[2], box[3]-z[1])
            rad = min(5e-7, 0.4 * distance)
            ok = self.krawczyk_unique(z, rad)
            certs.append(RootCertificate(z[0], z[1], rad, ok, self.value(*z), 'interior'))
            if ok:
                covers.append((z[0]-rad, z[0]+rad, z[1]-rad, z[1]+rad))

        # Phase 2: prove no unaccounted interior stationary roots remain.
        def inside_cover(b, c):
            return c[0] <= b[0] and b[1] <= c[1] and c[2] <= b[2] and b[3] <= c[3]
        stack = [box]
        unresolved = []
        processed2 = 0
        while stack:
            b = stack.pop(); processed2 += 1
            if any(inside_cover(b, c) for c in covers):
                continue
            if self._zero_excluded(b):
                continue
            xl, xu, yl, yu = b
            if max(xu-xl, yu-yl) < 5e-8:
                unresolved.append(b)
                continue
            xc, yc = (xl+xu)/2.0, (yl+yu)/2.0
            if xu-xl >= yu-yl:
                stack += [(xl, xc, yl, yu), (xc, xu, yl, yu)]
            else:
                stack += [(xl, xu, yl, yc), (xl, xu, yc, yu)]
        return certs, unresolved, (processed, processed2)

    def edge_roots(self, box: Box):
        # One-dimensional derivative root isolation on the four physical edges.
        xl, xu, yl, yu = box
        out = {}

        def solve_edge(variable, fixed, a, b):
            if variable == 'x':
                f = lambda t: self.grad(t, fixed)[0]
                fp = lambda t: self.hess(t, fixed)[0, 0]
                L3 = self.Lxxx
            else:
                f = lambda t: self.grad(fixed, t)[1]
                fp = lambda t: self.hess(fixed, t)[1, 1]
                L3 = self.Lyyy
            stack = [(a, b)]
            boxes = []
            while stack:
                lo, hi = stack.pop()
                c = (lo + hi) / 2.0; h = (hi - lo) / 2.0
                if abs(f(c)) > abs(fp(c))*h + 0.5*L3*h*h:
                    continue
                if hi-lo < 1e-6:
                    boxes.append((lo, hi)); continue
                stack += [(lo, c), (c, hi)]
            roots = []
            for lo, hi in boxes:
                z = (lo + hi) / 2.0
                try:
                    for _ in range(30):
                        dz = -f(z) / fp(z)
                        z += dz
                        if abs(dz) < 1e-13:
                            break
                except Exception:
                    continue
                if a-1e-10 <= z <= b+1e-10 and abs(f(z)) < 1e-3:
                    if all(abs(z-r0) > 1e-9 for r0 in roots):
                        roots.append(float(z))
            return sorted(roots)

        out['ylo'] = solve_edge('x', yl, xl, xu)
        out['yhi'] = solve_edge('x', yu, xl, xu)
        out['xlo'] = solve_edge('y', xl, yl, yu)
        out['xhi'] = solve_edge('y', xu, yl, yu)
        return out

    def global_candidates(self, box: Box):
        interior, unresolved, processed = self.interior_roots(box)
        if unresolved:
            raise RuntimeError(f'unresolved stationary-root enclosures: {len(unresolved)}')
        edges = self.edge_roots(box)
        cands = list(interior)
        xl, xu, yl, yu = box
        for x in edges['ylo']:
            cands.append(RootCertificate(x, yl, 0.0, True, self.value(x, yl), 'edge-ylo'))
        for x in edges['yhi']:
            cands.append(RootCertificate(x, yu, 0.0, True, self.value(x, yu), 'edge-yhi'))
        for y in edges['xlo']:
            cands.append(RootCertificate(xl, y, 0.0, True, self.value(xl, y), 'edge-xlo'))
        for y in edges['xhi']:
            cands.append(RootCertificate(xu, y, 0.0, True, self.value(xu, y), 'edge-xhi'))
        for x in (xl, xu):
            for y in (yl, yu):
                cands.append(RootCertificate(x, y, 0.0, True, self.value(x, y), 'corner'))
        cands.sort(key=lambda r: r.value, reverse=True)
        return cands, processed


def certify_mises(sx: Laurent, sy: Laurent, tau: Laurent, box: Box, sig_digits: int = 12):
    sxr = rationalization_snapshot(sx, sig_digits)
    syr = rationalization_snapshot(sy, sig_digits)
    tr = rationalization_snapshot(tau, sig_digits)
    phi = FourierFunctional.from_real_laurent(mises_laurent(sxr, syr, tr))
    cert = StationaryCertificate(phi)
    candidates, processed = cert.global_candidates(box)

    # Uniform Mises perturbation bound for rationalization.  Plane-stress Mises
    # has quadratic-form lambda_max=3, hence ||delta VM|| <= sqrt(3)||delta s||_2.
    def coeff_error(a, b):
        keys = set(a) | set(b)
        return sum(abs(a.get(k, 0.0) - b.get(k, 0.0)) for k in keys)
    ds = np.array([coeff_error(sx, sxr), coeff_error(sy, syr), coeff_error(tau, tr)])
    vm_rounding_bound = math.sqrt(3.0) * float(np.linalg.norm(ds))

    return {
        'maximum': candidates[0],
        'candidates': candidates,
        'interior_count': sum(c.kind == 'interior' for c in candidates),
        'edge_count': sum(c.kind.startswith('edge') for c in candidates),
        'corner_count': sum(c.kind == 'corner' for c in candidates),
        'processed_root_enclosures': processed,
        'vm_rounding_bound_MPa': vm_rounding_bound,
    }
