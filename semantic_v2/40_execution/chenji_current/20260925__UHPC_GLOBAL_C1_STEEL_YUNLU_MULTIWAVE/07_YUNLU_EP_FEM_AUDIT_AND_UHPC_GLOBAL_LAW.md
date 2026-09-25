# 07 Yun-Lu elastoplastic FEM audit and UHPC global-law continuation

Date: 2026-09-25

## A. Steel: compare the current reduced law with Yun-Lu's elastoplastic FEM

Yun-Lu Chapter 4 compares three paths:
- elastic FEM;
- elastoplastic FEM;
- analytical theory.

The thesis states that the elastoplastic FEM coincides with elastic FEM before buckling, grows more slowly after buckling, and descends after the ultimate point. It also states that aspect ratio has little effect on buckling/ultimate stresses at fixed b/t, while b/t is dominant.

The current exact q=0,N=1 reduction is Yun-Lu's analytical elastic path. Therefore its first-edge-yield stress reproduces Yun-Lu's blue theory curve and not the red elastoplastic FEM curve.

For the six representative b/t values, the current first-yield/theory values and figure-read elastoplastic FEM peaks are:

b/t | current/Yun-Lu theory | FEM a/b=3 | FEM a/b=2 | FEM a/b=1 | FEM mean | current-vs-mean
150 | 176.36 | 135 | 133 | 133 | 133.67 | +31.94%
125 | 189.91 | 149 | 150 | 149 | 149.33 | +27.17%
100 | 212.23 | 175 | 172 | 172 | 173.00 | +22.68%
90  | 222.89 | 180 | 185 | 185 | 183.33 | +21.58%
80  | 229.92 | 201 | 200 | 202 | 201.00 | +14.39%
60  | 233.44 | 236 | 237 | 237 | 236.67 | -1.36%

The figure values are read from Yun-Lu Figs.4-8--4-10, so they are diagnostic graphical values rather than digitized raw ODB data.

### Consequence

The simple reduced continuation

p_s^Y = "hold the elastic edge stress at fy"

is rejected as the final post-yield constitutive path.

Reason 1: for b/t>=80 the major discrepancy already exists at the elastic-theory / FEM level. Yun-Lu explicitly reports that the analytical path is higher than elastic FEM at the same deflection. Hence a post-yield rule cannot repair that pre-yield membrane-path bias.

Reason 2: Yun-Lu's elastoplastic FEM uses Q235 with an elastic plateau followed by strain hardening, not perfect plasticity. Therefore a one-point edge-yield consistency equation cannot represent expansion of the plastic region and later hardening.

Reason 3: Yun-Lu states that for b/t>70, considering plasticity has little effect on buckling/ultimate stress, whereas for b/t<70 the elastoplastic FEM ultimate may exceed fy because residual/hardening capacity is mobilized. Thus:
- wide/slender plates: main correction is the elastic/postbuckling kinematic-membrane field;
- stockier plates: steel plastic evolution/hardening becomes a separate mechanism.

This is consistent with the previous project K2+I2 diagnosis: expanding the admissible in-plane compatibility space removes most of the wide/slender-plate overestimate, without needing an ad-hoc material reduction.

### Next steel derivation target

Keep:
1. exact whole-face q+A(N,m) geometry;
2. exact GG+GL+LL source;
3. exact finite Airy harmonics;
4. explicit average strain/load interface.

Replace the single Yun-Lu homogeneous/in-plane closure by the smallest richer compatible in-plane/Airy homogeneous space that can reproduce the I2 effect analytically. Do this before adding plasticity.

Only after that elastic membrane path is corrected:
- determine first plastic-front initiation;
- represent the yielded-width/plastic-front position as a generalized internal variable;
- use Yun-Lu's actual Q235 multilinear law (elastic -> yield plateau -> strain hardening) at the generalized level;
- integrate the finite harmonic stress field analytically over the yielded/un-yielded subregions, with no Gauss quadrature.

## B. UHPC: physical-anchor global constitutive law

Source-supported physical anchors:

Compression:
- origin: sigma(0)=0, sigma'(0)=Ec;
- approximately linear response up to about 0.8 fc;
- compression peak: (-eps_cp,-fc), zero tangent;
- one post-peak descriptor, preferably eps_c50 where sigma=-0.5fc;
- domain tail check at -5 eps_cp, not necessarily zero stress.

Tension:
- cracking point (eps_tcr, ftcr);
- tensile peak (eps_tp, ft), zero tangent;
- localization point (eps_tloc, ftloc);
- tensile limit eps_tlim and corresponding residual stress ftlim.

Hiew 2024 directly supports separate cracking, peak, localization, and tensile-limit descriptors; its reported localization stress is modestly below peak and epsilon_tlim is typically around 0.8--1.2%.

Recommended finite physical domain:
[-5 eps_cp, eps_tlim].
Do not use +5 eps_tp as a universal tensile bound.

### Single-expression family

Define x=epsilon/eps_cp, n=Ec eps_cp/fc.

Use

s(x)=sigma/fc
= n x
  [1+(a1 x+a2 x^2+a3 x^3+a4 x^4)^2]
  /
  [1+(b1 x+b2 x^2+b3 x^3+b4 x^4+b5 x^5)^2].

Properties:
- only ordinary epsilon appears;
- sigma(0)=0 and sigma'(0)=Ec automatically;
- denominator is strictly positive;
- sign(sigma)=sign(epsilon);
- no external tension/compression switch;
- since denominator degree exceeds numerator degree, sigma->0 for both far tails.

Nine physical equations can be imposed:
1. sigma(-0.8fc/Ec)=-0.8fc;
2. sigma(-eps_cp)=-fc;
3. sigma'(-eps_cp)=0;
4. sigma(-eps_c50)=-0.5fc;
5. sigma(eps_tcr)=ftcr;
6. sigma(eps_tp)=ft;
7. sigma'(eps_tp)=0;
8. sigma(eps_tloc)=ftloc;
9. sigma(eps_tlim)=ftlim.

### Pilot order audit

An exact nine-equation interpolation test was performed with the above 9-shape-parameter family on a representative Hiew strain-hardening set (SL-2.0), using a generic compression-shape test value n=1.1 and eps_c50=2eps_cp only for architecture screening.

The nine anchor equations can be satisfied to machine precision, but the exact interpolation produces extra stationary points inside the physical domain. Therefore:
- "9 parameters for 9 anchor equations" is NOT sufficient as an acceptance criterion;
- exact interpolation is rejected as the fitting rule.

The final calibration must be shape-constrained.

For the above rational law,

ds/dx =
n D(x)/(1+Q(x)^2)^2,

with
P=a1x+a2x^2+a3x^3+a4x^4,
Q=b1x+b2x^2+b3x^3+b4x^4+b5x^5,

D(x)=
(1+P^2)(1+Q^2)
+2x P P'(1+Q^2)
-2x Q Q'(1+P^2).

D(x) is an ordinary polynomial. Therefore physical shape can be audited without Gauss points or discretized material integration by requiring:
- D(x)<0 on [-5,-1);
- D(-1)=0;
- D(x)>0 on (-1,x_tp);
- D(x_tp)=0;
- D(x)<0 on (x_tp,x_tlim].

The exact root count/sign can be checked algebraically (e.g. real polynomial roots/Sturm sequence), not by treating check points as theory variables.

Thus the next UHPC task is now well-defined:
fit the nine coefficients to the physical anchor data under the polynomial root-count/sign gate, increasing polynomial order only if no admissible solution exists.
