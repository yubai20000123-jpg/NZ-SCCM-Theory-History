# NZ-SCCM Z6 H0 analytic-domain / shell-compiler gate reproduction
# Timestamp: 2026-08-15 15:00 +08:00
# Structural spatial sampling/quadrature = 0.
# Material-coordinate nodes below generate finite analytic coefficients only.
# No Zhou/Winter load enters any root selection.

from pathlib import Path
import importlib.util
import math
import numpy as np
from scipy.optimize import root_scalar
from numpy.polynomial.chebyshev import chebvander, chebval

HERE = Path(__file__).resolve().parent
BASE_PATH = HERE / '20260814_2240__NZSCCM_Z0_Z6__REDUCED_IDEALEP_D15__REPRO.py'
LOCAL_PATH = HERE / '20260815_1148__NZSCCM__Z0_Z5__A500_LOCAL_PROGRESSIVE_CAP_D15__REPRO.py'


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


base = load_module('base_kernel', BASE_PATH)
loc = load_module('local_shell_kernel', LOCAL_PATH)

Z6 = dict(
    a=9000.0,
    ns=60,
    ls=200.0,
    h=130.0,
    c=dict(
        b=12000.0,
        ell=9000.0,
        tc=122.0,
        eps0=0.0018712490394580678,
        fc=30.4,
        ts=4.0,
        Es=206000.0,
        fy=355.0,
    ),
)
Z6['q0'] = Z6['a'] / (500.0 * Z6['c']['b'])
Z6['rho_w'] = Z6['c']['ts'] / Z6['ls']


# -----------------------------------------------------------------------------
# 1. Analytic concrete N48 material-coordinate envelope
# -----------------------------------------------------------------------------
def lambda_envelope(D, q, c=Z6['c'], q0=Z6['q0'], nu=0.18):
    b, ell, tc, e0 = c['b'], c['ell'], c['tc'], c['eps0']
    k = b / ell
    M = math.pi**2 / e0 * (q0*q + 0.5*q*q)
    B = math.pi**2 * tc / (2.0*e0*b) * q
    den = 1.0 - nu*nu
    C1 = 1.0 + nu*k*k
    lmin = -D - (nu + k*k)*B/den
    if M <= 0.0:
        xstar = float('inf')
        lmax = max(0.0, C1*B/den)
    else:
        xstar = C1*B/(2.0*M)
        if xstar <= 1.0:
            lmax = (M + C1*C1*B*B/(4.0*M))/den
        else:
            lmax = C1*B/den
    return dict(M=M, B=B, xstar=xstar, lambda_min=lmin, lambda_max=lmax)


# -----------------------------------------------------------------------------
# 2. Same frozen R10/N48 degree on a wider scalar material domain
# -----------------------------------------------------------------------------
def compiler_errors(la, lb, ngrid_fit=5001, ncheck=20001):
    tminimax = base.set_compiler(la, lb, ngrid_fit)
    lam = np.linspace(la, lb, ncheck)  # material-coordinate check nodes only
    xi = (lam - base.lc) / base.lh
    U, C, T, T7 = base.targets(lam)
    pred = {
        'U': chebval(xi, base.Ucoef),
        'C': chebval(xi, base.Ccoef),
        'T': chebval(xi, base.Tcoef),
        'T7': chebval(xi, base.T7coef),
    }
    target = {'U': U, 'C': C, 'T': T, 'T7': T7}
    return {
        'interval': (la, lb),
        'T_minimax': float(tminimax),
        **{f'{name}_max_error': float(np.max(np.abs(pred[name]-target[name]))) for name in target},
    }


# -----------------------------------------------------------------------------
# 3. q0-parameterized concrete resultants; same R10/CH/D15 algebra
# -----------------------------------------------------------------------------
def buildS_q0(D, q, c, q0, tol=2e-9):
    f = base.low(D, q, c, nu=0.18, q0=q0)
    K1, K2 = f['K1'], f['K2']
    U = base.recur(K1, K2, base.Ucoef, tol)
    C = base.recur(K1, K2, base.Ccoef, tol)
    T = base.recur(K1, K2, base.Tcoef, tol)
    T7 = base.recur(K1, K2, base.T7coef, tol)
    CC = base.sm(base.det(C, K1, K2, tol), C, tol)
    TC = base.pa(base.sm(base.tr(T, K1, tol), C, tol), base.pm(C, T, K1, K2, tol), -1, tol)
    t7 = base.tr(T7, K1, tol)
    inner = (base.add(t7, T7[0], -1, tol), base.scale(T7[1], -1, tol))
    TT = base.sm(base.det(T, K1, K2, tol), inner, tol)
    S = base.pa(base.pa(base.pa(U, CC, -base.acc, tol), TC, 1, tol), TT, -base.rho*base.at, tol)
    return S, f


