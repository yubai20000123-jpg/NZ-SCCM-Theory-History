# NZ-SCCM — UHPC resultant compression-block source gate R10

**Date:** 2026-08-24  
**Status:** `SOURCE_GATE_PASS / FHWA_085_SCREEN_EXECUTED / NO_PANEL_CALIBRATION`

## 0. Locked architecture

This gate does not reopen the structural front or pointwise material model.

```text
STRUCTURAL_FRONT = FULL_2D_MARGUERRE_AIRY
TERMINAL_OBJECT = AXIAL_Y_NORMAL_Ny_My
Nx_Mx_IN_STRUCTURAL_FIELD = YES
Nx_Mx_HARD_TERMINAL_ON_Y_CUT = NO
MATERIAL_POINTS = 0
THICKNESS_QUADRATURE = 0
COMPARATOR_IN_PARAMETER_SELECTION = 0
```

The question is only whether the R08 UHPC core bound

\[
0\le r_c(z)\le(1-\rho_w)f_c
\]

is an appropriate production resultant-capacity identity.

---

## 1. Source audit

### 1.1 FHWA-HRT-23-077

The FHWA UHPC structural-design framework requires equilibrium and strain compatibility for strength calculations and uses the UHPC uniaxial compression design model. In the worked flexural example, the compression model is defined by

\[
\alpha_u f'_c,\qquad \alpha_u=0.85,
\]

with

