# NZ-SCCM R10B — FROZEN R10 1D ENERGY SMOOTHING -> ZERO-SPATIAL D15 CASE21

Date: 2026-08-11

## 1. Identity

R10B changes no material parameter and does not retune the R10 scalar. It recompiles the frozen R10 one-dimensional energy-smoothed tensile scalar into a Case21-local zero-spatial analytic backend.

```text
N_formal_spatial_sampling   = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_Pu_CALIBRATION   = NO
```

Formal chain:

```text
frozen R10 u_sm(t)
-> 1D material-coordinate Chebyshev compiler
-> SAME U/C/T + CC/TC/TT current map
-> Nguyen continuous Case21 kinematics
-> Cayley-Hamilton tensor-Chebyshev coefficient algebra
-> exact complete-halfwave moments
-> P(D,q), R(D,q)
-> same-expression P_D,P_q,R_D,R_q
-> limit state
```

Material-coordinate samples are used only to derive finite 1D analytic compiler coefficients. They are not spatial samples and are not free material parameters.

## 2. Analytic Case21 spectral certificate

Freeze the Case21 search box

\[
D\in[0.78,0.90],\qquad q\in[0.0015,0.0021].
\]

For Case21, `ell/b=1`. At `qmax=0.0021`:

```text
Mmax = 0.035204737229723046
Bmax = 0.07844047893484817
```

The equivalent-uniaxial diagonal gap satisfies

\[
X_{11}-X_{22}\ge D-\frac{M}{1+\nu},
\]

hence

\[
\boxed{g_{min}=0.7501654769239635>0}.
\]

Also

\[
|X_{12}|\le\frac{M/4+B}{1+\nu}
=0.07393361291718553,
\]

and the eigenvalue correction is bounded by

\[
\frac{|X_{12}|^2}{g_{min}}
\le0.007286631132909724.
\]

Using the diagonal bounds gives

\[
\boxed{\lambda_+\in[-0.0956591207,0.1029457518]},
\]

\[
\boxed{\lambda_-\in[-1.0029457518,-0.6843408793]}.
\]

The compiler therefore uses safe-margin intervals

```text
lambda+ : [-0.10,  0.105]
lambda- : [-1.01, -0.68]
```

inside one single scalar polynomial hull `[-1.01,0.105]`. This is spectral-domain reduction, not a spatial material-state partition.

## 3. Multiaxial reconstruction without a 2D refit

Map the equivalent-uniaxial tensor to

\[
\mathbf Y=a\mathbf I+b\mathbf E_u
\]

so the compiler hull maps to `[-1,1]`. Let

\[
K_1=\operatorname{tr}\mathbf Y,\qquad K_2=\det\mathbf Y.
\]

For every retained matrix Chebyshev polynomial,

\[
\mathbf Y^2-K_1\mathbf Y+K_2\mathbf I=0.
\]

Represent a matrix function by the pair

\[
F(\mathbf Y)=A(K_1,K_2)\mathbf I+B(K_1,K_2)\mathbf Y.
\]

Pair multiplication is exactly

\[
(A,B)(C,D)
=(AC-BDK_2,\ AD+BC+BDK_1).
\]

The frozen R10 interaction is reconstructed algebraically, not fitted:

\[
CC=\det(C)C,
\]

\[
TC=C[\operatorname{tr}(T)I-T],
\]

\[
TT=\det(T)[\operatorname{tr}(T^7)I-T^7],
\]

\[
\boxed{\mathbf S=\mathbf U-a_{cc}CC+TC-\rho a_tTT}.
\]

Thus the principal R10 formulas are retained exactly at the finite compiler level.

## 4. Zero-spatial exact moments

Every retained scalar field is a finite tensor-Chebyshev series

\[
F=\sum_{ijk}c_{ijk}T_i(\sin X)T_j(\sin Y)T_k(\zeta).
\]

Coefficient multiplication is performed entirely in coefficient space. FFT is used only to accelerate coefficient-index convolution; it never evaluates the physical-space integrand.

The complete-halfwave moments are closed form:

\[
\int_0^\pi T_n(\sin X)dX=
\begin{cases}
\pi,&n=0,\\
2\sin(n\pi/2)/n,&n\ge1,
\end{cases}
\]

