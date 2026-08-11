# GOVERNANCE DECISION — R10B FIDELITY AUDIT AND COEFFICIENT RE-FREEZE

**Updated:** 2026-08-11 16:31 +08:00

## Decision

The R10B representation-fidelity audit remains accepted:

```text
R10B_REPRESENTATION_FIDELITY_AUDIT
= PASS_ENGINEERING_WITH_REPRODUCIBILITY_GAP
```

The exact historical coefficient generator and arrays remain unrecovered. They must not be invented retroactively.

However, the project priority is now explicitly **simplicity over unnecessary compiler refinement**. The earlier N112 re-freeze is therefore superseded.

The governing compiler order is restored to the already successful historical engineering order:

\[
\boxed{N_M=48}.
\]

The coefficient rule is the compact formula given in

- `current/theory/NZ_SCCM_R10B_COEFFICIENT_GENERATION_CONTRACT_V1_20260811.md`

and implemented by

- `current/theory/r10b_coefficient_generator_v1.py`.

The theory shall not publish long decimal coefficient arrays. It shall publish the closed R10 material formula and one general expression defining all \(a_n^{(F)}\).

Historical R10B already produced a complete N48 zero-spatial stationary root. The archived N96 fixed-D engineering audit differed by about 0.051%, which is accepted for the project's engineering purpose. No theorem-level or near-zero compiler error is required.

Therefore:

```text
MATERIAL_COMPILER_ORDER = 48
N112_REPRODUCTION_BASELINE = SUPERSEDED
N112_COEFFICIENT_TABLE = NON_GOVERNING
LONG_DECIMAL_COEFFICIENT_LISTS = NOT_THEORY
R10_CLOSED_PARAMETER_FORMULA = GOVERNING_MATERIAL_DESCRIPTION
```

If N48 later proves inadequate for another material, first recover or choose the simplest already-closed material expression consistent with the material evidence. Do not automatically increase polynomial order and do not create a new material route without explicit user approval.

No Case21/Swartz structural result is used to tune the material formula or coefficient values.
