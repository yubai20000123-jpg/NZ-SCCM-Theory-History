# CURRENT STATE — Steel-Shell UHPC

**Updated:** 2026-08-25 16:22 +08:00  
**Status:** `RC_SSNC_MILESTONE_ANCHORED / CORE_NM_SUBSTITUTION_ONLY / COMMON_R06_INHERITED / SEVEN_CASE_R06_COMPLETE`

Canonical parent:

`current/MILESTONE_RC_SSNC_FINAL_THEORY_20260825.md`

Canonical SSUHPC core substitution:

`semantic_v2/20_theory/20260825_1330__NZSCCM__SSUHPC_FROM_RC_SSNC_MILESTONE_CORE_NM_SUBSTITUTION_V1.md`

Canonical common R06 theory:

`semantic_v2/20_theory/20260825_1530__NZSCCM__STEEL_SHELL_COMMON_R06_LOCAL_YIELD_RESULTANT_GATE_V1.md`

Prior R06 control execution:

`semantic_v2/40_execution/steel_shell/20260825_1550__NZSCCM__STEEL_SHELL_COMMON_R06_Z6_NONREGRESSION_T360_BH032_BLIND_EXECUTION_R01.md`

Current complete SSUHPC seven-case execution:

`semantic_v2/40_execution/steel_shell/20260825_1622__NZSCCM__STEEL_SHELL_COMMON_R06_SSUHPC_7CASE_BH050_FULL_EXECUTION_R01.md`

---

## 0. Theory identity

\[
\boxed{SSUHPC=SSNC_{20260825}-\mathcal C_c^{NC}+\mathcal C_c^{UHPC}.}
\]

```text
AIRY = unchanged
UHPC N-M = unchanged
WEB = unchanged
R02 = unchanged
R04 = retained as exact yield-first degeneration
R06 = common local-buckling-first steel-face gate
R03 Pu gate = NO
formal spatial sampling = 0
formal spatial quadrature = 0
material points = 0
effective width/area = 0
comparator in root solve = 0
```

UHPC unit remains frozen:

```text
fc=141.1 MPa; Ec=43.4 GPa; epsc0=0.0035; nu_c=0.20
fct=4.513133983249735 MPa; epst0=0.001; mt=0.4418
```

---

## 1. Common R06 branch rule

```text
sigma_cr^E >= fy:
    R06 == R04 exactly

sigma_cr^E < fy:
    retain R02 local postbuckling field
    -> finite-algebraic local Mises maximum
    -> first radial local-yield boundary
    -> whole-width R02 mean face resultant at that boundary
```

The activation variable is the local steel-shell state, not NC/UHPC label.

---

## 2. Current authoritative seven-case results

| Case | sigma_cr,s / MPa | R06 branch | current Pu / MN | Abaqus / MN | error |
|---|---:|---|---:|---:|---:|
| T120 | 2206.635 | yield-first = R04 | **12.76914369** | 12.6378 | **+1.0393%** |
| T360 | 245.795 | local-buckling-first | **10.81837778** | 10.9688 | **-1.3714%** |
| BH005 | 10044.967 | yield-first = R04 | **2.46233215** | 2.3558 | **+4.5221%** |
| BH010 | 2511.242 | yield-first = R04 | **4.58337285** | 4.3043 | **+6.4836%** |
| BH020 | 627.810 | yield-first = R04 | **8.55797773** | 8.0076 | **+6.8732%** |
| BH032 | 245.238 | local-buckling-first | **10.94053451** | 10.9905 | **-0.4546%** |
| BH050 | 100.450 | local-buckling-first | **13.35637635** | 12.2198 | **+9.3011%** |

All seven:

```text
mean signed error = +3.7705%
MAE               = 4.2922%
RMSE              = 5.3373%
```

Historical primary six excluding the lower-confidence BH050 comparator:

```text
mean signed error = +2.8487%
MAE               = 3.4574%
RMSE              = 4.3377%
```

---

## 3. BH050 current root

BH050 is now actually rerun, not carried over from R01.

```text
b = 2500 mm
a = 5000 mm
local cell = 562.5 x 555.5555556 x 4 mm
A0 = 0.3515625 mm
sigma_cr = 100.4496675 MPa < 355 MPa
branch = R06_LOCAL_BUCKLING_FIRST
q = 0.004772819645833164
Pu = 13.3563763545430 MN
```

Current section state:

```text
eps_x0 = +2.820431413e-5
kappa_x = 4.402758337803803e-5 1/mm
eps_y0 = -0.00213545799
kappa_y = 6.497819104663830e-5 1/mm
active UHPC contact: eps_y(-21 mm) = -0.0035
```

Upper steel face:

```text
strain = (+0.001040838732,-0.000640959594)
U = 0.169266885792 mm
max finite-algebraic local VM = 239.8727015 MPa < 355
whole-width mean stress = (+190.7746,-75.7434) MPa
```

Lower steel face:

```text
full strain = (-0.000984430104,-0.003629956382)
full unprojected R02 local max VM = 960.3177033 MPa
eta_y = 0.384465068379632
R02 amplitude at local yield = 2.939845914478 mm
whole-width mean stress at local yield = (-62.4713,-222.0556) MPa
finite-algebraic global max local VM = 355.000000000001 MPa
active candidate = v=-1, u=0.757308975358
```

Four resultant balances close to about `1e-11` or better.

Only after this root was frozen was the existing comparator reopened:

```text
Abaqus = 12.2198 MN
error = +9.3011%
previous R04 error = +28.4602%
```

---

## 4. Common-parent non-regression

Z6 remains protected by the common rule:

```text
sigma_cr = 794.3886717 MPa > fy
R06 == R04
Pu = 49.45439833719624 MN
```

Thus R06 does not impose a generic strength reduction on stocky/yield-first shells.

---

## 5. Current decision boundary

```text
COMMON_R06_CURRENT_AXIAL_TERMINAL_SCOPE = PROMOTED
SSUHPC_SEVEN_CASE_R06_BATCH = COMPLETE
SSUHPC_ONLY_R06 = PROHIBITED
UHPC_RETUNING = PROHIBITED
EFFECTIVE_WIDTH_AREA = PROHIBITED
COMPARATOR_BASED_BRANCH_OR_ROOT_SELECTION = PROHIBITED
```

BH050 remains the largest positive discrepancy and retains its prior lower-confidence/different-model-family comparator status. No post-comparator repair has been introduced.