"""
R02 mean-compatibility repair root audit.
This is an elastic-predictor/root-existence audit only.
It does NOT accept states whose combined Mises exceeds fy.
"""
from dataclasses import dataclass
from math import pi
from scipy.optimize import brentq

EC=43400.0
NUC=0.30
ES=206000.0
NUS=0.30
TC=42.0
TS=4.0
Q0=0.0025
N=4
M=4

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

CASES=[
    Case("BH005",250.0),Case("BH010",500.0),Case("BH020",1000.0),
    Case("BH032",1600.0),Case("BH050",2500.0),Case("BH060",3000.0),
    Case("BH070",3500.0),Case("BH085",4250.0),Case("BH100",5000.0),
]

def kp(beta,m):
    num=(272*m**16+2856*m**14*beta**2+11273*m**12*beta**4+
         23146*m**10*beta**6+31506*m**8*beta**8+
         23146*m**6*beta**10+11273*m**4*beta**12+
         2856*m**2*beta**14+272*beta**16)
    den=(m**2*beta**2*(m**2+beta**2)**2*
         (4*m**2+beta**2)**2*(m**2+4*beta**2)**2)
    return num/den

KP=kp(8.0,4)

def cgl(c):
    return 64*N**2*M**2/(c.ah**2*(4*N**2-1)*(4*M**2-1))

def kcr(c):
    beta_star=N*c.ah/c.b
    return 4*beta_star**2/M**2 + 8/3 + 4*M**2/beta_star**2

def NyE(c,w):
    alpha=pi/c.b
    beta=pi/c.ah
    D0=EC*TC**3/(12*(1-NUC**2))
    QE=w*w+2*c.w0*w
    return (D0*((alpha*alpha+beta*beta)**2/beta**2)*w/(c.w0+w)
            +EC*TC/16*((alpha**4+beta**4)/beta**2)*QE)

def eU(c,w,s):
    # Compression-positive area-average surface axial strain
    # from the current elastic Airy trial field.
    return NyE(c,w)/(EC*TC) - s*(2*TC*w/c.ah**2)

def sigma_yun_E(c,A):
    bstar=c.b/N
    K=pi**2*ES*TS**2/(12*(1-NUS**2)*bstar**2)
    return K*(kcr(c)*A/(c.A0+A)
              +KP*(1-NUS**2)*(2*c.A0*A+A*A)/TS**2)

def RA_E(c,w,A,s):
    return (sigma_yun_E(c,A)/ES
            -eU(c,w,s)
            -s*cgl(c)*(c.w0*A+w*c.A0+w*A))

def first_nonnegative_root(c,w,s):
    f0=RA_E(c,w,0.0,s)
    if f0==0.0:
        return 0.0
    hi=max(0.01,0.001*c.b)
    for _ in range(80):
        fh=RA_E(c,w,hi,s)
        if f0*fh<=0:
            return brentq(lambda A:RA_E(c,w,A,s),0.0,hi,xtol=1e-13)
        hi*=2.0
    raise RuntimeError(f"no bracket: {c.name}, w={w}, s={s}")

def audit():
    print("kp(8,4) =",KP)
    print("kcr =",kcr(CASES[0]))
    for q in (0.001,0.005,0.010,0.020):
        print("\nq =",q)
        for c in CASES:
            w=q*c.b
            ap=first_nonnegative_root(c,w,+1)
            am=first_nonnegative_root(c,w,-1)
            print(c.name, f"A+={ap:.10f}", f"A-={am:.10f}",
                  f"RA+={RA_E(c,w,ap,+1):+.3e}",
                  f"RA-={RA_E(c,w,am,-1):+.3e}")
    c=next(c for c in CASES if c.name=="BH050")
    w=56.05
    ap=first_nonnegative_root(c,w,+1)
    am=first_nonnegative_root(c,w,-1)
    print("\nBH050 w=56.05")
    print("A+ =",ap,"sigmaY+ =",sigma_yun_E(c,ap))
    print("A- =",am,"sigmaY- =",sigma_yun_E(c,am))
    print("NOTE: these stresses exceed fy=355 MPa; combined-Mises corrector is mandatory.")

if __name__=="__main__":
    audit()
