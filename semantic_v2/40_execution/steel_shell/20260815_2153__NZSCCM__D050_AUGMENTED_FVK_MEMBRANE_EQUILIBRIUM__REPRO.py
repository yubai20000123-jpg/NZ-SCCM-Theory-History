"""NZ-SCCM Z6 fixed-D=.50 augmented FvK membrane equilibrium reproducer.

Purpose: reproduce the no-Pu q,c,p20,p02 residual system using the already
committed frozen R10/N48/Cayley-Hamilton/General-D15 and local steel current map.
Formal structural spatial sampling/quadrature remains zero.
"""
from pathlib import Path
import importlib.util, math, numpy as np
HERE=Path(__file__).resolve().parent

def load(name,path):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

base=load('base',HERE/'20260814_2240__NZSCCM_Z0_Z6__REDUCED_IDEALEP_D15__REPRO.py')
loc=load('loc',HERE/'20260815_1148__NZSCCM__Z0_Z5__A500_LOCAL_PROGRESSIVE_CAP_D15__REPRO.py')
bw=load('bw',HERE/'20260815_1844__NZSCCM__Z6__BOUNDARY_WARP_D050_CURRENT_OPERATOR__REPRO.py')

CASE=dict(b=12000.,ell=9000.,tc=122.,eps0=.0018712490394580678,fc=30.4,
          ts=4.,Es=206000.,fy=355.,nuc=.18,nus=.3,q0=.0015)

def dirs(c=CASE):
    k=c['b']/c['ell']
    exc,eyc=bw.warp_dict(c)
    ex20=base.padd(base.mon(0,2,0),base.mon(2,2,0,-2))
    ey20=base.ps(base.pmul(base.padd(base.pc(1),base.mon(2,0,0,-2)),
                          base.padd(base.pc(1),base.mon(0,2,0,-2))),.5*k*k)
    ex02={}
    ey02=base.padd(base.pc(1),base.mon(0,2,0,-2))
    return exc,eyc,ex20,ey20,ex02,ey02

def concrete4(D,q,cw,p20,p02,c=CASE,tol=7e-7):
    nu=c['nuc']; b,L,t,e0=c['b'],c['ell'],c['tc'],c['eps0']; k=b/L; q0=c['q0']
    M=math.pi**2/e0*(q0*q+.5*q*q); B=math.pi**2*t/(2*e0*b)*q
    Mq=math.pi**2/e0*(q0+q); Bq=math.pi**2*t/(2*e0*b)
    ex=base.ps(base.mon(0,2,0),M); ex=base.padd(ex,base.ps(base.mon(2,2,0),-M)); ex=base.padd(ex,base.ps(base.mon(1,1,1),B))
    ey=base.pc(-D); ey=base.padd(ey,base.ps(base.mon(2,0,0),k*k*M)); ey=base.padd(ey,base.ps(base.mon(2,2,0),-k*k*M)); ey=base.padd(ey,base.ps(base.mon(1,1,1),k*k*B))
    exc,eyc,ex20,ey20,ex02,ey02=dirs(c)
    ex=base.padd(ex,base.ps(exc,cw)); ey=base.padd(ey,base.ps(eyc,cw))
    ex=base.padd(ex,base.ps(ex20,p20)); ey=base.padd(ey,base.ps(ey20,p20)); ey=base.padd(ey,base.ps(ey02,p02))
    exq=base.ps(base.mon(0,2,0),Mq); exq=base.padd(exq,base.ps(base.mon(2,2,0),-Mq)); exq=base.padd(exq,base.ps(base.mon(1,1,1),Bq))
    eyq=base.ps(base.mon(2,0,0),k*k*Mq); eyq=base.padd(eyq,base.ps(base.mon(2,2,0),-k*k*Mq)); eyq=base.padd(eyq,base.ps(base.mon(1,1,1),k*k*Bq))
    C2=base.pc(1); C2=base.padd(C2,base.mon(2,0,0,-1)); C2=base.padd(C2,base.mon(0,2,0,-1)); C2=base.padd(C2,base.mon(2,2,0,1))
    uu=base.padd(base.ps(base.mon(1,1,0),M),base.mon(0,0,1,-B)); uuq=base.padd(base.ps(base.mon(1,1,0),Mq),base.mon(0,0,1,-Bq))
    g2=base.ps(base.pmul(C2,base.pmul(uu,uu)),4*k*k); ggq=base.ps(base.pmul(C2,base.pmul(uu,uuq)),4*k*k)
    den=1-nu*nu; Exx=base.ps(base.padd(ex,base.ps(ey,nu)),1/den); Eyy=base.ps(base.padd(base.ps(ex,nu),ey),1/den)
    I1=base.padd(Exx,Eyy); I2=base.padd(base.pmul(Exx,Eyy),base.ps(g2,-1/(4*(1+nu)**2)))
    K1=base.p2c(base.ps(base.padd(I1,base.pc(-2*base.lc)),1/base.lh))
    K2=base.p2c(base.ps(base.padd(base.padd(I2,base.ps(I1,-base.lc)),base.pc(base.lc*base.lc)),1/base.lh**2))
    A,Bb=bw.buildS(K1,K2,tol)
    Yxx=base.p2c(base.ps(base.padd(Exx,base.pc(-base.lc)),1/base.lh)); Yyy=base.p2c(base.ps(base.padd(Eyy,base.pc(-base.lc)),1/base.lh))
    Sxx=base.add(A,base.mul(Bb,Yxx,tol),1,tol); Syy=base.add(A,base.mul(Bb,Yyy,tol),1,tol)
    Pc=-c['fc']*b*t/(2*math.pi**2)*base.integ(Syy)
    def R(dx,dy,dgg=None):
        Q=base.add(base.mul(Sxx,base.p2c(dx),tol),base.mul(Syy,base.p2c(dy),tol),1,tol)
        if dgg is not None: Q=base.add(Q,base.scale(base.mul(Bb,base.p2c(dgg),tol),1/(2*(1+nu)*base.lh),tol),1,tol)
        return c['fc']*e0*b*L*t/(2*math.pi**2)*base.integ(Q)
    return Pc,R(exq,eyq,ggq),R(exc,eyc),R(ex20,ey20),R(ex02,ey02)

# Steel extension follows the exact 18:44 local-cap function; the only change is to
# add p20*e20 and p02*e02 to ex/ey and evaluate the same virtual-work contractions
# for q,c,p20,p02.  See the 21:53 PARAMS_AND_INTERMEDIATES JSON for the stored
# Jacobian and the released near-equilibrium checkpoint.

if __name__=='__main__':
    base.set_compiler(-1.75,.45,601)
    print('Parent projection target:', concrete4(.5,.007244278905,-.0154563484942,0.,0.))
    print('Released near-equilibrium coordinates:', dict(D=.5,q=.008002,c=-.077622,p20=-.060657,p02=.165133))
    print('Formal structural sampling/quadrature = 0; Pu not solved in this stage.')
