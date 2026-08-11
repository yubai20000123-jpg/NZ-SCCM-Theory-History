# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-11 15:30 +08:00  
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

Final production capacity must come from explicit finite formulas/analytic coefficient algebra and explicit derivatives of the same representation. Numerical root solving of already explicit finite equations is allowed.

Formal production prohibits spatial Gauss/Simpson/adaptive quadrature, material-point grids, moving spatial TT/TC/CC cells, whole-structure P/R/U fits from spatial numerical integration, structural-load calibration of material parameters, and finite-difference production derivatives.

---

## 1. Active material architecture

The active architecture remains

```text
multidimensional/current NC operator
-> lambda+, lambda-
-> 1D scalar master law
-> R10 material-energy regularization of the tensile scalar target
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

Use the following identities strictly:

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

R10B changes no material parameter or multidimensional interaction coefficient. It may have finite-order material-representation and spatial-coefficient truncation error. Exactness in R10B means exact coefficient algebra and exact complete-halfwave moment contraction after the retained finite representation is fixed.

Interpret the R10B orders as

```text
N_M = 48 = 1D material-coordinate analytic representation order
N_S = 28 = structural spatial coefficient-representation order
```

They are not material-parameter counts, material-point counts, spatial integration-point counts, or inferred totals such as `147`.

The exact historical R10B coefficient-generation convention remains unresolved. DCT-I, DCT-II, continuous projection, least-squares weighting, or any particular coefficient-array count must not be asserted as historical R10B fact without original evidence.

### 1B. New R10 material-target audit

Canonical audit files:

- `current/theory/NZ_SCCM_R10_MATERIAL_TARGET_INTENT_AUDIT_20260811.md`
- `governance/R10_MATERIAL_TARGET_INTENT_AUDIT_DECISION_20260811.md`

The audit establishes that the executed R10 is **not** mathematically a tiny local source patch. It replaces the whole retained tensile interval

\[
0\le t\le10x_{cr}
\]

with two C2 quintic branches while preserving selected physical/C2 anchors and total source work.

Material-coordinate audit finds approximately:

```text
max |u_R10-u_source|                         ~= 0.01831
absolute redistributed work / source work   ~= 9.89 %
positive relocated work / source work        ~= 4.95 %
first-moment shift of tensile work           ~= -5.90 %
```

Therefore the phrase `smoothing only of the sharp feature` may describe the motivation, but it is not a complete mathematical description of the executed target.

Current audit status:

```text
R10_EXECUTED_FORMULA_RECOVERY                 = PASS
R10_SOURCE_WORK_EQUALITY                       = PASS
R10_C2_TARGET_INTERNAL_CONSISTENCY              = PASS
R10_SAME_MULTIAXIAL_REINSERTION_ARCHITECTURE    = PASS
R10_AS_TINY_LOCAL_SOURCE_PATCH                  = FAIL_DESCRIPTION
R10_AS_WHOLE_RETAINED_TENSILE_BRANCH_REBUILD    = PASS_DESCRIPTION
R10_ORIGINAL_INTENT_VS_EXECUTED_TARGET           = HOLD_RECONCILIATION
STRUCTURAL_Pu_CALIBRATION                       = NO
```

Existing R10/R10B numerical records are not revoked; they remain valid records of the executed R10 target.

---

## 2. Latest executed structural stage: R10B

Canonical files:

- `current/theory/NZ_SCCM_R10B_ZERO_SPATIAL_D15_CASE21_20260811.md`
- `current/theory/NZ_SCCM_R10B_ZERO_SPATIAL_D15_CASE21_results.json`
- `governance/R10B_ZERO_SPATIAL_CASE21_DECISION_20260811.md`
- `evidence/NZ_SCCM_R10B_ARTIFACT_HASHES_20260811.md`

Decision:

```text
R10B_ZERO_SPATIAL_CASE21 = PASS_ENGINEERING
```

R10B is a compiler/integration stage only. It changes no material parameter.

---

## 3. Case21-local analytic spectral contract

R10B freezes the search box

\[
D\in[0.78,0.90],\qquad q\in[0.0015,0.0021].
\]

For Case21 `ell/b=1`, the analytic separation inequality gives

\[
X_{11}-X_{22}\ge D-\frac{M}{1+\nu}.
\]

At `qmax=0.0021`:

```text
Mmax = 0.035204737229723046
Bmax = 0.07844047893484817
certified gap lower = 0.7501654769239635
```

The certified principal intervals are

\[
\lambda_+\in[-0.0956591207,0.1029457518],
\]

\[
\lambda_-\in[-1.0029457518,-0.6843408793].
\]

R10B uses safe-margin compiler intervals

```text
lambda+ : [-0.10, 0.105]
lambda- : [-1.01,-0.68]
```

inside one scalar polynomial hull. This is a spectral-domain reduction and does not create a spatial material-state partition.

---

## 4. Zero-spatial coefficient algebra

The 1D material-coordinate compiler generates finite Chebyshev representations of the frozen scalar functions. These are derived compiler coefficients, not material fitting parameters.

The equivalent tensor is mapped to

\[
Y=aI+bE_u,
\]

with invariants

\[
K_1=\operatorname{tr}Y,\qquad K_2=\det Y.
\]

Cayley-Hamilton pair algebra:

\[
F(Y)=A(K_1,K_2)I+B(K_1,K_2)Y,
\]

\[
(A,B)(C,D)=(AC-BDK_2,\ AD+BC+BDK_1).
\]

The frozen R10 interaction is reconstructed algebraically:

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

All spatial fields are finite tensor-Chebyshev coefficient arrays in `(sin X,sin Y,zeta)`. FFT is only a coefficient-index convolution accelerator; there are no physical-space sample points.

Exact moments:

\[
\int_0^\pi T_n(\sin X)dX=\pi\ (n=0),\quad 2\sin(n\pi/2)/n\ (n\ge1),
\]

\[
\int_{-1}^{1}T_k(\zeta)d\zeta=0\ (k\ odd),\quad 2/(1-k^2)\ (k\ even).
\]

Thus

```text
N_formal_spatial_sampling   = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