def concrete_q0(D, q, c, q0, tol=2e-9):
    S, f = buildS_q0(D, q, c, q0, tol)
    A, B = S
    Syy = base.add(A, base.mul(B, f['Yyy'], tol), 1, tol)
    iS = base.integ(Syy)
    Pc = -c['fc']*c['b']*c['tc']/(2.0*math.pi**2)*iS
    trs = base.tr(S, f['K1'], tol)
    gm = base.add(f['Gq'], base.scale(f['I1q'], base.lc, tol), -1, tol)
    sxq = base.add(base.mul(A, f['I1q'], tol), base.scale(base.mul(B, gm, tol), 1.0/base.lh, tol), 1, tol)
    Q = base.add(base.scale(sxq, 1.18, tol), base.scale(base.mul(f['I1q'], trs, tol), 0.18, tol), -1, tol)
    iQ = base.integ(Q)
    Rq = c['fc']*c['eps0']*c['b']*c['ell']*c['tc']/(2.0*math.pi**2)*iQ
    return Pc, Rq


# -----------------------------------------------------------------------------
# 4. H0 web phase and outer-shell radial cap, finite coefficient space only
# -----------------------------------------------------------------------------
def alpha_coeff(deg=24, rmax=4.0, nodes=4001, pre_weight=100.0):
    r = np.linspace(0.0, rmax, nodes)  # material coordinate only
    t = 2.0*r/rmax - 1.0
    y = np.where(r <= 1.0, 1.0, 1.0/np.sqrt(np.maximum(r, 1e-300)))
    w = np.where(r <= 1.0, pre_weight, 1.0)
    V = chebvander(t, deg)
    return np.linalg.lstsq(V*w[:, None], y*w, rcond=None)[0]


def alpha_field_custom(rfield, deg=24, rmax=4.0, nodes=4001, tol=1e-10):
    co = alpha_coeff(deg, rmax, nodes, 100.0)
    t = loc.add(loc.scale(rfield, 2.0/rmax, tol), loc.const(-1.0), tol=tol)
    T0 = loc.const(1.0)
    out = loc.scale(T0, co[0], tol)
    if deg == 0:
        return out
    T1 = t
    out = loc.add(out, loc.scale(T1, co[1], tol), tol=tol)
    a, b = T0, T1
    for n in range(2, deg+1):
        cc = loc.add(loc.scale(loc.mul(t, b, tol), 2.0, tol), a, -1.0, tol)
        out = loc.add(out, loc.scale(cc, co[n], tol), tol=tol)
        a, b = b, cc
    return out


def shell_local_resultants(D, q, c, q0, deg=24, rmax=4.0, nodes=4001, tol=2e-9):
    ips = 0.0
    irq = 0.0
    for face in (-1, 1):
        f = loc.steel_fields(D, q, c, q0, face)
        r = loc.scale(f['vm2'], 1.0/(c['fy']**2), tol)
        alpha = alpha_field_custom(r, deg, rmax, nodes, tol)
        ips += loc.integ(loc.mul(alpha, f['sy'], tol))
        irq += loc.integ(loc.mul(alpha, f['Q'], tol))
    Ps = -c['b']*c['ts']/(2.0*math.pi**2)*ips
    Rq = c['b']*c['ell']*c['ts']/(2.0*math.pi**2)*irq
    return Ps, Rq


