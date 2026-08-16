# NC + rebar panel theory semantic branch

## Current production identity

The previously published Case21 five-free-coordinate membrane result `320.749185 kN` is retracted as a physical membrane Pu. It remains diagnostic evidence of unstable internal over-relaxation.

Current controlling mechanics are the recovered historical RC backbone plus a compatibility/equilibrium membrane-redistribution layer whose internal coordinates may be Schur-condensed **only while the internal membrane block remains stable**.

## Active mechanics

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
 -> global (D,q), A=bq
 -> Nguyen second-order continuous strain
 -> five-term leading compatible membrane subspace r=[r0,r20,r22,s02,s22]
 -> same-state R10 concrete + reinforcement
 -> solve Rm=0
 -> verify internal membrane stability lambda_min(sym(Krr))>0
 -> ONLY THEN Schur-condense r
 -> outer P,Rq,L / same-state KZ event ordering
```

At first `lambda_min(sym(Krr))=0`, the internal membrane mode is an explicit stability event. The solver must not jump to another relaxed `Rm=0` root and must not condense an unstable internal state.

## Historical recovery

```text
20260816_1848 compatibility-coupled Airy/FvK delta = RETAIN
20260816_1912 five-term elastic Airy recovery = PASS_EXACT
20260816_1912 legacy N48 five-coordinate current solve = REJECTED / NEW_R_SOLVE_NOT_AUTHORIZED
20260816_2136 anti-loop override to legacy N48 five-coordinate production = RETRACTED
```

## Exact elastic leading direction

For square halfwave and `nu=.18`:

```text
r/M=[-.295,-.205,+.25,-.205,+.25]
Kbar eig=[.205,.5,.5,.5,1]
```

This reproduces the positive classical Airy/FvK postbuckling membrane redistribution exactly.

## Case21 diagnostic

Airy-direction K-projection:

```text
low-q point1: lambda_A=+1.1373, K-perp=.1624
low-q point2: lambda_A=+1.0979, K-perp=.2198
retracted 320.749-kN state: lambda_A=-1.1460, K-perp=.9719
```

A direct frozen-R10 audit-only oracle confirms that a full five-coordinate `Rm=0` root can become internally unstable:

```text
sym(Krr) eig ~= [-238.65,-28.05,+281.46,+492.27,+733.27]
```

while the two low-q states retain all-positive internal symmetric tangent eigenvalues.

Therefore:

```text
Case21 320.749185 kN = RETRACTED / unstable-overrelaxation diagnostic
NEW_CORRECTED_CASE21_MEMBRANE_Pu = NOT RELEASED
```

Retained support baseline pending corrected event ordering:

`Case21 historical/current-support closure = 368.189 kN`.

## Compiler identity / scope

Case21-local N48 remains useful as a value-evaluator regression object on its certified local interval, but the 19:12 legacy-five-coordinate production rejection is controlling for this membrane-root task. N48 is not a universal NC-family compiler and Case21 coefficients must not be reused for Z6.

## Z6 boundary

Z6 requires its historical mixed in-plane boundary class:

```text
loaded ends ux=0
lateral sides in-plane free
```

and the corresponding Airy/homogeneous-biharmonic family before current-material internal condensation. Simple Case21/free-Poisson five-term fields are not a complete Z6 closure.

Retained Z6 support baseline pending corrected closure: `51.30 MN`.

## Formal zero-integration identity

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```

Direct Gauss-Legendre calculations used in the recovery gate are independent audit oracles only, not formal production integration.

## Current next task

`STABLE_CURRENT_MEMBRANE_CONDENSATION_AND_MIXED_EVENT_GATE`

First locate the first internal-stability event on the origin-connected Case21 membrane branch and compare its order with the retained support peak / outer limit event. Do not relax through the event and do not release a new Pu before the ordering is closed.

## Current artifacts

- `../../00_index/20260817_0010__NZSCCM__PROJECT__CURRENT_STATE_MEMBRANE_CLOSURE_RECOVERED_INTERNAL_STABILITY_GATE__SEMANTIC_INDEX.md`
- `../../40_execution/common/20260817_0010__NZSCCM__MEMBRANE_CLOSURE_TRANSITION_RECOVERY__EXECUTION_REPORT.md`
- `../../40_execution/common/20260817_0010__NZSCCM__MEMBRANE_CLOSURE_TRANSITION_RECOVERY__PARAMS_AND_INTERMEDIATES.json`
- `../../40_execution/common/20260817_0010__NZSCCM__MEMBRANE_CLOSURE_TRANSITION_RECOVERY__REPRO.py`
- `../../60_validation/common/20260817_0010__NZSCCM__MEMBRANE_CLOSURE_TRANSITION_AND_INTERNAL_STABILITY__AUDIT.md`
- `../../10_governance/20260817_0010__NZSCCM__STABLE_CURRENT_MEMBRANE_CONDENSATION__GATE_LOCK.md`
