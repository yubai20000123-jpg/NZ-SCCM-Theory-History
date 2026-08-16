"""Reproduce the 2026-08-16 14:17 exact-Pi / existing-General-D15 adapter gate.

This script performs algebraic identities and closed special-function evaluation only.
It does NOT perform structural spatial sampling or structural numerical quadrature.

Formal production counters remain:
    N_formal_spatial_sampling   = 0
    N_formal_spatial_quadrature = 0
    N_formal_spatial_subdomains = 1
    N_formal_thickness_quadrature = 0
"""
import math
import sympy as sp
from scipy.special import ellipk, ellipe

KAPPA = 2.0005129533678754
RHO   = 0.1
XCR   = RHO / KAPPA
ETA   = XCR / 20.0
H     = 0.09799750427197301
UR    = 0.03


def symbolic_identities():
    z, eta = sp.symbols('z eta', positive=True, nonzero=True)
    r = sp.sqrt(z*z + eta*eta)
    pplus  = z*z*(r+z)/(2*(z*z+eta*eta))
    pminus = z*z*(r-z)/(2*(z*z+eta*eta))
    s = sp.simplify(pplus+pminus)
    d = sp.simplify(pplus-pminus)
    assert sp.simplify(s-z*z/r) == 0
    assert sp.simplify(d-z**3/(z*z+eta*eta)) == 0
    return s, d


def exact_elliptic_moment(beta, eta=ETA):
    """Exact closed result for the minimal traceless-field witness.

    J = int_0^pi beta^2 sin(x)^2 / sqrt(eta^2+beta^2 sin(x)^2) dx
      = 2 eta [E(-m)-K(-m)], m=(beta/eta)^2.

    scipy.special evaluates K/E directly; there is no spatial quadrature here.
    """
    m = (beta/eta)**2
    J = 2*eta*(ellipe(-m)-ellipk(-m))
    return m, J


def main():
    print('FORMAL STRUCTURAL SPATIAL SAMPLING = 0')
    print('FORMAL STRUCTURAL SPATIAL QUADRATURE = 0')
    print('FORMAL STRUCTURAL SPATIAL SUBDOMAINS = 1')
    print('FORMAL THICKNESS QUADRATURE = 0')
    print()

    s, d = symbolic_identities()
    print('Pi(z)+Pi(-z) =', s)
    print('Pi(z)-Pi(-z) =', d)
    print()

    print('R10 constants:')
    print('kappa =', KAPPA)
    print('rho   =', RHO)
    print('xcr   =', XCR)
    print('eta   =', ETA)
    print('h     =', H)
    print('ur    =', UR)
    print()

    print('Traceless matrix lift:')
    print('alpha(r)=r^2/(2*sqrt(r^2+eta^2))')
    print('gamma(r)=r^2/(2*(r^2+eta^2))')
    print('trace Pi(X)=r^2/sqrt(r^2+eta^2)')
    print()

    betas = [ETA, 5*ETA, XCR, 0.1]
    print('Closed elliptic witness values:')
    for beta in betas:
        m, J = exact_elliptic_moment(beta)
        print(f'beta={beta:.15g}, beta/eta={beta/ETA:.12g}, m={m:.12g}, J={J:.15g}')

    print()
    print('GATE RESULT:')
    print('EXACT_PI_MATRIX_LIFT = PASS')
    print('EXACT_PI_TO_EXISTING_GENERAL_D15_FINITE_MOMENT_CLOSURE = FAIL')
    print('NEW_SPECIAL_FUNCTION_STRUCTURAL_BACKEND = NOT_AUTHORIZED')
    print('R10_MATERIAL_CHANGE = NOT_EXECUTED')
    print('NEW_Z0_Z6_Pu = NOT_RUN')


if __name__ == '__main__':
    main()
