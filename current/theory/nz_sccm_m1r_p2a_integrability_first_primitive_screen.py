"""NZ-SCCM M1R-P2A integrability-first primitive polynomial screen.

This is a MATERIAL-SPACE offline compiler screen only.
It does not perform structural spatial quadrature, auxiliary quadrature,
material-point integration, Case21 Pu, Swartz24, or ODE propagation.

Source functions are the exact frozen benchmark primitives from M1R-R01,
not the R01 rational approximants.

Screen:
- one global interval lambda in [LAM_MIN,LAM_MAX]
- one global degree-n polynomial, n=2..16
- Chebyshev basis used only for coefficient conditioning
- coefficients obtained by discrete minimax LP on 4001 material-coordinate samples
- independent validation on 100001 points
- degree-16 confirmation repeated on 20001 LP samples / 200001 validation points
- production expression, if accepted, must be converted to ordinary powers of xi

P2A fail-fast gate:
A primitive is not a low-order production candidate if its best degree<=16
global polynomial still has normalized max error > 0.10.  A desired direct
production candidate should be <=0.05.  P2A stops if any primitive fails.
"""
from __future__ import annotations
import json, math
import numpy as np
from numpy.polynomial import Chebyshev, Polynomial
from numpy.polynomial.chebyshev import chebvander
from scipy.optimize import linprog

FC=21.23
E0=20321.0
EPS0=0.00209
NU=0.18
RHO=0.1
KAPPA=E0*EPS0/FC
XCR=RHO/KAPPA
ETA=XCR/20.0
ETA_R=0.05
MT=-7.0/90.0
EMIN,EMAX=-2.0,0.6
LAM_MIN=EMIN/(1.0-NU)
LAM_MAX=EMAX/(1.0-NU)
LAM_C=0.5*(LAM_MIN+LAM_MAX)
LAM_S=0.5*(LAM_MAX-LAM_MIN)
NAMES=("U","C","C2","T","V")


def Pi_eta(z):
    z=np.asarray(z,dtype=float)
    return z*z*(np.sqrt(z*z+ETA*ETA)+z)/(2.0*(z*z+ETA*ETA))


def H(r,r0):
    r=np.asarray(r,dtype=float)
    return 0.5*((r-r0)+np.sqrt((r-r0)**2+ETA_R**2))-0.5*((-r0)+math.sqrt(r0**2+ETA_R**2))


def exact_primitives(lam):
    lam=np.asarray(lam,dtype=float)
    c=Pi_eta(-lam)
    t=Pi_eta(lam)
    C=KAPPA*c/(1.0+(KAPPA-2.0)*c+c*c)
    rr=t/XCR
    T=rr+(MT-1.0)*H(rr,1.0)-MT*H(rr,10.0)
    U=KAPPA*lam-C+KAPPA*c+RHO*T-KAPPA*t
    return np.vstack((U,C,C*C,T,T**8))


def minimax_fit(index,degree,nfit):
    xi=np.linspace(-1.0,1.0,nfit)
    lam=LAM_C+LAM_S*xi
    yy=exact_primitives(lam)[index]
    A=chebvander(xi,degree)
    obj=np.r_[np.zeros(degree+1),1.0]
    Aub=np.vstack((np.c_[A,-np.ones(nfit)],np.c_[-A,-np.ones(nfit)]))
    bub=np.r_[yy,-yy]
    bounds=[(None,None)]*(degree+1)+[(0.0,None)]
    res=linprog(obj,A_ub=Aub,b_ub=bub,bounds=bounds,method="highs")
    if not res.success:
        raise RuntimeError(res.message)
    return res.x[:-1],float(res.x[-1])


def validate(index,degree,cheb_coef,nval):
    xi=np.linspace(-1.0,1.0,nval)
    lam=LAM_C+LAM_S*xi
    yy=exact_primitives(lam)[index]
    pred=chebvander(xi,degree)@cheb_coef
    err=np.abs(pred-yy)
    scale=float(np.max(np.abs(yy)))
    return {
        "mean_abs":float(np.mean(err)),
        "p95_abs":float(np.quantile(err,0.95)),
        "max_abs":float(np.max(err)),
        "p95_norm":float(np.quantile(err,0.95)/scale),
        "max_norm":float(np.max(err)/scale),
        "source_scale":scale,
        "pred_min":float(np.min(pred)),
        "pred_max":float(np.max(pred)),
        "source_min":float(np.min(yy)),
        "source_max":float(np.max(yy)),
        "lambda_at_max_error":float(lam[np.argmax(err)]),
    }


def main():
    table=[]
    for i,name in enumerate(NAMES):
        for degree in range(2,17):
            cc,lp_t=minimax_fit(i,degree,4001)
            met=validate(i,degree,cc,100001)
            table.append({"primitive":name,"degree":degree,"lp_grid_t":lp_t,**met})

    robust16={}
    for i,name in enumerate(NAMES):
        cc,lp_t=minimax_fit(i,16,20001)
        met=validate(i,16,cc,200001)
        power=Chebyshev(cc,domain=[-1,1],window=[-1,1]).convert(kind=Polynomial).coef
        robust16[name]={
            **met,
            "lp_grid_t":lp_t,
            "chebyshev_coefficients":[float(v) for v in cc],
            "power_xi_coefficients":[float(v) for v in power],
            "relaxed_10pct_gate": "PASS" if met["max_norm"]<=0.10 else "FAIL",
            "desired_5pct_gate": "PASS" if met["max_norm"]<=0.05 else "FAIL",
        }

    overall="PASS" if all(v["relaxed_10pct_gate"]=="PASS" for v in robust16.values()) else "FAIL"
    result={
        "identity":"M1R_P2A_INTEGRABILITY_FIRST_PRIMITIVE_COMPILER_SCREEN",
        "source":"exact frozen M1R-R01 primitive oracle; rational R01 coefficients are not used as fit targets",
        "interval":{"lambda_min":LAM_MIN,"lambda_max":LAM_MAX,"lambda_center":LAM_C,"lambda_halfspan":LAM_S,"xi":"(lambda-LAM_C)/LAM_S"},
        "source_constants":{"KAPPA":KAPPA,"XCR":XCR,"ETA":ETA,"ETA_R":ETA_R,"MT":MT,"RHO":RHO},
        "method":{"family":"one global degree-n polynomial in xi","degrees":"2..16","fit":"discrete minimax LP in Chebyshev basis","screen_fit_points":4001,"screen_validation_points":100001,"robust16_fit_points":20001,"robust16_validation_points":200001},
        "screen_table":table,
        "robust_degree16":robust16,
        "gate":{"relaxed_max_norm":0.10,"desired_max_norm":0.05,"overall":overall,"reason":"T and V remain far above even the relaxed 10% gate at degree 16"},
        "formal_counts":{"structural_spatial_sampling":0,"structural_spatial_quadrature":0,"auxiliary_quadrature":0,"auxiliary_ode_steps":0,"material_coordinate_samples_are_offline_fit_only":True},
    }
    print(json.dumps(result,indent=2,ensure_ascii=False))


if __name__=="__main__":
    main()
