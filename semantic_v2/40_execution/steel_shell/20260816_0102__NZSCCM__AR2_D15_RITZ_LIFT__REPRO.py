"""NZ-SCCM 20260816_0102 AR2 boundary-admissible D15 Ritz-lift reproducer.

NO spatial sampling. NO spatial quadrature. NO collocation.
Every integral is evaluated from finite Fourier coefficients and the exact
antiderivative int exp(i*k*theta)dtheta.

This script validates the elastic coefficient-space lift only. It does not
run R10/N48 and does not calculate Pu.
"""
import cmath, math
import numpy as np

PI=math.pi
NU=.18


def add(a,b,s=1.0):
    c=dict(a)
    for k,v in b.items():
        c[k]=c.get(k,0.0)+s*v
        if abs(c[k])<1e-14:c.pop(k,None)
    return c

def scale(a,s):return {k:s*v for k,v in a.items() if abs(s*v)>=1e-14}

def mul(a,b):
    c={}
    for (i,j),v in a.items():
        for (r,s),w in b.items():
            k=(i+r,j+s);c[k]=c.get(k,0.0)+v*w
    return {k:v for k,v in c.items() if abs(v)>=1e-14}

def cs(n,axis):
    if n==0:return {(0,0):1.0}
    return {(n,0):.5,(-n,0):.5} if axis=='x' else {(0,n):.5,(0,-n):.5}

def sn(n,axis):
    if n==0:return {}
    return {(n,0):1/(2j),(-n,0):-1/(2j)} if axis=='x' else {(0,n):1/(2j),(0,-n):-1/(2j)}

def iexp(k,L=PI):
    if k==0:return L
    return (cmath.exp(1j*k*L)-1)/(1j*k)

def integ(a):
    z=sum(v*iexp(i)*iexp(j) for (i,j),v in a.items())
    if abs(z.imag)>1e-9:raise RuntimeError(('unexpected imaginary integral',z))
    return z.real

def inner(A,B,nu=NU):
    ex1,ey1,g1=A;ex2,ey2,g2=B
    q=mul(ex1,ex2)
    q=add(q,mul(ey1,ey2))
    q=add(q,mul(ex1,ey2),nu)
    q=add(q,mul(ey1,ex2),nu)
    q=add(q,mul(g1,g2),(1-nu)/2)
    return integ(q)

# Unit Gamma = pi^2 S/b^2 geometric strain source on the square AR2 halfwave.
sx,cx=sn(1,'x'),cs(1,'x');sy,cy=sn(1,'y'),cs(1,'y')
G=(scale(mul(mul(cx,cx),mul(sy,sy)),.5),
   scale(mul(mul(sx,sx),mul(cy,cy)),.5),
   mul(mul(sx,cx),mul(sy,cy)))
D=({}, {(0,0):-1.0}, {})


def basis(R,S):
    out=[]
    # u=(b/pi)U cos(rX)[1-cos(sY)], r odd
    for ir in range(R):
        r=2*ir+1
        for s in range(1,S+1):
            one_minus_cos=add({(0,0):1.0},cs(s,'y'),-1)
            B=(scale(mul(sn(r,'x'),one_minus_cos),-r),
               {},
               scale(mul(cs(r,'x'),sn(s,'y')),s))
            out.append((f'u_r{r}_s{s}',B))
    # v=(b/pi)V cos(rX)sin(sY), r even
    for ir in range(R):
        r=2*ir
        for s in range(1,S+1):
            B=({},
               scale(mul(cs(r,'x'),cs(s,'y')),s),
               scale(mul(sn(r,'x'),sn(s,'y')),-r))
            out.append((f'v_r{r}_s{s}',B))
    return out


def solve(R,S):
    B=basis(R,S);n=len(B)
    K=np.zeros((n,n));fG=np.zeros(n);fD=np.zeros(n)
    for i,(_,bi) in enumerate(B):
        fG[i]=inner(bi,G);fD[i]=inner(bi,D)
        for j in range(i+1):
            K[i,j]=K[j,i]=inner(bi,B[j][1])
    cG=np.linalg.solve(K,-fG);cD=np.linalg.solve(K,-fD)
    QGG=inner(G,G)+2*cG@fG+cG@K@cG
    QDD=inner(D,D)+2*cD@fD+cD@K@cD
    QDG=inner(D,G)+cD@fG+cG@fD+cD@K@cG
    return B,K,cG,cD,QGG,QDD,QDG


def main():
    print('FORMAL_SPATIAL_SAMPLING=0')
    print('FORMAL_SPATIAL_QUADRATURE=0')
    print('FORMAL_SPATIAL_SUBDOMAINS=1')
    print('Q_DD_restrained=',PI**2)
    print('Q_DD_free_poisson=',(1-NU**2)*PI**2)
    for R in [1,2,3,4,5,6,8,10,12]:
        B,K,cG,cD,QGG,QDD,QDG=solve(R,R)
        print('LEVEL',R,'nmem',len(B),'QGG',QGG,'QDD',QDD,'QDG',QDG,'condK',np.linalg.cond(K))
        if R==4:
            for i,(name,_) in enumerate(B):
                print('R4COEF',name,'cG',cG[i],'cD',cD[i])
    print('ELASTIC_RELATION: r = cD*D + cG*(Gamma/eps0) = cD*D + 2*cG*M')
    print('NONLINEAR_RULE: coefficients are independent generalized coordinates; do not freeze cD/cG.')
    print('NEW_PU=NOT_CALCULATED')

if __name__=='__main__':main()
