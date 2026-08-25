# CURRENT STATE — Steel-shell common terminal face operator

**Updated:** 2026-08-25 15:50 +08:00  
**Status:** `COMMON_R06_PROMOTED / Z6_NONREGRESSION_PASS / T360_BH032_BLIND_PASS / NO_EFFECTIVE_WIDTH`

Canonical parent:

`current/MILESTONE_RC_SSNC_FINAL_THEORY_20260825.md`

Canonical scope audit:

`semantic_v2/40_execution/steel_shell/20260825_1450__NZSCCM__STEEL_SHELL_COMMON_R02_R04_LOCAL_YIELD_AUDIT_Z6_T360_R01.md`

Canonical R06 theory:

`semantic_v2/20_theory/20260825_1530__NZSCCM__STEEL_SHELL_COMMON_R06_LOCAL_YIELD_RESULTANT_GATE_V1.md`

Canonical R06 code gate:

`semantic_v2/40_execution/steel_shell/20260825_1535__NZSCCM__STEEL_SHELL_COMMON_R06_LOCAL_YIELD_RESULTANT_GATE.py`

Canonical blind execution:

`semantic_v2/40_execution/steel_shell/20260825_1550__NZSCCM__STEEL_SHELL_COMMON_R06_Z6_NONREGRESSION_T360_BH032_BLIND_EXECUTION_R01.md`

---

## 0. Current operator identity

R02/R04/R06 belong to the **common steel-shell layer**, not to NC or UHPC individually.

Current production face gate for the present axial terminal scope (`gamma_xy=0`) is:

```text
R02 amplitude + finite local harmonic field
-> compute sigma_cr^E / fy event order

if sigma_cr^E >= fy:
    R04_YIELD_FIRST exactly

if sigma_cr^E < fy:
    R06_LOCAL_BUCKLING_FIRST
    -> finite-algebraic max local Mises
    -> first radial local-yield boundary
    -> full-area R02 mean resultant at that boundary
```

No effective width or effective area is used.

---

## 1. Frozen governance

```text
INITIAL_FULL_COMPOSITE_ABD = RETAIN
MARGUERRE_AIRY = RETAIN
R02_PBL_YUN = RETAIN
R04 = RETAIN AS EXACT YIELD-FIRST SUBBRANCH
R06 = COMMON PRODUCTION GATE FOR LOCAL-BUCKLING-FIRST CELLS
R03_AS_Pu_GATE = NO
CURRENT_MATERIAL_TANGENT_INTO_AIRY = NO
STEEL_FACE_OFFSET = INCLUDED ONCE ONLY
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
EFFECTIVE_WIDTH_AREA = 0
COMPARATOR_IN_ROOT_SELECTION = 0
```

The 2D local-Mises continuation is explicitly a project extension of Yun/R02's first-local-yield concept using the already-frozen R04 Mises material surface; it is not attributed verbatim to Yun.

---

## 2. Z6 strict non-regression

Z6 local cell:

```text
200 x 200 x 4 mm
sigma_cr = 794.3886717 MPa > fy = 355 MPa
```

Therefore R06 selects R04 identically.

Frozen Z6 R05/R06:

```text
U = 0.127098680688 mm
R04 lambda = 0.699621324802
face stress = (+200.320039918,-209.563907443,0) MPa
Pu = 49.45439833719624 MN
```

```text
Z6_STRICT_NONREGRESSION = PASS
```

---

## 3. T360 blind R06

```text
local cell = 360 x 375 x 4 mm
sigma_cr = 245.7948984 MPa < fy
branch = LOCAL_BUCKLING_FIRST
```

Blind root fixed before comparator:

```text
q = 0.00134518627955957
Pu = 10.8183777809815 MN
upper local max VM = 303.5620245 MPa -> uncapped
lower eta_y = 0.419889652186
lower boundary U = 1.541807734687 mm
lower boundary mean stress = (-57.13167383,-277.92910355,0) MPa
lower finite-algebraic max VM = 355.000000004 MPa
```

Four normal resultants close to the unchanged Airy demand to about `1e-10`.

Comparator opened only after root freeze:

```text
Abaqus R02 = 10.9688 MN
R06 error = -1.3714%
previous R01 error = +11.0655%
```

---

## 4. BH032 blind R06

Current corrected geometry uses 9 webs with net height 37 mm; this is independently reproduced by current `Pcr=30.6035224491 MN`.

```text
b = 1600 mm
a = 3200 mm
local cell = 360 x (3200/9) x 4 mm
sigma_cr = 245.2384460 MPa < fy
branch = LOCAL_BUCKLING_FIRST
```

Blind root fixed before comparator:

```text
q = 0.00137889961633743
Pu = 10.9405345132294 MN
upper local max VM = 317.2371632 MPa -> uncapped
lower eta_y = 0.425379325768
lower boundary U = 1.518650391337 mm
lower boundary mean stress = (-58.01556424,-278.08007693,0) MPa
lower finite-algebraic max VM = 355.000000002 MPa
```

Comparator opened only after root freeze:

```text
Abaqus R02 = 10.9905 MN
R06 error = -0.4546%
previous R01 error = +12.3959%
```

---

## 5. Current decision

```text
SSUHPC_ONLY_R06 = REJECTED / SUPERSEDED
STEEL_SHELL_COMMON_R06 = PROMOTED
Z6_R05 = NOT REVOKED
T360_R01_R04_VALUE = SUPERSEDED BY R06 FOR CURRENT AXIAL TERMINAL THEORY
BH032_R01_R04_VALUE = SUPERSEDED BY R06 FOR CURRENT AXIAL TERMINAL THEORY
```

Current common mechanism is state-driven:

```text
YIELD-FIRST steel cell -> R04
LOCAL-BUCKLING-FIRST steel cell -> R06
```

It is not driven by the core label `NC` versus `UHPC`.

Next work, if authorized, is validation of this already-frozen R06 over the remaining stocky cases and the more severe BH050 case. No refitting or new branch rule is authorized by that validation.
