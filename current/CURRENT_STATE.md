# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-16 22:40 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

## Current operational entry

`semantic_v2/00_index/20260816_2240__NZSCCM__PROJECT__CURRENT_STATE_CASE21_MEMBRANE_BRANCH_TWO_POINTS_ACCEPTED__SEMANTIC_INDEX.md`

## Frozen backbone

```text
UNIFIED_PRODUCTION_WORKFLOW_V1=ACTIVE
ONE_CONTINUOUS_COMPLETE_HALFWAVE=ACTIVE
Nguyen second-order continuous kinematics=ACTIVE
R10=FROZEN
five-term membrane redistribution=REQUIRED
N48-C1/MM + Cayley-Hamilton=ACTIVE PRODUCTION COMPILER
General-D15 exact structural moments=ACTIVE
reinforcement before root solve=REQUIRED
connected P,Rq,L branch=ACTIVE
same-state Schur + KZ before Pu=REQUIRED
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```

The exact-algebraic/holonomic Pu route remains a paused research branch under the anti-loop rule.

## N48 evaluator fingerprint

The 2026-08-12 18:02 `r=0` Case21 closure has been reconstructed:

```text
P_freeze=365.58042756532977 kN
P_repro =365.58042692483133 kN
DeltaP  =-6.4049844e-7 kN
Rqc component relative difference ~=7.8e-7
```

`N48_1802_FINGERPRINT=PASS`.

## Origin-connected five-membrane branch

Direct insertion of new membrane coordinates at the old `r=0` limit is rejected as a start strategy. Continuation starts from the origin.

Accepted points:

```text
point1:
 q=1e-4
 D=0.016046306
 P=15.2626325741107 kN
 ||Rm||2=6.9022384258e-6
 Rq=+1.9082556149e-6 kN mm
 r=[-0.0004765646208971642,-0.0002322819318541890,+0.0002805628349612065,-0.0002432861950486819,+0.0003034158793738149]

point2:
 q=2e-4
 D=0.031737797
 P=31.4300211269425 kN
 ||Rm||2=1.3545457160e-5
 Rq=+3.9798686409e-6 kN mm
 r=[-0.0009851269073948984,-0.0004459452528374698,+0.0006055135286393538,-0.0003630828054164307,+0.0005376886688340636]
```

Point2 continuous compiler-domain enclosure:

`lambda in [-0.0486323165234,+0.0188154748336]`, inside `[-1.15,+0.12]`.

The load is increasing from point1 to point2; no limit conclusion is made from only two states.

## Capacity boundary

```text
Case21 368.189 kN=historical/current-support closure only
Z6 51.30 MN=retained engineering baseline only
NEW membrane-redistributed Case21 Pu=NOT RELEASED
```

## Current unique next gate

`CASE21_N48_MEMBRANE_CONNECTED_BRANCH_CONTINUATION_AND_SCHUR_GATE`

Use point1-point2 secant predictor to compute point3 and continue monotonically in q. Every accepted state must close five `Rm` and total `Rq`, pass the continuous compiler-domain certificate, and be rechecked by N=28 corrector. Near the first connected load maximum, construct consistent Schur derivatives and run same-state KZ before releasing Pu.

## Current artifacts

- `semantic_v2/00_index/20260816_2240__NZSCCM__PROJECT__CURRENT_STATE_CASE21_MEMBRANE_BRANCH_TWO_POINTS_ACCEPTED__SEMANTIC_INDEX.md`
- `semantic_v2/40_execution/common/20260816_2240__NZSCCM__CASE21_N48_MEMBRANE_CONNECTED_BRANCH__LEDGER.jsonl`
- `semantic_v2/40_execution/common/20260816_2240__NZSCCM__CASE21_N48_MEMBRANE_CONNECTED_BRANCH_POINT2__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/common/20260816_2234__NZSCCM__CASE21_N48_MEMBRANE_CONTINUATION_START__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/common/20260816_2234__NZSCCM__CASE21_N48_MEMBRANE_CONTINUATION_START__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/40_execution/common/20260816_2234__NZSCCM__CASE21_N48_MEMBRANE_CONTINUATION_START__REPRO.py`
- `semantic_v2/60_validation/common/20260816_2234__NZSCCM__CASE21_N48_MEMBRANE_CONTINUATION_START__AUDIT.md`
- `semantic_v2/10_governance/20260816_2234__NZSCCM__CASE21_N48_MEMBRANE_CONNECTED_CONTINUATION__GATE_LOCK.md`
