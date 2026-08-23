# NZ-SCCM — Membrane work-conjugacy + axial-cut terminal gate R03

**Time:** 2026-08-24 07:16 +08:00  
**Status:** `MEMBRANE_WORK_CONJUGACY = PASS / HARD_Nx_TERMINAL = REJECTED_FOR_AXIAL_CUT / AXIAL_Y_NORMAL_CUT_Ny_My = SELECTED / FULL_2D_AIRY = RETAINED / SWARTZ8_ONLY`

## 0. Scope

Only the fixed common set

\[
\{4,5,6,8,9,14,21,23\}
\]

is considered. The Marguerre–Airy structural front end, representative halfwaves, corrected reinforcement mapping, resultant-only Brøndum-Nielsen-family capacity assumptions, and finite active-set elimination are unchanged.

This gate answers one question left open by R02:

> Is the local Airy transverse membrane resultant `Nx` an independent terminal-capacity coordinate for the current uniaxially loaded axial-wall collapse problem?

The answer is **no for the selected axial y-normal cut terminal**. This does not delete `Nx` from the 2D Airy structural field.

---

## 1. Source-level Airy evidence: `Nx` is compatibility generated, not an independent load coordinate

The classical FvK/Airy derivation already frozen in
`20260816_0007__NZSCCM__CLASSICAL_FVK_AIRY_POSTBUCKLING_LIMIT__THEORY.md`
starts from the single modal driver

\[
S=A^2+2A_0A.
\]

The compatibility-generated Airy coefficients are

\[
C_{20}=\frac{EtS\beta^2}{32\alpha^2},\qquad
C_{02}=\frac{EtS\alpha^2}{32\beta^2},
\]

so their ratio is fixed by compatibility. The resulting membrane field contains

\[
N_y=-N-\frac{EtS\beta^2}{8}\cos 2\alpha x,
\qquad
N_x=-\frac{EtS\alpha^2}{8}\cos 2\beta y.
\]

The source file explicitly rejects treating the two harmonics as independent generalized coordinates. The valid chain is

\[
w_0,w_a\to S\to\Phi(S)\to(N_x,N_y,N_{xy})\to\text{transverse equilibrium}.
\]

The Zhou mixed-boundary audit
`20260816_0016__NZSCCM__ZHOU_BOUNDARY_FVK_AIRY_MIXED_BC__THEORY.md`
further shows that transverse Airy resultants are modified by homogeneous boundary corrections so that the free lateral sides satisfy

\[
N_x=N_{xy}=0.
\]

Thus the pointwise `Nx` field is an internal compatibility/boundary-response field, not an externally prescribed transverse membrane load.

---

## 2. Virtual-work classification of the axial cut

For membrane resultants the internal virtual work is

\[
\delta W_m=\iint_\Omega
\left(N_x\,\delta\varepsilon_x+N_y\,\delta\varepsilon_y+N_{xy}\,\delta\gamma_{xy}\right)dA.
\]

After membrane equilibrium is integrated by parts, the boundary/cut traction work is

\[
\delta W_\Gamma^m
=\int_\Gamma
\left[(n_xN_x+n_yN_{xy})\delta u
+(n_xN_{xy}+n_yN_y)\delta v\right]ds.
\]

For a section cut normal to the axial `y` direction,

\[
\mathbf n=(0,1),
\]

hence

\[
\boxed{
\delta W_{cut}^m
=\int\left(N_{xy}\delta u+N_y\delta v\right)dx.
}
\]

Therefore `Nx` is **not** a traction resultant on the y-normal cut. It acts on the perpendicular x-normal cut.

For the current symmetric control section,

\[
N_{xy}=0,
\]

so the only hard membrane resultant on the axial cut is

\[
\boxed{N_y}.
\]

The same distinction applies to bending. A y-normal cut carries the normal bending resultant `My` and twisting resultant `Mxy`; `Mx` belongs to the perpendicular cut. At the current symmetric control section

\[
M_{xy}=0,
\]

so the hard bending resultant of the axial cut is

\[
\boxed{M_y}.
\]

Thus the correct resultant vector for the present collapse cut is

\[
\boxed{\mathbf R_{cut}=(N_y,M_y)^T}.
\]

---

## 3. Why this does not make the structural theory one-dimensional

The structural field remains fully two-dimensional:

\[
q\to\Phi_{Airy}\to
(N_x,N_y,N_{xy},M_x,M_y,M_{xy})
\to P_{pb}(q).
\]

`Nx` and `Mx` remain in the Airy compatibility, postbuckling redistribution, stiffness, and global modal equilibrium. They are not set to zero and are not deleted from the structural solution.

Only the **terminal object** changes. Instead of asking whether one local shell point can reproduce the complete 2D resultant tuple as independent capacity coordinates, the present axial-collapse branch asks whether a y-normal section cut can transmit its work-conjugate cut resultants.

Hence

```text
FULL_2D_STRUCTURAL_FIELD = YES
UNIAXIAL_MATERIAL_THEORY = NO
TERMINAL_OBJECT = AXIAL_Y_NORMAL_SECTION_CUT
HARD_CUT_RESULTANTS = Ny, My
Nx, Mx = RETAINED_IN_2D_STRUCTURAL_FIELD / NOT_HARD_ON_THIS_CUT
```

