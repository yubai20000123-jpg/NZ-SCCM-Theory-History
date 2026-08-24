# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-24 16:12 +08:00  
**Status:** `MARGUERRE_AIRY_EXPLICIT / Ny_My_RESULTANT_TERMINAL / R19_CANONICAL_MA_UV_YUN_BRIDGE_SOURCE_CLOSED / R18_MANUFACTURED_COORDINATE_SCALING_BRIDGE_SUPERSEDED / DIRECT_SIGMA_ET_TO_RESIDUAL_JACOBIAN / NO_ABD_INTERMEDIATE / YUN_ALWAYS_ON / D15_DIRECT_YUN_COMPILE_NEXT / R07_R14_PRE_YUN_BASELINES / TC_ROUTE_WITHDRAWN / USER_ACCEPTANCE_PENDING`

> R19 closes the exact upstream Marguerre--Airy/Yun interface that remained unresolved after R18. The production `A_y=B_A^y` basis, physical \(\varepsilon_0\)/\(k^2\) scaling, sine coordinates, and strip-local-to-global coordinate map are now explicit and derivative-audited. R18 remains a useful scaffold calculus test but its manufactured `B_A^y` and diagnostic coordinate/scaling form are not production theory.

## 0. Frozen architecture

```text
STRUCTURAL_FRONT = FULL_2D_MARGUERRE_AIRY
TERMINAL_OBJECT = AXIAL_Y_NORMAL_Ny_My
FORMAL_SPATIAL_QUADRATURE = 0
THICKNESS_QUADRATURE = 0
MATERIAL_POINTS = 0
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
TC_CC_TT_ROUTE = OFF_MAINLINE
YUN_STEEL_SHELL_MODULE = ALWAYS_ON
SIGMA_CR_OVER_FY = DIAGNOSTIC_ONLY
A_B_D_INTERMEDIATE_BEFORE_EQUILIBRIUM = NO
```

Current chain:

\[
\boxed{
(D,q,\alpha,\{A_i^\pm\})
\xrightarrow{\text{canonical Marguerre--Airy UV}}
\varepsilon_s
\xrightarrow{\text{always-on Yun/Karman}}
(\sigma_s,E_{t,s})
\xrightarrow{\text{direct virtual work}}
(\mathbf R,\mathbf J)
\rightarrow
(N_y,M_y)
\rightarrow P_u.
}
\]

## 1. R19 canonical Marguerre--Airy y-strain

Sources:

`semantic_v2/20_theory/20260820_2358__NZSCCM__NGUYEN_KINEMATICS_EXPLICIT_UV_AND_NC_M6_VIRTUAL_WORK_SYSTEM.md`

`semantic_v2/40_execution/steel_shell/20260818_1421__NZSCCM__Z1_Z4__UNIFIED_YUN_IDEAL_EP_LOCAL_AMPLITUDE_FULL_RECALC.md`

Use

\[
X=\pi x/b,\qquad Y=\pi y/\ell,\qquad k=b/\ell,
\]

\[
F_y=\sin^2X(1-\sin^2Y),\qquad H_s=\sin X\sin Y,
\]

\[
\boxed{
A_y=
\frac{\nu}{4}
-\frac{k^2}{2}\sin^2X
-\frac{\nu}{2}\sin^2Y
+k^2\sin^2X\sin^2Y.
}
\]

Then

\[
\boxed{
e_y=
-D+\alpha A_y
+\frac{\pi^2k^2}{\varepsilon_0}
\left(q_0q+\frac12q^2\right)F_y
+\frac{\pi^2t_rk^2}{2\varepsilon_0b}qH_s\zeta.
}
\]

The project `B_A^y` blocker is therefore closed.

## 2. Nested Yun strip coordinate map

Historical Yun strips use local \(x_i\) in \(\phi_i\), while global Marguerre--Airy fields must retain their global face coordinate. R19 uses

\[
\boxed{x_g=iB_s+x_i,\qquad 0\le x_i\le B_s.}
\]

Therefore:

```text
GLOBAL_MA_FIELD_COORDINATE = x_g
LOCAL_YUN_SHAPE_COORDINATE = x_i
RESET_GLOBAL_X_TO_ZERO_EACH_STRIP = NO
```

Z1: 30 × 200 mm strips cover exactly 0--6000 mm.  
Z4: 40 × 200 mm strips cover exactly 0--8000 mm.

## 3. R19 executable and audit

Report:

`semantic_v2/40_execution/20260824_1612__NZSCCM__CANONICAL_MA_UV_TO_YUN_RESIDUAL_JACOBIAN_R19.md`

Executable:

`semantic_v2/40_execution/steel_shell/20260824_1612__NZSCCM__CANONICAL_MA_UV_TO_YUN_RESIDUAL_JACOBIAN_R19.py`

Results:

`semantic_v2/40_execution/steel_shell/20260824_1612__NZSCCM__CANONICAL_MA_UV_TO_YUN_RESIDUAL_JACOBIAN_R19_RESULTS.csv`

Executed audit:

```text
POINTWISE_FIRST_DERIV_MAX_ABS_ERR = 2.659429e-12
POINTWISE_SECOND_DERIV_MAX_ABS_ERR = 2.140954e-12
DIAGNOSTIC_RA_JAC_MAX_ABS_ERR = 1.653234e-08
DIAGNOSTIC_RA_JAC_MAX_REL_ERR = 8.276635e-10
R19_CANONICAL_MA_TO_YUN_JACOBIAN_AUDIT = PASS
```

High-order Gauss-Legendre appears only in the diagnostic finite-difference/oracle check, not in the formal operator.

## 4. R18 supersession

Retain R18 architecture:
- direct \(\sigma_s\to R\);
- direct \(E_{t,s}\to J\);
- current stress geometric tangent;
- always-on \(R_{A_i}\);
- no A/B/D prerequisite.

Supersede R18 production placeholders:
```text
MANUFACTURED_BAy = SUPERSEDED
u=x/b, v=y/ell EXECUTABLE PLACEHOLDER = SUPERSEDED
COSINE_REPORT_SHORTHAND = SUPERSEDED
MISSING_eps0_k2_PHYSICAL_SCALING = SUPERSEDED
```

## 5. Baseline status

R07 and R14 numerical values remain **PRE-YUN-REWIRE regression baselines only**.

Historical 2026-08-18 Z1/Z4 unified-Yun numbers remain **historical regression targets only**.

```text
PRODUCTION_Pu_CHANGED_IN_R19 = NO
```

## 6. Next task

```text
NEXT_TASK =
D15_COMPILE_CANONICAL_DIRECT_YUN_STEEL_RESIDUAL_JACOBIAN
+ HISTORICAL_Z1_Z4_REGRESSION
+ Z0_Z6_RERUN
+ R08_R10A_R11_R12_R14_UHPC_ADAPTER_RERUN
```

Required order:
1. compile the source-closed R19 trigonometric steel strain and derivatives into the finite D15/moment representation;
2. preserve ideal-EP/Yun current stress semantics without giving numerical spatial quadrature formal identity;
3. reproduce historical Z1/Z4 unified-Yun states as regression checks;
4. solve the current coupled Marguerre--Airy/Yun branch;
5. then rerun Z0--Z6 and UHPC adapter families with comparators closed during solve.

```text
USER_ACCEPTANCE = PENDING
```
