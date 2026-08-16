"""NZ-SCCM Z0-Z5 AR2 four-edge SSSS full-section reproduction driver.

Timestamp: 2026-08-16 10:43 +08:00
Formal structural spatial sampling/quadrature = 0.
Material-coordinate nodes are coefficient-generation nodes only.
Zhou/Winter values are evaluated only after NZ-SCCM states are frozen.
"""
from pathlib import Path
import importlib.util, math
import numpy as np
from scipy.optimize import root_scalar

HERE=Path(__file__).resolve().parent
H0_PATH=HERE/'20260815_1500__NZSCCM__Z6_H0__ANALYTIC_DOMAIN_AND_SHELL_COMPILER_GATE__REPRO.py'

def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod

h0=load_module('h0_kernel',H0_PATH)
base=h0.base
base.set_compiler(-2.35,1.90,10001)

# aliases to the already-committed exact Chebyshev/D15 algebra
pc,padd,ps,mon,pmul,p2c=base.pc,base.padd,base.ps,base.mon,base.pmul,base.p2c
add,scale,mul,integ=base.add,base.scale,base.mul,base.integ

CASES={
'Z0':dict(a=12000.,ns=30,ls=200.,h=130.,rho=.02,c=dict(b=6000.,ell=6000.,tc=122.,eps0=.0018712490394580678,fc=30.4,ts=4.,Es=206000.,fy=355.,fcu=40.)),
'Z1':dict(a=12000.,ns=30,ls=200.,h=100.,rho=.02,c=dict(b=6000.,ell=6000.,tc=92.,eps0=.0018712490394580678,fc=30.4,ts=4.,Es=206000.,fy=235.,fcu=40.)),
'Z2':dict(a=12000.,ns=30,ls=200.,h=130.,rho=.02,c=dict(b=6000.,ell=6000.,tc=122.,eps0=.0018712490394580678,fc=30.4,ts=4.,Es=206000.,fy=460.,fcu=40.)),
'Z3':dict(a=12000.,ns=30,ls=200.,h=130.,rho=.02,c=dict(b=6000.,ell=6000.,tc=122.,eps0=.0025344898708809867,fc=45.6,ts=4.,Es=206000.,fy=355.,fcu=60.)),
'Z4':dict(a=16000.,ns=40,ls=200.,h=200.,rho=.02,c=dict(b=8000.,ell=8000.,tc=192.,eps0=.0018712490394580678,fc=30.4,ts=4.,Es=206000.,fy=355.,fcu=40.)),
'Z5':dict(a=4000.,ns=10,ls=200.,h=130.,rho=.02,c=dict(b=2000.,ell=2000.,tc=122.,eps0=.0018712490394580678,fc=30.4,ts=4.,Es=206000.,fy=355.,fcu=40.)),
}

PEAK_SAMPLES={
'Z0':[.910,.915,.920], 'Z1':[.560,.580,.600], 'Z2':[1.100,1.120,1.140],
'Z3':[.660,.680,.700], 'Z4':[.920,.940,.960], 'Z5':[.980,1.000,1.020],
}
Q_SEED={'Z0':.00317,'Z1':.00359,'Z2':.00412,'Z3':.00365,'Z4':.00234,'Z5':.00038}

# stable ideal-EP radial cap evaluated in the same Chebyshev coefficient algebra

