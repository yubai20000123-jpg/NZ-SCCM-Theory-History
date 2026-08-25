# CURRENT STATE — Steel-Shell UHPC / SSUHPC-HU-R01

**Updated:** 2026-08-25 13:00 +08:00  
**Status:** `THEORY_ESTABLISHED / CURRENT_STEEL_SHELL_RETAINED / EARLY_HU_UHPC_RESTORED / LATER_REPAIR_CHAIN_OFF / SEVEN-CASE REEXECUTION PENDING`

Canonical theory:

`semantic_v2/20_theory/20260825_1300__NZSCCM__STEEL_SHELL_UHPC_HU_EARLY_REPLACEMENT_THEORY_V1.md`

---

## 1. Branch identity

This branch is deliberately separate from the ordinary-concrete `current/CURRENT_STATE.md`.

```text
STRUCTURE = STEEL-SHELL UHPC
STRUCTURAL_FRONT = CURRENT FULL-2D MARGUERRE-AIRY
AIRY_STIFFNESS = INITIAL FULL-COMPOSITE ABD
CORE_MATERIAL = EARLY HU-WENXU UHPC TERMINAL
STEEL_FACE = CURRENT R02 PBL + R04 IDEAL-EP MISES CAP
WEB = LONGITUDINAL IDEAL-EP
R03_Pu_GATE = NO
```

Only the concrete core is replaced. The current steel-shell mechanics are not rolled back.

---

## 2. UHPC material identity

Historical early replacement parameters retained for this branch:

```text
fc      = 141.1 MPa
Ec      = 43.4 GPa
epsc0   = 0.0035
nu_c    = 0.20
Es      = 206 GPa
nu_s    = 0.30
fy      = 355 MPa
```

Hu compression rising branch:

\[
\sigma_c=f_c\frac{n\xi-\xi^2}{1+(n-2)\xi},
\qquad
\xi=\varepsilon/\varepsilon_{c0},
\qquad
n=E_c\varepsilon_{c0}/f_c,
\qquad 0\le\xi\le1.
\]

Primary ultimate terminal is first compressed-face contact with

\[
\varepsilon_c=\varepsilon_{c0},\qquad\sigma_c=f_c.
\]

The post-peak Hu branch is source-retained but does not extend Pu in this early theory.

The compression-zone thickness resultants use exact analytic primitives `F0,F1`; formal thickness quadrature is zero.

---

## 3. Current steel side retained

```text
R02 = finite 2D PBL face postbuckling operator
R04 = path-free radial Mises cap
face current stress = R04(R02(common face strain))
face resultant N = ts * sigma
face centroid moment M = zf * N
```

Initial face bending still contains both

\[
t_sz_f^2
\]

and

\[
t_s^3/12.
\]

No additional offset correction is allowed.

---

## 4. Terminal system

For a bending controller, use finite unknowns

\[
(q,c,\varepsilon_x)
\]

and solve

\[
N_x^{sec}=N_x^d,
\qquad
N_y^{sec}=N_y^d,
\qquad
M_y^{sec}=M_y^d.
\]

The section contains:

```text
UHPC Hu closed-form compression zone
+ exact finite web clip integral
+ top R02/R04 steel face
+ bottom R02/R04 steel face
```

For an internal controlling location add a finite stationarity/contact condition; for an endpoint use the boundary condition directly.

The early UHPC transverse companion is only the plane-stress closure/precheck

\[
\sigma_x^U=E_c\varepsilon_x+\nu_c\sigma_y^U.
\]

It is not promoted to a full biaxial nonlinear UHPC state machine.

If the historical tensile qualification `f_t,cr≈9.7677 MPa` is exceeded, the branch reports `EARLY_HU_DOMAIN_EXCEEDED` and stops. It does not automatically call later Liu/DP/W-W/FHWA repairs.

---

## 5. Hard exclusions

```text
LATER_37MM_WEB_REBASE_AS_HISTORICAL_0821_REPRODUCTION = NO
ZHANG_UHPC_BACKBONE = OFF
LIU_CC_TC_TT_REPAIR = OFF
DP_PRODUCTION_GATE = OFF
WILLAM_WARNKE_PRODUCTION_GATE = OFF
FHWA_HIEW_REPLACEMENT = OFF
R08_RECTANGULAR_UHPC_RESULTANT_BLOCK = OFF
D15_GXX_UHPC_SURFACE = OFF
EFFECTIVE_WIDTH_BT_CORRECTION = OFF
FEM_TEST_CALIBRATION = OFF
CURRENT_MATERIAL_TANGENT_INTO_AIRY = OFF
MATERIAL_POINTS = 0
FORMAL_SPATIAL_QUADRATURE = 0
```

For new specimens `rho_w` always comes from raw geometry. The historical `9×4×32=1152 mm²` web contract is retained only to reproduce the 2026-08-21 seven-case regression.

---

## 6. Historical regression reference — not new production output

The early Hu replacement branch previously produced approximately:

```text
T120   12.3480 MN
T360   11.2978 MN
BH005   2.3829 MN
BH010   4.4173 MN
BH020   8.1398 MN
BH032  11.1101 MN
BH050  13.5946 MN
```

These numbers establish the identity of the restored early replacement scheme. They are not silently reused as the output of the current R02/R04 steel theory.

---

## 7. Next task

```text
NEXT = CLEAN 7-CASE REEXECUTION
CASES = T120,T360,BH005,BH010,BH020,BH032,BH050
COMPARATORS DURING SOLVE = CLOSED
STRUCTURAL FRONT = CURRENT
STEEL = R02/R04
UHPC = EARLY HU TERMINAL
AFTER ALL ROOTS FIXED = OPEN FEM/TEST COMPARISON
IF ONLY LARGE-B/T END IS BAD = RECORD IT; DO NOT AUTO-REPAIR
```

Current branch gate:

```text
SSUHPC_HU_EARLY_REPLACEMENT_THEORY = PASS
NUMERICAL_REEXECUTION = PENDING
```
