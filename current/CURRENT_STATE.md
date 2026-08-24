# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-24 11:51 +08:00  
**Status:** `MARGUERRE_AIRY_EXPLICIT / Ny_My_RESULTANT_TERMINAL / R13_FHWA_DESIGN_ROLE_CLOSED / R14_ZHANG_PHYSICAL_PEAK_COMPLETE / PRIMARY6_MEAN_PLUS1P392 / ZERO_THICKNESS_QUADRATURE / BLANKET_TC_NOT_AUTHORIZED / TC_ACTIVATION_AUDIT_NEXT / USER_ACCEPTANCE_PENDING`

> This entry supersedes the earlier 2026-08-24 R12 entry. The repository-wide mainline has now advanced through the FHWA design-vs-physical source-role audit and the Zhang peak-anchored strain-compatible `Ny-My` rerun.

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
HISTORY_STATE_MACHINE = OFF_MAINLINE
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
STRUCTURAL_BACKBONE_CHANGED = FALSE
```

Current production-development sequence:

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

Do not reopen the structural front merely because the material/capacity representation of the terminal changes.

---

## 1. Current source-of-truth chain

### R09 — cross-family resultant diagnosis

`semantic_v2/40_execution/20260824_0950__NZSCCM__CROSS_FAMILY_NY_MY_RESULTANT_DIAGNOSIS_R09.md`

Locked decision:

```text
MARGUERRE_AIRY_STRUCTURAL_FRONT = RETAIN
Ny_My_TERMINAL_IDENTITY = RETAIN
POINTWISE_MATERIAL_OPERATOR = DO_NOT_REOPEN
NEXT_RESEARCH_OBJECT = RESULTANT_CAPACITY_LAW
```

### R10 — FHWA `alpha_u=0.85` screening block

`semantic_v2/40_execution/20260824__NZSCCM__UHPC_RESULTANT_COMPRESSION_BLOCK_SOURCE_GATE_R10.md`

Primary six higher-confidence cases:

```text
mean signed = -0.668 percent
MAE = 2.534 percent
RMSE = 2.597 percent
```

R10-A remains a high-value design/screening baseline, not the current physical material law.

### R11 — exact FHWA strain-compatible compression design section

Report:

`semantic_v2/40_execution/20260824_1040__NZSCCM__FHWA_EXACT_STRAIN_COMPATIBLE_NY_MY_ENVELOPE_R11.md`

Reproducer:

`semantic_v2/40_execution/steel_shell/20260824_1040__NZSCCM__FHWA_EXACT_STRAIN_COMPATIBLE_NY_MY_R11.py`

Primary six:

```text
mean signed = -4.218 percent
MAE = 4.218 percent
RMSE = 4.408 percent
```

### R12 — UHPC tension activation gate

`semantic_v2/40_execution/20260824__NZSCCM__UHPC_TENSION_ACTIVATION_GATE_R12.md`

All seven R11 roots remain fully compressive through the UHPC core. Hiew tension is therefore inactive and cannot explain the R11 low bias.

### R13 — FHWA design-vs-physical source-role gate

`semantic_v2/40_execution/20260824_1151__NZSCCM__FHWA_DESIGN_VS_PHYSICAL_COMPRESSION_ROLE_GATE_R13.md`

Official FHWA-HRT-23-077 identity:

- `alpha_u` is a source-supported reduction for UHPC compressive-response nonlinearity;
- Article 1.4.2.4.3 is explicitly a **Compression Design Model**;
- the elastic-to-`alpha_u f'c` plateau is retained as a design idealization;
- it is not assigned the stronger identity of the unique measured physical peak constitutive curve for nonlinear test/FEM peak comparison.

Decision:

```text
FHWA_R11_R12 = RETAIN_AS_DESIGN_BASELINE
FHWA_R11_R12_AS_PHYSICAL_PRODUCTION_TERMINAL = REJECT
ZHANG_PHYSICAL_REINSERTION = AUTHORIZED
```

### R14 — Zhang peak-anchored exact strain-compatible `Ny-My`

Report:

`semantic_v2/40_execution/20260824_1151__NZSCCM__ZHANG_PEAK_STRAIN_COMPATIBLE_NY_MY_R14.md`

Reproducer:

`semantic_v2/40_execution/steel_shell/20260824_1151__NZSCCM__ZHANG_PEAK_STRAIN_COMPATIBLE_NY_MY_R14.py`

Results:

