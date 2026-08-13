# NC material semantic branch

## Current material target

- R10 material target: CURRENT_SUPPORT / FROZEN in the current NC+rebar production chain.
- Current finite compiler identity remains: U/C/T7 = N48-C1; T = N48-C1 constrained minimax; order 48.

## 2026-08-13 compiler-fidelity review

New source-only audit:

- `20260813_1719__NZSCCM__NC_MATERIAL__VALUE_TANGENT_BALANCED_MINIMAX_AND_REACHABLE_SPECTRUM__COMPILER_AUDIT.md`

The audit was triggered by the Case1 reconstruction showing that C1/MM changes material values as well as tangents. It introduces a **candidate only** balanced-minimax (BMM) objective that simultaneously controls full-hull value and first-tangent fidelity relative to their independently attainable degree-48 optima, under the same exact R10 C1 anchors.

Important governance:

```text
BMM = SOURCE_FIDELITY_CANDIDATE / NOT_PRODUCTION
CURRENT_N48_C1_MM = RETAINED_PRODUCTION_PENDING_REVIEW
EXPERIMENT_IN_COMPILER_OBJECTIVE = NO
STRUCTURAL_Pu_BACKFIT = NO
R10_CHANGED = NO
N48_ORDER_CHANGED = NO
```

The same audit also identifies a candidate non-calibrating self-consistency route for the compiler interval using continuous structural principal-spectrum enclosure. No trial narrowed interval is promoted to production.

## Key legacy/current-support bodies

- `current/theory/NZ_SCCM_R10_1D_ENERGY_SMOOTHING_REINSERTION_CASE21_20260810.md`
- `current/theory/NZ_SCCM_R10_MATERIAL_TARGET_INTENT_AUDIT_20260811.md`
- `governance/R10_1D_ENERGY_SMOOTHING_DECISION_20260810.md`
- `governance/R10_MATERIAL_TARGET_INTENT_AUDIT_DECISION_20260811.md`
- `governance/N48_C1_TENSILE_MINIMAX_BOUNDARY_LAYER_DECISION_20260812.md`

Older direct-N48, global-energy, rational/PF1 and other compiler routes belong to semantic history/rejected branches and do not become current merely because some files remain under `current/theory`.
