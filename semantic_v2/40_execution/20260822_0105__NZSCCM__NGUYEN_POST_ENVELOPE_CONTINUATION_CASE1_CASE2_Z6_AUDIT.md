# NZ-SCCM — Nguyen post-envelope continuation audit for Case1 / Case2 / Z6

**Time:** 2026-08-22 01:05 +08:00  
**Status:** `EXECUTED / SOURCE_CONTINUATION_AUDIT / LITERAL_HISTORY_OVERLAY_REJECTED_FOR_FORMAL_PRODUCTION`

## 0. Question

The preceding strict-hard-surface audit established three distinct objects:

- NC-M6 current-map UMCG section fold;
- first Nguyen/Foster envelope contact;
- still-open post-envelope continuation.

This execution asks only:

> Can the literal Nguyen cracked/crushed state continuation be appended after an NC-M6 hard-envelope contact and become the common formal NC post-envelope law for RC, steel-shell concrete and later steel-shell UHPC?

No experiment, Zhou value or Winter value is used in any branch selection or parameter choice.

## 1. Source facts recovered before execution

Nguyen Chapter 3 does **not** define the modified Kupfer/Foster envelope as member collapse. Envelope breach changes the concrete material state.

The source state family is:

```text
U   = undamaged
TC  = cracked tension-compression
TT  = cracked tension-tension
CC  = crushed compression-compression
TCX = crushing of cracked tension-compression concrete
```

For TC, Nguyen Eqs. 3.43--3.58 use:

- tension stiffening in the major tensile direction;
- compression softening dependent on the coexisting tensile strain;
- shear retention;
- history quantities inherited from the crack event.

For TCX, Eqs. 3.77--3.80 retain the major-direction tension-stiffening law and use a descending bilinear/constant post-crushing compression branch.

The source implementation registry already records:

```text
U -> TC/TT/CC handoff = PASS_SOURCE_EXACT_WITH_FINITE_SOURCE_JUMP
TC -> TCX handoff      = PASS_CONTINUOUS
```

and records the general TC/TT/CC/TCX state family as requiring crack/crush histories and moving state fronts.

## 2. Why the audit is hybrid rather than a replacement of NC-M6 before the event

The current project material identity is NC-M6. Therefore the source continuation audit must **not** replace the pre-event NC-M6 stress field with Nguyen's original uncracked state machine.

The audit identity is instead:

\[
\boxed{
\text{NC-M6 before source-envelope contact}
\rightarrow
\text{Nguyen source TC/TT/CC/TCX continuation after contact}
}
\]

At a local TC transition, the source quantities are initialized from the envelope event:

\[
f_{cr}=\sigma_{1p},\qquad \varepsilon_{cr}=f_{cr}/E_0,
\]

then the post-crack tensile direction uses Nguyen/Foster tension stiffening with

\[
\alpha_1=10,\qquad \alpha_2=0.3,
\]

and the compressive direction uses Nguyen Eq. 3.43 compression softening. If the current compressive strain has already passed the cracked-compression peak, the local state proceeds to TCX and uses the source post-crushing continuation.

Steel remains unchanged:

- RC rebars: source one-dimensional elastic-perfectly-plastic law;
- Z6 external faces: current plane-stress von-Mises radial cap;
- Z6 web: y-only source yield clip.

The Marguerre--Airy structural backbone is unchanged.

## 3. Formal obstacle discovered before promotion

The exact Nguyen source continuation stores, depending on state,

\[
\varepsilon_{cr}(x,y,z),\quad f_{cr}(x,y,z),\quad
\sigma_p(x,y,z),\quad \varepsilon_p(x,y,z),\ldots
\]

and the cracked/crushed regions are moving subsets of the continuous section/domain.

For a section with

\[
\varepsilon_y(z)=\varepsilon_y^0+\kappa_y z,
\]

the first envelope contact may occur at an isolated thickness coordinate. After that event, the cracked region grows with one or more moving fronts, while every already-cracked point retains its own event history. Therefore a source-exact section resultant is not determined by only one crack-front coordinate; it generally also contains a continuous history field.