`semantic_v2/40_execution/steel_shell/20260824_1151__NZSCCM__ZHANG_PEAK_STRAIN_COMPATIBLE_NY_MY_R14_RESULTS.csv`

R14 uses the source-registered Zhang-2023 zero-confinement ascending compression backbone with one common plane-section strain field and the extreme UHPC compression fibre anchored at

\[
\varepsilon_{top}=\varepsilon_{c0}=0.0035.
\]

This is a first-attainment-of-material-peak terminal. Zhang post-peak continuation is source-retained but not silently activated because the current mainline has no load-path/post-peak continuation state machine.

---

## 2. Current R14 steel-shell UHPC results

|Case|R14 Pu / MN|Comparator / MN|Error|
|---|---:|---:|---:|
|T120|12.25216|12.6378|-3.051%|
|T360|11.13326|10.9688|+1.499%|
|BH005|2.42237|2.3558|+2.826%|
|BH010|4.46204|4.3043|+3.665%|
|BH020|8.15535|8.0076|+1.845%|
|BH032|11.16306|10.9905|+1.570%|
|BH050|13.65045|12.2198*|+11.708%|

`*` BH050 retains its lower-confidence comparator identity and is excluded from primary-six statistics.

Primary six:

\[
\boxed{\text{mean signed}=+1.392\%},
\]

\[
\boxed{MAE=2.409\%,\qquad RMSE=2.544\%}.
\]

This removes the R11/R12 systematic low bias while keeping the structural front unchanged and using no comparator in parameter/root selection.

---

## 3. R14 exactness and control-location status

```text
R14_FORMAL_SPATIAL_QUADRATURE = 0
R14_THICKNESS_QUADRATURE = 0
R14_MATERIAL_POINTS = 0
R14_UHPC_ASCENDING_PRIMITIVES = FINITE_HYPERGEOMETRIC_ENDPOINTS
R14_STEEL_PRIMITIVES = FINITE_CLIPPED_AFFINE
R14_CONTROL_s = 1 FOR ALL 7
R14_INTERIOR_STATIONARY_ROOT_PRECEDENCE = NONE_FOUND
R14_UHPC_TENSION = INACTIVE_AT_ALL 7 ROOTS
```

All `s=0` pure-axial candidates occur after the `s=1` roots.

---

## 4. Material-role identities now locked

```text
UHPC_PHYSICAL_UNIAXIAL_COMPRESSION_BACKBONE = ZHANG_2023
UHPC_FHWA_085_COMPRESSION = DESIGN_BASELINE / SCREENING ROLE
UHPC_TENSION_SOURCE = HIEW_2024
UHPC_TC_CT_SOURCE_EVIDENCE = LIU / LEUTBECHER FAMILY
UHPC_ZHANG_POSTPEAK = SOURCE_RETAINED / OFF_MAINLINE_CONTINUATION
HU_WENXU = HISTORICAL_UNIAXIAL_COMPARATOR_ONLY
```

The R14 peak terminal does not abolish the Zhang descending branch; it only prevents a post-peak continuation from being silently imported into a no-load-path theory.

---

## 5. Ordinary-concrete branch status

The Aug-22 NC TC-R2 and Z6 active-set work remains retained as ordinary-concrete branch provenance. It is not the repository-wide next task and does not override R14.

No NC material law is reopened by R13/R14.

---

## 6. Next task

A blanket TC compression-softening multiplier is not authorized.

Reason:

- R14 primary-six mean is already only `+1.392%`;
- T120 is already low by `-3.05%`;
- other primary cases are modestly high by about `+1.5%` to `+3.7%`.

A universal TC reduction would therefore mix physically different states and would worsen at least T120.

The next task is a **source/state activation audit**, not coefficient fitting:

\[
\boxed{
\text{transverse Marguerre--Airy state}
\rightarrow
\text{is a Liu/Leutbecher TC reduction physically active at the R14 control section?}
}
\]

This gate must be evaluated case by case using the existing Airy transverse demand/state. It may activate no TC reduction for some cases and a finite source-supported reduction for others. No structural-load calibration is permitted.

```text
NEXT_TASK = TRANSVERSE_AIRY_STATE_TO_TC_ACTIVATION_AUDIT
BLANKET_TC_SOFTENING = PROHIBITED
NEW_FITTED_FACTOR = PROHIBITED
STRUCTURAL_FRONT_REOPEN = NO
USER_ACCEPTANCE = PENDING
```
