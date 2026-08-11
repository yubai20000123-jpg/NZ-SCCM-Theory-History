# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-11 16:05 +08:00  
**Purpose:** 唯一当前工作入口。

## 0. Highest-priority contract

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
ACTIVE_MODE = m=1
KINEMATICS = NGUYEN_SECOND_ORDER
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

Final production capacity must come from explicit finite formulas / analytic coefficient algebra and explicit derivatives of the same representation. Numerical root solving of already explicit finite equations is allowed.

Formal production prohibits spatial Gauss/Simpson/adaptive quadrature, material-point grids, moving spatial TT/TC/CC cells, whole-structure P/R/U fits from spatial numerical integration, structural-load calibration of material parameters, and finite-difference production derivatives.

---

## 1. Active material architecture

The active architecture remains

```text
multidimensional/current NC operator
-> lambda+, lambda-
-> 1D scalar master law
-> executed R10 material-energy regularization
-> SAME U/C/T + CC/TC/TT interaction
-> same spectral return
```

No global material-energy-potential fit is active.

The executed R10 scalar used by the current R10B record is

```text
W_source = W_smooth = 0.031741235181249904
h = 0.09799750427197301
```

No Case21/Swartz capacity was used to choose `h`.

### 1A. Governing identity — R10 vs R10B

```text
SOURCE FOSTER -> R10
= material-target modification

R10 -> R10B
= finite analytic compilation / reintegration only
```

R10 acts on the internal tensile scalar coordinate

\[
t=\Pi_\eta(\lambda).
\]

R10B changes no material parameter or multidimensional interaction coefficient. It may have finite-order material-representation and spatial-coefficient truncation error. Exactness means exact coefficient algebra and exact complete-halfwave moment contraction after the retained finite representation is fixed.

### 1B. R10 material-target audit — COMPLETE

Canonical files:

- `current/theory/NZ_SCCM_R10_MATERIAL_TARGET_INTENT_AUDIT_20260811.md`
- `governance/R10_MATERIAL_TARGET_INTENT_AUDIT_DECISION_20260811.md`

The audit establishes that the executed R10 replaces the retained tensile interval

\[
0\le t\le10x_{cr}
\]

with two C2 quintic branches while preserving selected physical/C2 anchors and total source work.

Material-coordinate audit:

```text
max |u_R10-u_source|                         ~= 0.01831
absolute redistributed work / source work   ~= 9.89 %
positive relocated work / source work        ~= 4.95 %
first-moment shift of tensile work           ~= -5.90 %
```

Status:

```text
R10_EXECUTED_FORMULA_RECOVERY                 = PASS
R10_SOURCE_WORK_EQUALITY                       = PASS
R10_C2_TARGET_INTERNAL_CONSISTENCY             = PASS
R10_SAME_MULTIAXIAL_REINSERTION_ARCHITECTURE   = PASS
R10_AS_TINY_LOCAL_SOURCE_PATCH                 = FAIL_DESCRIPTION
R10_AS_WHOLE_RETAINED_TENSILE_BRANCH_REBUILD   = PASS_DESCRIPTION
R10_MATERIAL_TARGET_AUDIT                      = PASS_COMPLETE
NEW_R10_TARGET_SELECTED_DURING_RECOVERY        = NO
STRUCTURAL_Pu_CALIBRATION                      = NO
```

No new R10A material route is active.

### 1C. R10B representation-fidelity audit — COMPLETE

Canonical file:

- `current/theory/NZ_SCCM_R10B_REPRESENTATION_FIDELITY_AUDIT_20260811.md`

Archived historical N48 material-coordinate errors:

| scalar | max abs error | p95 abs error |
|---|---:|---:|
| U | 0.000200 | 0.000138 |
| C | 0.002895 | 0.000712 |
| T | 0.027887 | 0.006928 |
| T^7 | 0.027497 | 0.017399 |

Historical structural order evidence changes material and spatial orders together, so it cannot isolate the two truncation sources. The N96 fixed-D equilibrium reclosure differs from the N48 stationary result by

```text
0.18849035625 kN = 0.0511757671 %
```

and is engineering sensitivity evidence, not a full N96 stationary-root certificate.

Decision:

```text
R10B_REPRESENTATION_FIDELITY_AUDIT
= PASS_ENGINEERING_WITH_REPRODUCIBILITY_GAP

HISTORICAL_COEFFICIENT_GENERATOR = UNRECOVERED
HISTORICAL_COEFFICIENT_ARRAYS    = UNRECOVERED
```

The missing historical generator must not be invented retroactively.

### 1D. Coefficient-generation rule — RE-FROZEN

Canonical files:

- `current/theory/NZ_SCCM_R10B_COEFFICIENT_GENERATION_CONTRACT_V1_20260811.md`
- `current/theory/r10b_coefficient_generator_v1.py`
- `current/theory/NZ_SCCM_R10B_N112_MATERIAL_COEFFICIENTS_20260811.csv`
- `evidence/NZ_SCCM_R10B_CHEB_ROOT_DCT_ORDER_AUDIT_20260811.csv`
- `governance/R10B_FIDELITY_AND_COEFFICIENT_REFREEZE_DECISION_20260811.md`

