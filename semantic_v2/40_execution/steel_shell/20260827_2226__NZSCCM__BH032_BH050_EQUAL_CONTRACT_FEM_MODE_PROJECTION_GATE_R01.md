# NZ-SCCM — BH032 / equal-contract BH050 direct FEM out-of-plane mode projection gate R01

**Updated:** 2026-08-27 22:38 +08:00  
**Parent current state:** `current/SSUHPC_CURRENT_STATE_ADDENDUM_20260827_2052_KINEMATIC_CURVATURE_RESET.md`  
**Current projector:** `semantic_v2/40_execution/steel_shell/20260827_2238__NZSCCM__BH_FEM_OUT_OF_PLANE_MODE_PROJECTOR_R02.py`  
**Superseded first implementation:** `20260827_2226__NZSCCM__BH_FEM_OUT_OF_PLANE_MODE_PROJECTOR_R01.py`  
**Status:** `R02 PROJECTOR IMPLEMENTED / CANONICAL PEAK FRAMES FIXED / SAME-LOAD THEORY TARGETS FIXED / ODB BYTES NOT MOUNTED IN REMOTE RUNTIME / FEM q NOT FABRICATED`

---

## 0. Scope

This node executes the unique current kinematic gate as far as the available data permit, without changing Marguerre–Airy, common R06, terminal capacity contact, or any material parameter.

The requested observable is the global FEM out-of-plane displacement mode:

\[
U_{oop}^{FE}(x,y)\rightarrow W_d^{FE}\rightarrow q_{FE}=W_d^{FE}/b\rightarrow \kappa_{FE}^{geom}.
\]

The accepted canonical ODB contract fixes

```text
FE global X -> theory x
FE global Z -> theory y / loading direction
FE global Y -> theory out-of-plane direction
incremental out-of-plane displacement -> U2
steel-shell instance -> C-S-SHELL-1
step -> EXPLICIT_LOADING
```

The initial imperfection is encoded in the initial mesh, while `U2` is displacement from that imperfect configuration. Therefore the projector separately evaluates

```text
initial paired-face midsurface Y -> W0_FE -> q0_FE
peak incremental paired-face U2 -> Wd_FE -> q_FE
```

No initial imperfection is added to `q_FE`.

---

## 1. Canonical ODB and peak-frame identities recovered before execution

The project File Library confirms the current canonical family and field inventory:

```text
BH032 ODB = BH032_EXPLICIT_R02_GRID_B400.odb
BH050 ODB = BH050_EQUAL_CONTRACT_R02_GRID_B400.odb
step = EXPLICIT_LOADING
frames per ODB = 501
U field = AVAILABLE
shell instance = C-S-SHELL-1
```

It also fixes the actual accepted peak frames:

```text
BH032:
  P_FE = 10.990480 MN
  peak frame index = 262
  peak time = 2.6200008392334 s

BH050 equal-contract:
  P_FE = 12.591227 MN
  peak frame index = 212
  peak time = 2.1200006 s
```

The old special BH050 ODB remains excluded.

The same sources provide the local machine paths to both ODBs, but the multi-GB ODB binaries themselves are not mounted into the present ChatGPT/GitHub runtime and are not stored in GitHub. No archived nodal U2 table containing the full global shell field was found in File Library. Therefore actual `q_FE` cannot be evaluated here without fabricating data.

```text
ODB_IDENTITY = RESOLVED
PEAK_FRAME_IDENTITY = RESOLVED
U_FIELD_AVAILABILITY_IN_LOCAL_ODB = CONFIRMED
ODB_BYTES_IN_REMOTE_RUNTIME = NO
NODAL_U2_ARCHIVE_IN_REMOTE_RUNTIME = NO
```

This is a runtime/data-mount blocker only.

---

## 2. R02 read-only projector

R02 replaces the first implementation before any ODB result is accepted. It follows the existing canonical extraction discipline:

1. opens exactly one ODB `readOnly=True`;
2. addresses the frozen `C-S-SHELL-1` instance directly rather than scanning the full assembly;
3. reads only the specified certified peak frame instead of looping through all 501 field frames;
4. obtains displacement by
   `frame.fieldOutputs['U'].getSubset(region=C-S-SHELL-1)`;
5. identifies horizontal steel-face shell elements geometrically from undeformed normals (`|n_y|>=0.90` by default);
6. pairs outer TOP/BOTTOM face nodes at common FE `(X,Z)` coordinates;
7. forms
   \[
   Y_{mid,0}=\frac{Y_++Y_-}{2},\qquad
   U_{2,mid}=\frac{U_{2,+}+U_{2,-}}{2};
   \]
8. defines the frozen global mode on the actual FE span
   \[
   \phi=\sin\!\left(\pi\frac{X-X_{min}}{L_x^{FE}}\right)
   \sin\!\left(m_*\pi\frac{Z-Z_{min}}{L_z^{FE}}\right);
   \]
9. removes constant out-of-plane translation and linear X/Z tilt using the weighted basis `[1,X,Z,phi]`;
10. fixes the sign of `phi` from the initial imperfection projection, never from the favorable loaded response;
11. returns initial `W0_FE,q0_FE`, peak `Wd_FE,q_FE`, geometric curvatures, modal `R2`, RMS residual, and actual FE spans.

The weighting is diagnostic FEM data reduction only; it is not production-theory quadrature.

