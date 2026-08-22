# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-22 14:50 +08:00  
**Status:** `MARGUERRE_AIRY_EXPLICIT / SUHPC_2D_RESOLVED / NC_TC_R1_GENERAL_S_RETIRED / NC_TC_R2_COMPACT_CANDIDATE / Z6_S0_AND_S0PLUS_LIMIT_RESOLVED / STEEL_SOURCE_AUDIT_NO_HARDENING / Z_GLOBAL_PU_OPEN / GENERAL_S_ACTIVESET_CERT_NEXT / USER_ACCEPTANCE_PENDING`

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

Current steel source audit:

10. `semantic_v2/20_theory/20260822_1450__NZSCCM__Z_STEEL_FACE_SOURCE_IDENTITY_AND_HARDENING_GATE.md`

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

The prior memoryless TC-R1 map is retired for general-s production.

For affine through-thickness material coordinates:

- T5 contributes an [8/8] rational function in z;
- the TC-R1 shifted-peak Saenz branch reduces symbolically to a rational function with numerator degree 5 and denominator degree 8 in z.

An exact implementation would therefore require an opaque eighth-degree root/primitive compiler.

```text
TC_R1_LOCAL_MEMORYLESS_MAP = HISTORICAL_PASS_CANDIDATE
TC_R1_GENERAL_S_COMPACTNESS = FAIL
TC_R1_GENERAL_S_PRODUCTION = RETIRED
TC_R1_OLD_Z6_S0_50_22069 = HISTORICAL_PROVENANCE_ONLY
```

---

## 4. Current NC TC candidate = TC-R2

TC-R2 uses a smaller source-transparent current law.

### Tension

Finite Foster/Nguyen piecewise tension with

\[
\alpha_1=10,
\qquad
\alpha_2=0.3
\]

where `alpha2=0.3` is a declared conservative project choice within the Foster source range, not a structural-load fit.

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
NC_TC_R2_PRODUCTION_FREEZE = PENDING_GLOBAL_SECTION_CERTIFICATE
```

---

## 5. Selected Swartz RC working status

No specimen-specific Swartz tensile data were found in the current source set, so the selected RC numerical table remains a working diagnostic under the transparent common ft assumption rather than specimen-source-closed production values.

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

as \(s\to0^+\).

```text
Z6_TC_R2_S0_ENDPOINT = RESOLVED_CANDIDATE
Z6_TC_R2_S0PLUS_LOCAL_LIMIT = RESOLVED_CANDIDATE
Z6_TC_R2_GLOBAL_S_MINIMUM = OPEN
```

---

## 9. Steel source audit — completed

The current Z source chain supplies

\[
E_s,\quad \nu_s,\quad f_y
\]

but no post-yield tangent, ultimate stress/strain curve or Ramberg–Osgood parameters.

The historical successful Z6 nonlinear steel current map itself is:

- external faces: plane-stress elastic trial + path-independent von-Mises radial cap;
- equivalent web: one-dimensional elastic-perfectly-plastic clip.

No hardening parameter is present.

Related audited UCFT Abaqus `Q355-355` also contains only one plastic row `(355 MPa, 0 plastic strain)`, so it supplies first yield but no positive hardening slope. It is not the governing Zhou Z-source, but confirms there is no hidden measured hardening table in the currently audited project material inventory.

Historical provisional R–O values `p=0.0005, n=10` are explicitly documented as engineering assumptions to be used only when actual parameters are absent. They are therefore not admissible as a source-grounded repair of Z6.

```text
Z_STEEL_SOURCE_HARDENING = NOT_AVAILABLE
Z_FACE_CURRENT_MAP = MEMORYLESS_IDEAL_PLASTIC_RADIAL_CAP
Z_WEB_CURRENT_MAP = IDEAL_PLASTIC_CLIP
INVENT_HARDENING_TO_REMOVE_ACTIVESET_LIMIT = PROHIBITED
```

Hence changing the NC concrete law again or introducing an arbitrary small hardening modulus is not justified by the current source chain.

---

## 10. Current blocker and next action

An off-mainline numerical-through-thickness diagnostic identified a nonuniform active-set limit: for finite s>0 the second-face radial-yield terminal family approaches `48.905551 MN` as s→0+, while the exactly symmetric s=0 doubly-capped branch can continue to the later web-yield endpoint `50.186383 MN`.

The s→0+ value itself is already a direct finite no-quadrature root; what remains unproven is whether the corresponding terminal family is the global minimum over the entire continuous interval `0<s<=1`.

Therefore the next task is no longer another constitutive-model search. It is:

\[
\boxed{\text{formal TC-R2 general-s active-set envelope + global-minimum certificate}.}
\]

This certificate must use the compact TC-R2 primitive family and finite active-set equations; no formal spatial grid or quadrature is permitted.

```text
STEEL_SOURCE_AUDIT = CLOSED_NO_HARDENING
CEDOLIN_MULAS_1984 = DEFERRED_NC_ALTERNATIVE
NEXT_TASK = GENERAL_S_ACTIVESET_ENVELOPE_AND_GLOBAL_MINIMUM_CERTIFICATE
Z0_Z6_FINAL_POSTCRACK_2D_PU = OPEN
```
