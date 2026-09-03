from __future__ import annotations
import math

# BH050 frozen input
B=2500.0
a=5000.0
tc=42.0
ts=4.0
Aw=1332.0
Es=206000.0
nu_s=0.30
Ec=43400.0
nu_c=0.20
Lx=562.5
Ly=a/9.0
A0=Lx/1600.0

rho=Aw/(B*tc)
kx=2*math.pi/Lx
ky=2*math.pi/Ly
cx=3*kx*kx/8
cy=3*ky*ky/8
Ds=Es*ts**3/(12*(1-nu_s**2))

# R14 Airy
Pcr=19.581877236731064e6
q0=0.0025
C_A=10841371806.523354
Kx_A=4272925.9661361715
G_A=4400171.479082514
Jx_A=6234616.244717026
Jy_A=6298311.7090612

def P_A(q: float) -> float:
    Q=q*(q+2*q0)
    return Pcr*q/(q+q0)+C_A*Q

def r02_integrals():
    return {
        "int_phi2":9*Lx*Ly/4,
        "int_phix2":3*Lx*Ly*kx**2/4,
        "int_phiy2":3*Lx*Ly*ky**2/4,
        "int_phixx2":3*Lx*Ly*kx**4/4,
        "int_phiyy2":3*Lx*Ly*ky**4/4,
        "int_phixy2":Lx*Ly*kx**2*ky**2/4,
        "int_phixx_phiyy":Lx*Ly*kx**2*ky**2/4,
    }

def reference_C0():
    """Per-face, one-interior-bay elastic normalization only."""
    As=Lx*ts
    Ac=(1-rho)*Lx*tc
    Ks=Es*As
    Kc=Ec*Ac
    Keq=Ks*Kc/(Ks+Kc)
    C0=Keq/Ly
    return Ks,Kc,Keq,C0

def harmonic_kernel(Lambda: float, n: int=4):
    den=n*n*math.pi**2+Lambda
    eta=0.0 if Lambda==0 else Lambda/den
    slip_relief=n*n*math.pi**2/den
    return eta,slip_relief

if __name__=="__main__":
    Ks,Kc,Keq,C0=reference_C0()
    print("rho_w =",rho)
    print("kx, ky =",kx,ky)
    print("cx, cy =",cx,cy)
    print("Ds =",Ds)
    print("R02 exact integrals:")
    for k,v in r02_integrals().items():
        print(" ",k,"=",v)
    print("Ks0, Kc0, Keq0, C0 =",Ks,Kc,Keq,C0)
    print("\nLambda, C_P(MN/mm), eta4, slip_relief, ell(mm)")
    for Lam in [0,0.1,0.25,0.5,1,2,5,10,20,40,80,16*math.pi**2,200,500,1000]:
        eta,rel=harmonic_kernel(Lam,4)
        cp=Lam*C0/1e6
        ell=math.inf if Lam==0 else Ly/math.sqrt(Lam)
        print(f"{Lam:12.6f} {cp:14.6f} {eta:12.8f} {rel:12.8f} {ell:12.6f}")
    print("\nR14 P(q) reference:")
    for q in [0.00493091069216,0.005,0.0055,0.006,0.0065,0.007,0.0070257]:
        print(q,P_A(q)/1e6)
