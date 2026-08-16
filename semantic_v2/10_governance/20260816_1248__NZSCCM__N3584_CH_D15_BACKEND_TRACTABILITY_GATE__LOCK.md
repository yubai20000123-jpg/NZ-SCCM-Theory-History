# NZ-SCCM — N3584 Cayley–Hamilton / moment-first D15 backend tractability gate

**Timestamp:** 2026-08-16 12:48 +08:00  
**Gate:** `UNIFIED_V1_N3584_CH_MOMENT_FIRST_D15_BACKEND_AND_Z0_Z6_RERUN_GATE`  
**Decision:** `PARTIAL_PASS_BACKEND_IDENTITY / FAIL_PRODUCTION_TRACTABILITY`

## 1. Governing interpretation

The 12:29 result remains valid as a **source-fidelity result**:

```text
R10_SOURCE_OPERATOR = FROZEN
NC_SOURCE_FIDELITY_ORDER = 3584
CORE = [-2.35,+1.90]
GUARD = [-2.60,+2.15]
E_sigma <= .005
E_tangent <= .05
E_divided_difference <= .05
```

However, this gate proves that source fidelity alone is not sufficient to promote `N=3584` to a production family compiler. A production compiler must also be structurally tractable through the same Cayley-Hamilton / moment-first General-D15 backend for the full intended NC specimen family, including Z6.

Therefore:

```text
NC_N3584_SOURCE_FIDELITY_FREEZE = PASS
NC_N3584_PRODUCTION_COMPILER_FREEZE = NOT_PASSED
```

## 2. Order-agnostic Cayley-Hamilton Clenshaw identity

For the frozen Chebyshev material polynomial

\[
f(Y)=\sum_{n=0}^{N}c_nT_n(Y),
\qquad
Y=(E-l_cI)/l_h,
\]

use backward Clenshaw rather than building every unweighted `T_n(Y)` forward:

\[
B_{N+1}=B_{N+2}=0,
\qquad
B_k=2YB_{k+1}-B_{k+2}+c_kI.
\]

With the 2x2 Cayley-Hamilton identity

\[
Y^2=K_1Y-K_2I
\]

and

\[
B_k=A_kI+G_kY,
\]

the recurrence is

\[
A_k=-2K_2G_{k+1}-A_{k+2}+c_k,
\]

\[
G_k=2A_{k+1}+2K_1G_{k+1}-G_{k+2}.
\]

The final pair is

\[
f(Y)=A_fI+G_fY,
\]

\[
A_f=-K_2G_1-A_2+c_0,
\qquad
G_f=A_1+K_1G_1-G_2.
\]

This is algebraically order-agnostic and retains the same R10 -> Cayley-Hamilton -> General-D15 architecture. No spatial collocation or quadrature is introduced.

## 3. What passed

At degree 48 the backward pair recurrence was checked against the historical forward Cayley-Hamilton recurrence in coefficient space. The maximum pair-coefficient disagreement was at floating roundoff scale (about `2.4e-12` for the scalar-I pair and `1.9e-11` for the Y pair in the benchmark state).

Thus:

```text
ORDER_AGNOSTIC_CH_CLENSHAW_IDENTITY = PASS
NO_NAIVE_FORWARD_UNWEIGHTED_TN_BUILD = PASS
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_SPATIAL_SUBDOMAINS = 1
FORMAL_THICKNESS_QUADRATURE = 0
```

## 4. Coefficient-space compression is not yet a production proof

For `N=3584`, a coefficient-space tail-pruning tolerance was introduced only to test tractability. This is not spatial discretization, but it is an algebraic approximation and therefore must itself converge before production promotion.

At the Z0 diagnostic state `D=.915, q=.002573`, concrete resultants were:

| coefficient tolerance | Pc (MN) | Rq,c (MN mm) | time (s) |
|---:|---:|---:|---:|
|2e-4|11.081098|493.845303|0.617|
|1e-4|11.107623|485.805665|0.603|
|5e-5|11.110069|485.251638|1.476|
|2e-5|11.106763|487.025622|3.282|
|1e-5|11.109297|486.610020|10.982|

