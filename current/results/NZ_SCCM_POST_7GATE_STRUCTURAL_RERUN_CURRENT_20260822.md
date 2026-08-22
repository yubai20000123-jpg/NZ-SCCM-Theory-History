# NZ-SCCM — Post-7Gate Structural Rerun Current Summary

**Updated:** 2026-08-22 14:40 +08:00  
**Status:** `SUHPC RESOLVED / TC_R1 GENERAL-S RETIRED / NC_TC_R2 COMPACT CANDIDATE / Z6 S0 AND S0+ LIMIT RESOLVED / GLOBAL Z Pu OPEN / STEEL GATE NEXT`

Current theory/audit:

`semantic_v2/20_theory/20260822_1440__NZSCCM__NC_TC_R1_COMPACTNESS_FAIL_TC_R2_REDUCTION_AND_STEEL_ACTIVESET_AUDIT.md`

Current Z6 execution:

`semantic_v2/40_execution/20260822_1440__NZSCCM__Z6_TC_R2_S0_AND_GENERAL_S_STEEL_ACTIVESET_DIAGNOSTIC.md`

Direct no-quadrature solver:

`semantic_v2/40_execution/steel_shell/20260822_1440__NZSCCM__Z6_TC_R2_DIRECT_ENDPOINT_AND_S0PLUS_LIMIT_SOLVER.py`

---

## 1. SUHPC current post-7gate results — unchanged by this NC step

| Case | Zhang 1D / MN | Current 2D / MN | status |
|---|---:|---:|---|
|T120|12.41101|12.22252|Liu TC active / finite re-cut|
|T360|11.36533|11.36533|2D gate inactive|
|BH005|2.42351|2.42351|2D gate inactive|
|BH010|4.46632|4.46632|2D gate inactive|
|BH020|8.21925|8.21925|2D gate inactive|
|BH032|11.21046|11.21046|2D gate inactive|
|BH050|13.67770|12.77154|Liu TC active / finite re-cut|

---

## 2. Z0–Z6 Nguyen-source TC transition markers — retained as cracking markers

|Case|P_TC-transition / MN|
|---|---:|
|Z0|27.033151885|
|Z1|17.093528920|
|Z2|27.033151885|
|Z3|36.744639968|
|Z4|56.203522296|
|Z5|10.747333454|
|Z6|23.832330467|

These are cracking/state-transition markers, not final Pu.

```text
TC_ENVELOPE_AS_FINAL_SC_PU = REJECTED
OLD_Z6_51_345 = SUPERSEDED
```

---

## 3. TC-R1 compactness decision

Literal Nguyen postcrack TC/TCX remains off-mainline because it stores crack/history variables.

The prior memoryless TC-R1 map also is no longer the production candidate for general-s sections. Although finite in principle, its general-s exact section integrands contain:

- [8/8] T5 rational tension in affine z;
- softened shifted-peak Saenz with a rational `degree 5 / degree 8` form in z.

That would require an opaque eighth-degree primitive/compiler layer.

```text
LITERAL_NGUYEN_POSTCRACK_TC = OFF_MAINLINE_ORACLE
TC_R1_GENERAL_S_COMPACTNESS = FAIL
TC_R1_GENERAL_S_PRODUCTION = RETIRED
```

The old TC-R1 symmetric endpoint `50.22069 MN` remains historical provenance, not current NC result.

---

## 4. Current NC TC candidate = TC-R2

TC-R2 uses:

1. finite Foster/Nguyen piecewise tension (`alpha1=10`, declared conservative project `alpha2=0.3`);
2. Poisson-free transverse material coordinate;
3. current Nguyen/MCFT softening amplitude
   \[
   \gamma_c=\min[1,(0.8+0.34\lambda_t)^{-1}];
   \]
4. fixed-peak uniaxial Saenz/postpeak compression backbone scaled directly by \(\gamma_c\):
   \[
   \sigma_c^{TC}=\gamma_c\sigma_{c0}(\lambda_c).
   \]

This is a project-derived current-strength reduction, not a claim that Nguyen proposed a history-free multiplicative law.

For affine through-thickness coordinates

\[
\lambda_t(z)=\lambda_{t0}+\nu_c\chi z,
\qquad
\lambda_c(z)=\lambda_{c0}+\chi z,
\]

