# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-25 08:51 +08:00  
**Status:** `MARGUERRE_AIRY_EXPLICIT_RETAINED / AIRY_USES_INITIAL_FULL_COMPOSITE_ABD / STEEL_OFFSET_STIFFNESS_LOCKED / SSNC_R02_FULL_RESULTANT_RETAINED / SSNC_R03_CURRENT_6X6_TANGENT_DIAGNOSTIC_ONLY / SSNC_R04_IDEAL_EP_2D_TERMINAL_GATE_PASS / POST_YIELD_TANGENT_NOT_A_Pu_GATE / Pu_NOT_YET_RECALCULATED`

> Architecture correction: the accepted explicit Marguerre–Airy production route requires the **initial elastic full-section** `A0,B0,D0` to generate the structural demand family. Current postbuckling/yield tangent degradation is not fed back into the Airy compatibility/Galerkin operator. Steel nonlinearity acts at the terminal resultant-capacity layer. Therefore the R03 current 6x6 tangent remains mechanically valid but is no longer a prerequisite for `Pu`.

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

No new Z0–Z6 `Pu` has yet been promoted after the R04 correction.

## 1. Correct role separation

The steel shell enters the theory twice, in different roles:

```text
ROLE A — STRUCTURAL DEMAND
initial elastic steel stiffness
+ initial concrete/core stiffness
-> full composite A0,B0,D0
-> explicit Marguerre–Airy demand Ppb(q), N, M

ROLE B — TERMINAL CAPACITY
R02 biaxial PBL postbuckling trial stress/resultants
+ simplified ideal-EP 2D steel cap
+ concrete/core terminal resultants
-> terminal resultant intersection
-> Pu
```

These roles are not double counting.

## 2. Initial steel-face offset stiffness is mandatory

For a uniform layer centered at `z_c`,

\[
\mathbf A=\mathbf Q t,
\qquad
\mathbf B=\mathbf Q t z_c,
\]

\[
\boxed{
\mathbf D=\mathbf Q\left(tz_c^2+\frac{t^3}{12}\right).
}
\]

For the two external steel faces at `z_+=+z_f`, `z_-=-z_f`,

\[
\boxed{
\mathbf D_s^0
=2\mathbf Q_s\left(t_sz_f^2+\frac{t_s^3}{12}\right).
}
\]

The offset/parallel-axis term

\[
\boxed{2\mathbf Q_st_sz_f^2}
\]

is therefore included exactly in the initial Airy bending stiffness.

For a symmetric shell,

\[
\mathbf B_s^0=0,
\]

but this cancellation of `B` does **not** remove the large offset contribution to `D`.

### Executed offset gate

Using the source-audited reduced DSCW gate geometry (`h=130 mm`, `ts=4 mm`, `zf=63 mm`) gives

```text
B0_sym_abs                    = 0.000000000000e+00
Dsteel_parallel_axis_abs      = 4.768371582031e-07
Dsteel_direct_integral_abs    = 9.536743164062e-07
Dsteel11_full_Nmm             = 7.190230036630e+09
Dsteel11_offset_Nmm           = 7.187815384615e+09
Dsteel11_own_skin_Nmm         = 2.414652014652e+06
offset_fraction_of_steel_D11  = 9.996641759718e-01
steel_fraction_of_total_D11   = 5.839512724645e-01
```

Thus roughly `99.9664%` of the steel-face `D11` in this gate state comes from physical offset rather than the own-skin `t_s^3/12` term.

Any coefficient generator that retains only `Et_s^3/12` for the external faces is invalid.

## 3. SSNC-R02 retained role

R02 remains the active pre-yield/current steel-shell stress/resultant kernel:

- full physical steel area;
- biaxial normal coupling;
- finite local PBL amplitude equation;
- finite Airy harmonic redistribution;
- pointwise 2D Mises diagnostic;
- exact Yun uniaxial `kcr/kp` degeneration.

Artifact:

`semantic_v2/40_execution/steel_shell/20260825_0130__NZSCCM__SSNC_R02_PBL_2D_FULL_RESULTANT_GATE.md`

## 4. SSNC-R03 role is downgraded from Pu gate to diagnostic

R03 proved the exact elastic-material postbuckling current tangent

\[
\mathbf A_{pb}^{tan}
=\mathbf A_e-\frac{\mathbf h\mathbf h^{\mathsf T}}{k_U},
\]

and the two-face current 6x6 tangent with

\[
\mathbf D_s^{current}
=z_+^2\mathbf A_+^{pb}+z_-^2\mathbf A_-^{pb}
+\mathbf D_{skin,e}^++\mathbf D_{skin,e}^-.
\]

This remains a valid mechanics result and useful future/current-stability diagnostic.

However, under the accepted explicit Airy architecture:

```text
R03_CURRENT_6X6_TANGENT_AS_Pu_GATE = NO
R03_CURRENT_6X6_TANGENT_AS_DIAGNOSTIC = YES
POST_FIRST_YIELD_6X6_TANGENT_REQUIRED_BEFORE_Z_Pu = NO
```

Artifact:

`semantic_v2/40_execution/steel_shell/20260825_0746__NZSCCM__SSNC_R03_CURRENT_6X6_TANGENT_GATE.md`

## 5. SSNC-R04 simplified ideal-EP 2D terminal

The user-authorized simplification is now frozen for the terminal steel layer.

### 5.1 No through-thickness plastic partition

Each external steel face is treated as one homogenized membrane layer at its physical centroid `z_f`.

The terminal gross bending resultant is

\[
\boxed{\mathbf M_f=z_f\mathbf N_f}.
\]

The own-skin `Et_s^3/12` term is retained in the initial Airy `D0`, but no separate through-thickness plastic bending block is introduced at the terminal.

### 5.2 2D Mises cap

For a trial mean plane-stress state

\[
\boldsymbol\sigma^{tr}=(\sigma_x^{tr},\sigma_y^{tr},\tau_{xy}^{tr})^T,
\]

\[
\sigma_{vm}^{tr}
=\sqrt{(\sigma_x^{tr})^2-\sigma_x^{tr}\sigma_y^{tr}
+(\sigma_y^{tr})^2+3(\tau_{xy}^{tr})^2}.
\]

Define

\[
\boxed{
\lambda=\min\left(1,\frac{f_y}{\sigma_{vm}^{tr}}\right),
\qquad
\boldsymbol\sigma^{cap}=\lambda\boldsymbol\sigma^{tr}.
}
\]

Then

\[
\boxed{
\mathbf N_f=t_s\boldsymbol\sigma^{cap},
\qquad
\mathbf M_f=z_f\mathbf N_f.
}
\]

This is exact for the uniaxial ideal-perfectly-plastic degeneration and `x<->y` symmetric. For general biaxial/shear post-yield states it is explicitly classified as a **proportional-loading analytical approximation**, not a full history-dependent associated-J2 return map.

### 5.3 Post-yield tangent convention

Theory:

\[
E_t=0.
\]

Optional numerical regularization only if a solver requires it:

\[
E_t=\eta E_s,
\qquad \eta\sim10^{-8}\text{--}10^{-6}.
\]

This tangent is not fed into Airy. Yielded steel stress/resultants remain finite; only incremental tangent vanishes.

### Executed R04 gate

```text
SSNC_R04_IDEAL_EP_2D_TERMINAL_RESULTANT_GATE = PASS
AIRY_USES_INITIAL_ABD_ONLY = True
INITIAL_STEEL_OFFSET_STIFFNESS_INCLUDED = True
CURRENT_TANGENT_FEEDBACK_TO_AIRY = False
THROUGH_THICKNESS_PLASTIC_PARTITION = False
POST_YIELD_TANGENT_THEORY = 0.0
trial_vm_MPa = 374.032084185301
plastic_scale_lambda = 0.949116439498
capped_vm_MPa = 355.000000000000
uniaxial_capped_sy_MPa = 355.000000000000
xy_sym_abs = 0.000000000000e+00
```

Artifacts:

- report: `semantic_v2/40_execution/steel_shell/20260825_0851__NZSCCM__SSNC_R04_IDEAL_EP_2D_TERMINAL_RESULTANT_GATE.md`
- executable: `semantic_v2/40_execution/steel_shell/20260825_0851__NZSCCM__SSNC_R04_IDEAL_EP_2D_TERMINAL_RESULTANT_GATE.py`

## 6. Offset term is present in both stiffness and terminal moment, without double counting

Initial structural stiffness:

\[
\mathbf D_f^0
=\mathbf Q_s\left(t_sz_f^2+\frac{t_s^3}{12}\right).
\]

Terminal resisting moment:

\[
\mathbf M_f^{cap}=z_f\mathbf N_f^{cap}.
\]

The former is an elastic derivative used to generate the Airy demand path. The latter is the physical force lever arm in the terminal resistance state. They are different objects and both are required.

## 7. Current stopping point

Closed:

```text
initial full composite ABD including steel-face offset
-> explicit Airy structural demand

R02 biaxial PBL trial stress/resultants
-> R04 ideal-EP 2D Mises terminal cap
-> top/bottom face terminal N,M with physical lever arms
```

Still to execute before new Z0–Z6 results are promoted:

```text
1. regenerate/audit each Z specimen's initial Airy coefficients with the explicit full-section ABD formula;
2. connect the R02 trial steel resultants to the R04 ideal-EP terminal cap;
3. combine with the unchanged NC terminal resultants;
4. solve the unchanged Airy demand/resultant-capacity intersection;
5. only after predictions are fixed, open Zhou/Winter comparators.
```

No post-first-yield 6x6 tangent derivation is required as a prerequisite.
