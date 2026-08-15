import numpy as np, math, json, time
from scipy.optimize import root
from numpy.polynomial.legendre import leggauss

# frozen physical material constants
kappa=2.0005129533678754; rho=.1; xcr=rho/kappa; eta0=xcr/20; ur=.03; hh=.09799750427197301
acc=.1072329249362415; at=1-2**(-1/8)
CASE=dict(a=24000.,b=12000.,ell=12000.,m=2,tc=122.,h=130.,eps0=.0018712490394580678,fc=30.4,
          ts=4.,Es=206000.,fy=355.,nuc=.18,nus=.3,q0=.004)

def Pi(z):
    z=np.asarray(z,float); return z*z*(np.sqrt(z*z+eta0*eta0)+z)/(2*(z*z+eta0*eta0))
def uR(t):
    t=np.asarray(t,float); r=t/xcr; o=np.empty_like(r); m=r<=1; rr=r[m]
    o[m]=rho*rr+(10*hh-6*rho)*rr**3+(8*rho-15*hh)*rr**4+(6*hh-3*rho)*rr**5
    m2=(r>1)&(r<=10); s=(r[m2]-1)/9; o[m2]=hh+(ur-hh)*(10*s**3-15*s**4+6*s**5); o[r>10]=ur; return o
def scalar_targets(lam):
    c=Pi(-lam); t=Pi(lam); C=kappa*c/(1+(kappa-2)*c+c*c); u=uR(t); T=u/rho; U=kappa*lam-C+kappa*c+u-kappa*t; return U,C,T,T**7

def matfun_from_eigh(vals,vecs,fvals):
    return np.einsum('...ia,...a,...ja->...ij',vecs,fvals,vecs,optimize=True)
def concrete_S(Exx,Eyy,G):
    shape=Exx.shape
    E=np.empty(shape+(2,2)); E[...,0,0]=Exx;E[...,1,1]=Eyy;E[...,0,1]=G;E[...,1,0]=G
    vals,vecs=np.linalg.eigh(E)
    Uv,Cv,Tv,T7v=scalar_targets(vals)
    U=matfun_from_eigh(vals,vecs,Uv); C=matfun_from_eigh(vals,vecs,Cv); T=matfun_from_eigh(vals,vecs,Tv); T7=matfun_from_eigh(vals,vecs,T7v)
    detC=C[...,0,0]*C[...,1,1]-C[...,0,1]*C[...,1,0]
    detT=T[...,0,0]*T[...,1,1]-T[...,0,1]*T[...,1,0]
    trT=T[...,0,0]+T[...,1,1]; trT7=T7[...,0,0]+T7[...,1,1]
    CT=np.einsum('...ik,...kj->...ij',C,T,optimize=True)
    I=np.zeros_like(U);I[...,0,0]=1;I[...,1,1]=1
    S=U - acc*detC[...,None,None]*C + trT[...,None,None]*C - CT - rho*at*detT[...,None,None]*(trT7[...,None,None]*I-T7)
    return S,vals

def grid(nxy=24,nz=10):
    gx,wx=leggauss(nxy); gz,wz=leggauss(nz)
    X=(gx+1)*math.pi/2; W=wx*math.pi/2
    XX=X[:,None,None]; YY=X[None,:,None]; ZZ=gz[None,None,:]
    WW=W[:,None,None]*W[None,:,None]*wz[None,None,:]
    return XX,YY,ZZ,WW

