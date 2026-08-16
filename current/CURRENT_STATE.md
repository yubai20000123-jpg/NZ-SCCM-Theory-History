# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-16 22:34 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

## Current operational entry

`semantic_v2/00_index/20260816_2234__NZSCCM__PROJECT__CURRENT_STATE_CASE21_N48_MEMBRANE_CONTINUATION_STARTED__SEMANTIC_INDEX.md`

## Frozen project-wide backbone

```text
UNIFIED_PRODUCTION_WORKFLOW_V1 = ACTIVE
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
Nguyen second-order continuous kinematics = ACTIVE
MEMBRANE_STRESS_REDISTRIBUTION = REQUIRED
R10 source current material operator = FROZEN
reinforcement before root solve = REQUIRED
same-state current stress + consistent tangent = REQUIRED
N48-C1/MM + Cayley-Hamilton = ACTIVE PRODUCTION COMPILER
General-D15 exact structural moments = ACTIVE
P,Rq,L connected-branch topology = ACTIVE
same-state material + geometric KZ audit = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
Gauss/Simpson/adaptive/collocation/material-point-grid = PROHIBITED
experiment/Zhou/Winter response calibration = PROHIBITED
```

## Structural coordinates

```text
global = (D,q), A=bq
internal membrane = [r0,r20,r22,s02,s22]
```

## Production progress

The 18:02 Case21 `r=0` N48 fresh closure has now been independently reconstructed in coefficient space:

```text
P_freeze = 365.58042756532977 kN
P_repro  = 365.58042692483133 kN
DeltaP   = -6.4049844e-7 kN
Rqc component relative difference ~= 7.8e-7
```

Therefore the current N48/CH/General-D15 evaluator is accepted as the same numerical implementation family.

Direct insertion of the five membrane coordinates at the old `r=0` limit point was rejected as a start strategy because the elastic predictor gives `||Rm||2=15.5546` and a diagnostic Jacobian has `cond2~=714.75` with an O(1) Newton jump.

Instead, origin-connected continuation has started. The first accepted nonzero state is

```text
q = 1e-4
D = 0.016046306
r = [-0.0004765646208971642,
     -0.0002322819318541890,
     +0.0002805628349612065,
     -0.0002432861950486819,
     +0.0003034158793738149]
||Rm||2 = 6.9022384258e-6
Rq = +1.9082556149e-6 kN mm
P = 15.2626325741107 kN
```

Continuous analytic interval/Gershgorin certificate:

```text
lambda in [-0.02454674538198,+0.00935909011672]
compiler interval = [-1.15,+0.12]
certificate = PASS
```

## Research branch status

```text
EXACT_ALGEBRAIC_HOLONOMIC_Pu_ROUTE = PAUSED_RESEARCH_BRANCH
NO_FURTHER_EXACT_INTEGRATION_MICRO_GATE = YES
```

The exact-algebraic work remains retained evidence but is not the active Pu backend.

## Capacity status

```text
Case21 368.189 kN = historical/current-support closure only
Z6 51.30 MN = retained engineering baseline only
NEW membrane-redistributed Case21 Pu = NOT RELEASED
```

## Current unique next gate

```text
CASE21_N48_MEMBRANE_CONNECTED_BRANCH_CONTINUATION_AND_SCHUR_GATE
```

Advance monotonically from the accepted `q=1e-4` connected state; at every accepted point close all five `Rm` and total `Rq`, retain the N=28 corrector, store `r/Krr/condition/P/domain-certificate`, then build consistent Schur derivatives near the first connected load maximum and run same-state `KZ` before releasing a new Pu.

## Current key artifacts

- `semantic_v2/00_index/20260816_2234__NZSCCM__PROJECT__CURRENT_STATE_CASE21_N48_MEMBRANE_CONTINUATION_STARTED__SEMANTIC_INDEX.md`
- `semantic_v2/40_execution/common/20260816_2234__NZSCCM__CASE21_N48_MEMBRANE_CONTINUATION_START__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/common/20260816_2234__NZSCCM__CASE21_N48_MEMBRANE_CONTINUATION_START__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/40_execution/common/20260816_2234__NZSCCM__CASE21_N48_MEMBRANE_CONTINUATION_START__REPRO.py`
- `semantic_v2/60_validation/common/20260816_2234__NZSCCM__CASE21_N48_MEMBRANE_CONTINUATION_START__AUDIT.md`
- `semantic_v2/10_governance/20260816_2234__NZSCCM__CASE21_N48_MEMBRANE_CONNECTED_CONTINUATION__GATE_LOCK.md`
