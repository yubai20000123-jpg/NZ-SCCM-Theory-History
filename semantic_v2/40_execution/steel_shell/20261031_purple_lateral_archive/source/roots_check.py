from rebuild_lateral import Model, Params, np
from scipy.optimize import least_squares,brentq
import csv

def run_one(b):
 M=Model(Params(b=b,a=b))
 rows=[]
 scale=M.p.E*M.p.t/b**2
 for d in [.0001,.0004,.0008,.0012,.0026]:
  cand=[]
  for seedW in [b*.0005,b*.004,b*.015]:
   for seedA in [.05,.5,4.,20.]:
    def f(z):
     W,A,ep=z;st=M.evaluate(d,W,A,ep)
     if not st['ok']:return np.array([1e5]*3)
     return np.r_[st['R']/scale,st['Nperp']/M.p.E*1000]
    res=least_squares(f,[seedW,seedA,M.p.nu*d],bounds=([0,0,-.02],[b/2,b/5,.02]),max_nfev=180,ftol=1e-10,gtol=1e-10,xtol=1e-10)
    z=res.x; s=M.evaluate(d,*z)
    rr=f(z)
    if s['ok'] and np.linalg.norm(rr)<1e-6 and z[1]>1e-6 and s['Misesmin']>=-1e-6 and not any(np.linalg.norm(z-c[0])<.001 for c in cand):
     cand.append((z,s,'interior'))
  # boundary local A=0, transverse solve at each W
  def getw(w):
   ans=M.solve_fixed(d,w,0.)
   if ans is None:return None
   ep,st=ans
   return ep,st
  ws=np.linspace(0,.06*b,40)
  pairs=[(w,getw(w)) for w in ws];pairs=[x for x in pairs if x[1] is not None]
  for (lo,ar),(hi,br) in zip(pairs[:-1],pairs[1:]):
   if ar[1]['R'][0]*br[1]['R'][0]<0:
    def fwb(w):return getw(w)[1]['R'][0]
    try:w=brentq(fwb,lo,hi,xtol=1e-8)
    except Exception:continue
    ep,st=getw(w)
    if st['R'][1]>=-1e-8 and st['Misesmin']>=-1e-6:
     cand.append((np.array([w,0.,ep]),st,'boundary_A0'))
  print('b,d',b,d,'candidates',len(cand),flush=True)
  for z,st,kind in sorted(cand,key=lambda e:e[1]['MN']):
   print(kind,'W A ep',np.round(z,8),'MN',st['MN'],'R',st['R'],'Nperp',st['Nperp'],'qmin',st['Misesmin'],flush=True)
   rows.append(dict(b=b,d=d,W=z[0],A=z[1],eperp=z[2],MN=st['MN'],RW=st['R'][0],RA=st['R'][1],mean_perp=st['Nperp'],mises_min=st['Misesmin'],kind=kind))
 return rows
if __name__=='__main__':
 with open('/mnt/data/purple_rebuild_lateral_20261031/roots_2size.csv','w',newline='') as fh:
  allr=run_one(2500)+run_one(5000)
  dw=csv.DictWriter(fh,fieldnames=['b','d','W','A','eperp','MN','RW','RA','mean_perp','mises_min','kind']);dw.writeheader();dw.writerows(allr)