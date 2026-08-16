"""NZ-SCCM five-term membrane-condensation exact reproducer.
Timestamp: 2026-08-16 19:12 +08:00

This script reproduces the exact elastic five-coordinate condensation, the
Airy/FvK stress recovery, and the Case21/Z6 benchmark coordinate amplitudes.
It performs no structural spatial numerical quadrature. SymPy antiderivatives
are used only to verify the closed-form coefficient-space identities.

It does NOT execute the still-open R10-MSAC-RC1 nested target-functional
runtime and does NOT calculate a new Pu.
"""
import sympy as sp
import numpy as np

X,Y,nu,M,D=sp.symbols('X Y nu M D', real=True)
cX=sp.cos(2*X); cY=sp.cos(2*Y)
sX=sp.sin(2*X); sY=sp.sin(2*Y)

B=[
    sp.Matrix([1,0,0]),
    sp.Matrix([cX,0,0]),
    sp.Matrix([cX*cY,0,-sX*sY]),
    sp.Matrix([0,cY,0]),
    sp.Matrix([0,cX*cY,-sX*sY]),
]

eM=sp.Matrix([
    (1+cX-cY-cX*cY)/4,
    (1-cX+cY-cX*cY)/4,
    sX*sY/2,
])
eD=sp.Matrix([nu,-1,0])

def bilinear(a,b):
    return (a[0]*b[0]+a[1]*b[1]
            +nu*(a[0]*b[1]+a[1]*b[0])
            +(1-nu)*a[2]*b[2]/2)

def exact_int(expr):
    return sp.simplify(sp.integrate(sp.integrate(sp.expand_trig(expr),(X,0,sp.pi)),(Y,0,sp.pi)))

K=sp.Matrix([[exact_int(bilinear(bi,bj)) for bj in B] for bi in B])
fM=sp.Matrix([exact_int(bilinear(bi,eM)) for bi in B])
fD=sp.Matrix([exact_int(bilinear(bi,eD)) for bi in B])
r_per_M=sp.simplify(-K.inv()*fM)

K_expected=sp.pi**2*sp.Matrix([
    [1,0,0,0,0],
    [0,sp.Rational(1,2),0,0,0],
    [0,0,(3-nu)/8,0,(1+nu)/8],
    [0,0,0,sp.Rational(1,2),0],
    [0,0,(1+nu)/8,0,(3-nu)/8],
])
fM_expected=sp.pi**2*sp.Matrix([(1+nu)/4,(1-nu)/8,-sp.Rational(1,8),(1-nu)/8,-sp.Rational(1,8)])
r_expected=sp.Matrix([-(1+nu)/4,-(1-nu)/4,sp.Rational(1,4),-(1-nu)/4,sp.Rational(1,4)])

assert sp.simplify(K-K_expected)==sp.zeros(5)
assert sp.simplify(fM-fM_expected)==sp.zeros(5,1)
assert fD==sp.zeros(5,1)
assert sp.simplify(r_per_M-r_expected)==sp.zeros(5,1)
assert sp.simplify(K.det()-sp.pi**10*(1-nu)/32)==0

# Reconstruct reduced strain and plane-stress response.
r0,r20,r22,s02,s22=list(M*r_expected)
ex_old=nu*D+M*(1+cX-cY-cX*cY)/4
ey_old=-D+M*(1-cX+cY-cX*cY)/4
g_old=M*sX*sY/2
ex=sp.simplify(ex_old+r0+r20*cX+r22*cX*cY)
ey=sp.simplify(ey_old+s02*cY+s22*cX*cY)
g=sp.simplify(g_old-(r22+s22)*sX*sY)

sx=sp.trigsimp((ex+nu*ey)/(1-nu**2))
sy=sp.trigsimp((nu*ex+ey)/(1-nu**2))

assert sp.trigsimp(sx + M*cY/4)==0
assert sp.trigsimp(sy - (-D+M*sp.sin(X)**2/2))==0
assert sp.simplify(g)==0

# General-D15 basis identities.
uX,vY=sp.symbols('u v', real=True)
assert sp.expand((1-2*uX**2)*(1-2*vY**2)) == 1-2*uX**2-2*vY**2+4*uX**2*vY**2
# shear target: g has cosX cosY factor, and -sin2X sin2Y has another;
# product uses cos^2X cos^2Y=(1-u^2)(1-v^2), hence finite polynomial.
shear_reduced=sp.expand(-4*uX*vY*(1-uX**2)*(1-vY**2))

nu0=.18
Kbar=np.array(sp.N((K/sp.pi**2).subs(nu,nu0)),float)
eigs=np.linalg.eigvalsh(Kbar)
cond=float(np.linalg.cond(Kbar))

benchmarks={
    'Case21': {'b':1220.0,'eps0':.00209,'M':.02869338081034484},
    'Z6': {'b':12000.0,'eps0':.0018712490394580678,'M':1.6948726156196714},
}
for name,d in benchmarks.items():
    mm=d['M']
    rv=np.array([-(1+nu0)*mm/4,-(1-nu0)*mm/4,mm/4,-(1-nu0)*mm/4,mm/4])
    disp=np.r_[d['eps0']*d['b']*rv[0], d['eps0']*d['b']/(2*np.pi)*rv[1:]]
    d['r']=rv.tolist(); d['displacement_scales_mm']=disp.tolist()

print('K/pi^2 =')
sp.pprint(sp.simplify(K/sp.pi**2))
print('fM/pi^2 =', list(sp.simplify(fM/sp.pi**2)))
print('fD/pi^2 =', list(sp.simplify(fD/sp.pi**2)))
print('r/M =', list(r_per_M))
print('detK =', sp.factor(K.det()))
print('nu=.18 eigenvalues =', eigs)
print('nu=.18 cond2 =', cond)
print('sigma_x/(E eps0) =', sx)
print('sigma_y/(E eps0) =', sy)
print('gamma_xy/eps0 =', g)
print('General-D15 shear reduced polynomial =', shear_reduced)
print('benchmarks =', benchmarks)
print('formal_spatial_sampling=0')
print('formal_spatial_quadrature=0')
print('formal_spatial_subdomains=1')
print('formal_thickness_quadrature=0')
print('RC1_nested_target_runtime=OPEN')
print('new_Pu=NOT_RUN')
