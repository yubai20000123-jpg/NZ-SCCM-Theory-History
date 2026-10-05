# BH100 restored peak-rebased UHPC + continuous local Mises steel evaluator
# Audit evaluator only. Theory identity is continuous integral / algebraic level set.
# 2026-10-05

import math
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq

# geometry/material
b=5000.0; ah=10000.0
tc=42.0; ts=4.0
Ec=43400.0; nuc=0.30
Es=206000.0; nus=0.30; fy=355.0
w0=12.5
alpha=math.pi/b; beta=math.pi/ah
D0=Ec*tc**3/(12*(1-nuc**2))

# locked UHPC peak markers
eps_tp=0.000972202765
eps_cp=0.0035
d_tp=0.584009
d_cp=0.036205109

# UC141 source tables
comp_stress=np.array([119.49,132.75,141.1,138.58,132.28,123.94,114.85,112.11,108.49,105.83,101.49,98.96,97.31,89.5,87.31,84.49,82.46,76.16,70.55,53.58,42.57,35.06,29.67,25.65,22.56,20.11,19.99,16.49,15.12,12.5])
comp_inel=np.array([0,9.13521e-05,.000248848,.000656904,.001152045,.001694258,.002253713,.002421853,.00264516,.002811636,.003086584,.003249806,.003357826,.003887702,.004043235,.004248136,.004399976,.004895117,.005374424,.007165385,.008819049,.01039226,.011916347,.013408881,.014880194,.016336653,.016413447,.019220066,.020651662,.024211923])
comp_d=np.array([0,.014607023,.036205109,.08929943,.148117621,.20776548,.265113285,.281589789,.302950867,.318494097,.343460315,.357869496,.367237654,.411268568,.423589916,.43940774,.450826893,.486295597,.518102554,.616622977,.683618827,.731449053,.767066078,.794518239,.816278321,.833927173,.834768917,.860772118,.87120749,.891564603])

tens_stress=np.array([5.57,6.2,6.63,6.92,7.11,7.22,7.28,7.3,7.29,7.25,7.19,7.11,7.02,6.93,6.82,6.72,6.6,6.49,5.9,5.32,4.79,4.31,2.85])
tens_crack=np.array([0,.000244535,.000331785,.000422283,.000515102,.00060963,.000705442,.000802233,.000899778,.000997908,.001096496,.001195439,.001294658,.001394093,.001493691,.001593413,.001693227,.001793106,.002292835,.002792172,.003290519,.003787701,.005765689])
tens_d=np.array([0,.390860215,.436692315,.474718165,.507108851,.535230945,.560004233,.58207912,.60193334,.619928546,.636345331,.65140589,.665289232,.678141723,.690084577,.701219306,.711631769,.721395225,.762415184,.79392965,.818976827,.839385484,.893368782])

comp_eta=comp_inel+comp_stress/Ec
tens_eta=tens_crack+tens_stress/Ec
p_c=comp_inel-(comp_d/(1-comp_d))*comp_stress/Ec
p_t=tens_crack-(tens_d/(1-tens_d))*tens_stress/Ec
p_tp=float(np.interp(eps_tp,tens_eta,p_t))
p_cp=float(np.interp(eps_cp,comp_eta,p_c))

def interp(x,xp,fp):
    return np.interp(x,xp,fp,left=fp[0],right=fp[-1])