This agrees with the previously recovered `NSC_STATE_EQUATION_LEDGER`: general TC, TT, CC and TCX are explicitly `NOT_ADMISSIBLE_FULL_STATE` for the formal zero-quadrature operator because of direction-specific history fields, moving fronts and mixed branch occupancy.

Therefore a Gauss/material-point update can be used only as an **audit oracle**. It cannot define the formal theory.

## 4. Audit-only numerical continuation

To test the consequence rather than stopping at the source audit, a finite material-point oracle was run with:

```text
FORMAL_OPERATOR_USES_ORACLE = NO
AUDIT_ONLY_THICKNESS_STATE_POINTS = YES
STRUCTURAL_BACKBONE_MODIFIED = NO
EXPERIMENT_IN_SOLVE = 0
ZHOU_WINTER_IN_SOLVE = 0
```

The oracle starts with NC-M6 and switches individual thickness points to Nguyen TC/TCX only after their local hard-envelope event.

Because U->cracked source switching has a finite local stress jump, a discrete material point represents a finite thickness weight. Hence the discrete section experiences artificial finite resultant jumps when a point changes state. This makes continuation limits depend on the oracle thickness resolution. That behavior is itself the principal audit result.

### 4.1 Case1

Exact current-map hard contact from the preceding audit:

\[
P_{hard,1}=588.598156\ \mathrm{kN},
\qquad q_{hard,1}=0.0033103796663,
\qquad s=1.
\]

The hybrid oracle reproduces the onset scale. With an 80-point thickness oracle, the first cracked points appear at approximately `588.98 kN` and the continuation remains only a few kN above first contact before the next finite point-transition discontinuity prevents a unique converged continuation. A representative last localized equilibrium was about

\[
P\approx592.05\ \mathrm{kN}.
\]

Changing oracle resolution does not yield a monotone formal limit: representative last localized values were approximately `595.67 kN` (20-point), `592.05 kN` (80-point) and `595.10 kN` (160-point).

Therefore there is **no resolution-independent source-continuation Pu** to promote.

### 4.2 Case2

Exact current-map hard contact:

\[
P_{hard,2}=584.544674\ \mathrm{kN},
\qquad q_{hard,2}=0.0028515509569,
\qquad s=1.
\]

The 80-point hybrid oracle begins switching near `584.9 kN` and localizes only a few kN of additional equilibrium before the moving-front/material-point discontinuity dominates; a representative last localized state is about

\[
P\approx588.41\ \mathrm{kN}.
\]

Again, this is an audit-localizer value, not a formal ultimate.

Most importantly, literal source continuation does **not** drive Case1/2 toward the old `495.989/501.025 kN` uniaxial TC sensitivity diagnostic.

### 4.3 Z6

Exact current-map first hard contact:

\[
s_{hard}=0.452284,
\]

\[
q_{hard}=0.0111245993274,
\]

\[
P_{hard}=47.20955472\ \mathrm{MN}.
\]

At this section the first hybrid source transition is TC, and the most-compressed switched points quickly enter TCX because the current postbuckling bending strain is already beyond the cracked-compression peak when the NC-M6 stress reaches the source TC envelope.

Representative post-contact audit localizers at the same control section are:

| oracle thickness order | first switched load / MN | last localized continuation / MN |
|---:|---:|---:|
|20|47.260|47.354|
|40|47.260|47.508|
|80|47.260|47.326|

The sequence is not a convergent formal capacity sequence. All are close to the first hard event and remain below both post-solution Zhou/Winter comparators; no parameter is changed to alter that fact.

## 5. Source-scope issue

A second, independent restriction is important. Nguyen's full Chapter-3 state machine is source-valid as a material model, but the thesis' later initial-imperfection/tangent-modulus wall formulation explicitly restricts that approximate route to walls without out-of-plane bending cracks. The present Marguerre--Airy ultimate section, by construction, develops through-thickness bending strain and can initiate exactly those bending cracks.

Therefore copying the complete Chapter-3 history machine point-by-point into the current postbuckled section would be a new project extension, not a source-closed continuation of Nguyen's imperfection formulation.

## 6. Consequence for the meaning of a strict gate

The audit rejects the following production interpretation:

\[
\boxed{
\text{NC-M6 current map}
+
\text{independent Nguyen initial failure envelope as a runtime hard cap}
+
\text{literal Nguyen point-history state machine}
}
\]

as the common formal UMCG material law.

Reasons are independent of prediction error:

1. it double-defines post-cracking physics already regularized into the NC-M6 memoryless current operator;
2. it reintroduces continuous crack/crush history fields and moving material fronts;
3. it is not compatible with `N_formal_material_points=0` without a new history-field theory;
4. direct audit localization is resolution-sensitive;
5. the Nguyen imperfection route does not source-close out-of-plane bending-crack history evolution.

The Nguyen/Foster envelopes remain valuable and are retained as:

```text
SOURCE_STRENGTH_TARGET
MATERIAL_QUALIFICATION_ANCHOR
STATE_MECHANISM_REFERENCE
```

but are **not** an extra terminal runtime cap on top of a production current operator that already contains post-cracking/post-peak continuation.

This distinction is also mandatory for UHPC: an initial TT/TC strength envelope cannot globally clip a fibre-bridged post-cracking hardening law.

## 7. Revised transferable UMCG interpretation

The common production architecture should be

\[
\boxed{
\text{structural resultants}
\rightarrow
\text{phase-compatible stress recovery}
\rightarrow
\mathcal M_r(\varepsilon)
\rightarrow
\text{operator-internal branch/domain admissibility}
\rightarrow
\text{section equilibrium/fold}
}
\]

where each material phase has **one** production current operator.

For ordinary concrete, NC-M6 remains the current memoryless production identity and Nguyen/Foster state/envelope data qualify its TC/TT/CC mechanisms. For UHPC, the same architecture is used but with its own fibre-bridged tension and UHPC CC/TC operator. For steel, the von-Mises/yield surface remains a runtime cap because it is part of the steel production operator itself, not a second incompatible post-yield model.

## 8. Numerical identities after this audit

The audit does not invent a new Pu from the nonconvergent source-history oracle.

Retained distinctions:

```text
CASE1_2_495_501 = OLD UNIAXIAL TC SENSITIVITY ONLY
CASE1_2_588P598_584P545 = NGUYEN ENVELOPE FIRST-CONTACT DIAGNOSTIC
CASE1_2_604P450_597P732 = CURRENT NC-M6 UMCG FOLD DIAGNOSTIC
NGUYEN_HISTORY_OVERLAY_CASE1_2_FINAL_PU = NOT DEFINED

Z6_47P210 = NGUYEN ENVELOPE FIRST-CONTACT DIAGNOSTIC
Z6_51P345 = CURRENT NC-M6 UMCG FOLD PREDICTION
NGUYEN_HISTORY_OVERLAY_Z6_FINAL_PU = NOT DEFINED
```

The desirable Zhou--Winter bracket is not used as a condition. Literal Nguyen source-history overlay does not naturally produce a stable root in that bracket.

## 9. Decision

```text
POST_ENVELOPE_SOURCE_CONTINUATION_AUDIT = EXECUTED
LITERAL_NGUYEN_POINT_HISTORY_OVERLAY = REJECTED_FOR_FORMAL_PRODUCTION
REJECTION_REASON = HISTORY_FIELDS + MOVING_FRONTS + SOURCE_SCOPE + ORACLE_NONCONVERGENCE
NGUYEN_ENVELOPE_RUNTIME_TERMINAL_CAP = NO
NGUYEN_ENVELOPE_ROLE = MATERIAL_QUALIFICATION_AND_MECHANISM_REFERENCE
NC_M6_MEMORYLESS_CURRENT_OPERATOR = RETAINED
STEEL_VM_RUNTIME_CAP = RETAINED
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_MATERIAL_POINTS = 0
STRUCTURAL_BACKBONE_MODIFIED = NO
DATASET_SPECIFIC_CALIBRATION = 0
```

The next admissible work is therefore **not** to add more Nguyen history variables. It is to keep one material current operator per phase and judge residual bias/material-input uncertainty at the system level. In particular, Swartz tensile-strength identity remains source-open, while Z6 already provides a strong SC transfer test for the common phase-compatible UMCG.