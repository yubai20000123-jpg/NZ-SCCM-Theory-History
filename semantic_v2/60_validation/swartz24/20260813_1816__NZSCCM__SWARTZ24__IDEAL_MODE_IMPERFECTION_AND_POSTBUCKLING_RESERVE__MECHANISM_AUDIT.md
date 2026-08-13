# NZ-SCCM Swartz24 — ideal mode, imperfection selection and postbuckling reserve mechanism audit

**Timestamp:** 2026-08-13 18:16 +08:00  
**Identity:** SOURCE-GROUNDED MECHANISM AUDIT / NO CALIBRATION  
**R10 change:** NO  
**Compiler change:** NO  
**Structural backfit:** NO

## 0. Question

Can the 24-panel error pattern be understood by separating:

1. the perfect/ideal buckling-mode family;
2. actual specimen imperfection/eccentricity/support heterogeneity selecting or localizing a weaker mode; and
3. postbuckling reserve that raises experimental failure load after initial buckling?

## 1. Classical aspect-ratio-2 baseline

For a homogeneous isotropic simply-supported plate under uniaxial compression, with `a/b=2`, the classical mode

\[
w=W\sin(m\pi x/a)\sin(\pi y/b)
\]

has critical-load coefficient

\[
k_m=\frac{(m^2/(a/b)^2+1)^2}{m^2/(a/b)^2}.
\]

Hence

```text
m=1, one full-length halfwave: k=6.25
m=2, two square halfwaves:    k=4.00
```

so the full-length one-wave branch has a classical critical load 1.5625 times the two-square-wave branch. Swartz explicitly states that the 2:1 plates were proportioned so that ideal homogeneous/isotropic/elastic behavior should produce two square panels.

This supports the user's core energetic intuition: if the material remained classical isotropic elastic, a single full-length halfwave is not the lowest critical branch.

## 2. Critical correction: one-wave does not uniquely prove initial imperfection for Cases1-16

Swartz also explicitly states that departures from the ideal two-square-panel form can arise because the load is not perfectly zero-eccentricity and because concrete plates are orthotropic and inelastic.

More importantly, Nguyen's **perfect nonlinear finite-element model** predicts:

```text
Cases 1-16  (b/t about 48 to 38): approximately one longitudinal halfwave
Cases 17-24 (b/t about 63):       two sinusoidal halfwaves
```

For Cases1-16 the critical stress is already about 0.795fc to 0.93fc, and Nguyen reports that the buckled shapes differ from the corresponding isotropic elastic plate but resemble a tangent-orthotropic plate.

Therefore:

```text
ONE_WAVE_IN_CASES1_16 = NOT UNIQUE EVIDENCE OF INITIAL IMPERFECTION
OFF_CENTER / UNEQUAL / LOCALIZED WAVE = STRONGER NONIDEALITY EVIDENCE
TWO_EQUAL_HALFWAVES_IN_CASES17_24 = PERFECT-NONLINEAR MODE CONSISTENT
```

The earlier source-correct Case1 audit is fully consistent with this: replacing the square representative halfwave by the full-length one-wave (`ell=2440 mm`) increased the audit-only first load maximum from about 608.9 kN to about 647.5 kN. Thus a weaker real localized/asymmetric path could indeed lower the observed capacity relative to that ideal full-length branch; however the existence of the one-wave family itself is not attributable uniquely to imperfection.

## 3. Source experimental quantities used here

The source table gives each specimen's observed buckling/bulge location and experimental reserve from initial buckling to failure. The current C1/MM result table gives signed failure-load error. No value below is used to fit any model.

Approximate current signed errors are:

```text
1 +24.22   2 +17.81   3 +16.84   4 +3.97
5 -12.31   6 -10.69   7 -4.29    8 +14.96
9 -14.98  10 -21.01  11 -17.46  12 -12.35
13 +11.25 14 -10.07  15 -12.32  16 -17.85
17 -22.33 18 -9.74   19 -5.63   20 -6.67
21 -0.74  22 +3.29   23 +8.35   24 +10.32
```

Experimental postbuckling reserve `(Pf/Pcr-1)` is strongly group-structured. Using the tabulated values as a diagnostic, the Pearson correlation between current signed error and experimental reserve is approximately

\[
r\approx-0.626.
\]

Thus panels with larger experimental postbuckling reserve tend to be underpredicted by the current first-load-maximum model. This is a stronger aggregate relation than thickness alone.

## 4. Specimen-by-specimen mechanism classification

The following classification is explanatory only.

