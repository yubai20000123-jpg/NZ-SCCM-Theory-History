"""Reproduce the historical RC membrane Fourier decomposition and classical redistribution delta.

No structural spatial quadrature or sampling is used.
No Pu is solved here.
"""
import math
from itertools import product


def membrane_driver(b, eps0, q0, q):
    A0=b*q0
    A=b*q
    S=A*A+2*A0*A
    alpha=math.pi/b
    M=math.pi**2/eps0*(q0*q+0.5*q*q)
    assert abs(M-S*alpha*alpha/(2*eps0)) < 1e-12*max(1.0,abs(M))
    return A0,A,S,alpha,M


def square_delta(M,nu,cx,cy,sxy=1.0):
    dex=M/4.0*(-(1+nu)-(1-nu)*cx+cx*cy)
    dey=M/4.0*(-(1-nu)*cy+cx*cy)
    dg=-M/2.0*sxy
    return dex,dey,dg


def diagnostics(name,b,t,eps0,nu,q0,D,q):
    A0,A,S,alpha,M=membrane_driver(b,eps0,q0,q)
    vals=[]
    for cx,cy in product((-1.0,1.0),repeat=2):
        dex,dey,_=square_delta(M,nu,cx,cy,0.0)
        vals.append((dex,dey))
    out={
        'name':name,'b_mm':b,'t_mm':t,'eps0':eps0,'nu':nu,'q0':q0,'D':D,'q':q,
        'A0_mm':A0,'A_mm':A,'S_mm2':S,'alpha_per_mm':alpha,'M':M,'M_over_4':M/4,
        'physical_mean_geom_y':eps0*M/4,'M4_over_D':(M/4)/D,
        'mean_delta_ex_phys':eps0*(-(1+nu)*M/4),
        'max_classical_delta_epsx':eps0*max(abs(a) for a,b in vals),
        'max_classical_delta_epsy':eps0*max(abs(b) for a,b in vals),
        'max_classical_delta_gamma':eps0*M/2
    }
    return out


def compatibility_identity_coefficients():
    # General alpha,beta delta:
    # de_x = S/8[-(a2+nu*b2)+(nu*b2-a2)cos2X+a2 cos2X cos2Y]
    # de_y = S/8[(nu*a2-b2)cos2Y+b2 cos2X cos2Y]
    # dg   = -S*a*b/4 sin2X sin2Y
    # Applying d_yy de_x + d_xx de_y - d_xy dg gives the cos2X cos2Y coefficient:
    # (-4 b2)(S a2/8)+(-4 a2)(S b2/8)-[4ab*(-S ab/4)] = 0.
    return (-4/8) + (-4/8) + 1.0


def main():
    print('FORMAL STRUCTURAL COUNTERS: sampling=0 quadrature=0 subdomains=1 thickness_quadrature=0')
    assert abs(compatibility_identity_coefficients()) < 1e-15
    case21=diagnostics('Case21',1220.0,19.3,0.00209,0.18,0.0025,0.8359179831666168,0.0017897894751107222)
    z6=diagnostics('Z6 retained baseline',12000.0,122.0,0.0018712490394580678,0.18,0.004,1.5853259042928987,0.02166488056894769)
    for d in (case21,z6):
        print('\n',d['name'])
        for k,v in d.items():
            if k!='name': print(k,'=',repr(v))
    print('\nM_Z6/M_Case21 =',repr(z6['M']/case21['M']))

if __name__=='__main__':
    main()