all branch fronts are linear in z and the required concrete/web primitives reduce to polynomial, linear/quadratic rational, factored linear×quadratic rational, logarithmic and arctangent forms.

```text
NC_TC_R2_MATERIAL_7GATE = PASS_CANDIDATE
TC_R2_GENERAL_S_CONCRETE_WEB_PRIMITIVE_COMPACTNESS = PASS
FORMAL_SPATIAL_QUADRATURE_REQUIRED = NO
```

---

## 5. Z6 current direct TC-R2 candidates

### 5.1 Exactly symmetric s=0 branch

Uniform-section phase equilibrium + web compression-yield gives

\[
\lambda_t=0.72375111146,
\qquad
\lambda_c=-0.79066099525,
\]

\[
q=0.012018755437,
\]

\[
\boxed{P_{Z6,s=0}^{TC-R2}=50.1863826545\ \mathrm{MN}}.
\]

This is the current symmetric endpoint candidate.

### 5.2 Asymmetric s→0+ second-face-yield limit

A separate direct **no-thickness-quadrature** uniform limiting system gives

\[
\lambda_t\approx0.53638962,
\qquad
\lambda_c\approx-0.63294763,
\]

\[
q\approx0.01163665,
\]

\[
\boxed{P_{Z6,s\to0^+}^{face-yield}=48.9055510040\ \mathrm{MN}}.
\]

At this state the outer-face elastic trial stress is approximately

\[
(\sigma_x^s,\sigma_y^s)
=(+182.772,-226.373)\ \mathrm{MPa},
\]

with exactly \(\sigma_{VM}=355\) MPa, while the web remains elastic.

A local implicit-function audit gives a nonsingular asymmetric branch with

\[
P_{terminal}(s)=48.9055510+4.68s+O(s^2)\ \mathrm{MN}
\]

as \(s\to0^+\).

```text
Z6_TC_R2_S0_ENDPOINT = 50.1863826545 MN / DIRECT CANDIDATE
Z6_TC_R2_S0PLUS_LIMIT = 48.9055510040 MN / DIRECT LOCAL-LIMIT CANDIDATE
```

Neither is yet declared the global Pu because the full continuous s-domain minimum is not formally certified.

---

## 6. Why the global Z6 value is still open

An off-mainline high-order thickness-integration diagnostic was used only to expose active-set topology. It showed that for finite \(s>0\):

- one outer face yields first and may continue on the radial cap;
- web edge yielding may create a partial yield front and need not terminate the section;
- when the second outer face reaches the radial cap, the doubly-capped continuation can point back across the active surface.

Diagnostic second-face terminal values approach the direct limit:

|s|off-mainline diagnostic / MN|
|---:|---:|
|0.020|49.00288|
|0.010|48.95329|
|0.005|48.92919|
|0.001|48.91024|
|0.00001|48.90560|

At `s≈0.444855`, representative diagnostic events are:

- first web-edge yield: `~48.72244 MN`, nonterminal because partial yielding continues;
- second outer-face yield: `~51.67326 MN`, terminal complementarity kink for that fixed s.

These spatially integrated diagnostic values are **not formal Pu values**.

The current obstruction is now classified as:

```text
STEEL_FACE_MEMORYLESS_RADIAL_CAP_ACTIVESET_NONUNIFORMITY = IDENTIFIED
Z6_GLOBAL_GENERAL_S_MINIMUM = OPEN
Z0_Z6_FINAL_POSTCRACK_2D_PU = OPEN
```

Changing NC concrete to Cedolin–Mulas would not by itself remove this steel-phase topology.

---

## 7. Next hard gate

The next task is the steel-face constitutive source audit:

- verify whether the governing Z steel source is genuinely elastic-perfectly-plastic;
- search for source-grounded hardening/deformation-theory data if present;
- no hardening/Ramberg–Osgood parameter may be chosen from Z6, Zhou/Winter, FEM or experiment;
- if no source hardening exists, retain the ideal-plastic law and treat the nonuniform limit as an explicit theoretical limitation/feature rather than tuning it away.

Cedolin–Mulas 1984 remains an NC fallback, but it is no longer the immediate blocker-clearing move.

---

## 8. Formal execution flags

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_material_points = 0
RITZ_ORDER = NONE
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
STRUCTURAL_BACKBONE_CHANGED = FALSE
```
