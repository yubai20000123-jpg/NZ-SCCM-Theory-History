# NZ-SCCM R10B transparent material-coordinate coefficient generator
# Frozen 2026-08-11. No spatial sampling/quadrature is used here.
import numpy as np

FC = 21.23
E0 = 20321.0
EPS0 = 0.00209
NU = 0.18
RHO = 0.1
KAPPA = E0 * EPS0 / FC
XCR = RHO / KAPPA
ETA = XCR / 20.0
H = 0.09799750427197301
UR = 0.03

LAM_A = -1.01
LAM_B = 0.105
LAM_C = 0.5 * (LAM_A + LAM_B)
LAM_H = 0.5 * (LAM_B - LAM_A)

def pi_eta(z):
    z = np.asarray(z, dtype=float)
    return z*z * (np.sqrt(z*z + ETA*ETA) + z) / (2.0 * (z*z + ETA*ETA))

def u_sm(t):
    t = np.asarray(t, dtype=float)
    out = np.empty_like(t)
    rise = t <= XCR
    tau = t[rise] / XCR
    out[rise] = (
        RHO*tau
        + (10*H - 6*RHO)*tau**3
        + (8*RHO - 15*H)*tau**4
        + (6*H - 3*RHO)*tau**5
    )
    fall = ~rise
    tau_f = (t[fall] - XCR) / (9*XCR)
    out[fall] = H + (UR-H) * (10*tau_f**3 - 15*tau_f**4 + 6*tau_f**5)
    return out

def C(lam):
    c = pi_eta(-np.asarray(lam, dtype=float))
    return KAPPA*c / (1.0 + (KAPPA-2.0)*c + c*c)

def T(lam):
    return u_sm(pi_eta(np.asarray(lam, dtype=float))) / RHO

def U(lam):
    lam = np.asarray(lam, dtype=float)
    c = pi_eta(-lam)
    t = pi_eta(lam)
    cc = KAPPA*c / (1.0 + (KAPPA-2.0)*c + c*c)
    return KAPPA*lam - cc + KAPPA*c + u_sm(t) - KAPPA*t

FUNCTIONS = {
    "U": U,
    "C": C,
    "T": T,
    "T7": lambda lam: T(lam)**7,
}

def coefficients(N, f):
    j = np.arange(N + 1)
    theta = (j + 0.5) * np.pi / (N + 1)
    lam = LAM_C + LAM_H * np.cos(theta)
    values = f(lam)
    a = np.empty(N + 1)
    for n in range(N + 1):
        prefactor = (1.0 if n == 0 else 2.0) / (N + 1)
        a[n] = prefactor * np.sum(values * np.cos(n * theta))
    return a

def evaluate(a, lam):
    xi = (np.asarray(lam, dtype=float) - LAM_C) / LAM_H
    return np.polynomial.chebyshev.chebval(xi, a)

if __name__ == "__main__":
    N = 112
    for name, f in FUNCTIONS.items():
        a = coefficients(N, f)
        print(name, len(a), np.max(np.abs(a)))
