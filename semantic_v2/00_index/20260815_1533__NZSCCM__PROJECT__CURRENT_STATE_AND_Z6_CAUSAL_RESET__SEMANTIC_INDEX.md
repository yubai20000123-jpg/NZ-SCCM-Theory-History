# NZ-SCCM project current state — Z6 causal reset

**Timestamp:** 2026-08-15 15:33 +08:00

## Current source-grounded correction

Z6 is **inside** Zhou Chapter-5 four-edge axial nominal parameter range, but at the extreme corner of Group 4. It is also the only current representative Z0–Z6 case with `lambda_n > 1`.

The current Zhou value `49.6724359 MN` is the output of Zhou Eqs. (5-87)/(5-88), an FE-informed Perry-Robertson lower-envelope design curve, not a literal raw FE load for a source specimen named Z6. Winter gives an upper-envelope reference around `52.001988 MN` for the same parameters.

Small Zhou-formula perturbations around Z6 are smooth; no formula singularity has been found. Therefore the 15:00 shell coefficient-composition breakdown is demoted from causal focus to a representation gate.

## Current causal status

```text
ORIGINAL_NZ_METHOD_AS_ROOT_CAUSE = NOT ESTABLISHED
Z6_OUTSIDE_ZHOU_RANGE = NO
Z6_EXTREME_CORNER = YES
Z6_ONLY_CASE_WITH_LAMBDA_N_GT_1 = YES
ZHOU_LOWER_COMPARATOR = FE_INFORMED_LOWER_ENVELOPE_DESIGN_VALUE
ZHOU_NEIGHBORHOOD_RESPONSE = SMOOTH
H0_SHELL_COMPILER_FAILURE_AS_Z6_PHYSICAL_CAUSE = REJECTED
```

## Current next task

```text
CURRENT_NEXT_TASK = Z6_UNCHANGED_NZ_METHOD_NEIGHBORHOOD_SWEEP
```

Run unchanged NZ-SCCM on:

```text
S0  a=9000 b=12000 h=130 ns=60
S1  a=8000 b=12000 h=130 ns=60
S2  a=9000 b=10000 h=130 ns=50
S3  a=8000 b=10000 h=130 ns=50
S4  a=8550 b=11400 h=130 ns=57
```

with `ls=200, ts=4, fy=355, fcu=40`, `A0=a/500`, and no changes to R10/N48/CH/D15/Nguyen/local progressive outer-shell map.

## Latest artifacts

- `semantic_v2/10_governance/20260815_1533__Z6_ORIGINAL_METHOD_CAUSAL_RESET_AND_NEIGHBOR_SWEEP__LOCK.md`
- `semantic_v2/60_validation/steel_shell/20260815_1533__NZSCCM__Z6__ZHOU_APPLICABILITY_AND_NEIGHBORHOOD_PERTURBATION__AUDIT.md`
- `semantic_v2/50_results/steel_shell/20260815_1533__ZHOU_Z6_NEIGHBORHOOD_PERTURBATION__RESULT.csv`

Historical 15:00 analytic-domain and shell-compiler files remain valid records of that H0 diagnostic route but are not the current causal priority.
