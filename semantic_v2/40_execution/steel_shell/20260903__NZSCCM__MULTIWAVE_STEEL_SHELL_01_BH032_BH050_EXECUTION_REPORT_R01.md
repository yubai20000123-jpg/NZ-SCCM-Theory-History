# NZ-SCCM 多波钢壳01——BH032/BH050 不考虑剪切滑移计算报告 R01

**Date:** 2026-09-03  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Theory source:** `semantic_v2/20_theory/20260903__NZSCCM__MULTIWAVE_STEEL_SHELL_01_NO_SHEAR_SLIP_FULL_DERIVATION_R01.md`  
**Repro code:** `semantic_v2/40_execution/steel_shell/20260903__NZSCCM__MULTIWAVE_STEEL_SHELL_01_BH032_BH050_CALC_R01.py`  
**CSV:** `semantic_v2/40_execution/steel_shell/20260903__NZSCCM__MULTIWAVE_STEEL_SHELL_01_BH032_BH050_RESULTS_R01.csv`  
**Status:** `NUMERICAL THEORY EXECUTION / NO SHEAR SLIP / NO FE IN ROOT SOLVE / R06 NUMERICAL EXTREMUM CHECK / NOT PRODUCTION R14`

---

## 0. Execution boundary

本计算只执行“多波钢壳01—不考虑剪切滑移版本”。

禁止并未使用：

- steel-UHPC slip；
- PBL interface shear stiffness；
- qU global-local cross term；
- partial interaction；
- 99 independent local amplitudes；
- effective width/effective area；
- FE load or FE stress used in root solve；
- stored historical Pu used to select roots。

保留：

- 一个完整整体半波；
- 同一组 section kinematics `(eps_x0,kappa_x,eps_y0,kappa_y)`；
- four cell classes `E / n0-1 / n0 / n0+1`；
- R02 local amplitude；
- R06 first-local-yield mean stress return；
- current theory's scalar UHPC thickness primitives；
- exact ideal-EP web thickness integration；
- R14 outer `P(q), Nx^A, Mx^A, Ny^A, My^A`；
- four section equilibrium equations。

---

# 1. Raw inputs

当前冻结 BH 输入：

| parameter | BH032 | BH050 |
|---|---:|---:|
| `b` / mm | 1600 | 2500 |
| `a` / mm | 3200 | 5000 |
| `tc` / mm | 42 | 42 |
| `ts` / mm | 4 | 4 |
| `A0g` / mm | 4.0 | 6.25 |
| `q0=A0g/b` | 0.0025 | 0.0025 |
| `Aw` / mm² | 1332 | 1332 |
| `Es` / MPa | 206000 | 206000 |
| `nu_s` | 0.30 | 0.30 |
| `fy` / MPa | 355 | 355 |
| `Ec` / MPa | 43400 | 43400 |
| `nu_c` | 0.20 | 0.20 |
| `fc` / MPa | 141.1 | 141.1 |
| `eps_c0` | 0.0035 | 0.0035 |
| regular same-side PBL spacing `s=0.225b` / mm | 360 | 562.5 |
| local imperfection `A0l=s/1600` / mm | 0.225 | 0.3515625 |

UHPC tension anchors retained from the current R13/R14 parameter contract:

```text
(0,        0)
(0.000420, 9.767718 MPa)
(0.003800,10.734818 MPa)
(0.006900,10.347978 MPa)
(0.007590, 0)
```

No FE value is included in these raw inputs.

---

# 2. Global halfwave and local integer count

Both cases reproduce the frozen overall integer mode

\[
\boxed{m^*=2}.
\]

Therefore

## BH032

\[
L_G=3200/2=1600\ \mathrm{mm}.
\]

## BH050

\[
L_G=5000/2=2500\ \mathrm{mm}.
\]

For both cases

\[
\frac{L_G}{s}=\frac{1}{0.225}=4.444444\ldots
\]