\[
\varepsilon_{cp}=\frac{\alpha_u f'_c}{E_c},
\qquad
\varepsilon_{cu}=0.0035.
\]

FHWA explicitly identifies `alpha_u=0.85` as a reduction accounting for the nonlinearity of the UHPC compressive stress-strain response. It is separate from the global resistance factor `phi`.

Therefore a full-strength perfectly plastic UHPC block at `fc` is not the source-faithful FHWA compression design representation.

### 1.2 Leutbecher 2020

The UHP(FR)C biaxial panel program shows that transverse tension/cracking reduces compression-strut strength and stiffness. The reduction is already pronounced at small transverse tensile strain/crack width and then tends to stabilize. Fiber-reinforced panels show less reduction than plain UHPC, but the reduction does not disappear.

### 1.3 Liu et al. 2023

The PBET tension-compression tests give a principal-tensile-strain-dependent compression softening law. In the recovered formula the stress-softening coefficient is already below unity in the small-tensile-strain regime and decreases further at larger tensile strain. Thus local transverse tension can reduce the attainable longitudinal compression even though `Nx` is not imposed as an independent hard terminal coordinate on the y-normal cut.

### 1.4 Diab & Ferche 2026

The UHPC-specific compression-softening model is introduced as necessary for realistic structural response, and the influence of compression softening on analytical accuracy depends on the magnitude of compressive stress.

### 1.5 Gate conclusion

The R08 full-`fc` rectangle is retained only as an upper-bound diagnostic. It is rejected as the current production UHPC resultant terminal because two independent source mechanisms make it systematically generous:

1. even uniaxial UHPC compression is not represented by a full-`fc` perfectly plastic block in the FHWA design model;
2. transverse tensile strain/cracking further reduces compression capacity in biaxial TC states.

---

## 2. First source-supported resultant replacement: FHWA reduced plateau

Without changing the R08 bounded-resultant allocation architecture, replace only the UHPC core upper bound by

\[
\boxed{
0\le r_c(z)\le(1-\rho_w)\alpha_u f_c,
\qquad \alpha_u=0.85.
}
\]

Then

\[
w_c^{85}=(1-\rho_w)(0.85f_c)+2\rho_w f_y,
\]

and

\[
N_U^{85}=(1-\rho_w)(0.85f_c)t_c
+\rho_wf_yt_c+2f_{c,s}t_s.
\]

All steel-face caps, web-steel bounds, Marguerre-Airy coefficients, halfwaves, control-location search, and root rules remain unchanged.

This preserves a finite resultant-only calculation. No material point, thickness quadrature, loading history, or panel-load calibration is introduced.

---

## 3. R10-A screening results

`alpha_u=0.85` was fixed from the FHWA source before the Abaqus comparator errors were evaluated. It was not fitted to T120/T360/BH results.

| Case | R08 full-fc Pu / MN | R10-A FHWA-0.85 Pu / MN | change | Abaqus / MN | R10-A error |
|---|---:|---:|---:|---:|---:|
| T120 | 13.517551912 | 12.358048731 | -8.578% | 12.6378 | -2.214% |
| T360 | 12.506475456 | 11.285025825 | -9.767% | 10.9688 | +2.883% |
| BH005 | 2.455396391 | 2.282621069 | -7.037% | 2.3558 | -3.106% |
| BH010 | 4.589632993 | 4.180681309 | -8.910% | 4.3043 | -2.872% |
| BH020 | 8.717470347 | 7.894459281 | -9.441% | 8.0076 | -1.413% |
| BH032 | 12.523899913 | 11.288779587 | -9.862% | 10.9905 | +2.714% |
| BH050 | 15.917403879 | 14.605880557 | -8.240% | 12.2198* | +19.526% |

`*` BH050 comparator remains lower confidence and is excluded from the primary six-case statistics.

For T120/T360/BH005/BH010/BH020/BH032:

### R08 full-fc block

\[
\text{mean signed}=+9.109\%,
\qquad
MAE=9.109\%,
\qquad
RMSE=9.832\%.
\]

### R10-A FHWA 0.85 block

\[
\boxed{\text{mean signed}=-0.668\%},
\]

\[
\boxed{MAE=2.534\%,\qquad RMSE=2.597\%}.
\]

This numerical improvement is validation evidence only. It is not used to choose or adjust `alpha_u`.

BH005 changes controlling identity under the 0.85 block: the axial upper-bound/squash candidate occurs before the previous moment-intersection candidate. This is retained rather than forcing the previous branch.

---

## 4. Why the 0.85 rectangle is not yet the final physical law

FHWA itself does not define a universal rigid-plastic rectangular `N-M` surface. Its strength framework is strain-compatible and uses an elastic-to-reduced-plateau compression model with an ultimate compression strain.

For the current project UHPC values

\[
f_c=141.1\ \text{MPa},\qquad E_c=43.4\ \text{GPa},
\]

\[
\varepsilon_{cp}=\frac{0.85f_c}{E_c}
=0.00276348,
\qquad
\varepsilon_{cu}=0.0035.
\]

If a compression zone of depth `c` terminates at zero strain and the extreme compression strain is `epsilon_c > epsilon_cp`, define

\[
\lambda=\frac{\varepsilon_{cp}}{\varepsilon_c}.
\]

Closed-form integration of the FHWA elastic-perfectly-plastic compression diagram gives

\[
C_c=0.85f_c c\left(1-\frac{\lambda}{2}\right),
\]

and centroid from the compressed face

\[
\bar y
=c\frac{\lambda^2/6-\lambda/2+1/2}{1-\lambda/2}.
\]

At `epsilon_c=epsilon_cu`,

\[
\lambda=0.7895655,
\]

which is equivalent for this particular zero-strain neutral-axis case to a matched rectangle

\[
\beta_{eq}=0.691056,
\qquad
\alpha_{eq}=0.744418,
\]

with total force

\[
C_c=0.514435 f_c c.
\]

This equivalent rectangle is **not** declared a universal terminal block, because highly compressed `N-M` sections can be fully in compression and need not terminate at zero strain.

Therefore the more rigorous next refinement is an analytic strain-compatible resultant envelope in `(epsilon_0,kappa)` followed by elimination to `(N_y,M_y)`. This remains zero-quadrature and resultant-level because every thickness integral of the clipped linear-strain EPP law is elementary and closed form.

---

## 5. TC softening remains a second, separate gate

The Leutbecher/Liu evidence supports an additional dependence of the longitudinal UHPC compression capacity on transverse tensile state. This must not be implemented by restoring `Nx` as a hard y-cut terminal equality.

The correct architecture is instead

\[
\boxed{
\mathcal C_{NyMy}
=\mathcal C_{NyMy}(\text{transverse Airy state})
}
\]

where the y-cut capacity surface can be parametrically softened by a source-supported transverse tensile strain/crack measure.

A production TC modifier is not frozen in R10 because the mapping

\[
\text{Airy transverse resultant/state}
\to
\varepsilon_t\text{ or crack measure}
\]

must first be derived without reintroducing material points or an arbitrary local state sampler.

---

## 6. Decision

```text
UHPC_FULL_FC_RECTANGULAR_BLOCK = RETAIN_UPPER_BOUND_DIAGNOSTIC_ONLY
UHPC_FULL_FC_BLOCK_AS_PRODUCTION_TERMINAL = REJECT

FHWA_ALPHA_U = 0.85
FHWA_085_RESULTANT_BLOCK_SOURCE_GATE = PASS
FHWA_085_CROSS_FAMILY_SCREEN = PASS_STRONG
PANEL_LOAD_FITTING = NONE

FHWA_EXACT_STRAIN_COMPATIBLE_RESULTANT_ENVELOPE = NEXT_PRIMARY_REFINEMENT
LIU_LEUTBECHER_TC_RESULTANT_SOFTENING = NEXT_SECONDARY_GATE

STRUCTURAL_FRONT_REOPEN = NO
Ny_My_TERMINAL_REOPEN = NO
POINTWISE_MATERIAL_OPERATOR_REOPEN = NO
THICKNESS_QUADRATURE = 0
```

R10 does not claim that `0.85` is a newly calibrated physical material constant for this specific UHPC. It is a source-specified FHWA compression-design reduction that, when transferred without fitting into the current resultant architecture, removes nearly all of the systematic high bias in the six higher-confidence steel-shell UHPC comparisons. The next theorem-level task is to replace the reduced rectangle by the exact closed-form FHWA strain-compatible `N-M` envelope and then test whether the TC modifier is still needed.