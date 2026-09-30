import sys,math,time,warnings
from scipy.integrate import quad, IntegrationWarning
sys.path.insert(0,'/mnt/data/m8_work')
import UCFT_M8_production_UHPC_law as plaw
import UCFT_M8_fourier_rational_Y_operator as fy
law=plaw.build_production_law()
weights={'1':fy.FS.const(1),'c7':fy.FS.from_trig(0,{7:1},{}),'s9':fy.FS.from_trig(0,{}, {9:1})}
cases=[
 (.0007,{2:.0005,7:-.0012,9:.0007,16:.00025},{1:.0010,7:.0003,9:-.00025},5e-5),
 (-.0010,{2:.0012,5:.0008,12:-.0005},{1:.0005,7:-.0007},8e-5),
 (.0032,{2:-.0011,7:.0013,16:-.0004},{1:.0008,9:.00055},1.1e-4),
]
rows=[];maxerr=0
warnings.simplefilter('ignore',IntegrationWarning)
for ci,(a0,cc,ss,ch) in enumerate(cases):
    st=time.time();got,cuts=fy.generalized_y_moments(law,a0,cc,ss,ch,42.,weights);dt=time.time()-st
    def point(Y):
        em=a0+sum(a*math.cos(k*Y) for k,a in cc.items())+sum(b*math.sin(k*Y) for k,b in ss.items())
        chi=ch*math.sin(Y)
        if abs(chi)<1e-13:return 42*law.stress(em),0.
        ep=em+21*chi; en=em-21*chi; Fp,Hp=law.FH(ep); Fm,Hm=law.FH(en); dF=Fp-Fm
        return dF/chi,(Hp-Hm-em*dF)/(chi*chi)
    for kind,wname in [('N','1'),('N','c7'),('N','s9'),('M','1'),('M','c7'),('M','s9')]:
        def f(Y):
            N,M=point(Y); w=1 if wname=='1' else (math.cos(7*Y) if wname=='c7' else math.sin(9*Y))
            return (N if kind=='N' else M)*w
        ref=quad(f,0,math.pi,points=cuts[1:-1],epsabs=3e-7,epsrel=3e-10,limit=2000)[0]
        v=got[kind+'_'+wname]; err=abs(v-ref)/max(1,abs(ref)); maxerr=max(maxerr,err)
        rows.append((ci,kind,wname,len(cuts)-1,v,ref,err,dt))
print('MAX_REL_SCALED',maxerr)
for r in rows:print(r)