```text
FORMAL_STRUCTURAL_SPATIAL_QUADRATURE = 0
FORMAL_THICKNESS_QUADRATURE = 0
MATERIAL_POINTS = 0
FEM_POSTPROCESS_WEIGHTED_LS = DIAGNOSTIC_ONLY
THEORY_MODIFIED = NO
```

---

## 3. Same-load theory targets fixed independently of FEM displacement

The frozen Airy branch is

\[
P(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0),
\]

which is monotonic for `q>=0`. Therefore the correct primary kinematic comparator at an FEM peak is the theoretical amplitude at that **same load**, not only the theoretical terminal `q_u`.

### 3.1 BH032

```text
Pcr = 30.6035224490574 MN
C = 6977.19391202655 MN
q0 = 0.0025
b = 1600 mm
P_FE,peak = 10.990480 MN
frame = 262
time = 2.6200008392334 s
```

Solving the unchanged Airy equation gives

\[
\boxed{q_{theory}(P_{FE})=0.0013886422347494445},
\]

\[
\boxed{W_{d,theory}(P_{FE})=2.22182757559911\;\mathrm{mm}},
\]

\[
\boxed{\kappa_{theory}^{geom}(P_{FE})=8.56584344476355\times10^{-6}\;\mathrm{mm}^{-1}}.
\]

The production terminal root is

\[
q_u=0.00137889961633743,
\]

so `q_theory(P_FE)` is only `+0.70655%` above `q_u`.

### 3.2 equal-contract BH050

```text
Pcr = 19.5818772367311 MN
C = 10841.3718065234 MN
q0 = 0.0025
b = 2500 mm
P_FE,peak = 12.591227 MN
frame = 212
time = 2.1200006 s
```

The same unchanged equation gives

\[
\boxed{q_{theory}(P_{FE})=0.004117589557476763},
\]

\[
\boxed{W_{d,theory}(P_{FE})=10.2939738936919\;\mathrm{mm}},
\]

\[
\boxed{\kappa_{theory}^{geom}(P_{FE})=1.62555920073409\times10^{-5}\;\mathrm{mm}^{-1}}.
\]

The production terminal root is

\[
q_u=0.004772819645833164,
\qquad
W_{d,u}=11.9320491146\;\mathrm{mm}.
\]

Thus the same-load theoretical amplitude is `13.7284%` below the terminal amplitude. This is not a correction: the FEM peak occurs below the current theoretical terminal load.

---

## 4. Final gate logic when the local ODB is actually opened

First verify the imperfection contract:

\[
q_{0,FE}=W_{0,FE}/b
\]

against the frozen `q0=0.0025`, together with its modal fit quality.

At the peak, report both:

```text
PRIMARY:   q_FE,peak versus q_theory(P_FE,peak)
SECONDARY: q_FE,peak versus q_u
```

A poor modal `R2` or large normalized residual means that the one-mode reduced coordinate does not represent the FEM deformation well. It does not authorize fitting a correction factor.

No FEM displacement may alter `Pcr`, `C`, `q0`, common R06, terminal capacity coordinates, or root selection.

---

## 5. Deterministic local execution commands

Using the canonical local ODB identities:

```bat
abaqus python 20260827_2238__NZSCCM__BH_FEM_OUT_OF_PLANE_MODE_PROJECTOR_R02.py ^
  BH032_EXPLICIT_R02_GRID_B400.odb BH032_MODE_PROJECTION 1600 3200 2 0.0025 262 ^
  --step EXPLICIT_LOADING --instance C-S-SHELL-1 --peak-time 2.6200008392334
```

```bat
abaqus python 20260827_2238__NZSCCM__BH_FEM_OUT_OF_PLANE_MODE_PROJECTOR_R02.py ^
  BH050_EQUAL_CONTRACT_R02_GRID_B400.odb BH050_EQUAL_MODE_PROJECTION 2500 5000 2 0.0025 212 ^
  --step EXPLICIT_LOADING --instance C-S-SHELL-1 --peak-time 2.1200006
```

Each case writes only the needed diagnostic artifacts:

```text
FEM_GLOBAL_OUT_OF_PLANE_MODE_SUMMARY.json
FEM_GLOBAL_MODE_PAIRED_NODES.csv
```

---

## 6. Current decision

The requested gate is now fully specified and executable with one read-only peak-frame extraction per ODB. The theory-side values and canonical FEM frame identities are fixed before seeing the displacement projection.

The final numerical PASS/FAIL remains open solely because this runtime cannot open the local ODB bytes.

```text
PROJECTOR_R02_IMPLEMENTATION = PASS
BH032_CANONICAL_PEAK_FRAME = FIXED_262
BH050_EQUAL_CANONICAL_PEAK_FRAME = FIXED_212
BH032_SAME_LOAD_THEORY_TARGET = FIXED
BH050_EQUAL_SAME_LOAD_THEORY_TARGET = FIXED
BH032_FEM_MODE_PROJECTION = WAITING_FOR_LOCAL_ODB_EXECUTION
BH050_EQUAL_FEM_MODE_PROJECTION = WAITING_FOR_LOCAL_ODB_EXECUTION
qU_IN_PRODUCTION = NO
AIRY_CHANGE = NO
q_CHANGE = NO
CURVATURE_FORMULA_CHANGE = NO
TERMINAL_B_CAP_AS_GLOBAL_CURVATURE = NO
CURRENT_NEXT_ONLY = DIRECT_FEM_OUT_OF_PLANE_MODE_PROJECTION_BH032_AND_EQUAL_CONTRACT_BH050
```

The current production pointer is intentionally not advanced to a kinematic PASS state until actual peak-frame `U2` has been projected.
