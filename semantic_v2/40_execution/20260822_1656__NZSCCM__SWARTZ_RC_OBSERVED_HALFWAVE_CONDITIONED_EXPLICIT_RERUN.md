# NZ-SCCM — Swartz RC observed-halfwave-conditioned explicit rerun

**Time:** 2026-08-22 16:56 +08:00  
**Status:** `EXECUTED / STRUCTURAL_WAVEFORM_DIAGNOSTIC / CURRENT_EXPLICIT_METHOD_UNCHANGED / 1D RERUN CLOSED / WAVEFORM-CONDITIONED 2D PROPAGATION NOT YET EXECUTED`

## 0. Purpose

This execution answers one narrow question:

> If the current Marguerre–Airy explicit calculation method is kept unchanged, but the representative half-wave length is imposed from the frozen Swartz/Nguyen waveform evidence, how much do the selected RC ultimate-load predictions change?

This is a diagnostic of structural waveform error, not a production mode-selection rule.

The experimental failure load `Pf` is opened only after each theoretical root is frozen. It is not used to select the half-wave, root, material coefficient, or branch.

---

## 1. What changed and what did not

Only the representative half-wave length changed:

- Cases 1–16 source waveform: approximately one sinusoidal half-wave over the 2440-mm physical length, so `ell = 2440 mm`;
- Cases 17–24 source waveform: two sinusoidal half-waves, so one representative half-wave has `ell = 1220 mm`.

The shape inside one representative half-wave remains

\[
w(\xi,y)=A\sin\frac{\pi\xi}{\ell}\sin\frac{\pi y}{b}.
\]

The current explicit structural method is unchanged:

\[
P_{pb}(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0),
\]

\[
n(s;q)=\frac{P_{pb}(q)}b+Gq(q+2q_0)(1-2s^2),
\qquad
m(s;q)=Jqs.
\]

For every imposed `ell`, all dependent quantities are regenerated from the same formulas:

\[
\alpha=\frac{\pi}{b},\qquad \beta=\frac{\pi}{\ell},
\]

\[
P_{cr},\quad C,\quad G,\quad J.
\]

No old `m=2` coefficients are reused after changing `ell`.

