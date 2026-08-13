# NZ-SCCM Swartz24 full same-expression L/KZ bulk-gate execution audit

**Timestamp:** 2026-08-13 10:35 +08:00  
**Identity:** CURRENT EXECUTION AUDIT / NO FALSE PASS / NO THEORY CHANGE

## 0. Purpose

The user authorized completion of the 24-panel `L/K_Z` bulk gate. This audit records what can be reproduced from the current governing repository state and what still prevents a legitimate `24/24 PASS` signature.

No R10 change, N48-order change, panel calibration, spatial quadrature, spatial sampling, material-point grid or spatial subdivision is introduced.

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
ACTIVE_MODE = m=1
KINEMATICS = NGUYEN_SECOND_ORDER
R10_MATERIAL_TARGET = FROZEN
N48_ORDER = 48
CAYLEY_HAMILTON = GOVERNING
EXACT_MOMENT_ENGINE = D15_GENERAL_TRIG_MOMENTS
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_CALIBRATION = NO
```

## 1. Governing gate

For each panel, the current production gate requires the same finite analytic expressions for

\[
P(D,q),\qquad R_q(D,q),
\]

and their same-expression derivatives

\[
P_D,\ P_q,\ R_{q,D},\ R_{q,q},
\]

with

\[
L=P_D R_{q,q}-P_qR_{q,D}.
\]

The accepted limit state must belong to the primary connected equilibrium branch from `(0,0)` and be the first `+ -> -` local maximum of P. The Zhou/Navier current-tangent quantity

\[
K_Z=K_{Z,c}^{mat}+K_{Z,c}^{geo}+K_{Z,s}^{mat}+K_{Z,s}^{geo}
\]

must be checked on the same branch to establish whether tangent loss precedes the limit point.

## 2. Current repository state before this audit

The repository already freezes:

```text
SWARTZ24_CURRENT_Pu = 24/24 AVAILABLE
SWARTZ24_CURRENT_Pu_VS_FAILURE_COMPARISON = COMPLETE
CASE21_FULL_L_KZ_GATE = PASS
SWARTZ24_FULL_L_KZ_PRODUCTION_GATE = PENDING_24_PANEL_BULK_COMPLETION
```

The current 2026-08-13 Swartz continuation retains current corrected `(D_u,q_u)` coordinates only for Cases 19, 20, 21, 22, 23 and 24. Cases 1–18 have current `Pu` values in the frozen comparison table, but their corrected C1/MM + general-D15 `(D_u,q_u)` coordinates are not retained in the current result package.

This distinction is critical: an old `(D,q)` from the 2026-08-11 direct-N48 production run cannot be silently attached to a later current Pu.

## 3. Independent exact-moment implementation regression performed in this audit

A separate zero-spatial invariant-ring implementation was constructed for the governing current operator. Structural-space integration is performed by analytic trigonometric/thickness moments; no structural-space point grid, Gauss rule, Simpson rule, collocation or cells are used.

At the current formal Case21 root

\[
D=0.7822850963110681,\qquad q=0.0017707520964949533,
\]

the independent base P/R engine reproduced

```text
P  = 365580.426864572 N
Pc = 336968.776632496 N
Ps =  28611.650232076 N
Rq =       1.191279183 N mm
```

against the frozen current values

```text
P  = 365580.427565 N
Pc = 336968.777333 N
Ps =  28611.650232 N
```

The load difference is about `0.000700 kN`; the small Rq residue is consistent with coefficient/minimax numerical tolerance. Thus the independent exact-moment base P/R implementation passes the Case21 regression at engineering precision.

## 4. Provenance test: old 2026-08-11 roots are not valid substitutes for missing current roots

Several old direct-N48 roots were deliberately inserted into the current C1/MM + general-D15 P/R engine only as a provenance rejection test.

|Case|old 2026-08-11 D|old q|current-expression P at old root / kN|current-expression Rq at old root / N mm|current frozen Pu / kN|verdict|
|---:|---:|---:|---:|---:|---:|---|
|1|0.994049|~0.0007740|~631.817|~+541065|608.925|REJECT OLD ROOT|
|2|0.994522|~0.0006924|~619.089|~+486794|596.865|REJECT OLD ROOT|
|4|1.024547|~0.0006073|~575.225|~+460743|555.423|REJECT OLD ROOT|

These are large equilibrium violations, not rounding differences. Therefore the old root table cannot be used to sign the current 24-panel L/KZ gate.

## 5. Current corrected roots retained for Cases 19–24

|Case|D_u|q_u|Pc / kN|Ps / kN|Pu / kN|current identity|
|---:|---:|---:|---:|---:|---:|---|
|19|0.895498262463|0.001490667301|336.793838|19.608371|356.402209|current-fresh root retained|
|20|0.841997608509|0.001686144683|328.767761|19.130876|347.898637|current-fresh root retained|
|21|0.782285096311|0.001770752096|336.968777|28.611650|365.580428|FULL L/KZ PASS|
|22|0.829956917853|0.001656490263|338.847839|28.705329|367.553168|current-fresh root retained|
|23|0.925495201721|0.001295223916|339.612749|36.305167|375.917916|current-fresh root retained|
|24|0.922369098591|0.001430121260|400.126085|41.516378|441.642463|current-fresh root retained|

Cases 19, 20, 22, 23 and 24 also have fresh exact-D15 `Syy/Qq` contractions and steel-branch checks in the current Swartz result, but the current result explicitly does not claim their full same-expression L/KZ production gate.

## 6. Why this audit does not sign 24/24 PASS

Two independent blockers remain at the execution-artifact level:

1. **Missing current corrected root coordinates for Cases 1–18.** Their current Pu values are frozen, but the current repository does not retain the corresponding C1/MM + general-D15 `(D_u,q_u)` states needed for a reproducible L/KZ gate.
2. **Full current-tangent exact-moment bulk evaluation is not yet frozen for Cases other than Case21.** The independent exact coefficient-space tangent implementation is substantially more expensive than the base P/R contraction; a full 24-panel derivative/tangent run has not been completed and must not be replaced by old N48 tangent proxies.

This is a reproducibility/execution-package gap, not evidence that the governing theory has failed.

## 7. Required continuation to obtain a legitimate final bulk signature

```text
STEP A: regenerate current C1/MM + general-D15 primary branch roots for Cases 1–18 from raw inputs
STEP B: freeze current (D_u,q_u,Pc,Ps,Pu,Rnorm,Lnorm) for all 24
STEP C: verify first +->- maximum on Gamma0 for all 24
STEP D: evaluate full same-expression KZ on the same branch for all 24
STEP E: locate any pre-limit KZ=0 event
STEP F: issue 24-row PASS/CONTROL table
```

No experimental failure load is required for Steps A–E.

## 8. Current audit status

```text
CASE21_FULL_L_KZ_GATE = PASS
SWARTZ24_CURRENT_Pu = 24/24 AVAILABLE
SWARTZ24_CURRENT_ROOT_COORDINATES_RETAINED = 6/24
SWARTZ24_FULL_SAME_EXPRESSION_L_KZ_GATE = IN_PROGRESS / NOT YET SIGNABLE
OLD_DIRECT_N48_ROOTS_AS_CURRENT_ROOTS = PROHIBITED / DEMONSTRATED_INVALID
BASE_CURRENT_P_R_INDEPENDENT_REGRESSION = PASS_ON_CASE21
FALSE_24_OF_24_PASS = PROHIBITED
R10_MODIFIED = NO
N48_ORDER_CHANGED = NO
FORMAL_SPATIAL_DISCRETIZATION_ADDED = NO
```

The next calculation must continue from this execution audit rather than report a synthetic bulk PASS.