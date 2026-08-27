# NZ-SCCM — BH032 / equal-contract BH050 direct FEM out-of-plane mode projection gate R01

**Time:** 2026-08-27 22:26 +08:00  
**Parent current state:** `current/SSUHPC_CURRENT_STATE_ADDENDUM_20260827_2052_KINEMATIC_CURVATURE_RESET.md`  
**Projector:** `semantic_v2/40_execution/steel_shell/20260827_2226__NZSCCM__BH_FEM_OUT_OF_PLANE_MODE_PROJECTOR_R01.py`  
**Status:** `PROJECTOR IMPLEMENTED / SAME-LOAD THEORY TARGETS FIXED / ODB RUNTIME DATA NOT PRESENT IN REPOSITORY / FEM q NOT FABRICATED`

---

## 0. Scope

This node executes the unique current kinematic gate as far as the available runtime data permit. It does **not** change the Marguerre–Airy theory, common R06, terminal capacity-contact equations, or any material parameter.

The target observable is the global FEM out-of-plane displacement mode, not a strain-derived curvature:

\[
U_{oop}^{FE}(x,y)\rightarrow W_d^{FE}\rightarrow q_{FE}=W_d^{FE}/b\rightarrow \kappa_{FE}^{geom}.
\]

For the accepted Abaqus coordinate contract:

```text
FE global X -> theory x
FE global Z -> theory y / loading direction
FE global Y -> theory out-of-plane direction
incremental out-of-plane displacement -> U2
```

The Abaqus imperfection is encoded in the initial mesh, while `U2` is incremental displacement from that imperfect configuration. Therefore the projector treats them separately:

```text
initial paired-face midsurface Y -> W0_FE -> q0_FE
incremental paired-face midsurface U2 -> Wd_FE -> q_FE
```

No initial imperfection is added to `q_FE`.

---

## 1. Repository/runtime audit

The current Git repository was searched before execution for:

- `.odb` files;
- archived BH032/BH050 nodal `U2` fields;
- a completed equal-contract BH050 global displacement-mode projection.

No ODB binary and no archived nodal U2 field needed for this gate is present in the repository tree. The current sources contain the accepted equal-contract BH050 peak reaction result and older strain/stress diagnostics, but those are not substitutes for the requested global displacement field.

Therefore:

```text
BH032_FEM_q_FE = NOT YET EVALUABLE IN THIS REMOTE RUNTIME
BH050_EQUAL_CONTRACT_q_FE = NOT YET EVALUABLE IN THIS REMOTE RUNTIME
NO_FEM_q_INFERENCE_FROM_STRAIN = ENFORCED
NO_FEM_q_FABRICATION = ENFORCED
```

This is a data-mount/runtime blocker only, not a theoretical or algorithmic blocker.

---

## 2. Read-only Abaqus projector now implemented

The committed Abaqus-2019/Python-2-compatible projector performs the following read-only operations.

1. opens the supplied ODB `readOnly=True`;
2. finds the dominant shell instance unless an instance is specified;
3. identifies horizontal steel-face shell elements from undeformed normals (`|n_y|>=0.90` by default);
4. pairs the outer top and bottom steel-face nodes at common FE `(X,Z)` coordinates;
5. constructs the face-midpoint geometry and incremental midpoint displacement
   \[
   Y_{mid,0}=\frac{Y_++Y_-}{2},\qquad
   U_{2,mid}=\frac{U_{2,+}+U_{2,-}}{2};
   \]
6. defines the frozen global mode on the actual FE span
   \[
   \phi=\sin\!\left(\pi\frac{X-X_{min}}{L_x^{FE}}\right)
   \sin\!\left(m_*\pi\frac{Z-Z_{min}}{L_z^{FE}}\right);
   \]
7. removes rigid out-of-plane translation and two rigid tilt terms with a weighted least-squares basis `[1,X,Z,phi]`;
8. fixes the sign of `phi` from the **initial imperfection projection**, never from the favorable loaded response;
9. projects every field-output frame and returns `Wd_FE`, `q_FE`, geometric curvature, modal `R2`, RMS residual, and normalized residual;
10. records the actual FE spans separately from the frozen theoretical `b,a` so a 1592-vs-1600 type geometry difference is never silently erased.

The area weights are only a diagnostic FEM data-reduction measure. They are not formal structural quadrature and do not enter the production theory.

```text
FORMAL_STRUCTURAL_SPATIAL_QUADRATURE = 0
FORMAL_THICKNESS_QUADRATURE = 0
MATERIAL_POINTS = 0
FEM_POSTPROCESS_WEIGHTED_LS = DIAGNOSTIC_ONLY
THEORY_MODIFIED = NO
```

---

## 3. Frozen same-load theory targets computed now

A direct comparison at the FEM peak must not compare the FEM peak deformation only with the theoretical **terminal** root. The frozen monotonic Airy branch allows the theory amplitude at the same load to be computed independently:

