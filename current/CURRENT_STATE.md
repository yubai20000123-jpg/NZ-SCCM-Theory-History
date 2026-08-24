# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-24  
**Status:** `MARGUERRE_AIRY_EXPLICIT / Ny_My_RESULTANT_TERMINAL / R11_FHWA_EXACT_COMPRESSION_COMPLETE / R12_UHPC_TENSION_INACTIVE / PRIMARY6_LOW_BIAS_PERSISTS / TC_SOFTENING_DEFERRED / R13_FHWA_DESIGN_VS_PHYSICAL_ROLE_GATE_NEXT / USER_ACCEPTANCE_PENDING`

> This file supersedes the 2026-08-22 14:50 current-state entry. The Aug-22 TC-R2 general-s certificate is no longer the repository-wide next task. It remains historical/provenance material for the ordinary-concrete branch.

## 0. Governing structural mainline — frozen

```text
STRUCTURAL_FRONT = FULL_2D_MARGUERRE_AIRY
TERMINAL_OBJECT = AXIAL_Y_NORMAL_Ny_My
Nx_Mx_IN_STRUCTURAL_FIELD = YES
Nx_Mx_HARD_TERMINAL_ON_Y_CUT = NO
FORMAL_SPATIAL_QUADRATURE = 0
THICKNESS_QUADRATURE = 0
MATERIAL_POINTS = 0
RITZ_ORDER = NONE
LOAD_PATH_TRACKING = 0
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
STRUCTURAL_BACKBONE_CHANGED = FALSE
```

The current production-development sequence is

\[
\boxed{
\text{full 2D Marguerre--Airy demand}
\rightarrow
\text{finite control-location audit}
\rightarrow
\text{strain-compatible }N_y-M_y\text{ section terminal}
\rightarrow
P_u.
}
\]

Do not reopen the structural front merely because a terminal material/capacity representation changes.

---

## 1. Current source-of-truth chain

### R09 — cross-family resultant diagnosis

`semantic_v2/40_execution/20260824_0950__NZSCCM__CROSS_FAMILY_NY_MY_RESULTANT_DIAGNOSIS_R09.md`

Decision:

```text
MARGUERRE_AIRY_STRUCTURAL_FRONT = RETAIN
Ny_My_TERMINAL_IDENTITY = RETAIN
POINTWISE_MATERIAL_OPERATOR = DO_NOT_REOPEN
NEXT_RESEARCH_OBJECT = RESULTANT_CAPACITY_LAW
```

### R10 — UHPC compression-block source gate

`semantic_v2/40_execution/20260824__NZSCCM__UHPC_RESULTANT_COMPRESSION_BLOCK_SOURCE_GATE_R10.md`

The R08 full-`fc` UHPC rectangle was demoted to upper-bound diagnostic. FHWA `alpha_u=0.85` was introduced as a source-specified design compression reduction, not fitted to panel loads.

R10-A rigid `0.85fc` screening block, primary six higher-confidence steel-shell UHPC cases:

```text
mean signed = -0.668 percent
MAE = 2.534 percent
RMSE = 2.597 percent
```

R10-A is a high-value screening baseline, not the final physical section law.

### R11 — exact FHWA strain-compatible compression section

Report:

`semantic_v2/40_execution/20260824_1040__NZSCCM__FHWA_EXACT_STRAIN_COMPATIBLE_NY_MY_ENVELOPE_R11.md`

Reproducer:

`semantic_v2/40_execution/steel_shell/20260824_1040__NZSCCM__FHWA_EXACT_STRAIN_COMPATIBLE_NY_MY_R11.py`

R11 replaces the rigid compression rectangle by one exact plane-section strain field:

\[
\varepsilon(y)=\varepsilon_{cu}-\kappa y,
\qquad \varepsilon_{cu}=0.0035,
\]

with FHWA UHPC compression `elastic -> 0.85fc plateau`, elastic-perfectly-plastic steel, retained Yun compression caps where applicable, and exact finite through-thickness primitives.

All seven current cases control at `s=1`; no earlier admissible interior stationary root was found.

### R12 — UHPC tensile-resultant activation gate

Report:

`semantic_v2/40_execution/20260824__NZSCCM__UHPC_TENSION_ACTIVATION_GATE_R12.md`

Reproducer:

`semantic_v2/40_execution/steel_shell/20260824__NZSCCM__UHPC_TENSION_ACTIVATION_GATE_R12.py`

Results:

`semantic_v2/40_execution/steel_shell/20260824__NZSCCM__UHPC_TENSION_ACTIVATION_GATE_R12_RESULTS.csv`

Hiew 2024 remains the admissible UHPC direct-tension source, but no Hiew fibre-family selection is required at the present roots because the entire UHPC core is still in compression.

---

## 2. R12 exact activation result

For the R11 section geometry,

