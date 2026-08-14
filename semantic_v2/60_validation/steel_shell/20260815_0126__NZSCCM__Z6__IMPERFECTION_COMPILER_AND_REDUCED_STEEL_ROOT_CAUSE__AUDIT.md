# NZ-SCCM Z6 root-cause isolation — imperfection identity, compiler fidelity, and reduced steel continuation audit

**Timestamp:** 2026-08-15 01:26 +08:00  
**Identity:** CURRENT DIAGNOSTIC AUDIT / NO THEORY CHANGE / NO STRUCTURAL CALIBRATION  
**Parent current-state entry:** `semantic_v2/00_index/20260815_0126__NZSCCM__PROJECT__CURRENT_STATE_AND_OPEN_GAPS__SEMANTIC_INDEX.md`  
**Baseline execution:** `semantic_v2/40_execution/steel_shell/20260814_2240__NZSCCM_Z0_Z6__VS_ZHOU__EXECUTION_REPORT.md`

---

## 0. Purpose and frozen boundaries

This audit executes the user-directed next task: isolate why representative Zhou point Z6 is approximately `23.4%` below the Zhou comparator, without reopening Z1/Z3/Z4/Z5 and without changing the successful ordinary-concrete parent theory.

Frozen identities remain:

```text
FORMAL_DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
GENERALIZED_COORDINATES = D,q
KINEMATICS = NGUYEN_SECOND_ORDER
R10 = FROZEN
N48-C1/MM = FROZEN PRODUCTION COMPILER IDENTITY
CAYLEY_HAMILTON = GOVERNING
GENERAL_D15 = GOVERNING
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_SPATIAL_SUBDOMAINS = 1
STRUCTURAL_CALIBRATION = NO
EXPERIMENTAL/COMPARATOR_LOAD_USED_FOR_ROOT_SELECTION = NO
```

No Z6-specific load factor, R10 refit, observed-mode fit, or cross-case scaling is introduced.

---

## 1. Baseline Z6 regression

The persisted reduced ideal-EP coefficient-space kernel was reconstructed and first required to reproduce the stored Z6 control state before any sensitivity test.

Baseline input:

```text
a = 9000 mm
b = 12000 mm
h = 130 mm
tc = 122 mm
ts_each_face = 4 mm
fy = 355 MPa
fcu = 40 MPa
ell = 9000 mm
q0 = 1/400 = 0.0025
compiler interval = [-1.15, 0.23]
```

Stored control:

```text
D = 0.663425
q = 0.0054394
Pc = 11.9026733 MN
Ps = 22.3585766 MN
Pu = 34.2612499 MN
Zhou comparator = 44.7404028 MN
error = -23.4221246 %
control = yield cusp first maximum
```

Independent re-evaluation of the same finite coefficient-space expressions gives

```text
P = 34.26124986995 MN
Pc = 11.90267330996 MN
Ps = 22.35857655999 MN
sigma_VM,max ~= 354.9994 MPa
```

Therefore:

```text
Z6_BASELINE_KERNEL_REGRESSION = PASS
```

The following sensitivities are not contaminated by a failure to reproduce the parent execution.

---

## 2. Z6-A — comparator / initial-imperfection identity

### 2.1 What the current NZ-SCCM run uses

The Z0-Z6 reduced execution fixes

\[
q_0=\frac{1}{400}=0.0025.
\]

Because the structural amplitude is normalized by `b`, this means

\[
A_{0,NZ}=q_0b=\frac{b}{400}.
\]

For Z6 (`b=12000 mm`):

\[
\boxed{A_{0,NZ}=30\ \mathrm{mm}}.
\]

Historical project records also explicitly classify `b/400` as an engineering imperfection assumption rather than a measured specimen imperfection.

### 2.2 What Zhou's source numerical methodology states

Zhou Siming's dissertation, Chapter 2 §2.5.1, states for the elastoplastic stability finite-element model that the first elastic eigen-buckling mode is introduced as the initial imperfection and **the imperfection amplitude is 1/500 of the wall height**.