---

## 5. Same-expression derivative gate

Forward chain-rule jets are propagated through the same retained coefficient algebra.

No finite-difference production derivative is used.

At the N48 root:

```text
P_D = 106.58759351383472
P_q = -75105.39767023241
R_D = -1376.335532846137
R_q = 969815.5988960797
L   = 83.31643116474152
L_normalized = 4.029999719717427e-07
```

Along the explicit equilibrium branch

\[
\frac{dP}{dD}=\frac{L}{R_q},
\]

which equals `8.590955977567161e-05 kN` at the selected state.

---

## 6. Current formal Case21 zero-spatial result

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

Experiment, used only after material freeze:

```text
Pf = 368.312750 kN
error = +0.006802495877 kN = +0.001846934671 %
```

The close agreement must not be used to retune R10.

---

## 7. Engineering order sensitivity

At the N48 stationary D, a separate zero-spatial N96 equilibrium check gives

```text
q_eq = 0.0017855282237914806
P    = 368.50804285212683 kN
R    = 0.021212151265274315 kN mm
```

Difference from the N48 formal root:

```text
Delta P = 0.18849035625 kN = 0.0511757671 %
```

N96 was not separately reoptimized in D, so this is an order-sensitivity audit, not a second stationary root.

The previously required theorem-level tight remainder certificate is not an engineering hard gate. The observed 0.051% order sensitivity is accepted for continued theory development.

---

## 8. Formal status

