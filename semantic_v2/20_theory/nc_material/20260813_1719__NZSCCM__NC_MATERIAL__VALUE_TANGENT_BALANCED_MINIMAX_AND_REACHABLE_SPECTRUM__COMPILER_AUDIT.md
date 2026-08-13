# NZ-SCCM NC material compiler — value/tangent balanced minimax and reachable-spectrum audit

**Timestamp:** 2026-08-13 17:19 +08:00  
**Identity:** COMPILER-LAYER AUDIT / CANDIDATE OBJECTIVE / NOT PRODUCTION  
**Theory change:** NO  
**R10 change:** NO  
**Structural calibration:** NO

## 0. Trigger

The Case1 reconstruction showed that the current N48-C1/MM repair cannot be interpreted as a tangent-only correction. At the historical direct-N48 Case1 state, replacing only the material compiler by the current C1/MM compiler increased the axial resultant by about +19.16 kN; subsequent re-equilibration reduced the load by about -9.75 kN, leaving a net increase of about +9.41 kN.

Therefore the compiler must be audited against the source material operator itself for **both value and first derivative over the occupied material domain**, rather than accepting exact C1 fidelity only at `lambda=0`.

This audit does not use any Swartz `Pcr`, `Pf`, historical `Pu`, current `Pu`, Case number error, or structural root in coefficient generation.

```text
EXPERIMENT_IN_COMPILER_OBJECTIVE = NO
STRUCTURAL_PU_IN_COMPILER_OBJECTIVE = NO
STRUCTURAL_ROOT_IN_COMPILER_OBJECTIVE = NO
R10_MATERIAL_TARGET = FROZEN
N48_ORDER = 48
CAYLEY_HAMILTON_COMPATIBILITY = REQUIRED
GENERAL_D15_COMPATIBILITY = REQUIRED
```

## 1. Current compiler and the identified limitation

Current production identity remains, until a later explicit promotion decision:

```text
U  = N48-C1
C  = N48-C1
T7 = N48-C1
T  = N48-C1-CONSTRAINED-MINIMAX
```

The C1 constraints are exact source conditions at `lambda=0`:

\[
F_{48}(0)=F_{R10}(0),\qquad F'_{48}(0)=F'_{R10}(0).
\]

For `T`, the current constrained minimax objective primarily minimizes full-hull **value** error subject to exact C1. This successfully improved the narrow tensile-boundary-layer value representation relative to plain C1, but does not control full-hull first-derivative fidelity.

The later Case1 full-field reconstruction demonstrates why this matters: the plate samples a continuum of material coordinates, not only `lambda=0`.

## 2. Source-only fidelity metrics

For each primitive `F in {U,C,T,T7}` on a declared material interval `[lambda_a,lambda_b]`, define

\[
E_0(F)=\|F_{48}-F_{R10}\|_{L^\infty},
\]

\[
E_1(F)=\lambda_h\|F'_{48}-F'_{R10}\|_{L^\infty},
\qquad
\lambda_h=(\lambda_b-\lambda_a)/2.
\]

`E0` is dimensionless value fidelity; the scaled `E1` is a dimensionless first-tangent fidelity measure on the same material interval.

The objective must not combine these with an arbitrary engineering weight selected from panel-response accuracy.

## 3. Balanced minimax candidate (BMM)

For one primitive, retain the exact C1 affine space

\[
\mathcal F_{C1}=\{a:Ga=d_F\}.
\]

First compute the two source-only attainable optima within the same degree-48 affine space:

\[
E_0^*=\min_{a\in\mathcal F_{C1}}\|p_a-F_{R10}\|_\infty,
\]

\[
E_1^*=\min_{a\in\mathcal F_{C1}}\lambda_h\|p'_a-F'_{R10}\|_\infty.
\]

Then define the **balanced minimax** candidate by

\[
\boxed{
\min_{a,\tau}\ \tau
}
\]

subject to

\[
\|p_a-F_{R10}\|_\infty\le\tau E_0^*,
\]

\[
\lambda_h\|p'_a-F'_{R10}\|_\infty\le\tau E_1^*,
\]

\[
Ga=d_F,\qquad \tau\ge1.
\]

Interpretation: the candidate minimizes the worst relative degradation from the independently attainable best value approximation and best tangent approximation. There is no fitted value/tangent weight and no structural response in this definition.

The diagnostic solve used material-coordinate linear-program/exchange calculations. These material-coordinate operations are coefficient-generation tools, not structural spatial quadrature or material-point discretization. A production promotion would require a frozen exchange/Remez-style material-coordinate implementation and independent extremum verification.

## 4. Case1 broad-interval source-fidelity result

Case1 source inputs used here are only its material inputs and its already-declared compiler interval:

```text
fc = 22.81 MPa
E0 = 21730 MPa
eps0 = 0.00210
compiler interval = [-1.12, +0.105]
N = 48
```

The source-only BMM exchange audit gave approximately:

