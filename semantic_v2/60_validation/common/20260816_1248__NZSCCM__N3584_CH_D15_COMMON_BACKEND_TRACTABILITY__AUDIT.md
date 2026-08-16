# NZ-SCCM — N3584 Cayley–Hamilton / General-D15 common-backend tractability audit

**Timestamp:** 2026-08-16 12:48 +08:00  
**Identity:** CURRENT VALIDATION AUDIT

## Audit question

Can the source-faithful ordinary-concrete candidate compiler selected at `N=3584` be promoted, without changing the common calculation method, into a practical zero-spatial-integration Cayley–Hamilton / moment-first General-D15 backend for the whole current Z0–Z6 family?

## Evidence chain

1. `20260816_1229__NZSCCM__NC_FAMILY_COMPILER_FREEZE__REPRO.py` established the source-only stress/tangent/divided-difference pass at N=3584.
2. The historical coefficient-space D15 kernel establishes the finite invariant fields and exact Chebyshev moment identities.
3. `20260816_1248__NZSCCM__N3584_CH_CLENSHAW_D15_BACKEND__REPRO.py` removes the fixed-N48 recurrence assumption and implements an order-agnostic backward CH/Clenshaw pair.
4. The 12:48 execution report records coefficient-support convergence probes, Z0–Z5 branch locators, and the Z6 timeout boundary.

## Gate matrix

|Gate|Decision|Reason|
|---|---|---|
|R10 physical source unchanged|PASS|No material physics reopened|
|N3584 source stress fidelity|PASS|Inherited 12:29 source audit|
|N3584 source tangent fidelity|PASS|Inherited 12:29 source audit|
|N3584 divided-difference fidelity|PASS|Inherited 12:29 source audit|
|Order-agnostic CH algebra|PASS|N48 forward/backward pair agrees at ~1e-11 or better|
|Formal spatial sampling|PASS = 0|No spatial nodes used|
|Formal spatial quadrature|PASS = 0|No Gauss/Simpson/adaptive integral|
|Formal thickness quadrature|PASS = 0|No thickness point integration|
|Membrane redistribution retained|PASS|No stocky-case switch-off|
|Same NC compiler source protocol for Z0–Z6|PASS|No case-specific source compiler introduced|
|Coefficient-threshold compression convergence|FAIL / NOT CERTIFIED|Rq changes non-monotonically as support threshold is lowered|
|Z0–Z5 common-backend diagnostic branch accessibility|PASS DIAGNOSTIC|All six locator neighborhoods reached|
|Z0–Z5 production Pu|NOT PASSED|No certified L/KZ and no exact compression rule|
|Z6 common-backend tractability|FAIL|N3584 deep-state coefficient recurrence does not complete in practical probe windows|
|Same-expression L at production accuracy|NOT EXECUTED|Blocked by backend tractability/convergence|
|Same-state KZ at production accuracy|NOT EXECUTED|Blocked by backend tractability/convergence|
|Unified Z0–Z6 production rerun|FAIL / INCOMPLETE|Common backend not yet viable|

## Important interpretation 1 — source fidelity is necessary but not sufficient

The N=3584 material result is not being retracted as a source approximation result. Instead its identity is narrowed:

```text
N3584 = NC_SOURCE_FIDELITY_CANDIDATE_ORDER
```

A production compiler must satisfy both:

```text
SOURCE_FIDELITY
AND
COMMON_STRUCTURAL_TRACTABILITY / EXACT-MOMENT CLOSURE
```

The 12:29 work established only the first condition.

## Important interpretation 2 — the old Z0–Z5 discrepancy is reopened, not solved

The N3584 diagnostic locators remain near the previously retracted 10:43 load neighborhood for several cases. Because the old wide-N48 source error has now been strongly reduced while the load neighborhood did not automatically return to the flat/squash scale, the hypothesis

```text
OLD_LOW_Z0_Z4_LOADS_WERE_CAUSED_ONLY_BY_WIDE_N48_MATERIAL_ERROR
```

is no longer supported.

This does **not** validate the new locator loads as ultimate capacities. The production question remains open until the unified backend gives converged `Rq`, exact same-expression `L`, and same-state `KZ`.

## Important interpretation 3 — Z6 prevents specimen-specific shortcuts

The Z6 state spans nearly the whole NC material core. A coefficient representation that is cheap only for stockier Z0–Z5 but becomes impractical for Z6 is not a universal NC structural backend.

The project therefore explicitly rejects:

```text
Z0-Z5 -> new N3584 backend
Z6    -> retained old N48 backend
```

as a production architecture.

The retained `51.30 MN` Z6 number remains an engineering baseline for later comparison, not a bypass around the common backend gate.

## Audit decision

```text
N3584_SOURCE_FIDELITY = PASS
ORDER_AGNOSTIC_CH_IDENTITY = PASS
N3584_CURRENT_COEFFICIENT_TENSOR_REALIZATION = FAIL_COMMON_TRACTABILITY
N3584_PRODUCTION_FAMILY_COMPILER_PROMOTION = WITHHELD
NEW_Z0_Z5_PRODUCTION_Pu = WITHHELD
Z6_UNIFIED_RERUN = WITHHELD_PENDING_BACKEND_REDESIGN
```

## Required next gate

`UNIFIED_V1_NC_COMPILER_STRUCTURAL_TRACTABILITY_REDESIGN_GATE`

The next design must be family-level and source-controlled. A valid replacement may use factorization, low-rank analytic separation, or another finite analytic representation, but it must preserve the already frozen common mechanics and zero-spatial-integration contract.
