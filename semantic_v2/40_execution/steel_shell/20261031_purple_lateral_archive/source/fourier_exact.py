"""Exact integration for *finite* trigonometric polynomials on X,Y in [0,pi].
No spatial sampling or quadrature.  Functions are dictionaries of complex
Fourier coefficients for exp(1j*(k*X+l*Y)).
"""
import math
from functools import lru_cache

PI=math.pi

def trim(a):
    return {k:v for k,v in a.items() if abs(v)>1.e-25}

def const(v=1.):return {(0,0):complex(v)} if v else {}

def add(a,b,fa=1.,fb=1.):
    o={k:fa*v for k,v in a.items()}
    for k,v in b.items():o[k]=o.get(k,0j)+fb*v
    return trim(o)

def scale(a,s):return trim({k:v*s for k,v in a.items()})

def mul(a,b):
    o={}
    for (k,l),v in a.items():
        for (m,n),u in b.items():
            key=(k+m,l+n);o[key]=o.get(key,0j)+v*u
    return trim(o)

def sinfreq(k,axis):
    u=(k,0) if axis=='x' else (0,k)
    return {u:-.5j,(-u[0],-u[1]):.5j}

def cosfreq(k,axis):
    u=(k,0) if axis=='x' else (0,k)
    return {u:.5,(-u[0],-u[1]):.5}

def deriv(a,axis,length):
    i=0 if axis=='x' else 1
    return trim({key:val*1j*key[i]*PI/length for key,val in a.items()})

@lru_cache(None)
def oned(k):
    if k==0:return 1.+0j
    # (1/pi) integral_0^pi exp(i*k*X) dX.
    return ((-1)**k-1)/(1j*k*PI)

def mean(a):
    val=sum(v*oned(k)*oned(l) for (k,l),v in a.items())
    if abs(val.imag)>1e-8*max(1.,abs(val.real)):
        raise ArithmeticError(f'Fourier integral is not real: {val}')
    return float(val.real)

def inner(a,b):return mean(mul(a,b))

def norm2(a):return inner(a,a)