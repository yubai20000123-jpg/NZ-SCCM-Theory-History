import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import least_squares

# ---------------- frozen BH050 inputs ----------------
a,b,tc,ts,Aw,A0g=5000.,2500.,42.,4.,1332.,6.25
Es,nus,fy=206000.,0.3,355.
Ec,fc,ec0=43400.,141.1,.0035
m=2; q0=A0g/b; rho=Aw/(b*tc); zf=(tc+ts)/2
al=np.pi/b; be=m*np.pi/a; Qs=Es/(1-nus**2); Gs=Es/(2*(1+nus))
L=a/m; Lx=562.5; A0l=.3515625
strips_top=[(3,.225),(4,.225),(5,.225),(6,.325)]
strips_bot=[(3,.225),(4,.45),(5,.225),(20,.10)]

# ---------------- unchanged UHPC-U0 scalar principal law ----------------
etu,ftp=.00759,10.734818
rkn=np.array([0.,.055335968379,.500658761528,.909090909091,1.])
coef=np.array([[0.,1.698025993547,-.695943390615,-.092172625884],
 [.909909977049,.238381217069,-.206492365284,.058201171166],
 [1.,0.,-.017806150057,-.018229859124],
 [.963963990819,-.020099450150,-2.851693072159,1.907828531489]])
Ac=Ec*ec0/fc; Bc=6-5*Ac; Cc=4*Ac-5

def uhpc_sig_scalar(e):
    e=np.asarray(e); out=np.empty_like(e,dtype=float)
    if np.any(e < -ec0) or np.any(e > etu):
        return None
    neg=e<0
    en=e[neg]
    out[neg]=Ec*en+fc*Bc*en**5/ec0**5-fc*Cc*en**6/ec0**6
    ep=e[~neg]; xi=ep/etu; val=np.zeros_like(ep)
    for j in range(4):
        lo,hi=rkn[j],rkn[j+1]
        take=(xi>=lo)&((xi<=hi) if j==3 else (xi<hi))
        if np.any(take):
            th=(xi[take]-lo)/(hi-lo); c=coef[j]
            val[take]=ftp*(c[0]+c[1]*th+c[2]*th**2+c[3]*th**3)
    out[~neg]=val
    return out

def uhpc_stress(ex,ey,ga):
    # spectral derivative of phi(e1)+phi(e2), engineering shear convention
    av=.5*(ex+ey); d=.5*(ex-ey); h=.5*ga
    rad=np.hypot(d,h)
    e1=av+rad; e2=av-rad
    ss=uhpc_sig_scalar(np.array([e1,e2]))
    if ss is None: return None
    s1,s2=ss
    if rad < 1e-14:
        sx=sy=.5*(s1+s2); tau=0.
    else:
        c2=d/rad; s2ang=h/rad
        sx=.5*(s1+s2)+.5*(s1-s2)*c2
        sy=.5*(s1+s2)-.5*(s1-s2)*c2
        tau=.5*(s1-s2)*s2ang
    return sx,sy,tau,e1,e2

def steel_sig_scalar(e):
    eyld=fy/Es
    if e > eyld: return fy
    if e < -eyld: return -fy
    return Es*e