thus the Multiwave-01 rule gives

\[
\boxed{n_0=4}
\]

and the only standard equal-width locally buckling candidates are

\[
\boxed{n=3,4,5}.
\]

No `8` or `9` is used in this execution.

---

# 3. Local elastic-buckling gates for n=3/4/5

## BH032 (`s=360 mm`)

| n | `Ly=LG/n` / mm | `Ly/s` | `sigma_cr^E` / MPa | gate |
|---:|---:|---:|---:|---|
| 3 | 533.3333 | 1.48148 | **304.98264** | LOCAL_FIRST |
| 4 | 400.0000 | 1.11111 | **249.27940** | LOCAL_FIRST |
| 5 | 320.0000 | 0.88889 | **250.30738** | LOCAL_FIRST |

All three are below `fy=355 MPa`.

## BH050 (`s=562.5 mm`)

| n | `Ly=LG/n` / mm | `Ly/s` | `sigma_cr^E` / MPa | gate |
|---:|---:|---:|---:|---|
| 3 | 833.3333 | 1.48148 | **124.92089** | LOCAL_FIRST |
| 4 | 625.0000 | 1.11111 | **102.10484** | LOCAL_FIRST |
| 5 | 500.0000 | 0.88889 | **102.52590** | LOCAL_FIRST |

Again all three are below `fy`.

Thus, for the regular equal-width bays, both BH032 and BH050 genuinely exercise the R02/R06 local-buckling branch in all three candidate classes.

---

# 4. Face-bay geometry used for aggregation

The current BH same-side PBL registration has regular bay width `0.225b` but leaves non-standard edge residual strips. The Multiwave-01 adjacency rule was explicitly stated to apply to **equal-width** bays. Therefore this execution uses the following strict specialization:

### TOP face

Three regular equal-width bays:

\[
3\times0.225b=0.675b.
\]

The two non-standard edge residual strips occupy together

\[
1-0.675=0.325b
\]

and are entered as full-thickness nonbuckled ideal-EP `E` steel.

### BOTTOM face

Four regular equal-width bays:

\[
4\times0.225b=0.900b.
\]

The two narrow edge residual strips occupy together

\[
0.100b
\]

and are entered as full-thickness nonbuckled ideal-EP `E` steel.

Thus

\[
\bar\sigma^{TOP}=0.325\sigma_E+0.225(c_3\sigma_3+c_4\sigma_4+c_5\sigma_5),
\]

with

\[
c_3+c_4+c_5=3,
\]

and

\[
\bar\sigma^{BOTTOM}=0.100\sigma_E+0.225(c_3\sigma_3+c_4\sigma_4+c_5\sigma_5),
\]

with

\[
c_3+c_4+c_5=4.
\]

This is geometry weighting only; no effective width is introduced.

---

# 5. Classification issue and deterministic execution set

The theory defines the allowed classes but deliberately does **not** prescribe which individual regular bay must be `n=3`, `4`, or `5`. Since all regular bays of one face have the same width and are subjected to the same generalized face strain, their order does not affect the present area-average N-M operator; only class counts matter.

No FE classification was used. Four purely theory-side count patterns were therefore executed:

| execution ID | TOP regular bays `(n3,n4,n5)` | BOTTOM regular bays `(n3,n4,n5)` | role |
|---|---|---|---|
| `ALL_n0` | `(0,3,0)` | `(0,4,0)` | strict direct base from `n0=4` |
| `BALANCED` | `(1,1,1)` | `(1,2,1)` | no-bias mixed-class sensitivity |
| `ALL_nminus` | `(3,0,0)` | `(4,0,0)` | lower-neighbor extreme |
| `ALL_nplus` | `(0,0,3)` | `(0,0,4)` | upper-neighbor extreme |

`ALL_n0` is the primary result because `n0` is the only class directly determined by the explicit floor rule. The other three quantify the finite classification sensitivity; they are not new selection rules.