def uhpc_state(w,nq=120):
    gx,wx=leggauss(nq); gy,wy=leggauss(nq)
    x=(gx+1)*b/2; y=(gy+1)*ah/2
    wx=wx*b/2; wy=wy*ah/2
    X,Y=np.meshgrid(x,y,indexing='ij')
    W=np.outer(wx,wy)
    phi=np.sin(alpha*X)*np.sin(beta*Y)
    c2x=np.cos(2*alpha*X); c2y=np.cos(2*beta*Y)
    ccx=np.cos(alpha*X); ccy=np.cos(beta*Y)
    Q=w*w+2*w0*w
    NyE=D0*((alpha**2+beta**2)**2/beta**2)*w/(w0+w)+Ec*tc/16*((alpha**4+beta**4)/beta**2)*Q if w>0 else 0.0
    ex0=nuc*NyE/(Ec*tc)-alpha**2*Q/8*c2y+nuc*beta**2*Q/8*c2x
    ey0=-NyE/(Ec*tc)-beta**2*Q/8*c2x+nuc*alpha**2*Q/8*c2y
    dface=[]; epx=[]; epy=[]
    for s in (+1,-1):
        z=s*tc/2
        ex=ex0+z*alpha**2*w*phi
        ey=ey0+z*beta**2*w*phi
        gam=2*z*alpha*beta*w*ccx*ccy
        avg=(ex+ey)/2
        rad=np.sqrt(((ex-ey)/2)**2+(gam/2)**2)
        e1=avg+rad; e2=avg-rad
        et=np.maximum(e1,0); ec=np.maximum(-e2,0)

        dt_raw=interp(et,tens_eta,tens_d)
        dc_raw=interp(ec,comp_eta,comp_d)
        dt=np.where(et>eps_tp,np.maximum((dt_raw-d_tp)/(1-d_tp),0),0)
        dc=np.where(ec>eps_cp,np.maximum((dc_raw-d_cp)/(1-d_cp),0),0)
        dface.append(np.maximum(dt,dc))

        pt_raw=interp(et,tens_eta,p_t)
        pc_raw=interp(ec,comp_eta,p_c)
        dpt=np.where(et>eps_tp,np.maximum(pt_raw-p_tp,0),0)
        dpc=np.where(ec>eps_cp,np.maximum(pc_raw-p_cp,0),0)

        den=np.sqrt((ex-ey)**2+gam**2)
        c2=np.divide(ex-ey,den,out=np.ones_like(den),where=den>1e-18)
        c2sq=(1+c2)/2; s2sq=(1-c2)/2
        epx.append(dpt*c2sq-dpc*s2sq)
        epy.append(dpt*s2sq-dpc*c2sq)

    dp,dm=dface
    d0=(dp+dm)/2; d1=(dp-dm)/2
    rhoA_loc=1-d0
    rhoD_loc=(1-d0)-np.divide(d1*d1,3*(1-d0),out=np.zeros_like(d0),where=(1-d0)>1e-12)

    psiA=alpha**4*c2y**2+beta**4*c2x**2-2*nuc*alpha**2*beta**2*c2x*c2y
    psiD=(alpha**4+beta**4+2*nuc*alpha**2*beta**2)*phi**2+2*(1-nuc)*alpha**2*beta**2*ccx**2*ccy**2
    IA=b*ah/2*(alpha**4+beta**4)
    ID=b*ah/4*(alpha**2+beta**2)**2
    rhoA=float(np.sum(W*rhoA_loc*psiA)/IA)
    rhoD=float(np.sum(W*rhoD_loc*psiD)/ID)

    kxp=(epx[0]-epx[1])/tc
    kyp=(epy[0]-epy[1])/tc
    denwp=(alpha**4+beta**4+2*nuc*alpha**2*beta**2)*(b*ah/4)
    wP=float(np.sum(W*phi*((alpha**2+nuc*beta**2)*kxp+(beta**2+nuc*alpha**2)*kyp))/denwp)

    QP=w*w+2*w0*w-wP*wP-2*w0*wP
    NyU=rhoD*D0*((alpha**2+beta**2)**2/beta**2)*(w-wP)/(w0+w)+rhoA*Ec*tc/16*((alpha**4+beta**4)/beta**2)*QP if w>0 else 0.0
    return dict(PU=b*NyU/1e6,rhoA=rhoA,rhoD=rhoD,wP=wP,NyE=NyE)

# whole-face Yun predictor
N=m=4; A0=0.703125
bstar=b/N; betastar=ah/bstar
kcr=4*betastar**2/m**2+8/3+4*m**2/betastar**2
kp=77.98072664
Hcoef=kp*(1-nus**2)/ts**2
Csigma=math.pi**2*Es*ts**2/(12*(1-nus**2)*bstar**2)
CGL=64*N*N*m*m/(ah**2*(4*N*N-1)*(4*m*m-1))

def yun_mean(A):
    return Csigma*(kcr*A/(A0+A)+Hcoef*(2*A0*A+A*A))

def solve_A(w,wP,NyE,s):
    eU=NyE/(Ec*tc)-s*2*tc*w/ah**2
    G=lambda A:(w0+wP)*A+(w-wP)*A0+(w-wP)*A
    f=lambda A:yun_mean(A)/Es-eU-s*CGL*G(A)
    xs=np.linspace(0,20,2001); vals=np.array([f(x) for x in xs])
    roots=[]
    for i in range(len(xs)-1):
        if vals[i]*vals[i+1]<0:
            roots.append(brentq(f,xs[i],xs[i+1]))
    if not roots: raise RuntimeError("no positive predictor root")
    return roots[0]

def global_field(w,s,nq=96,nz=8):
    gx,wx=leggauss(nq); gy,wy=leggauss(nq); gz,wz=leggauss(nz)
    x=(gx+1)*b/2; y=(gy+1)*ah/2; zz=gz*ts/2
    wx=wx*b/2; wy=wy*ah/2; wz=wz*ts/2
    X,Y,Z=np.meshgrid(x,y,zz,indexing='ij')
    W=np.einsum('i,j,k->ijk',wx,wy,wz)
    phi=np.sin(alpha*X)*np.sin(beta*Y)
    c2x=np.cos(2*alpha*X); c2y=np.cos(2*beta*Y)
    ccx=np.cos(alpha*X); ccy=np.cos(beta*Y)
    Q=w*w+2*w0*w
    NyE=D0*((alpha**2+beta**2)**2/beta**2)*w/(w0+w)+Ec*tc/16*((alpha**4+beta**4)/beta**2)*Q if w>0 else 0
    ex0=nuc*NyE/(Ec*tc)-alpha**2*Q/8*c2y+nuc*beta**2*Q/8*c2x
    ey0=-NyE/(Ec*tc)-beta**2*Q/8*c2x+nuc*alpha**2*Q/8*c2y
    z=s*(tc+ts)/2+Z
    ex=ex0+z*alpha**2*w*phi
    ey=ey0+z*beta**2*w*phi
    ga=2*z*alpha*beta*w*ccx*ccy
    fac=Es/(1-nus**2)
    sx=-(fac*(ex+nus*ey))
    sy=-(fac*(ey+nus*ex))
    ta=-(Es/(2*(1+nus))*ga)
    return X,Y,W,sx,sy,ta,float(np.sum(W*sy)/(b*ah*ts))

