# 02 — Full finite-harmonic Airy expansion, Galerkin closure, and raw-data UHPC screening

Date: 2026-09-25

## A. UHPC raw-data screening

Formal family (ordinary epsilon only):
u = epsilon/0.0035

sigma_U(epsilon)=
[151.9 u + a2 u^2 + ... + ap u^p] /
[1 + (b1 u + ... + br u^r)^2].

No abs(epsilon), positive/negative parts, Heaviside, max/min, or external branch switch occurs in the formal function. The denominator is >=1 for all real epsilon, hence has no real poles. sigma(0)=0 and sigma'(0)=Ec=43400 MPa are automatic.

Raw compression data used: the 30-row Abaqus table previously supplied by the user. Its second column is inelastic strain; total compression strain magnitude is epsilon_inel + sigma/Ec, then assigned negative sign. It starts 119.49 MPa, 0 inelastic strain; peaks at 141.1 MPa, 0.000248848 inelastic strain, giving total epsilon=-0.00350000007; and ends 12.5 MPa, 0.024211923 inelastic strain, giving total epsilon=-0.0244999414.

Raw tension data used: the 23-row Abaqus stress/cracking-strain table supplied by the user. Total tensile strain is epsilon_cr + sigma/Ec. The 7.3 MPa peak at cracking strain 0.000804 gives total epsilon=0.000972202765.

Nested screening found the first tested family with the correct global two-extrema topology (one compression peak, one tension peak), enforced origin tangent, no poles, and no spurious turning point to be p=5,r=3:

sigma_U(epsilon)=
[151.9u
-192.19420930u^2
+10424.16782943u^3
-8187.97997370u^4
+5190.98157296u^5]
/
[1+(14.18112359u+13.82202054u^2+12.68450845u^3)^2].

Its derivative has exactly two real zeros over the entire real axis:
epsilon=-0.003500000716, sigma=-141.0997784 MPa;
epsilon=+0.000972372123, sigma=+7.30000455 MPa.

Fit errors against the raw tables:
compression RMSE 4.04579 MPa, max absolute error 8.80889 MPa;
tension RMSE 0.313902 MPa, max absolute error 1.06853 MPa.

Lower tested families either could not reproduce the two peaks with acceptable raw-data fit or introduced extra extrema. This establishes p=5,r=3 only as the provisional lowest-order candidate within this pole-free squared-denominator family; it is not a universal minimum over every conceivable analytic family.

## B. Steel whole-face shape

alpha=pi/b, beta=pi/a_h,
g=sin(alpha x)sin(beta y),
phi=[1-cos(2N alpha x)][1-cos(2m beta y)].

TOP:
Ws0=b q0 g+A0 phi,
Ws=b(q0+q)g+(A0+A)phi.

Let
QG=q^2+2q0 q,
QGL=q0 A+q A0+q A,
QLL=2A0 A+A^2.

Compatibility source:
H(Ws)-H(Ws0)=b^2 QG HGG+b QGL HGL+QLL HLL.

HGG =
(alpha^2 beta^2/2)[cos(2 alpha x)+cos(2 beta y)].

HGL =
alpha^2 beta^2{
-(N-m)^2 sin[(2N+1)alpha x]sin[(2m+1)beta y]
+(N+m)^2 sin[(2N+1)alpha x]sin[(2m-1)beta y]
+(N+m)^2 sin[(2N-1)alpha x]sin[(2m+1)beta y]
-(N-m)^2 sin[(2N-1)alpha x]sin[(2m-1)beta y]
+2m^2 sin(alpha x)sin[(2m+1)beta y]
-2m^2 sin(alpha x)sin[(2m-1)beta y]
+2N^2 sin[(2N+1)alpha x]sin(beta y)
-2N^2 sin[(2N-1)alpha x]sin(beta y)
}.

HLL =
8N^2m^2 alpha^2 beta^2{
cos(2N alpha x)+cos(2m beta y)
-2cos(2N alpha x)cos(2m beta y)
-cos(4N alpha x)-cos(4m beta y)
+cos(4N alpha x)cos(2m beta y)
+cos(2N alpha x)cos(4m beta y)
}.

## C. Fully expanded Airy particular

Compatibility is nabla^4 Fp = Es [H(Ws)-H(Ws0)].

FGG contribution:
Es b^2 QG [
 beta^2/(32 alpha^2) cos(2alpha x)
+alpha^2/(32 beta^2) cos(2beta y)
].