\[
P(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0).
\]

This equation is monotonic for `q>=0`, so each accepted FEM peak load has one positive theory amplitude.

### 3.1 BH032

Frozen inputs:

```text
Pcr = 30.6035224490574 MN
C   = 6977.19391202655 MN
q0  = 0.0025
b   = 1600 mm
P_FE,peak = 10.99048 MN
```

Solving the unchanged Airy equation gives

\[
\boxed{q_{theory}(P_{FE})=0.0013886422347494445}.
\]

Hence

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

so the same-load amplitude differs from the terminal amplitude by only

\[
\boxed{+0.70655\%}.
\]

This is expected because BH032 FEM and theory peak loads are already almost equal.

### 3.2 equal-contract BH050

Frozen production inputs:

```text
Pcr = 19.5818772367311 MN
C   = 10841.3718065234 MN
q0  = 0.0025
b   = 2500 mm
P_FE,peak = 12.591227 MN
peak time = 2.1200006 s
peak frame = 212
```

Solving the same unchanged Airy equation at the FEM peak gives

\[
\boxed{q_{theory}(P_{FE})=0.004117589557476763}.
\]

Thus

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

The same-load amplitude is therefore `13.7284%` below the terminal amplitude. This difference is **not** an error and is not a correction: the FEM peak occurs below the current theoretical terminal load, so the proper kinematic comparator at `12.591227 MN` is `q_theory(P_FE)`, not `q_u`.

---

## 4. Formal pass/fail logic once the ODBs are mounted

For each case, the first gate is the initial-imperfection contract:

\[
q_{0,FE}=W_{0,FE}/b
\]

must be compared with the frozen `q0=0.0025`, together with the modal fit quality. A poor initial-mode projection indicates a geometry/observable mismatch before any loaded comparison.

At the FEM peak, report both comparisons:

```text
A. q_FE,peak versus q_theory(P_FE,peak)  <- primary same-load kinematic check
B. q_FE,peak versus q_u                  <- secondary peak-vs-terminal reference only
```

No FEM value may be used to alter `Pcr`, `C`, `q0`, common R06, the terminal capacity surface, or root selection.

A low modal `R2` or large normalized residual means the FEM deformation is not adequately represented by the frozen single global mode; it does **not** authorize a fitted correction coefficient.

---

## 5. Exact execution commands

BH032, producing the complete frame path because the repository does not currently contain a certified peak frame/time identifier for this ODB:

```bat
abaqus python 20260827_2226__NZSCCM__BH_FEM_OUT_OF_PLANE_MODE_PROJECTOR_R01.py ^
  BH032_EXPLICIT_R02_GRID_B400.odb BH032_MODE_PROJECTION 1600 3200 2 0.0025 ^
  --step EXPLICIT_LOADING
```

Equal-contract BH050, using the already-certified peak frame/time:

```bat
abaqus python 20260827_2226__NZSCCM__BH_FEM_OUT_OF_PLANE_MODE_PROJECTOR_R01.py ^
  BH050_EQUAL_CONTRACT_R02_GRID_B400.odb BH050_EQUAL_MODE_PROJECTION 2500 5000 2 0.0025 ^
  --step EXPLICIT_LOADING --target-frame 212 --target-time 2.1200006
```

Each run writes:

```text
FEM_GLOBAL_OUT_OF_PLANE_MODE_PATH.csv
FEM_GLOBAL_MODE_PAIRED_NODES.csv
FEM_GLOBAL_OUT_OF_PLANE_MODE_SUMMARY.json
```

---

## 6. Current decision

The requested kinematic gate has been reduced to a deterministic read-only ODB operation. The code and all theory-side comparison targets are now fixed. The final numerical gate cannot be marked PASS or FAIL in the present remote runtime because the two ODB displacement fields are not mounted or archived in GitHub.

```text
PROJECTOR_IMPLEMENTATION = PASS
BH032_SAME_LOAD_THEORY_TARGET = FIXED
BH050_EQUAL_SAME_LOAD_THEORY_TARGET = FIXED
BH032_FEM_MODE_PROJECTION = WAITING_FOR_ODB_RUNTIME
BH050_EQUAL_FEM_MODE_PROJECTION = WAITING_FOR_ODB_RUNTIME
qU_IN_PRODUCTION = NO
AIRY_CHANGE = NO
q_CHANGE = NO
CURVATURE_FORMULA_CHANGE = NO
TERMINAL_B_CAP_AS_GLOBAL_CURVATURE = NO
CURRENT_NEXT_ONLY = DIRECT_FEM_OUT_OF_PLANE_MODE_PROJECTION_BH032_AND_EQUAL_CONTRACT_BH050
```

The current production pointer is intentionally **not** advanced to a kinematic PASS state until actual `U2` data have been projected.
