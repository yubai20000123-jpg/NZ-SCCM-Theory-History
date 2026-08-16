# NZ-SCCM — R10 global-order cause and intrinsic-factor validation audit

**Timestamp:** 2026-08-16 13:55 +08:00

## Audit questions

1. Does the frozen R10 source intrinsically require a thousands-order description?
2. Which source factor creates the wide-global polynomial pressure?
3. Is there numerical evidence for a substantially lower-complexity source-faithful factorization before structural integration?

## Findings

### A. Historical consistency — PASS

The current diagnosis matches earlier project evidence:

- R5 already separated a material-faithful high-order object from the structural adapter/expression-swell failure.
- G26/moment-first was created specifically to avoid expand-all-then-D15.
- Compiler experiments M1R/PF1/P2A were never authorized to replace the current-map architecture.
- The energy-potential gate explicitly rejected hidden global high-degree coefficient inflation as a mechanical simplification strategy.
- R10 itself is a low-parameter C2 quintic material construction.

### B. Intrinsic scale localization — PASS

```text
eta = .0024993589727
core width / eta  = 1700.436
 guard width / eta = 1900.487
```

The N3584 maximum C/T derivative errors occur near `lambda≈±.0028-.0029`, i.e. the `Pi_eta` sign-split layer.

At N3584, the `Pi_eta` factor alone still has approximately `5.8e-2` maximum derivative error in the wide single-global lambda polynomial.

Therefore the global-order pressure is localized and source-factor specific rather than distributed uniformly across the material law.

### C. Local source simplicity — PASS

- `C(c)` is a simple rational function. In its natural coordinate, N=6 already gives about 3.88% peak-normalized derivative error and N=10 about 0.173%.
- `u_R(t)` is two C2 quintics plus a constant branch. In its natural coordinate, N=64 gives about 3.59% peak-normalized derivative error.

The source-law complexity is therefore not commensurate with 3584 independent global polynomial modes.

### D. Low-complexity material-only factor screen — PASS DIAGNOSTIC

With exact `Pi_eta`, N_C=6 and N_u=64:

```text
E_sigma = .003337
E_tangent = .030469
E_divided_difference = .046869
```

All existing material source-fidelity thresholds pass.

Fitted coefficient count:

```text
7 + 65 = 72
```

versus

```text
4*(3584+1)=14340
```

for the four-channel global N3584 candidate.

### E. Production D15 compatibility — OPEN

The factor screen leaves `Pi_eta` exact. The exact algebraic square-root/rational sign splitter has not yet been contracted through the formal General-D15 structural moment engine.

Hence the 72-coefficient screen is **not** a production compiler and cannot be used for Pu, Rq, L or KZ.

## Verdict

```text
R10_PHYSICS_CAUSES_3584_INTRINSICALLY = NOT_SUPPORTED
GLOBAL_LAMBDA_COORDINATE_MISMATCH = STRONGLY_SUPPORTED
PI_ETA_SIGN_SPLIT = PRIMARY_GLOBAL_ORDER_PRESSURE
C2_TENSILE_KNOTS = SECONDARY_PRESSURE
N3584_SOURCE_FIDELITY_WITNESS = RETAIN
N3584_NEXT_PRODUCTION_BASIS = REJECT
LOW_COMPLEXITY_INTRINSIC_FACTOR_MATERIAL_SCREEN = PASS_DIAGNOSTIC
PI_TO_ZERO_SPATIAL_EXACT_MOMENT_ADAPTER = OPEN
```

## Required next gate

`UNIFIED_V1_R10_INTRINSIC_SCALE_FACTORIZED_PI_ADAPTER_GATE`

No source smoothing-width change is authorized by this audit. R10 remains frozen until/unless a later explicit material-regularization gate is approved.
