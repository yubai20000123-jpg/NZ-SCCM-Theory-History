# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-24 22:50 +08:00  
**Status:** `MARGUERRE_AIRY_EXPLICIT / AXIAL_Y_NORMAL_Ny_My_TERMINAL / R20_0_DIRECT_AIRY_YUN_GOVERNANCE_FROZEN / R19_KINEMATIC_SCALING_COORDINATE_BRIDGE_RETAINED / R19_GLOBAL_VIRTUAL_WORK_HANDOFF_SUPERSEDED / D15_NEXT_SUPERSEDED / YUN_ALWAYS_ON / R20_1_DIRECT_NYMY_CLOSURE_ACTIVE / R20_2_Z1_Z4_AUTHORIZED_AFTER_CLOSURE / R20_3_FULL_BATCH_HOLD`

> R20-0 is the user-approved governance correction after R19. R19 remains authoritative for the canonical Marguerre--Airy y-strain basis, physical scaling, local-to-global strip coordinate map and derivative audit. Its pending `D15_DIRECT_YUN_COMPILE_NEXT` and global direct-virtual-work residual/Jacobian handoff are not the accepted R20 structural route. R20 restores the already-frozen architecture `Airy structural demand -> direct axial y-normal Ny-My terminal -> Pu` and inserts the always-on Yun steel-shell mechanism on the terminal-capacity side.

## 0. Frozen architecture

```text
STRUCTURAL_FRONT = FULL_2D_MARGUERRE_AIRY
TERMINAL_OBJECT = AXIAL_Y_NORMAL_Ny_My
MA_V1_MONOTONE_POSTBUCKLING = TRUE
GLOBAL_GEOMETRIC_FOLD_REQUIRED = FALSE
CURRENT_MATERIAL_INTO_AIRY_COMPATIBILITY = NO
GLOBAL_VIRTUAL_WORK_RJ_AS_R20_STRUCTURAL_MAINLINE = NO
D15_AS_R20_NEXT_ROUTE = NO
FORMAL_SPATIAL_QUADRATURE = 0
THICKNESS_QUADRATURE = 0
MATERIAL_POINTS = 0
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
YUN_STEEL_SHELL_MODULE = ALWAYS_ON
SIGMA_CR_OVER_FY = DIAGNOSTIC_ONLY
YIELD_ORDERING = DIAGNOSTIC_ONLY
R20_3_FULL_BATCH = HOLD
```

Current production architecture:

\[
\boxed{
q
\xrightarrow{\text{Marguerre--Airy}}
\{P_{pb}(q),n_d(s;q),m_d(s;q)\}
\longrightarrow
\text{direct }(N_y,M_y)\text{ terminal contact}
\longleftarrow
\{\text{concrete/core resultants},\text{Yun steel resultants}\}
\rightarrow P_u=P_{pb}(q).
}
\]

## 1. Structural demand retained

Primary architecture correction:

`semantic_v2/40_execution/20260823_0322__NZSCCM__MARGUERRE_AIRY_TERMINAL_CAPACITY_ARCHITECTURE_CORRECTION.md`

Z-family direct resultant baseline:

`semantic_v2/40_execution/20260824_0918__NZSCCM__Z0_Z6_NY_MY_RESULTANT_RECALCULATION_R07.md`

\[
P_{pb}(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0),
\]

\[
n_d(s;q)=\frac{P_{pb}(q)}b+Gq(q+2q_0)(1-2s^2),
\qquad
m_d(s;q)=J_yqs.
\]

The full 2D Airy field is retained. `Nx`/`Mx` are not hard terminal equalities on the selected symmetric y-normal cut.

## 2. R19 bridge retained but role restricted

Retain the R19 canonical basis and scaling:

\[
A_y=\frac{\nu}{4}-\frac{k^2}{2}\sin^2X-\frac{\nu}{2}\sin^2Y+k^2\sin^2X\sin^2Y,
\]

\[
e_y=-D+\alpha A_y
+\frac{\pi^2k^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right)F_y
+\frac{\pi^2t_rk^2}{2\varepsilon_0b}qH_s\zeta,
\]

and

\[
\boxed{x_g=iB_s+x_i}.
\]

```text
R19_KINEMATIC_SCALING_COORDINATE_BRIDGE = RETAIN
R19_DERIVATIVE_AUDIT = RETAIN
R19_GLOBAL_VIRTUAL_WORK_CLOSURE_AS_R20_MAINLINE = SUPERSEDED
R19_D15_NEXT_HANDOFF = SUPERSEDED
```

## 3. Always-on Yun steel-shell mechanism

Historical direct source:

`semantic_v2/40_execution/steel_shell/20260818_1421__NZSCCM__Z1_Z4__UNIFIED_YUN_IDEAL_EP_LOCAL_AMPLITUDE_FULL_RECALC.md`

\[
\sigma_s=\operatorname{clip}(E_s\varepsilon_s,-f_y,+f_y),
\]

\[
R_{A_i}=C_\sigma\left[k_{cr}A_i+H(2A_{0i}A_i+A_i^2)(A_i+A_{0i})\right]
-\bar\sigma_{c,i}(A_i+A_{0i})=0.
\]

```text
YUN_LOCAL_KARMAN_GEOMETRY = ACTIVE
LOCAL_Ai = FINITE_CURRENT_ALGEBRAIC_COORDINATE
LOCAL_Ai_AS_GROSS_RITZ_MODE = NO
LOCAL_Ai_HISTORY_STATE = NO
WHOLE_FACE_Et_ZERO_SWITCH = NO
```

## 4. R20-0 governance report

`semantic_v2/40_execution/20260824_2250__NZSCCM__R20_0_DIRECT_AIRY_YUN_NYMY_GOVERNANCE_AND_INTERFACE_FREEZE.md`

R20-0 calculates no new `Pu`.

Historical R07/R14 values and the 2026-08-18 Z1/Z4 Yun values remain regression/reference values only.

## 5. Exact active next task

```text
R20_1 = SOURCE-CLOSE DIRECT YUN STEEL -> y-NORMAL Ny,My RESULTANT MAPPING
        + NO-DOUBLE-COUNTING GATE
        + BUILD DIRECT TERMINAL EQUATIONS

R20_2 = AFTER R20_1 PASS, SOLVE ONLY Z1 AND Z4
        WITH HISTORICAL 14.44689544 / 52.43155584 MN CLOSED DURING SOLVE

R20_3 = HOLD
```

R20-1 formal target:

\[
F_N=N_y^{cap}-n_d=0,
\qquad
F_M=M_y^{cap}-m_d=0,
\qquad
R_{A_i}=0,
\]

with

\[
N_y^{cap}=N_y^c+N_y^{s,Yun}+N_y^{web},
\qquad
M_y^{cap}=M_y^c+M_y^{s,Yun}+M_y^{web}.
\]

**Fail-fast gate:** numerical R20-2 is forbidden until repository sources uniquely close the mapping from the historical Yun strip/area stress field to the work-conjugate y-normal cut resultants `Ny,My` without double counting the gross Airy mode. No new section law may be invented to bypass this gate.
