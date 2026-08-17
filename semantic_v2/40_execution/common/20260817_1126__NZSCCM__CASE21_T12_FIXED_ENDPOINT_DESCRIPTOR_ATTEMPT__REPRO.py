"""NZ-SCCM Case21 T12 fixed-endpoint descriptor ATTEMPT reproducer.

This script reproduces the audit-side T12 contraction and derivative checks that
were used to verify the formal target contract before the true fixed-endpoint
algebraic-period runtime was found to be absent.

IMPORTANT:
- The Gauss-Legendre executor imported from the 02:10 reproducer is AUDIT ONLY.
- This script does NOT implement the formal fixed-endpoint algebraic-period runtime.
- It therefore does NOT release a formal zero-spatial Case21 Pu.
- Formal counters remain sampling=0, quadrature=0, subdomains=1,
  thickness_quadrature=0.
"""
from pathlib import Path
import runpy
import math
import numpy as np

HERE = Path(__file__).resolve().parent
BASE = HERE / "20260817_0210__NZSCCM__CASE21_AIRY_SCALAR_CURRENT_R10_CONTINUATION__REPRO.py"
ns = runpy.run_path(str(BASE))
Oracle = ns["Oracle"]
A_AIRY = ns["A_AIRY"]

# frozen Case21 parameters from the 02:10/11:05 state
fc = ns["fc"]
E0 = ns["E0"]
eps0 = ns["eps0"]
nu = ns["nu"]
b = ns["b"]
ell = ns["ell"]
tp = ns["tp"]
q0 = ns["q0"]
Es = ns["Es"]
rsx = ns["rsx"]
rsy = ns["rsy"]

D = 0.7887924801
q = 0.0018083572562965242
lam = 0.08623596353826937


def M_of(qv):
    return math.pi**2/eps0*(q0*qv + 0.5*qv*qv)


def T12_from_oracle(oracle, Dv, qv, lv):
    """Compute the 12 structural target functionals from direct-source stresses.

    This is audit-only numerical quadrature, not the formal production map.
    """
    M = M_of(qv)
    r = lv*M*A_AIRY
    ex, ey, g, _, _ = oracle.kin(Dv, qv, r, True)
    sx, sy, txy = ns["global_stress"](ex, ey, g)
    X = oracle.X3
    Y = oracle.Y3
    Z = oracle.Z3
    W = oracle.W3

    c2x = np.cos(2*X); c2y = np.cos(2*Y)
    c22 = c2x*c2y
    s22 = np.sin(2*X)*np.sin(2*Y)
    s11 = np.sin(X)*np.sin(Y)
    c11 = np.cos(X)*np.cos(Y)

    def I(arr):
        return float(np.sum(arr*W))

    return np.array([
        I(sx), I(sx*c2x), I(sx*c2y), I(sx*c22),
        I(sy), I(sy*c2x), I(sy*c2y), I(sy*c22),
        I(txy*s22),
        I(Z*sx*s11), I(Z*sy*s11), I(Z*txy*c11)
    ], float)


def contract(T, Dv, qv, lv):
    Jx00,Jx20,Jx02,Jx22c,Jy00,Jy20,Jy02,Jy22c,Jxy22s,Jx11,Jy11,Jxy11 = T
    M = M_of(qv)
    Mq = math.pi**2/eps0*(q0+qv)
    Bq = math.pi**2/(2*eps0)*(tp/b)
    Cvol = eps0*b*ell*tp/(2*math.pi**2)/1000.0

    Pc = -b*tp/(2*math.pi**2)*Jy00/1000.0
    RAc = Cvol*(-(1+nu)*Jx00/4 -(1-nu)*Jx20/4 +Jx22c/4
                -(1-nu)*Jy02/4 +Jy22c/4 -Jxy22s/2)
    F0 = (Jx00+Jx20-Jx02-Jx22c + Jy00-Jy20+Jy02-Jy22c + 2*Jxy22s)
    F1 = Jx11 + Jy11 - 2*Jxy11
    Rqc = Cvol*(Mq*F0/4 + Bq*F1)

    Cs = rsy*tp*b*Es*eps0/1000.0
    CR = rsy*Es*eps0**2*b*ell*tp/(32*1000.0)
    Ps = Cs*(Dv-M/4)
    RAs = -CR*(8*Dv*nu*(nu+1)+M*(5-(4*nu**2+5)*lv))
    Rqs = CR*Mq*(8*Dv*(nu-1)+M*(9-5*lv))
    return np.array([Pc+Ps, Rqc+Rqs, RAc+RAs], float)


def fd_T12(oracle, Dv, qv, lv, var, h):
    p=[Dv,qv,lv]; m=[Dv,qv,lv]
    idx={"D":0,"q":1,"lambda":2}[var]
    p[idx]+=h; m[idx]-=h
    return (T12_from_oracle(oracle,*p)-T12_from_oracle(oracle,*m))/(2*h)


def main():
    print("CURRENT_END_TO_END_TASK=CASE21_AIRY_SCALAR_FORMAL_ZERO_SPATIAL_ULTIMATE_LOAD")
    print("FORMAL_COUNTERS sampling=0 quadrature=0 subdomains=1 thickness_quadrature=0")
    print("AUDIT_GRID_BELOW_DOES_NOT_CHANGE_FORMAL_COUNTERS")

    oracle=Oracle(128,68)
    T=T12_from_oracle(oracle,D,q,lam)
    print("T12_AUDIT",T.tolist())
    y=contract(T,D,q,lam)
    print("CONTRACTED_AUDIT_P_Rq_RA",y.tolist())

    dD=fd_T12(oracle,D,q,lam,"D",1e-6)
    dq=fd_T12(oracle,D,q,lam,"q",1e-8)
    dl=fd_T12(oracle,D,q,lam,"lambda",1e-5)
    print("dT12_dD",dD.tolist())
    print("dT12_dq",dq.tolist())
    print("dT12_dlambda",dl.tolist())

    # Structural finite-difference Jacobian from the T12 contract + exact steel package.
    def F(Dv,qv,lv):
        return contract(T12_from_oracle(oracle,Dv,qv,lv),Dv,qv,lv)
    cols=[]
    for idx,h in [(0,1e-6),(1,1e-8),(2,1e-5)]:
        p=[D,q,lam]; m=[D,q,lam]; p[idx]+=h; m[idx]-=h
        cols.append((F(*p)-F(*m))/(2*h))
    J=np.column_stack(cols)
    print("JACOBIAN_P_Rq_RA_by_D_q_lambda",J.tolist())
    rhs=-J[1:,0]
    dqD,dlD=np.linalg.solve(J[1:,1:],rhs)
    dPD=J[0,0]+J[0,1]*dqD+J[0,2]*dlD
    print("BRANCH_DERIVATIVES",dict(dq_dD=float(dqD),dlambda_dD=float(dlD),dP_dD_kN=float(dPD)))

    print("FORMAL_FIXED_ENDPOINT_ALGEBRAIC_PERIOD_NUMERIC_RUNTIME=NOT_IMPLEMENTED")
    print("FORMAL_CASE21_Pu=NOT_RELEASED")

if __name__=="__main__":
    main()