|primitive|current E0|current E1|BMM E0|BMM E1|max abs BMM coefficient|
|---|---:|---:|---:|---:|---:|
|U|0.001186|1.477|0.000940|0.0821|0.596|
|C|0.012406|3.814|0.00937|0.951|0.613|
|T|~0.0819|~187.45|0.0903|9.13|0.318|
|T7|0.126081|14.33|0.0486|6.86|0.247|

The important result is not a structural load change. It is that degree 48 has a large amount of unused freedom for improving full-hull first-tangent fidelity while keeping coefficients O(1). For `T`, the balanced solution accepts roughly a 10% increase of the already-minimax value error in exchange for an approximately 95% reduction of the full-hull scaled derivative error.

## 5. Cases1-8 group diagnostic

Using only each specimen's source material parameters and the previously declared compiler intervals (`[-1.12,0.105]` for Cases1-4 and `[-1.16,0.105]` for Cases5-8), the rounded batch diagnostic showed the following mean changes:

|primitive|mean current E0|mean BMM E0|mean current E1|mean BMM E1|
|---|---:|---:|---:|---:|
|U|0.001166|0.000977|1.487|0.089|
|C|0.012553|0.00942|3.775|0.972|
|T|0.0833|0.0927|190.2|9.35|
|T7|0.1337|0.0525|23.6|7.19|

This is a **material representation result only**. It is not evidence that BMM improves Swartz ultimate-load accuracy, and the group statistics are not used to choose the coefficients.

## 6. Structural crosscheck does not promote BMM

An independent audit-only structural evaluator was used only after the source-only BMM coefficients had been generated.

At the old direct-N48 Case1 state, the BMM compiler gives an axial resultant around 615.6 kN, between direct-N48 (~599.5 kN) and current C1/MM (~618.7 kN). At the reconstructed current C1/MM state, BMM gives a load near 606 kN but that state is not BMM equilibrium.

A coarse BMM equilibrium audit did **not** demonstrate a material reduction of the Case1 first load maximum; it remained in the same roughly 607-609 kN range.

Therefore:

```text
BMM_SELECTED_BECAUSE_CASE1_ERROR_IMPROVES = NO
BMM_PRODUCTION_PROMOTION = NO
CASE1_PF_USED_TO_CHOOSE_BMM = NO
```

BMM is retained because it is a materially better source-fidelity objective, not because it happens to move a panel result in a desired direction.

## 7. Reachable-spectrum finding

At the reconstructed current Case1 load-maximum state, the independent continuous-field audit indicated approximately

```text
lambda_min ~ -1.036 to -1.037
lambda_max ~ +0.048 to +0.049
```

whereas the declared compiler hull is `[-1.12,+0.105]`.

A **trial only** BMM solve on `[-1.05,+0.055]` gave:

|primitive|trial E0|trial E1|
|---|---:|---:|
|U|0.000231|0.0319|
|C|0.00612|0.751|
|T|0.0610|7.24|
|T7|0.00643|0.929|

This shows that broad unused tails of the compiler interval materially consume approximation power. However, the trial interval is **not authorized as a new production interval**, because it was inferred after seeing a solved structural state.

## 8. Required non-calibrating self-consistency route

If compiler interval tightening is pursued, it must be self-consistent and independent of experiment:

```text
conservative source interval
-> generate source-only compiler
-> blind structural branch solve
-> continuous Bernstein/interval enclosure of all reachable principal values
-> derive a conservative reachable material envelope
-> regenerate source-only compiler on that envelope
-> resolve
-> repeat until compiler interval and reachable spectrum are self-consistent
```

The envelope may be tightened only from the structural equations and certified continuous spectrum, never from `Pf`, desired `Pu`, historical roots, or panel error.

## 9. Degree escalation diagnostic

For Case1 `T` on the broad interval, a source-only degree sweep under exact C1 and the balanced objective gave approximately:

```text
N=48 : E0 ~0.091, E1 ~9.1
N=64 : E0 ~0.063, E1 ~8.2
N=80 : E0 ~0.047, E1 ~7.3
N=96 : E0 ~0.037, E1 ~6.6
```

Moderate degree escalation improves value fidelity but does not remove the derivative difficulty created by the very narrow R10 tensile transition relative to the full compiler width. Therefore "just increase N" is not presently the preferred first repair.

## 10. Current verdict

```text
CURRENT_N48_C1_MM = RETAINED_PRODUCTION_PENDING_REVIEW
BMM = SOURCE_FIDELITY_CANDIDATE / NOT_PRODUCTION
EXACT_C1_AT_LAMBDA_ZERO = RETAINED
FULL_HULL_VALUE_AND_TANGENT_FIDELITY = MUST_BE_JOINTLY_REPORTED
REACHABLE_SPECTRUM_SELF_CONSISTENCY = CANDIDATE_GOVERNANCE / NOT_YET_PRODUCTION
R10_CHANGED = NO
N48_ORDER_CHANGED = NO
STRUCTURAL_CALIBRATION = NO
FORMAL_SPATIAL_QUADRATURE = 0
```

The next compiler-layer task is to freeze a material-coordinate exchange implementation of BMM, verify extremal errors without a structural-space grid, and then recompile the formal zero-spatial `P,Rq,L,KZ` expressions before any production replacement decision.