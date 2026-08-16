"""NZ-SCCM R10 exact finite-matrix source-lift / fixed algebraic-atom reduction gate.

This reproducer does NOT compute structural P, Rq, Rm, L, KZ, or Pu.
It introduces no structural spatial/thickness numerical integration.
"""
import numpy as np
import sympy as sp

RHO = 0.1
H = 0.09799750427197301
UR = 0.03
ACC = 0.1072329249362415
AT = 1.0 - 2.0**(-1.0/8.0)

CASES = {
    "Z0": {"guard": (-2.4632226527364014, 0.534418784330357), "kappa": 2.000512953368},
    "Z1": {"guard": (-2.3741117667045084, 0.4319238472937275), "kappa": 2.000512953368},
    "Z2": {"guard": (-2.4632226527364014, 0.534418784330357), "kappa": 2.000512953368},
    "Z3": {"guard": (-2.368172, 0.420738), "kappa": 2.0009130559586734},
    "Z4": {"guard": (-2.528721, 0.612756), "kappa": 2.000512953368},
    "Z5": {"guard": (-3.189668, 1.403255), "kappa": 2.000512953368},
    "Z6": {"guard": (-3.013646, 2.372868), "kappa": 2.000512953368},
}


def spline_exact_identity():
    z, rho, Hs, Us = sp.symbols("z rho H U", real=True)
    p1 = rho*z + (10*Hs-6*rho)*z**3 + (8*rho-15*Hs)*z**4 + (6*Hs-3*rho)*z**5
    s = (z-1)/9
    p2 = Hs + (Us-Hs)*(10*s**3 - 15*s**4 + 6*s**5)
    A3 = 4*rho + (-7300*Hs + 10*Us)/729
    A4 = 7*rho + (-32800*Hs - 5*Us)/2187
    A5 = 3*rho + (-118100*Hs + 2*Us)/19683
    B3 = 10*(Hs-Us)/729
    B4 = 5*(Hs-Us)/2187
    B5 = 2*(Hs-Us)/19683
    mid = sp.expand(p1 + A3*(z-1)**3 + A4*(z-1)**4 + A5*(z-1)**5)
    high = sp.expand(mid + B3*(z-10)**3 + B4*(z-10)**4 + B5*(z-10)**5)
    return sp.simplify(mid-p2), sp.simplify(high-Us), (A3,A4,A5,B3,B4,B5)


def pi_scalar(x, kappa):
    x = np.asarray(x, float)
    eta = (RHO/kappa)/20.0
    r = np.sqrt(x*x + eta*eta)
    return x*x*(r+x)/(2.0*(x*x+eta*eta))


def ur_scalar(t, kappa):
    t = np.asarray(t,float)
    a = RHO/kappa
    out = np.empty_like(t)
    m1 = t <= a
    tau = t[m1]/a
    out[m1] = RHO*tau + (10*H-6*RHO)*tau**3 + (8*RHO-15*H)*tau**4 + (6*H-3*RHO)*tau**5
    m2 = (t>a) & (t<=10*a)
    s = (t[m2]-a)/(9*a)
    out[m2] = H + (UR-H)*(10*s**3-15*s**4+6*s**5)
    out[t>10*a] = UR
    return out


def cf_scalar(c,kappa):
    return kappa*c/(1+(kappa-2)*c+c*c)


def scalar_principal_stress(vals,kappa):
    vals = np.asarray(vals,float)
    c = pi_scalar(-vals,kappa)
    t = pi_scalar(vals,kappa)
    C = cf_scalar(c,kappa)
    u = ur_scalar(t,kappa)
    T = u/RHO
    U = kappa*vals - C + kappa*c + u - kappa*t
    s1 = U[0] - ACC*C[0]**2*C[1] + C[0]*T[1] - RHO*AT*T[0]*T[1]*T[1]**7
    s2 = U[1] - ACC*C[1]**2*C[0] + C[1]*T[0] - RHO*AT*T[1]*T[0]*T[0]**7
    return np.array([s1,s2])


def matfunc_sym(A,f):
    w,V = np.linalg.eigh(A)
    return V @ np.diag(f(w)) @ V.T


def sqrtm_sym(A):
    w,V = np.linalg.eigh(A)
    return V @ np.diag(np.sqrt(np.maximum(w,0.0))) @ V.T


def pi_matrix_algebraic(E, sign, kappa):
    X = sign*E
    eta = (RHO/kappa)/20.0
    A = X@X + eta*eta*np.eye(2)
    R = sqrtm_sym(A)
    return 0.5*(X@X)@(R+X)@np.linalg.inv(A)


def stress_matrix_invariant(E,kappa):
    I = np.eye(2)
    c = matfunc_sym(E, lambda x: pi_scalar(-x,kappa))
    t = matfunc_sym(E, lambda x: pi_scalar(x,kappa))
    C = kappa*c @ np.linalg.inv(I+(kappa-2)*c+c@c)
    u = matfunc_sym(t, lambda x: ur_scalar(x,kappa))
    T = u/RHO
    U = kappa*E - C + kappa*c + u - kappa*t
    T7 = np.linalg.matrix_power(T,7)
    return U - ACC*np.linalg.det(C)*C + C@(np.trace(T)*I-T) - RHO*AT*np.linalg.det(T)*(np.trace(T7)*I-T7)


def audit_case(name,d,nsamp=500,seed=20260816):
    rng=np.random.default_rng(seed+sum(map(ord,name)))
    lo,hi=d["guard"]; kappa=d["kappa"]
    e_stress=0.0; e_pi=0.0
    for _ in range(nsamp):
        vals=np.sort(rng.uniform(lo,hi,2))
        Q,_=np.linalg.qr(rng.normal(size=(2,2)))
        E=Q@np.diag(vals)@Q.T
        S=stress_matrix_invariant(E,kappa)
        Sref=Q@np.diag(scalar_principal_stress(vals,kappa))@Q.T
        e_stress=max(e_stress,float(np.linalg.norm(S-Sref,ord=np.inf)))
        for sign in (-1,+1):
            Pa=pi_matrix_algebraic(E,sign,kappa)
            Pref=matfunc_sym(E,lambda x:pi_scalar(sign*x,kappa))
            e_pi=max(e_pi,float(np.linalg.norm(Pa-Pref,ord=np.inf)))
    return e_stress,e_pi


def main():
    r1,r2,coefs=spline_exact_identity()
    print("FORMAL STRUCTURAL COUNTERS: sampling=0 quadrature=0 subdomains=1 thickness_quadrature=0")
    print("SPLINE_INTERVAL_1_TO_10_RESIDUAL =", r1)
    print("SPLINE_INTERVAL_ABOVE_10_RESIDUAL =", r2)
    print("TRUNCATED_POWER_COEFFICIENTS =", [sp.simplify(x) for x in coefs])
    for name,d in CASES.items():
        es,ep=audit_case(name,d)
        print(name,"max_matrix_stress_identity_error",es,"max_pi_algebraic_error",ep)
    print("FIXED_NONPOLYNOMIAL_ATOM_FAMILIES =", [
        "sqrt(E^2+eta^2 I)",
        "inverse(I+(kappa-2)c+c^2)",
        "positive_part_power(t/a-I), k=3..5",
        "positive_part_power(t/a-10I), k=3..5"])
    print("INDEPENDENT_T7_FIT_REQUIRED = NO")
    print("NEW_Pu = NOT_RUN")


if __name__ == "__main__":
    main()
