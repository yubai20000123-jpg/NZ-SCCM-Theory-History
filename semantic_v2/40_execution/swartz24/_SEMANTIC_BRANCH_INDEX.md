# Swartz24 execution semantic branch

This branch distinguishes stored result values from resumable execution state, audit reconstruction, and governing control-event certification.

Current status:

- 24/24 current equilibrium-branch first-load-maximum values: present.
- Cases19–24 current `(D_u,q_u)` roots: present.
- Case21 full derivatives/KZ and same-branch control ordering: formal zero-spatial PASS; first load maximum occurs before tangent zero.
- Cases1–18 final preserved current corrected roots: not located in the historical committed artifacts.
- Case1 current root has now been independently reconstructed from the frozen current equations as an AUDIT-ONLY state: approximately `D=0.98833818`, `q=0.00083313173`, `P=608.92642 kN`, reproducing the stored 608.925 kN.
- Case1 audit-only full-field KZ at that state is approximately `+3066.68 N/mm`; 15 checked pre-limit branch states remain positive.
- Case1 formal zero-spatial general-D15 KZ: still pending.
- Cases19,20,22,23,24: current roots retained, but full same-branch formal KZ ordering not yet frozen.
- exact final Aug12–13 transient batch tool source/run-id: not located.

Therefore:

```text
CASE21_GOVERNING_CAPACITY = CERTIFIED_CURRENT
CASE1_CURRENT_LIMIT_POINT_STATE = RECONSTRUCTED_AUDIT_ONLY
CASE1_CURRENT_FULL_FIELD_KZ = POSITIVE_IN_AUDIT / FORMAL_D15_PENDING
CASE1_608p925 = LIMIT_POINT_CANDIDATE / PRODUCTION_CONTROL_IDENTITY_HOLD
OTHER_22_STORED_LOAD_MAXIMA = CONTROL_ORDERING_PENDING
```

Priority execution checkpoints:

- `20260813_1647__NZSCCM__CASE1__CURRENT_BRANCH_KZ_CONTROL_ORDERING__RECOMPUTATION_CHECKPOINT.md`
- `20260813_TUNK__NZSCCM__CASE1__CURRENT_BRANCH_RECONSTRUCTION_AFTER_FULL_FIELD_AUDIT__EXECUTION_CHECKPOINT.md`

Priority validation audit:

- `semantic_v2/60_validation/swartz24/20260813_TUNK__NZSCCM__CASE1__COMPILER_VALUE_SHIFT_AND_FULL_FIELD_KZ_RECONSTRUCTION__AUDIT.md`

The remaining production task is not to guess a lower Case1 capacity. It is to regenerate the current coefficient-space/general-D15 full KZ at the reconstructed current branch and formally establish the control ordering.

Governing checkpoint requirements are indexed by:
`semantic_v2/10_governance/20260813_1207__NZSCCM__PROJECT__RESUMABLE_EXECUTION_CHECKPOINT_REQUIREMENTS__GOVERNANCE.LOCATOR.md`.

`NOT_LOCATED` or `FORMAL_PENDING` never authorizes substitution of an old direct-N48 root, a spatial audit result, or an experimental target. Blank formal fields remain acceptable until the zero-spatial engine is recovered or reconstructed.
