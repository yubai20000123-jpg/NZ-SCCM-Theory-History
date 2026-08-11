# GOVERNANCE DECISION — R10B FIDELITY AUDIT AND COEFFICIENT RE-FREEZE

**Date:** 2026-08-11 16:05 +08:00

## Decision

Recovery step 2 is closed:

```text
R10B_REPRESENTATION_FIDELITY_AUDIT
= PASS_ENGINEERING_WITH_REPRODUCIBILITY_GAP
```

The historical R10B finite representation is accepted as engineering-faithful to the executed R10 target on the retained Case21 spectral branches, based on the archived N48 scalar error table and the combined N48/N96 structural order-sensitivity evidence.

The exact historical coefficient generator remains unrecovered:

```text
HISTORICAL_COEFFICIENT_GENERATOR = UNRECOVERED
HISTORICAL_COEFFICIENT_ARRAYS    = UNRECOVERED
```

Therefore recovery step 3 is closed by an explicit new reproducibility convention rather than by pretending to recover the missing historical implementation:

```text
R10B_COEFFICIENT_GENERATION_CONVENTION
= CHEBYSHEV_ROOT_DCT_V1
```

The convention is fully defined in:

- `current/theory/NZ_SCCM_R10B_COEFFICIENT_GENERATION_CONTRACT_V1_20260811.md`
- `current/theory/r10b_coefficient_generator_v1.py`

For the deterministic full-hull convention, the first tested order in the sequence 48,56,... that passes all four archived N48 material error ceilings for both max and p95 errors is:

```text
MATERIAL_REPRODUCTION_ORDER = 112
```

This is an analytic compiler order only. It changes no R10 material parameter.

## Important identity boundary

The previous N48 coefficient generator is not retroactively redefined. Historical N48 remains historical evidence.

The newly frozen N112 convention is a **new transparent reproducibility baseline** generated directly from the already executed R10 material formulas.

No Case21 or Swartz test load is used to choose the convention or N=112. N=112 is selected solely by material-coordinate fidelity relative to the archived historical N48 material error ceilings.

## Structural boundary

The structural spatial order is not re-frozen in this decision because the historical order study changed N_M and N_S simultaneously.

The next and only next task is:

```text
CURRENT_RECOVERY_NEXT_TASK
= RECOMPILE_N112_MATERIAL_BASELINE_IN_EXISTING_ZERO_SPATIAL_D15_BACKEND
```

That task must:

1. use the frozen N112 material coefficients without material retuning;
2. reuse the existing Cayley-Hamilton/D15 coefficient algebra;
3. determine the smallest spatial coefficient order meeting the engineering order gate;
4. regenerate P,R and same-expression derivatives;
5. reclose the Case21 stationary root;
6. compare with the historical R10B result only after the new reproducible chain is complete.

No new material route is authorized.
