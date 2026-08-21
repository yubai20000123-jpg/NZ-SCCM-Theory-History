# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-22 00:18 +08:00  
**Status:** `MARGUERRE_AIRY_EXPLICIT + UMCG_ARCHITECTURE_ACTIVE / FINAL_STRICT_POST_ENVELOPE_CLOSURE_OPEN`

## 0. Governing architecture

The structural backbone remains frozen:

\[
P_{pb}(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0),
\]

\[
n(s;q)=\frac{P_{pb}(q)}b+Gq(q+2q_0)(1-2s^2),
\qquad
m(s;q)=Jqs.
\]

Canonical structural theory:

`semantic_v2/20_theory/20260821_1733__NZSCCM__MARGUERRE_AIRY_EXPLICIT_LIMIT_THEORY_V1.md`

Unified material-capacity architecture:

`semantic_v2/20_theory/20260821_2315__NZSCCM__UNIFIED_MULTIAXIAL_CAPACITY_GATE_V1.md`

Mandatory common interface:

\[
\boxed{
\text{structural resultants}
\to
\text{phase stress recovery}
\to
\text{current material map}
\to
\text{hard material surfaces / state transition}
\to
\text{admissible section continuation}
}
\]

```text
STRUCTURAL_BACKBONE = FROZEN
UMCG_ARCHITECTURE = RETAINED
UMCG_DIMENSION = PLANE_STRESS_2D
SIGMA_Z_RECOVERY = NOT_ACTIVATED
RITZ_ORDER = NONE
LOAD_PATH_TRACKING = NOT_REQUIRED AT STRUCTURAL LEVEL
FORMAL_SPATIAL_QUADRATURE = 0
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
STRUCTURE_SPECIFIC_CAPACITY_MULTIPLIER = PROHIBITED
```

## 1. Strict-hard-surface correction

Latest audit:

`semantic_v2/40_execution/20260822_0015__NZSCCM__STRICT_HARD_ADMISSIBILITY_CASE1_CASE2_Z6_AUDIT.md`

The ordinary-concrete Nguyen/Foster/Kupfer hard envelopes are now explicitly distinguished from the smooth NC-M6 current map.

A literal execution of

\[
\sigma=\mathcal M(\varepsilon),
\qquad
F_{CC},F_{TC},F_{TT}\le0,
\qquad
F_{VM}^{steel}\le0
\]

without adding any new projection/capping law was performed for Swartz Case1/2 and Z6.

Critical finding:

\[
\boxed{\text{first hard-envelope contact is a material state-transition event, not automatically global collapse.}}
\]

Nguyen's source model permits cracked/crushed continuation after envelope contact. Therefore neither of the following is yet the final strict production theory:

1. smooth NC-M6 current-map section fold with no hard transition surface;
2. member termination at the first hard-envelope touch.

The final strict UMCG requires a source-grounded admissible post-envelope continuation.

## 2. Swartz Case1/2 status correction

Mandatory source mapping remains

\[
\rho_x=\rho_y=p_{table}.
\]

The prior numbers must be separated by identity:

|Object|Case1 kN|Case2 kN|Status|
|---|---:|---:|---|
|corrected-reinforcement uniaxial N-M candidate|567.712|561.638|PRE-GATE|
|earlier separate TC-contact diagnostic|495.989|501.025|MECHANISM SENSITIVITY ONLY|
|smooth current-map UMCG fold|604.450|597.732|AUDIT-ONLY, NON-STRICT|
|literal current-map + hard-envelope first event|588.598|584.545|STRICT FIRST EVENT, NOT FINAL ULTIMATE|

The consistent literal strict events occur at \(s=1\):

\[
P_{hard,1}=588.598156\rm\ kN,
\]

\[
P_{hard,2}=584.544674\rm\ kN.
\]

Post-solution errors are approximately

\[
+20.075\%,\qquad +15.374\%.
\]

Therefore the earlier statement that the unified strict gate naturally reduces Case1/2 to about the experiment is **superseded**. The `495.989/501.025 kN` values came from a different uniaxial-state TC diagnostic and are not the unified strict solution.

Swartz specimen-specific \(f_t\) remains source-open. No specimen-specific correction factor is authorized.

## 3. Z6 status correction

PRE-GATE uniaxial N-M candidate:

\[
P_u^{pre}=56.37942109\rm\ MN.
\]

Smooth current-map phase-rebalanced UMCG fold previously reported:

\[
P^{map-fold}=51.34502179\rm\ MN.
\]

