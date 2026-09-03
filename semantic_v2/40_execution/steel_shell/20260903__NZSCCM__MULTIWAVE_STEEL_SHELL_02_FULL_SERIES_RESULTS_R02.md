# NZ-SCCM 多波钢壳02——固定单肋滑移刚度全系列计算结果 R02

Date: 2026-09-03
Branch: `diagnostic/bh032-bh050-mode-projection-20260827`
Status: **NUMERICAL DIAGNOSTIC / NOT PRODUCTION R14**
Theory: `20260903__NZSCCM__MULTIWAVE_STEEL_SHELL_02_FIXED_RIB_SLIP_STIFFNESS_R01.md`

## 1. Fixed connector parameter

\[
K_r=75.835\ \mathrm{kN/mm/rib}.
\]

No FEM load was used to fit `K_r` or select roots.

For BH005-BH100: TOP 4 ribs, BOTTOM 5 ribs, so
\[
\gamma_+=0.412096588866410,\qquad \gamma_-=0.467007669218195.
\]

For T360: `b=1600 mm`, `a=3000 mm`, `L_G=1500 mm`, TOP 4, BOTTOM 5:
\[
\gamma_+=0.396554217072007,\qquad \gamma_-=0.450982971541861.
\]

For T120: source-backed total longitudinal rib steel corresponds to 25 ribs; the present staggered execution specialization uses TOP 12, BOTTOM 13:
\[
\gamma_+=0.663463864517450,\qquad \gamma_-=0.681095656844243.
\]

## 2. Global/local identities

BH family: `m*=2`, `L_G=b`, `s=0.225b`, `n0=4`, candidates `3/4/5`.

T360: `m*=2`, `L_G=1500 mm`, `s=360 mm`, `n0=4`, candidates `3/4/5`.

T120: `m*=2`, `L_G=1500 mm`, `s=120 mm`, `n0=12`, candidates `11/12/13`; all three local candidates have `sigma_cr^E > fy`, so they degenerate to the full-thickness ideal-EP branch.

## 3. Terminal results

| Case | terminal | q | Pu02 / MN | Pu01 / MN | 02 vs 01 |
|---|---|---:|---:|---:|---:|
| BH005 | material-domain | 0.000031994092634 | 2.48339103 | 2.48343 | -0.0016% |
| BH010 | material-domain | 0.000123777698248 | 4.62768331 | 4.62777 | -0.0019% |
| BH020 | material-domain | 0.000536166339206 | 8.66328252 | 8.66421 | -0.0107% |
| BH032 | material-domain | 0.001381063538151 | 10.95164917 | 11.32879 | -3.3290% |
| BH050 | material-domain | 0.004590062664227 | 13.15441229 | 13.85846 | -5.0803% |
| BH060 | material-domain | 0.007716875026501 | 13.59903535 | 14.45680 | -5.9333% |
| BH070 | material-domain | 0.011334567930855 | 14.26033767 | 15.24042 | -6.4308% |
| BH085 | numerical J4 fold | 0.014690092270434 | 15.15107146 | 15.2281322 | -0.5060% |
| BH100 | numerical J4 fold | 0.016060748225033 | 15.76823132 | 15.8486001 | -0.5071% |
| T120 | material-domain | 0.001746314472889 | 12.76182046 | 12.96637 | -1.5775% |
| T360 | material-domain | 0.001337649430040 | 10.77870293 | 11.20480 | -3.8028% |

## 4. Section states

