# NZ-SCCM CURRENT STATE — SPARSE MASTER GKZ A* R12

**Date:** 2026-08-19  
**Status:** `CASE21_SPARSE_CH_CIRCUIT_MASTER_GKZ_ASTAR_R12 = ACTIVE`

## Mandatory governance

`semantic_v2/10_governance/20260819_0142__NZSCCM__PROJECT__ZERO_DISCRETIZATION_AND_GITHUB_CONTINUITY__LOCKED_GOVERNANCE.md`

## Governing material-series correction

`semantic_v2/20_theory/20260819__NZSCCM__MATERIAL_SERIES_LAYER_REMOVAL_AND_MAINLINE_REBASE__R09.md`

## Exact-integration progression

R10 local thickness representation:

`semantic_v2/20_theory/20260819__NZSCCM__CASE21_CONCRETE__THICKNESS_ALGEBRAIC_FIELD_TO_FINITE_LAURICELLA_CLOSURE__R10.md`

R11 global residue / GKZ constructor switch:

`semantic_v2/20_theory/20260819__NZSCCM__CASE21_CONCRETE__GLOBAL_RESIDUE_GKZ_AND_RELATIVE_INCOMPLETE_A_HYPERGEOMETRIC_CLOSURE__R11.md`

R12 sparse CH-pair master A* construction:

`semantic_v2/20_theory/20260819__NZSCCM__CASE21__SPARSE_CH_CIRCUIT_MASTER_GKZ_ASTAR__R12.md`

## R12 exact result

For the R07 globally first-tension-branch pilot, the complete finite-R10 stress computation was retained as a sparse 2x2 Cayley-Hamilton polynomial circuit rather than globally expanded.

```text
circuit relations = 78
monomial-space variables = 81
Cayley A* rows = 159
Cayley A* columns = 271
maximum monomials per one relation = 13
```

This is an exact symbolic support count; no spatial or material discretization was used.

The circuit covers finite kinematics -> algebraic projectors -> compression -> first-branch u_R -> T/U/T^7 -> full R10 S -> Syy.

`P_c`, `Rq`, and `Ralpha` share the same denominator/support family. Same-source derivatives raise denominator powers but do not require a new support family, so the target system can use one master A* under finite differential/contiguity shifts.

## Important scope

The printed 159x271 A* is the certified first-tension-branch pilot A*, not yet the full three-branch Case21 Pu A*. If the real limit search crosses xcr or 10*xcr, add exact threshold divisors / relative-incomplete-GKZ boundary data. Do not create numerical spatial regions or return to finite material prefixes.

## Current status

```text
MATERIAL_TRUE_INFINITE_SERIES_LAYER = REMOVED
R11_GLOBAL_MULTIRESIDUE_RATIONALIZATION = PASS
R11_GKZ_CLASSIFICATION = PASS
R12_SPARSE_CH_CIRCUIT = CONSTRUCTED
R12_PILOT_ASTAR_159x271 = PASS
P_RQ_RALPHA_SHARED_SUPPORT = PASS FOR PILOT
J_SHARED_SUPPORT = PASS AT DIFFERENTIAL-CLOSURE LEVEL
FULL_THREE_BRANCH_CASE21_ASTAR = OPEN
ZERO_DISCRETIZATION = PASS
```

## Current unique next task

Extend the sparse circuit with finite R10 threshold variables/divisors and construct the full three-branch Case21 relative/incomplete-GKZ master A*. If one exact evaluation representation becomes inconvenient, switch among Carlson/Lauricella, GKZ residue/Euler, Mellin-Barnes, incomplete-GKZ, or differential-system representations without altering the finite current material operator or introducing discretization.