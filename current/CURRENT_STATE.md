# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-25 09:10 +08:00  
**Status:** `MARGUERRE_AIRY_EXPLICIT_RETAINED / AIRY_USES_INITIAL_FULL_COMPOSITE_ABD / Z0-Z6_INITIAL_OFFSET_AUDIT_PASS / R07_AIRY_COEFFICIENTS_RETAIN_NO_DOUBLE_COUNT / SSNC_R02_AVAILABLE / SSNC_R04_IDEAL_EP_TERMINAL_AVAILABLE / R02-R04_DIRECT_INTERFACE_BLOCKED_AT_FACE_STRAIN_MAP / Pu_NOT_RECALCULATED`

> The Z0–Z6 stiffness audit is now complete: the archived/current Airy front already contains the external steel-face parallel-axis term `t_s z_f^2` for every Z specimen. No additional offset correction is permitted. The remaining obstacle to a new R02+R04 Z batch is not stiffness or post-yield tangent; it is the missing production identity from total Airy terminal demand to the current steel-face mean strain state required by R02.

## 0. Hard architecture

```text
STRUCTURAL_FRONT = FULL_2D_MARGUERRE_AIRY
AIRY_FUNCTION = RETAINED
AIRY_STIFFNESS = INITIAL_FULL_COMPOSITE_ABD
CURRENT_MATERIAL_TANGENT_INTO_AIRY = NO
GLOBAL_ULTIMATE_STATE_CRITERION = UNCHANGED
TERMINAL_OBJECT = CURRENT/CAPACITY RESULTANTS

D15 = NO
GLOBAL_MATERIAL_VIRTUAL_WORK_RJ = NO
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
EFFECTIVE_WIDTH_OR_AREA_AS_PRODUCTION = PROHIBITED
FORMAL_Z_COMPARATORS = ZHOU_SIMING + WINTER ONLY
```

## 1. Steel offset stiffness — Z0–Z6 audit complete

For a symmetric external steel face pair,

\[
\mathbf D_s^0
=
2\mathbf Q_s
\left(
t_sz_f^2+\frac{t_s^3}{12}
\right),
\qquad
\mathbf B_s^0=0.
\]

The 2026-08-25 09:10 execution independently reconstructed the archived scalar bending rigidity with

\[
D_{EI}^{calc}
=
E_c\frac{t_c^3}{12}
+
E_s
\left(
2t_sz_f^2+2\frac{t_s^3}{12}
\right).
\]

Results:

```text
Case  zf mm  offset/steel-D   steel/total-D   Dcalc - Darch [N mm]
Z0     63     0.999664176      0.570900588      0
Z1     48     0.999421631      0.643043649     -9.54e-7
Z2     63     0.999664176      0.570900588      0
Z3     63     0.999664176      0.545733716      0
Z4     98     0.999861188      0.452288592      0
Z5     63     0.999664176      0.570900588      0
Z6     63     0.999664176      0.570900588      0
```

Hence

```text
Z0_Z6_INITIAL_OFFSET_D = PASS
R07_AIRY_OFFSET_CORRECTION_NEEDED = NO
ADD_STEEL_OFFSET_AGAIN = PROHIBITED_DOUBLE_COUNTING
```

Z6's source-closed initial `A11,A22,A12,A66` is also reproduced to `2.51e-7 N/mm` maximum absolute error.

Therefore the existing current R07 structural coefficients `Pcr,C,G,Jy` are retained.

Artifacts:

- executable: `semantic_v2/40_execution/steel_shell/20260825_0910__NZSCCM__Z0_Z6_INITIAL_ABD_OFFSET_AUDIT_AND_R02_R04_INTERFACE_GATE.py`
- report: `semantic_v2/40_execution/steel_shell/20260825_0910__NZSCCM__Z0_Z6_INITIAL_ABD_OFFSET_AUDIT_AND_R02_R04_INTERFACE_GATE.md`

## 2. R03 remains diagnostic only

The exact elastic-postbuckling current 6x6 tangent derived in R03 remains mechanically valid.

However:

```text
R03_CURRENT_6X6_TANGENT_AS_Pu_GATE = NO
POST_FIRST_YIELD_6X6_TANGENT_REQUIRED_BEFORE_Z_Pu = NO
```

No further post-yield stiffness derivation is needed for the current explicit Airy production path.

## 3. R04 simplified terminal remains accepted

Each external steel face is a homogenized membrane layer at its physical centroid `z_f`.

For trial mean plane stress

\[
\boldsymbol\sigma^{tr}
=
(\sigma_x^{tr},\sigma_y^{tr},\tau_{xy}^{tr})^T,
\]

\[
\sigma_{vm}^{tr}
=
\sqrt{
(\sigma_x^{tr})^2
-\sigma_x^{tr}\sigma_y^{tr}
+(\sigma_y^{tr})^2
+3(\tau_{xy}^{tr})^2
},
\]

\[
\lambda
=
\min\left(1,\frac{f_y}{\sigma_{vm}^{tr}}\right),
\qquad
\boldsymbol\sigma^{cap}
=
\lambda\boldsymbol\sigma^{tr}.
\]

Then

\[
\mathbf N_f=t_s\boldsymbol\sigma^{cap},
\qquad
\mathbf M_f=z_f\mathbf N_f.
\]

No through-thickness plastic front is introduced.

Theory post-yield tangent is `Et=0`; optional tiny numerical regularization is allowed only if a solver requires it and is never fed back into Airy.

## 4. Exact remaining interface blocker

R02's active face operator is strain-driven:

```python
solve_total_amplitude(cell, ex, ey, gamma)
face_resultants(cell, ex, ey, gamma, kappa)
```

Hence R02 requires

\[
(e_x,e_y,\gamma_{xy})_f.
\]

The accepted reduced Airy production front supplies

\[
q,s
\to
(N_x^d,N_y^d,N_{xy}^d,M_x^d,M_y^d,M_{xy}^d),
\]

i.e. **total composite demand resultants**.

No currently frozen production identity uniquely maps these total resultants to the top/bottom steel-face strain triples while simultaneously closing the concrete/core terminal redistribution.

Therefore:

```text
R02_R04_COMPONENTS = AVAILABLE
R02_R04_DIRECT_Z_Pu_INTERFACE = BLOCKED
MISSING_IDENTITY =
  AIRY total terminal demand
  -> common current terminal section strains
  -> steel-face (ex,ey,gamma)
  -> R02 trial steel state
NEW_Pu_Z0_Z6 = NOT CALCULATED
```

This reproduces the same class of interface issue already identified in the earlier direct-current-Yun terminal audit; the 09:10 execution now shows that offset stiffness is **not** the cause.

## 5. Shortcuts not silently activated

The following could be made executable but are new modelling choices and are therefore not silently promoted:

```text
A. initial-elastic ABD inversion all the way to nonlinear terminal strains
B. promote the earlier affine 2D projected-moment diagnostic terminal to production
C. return to the superseded global material residual/current-tangent route
D. use effective width/effective area
```

`C` and `D` remain prohibited by the current architecture. `A` or `B` would require an explicit production decision plus one-dimensional degeneration and no-double-counting checks.

## 6. Exact current stopping point

Closed:

```text
raw Z geometry/material
-> initial full composite ABD
-> steel-face offset stiffness verified for Z0-Z6
-> existing Airy structural coefficients retained
-> explicit Airy demand
-> R02 PBL operator available
-> R04 ideal-EP 2D cap available
```

Open:

```text
ONE COMMON TERMINAL STRAIN/RESULTANT BRIDGE
```

Only after this bridge is frozen should the new Z0–Z6 `Pu` batch be solved and Zhou/Winter reopened for post-solution validation.

## 7. Next task

```text
NEXT =
FREEZE ONE PRODUCTION COMMON-SECTION STRAIN BRIDGE
THAT RETURNS STEEL-FACE (ex,ey,gamma) FROM THE AIRY TERMINAL STATE,
WITHOUT CURRENT-TANGENT FEEDBACK, EFFECTIVE WIDTH, OR GLOBAL MATERIAL RJ;

THEN CONNECT R02 -> R04 -> NC TERMINAL AND SOLVE Z0-Z6.
```