\[
\int_{-1}^1T_k(\zeta)d\zeta=
\begin{cases}
0,&k\text{ odd},\\
2/(1-k^2),&k\text{ even}.
\end{cases}
\]

Therefore every formal structural integral is the finite contraction

\[
\boxed{\sum_{ijk}c_{ijk}M_iM_jZ_k}.
\]

No spatial Gauss/Simpson/adaptive quadrature or spatial sampling is present in the formal operator.

## 5. Same-expression derivatives and limit condition

Forward chain-rule jets are propagated through the same coefficient algebra. There is no finite-difference production derivative.

At the selected N48 state:

```text
P_D = 106.58759351383472
P_q = -75105.39767023241
R_D = -1376.335532846137
R_q = 969815.5988960797
```

\[
L=P_D R_q-P_qR_D=83.31643116474152.
\]

Normalized by the two determinant terms:

\[
\boxed{L_{norm}=4.0299997197\times10^{-7}}.
\]

Along the explicit equilibrium branch,

\[
\frac{dP}{dD}=\frac{L}{R_q}
=8.59095598\times10^{-5}\ \mathrm{kN},
\]

so the selected branch maximum and the explicit `L=0` condition are numerically coincident at engineering precision.

## 6. N48 formal Case21 result

```text
material degree = 48
spatial Chebyshev degree = 28
D_u  = 0.8449505
q_u  = 0.001779254542005754
A_u  = 2.1706905412470197 mm
Pc   = 337.39660909142 kN
Ps   = 30.922943404456966 kN
Pu   = 368.31955249587696 kN
R    = -2.2383016926141863e-05 kN mm
```

Experiment is introduced only after the material law is frozen:

```text
Pf = 368.312750 kN
Pu-Pf = +0.006802495877 kN
error = +0.001846934671 %
```

This agreement is not a calibration result.

## 7. Order-convergence audit

At the fixed R10 audit state, the zero-spatial coefficient algebra gives:

| material degree | spatial degree | P (kN) | R (kN mm) |
|---:|---:|---:|---:|
|32|20|366.9675246|18.8609835|
|40|24|367.6357111|8.2488354|
|48|28|367.8426262|6.1492893|
|56|30|368.1017038|3.4003506|
|64|32|368.2664235|1.8739463|
|72|34|368.3534474|1.1915080|
|80|36|368.3983685|0.8428271|
|96|40|368.5026604|0.1030400|

A separate N96 high-order equilibrium check at the N48 stationary D, with q reclosed, gives

```text
D fixed = 0.8449505
q_eq    = 0.0017855282237914806
P       = 368.50804285212683 kN
R       = 0.021212151265274315 kN mm
```

The N96 equilibrium check differs from the N48 formal stationary result by

\[
\boxed{0.1884903563\ \mathrm{kN}=0.0511757671\%}.
\]

N96 was not separately reoptimized in D and is therefore an order-sensitivity audit, not a second stationary root.

Under the current project rule that theorem-level tight remainder certificates are no longer an engineering hard gate, this 0.051% order sensitivity is accepted for continued theory development.

## 8. Decision

```text
R10B_1D_MATERIAL_RECOMPILE                 = PASS
SAME_MULTIAXIAL_CURRENT_MAP                = PASS
CASE21_SPECTRAL_DOMAIN_CERTIFICATE         = PASS
N_formal_spatial_sampling                  = 0
N_formal_spatial_quadrature                = 0
N_formal_spatial_subdomains                = 1
EXACT_COMPLETE_HALFWAVE_MOMENT_CONTRACTION = PASS
SAME_EXPRESSION_DERIVATIVES                = PASS
CASE21_N48_LIMIT_ROOT                       = PASS
N96_ENGINEERING_ORDER_CHECK                = PASS
STRUCTURAL_Pu_CALIBRATION                   = NO
SWARTZ24                                   = NOT_STARTED

R10B_ZERO_SPATIAL_CASE21 = PASS_ENGINEERING
```

Next work must not modify the R10 scalar merely because Case21 is close to experiment. Before Swartz24 calculation, a common all-24-panel spectral/search-domain contract must be established.