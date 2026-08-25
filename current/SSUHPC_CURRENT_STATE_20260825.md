# CURRENT STATE — Steel-Shell UHPC

**Updated:** 2026-08-25 15:50 +08:00  
**Status:** `RC_SSNC_MILESTONE_ANCHORED / CORE_NM_SUBSTITUTION_ONLY / COMMON_R06_INHERITED / T360_BH032_R06_SUPERSEDE_R01`

Canonical parent:

`current/MILESTONE_RC_SSNC_FINAL_THEORY_20260825.md`

Canonical SSUHPC core substitution:

`semantic_v2/20_theory/20260825_1330__NZSCCM__SSUHPC_FROM_RC_SSNC_MILESTONE_CORE_NM_SUBSTITUTION_V1.md`

Canonical common steel-shell state:

`current/STEEL_SHELL_COMMON_R02_R04_STATE_20260825.md`

Canonical common R06 theory:

`semantic_v2/20_theory/20260825_1530__NZSCCM__STEEL_SHELL_COMMON_R06_LOCAL_YIELD_RESULTANT_GATE_V1.md`

Canonical R06 blind execution:

`semantic_v2/40_execution/steel_shell/20260825_1550__NZSCCM__STEEL_SHELL_COMMON_R06_Z6_NONREGRESSION_T360_BH032_BLIND_EXECUTION_R01.md`

---

## 0. Theory identity remains unchanged

\[
\boxed{
SSUHPC
=
SSNC_{20260825}
-\mathcal C_c^{NC}
+\mathcal C_c^{UHPC}.
}
\]

The common steel-shell operator is inherited from SSNC. R06 is therefore **not** an UHPC-specific repair.

```text
AIRY = unchanged
UHPC N-M = unchanged
WEB = unchanged
R02 = unchanged
R04 = retained as yield-first branch
R06 = common local-buckling-first face gate
R03 Pu gate = NO
formal spatial quadrature = 0
material points = 0
effective width/area = 0
```

---

## 1. UHPC core remains frozen

```text
fc    = 141.1 MPa
Ec    = 43.4 GPa
epsc0 = 0.0035
nu_c  = 0.20
fct   = 4.513133983249735 MPa
epst0 = 0.001
mt    = 0.4418
```

The exact x/y UHPC N-M primitives and first compressed-face contact at `-epsc0` remain unchanged. No UHPC parameter was altered during R06.

---

## 2. Common R06 branch rule inherited by SSUHPC

```text
if sigma_cr^E >= fy:
    exact R04 yield-first branch

if sigma_cr^E < fy:
    R02 local-buckling-first
    -> finite-algebraic local Mises maximum
    -> first radial local-yield boundary
    -> full-area R02 mean face resultant at that boundary
```

The activation variable is the **local steel-shell state**, not the core material label.

---

## 3. R06 results now authoritative where executed

### T360

Previous R01/R04 result:

```text
Pu = 12.18255684307 MN
Abaqus post-check error = +11.0655%
```

Common R06 blind root, fixed before reopening Abaqus:

```text
q = 0.00134518627955957
Pu = 10.8183777809815 MN
upper face = R02 local-elastic, max local VM = 303.5620 MPa
lower face = R06 local-yield, eta_y = 0.419889652186
lower boundary U = 1.541807734687 mm
lower boundary mean stress = (-57.1317,-277.9291,0) MPa
finite-algebraic max local VM = 355.000000004 MPa
```

Only after the root was frozen:

```text
Abaqus R02 = 10.9688 MN
R06 error = -1.3714%
```

Therefore:

```text
T360_R01_R04_Pu = SUPERSEDED
T360_CURRENT_Pu = 10.8183777809815 MN
```

### BH032

Previous R01/R04 result:

```text
Pu = 12.35286994754 MN
Abaqus post-check error = +12.3959%
```

Common R06 blind root:

```text
q = 0.00137889961633743
Pu = 10.9405345132294 MN
upper face = R02 local-elastic, max local VM = 317.2372 MPa
lower face = R06 local-yield, eta_y = 0.425379325768
lower boundary U = 1.518650391337 mm
lower boundary mean stress = (-58.0156,-278.0801,0) MPa
finite-algebraic max local VM = 355.000000002 MPa
```

Only after root fixation:

```text
Abaqus R02 = 10.9905 MN
R06 error = -0.4546%
```

Therefore:

```text
BH032_R01_R04_Pu = SUPERSEDED
BH032_CURRENT_Pu = 10.9405345132294 MN
```

---

## 4. Z6 parent non-regression protects the common architecture

The common Z6 control has

```text
sigma_cr = 794.3886717 MPa > fy = 355 MPa
```

so R06 degenerates exactly to R04 and retains

```text
Z6 Pu = 49.45439833719624 MN
```

This is the mandatory proof that R06 does not blindly penalize all steel-shell members.

---

## 5. Remaining SSUHPC cases

The earlier R01 values remain frozen **only for cases not yet rerun under R06**:

| Case | R01 Pu / MN | local sigma_cr / MPa | current status |
|---|---:|---:|---|
| T120 | 12.76914369 | 2206.635 | R06 not rerun; yield-first expected to degenerate to R04 |
| BH005 | 2.46233215 | 10044.967 | R06 not rerun; yield-first expected to degenerate to R04 |
| BH010 | 4.58337285 | 2511.242 | R06 not rerun; yield-first expected to degenerate to R04 |
| BH020 | 8.55797773 | 627.810 | R06 not rerun; yield-first expected to degenerate to R04 |
| BH050 | 15.69757377 | 100.450 | R06 not rerun; severe local-buckling-first validation still pending |

No numerical value in this table is allowed to be silently changed until its R06 rerun is actually performed.

---

## 6. Current decision boundary

```text
COMMON_R06 = PROMOTED FOR CURRENT AXIAL TERMINAL SCOPE
SSUHPC_ONLY_R06 = PROHIBITED
UHPC_RETUNING = PROHIBITED
EFFECTIVE_WIDTH_AREA = PROHIBITED
COMPARATOR_BASED_BRANCH_OR_ROOT_SELECTION = PROHIBITED
```

The next useful execution is a validation batch of T120/BH005/BH010/BH020 strict non-regression plus BH050 local-buckling-first prediction. That batch may validate R06 but may not refit it.
