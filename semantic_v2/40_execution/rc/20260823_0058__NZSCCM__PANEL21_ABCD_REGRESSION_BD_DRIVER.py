from __future__ import annotations
from pathlib import Path
import importlib.util
import numpy as np
from scipy.optimize import root

HERE = Path(__file__).resolve().parent
M6_PATH = HERE / "20260822_2130__NZSCCM__NC_M6_2D_TC_CRACK_FRONT_EXACT_SECTION.py"
spec = importlib.util.spec_from_file_location("m6_regression", M6_PATH)
m6 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(m6)
base = m6.base
NU, ES = m6.NU, m6.ES
PANEL = base.PANELS[21]

# Nguyen p is nominal total two-way steel ratio: each direction receives p/2.
def corrected_rc_stiffness(panel):
    t,E0,p = panel["t"],panel["E0"],panel["p"]
    z=panel["z"]; L=len(z); rho=0.5*p
    ax=[rho*t/L]*L; ay=[rho*t/L]*L
    Q=E0/(1-NU**2); Q12=NU*E0/(1-NU**2); Q66=E0/(2*(1+NU))
    tc=t-sum(np.asarray(ax)+np.asarray(ay))
    A11=Q*tc+ES*sum(ax); A22=Q*tc+ES*sum(ay); A12=Q12*tc; A66=Q66*tc
    Ieff=t**3/12-sum((ax[i]+ay[i])*z[i]**2 for i in range(L))
    Dx=Q*Ieff+ES*sum(ax[i]*z[i]**2 for i in range(L)); Dy=Q*Ieff+ES*sum(ay[i]*z[i]**2 for i in range(L))
    Dmu=Q12*Ieff; D66=Q66*Ieff; H=Dmu+2*D66
    return locals()
base.rc_stiffness = corrected_rc_stiffness

def solve(c,u,seed):
    op=base.build_wave_operator(PANEL,np.asarray(c,float))
    fun=lambda X:m6.fold_system(X,op,u)
    sol=root(fun,np.asarray(seed,float),options={"xtol":1e-11,"maxfev":5000})
    if (not sol.success) or np.linalg.norm(fun(sol.x))>1e-6:
        raise RuntimeError((sol.message,np.linalg.norm(fun(sol.x))))
    P=base.resultants(op,float(sol.x[4]),1.0,u)["P"]/1000.0
    return op,sol.x,P,float(np.linalg.norm(fun(sol.x)))

def main():
    print("FORMAL_SPATIAL_QUADRATURE=0")
    print("FORMAL_MATERIAL_POINTS=0")
    print("Pf_IN_SOLVE=0")
    print("RHO_DIRECTION=",0.5*PANEL["p"])

    # D: corrected source-wave NC-M6/F03 local fold; must reproduce 173.209915 kN.
    opD,XD,PD,nD=solve(base.PHI_COEFF[21],0.3559087784,[0.04969829,-0.16734044,-0.01614820,-0.01115785,0.001347589965])
    print("D_SOURCE",XD[4],PD,nD,opD["Pcr"]/1000.0,opD["C"]/1000.0)

    # B: same material/input/criterion, but ideal pure n=2 shape = two equal 1220-mm halfwaves.
    cB=np.array([0.0,-1.0])
    opB,XB,PB,nB=solve(cB,0.25,[0.05067677,-0.15418355,-0.01680982,-0.00778703,0.001531925676])
    print("B_M2",XB[4],PB,nB,opB["Pcr"]/1000.0,opB["C"]/1000.0)
    for u in (0.245,0.250,0.255,0.750):
        _,X,P,n=solve(cB,u,XB)
        print("B_SYMMETRY",u,X[4],P,n)

if __name__ == "__main__":
    main()
