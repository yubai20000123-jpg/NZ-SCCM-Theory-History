"""Transverse-free purple Lagrange projection for one two-wave steel shell.

Equation origins: 2026-10-25 purple handoff (signed Lagrange 7-node,
projected C-H-C Mises, clipped chord and vertex splitting, elastic D recovery)
and the user-locked additional constraint mean transverse membrane force=0.

Only proposed extension: two-modal membrane-work capacity, explicitly marked.
No Gauss/Simpson/surface grid and no FEM fit. Given axial d, unknown W,A and
nonlinearly condensed e_perp. Coordinate x transverse, y compression.
"""
from pathlib import Path
import sys
# self-contained project import
from purple_projection_kernel import Model as OldModel, Params, vadd, vscale, vdot_integral, vd, f, np, math
from scipy.optimize import root,least_squares

class Model(OldModel):
    def __init__(self,p):
        super().__init__(p)
        # Replace old uniform base [nu,-1,0] by [0,-1,0] and independent
        # transverse [1,0,0]. Recompute affine elastic condensation in exactly
        # the same six in-plane Ritz functions.
        self.base=[[{},f.const(-1),{}],[f.const(),{},{}],self.GG,self.GL,self.LL]
        K=np.array([[vdot_integral(u,v,self.C,f.mean) for v in self.modes] for u in self.modes])
        B=np.array([[vdot_integral(u,v,self.C,f.mean) for v in self.base] for u in self.modes])
        self.Kplan=K
        self.cond=np.linalg.solve(K,-B)
        self.basis=[]
        for i in range(5):
            result=self.base[i]
            for j in range(len(self.modes)):
                result=vadd(result,vscale(self.modes[j],self.cond[j,i]))
            self.basis.append(result)
        self.m1=np.zeros((7,5,3));self.Q00=np.zeros((7,5,5));self.Q01=np.zeros((7,5,2))
        for j in range(7):
            for i in range(5):
                for k in range(3):self.m1[j,i,k]=self.weighted(self.basis[i][k],j)/self.omega[j]
                for ii in range(5):
                    self.Q00[j,i,ii]=self.weighted(vd(self.basis[i],self.basis[ii],self.HC),j)/self.omega[j]
                for ii in range(2):
                    self.Q01[j,i,ii]=self.weighted(vd(self.basis[i],self.Kcur[ii],self.HC),j)/self.omega[j]
        # Current active membrane shape at each node = condensed geometric bases
        self.geom_reps=self.m1[:,2:,:]
        self.geom_means=np.array([[f.mean(comp) for comp in self.basis[i]] for i in range(2,5)])
        # Ritz critical strain for axial y, use exact bending and geometric energy.
        self.ecr_modes=[]
        for wave in (self.phi,self.psi):
            gy=f.deriv(wave,'y',p.a)
            den=p.E*f.mean(f.mul(gy,gy))
            idx=len(self.ecr_modes)
            self.ecr_modes.append(self.Dexact[idx,idx]/(12*den))
        self.ecr_modes=np.array(self.ecr_modes)

    def evaluate(self,d,W,A,e_perp=0.,cap=True):
        p=self.p
        U=p.W0+W;L=p.A0+A
        q0=np.array([d,e_perp,U**2-p.W0**2,U*L-p.W0*p.A0,L**2-p.A0**2])
        dW=np.array([0,0,2*U,L,0.]);dA=np.array([0,0,0,U,2*L])
        kv=np.array([W,A])
        n=[];m=[];I2=[];Misesmin=[]
        for j in range(7):
            # Keep original purple material algorithm, *not* a replacement J2.
            try:nn,mm,ec,poly=self.solve_section(j,q0,kv)
            except ValueError as exc:
                return {'ok':False,'cause':str(exc)}
            n.append(nn);m.append(mm);I2.append(ec)
            C,B,Aa=poly
            vals=[Aa+B*x+C*x*x for x in [-.5,.5]]
            if C>0 and -.5<(-B/(2*C))<.5:vals.append(Aa-B*B/(4*C))
            Misesmin.append(min(vals))
        n=np.asarray(n);m=np.asarray(m)
        chi=12*np.dot(self.omega,I2)
        # Scalar deviation inspired by *original purple* eta|a_j-corth|:
        # axial geometric membrane strain minus mean axial+nu*transverse.
        geom=np.einsum('k,jkl->jl',q0[2:],self.geom_reps)
        geom_mean=np.einsum('k,kl->l',q0[2:],self.geom_means)
        dev=np.abs(geom[:,1]-(geom_mean[1]+p.nu*geom_mean[0]))
        parts=[]
        for ii,dr in enumerate((dW,dA)):
            dk=np.array([float(ii==0),float(ii==1)])
            de=np.einsum('k,jkl->jl',dr,self.m1)
            dkb=np.einsum('k,jkl->jl',dk,self.mb)
            Rmem=float(np.sum(self.omega*np.sum(n*de,axis=1)))
            Rbend=float(np.sum(self.omega*np.sum(m*dkb,axis=1)))
            Rextra=float((dk@self.Dmissing@kv)*chi/12)
            # Proposed mode-aware capacity extension, NOT an identity of purple.
            Rcap=0.
            if cap:
                G_mean=np.einsum('k,kl->l',dr[2:],self.geom_means)
                cq=G_mean[1]+p.nu*G_mean[0]
                independent=np.sum(n*de,axis=1)-cq*n[:,1]
                gj=np.maximum(0.,1.-self.ecr_modes[ii]/np.maximum(dev,1e-30))
                Rcap=float(-np.dot(self.omega,gj*np.maximum(independent,0.)))
            parts.append([Rmem,Rbend,Rextra,Rcap])
        force=-float(np.dot(self.omega,n[:,1]))*p.b*p.t/1e6
        return {'ok':True,'R':np.sum(parts,axis=1),'parts':np.array(parts),
                'Nperp':float(np.dot(self.omega,n[:,0])), 'Nax':float(np.dot(self.omega,n[:,1])),
                'MN':force,'chi':chi,'Misesmin':min(Misesmin),
                'q0':q0,'n':n,'m':m,'ecr':self.ecr_modes}

    def residual3(self, d, W,A,eperp,cap=True):
        st=self.evaluate(d,W,A,eperp,cap)
        if not st['ok']:return np.array([1e5]*3)
        s=self.p.E*self.p.t/self.p.b**2
        return np.r_[st['R']/s,st['Nperp']/self.p.E*1e3]

    def solve_fixed(self,d,W,A,seed=None):
        # Mean-transverse force is a genuine nonlinear scalar equation; if
        # a root is found it is NOT replaced with a linear Poisson expression.
        from scipy.optimize import brentq
        if seed is None:seed=self.p.nu*d
        grid=np.linspace(-0.008,0.008,81)
        vals=[]
        for z in grid:
            st=self.evaluate(d,W,A,z)
            if st['ok'] and st['Misesmin']>=-1e-7:vals.append((z,st['Nperp']))
        roots=[]
        for (lo,a),(hi,b) in zip(vals[:-1],vals[1:]):
            if a*b<0 and hi-lo<.0003:
                try:roots.append(brentq(lambda x:self.evaluate(d,W,A,x)['Nperp'],lo,hi))
                except ValueError:pass
        if not roots:return None
        ep=min(roots,key=lambda t:abs(t-seed))
        return ep,self.evaluate(d,W,A,ep)


def demonstrate():
    for b in [2500.,5000.]:
        mod=Model(Params(b=b,a=b))
        print('SIZE',b,'epscr Ritz global/local',mod.ecr_modes,
              'weights sum',np.sum(mod.omega),
              'cond d,eperp',np.max(abs(mod.cond[:,:2])))
        for d,W,A in [(0.0004,b*.002,0.05),(0.0008,b*.006,0.5),(0.0012,b*.008,1.)]:
            ans=mod.solve_fixed(d,W,A)
            if ans is None:
                print('NO transverse root',d,W,A)
            else:
                ep,st=ans
                print('FIXED',f'd={d:.6g}',f'W={W:.4g}',f'A={A:.4g}',
                      f'e_perp={ep:.9g}',f'Nperp={st["Nperp"]:.5g}',
                      f'P_MN={st["MN"]:.8g}',f'Misesmin={st["Misesmin"]:.6g}',
                      f'R={st["R"]}')
if __name__=='__main__':demonstrate()