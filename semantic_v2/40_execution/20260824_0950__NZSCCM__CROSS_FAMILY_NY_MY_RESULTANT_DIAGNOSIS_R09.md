# NZ-SCCM — RC / steel-shell NC / steel-shell UHPC cross-family `Ny-My` diagnosis R09

**Date:** 2026-08-24 09:50 +08:00  
**Status:** `CROSS_FAMILY_BASELINE_COMPLETE / NO_TUNING_PERFORMED`

## 1. Frozen common architecture

```text
STRUCTURAL_FRONT = FULL_2D_MARGUERRE_AIRY
TERMINAL_OBJECT = AXIAL_Y_NORMAL_Ny_My
Nx_Mx_IN_STRUCTURE = YES
Nx_Mx_AS_HARD_TERMINAL_ON_Y_CUT = NO
MATERIAL_POINTS = 0
FORMAL_SPATIAL_QUADRATURE = 0
COMPARATOR_IN_ROOT_SELECTION = 0
```

## 2. RC baseline

Selected eight Swartz panels, R05:

- mean signed error: +3.18%;
- MAE: 9.28%;
- RMSE: 9.72%.

The current Brøndum-Nielsen-type RC resultant terminal remains the RC baseline; no RC tuning is reopened here.

## 3. Steel-shell ordinary concrete baseline

R07 reproduces the finite Z `Ny-My` plastic-resultant architecture.

Against Zhou:

- mean signed: +3.88%;
- MAE: 4.97%.

Against Winter:

- mean signed: −4.06%;
- MAE: 7.59%.

Z0–Z5 remain reasonably bounded by the comparator scale; Z6 remains high by about 12–14% and is retained as a visible outlier.

## 4. Steel-shell UHPC baseline

R08 is fully calculable but systematically high. For the six higher-confidence Abaqus comparators T120/T360/BH005–BH032:

- mean signed: +9.11%;
- MAE: 9.11%;
- RMSE: 9.83%.

Bias increases strongly with the stability-sensitive BH sequence:

\[
+4.23\%,\ +6.63\%,\ +8.86\%,\ +13.95\%
\]

for BH005, BH010, BH020 and BH032 respectively.

## 5. Cross-family decision

The common structural front survives this comparison. The strongest common signal is instead in the **terminal capacity representation**:

- RC: no decisive systematic sign bias;
- ordinary-concrete steel shell: generally reasonable, one Z6 high outlier;
- UHPC steel shell: systematic positive bias under the simplest rectangular UHPC compression block.

Therefore:

```text
MARGUERRE_AIRY_STRUCTURAL_FRONT = RETAIN
Ny_My_TERMINAL_IDENTITY = RETAIN
POINTWISE_MATERIAL_OPERATOR = DO_NOT_REOPEN

NEXT_RESEARCH_OBJECT = RESULTANT_CAPACITY_LAW
FIRST_PRIORITY = UHPC_COMPRESSION_RESULTANT_BLOCK / ATTAINABLE_N-M_ENVELOPE
SECOND_PRIORITY = Z6_OUTLIER_DIAGNOSIS
RC_RETUNING = DEFER
```

No reduction factor, empirical fit, comparator-based coefficient, or root reselection is introduced in R09.