This distinction also resolves the apparent conflict with the earlier projected-moment gate. `M_parallel=d_xMx+d_yMy` is the work-conjugate moment of a **local frozen shell-point bending mode**. It is a legitimate local shell-point reduction. It is not automatically the moment traction of a y-normal collapse cut. For the latter, the hard normal bending resultant is `My`.

---

## 4. Three-way numerical discrimination on the same capacity model

No material parameter, halfwave, Airy law, steel mapping, concrete strength, or test load is changed between the three variants:

A. `HARD_SHELL_POINT`: enforce `Nx + Ny + M_parallel` (R02 full resultant).

B. `Nx_RELEASE_PROJECTED_M`: release hard `Nx`, but retain the local shell-point `M_parallel` terminal.

C. `AXIAL_CUT`: enforce only the y-normal cut resultants `Ny + My`.

Variant B is evaluated with the same finite resultant bounds. With `Nx` released, the x-direction maximizing force allocation is explicit. For the common active family, using a bottom concrete compression block `c_b` and the highest positive-ordinate steel layer,

\[
M_x^+=f_cc_b\left(h-\frac{c_b}{2}\right)+z_+F_s,
\]

\[
T_y=N_y+f_cc_b,
\]

\[
M_y^+=f_cc_b\left(h-\frac{c_b}{2}\right)+z_+T_y,
\]

with

\[
0\le T_y\le F_s.
\]

The unconstrained projected-moment stationary depth is

\[
\boxed{
c_b^*=h+\frac{d_y}{d_x+d_y}z_+,
}
\]

clipped to the exact longitudinal-force admissibility interval

\[
\max\left(0,-\frac{N_y}{f_c}\right)
\le c_b\le
\min\left(t,\frac{F_s-N_y}{f_c}\right).
\]

Thus variant B also requires no generic optimizer.

|Case|hard shell-point Pu / kN|Nx-release + projected-M Pu / kN|axial-cut Ny-My Pu / kN|Pf / kN|
|---:|---:|---:|---:|---:|
|4|568.799|617.592|595.536|534.231|
|5|547.473|591.377|568.598|623.641|
|6|595.087|645.372|621.074|691.698|
|8|516.478|540.008|521.237|455.053|
|9|567.954|605.544|592.150|625.865|
|14|780.207|774.566|766.430|716.164|
|21|304.544|408.081|408.081|368.313|
|23|341.033|390.409|367.811|346.961|

Statistics:

```text
HARD_SHELL_POINT:
  mean signed = -3.1931 %
  MAE         = 10.4209 %
  RMSE        = 11.3831 %

Nx_RELEASE_PROJECTED_M:
  mean signed = +6.3287 %
  MAE         = 10.1082 %
  RMSE        = 11.2588 %

AXIAL_CUT_Ny_My:
  mean signed = +3.1777 %
  MAE         =  9.2835 %
  RMSE        =  9.7233 %
```

The Case21 penalty is entirely removed when hard `Nx` is released:

\[
304.544\to408.081\ \mathrm{kN}.
\]

However releasing `Nx` alone does not produce the best common-8 result. Keeping local shell-point `M_parallel` still includes the perpendicular-cut `Mx` capacity channel. The y-normal axial cut removes this remaining category mismatch and gives the lowest MAE/RMSE of the three controlled variants.

The 8-panel statistics are a consistency check, not the derivation of the gate. The gate itself comes from the cut virtual-work identity and the Airy compatibility structure; `Pf` is used only afterwards.

---

## 5. Gate decision

```text
MEMBRANE_WORK_CONJUGACY = PASS
Nx_AS_INDEPENDENT_EXTERNAL_GENERALIZED_FORCE = NO
Nx_AS_LOCAL_AIRY_INTERNAL_RESULTANT = YES
Nx_HARD_TERMINAL_EQUALITY_FOR_Y_NORMAL_CUT = REJECTED
Mx_HARD_TERMINAL_EQUALITY_FOR_Y_NORMAL_CUT = REJECTED

STRUCTURAL_FIELD = FULL_2D_MARGUERRE_AIRY
TERMINAL_OBJECT = AXIAL_Y_NORMAL_SECTION_CUT
HARD_MEMBRANE_TERMINAL = Ny
HARD_BENDING_TERMINAL = My
Nxy_Mxy_AT_CURRENT_SYMMETRIC_CONTROL = 0
CURRENT_RESULTANT_TERMINAL = Ny_My

LOCAL_SHELL_POINT_PROJECTED_M_TERMINAL = RETAIN_DIAGNOSTIC_ONLY
POINTWISE_CONCRETE_STRAIN_STRESS = NOT_REQUIRED
CC_TC_TT = NOT_REQUIRED
THICKNESS_MATERIAL_QUADRATURE = NOT_REQUIRED
GENERIC_OPTIMIZER = NOT_REQUIRED
```

This is **not** a claim that general shell-point biaxial capacity surfaces are invalid. It states that they are the wrong terminal object for the present axial y-normal collapse-cut mechanism unless a full 2D plastic/resultant redistribution analysis is introduced.

## 6. Current next step

Keep `Ny-My` as the selected terminal identity and do not reopen material-point constitutive mechanics. The remaining improvement problem is now strictly at the **resultant capacity law** level: audit the Brøndum-Nielsen R01/R02 simplifications (especially no compression-reinforcement credit and rectangular concrete compression blocks) against source-supported resultant-level extensions, without changing the Airy structural backbone or using test loads for calibration.