def steel_fields_cheb(D,q,c,q0,face=1,nuc=.18,nus=.30):
    b,L,tc,ts,e0,Es=c['b'],c['ell'],c['tc'],c['ts'],c['eps0'],c['Es']; k=b/L
    M=math.pi**2/e0*(q0*q+.5*q*q); Mq=math.pi**2/e0*(q0+q)
    kz=math.pi**2*q/(e0*b); kzq=math.pi**2/(e0*b)
    zc=face*(tc/2+ts/2); zh=ts/2
    ex=pc(nuc*D); ex=padd(ex,ps(mon(0,2,0),M)); ex=padd(ex,ps(mon(2,2,0),-M)); ex=padd(ex,ps(mon(1,1,0),kz*zc)); ex=padd(ex,ps(mon(1,1,1),kz*zh))
    ey=pc(-D); ey=padd(ey,ps(mon(2,0,0),k*k*M)); ey=padd(ey,ps(mon(2,2,0),-k*k*M)); ey=padd(ey,ps(mon(1,1,0),k*k*kz*zc)); ey=padd(ey,ps(mon(1,1,1),k*k*kz*zh))
    exq=ps(mon(0,2,0),Mq); exq=padd(exq,ps(mon(2,2,0),-Mq)); exq=padd(exq,ps(mon(1,1,0),kzq*zc)); exq=padd(exq,ps(mon(1,1,1),kzq*zh))
    eyq=ps(mon(2,0,0),k*k*Mq); eyq=padd(eyq,ps(mon(2,2,0),-k*k*Mq)); eyq=padd(eyq,ps(mon(1,1,0),k*k*kzq*zc)); eyq=padd(eyq,ps(mon(1,1,1),k*k*kzq*zh))
    C2=pc(1); C2=padd(C2,mon(2,0,0),-1); C2=padd(C2,mon(0,2,0),-1); C2=padd(C2,mon(2,2,0),1)
    u=ps(mon(1,1,0),M); u=padd(u,pc(-kz*zc)); u=padd(u,ps(mon(0,0,1),-kz*zh))
    uq=ps(mon(1,1,0),Mq); uq=padd(uq,pc(-kzq*zc)); uq=padd(uq,ps(mon(0,0,1),-kzq*zh))
    g2=ps(pmul(C2,pmul(u,u)),4*k*k); ggq=ps(pmul(C2,pmul(u,uq)),4*k*k)
    exA,eyA,exqA,eyqA,g2A,ggqA=map(p2c,[ex,ey,exq,eyq,g2,ggq])
    fac=Es*e0/(1-nus*nus)
    sx=scale(add(exA,scale(eyA,nus)),fac); sy=scale(add(scale(exA,nus),eyA),fac)
    tau2=scale(g2A,(fac*(1-nus)/2)**2)
    vm2=add(add(mul(sx,sx),mul(sy,sy)),mul(sx,sy),-1); vm2=add(vm2,scale(tau2,3))
    Qn=add(mul(add(exA,scale(eyA,nus)),exqA),mul(add(scale(exA,nus),eyA),eyqA)); Qn=add(Qn,scale(ggqA,(1-nus)/2))
    return sy,vm2,scale(Qn,fac*e0)

def alpha_field(rfield,deg=40,rmax=8.,nodes=3001,tol=2e-9):
    co=h0.alpha_coeff(deg,rmax,nodes,100.0)
    tt=add(scale(rfield,2/rmax,tol),np.array([[[-1.0]]]),1,tol)
    T0=np.ones((1,1,1)); out=scale(T0,co[0],tol)
    if deg==0:return out
    T1=tt; out=add(out,scale(T1,co[1],tol),1,tol); a,b=T0,T1
    for n in range(2,deg+1):
        cc=add(scale(mul(tt,b,tol),2,tol),a,-1,tol); out=add(out,scale(cc,co[n],tol),1,tol); a,b=b,cc
    return out

def shell_resultants(D,q,c,q0,deg):
    ips=irq=0.0
    for face in (-1,1):
        sy,vm2,Q=steel_fields_cheb(D,q,c,q0,face)
        alpha=alpha_field(scale(vm2,1/c['fy']**2),deg)
        ips+=integ(mul(alpha,sy)); irq+=integ(mul(alpha,Q))
    return -c['b']*c['ts']/(2*math.pi**2)*ips, c['b']*c['ell']*c['ts']/(2*math.pi**2)*irq

def web_resultants(D,q,c,q0,rho_w,deg):
    b,L,tc,e0,Es,fy=c['b'],c['ell'],c['tc'],c['eps0'],c['Es'],c['fy']; k=b/L
    M=math.pi**2/e0*(q0*q+.5*q*q); Mq=math.pi**2/e0*(q0+q); B=math.pi**2*tc/(2*e0*b)*q; Bq=math.pi**2*tc/(2*e0*b)
    ey=pc(-D); ey=padd(ey,ps(mon(2,0,0),k*k*M)); ey=padd(ey,ps(mon(2,2,0),-k*k*M)); ey=padd(ey,ps(mon(1,1,1),k*k*B))
    eyq=ps(mon(2,0,0),k*k*Mq); eyq=padd(eyq,ps(mon(2,2,0),-k*k*Mq)); eyq=padd(eyq,ps(mon(1,1,1),k*k*Bq))
    eyA,eyqA=p2c(ey),p2c(eyq); u=scale(eyA,Es*e0/fy); alpha=alpha_field(mul(u,u),deg)
    sigma=scale(mul(alpha,u),fy); qwork=mul(sigma,scale(eyqA,e0))
    return -rho_w*b*tc/(2*math.pi**2)*integ(sigma), rho_w*b*L*tc/(2*math.pi**2)*integ(qwork)

