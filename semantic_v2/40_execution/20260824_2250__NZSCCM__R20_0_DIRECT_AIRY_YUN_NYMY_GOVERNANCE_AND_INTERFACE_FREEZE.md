# NZ-SCCM — R20-0 direct Airy + Yun -> Ny-My governance and interface freeze

**Time:** 2026-08-24 22:50 +08:00  
**Status:** `EXECUTED / GOVERNANCE_FROZEN / NO_Pu_CALCULATED / R20_1_AUTHORIZED / R20_3_HOLD`

## 0. Purpose

R20-0 is a governance correction only. It does **not** calculate a new ultimate load.

The user-approved R20 route is

\[
\boxed{
\text{Marguerre--Airy structural demand}
\rightarrow
\text{direct axial y-normal }(N_y,M_y)\text{ terminal}
\leftarrow
\text{Yun steel-shell + concrete/UHPC capacity resultants}
\rightarrow P_u=P_{pb}(q).
}
\]

The following two R19 handoff items were explicitly pending user acceptance and are now superseded as R20 next-task governance:

```text
D15_DIRECT_YUN_COMPILE_NEXT = SUPERSEDED_FOR_R20
GLOBAL_DIRECT_VIRTUAL_WORK_RJ_AS_STRUCTURAL_MAINLINE = SUPERSEDED_FOR_R20
```

This supersession does not declare the R18/R19 derivative algebra invalid. It changes only their role in the accepted production architecture.

## 1. Frozen structural architecture

Primary governance source:

`semantic_v2/40_execution/20260823_0322__NZSCCM__MARGUERRE_AIRY_TERMINAL_CAPACITY_ARCHITECTURE_CORRECTION.md`

Retained identities:

```text
STRUCTURAL_FRONT = FULL_2D_MARGUERRE_AIRY
TERMINAL_OBJECT = AXIAL_Y_NORMAL_Ny_My
MA_V1_MONOTONE_POSTBUCKLING = TRUE
GLOBAL_GEOMETRIC_FOLD_REQUIRED = FALSE
CURRENT_MATERIAL_INTO_AIRY_COMPATIBILITY = NO
NONLINEAR_CURRENT_MATERIAL_GLOBAL_WORK_CLOSURE = NOT_R20_ROUTE
LOCAL_detJsec_AS_PLATE_Pu = REJECTED
FORMAL_SPATIAL_QUADRATURE = 0
THICKNESS_QUADRATURE = 0
MATERIAL_POINTS = 0
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
```

The structural demand law is

\[
P_{pb}(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0),
\]

\[
n_d(s;q)=\frac{P_{pb}(q)}{b}+Gq(q+2q_0)(1-2s^2),
\qquad
m_d(s;q)=J_yqs.
\]

The Airy field remains fully two-dimensional. `Nx`, `Mx`, `Nxy`, `Mxy` are not deleted from the structural solution; only the hard terminal of the selected symmetric axial y-normal cut is `(Ny,My)`.

## 2. Yun steel-shell role

Primary historical source:

`semantic_v2/40_execution/steel_shell/20260818_1421__NZSCCM__Z1_Z4__UNIFIED_YUN_IDEAL_EP_LOCAL_AMPLITUDE_FULL_RECALC.md`

Retained current steel law:

\[
\sigma_s=\operatorname{clip}(E_s\varepsilon_s,-f_y,+f_y).
\]

Retained local geometry/current coordinate:

\[
\phi_i=\left(1-\cos\frac{2\pi x_i}{B_s}\right)
\left(1-\cos\frac{2m_i\pi y}{\ell}\right),
\]

\[
\varepsilon_s=\varepsilon_y^g
+A_i(w_{0,y}^g+\Delta w_{,y}^g)\phi_{i,y}
+A_{0i}\Delta w_{,y}^g\phi_{i,y}
+\left(A_{0i}A_i+\frac12A_i^2\right)\phi_{i,y}^2.
\]

Retained always-on local amplitude equation:

\[
\boxed{
R_{A_i}=C_\sigma\left[
 k_{cr}A_i+H(2A_{0i}A_i+A_i^2)(A_i+A_{0i})
\right]-\bar\sigma_{c,i}(A_i+A_{0i})=0.
}
\]

Governance:

