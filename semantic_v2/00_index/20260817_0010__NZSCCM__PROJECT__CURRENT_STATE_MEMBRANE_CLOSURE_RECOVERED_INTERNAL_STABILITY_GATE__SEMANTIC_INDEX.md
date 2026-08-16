# NZ-SCCM PROJECT CURRENT STATE — MEMBRANE CLOSURE TRANSITION RECOVERED

**Updated:** 2026-08-17 00:10 +08:00

## Current controlling conclusion

The 18:48→19:12→21:36 transition has been audited.

```text
1848 classical compatibility-coupled membrane delta = RETAIN
1912 five-term elastic Airy/FvK recovery = RETAIN / PASS_EXACT
1912 legacy N48 five-current-coordinate root = REJECTED / NOT_AUTHORIZED
2136 anti-loop override to legacy N48 five-coordinate production = RETRACTED
```

The five-term basis is not the problem. The missing production gate was **internal membrane stability before Schur condensation**.

## Corrected internal condensation rule

For

```text
r=[r0,r20,r22,s02,s22]
```

current in-plane equilibrium still requires

`Rm(D,q,r)=0`.

But stable condensation additionally requires

`lambda_min(sym(Krr)) > 0`,

with

`Krr=dRm/dr` and `sym(Krr)=(Krr+Krr^T)/2`.

`Rm=0` plus mere invertibility of `Krr` is insufficient.

At first internal stability loss:

```text
DO_NOT_CONTINUE_TO_ANOTHER_RELAXED_Rm_ROOT
DO_NOT_SCHUR_CONDENSE_UNSTABLE_INTERNAL_ROOT
TREAT_AS_INTERNAL_MEMBRANE_STABILITY_EVENT
```

## Key diagnostic evidence

Case21 Airy-direction K-projection:

```text
low-q point1: lambda_A=+1.1373, K-perp=.1624
low-q point2: lambda_A=+1.0979, K-perp=.2198
retracted 320.75-kN state: lambda_A=-1.1460, K-perp=.9719
```

Direct frozen-R10 audit-only oracle at historical Case21 D,q:

```text
scalar Airy projected root lambda=+0.0677334
scalar projected derivative > 0
full 5-coordinate Rm=0 root exists
but sym(Krr) eigenvalues ≈ [-238.65,-28.05,+281.46,+492.27,+733.27]
=> internally unstable / saddle-like root
```

Low-q point1/point2 direct-R10 internal symmetric tangent eigenvalues are all positive, confirming that the origin-connected branch begins stable and loses stability later.

## Capacity status

```text
Case21 320.749185 kN = RETRACTED / unstable-overrelaxation diagnostic only
Z6 43.762840 MN = RETRACTED / boundary+stability diagnostic only
Case21 retained support baseline = 368.189 kN
Z6 retained engineering baseline = 51.30 MN
NEW_CORRECTED_MEMBRANE_Pu = NOT RELEASED
```

## Z6 boundary rule

Z6 cannot reuse the simple Case21/free-Poisson five-term field. Its loaded-end `ux=0` + free lateral side boundary requires the already-identified Airy/homogeneous-biharmonic mixed-boundary family before current-material condensation.

## Formal counters

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```

The direct R10 Gauss-Legendre calculation in the recovery report is explicitly an independent audit oracle only and is not a formal production integrator.

## Current unique next gate

`STABLE_CURRENT_MEMBRANE_CONDENSATION_AND_MIXED_EVENT_GATE`

First locate the first internal-stability event on the origin-connected Case21 membrane branch and determine its order relative to the retained support peak / outer limit event. Do not compute or release a new Pu before this event ordering is closed.

## Current artifacts

- `../40_execution/common/20260817_0010__NZSCCM__MEMBRANE_CLOSURE_TRANSITION_RECOVERY__EXECUTION_REPORT.md`
- `../40_execution/common/20260817_0010__NZSCCM__MEMBRANE_CLOSURE_TRANSITION_RECOVERY__PARAMS_AND_INTERMEDIATES.json`
- `../40_execution/common/20260817_0010__NZSCCM__MEMBRANE_CLOSURE_TRANSITION_RECOVERY__REPRO.py`
- `../60_validation/common/20260817_0010__NZSCCM__MEMBRANE_CLOSURE_TRANSITION_AND_INTERNAL_STABILITY__AUDIT.md`
- `../10_governance/20260817_0010__NZSCCM__STABLE_CURRENT_MEMBRANE_CONDENSATION__GATE_LOCK.md`