|Case|Source bulge location|Experimental reserve|Current error|Mode/nonideality interpretation|
|---:|---|---:|---:|---|
|1|top 2/3 + bottom 1/3, multiple zones|Southwell Pcr invalid for reserve sign|+24.22%|Strong nonideal/asymmetric pattern. A source-correct ideal full-length branch is even stronger; imperfection/eccentricity/local heterogeneity is therefore a credible downward selector. Strong fit to the user's mechanism, but not uniquely initial geometric imperfection.|
|2|middle|+13.45%|+17.81%|Centered one-wave is consistent with Nguyen's perfect nonlinear mode. Location gives little evidence for imperfection; an unknown imperfection amplitude may still lower capacity, but compiler/material/specimen effects remain needed.|
|3|middle|+10.26%|+16.84%|Same as Case2: mode location is ideal-family consistent, so positive error cannot be assigned to imperfection from shape alone.|
|4|bottom 1/3|Southwell Pcr invalid for reserve sign|+3.97%|Off-center localization is clear nonideality evidence, but net error is already small; competing effects nearly cancel.|
|5|top 2/3 + bottom 1/3, multiple zones|+7.68%|-12.31%|Nonideal mode exists, but capacity is underpredicted. Imperfection-lowering cannot explain the sign; missing postbuckling redistribution/reserve is more important.|
|6|top 1/3|+16.57%|-10.69%|Strong off-center nonideality plus large reserve. Negative error indicates the upward postbuckling reserve dominates the downward imperfection effect.|
|7|middle|+10.69%|-4.29%|Centered ideal-family one-wave and moderate reserve; mild underprediction is consistent with missing reserve rather than mode-selection error.|
|8|top 1/4|+1.49%|+14.96%|One of the strongest cases for the user's mechanism: highly localized/off-center buckle, almost no measured postbuckling reserve, and strong positive theoretical error.|
|9|top 1/3|+21.29%|-14.98%|Off-center nonideality exists, but very large experimental reserve dominates; current theory remains low.|
|10|middle|+11.79%|-21.01%|Centered Nguyen-perfect one-wave. Initial-imperfection explanation is weak from shape; full-length mode correction and missing high-stress redistribution/reserve are higher priority.|
|11|middle|+18.85%|-17.46%|Same pattern as Case10, with larger reserve; strongly consistent with missing postbuckling capacity.|
|12|middle|+19.63%|-12.35%|Centered ideal-family mode and large reserve; underprediction is not an imperfection-lowering signature.|
|13|middle|+14.87%|+11.25%|Anomaly within the thick group: centered mode yet positive error. Shape does not support an imperfection explanation; specimen/material/compiler differences require separate scrutiny.|
|14|middle|+23.94%|-10.07%|Centered ideal-family mode and very large reserve. Correct `ell=2440` should be restored before interpreting final magnitude; missing reserve is strongly indicated.|
|15|middle|+14.79%|-12.32%|Centered ideal-family mode; negative error again points to postbuckling/redistribution reserve.|
|16|middle|+24.27%|-17.85%|Strongest reserve in the group and large underprediction; very strong evidence that an ideal first-mode/low-dimensional model misses real postbuckling capacity.|
|17|middle 1/3 + bottom 1/3, multiple zones|+20.02%|-22.33%|Departs from Nguyen's ideal two-equal-halfwave family, but huge reserve overwhelms any imperfection reduction; worst slender-group underprediction.|
|18|top 2/3|+11.24%|-9.74%|Localized departure from ideal two-wave form, yet underprediction; mixed mechanism, reserve larger than mode-localization penalty.|
|19|top 1/2 + bottom 1/2|+21.11%|-5.63%|Closest to ideal two-halfwave pattern. Despite large reserve, error is only moderate negative. Strong modal-consistency benchmark.|
|20|middle 1/3 + bottom 1/3, multiple zones|+11.29%|-6.67%|Unequal/misaligned two-zone response indicates nonideality, but net result remains modestly underpredicted.|
|21|top 1/2 + bottom 1/2|+9.52%|-0.74%|Best source match to Nguyen's ideal two-halfwave family and current theory is nearly exact. This is the strongest single supporting specimen for the mode-consistency interpretation.|
|22|top 1/3|+14.29%|+3.29%|Localized one-zone response instead of ideal two equal halves; modest positive error is compatible with a downward imperfection effect roughly offset by reserve.|
|23|top 1/3|+11.43%|+8.35%|Localized departure from ideal two-wave family plus positive error; good support for the user's imperfection/mode-selection mechanism.|
|24|middle|+12.50%|+10.32%|A central dominant zone rather than two equal halves, with positive error; also supports nonideal mode selection, though material/specimen effects cannot be excluded.|

## 5. Group-level synthesis

### Cases1-8, b/t about 48

Nguyen's perfect nonlinear baseline is already one full-length halfwave. Therefore the relevant imperfection signature is **not one-wave versus two-wave**, but whether the one-wave response is centered and smooth versus off-center/multiple/localized.