def total(name,D,q,deg):
    d=CASES[name]; c=d['c']; q0=d['a']/(500*c['b'])
    Pc,Rc=h0.concrete_q0(D,q,c,q0,tol=2e-9)
    Ps,Rs=shell_resultants(D,q,c,q0,deg); Pw,Rw=web_resultants(D,q,c,q0,d['rho'],deg)
    return {'Pc_eff':(1-d['rho'])*Pc,'Ps':Ps,'Pw':Pw,'P':(1-d['rho'])*Pc+Ps+Pw,'Rc_eff':(1-d['rho'])*Rc,'Rs':Rs,'Rw':Rw,'Rq':(1-d['rho'])*Rc+Rs+Rw}

def solve_q(name,D,qg,deg):
    def f(q):return total(name,D,q,deg)['Rq']
    lo=max(0.,.75*qg); hi=1.25*qg; flo,fhi=f(lo),f(hi)
    for _ in range(10):
        if flo*fhi<=0:break
        if flo>0 and fhi>0: hi,fhi,lo=lo,flo,max(0.,.6*lo); flo=f(lo)
        else: lo,flo,hi=hi,fhi,1.4*hi; fhi=f(hi)
    r=root_scalar(f,bracket=(lo,hi),method='brentq',xtol=1e-10,rtol=1e-9)
    return r.root,total(name,D,r.root,deg)

def zhou_winter(name):
    d=CASES[name]; c=d['c']; ns,ls,h,ts,fy,fcu,a,b=d['ns'],d['ls'],d['h'],c['ts'],c['fy'],c['fcu'],d['a'],c['b']
    ES=206000.; nu_s=.30; nu_c=.20; Ec=32500. if fcu==40 else 1e5/(34.7/fcu+2.2); Gs=ES/(2*(1+nu_s)); Gc=Ec/(2*(1+nu_c)); fc=.76*fcu; tc=h-2*ts
    Ac=ns*(ls-ts)*tc; Ag=b*h; As=Ag-Ac; Pyth=(fy*As+fc*Ac)/1e6
    voidI=ns*(ls-ts)*tc**3/12; Dy_s=ES/b*(b*h**3/12-voidI); Dy_c=Ec/b*voidI; Dy=Dy_s+Dy_c; Dx=ES*(h**3-tc**3)/12+Ec*tc**3/12
    A0=(b-ts)*(h-ts); s=2*((b-ts)+(h-ts)); beta=(1/3)*(1-.63*tc/(b-2*ts)+.052*(tc/(b-2*ts))**5); Dt=(4*Gs*A0**2/(s/ts)+Gc*beta*(b-2*ts)*tc**3)/b; Dxy=Dt/2; H=Dxy+nu_s*Dy_s+nu_c*Dy_c
    candidates=[]
    for m in range(1,51):
        Ncr=math.pi**2*(Dx*a*a/(m*m*b**4)+2*H/b**2+Dy*m*m/a**2); candidates.append((m,Ncr*b/1e6))
    m,Pcr=min(candidates,key=lambda x:x[1]); lam=math.sqrt(Pyth/Pcr)
    Phi=.454+.192*lam+.416*lam**2 if lam<=1 else -.140+1.387*lam-.186*lam**2
    phiZ=1. if lam<=.55 else 1/(Phi+math.sqrt(Phi**2-lam**2)); phiW=1. if lam<=.673 else (1-.22/lam)/lam
    return dict(Pyth=Pyth,m=m,Pcr=Pcr,lam=lam,Pz=phiZ*Pyth,Pw=phiW*Pyth)

if __name__=='__main__':
    print('FORMAL STRUCTURAL SAMPLING/QUADRATURE = 0')
    print('case,Dpeak,q48,Pu48_MN,Pcr_MN,Pyth_MN,Zhou_MN,Winter_MN,NZ-Zhou_pct,NZ-Winter_pct')
    for name in CASES:
        vals=[]
        for D in PEAK_SAMPLES[name]:
            q,st=solve_q(name,D,Q_SEED[name],40); vals.append((D,st['P']/1e6,q))
        coef=np.polyfit([x[0] for x in vals],[x[1] for x in vals],2); Dp=-coef[1]/(2*coef[0])
        q48,st48=solve_q(name,Dp,vals[1][2],48); z=zhou_winter(name); Pu=st48['P']/1e6
        print(f"{name},{Dp:.10f},{q48:.15g},{Pu:.12f},{z['Pcr']:.12f},{z['Pyth']:.12f},{z['Pz']:.12f},{z['Pw']:.12f},{(Pu-z['Pz'])/z['Pz']*100:.9f},{(Pu-z['Pw'])/z['Pw']*100:.9f}")