def web_resultants(D, q, c, q0, rho_w, deg=24, rmax=4.0, nodes=4001, tol=2e-9):
    b, ell, tc, e0, Es, fy = c['b'], c['ell'], c['tc'], c['eps0'], c['Es'], c['fy']
    k = b/ell
    M = math.pi**2/e0*(q0*q + 0.5*q*q)
    Mq = math.pi**2/e0*(q0 + q)
    B = math.pi**2*tc/(2.0*e0*b)*q
    Bq = math.pi**2*tc/(2.0*e0*b)
    x2 = loc.mono(2, 0, 0)
    x2y2 = loc.mono(2, 2, 0)
    xyeta = loc.mono(1, 1, 1)
    ey = loc.const(-D)
    ey = loc.add(ey, loc.scale(x2, k*k*M))
    ey = loc.add(ey, loc.scale(x2y2, -k*k*M))
    ey = loc.add(ey, loc.scale(xyeta, k*k*B))
    eyq = loc.scale(x2, k*k*Mq)
    eyq = loc.add(eyq, loc.scale(x2y2, -k*k*Mq))
    eyq = loc.add(eyq, loc.scale(xyeta, k*k*Bq))
    u = loc.scale(ey, Es*e0/fy, tol)
    r = loc.mul(u, u, tol)
    alpha = alpha_field_custom(r, deg, rmax, nodes, tol)
    sigma = loc.scale(loc.mul(alpha, u, tol), fy, tol)
    qwork = loc.mul(sigma, loc.scale(eyq, e0, tol), tol)
    jacP = rho_w*b*tc/(2.0*math.pi**2)
    jacR = rho_w*b*ell*tc/(2.0*math.pi**2)
    Pw = -jacP*loc.integ(sigma)
    Rq = jacR*loc.integ(qwork)
    return Pw, Rq


def H0_total(D, q, c=Z6['c'], q0=Z6['q0'], rho_w=Z6['rho_w'], shell_deg=24):
    Pc, Rc = concrete_q0(D, q, c, q0)
    Pw, Rw = web_resultants(D, q, c, q0, rho_w, deg=24)
    Psh, Rsh = shell_local_resultants(D, q, c, q0, deg=shell_deg)
    Pc_eff = (1.0-rho_w)*Pc
    Rc_eff = (1.0-rho_w)*Rc
    return dict(
        Pc_full=Pc,
        Pc_eff=Pc_eff,
        Pw=Pw,
        Psh=Psh,
        P=Pc_eff+Pw+Psh,
        Rc_eff=Rc_eff,
        Rw=Rw,
        Rsh=Rsh,
        Rq=Rc_eff+Rw+Rsh,
    )


def branch_root(D, qlo, qhi, shell_deg=24):
    f = lambda qq: H0_total(D, qq, shell_deg=shell_deg)['Rq']
    r = root_scalar(f, bracket=(qlo, qhi), method='brentq', xtol=2e-9, rtol=1e-9)
    if not r.converged:
        raise RuntimeError('Rq root failed')
    return r.root, H0_total(D, r.root, shell_deg=shell_deg)


if __name__ == '__main__':
    print('FORMAL STRUCTURAL SAMPLING/QUADRATURE = 0')
    print('q0=', Z6['q0'], 'rho_w=', Z6['rho_w'])

    for D, q in [(0.705, 0.006), (0.705, 0.008), (0.80, 0.009)]:
        print('lambda envelope', D, q, lambda_envelope(D, q))

    for interval in [(-1.15, 0.30), (-1.15, 0.32), (-1.30, 0.40)]:
        print('compiler', compiler_errors(*interval))

    # Reproduce old H0 state after restoring the historical Z6 compiler.
    base.set_compiler(-1.15, 0.23, 3001)
    print('old H0', H0_total(0.705, 0.0058975999))

    # Minimal-domain same-D root.
    base.set_compiler(-1.15, 0.30, 5001)
    qroot, state = branch_root(0.705, 0.00734, 0.0073573, shell_deg=24)
    print('minimal-domain D=.705 root', qroot, state, lambda_envelope(0.705, qroot))

    # Unified-domain branch locators. Stop before the shell coefficient gate.
    base.set_compiler(-1.30, 0.40, 5001)
    brackets = [
        (0.650, 0.00640, 0.00680),
        (0.705, 0.00735, 0.0073595),
        (0.720, 0.00761, 0.00765),
        (0.740, 0.00782, 0.00796),
        (0.760, 0.00790, 0.00825),
        (0.780, 0.00810, 0.00825),
    ]
    for D, qlo, qhi in brackets:
        qroot, state = branch_root(D, qlo, qhi, shell_deg=24)
        print('branch', D, qroot, state['P']/1e6, state['Rq'], lambda_envelope(D, qroot))

    # Deep-q shell degree-conditioning audit: shell only, no branch promotion.
    for q in [0.00810, 0.00820, 0.00830, 0.00840, 0.00845, 0.00900]:
        for deg in ([10, 16, 20, 24] if q < 0.009 else [8, 10, 12, 14, 16, 18, 20, 22, 24]):
            Ps, Rs = shell_local_resultants(0.80, q, Z6['c'], Z6['q0'], deg=deg)
            print('shell-degree', q, deg, Ps/1e6, Rs)

    print('FULL KZ NOT RELEASED: shell coefficient composition must be stabilized first.')
