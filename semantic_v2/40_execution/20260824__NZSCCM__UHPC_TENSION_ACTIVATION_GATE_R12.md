# NZ-SCCM — UHPC tensile-resultant activation gate R12

**Date:** 2026-08-24  
**Status:** `EXECUTED / HIEW_TENSION_SOURCE_ADMISSIBLE / TENSION_INACTIVE_AT_ALL_7_CONTROL_ROOTS / R11_ROOTS_UNCHANGED / ZERO_QUADRATURE`

## 0. Purpose and locked architecture

R12 executes the next gate identified after R11: add the source-supported UHPC tensile branch to the same strain-compatible steel-shell/UHPC section terminal, without reopening the structural front.

```text
STRUCTURAL_FRONT = FULL_2D_MARGUERRE_AIRY
TERMINAL_OBJECT = AXIAL_Y_NORMAL_Ny_My
Nx_Mx_IN_STRUCTURAL_FIELD = YES
Nx_Mx_HARD_TERMINAL_ON_Y_CUT = NO
FORMAL_SPATIAL_QUADRATURE = 0
THICKNESS_QUADRATURE = 0
MATERIAL_POINTS = 0
COMPARATOR_IN_ROOT_SELECTION = 0
```

The R11 compression law, external-face steel law, distributed-web steel law, structural coefficients and finite control-location rule are unchanged.

## 1. Tensile source identity

The admissible tensile source is Hiew et al. (2024), *A unified tensile constitutive model for mono/hybrid fibre-reinforced ultra-high-performance concrete (UHPC)*. The project evidence archive records the direct-tension model as

```text
elastic -> strain hardening -> peak -> localisation -> fibre-pullout decay
```

and retains the source Table-7 parameter sets for the 2% straight, hooked-end and hybrid fibre families.

Those three 2% families do **not** have identical peak/localisation strains. Therefore R12 does not choose one Hiew family by comparison with T120/T360/BH ultimate loads.

This turns out not to be a blocker, because the tensile law is never activated at any current controlling root.

## 2. Exact activation condition

R11 uses one plane-section axial strain field through the complete section:

\[
\varepsilon(y)=\varepsilon_{cu}-\kappa y,
\qquad
\varepsilon_{cu}=0.0035,
\qquad
0\le y\le t_c=42\ \mathrm{mm}.
\]

With the R11 sign convention, positive strain is compression. UHPC tension can therefore begin only when the bottom UHPC-core fibre reaches zero strain:

\[
\varepsilon(t_c)=0.
\]

Hence the exact tensile-activation curvature is

\[
\boxed{
\kappa_t=\frac{\varepsilon_{cu}}{t_c}
=\frac{0.0035}{42}
=8.333333333333\times10^{-5}\ \mathrm{mm}^{-1}.
}
\]

For every state satisfying

\[
0\le\kappa<\kappa_t,
\]

the complete UHPC core remains in compression. On that interval the Hiew tensile resultant is identically zero, independent of fibre family and independent of the detailed post-localisation law.

## 3. R11 roots against the tensile-activation front

|Case|R11 \(\kappa_u\) / mm^-1|\(\kappa_u/\kappa_t\)|bottom-core strain|tension active?|
|---|---:|---:|---:|---|
|T120|4.979774776e-5|0.597573|0.00140849|NO|
|T360|5.145272562e-5|0.617433|0.00133899|NO|
|BH005|2.758413669e-5|0.331010|0.00234147|NO|
|BH010|3.239444538e-5|0.388733|0.00213943|NO|
|BH020|4.119300501e-5|0.494316|0.00176989|NO|
|BH032|5.086216664e-5|0.610346|0.00136379|NO|
|BH050|6.855138326e-5|0.822617|0.000620842|NO|

Thus all seven controlling R11 section states remain strictly on the compression-only side of the tensile front.

A second exact onset check was made using the same R11 clipped-affine section primitives. At \(\kappa=\kappa_t\), the section axial resultant has already dropped well below the axial resultant at every controlling R11 root:

|Case|\(N_y\) at R11 root N/mm|\(N_y\) at tensile onset N/mm|margin N/mm|
|---|---:|---:|---:|
|T120|7312.106945|4782.290741|2529.816204|
|T360|6614.264322|4281.134869|2333.129453|
|BH005|9007.365071|5370.361460|3637.003611|
|BH010|8259.160764|4850.835407|3408.325357|
|BH020|7651.896017|4591.072422|3060.823595|
|BH032|6630.111828|4255.341261|2374.770567|
|BH050|5103.410893|4015.494532|1087.916361|

The corresponding positive bending capacity at tensile onset is also above the already controlling R11 bending demand for every case. A diagnostic continuation through all three Hiew 2% source families found no earlier tension-active terminal root; the first controlling root remains the existing compression-only R11 root.

