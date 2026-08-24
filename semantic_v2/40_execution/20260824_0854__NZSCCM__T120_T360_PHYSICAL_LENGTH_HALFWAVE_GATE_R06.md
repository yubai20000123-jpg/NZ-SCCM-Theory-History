# NZ-SCCM — T120/T360 physical-length / halfwave identity gate R06

**Date:** 2026-08-24 08:54 +08:00  
**Status:** `PHYSICAL_LENGTH_GATE = PASS / OLD_1600_AXIAL_ANALYTICAL_LENGTH_WITHDRAWN_FOR_NEW_RUN`

## 0. Scope

This gate resolves one preflight question before the new cross-family `Ny-My` resultant-capacity calculations:

> For T120/T360, should the Marguerre–Airy structural front use 1600 mm as the axial physical length, or the actual 3000 mm specimen/model length, and what longitudinal halfwave is source-supported?

No comparator load is used to select a length or mode.

---

## 1. Physical geometry evidence

The canonical T120/T360 geometry contract is

\[
B=1600\ \mathrm{mm},\qquad H=50\ \mathrm{mm},\qquad L=3000\ \mathrm{mm},
\]

with UHPC core

\[
B_c=1592\ \mathrm{mm},\qquad H_c=42\ \mathrm{mm}.
\]

Therefore the new structural-front geometry is

\[
\boxed{b=1600\ \mathrm{mm},\qquad a_{phys}=3000\ \mathrm{mm}}.
\]

The old `1600 x 1600 analytical panel` is not the physical geometry contract and is withdrawn as the axial-length input for the new calculation.

---

## 2. FE/global-wave evidence

The existing R02 wave-to-damage audit used the global longitudinal factor

\[
\left|\sin\frac{2\pi z}{L}\right|,
\]

which is a two-halfwave longitudinal class over the 3000-mm physical length. Its nominal complete-halfwave length is

\[
\boxed{\ell=1500\ \mathrm{mm}}.
\]

The same audit found:

- T120 core damage most compatible with the global `m=2` wave;
- T360 core damage longitudinal location close to the `m=2` antinode;
- the old T120 textual label `m*=1` is more likely a documentation-label error than the numerical/physical mode identity.

The Abaqus nonlinear imperfection itself is imported from the linear buckling result (`*IMPERFECTION, FILE=..., STEP=1`, mode 1), so the `sin(2 pi z/L)` field is treated as a global analytical classification/mapping, not claimed to be the exact nodal eigenvector.

---

## 3. Independent elastic-front check on the physical 3000-mm domain

The current web-corrected initial laminate stiffnesses are:

### T120

\[
D_x=1.224175948103\times10^9\ \mathrm{N\,mm},
\]
\[
D_y=1.294203678743\times10^9\ \mathrm{N\,mm},
\]
\[
H=1.224175948103\times10^9\ \mathrm{N\,mm}.
\]

### T360

\[
D_x=1.234012004753\times10^9\ \mathrm{N\,mm},
\]
\[
D_y=1.259219952833\times10^9\ \mathrm{N\,mm},
\]
\[
H=1.234012004753\times10^9\ \mathrm{N\,mm}.
\]

For

\[
\alpha=\frac{\pi}{b},\qquad \beta_j=\frac{j\pi}{a_{phys}},
\]

use

\[
P_{cr,j}
=b\frac{D_x\alpha^4+2H\alpha^2\beta_j^2+D_y\beta_j^4}{\beta_j^2}.
\]

The direct integer scan gives:

| Case | j | ell=a/j (mm) | Pcr (MN) |
|---|---:|---:|---:|
| T120 | 1 | 3000 | 43.921124 |
| T120 | 2 | 1500 | **30.822799** |
| T120 | 3 | 1000 | 38.489650 |
| T120 | 4 | 750 | 53.094774 |
| T120 | 5 | 600 | 72.934697 |
| T120 | 6 | 500 | 97.589082 |
| T360 | 1 | 3000 | 44.194396 |
| T360 | 2 | 1500 | **30.751944** |
| T360 | 3 | 1000 | 38.082257 |
| T360 | 4 | 750 | 52.247336 |
| T360 | 5 | 600 | 71.530019 |
| T360 | 6 | 500 | 95.506591 |

Hence both independent elastic fronts select

\[
\boxed{m_*=2,\qquad \ell=1500\ \mathrm{mm}}.
\]

This agrees with the existing global-wave/damage evidence without using any ultimate-load comparator.

---

## 4. Decision

```text
T120_T360_PHYSICAL_WIDTH = 1600 mm
T120_T360_PHYSICAL_AXIAL_LENGTH = 3000 mm
OLD_AXIAL_ANALYTICAL_LENGTH_1600 = WITHDRAWN_FOR_NEW_PHYSICAL_RUN
ELASTIC_FRONT_MODE_T120 = m=2
ELASTIC_FRONT_MODE_T360 = m=2
REPRESENTATIVE_COMPLETE_HALFWAVE = 1500 mm
FE_GLOBAL_MODE_CLASS_SUPPORT = YES
EXACT_FE_EIGENVECTOR_EQUALS_SINE = NOT_CLAIMED
COMPARATOR_LOAD_USED_FOR_MODE_SELECTION = NO
PHYSICAL_LENGTH_HALFWAVE_GATE = PASS
```

The next formal cross-family calculation shall therefore use the full physical domain for mode selection, then one continuous representative complete halfwave of length 1500 mm for T120/T360.