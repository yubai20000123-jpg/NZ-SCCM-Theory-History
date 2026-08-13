# Swartz24 validation semantic branch

Current stored validation entry:

- the 24-row C1/MM + general-D15 first-load-maximum comparison is located in `semantic_v2/50_results/swartz24/`.

## Governing-capacity boundary

The 24 stored loads are equilibrium first-load-maximum candidates. Governing physical capacity additionally requires the same-branch full current-tangent ordering:

```text
first KZ=0 vs first L=0, g:+->- maximum
```

Case21 has the formal zero-spatial ordering completed. The other 23 formal KZ orderings remain pending.

## Case1 reconstruction refinement

The 16:47 audit correctly reopened the Case1 KZ gate, but a later independent reconstruction materially narrows the diagnosis.

Current priority files:

- `20260813_TUNK__NZSCCM__CASE1__COMPILER_VALUE_SHIFT_AND_FULL_FIELD_KZ_RECONSTRUCTION__AUDIT.md`
- `20260813_TUNK__NZSCCM__CASE1__CURRENT_BRANCH_KZ__AUDIT_TRACE.csv`
- `20260813_TUNK__NZSCCM__SWARTZ24__CONTROL_ORDERING_REFINEMENT_AFTER_CASE1_RECONSTRUCTION__AUDIT.md`
- `20260813_1647__NZSCCM__SWARTZ24__LIMIT_POINT_VS_TANGENT_LOSS_CONTROL_ORDERING__AUDIT.md`
- `20260813_1035__NZSCCM__SWARTZ24__FULL_SAME_EXPRESSION_L_KZ_BULK_GATE__EXECUTION_AUDIT.md`
- `20260811_TUNK__NZSCCM__SWARTZ24__C1_TANGENT_REPAIR_AT_DIRECT_N48_STATES__AUDIT_TABLE.csv`

The Case1 independent audit reconstructs the current first load maximum at approximately

```text
D = 0.98833818
q = 0.00083313173
P = 608.92642 kN
```

versus the stored 608.925 kN. It also finds the audit-only complete-halfwave KZ remains strongly positive at the maximum, approximately +3066.68 N/mm, with all 15 checked pre-limit branch states positive.

Therefore the present evidence does **not** support an early full-field KZ zero as the cause of the Case1 +22.30% -> +24.22% worsening. The reconstructed dominant mechanism is the finite compiler value/tangent trade-off: at the same old direct-N48 state the current C1/MM value field raises P by about +19.16 kN, while re-equilibration lowers it by about -9.75 kN, leaving the observed net +9.41 kN increase.

The full-field audit uses high-order physical-space Gauss only as an independent diagnostic. It is not promoted to the formal zero-spatial D15 result. Formal Case1 KZ remains pending until the coefficient-space engine is regenerated.

Historical mechanism/source audits from 2026-08-11 are partially superseded because their Pu/error columns use old direct-N48 predictions. Their source-observation columns remain usable within provenance limits.

Experimental buckling/critical load and experimental failure/ultimate load must remain distinct quantities, but that distinction does not explain the Case1 worsening addressed here.
