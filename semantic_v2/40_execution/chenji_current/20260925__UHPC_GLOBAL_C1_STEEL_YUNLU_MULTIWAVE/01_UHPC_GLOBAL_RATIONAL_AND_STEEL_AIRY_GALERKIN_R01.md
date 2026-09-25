# R01 — UHPC single-epsilon global law + Yun-Lu/Chen-Ji whole-face multiwave steel derivation

Date: 2026-09-25

## A. UHPC: one ordinary-epsilon law

Formal family:
xi = epsilon / eps_cp

sigma_U(epsilon) =
[Ec eps_cp xi + a2 xi^2 + ... + am xi^m] /
[1 + b1 xi + ... + bn xi^n].

No abs(epsilon), epsilon_plus/minus, Heaviside, max/min, or external branch switch is permitted.

Eight exact material constraints are imposed:
compression peak value and zero tangent;
compression half-peak-strain stress;
compression double-peak-strain stress;
tension peak value and zero tangent;
tension half-peak-strain stress;
tension double-peak-strain stress.

With Ec fixed at the origin, the number of free coefficients is (m-1)+n=m+n-1.
A scan over the present physical interval epsilon in [-0.007, 0.0058317] found:
- m+n=9: the exact eight-condition solutions develop poles and/or wrong-sign/non-monotone branches;
- m+n=10: no tested degree split admitted a pole-free and correct single-peak branch over the full interval;
- m+n=11: the first feasible family was found, including the balanced (m,n)=(5,6) form.

Preliminary 5/6 coefficients, using the current C1 anchors as exact constraints:
a2 = 1611.747954551746
a3 = 12225.172559052966
a4 = -5730.715600721019
a5 = 9005.079639007728
b1 = 21.167658937878
b2 = 314.138767898078
b3 = 778.047539194560
b4 = 1155.740517817604
b5 = 769.388031953706
b6 = 278.454772465645

Thus:
sigma_U =
(151.9 xi +1611.74795455 xi^2 +12225.17255905 xi^3 -5730.71560072 xi^4 +9005.07963901 xi^5) /
(1 +21.16765894 xi +314.13876790 xi^2 +778.04753919 xi^3 +1155.74051782 xi^4 +769.38803195 xi^5 +278.45477247 xi^6) MPa.

It satisfies exactly the eight chosen C1 anchor/peak conditions, sigma(0)=0, and sigma'(0)=Ec. The denominator remains positive on the checked physical interval. This is a preliminary lowest-order feasible member of this rational family, not a final accuracy acceptance.

## B. Steel whole-face geometry

alpha=pi/b, beta=pi/a_h.
g=sin(alpha x) sin(beta y).
phi=[1-cos(2N alpha x)][1-cos(2m beta y)].

TOP:
W0 = G0 g + T0 phi,  G0=b q0, T0=A0.
W  = G  g + T  phi,  G=b(q0+q), T=A0+A.

Define H(f)=f_xy^2-f_xx f_yy.

Exactly:
H(W)-H(W0)
=DeltaG2 H_g + DeltaGT B_gphi + DeltaT2 H_phi,

DeltaG2=b^2(q^2+2q0 q),
DeltaGT=b(q0 A+q A0+q A),
DeltaT2=2A0 A+A^2.

H_g =
(alpha^2 beta^2/2)[cos(2 alpha x)+cos(2 beta y)].

Let P=2N alpha, Q=2m beta.

H_phi=P^2 Q^2[
-1/2 cos(2Px)
-1/2 cos(2Qy)
-cos(Px)cos(Qy)
+1/2 cos(Qy)
+1/2 cos(2Px)cos(Qy)
+1/2 cos(Px)
+1/2 cos(Px)cos(2Qy)
].

B_gphi =
alpha^2 beta^2 {
-(N-m)^2[sin((2N+1)alpha x)sin((2m+1)beta y)+sin((2N-1)alpha x)sin((2m-1)beta y)]
+(N+m)^2[sin((2N+1)alpha x)sin((2m-1)beta y)+sin((2N-1)alpha x)sin((2m+1)beta y)]
+2m^2 sin(alpha x)[sin((2m+1)beta y)-sin((2m-1)beta y)]
+2N^2[sin((2N+1)alpha x)-sin((2N-1)alpha x)]sin(beta y)
}.

## C. Airy particular solution

At resultant level:
nabla^4 Phi_p = Es ts [H(W)-H(W0)].

Uniform axial compression along y is represented by
Phi_h = -(p_s/2)x^2,
so Ny_h=Phi_h,xx=-p_s.

Phi_p=Es ts[DeltaG2 Psi_GG+DeltaGT Psi_GL+DeltaT2 Psi_LL].

Psi_GG =
(beta^2/(32 alpha^2))cos(2 alpha x)
+(alpha^2/(32 beta^2))cos(2 beta y).

Psi_LL =
-Q^2/(32P^2) cos(2Px)
-P^2/(32Q^2) cos(2Qy)
-P^2 Q^2/(P^2+Q^2)^2 cos(Px)cos(Qy)
+P^2/(2Q^2) cos(Qy)
+P^2 Q^2/[2(4P^2+Q^2)^2] cos(2Px)cos(Qy)
+Q^2/(2P^2) cos(Px)
+P^2 Q^2/[2(P^2+4Q^2)^2] cos(Px)cos(2Qy).

