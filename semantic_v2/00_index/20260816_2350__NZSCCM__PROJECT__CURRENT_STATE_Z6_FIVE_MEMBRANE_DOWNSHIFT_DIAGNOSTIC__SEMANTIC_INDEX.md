# NZ-SCCM semantic current-state index

**Timestamp:** 2026-08-16 23:50 +08:00

## Current status

Case21 formal five-membrane result remains:

```text
Pu=320.749185 kN
error vs experiment 336 kN = -4.5389%
r=0 -> five-membrane shift = -12.2630%
```

Z6 formal five-membrane Pu is NOT released.

Independent same-evaluator direct-R10 full-section diagnostic:

```text
r=0 audit peak = 51.480540 MN
five-membrane audit peak = 43.762840 MN
shift = -14.9915%
```

This supports a systematic downward shift caused by the current membrane-redistribution release relative to the previously constrained membrane model.

## Formal boundary

```text
43.762840 MN = AUDIT-ONLY DIAGNOSTIC LOCATOR
NOT FORMAL Z6 Pu
```

Formal Z6 still cannot be released through the broad-family compiler path because:

```text
wide-family N48 source fidelity = FAIL
N3584 source fidelity candidate = PASS
current N3584 structural coefficient backend = FAIL_COMMON_TRACTABILITY
```

## Current unique next gate

`FIVE_MEMBRANE_PARENT_DISPLACEMENT_BOUNDARY_WORK_AND_CONDENSATION_AUDIT`

Do not tune R10 or reopen a new symbolic backend before auditing whether all five membrane coordinates are physically admissible internal coordinates under the intended in-plane boundary/work conditions.

## Key artifacts

- `../40_execution/steel_shell/20260816_2350__NZSCCM__Z6_FIVE_MEMBRANE_DIRECT_R10_DIAGNOSTIC__EXECUTION_REPORT.md`
- `../40_execution/steel_shell/20260816_2350__NZSCCM__Z6_FIVE_MEMBRANE_DIRECT_R10_DIAGNOSTIC__PARAMS_AND_INTERMEDIATES.json`
- `../60_validation/steel_shell/20260816_2350__NZSCCM__Z6_FIVE_MEMBRANE_SYSTEMATIC_DOWNSHIFT__AUDIT.md`
- `../10_governance/20260816_2350__NZSCCM__MEMBRANE_REDISTRIBUTION_DOWNSHIFT_DIAGNOSTIC__GATE_LOCK.md`
