# NZ-SCCM — N3584 common Cayley–Hamilton / moment-first D15 backend and Z0–Z6 rerun execution report

**Timestamp:** 2026-08-16 12:48 +08:00  
**Requested gate:** `UNIFIED_V1_N3584_CH_MOMENT_FIRST_D15_BACKEND_AND_Z0_Z6_RERUN_GATE`  
**Result:** `PARTIAL_PASS / STOPPED_AT_COMMON_BACKEND_TRACTABILITY_GATE`

## 1. Scope actually executed

This run inherited without modification:

```text
UNIFIED_PRODUCTION_WORKFLOW_V1
ONE_CONTINUOUS_COMPLETE_HALFWAVE
THEORETICAL SSSS/NAVIER for Zhou Z-series
NGUYEN_SECOND_ORDER
MEMBRANE_STRESS_REDISTRIBUTION = REQUIRED
R10 source current operator = frozen
NC source-fidelity candidate = N=3584
NC core = [-2.35,+1.90]
NC guard = [-2.60,+2.15]
Cayley-Hamilton = active
moment-first General-D15 = active
P,Rq,L connected-branch topology = active
same-state current tangent/KZ requirement = active
formal structural spatial quadrature = 0
formal structural spatial sampling = 0
formal spatial subdomains = 1
formal thickness quadrature = 0
```

No experiment, Zhou/Winter capacity, desired Pu, or sign of structural error was used to choose the compiler/backend.

## 2. Source-fidelity result inherited from 12:29

The 12:29 material-only gate remains valid:

```text
N=3584
E_sigma = 0.00107218
E_tangent = 0.04066517
E_divided_difference = 0.00381386
```

This gate therefore did **not** reopen R10 or re-select the material order. It tested whether that source-faithful representation can be carried through one common zero-spatial-integration structural backend for Z0–Z6.

## 3. Order-agnostic Cayley-Hamilton implementation

The former structural code had a degree-48-specific forward recurrence. The new backend first removes that fixed-order assumption by using a backward matrix-Chebyshev Clenshaw recurrence.

For

\[
f(Y)=\sum_{n=0}^{N}c_nT_n(Y),
\qquad Y=(E-l_cI)/l_h,
\]

write

\[
B_k=A_k I+G_kY,
\]

and use the 2x2 identity

\[
Y^2=K_1Y-K_2I.
\]

The recurrence is

\[
A_k=-2K_2G_{k+1}-A_{k+2}+c_k,
\]

\[
G_k=2A_{k+1}+2K_1G_{k+1}-G_{k+2},
\]

with final

\[
A_f=-K_2G_1-A_2+c_0,
\qquad
G_f=A_1+K_1G_1-G_2.
\]

This computes the weighted final polynomial directly and avoids first materializing every unweighted `T_n(Y)` field.

### Degree-48 exact identity check

The new backward pair was compared with the existing forward CH recurrence at degree 48. Maximum pair-coefficient disagreement was approximately

```text
I-pair coefficient max difference ~= 2.4e-12
Y-pair coefficient max difference ~= 1.9e-11
```

Therefore:

```text
ORDER_AGNOSTIC_CH_CLENSHAW_ALGEBRA = PASS
```

## 4. Exact low-order coefficient multiplication

A Numba-accelerated coefficient product was implemented for multiplication by the low-order invariant fields `K1,K2` using the exact Chebyshev identity

\[
T_iT_j=\frac12\left(T_{i+j}+T_{|i-j|}\right)
\]

independently in each analytic coordinate.

This operation is coefficient algebra only. It introduces no structural spatial point and no thickness integration point.

## 5. Coefficient-support compression probe

At N=3584, retaining every coefficient during every nonlinear product is expensive. To determine whether a simple coefficient-amplitude truncation could serve as the common backend, the following tolerance study was executed at a Z0 branch-neighborhood state:

```text
D=.915
q=.002573
q0=.004
```

| coefficient tolerance | Pc (MN) | Rq,c (MN mm) | elapsed (s) |
|---:|---:|---:|---:|
|2e-4|11.081098|493.845303|0.617|
|1e-4|11.107623|485.805665|0.603|
|5e-5|11.110069|485.251638|1.476|
|2e-5|11.106763|487.025622|3.282|
|1e-5|11.109297|486.610020|10.982|

The load resultant is comparatively stable, but the generalized residual does not converge monotonically with threshold because deleting coefficients changes subsequent nonlinear product support.

Decision:

```text
COEFFICIENT_THRESHOLD_PRUNING = DIAGNOSTIC_ONLY
COEFFICIENT_THRESHOLD_PRUNING_AS_EXACT_D15_PRODUCTION = NOT_ACCEPTED
```

## 6. Z0 finer diagnostic locator

Using the same N3584 source coefficients and the same structural equations at coefficient tolerance `1e-4`, a Z0 branch/peak locator was obtained:

```text
D ~= 0.9091939627
q ~= 0.00251762190
A ~= 15.1057 mm
P ~= 32.9241946 MN
Rq ~= 0.542972 MN mm
lambda_min ~= -1.073829
lambda_max ~= +0.164635
```

Phase load decomposition:

```text
Pc_eff ~= 10.983038 MN
Ps     ~= 16.922780 MN
Pw     ~=  5.018377 MN
```

This is **not a production Pu** because the coefficient-compression rule, exact same-expression `L`, and same-state `KZ` are not certified.

## 7. Z0–Z5 common-backend locator diagnostics

A coarser `2e-4` coefficient-support probe was able to follow all six Z0–Z5 branch neighborhoods under the same N3584 source compiler and same SSSS/Nguyen/membrane/phase equations:

|case|D locator|q locator|P locator (MN)|lambda_min|lambda_max|
|---|---:|---:|---:|---:|---:|
|Z0|0.907427|0.002488991|32.9277|-1.07019|+0.16276|
|Z1|0.595916|0.003143830|19.5542|-0.75095|+0.15841|
|Z2|1.133786|0.004060976|36.0559|-1.39935|+0.26556|
|Z3|0.667726|0.002496755|39.0559|-0.78827|+0.12055|
|Z4|0.932337|0.001342230|64.0427|-1.03594|+0.10360|
|Z5|0.997894|0.000184231|14.5423|-1.03404|+0.03614|

All six material envelopes remain inside the NC operational core `[-2.35,+1.90]`.

These are `BACKEND_DIAGNOSTIC_LOCATORS`, not corrected ultimate capacities.

A significant diagnostic consequence is that several of these high-source-fidelity locator loads remain close to the earlier retracted 10:43 values. Therefore the former Z0–Z4 low-load discrepancy can no longer be attributed solely to the old wide-N48 source-representation error. A production conclusion must wait until the common backend, `L`, and same-state `KZ` are fully closed.

## 8. Z6 common-backend tractability probe

The retained Z6 engineering baseline has approximately

```text
D = 1.5853259043
q = .02166488057
old continuous principal envelope ~= [-2.2937,+1.8232]
```

This state occupies almost the full frozen NC material core. The N3584 coefficient recurrence therefore retains far more analytic support than in Z0–Z5.

Observed execution boundary:

```text
full N3584 Z6 concrete evaluation, coefficient tol=2e-4:
    >180 s / not completed

full N3584 Z6 concrete evaluation, coefficient tol=1e-3:
    >120 s / not completed

N3584 T-channel Clenshaw pair alone at Z6, coefficient tol=1e-3:
    >120 s / not completed
```

This is not a mathematical inability to calculate Z6; it is a failure of the **present coefficient-tensor realization** to be a practical common backend at the source-fidelity order selected in 12:29.

## 9. Why the gate stops here

The project requires one method across specimens. It would violate the unified workflow to accept:

```text
Z0-Z5 -> N3584 threshold-compressed coefficient backend
Z6    -> old N48 backend or a different fallback solver
```

Likewise it would be invalid to release Z0–Z5 locators while `L` and `KZ` are computed under a different material/derivative approximation.

Therefore the correct fail-fast decision is:

```text
NC_N3584_SOURCE_FIDELITY = PASS
ORDER_AGNOSTIC_CH_CLENSHAW_IDENTITY = PASS
CURRENT_N3584_COEFFICIENT_TENSOR_BACKEND_COMMON_TRACTABILITY = FAIL
Z0_Z5_DIAGNOSTIC_LOCATORS = AVAILABLE
Z0_Z5_NEW_PRODUCTION_Pu = NOT_RELEASED
Z6_UNIFIED_RERUN = NOT_COMPLETED
SAME_EXPRESSION_L = NOT_COMPLETED
SAME_STATE_KZ = NOT_COMPLETED
```

## 10. Current interpretation of N=3584

The earlier wording `NC_FAMILY_ORDER=3584` is narrowed to:

```text
NC_SOURCE_FIDELITY_CANDIDATE_ORDER = 3584
```

It is **not yet** a fully promoted production family compiler because the universal workflow requires both:

1. source stress/tangent fidelity;
2. common structural tractability and exact-moment closure.

## 11. Next unique gate

`UNIFIED_V1_NC_COMPILER_STRUCTURAL_TRACTABILITY_REDESIGN_GATE`

This next gate must preserve the common mechanics while changing only the material analytic representation and/or exact coefficient contraction architecture at **family level**.

The replacement must simultaneously satisfy:

```text
same NC method for Z0-Z6 and NC+rebar/NC+shell
source-controlled stress/tangent error
zero structural spatial/thickness numerical integration
Cayley-Hamilton or equivalent approved finite matrix lift
moment-first General-D15 compatibility
same-expression P,Rq,L
same-state KZ
no specimen-response calibration
```

No Z6-only fallback and no specimen-specific compiler interval/order is permitted.