The new transparent reproducibility convention is explicitly **not** claimed to be the byte-exact historical R10B generator.

Compiler hull:

\[
\lambda_a=-1.01,\qquad \lambda_b=0.105,
\]

\[
\lambda_c=-0.4525,\qquad \lambda_h=0.5575,
\]

\[
\xi(\lambda)=\frac{\lambda-\lambda_c}{\lambda_h}
=\frac{400\lambda+181}{223}.
\]

For order \(N\):

\[
\theta_j=\frac{(j+\tfrac12)\pi}{N+1},
\qquad
\lambda_j=\lambda_c+\lambda_h\cos\theta_j,
\]

\[
F_N(\lambda)=\sum_{n=0}^{N}a_n^{(F)}T_n[\xi(\lambda)],
\]

\[
\boxed{
a_n^{(F)}
=
\frac{2-\delta_{n0}}{N+1}
\sum_{j=0}^{N}F(\lambda_j)\cos(n\theta_j)
},
\qquad
F\in\{U,C,T,T^7\}.
\]

This is direct formula-to-formula compilation; no least-squares weights, SVD/rcond, regularization coefficient, or structural-test data are involved.

Using the archived N48 material error table only as a material-fidelity floor, the first tested order in `48,56,...` that passes all four historical max and p95 ceilings is

\[
\boxed{N_M^{repro}=112}.
\]

At N=112:

| scalar | max abs error | p95 abs error |
|---|---:|---:|
| U | 7.3352195900e-05 | 4.1632950383e-05 |
| C | 2.0457015200e-03 | 6.0108850303e-04 |
| T | 1.6385185836e-02 | 3.7906918519e-03 |
| T^7 | 2.8889305301e-03 | 5.2677094828e-04 |

Machine coefficients are stored with 17 significant digits.

Therefore:

```text
COEFFICIENT_GENERATION_CONVENTION = CHEBYSHEV_ROOT_DCT_V1
MATERIAL_REPRODUCTION_ORDER       = 112
HISTORICAL_N48_ORDER              = RETAINED_REFERENCE_ONLY
FORMAL_N112_COEFFICIENT_TABLE     = SAVED
```

---

## 2. Latest executed structural stage: historical R10B Case21

Canonical historical execution files:

- `current/theory/NZ_SCCM_R10B_ZERO_SPATIAL_D15_CASE21_20260811.md`
- `current/theory/NZ_SCCM_R10B_ZERO_SPATIAL_D15_CASE21_results.json`
- `governance/R10B_ZERO_SPATIAL_CASE21_DECISION_20260811.md`
- `evidence/NZ_SCCM_R10B_ARTIFACT_HASHES_20260811.md`

Historical decision:

```text
R10B_ZERO_SPATIAL_CASE21 = PASS_ENGINEERING
```

This remains the valid result record for the original R10B compiler execution, but the exact old coefficient generator is not independently reproducible from retained artifacts.

---

## 3. Case21-local analytic spectral contract

Historical R10B certified

\[
\lambda_+\in[-0.0956591207,0.1029457518],
\]

\[
\lambda_-\in[-1.0029457518,-0.6843408793].
\]

Safe-margin compiler intervals:

```text
lambda+ : [-0.10, 0.105]
lambda- : [-1.01,-0.68]
```

inside the single scalar hull `[-1.01,0.105]`.

This is a spectral-domain reduction and does not create a spatial material-state partition.

---

## 4. Zero-spatial coefficient algebra retained

The equivalent tensor is mapped to

\[
Y=aI+bE_u,
\]

with

\[
K_1=\operatorname{tr}Y,\qquad K_2=\det Y.
\]

For

\[
F(Y)=A(K_1,K_2)I+B(K_1,K_2)Y,
\]

pair multiplication is

\[
(A,B)(C,D)=(AC-BDK_2,\ AD+BC+BDK_1).
\]

The same multidimensional interaction is reconstructed algebraically:

\[
CC=\det(C)C,
\]

\[
TC=C[\operatorname{tr}(T)I-T],
\]

\[
TT=\det(T)[\operatorname{tr}(T^7)I-T^7],
\]

\[
S=U-a_{cc}CC+TC-\rho a_tTT.
\]

All formal structural fields remain finite coefficient objects. Exact complete-halfwave moments remain

\[
\int_0^\pi T_n(\sin X)dX
=
\pi\ (n=0),
\quad
2\sin(n\pi/2)/n\ (n\ge1),
\]

\[
\int_{-1}^{1}T_k(\zeta)d\zeta
=
0\ (k\ {\rm odd}),
\quad
2/(1-k^2)\ (k\ {\rm even}).
\]

Therefore:

```text
N_formal_spatial_sampling   = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

---

## 5. Same-expression derivative architecture retained

Forward chain-rule jets through the same retained coefficient algebra remain required.

No finite-difference production derivative is allowed.

Historical N48 derivative values:

```text
P_D = 106.58759351383472
P_q = -75105.39767023241
R_D = -1376.335532846137
R_q = 969815.5988960797
L   = 83.31643116474152
L_normalized = 4.029999719717427e-07
```

These remain evidence for the historical R10B representation and must be regenerated under the N112 reproducibility baseline.

---

## 6. Historical R10B Case21 result

```text
material degree = 48
spatial Chebyshev degree = 28
D_u  = 0.8449505
q_u  = 0.001779254542005754
A_u  = 2.1706905412470197 mm
Pc   = 337.39660909142 kN
Ps   = 30.922943404456966 kN
Pu   = 368.31955249587696 kN
R    = -2.2383016926141863e-05 kN mm
```

Experiment was introduced only after material freeze:

```text
Pf = 368.312750 kN
error = +0.006802495877 kN = +0.001846934671 %
```

The agreement must not be used to alter R10 material physics or compiler coefficients.

---

## 7. Historical N96 engineering sensitivity

At the N48 stationary D:

```text
q_eq = 0.0017855282237914806
P    = 368.50804285212683 kN
R    = 0.021212151265274315 kN mm
```

Difference from N48 stationary result:

```text
Delta P = 0.18849035625 kN = 0.0511757671 %
```

This is an order-sensitivity audit, not a second stationary root.

---

## 8. Formal status

```text
R10_MATERIAL_TARGET_AUDIT                         = PASS_COMPLETE
R10B_REPRESENTATION_FIDELITY_AUDIT                = PASS_ENGINEERING_WITH_REPRODUCIBILITY_GAP
HISTORICAL_COEFFICIENT_GENERATOR                   = UNRECOVERED
HISTORICAL_COEFFICIENT_ARRAYS                      = UNRECOVERED
R10B_COEFFICIENT_GENERATION_CONVENTION             = CHEBYSHEV_ROOT_DCT_V1
MATERIAL_REPRODUCTION_ORDER                        = 112
FORMAL_N112_COEFFICIENT_TABLE                      = SAVED
R10_R10B_RECOVERY_SEQUENCE_THROUGH_COEFFICIENTS    = COMPLETE
ZERO_SPATIAL_D15_ARCHITECTURE                      = RETAINED
SAME_MULTIAXIAL_CURRENT_MAP                        = RETAINED
STRUCTURAL_Pu_CALIBRATION                          = NO
SWARTZ24                                           = NOT_STARTED
```

---

## 9. Current prohibitions

- do not invent/select a new R10 material law during recovery;
- do not use Case21/Swartz Pu to alter R10 material physics;
- do not retroactively label `CHEBYSHEV_ROOT_DCT_V1` as the historical R10B generator;
- do not reinterpret N=112 as a material parameter count;
- do not replace coefficient algebra by spatial numerical quadrature;
- do not fit whole-structure P/R/U from spatial samples;
- do not use finite-difference production derivatives;
- do not start Swartz24 until the reproducible N112 material baseline is recompiled and Case21 is reclosed.

---

## 10. Agreed recovery sequence — CLOSED THROUGH COEFFICIENT TABLE

```text
1. audit the R10 material target;                         DONE
2. audit R10B representation fidelity to that R10 target; DONE
3. recover or explicitly re-freeze coefficient rule;      DONE
4. output formal coefficient table and derivation;        DONE
```

No additional material-recovery stage is authorized.

### 10.1 Immediate next task

```text
CURRENT_RECOVERY_NEXT_TASK
= RECOMPILE_N112_MATERIAL_BASELINE_IN_EXISTING_ZERO_SPATIAL_D15_BACKEND
```

This is not a new theory route. It must:

1. use the frozen N112 coefficient table;
2. reuse the existing Cayley-Hamilton/D15 backend;
3. determine the smallest structural spatial coefficient order meeting the engineering order gate;
4. regenerate P,R and same-expression derivatives;
5. reclose the Case21 stationary root;
6. compare with the historical R10B result only after the new reproducible chain is complete.

### 10.2 Production-stage task after reclosure

```text
CURRENT_PRODUCTION_NEXT_TASK
= R11_SWARTZ24_COMMON_SPECTRAL_DOMAIN_AND_ZERO_SPATIAL_BATCH_PRECHECK
```

R11 remains deferred until the reproducible R10B Case21 chain is reclosed.

---

## 11. Recovery read order

1. `current/CURRENT_STATE.md`
2. `governance/R10B_FIDELITY_AND_COEFFICIENT_REFREEZE_DECISION_20260811.md`
3. `current/theory/NZ_SCCM_R10B_COEFFICIENT_GENERATION_CONTRACT_V1_20260811.md`
4. `current/theory/NZ_SCCM_R10B_REPRESENTATION_FIDELITY_AUDIT_20260811.md`
5. `current/theory/r10b_coefficient_generator_v1.py`
6. `current/theory/NZ_SCCM_R10B_N112_MATERIAL_COEFFICIENTS_20260811.csv`
7. `governance/R10_MATERIAL_TARGET_INTENT_AUDIT_DECISION_20260811.md`
8. `current/theory/NZ_SCCM_R10_MATERIAL_TARGET_INTENT_AUDIT_20260811.md`
9. historical R10/R10B theory/results
10. frozen current operator + exact-moment foundation
11. original conversation evidence
12. recovery notes only after governing/current files above
