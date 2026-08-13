# NZ-SCCM Swartz Case1-led panels — source specimen variability and test nonideality audit

**Timestamp:** 2026-08-13 17:19 +08:00  
**Identity:** SOURCE-GROUNDED EXPERIMENT AUDIT / NO CALIBRATION / NO EXPERIMENT CORRECTION

## 0. Purpose and evidence labels

This audit asks a narrow question: besides the material-compiler representation issue, do the original Swartz/Nguyen sources provide evidence that individual test panels — especially Case1-led `b/t≈48` specimens — could have lower physical capacity than an idealized average-property plate because of specimen/test nonidealities?

Every item is labelled as one of:

```text
SOURCE_EXPLICIT      = directly stated or tabulated in Swartz/Nguyen
MECHANICS_INFERENCE  = consequence inferred from a source-explicit fact
NOT_QUANTIFIED       = plausible/source-admitted but no Case-specific magnitude found
```

No item below is permitted to alter the experimental failure load or to tune R10/compiler/structural parameters.

## 1. First correction: Case1 failure load is not a transcription mistake

Swartz et al. Table 2 gives for Plate 1:

```text
experimental buckling load = 125.1 kip *
experimental failure load  = 110.2 kip
buckling location           = top 2/3 and bottom 1/3 of plate
* = obtained from Southwell plots
```

Thus `Pf=110.2 kip = 490.194 kN` is an original source failure value.

The apparent contradiction `Pf < reported Pcr` is explained by the **buckling identification method**, not by a failure-load error. Swartz explicitly states that Plates 1 and 4 used Southwell plots, and the detailed test-method paper states that Southwell is fundamentally a linear-elastic method, becomes uncertain for increasingly inelastic concrete, and in almost all tested cases yielded values considerably higher than actual collapse loads. The ACI paper also notes that actual buckling of Plates 1 and 4 was visually observed at somewhat lower loads than the Southwell estimate.

Therefore:

```text
CASE1_Pf_110p2_KIP = SOURCE_CONFIRMED
CASE1_Pcr_125p1_KIP = SOUTHWELL_DERIVED / HIGH_BIAS_RISK
Pf_LESS_THAN_TABULATED_Pcr = NOT_EVIDENCE_OF_FAILURE_LOAD_ERROR
```

This matters for Pcr validation, but it does not by itself explain why a current ultimate-load calculation is about 24% above `Pf`.

## 2. Unavoidable load eccentricity

### Source evidence — SOURCE_EXPLICIT

The detailed Swartz/Rosebraugh/Rogacki test-frame paper explicitly states that forces normal to the panel edges arise from the combined effects of **unavoidable load eccentricity** and post-buckling behavior. The authors also state that deviations from the ideal homogeneous/isotropic plate response are expected because load may not be applied with zero eccentricity and because the material is orthotropic and inelastic.

The measured strain examples were described as indicating a *fairly small* or *fairly low* eccentricity, not exactly zero. Deflection profiles were said to contain a mixture of unavoidable loading eccentricity and buckling deformation.

### Mechanics implication — MECHANICS_INFERENCE

A nonzero load eccentricity creates bending before the ideal symmetric plate would develop the same curvature. For an imperfection-sensitive nonlinear plate this can lower the load at which one local bulge becomes dominant and can reduce post-buckling reserve.

### Current status

```text
LOAD_ECCENTRICITY_EXISTS_IN_TEST = SOURCE_EXPLICIT
CASE1_EQUIVALENT_ECCENTRICITY = NOT_QUANTIFIED
USE_AS_FITTED_CASE1_PARAMETER = PROHIBITED
```

No numerical eccentricity should be inserted into Case1 until a specimen-specific measurement/bound can be recovered from the detailed records.

## 3. Initial geometric imperfection: current b/400 is not a measured Case1 quantity

### Source evidence

Nguyen's review of the Swartz analytical assumptions states that the original analytical treatment assumed small-deflection theory and ignored initial imperfections, as well as assuming zero eccentricity and uniform load. The experimental test papers, however, show nonzero deflection profiles and explicitly discuss unavoidable eccentricity and real plate movement.

The current NZ-SCCM `q0=b/400` input is a project-locked kinematic closure; the project source registry explicitly says it is **not claimed as a measured Swartz imperfection**.

### Mechanics implication

The real initial shape of an individual 4 ft × 8 ft panel may have an amplitude and spatial pattern different from a single ideal sine halfwave with amplitude `b/400=3.05 mm`. A larger or more localized initial bulge can reduce stability/ultimate capacity; a smaller imperfection can increase it.

### Current status

```text
MEASURED_CASE1_INITIAL_IMPERFECTION = NOT_FOUND
CURRENT_B_OVER_400 = PROJECT_INPUT / NOT_SOURCE_MEASUREMENT
IMPERFECTION_AS_CASE1_EXPLANATION = PLAUSIBLE_BUT_NOT_QUANTIFIED
```

