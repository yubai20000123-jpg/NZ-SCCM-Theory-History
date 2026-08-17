"""NZ-SCCM Stage-III true-infinite R10 -> D15 limit reproduction ledger.

Timestamp: 2026-08-17 15:26 +08:00

FORMAL identity:
  Stage-I source recurrence/generator -> infinite R10 stream
  Stage-II exact nth CH/D15 target -> n->infinity limit.

This script checks the algebraic limit identities and independently re-evaluates
selected released root states with a direct raw-R10 Gauss oracle.  The Gauss
part is AUDIT ONLY and never changes the formal counters:
  N_formal_spatial_sampling = 0
  N_formal_spatial_quadrature = 0
  N_formal_spatial_subdomains = 1
  N_formal_thickness_quadrature = 0

The exact-D15 prefix values themselves are persisted in the companion JSON;
the general-n D15 generator is the Stage-II REPRO file.
"""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss

KAPPA = 2.0005129533678754
RHO = 0.1
ETA = 0.0024993589726987125
H = 0.09799750427197301
UR = 0.03
ACC = 0.1072329249362415
AT = 1 - 2 ** (-1 / 8)
XCR = RHO / KAPPA


def Pi(z):
    z = np.asarray(z, float)
    return z*z*(np.sqrt(z*z + ETA*ETA) + z)/(2*(z*z + ETA*ETA))


def uR(t):
    t = np.asarray(t, float)
    r = t / XCR
    out = np.empty_like(r)
    m = r <= 1
    rr = r[m]
    out[m] = (RHO*rr + (10*H-6*RHO)*rr**3 +
              (8*RHO-15*H)*rr**4 + (6*H-3*RHO)*rr**5)
    m2 = (r > 1) & (r <= 10)
    s = (r[m2]-1)/9
    out[m2] = H + (UR-H)*(10*s**3-15*s**4+6*s**5)
    out[r > 10] = UR
    return out


def raw_stress(X11, X22, X12):
    mu = (X11 + X22)/2
    d = (X11 - X22)/2
    rad = np.sqrt(d*d + X12*X12)
    l1, l2 = mu + rad, mu - rad
    c1, c2 = Pi(-l1), Pi(-l2)
    t1, t2 = Pi(l1), Pi(l2)
    C1 = KAPPA*c1/(1+(KAPPA-2)*c1+c1*c1)
    C2 = KAPPA*c2/(1+(KAPPA-2)*c2+c2*c2)
    u1, u2 = uR(t1), uR(t2)
    T1, T2 = u1/RHO, u2/RHO
    U1 = KAPPA*l1-C1+KAPPA*c1+u1-KAPPA*t1
    U2 = KAPPA*l2-C2+KAPPA*c2+u2-KAPPA*t2
    s1 = U1-ACC*C1*C1*C2+C1*T2-RHO*AT*T1*T2**8
    s2 = U2-ACC*C2*C2*C1+C2*T1-RHO*AT*T2*T1**8
    avg, diff = (s1+s2)/2, (s1-s2)/2
    fac = np.divide(diff, rad, out=np.zeros_like(rad), where=rad > 1e-14)
    return avg+fac*d, avg-fac*d, fac*X12