---

# 6. Outer coefficients reproduced before solving

## BH032

\[
m^*=2,
\qquad
P_{cr}=30.6035224491\ \mathrm{MN},
\]

\[
K_x=4.26124168385\times10^6\ \mathrm{N/mm},
\]

\[
G=4.46025070618\times10^6\ \mathrm{N/mm},
\]

\[
C=6.97719391203\times10^9\ \mathrm N,
\]

\[
J_x=9.72684495986\times10^6\ \mathrm N,
\qquad
J_y=9.88235146460\times10^6\ \mathrm N.
\]

## BH050

\[
m^*=2,
\qquad
P_{cr}=19.5818772367\ \mathrm{MN},
\]

\[
K_x=4.27292596614\times10^6\ \mathrm{N/mm},
\]

\[
G=4.40017147908\times10^6\ \mathrm{N/mm},
\]

\[
C=1.08413718065\times10^{10}\ \mathrm N,
\]

\[
J_x=6.23461624472\times10^6\ \mathrm N,
\qquad
J_y=6.29831170906\times10^6\ \mathrm N.
\]

These match the current R14 outer-coefficient ledger. They are recomputed from raw inputs, not read as Pu roots.

---

# 7. Primary result: ALL_n0

## 7.1 BH032

The connected material-domain terminal candidate gives

\[
\boxed{q_u=0.001445638104624}
\]

and

\[
\boxed{P_u=11.2778056112\ \mathrm{MN}}.
\]

Section coordinates:

\[
\varepsilon_x^0=+1.37110444\times10^{-4},
\]

\[
\kappa_x=2.00826272\times10^{-5}\ /\mathrm{mm},
\]

\[
\varepsilon_y^0=-2.49196653\times10^{-3},
\]

\[
\kappa_y=4.80015938\times10^{-5}\ /\mathrm{mm}.
\]

The terminal UHPC longitudinal endpoints are

\[
\varepsilon_y^{U,+}=-0.00148393306,
\qquad
\boxed{\varepsilon_y^{U,-}=-0.0035}.
\]

### Constituent resultants

UHPC:

\[
N_x^U=+98.817965\ \mathrm{N/mm},
\qquad
M_x^U=3371.680396\ \mathrm N,
\]

\[
N_y^U=-4486.702410\ \mathrm{N/mm},
\qquad
M_y^U=11799.289409\ \mathrm N.
\]

Steel shell:

\[
N_x^s=-59.111459\ \mathrm{N/mm},
\qquad
M_x^s=10689.817316\ \mathrm N,
\]

\[
N_y^s=-2227.264673\ \mathrm{N/mm},
\qquad
M_y^s=2439.889042\ \mathrm N.
\]

Web:

\[
N_y^w=-293.100540\ \mathrm{N/mm},
\qquad
M_y^w=47.125389\ \mathrm N.
\]

Total section:

\[
\boxed{N_x=+39.706506\ \mathrm{N/mm}},
\]

\[
\boxed{M_x=14061.497712\ \mathrm N},
\]

\[
\boxed{N_y=-7007.067623\ \mathrm{N/mm}},
\]

\[
\boxed{M_y=14286.303840\ \mathrm N}.
\]

Corresponding outer demand:

\[
N_x^A=39.706506,
\quad
M_x^A=14061.497712,
\]

\[
N_y^A=-7007.067623,
\quad
M_y^A=14286.303841.
\]

Maximum raw resultant closure error is below approximately `4e-7` in the retained calculation.

### Face-average steel stresses

TOP:

\[
\boxed{(\bar\sigma_x^+,\bar\sigma_y^+)=(+50.7079,-265.1478)\ \mathrm{MPa}}
\]

BOTTOM:

\[
\boxed{(\bar\sigma_x^-,\bar\sigma_y^-)=(-65.4858,-291.6684)\ \mathrm{MPa}}.
\]

