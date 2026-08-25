# NZ-SCCM — SSUHPC BH032/BH050 first-local-yield continuation diagnosis R01

**Time:** 2026-08-25 21:45 +08:00  
**Status:** DIAGNOSTIC / NO THEORY CHANGE / COMPARATOR NOT USED IN ROOT SOLVE  
**Parent R06:** `semantic_v2/20_theory/20260825_1530__NZSCCM__STEEL_SHELL_COMMON_R06_LOCAL_YIELD_RESULTANT_GATE_V1.md`  
**R06 code:** `semantic_v2/40_execution/steel_shell/20260825_1535__NZSCCM__STEEL_SHELL_COMMON_R06_LOCAL_YIELD_RESULTANT_GATE.py`

## 0. Purpose

This diagnostic isolates the global load at which the **first R06 local-Mises yield event** is reached on the uncapped R02 section path, before the UHPC compression-peak terminal condition is imposed.

For each case and longitudinal station parameter `s`, solve the same four section-resultant balances using uncapped R02 steel faces plus exact UHPC/web resultants, with the fifth equation replaced by

\[
\max_{[-1,1]^2}\Phi_{-,loc}=f_y^2.
\]

No Abaqus/comparator enters this solve.  The complete finite-algebraic local candidate set is used to certify the fixed event state.  Station continuation confirms the earliest event on the current branch occurs at `s=1` for both BH032 and BH050.

Important identity clarification: current R06 does **not** freeze the globally first-yield face resultant forever.  At each later physical face strain it projects along that current strain ray to the first local-yield boundary.  Therefore the returned capped face state can evolve after the first global local-yield event.

---

## 1. BH032 first local yield

At `s=1`, the blind event solution is

\[
q_{LY}=0.000797081466899,
\]
\[
\varepsilon_x^0=1.74109924\times10^{-4},\quad
\kappa_x=1.03905984\times10^{-5}\ \mathrm{mm}^{-1},
\]
\[
\varepsilon_y^0=-1.34664690\times10^{-3},\quad
\kappa_y=8.19005939\times10^{-6}\ \mathrm{mm}^{-1}.
\]

The corresponding load is

\[
\boxed{P_{LY}^{BH032}=7.43075298512\ \mathrm{MN}}.
\]

The lower face is the active local-yield face:

\[
\max\sigma_{VM,-}=355.000000000\ \mathrm{MPa},
\]

while the upper-face complete finite-algebraic maximum is only

\[
\max\sigma_{VM,+}=256.783065075\ \mathrm{MPa}.
\]

Lower/upper face mean R02 stresses at the event are approximately

\[
\bar\sigma_+= (29.5766,-219.2267,0)\ \mathrm{MPa},
\]
\[
\bar\sigma_-= (-47.4180,-279.4163,0)\ \mathrm{MPa}.
\]

The UHPC y strains at `z=+/-21 mm` are approximately

\[
\varepsilon_y(+21)=-0.00117466,\qquad
\varepsilon_y(-21)=-0.00151864,
\]

so the first steel local-yield event is far earlier than the frozen UHPC compression terminal `-0.0035`.

Event section decomposition:

\[
N_y^U=-2398.0961,\quad
N_y^w=-230.9432,\quad
N_y^f=-1994.5717\ \mathrm{N/mm}.
\]

Current terminal R06 theory remains

\[
P_u^{BH032}=10.9405345132\ \mathrm{MN}.
\]

Thus the theoretical post-local-yield load gain is

\[
\Delta P_{th}=3.5097815281\ \mathrm{MN}.
\]

Only after this theoretical event is fixed, reopening the existing Abaqus peak `10.9905 MN` gives an apparent post-event gain

\[
\Delta P_{FE}=3.5597470149\ \mathrm{MN},
\]

so

\[
\frac{\Delta P_{th}}{\Delta P_{FE}}=0.98596.
\]

Therefore BH032's current theory and existing FE comparator exhibit nearly identical total load growth after the theoretical first-local-yield load.

---

## 2. BH050 first local yield

At `s=1`, the blind event solution is

\[
q_{LY}=0.00199124621749,
\]
\[
\varepsilon_x^0=9.94769377\times10^{-5},\quad
\kappa_x=1.65858895\times10^{-5}\ \mathrm{mm}^{-1},
\]
\[
\varepsilon_y^0=-1.07753949\times10^{-3},\quad
\kappa_y=1.41189052\times10^{-5}\ \mathrm{mm}^{-1}.
\]

The corresponding load is

\[
\boxed{P_{LY}^{BH050}=8.83277880474\ \mathrm{MN}}.
\]

Again the lower face is active:

\[
\max\sigma_{VM,-}=355.000000000\ \mathrm{MPa},
\]

while the upper-face complete finite-algebraic maximum is

\[
\max\sigma_{VM,+}=183.010656164\ \mathrm{MPa}.
\]

At the event:

\[
\bar\sigma_+=(64.7553,-130.6534,0)\ \mathrm{MPa},
\]
\[
\bar\sigma_-=(-48.1030,-224.1292,0)\ \mathrm{MPa}.
\]

UHPC y strains at `z=+/-21 mm` are approximately

\[
\varepsilon_y(+21)=-0.00078104,\qquad
\varepsilon_y(-21)=-0.00137404,
\]