That value is now downgraded from `FINAL` to

```text
Z6_51P345_MN = CURRENT_MAP_UMCG_FOLD_CANDIDATE
```

because the Nguyen hard concrete surface was not simultaneously retained as a transition constraint.

The literal hard-envelope first-event search over the control coordinate gives

\[
\boxed{s_{hard}\approx0.452284},
\]

\[
\boxed{q_{hard}=0.0111245993274},
\]

\[
\boxed{P_{hard}=47.20955472\rm\ MN}.
\]

The active point is at the concrete-core face \(z=-61\rm\ mm\), in TC, with approximately

\[
\sigma_1=+0.990248\rm\ MPa,
\qquad
\sigma_2=-27.099174\rm\ MPa,
\]

and the tensile TC hard-envelope equality active.

Only after fixing that event, comparison gives

\[
-4.602\%\quad\text{vs Zhou},
\]

\[
-5.931\%\quad\text{vs Winter}.
\]

Thus treating first TC-envelope contact as the member ultimate makes Z6 too conservative and does **not** naturally yield

\[
P_{Zhou}<P_{NZ-SCCM}<P_{Winter}.
\]

The Zhou--Winter bracket remains a post-solution desirability observation only and is prohibited as a root condition.

Current Z6 identities:

```text
Z6_56P379_MN = UNIAXIAL_PRE_GATE
Z6_51P345_MN = CURRENT_MAP_UMCG_FOLD_CANDIDATE
Z6_47P210_MN = LITERAL_FIRST_HARD_ENVELOPE_EVENT
Z6_FINAL_STRICT_POST_ENVELOPE_PU = OPEN
```

## 4. What the strict audit proves

The current theory has now bracketed the missing physics from two sides:

- ignoring the hard transition surface can leave too much post-envelope current-map capacity;
- terminating the member at first envelope contact is too severe because Nguyen permits cracked/post-peak redistribution.

Therefore the missing object is not a scale factor. It is

\[
\boxed{
\text{one transferable source-grounded post-envelope continuation under the same UMCG architecture}
}
\]

for ordinary concrete, followed later by the corresponding UHPC continuation.

This continuation must preserve:

- common NC--SC--SUHPC architecture;
- no experiment/FEM in root selection;
- no structure-specific multiplier;
- phase compatibility and equilibrium;
- steel von-Mises/yield admissibility;
- hard material transitions rather than silent surface crossing.

## 5. Steel-shell UHPC status

Codex geometry/material audit remains active:

`current/audits/NZ_SCCM_STEEL_SHELL_UHPC_CODEX_R02_DAMAGE_GEOMETRY_INTEGRATION_20260821.md`

For BH005--BH050:

```text
BH_32MM_WEB_HEIGHT = SUPERSEDED_AS_CURRENT_VALIDATION_GEOMETRY
BH_37MM_WEB_HEIGHT = STRONGLY_INDICATED_REBASE_CANDIDATE
BH_37MM_FINAL_CONTRACT = PENDING_FORMAL_FREEZE
BH_CURRENT_QUANTITATIVE_VALIDATION_BASELINE = OPEN
```

T120/T360 existing web-included values remain working scale checks, not verified strict-UMCG predictions.

## 6. Governance

```text
SWARTZ_SPECIFIC_K = PROHIBITED
SC_GLOBAL_SCALE_FACTOR = PROHIBITED
SUHPC_EMPIRICAL_CONFINEMENT_MULTIPLIER = PROHIBITED
STRUCTURAL_PU_BACKFIT_TO_MATERIAL = PROHIBITED
Z6_51P345_FINAL_STATUS = SUPERSEDED
CASE1_2_495_501_AS_UNIFIED_STRICT = SUPERSEDED
FIRST_HARD_EVENT_AS_GLOBAL_ULTIMATE = NOT GENERALLY AUTHORIZED
POST_ENVELOPE_SOURCE_CONTINUATION = CURRENT PRIMARY OPEN GAP
```

## 7. Recommended next execution

Before extending strict UMCG to T120/T360/BH, close the ordinary-concrete post-envelope continuation in one unified form. The immediate validation set should remain only:

1. Swartz Case1/2 — to test TC/cracking continuation;
2. Z6 — to test TC + steel multiaxial redistribution;
3. only after those two are coherent, expand to Swartz24 and steel-shell UHPC.

No attempt should be made to force Case1/2 to zero error or Z6 into the Zhou--Winter interval.