For the regular `n=4` cell specifically:

TOP:

\[
U_4^+=0.694448\ \mathrm{mm},
\qquad
\eta_4^+=1,
\]

so the top regular bay remains uncapped R02 at the final section state.

BOTTOM:

\[
U_4^-=1.556862\ \mathrm{mm},
\qquad
\boxed{\eta_4^-=0.415118},
\]

so the lower regular bay is returned by R06 at first local Mises yield.

---

## 7.2 BH050

Primary terminal candidate:

\[
\boxed{q_u=0.005215863114038}
\]

\[
\boxed{P_u=13.8148733974\ \mathrm{MN}}.
\]

Section coordinates:

\[
\varepsilon_x^0=+1.19818373\times10^{-5},
\]

\[
\kappa_x=4.48747092\times10^{-5}\ /\mathrm{mm},
\]

\[
\varepsilon_y^0=-2.13010497\times10^{-3},
\]

\[
\kappa_y=6.52330965\times10^{-5}\ /\mathrm{mm}.
\]

UHPC y endpoints:

\[
\varepsilon_y^{U,+}=-0.000760209945,
\qquad
\boxed{\varepsilon_y^{U,-}=-0.0035}.
\]

### Constituent resultants

UHPC:

\[
N_x^U=-243.339029\ \mathrm{N/mm},
\qquad
M_x^U=7903.777872\ \mathrm N,
\]

\[
N_y^U=-3861.562170\ \mathrm{N/mm},
\qquad
M_y^U=16924.267158\ \mathrm N.
\]

Steel shell:

\[
N_x^s=+471.019939\ \mathrm{N/mm},
\qquad
M_x^s=24615.127029\ \mathrm N,
\]

\[
N_y^s=-1259.360910\ \mathrm{N/mm},
\qquad
M_y^s=15628.140442\ \mathrm N.
\]

Web:

\[
N_y^w=-170.565150\ \mathrm{N/mm},
\qquad
M_y^w=298.724124\ \mathrm N.
\]

Total section:

\[
\boxed{N_x=+227.680910\ \mathrm{N/mm}},
\]

\[
\boxed{M_x=32518.904901\ \mathrm N},
\]

\[
\boxed{N_y=-5291.488230\ \mathrm{N/mm}},
\]

\[
\boxed{M_y=32851.131724\ \mathrm N}.
\]

The outer demand matches these four values to below approximately `3e-8` in the retained calculation.

### Face-average steel stresses

TOP:

\[
\boxed{(\bar\sigma_x^+,\bar\sigma_y^+)=(+192.6554,-72.4846)\ \mathrm{MPa}}
\]

BOTTOM:

\[
\boxed{(\bar\sigma_x^-,\bar\sigma_y^-)=(-74.9004,-242.3557)\ \mathrm{MPa}}.
\]

Regular `n=4` cell:

TOP:

\[
U_4^+=0.135934\ \mathrm{mm},
\qquad
\eta_4^+=1,
\]

BOTTOM:

\[
U_4^-=3.002933\ \mathrm{mm},
\qquad
\boxed{\eta_4^-=0.368460}.
\]

Again the lower regular cell is R06-limited while the upper regular cell remains uncapped R02 at the terminal state.

---

# 8. Mixed-class sensitivity

Because the theory does not prescribe the class-count tuple, the finite sensitivity is retained rather than hidden.

## BH032

| classification | q | P / MN |
|---|---:|---:|
| `ALL_n0` | 0.001445638105 | **11.27780561** |
| `BALANCED` | 0.001455923871 | **11.32879036** |
| `ALL_nminus` | 0.001479411091 | **11.44424087** |
| `ALL_nplus` | 0.001452820697 | **11.31343595** |

Range:

\[
\boxed{11.2778\le P_u\le11.4442\ \mathrm{MN}}
\]

with total spread about