The strongest positive-error/nonideal-shape specimens are Case1 and Case8. Cases2-3 are positive-error but centered, so they prevent any claim that imperfection shape alone explains the group. Cases5-7 are underpredicted despite nonideal or centered buckles, and their larger postbuckling reserve supplies the opposite correction.

### Cases9-16, b/t about 38

This group is the clearest counterexample to a universal `imperfection lowers experiment` explanation. Nguyen's perfect nonlinear mode is a centered full-length one-wave and Cases10-16 mostly show exactly that. Yet the current theory is strongly low for nearly all except Case13.

The source reports high stresses near `0.93fc` before buckling and experimental postbuckling reserves mostly around 12-24%. Therefore the dominant open issue is likely capacity available after initial buckling through membrane/in-plane/material/reinforcement redistribution, together with restoring the correct full-length mode in the production input. Initial imperfection cannot explain a systematic negative error here.

### Cases17-24, b/t about 63

This is the cleanest test of the user's mode-selection hypothesis because Nguyen's perfect nonlinear baseline is two halfwaves. Cases19 and21 most closely display the two-halfwave pattern; their current errors are only about -5.6% and -0.7%, respectively. Case21 is especially compelling.

Cases22-24 depart toward a localized single dominant zone and all have positive error (+3.3%, +8.3%, +10.3%). This is qualitatively exactly what an imperfection/eccentricity/support-selected weaker mode would produce.

Cases17-20 show that this is not the whole story: their experimental postbuckling reserve is sufficient to keep failure above the present theoretical prediction despite nonideal modes.

## 6. Revised unified mechanism

A useful non-calibrating decomposition is

\[
P_f^{exp}
\approx
P_u^{ideal,source-faithful}
-\Delta P_{imperfection/eccentricity/support/localization}
+\Delta P_{postbuckling\ redistribution}
+\delta P_{specimen/material}
\]

where none of the terms is inferred from `Pf` for coefficient generation.

This explains why the same test series can contain both positive and negative prediction errors:

- positive error: downward nonideality/localization effect dominates;
- negative error: experimental postbuckling redistribution/reserve dominates;
- near-zero error: the two effects plus material/compiler errors approximately cancel.

The current data support this competition much better than a one-parameter thickness rule.

## 7. Main verdict

```text
CLASSICAL_a_over_b_2_TWO_SQUARE_HALFWAVE_BASELINE = CONFIRMED
FULL_LENGTH_ONE_WAVE_CLASSICAL_CRITICAL_LEVEL = HIGHER
CASE1_SOURCE_CORRECT_FULL_LENGTH_AUDIT = HIGHER_CAPACITY_DIRECTION_CONFIRMED

ONE_WAVE_CASES1_16_CAUSED_ONLY_BY_INITIAL_IMPERFECTION = NOT_SUPPORTED
NGUYEN_PERFECT_NONLINEAR_ONE_WAVE_CASES1_16 = SOURCE_CONFIRMED

OFF_CENTER_UNEQUAL_LOCALIZED_BULGE_AS_NONIDEALITY_SIGNATURE = SUPPORTED
CASES19_21_TWO_HALFWAVE_MODAL_CONSISTENCY = STRONGLY SUPPORTIVE
CASES22_24_LOCALIZATION_PLUS_POSITIVE_ERROR = SUPPORTIVE

POSTBUCKLING_RESERVE_VS_CURRENT_SIGNED_ERROR_r = APPROX_-0.626
IMPERFECTION_ONLY_GLOBAL_EXPLANATION = REJECTED
IMPERFECTION_PLUS_POSTBUCKLING_COMPETITION = CURRENT_BEST_MECHANISM_HYPOTHESIS

STRUCTURAL_CALIBRATION = NO
EXPERIMENTAL_Pf_USED_IN_MODEL_GENERATION = NO
```

## 8. Next discriminating calculation

Do not fit `q0` to each panel. Instead, after recovering the actual production halfwave provenance, perform two blind source-defined structural families:

1. `IDEAL_MODE`: Nguyen source-mode family — full-length one-wave for Cases1-16, square representative halfwave for Cases17-24.
2. `IMPERFECTION_SHAPE_SENSITIVITY`: a finite analytic basis containing centered and admissible asymmetric/localized modes, with amplitudes treated as prescribed source-bounded sensitivity variables, not fitted from `Pf`.

Separately enrich the in-plane/postbuckling Ritz freedom and observe whether the large negative errors in Cases9-16 reduce. This cleanly separates downward imperfection sensitivity from upward redistribution reserve while preserving finite analytic basis + Cayley-Hamilton + general-D15 and zero formal spatial quadrature.
