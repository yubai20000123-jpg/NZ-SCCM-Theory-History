# NZ-SCCM governance lock — membrane redistribution downshift diagnostic

**Timestamp:** 2026-08-16 23:50 +08:00

## Locked findings

```text
CASE21_r0_to_five_membrane_shift = -12.2630%
Z6_same_direct_R10_r0_to_five_membrane_shift = -14.9915%
SYSTEMATIC_DOWNSHIFT_RELATIVE_TO_PREVIOUS_CONSTRAINED_MEMBRANE_MODEL = EVIDENCE_PRESENT
SYSTEMATIC_EXPERIMENTAL_UNDERPREDICTION = NOT_YET_PROVEN
```

## Interpretation rule

The Z6 diagnostic deliberately uses the same direct-R10 full-section audit evaluator for r=0 and five-membrane states. Therefore the roughly 15% drop cannot be attributed primarily to switching from N48 to direct R10.

The current membrane module must be audited for physical admissibility before any material recalibration or empirical correction is considered.

## Prohibited reactions

```text
DO_NOT_TUNE_R10_TO_RECOVER_CAPACITY = YES
DO_NOT_TUNE_MEMBRANE_COEFFICIENTS_TO_MATCH_CASE21_OR_Z6 = YES
DO_NOT_REUSE_CASE21_LOCAL_N48_FOR_Z6 = YES
DO_NOT_RELEASE_43.763_MN_AS_FORMAL_Z6_Pu = YES
DO_NOT_OPEN_ANOTHER_UNBOUNDED_SYMBOLIC_BACKEND_LOOP = YES
```

## Required next gate

`FIVE_MEMBRANE_PARENT_DISPLACEMENT_BOUNDARY_WORK_AND_CONDENSATION_AUDIT`

This gate must trace all five membrane coordinates to their parent in-plane displacement fields and verify edge admissibility, external work, coordinate independence, and correct internal-vs-global status. Only if that gate passes should a new formal Z6 capacity solve be pursued.
