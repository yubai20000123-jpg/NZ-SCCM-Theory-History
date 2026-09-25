# 04 Steel first-yield / descending generalized branch + generic UHPC single-expression audit

Date: 2026-09-25

## A. Steel: explicit edge stress and first-yield equation

Use alpha=pi/b, beta=pi/a_h and the previously derived whole-face field
Ws0=b q0 sin(alpha x)sin(beta y)+A0 phi,
Ws=b(q0+q)sin(alpha x)sin(beta y)+(A0+A)phi,
phi=(1-cos 2N alpha x)(1-cos 2m beta y).

With tension-positive stress convention and homogeneous Airy term
F_h=-p_s y^2/(2t_s),
the axial stress at the free-side edge y=0 is exactly

sigma_x(x,0)=
-p_s/t_s
-E_s*pi^2(q^2+2q0q)/8
+(E_s N^2 alpha^2(2A0A+A^2)/2)*
[
-3
+8m^4 beta^4{
  1/(N^2 alpha^2+m^2 beta^2)^2
 -2/(N^2 alpha^2+4m^2 beta^2)^2
 } cos(2N alpha x)
-4m^4 beta^4/(4N^2 alpha^2+m^2 beta^2)^2 cos(4N alpha x)
].

Important: the GL Airy part is sine-sine in y, hence its second y derivative vanishes at y=0. Thus GL changes the average elastic load p_s(q,A), but it does not directly add to the edge axial stress at y=0.

Let X=N^2 alpha^2 and Y=m^2 beta^2. If
1/(X+Y)^2 - 2/(X+4Y)^2 >= 0,
the most compressive edge point is cos(2N alpha x)=-1, cos(4N alpha x)=1, i.e. x=(2j+1)b/(2N).

At that point the compressive stress magnitude is

sigma_edge,c =
p_s/t_s
+E_s*pi^2(q^2+2q0q)/8
+(E_s N^2 alpha^2(2A0A+A^2)/2)*
[
3
+8m^4 beta^4{
  1/(N^2 alpha^2+m^2 beta^2)^2
 -2/(N^2 alpha^2+4m^2 beta^2)^2
 }
+4m^4 beta^4/(4N^2 alpha^2+m^2 beta^2)^2
].

First yield is therefore the explicit scalar condition
sigma_edge,c(q,A,p_s^E(q,A))=f_y.

Because p_s^E(q,A) is a rational function whose numerator is at most cubic in A and denominator is linear in A, clearing its denominator gives a cubic equation in A for fixed q. No area or thickness integration is required. The physical first-yield amplitude is the first positive root connected to A=0.

### Square-wave-count simplification

For a_h=b and N=m, X=Y and the square bracket reduces exactly to 113/25. Hence

sigma_edge,c =
p_s/t_s
+E_s*pi^2(q^2+2q0q)/8
+(113/50) E_s N^2 pi^2(2A0A+A^2)/b^2.

First yield:
p_s^E(q,A)/t_s
+E_s*pi^2(q^2+2q0q)/8
+(113/50)E_s N^2 pi^2(2A0A+A^2)/b^2
=f_y.

## B. Candidate post-yield reduced branch

Chen Ji Fig.8.19 states that after edge yielding, plastic development allows deflection to grow rapidly and the load approaches a limit/plateau-descending segment. Yun Lu stops at first edge yield.

A minimal ideal-plastic reduced continuation is obtained by enforcing edge-yield consistency after first yield:
sigma_edge,c=f_y
while q,A continue evolving.

Therefore

p_s^Y(q,A)=t_s[
f_y
-E_s*pi^2(q^2+2q0q)/8
-(E_s N^2 alpha^2(2A0A+A^2)/2)*
(
3
+8m^4 beta^4{
  1/(N^2 alpha^2+m^2 beta^2)^2
 -2/(N^2 alpha^2+4m^2 beta^2)^2
 }
+4m^4 beta^4/(4N^2 alpha^2+m^2 beta^2)^2
)
].

For a_h=b and N=m:
p_s^Y=t_s[
f_y
-E_s*pi^2(q^2+2q0q)/8
-(113/50)E_s N^2 pi^2(2A0A+A^2)/b^2
].

Then
partial p_s^Y/partial A =
-(113/25)E_s t_s N^2 pi^2(A0+A)/b^2 <0
for A0+A>0,

and
partial p_s^Y/partial q =
-(E_s t_s pi^2/4)(q0+q)<0
for q0+q>0.

Thus the ideal-plastic generalized branch has a natural descending tangent without pointwise Mises integration or an imposed empirical descending function.

Identity: this is a new reduced H1/Yun-Lu/Chen-Ji candidate continuation, not an equation copied from Chen Ji or Yun Lu. It must be tested against the full plate response before being LOCKED.

## C. UHPC: generic single-expression family, not UC141-specific

The existing account/project compression baseline is the common normalized UHPC full-curve form:
xi=eps_c/eps_c0,
n=E_c eps_c0/f_c,
ascending sigma/f_c=(n xi-xi^2)/(1+(n-2)xi),
descending sigma/f_c=xi/[2(xi-1)^2+xi].
This implies sigma(2 eps_c0)=0.5 f_c for the descending branch.

The formal new model must be one expression in ordinary epsilon only, with no abs, positive/negative parts, Heaviside, max/min, or external tension/compression branch selection.

A useful dimensionless family is

x=epsilon/epsilon_c0,
s=sigma/f_c,
n=E_c epsilon_c0/f_c,

s(x)=
n x (1+a x^2) /
[
1+(b1 x+b2 x^2+b3 x^3)^2+d4 x^4+d6 x^6
],

with a>=0,d4>=0,d6>=0.

Properties:
- s(0)=0;
- ds/dx|0=n, hence d sigma/d epsilon|0=E_c;
- sign(s)=sign(x);
- denominator >0 for all real x;
- if b3 or d6 is nonzero, s->0 as |x|->infinity;
- tension/compression asymmetry is produced by ordinary odd/even powers of x, not by a sign switch.

Material descriptors used for calibration should be:
E_c, f_c, epsilon_c0,
f_t, epsilon_t0,
one compression post-peak descriptor rho_c=sigma(-kappa_c epsilon_c0)/(-f_c),
and one tension post-peak descriptor rho_t=sigma(kappa_t epsilon_t0)/f_t.

The compression descriptor can default to the widely used Yang/FIB-type reference if no full test curve is available; for kappa_c=2 that reference gives rho_c=0.5.
The tension descriptor must remain material/fibre dependent rather than universal.

Order audit:
- four free shape parameters can satisfy the two peak values and two peak-stationarity conditions, but the current representative test gives overly rapid compression softening;
- one additional parameter can force a compression post-peak anchor but can create secondary tensile extrema if unconstrained;
- therefore the first robust candidate is the six-shape-parameter form above, calibrated by constrained least squares with one compression and one tension softening descriptor plus monotonicity constraints. This is a candidate family, not yet LOCKED.

