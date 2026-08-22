# NZ-SCCM — Panel21 global-vs-local limit regression audit R01

**Time:** 2026-08-23 00:58 +08:00  
**Status:** `EXECUTED / B_D_CONTROLLED / A_HISTORICAL_BLIND_BASELINE_CONFIRMED / C_NOT_YET_OPERATOR_CLOSED / MATERIAL_ENRICHMENT_PAUSED`

## 0. Trigger

Panel21 had already been a near-exact blind prediction before source waveform prescription. The old blind calculation used the same nominal halfwave scale `ell=1220 mm` and the source-correct directional reinforcement ratio `rho_x=rho_y=0.00375`. Therefore the later collapse to roughly 173–183 kN cannot be attributed to choosing the wrong halfwave length.

The regression audit separates waveform detail from the later local-section singularity criterion.

## 1. Four-cell audit definition

| Cell | waveform | limit criterion | status |
|---|---|---|---|
| A | ideal pure m=2, ell=1220 mm | global `Rq=0, L=0` | historical blind baseline confirmed |
| B | ideal pure m=2, ell=1220 mm | local 4-resultant section equilibrium + `det Jsec=0` | executed now |
| C | prescribed multi-harmonic Panel21 source waveform | global `Rq=0, L=0` | not yet operator-closed |
| D | prescribed multi-harmonic Panel21 source waveform | local 4-resultant section equilibrium + `det Jsec=0` | reproduced now |

No `Pf` is used in any solve or root selection.

## 2. Cell A — authoritative historical blind global result

The 2026-08-11 Swartz24 blind run used:

- `halfwave_b=1220 mm`, `halfwave_ell=1220 mm`;
- total two-way steel ratio `0.75%`;
- `rho_s_each_direction=0.00375`;
- one mid-plane layer;
- global equilibrium `Rq(D,q)=0`;
- global limit determinant `L=P_D Rq_q-P_q Rq_D=0`;
- zero formal spatial quadrature.

It gave

\[
\boxed{P_A=368.189337\ \mathrm{kN}}
\]

before the experimental failure load was read. The later comparison gives `-0.0335%` versus `Pf`.

An independent fresh Case21 N48-C1/MM calculation gave `365.607776 kN` (`-0.734%` vs `Pf`), confirming that the old global branch was not a one-off root selected from experiment.

## 3. Controlled B/D execution with the same current local material

To isolate waveform detail inside the later local-section architecture, B and D use exactly the same:

- NC-M6/F03 current material map;
- corrected directional steel split `p/2`;
- two-independent-affine-slope section variables `(ax,ay,bx,by)`;
- full `Nx,Ny,Mx,My` section equilibrium;
- same-law section Jacobian and `det Jsec=0`;
- zero formal spatial/thickness quadrature.

Only the prescribed longitudinal waveform is changed.

Reproduction driver:

`semantic_v2/40_execution/rc/20260823_0058__NZSCCM__PANEL21_ABCD_REGRESSION_BD_DRIVER.py`

### D reproduction gate

Using the current source waveform at the corrected stationary location gives

\[
q_D=0.001347589965,
\qquad
\boxed{P_D=173.209915\ \mathrm{kN}}.
\]

This reproduces the previously published corrected NC-M6/F03 Panel21 result to sub-micro-kN level, so the controlled audit is on the same current local-section calculation path.

For D,

\[
P_{cr,\Phi}=478.906112\ \mathrm{kN},
\qquad
C_\Phi=640240.833\ \mathrm{kN}.
\]

### B pure m=2 execution

Set

\[
\Phi_B(u)=-\sin(2\pi u),
\]

which is exactly two equal longitudinal halfwaves over the 2440-mm physical length, hence each halfwave is 1220 mm. Symmetry fixes equivalent stationary sections at `u=0.25` and `0.75`.

The local section fold is

\[
q_B=0.001531925676,
\qquad
\boxed{P_B=160.778280\ \mathrm{kN}}.
\]

with