def r06_fluctuation(A,X,Y):
    U=A0+A; d=U*U-A0*A0
    kx=2*math.pi*N/b; ky=2*math.pi*m/ah
    z=np.cos(kx*X); e=np.cos(ky*Y); Ed=Es*d
    A01=Ed/2*kx**2/ky**2; A02=-Ed/32*kx**2/ky**2
    A10=Ed/2*ky**2/kx**2
    A11=-Ed*kx**2*ky**2/(kx**2+ky**2)**2
    A12=Ed/2*kx**2*ky**2/(kx**2+4*ky**2)**2
    A20=-Ed/32*ky**2/kx**2
    A21=Ed/2*kx**2*ky**2/(4*kx**2+ky**2)**2
    lx=(-ky**2*A01*e-4*ky**2*A02*(2*e**2-1)-ky**2*A11*z*e-4*ky**2*A12*z*(2*e**2-1)-ky**2*A21*(2*z**2-1)*e)
    ly=(-kx**2*A10*z-kx**2*A11*z*e-kx**2*A12*z*(2*e**2-1)-4*kx**2*A20*(2*z**2-1)-4*kx**2*A21*(2*z**2-1)*e)
    lt=-kx*ky*np.sin(kx*X)*np.sin(ky*Y)*(A11+4*A12*e+4*A21*z)
    return lx,ly,lt

def radial_cap(sx,sy,ta):
    vm=np.sqrt(sx*sx-sx*sy+sy*sy+3*ta*ta)
    f=np.minimum(1.0,fy/np.maximum(vm,1e-30))
    return sx*f,sy*f,ta*f,vm

def steel_face(w,wP,NyE,s,nq=96,nz=8):
    A=solve_A(w,wP,NyE,s)
    pred=yun_mean(A)
    X,Y,W,gx,gy,gt,gmean=global_field(w,s,nq,nz)
    cgx,cgy,cgt,gvm=radial_cap(gx,gy,gt)
    lx,ly0,lt=r06_fluctuation(A,X,Y)
    ly=ly0+(pred-gmean)
    tx=cgx+lx; ty=cgy+ly; tt=cgt+lt
    phi=tx*tx-tx*ty+ty*ty+3*tt*tt
    active=phi>fy*fy
    aa=lx*lx-lx*ly+ly*ly+3*lt*lt
    bb=cgx*lx-0.5*(cgx*ly+cgy*lx)+cgy*ly+3*cgt*lt
    cc=cgx*cgx-cgx*cgy+cgy*cgy+3*cgt*cgt-fy*fy
    disc=np.maximum(bb*bb-aa*cc,0)
    sq=np.sqrt(disc)
    r1=np.divide(-bb+sq,aa,out=np.zeros_like(aa),where=np.abs(aa)>1e-20)
    r2=np.divide(-bb-sq,aa,out=np.zeros_like(aa),where=np.abs(aa)>1e-20)
    v1=np.where((r1>=0)&(r1<=1),r1,-np.inf)
    v2=np.where((r2>=0)&(r2<=1),r2,-np.inf)
    lam=np.where(active,np.maximum(v1,v2),1.0)
    lam=np.where(np.isfinite(lam),lam,0.0)
    sy=cgy+lam*ly
    mean=float(np.sum(W*sy)/(b*ah*ts))
    return dict(A=A,mean=mean,P=b*ts*mean/1e6,
                local_fraction=float(np.sum(W*active)/(b*ah*ts)),
                global_fraction=float(np.sum(W*(gvm>fy))/(b*ah*ts)),
                predictor_mean=pred,global_mean=gmean)

def solve_state(w,nqu=120,nqs=80):
    if w==0:
        return dict(w=0,P=0,PU=0,Ptop=0,Pbottom=0,rhoA=1,rhoD=1,wP=0)
    u=uhpc_state(w,nqu)
    t=steel_face(w,u["wP"],u["NyE"],+1,nqs,8)
    d=steel_face(w,u["wP"],u["NyE"],-1,nqs,8)
    return dict(w=w,P=u["PU"]+t["P"]+d["P"],PU=u["PU"],
                Ptop=t["P"],Pbottom=d["P"],rhoA=u["rhoA"],rhoD=u["rhoD"],wP=u["wP"],
                A_top=t["A"],A_bottom=d["A"],sig_top=t["mean"],sig_bottom=d["mean"],
                frac_top=t["local_fraction"],frac_bottom=d["local_fraction"])

if __name__=="__main__":
    # mandatory regression
    r=solve_state(82.2,120,80)
    print("w=82.2",r)
    # candidate peak neighborhood
    for w in [141.8,142.0,142.2,142.3,142.4,142.6,142.8]:
        print(w,solve_state(w,120,80))
