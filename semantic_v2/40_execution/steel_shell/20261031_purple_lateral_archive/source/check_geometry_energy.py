from rebuild_lateral import Model,Params,vdot_integral,f,np

def energy(mod,d,W,A,h):
 p=mod.p;U=p.W0+W;L=p.A0+A
 q=np.array([d,h,U*U-p.W0*p.W0,U*L-p.W0*p.A0,L*L-p.A0*p.A0])
 v=[{} for _ in range(3)]
 for i in range(5):
  for k in range(3): v[k]=f.add(v[k],f.scale(mod.basis[i][k],q[i]))
 kcur=[{} for _ in range(3)]
 for i,amt in enumerate((W,A)):
  for k in range(3):kcur[k]=f.add(kcur[k],f.scale(mod.Kcur[i][k],amt))
 q_m=np.einsum("i,jik->jk",q,mod.m1)
 return (sum(mod.omega[j] * (q_m[j]@mod.C@q_m[j]) for j in range(7))/2 + vdot_integral(kcur,kcur,mod.C,f.mean)/24)

for b in [2500.,5000.]:
 m=Model(Params(b=b,a=b));d=.000005;W=.013;A=.002;h=.000001
 st=m.evaluate(d,W,A,h,cap=False)
 print('b',b,'chi',st['chi'],'max mismatch on linear elastic',end=' ')
 for k in [0,1,2]:
  x=[W,A,h];step=1e-5 if k<2 else 1e-7
  xx=x.copy();xx[k]+=step;yy=x.copy();yy[k]-=step
  der=(energy(m,d,*xx)-energy(m,d,*yy))/(2*step)
  reported=st['R'][k] if k<2 else st['Nperp']
  print(k,der,reported,abs(der-reported)/max(abs(der),abs(reported),1e-14),end='; ')
 print()