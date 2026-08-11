# GOVERNANCE DECISION — R10 MATERIAL-TARGET INTENT AUDIT

**Date:** 2026-08-11 16:01 +08:00

## Decision

The R10 material-target audit is complete. Its purpose was to identify exactly what the executed R10 target is; it was **not** authorization to invent or select a new R10A material law during recovery.

The following identities are governing:

```text
R10_EXECUTED_FORMULA_RECOVERY                 = PASS
R10_SOURCE_WORK_EQUALITY                       = PASS
R10_C2_TARGET_INTERNAL_CONSISTENCY             = PASS
R10_SAME_MULTIAXIAL_REINSERTION_ARCHITECTURE   = PASS
R10_AS_TINY_LOCAL_SOURCE_PATCH                 = FAIL_DESCRIPTION
R10_AS_WHOLE_RETAINED_TENSILE_BRANCH_REBUILD   = PASS_DESCRIPTION
R10_MATERIAL_TARGET_AUDIT                      = PASS_COMPLETE
NEW_R10_TARGET_SELECTED_DURING_RECOVERY         = NO
STRUCTURAL_Pu_CALIBRATION                       = NO
```

The existing R10/R10B numerical records remain the governing executed records. The audit establishes only that the executed R10 replaces the whole retained tensile interval

\[
0\le t\le10x_{cr}
\]

with two C2 quintic branches while conserving total source work and enforcing the documented anchors.

Material-coordinate audit found approximately:

```text
max |u_R10-u_source|                         ~= 0.01831
absolute redistributed work / source work   ~= 9.89 %
positive relocated work / source work        ~= 4.95 %
first-moment shift of tensile work           ~= -5.90 %
```

These facts correct the description of R10. They do **not** by themselves replace R10 with a new local-patch law.

## Recovery-sequence correction

The agreed recovery order is restored exactly as:

```text
1. audit the R10 material target;                         DONE
2. audit R10B representation fidelity to that R10 target; NEXT
3. recover or explicitly re-freeze the coefficient-generation rule;
4. output the formal coefficient table and derivation.
```

The previously created `R10A_MATERIAL_TARGET_INTENT_RECONCILIATION` detour is revoked as recovery overreach and removed from the current branch.

## Immediate next task

```text
CURRENT_RECOVERY_NEXT_TASK
= R10B_REPRESENTATION_FIDELITY_AUDIT
```

This task must compare the frozen executed R10 scalar/current-map objects with the retained R10B finite analytic representation and available N48/N96 evidence. It must not change R10 material physics, introduce a new material target, or start Swartz24.

Only after that fidelity audit may coefficient-generator recovery/re-freezing proceed.