The correct next source task is to look for Rogacki/Berman detailed records or preload dial-gage data, not to tune `q0` until Case1 matches `Pf`.

## 4. Thickness variation within a plate

### Source evidence — SOURCE_EXPLICIT

The detailed test-method paper states that thickness variation **within an individual plate was about ±3%**. The published Table 1 reports an **average thickness** for each specimen. Case1 is reported as 1.00 in (25.4 mm).

Thus the current uniform-thickness Case1 representation uses an average of a physically nonuniform plate.

### Mechanics implication — MECHANICS_INFERENCE

For bending-dominated plate stiffness, the local bending scale contains `t^3`. A ±3% thickness variation corresponds approximately to a local bending-stiffness factor range

```text
0.97^3 = 0.9127
1.03^3 = 1.0927
```

or about -8.7% to +9.3% around the nominal cubic scale, before material nonlinearity and geometric coupling are considered.

This does **not** mean Case1 capacity is 9% lower. It means a source-confirmed ±3% geometric nonuniformity is mechanically large enough that a local thin region could bias which halfwave/panel becomes controlling.

### Current status

```text
WITHIN_PANEL_THICKNESS_VARIATION = ABOUT_PLUS_MINUS_3_PERCENT / SOURCE_EXPLICIT
CASE1_LOCAL_THICKNESS_MAP = NOT_FOUND
UNIFORM_T_MODEL = AVERAGE_GEOMETRY_IDEALIZATION
```

This is one of the strongest source-supported unmodelled heterogeneities.

## 5. Cylinder-to-panel material representation and material scatter

### Source evidence — SOURCE_EXPLICIT

Swartz reports that only **two 6×12 in cylinders were cast for each panel** and were tested on the day of the panel test; the average cylinder strength and corresponding peak strain were tabulated. For Plate 1 the original table reports approximately:

```text
average cylinder fc' = 3896 psi (~26.84 MPa)
peak strain          = 2.10e-3
```

Nguyen then takes the concrete strength used in analysis as **0.85 times the cylinder strength** specifically to account for the difference between in-situ panel strength and standard cylinder strength. Current Case1 therefore uses approximately 22.81 MPa.

### Interpretation

The 0.85 factor already provides a source-based mean panel/cylinder correction and must not be re-fit to Case1 failure. However, two cylinders provide no spatial map of the 4×8 ft panel and do not eliminate local material variability within the slab.

### Current status

```text
CASE1_FCYL_AVERAGE = SOURCE_EXPLICIT
NGUYEN_0p85_IN_SITU_REDUCTION = SOURCE_EXPLICIT
SPATIAL_CASE1_CONCRETE_STRENGTH_FIELD = NOT_MEASURED_IN_AVAILABLE_SOURCE
ADDITIONAL_STRENGTH_REDUCTION_FROM_Pf = PROHIBITED
```

Material scatter is therefore a credible residual uncertainty but not a quantified correction.

## 6. Supports were engineered approximations, not mathematical continuous simple supports

### Source evidence — SOURCE_EXPLICIT

Swartz describes the frame as satisfying the intended no-normal-displacement/free-rotation edge conditions **acceptably**, not exactly. Side boundary conditions were approximated using discrete clamps and rods. Top/bottom supports also used spaced clamps and rollers so the panel could warp as buckling commenced.

The detailed test paper further states that uniform distribution of applied load/reaction along the loaded edges was itself a practical problem. The solution used 1/4-in crushable wood strips, a 20–40 kip seating load depending on thickness, and hydrocal bedding/alignment of the grooved plate/load beam.

### Mechanics implication

Discrete clamps, finite support stiffness, bedding compliance and residual load-distribution imperfections can create nonuniform in-plane stress and alter local out-of-plane restraint. This is exactly the class of perturbation that can select a weaker local bulge in an imperfection-sensitive nonlinear plate.

### Current status

```text
IDEAL_CONTINUOUS_SUPPORT = NOT_LITERAL_TEST_REALITY
LOAD_UNIFORMITY_WAS_ENGINEERED_BUT_NOT_EXACT = SOURCE_EXPLICIT
CASE1_SUPPORT_STIFFNESS_FIELD = NOT_QUANTIFIED
CASE1_LOAD_NONUNIFORMITY_FIELD = NOT_QUANTIFIED
```

These effects should not be represented by an arbitrary penalty factor.

## 7. Failure localization and weakest-half selection

### Source evidence — SOURCE_EXPLICIT

The original 4×8 ft panels have aspect ratio 2. Ideal elastic reasoning suggests two square buckling panels. Experimentally, only some specimens approximately followed that pattern; many tended to develop one dominant panel/bulge. Swartz reports that failure occurred in a plate-collapse mechanism and generally localized in one portion of the specimen.

