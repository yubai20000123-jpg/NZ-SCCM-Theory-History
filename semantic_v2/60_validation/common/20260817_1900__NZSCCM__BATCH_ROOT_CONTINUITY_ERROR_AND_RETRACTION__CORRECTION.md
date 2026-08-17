# NZ-SCCM — 2026-08-17 批量结果膜内标量根连续性错误与撤回

**Timestamp:** 2026-08-17 19:00 +08:00  
**Identity:** IMPLEMENTATION CORRECTION / BATCH RESULT RETRACTION  
**Parent theory:** `20260817_1824__NZSCCM__ZERO_SPATIAL_DISCRETIZATION_FINITE_CURRENT_TRUE_INFINITE_D15__CANONICAL_LOCK.md`

## 1. Correction

The canonical theory remains valid. The error is in the 2026-08-17 bulk root localization used for Case01–Case24 and Z0–Z5.

The active Airy-scalar current membrane closure is

\[
r=\lambda_A M a(\nu),
\]

with the elastic degeneration

\[
\lambda_A\to1
\]

on the physical connected branch as the membrane driver tends to zero. The physical nonlinear root must therefore be obtained by branch continuation from that positive Airy/FvK limit; `R_A=0` alone does not authorize selecting an arbitrary algebraic root at each load state.

The bulk localizer failed to enforce this connected-root identity and selected disconnected scalar roots.

## 2. Direct evidence from the retracted batch

The persisted bulk CSV contains, among others,

```text
Z0  lambda_A = -0.1494130344
Z1  lambda_A = +0.4040830493
Z2  lambda_A = +0.4499556603
Z3  lambda_A = -0.1425932520
Z4  lambda_A = -0.9682078202
Z5  lambda_A = -13.1298459
```

Z5 is decisive: `q=1.284475e-4`, hence its membrane driver is already very small, yet the selected scalar amplitude is `lambda_A=-13.13` instead of remaining on the branch connected to `lambda_A=1`. This is a disconnected/nonphysical Airy-scalar root.

The same symptom appears in many Swartz batch rows (negative `lambda_A`), while the released Case21 anchor remains on its independently established connected root (`lambda_A=+0.08623596`).

## 3. Historical consistency

The repository had already locked that:

1. correct compatibility-generated FvK/Airy membrane redistribution has positive postbuckling stiffness in the elastic degeneration;
2. earlier apparent membrane-induced large downward shifts were retracted as over-relaxation/root-space errors;
3. Z6 was the unique below-Zhou case in the pre-redistribution comparison hierarchy, so a new result in which all Z0–Z5 suddenly fall below Zhou is a mandatory implementation-warning pattern, not a new physical conclusion.

The 2026-08-17 bulk run violated that history by treating `R_A=0` as a pointwise root equation without preserving branch identity.

## 4. Retraction

```text
20260817_1946_CASE01_CASE24_Z0_Z5_BATCH = RETRACTED_AS_PRODUCTION_RESULT
CASE21_RELEASED_ANCHOR_366.767828685_kN = RETAINED
Z6_RELEASED_ANCHOR_48.4061215_MN = RETAINED
CANONICAL_ZERO_SPATIAL_DISCRETIZATION_TRUE_INFINITE_D15_THEORY = RETAINED
```

The reported Z0–Z5 values `31.99, 20.02, 36.54, 38.20, 59.43, 12.64 MN` and their Zhou/Winter errors are not valid production predictions.

The newly generated Case01–20 and Case22–24 values are also not retained as production predictions because their membrane scalar roots were not certified as connected to the physical Airy branch.

## 5. Correct production root rule

For every specimen:

```text
start from the small-amplitude elastic/near-elastic state
lambda_A -> +1 on the compatibility-generated Airy/FvK branch
continue the same root in the loading parameter
solve total Rq=0 and RA=0 with all material phases present
never select a different algebraic RA root independently at a later state
locate the first reachable limit point on that connected branch
only after Pu is frozen compare with Pf / Zhou / Winter
```

This correction changes no material parameter, no D15 identity, no geometry, no formal integration counter, and introduces no new theory branch. It repairs only the root-continuity implementation.