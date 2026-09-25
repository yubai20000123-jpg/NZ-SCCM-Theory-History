# First execution: epsilon-only UHPC candidate + Yun-Lu/Chen-Ji whole-face multiwave derivation

Date: 2026-09-25

## A. UHPC single-expression candidate

Formal law must contain only ordinary epsilon. No abs(epsilon), positive/negative parts, Heaviside, max/min, or external tension/compression switch.

A pole-free candidate family was tested:
sigma(epsilon) = [Ec*ecp*u + a2*u^2+a3*u^3+a4*u^4+a5*u^5] /
                 [1+(b1*u+b2*u^2+b3*u^3)^2],
u=epsilon/ecp.

Using the current signed-C1 compression/tension curves as reference over the physical calibration range, the first tested family in the nested set that reproduced the required one compression peak and one tension peak without denominator poles was numerator degree 5 / squared-cubic denominator.

Current candidate coefficients:
a2=-466.23333324 MPa
a3=11242.93041725 MPa
a4=-8127.66358347 MPa
a5=4655.87683348 MPa
b1=14.27991175
b2=13.35856539
b3=12.29412017

This is a candidate only; it is not yet LOCKED. It is to be refitted against the full original compression and tension datasets rather than only the present signed-C1 reference.

The denominator is 1+Q(u)^2 > 0 for every real epsilon, so the law is globally pole-free and is a genuine single ordinary-epsilon expression.

## B. Steel shell whole-face geometry

g=sin(pi x/b) sin(pi y/a_h)
phi=[1-cos(2N pi x/b)][1-cos(2m pi y/a_h)]

TOP:
Ws0+=b q0 g + A0+ phi
Ws+=b(q0+q)g +(A0+ +A+)phi.

BOTTOM: same global term and opposite local outward sign if the side convention requires it.

Let alpha=pi/b, beta=pi/a_h, Kx=2N alpha, Ky=2m beta.

For H(W)=W_xy^2-W_xx W_yy:

Hgg = alpha^2 beta^2/2 [cos(2alpha x)+cos(2beta y)].

Hgp =
-4 alpha^2 beta^2 [
 (N^2+m^2) sin(alpha x)sin(beta y)cos(Kx x)cos(Ky y)
 -N^2 sin(alpha x)sin(beta y)cos(Kx x)
 -m^2 sin(alpha x)sin(beta y)cos(Ky y)
 -2Nm sin(Kx x)sin(Ky y)cos(alpha x)cos(beta y)
].

Hpp = Kx^2 Ky^2 {
 sin^2(Kx x)sin^2(Ky y)
 -cos(Kx x)cos(Ky y)[1-cos(Kx x)][1-cos(Ky y)]
}.

Thus
Delta H =
b^2(q^2+2q0q) Hgg
+b(q0 A+q A0+q A) Hgp
+(2A0 A+A^2) Hpp.

Each term is a finite trigonometric polynomial. Therefore the Airy particular is obtained harmonic-by-harmonic from
nabla^4[cos(kx x)cos(ky y)] = (kx^2+ky^2)^2 cos(kx x)cos(ky y),
and similarly for sin-sin / sin-cos harmonics.

The particular Airy field consequently has the exact amplitude structure:
Fp = Es [
 b^2(q^2+2q0q) Psi_GG
 +b(q0 A+q A0+q A) Psi_GL
 +(2A0 A+A^2) Psi_LL
],
where Psi_GG/Psi_GL/Psi_LL are explicit finite harmonic fields obtained by biharmonic inversion. This notation is only a temporary derivation label; final formal output must expand them.

Substitution into the first Marguerre/Karman equilibrium equation and Galerkin projection with phi yields a scalar local whole-face equation whose algebraic dependence is necessarily:
R_A =
C_Dq q + C_DA A
-p_x(C_pq q + C_pA(A+A0))
+Es[
C_GGq * b^2(q^2+2q0q)*(linear in q,A,A0)
+C_GL * b(q0A+qA0+qA)*(linear in q,A,A0)
+C_LL * (2A0A+A^2)*(linear in q,A,A0)
]=0.
All C coefficients are exact trigonometric integrals depending only on b,a_h,N,m and the chosen edge conditions. No width-thickness normalization is introduced before these integrals are completed.

When q=q0=0, the equation must reduce to Yun-Lu's single-side whole-face relation, including the A/(A+A0) imperfection factor and the (2A0A+A^2) membrane term.

## C. Chen Ji Figure 8.19 correction

The surrounding text supplied by the user establishes the mechanism:
- curve a: perfect plate elastic postbuckling rises until A, where edge stress first yields;
- after A, plasticity develops, deflection increases rapidly, and the path reaches an ultimate load then flattens/descends;
- curve b: imperfect plate; edge yielding begins at A'; its ultimate load is close to the perfect-plate edge-fiber-yield load;
- because full plate ultimate load is difficult to calculate, Chen Ji takes the perfect-plate edge-fiber-yield load as pu;
- Eq.(8.72): sigma_u=(fy+sigma_crx)/2 for m=a/b.

Therefore the descending/plateau segment in Figure 8.19 is not produced by the isolated elastic Eq.(8.68b); it is associated with post-edge-yield plastic development. The steel reduced model must reproduce both:
(1) elastic Yun-Lu/Chen-Ji Karman-Airy path before first edge yield;
(2) a post-yield generalized path, without reverting to pointwise Mises area/thickness integration.