| Case | eps_x0 | kappa_x /mm | eps_y0 | kappa_y /mm |
|---|---:|---:|---:|---:|
| BH005 | 6.00491981e-4 | 2.65535845e-6 | -3.23569653e-3 | 1.25858794e-5 |
| BH010 | 5.55177440e-4 | 5.65899203e-6 | -3.13900117e-3 | 1.71904204e-5 |
| BH020 | 5.07743990e-4 | 1.19245316e-5 | -2.93378919e-3 | 2.69624196e-5 |
| BH032 | 1.84627660e-4 | 2.03786648e-5 | -2.27982889e-3 | 5.81033861e-5 |
| BH050 | 9.34456605e-5 | 3.97813944e-5 | -1.80675450e-3 | 8.06307381e-5 |
| BH060 | 1.17204025e-4 | 5.21685808e-5 | -1.54869701e-3 | 9.29191900e-5 |
| BH070 | 2.20546244e-4 | 6.22541935e-5 | -1.30310379e-3 | 1.04614105e-4 |
| BH085 | 2.93045104e-3 | 1.93912072e-4 | -9.30739701e-4 | 1.00085614e-4 |
| BH100 | 3.10013559e-3 | 1.77449828e-4 | -6.01774885e-4 | 8.43170501e-5 |
| T120 | 3.69233621e-4 | 1.61501379e-5 | -2.42860333e-3 | 5.10188891e-5 |
| T360 | 1.78583861e-4 | 1.95132742e-5 | -2.22867237e-3 | 6.05394108e-5 |

## 5. Steel face averages and steel resultants

| Case | sx+ MPa | sy+ MPa | sx- MPa | sy- MPa | Ny_s N/mm | My_s N |
|---|---:|---:|---:|---:|---:|---:|
| BH005 | -34.7655 | -371.1037 | -55.8150 | -379.6013 | -3002.8199 | 781.7746 |
| BH010 | -27.5585 | -367.9761 | -68.7967 | -384.3630 | -3009.3562 | 1507.5978 |
| BH020 | -3.13154 | -356.5554 | -91.1125 | -391.6760 | -2992.9256 | 3231.0936 |
| BH032 | 42.9203 | -310.2060 | -69.9561 | -295.1014 | -2421.2295 | -1389.6192 |
| BH050 | 157.6019 | -167.2156 | -82.8427 | -244.4333 | -1646.5955 | 7104.0356 |
| BH060 | 251.7566 | -62.7018 | -97.4458 | -230.2686 | -1171.8815 | 15416.1415 |
| BH070 | 351.8066 | 40.6943 | -105.8499 | -221.5128 | -723.2739 | 24123.0517 |
| BH085 | 398.0961 | 119.6321 | -144.0820 | -205.2249 | -342.3713 | 29886.8495 |
| BH100 | 400.2875 | 129.3674 | -124.1042 | -207.1149 | -310.9901 | 30956.3734 |
| T120 | 55.6121 | -323.2312 | -120.0907 | -399.4694 | -2890.8023 | 7013.9135 |
| T360 | 42.8613 | -307.0364 | -70.4279 | -294.5087 | -2406.1804 | -1152.5525 |

## 6. High-B/H fold audit

BH085 fold:
\[
q\approx0.01469009227,\quad P\approx15.15107146\ \mathrm{MN},
\]
with lower UHPC longitudinal endpoint
\[
\varepsilon_y^-\approx-0.00303254>-0.0035.
\]
Thus fold remains before the compression material boundary.

BH100 fold:
\[
q\approx0.01606074823,\quad P\approx15.76823132\ \mathrm{MN},
\]
with
\[
\varepsilon_y^-\approx-0.00237243>-0.0035.
\]
Thus fold remains first.

The fold locations are numerical continuation results. The R06 execution uses finite harmonic edge extrema with interior screening; it is not promoted here to a theorem-level global resultant certificate.

## 7. Interpretation

1. Fixed finite transfer is negligible for yield-first BH005-BH020.
2. Sensitivity grows strongly in the local-buckling-first transition BH032-BH070.
3. T120 is relatively insensitive because its dense ribs give much larger transfer factors and its local candidates are yield-first.
4. T360 is more sensitive because its transfer factors are lower and its local cells are local-buckling-first.
5. BH085/BH100 remain controlled by J4 folds, so the change in terminal load is much smaller than BH050-BH070.
6. `K_r=75.835 kN/mm/rib` remains a diagnostic engineering estimate, not a source-locked production parameter.
