# CURRENT STATE ADDENDUM — SSUHPC qU retirement + classical curvature contract reset

**Updated:** 2026-08-27 20:52 +08:00  
**Parent current state:** `current/SSUHPC_CURRENT_STATE_20260825.md`  
**Supersedes for current task priority:** `current/SSUHPC_CURRENT_STATE_ADDENDUM_20260827_1730.md`  
**Detailed audit:** `semantic_v2/40_execution/steel_shell/20260827_2052__NZSCCM__BH050_BH032_CLASSICAL_W_KAPPA_EPS_KINEMATIC_RECONSTRUCTION_R01.md`

## Current decision

The formally certified qU branch is retained in history as a valid sensitivity calculation, but is removed from the production theory because its BH050 effect is only about `-0.47%` while it materially increases the local steel backend complexity.

```text
qU_IN_PRODUCTION = NO
qU_CERTIFICATE = RETAIN_ARCHIVE_ONLY
COMMON_R06_qU_OFF = CURRENT_PRODUCTION_BASELINE
CURRENT_PRODUCTION_BH050 = 13.3563763545430 MN
ARCHIVED_qU_BH050 = 13.2934844671869 MN
```

No qU result or certificate is deleted; only its current theoretical role changes.

## Classical curvature identity

The frozen structural ansatz remains

\[
w_i=bq_0\sin\alpha x\sin\beta y,
\qquad
w_d=bq\sin\alpha x\sin\beta y.
\]

Because `w_i` is the stress-free initial imperfection, the stress-producing incremental curvature is

\[
\Delta\kappa_x=-w_{d,xx},
\qquad
\Delta\kappa_y=-w_{d,yy},
\qquad
\Delta\kappa_{xy}=-2w_{d,xy}.
\]

At the BH control antinode with `ell=b`,

\[
\boxed{\Delta\kappa_x=\Delta\kappa_y=\pi^2q/b}.
\]

The existing Airy structural moment already satisfies

\[
\boxed{M_y^d=D_\mu\Delta\kappa_x+D_y\Delta\kappa_y=J_yqs}.
\]

Therefore the Airy bending demand is already classical-q-kinematic. It is not corrected by forcing the terminal capacity parameter to equal `pi^2 q/b`.

## Terminal parameter identity reset

The terminal affine variables historically named `(A_x,B_x,A_y,B_y)` remain the finite coordinates used to parameterize the N-M capacity surface. From this node onward their interpretation is locked as

```text
Ax_cap, Bx_cap, Ay_cap, By_cap = CAPACITY-SURFACE COORDINATES
Bx_cap, By_cap = NOT ACTUAL GLOBAL CURVATURE OBSERVABLES
```

Code or historical formulas may retain the short symbols `Ax,Bx,Ay,By`, but prose/theory interpretation must not call `Bx,By` the actual global q-derived curvature unless explicitly referring to a separate physical curvature variable.

The previously retracted constraint remains prohibited:

```text
Bx_cap = pi^2*q/b = NO
By_cap = pi^2*q/b = NO
```

## BH032/BH050 cross-check

Classical q-kinematics gives:

```text
BH032:
  q = 0.00137889961633743
  Wd = 2.20623938614 mm
  total one-mode slope scale = 0.6982 deg
  kappa_geo = 8.50574607629e-6 1/mm
  FEM UHPC fitted kappa at peak = 1.93135e-5 1/mm
  FEM steel mean apparent kappa at peak = 3.48531e-6 1/mm
  structural demand eccentricity |My/Ny| = 2.00435 mm

BH050 qU-off:
  q = 0.004772819645833164
  Wd = 11.9320491146 mm
  total one-mode slope scale = 1.3091 deg
  kappa_geo = 1.88423367128e-5 1/mm
  old-special-ODB UHPC fitted kappa at peak = 1.83974e-5 1/mm
  old-special-ODB steel mean apparent kappa at peak = 6.25282e-6 1/mm
  structural demand eccentricity |My/Ny| = 5.85145 mm
```

With total thickness `h=50 mm`, the demand eccentricities are only `0.0802*(h/2)` for BH032 and `0.2341*(h/2)` for BH050. The structural demand is therefore membrane-compression dominated; the previous appearance of a much stronger compression-bending state came from reading `By_cap` and its capacity-state face strains as actual deformation-path observables.

The BH050 near equality between `kappa_geo` and the old-special-ODB UHPC fitted curvature is not generalized: BH032 fails the same identity by a factor about `2.27`. Also, the current equal-contract BH050 ODB has a verified peak `12.591227 MN` but no archived equal-contract displacement/curvature projection in the current source set.

## Current architecture

```text
initial full-composite Airy/Galerkin demand = RETAIN
q = sole global postbuckling amplitude = RETAIN
classical physical curvature kappa_geo(q) = RETAIN
Airy moment My=Jy*q*s = RETAIN
terminal N-M capacity contact = RETAIN
terminal B_cap as actual physical curvature = NO
current-moment feedback into Airy = NO
common-kappa terminal constraint = NO
qU production = NO
formal spatial quadrature = 0
formal thickness quadrature = 0
material points = 0
```

## Unique next kinematic gate

The next task is **not** another terminal-curvature closure and not a qU variant. It is a direct read-only FEM displacement-mode projection for BH032 and the equal-contract BH050 model:

\[
U_{oop}^{FE}(x,y)
\rightarrow W_{FE}
\rightarrow q_{FE}=W_{FE}/b
\rightarrow \kappa_{FE}^{geom}.
\]

This is diagnostic only. It must be compared against the theoretical `q` without using the FEM result to tune or select the theory root.

```text
NEXT_ONLY = DIRECT_FEM_OUT_OF_PLANE_MODE_PROJECTION_BH032_AND_EQUAL_CONTRACT_BH050
```
