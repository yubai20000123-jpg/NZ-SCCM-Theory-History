# Swartz24 execution semantic branch

This branch distinguishes stored result values from resumable execution state and from governing control-event certification.

Current status:

- 24/24 current equilibrium-branch first-load-maximum values: present.
- Cases19–24 current `(D_u,q_u)` roots: present.
- Case21 full derivatives/KZ and same-branch control ordering: present and PASS; first load maximum occurs before tangent zero.
- Cases1–18 current corrected `(D_u,q_u)` and derivative checkpoints: not yet located in preserved current artifacts.
- Cases19,20,22,23,24: current roots retained, but full same-branch KZ ordering not yet frozen.
- exact final Aug12–13 transient batch tool source/run-id: not yet located.

Therefore:

```text
CASE21_GOVERNING_CAPACITY = CERTIFIED_CURRENT
OTHER_23_STORED_LOAD_MAXIMA = CONTROL_ORDERING_PENDING
CASE1_608p925 = LIMIT_POINT_CANDIDATE / NOT YET CERTIFIED GOVERNING Pu
```

The priority execution checkpoint is now Case1:

`semantic_v2/40_execution/swartz24/20260813_1647__NZSCCM__CASE1__CURRENT_BRANCH_KZ_CONTROL_ORDERING__RECOMPUTATION_CHECKPOINT.md`.

The governing control-ordering audit is:

`semantic_v2/60_validation/swartz24/20260813_1647__NZSCCM__SWARTZ24__LIMIT_POINT_VS_TANGENT_LOSS_CONTROL_ORDERING__AUDIT.md`.

Governing checkpoint requirements are indexed by:
`semantic_v2/10_governance/20260813_1207__NZSCCM__PROJECT__RESUMABLE_EXECUTION_CHECKPOINT_REQUIREMENTS__GOVERNANCE.LOCATOR.md`.

`NOT_YET_LOCATED` does not mean the historical computation never occurred. It means no unsupported root or KZ event may be fabricated; blank fields are allowed until recovery or fresh recomputation succeeds.