The load component is fairly stable, while the generalized residual is non-monotone at the sub-percent level because threshold pruning changes the retained coefficient support. Therefore the pruning operation cannot yet be called an exact/frozen production D15 backend.

## 5. Z0–Z5 locator calculations are diagnostic only

Using the same frozen N3584 source compiler and the same SSSS/Nguyen/membrane/steel-phase equations, a `2e-4` coefficient-space locator was able to follow Z0–Z5 branch neighborhoods. These are saved only as backend diagnostics, not new production Pu values:

|case|D locator|q locator|P locator (MN)|lambda_min|lambda_max|
|---|---:|---:|---:|---:|---:|
|Z0|0.907427|0.00248899|32.9277|-1.07019|0.16276|
|Z1|0.595916|0.00314383|19.5542|-0.75095|0.15841|
|Z2|1.133786|0.00406098|36.0559|-1.39935|0.26556|
|Z3|0.667726|0.00249675|39.0559|-0.78827|0.12055|
|Z4|0.932337|0.00134223|64.0427|-1.03594|0.10360|
|Z5|0.997894|0.000184231|14.5423|-1.03404|0.03614|

All six diagnostic material envelopes remain inside the frozen NC core `[-2.35,+1.90]`.

These values are **not** released as corrected ultimate capacities because the common `L` condition, same-state KZ audit, and coefficient-compression convergence are not yet closed.

## 6. Decisive failure at Z6

The user-accepted Z6 engineering state is approximately

```text
D = 1.5853259043
q = .02166488057
lambda envelope ~= [-2.2937,+1.8232]
```

which occupies almost the entire frozen NC core. At that state the N3584 coefficient-space field loses the strong compression available in the stockier/narrower-spectrum cases.

Observed execution boundary:

```text
N3584 Z6 full concrete evaluation, coefficient tol=2e-4: >180 s / not completed
N3584 Z6 full concrete evaluation, coefficient tol=1e-3: >120 s / not completed
N3584 Z6 T-channel Clenshaw pair alone, coefficient tol=1e-3: >120 s / not completed
```

Therefore the present N3584 + threshold-compressed 3D coefficient backend is not a viable common production backend for Z0–Z6.

This is exactly the kind of failure the unified-workflow rule is intended to catch: Z0–Z5 may not be allowed to use one cheap backend while Z6 silently receives a different structural solver.

## 7. Gate decision

```text
R10_SOURCE_PHYSICS = UNCHANGED
NC_N3584_SOURCE_FIDELITY = PASS
ORDER_AGNOSTIC_CH_CLENSHAW_ALGEBRA = PASS
Z0_Z5_DIAGNOSTIC_LOCATOR = EXECUTED
Z0_Z5_PRODUCTION_Pu = NOT_RELEASED
Z6_N3584_COMMON_BACKEND_TRACTABILITY = FAIL
SAME_EXPRESSION_L_AND_KZ_FINAL_CERTIFICATION = NOT_COMPLETED
UNIFIED_Z0_Z6_PRODUCTION_RERUN = NOT_COMPLETED
```

The earlier statement `NC_FAMILY_ORDER=3584` must henceforth be read as **source-fidelity candidate order**, not as a fully promoted production compiler.

## 8. Next unique gate

`UNIFIED_V1_NC_COMPILER_STRUCTURAL_TRACTABILITY_REDESIGN_GATE`

The next gate must retain all common mechanics and zero-spatial-integration constraints, but redesign the **material analytic representation and/or exact coefficient-space contraction architecture at family level** so that one NC method is both source-faithful and structurally tractable for Z0–Z6.

Allowed directions include a universal factorized/low-rank analytic coefficient representation or another finite analytic material-family representation whose error is source-controlled and whose contraction remains General-D15 compatible.

Not allowed:

```text
case-specific compiler intervals/orders
Z6-only fallback solver
spatial Gauss/Simpson/adaptive integration
spatial collocation/material-point grid
experiment/Zhou/Winter-driven representation tuning
reopening Nguyen second-order kinematics
turning membrane redistribution off for stocky cases
```