# ---------------- frozen qU-off R02 condensation, now retaining macro shear ----------------
def strip_state(ex,ey,ga,n):
    Ly=L/n; kx=2*np.pi/Lx; ky=2*np.pi/Ly
    cx=3*kx*kx/8; cy=3*ky*ky/8
    Ds=Es*ts**3/(12*(1-nus**2))
    Kb=Ds*(.75*(kx**4+ky**4)+.5*kx*kx*ky*ky)
    KA=kx**4*ky**4*(17/(256*ky**4)+17/(256*kx**4)+1/(8*(kx*kx+ky*ky)**2)+1/(32*(kx*kx+4*ky*ky)**2)+1/(32*(4*kx*kx+ky*ky)**2))
    Cg=Qs*(cx*cx+cy*cy+2*nus*cx*cy)
    B3=4*ts*Es*KA+2*ts*Cg
    B1=Kb-A0l*A0l*B3+2*ts*Qs*((cx+nus*cy)*ex+(cy+nus*cx)*ey)
    roots=np.roots([B3,0,B1,-A0l*Kb])
    cand=[0.]+[z.real for z in roots if abs(z.imag)<1e-8 and z.real>=0]
    vals=[]
    for U in cand:
        dd=U*U-A0l*A0l; mx=ex+cx*dd; my=ey+cy*dd
        pi=.5*Kb*(U-A0l)**2+.5*ts*Qs*(mx*mx+my*my+2*nus*mx*my)+.5*ts*Gs*ga*ga+ts*Es*KA*dd*dd
        vals.append(pi)
    U=cand[int(np.argmin(vals))]
    dd=U*U-A0l*A0l
    sx=Qs*(ex+nus*ey+(cx+nus*cy)*dd)
    sy=Qs*(ey+nus*ex+(cy+nus*cx)*dd)
    tau=Gs*ga
    return U,sx,sy,tau

# ---------------- full-length M1 kinematics ----------------
def kin(lam,exbar,rmode,q,x,y):
    # rmode = beta*qv1, with qv1 sign defined in centered-x audit coordinate xc=x-b/2.
    # cos(2*pi*xc/b)=-cos(2*alpha*x), hence v=-lambda*y-(rmode/beta)sin(beta y)cos(2alpha x).
    sx,cx=np.sin(al*x),np.cos(al*x); sy,cy=np.sin(be*y),np.cos(be*y)
    c2=np.cos(2*al*x); s2=np.sin(2*al*x)
    Q=q*q+2*q0*q; dQ=2*(q+q0)
    ex=exbar+.5*b*b*al*al*Q*cx*cx*sy*sy
    ey=-lam-rmode*cy*c2+.5*b*b*be*be*Q*sx*sx*cy*cy
    ga=(2*al/be)*rmode*sy*s2+b*b*al*be*Q*sx*cx*sy*cy
    kx=b*q*al*al*sx*sy; ky=b*q*be*be*sx*sy; kxy=-2*b*q*al*be*cx*cy
    de_q=np.array([.5*b*b*al*al*dQ*cx*cx*sy*sy,
                   .5*b*b*be*be*dQ*sx*sx*cy*cy,
                   b*b*al*be*dQ*sx*cx*sy*cy,
                   b*al*al*sx*sy,b*be*be*sx*sy,-2*b*al*be*cx*cy])
    de_r=np.array([0.,-cy*c2,(2*al/be)*sy*s2,0.,0.,0.])
    return np.array([ex,ey,ga,kx,ky,kxy]),de_r,de_q

# Diagnostic Gaussian evaluation only, not formal zero-quadrature theory.
NG=9
gx,gw=leggauss(NG); gz,zw=leggauss(NG)
X=(gx+1)*b/2; Y=(gx+1)*a/2; Z=gz*tc/2
WX=gw*b/2; WY=gw*a/2; WZ=zw*tc/2
AREA=a*b

