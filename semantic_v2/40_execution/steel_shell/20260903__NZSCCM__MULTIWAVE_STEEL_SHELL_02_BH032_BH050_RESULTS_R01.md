# NZ-SCCM 多波钢壳02——BH032 / BH050 固定单肋滑移刚度计算结果 R01

**Date:** 2026-09-03  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Theory:** `20260903__NZSCCM__MULTIWAVE_STEEL_SHELL_02_FIXED_RIB_SLIP_STIFFNESS_R01.md`  
**Status:** `NUMERICAL DIAGNOSTIC / NOT PRODUCTION Pu`

---

## 0. Locked execution identity

The following results archive the already executed Multiwave Steel Shell 02 diagnostic calculation.

Fixed rib stiffness:

\[
\boxed{K_r=75.835\ \mathrm{kN/mm/rib}}.
\]

For BH032/BH050:

\[
K_{eq}=432.750\ \mathrm{kN/mm},
\]

\[
\boxed{\gamma_+=0.41210},
\qquad
\boxed{\gamma_-=0.46701}.
\]

Multiwave classification:

```text
TOP regular bays    = 3 / 4 / 5
BOTTOM regular bays = 3 / 4 / 5 / 4
non-standard edge residual strips = ideal-EP E branch
```

No FEM load was used to fit `Kr` or choose a root.

---

# 1. BH032

## 1.1 Terminal root

\[
\boxed{q_u=0.00138106354}
\]

\[
\boxed{P_u^{BH032,02}=10.9516492\ \mathrm{MN}}
\]

Section variables:

\[
\boxed{\varepsilon_x^0=1.84628\times10^{-4}}
\]

\[
\boxed{\kappa_x=2.03787\times10^{-5}\ \mathrm{mm^{-1}}}
\]

\[
\boxed{\varepsilon_y^0=-2.27983\times10^{-3}}
\]

\[
\boxed{\kappa_y=5.81034\times10^{-5}\ \mathrm{mm^{-1}}}
\]

## 1.2 Face-average steel stresses

TOP:

\[
\boxed{(\bar\sigma_x^+,\bar\sigma_y^+)=(+42.92,-310.21)\ \mathrm{MPa}}
\]

BOTTOM:

\[
\boxed{(\bar\sigma_x^-,\bar\sigma_y^-)=(-69.96,-295.10)\ \mathrm{MPa}}
\]

## 1.3 Steel-shell resultants

\[
\boxed{N_x^s=-108.14\ \mathrm{N/mm}}
\]

\[
\boxed{M_x^s=10384.63\ \mathrm N}
\]

\[
\boxed{N_y^s=-2421.23\ \mathrm{N/mm}}
\]

\[
\boxed{M_y^s=-1389.62\ \mathrm N}
\]

The sign reversal of `M_y^s` relative to the no-slip result is a direct consequence of the changed top/bottom longitudinal force difference under finite composite transfer.

## 1.4 Comparison after the theoretical root was fixed

Canonical FEM reference used only as comparator:

\[
P_{FEM}=10.990480\ \mathrm{MN}.
\]

Therefore

\[
\boxed{\frac{P_u^{02}}{P_{FEM}}-1=-0.35\%}.
\]

The no-slip Multiwave 01 result was

\[
P_u^{01}=11.328790\ \mathrm{MN},
\]

so the finite-slip diagnostic changes

\[
11.328790\rightarrow10.951649\ \mathrm{MN},
\]

a reduction of approximately

\[
\boxed{3.33\%}.
\]

---

# 2. BH050

## 2.1 Terminal root

\[
\boxed{q_u=0.00459006248}
\]

\[
\boxed{P_u^{BH050,02}=13.1544121\ \mathrm{MN}}
\]

Section variables:

\[
\boxed{\varepsilon_x^0=9.34457\times10^{-5}}
\]

\[
\boxed{\kappa_x=3.97814\times10^{-5}\ \mathrm{mm^{-1}}}
\]

\[
\boxed{\varepsilon_y^0=-1.80675\times10^{-3}}
\]

\[
\boxed{\kappa_y=8.06307\times10^{-5}\ \mathrm{mm^{-1}}}
\]

## 2.2 Face-average steel stresses

TOP:

\[
\boxed{(\bar\sigma_x^+,\bar\sigma_y^+)=(+157.60,-167.22)\ \mathrm{MPa}}
\]

BOTTOM:

\[
\boxed{(\bar\sigma_x^-,\bar\sigma_y^-)=(-82.84,-244.43)\ \mathrm{MPa}}
\]

## 2.3 Steel-shell resultants

\[
\boxed{N_x^s=+299.04\ \mathrm{N/mm}}
\]

\[
\boxed{M_x^s=22120.90\ \mathrm N}
\]

\[
\boxed{N_y^s=-1646.60\ \mathrm{N/mm}}
\]

\[
\boxed{M_y^s=7104.03\ \mathrm N}
\]

## 2.4 Comparison after the theoretical root was fixed

Canonical FEM reference:

\[
P_{FEM}=12.591227\ \mathrm{MN}.
\]

Thus

\[
\boxed{\frac{P_u^{02}}{P_{FEM}}-1=+4.47\%}.
\]

The no-slip Multiwave 01 result was

\[
P_u^{01}=13.858459\ \mathrm{MN},
\]

so

\[
13.858459\rightarrow13.154412\ \mathrm{MN},
\]

a reduction of approximately

\[
\boxed{5.08\%}.
\]

---

# 3. Side-by-side diagnostic summary

| Case | Multiwave 01 no slip / MN | Multiwave 02 fixed `Kr` / MN | canonical FEM / MN | 02 vs FEM |
|---|---:|---:|---:|---:|
| BH032 | 11.328790 | **10.951649** | 10.990480 | **-0.35%** |
| BH050 | 13.858459 | **13.154412** | 12.591227 | **+4.47%** |

The present diagnostic therefore shows a materially stronger Pu sensitivity to finite longitudinal composite transfer than to the previously tested `3/4/5` local-wave arrangement sensitivity.

This observation does **not** validate `Kr=75.835 kN/mm/rib` as a production parameter. It only records the numerical consequence of the fixed diagnostic stiffness.
