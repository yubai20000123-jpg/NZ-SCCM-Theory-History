# NZ-SCCM Z6 Nguyen-vs-mode-space / S0-S4 neighborhood reproduction
# Timestamp: 2026-08-15 16:15 +08:00
# Formal structural spatial sampling/quadrature = 0.
# Uses the frozen R10->N48->CH->D15 concrete kernel and current local progressive radial-cap shell map.

from pathlib import Path
import importlib.util, math

HERE = Path(__file__).resolve().parent
BASE = HERE / '20260814_2240__NZSCCM_Z0_Z6__REDUCED_IDEALEP_D15__REPRO.py'
LOCAL = HERE / '20260815_1148__NZSCCM__Z0_Z5__A500_LOCAL_PROGRESSIVE_CAP_D15__REPRO.py'

def load(name,path):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

base=load('base',BASE)
loc=load('loc',LOCAL)

Es=206000.0; Ec=32500.0; fy=355.0; fcu=40.0; fcp=30.4
nus=0.30; nuc_zhou=0.20; ls=200.0; ts=4.0; eps0=0.0018712490394580678

CASES={
'S0_Z6':(9000.,12000.,130.,60),
'S1_a8000':(8000.,12000.,130.,60),
'S2_b10000':(9000.,10000.,130.,50),
'S3_a8000_b10000':(8000.,10000.,130.,50),
'S4_minus5pct':(8550.,11400.,130.,57),
}

# Fixed sign-changing q brackets used in the 20260815_1615 audit.
BRACKETS={
'S1_a8000':{0.60:(.0035,.0038),0.65:(.0041,.0043),0.70:(.0046,.0048),0.75:(.0053,.0055)},
'S2_b10000':{0.65:(.00365,.0038),0.70:(.0042,.0045),0.75:(.0051,.0055)},
'S3_a8000_b10000':{0.60:(.0023,.0026),0.65:(.0028,.0031),0.70:(.0035,.0038)},
'S4_minus5pct':{0.60:(.0038,.0040),0.65:(.0044,.0046),0.68:(.0047,.0049),0.705:(.00518,.00519),0.73:(.0055,.0057)},
}

def zhou_stiff(a,b,h,ns):
    tc=h-2*ts
    Ac=ns*(ls-ts)*tc; As=b*h-Ac
    Pyth=fy*As+fcp*Ac
    Dx=Es*(h**3-tc**3)/12+Ec*tc**3/12
    Dys=Es/b*(b*h**3/12-ns*(ls-ts)*tc**3/12)
    Dyc=Ec/b*(ns*(ls-ts)*tc**3/12); Dy=Dys+Dyc
    Gs=Es/(2*(1+nus)); Gc=Ec/(2*(1+nuc_zhou))
    A0=(b-ts)*(h-ts); int_ds=2*((b-ts)+(h-ts))/ts
    beta=(1/3)*(1-0.63*(h-2*ts)/(b-2*ts)+0.052*((h-2*ts)/(b-2*ts))**5)
    Dt=(1/b)*(4*Gs*A0*A0/int_ds+Gc*beta*(b-2*ts)*(h-2*ts)**3)
    H=Dt/2+nus*Dys+nuc_zhou*Dyc
    def pcr(m=1,n=1):
        return b*math.pi**2*(Dx*n**4*a*a/(m*m*b**4)+2*H*n*n/b**2+Dy*m*m/a**2)
    return Pyth,pcr

def small_slope(a,b,q):
    q0=a/(500*b); qt=q0+q
    wx=math.pi*qt*b/a; wy=math.pi*qt; th=max(abs(wx),abs(wy))
    return dict(q0=q0,q_total=qt,max_wx=abs(wx),max_wy=abs(wy),max_slope_rad=th,
                max_slope_deg=th*180/math.pi,
                sin_leading_relative_error=th*th/6,
                cos_second_order_leading_absolute_error=th**4/24)

def current_total(case,D,q,deg=20):
    a,b,h,ns=CASES[case]; q0=a/(500*b)
    c=dict(b=b,ell=a,tc=h-8,eps0=eps0,fc=fcp,ts=ts,Es=Es,fy=fy)
    Pc,Rc,*_=base.concrete(D,q,c,tol=1e-7,q0=q0)
    Ps,Rs=loc.steel_local_resultants(D,q,c,q0,deg=deg,rmax=6.25,tol=2e-9)
    return dict(P_MN=(Pc+Ps)/1e6,Rq_MNmm=(Rc+Rs)/1e6,Pc_MN=Pc/1e6,Ps_MN=Ps/1e6)

if __name__=='__main__':
    print('Z6 small-slope checkpoints')
    for q in (0.0058975999,0.0073561,0.01,0.015,0.02):
        print(q,small_slope(9000.,12000.,q))
    print('\nLinear mode separation')
    for name,(a,b,h,ns) in CASES.items():
        Pyth,pcr=zhou_stiff(a,b,h,ns); p11=pcr(1,1)
        print(name,'Pcr11_MN',p11/1e6,'lambda',math.sqrt(Pyth/p11),
              'P21/P11',pcr(2,1)/p11,'P31/P11',pcr(3,1)/p11,'P12/P11',pcr(1,2)/p11)
    print('\nNonlinear connected-branch q brackets')
    for case,Ds in BRACKETS.items():
        for D,(q1,q2) in Ds.items():
            r1=current_total(case,D,q1,20); r2=current_total(case,D,q2,20)
            q=q1-r1['Rq_MNmm']*(q2-q1)/(r2['Rq_MNmm']-r1['Rq_MNmm'])
            p=r1['P_MN']+(q-q1)*(r2['P_MN']-r1['P_MN'])/(q2-q1)
            print(case,D,'q~',q,'P~',p,'bracket',r1['Rq_MNmm'],r2['Rq_MNmm'])
