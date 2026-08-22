# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-22 14:40 +08:00  
**Status:** `MARGUERRE_AIRY_EXPLICIT / SUHPC_2D_RESOLVED / NC_TC_R1_GENERAL_S_RETIRED / NC_TC_R2_COMPACT_CANDIDATE / Z6_S0_AND_S0PLUS_LIMIT_RESOLVED / STEEL_ACTIVESET_GATE / Z_GLOBAL_PU_OPEN / USER_ACCEPTANCE_PENDING`

## 0. Governing structural mainline

The structural theory remains unchanged:

`semantic_v2/20_theory/20260821_1733__NZSCCM__MARGUERRE_AIRY_EXPLICIT_LIMIT_THEORY_V1.md`

The governing sequence remains

\[
\boxed{
\text{1D explicit structural/capacity root}
\to
\text{Airy 2D membrane demand}
\to
\text{finite 2D phase/material current-capacity judgment}
}
\]

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_material_points = 0
RITZ_ORDER = NONE
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
HARD_ENVELOPE_HISTORY_OVERLAY = OFF_MAINLINE_DIAGNOSTIC
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
STRUCTURAL_BACKBONE_CHANGED = FALSE
USER_ACCEPTANCE = PENDING
```

---

## 1. Current source-of-truth chain

Material seven-gate chain:

1. `semantic_v2/20_theory/20260822_1151__NZSCCM__NC_UHPC_7GATE_EXPLICIT_MATERIAL_REORGANIZATION_V1.md`
2. `semantic_v2/20_theory/20260822_1240__NZSCCM__UHPC_ZHANG_BACKBONE_AND_LIU_CC_CONTINUOUS_SOURCE_MIN_GATE.md`
3. `semantic_v2/20_theory/20260822_1255__NZSCCM__NC_TC_FAILURE_ENVELOPE_VS_APPENDIXB_CONSTITUTIVE_PEAK_RESOLUTION.md`
4. `semantic_v2/20_theory/20260822_1315__NZSCCM__NC_UHPC_7GATE_MATERIAL_CERTIFICATE_V1.md`
5. `semantic_v2/20_theory/20260822_1320__NZSCCM__NC_CC_EQ317_PRINTED_TYPO_VS_FIG32_APPENDIXB_RESOLUTION.md`

Superseded postcrack candidate audit retained for provenance:

6. `semantic_v2/20_theory/20260822_1338__NZSCCM__NC_TC_MEMORYLESS_REDUCTION_R1_AND_ALTERNATIVE_MODEL_AUDIT.md`

Current NC postcrack/compactness audit:

7. `semantic_v2/20_theory/20260822_1440__NZSCCM__NC_TC_R1_COMPACTNESS_FAIL_TC_R2_REDUCTION_AND_STEEL_ACTIVESET_AUDIT.md`

Current Z6 execution:

8. `semantic_v2/40_execution/20260822_1440__NZSCCM__Z6_TC_R2_S0_AND_GENERAL_S_STEEL_ACTIVESET_DIAGNOSTIC.md`

Direct no-quadrature reproduction:

9. `semantic_v2/40_execution/steel_shell/20260822_1440__NZSCCM__Z6_TC_R2_DIRECT_ENDPOINT_AND_S0PLUS_LIMIT_SOLVER.py`

Current result summary:

`current/results/NZ_SCCM_POST_7GATE_STRUCTURAL_RERUN_CURRENT_20260822.md`

---

## 2. Normal concrete axis/source identities

```text
NC_COMPRESSION_BACKBONE = SAENZ_RETAINED_FOR_SWARTZ_RANGE
NC_SWARTZ_COMPRESSION_STRENGTH = 0.85_FCYL_SOURCE_IN_SITU_PANEL_STRENGTH
NC_SWARTZ_SPECIMEN_FT = SOURCE_OPEN
NC_CC_CAPACITY = NGUYEN/FOSTER-KUPFER SOURCE ENVELOPE / PASS_G6
NC_TC_CRACKING_BOUNDARY = NGUYEN_EQ318_319 / SOURCE TRANSITION MARKER
LITERAL_NGUYEN_POSTCRACK_TC = OFF_MAINLINE_ORACLE
```

The Nguyen TC envelope remains a cracking/state-transition marker and is not treated as the final steel-shell ultimate cap.

---

## 3. TC-R1 compactness result

The prior memoryless TC-R1 local map is no longer the current general-s production candidate.

For affine through-thickness material coordinates:

- T5 contributes an [8/8] rational function in z;
- the TC-R1 shifted-peak Saenz branch reduces symbolically to a rational function with numerator degree 5 and denominator degree 8 in z.

An exact section implementation would therefore require an opaque eighth-degree root/primitive compiler.

```text
TC_R1_LOCAL_MEMORYLESS_MAP = HISTORICAL_PASS_CANDIDATE
TC_R1_GENERAL_S_COMPACTNESS = FAIL
TC_R1_GENERAL_S_PRODUCTION = RETIRED
TC_R1_OLD_Z6_S0_50_22069 = HISTORICAL_PROVENANCE_ONLY
```

---

## 4. Current NC TC candidate = TC-R2

TC-R2 uses a smaller source-transparent current law:

### Tension

Finite Foster/Nguyen piecewise tension with

\[
\alpha_1=10,
\qquad
\alpha_2=0.3
\]

where `alpha2=0.3` is declared as the conservative project choice within the source range, not a structural Pu fit.

### Compression softening

\[
\widehat\varepsilon_t
=\frac{\varepsilon_t+\nu\varepsilon_c}{1-\nu^2}
=\varepsilon_0\lambda_t,
\]

\[
\gamma_c(\lambda_t)
=\min\left(1,\frac1{0.8+0.34\lambda_t}\right).
\]

### Compression current law

The fixed uniaxial NC compression backbone is scaled directly:

\[
\boxed{
\sigma_c^{TC}(\lambda_t,\lambda_c)
=\gamma_c(\lambda_t)\sigma_{c0}(\lambda_c).
}
\]

This is a declared `PROJECT-DERIVED CURRENT-STRENGTH REDUCTION`, not literal Nguyen.

For

\[
\lambda_t(z)=\lambda_{t0}+\nu_c\chi z,
\qquad
\lambda_c(z)=\lambda_{c0}+\chi z,
\]

all material fronts are affine in z. Required concrete/web primitives reduce to polynomial, linear/quadratic rational, factored linear×quadratic rational, logarithmic and arctangent forms.

```text
NC_TC_R2_MATERIAL_7GATE = PASS_CANDIDATE
TC_R2_GENERAL_S_CONCRETE_WEB_COMPACTNESS = PASS
NC_TC_R2_PRODUCTION_FREEZE = PENDING_STEEL_PHASE_GATE
```

---

## 5. Selected Swartz RC working status

No specimen-specific Swartz tensile data were found in the current source set, so the selected RC numerical table remains a working diagnostic under the transparent common `ft` assumption rather than specimen-source-closed production values.

|Case|1D / kN|2D working / kN|Pf / kN|
|---:|---:|---:|---:|
|1|567.712|495.989|490.194|
|2|561.638|501.025|506.652|
|9|515.424|515.424|625.865|
|10|534.711|534.711|696.147|
|19|339.177|339.177|377.654|
|20|335.013|335.013|372.761|
|21|350.460|350.460|368.313|
|22|351.679|351.679|355.858|

TC-R2 has not yet been propagated through this RC table; no old RC value is silently relabelled as a TC-R2 result.

---

## 6. UHPC current state — unchanged

```text
UHPC_COMPRESSION_BACKBONE = ZHANG_2023
HU_WENXU = HISTORICAL_UNIAXIAL_COMPARATOR_ONLY
UHPC_TENSION_BACKBONE = HIEW_2024
UHPC_CC_CAPACITY = LIU2024_SOURCE_MIN_PROJECT_REDUCTION
UHPC_TC_CT_CAPACITY = LIU2024_SEQUENTIAL_CONSERVATIVE_ENVELOPE
UHPC_TT_CAPACITY = LIU2024_UNIAXIAL_TENSILE_CAP
```

Current post-7gate results remain:

|Case|Current 2D / MN|
|---|---:|
|T120|12.22252|
|T360|11.36533|
|BH005|2.42351|
|BH010|4.46632|
|BH020|8.21925|
|BH032|11.21046|
|BH050|12.77154|

---

## 7. Z0–Z6 Nguyen-source TC transitions remain solved

|Case|P_TC-transition / MN|
|---|---:|
|Z0|27.033151885|
|Z1|17.093528920|
|Z2|27.033151885|
|Z3|36.744639968|
|Z4|56.203522296|
|Z5|10.747333454|
|Z6|23.832330467|

These remain source cracking markers, not final Pu.

---

## 8. Z6 TC-R2 direct finite results

### Symmetric s=0 endpoint

Uniform section + web compression-yield boundary gives

\[
\lambda_t=0.72375111146,
\quad
\lambda_c=-0.79066099525,
\]

\[
q=0.012018755437,
\]

\[
\boxed{P_{Z6,s=0}^{TC-R2}=50.1863826545\ \mathrm{MN}}.
\]

### Asymmetric s→0+ face-yield limit

A separate uniform, no-quadrature limiting system gives

\[
\lambda_t\approx0.53638962,
\quad
\lambda_c\approx-0.63294763,
\]

\[
q\approx0.01163665,
\]

\[
\boxed{P_{Z6,s\to0^+}^{face-yield}=48.9055510040\ \mathrm{MN}}.
\]

At this limit the face elastic trial state has \(\sigma_{VM}=355\) MPa and the equivalent web remains elastic.

A local implicit-function audit gives

\[
P_{terminal}(s)
=48.9055510+4.68s+O(s^2)\ \mathrm{MN}
\]

as \(s\to0^+\), so the asymmetric terminal family exists locally and rises from the limit.

```text
Z6_TC_R2_S0_ENDPOINT = RESOLVED_CANDIDATE
Z6_TC_R2_S0PLUS_LOCAL_LIMIT = RESOLVED_CANDIDATE
Z6_TC_R2_GLOBAL_S_MINIMUM = OPEN
```

---

## 9. New current blocker = steel phase active-set topology

An explicitly off-mainline numerical-through-thickness diagnostic was used only to diagnose general-s topology. It is not a formal integration method and its spatially integrated values are not adopted as Pu.

It shows that for finite \(s>0\), one face can be capped while the second remains elastic. When the second face reaches the radial cap, the assumed doubly-capped continuation may point immediately back across the active surface. As \(s\to0^+\), this terminal family approaches `48.905551 MN`, whereas the exactly symmetric `s=0` doubly-capped branch can continue to the later web-yield endpoint `50.186383 MN`.

```text
STEEL_FACE_CURRENT_LAW = MEMORYLESS PLANE-STRESS ELASTIC-PERFECTLY-PLASTIC RADIAL CAP
STEEL_FACE_ACTIVESET_NONUNIFORM_LIMIT = IDENTIFIED
GENERAL_S_FINAL_Z_PU = OPEN
```

Changing the NC concrete law again does not remove this steel-phase obstruction.

---

## 10. Constitutive pivot governance

Cedolin–Mulas remains an NC alternative, but is deferred because the concrete primitive problem is now compact under TC-R2 while the active blocker is the steel phase.

Next hard gate:

\[
\boxed{\text{STEEL-FACE SOURCE CONSTITUTIVE AUDIT}.}
\]

Required decision:

1. if the governing steel source supports a monotonic hardening/deformation-theory current law, derive it explicitly and re-audit the active set without fitting any structural comparator;
2. if the source is genuinely ideal elastic-perfectly-plastic, retain it and treat the nonuniform limit as an explicit theoretical limitation/feature rather than inventing hardening;
3. do not select Ramberg–Osgood or bilinear hardening parameters from Z6/Zhou/Winter/FEM/experiment.

```text
CEDOLIN_MULAS_1984 = DEFERRED_NC_ALTERNATIVE
NEXT_TASK = STEEL_FACE_SOURCE_AUDIT
Z0_Z6_FINAL_POSTCRACK_2D_PU = OPEN
```
