# NZ-SCCM 多波钢壳01——BH032/BH050 相邻格室分类判定 R02

**Date:** 2026-09-03  
**Parent theory:** `20260903__NZSCCM__MULTIWAVE_STEEL_SHELL_01_NO_SHEAR_SLIP_FULL_DERIVATION_R01.md`  
**Parent execution:** `20260903__NZSCCM__MULTIWAVE_STEEL_SHELL_01_BH032_BH050_EXECUTION_REPORT_R01.md`

## 1. Correction of execution identity

The user's explicit physical rule is:

1. local longitudinal reference wavelength = same-side stiffener spacing `s`;
2. one complete global halfwave length = `L_G`;
3. reference lobe count `n0=floor(L_G/s)`;
4. an adjacent equal-width bay that also buckles takes `n0-1` or `n0+1`;
5. a bay that does not buckle is entered as full-thickness ideal-EP steel.

For BH032 and BH050:

\[
L_G/s=1/0.225=4.44444\ldots,\qquad \boxed{n_0=4}.
\]

Therefore the direct adjacency implementation for the regular equal-width bays is:

### TOP
Three regular equal-width bays. Taking the central bay as the reference `n0=4`, the two adjacent bays take the neighboring counts:

\[
\boxed{[3,4,5]}
\]

or its mirror `[5,4,3]`. Both have identical area-averaged N-M response because the generalized face strain and bay width are identical.

Thus TOP class counts are

\[
\boxed{(C_3,C_4,C_5)=(1,1,1)}.
\]

### BOTTOM
Four regular equal-width bays. The minimal symmetric/count-balanced continuation is represented by

\[
\boxed{[3,4,5,4]}
\]

or a mirror/permutation with the same counts. For the present face-average operator only the counts matter:

\[
\boxed{(C_3,C_4,C_5)=(1,2,1)}.
\]

The non-standard edge residual strips do not satisfy the equal-width adjacency condition and are retained as full-thickness ideal-EP E strips in this execution specialization.

Accordingly the `BALANCED` row in the R01 execution is promoted to

```text
DIRECT_ADJACENCY_INTERPRETATION
```

while `ALL_n0` remains a reference baseline, not the preferred physical interpretation of the user's adjacency rule.

## 2. Final direct-adjacency results

### BH032

\[
\boxed{q_u=0.001455923871048}
\]

\[
\boxed{P_u^{MW01-NS}=11.328790359\ \mathrm{MN}}
\]

Section state:

\[
\varepsilon_x^0=1.45318349\times10^{-4},
\quad
\kappa_x=1.99888417\times10^{-5}\ /\mathrm{mm},
\]

\[
\varepsilon_y^0=-2.49677858\times10^{-3},
\quad
\kappa_y=4.77724486\times10^{-5}\ /\mathrm{mm}.
\]

Constituent N-M:

UHPC:

\[
(N_x^U,M_x^U,N_y^U,M_y^U)
=(108.356013,3296.870299,-4495.339881,11730.495400).
\]

Steel shell:

\[
(N_x^s,M_x^s,N_y^s,M_y^s)
=(-68.303180,10864.675468,-2249.948913,2613.702184).
\]

Web:

\[
(N_y^w,M_y^w)=(-293.281795,43.753816).
\]

Total:

\[
\boxed{(N_x,M_x,N_y,M_y)
=(40.052832,14161.545767,-7038.570590,14387.951400)}.
\]

Face-average steel stresses:

\[
\boxed{(\bar\sigma_x^+,\bar\sigma_y^+)=(+50.5093,-267.0387)\ \mathrm{MPa}}
\]

\[
\boxed{(\bar\sigma_x^-,\bar\sigma_y^-)=(-67.5850,-295.4485)\ \mathrm{MPa}}.
\]

### BH050

\[
\boxed{q_u=0.005260095555391}
\]

\[
\boxed{P_u^{MW01-NS}=13.858459343\ \mathrm{MN}}
\]

Section state:

\[
\varepsilon_x^0=1.86497816\times10^{-5},
\quad
\kappa_x=4.48414469\times10^{-5}\ /\mathrm{mm},
\]

\[
\varepsilon_y^0=-2.13102622\times10^{-3},
\quad
\kappa_y=6.51892277\times10^{-5}\ /\mathrm{mm}.
\]

Constituent N-M:

UHPC:

\[
(N_x^U,M_x^U,N_y^U,M_y^U)
=(-235.653106,7841.768785,-3863.238104,16911.834737).
\]

Steel shell:

\[
(N_x^s,M_x^s,N_y^s,M_y^s)
=(466.259002,24952.908414,-1272.048699,15919.991046).
\]

Web:

\[
(N_y^w,M_y^w)=(-170.623714,297.895645).
\]

Total:

\[
\boxed{(N_x,M_x,N_y,M_y)
=(230.605896,32794.677198,-5305.910517,33129.721427)}.
\]

Face-average steel stresses:

\[
\boxed{(\bar\sigma_x^+,\bar\sigma_y^+)=(+193.8960,-72.4844)\ \mathrm{MPa}}
\]

\[
\boxed{(\bar\sigma_x^-,\bar\sigma_y^-)=(-77.3313,-245.5278)\ \mathrm{MPa}}.
\]

## 3. Neighbor-class sensitivity retained

The all-3/all-4/all-5 extreme count patterns give:

BH032:

\[
11.2778\le P_u\le11.4442\ \mathrm{MN}
\]

BH050:

\[
13.8008\le P_u\le13.9943\ \mathrm{MN}.
\]

Thus the direct-adjacency results lie inside a narrow approximately 1.4--1.5% classification envelope.

## 4. Status boundary

These values are `MULTIWAVE_STEEL_SHELL_01 / NO_SLIP / DIRECT_ADJACENCY` numerical theory results. They do not modify production R14. FE is not used in any root solve or classification. The current calculator implements the theory file's stated PCHIP tension interpolation using SciPy's standard PCHIP implementation; it is not asserted to reproduce every historical workbook-specific Hermite slope coefficient unless those coefficients are separately frozen into this version.
