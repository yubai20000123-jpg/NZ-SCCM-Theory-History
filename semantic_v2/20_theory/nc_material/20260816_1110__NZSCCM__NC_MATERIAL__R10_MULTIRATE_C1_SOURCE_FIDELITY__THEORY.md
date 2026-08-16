# NZ-SCCM NC material — R10 multirate-C1 source-fidelity rebuild

**Timestamp:** 2026-08-16 11:10 +08:00  
**Identity:** SOURCE-MATERIAL REPRESENTATION REBUILD / NO MATERIAL-PHYSICS CHANGE

## 1. Frozen R10 source

The physical source remains the R10 current operator. Its scalar primitives are

\[
\Pi_\eta(\lambda)=\frac{\lambda^2(\sqrt{\lambda^2+\eta^2}+\lambda)}{2(\lambda^2+\eta^2)},
\]

\[
c=\Pi_\eta(-\lambda),\qquad t=\Pi_\eta(\lambda),
\]

\[
C=\frac{\kappa c}{1+(\kappa-2)c+c^2},
\qquad T=\frac{u_R(t)}{\rho},
\]

\[
U=\kappa\lambda-C+\kappa c+u_R(t)-\kappa t,
\qquad T7=T^7.
\]

The C2 energy-smoothed tensile scalar `u_R` and all R10 constants are unchanged.

For two principal equivalent strains \(\lambda_+,\lambda_-\), the same R10 spectral master is retained:

\[
s_+=U_+-a_{cc}C_+^2C_-+C_+T_- -\rho a_t T_+T_-^8,
\]

\[
s_-=U_- -a_{cc}C_-^2C_+ + C_-T_+ -\rho a_tT_-T_+^8.
\]

No 2D stress-surface refit is introduced.

## 2. Why single N48 failed for the AR2 stocky set

The stocky AR2 recalculation inherited the Z6-wide material interval `[-2.35,+1.90]`. On that width, one strict-C1 degree-48 polynomial cannot resolve the R10 small-positive transition. Inside the Z0–Z5 occupied material range the old representation has approximately

```text
U  E0=.02625
C  E0=.08247
T  E0=.70402
T7 E0=.79606
```

The problem is representation capacity, not a need to change R10.

## 3. Non-partitioned multirate polynomial representation

The repair remains one global material interval:

\[
\boxed{\lambda\in[-1.50,+0.35]}.
\]

For each primitive

\[
F_N(\lambda)=\sum_{n=0}^{N}a_n\,\mathcal C_n(\xi),
\qquad
\xi=\frac{\lambda-\lambda_c}{\lambda_h},
\]

where

\[
\lambda_c=-0.575,\qquad \lambda_h=0.925.
\]

All coefficients are generated only from the R10 source function using overdetermined Chebyshev material-coordinate least squares with exact C1 constraints imposed by a KKT solve.

Orders are allocated by source difficulty:

\[
\boxed{N_U=256,\quad N_C=1024,\quad N_T=1280,\quad N_{T7}=512.}
\]

This is called

`R10-MR-C1(256,1024,1280,512)`.

It is **not** a four-zone or multi-cell material model. All four functions remain single global polynomials of the same scalar coordinate.

## 4. Exact source anchors

The R10 anchors are imposed exactly:

For U:

\[
U(0)=0,\qquad U'(0)=\kappa.
\]

For C,T,T7:

\[
F(0)=0,\qquad F'(0)=0.
\]

Numerical residuals in the generated coefficient set are around machine precision:

```text
U(0)  =  2.22e-16
U'(0) =  2.000512953367875
C(0)  =  1.11e-16
C'(0) = -4.80e-16
T(0)  = -1.11e-16
T'(0) = -2.69e-14
T7(0) =  5.55e-17
T7'(0)=  2.88e-15
```

## 5. Guard hull and operational core

Coefficients are generated on the conservative guard hull

\[
[-1.50,+0.35].
\]

The material tangent is certified for production on the inner operational core

\[
\boxed{[-1.40,+0.30]}.
\]

The earlier equation-derived Z0–Z5 ranges all fall in this core, including the former widest Z2 range approximately `[-1.3895,+.2696]`.

The next blind structural solve must re-certify this statement. The core is not a load-fitting device; leaving it is a fail-fast event requiring compiler regeneration.

## 6. Primitive source fidelity

On the operational core:

|primitive|degree|max value error|max derivative error / source peak derivative|max |a_n||sum |a_n||
|---|---:|---:|---:|---:|---:|
|U|256|8.60e-5|0.94%|0.59483|1.70739|
|C|1024|1.57e-4|7.61%|0.58126|1.65631|
|T|1280|6.01e-4|2.81%|0.32873|2.02398|
|T7|512|4.37e-4|0.69%|0.11546|1.70141|

The primitive derivative metric is reported but not by itself used as the final material-map verdict, because the R10 master combines these primitives nonlinearly.

## 7. Current-operator fidelity

The compiled primitives are reinserted into the exact unchanged R10 spectral master. No operator coefficient is fitted at this stage.

On `lambda_+,lambda_- in [-1.40,+.30]`, a source-only material-coordinate audit gives

\[
\boxed{\max |s^{MR}-s^{R10}|=4.2153\times10^{-4}}.
\]

The worst audited pair is approximately

\[
(\lambda_+,\lambda_-)=(-0.99483,+0.00108),
\]

where

```text
source   s ~= -0.99399979
compiled s ~= -0.99442132
```

For the first spectral derivatives, the maximum audited absolute discrepancy is

\[
0.8431,
\]

while the maximum source tangent magnitude on the same core is approximately

\[
29.8917.
\]

Hence

\[
\boxed{E_{tangent,rel}\approx2.82\%}.
\]

The controlling tangent point is near the R10 small-positive transition, as expected.

## 8. Improvement over the rejected wide N48 representation

On the same operational core, the old wide N48 compiler gives approximately

```text
max spectral stress error = .71852
max tangent error / source peak tangent = 81.5%
```

The multirate compiler gives

```text
max spectral stress error = .0004215
max tangent error / source peak tangent = 2.82%
```

Thus the source current-map error falls by about 1.7e3 in value and about 29 in relative tangent error.

## 9. Cayley-Hamilton / D15 identity

Every primitive remains a finite polynomial. Therefore each spectral polynomial still lifts through the same 2x2 Cayley-Hamilton identity

\[
F(\mathbf Y)=A_F\mathbf I+B_F\mathbf Y.
\]

The only change is that different primitive recurrences terminate at different finite orders. The General-D15 analytical moment definitions are unchanged.

```text
MATERIAL_ZONE_PARTITION = NO
SPATIAL_SUBDOMAIN_PARTITION = NO
SPATIAL_QUADRATURE = NO
CAYLEY_HAMILTON_THEORY_CHANGE = NO
GENERAL_D15_THEORY_CHANGE = NO
```

## 10. What has and has not passed

```text
R10_PHYSICAL_TARGET = UNCHANGED
R10_MR_C1_SOURCE_VALUE_GATE = PASS
R10_MR_C1_SOURCE_TANGENT_GATE_ON_CORE = PASS
C1_ANCHOR_GATE = PASS
O1_COEFFICIENT_GATE = PASS
FORMAL_CH_D15_COMPATIBILITY = PASS
```

But the current structural implementation still assumes N48-style fixed recurrence. Therefore this theory file does **not** promote any new Z0–Z5 Pu.

The next task is a variable-order, moment-first D15 recompile and conditioning test.