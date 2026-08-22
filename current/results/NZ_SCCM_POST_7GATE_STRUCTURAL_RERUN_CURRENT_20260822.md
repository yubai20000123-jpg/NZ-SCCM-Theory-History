# NZ-SCCM — Post-7Gate Structural Rerun Current Summary

**Updated:** 2026-08-22 14:50 +08:00  
**Status:** `SUHPC RESOLVED / TC_R2 COMPACT NC CANDIDATE / Z6 DIRECT S0 + S0PLUS LIMIT RESOLVED / STEEL SOURCE AUDIT CLOSED / GLOBAL Z Pu OPEN`

Current detailed files:

1. `semantic_v2/20_theory/20260822_1440__NZSCCM__NC_TC_R1_COMPACTNESS_FAIL_TC_R2_REDUCTION_AND_STEEL_ACTIVESET_AUDIT.md`
2. `semantic_v2/40_execution/20260822_1440__NZSCCM__Z6_TC_R2_S0_AND_GENERAL_S_STEEL_ACTIVESET_DIAGNOSTIC.md`
3. `semantic_v2/40_execution/steel_shell/20260822_1440__NZSCCM__Z6_TC_R2_DIRECT_ENDPOINT_AND_S0PLUS_LIMIT_SOLVER.py`
4. `semantic_v2/20_theory/20260822_1450__NZSCCM__Z_STEEL_FACE_SOURCE_IDENTITY_AND_HARDENING_GATE.md`

---

## 1. SUHPC current post-7gate results — unchanged

| Case | Zhang 1D / MN | Current 2D / MN |
|---|---:|---:|
|T120|12.41101|12.22252|
|T360|11.36533|11.36533|
|BH005|2.42351|2.42351|
|BH010|4.46632|4.46632|
|BH020|8.21925|8.21925|
|BH032|11.21046|11.21046|
|BH050|13.67770|12.77154|

---

## 2. Z0–Z6 Nguyen TC transition markers — retained, not Pu

|Case|P_TC-transition / MN|
|---|---:|
|Z0|27.033151885|
|Z1|17.093528920|
|Z2|27.033151885|
|Z3|36.744639968|
|Z4|56.203522296|
|Z5|10.747333454|
|Z6|23.832330467|

These are cracking/state-transition markers. Nguyen enters cracked constitutive continuation after them.

```text
TC_ENVELOPE_AS_FINAL_SC_PU = REJECTED
OLD_Z6_51_345 = SUPERSEDED
```

---

## 3. NC postcrack candidate change

Literal Nguyen TC/TCX remains off-mainline because it requires crack/history variables.

The earlier memoryless TC-R1 is also retired from general-s production because:

- T5 becomes an [8/8] rational function of affine thickness coordinate z;
- the TC-R1 shifted-peak softened Saenz branch becomes degree-5 / degree-8 rational in z;
- exact integration would require an opaque eighth-degree primitive/compiler layer.

Current candidate `TC-R2` instead uses:

- literal finite Foster/Nguyen piecewise tension (`alpha1=10`, declared project `alpha2=0.3`);
- Poisson-free material-coordinate transverse tension;
- Nguyen/MCFT current softening amplitude
  \[
  \gamma_c=\min[1,(0.8+0.34\lambda_t)^{-1}];
  \]
- fixed NC compression backbone scaled directly:
  \[
  \sigma_c^{TC}=\gamma_c\sigma_{c0}(\lambda_c).
  \]

For affine \(\lambda_t(z),\lambda_c(z)\), branch fronts are linear and the required concrete/web moments use only a small finite set of polynomial/log/arctan rational primitives.

```text
TC_R1_GENERAL_S_PRODUCTION = RETIRED
NC_TC_R2_MATERIAL_7GATE = PASS_CANDIDATE
TC_R2_GENERAL_S_CONCRETE_WEB_COMPACTNESS = PASS
```

---