Psi_GL equals:
alpha^2 beta^2 times the following eight sine-sine terms, each source coefficient divided by its biharmonic eigenvalue:

-(N-m)^2 sin((2N+1)alpha x)sin((2m+1)beta y) /
{[(2N+1)^2 alpha^2+(2m+1)^2 beta^2]^2}

-(N-m)^2 sin((2N-1)alpha x)sin((2m-1)beta y) /
{[(2N-1)^2 alpha^2+(2m-1)^2 beta^2]^2}

+(N+m)^2 sin((2N+1)alpha x)sin((2m-1)beta y) /
{[(2N+1)^2 alpha^2+(2m-1)^2 beta^2]^2}

+(N+m)^2 sin((2N-1)alpha x)sin((2m+1)beta y) /
{[(2N-1)^2 alpha^2+(2m+1)^2 beta^2]^2}

+2m^2 sin(alpha x)sin((2m+1)beta y) /
{[alpha^2+(2m+1)^2 beta^2]^2}

-2m^2 sin(alpha x)sin((2m-1)beta y) /
{[alpha^2+(2m-1)^2 beta^2]^2}

+2N^2 sin((2N+1)alpha x)sin(beta y) /
{[(2N+1)^2 alpha^2+beta^2]^2}

-2N^2 sin((2N-1)alpha x)sin(beta y) /
{[(2N-1)^2 alpha^2+beta^2]^2}.

## D. Local-amplitude Galerkin equation and load-amplitude relation

Use Marguerre/Karman transverse equilibrium:
Ds nabla^4(W-W0)
=
Phi_yy W_xx + Phi_xx W_yy - 2 Phi_xy W_xy.

Project with phi = dW/dA over x in [0,b], y in [0,a_h].

Define only for the derivation:
I_gphi =
64 b a_h N^2 m^2 /
[pi^2(4N^2-1)(4m^2-1)].

K_y =
3 b a_h Q^2/4
=3 b a_h m^2 beta^2.

K_phi =
(b a_h/4)(3P^4+2P^2Q^2+3Q^4).

Then:
-int int W_yy phi dA =
beta^2 G I_gphi + K_y T.

The bending term is exactly:
Ds int int nabla^4(W-W0) phi dA
=
Ds[
b q(alpha^2+beta^2)^2 I_gphi
+A K_phi
].

For the nonlinear membrane term, with
C(F,W)=F_yy W_xx+F_xx W_yy-2F_xy W_xy,
integration by parts gives
int int C(Phi_p,W) phi dA
=
-int int Phi_p [G B_gphi+2T H_phi] dA.

Therefore the exact whole-face elastic steel load-amplitude equation is:

p_s(q,A)=
{
Ds[b q(alpha^2+beta^2)^2 I_gphi+A K_phi]
+Es ts int int
[DeltaG2 Psi_GG+DeltaGT Psi_GL+DeltaT2 Psi_LL]
[G B_gphi+2T H_phi] dA
}
/
{
beta^2 G I_gphi+K_y T
}.

All functions inside the remaining displayed inner product are the finite explicit harmonics listed above. Hence this area integral is an exact finite trigonometric moment, not a numerical quadrature.

## E. Exact local-only reduction and Yun-Lu structural recovery

Set q=q0=0. Then G=0, T=A0+A, DeltaT2=2A0A+A^2.

The entire relation reduces exactly to

p_s(A,A0)
=
[Ds K_phi/K_y] A/(A0+A)
+
[2 Es ts C_phi/K_y](2A0A+A^2),

where

C_phi =
b a_h[
17/128(P^4+Q^4)
+P^4Q^4/[4(P^2+Q^2)^2]
+P^4Q^4/[16(4P^2+Q^2)^2]
+P^4Q^4/[16(P^2+4Q^2)^2]
].

This reproduces the exact Yun-Lu structural form:
buckling term A/(A+A0)
+
membrane term (2A0A+A^2).

Coefficient identity with Yun-Lu's published k_crx and k_p is to be checked after mapping coordinate orientation and her boundary-condition coefficient convention; structural identity is already explicit.

## F. Chen Ji Figure 8.19 interpretation

The uploaded original text makes clear that:
- the elastic large-deflection path leads to edge first yield at A for the perfect plate and A' for the imperfect plate;
- after edge yielding, plastic development causes rapid deflection and the path reaches an ultimate point, shown with a plateau/descending branch in Fig. 8.19;
- the actual ultimate load generally needs a numerical method;
- because the actual ultimate and the perfect-plate edge-fiber-yield load are close, Chen Ji proposes using the latter as the approximate ultimate, giving Eq.(8.72).

Therefore the reduced steel program must distinguish:
1. elastic Yun-Lu/Chen-Ji whole-face path, derived above;
2. first-yield condition max axial compressive stress = fy, obtained from the explicit Airy field;
3. post-yield reduced continuation, which cannot be claimed to follow from the elastic formula alone and must be constructed/solved numerically if the actual descending branch is required.

No pointwise Mises surface/thickness integration is introduced in this reduced steel route.