again far before the UHPC compression terminal.

Event section decomposition:

\[
N_y^U=-1934.4575,\quad
N_y^w=-118.2673,\quad
N_y^f=-1419.1307\ \mathrm{N/mm}.
\]

Current terminal R06 theory is

\[
P_u^{BH050}=13.3563763545\ \mathrm{MN},
\]

so

\[
\Delta P_{th}=4.5235975498\ \mathrm{MN}.
\]

Only after fixing the theory event, comparing with the existing Abaqus peak `12.2198 MN` gives

\[
\Delta P_{FE}=3.3870211953\ \mathrm{MN},
\]

hence

\[
\boxed{\frac{\Delta P_{th}}{\Delta P_{FE}}=1.33557}.
\]

The present BH050 theory therefore carries about **33.6% more post-theoretical-local-yield load gain** than the existing FE comparator.

This excess continuation is exactly the final peak difference

\[
13.3563763545-12.2198=1.1365763545\ \mathrm{MN}.
\]

This statement is conditional on using the theoretical `P_LY` as the common reference.  The actual FE first-PEEQ/local-yield load still has to be extracted from the ODB before claiming event-to-event equivalence.

---

## 3. Post-local-yield section redistribution

### BH032

From theoretical first local yield to the current terminal R06 state:

\[
|N_y^U|:2398.10\to4367.14,
\]
\[
|N_y^f|:1994.57\to2138.27,
\]
\[
|N_y^w|:230.94\to293.19\ \mathrm{N/mm}.
\]

Of the added total compression resultant, approximately

- UHPC: 90.5%,
- outer steel faces: 6.6%,
- web: 2.9%.

### BH050

From theoretical first local yield to the current terminal R06 state:

\[
|N_y^U|:1934.46\to3775.21,
\]
\[
|N_y^f|:1419.13\to1191.20,
\]
\[
|N_y^w|:118.27\to170.90\ \mathrm{N/mm}.
\]

The total added compression resultant is `1665.45 N/mm`, but its decomposition is approximately

- UHPC: **+110.5%** of the net increment,
- outer steel faces: **-13.7%** (steel faces unload in net y compression),
- web: +3.2%.

Thus the BH050 continuation is qualitatively different: the theoretical section gains additional total compression while the outer steel faces are unloading and the UHPC absorbs more than 100% of the net increment.

---

## 4. Upper-face reversal is the sharpest current signal

BH050 theoretical upper-face mean y stress evolves from

\[
\bar\sigma_{y,+}^{LY}\approx-130.65\ \mathrm{MPa}
\]

to

\[
\bar\sigma_{y,+}^{Pu}\approx-75.74\ \mathrm{MPa},
\]

i.e. the upper steel face **unloads** in y compression after first local yield.

By contrast the currently available FEM peak diagnostic reported approximately

\[
\bar\sigma_{y,+}^{FE,peak}\approx-255\ \mathrm{MPa},
\]

while the lower face was approximately `-233 MPa`, close in scale to the theoretical lower-face R06 value near `-222 MPa`.

Therefore the current strongest component-level mismatch is not the lower R06 local-yield cap itself.  It is the post-yield section curvature/load redistribution that unloads the theoretical upper steel face and transfers too much y compression to the UHPC.

A useful dimensionless curvature-to-membrane measure is

\[
\chi_y=\frac{z_f\kappa_y}{|\varepsilon_y^0|}.
\]

For BH032:

\[
\chi_y:0.140\ (LY)\to0.442\ (Pu).
\]

For BH050:

\[
\chi_y:0.301\ (LY)\to0.700\ (Pu).
\]

BH050 therefore enters a much more bending-dominated terminal section state, which explains the theoretical upper-face unloading and the strong constituent redistribution.

---

## 5. Current diagnosis

The simple hypothesis

```text
BH050 first local yield ≈ FE peak
```

is **rejected** by the frozen theory itself: theoretical first local yield occurs at only `8.8328 MN`, well before the existing `12.2198 MN` FE peak.

The stronger revised hypothesis is:

```text
The first-local-yield detector itself is not the main BH050 problem.
The severe-local-buckling discrepancy develops during the post-local-yield continuation path.
In BH050 that path drives an excessive curvature/load redistribution:
upper steel unloads, UHPC is forced to take disproportionate additional compression,
and the theoretical terminal remains delayed until UHPC reaches -0.0035.
```

BH032 is the key control: its total post-theoretical-local-yield load gain agrees with the existing FE peak to about 1.4% of the gain, whereas BH050 overpredicts that post-event gain by about 33.6%.

No theory modification is authorized from this diagnostic alone.

---

## 6. Required next ODB check

To close the diagnosis, extract from the existing BH032/BH050 ODBs:

1. actual first meaningful steel PEEQ/local-yield load;
2. component `N_y` at the theoretical event loads `7.430753 MN` (BH032) and `8.832779 MN` (BH050);
3. upper/lower steel-face mean `sigma_y` histories from those loads to peak;
4. UHPC `N_y` history over the same interval;
5. a same-section fitted `epsilon_y^0` and `kappa_y`, if reliable, to test the theoretical curvature-growth/upper-face-unloading mechanism directly.

Until that ODB event history is available, the present result is a theory-side diagnosis plus peak-level FEM consistency check, not a full event-to-event validation.