Chapter 6 §6.3.5 and §6.4.5 repeat the same `A0=a/500` convention for the refined numerical simulations of the test walls.

The current text retrieval did not expose an equally explicit repeated sentence inside Chapter 5 §5.3.2 itself. Therefore this audit does **not** relabel `a/500` as a fully proven Table-5.1-row-specific input. Instead:

```text
ZHOU_GENERAL_ELASTOPLASTIC_FE_IMPERFECTION = FIRST EIGENMODE, A0=a/500 : SOURCE-CONFIRMED
CH5_TABLE5.1_EXPLICIT_RESTATEMENT = NOT YET DIRECTLY RECOVERED
```

This is sufficient to identify a serious comparator-identity mismatch candidate and to justify an **identity sensitivity**, not a production correction.

### 2.3 Z6 normalization mismatch

If the Chapter-2 source convention applies to the Chapter-5 Table-5.1 elastoplastic family, Z6 would use

\[
A_{0,Zhou}=\frac{a}{500}=\frac{9000}{500}=18\ \mathrm{mm}.
\]

In the NZ-SCCM `q=A/b` normalization this is

\[
q_{0,Zhou-equivalent}
=\frac{a}{500b}
=\frac{9000}{500\times12000}
=0.0015.
\]

Thus current Z6 uses

```text
NZ-SCCM A0 = 30 mm
source-equivalent sensitivity A0 = 18 mm
NZ/source-equivalent amplitude ratio = 1.6667
```

The present Z6 calculation therefore carries a **66.7% larger initial-amplitude assumption** than the source-equivalent `a/500` sensitivity.

### 2.4 One-variable exact-kernel sensitivity

Only `q0` was changed from `0.0025` to `0.0015`. The following were held fixed:

- R10 physical target;
- N48 order and coefficient-generation rule;
- Z6 compiler interval `[-1.15,0.23]`;
- Cayley-Hamilton lift;
- Nguyen second-order field;
- general-D15 exact moments;
- geometry and material data;
- reduced ideal-EP steel rule;
- no experimental/comparator load in solving.

Because the persisted reduced steel yield monitor is independent of `q0`, the yield-cusp control was isolated by solving the equilibrium condition together with first yield.

Result:

```text
q0 = 0.0015
D_y = 0.6658418936
q_y ~= 0.0053954
Pc_y = 14.2862433639 MN
Ps_y = 23.0914841646 MN
Pu_y = 37.3777275285 MN
error vs Zhou = -16.4564349 %
```

Relative to the current baseline:

```text
Pu gain = +3.11647766 MN
original gap = 10.47915291 MN
remaining gap = 7.36267525 MN
fraction of original gap closed = 29.7398 %
```

A post-yield equilibrium point under the same `q0=0.0015` reduced rule was also checked:

```text
D = 0.67
q ~= 0.0054464
P ~= 37.2361667 MN
alpha ~= 0.99282
sigma_VM,max^E ~= 357.57 MPa
```

The branch has already descended from `37.37773 MN`. Therefore the reduced model **still has a yield-cusp first maximum** after the imperfection sensitivity; the load increase is not produced by selecting a later arbitrary point.

### 2.5 Z6-A decision

```text
Z6_IMPERFECTION_IDENTITY_MISMATCH = SIGNIFICANT / SOURCE-MOTIVATED
EXPLAINS_ENTIRE_23p4_PERCENT_GAP = NO
CLOSES_APPROX_ORIGINAL_GAP = 29.74 %
PROMOTE_q0_0p0015_TO_PRODUCTION = NOT YET AUTHORIZED
REQUIRED_SOURCE_FOLLOWUP = CONFIRM CH5 TABLE5.1 INHERITANCE EXPLICITLY
```

---

## 3. Why the mismatch is especially important for Z6

The source convention is referenced to wall height `a`, whereas the current NZ-SCCM engineering assumption is referenced to width `b`.

Under `q=A/b`, a source-equivalent `a/500` becomes

\[
q_0^{src}=\frac{a}{500b}.
\]

For the seven representative geometries this would be:

