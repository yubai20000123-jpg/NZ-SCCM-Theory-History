# PF1 PATH INVARIANTS LOCK — 2026-08-10

**Status:** CURRENT GOVERNANCE / HARD EXECUTION BOUNDARY  
**Trigger:** user explicitly reiterated that the fundamental restrictions must not change and the route must not drift while executing PF1.

## 1. Structural problem identity is frozen

PF1 is a mathematical closure task only. It is not authorized to change the structural mechanics problem.

The following remain frozen:

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
KINEMATICS = NGUYEN_SECOND_ORDER / CURRENT CASE21 FINITE ANALYTIC KINEMATICS
STRUCTURAL_TARGETS = P(D,q), Rq(D,q), L(D,q)
L = P_,D Rq_,q - P_,q Rq_,D
```

No alternative structural residual, limit criterion, effective-width substitute, FE eigenproblem, load calibration, or different generalized-coordinate problem may replace these targets during PF1.

## 2. Formal integration identity is immutable

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
FORMAL_INTEGRATION = ANALYTIC_EXACT
ELEMENT_INTEGRATION = PROHIBITED
MATERIAL_POINT_GRID = PROHIBITED
SPATIAL_CELLS = PROHIBITED
GAUSS_SIMPSON_ADAPTIVE = PROHIBITED_IN_FORMAL_OPERATOR
COLLOCATION_AS_FORMAL_OPERATOR = PROHIBITED
```

Auxiliary variables, algebraic curves, periods, differential systems, special functions, analytic continuation, and finite matrix recurrences are allowed only when they analytically represent the same whole-halfwave integral and introduce no hidden spatial/material-point quadrature.

## 3. Current material-route identity is frozen during PF1

PF1 must start from the already accepted current architecture:

```text
M1R source-shaped rational primitive compiler
-> invariant / Cayley-Hamilton resolvent reduction
-> s = I1 exact inner elimination
-> canonical single/pair resolvent outer periods
```

PF1 is not authorized to:

- return to M1 high-degree free two-dimensional polynomial surfaces;
- change the frozen-NC oracle to improve structural results;
- calibrate any material coefficient against Case21 / Swartz24 / UCFT Pu;
- introduce TT/TC/CC spatial partitions;
- replace the current route by coarea/pushforward before PF1 is actually shown to fail;
- start UHPC production fitting or shell/Y production closure.

## 4. PF1 authorized scope

PF1 may only attempt:

```text
canonical M1R single-resolvent outer algebraic kernel
-> genus-2 de-Rham basis
-> exact Griffiths/Hermite reduction
-> finite Gauss-Manin connection in physical parameters
-> relative/logarithmic-period extension
-> pair-resolvent extension
-> y-direction closure
-> finite whole-halfwave Picard-Fuchs / Gauss-Manin system
```

Every accepted reduction must be an identity modulo explicitly recorded exact differentials / endpoint terms. Numerical sampling may be used only as an independent audit of an already-derived identity and can never define the formal operator.

## 5. Fail-fast rule

If any PF1 stage requires one of the following as a production ingredient, PF1 must stop at that stage and report FAIL/HOLD rather than silently changing route:

```text
spatial quadrature
material-point integration
space subdivision / cells
adaptive integration
uncertified black-box Integral objects
structure-based material refitting
replacement of P/Rq/L
replacement of the one-complete-halfwave domain
```

Only after a genuine PF1 mathematical failure may the already-retained next candidate `joint pushforward/coarea` be opened, and that transition itself requires a new recorded checkpoint.

## 6. GitHub checkpoint discipline

PF1 execution follows `CONTINUOUS_CHECKPOINT_SYNC`:

1. this invariant lock is committed before the long derivation;
2. each stable PASS/FAIL/HOLD mathematical stage is committed;
3. `current/CURRENT_STATE.md` is updated only after a stable new state exists;
4. historical identities are not overwritten.

This file does not add a new theory. It freezes the boundary within which the already-authorized PF1 next step must be executed.