```text
YUN_STEEL_SHELL_MODULE = ALWAYS_ON
SIGMA_CR_OVER_FY = DIAGNOSTIC_ONLY
YIELD_ORDERING = DIAGNOSTIC_ONLY
WHOLE_FACE_Et_ZERO_SWITCH = NOT_USED
LOCAL_Ai = CURRENT_LOCAL_ALGEBRAIC_COORDINATE
LOCAL_Ai_AS_NEW_GROSS_RITZ_MODE = NO
LOCAL_Ai_HISTORY_STATE = NO
```

## 3. R19 role retained and restricted

R19 remains the canonical bridge for the global strain basis, scaling, nested coordinates and derivative audit.

Retain

\[
A_y=\frac{\nu}{4}-\frac{k^2}{2}\sin^2X-\frac{\nu}{2}\sin^2Y+k^2\sin^2X\sin^2Y,
\]

\[
e_y=-D+\alpha A_y
+\frac{\pi^2k^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right)F_y
+\frac{\pi^2t_rk^2}{2\varepsilon_0b}qH_s\zeta,
\]

and the nested coordinate identity

\[
\boxed{x_g=iB_s+x_i}.
\]

Therefore

```text
R19_KINEMATIC_SCALING_COORDINATE_BRIDGE = RETAIN
R19_DERIVATIVE_AUDIT = RETAIN
R19_GLOBAL_VIRTUAL_WORK_CLOSURE_AS_R20_MAINLINE = NO
R19_D15_NEXT_HANDOFF = SUPERSEDED
```

## 4. Source/interface ledger

| Object | Source | R20 role |
|---|---|---|
| Airy `Ppb(q), n(s;q), m(s;q)` | 20260823_0322 + R07 | **production structural demand** |
| axial y-normal `(Ny,My)` terminal identity | R03/R07 | **production terminal** |
| Z0--Z6 forward structural coefficients | R07 | **production input for corresponding Z case** |
| historical Yun steel strain / `R_Ai` / ideal-EP | 20260818_1421 | **production steel-shell mechanism after interface closure** |
| R19 `Ay`, physical scaling, `xg=iBs+xi` | R19 | **production bridge/input field** |
| R19 virtual-work global `R,J` | R19 | diagnostic/scaffold only; **not R20 structural closure** |
| D15 compilation | historical/R19 handoff | **not R20 route** |
| R07 fixed plastic face-cap capacity | R07 | **pre-Yun regression baseline**, not final R20 steel phase |
| R15 static effective width | R15 | equivalence/provenance only; not new production mechanism |
| R16 `sigma_cr/fy` activation screen | R16 | diagnostic only; activation rule withdrawn |
| R14 Zhang UHPC peak terminal | R14 | later R20-3 UHPC physical candidate; R20-3 HOLD |
| R10A/R11/R12 | R10--R12 | later design/sensitivity comparators; R20-3 HOLD |

## 5. R20 direct terminal contract

R20-1 shall construct the steel and concrete/core terminal resultants directly on the selected y-normal cut. The formal target is

\[
\boxed{
F_N=N_y^{cap}(q,s,\text{finite current internal coordinates})-n_d(s;q)=0,
}
\]

\[
\boxed{
F_M=M_y^{cap}(q,s,\text{finite current internal coordinates})-m_d(s;q)=0,
}
\]

with

\[
N_y^{cap}=N_y^c+N_y^{s,Yun}+N_y^{web},
\qquad
M_y^{cap}=M_y^c+M_y^{s,Yun}+M_y^{web},
\]

and all required local algebraic equations

\[
R_{A_i}=0.
\]

No D15 layer and no global material virtual-work residual are allowed between the Airy structural demand and this terminal contact.

**Important closure gate:** R20-1 may proceed to numerical Z1/Z4 only after the repository sources uniquely define how the historical Yun area/strip stress field is converted to the work-conjugate y-normal cut resultants `Ny,My` without double counting the gross Airy mode. If that mapping is not source-closed, execution must stop at the exact missing identity rather than invent a new section law.

## 6. R20-2 acceptance rule

Only Z1 and Z4 are authorized in R20-2.

The historical unified-Yun results

```text
Z1 14.44689544 MN
Z4 52.43155584 MN
```

are closed during current root solving and may be opened only afterwards as regression comparators.

Likewise Zhou/Winter/test/FE values are not used in mode choice, parameter selection, local-amplitude solution, candidate generation, root selection or control-location selection.

```text
R20_0 = COMPLETE
R20_1 = AUTHORIZED
R20_2_Z1_Z4 = AUTHORIZED_AFTER_R20_1_CLOSURE
R20_3_FULL_BATCH = HOLD
NEW_FITTED_FACTOR = NO
Pu_CHANGED_IN_R20_0 = NO
```