def section_forward(e):
    ex,ey,ga,kx,ky,kxy=e
    Nx=Ny=Nxy=Mx=My=Mxy=0.
    minp=1e9; maxp=-1e9; maxvm=0.; umax=0.
    # UHPC thickness
    for z,wz in zip(Z,WZ):
        st=uhpc_stress(ex+z*kx,ey+z*ky,ga+z*kxy)
        if st is None: return None
        sx,sy,tau,e1,e2=st
        fac=(1-rho)*wz
        Nx+=fac*sx; Ny+=fac*sy; Nxy+=fac*tau
        Mx+=fac*sx*z; My+=fac*sy*z; Mxy+=fac*tau*z
        minp=min(minp,e1,e2); maxp=max(maxp,e1,e2)
    # two steel faces, Multiwave R02 current response
    for strips,z in ((strips_top,zf),(strips_bot,-zf)):
        exs=ex+z*kx; eys=ey+z*ky; gas=ga+z*kxy
        fx=fy_=ft=0.
        for n,wt in strips:
            U,sx,sy,tau=strip_state(exs,eys,gas,n)
            fx+=wt*ts*sx; fy_+=wt*ts*sy; ft+=wt*ts*tau
            umax=max(umax,U)
            maxvm=max(maxvm,np.sqrt(sx*sx-sx*sy+sy*sy+3*tau*tau))
        Nx+=fx; Ny+=fy_; Nxy+=ft
        Mx+=z*fx; My+=z*fy_; Mxy+=z*ft
    # PBL web distributed through core depth: unchanged axial-only surrogate from prior U0 diagnostic
    for z,wz in zip(Z,WZ):
        sy=steel_sig_scalar(ey+z*ky)
        fac=rho*wz
        Ny+=fac*sy; My+=fac*sy*z
    return np.array([Nx,Ny,Nxy,Mx,My,Mxy]),minp,maxp,maxvm,umax

def evaluate(lam,y,diag=False):
    exbar,rmode,q=y
    if q < -1e-10: return None
    Rxe=Rr=Rq=NyInt=0.
    minp=1e9; maxp=-1e9; maxvm=0.; umax=0.
    for i,x in enumerate(X):
      for j,yy in enumerate(Y):
        e,de_r,de_q=kin(lam,exbar,rmode,q,x,yy)
        sf=section_forward(e)
        if sf is None: return None
        s,mn,mx,vm,uu=sf; wa=WX[i]*WY[j]
        Rxe += wa*s[0]
        Rr += wa*np.dot(s,de_r)
        Rq += wa*np.dot(s,de_q)
        NyInt += wa*s[1]
        minp=min(minp,mn); maxp=max(maxp,mx); maxvm=max(maxvm,vm); umax=max(umax,uu)
    # residual scaling: mean Nx and two energy derivatives normalized by Es*ts*AREA (N mm)
    raw=np.array([Rxe/AREA,Rr,Rq])
    scale=np.array([2.0e6, Es*ts*AREA, Es*ts*AREA])
    rr=raw/scale
    if not diag: return rr
    P=-NyInt/a
    return dict(res_scaled=rr,res_raw=raw,P=P,minp=minp,maxp=maxp,maxvm=maxvm,umax=umax)

def solve_path():
    rows=[]; prev=np.array([0.,0.,0.])
    for lam in np.arange(0,0.002401,0.00005):
        def fun(y):
            out=evaluate(lam,y,False)
            if out is None: return np.ones(3)*1e4
            return out
        # q>=0. rmode allows both signs. exbar bounded to physical small strain range.
        sol=least_squares(fun,prev,bounds=([-0.01,-0.01,0.],[0.01,0.01,0.05]),xtol=2e-11,ftol=2e-11,gtol=2e-11,max_nfev=180,x_scale=np.array([1e-3,1e-3,5e-3]))
        prev=sol.x
        d=evaluate(lam,sol.x,True)
        if d is None: break
        exbar,rmode,q=sol.x; qv1=rmode/be
        rows.append((lam,exbar,rmode,qv1,q,d['P']/1e6,d['minp'],d['maxp'],d['maxvm'],d['res_scaled'][0],d['res_scaled'][1],d['res_scaled'][2],sol.cost,float(sol.success)))
        print(','.join(f'{v:.12g}' for v in rows[-1]),flush=True)
        if d['minp'] < -0.00345 or d['maxvm']>fy*1.001: break
    arr=np.array(rows,float)
    np.savetxt('/mnt/data/bh050_m1_full_length_residual_path_NG9.csv',arr,delimiter=',',header='lambda,exbar,rmode_beta_qv1,qv1_mm,q,P_MN,min_principal,max_principal,max_VM_R02,Rx_scaled,Rv_scaled,Rq_scaled,cost,success',comments='')
    return arr

if __name__=='__main__':
    arr=solve_path()
    print('ROWS',len(arr))
    if len(arr): print('FINAL',arr[-1])