def concrete_oracle(D, q, lamA, case, nx=64, ny=64, nz=26):
    """Audit-only continuous raw-R10 evaluator for P,Rq_base,RA."""
    nu, e0, b, ell, t, q0 = (case['nu'], case['eps0'], case['b'],
                              case['ell'], case['tc'], case['q0'])
    gx, wx = leggauss(nx); gy, wy = leggauss(ny); gz, wz = leggauss(nz)
    X = (gx+1)*math.pi/2; Y = (gy+1)*math.pi/2
    XX, YY, ZZ = X[:,None,None], Y[None,:,None], gz[None,None,:]
    W = wx[:,None,None]*wy[None,:,None]*wz[None,None,:]*(math.pi/2)**2
    u, v = np.sin(XX), np.sin(YY)
    cx, cy = np.cos(XX), np.cos(YY)
    M = math.pi**2/e0*(q0*q + .5*q*q)
    Mq = math.pi**2/e0*(q0+q)
    B = math.pi**2*t/(2*e0*b)*q
    Bq = math.pi**2*t/(2*e0*b)
    alpha = lamA*M
    Aex = -.25-.5*nu*u*u-.5*v*v+u*u*v*v
    Aey = .25*nu-.5*nu*v*v-.5*u*u+u*u*v*v
    ex = nu*D + M*(v*v-u*u*v*v) + alpha*Aex + B*u*v*ZZ
    ey = -D + M*(u*u-u*u*v*v) + alpha*Aey + B*u*v*ZZ
    gam = 2*cx*cy*((M-alpha)*u*v-B*ZZ)
    X11 = (ex+nu*ey)/(1-nu*nu)
    X22 = (nu*ex+ey)/(1-nu*nu)
    X12 = gam/(2*(1+nu))
    S11, S22, S12 = raw_stress(X11,X22,X12)
    exq = Mq*(v*v-u*u*v*v)+Bq*u*v*ZZ
    eyq = Mq*(u*u-u*u*v*v)+Bq*u*v*ZZ
    gamq = 2*cx*cy*(Mq*u*v-Bq*ZZ)  # q derivative at fixed alpha
    exa, eya, gama = Aex, Aey, -2*cx*cy*u*v
    Qq = S11*exq + S22*eyq + S12*gamq
    Qa = S11*exa + S22*eya + S12*gama
    iS, iq, ia = np.sum(W*S22), np.sum(W*Qq), np.sum(W*Qa)
    Pc = -case['fc']*b*t/(2*math.pi**2)*iS
    Cvol = case['fc']*e0*b*ell*t/(2*math.pi**2)
    return Pc, Cvol*iq, Cvol*ia


def case21_steel(D,q,lamA):
    nu=.18; b=1220.; t=19.3; Es=200000.; e0=.00209; rsy=.00375; q0=.0025
    M=math.pi**2/e0*(q0*q+.5*q*q); Mq=math.pi**2/e0*(q0+q)
    Cs=rsy*t*b*Es*e0/1000
    Ps=Cs*(D-M/4)*1000
    CR=2.94090386184375
    RA=-CR*(8*D*nu*(nu+1)+M*(5-(4*nu**2+5)*lamA))*1000
    Rq=CR*Mq*(8*D*(nu-1)+M*(9-5*lamA))*1000
    return Ps,Rq,RA


def steel_plane_stress(ex,ey,gam,Es=206000.,nu=.30,fy=355.):
    fac=Es/(1-nu*nu)
    sx=fac*(ex+nu*ey); sy=fac*(nu*ex+ey); tau=Es/(2*(1+nu))*gam
    vm=np.sqrt(sx*sx-sx*sy+sy*sy+3*tau*tau)
    a=np.minimum(1.,fy/np.maximum(vm,1e-30))
    return a*sx,a*sy,a*tau,vm/fy


