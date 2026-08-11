# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-11 15:53 +08:00  
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
-> local source-preserving material-energy regularization
-> SAME U/C/T + CC/TC/TT interaction
-> same spectral return
```

No global material-energy-potential fit is active.

### 1A. Governing identity — material change vs analytic compilation

Use the following identities strictly:

```text
SOURCE FOSTER -> final local regularized target
= material-target modification

final local regularized target -> analytic/D15 compiler
= finite analytic compilation / reintegration only
```

The material scalar coordinate remains

\[
t=\Pi_\eta(\lambda).
\]

The analytic compiler may have finite-order material-representation and spatial-coefficient truncation error. Exactness means exact coefficient algebra and exact complete-halfwave moment contraction after the retained finite representation is fixed.

The historical R10B orders remain interpreted as

```text
N_M = 48 = 1D material-coordinate analytic representation order
N_S = 28 = structural spatial coefficient-representation order
```

They are not material-parameter counts, material-point counts, spatial integration-point counts, or inferred totals such as `147`.

The exact historical R10B coefficient-generation convention remains unresolved. DCT-I, DCT-II, continuous projection, least-squares weighting, or any particular coefficient-array count must not be asserted as historical R10B fact without original evidence.

### 1B. Executed R10 audit

Canonical audit files:

- `current/theory/NZ_SCCM_R10_MATERIAL_TARGET_INTENT_AUDIT_20260811.md`
- `governance/R10_MATERIAL_TARGET_INTENT_AUDIT_DECISION_20260811.md`

The audit established that the executed R10 is not mathematically a tiny local source patch. It replaces the whole retained tensile interval

\[
0\le t\le10x_{cr}
\]

with two C2 quintic branches while preserving selected physical/C2 anchors and total source work.

Material-coordinate audit found approximately:

```text
max |u_R10-u_source|                         ~= 0.01831
absolute redistributed work / source work   ~= 9.89 %
positive relocated work / source work        ~= 4.95 %
first-moment shift of tensile work           ~= -5.90 %
```

Therefore the executed R10 is a broad equivalent tensile-law reconstruction.

### 1C. R10A governing reconciliation

Canonical files:

- `current/theory/NZ_SCCM_R10A_MATERIAL_TARGET_INTENT_RECONCILIATION_20260811.md`
- `governance/R10A_MATERIAL_TARGET_INTENT_RECONCILIATION_DECISION_20260811.md`

R10A resolves the target identity as

```text
R10A_MATERIAL_TARGET_INTENT_RECONCILIATION = PASS_DECISION

SELECTED_TARGET
= B_LOCAL_SOURCE_PRESERVING_REGULARIZATION
```

The formal target must satisfy exact source identity outside local regularization intervals:

\[
\boxed{u_{local}(t)=u_{src}(t),\qquad t\notin\mathcal I_{reg}.}
\]

For each interval \([a_k,b_k]\), the minimum contract is source value/slope/curvature matching at both endpoints plus local work equality:

\[
p_k(a_k)=u_{src}(a_k),\quad p_k'(a_k)=u'_{src}(a_k),\quad p_k''(a_k)=u''_{src}(a_k),
\]

\[
p_k(b_k)=u_{src}(b_k),\quad p_k'(b_k)=u'_{src}(b_k),\quad p_k''(b_k)=u''_{src}(b_k),
\]

\[
\boxed{\int_{a_k}^{b_k}p_k(t)dt=\int_{a_k}^{b_k}u_{src}(t)dt.}
\]

These are seven deterministic constraints; degree 6 is the minimum polynomial degree capable of satisfying the complete C2 + local-work contract without a free fitting coefficient. The actual interval endpoints and final patch order are not yet frozen and must be determined from material/source/analytic quantities only.

No Case21/Swartz capacity is used in this selection.

---

## 2. Latest executed structural stage and its new identity

The latest executed structural stage remains the previous R10B calculation:

- `current/theory/NZ_SCCM_R10B_ZERO_SPATIAL_D15_CASE21_20260811.md`
- `current/theory/NZ_SCCM_R10B_ZERO_SPATIAL_D15_CASE21_results.json`
- `governance/R10B_ZERO_SPATIAL_CASE21_DECISION_20260811.md`
- `evidence/NZ_SCCM_R10B_ARTIFACT_HASHES_20260811.md`

However, after R10A selects the local source-preserving material target, the prior R10/R10B identity is now

```text
R10_WHOLE_BRANCH_C2_TARGET
= EXECUTED_REFERENCE_BASELINE

R10B_ZERO_SPATIAL_CASE21_FOR_WHOLE_BRANCH_TARGET
= EXECUTED_REFERENCE_BASELINE
```

The prior calculation remains valid evidence for the actually executed whole-branch R10 target and for the zero-spatial analytic architecture. It is not the final production result of the newly selected local material target.

---

## 3. Historical Case21-local analytic spectral contract

The previous R10B execution froze

\[
D\in[0.78,0.90],\qquad q\in[0.0015,0.0021].
\]

For Case21 `ell/b=1`, it certified

\[
\lambda_+\in[-0.0956591207,0.1029457518],
\]

\[
\lambda_-\in[-1.0029457518,-0.6843408793].
\]

and used safe-margin compiler intervals

```text
lambda+ : [-0.10, 0.105]
lambda- : [-1.01,-0.68]
```

inside one scalar polynomial hull.

These bounds remain evidence from the executed R10B Case21 branch. They may be reused as a structural-domain starting point only after the new local target is frozen; they do not determine the material patch interval and must not be used as a material calibration rule.

---

## 4. Zero-spatial coefficient algebra retained

The retained analytic architecture is unchanged.

The equivalent tensor is mapped to

\[
Y=aI+bE_u,
\]

with

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
\int_0^\pi T_n(\sin X)dX=\pi\ (n=0),\quad 2\sin(n\pi/2)/n\ (n\ge1),
\]

\[
\int_{-1}^{1}T_k(\zeta)d\zeta=0\ (k\ odd),\quad 2/(1-k^2)\ (k\ even).
\]

Thus the governing formal contract remains

```text
N_formal_spatial_sampling   = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