## 4. Z6 direct no-quadrature TC-R2 candidates

### Exactly symmetric s=0

Uniform phase equilibrium plus web compression yield:

\[
\lambda_t=0.72375111146,
\quad
\lambda_c=-0.79066099525,
\]

\[
q=0.012018755437,
\]

\[
\boxed{P_{s=0}=50.1863826545\ \mathrm{MN}}.
\]

### Asymmetric s→0+ second-face-yield limit

A separate uniform limiting root, with web elastic and face elastic trial exactly at von-Mises yield, gives

\[
\lambda_t\approx0.53638962,
\quad
\lambda_c\approx-0.63294763,
\]

\[
q\approx0.01163665,
\]

\[
\boxed{P_{s\to0^+}=48.9055510040\ \mathrm{MN}}.
\]

At the limit:

\[
(\sigma_x^s,\sigma_y^s)
\approx(+182.772,-226.373)\ \mathrm{MPa},
\qquad
\sigma_{VM}=355\ \mathrm{MPa}.
\]

A local implicit-function audit gives

\[
P_{terminal}(s)=48.9055510+4.68s+O(s^2)\ \mathrm{MN},
\]

so the asymmetric terminal branch exists locally and rises away from the boundary.

```text
Z6_TC_R2_S0_ENDPOINT = 50.1863826545 MN / DIRECT CANDIDATE
Z6_TC_R2_S0PLUS_LIMIT = 48.9055510040 MN / DIRECT LOCAL-LIMIT CANDIDATE
Z6_GLOBAL_GENERAL_S_PU = OPEN
```

---

## 5. Off-mainline general-s diagnostic and steel active-set issue

A high-order thickness-integration calculation was used only as an **OFF_MAINLINE diagnostic**, never as the formal operator. It reproduces the approach to the direct boundary limit:

|s|second-face terminal diagnostic / MN|
|---:|---:|
|0.020|49.00288|
|0.010|48.95329|
|0.005|48.92919|
|0.001|48.91024|
|0.00001|48.90560|

At a representative `s≈0.444855`, first web-edge yield occurs near `48.72244 MN` but partial web yielding continues; second outer-face yield occurs near `51.67326 MN` and forms a terminal active-set kink for that fixed s.

The nonuniformity is between:

- the exactly symmetric doubly-capped `s=0` branch, and
- the arbitrarily-small-asymmetry second-face terminal family.

No diagnostic spatial integration value is adopted as final Pu.

---

## 6. Steel source audit — closed

The available Z steel source contract provides only

\[
E_s,\quad \nu_s,\quad f_y,
\]

with no post-yield tangent, ultimate stress/strain curve or Ramberg–Osgood parameters.

The historical successful Z6 current law is itself:

- face: plane-stress elastic trial + path-independent von-Mises radial cap;
- web: elastic-perfectly-plastic clip.

Related audited UCFT `Q355-355` Abaqus material also has only one plastic row `(355 MPa, 0 plastic strain)`, i.e. no positive hardening slope. Historical `p=0.0005, n=10` R–O numbers were explicitly temporary engineering assumptions and are not admissible source data.

Therefore:

```text
Z_STEEL_SOURCE_HARDENING = NOT_AVAILABLE
INVENT_HARDENING_TO_REPAIR_Z6 = PROHIBITED
STEEL_IDEAL_PLASTIC_CURRENT_LAW = RETAINED
```

Changing NC concrete to Cedolin–Mulas would not remove the current steel active-set topology.

---

## 7. Current next task

The remaining formal task is:

\[
\boxed{\text{TC-R2 continuous general-s active-set envelope + global-minimum certificate}.}
\]

It must use the compact finite TC-R2 primitives and finite active-set equations, with zero formal spatial quadrature/material points.

Until that is complete:

```text
Z0_Z6_FINAL_POSTCRACK_2D_PU = OPEN
```

---

## 8. Formal flags

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
