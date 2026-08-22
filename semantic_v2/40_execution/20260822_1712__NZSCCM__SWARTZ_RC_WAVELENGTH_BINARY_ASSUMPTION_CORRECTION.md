# NZ-SCCM — Swartz RC wavelength binary-assumption correction

**Time:** 2026-08-22 17:12 +08:00  
**Status:** `CORRECTION / PREVIOUS_1220_2440_BINARY_MAPPING_DOWNGRADED / EXACT_WAVELENGTH_AUDIT_REQUIRED`

## 0. Correction

The immediately preceding observed-halfwave diagnostic mechanically mapped

```text
Panels 1-16 -> ell = 2440 mm
Panels 17-24 -> ell = 1220 mm
```

from Nguyen's qualitative half-wave classification. That mapping is too strong and is **not source-closed**.

The calculation itself remains a valid endpoint sensitivity test, but it must no longer be described as the actual observed-waveform-conditioned result.

Correct identity:

```text
20260822_1656 rerun = COARSE ENDPOINT WAVELENGTH SENSITIVITY TEST
NOT = PER-PANEL OBSERVED WAVELENGTH RERUN
```

---

## 1. What Nguyen actually says

Nguyen Chapter 5 states:

- Panels 17-24: the computed buckled shapes had `two sinusoidal half waves`;
- panels with slenderness ratios about 48 and 38: the computed shapes had an `approximate one half sinusoidal wave`;
- Figures 5.7 and 5.8 show Panel 1 and Panel 14 as representative nonlinear buckled shapes;
- those shapes differ from the isotropic elastic plate shapes and are instead similar to tangent-orthotropic STRAND6 shapes.

The word `approximate` is essential. It does not establish an exact global sine with half-wave length `2440 mm`.

The rendered Figures 5.7/5.8 also visibly show a broad/flattened nonlinear bulge rather than an exact single sine. Figure 5.6 shows the two-lobe class for Panel 21, but the source does not provide a table assigning exact equal 1220-mm local wavelengths to every Panel 17-24 specimen.

---

## 2. Swartz raw experimental morphology is even less discrete

The prior source audit already established from Swartz et al. (1974):

- bulge location is reported panel by panel;
- the actual bulge position and shape are not strictly identical inside a nominal group;
- some specimens resemble the Plate-21 morphology, while the general observed form is a localized single-panel bulge similar to Plate 6.

Therefore the source evidence supports a **mode/morphology class**, not a binary exact wavelength table.

---

## 3. Why an intermediate apparent wavelength cannot simply be inserted into the old global sine

The current global single-term longitudinal form is of Navier type,

\[
w(x,y)=A\sin\left(\frac{m\pi x}{a}\right)\sin\left(\frac{\pi y}{b}\right).
\]

For an exact full-panel simply-supported single sine, the end conditions require integer `m`, hence

\[
\ell_h=\frac{a}{m}.
\]

With `a=2440 mm`, exact single-term candidates are discrete: 2440, 1220, 813.33, ... mm.

Consequently, if the physical/FE shape exhibits an effective wavelength between 1220 and 2440 mm, it cannot be represented faithfully merely by replacing `ell` with an arbitrary continuous value in the same one-term full-panel sine while retaining exact end conditions.

An intermediate effective wavelength indicates at least one of the following:

1. a nonlinear/non-sinusoidal localized bulge;
2. a finite superposition of admissible integer Navier modes;
3. unequal/local half-waves separated by an interior nodal line;
4. a representative local half-wave whose length differs from `a/m`, requiring a separate global compatibility closure.

This distinction must be resolved before another ultimate-load rerun.

---

## 4. Correct next task: wavelength consistency audit first

Before any further 2D capacity propagation, establish a per-panel/per-group wavelength ledger.

For every available source shape, record:

\[
\ell_{obs},\qquad \eta=\ell_{obs}/b,
\]

or, when exact `ell_obs` cannot be recovered, a bounded morphology interval rather than an invented number.

Required evidence hierarchy:

1. Swartz original measured bulge/nodal locations where recoverable;
2. Nguyen FE buckled-shape figures/data;
3. Nguyen/STRAND6 tangent-orthotropic equivalent shapes;
4. qualitative one-half/two-half class only when no metric data exist.

Then test:

```text
WITHIN_PAIR_WAVELENGTH_CONSISTENCY
WITHIN_GROUP_WAVELENGTH_CONSISTENCY
GROUP1_VS_GROUP2_DIFFERENCE
GROUP3_EQUAL_HALFWAVE_ASSUMPTION
```

Only after this audit may a common wavelength, discrete mode mixture, or local representative half-wave be adopted.

---

## 5. Governance

```text
PANELS_1_16_EXACT_ELL_2440 = WITHDRAWN
PANELS_17_24_EXACT_ELL_1220 = NOT PROVEN PANEL-BY-PANEL
NGUYEN_1_16_APPROX_ONE_HALF_WAVE = RETAINED
NGUYEN_17_24_TWO_HALF_WAVE_CLASS = RETAINED
20260822_1656_NUMERICAL_VALUES = RETAINED_AS_ENDPOINT_SENSITIVITY_ONLY
WAVEFORM_CONDITIONED_2D_PROPAGATION = PAUSED
NEXT_RC_TASK = PER_PANEL_WAVELENGTH_CONSISTENCY_AND_REPRESENTATION_AUDIT
MATERIAL_RETUNING = OFF
```
