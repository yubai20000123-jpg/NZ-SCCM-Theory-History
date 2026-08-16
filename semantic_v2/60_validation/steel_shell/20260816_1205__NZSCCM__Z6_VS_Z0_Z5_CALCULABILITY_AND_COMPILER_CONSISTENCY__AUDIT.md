# NZ-SCCM — Z6 versus Z0–Z5 calculability and compiler-consistency audit

**Timestamp:** 2026-08-16 12:05 +08:00  
**Status:** CURRENT CONSISTENCY AUDIT

## Trigger

The user correctly asked why Z6 could be calculated and accepted, whereas returning to Z0–Z5 caused the workflow to stop for compiler-fidelity repair.

## Core finding

There is **no mathematical/algorithmic inability to calculate Z0–Z5** with the same old kernel. In fact the 10:43 run already produced numerical roots for all Z0–Z5.

The difference was a governance/validation inconsistency:

1. Z6 was solved earlier under the 2026-08-12 production contract, where full-hull compiler error was required to be reported but no universal reject threshold existed.
2. Z6 therefore remained accepted after obtaining a stable connected branch, very small Rq residual, compiler-domain coverage, and a final load close to Zhou/Winter.
3. The later Z0–Z5 run exposed a physically implausible 20–36% drop from the exact q=0 section strength.
4. That anomaly triggered a source-operator audit, which proved that the same wide `[-2.35,+1.90]` N48 compiler has order-one error in the small-positive tensile transition actually visited by the solutions.
5. Once that defect was proven, it became inconsistent to treat "a numerical root exists" as sufficient evidence of material-operator validity.

Therefore the correct statement is:

```text
Z0_Z5_ARE_COMPUTATIONALLY_SOLVABLE = YES
Z0_Z5_OLD_NUMBERS_ARE_PRODUCTION_RELIABLE = NO
```

## Why Z6 is not exempt from the compiler concern

The accepted Z6 final material envelope was

```text
lambda_min = -2.2936943231
lambda_max = +1.8232424497
```

which necessarily contains the same small-positive transition near `lambda≈0.04–0.05` where the wide N48 primitive errors were later found to be large.

The Z6 execution report itself already recorded a full-hull T error around `0.7046`, but the then-current contract classified it as representation uncertainty rather than a blocker.

Thus:

```text
Z6_51_30_MN = USER_ACCEPTED_ENGINEERING_RESULT
Z6_51_30_MN = NOT_PROOF_THAT_THE_WIDE_N48_COMPILER_IS_SOURCE_FAITHFUL
```

The good agreement of Z6 with Zhou/Winter may result from structural/material-load-share cancellation, regime differences, or simply that the current-map approximation error has much less influence on the final integral for that case. Agreement with a comparator cannot be used as a compiler-fidelity certificate.

## Unified consistency rule going forward

Under the 11:52 unified workflow governance, ordinary concrete must have one family-level source-only compiler/fidelity contract used unchanged for:

- NC + reinforcement;
- NC + steel shell;
- Z0–Z6 and other NC specimens.

Once that NC compiler is frozen, the consistent action is:

1. recompute Z0–Z5 with the unified NC compiler;
2. **also rerun Z6 with exactly the same unified NC compiler** as a consistency audit;
3. preserve the user-accepted `51.30 MN` as the current engineering datum until that rerun, but do not use it to waive compiler-fidelity requirements;
4. compare the rerun Z6 result against 51.30 MN to quantify how much of the old result depended on the wide N48 representation.

This avoids both inconsistent standards:

- not rejecting Z0–Z5 merely because they differ from Zhou/Winter;
- not accepting Z6 material fidelity merely because it happens to agree with Zhou/Winter.

## Current status

```text
Z6_51_30_MN = RETAINED_USER_ACCEPTED_ENGINEERING_BASELINE
Z6_UNIFIED_COMPILER_RERUN = REQUIRED_AFTER_NC_COMPILER_FREEZE
Z0_Z5_1043_RESULTS = RETRACTED_PENDING_RECALCULATION
ALL_NC_SPECIMENS_MUST_SHARE_ONE_COMPILER_WORKFLOW = ACTIVE
```

The project issue is therefore not "Z6 can be calculated but other specimens cannot". The issue is that the fidelity standard was tightened only after Z0–Z5 exposed a defect. The standard is now made uniform retroactively for future production verification.