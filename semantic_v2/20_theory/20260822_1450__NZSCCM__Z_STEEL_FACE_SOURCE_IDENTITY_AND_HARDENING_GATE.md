# NZ-SCCM — Z steel-face source identity and hardening gate

**Date:** 2026-08-22 14:50 +08:00  
**Status:** `SOURCE_AUDIT_EXECUTED / NO_SOURCE_HARDENING_IDENTIFIED / PERFECT_PLASTIC_CURRENT_LAW_RETAINED / NO_TUNED_REPAIR`

## 0. Purpose

The 14:40 TC-R2 general-s audit showed that the remaining Z6 obstruction is the external-steel active-set topology, not the NC concrete primitive family. This file checks whether the current source chain actually authorizes a steel hardening law that could replace the memoryless ideal-plastic radial cap.

No Z6/Zhou/Winter/FEM/experiment value is used to identify a steel parameter.

---

# 1. Current Z steel material inputs

The current Z0–Z6 raw/representative input chain provides steel properties of the form

\[
E_s,\qquad \nu_s,\qquad f_y,
\]

with case-dependent \(f_y\) and no independent tangent modulus, ultimate stress, plastic strain table or Ramberg–Osgood parameters.

For Z6:

\[
E_s=206000\ \mathrm{MPa},
\qquad \nu_s=0.30,
\qquad f_y=355\ \mathrm{MPa}.
\]

The current explicit Z section capacity also uses \(f_y\) as an ideal plastic strength quantity.

```text
Z_STEEL_SOURCE_INPUT_HAS_HARDENING_MODULUS = NO
Z_STEEL_SOURCE_INPUT_HAS_ULTIMATE_STRESS_STRAIN_CURVE = NO
Z_STEEL_SOURCE_INPUT_HAS_RAMBERG_OSGOOD = NO
```

---

# 2. Historical successful Z6 nonlinear steel current map

The locked historical Z6 calculation ledger explicitly records the later nonlinear current operators as:

### Outer faces

Plane-stress elastic trial followed by the path-independent radial cap

\[
\sigma_{VM}^{tr}
=\sqrt{(\sigma_x^{tr})^2-\sigma_x^{tr}\sigma_y^{tr}+(\sigma_y^{tr})^2+3(\tau^{tr})^2},
\]

\[
g_f=\min\left(1,\frac{f_y}{\sigma_{VM}^{tr}}\right),
\]

\[
\boxed{\boldsymbol\sigma_f=g_f\boldsymbol\sigma^{tr}}.
\]

### Longitudinal web

\[
\boxed{
\sigma_y^w=\operatorname{clip}(E_s\varepsilon_y^w,-f_y,+f_y).
}
\]

with zero ideal-plastic tangent outside the elastic interval.

The historical ledger itself calls the face law a `path-independent radial cap current map`; it is a project current-law closure built from the steel elastic constants and yield stress, not a recovered hardening curve from Zhou.

```text
Z_FACE_CURRENT_MAP = MEMORYLESS_PLANE_STRESS_RADIAL_CAP
Z_WEB_CURRENT_MAP = 1D_ELASTIC_PERFECTLY_PLASTIC_CLIP
HARDENING_IN_HISTORICAL_SUCCESSFUL_Z6 = NONE
```

---

# 3. Related Q355 Abaqus material is not evidence for hardening either

The separately audited UCFT Abaqus Q355-355 material contains:

```text
Elastic: (206000 MPa, 0.30)
Plastic: one row only -> (355 MPa, 0 plastic strain)
Hardening flag: isotropic
```

A one-row Abaqus plastic table supplies first yield but no positive post-yield hardening slope. This model family is not the governing source for the Zhou Z0–Z6 analytical set, but it confirms that there is no hidden measured Q355 hardening curve in the currently audited project material inventory.

---

# 4. Historical Ramberg–Osgood values are not source data

Older UCFT planning text contains provisional values such as

\[
p=0.0005,\qquad n=10,
\]

but the same text explicitly states that these are temporary engineering assumptions **if the user has not supplied R–O parameters**, and must be replaced by measured Q355 stress–strain data when available.

Therefore they cannot be promoted into the current Z production theory merely to remove the active-set discontinuity.

```text
HISTORICAL_RO_P_0_0005_N_10 = ENGINEERING_ASSUMPTION_NOT_SOURCE
USE_RO_TO_REPAIR_Z6 = PROHIBITED_WITHOUT_NEW_SOURCE
```

---

# 5. Seven-gate steel verdict

For the currently available Z source contract:

|Item|Verdict|
|---|---|
|elastic constants|SOURCE-CLOSED|
|yield stress|SOURCE-CLOSED|
|ideal-plastic strength model|compatible with current source data / historical current map|
|post-yield hardening slope|SOURCE-OPEN / unavailable|
|Ramberg–Osgood parameters|not source-closed|
|using comparator to choose hardening|PROHIBITED|

Hence the 14:40 active-set nonuniformity cannot be repaired by inventing a small hardening modulus while still claiming the seven-gate source discipline.

---

# 6. Consequence for the Z6 calculation

The current mathematically honest options are now:

1. retain the ideal-plastic radial-cap/current law and solve/certify its continuous-s active-set limit structure; or
2. obtain a genuine steel stress–strain source and then rebuild the steel current operator from that source.

Option 1 is the only immediately source-closed route with present inputs.

Thus:

```text
STEEL_HARDENING_REPAIR = NOT_AUTHORIZED_BY_CURRENT_SOURCE
STEEL_IDEAL_PLASTIC_CURRENT_LAW = RETAINED
Z6_S0PLUS_48_905551_LIMIT = NOT_REMOVED_BY_TUNING
NEXT_TASK = FORMAL_GENERAL_S_ACTIVESET_ENVELOPE_AND_GLOBAL_MINIMUM_CERTIFICATE
```

Cedolin–Mulas or another NC concrete replacement is not the next rational action because it does not alter this steel active-set topology.

---

# 7. Formal boundary remains

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_material_points = 0
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
```