def eval_total(D,x,nxy=24,nz=10,case=CASE,return_audit=False):
    q,cw,p20,p02=x; b,L,tc,ts,e0,fc,Es,fy,nu,nus=case['b'],case['ell'],case['tc'],case['ts'],case['eps0'],case['fc'],case['Es'],case['fy'],case['nuc'],case['nus']; k=b/L;q0=case['q0']
    M=math.pi**2/e0*(q0*q+.5*q*q);Mq=math.pi**2/e0*(q0+q);B=math.pi**2*tc/(2*e0*b)*q;Bq=math.pi**2*tc/(2*e0*b)
    X,Y,Z,W=grid(nxy,nz); sx=np.sin(X);sy=np.sin(Y);cx=np.cos(X);cy=np.cos(Y)
    exc=4/math.pi*sx*sy**2;eyc=8*k*k/math.pi*sx*(1-2*sy**2);ex20=sy**2-2*sx**2*sy**2;ey20=.5*k*k*(1-2*sx**2)*(1-2*sy**2);ey02=1-2*sy**2
    ex=M*sy**2-M*sx**2*sy**2+B*sx*sy*Z+cw*exc+p20*ex20
    ey=-D+k*k*M*sx**2-k*k*M*sx**2*sy**2+k*k*B*sx*sy*Z+cw*eyc+p20*ey20+p02*ey02
    exq=Mq*sy**2-Mq*sx**2*sy**2+Bq*sx*sy*Z
    eyq=k*k*Mq*sx**2-k*k*Mq*sx**2*sy**2+k*k*Bq*sx*sy*Z
    uu=M*sx*sy-B*Z; uuq=Mq*sx*sy-Bq*Z
    gam=2*k*cx*cy*uu; gamq=2*k*cx*cy*uuq
    Exx=(ex+nu*ey)/(1-nu*nu);Eyy=(nu*ex+ey)/(1-nu*nu);G=gam/(2*(1+nu))
    S,lam=concrete_S(Exx,Eyy,G)
    def qint(v):return float(np.sum(W*v))
    Pc=-fc*b*tc/(2*math.pi**2)*qint(S[...,1,1])
    facr=fc*e0*b*L*tc/(2*math.pi**2)
    Rq=facr*qint(S[...,0,0]*exq+S[...,1,1]*eyq+S[...,0,1]*gamq)
    Rc=facr*qint(S[...,0,0]*exc+S[...,1,1]*eyc)
    R20=facr*qint(S[...,0,0]*ex20+S[...,1,1]*ey20)
    R02=facr*qint(S[...,1,1]*ey02)
    gz, wz=leggauss(nz); Zs=gz[None,None,:]; Ws=(leggauss(nxy)[1]*math.pi/2)[:,None,None]*(leggauss(nxy)[1]*math.pi/2)[None,:,None]*wz[None,None,:]
    Pst=Rqst=Rcst=R20st=R02st=0.0; rmax=0.0; rmin=1e99
    fac=Es*e0/(1-nus*nus); kb=math.pi**2*q/(e0*b);kbq=math.pi**2/(e0*b)
    for face in (-1,1):
        z=face*(tc/2+ts/2)+(ts/2)*Zs
        bz=kb*z;bzq=kbq*z
        exs=M*sy**2-M*sx**2*sy**2+bz*sx*sy+cw*exc+p20*ex20
        eys=-D+k*k*M*sx**2-k*k*M*sx**2*sy**2+k*k*bz*sx*sy+cw*eyc+p20*ey20+p02*ey02
        exqs=Mq*sy**2-Mq*sx**2*sy**2+bzq*sx*sy
        eyqs=k*k*Mq*sx**2-k*k*Mq*sx**2*sy**2+k*k*bzq*sx*sy
        us=M*sx*sy-bz;uqs=Mq*sx*sy-bzq;gams=2*k*cx*cy*us;gamqs=2*k*cx*cy*uqs
        sxx=fac*(exs+nus*eys);syy=fac*(nus*exs+eys);tau=fac*(1-nus)/2*gams
        vm=np.sqrt(np.maximum(sxx*sxx-sxx*syy+syy*syy+3*tau*tau,0)); alpha=np.minimum(1.0,fy/np.maximum(vm,1e-300));r=vm/fy;rmax=max(rmax,float(np.max(r)));rmin=min(rmin,float(np.min(r)))
        sxx*=alpha;syy*=alpha;tau*=alpha
        def sint(v):return float(np.sum(Ws*v))
        Pst += sint(syy)
        Rqst += sint(sxx*e0*exqs+syy*e0*eyqs+tau*e0*gamqs)
        Rcst += sint(sxx*e0*exc+syy*e0*eyc)
        R20st += sint(sxx*e0*ex20+syy*e0*ey20)
        R02st += sint(syy*e0*ey02)
    Ps=-b*ts/(2*math.pi**2)*Pst;fr=b*L*ts/(2*math.pi**2);Rqs=fr*Rqst;Rcs=fr*Rcst;R20s=fr*R20st;R02s=fr*R02st
    tot=np.array([Pc+Ps,Rq+Rqs,Rc+Rcs,R20+R20s,R02+R02s])
    if return_audit:
        return tot,np.array([Pc,Rq,Rc,R20,R02]),np.array([Ps,Rqs,Rcs,R20s,R02s]),{'lam_min':float(np.min(lam)),'lam_max':float(np.max(lam)),'steel_rmin':rmin,'steel_rmax':rmax,'M':M,'B':B,'Mq':Mq,'Bq':Bq}
    return tot

def solve_path(Ds,nxy_solve=18,nz_solve=8,nxy_final=32,nz_final=12):
    rows=[]; x=np.zeros(4); prev=None;prevD=None
    for D in Ds:
        if prev is not None and len(rows)>=2:
            x0=x+(D-prevD)/(prevD-rows[-2]['D'])*(x-prev)
        else:x0=x.copy()
        def F(z):return eval_total(D,z,nxy_solve,nz_solve)[1:]/1e9
        sol=root(F,x0,method='hybr',options={'xtol':1e-9,'maxfev':80})
        if (not sol.success) or np.linalg.norm(sol.fun,np.inf)>1e-6:
            sol2=root(F,x,method='lm',options={'ftol':1e-10,'xtol':1e-10,'maxiter':120})
            if np.linalg.norm(sol2.fun,np.inf)<np.linalg.norm(sol.fun,np.inf):sol=sol2
        if np.linalg.norm(sol.fun,np.inf)>2e-5:
            print('STOP',D,sol.success,sol.fun,sol.x);break
        prev=x.copy(); prevD=D; x=sol.x.copy()
        tot,cc,ss,aud=eval_total(D,x,nxy_final,nz_final,return_audit=True)
        row={'D':float(D),'q':float(x[0]),'c':float(x[1]),'p20':float(x[2]),'p02':float(x[3]),'P_MN':float(tot[0]/1e6),'Pc_MN':float(cc[0]/1e6),'Ps_MN':float(ss[0]/1e6),'Rq_MNmm':float(tot[1]/1e6),'Rc_MNmm':float(tot[2]/1e6),'R20_MNmm':float(tot[3]/1e6),'R02_MNmm':float(tot[4]/1e6),**aud}
        rows.append(row);print(row,flush=True)
    return rows

if __name__=='__main__':
    Ds=np.r_[np.arange(.05,.51,.05),np.arange(.6,2.01,.1)]
    t=time.time();rows=solve_path(Ds);print('runtime',time.time()-t,'n',len(rows))
    open('ar2_direct_path.json','w').write(json.dumps(rows,indent=2))
