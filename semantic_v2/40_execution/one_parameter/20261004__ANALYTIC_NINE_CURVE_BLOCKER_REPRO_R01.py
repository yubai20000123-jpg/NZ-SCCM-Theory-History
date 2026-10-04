"""
2026-10-04 analytic one-parameter nine-curve execution scaffold.
STATUS: STOPPED BY EXACT BOTTOM-FACE LOCAL-COMPATIBILITY CONTRADICTION.

No spatial grid, no Newton, no global optimizer is used in this audit.
"""
from dataclasses import dataclass
import math

EC = 43400.0
NUC = 0.30
ES = 206000.0
NUS = 0.30
FY = 355.0
TC = 42.0
TS = 4.0
Q0 = 0.0025
N_WAVE = 4
M_WAVE = 4

@dataclass(frozen=True)
class Case:
    name: str
    b: float
    @property
    def ah(self): return 2.0*self.b
    @property
    def w0(self): return self.b*Q0
    @property
    def A0(self): return 0.225*self.b/1600.0

CASES = [
    Case("BH005",250.0), Case("BH010",500.0), Case("BH020",1000.0),
    Case("BH032",1600.0), Case("BH050",2500.0), Case("BH060",3000.0),
    Case("BH070",3500.0), Case("BH085",4250.0), Case("BH100",5000.0),
]

def kp(beta,m):
    num = (
        272*m**16 + 2856*m**14*beta**2 + 11273*m**12*beta**4
        + 23146*m**10*beta**6 + 31506*m**8*beta**8
        + 23146*m**6*beta**10 + 11273*m**4*beta**12
        + 2856*m**2*beta**14 + 272*beta**16
    )
    den = (
        m**2*beta**2*(m**2+beta**2)**2*(4*m**2+beta**2)**2
        *(m**2+4*beta**2)**2
    )
    return num/den

def steel_constants(case):
    N = N_WAVE; m = M_WAVE
    beta_star = N*case.ah/case.b
    kcr = 4*beta_star**2/m**2 + 8/3 + 4*m**2/beta_star**2
    cgl = 64*N**2*m**2/(case.ah**2*(4*N**2-1)*(4*m**2-1))
    cll = 3*math.pi**2*m**2/(2*case.ah**2)
    return beta_star, kcr, kp(beta_star,m), cgl, cll

def delta_sigma_local_elastic(case,A):
    beta_star,kcr,kp_,_,_ = steel_constants(case)
    bstar = case.b/N_WAVE
    K = math.pi**2*ES*TS**2/(12*(1-NUS**2)*bstar**2)
    return K*(kcr*A/(case.A0+A) + kp_*(1-NUS**2)*(2*case.A0*A+A*A)/TS**2)

def RA_local_only(case,w,A,s):
    # literal formula in the 2026-10-04 reply
    _,_,_,cgl,_ = steel_constants(case)
    return (
        delta_sigma_local_elastic(case,A)/ES
        - s*cgl*(case.w0*A + w*case.A0 + w*A)
    )

def bottom_no_root_certificate(case,w):
    assert w > 0
    _,_,_,cgl,_ = steel_constants(case)
    r0 = RA_local_only(case,w,0.0,-1)
    expected = cgl*w*case.A0
    assert r0 > 0 and abs(r0-expected) < 1e-15
    # For every A>0, both terms in R_- are strictly positive.
    return r0

if __name__ == "__main__":
    print("k_p(8,4) =", kp(8.0,4))
    for c in CASES:
        # choose w=0.01 b only to print a scale; proof holds for every w>0
        w = 0.01*c.b
        r0 = bottom_no_root_certificate(c,w)
        print(c.name, "b=",c.b, "A0=",c.A0, "Rminus(A=0,w=0.01b)=",r0)

    bh050 = next(c for c in CASES if c.name=="BH050")
    print("BH050 w=56.05 certificate:", bottom_no_root_certificate(bh050,56.05))