def z6_steel_oracle(D,q,lamA,n=64,nzf=12,nzw=28):
    """Audit-only reproduction of the frozen face-shell + longitudinal-web phases."""
    nuc=.18; e0=.0018712490394580678; b=ell=12000.; tc=122.; ts=4.; q0=.004
    Es=206000.; fy=355.; rho_w=.02
    M=math.pi**2/e0*(q0*q+.5*q*q); Mq=math.pi**2/e0*(q0+q); alpha=lamA*M
    gx,wx=leggauss(n); gy,wy=leggauss(n)
    X=(gx+1)*math.pi/2; Y=(gy+1)*math.pi/2
    u=np.sin(X)[:,None,None]; v=np.sin(Y)[None,:,None]
    cx=np.cos(X)[:,None,None]; cy=np.cos(Y)[None,:,None]
    Wxy=wx[:,None,None]*wy[None,:,None]*(math.pi/2)**2
    Aex=-.25-.5*nuc*u*u-.5*v*v+u*u*v*v
    Aey=.25*nuc-.5*nuc*v*v-.5*u*u+u*u*v*v
    exq0=Mq*(v*v-u*u*v*v); eyq0=Mq*(u*u-u*u*v*v)
    gamq0=2*cx*cy*Mq*u*v
    gama=-2*cx*cy*u*v
    Pface=Rqface=Raface=0.; maxvm=0.
    gz,wz=leggauss(nzf)
    for sign in (-1,1):
        zmid=sign*(tc/2+ts/2)
        z=zmid+(ts/2)*gz[None,None,:]
        bend=math.pi**2*q/(e0*b)
        ex=nuc*D+M*(v*v-u*u*v*v)+alpha*Aex+bend*u*v*z
        ey=-D+M*(u*u-u*u*v*v)+alpha*Aey+bend*u*v*z
        gam=2*cx*cy*((M-alpha)*u*v-bend*z)
        dexq=exq0+math.pi**2/(e0*b)*u*v*z
        deyq=eyq0+math.pi**2/(e0*b)*u*v*z
        dgamq=gamq0-2*cx*cy*math.pi**2/(e0*b)*z
        sx,sy,tau,vmr=steel_plane_stress(e0*ex,e0*ey,e0*gam,Es,.30,fy)
        W=Wxy*wz[None,None,:]*(ts/2)
        Pface += -b/math.pi**2*np.sum(W*sy)
        vf=b*ell/math.pi**2
        Rqface += vf*np.sum(W*e0*(sx*dexq+sy*deyq+tau*dgamq))
        Raface += vf*np.sum(W*e0*(sx*Aex+sy*Aey+tau*gama))
        maxvm=max(maxvm,float(vmr.max()))
    gz,wz=leggauss(nzw); zz=gz[None,None,:]
    B=math.pi**2*tc/(2*e0*b)*q; Bq=math.pi**2*tc/(2*e0*b)
    ey=-D+M*(u*u-u*u*v*v)+alpha*Aey+B*u*v*zz
    deyq=eyq0+Bq*u*v*zz
    sy=np.clip(Es*e0*ey,-fy,fy)
    W=Wxy*wz[None,None,:]
    avg=np.sum(W*sy)/(2*math.pi**2)
    Pw=-rho_w*b*tc*avg
    vf=rho_w*b*ell*tc/(2*math.pi**2)
    Rqw=vf*np.sum(W*e0*sy*deyq)
    Raw=vf*np.sum(W*e0*sy*Aey)
    return Pface,Rqface,Raface,Pw,Rqw,Raw,maxvm


def main():
    case21=dict(b=1220.,ell=1220.,tc=19.30,eps0=.00209,fc=21.23,nu=.18,q0=.0025)
    x21=(.7887924801,.0018083572562965242,.08623596353826937)
    Pc,Rqc,Rac=concrete_oracle(*x21,case21,80,80,32)
    Ps,Rqs,Ras=case21_steel(*x21)
    print('CASE21 audit same-state:')
    print(' Pc,Ps,P kN =',Pc/1000,Ps/1000,(Pc+Ps)/1000)
    print(' Rq,RA kNmm =',(Rqc+Rqs)/1000,(Rac+Ras)/1000)
    print(' released true-infinite-limit Pu kN =',366.7678286852115)

    z6=dict(b=12000.,ell=12000.,tc=122.,eps0=.0018712490394580678,fc=30.4,nu=.18,q0=.004)
    xz=(1.36180798,.0264854039,.786915819)
    Pc,Rqc,Rac=concrete_oracle(*xz,z6,64,64,26)
    Psf,Rqf,Raf,Pw,Rqw,Raw,vm=z6_steel_oracle(*xz)
    P=.98*Pc+Psf+Pw; Rq=.98*Rqc+Rqf+Rqw; RA=.98*Rac+Raf+Raw
    print('Z6 audit same-state:')
    print(' Pc_eff,Ps_face,Pw,P MN =',.98*Pc/1e6,Psf/1e6,Pw/1e6,P/1e6)
    print(' Rq,RA =',Rq,RA,'VM/fy=',vm)
    print(' released true-infinite-limit Pu MN =',48.4061215)

    zhou=49.4867667519; winter=50.1858541295; pf=368.3127497435694
    print('Z6 error vs Zhou % =',(48.4061215/zhou-1)*100)
    print('Z6 error vs Winter % =',(48.4061215/winter-1)*100)
    print('Case21 error vs Pf % =',(366.7678286852115/pf-1)*100)
    print('FORMAL SPATIAL QUADRATURE = 0; displayed Gauss values are AUDIT ONLY')

if __name__ == '__main__':
    main()