\[
P_{cr,B}=407.136279\ \mathrm{kN},
\qquad
C_B=608339.560\ \mathrm{kN}.
\]

Direct symmetry/continuation checks give:

| u | q_fold | P_fold / kN |
|---:|---:|---:|
|0.245|0.00153287248|160.842192|
|0.250|0.00153192568|160.778280|
|0.255|0.00153287248|160.842192|
|0.750|0.00153192568|160.778280|

Thus the pure m=2 local-fold result is numerically stationary and symmetric as required.

## 4. Quantitative regression decomposition

Using the main blind A baseline:

\[
A=368.189337\ \mathrm{kN},
\quad
B=160.778280\ \mathrm{kN},
\quad
D=173.209915\ \mathrm{kN}.
\]

Hence

\[
A\rightarrow B:\quad -207.411057\ \mathrm{kN}=-56.333\%,
\]

\[
A\rightarrow D:\quad -194.979422\ \mathrm{kN}=-52.956\%,
\]

while, **inside the same current local-section architecture**,

\[
B\rightarrow D:\quad +12.431635\ \mathrm{kN}=+7.732\%.
\]

This is the decisive controlled result:

\[
\boxed{\text{the prescribed multi-harmonic source waveform does not cause the low local fold.}}
\]

It actually raises the current local-fold load relative to the ideal pure-m2 waveform.

Therefore the earlier `wavelength/source-waveform causes Panel21 collapse` hypothesis is rejected.

## 5. What is and is not proven about the local fold criterion

The data establish:

1. A correct 1220-mm global blind model gave about 368 kN.
2. The current local-section architecture gives only about 161 kN even when returned to the same ideal pure-m2 wavelength family.
3. Changing pure m2 to the source multi-harmonic waveform changes that local result by only about +12.4 kN, not by the roughly -195 to -207 kN required to explain the historical-to-current collapse.

However A and B do **not** use the same material representation: A is the historical N48-C1/MM global current-map/D15 branch, while B is the later NC-M6/F03 exact local-section current map. Therefore the entire `A-B` difference cannot yet be assigned mathematically to `det Jsec=0` alone.

The strongest warranted verdict is:

```text
WAVELENGTH_ERROR = REJECTED
SOURCE_WAVEFORM_DETAIL_AS_PRIMARY_CAUSE = REJECTED
LOCAL_SECTION_FOLD_ARCHITECTURE = PRIMARY_STRUCTURAL_REGRESSION_SUSPECT
A_MINUS_B_ATTRIBUTABLE_100_PERCENT_TO_CRITERION = NOT_YET_PROVEN
MATERIAL_CHANGE_CONFOUND = STILL_PRESENT_IN_A_VS_B
```

## 6. Cell C status

Cell C requires the **old global** `Rq(D,q), L(D,q)` operator to be generalized from the ideal single finite halfwave to the prescribed finite multi-harmonic source waveform while retaining the same old N48-C1/MM material and exact D15/global work-conjugate construction.

The repository contains the complete formula/reproduction contract and frozen A results, but no already-qualified implementation of that old global operator for arbitrary `Phi(y)`. Replacing it with the later local `Nx,Ny,Mx,My` section system would simply recreate D and would not be Cell C.

Therefore Cell C is deliberately recorded as

```text
C_STATUS = NOT_YET_OPERATOR_CLOSED
C_NUMERICAL_VALUE = NOT_INVENTED
```

rather than silently changing the governing equations.

## 7. Governance consequence

All new postcrack-tension-shape work (BH04 or other TC/TT material enrichment) is paused. The next task is structural/operator recovery:

1. restore the old global `Rq=0,L=0` identity as the reference limit definition;
2. derive the finite-wave generalized global strain/work operator for a prescribed `Phi(y)` without spatial quadrature;
3. execute Cell C with the old global material unchanged;
4. only after C is known, decide whether the later local-section fold has any legitimate role as a secondary/local admissibility gate rather than the primary plate `Pu` criterion.

The present evidence already rules out wavelength selection as the explanation for Panel21's current ~50% underprediction.