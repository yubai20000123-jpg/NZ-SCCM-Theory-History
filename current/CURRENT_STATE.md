# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-17 00:10 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

## Current operational entry

`semantic_v2/00_index/20260817_0010__NZSCCM__PROJECT__CURRENT_STATE_MEMBRANE_CLOSURE_RECOVERED_INTERNAL_STABILITY_GATE__SEMANTIC_INDEX.md`

## Frozen backbone

```text
UNIFIED_PRODUCTION_WORKFLOW_V1=ACTIVE
ONE_CONTINUOUS_COMPLETE_HALFWAVE=ACTIVE
Nguyen second-order continuous kinematics=ACTIVE
R10=FROZEN
reinforcement before coupled solve=REQUIRED
General-D15 exact structural moments=ACTIVE
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```

## Membrane closure recovery result

The 18:48 -> 19:12 -> 21:36 transition has now been traced.

```text
1848 compatibility-coupled membrane delta = RETAIN
1912 five-term elastic Airy recovery = PASS_EXACT / RETAIN
1912 legacy N48 five-coordinate current root = REJECTED / NEW_R_SOLVE_NOT_AUTHORIZED
2136 anti-loop legacy-N48 five-coordinate production override = RETRACTED
```

The five-term basis itself remains valid. The first explicit governance regression occurred when the 21:36 anti-loop pivot restored the legacy N48 five-coordinate current root without a new mechanics/fidelity acceptance gate.

## Corrected internal membrane qualification

Current internal equilibrium remains

```text
Rm(D,q,r)=0
r=[r0,r20,r22,s02,s22]
Krr=dRm/dr
```

but `Rm=0` and `det(Krr)!=0` are not enough to authorize Schur condensation.

Stable condensation additionally requires the internal second-work block to be positive. Minimum current gate:

```text
Krr_sym=(Krr+Krr^T)/2
lambda_min(Krr_sym)>0
```

(or the strict equivalent from the final consistent tangent when its symmetry is established).

Only then may the model use

```text
r_,g=-Krr^-1 Rm_,g
Kgg_cond=Kgg-Kgr Krr^-1 Krg
```

At the first internal stability loss:

```text
INTERNAL_MEMBRANE_STABILITY_EVENT=ACTIVE
DO_NOT_CONTINUE_TO_ANOTHER_Rm_ROOT=YES
DO_NOT_SCHUR_CONDENSE_UNSTABLE_ROOT=YES
```

The event must enter the full coupled tangent / outer-limit event ordering.

## Diagnostic evidence

K-inner-product projection onto the exact elastic Airy leading direction:

```text
Case21 low-q point1: lambda_A=+1.13729089, K-perp=.1624
Case21 low-q point2: lambda_A=+1.09794176, K-perp=.2198
retracted 320.749-kN state: lambda_A=-1.14600789, K-perp=.97188
```

Direct frozen-R10 high-order oracle, at historical Case21 D,q, used only as an independent audit:

```text
scalar Airy projected equilibrium root lambda=+0.06773338661
projected derivative=+4.13439792
=> physical Airy direction does not reverse

full five-coordinate Rm=0 root exists
sym(Krr) eig ~= [-238.65,-28.05,+281.46,+492.27,+733.27]
=> root is internally unstable / saddle-like
```

Low-q point1/point2 direct-R10 `sym(Krr)` eigenvalues are all positive; the branch therefore starts internally stable and later loses that property.

The Gauss-Legendre oracle above is NOT a formal production integration route.

## Capacity status

```text
Case21 320.749185 kN = RETRACTED_AS_PHYSICAL_MEMBRANE_Pu / unstable-overrelaxation diagnostic only
Z6 43.762840 MN = RETRACTED_AS_PHYSICAL_MEMBRANE_Pu / boundary+stability diagnostic only
Case21 historical/current-support closure = 368.189 kN
Z6 retained engineering baseline = 51.30 MN
NEW_CORRECTED_MEMBRANE_REDISTRIBUTED_Pu = NOT RELEASED
```

## Recovered membrane physics/scale rule

```text
CLASSICAL_FVK_MEMBRANE_POSTBUCKLING_SIGN=POSITIVE
EDGEWARD_AXIAL_STRESS_REDISTRIBUTION=REQUIRED
Case21 M=.02869338081, (M/4)/D=.85814% -> small-perturbation expectation
Z6 M=1.69487261562, (M/4)/D=26.7275% -> first-order / strong membrane effect
M_Z6/M_Case21=59.0684
```

This is a theory/source qualification rule, not a calibration target.

## Z6 boundary rule

Z6 must not reuse the simple Case21/free-Poisson five-term membrane field. The historical Zhou/Z6 gate requires loaded-end `ux=0`, free lateral in-plane sides, and the corresponding Airy/homogeneous-biharmonic mixed-boundary family before current-material internal condensation.

## Anti-loop / anti-calibration

```text
DO_NOT_REOPEN_R10=YES
DO_NOT_TUNE_R10_TO_RECOVER_CAPACITY=YES
DO_NOT_FIT_MEMBRANE_AMPLITUDES_TO_CASE21_OR_Z6=YES
DO_NOT_USE_GAUSS_ORACLE_AS_FORMAL_PRODUCTION=YES
DO_NOT_START_ANOTHER_UNBOUNDED_SYMBOLIC_BACKEND_LOOP=YES
DO_NOT_RELEASE_NEW_Pu_BEFORE_INTERNAL_EVENT_ORDERING=YES
```

## Current unique next gate

`STABLE_CURRENT_MEMBRANE_CONDENSATION_AND_MIXED_EVENT_GATE`

First apply the corrected stable-condensation rule to the origin-connected Case21 membrane branch. Locate the first `lambda_min(Krr_sym)=0` event and establish its order relative to the retained support peak / outer limit event. Do not relax through the event. After Case21 closes, enter Z6 only with its mixed-boundary admissible membrane family.

## Current key artifacts

- `semantic_v2/00_index/20260817_0010__NZSCCM__PROJECT__CURRENT_STATE_MEMBRANE_CLOSURE_RECOVERED_INTERNAL_STABILITY_GATE__SEMANTIC_INDEX.md`
- `semantic_v2/40_execution/common/20260817_0010__NZSCCM__MEMBRANE_CLOSURE_TRANSITION_RECOVERY__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/common/20260817_0010__NZSCCM__MEMBRANE_CLOSURE_TRANSITION_RECOVERY__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/40_execution/common/20260817_0010__NZSCCM__MEMBRANE_CLOSURE_TRANSITION_RECOVERY__REPRO.py`
- `semantic_v2/60_validation/common/20260817_0010__NZSCCM__MEMBRANE_CLOSURE_TRANSITION_AND_INTERNAL_STABILITY__AUDIT.md`
- `semantic_v2/10_governance/20260817_0010__NZSCCM__STABLE_CURRENT_MEMBRANE_CONDENSATION__GATE_LOCK.md`