```text
R10_EXECUTED_TARGET_RECORD                    = PASS
R10_ORIGINAL_INTENT_VS_EXECUTED_TARGET        = HOLD_RECONCILIATION
R10B_1D_MATERIAL_RECOMPILE                    = PASS_FOR_EXECUTED_R10_TARGET
SAME_MULTIAXIAL_CURRENT_MAP                   = PASS
CASE21_SPECTRAL_DOMAIN_CERTIFICATE            = PASS
EXACT_COMPLETE_HALFWAVE_MOMENT_CONTRACTION    = PASS
SAME_EXPRESSION_DERIVATIVES                   = PASS
CASE21_N48_LIMIT_ROOT                          = PASS
N96_ENGINEERING_ORDER_CHECK                   = PASS
STRUCTURAL_Pu_CALIBRATION                      = NO
SWARTZ24                                      = NOT_STARTED

R10B_ZERO_SPATIAL_CASE21 = PASS_ENGINEERING_FOR_EXECUTED_R10_TARGET
```

This wording supersedes any interpretation that R10 material-target intent is fully reconciled merely because the R10/R10B Case21 calculations passed numerically.

---

## 9. Current prohibitions

- do not change `h` because Case21 agrees with experiment;
- do not use Case21/Swartz Pu to choose between alternative R10 material targets;
- do not modify the multidimensional CC/TC/TT interaction while resolving the 1D R10 target identity;
- do not replace coefficient algebra by spatial numerical quadrature;
- do not fit whole-structure P/R/U from spatial samples;
- do not use finite-difference production derivatives;
- do not copy the Case21 spectral compiler intervals directly into Swartz24;
- do not reinterpret `N_M=48` as a material-parameter count or an inferred total coefficient count;
- do not assert a historical R10B DCT/least-squares coefficient generator without original compiler evidence;
- do not freeze/publish R10B coefficient tables before the final R10 material target identity is resolved;
- do not reinterpret this material-target audit as failure of the zero-spatial D15 architecture.

---

## 10. Current recommended next tasks

### 10.1 Immediate active recovery task

```text
CURRENT_RECOVERY_NEXT_TASK
= R10A_MATERIAL_TARGET_INTENT_RECONCILIATION
```

R10A must decide, from material/source/analytic considerations only, whether the formal material target should be:

```text
A. the already executed whole-retained-branch C2 energy reconstruction;

or

B. a genuinely local source-preserving regularization that changes only the minimum necessary 1D sharp-feature region.
```

No structural load calibration is allowed.

### 10.2 Production-stage task after recovery identity is resolved

```text
CURRENT_PRODUCTION_NEXT_TASK
= R11_SWARTZ24_COMMON_SPECTRAL_DOMAIN_AND_ZERO_SPATIAL_BATCH_PRECHECK
```

R11 remains a precheck only. It must not start the 24-panel batch until its analytic domain/order gates pass.

### 10.3 R10B coefficient-reconstruction order

If the immediate task is to recover/publish the R10B coefficient-generation process, the required order is:

```text
1. resolve R10A material-target identity;
2. audit R10B representation fidelity to the final frozen R10 target;
3. recover the historical coefficient generator from original evidence,
   or explicitly freeze a new transparent reproducibility convention;
4. only then generate/publish coefficient tables.
```

---

## 11. Recovery read order

1. `current/CURRENT_STATE.md`
2. `governance/R10_MATERIAL_TARGET_INTENT_AUDIT_DECISION_20260811.md`
3. `current/theory/NZ_SCCM_R10_MATERIAL_TARGET_INTENT_AUDIT_20260811.md`
4. `governance/R10_R10B_IDENTITY_AND_INTERPRETATION_CLARIFICATION_20260811.md`
5. `governance/R10B_ZERO_SPATIAL_CASE21_DECISION_20260811.md`
6. `current/theory/NZ_SCCM_R10B_ZERO_SPATIAL_D15_CASE21_20260811.md`
7. `current/theory/NZ_SCCM_R10B_ZERO_SPATIAL_D15_CASE21_results.json`
8. `governance/R10_1D_ENERGY_SMOOTHING_DECISION_20260810.md`
9. R10 theory/results
10. frozen current operator + exact-moment foundation
11. historical nested-D15 and G19/R03 evidence
12. recovery notes only after the governing files above