\[
\boxed{1.48\%}
\]

relative to the lower end.

## BH050

| classification | q | P / MN |
|---|---:|---:|
| `ALL_n0` | 0.005215863114 | **13.81487340** |
| `BALANCED` | 0.005260095555 | **13.85845934** |
| `ALL_nminus` | 0.005400382591 | **13.99429771** |
| `ALL_nplus` | 0.005201640188 | **13.80077910** |

Range:

\[
\boxed{13.8008\le P_u\le13.9943\ \mathrm{MN}}
\]

with total spread about

\[
\boxed{1.40\%}.
\]

Thus, within the present no-slip Multiwave-01 model, replacing `n0=4` by the neighboring `3/5` classes changes the final load only at the order of about 1–1.5% across the deliberately extreme count patterns.

---

# 9. BALANCED detailed local state

The mixed case is retained as a sensitivity check only.

## BH032 BALANCED

TOP class means:

| class | sigma_x / MPa | sigma_y / MPa | U / mm | eta | local max VM / MPa |
|---|---:|---:|---:|---:|---:|
| E | +42.0281 | -275.3821 | — | — | ideal-EP trial VM 298.62 |
| n=3 | +46.9211 | -272.1294 | 0.46593 | 1.00000 | 305.29 |
| n=4 | +56.0604 | -262.8513 | 0.69799 | 1.00000 | 315.42 |
| n=5 | +60.7968 | -254.0839 | 0.75940 | 1.00000 | 317.28 |

BOTTOM:

| class | sigma_x / MPa | sigma_y / MPa | U / mm | eta | local max VM / MPa |
|---|---:|---:|---:|---:|---:|
| E | -153.2379 | -405.8812 | — | — | mean ideal-EP capped |
| n=3 | -58.9388 | -293.9917 | 1.55404 | 0.407274 | 355.00 |
| n=4 | -55.0109 | -279.0815 | 1.55372 | 0.415328 | 355.00 |
| n=5 | -63.3116 | -280.5581 | 1.46294 | 0.437161 | 355.00 |

The area-averaged faces are

\[
(\bar\sigma_x^+,\bar\sigma_y^+)=(+50.5093,-267.0387)\ \mathrm{MPa},
\]

\[
(\bar\sigma_x^-,\bar\sigma_y^-)=(-67.5850,-295.4485)\ \mathrm{MPa}.
\]

and

\[
\boxed{P_u=11.32879036\ \mathrm{MN}}.
\]

## BH050 BALANCED

TOP:

| class | sigma_x / MPa | sigma_y / MPa | U / mm | eta | local max VM / MPa |
|---|---:|---:|---:|---:|---:|
| E | +194.7947 | -71.6864 | — | — | ideal-EP trial VM 238.85 |
| n=3 | +193.4102 | -72.6068 | 0.09274 | 1.00000 | 239.59 |
| n=4 | +193.4081 | -72.9247 | 0.13520 | 1.00000 | 240.25 |
| n=5 | +193.5716 | -73.0744 | 0.19975 | 1.00000 | 240.73 |

BOTTOM:

| class | sigma_x / MPa | sigma_y / MPa | U / mm | eta | local max VM / MPa |
|---|---:|---:|---:|---:|---:|
| E | -218.8256 | -409.5986 | — | — | mean ideal-EP capped |
| n=3 | -57.4532 | -238.9916 | 3.02803 | 0.349637 | 355.00 |
| n=4 | -58.4706 | -223.8575 | 3.00033 | 0.368562 | 355.00 |
| n=5 | -72.0441 | -222.4841 | 2.87398 | 0.401310 | 355.00 |

Area-averaged faces:

\[
(\bar\sigma_x^+,\bar\sigma_y^+)=(+193.8960,-72.4844)\ \mathrm{MPa},
\]

\[
(\bar\sigma_x^-,\bar\sigma_y^-)=(-77.3313,-245.5278)\ \mathrm{MPa},
\]