For Case1, Table 2 identifies buckling activity in multiple regions (`top 2/3 and bottom 1/3`), rather than a perfectly symmetric pair of identical square halfwaves.

The detailed test paper explicitly suggests that differences between one- and two-panel buckling patterns may relate to the **relative stiffness of the side supports versus the plate bending stiffness**.

### Mechanics implication

A real 2.44 m specimen contains two potential nominal square halfwave regions that need not have identical thickness, concrete properties, eccentricity or support/load conditions. Experiment selects the weaker physical region. A theoretical representative halfwave built from whole-panel average material/geometric data does not automatically include this weakest-region selection.

This does not invalidate the `ONE_CONTINUOUS_COMPLETE_HALFWAVE` theory identity. It indicates that, for validation against a real 2-halfwave-long specimen, the representative controlling halfwave may need **source-measured local inputs** rather than global averages if such measurements can be recovered.

## 8. Why Case1-led b/t≈48 panels are especially sensitive

Nguyen's later analysis groups Cases1-8 near `b/t≈48` and reports an average critical stress around `0.795` of the reduced concrete compressive strength. He explicitly notes that the stresses are already above the proportional region and nonlinear, and that the predicted buckled shape of Panel 1 differs from the corresponding isotropic elastic plate but is similar to an orthotropic tangent-modulus plate.

Therefore Case1 is not an elastic plate where a few-percent geometric/test perturbation can automatically be dismissed. It lies in a coupled nonlinear-material/stability regime in which eccentricity, local thickness and support/load nonuniformity can be amplified.

## 9. Ranking of currently supported experimental-side mechanisms

This ranking concerns **evidentiary strength**, not fitted magnitude.

|mechanism|source evidence|Case1-specific magnitude|current assessment|
|---|---|---|---|
|within-panel thickness variation (~±3%)|direct|not mapped|HIGH evidentiary priority|
|unavoidable load eccentricity|direct|not quantified|HIGH evidentiary priority|
|nonuniform/discrete support and load transfer|direct|not quantified|HIGH evidentiary priority|
|weakest-half/localized bulge selection|direct pattern + mechanics inference|not quantified|HIGH structural priority|
|actual initial geometric imperfection|real nonideal response acknowledged; project b/400 not measured|not found|HIGH recovery priority, magnitude unknown|
|local material scatter beyond 0.85 cylinder reduction|two-cylinder average only + mechanics inference|not measured|MEDIUM/HIGH uncertainty|
|reinforcement ratio as primary explanation|source says buckling load effect not considerable|known|LOW as primary Case1 explanation|

## 10. What this audit does NOT conclude

It does **not** conclude that the experimental Case1 failure load is "wrong" or should be raised.

It does **not** conclude that any one of the above effects explains 24% by itself.

It does **not** authorize replacing average thickness by `0.97t`, adding an arbitrary eccentricity, changing `q0`, lowering `fc`, or selecting a weakened halfwave to match the experiment.

The defensible statement is narrower:

> The original test was deliberately close to simple support/uniform axial loading, but it was not a mathematically perfect homogeneous plate. The authors explicitly document unavoidable eccentricity, finite/discrete support and load-distribution engineering, about ±3% thickness variation, and localized/nonideal buckling patterns. The current validation model uses average material/geometric inputs and a project-defined imperfection. These differences are physically capable of lowering an individual specimen's capacity and are credible contributors to Case1-type positive prediction error, but the available sources do not quantify a Case1-specific correction.

## 11. Next source-grounded validation actions

```text
A. Search Rogacki/Berman detailed records for preload Case1 deflection/imperfection field.
B. Recover any per-position thickness measurements rather than using only average t.
C. Recover any Case1 edge strain/reaction evidence that can bound loading eccentricity or nonuniformity.
D. Keep Nguyen's 0.85 cylinder-to-panel strength relation frozen unless an independent source-level revision is made globally.
E. Do not use Pf to infer missing imperfection, eccentricity, thickness or strength fields.
F. After compiler repair is independently frozen, propagate only source-measured/bounded nuisance variables as sensitivity envelopes; do not fit them.
```

## 12. Current verdict

```text
CASE1_FAILURE_LOAD_SOURCE_IDENTITY = CONFIRMED
CASE1_SOUTHWELL_Pcr_AS_EXACT_PHYSICAL_ONSET = REJECT
EXPERIMENTAL_NONIDEALITIES_PRESENT = SOURCE_CONFIRMED
CASE1_SPECIFIC_NONIDEALITY_MAGNITUDES = MOSTLY_NOT_QUANTIFIED
EXPERIMENTAL_Pf_CORRECTION = NOT_AUTHORIZED
STRUCTURAL_BACKFITTING = PROHIBITED
COMPILER_AUDIT_AND_EXPERIMENT_VARIABILITY_AUDIT = MUST_REMAIN_SEPARATE
```