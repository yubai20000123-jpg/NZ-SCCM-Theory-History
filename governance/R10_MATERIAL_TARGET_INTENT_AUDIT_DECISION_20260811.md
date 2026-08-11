# GOVERNANCE DECISION — R10 MATERIAL-TARGET INTENT AUDIT

**Date:** 2026-08-11 15:30 +08:00

## Decision

The frozen R10 execution has been re-audited against both the source Foster formula and the previously stated material-modification intent.

The following identities are now governing:

```text
R10_EXECUTED_FORMULA_RECOVERY                 = PASS
R10_SOURCE_WORK_EQUALITY                       = PASS
R10_C2_TARGET_INTERNAL_CONSISTENCY              = PASS
R10_SAME_MULTIAXIAL_REINSERTION_ARCHITECTURE    = PASS
R10_AS_TINY_LOCAL_SOURCE_PATCH                  = FAIL_DESCRIPTION
R10_AS_WHOLE_RETAINED_TENSILE_BRANCH_REBUILD    = PASS_DESCRIPTION
R10_ORIGINAL_INTENT_VS_EXECUTED_TARGET           = HOLD_RECONCILIATION
STRUCTURAL_Pu_CALIBRATION                       = NO
```

The existing R10/R10B numbers are not revoked. They remain valid records of the actually executed R10 target.

However, R10 must no longer be described in formal theory merely as a tiny local smoothing of a narrow Foster peak. The executed target replaces the whole retained tensile interval

\[
0\le t\le10x_{cr}
\]

with two C2 quintic branches while conserving total source work and enforcing selected physical anchors.

## Why reconciliation is required

The source and R10 targets have nearly the same peak magnitude, but their tensile-work distribution differs materially across the retained interval. Material-coordinate audit finds approximately:

```text
max |u_R10-u_source|       ~= 0.01831
absolute redistributed work/source work ~= 9.89 %
positive relocated work/source work      ~= 4.95 %
first-moment shift of tensile work        ~= -5.90 %
```

Therefore equal total work does not imply a local or negligible material modification.

The original design intent recorded in conversation evidence emphasized source preservation outside the necessary sharp-feature regularization region. The executed R10 instead performs a broader retained-branch reconstruction. These two identities must be reconciled before R10B coefficient publication/reconstruction proceeds.

## Frozen boundaries during reconciliation

- do not use Case21 or Swartz structural capacity to choose the R10 target;
- do not retune `h` to improve the Case21 result;
- do not modify the multidimensional CC/TC/TT interaction while resolving this 1D identity;
- do not start a new global energy-potential fit;
- do not freeze or publish an R10B coefficient generator until the final R10 material target identity is resolved;
- do not reinterpret this audit as a failure of the zero-spatial D15 architecture.

## Immediate next task

```text
CURRENT_RECOVERY_NEXT_TASK
= R10A_MATERIAL_TARGET_INTENT_RECONCILIATION
```

R10A must decide, on material/source/analytic grounds only, between:

```text
A. retain the already executed whole-retained-branch C2 energy reconstruction;

or

B. restore a genuinely local source-preserving regularization that changes only the minimum necessary 1D sharp-feature region.
```

No structural load calibration is allowed in that decision.

The production-stage R11 Swartz24 precheck remains a separate later task and is not executed while this active R10/R10B reproducibility reconciliation is in progress.