and

\[
\boxed{P_u=13.85845934\ \mathrm{MN}}.
\]

---

# 10. Connected-branch check for the primary ALL_n0 case

A separate four-equilibrium continuation was run from low q to the material-domain endpoint, without using the stored R14 terminal coordinates as root selection.

## BH032

At fractions `0.05, 0.25, 0.50, 0.75, 0.90, 1.00` of the final q, all four section equations converged on the same connected branch. The lower UHPC y strain evolved approximately

```text
-0.0001573
-0.0007268
-0.0013575
-0.0023298
-0.0029849
-0.0035000
```

and the numerical current-section Jacobian did not show a vanishing smallest singular value before the material boundary.

## BH050

The same q fractions give lower UHPC y strain approximately

```text
-0.0002355
-0.0009692
-0.0017549
-0.0026630
-0.0031462
-0.0035000
```

with the same outcome: no numerical fold indication before the compression-domain endpoint in this primary execution.

This is a numerical connected-branch diagnostic, not a replacement for a theorem-level exact J4 certificate.

---

# 11. Post-solve comparison only; comparator was not used in roots

For orientation only, after the theory roots were fixed:

Current R14 audit values are approximately

```text
BH032  11.11364157 MN
BH050  13.52478195 MN
```

and current canonical FE peaks are approximately

```text
BH032  10.990480 MN
BH050  12.591227 MN
```

The new primary ALL_n0 no-slip values therefore differ from the current R14 values by

```text
BH032  +1.48%
BH050  +2.14%
```

and from the canonical FE peaks by

```text
BH032  +2.61%
BH050  +9.72%
```

The `BALANCED` mixed-class values differ from FE by approximately

```text
BH032  +3.08%
BH050 +10.06%
```

These comparators were not used anywhere in the classification, q solve, R02/R06 response, UHPC calculation or root selection.

---

# 12. Result interpretation limited to this theory version

1. The Multiwave-01 equations are numerically solvable for both BH032 and BH050. Therefore the fallback to the single-cell R14/R13 version is **not triggered by solvability**.
2. Both specimens give `m*=2`, one representative overall halfwave `LG=b`, `n0=4`, and local candidates `n=3,4,5`.
3. For regular bays, all three n values are local-buckling-first in BH032 and BH050.
4. The finite `n=3/4/5` classification changes Pu modestly: about 1.48% total spread in BH032 and 1.40% in BH050 across the extreme count patterns executed.
5. Under the strict no-slip assumption, the primary result is

\[
\boxed{P_{u,BH032}^{MW01,NS}=11.27780561\ \mathrm{MN}}
\]

and

\[
\boxed{P_{u,BH050}^{MW01,NS}=13.81487340\ \mathrm{MN}}.
\]

6. These are **Multiwave-01 no-slip theory results**, not replacement production R14 values.
7. This execution does not open or interpret any steel-UHPC shear-slip redistribution mechanism.

---

# 13. Formal status

```text
THEORY_FILE_SAVED = YES
BH032_NUMERICAL_CLOSURE = PASS
BH050_NUMERICAL_CLOSURE = PASS
ONE_COMPLETE_GLOBAL_HALFWAVE = YES
N0 = 4 FOR BOTH CASES
LOCAL_CANDIDATES = {3,4,5}
NO_SLIP = YES
PARTIAL_INTERACTION = NO
qU = NO
99_INDEPENDENT_U = NO
EFFECTIVE_WIDTH = NO
FE_IN_ROOT_SOLVE = NO
PRIMARY_CLASSIFICATION = ALL_n0
CLASSIFICATION_SENSITIVITY = RETAINED
FORMAL_FULL_R06_RESULTANT_CERTIFICATE_FOR_EVERY_NEW_CLASS = NOT_EMITTED
PRODUCTION_R14_MODIFIED = NO
```
