# NZ-SCCM 多波钢壳01——BH005至BH100及T120/T360全系列结果 R01

**Date:** 2026-09-03  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Theory:** `20260903__NZSCCM__MULTIWAVE_STEEL_SHELL_01_NO_SHEAR_SLIP_FULL_DERIVATION_R01.md`  
**Status:** `NUMERICAL DIAGNOSTIC / NOT PRODUCTION Pu`

---

## 0. Scope

This file archives the Multiwave Steel Shell 01 full-series numerical results already executed in chat.

Locked execution rules:

- steel shell and UHPC fully bonded / no slip;
- one complete global halfwave only;
- `n0=floor(L_G/s)`;
- equal-width buckling bays use only `n0-1`, `n0`, `n0+1`;
- non-buckling cells automatically use full-thickness ideal elastic-perfectly-plastic steel;
- no effective width/area;
- no qU;
- no partial interaction;
- no 99 independent local amplitudes;
- R02/R06 steel-cell response retained;
- UHPC and web resultants remain those of the 01 execution contract;
- terminal event is the first admissible material-domain event or J4 fold as already used in the numerical continuation.

---

# 1. Global-halfwave and local-wave counts

For the BH family used here,

\[
a=2b,
\qquad m^*=2,
\qquad L_G=b.
\]

With standard rib spacing

\[
s=0.225b,
\]

all BH cases therefore give

\[
\boxed{n_0=\lfloor b/(0.225b)\rfloor=4},
\]

and the local candidates are

\[
\boxed{n=3,4,5}.
\]

For T360:

\[
b=1600\ \mathrm{mm},\quad a=3000\ \mathrm{mm},\quad m^*=2,
\]

so

\[
L_G=1500\ \mathrm{mm},
\qquad s=360\ \mathrm{mm},
\]

hence

\[
\boxed{n_0=4},
\]

with candidates `3/4/5`.

For T120:

\[
L_G=1500\ \mathrm{mm},
\qquad s=120\ \mathrm{mm},
\]

so

\[
\boxed{n_0=12},
\]

with candidates

\[
\boxed{n=11,12,13}.
\]

In the T120 execution all three local candidates had elastic local critical stresses above steel yield, so the local branches degenerated automatically to the R04 yield-first/full-thickness ideal-EP state.

---

# 2. Full-series terminal results

| Case | `m*` | `n0` | terminal identity | `q_u` or `q_fold` | `P_u^01` / MN |
|---|---:|---:|---|---:|---:|
| BH005 | 2 | 4 | material-domain terminal | 0.0000319946 | **2.48343** |
| BH010 | 2 | 4 | material-domain terminal | 0.000123780 | **4.62777** |
| BH020 | 2 | 4 | material-domain terminal | 0.000536236 | **8.66421** |
| BH032 | 2 | 4 | material-domain terminal | 0.001455924 | **11.32879** |
| BH050 | 2 | 4 | material-domain terminal | 0.005260096 | **13.85846** |
| BH060 | 2 | 4 | material-domain terminal | 0.009083093 | **14.45680** |
| BH070 | 2 | 4 | material-domain terminal | 0.012949751 | **15.24042** |
| BH085 | 2 | 4 | **J4 fold** | 0.01479568054 | **15.2281322** |
| BH100 | 2 | 4 | **J4 fold** | 0.01615274908 | **15.8486001** |
| T120 | 2 | 12 | material-domain terminal | 0.001794015 | **12.96637** |
| T360 | 2 | 4 | material-domain terminal | 0.001420145 | **11.20480** |

---

# 3. High-B/H fold states

## BH085

\[
\boxed{q_{fold}^{01}=0.01479568054}
\]

\[
\boxed{P_u^{BH085,01}=15.2281322\ \mathrm{MN}}
\]

Approximate fold state:

\[
\varepsilon_x^0=2.77768\times10^{-3},
\]

\[
\kappa_x=2.00408\times10^{-4}\ \mathrm{mm^{-1}},
\]

\[
\varepsilon_y^0=-1.07956\times10^{-3},
\]

\[
\kappa_y=7.75655\times10^{-5}\ \mathrm{mm^{-1}}.
\]

The compression material-domain margin remained approximately

\[
\boxed{7.92\times10^{-4}>0},
\]

so the fold was reached before the frozen UHPC compression boundary.

## BH100

\[
\boxed{q_{fold}^{01}=0.01615274908}
\]

\[
\boxed{P_u^{BH100,01}=15.8486001\ \mathrm{MN}}
\]

Approximate fold state:

\[
\varepsilon_x^0=2.84721\times10^{-3},
\]

\[
\kappa_x=1.78006\times10^{-4}\ \mathrm{mm^{-1}},
\]

\[
\varepsilon_y^0=-7.53104\times10^{-4},
\]

\[
\kappa_y=6.38644\times10^{-5}\ \mathrm{mm^{-1}}.
\]

The numerical fold locator reduced the smallest singular value to approximately

\[
\boxed{2.1\times10^{-7}}.
\]

These are numerical J4 fold locations under the Multiwave 01 execution level; they are not theorem-level finite-algebraic certificates.

---

# 4. Locked interpretation

1. Multiwave 01 can be evaluated across the entire listed BH/T family without reverting to the historical single-cell implementation.
2. BH005 through BH070, T120 and T360 reached the current material-domain terminal in the executed branch.
3. BH085 and BH100 must not be forced to the UHPC `-0.0035` boundary; the J4 fold occurs first.
4. T120 automatically degenerates to the yield-first steel branch because its local steel cells do not elastically buckle before yield under the present local criterion.
5. These results are diagnostic results of Multiwave Steel Shell 01 and do not modify production R14.
