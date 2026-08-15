# Classical FvK/Airy postbuckling limit — exact one-halfwave derivation

**Timestamp:** 2026-08-16 00:07 +08:00

## 1. Benchmark identity

This file is a classical elastic thin-plate limit test for the NZ-SCCM membrane closure. It is deliberately simpler than the nonlinear concrete/steel system.

Coordinates:

- x: transverse plate width, `0<=x<=b`
- y: axial representative halfwave, `0<=y<=ell`
- axial compression acts in y

Define

alpha=pi/b, beta=pi/ell,
phi=sin(alpha x) sin(beta y).

Initial imperfection and load-induced deflection are

w0=A0 phi,
wa=A phi,
wt=w0+wa=(A0+A)phi.

The stress-free initial geometry is `w0`, so the incremental second-order compatibility source depends on

S=A^2+2 A0 A.

## 2. Incremental Kármán compatibility source

For the curvature determinant

K(w)=w_xx w_yy-w_xy^2,

exact trigonometric reduction gives

K(wt)-K(w0)
= - S alpha^2 beta^2/2 [cos(2 alpha x)+cos(2 beta y)].

Using the Airy stress function Phi with membrane resultants

Nx=Phi_yy,
Ny=Phi_xx,
Nxy=-Phi_xy,

the isotropic plane-stress FvK compatibility equation is written

nabla^4 Phi = - E t [K(wt)-K(w0)].

Therefore

nabla^4 Phi
= E t S alpha^2 beta^2/2 [cos(2 alpha x)+cos(2 beta y)].

A compatibility-generated particular solution is

Phi_p = C20 cos(2 alpha x)+C02 cos(2 beta y),

with **non-free** coefficients

C20 = E t S beta^2/(32 alpha^2),
C02 = E t S alpha^2/(32 beta^2).

Thus the two membrane harmonics have one common physical driver `S`; they are not two independent relaxation coordinates.

Their ratio is fixed:

C02/C20 = alpha^4/beta^4.

## 3. Mean axial compression and membrane redistribution

Represent the mean y-compression resultant `N>0` by the homogeneous Airy term

Phi_h = -N x^2/2.

Then

Phi=Phi_h+Phi_p.

The membrane resultants are

Ny = -N - E t S beta^2/8 cos(2 alpha x),
Nx =      - E t S alpha^2/8 cos(2 beta y),
Nxy = 0.

Using compression-positive axial magnitude `n_y=-Ny`,

n_y(x)=N+E t S beta^2/8 cos(2 alpha x).

Hence

at x=0,b:       n_y=N+E t S beta^2/8,
at x=b/2:       n_y=N-E t S beta^2/8.

Therefore the nonlinear membrane field explicitly transfers axial compression away from the plate middle and toward the longitudinal edges. The width average remains exactly `N` because the cosine term has zero mean.

## 4. Incremental transverse equilibrium

Use the initial-imperfection form

D_p nabla^4 wa = [Phi,wt],

where

D_p=E t^3/[12(1-nu^2)],

and

[Phi,w]=Phi_yy w_xx+Phi_xx w_yy-2 Phi_xy w_xy.

The one-term Galerkin test is the same `phi`.

The exact moments are

I0 = integral integral phi^2 dxdy = b ell/4,

I20 = integral integral phi^2 cos(2 alpha x) dxdy = -b ell/8,

I02 = integral integral phi^2 cos(2 beta y) dxdy = -b ell/8.

Thus

I20/I0=I02/I0=-1/2.

No spatial quadrature is required.

After exact projection,

N = Ncr * A/(A+A0)
    + E t S/16 [beta^2 + alpha^4/beta^2],

with

Ncr = D_p (alpha^2+beta^2)^2/beta^2.

The second term is strictly non-negative for `A>=0, A0>=0` and strictly positive once postbuckling amplitude develops.

## 5. Dimensionless form

Define

chi=beta/alpha=b/ell.

For axial stress `sigma=N/t`,

sigma(A,A0)
=
[ k_cr A/(A+A0)
 + k_p (1-nu^2)(A^2+2A0A)/t^2 ]
*pi^2 D_p/(t b^2),

where

k_cr=(1+chi^2)^2/chi^2,

k_p=3/4 (chi^2+chi^-2).

For the energy-optimal square representative halfwave `ell=b`, `chi=1`:

k_cr=4,
k_p=3/2.

Therefore

sigma(A,A0)
=
[4 A/(A+A0)
 + 3/2(1-nu^2)(A^2+2A0A)/t^2]
*pi^2 D_p/(t b^2).

For a perfect plate `A0=0`, the non-trivial postbuckling branch is

sigma_cr=4 pi^2 D_p/(t b^2),

sigma/sigma_cr
=1+3(1-nu^2)/8 (A/t)^2.

This is the required stable classical postbuckling branch.

## 6. Monotonicity

Let

C_m=E t/16 [beta^2+alpha^4/beta^2] > 0.

Then

N(A)=Ncr A/(A+A0)+C_m(A^2+2A0A),

and for `A0>0`

dN/dA
=Ncr A0/(A+A0)^2+2 C_m(A+A0) > 0.

For a perfect plate `A0=0`,

dN/dA=2 C_m A > 0 for A>0.

Thus this classical elastic limit cannot produce the previously observed artificial softening merely by releasing the compatibility-generated membrane harmonics.

## 7. Relation to Yun Lu source

Yun Lu's thesis derives the Airy stress function from the Kármán compatibility equation and obtains Eq. (2-32) in the same structural form:

p_x = [k_crx A/(A+A0)
       + k_p(1-nu^2)(2A0A+A^2)/t^2]
      *pi^2 D/(t b^2).

Yun's clamped/unilateral wall-panel shape gives different numerical `k_crx` and `k_p`; at integer aspect ratio the thesis reports positive `k_p=42.64`. The important source-level cross-check is the sign and structure: the membrane term is positive and proportional to `2A0A+A^2`.

## 8. Consequence for NZ-SCCM

The previous statement

`(2,0)/(0,2) harmonics exist -> introduce two independent p20,p02 coordinates`

is not a valid classical derivation.

The valid classical chain is

w0,wa
-> compatibility source S
-> Airy coefficients C20(S),C02(S)
-> membrane resultants
-> transverse equilibrium.

The harmonic amplitudes are coupled by compatibility/equilibrium and boundary conditions.

The next NZ-SCCM membrane closure must preserve this chain, either explicitly through an Airy/resultant representation or through a displacement basis proven to be exactly equivalent after constitutive elimination.