The production conclusion itself does not depend on that diagnostic sampling: the controlling roots lie before the tensile activation front, so the actual R12 resultant evaluated at those roots is exactly the R11 resultant.

## 4. R12 rerun results

Therefore

\[
\boxed{P_u^{R12}=P_u^{R11}}
\]

for all seven cases.

|Case|R12 Pu / MN|Comparator / MN|error|
|---|---:|---:|---:|
|T120|11.78605439|12.6378|-6.740%|
|T360|10.65015268|10.9688|-2.905%|
|BH005|2.25203558|2.3558|-4.405%|
|BH010|4.13093221|4.3043|-4.028%|
|BH020|7.66340795|8.0076|-4.298%|
|BH032|10.66798371|10.9905|-2.935%|
|BH050|13.25612091|12.2198*|+8.481%|

`*` BH050 retains its lower-confidence comparator identity.

For the six higher-confidence cases T120/T360/BH005/BH010/BH020/BH032:

\[
\boxed{\text{mean signed}=-4.218\%},
\]

\[
\boxed{MAE=4.218\%,\qquad RMSE=4.408\%}.
\]

These statistics are unchanged from R11.

## 5. What R12 falsifies

R11 proposed a plausible next explanation for its systematic conservative shift: UHPC tension had been suppressed. R12 now shows that this mechanism is **not active at the seven controlling states**.

Therefore the statement

```text
R11 negative bias is primarily caused by omitted UHPC tensile resultant
```

is rejected for the present seven-case steel-shell UHPC set.

This is a useful negative result: it prevents an unnecessary fibre-family selection and prevents a tensile law from being introduced merely to improve structural ultimate-load agreement.

## 6. TC compression-softening decision

The next step is **not** to apply Liu/Leutbecher TC softening as an accuracy correction.

The primary six R12 predictions are already low by approximately 3--7%. A TC compression-softening modifier would reduce available longitudinal UHPC compression and would therefore move the current primary-six bias further downward unless another independently justified mechanism offsets it.

Accordingly:

```text
LIU_LEUTBECHER_TC_PHYSICAL_EVIDENCE = RETAIN
TC_SOFTENING_AS_NEXT_ERROR_CORRECTION = NO
TC_SOFTENING_SOURCE_AUDIT = DEFERRED
```

This does not deny the physical TC effect. It only prevents using it in the wrong role.

## 7. New primary question exposed by R12

The remaining systematic low bias appears only after R10-A is replaced by the source-faithful R11 FHWA strain-compatible compression diagram:

- R10-A rigid `0.85 fc` screening block: primary-six MAE about 2.53%;
- R11/R12 exact FHWA compression design diagram: primary-six MAE about 4.22%, all six on the low side.

The next source-role gate is therefore:

\[
\boxed{
\text{Is FHWA }\alpha_u=0.85\text{ a design-level compression reduction being used as if it were a physical material terminal?}
}
\]

That question must be resolved before another physical reduction is added.

Recommended next task:

```text
R13 = FHWA_ALPHA_U_DESIGN_VS_PHYSICAL_TERMINAL_ROLE_GATE
```

R13 must:

1. keep the full 2D Marguerre-Airy structural front frozen;
2. keep the `Ny-My` terminal identity frozen;
3. distinguish design resistance from physical material response;
4. audit the comparator identity (Abaqus/experiment vs design resistance);
5. if a physical compression law is required, insert a source-supported UHPC uniaxial compression law into the **same exact strain-compatible resultant envelope**;
6. use no panel-load fitting, no material points and no thickness quadrature.

## 8. Decision

```text
R12_UHPC_TENSION_GATE = PASS_COMPLETE
HIEW_TENSION_SOURCE = ADMISSIBLE
HIEW_FIBRE_SERIES_SELECTION_FOR_CURRENT_7_ROOTS = NOT_REQUIRED
UHPC_TENSION_ACTIVE_AT_CURRENT_CONTROL_ROOTS = NO
R12_ROOTS_DIFFER_FROM_R11 = NO
R12_PRIMARY6_MEAN_SIGNED = -4.218 percent
R12_PRIMARY6_MAE = 4.218 percent
R12_PRIMARY6_RMSE = 4.408 percent

MARGUERRE_AIRY_STRUCTURAL_FRONT_REOPEN = NO
Ny_My_TERMINAL_REOPEN = NO
FORMAL_SPATIAL_QUADRATURE = 0
THICKNESS_QUADRATURE = 0
MATERIAL_POINTS = 0

NEXT_PRIMARY = R13_FHWA_ALPHA_U_DESIGN_VS_PHYSICAL_TERMINAL_ROLE_GATE
NEXT_SECONDARY = TC_SOFTENING_ONLY_AFTER_SOURCE_ROLE_RESOLUTION
```
