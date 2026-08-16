# NZ-SCCM semantic tree v2

This namespace is the **content-first, non-destructive semantic reconstruction** of the repository.

## Current operational entry

Use first:

`20260816_2136__NZSCCM__PROJECT__CURRENT_STATE_ANTI_LOOP_N48_MEMBRANE_PRODUCTION_REACTIVATED__SEMANTIC_INDEX.md`

## Frozen production backbone

```text
UNIFIED_PRODUCTION_WORKFLOW_V1
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order continuous kinematics
MEMBRANE_STRESS_REDISTRIBUTION = REQUIRED
R10 source current material operator = FROZEN
reinforcement/steel phase before root solve
same-state current stress + consistent tangent
General-D15 exact/controlled target framework
P,Rq,L connected-branch topology
same-state material + geometric KZ
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```

## Structural coordinates

Global production remains `(D,q)` with internal membrane coordinates

```text
r=[r0,r20,r22,s02,s22]
```

solved from `Rm=0` and consistently Schur-condensed.

## Exact-algebraic branch status

The exact R10 matrix/quartic/64-state/CH/adjoint results remain retained research evidence. A 21:36 regularity audit found that the current rationalized quadratic-tower basis has an apparent interior pole at `x=21/260` even though the physical smooth atom is regular there.

The exact denominator-gauge identity

```text
d V'=B V, W=V/G
=> (dG)W'=(BG-dG'I)W
```

passes for globally regular denominator signatures, but the current rationalized field requires an additional algebraic regularization layer before this can become a robust global production backend.

Under the anti-loop rule, that new backend is not opened automatically.

```text
EXACT_ALGEBRAIC_HOLONOMIC_Pu_ROUTE = PAUSED_RESEARCH_BRANCH
```

## 64-state erratum

For basis `[1,q,s,q*s]`, the accepted local derivative matrix is

```text
[0, 0,   0,        0]
[0, ell, 0,        0]
[0, 0,   c0,       c1]
[0, 0,   c1*Q,     ell+c0]
```

The 20:59 displayed matrix interchanged `c1` and `c1*Q`. State dimension `64` and sparsity `159/4096` are unchanged.

## Reactivated production route

The active Pu route is again the accepted zero-spatial production contract

`../current/theory/NZ_SCCM_NC_REBAR_ZERO_SPATIAL_PRODUCTION_THEORY_CONTRACT_20260812_2245.md`

with

```text
N48_ORDER=48
U=N48-C1
C=N48-C1
T7=N48-C1
T=N48-C1-CONSTRAINED-MINIMAX
CAYLEY_HAMILTON=GOVERNING
D15_GENERAL_TRIG_MOMENTS=ACTIVE
```

plus the five-term membrane redistribution before the outer `(D,q)` solve.

N48 roots remain material-coordinate compiler roots, not structural spatial points.

## Capacity boundary

```text
Case21 368.189 kN = historical/current-support closure only
Z6 51.30 MN = retained engineering baseline only
NEW membrane-redistributed Case21 Pu = not yet run
```

## Current next gate

```text
UNIFIED_V1_CASE21_MEMBRANE_REDISTRIBUTED_N48_PRODUCTION_GATE
```

This is an actual structural calculation gate, not another integration-backend gate.

## Repository semantic read order

1. `20260816_2136__NZSCCM__PROJECT__CURRENT_STATE_ANTI_LOOP_N48_MEMBRANE_PRODUCTION_REACTIVATED__SEMANTIC_INDEX.md`
2. `../10_governance/20260816_2136__NZSCCM__ANTI_LOOP_EXACT_BRANCH_PAUSE_AND_N48_MEMBRANE_PRODUCTION__LOCK.md`
3. `../20_theory/nc_rebar_panel/20260816_2136__NZSCCM__DUAL_HOLONOMIC_REGULARITY_ERRATUM_AND_PRODUCTION_PIVOT__THEORY.md`
4. `../40_execution/common/20260816_2136__NZSCCM__DUAL_HOLONOMIC_REGULARITY_AND_PRODUCTION_PIVOT__EXECUTION_REPORT.md`
5. `../40_execution/common/20260816_2136__NZSCCM__DUAL_HOLONOMIC_REGULARITY_AND_PRODUCTION_PIVOT__PARAMS_AND_INTERMEDIATES.json`
6. `../40_execution/common/20260816_2136__NZSCCM__DUAL_HOLONOMIC_REGULARITY_AND_PRODUCTION_PIVOT__REPRO.py`
7. `../60_validation/common/20260816_2136__NZSCCM__DUAL_HOLONOMIC_REGULARITY_AND_PRODUCTION_PIVOT__AUDIT.md`
8. `20260816_2118__NZSCCM__PROJECT__CURRENT_STATE_ADJOINT_CH_TARGET_PASS_DUAL_HOLONOMIC_THICKNESS_OPEN__SEMANTIC_INDEX.md` — predecessor
9. `20260816_2059__NZSCCM__PROJECT__CURRENT_STATE_FULL_R10_64_STATE_ADJOINT_TARGET_OPEN__SEMANTIC_INDEX.md` — predecessor

No legacy file is deleted, moved or renamed solely from filename identity.
