# RC–SSNC Unified Terminal-Capacity Milestone — Common Steel-Shell R06 Addendum

**Date:** 2026-08-25 15:50 +08:00  
**Base milestone:** `current/MILESTONE_RC_SSNC_FINAL_THEORY_20260825.md`  
**Status:** `ACTIVE SUPERSEDING ADDENDUM FOR STEEL-FACE TERMINAL GATE ONLY`

This addendum does not replace the base milestone architecture. It changes exactly one common steel-shell submodule after the user-authorized Z6/T360/BH032 gate.

## 1. Unchanged milestone content

```text
initial full-composite ABD
Marguerre–Airy structural demand
common terminal strain/resultant architecture
NC-M6 or UHPC core N-M according to family
longitudinal web
steel-face offset included once
R03 not Pu gate
current material tangent not fed into Airy
formal spatial quadrature = 0
material points = 0
effective width/area = prohibited
comparator in root selection = 0
```

## 2. Superseded steel-face line

Base-milestone line:

```text
R02 -> R04 mean-stress Mises cap
```

is superseded for the current axial terminal scope by:

```text
R02
-> event-order selector sigma_cr^E vs fy
-> if yield-first: R04 exactly
-> if local-buckling-first: Common R06 finite-local-yield resultant gate
```

R04 is not deleted. It remains the exact yield-first degeneration inside R06.

## 3. Gate evidence

```text
Z6:
  sigma_cr = 794.3887 MPa > fy
  R06 -> R04 exactly
  Pu = 49.45439833719624 MN unchanged

T360 blind R06:
  Pu = 10.8183777809815 MN
  Abaqus opened afterward = 10.9688 MN
  post-check = -1.3714%

BH032 blind R06:
  Pu = 10.9405345132294 MN
  Abaqus opened afterward = 10.9905 MN
  post-check = -0.4546%
```

No comparator entered the R06 operator or root selection.

## 4. Canonical files

- Theory: `semantic_v2/20_theory/20260825_1530__NZSCCM__STEEL_SHELL_COMMON_R06_LOCAL_YIELD_RESULTANT_GATE_V1.md`
- Code gate: `semantic_v2/40_execution/steel_shell/20260825_1535__NZSCCM__STEEL_SHELL_COMMON_R06_LOCAL_YIELD_RESULTANT_GATE.py`
- Blind execution: `semantic_v2/40_execution/steel_shell/20260825_1550__NZSCCM__STEEL_SHELL_COMMON_R06_Z6_NONREGRESSION_T360_BH032_BLIND_EXECUTION_R01.md`
- Current common state: `current/STEEL_SHELL_COMMON_R02_R04_STATE_20260825.md`

## 5. Recovery rule

Any future chat restoring the 2026-08-25 RC–SSNC milestone must read this addendum before using the steel-face terminal operator.

```text
BASE_MILESTONE = RETAIN
STEEL_FACE_R02_R04_ONLY = SUPERSEDED
CURRENT_COMMON_STEEL_FACE_GATE = R06
```
