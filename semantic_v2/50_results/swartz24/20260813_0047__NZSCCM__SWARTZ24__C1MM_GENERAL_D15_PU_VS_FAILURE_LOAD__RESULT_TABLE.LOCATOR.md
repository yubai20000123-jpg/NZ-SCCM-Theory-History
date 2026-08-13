# Canonical locator

- Canonical ID: `20260813_0047__NZSCCM__SWARTZ24__C1MM_GENERAL_D15_PU_VS_FAILURE_LOAD__RESULT_TABLE`
- Status: `CURRENT_RESULT`
- Result identity after 2026-08-13 16:47 control-ordering audit: `CURRENT_EQUILIBRIUM_LIMIT_POINT_CANDIDATE_TABLE`; only Case21 presently has completed full same-branch `L/K_Z` ordering and certified governing-capacity identity.
- Legacy path: `current/results/NZ_SCCM_SWARTZ24_CURRENT_FRESH_PU_FAILURE_COMPARISON_20260813_0047.csv`
- Legacy blob SHA: `a7be7d0890cbb8fee34fe3bd20d34c4ecd175178`
- Content: 24/24 current C1/MM + general-D15 first-load-maximum values versus experimental failure Pf.
- Limitation: does not contain current Cases1–18 `(D_u,q_u)` checkpoints; full same-branch KZ ordering is incomplete for all panels except Case21.
- Critical semantic rule: for a panel with an earlier current-branch `K_Z=0` event, the stored later load maximum is not the governing physical capacity.
- Governing correction audit: `semantic_v2/60_validation/swartz24/20260813_1647__NZSCCM__SWARTZ24__LIMIT_POINT_VS_TANGENT_LOSS_CONTROL_ORDERING__AUDIT.md`.
