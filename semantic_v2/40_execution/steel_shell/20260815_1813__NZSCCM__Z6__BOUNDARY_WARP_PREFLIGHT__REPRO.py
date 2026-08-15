"""NZ-SCCM Z6 boundary-compatible in-plane warp preflight.

Successful scope only:
- exact continuous admissible u,v family for Zhou loaded-edge ux=0;
- exact linear-plane-stress static condensation for N=1,3,5;
- zero-spatial finite-harmonic compatibility bookkeeping;
- Zhou Z4/Z6 base/square/a=1.25b comparator values.

The full nonlinear R10/N48 coupled Rc=Rq=0 attempt is intentionally not
implemented here because the naive generalized CH coefficient composition hit a
representation/runtime gate. See companion AUDIT and INTERMEDIATES JSON.
"""
import math

NU=0.18

def elastic_condensation(a_over_b, N, nu=NU):
    k=1.0/a_over_b
    if N==1:
        A=16*k**4-8*k*k*nu+3
        B=4*nu
    elif N==3:
        A=2*(5840*k**4-2952*k*k*nu+1215)/729
        B=40*nu/9
    elif N==5:
        A=(182511664*k**4-92395800*k*k*nu+39335625)/11390625
        B=1036*nu/225
    else:
        raise ValueError("N must be 1,3,5")
    c_over_D=B/A
    Keff_over_free=(math.pi**2-B*B/A)/(math.pi**2*(1-nu**2))
    F0_over_b=(4/math.pi**2)*sum(1/n**2 for n in range(1,N+1,2))
    side_u_ratio=c_over_D*F0_over_b/(nu/2)
    return dict(A=A,B=B,c_over_D=c_over_D,c_over_nuD=c_over_D/nu,
                Keff_over_freePoisson=Keff_over_free,
                midheight_side_u_over_freePoisson=side_u_ratio)

# Trial family, x in [0,b], y in [0,a], X=pi x/b, Y=pi y/a:
# F_N = -(4b/pi^2) sum_{odd n<=N} cos(nX)/n^2
# H_N = -(4b^2/pi^3) sum_{odd n<=N} sin(nX)/n^3 ; H_N,x=F_N
# u = eps0*c*F_N*sin^2(Y)
# v = -eps0*D*y - eps0*c*H_N*(pi/a)*sin(2Y)
# Hence u(x,0)=u(x,a)=0 exactly and u,y+v,x=0 for the added warp.
# ex,c=(4/pi)sum sin(nX)/n*sin^2Y
# ey,c=(8/pi)(b/a)^2 sum sin(nX)/n^3*cos2Y.

ES=206000.; EC=32500.; FY=355.; FCP=30.4; NUS=.30; NUC=.20; LS=200.; TS=4.
def zhou_case(a,b,h,ns):
    tc=h-2*TS
    Ac=ns*(LS-TS)*tc; As=b*h-Ac
    Pyth=FY*As+FCP*Ac
    Dx=ES*(h**3-tc**3)/12+EC*tc**3/12
    Dys=ES/b*(b*h**3/12-ns*(LS-TS)*tc**3/12)
    Dyc=EC/b*(ns*(LS-TS)*tc**3/12); Dy=Dys+Dyc
    Gs=ES/(2*(1+NUS)); Gc=EC/(2*(1+NUC))
    A0=(b-TS)*(h-TS); ids=2*((b-TS)+(h-TS))/TS
    beta=(1/3)*(1-.63*(h-2*TS)/(b-2*TS)+.052*((h-2*TS)/(b-2*TS))**5)
    Dt=(1/b)*(4*Gs*A0*A0/ids+Gc*beta*(b-2*TS)*(h-2*TS)**3)
    H=Dt/2+NUS*Dys+NUC*Dyc
    cand=[]
    for m in range(1,6):
        Pcr=b*math.pi**2*(Dx*a*a/(m*m*b**4)+2*H/b**2+Dy*m*m/a**2)
        cand.append((m,Pcr))
    m,Pcr=min(cand,key=lambda z:z[1])
    lam=math.sqrt(Pyth/Pcr)
    Phi=.454+.192*lam+.416*lam**2 if lam<=1 else -.140+1.387*lam-.186*lam**2
    phi=1 if lam<=.55 else 1/(Phi+math.sqrt(Phi**2-lam**2))
    return dict(a_over_b=a/b,m=m,Pyth_MN=Pyth/1e6,Pcr_MN=Pcr/1e6,
                lambda_n=lam,phi_lower=phi,Pu_Zhou_lower_MN=Pyth*phi/1e6,
                q0_a500_over_b=a/(500*b))

if __name__=='__main__':
    print('ELASTIC CONDENSATION')
    for r in (0.75,1.0,1.25,1.5):
        for N in (1,3,5):
            print('a/b=',r,'N=',N,elastic_condensation(r,N))
    print('\nZHOU COMPARATORS')
    cases={
      'Z4_base':(6000.,8000.,200.,40),
      'Z4_square':(8000.,8000.,200.,40),
      'Z4_a1p25b':(10000.,8000.,200.,40),
      'Z6_base':(9000.,12000.,130.,60),
      'Z6_square':(12000.,12000.,130.,60),
      'Z6_a1p25b':(15000.,12000.,130.,60),
    }
    for name,args in cases.items(): print(name,zhou_case(*args))