\[
\kappa_t
=\frac{\varepsilon_{cu}}{t_c}
=\frac{0.0035}{42}
=8.333333333333\times10^{-5}\ \mathrm{mm}^{-1}
\]

is the first possible UHPC tensile-activation curvature.

Every controlling curvature satisfies

\[
\kappa_u<\kappa_t,
\]

with strictly positive bottom-core strain.

|Case|R12 Pu / MN|Comparator / MN|error|UHPC tension at root?|
|---|---:|---:|---:|---|
|T120|11.78605439|12.6378|-6.740%|NO|
|T360|10.65015268|10.9688|-2.905%|NO|
|BH005|2.25203558|2.3558|-4.405%|NO|
|BH010|4.13093221|4.3043|-4.028%|NO|
|BH020|7.66340795|8.0076|-4.298%|NO|
|BH032|10.66798371|10.9905|-2.935%|NO|
|BH050|13.25612091|12.2198*|+8.481%|NO|

`*` BH050 comparator retains its lower-confidence identity.

Primary six:

\[
\boxed{\text{mean signed}=-4.218\%},
\qquad
\boxed{MAE=4.218\%},
\qquad
\boxed{RMSE=4.408\%}.
\]

Therefore:

```text
R12_ROOTS_DIFFER_FROM_R11 = NO
UHPC_TENSION_OMISSION_EXPLAINS_R11_LOW_BIAS = REJECTED_FOR_CURRENT_7_CASES
```

---

## 3. Hiew source role after R12

Hiew 2024 remains the high-priority source for monotonic UHPC direct tension:

```text
elastic -> strain hardening -> peak -> localisation -> fibre-pullout softening
```

The 2% SL, HL and SL-HL series have materially different tensile strain coordinates. They may not be selected by matching T120/T360/BH structural ultimate loads.

For the current seven roots this ambiguity is dormant because the tensile branch contributes exactly zero.

---

## 4. TC compression softening — retained physically, deferred as next correction

Liu/Leutbecher evidence for UHPC tension-compression softening remains valid source evidence.

However, it is **not** the next error-correction step for the present steel-shell UHPC baseline because the primary six R11/R12 predictions are already systematically low. Applying another compression reduction before resolving the compression-model source role would move the bias in the wrong direction.

```text
LIU_LEUTBECHER_TC_PHYSICAL_EVIDENCE = RETAIN
TC_SOFTENING_AS_IMMEDIATE_ERROR_CORRECTION = NO
TC_SOFTENING_FORMAL_GATE = DEFERRED
```

---

## 5. Ordinary-concrete and RC branches

The Aug-22 NC/RC material-source audits remain retained as branch-specific provenance. They are not deleted or relabelled.

Important carried-forward identities include:

```text
NC_SWARTZ_COMPRESSION_STRENGTH = 0.85_FCYL_SOURCE_IN_SITU_PANEL_STRENGTH
NC_CC_CAPACITY = NGUYEN/FOSTER-KUPFER SOURCE ENVELOPE
NC_TC_CRACKING_BOUNDARY = NGUYEN_EQ318_319 SOURCE TRANSITION MARKER
Z_STEEL_SOURCE_HARDENING = NOT_AVAILABLE
Z_FACE_CURRENT_MAP = MEMORYLESS_IDEAL_PLASTIC_RADIAL_CAP
Z_WEB_CURRENT_MAP = IDEAL_PLASTIC_CLIP
```

Z6 remains a visible ordinary-concrete steel-shell outlier and is not silently repaired by UHPC terminal choices.

---

## 6. Current blocker and next action

R12 falsified the proposed missing-tension explanation. The strongest unresolved source-role question is now the status of the FHWA `alpha_u=0.85` compression reduction.

FHWA supplies a **design** compression model. The current comparators are physical Abaqus/structural-response values. Before adding another physical reduction, the project must establish whether the R11 terminal mixes design resistance and physical material response.

Next task:

\[
\boxed{
\text{R13 = FHWA }\alpha_u\text{ DESIGN-vs-PHYSICAL TERMINAL ROLE GATE}
}
\]

R13 execution contract:

1. do not reopen full 2D Marguerre-Air y;
2. do not reopen `Ny-My` terminal identity;
3. distinguish design resistance from physical constitutive/capacity response;
4. audit comparator identity before interpreting error sign;
5. if a physical compression law is required, insert a source-supported UHPC uniaxial compression law into the same exact strain-compatible section envelope;
6. no specimen-level calibration, no root selection from comparators;
7. formal spatial quadrature = 0;
8. thickness quadrature = 0;
9. material points = 0.

```text
CURRENT_RECOMMENDED_NEXT_TASK = R13_FHWA_ALPHA_U_DESIGN_VS_PHYSICAL_TERMINAL_ROLE_GATE
STRUCTURAL_FRONT_REOPEN = NO
Ny_My_TERMINAL_REOPEN = NO
NEW_FITTED_FACTOR = NO
USER_ACCEPTANCE = PENDING
```