|Case|a/b|source-equivalent q0=a/(500b)|current q0|relation|
|---|---:|---:|---:|---|
|Z0|1.00|0.0020|0.0025|current +25%|
|Z1|1.00|0.0020|0.0025|current +25%|
|Z2|1.00|0.0020|0.0025|current +25%|
|Z3|1.00|0.0020|0.0025|current +25%|
|Z4|0.75|0.0015|0.0025|current +66.7%|
|Z5|1.50|0.0030|0.0025|current -16.7%|
|Z6|0.75|0.0015|0.0025|current +66.7%|

This table is an identity observation, not a proposal to recalculate all passed cases. It explains why a universal `b/400` assumption is not automatically comparator-equivalent across aspect ratios.

Z6 is additionally deep in the stability-sensitive range identified in Zhou's Chapter 5: source conclusions give elastic critical ratios around `a/h=36`, `b/h=60`, and elastoplastic critical ratios `a/h<20`, `b/h=40`. Z6 has

\[
a/h=69.23,\qquad b/h=92.31,
\]

so imperfection amplitude and post-yield redistribution are expected to be more consequential there than in a stockier strength-controlled point.

---

## 4. Z6-B — compiler-fidelity sensitivity

Z6 has the broadest positive reachable material spectrum and already required the expanded production diagnostic interval

```text
[-1.15, 0.23]
T constrained-minimax objective ~= 0.148153477
```

To test whether compiler breadth can plausibly account for the `10.479 MN` load gap, the same current `q0=0.0025` diagnostic was repeated with a still wider material interval:

```text
[-1.25, 0.30]
T constrained-minimax objective ~= 0.19660435
```

The objective actually becomes worse because the same N48 order is being asked to cover a wider domain. Re-equilibrating the reduced yield-cusp state gives approximately

```text
D ~= 0.6610466512
q ~= 0.0054827
Pu ~= 34.4622866 MN
error vs Zhou ~= -22.9728 %
```

Compared with baseline:

```text
capacity shift ~= +0.20104 MN
fraction of original gap ~= 1.92 %
```

Therefore:

```text
Z6_COMPILER_BREADTH = REAL FIDELITY CONCERN
COMPILER_BREADTH_AS_MAIN_23p4_PERCENT_CAUSE = NOT SUPPORTED
WIDEN_INTERVAL_TO_TUNE_Pu = REJECTED
INCREASE/REFIT_COMPILER_BEFORE_STEEL_MECHANISM_AUDIT = NOT JUSTIFIED
```

The compiler remains an uncertainty contributor, but it is not numerically capable of explaining the dominant discrepancy in this first isolation test.

---

## 5. Z6-C — reduced whole-shell radial cap emerges as the primary remaining hypothesis

After the source-equivalent imperfection sensitivity, the remaining comparator gap is

\[
44.7404028-37.3777275=7.3626753\ \mathrm{MN}.
\]

At that yield-cusp state, the reduced shell contribution is

\[
P_s\approx23.0914842\ \mathrm{MN}.
\]

The two faceplates have total area

\[
A_s=96000\ \mathrm{mm^2},
\]

so the ideal uniform axial yield-force upper reference is

\[
A_sf_y=96000\times355=34.08\ \mathrm{MN}.
\]

This leaves a purely arithmetic steel-force reserve relative to the first-yield state of

\[
34.08-23.09148=10.98852\ \mathrm{MN}.
\]

The remaining Z6 comparator gap is about

\[
\frac{7.36268}{10.98852}=67.0\%
\]

of that reserve.

This does **not** prove that the true structure must mobilize 67% of the remaining uniform yield force; global bending, concrete redistribution, `Rq=0`, and stability constraints remain active. It does show that the magnitude of the unexplained gap is mechanically compatible with a missing progressive steel redistribution mechanism.

The current reduced branch uses

\[
\alpha=\min\left(1,\frac{f_y}{\sigma_{VM,max}^E}\right),
\qquad
\boldsymbol\sigma_s=\alpha\boldsymbol\sigma_s^E,
\]

