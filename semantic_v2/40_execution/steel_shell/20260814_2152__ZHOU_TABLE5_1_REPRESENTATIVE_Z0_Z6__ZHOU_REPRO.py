from math import pi, sqrt

Es = 206000.0

cases = [
    ("Z0",30,200,130,4,355,40,6000,6000),
    ("Z1",30,200,100,4,235,40,6000,6000),
    ("Z2",30,200,130,4,460,40,6000,6000),
    ("Z3",30,200,130,4,355,60,6000,6000),
    ("Z4",40,200,200,4,355,40,6000,8000),
    ("Z5",10,200,130,4,355,40,3000,2000),
    ("Z6",60,200,130,4,355,40,9000,12000),
]

def Ec_from_source(fcu):
    # Existing project checkpoint uses Zhou's rounded C40 value 32500 MPa.
    if fcu == 40:
        return 32500.0
    # Zhou Eq. (2-7) for other strengths.
    return 1e5/(34.7/fcu + 2.2)

def calc(case):
    name,ns,ls,h,ts,fy,fcu,a,b = case
    Ec = Ec_from_source(fcu)
    fc = 0.76*fcu
    tc = h-2*ts
    Ac = b*tc
    As = 2*b*ts
    Pc0 = fc*Ac/1e6
    Ps0 = fy*As/1e6
    Pyth = Pc0+Ps0

    # Reduced concrete + two outer faceplate E*I, per unit width.
    Ic = tc**3/12.0
    Is = (h**3-tc**3)/12.0
    DEI = Ec*Ic + Es*Is

    # Same reduced isotropic diagnostic degeneration of the Zhou/Navier elastic formula.
    candidates=[]
    for m in range(1,51):
        alpha=pi/b
        beta=m*pi/a
        Ncr=DEI*(alpha**2+beta**2)**2/beta**2
        Pcr=Ncr*b/1e6
        candidates.append((Pcr,m))
    Pcr,m=min(candidates)
    ell=a/m

    lam=sqrt(Pyth/Pcr)
    if lam <= 1.0:
        Phi=0.454+0.192*lam+0.416*lam**2
    else:
        Phi=-0.140+1.387*lam-0.186*lam**2
    if lam <= 0.55:
        phi=1.0
    else:
        phi=1.0/(Phi+sqrt(Phi**2-lam**2))
    Pu=phi*Pyth
    return name,Pyth,DEI,m,ell,Pcr,lam,Phi,phi,Pu

for c in cases:
    print(calc(c))

# IMPORTANT: This script intentionally does NOT generate missing NZ-SCCM Pu values.
# Z1-Z6 require the actual NZ-SCCM R10->N48-C1/MM->CH->Nguyen->D15 connected D-q calculation.
# Cross-case scaling from Z0 is prohibited.
