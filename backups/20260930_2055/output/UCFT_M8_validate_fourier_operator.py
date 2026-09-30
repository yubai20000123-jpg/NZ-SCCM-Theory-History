import sys,math,time
from scipy.integrate import quad
sys.path.insert(0,'/mnt/data/m8_work')
import UCFT_M4_UHPC_analytic_partition_kernel as m4
import UCFT_M8_fourier_rational_Y_operator as fy
law=m4.build_validation_law(); geom={'b':1600.,'a_h':3200.,'t_c':42.,'nu':.2,'q0':.0025}
weights={'1':fy.FS.const(1),'cos2':fy.FS.from_trig(0,{2:1},{}),'sin':fy.FS.from_trig(0,{}, {1:1})}
maxrel=0; rows=[]
states=[
 {'q':.001,'Ex':-.0004,'Ey':-.0012,'Bx':.0002,'By':-.0001,'Hx':.00008,'Hy':-.00006},
 {'q':.0515191313462447,'Ex':.0029443624571463744,'Ey':.00018544968306641058,'Bx':.0014475111372089415,'By':.0010284688522175555,'Hx':-.0026158113706380164,'Hy':.0015493814777209044},
 {'q':.032807145512058024,'Ex':.002407270167881826,'Ey':-.00044303155159391506,'Bx':.0026135203302271263,'By':.0022731999620282497,'Hx':-.0024152741416147367,'Hy':-.0021841868387959865},
]
for si,state in enumerate(states):
 for X in (.31,.87,1.43):
  for direction in ('x','y'):
   em,_,_,chi0=m4.directional_face_polynomials(X,state['q'],state['Ex'],state['Ey'],state['Bx'],state['By'],state['Hx'],state['Hy'],geom['b'],geom['a_h'],geom['t_c'],geom['nu'],geom['q0'],direction)
   B=-float(em.coef[2])/2;A=float(em.coef[0])-B
   got,cuts=fy.generalized_y_moments(law,A,{2:B},{},chi0,geom['t_c'],weights)
   ref=m4.y_moments_exact(law,X,state,geom,direction)
   err=max(abs(got['N_1']-ref['N_1'])/max(1,abs(ref['N_1'])),abs(got['N_cos2']-ref['N_cos2'])/max(1,abs(ref['N_cos2'])),abs(got['N_sin']-ref['N_sin'])/max(1,abs(ref['N_sin'])),abs(got['M_1']-ref['M_1'])/max(1,abs(ref['M_1'])),abs(got['M_cos2']-ref['M_cos2'])/max(1,abs(ref['M_cos2'])),abs(got['M_sin']-ref['M_sin'])/max(1,abs(ref['M_sin'])))
   maxrel=max(maxrel,err);rows.append(('baseline',si,X,direction,len(cuts)-1,err))
highcases=[
 (.0007,{2:.0005,7:-.0012,9:.0007,16:.00025},{1:.0010,7:.0003,9:-.00025},5e-5),
 (-.0010,{2:.0012,5:.0008,12:-.0005},{1:.0005,7:-.0007},8e-5),
]
hweights={'1':fy.FS.const(1),'c7':fy.FS.from_trig(0,{7:1},{}),'s9':fy.FS.from_trig(0,{}, {9:1})}
for ci,(a0,cc,ss,ch) in enumerate(highcases):
 st=time.time();got,cuts=fy.generalized_y_moments(law,a0,cc,ss,ch,42.,hweights);elapsed=time.time()-st
 def point(Y):
  em=a0+sum(a*math.cos(k*Y) for k,a in cc.items())+sum(b*math.sin(k*Y) for k,b in ss.items());chi=ch*math.sin(Y)
  if abs(chi)<1e-14:return 42*law.stress(em),0.
  ep=em+21*chi;en=em-21*chi;Fp,Hp=law.FH(ep);Fm,Hm=law.FH(en);dF=Fp-Fm
  return dF/chi,(Hp-Hm-em*dF)/(chi*chi)
 for kind,wname in [('N','1'),('N','c7'),('N','s9'),('M','1'),('M','c7'),('M','s9')]:
  def fun(Y):
   N,M=point(Y);w=1 if wname=='1' else (math.cos(7*Y) if wname=='c7' else math.sin(9*Y));return (N if kind=='N' else M)*w
  ref=quad(fun,0,math.pi,points=cuts[1:-1],epsabs=1e-7,epsrel=2e-10,limit=1000)[0]
  val=got[kind+'_'+wname];err=abs(val-ref)/max(1,abs(ref));maxrel=max(maxrel,err);rows.append(('high',ci,wname,kind,len(cuts)-1,err,elapsed))
print('MAX_REL_SCALED',maxrel)
for r in rows:print(r)