so after the **first local point** reaches yield, one scalar `alpha` scales the stress contribution of the whole shell. The stability material tangent is simultaneously assigned the locked ideal-plastic effective value. This was explicitly introduced only as a reduced mechanism diagnostic, not as a resolved 2D expanding-plastic-zone operator.

For a very wide/slender panel such as Z6, this construction can suppress the natural sequence

```text
first local yield
-> finite yielded zone
-> surrounding elastic shell remains stiff
-> stress redistribution / progressive yield-front growth
-> possible continued load increase
```

and replace it by an artificially globalized loss of shell stress/tangent capacity.

Thus the current ranking is:

```text
PRIMARY_REMAINING_HYPOTHESIS = HOMOGENEOUS_WHOLE_SHELL_RADIAL_CAP / MISSING_PROGRESSIVE_YIELD_REDISTRIBUTION
STATUS = STRONGLY SUPPORTED BY MAGNITUDE AND MODEL IDENTITY, NOT YET PROVEN
```

No full 2D plastic operator is invented in this audit.

---

## 6. Z6-D — geometry, halfwave, and KZ remain downstream checks

Z6's extreme `a/h` and `b/h` make global stability ordering important. However, current governance remains binding:

- formal halfwave is selected by the design-side theoretical energy/minimum principle;
- an experimentally or numerically observed longer/asymmetric bulge must not be used to fit the production halfwave;
- `K_Z=0`, first yield, local shell buckling, and the direct limit event are distinct controls.

This audit does not yet change the formal halfwave or claim a completed Z6 full same-expression KZ ordering. That check follows the steel-continuation audit because the current shell tangent after first yield is precisely one of the mechanisms now under suspicion.

---

## 7. Root-cause ranking after this execution

|Rank|candidate|current evidence|decision|
|---:|---|---|---|
|1|homogeneous whole-shell post-yield radial cap / missing progressive yield-front redistribution|remaining 7.36 MN gap is commensurate with available steel reserve; current operator globalizes first local yield|**primary next calculation**|
|2|imperfection/comparator normalization (`b/400` vs source methodology `a/500`)|q0-only exact-kernel sensitivity raises Pu by 3.116 MN and closes 29.74% of baseline gap|**significant partial cause; Chapter-5 inheritance confirmation still required**|
|3|N48 compiler breadth / T minimax fidelity|wider-interval sensitivity changes Pu by only ~0.201 MN|secondary; cannot explain 23.4% gap|
|4|formal halfwave / KZ ordering|Z6 is deep stability-controlled and merits recheck|defer until steel tangent/continuation is made source-consistent; no mode fitting|
|5|R10 ordinary-concrete target|no evidence from this isolation requires reopening it|do not change|

---

## 8. Current decision and next executable task

```text
RERUN_Z1_Z3_Z4_Z5 = NO
CHANGE_R10 = NO
TUNE_N48_INTERVAL_TO_ZHOU = NO
APPLY_Z6_EMPIRICAL_FACTOR = NO
FIT_FORMAL_HALFWAVE_TO_ZHOU = NO

Z6_A_IMPERFECTION_IDENTITY_FIRST_PASS = COMPLETE / SIGNIFICANT_PARTIAL_CAUSE
Z6_B_COMPILER_SENSITIVITY_FIRST_PASS = COMPLETE / INSUFFICIENT_AS_MAIN_CAUSE
Z6_C_REDUCED_STEEL_CONTINUATION = NEXT PRIORITY
Z6_D_FULL_KZ_AND_HALFWAVE_ORDERING = AFTER Z6_C
```

The next steel task must preserve the project's zero-structural-quadrature architecture and should first determine a source-consistent way to represent **progressive** yield redistribution in the continuous steel shell. A controlled non-homogeneous analytic yield-front diagnostic may be used to test mechanism sufficiency, but it must not be promoted to the production steel operator unless its material identity and consistent tangent are source-grounded and finite-analytic/D15 compatible.

Before any q0 change is promoted from sensitivity to comparator correction, Chapter 5 §5.3.2/Table 5.1 inheritance of the Chapter-2 `a/500` imperfection convention must be explicitly confirmed from the source text or original model record.