Formal flags remain:

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = TRUE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_material_points = 0
RITZ_ORDER = NONE
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
EXPERIMENT_IN_ROOT_SELECTION = 0
```

---

## 2. Current explicit 1D section equations retained exactly

For the selected mid-plane-reinforcement cases, the current corrected reinforcement interpretation is

\[
\rho_x=\rho_y=p_{table}.
\]

The concrete compression section uses the same parabolic ascending profile. At `s=1` the finite section root remains

\[
n(1;q)=N_u(c),\qquad Jq=M_u(c).
\]

No additional structural coordinate is introduced.

---

## 3. Baseline reproduction gate

Before changing any half-wave, the reproduction script was run with `ell=1220 mm` for all eight selected cases. It reproduces the previously reported current explicit 1D table to the published rounding:

|Case|previous current 1D / kN|fresh reproduction / kN|
|---:|---:|---:|
|1|567.712|567.712185|
|2|561.638|561.638149|
|9|515.424|515.424342|
|10|534.711|534.711245|
|19|339.177|339.177259|
|20|335.013|335.013232|
|21|350.460|350.460343|
|22|351.679|351.679273|

Therefore the comparison below isolates the half-wave input change within the same current explicit solver.

---

## 4. Regenerated coefficients for source-observed one-half-wave cases

For Cases 1/2/9/10, changing `ell: 1220 -> 2440 mm` gives:

|Case|Pcr / kN|C / kN|G / N/mm|J / N|
|---:|---:|---:|---:|---:|
|1|1550.614006|1791782.528214|172785.200406|106682.243628|
|2|1655.082433|1910241.201728|184208.409038|113869.671363|
|9|2157.471024|1607581.474583|155022.321561|148434.006429|
|10|2460.743436|1827670.380502|176245.938332|169299.148418|

For this symmetric initial-stiffness family the `m=2 -> m=1` change has the exact coefficient tendencies

\[
\frac{P_{cr}^{m=1}}{P_{cr}^{m=2}}=1.5625,
\qquad
\frac{C^{m=1}}{C^{m=2}}=2.125,
\qquad
\frac{G^{m=1}}{G^{m=2}}=0.25.
\]

`J` also decreases because the longitudinal curvature wavenumber is halved.

---

## 5. Observed-waveform-conditioned 1D roots

|Case|source halfwaves|ell / mm|q_u|c_u / mm|old auto-m2 1D / kN|observed-wave 1D / kN|change|Pf / kN|observed-wave error|
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|1|1|2440|0.001881466|62.7835|567.7122|**689.0551**|+21.374%|490.1940|**+40.568%**|
|2|1|2440|0.001628111|64.5492|561.6381|**673.3721**|+19.894%|506.6524|**+32.906%**|
|9|1|2440|0.000911080|96.9811|515.4243|**584.9057**|+13.480%|625.8648|**−6.544%**|
|10|1|2440|0.000796083|98.8134|534.7112|**602.7616**|+12.727%|696.1467|**−13.415%**|
|19|2|1220|0.005847944|17.1694|339.1773|**339.1773**|0|377.6540|**−10.188%**|
|20|2|1220|0.006511069|16.1452|335.0132|**335.0132**|0|372.7610|**−10.127%**|
|21|2|1220|0.006907588|15.9059|350.4603|**350.4603**|0|368.3127|**−4.847%**|
|22|2|1220|0.006423918|16.3712|351.6793|**351.6793**|0|355.8577|**−1.174%**|

---

## 6. Main finding

The waveform correction has a strong and nonuniform structural effect.

### Cases 9/10

The old auto-`m=2` errors were approximately

\[
-17.65\%,\qquad -23.19\%.
\]

With the source-observed one-half-wave condition they become

\[
\boxed{-6.54\%,\qquad -13.41\%}.
\]

Thus the waveform change recovers about 11.10 and 9.78 percentage points respectively. The large Case9/10 low bias is therefore partly structural-waveform-related and cannot be assigned only to the concrete material law.

### Cases 1/2

The same waveform correction moves the 1D roots in the opposite practical direction:

\[
+15.81\%\to\boxed{+40.57\%},
\]

\[
+10.85\%\to\boxed{+32.91\%}.
\]

Therefore waveform correction alone does not solve the RC prediction problem. It makes the need for the two-dimensional material interaction in this pair more pronounced.

### Cases 19–22

Their source waveform already is two half-waves, so the imposed-waveform rerun is exactly identical to the current calculation. They form a clean control group.

---

## 7. Group statistics for this 1D waveform diagnostic

For Cases 1/2/9/10 together:

- old auto-m2 1D mean signed error = `-3.542%`;
- old auto-m2 1D MAE = `16.876%`;
- observed-wave 1D mean signed error = `+13.379%`;
- observed-wave 1D MAE = `23.358%`.

This combined statistic worsens because Cases1/2 become much more overpredicted. It must not hide the useful subgroup result:

- Cases1/2 MAE: `13.333% -> 36.737%`;
- Cases9/10 MAE: `20.418% -> 9.979%`.

For Cases19/20/21/22, both old and observed-wave MAE are `6.584%` because the waveform input is unchanged.

---

## 8. Important 2D status

This execution does **not** relabel the old 0745 `495.989/501.025 kN` values as waveform-corrected 2D results.

Those values were generated with the old `ell=1220 mm / m=2` structural demand and were later explicitly classified as a separate TC-sensitivity diagnostic, not as the current TC-R2 unified production result.

After changing `ell`, the Airy transverse demand and all dependent structural coefficients change. Therefore the old m=2 2D re-cut cannot simply be attached to the new m=1 1D roots.

Current status:

```text
OBSERVED_WAVEFORM_CONDITIONED_1D = EXECUTED
OBSERVED_WAVEFORM_CONDITIONED_2D = NOT_YET_EXECUTED
OLD_M2_CASE1_2_495_501_REUSE = PROHIBITED
```

The next RC calculation, if required, is to propagate the same fixed two-dimensional material constraint through these regenerated `ell=2440 mm` structural demands without changing the material model.

---

## 9. Interpretation and production implication

This experiment separates two questions:

1. **Can the existing explicit solver accept the source-observed half-wave without changing method?**  
   `YES` — only `ell` changes and all dependent coefficients are regenerated.

2. **Can experiment-supplied half-wave be the final predictive rule?**  
   `NO` — in production the half-wave must be selected from a source-grounded tangent-stiffness/mode gate, not from `Pf` or observed failure shape.

The present diagnostic demonstrates that the waveform is structurally important enough to deserve its own prediction gate before further material tuning.

---

## 10. Decision

```text
CURRENT_EXPLICIT_METHOD_CHANGED = FALSE
SOURCE_WAVEFORM_USED_AS_DIAGNOSTIC_INPUT = TRUE
CASE1_16_SOURCE_HALFWAVE = 1
CASE17_24_SOURCE_HALFWAVES = 2
SELECTED_8_FRESH_1D_RERUN = CLOSED
CASE9_10_WAVEFORM_CAUSAL_EFFECT = LARGE_AND_BENEFICIAL
CASE1_2_WAVEFORM_CAUSAL_EFFECT = LARGE_AND_INCREASES_1D_OVERPREDICTION
CASE19_22_WAVEFORM_CAUSAL_EFFECT = ZERO_BY_SOURCE_MATCH
MATERIAL_PARAMETERS_REFIT = FALSE
EXPERIMENTAL_PF_IN_ROOT = FALSE
NEXT_RC_TASK = WAVEFORM_CONDITIONED_2D_PROPAGATION_THEN_TANGENT_MODE_GATE
```

Reproduction script:

`semantic_v2/40_execution/rc/20260822_1656__NZSCCM__SWARTZ_RC_OBSERVED_HALFWAVE_EXPLICIT_RERUN.py`
