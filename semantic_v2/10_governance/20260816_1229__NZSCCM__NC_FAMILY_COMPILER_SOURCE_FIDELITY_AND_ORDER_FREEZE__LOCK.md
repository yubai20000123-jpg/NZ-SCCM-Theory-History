# NZ-SCCM NC family compiler — source-fidelity / domain / order freeze

**Timestamp:** 2026-08-16 12:29 +08:00  
**Identity:** CURRENT NC-FAMILY COMPILER GOVERNANCE under `UNIFIED_PRODUCTION_WORKFLOW_V1`

## 1. Scope

This lock implements the material-compiler part of `UNIFIED_PRODUCTION_WORKFLOW_V1_IMPLEMENTATION_AND_NC_FAMILY_COMPILER_FREEZE`.

It does **not** change the frozen R10 ordinary-concrete current operator, Nguyen kinematics, membrane redistribution, General-D15, zero-spatial-integration rule, generalized `P,Rq,L` root topology, or same-state tangent/stability requirement.

The purpose is to remove specimen-by-specimen compiler choices.

## 2. NC family core and guard domains

Current NC operational principal-coordinate core:

```text
LAMBDA_CORE_NC = [-2.35,+1.90]
```

This single core contains the current Case21/Swartz operating range and the historical Z0-Z6 ranges, including the old Z6 envelope `[-2.2936943231,+1.8232424497]`.

Coefficient generation is performed on the larger fixed guard interval

```text
LAMBDA_GUARD_NC = [-2.60,+2.15]
```

so endpoint derivative ringing is kept outside the operational core. The guard is a **material-coordinate guard**, not a structural spatial subdomain.

If a future admissible NC calculation exits the core, the response is family-level core/guard enlargement and family recompilation; a one-off specimen compiler is prohibited.

## 3. Common finite analytic architecture

For the current R10 spectral decomposition the compiler channels remain

```text
U, C, T, T7
```

and each channel uses one global Chebyshev polynomial of the **same family order `N_NC`** on the guard interval. There is no material-coordinate piecewise split and no structural spatial split.

Coefficient generation is an oversampled Gauss-Chebyshev least-squares projection with exact R10 C1 constraints at `lambda=0` using the diagonal normal matrix and the 2x2 Schur correction. The oversampling count is

```text
M = 8*(N+1)
```

for every channel.

The source C1 anchors are

```text
U(0)=0, U'(0)=kappa
C(0)=C'(0)=0
T(0)=T'(0)=0
T7(0)=T7'(0)=0
```

## 4. Project-wide source-fidelity metrics

Compiler acceptance is based on the **assembled source current operator**, not on structural `Pu`, experiment, Zhou/Winter or error sign.

On the NC operational core define:

```text
E_sigma = max spectral-current-stress error / max source spectral-current-stress magnitude
E_tan   = max spectral Jacobian error / max source spectral Jacobian magnitude
E_div   = max spectral divided-difference error / max source divided-difference magnitude
```

The divided difference is `(s1-s2)/(lambda1-lambda2)` with its continuous equal-principal-value limit. It audits the rotational/eigenprojector part of the consistent isotropic spectral tangent.

The V1 compiler gates are frozen as

```text
E_sigma <= 0.005   # 0.5%
E_tan   <= 0.05    # 5%
E_div   <= 0.05    # 5%
```

These thresholds are source-only numerical-compiler tolerances. They are intentionally smaller than the several-percent structural/model discrepancies being studied and are not theorem-level remainder certificates.

## 5. Deterministic order ladder

The same order-selection rule is used without case IDs:

```text
48, 96, 192, 384, 768,
then 1024, 1280, 1536, ... in increments of 256
```

At every candidate order the full current-stress and current-tangent gates above are audited on the fixed family core. The first candidate satisfying all three gates is frozen.

For the current frozen R10 NC family this procedure gives

```text
N_NC = 3584
```

`N=3328` fails the tangent gate; `N=3584` passes. Therefore 3584 is not a manually tuned Z-series order and is not selected from any structural load result.

## 6. R10 material-parameter envelope audited

The current Swartz NC source records contain the R10 normalized initial-slope envelope

```text
kappa_min = 1.9993148515
kappa_ref = 2.0005129533678754
kappa_max = 2.0008935611
```

The order-3584 compiler passes the same gates at all three audit values. Any future NC input outside the frozen parameter envelope must be reported and audited before production promotion; it may not silently use a specimen-specific order.

## 7. Structural identity retained

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
Nguyen second-order kinematics = ACTIVE
MEMBRANE_STRESS_REDISTRIBUTION = REQUIRED
CAYLEY_HAMILTON / approved matrix lift = ACTIVE
GENERAL_D15_MOMENT_FIRST = ACTIVE
P,Rq,L connected-branch root = ACTIVE
same-state material+geometric tangent audit = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

The high material polynomial order is an algebraic representation resolution. It does not introduce structural material points or spatial quadrature.

## 8. Production status boundary

```text
NC_R10_SOURCE_OPERATOR = FROZEN
NC_COMPILER_SOURCE_FIDELITY_CONTRACT = FROZEN
NC_CORE_GUARD_DOMAIN = FROZEN_CURRENT
NC_FAMILY_ORDER = 3584
NC_SOURCE_FIDELITY_GATE = PASS
NC_N3584_TO_MOMENT_FIRST_D15_STRUCTURAL_BACKEND = NOT_YET_EXECUTED
Z0_Z6_UNIFIED_RERUN = PENDING_STRUCTURAL_BACKEND_GATE
```

The next gate is therefore not another compiler-order change. It is the common high-order Cayley-Hamilton / moment-first General-D15 implementation and tractability audit, followed by a single-workflow Z0-Z6 rerun.
