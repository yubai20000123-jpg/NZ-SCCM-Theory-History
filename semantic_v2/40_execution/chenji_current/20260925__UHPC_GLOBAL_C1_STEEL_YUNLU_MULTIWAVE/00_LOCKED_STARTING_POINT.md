# Locked starting point: global UHPC law + Yun-Lu/Chen-Ji steel multiwave

Date: 2026-09-25

## 1 UHPC

Do not use abs(epsilon), epsilon_plus, epsilon_minus, Heaviside, max/min, or an externally selected tension/compression branch in the formal constitutive law.

Target: one ordinary real-variable function sigma_U(epsilon), using only epsilon as the state argument, fitted/constructed to reproduce the full tension and compression branches while satisfying sigma(0)=0 and sigma'(0)=Ec and remaining pole-free over the physical strain interval.

The current signed-C1 piecewise law remains reference data, not the final formal single-expression law.

## 2 Steel shell geometry

"Multiwave" here means a single whole-face amplitude with symbolic wave counts N,m, not a sum of independent modal amplitudes.

TOP initial:
Ws0+ = b q0 sin(pi x/b) sin(pi y/a_h)
      + A0+ [1-cos(2N pi x/b)][1-cos(2m pi y/a_h)].

TOP current:
Ws+ = b(q0+q) sin(pi x/b) sin(pi y/a_h)
     +(A0+ + A+) [1-cos(2N pi x/b)][1-cos(2m pi y/a_h)].

BOTTOM uses the corresponding minus local sign if outward directions are defined oppositely.

No normalized width-thickness parameter is introduced a priori. Retain b,a_h,t_s,Es,nu_s,fy,N,m,q0,q,A0,A and reduce only after the algebra reveals repeated combinations.

## 3 Exact Marguerre/Karman source decomposition

Let g=sin(pi x/b)sin(pi y/a_h), phi=[1-cos(2N pi x/b)][1-cos(2m pi y/a_h)],
G0=b q0, G=b(q0+q), At0=A0, At=A0+A.

For H(W)=W_xy^2-W_xx W_yy,

H(G g + At phi)-H(G0 g + At0 phi)
=(G^2-G0^2)(g_xy^2-g_xx g_yy)
+(G At-G0 At0)(2 g_xy phi_xy-g_xx phi_yy-phi_xx g_yy)
+(At^2-At0^2)(phi_xy^2-phi_xx phi_yy).

The three amplitudes are exactly:
G^2-G0^2=b^2(q^2+2q0 q),
G At-G0 At0=b[(q0+q)(A0+A)-q0 A0]=b(q0 A+q A0+q A),
At^2-At0^2=2A0 A+A^2.

This is the required GG + GL + LL decomposition for the Yun-Lu/Chen-Ji re-derivation.

## 4 Chen-Ji Figure 8.19 correction

The uploaded Figure 8.19 visibly contains post-peak/descending load-deflection branches. Therefore the prior blanket statement that "Chen-Ji has no descending branch" is withdrawn.

What remains true is narrower: the isolated elastic 8.65-8.67 relation px=pcr+C f^2 is monotone increasing. Figure 8.19 represents a fuller load-deflection construction than that isolated elastic relation. The exact mechanism/branch equations for A, A', B must be recovered from the surrounding original-book text before assigning the descending segment to a specific plastic or imperfection formula.

The steel route must therefore reproduce not only Yun-Lu's elastic postbuckling path but also audit the fuller Chen-Ji load-deflection construction that leads to Figure 8.19.