---

## 5. Same-expression derivative architecture retained

Forward chain-rule jets through the same retained coefficient algebra remain required.

No finite-difference production derivative is allowed.

The previous R10B derivative values remain reference evidence for the whole-branch target only; they must be regenerated after the local target is frozen and recompiled.

---

## 6. Previous R10B Case21 value — reference identity only

For the executed whole-branch R10 target, the prior R10B result was

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

Experiment was introduced only after that material target was frozen:

```text
Pf = 368.312750 kN
error = +0.006802495877 kN = +0.001846934671 %
```

After R10A, this numerical agreement must not be used to preserve the whole-branch material target. The value is now an executed-reference benchmark only.

---

## 7. Historical R10B order sensitivity

The prior N96 fixed-D equilibrium audit gave

```text
q_eq = 0.0017855282237914806
P    = 368.50804285212683 kN
R    = 0.021212151265274315 kN mm
```

with a difference from the N48 reference result of

```text
Delta P = 0.18849035625 kN = 0.0511757671 %
```

This remains evidence about the previous compiler/target combination only. A new order study is required after the local target is frozen and recompiled.

---

## 8. Formal status

```text
R10_EXECUTED_WHOLE_BRANCH_TARGET_RECORD          = RETAINED_REFERENCE
R10A_MATERIAL_TARGET_INTENT_RECONCILIATION       = PASS_DECISION
ACTIVE_1D_TARGET_IDENTITY                         = LOCAL_SOURCE_PRESERVING
LOCAL_PATCH_INTERVALS                             = NOT_YET_FROZEN
LOCAL_PATCH_FINAL_FORM                            = NOT_YET_FROZEN
R10B_PREVIOUS_RECOMPILE                           = RETAINED_REFERENCE_FOR_OLD_TARGET
ZERO_SPATIAL_D15_ARCHITECTURE                     = RETAINED
SAME_MULTIAXIAL_CURRENT_MAP                       = RETAINED
STRUCTURAL_Pu_CALIBRATION                         = NO
SWARTZ24                                          = NOT_STARTED

CURRENT_FINAL_PRODUCTION_CASE21_Pu_FOR_LOCAL_TARGET
= NOT_YET_COMPUTED
```

---

## 9. Current prohibitions

- do not use Case21/Swartz Pu to choose the local patch interval, degree or coefficients;
- do not retune the previous R10 peak `h` to recover the old Case21 result;
- do not modify the multidimensional CC/TC/TT interaction while constructing the local scalar target;
- do not revive a global material-energy potential;
- do not replace coefficient algebra by spatial numerical quadrature;
- do not fit whole-structure P/R/U from spatial samples;
- do not use finite-difference production derivatives;
- do not reinterpret `N_M=48` as a material-parameter count or inferred total coefficient count;
- do not assert a historical R10B DCT/least-squares coefficient generator without original compiler evidence;
- do not publish the old R10B coefficient tables as coefficients for the new local target;
- do not start Swartz24 before the new local target passes material gate and zero-spatial Case21 closure.

---

## 10. Current recommended next tasks

### 10.1 Immediate active task

```text
CURRENT_ACTIVE_NEXT_TASK
= R10A1_LOCAL_SOURCE_PRESERVING_PATCH_CONSTRUCTION_AND_MATERIAL_GATE
```

R10A1 must:

1. identify the source-defined sharp/high-curvature transition neighborhood(s) from the Foster scalar itself;
2. derive deterministic patch interval endpoints from source/analytic quantities only;
3. construct the lowest-complexity local C2 + local-work-preserving patch;
4. prove exact source identity outside the patch interval(s);
5. check monotonicity, no overshoot/rebound, derivative signs and curvature behavior;
6. quantify the local material perturbation;
7. pass an analytic-compilation quality gate;
8. stop before structural re-solution if the material gate fails.

### 10.2 Task after R10A1 material PASS

```text
NEXT_AFTER_R10A1
= RECOMPILE_LOCAL_TARGET_IN_ZERO_SPATIAL_D15_BACKEND
```

This recompile must use a transparent, fully reproducible material-coordinate coefficient-generation contract. Only after that may Case21 be re-solved and coefficient tables be published.

### 10.3 Deferred production-stage task

```text
R11_SWARTZ24_COMMON_SPECTRAL_DOMAIN_AND_ZERO_SPATIAL_BATCH_PRECHECK
= DEFERRED_UNTIL_LOCAL_TARGET_AND_CASE21_RECLOSE
```

---

## 11. Recovery read order

1. `current/CURRENT_STATE.md`
2. `governance/R10A_MATERIAL_TARGET_INTENT_RECONCILIATION_DECISION_20260811.md`
3. `current/theory/NZ_SCCM_R10A_MATERIAL_TARGET_INTENT_RECONCILIATION_20260811.md`
4. `governance/R10_MATERIAL_TARGET_INTENT_AUDIT_DECISION_20260811.md`
5. `current/theory/NZ_SCCM_R10_MATERIAL_TARGET_INTENT_AUDIT_20260811.md`
6. `governance/R10_R10B_IDENTITY_AND_INTERPRETATION_CLARIFICATION_20260811.md`
7. previous R10/R10B theory/results as executed-reference evidence
8. frozen source current operator + exact-moment foundation
9. original conversation evidence governing the local-source-preserving intent
10. historical nested-D15 and G19/R03 evidence
11. recovery notes only after the governing files above