FGL contribution:
Es b QGL alpha^2 beta^2 {
-(N-m)^2 sin[(2N+1)alpha x]sin[(2m+1)beta y] /
 [((2N+1)^2 alpha^2+(2m+1)^2 beta^2)^2]
+(N+m)^2 sin[(2N+1)alpha x]sin[(2m-1)beta y] /
 [((2N+1)^2 alpha^2+(2m-1)^2 beta^2)^2]
+(N+m)^2 sin[(2N-1)alpha x]sin[(2m+1)beta y] /
 [((2N-1)^2 alpha^2+(2m+1)^2 beta^2)^2]
-(N-m)^2 sin[(2N-1)alpha x]sin[(2m-1)beta y] /
 [((2N-1)^2 alpha^2+(2m-1)^2 beta^2)^2]
+2m^2 sin(alpha x)sin[(2m+1)beta y] /
 [(alpha^2+(2m+1)^2 beta^2)^2]
-2m^2 sin(alpha x)sin[(2m-1)beta y] /
 [(alpha^2+(2m-1)^2 beta^2)^2]
+2N^2 sin[(2N+1)alpha x]sin(beta y) /
 [((2N+1)^2 alpha^2+beta^2)^2]
-2N^2 sin[(2N-1)alpha x]sin(beta y) /
 [((2N-1)^2 alpha^2+beta^2)^2]
}.

FLL contribution:
Es QLL {
 m^2 beta^2/(2N^2 alpha^2) cos(2N alpha x)
+N^2 alpha^2/(2m^2 beta^2) cos(2m beta y)
-N^2m^2 alpha^2 beta^2/(N^2 alpha^2+m^2 beta^2)^2 cos(2N alpha x)cos(2m beta y)
-m^2 beta^2/(32N^2 alpha^2) cos(4N alpha x)
-N^2 alpha^2/(32m^2 beta^2) cos(4m beta y)
+N^2m^2 alpha^2 beta^2/[2(4N^2 alpha^2+m^2 beta^2)^2] cos(4N alpha x)cos(2m beta y)
+N^2m^2 alpha^2 beta^2/[2(N^2 alpha^2+4m^2 beta^2)^2] cos(2N alpha x)cos(4m beta y)
}.

No infinite Fourier expansion is generated: 2 GG harmonics + 8 GL harmonics + 7 LL harmonics.

## D. Exact Galerkin bending/load terms

With local Galerkin weight phi and compression along y:

BG =
64 N^2m^2(alpha^2+beta^2)^2/
[alpha beta(4N^2-1)(4m^2-1)].

BL =
4 pi^2/[alpha beta] *
[3 beta^4m^4+2alpha^2beta^2N^2m^2+3alpha^4N^4].

CG =
64 beta N^2m^2/
[alpha(4N^2-1)(4m^2-1)].

CL =
3 pi^2 beta m^2/alpha.

Thus the bending numerator is Ds[b q BG+A BL], and the homogeneous-load denominator is
b(q0+q)CG+(A0+A)CL.

## E. Exact local-only reduction

When q=q0=0, the full expression collapses exactly to

p_s=
(pi^2 Ds/b^2) [
 kcr(N,m,a_h,b) A/(A+A0)
 +(1-nu_s^2) kp(N,m,a_h,b)(2A0A+A^2)/t_s^2
].

The generalized elastic buckling coefficient is
kcr=
(4/3)[3m^2 b^2/a_h^2+2N^2+3N^4 a_h^2/(m^2 b^2)].

The generalized membrane coefficient is

kp =
[
272 N^16 a_h^16
+2856 N^14 a_h^14 b^2 m^2
+11273 N^12 a_h^12 b^4 m^4
+23146 N^10 a_h^10 b^6 m^6
+31506 N^8 a_h^8 b^8 m^8
+23146 N^6 a_h^6 b^10 m^10
+11273 N^4 a_h^4 b^12 m^12
+2856 N^2 a_h^2 b^14 m^14
+272 b^16 m^16
]
/
[
a_h^2 b^2 m^2
(N^2 a_h^2+b^2m^2)^2
(N^2 a_h^2+4b^2m^2)^2
(4N^2 a_h^2+b^2m^2)^2
].

Setting N=1 exactly recovers Yun Lu Eq.(2-32)/(2-34), including her published 272,2856,11273,23146,31506,... coefficient pattern.

## F. Status of the full q-A coupling

The full p_s(q,A) is algebraic and contains no spatial/material integration once the 17 harmonic Galerkin products are evaluated. The final assembly is

p_s =
{Ds[bq BG+A BL]-t_s Es[
 b^2 QG{b(q0+q)J_GG,g+(A0+A)J_GG,phi}
+b QGL{b(q0+q)J_GL,g+(A0+A)J_GL,phi}
+QLL{b(q0+q)J_LL,g+(A0+A)J_LL,phi}
]}
/
{b(q0+q)CG+(A0+A)CL}.

All six J terms are pure closed rational/trigonometric orthogonality results; no integral remains. Their expanded harmonic-by-harmonic formulas are to be kept in the companion derivation ledger, not replaced by fitted coefficients.

Important: this is still the elastic large-deflection branch. Chen Ji Figure 8.19 shows that the plateau/descending branch begins after edge yielding. That post-yield generalized branch remains a separate next derivation and is not silently inserted here.
