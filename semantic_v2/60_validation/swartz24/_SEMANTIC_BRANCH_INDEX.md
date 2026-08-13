# Swartz24 validation semantic branch

Current stored validation entry:

- the 24-row C1/MM + general-D15 first-load-maximum comparison is located in `semantic_v2/50_results/swartz24/`.

## Governing-capacity boundary

The 24 stored loads are equilibrium first-load-maximum candidates. Governing physical capacity additionally requires the same-branch full current-tangent ordering:

```text
first KZ=0 vs first L=0, g:+->- maximum
```

Case21 has the formal zero-spatial ordering completed. The other 23 formal KZ orderings remain pending.

## 2026-08-13 kinematics / halfwave provenance correction

Highest-priority kinematics audit:

- `20260813_1756__NZSCCM__SWARTZ24__SECOND_ORDER_KINEMATICS_AND_HALFWAVE_PROVENANCE__AUDIT.md`

Source-backed mode geometry is:

```text
Cases 1-16  : approximately one longitudinal halfwave -> ell=2440 mm
Cases 17-24 : two longitudinal halfwaves              -> ell=1220 mm
```

A later three-representative-panel blind input incorrectly stated `b=ell=1220 mm` for Case1, Case14 and Case21. The recent Case1 reconstruction also used `ell=1220 mm`. Therefore that reconstruction is now **partially superseded on structural-kinematics provenance**, even though it reproduces the stored 608.925 kN value closely.

The stored 608.925 kN result itself is not silently deleted or replaced; its exact execution provenance must be recovered before deciding whether it inherited the same halfwave error.

An audit-only source-correct Case1 rerun with `ell=2440 mm`, with R10/current C1-MM otherwise unchanged, gives a first-load-maximum around 647.5 kN. Thus correcting the halfwave length does not cure the Case1 overprediction; it increases it in the audit. This number has no production identity because the rerun used high-order spatial Gauss only as an independent diagnostic.

The same kinematics audit also finds that omitted third/higher geometric terms are too small by order-of-magnitude to plausibly explain a 10-25% capacity error at the current displacement amplitudes. The more serious open kinematic issue is the reduced `(D,q)` / fixed-mode subspace compared with Nguyen's general `u(x,y),v(x,y),w(x,y)` fields.

## 2026-08-13 ideal-mode / imperfection / reserve mechanism audit

New source-grounded mechanism audit:

- `20260813_1816__NZSCCM__SWARTZ24__IDEAL_MODE_IMPERFECTION_AND_POSTBUCKLING_RESERVE__MECHANISM_AUDIT.md`

Current synthesis:

```text
CLASSICAL a/b=2 ISOTROPIC BASELINE:
    two square halfwaves are the lowest mode;
    one full-length halfwave has classical k=6.25 vs k=4.00, i.e. 1.5625 times the critical level.

NGUYEN PERFECT NONLINEAR BASELINE:
    Cases1-16 -> approximately one full-length halfwave;
    Cases17-24 -> two halfwaves.

THEREFORE:
    one-wave existence in Cases1-16 does not uniquely prove initial imperfection;
    off-center / unequal / localized bulges are stronger nonideality signatures.
```

The 24-panel source table gives experimental bulge locations and postbuckling reserve. Across the current signed failure-load errors, the experimental reserve has an audit correlation of approximately `r=-0.626`: specimens with larger measured postbuckling reserve tend to be underpredicted by the present model.

Case21 is the strongest modal-consistency benchmark: source location is approximately top-half + bottom-half (two-wave family), matching Nguyen's perfect slender-panel mode, and current error is about -0.74%. Cases19 and21 are the two clearest two-halfwave source patterns and are comparatively well predicted. Cases22-24 depart toward a single/localized dominant zone and show positive current errors, which is qualitatively consistent with imperfection/eccentricity/support-selected weaker modes.

Conversely, Cases9-16 mostly show the centered full-length one-wave that Nguyen predicts even for a perfect nonlinear wall, while they have large experimental postbuckling reserves and mostly negative current errors. This strongly rejects `initial imperfection alone` as a global explanation.

The current best non-calibrating mechanism hypothesis is a competition:

```text
P_exp_failure
~ P_ideal_source_faithful
  - downward imperfection/eccentricity/support/localization effect
  + upward postbuckling redistribution/reserve
  + specimen/material scatter
```

No term may be inferred from `Pf` for parameter generation.

## Case1 reconstruction history

Priority files retained for evidence:

- `20260813_TUNK__NZSCCM__CASE1__COMPILER_VALUE_SHIFT_AND_FULL_FIELD_KZ_RECONSTRUCTION__AUDIT.md` — **PARTIALLY_SUPERSEDED ON HALFWAVE PROVENANCE**; retains value/tangent decomposition evidence for the square-halfwave execution identity.
- `20260813_TUNK__NZSCCM__CASE1__CURRENT_BRANCH_KZ__AUDIT_TRACE.csv` — same square-halfwave audit identity.
- `20260813_TUNK__NZSCCM__SWARTZ24__CONTROL_ORDERING_REFINEMENT_AFTER_CASE1_RECONSTRUCTION__AUDIT.md` — same qualification.
- `20260813_1719__NZSCCM__CASE1_TO_CASE8__SOURCE_SPECIMEN_VARIABILITY_AND_TEST_NONIDEALITY__AUDIT.md`
- `20260813_1647__NZSCCM__SWARTZ24__LIMIT_POINT_VS_TANGENT_LOSS_CONTROL_ORDERING__AUDIT.md`
- `20260813_1035__NZSCCM__SWARTZ24__FULL_SAME_EXPRESSION_L_KZ_BULK_GATE__EXECUTION_AUDIT.md`
- `20260811_TUNK__NZSCCM__SWARTZ24__C1_TANGENT_REPAIR_AT_DIRECT_N48_STATES__AUDIT_TABLE.csv`

The square-halfwave Case1 audit had reconstructed

```text
D ~ 0.98833818
q ~ 0.00083313173
P ~ 608.92642 kN
KZ_audit at maximum ~ +3066.68 N/mm
```

and isolated a compiler value/tangent effect. Those calculations remain useful for diagnosing that specific execution identity, but they are no longer accepted as a source-faithful Case1 structural reconstruction until the halfwave provenance is reconciled.

## Source-level experimental audit

The original Swartz papers and Nguyen's later review establish several real test/specimen nonidealities absent from an average-property ideal plate:

```text
CASE1_Pf_110p2_KIP = SOURCE_CONFIRMED
CASE1_Pcr_125p1_KIP = SOUTHWELL_DERIVED / HIGH_BIAS_RISK
WITHIN_PANEL_THICKNESS_VARIATION = ABOUT +/-3% / SOURCE_EXPLICIT
UNAVOIDABLE_LOAD_ECCENTRICITY = SOURCE_EXPLICIT
DISCRETE_SUPPORT_AND_LOAD_BEDDING = SOURCE_EXPLICIT
CURRENT_b_OVER_400 = PROJECT_INPUT / NOT_MEASURED_CASE1_IMPERFECTION
LOCAL_MATERIAL_FIELD = NOT_MEASURED; TWO CYLINDER AVERAGE ONLY
```

These are credible sources of individual-specimen capacity scatter, but no Case1-specific correction magnitude is currently source-closed. They may not be inferred from `Pf` or used to calibrate material/structure parameters.
