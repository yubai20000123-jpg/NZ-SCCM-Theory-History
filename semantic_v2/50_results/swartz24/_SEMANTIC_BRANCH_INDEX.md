# Swartz24 result semantic branch

Current stored result entries:

- `20260813_0047__NZSCCM__SWARTZ24__C1MM_GENERAL_D15_PU_VS_FAILURE_LOAD__RESULT_TABLE.LOCATOR.md` — 24/24 current equilibrium-branch first-load-maximum values versus experimental failure load Pf.
- `20260813_0047__NZSCCM__SWARTZ24__PU_COMPLETION_ROOTS19_24_FAILURE_AND_EXTERNAL_SCREEN__EXECUTION_REPORT.LOCATOR.md` — 24/24 stored load maxima, current roots printed for Cases19–24, and external-panel screening.

## Governing-capacity identity correction — 2026-08-13 16:47 +08:00

The stored 24 values must not all be labeled final physical `Pu` before the same-branch tangent-stability ordering is completed.

```text
CURRENT_EQUILIBRIUM_LIMIT_POINT_VALUES = 24/24 PRESENT
CASE21_FULL_L_KZ_CONTROL_ORDERING = COMPLETE
CASE21_GOVERNING_CURRENT_CAPACITY = 365.580427565 kN
OTHER_23_FULL_SAME_BRANCH_KZ_ORDERING = PENDING
OTHER_23_GOVERNING_CAPACITY_IDENTITY = NOT_YET_CERTIFIED
CURRENT_CORRECTED_ROOTS = Cases19-24 retained
CURRENT_CORRECTED_ROOTS_Cases1-18 = NOT_YET_LOCATED
FULL_24_PANEL_CURRENT_KZ_TABLE = NOT_PRESENT / NOT_COMPLETED
```

The governing theory requires comparing the first same-branch `K_Z=0` event against the first `L=0, g:+->-` load maximum. If `K_Z=0` occurs first, the later load maximum is not the governing capacity.

Case1 is the priority recheck because its direct-N48 load maximum was `599.515895 kN` (+22.30% vs Pf) whereas the stored current C1/MM + general-D15 load maximum is `608.925 kN` (+24.22%), despite the C1 repair strongly reducing the tangent-stability proxy at the old state.

See:

- `semantic_v2/60_validation/swartz24/20260813_1647__NZSCCM__SWARTZ24__LIMIT_POINT_VS_TANGENT_LOSS_CONTROL_ORDERING__AUDIT.md`
- `semantic_v2/60_validation/swartz24/20260813_1035__NZSCCM__SWARTZ24__FULL_SAME_EXPRESSION_L_KZ_BULK_GATE__EXECUTION_AUDIT.md`

The old direct-N48 24-panel root table remains semantic history under `semantic_v2/80_history/d_g_r_routes/` and must not be used as current C1/MM + general-D15 root coordinates.
