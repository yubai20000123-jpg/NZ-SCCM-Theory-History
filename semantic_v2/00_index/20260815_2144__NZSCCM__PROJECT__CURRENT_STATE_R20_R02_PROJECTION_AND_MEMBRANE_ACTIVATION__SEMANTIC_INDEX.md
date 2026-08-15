# NZ-SCCM current semantic state — 2026-08-15 21:44 +08

## Stage identity

```text
EXISTING-STATE R20/R02 D15 PROJECTION GATE COMPLETE
NO NEW Pu
NO NEW ROOT
MINIMAL FvK MEMBRANE SYSTEM ACTIVATED
```

## Formal gate result

At the certified Z6 `D=.50` boundary-warp state:

```text
P   = 37.34514010 MN
Rq  = +0.00137125 MN mm
Rc  = +0.00009898 MN mm
R20 = -19.48685822 MN mm
R02 = -23.47348406 MN mm
```

Thus the state that is stationary in the retained `q,c` directions is decisively nonstationary in both newly admissible FvK membrane directions.

Material decomposition:

```text
R20c=-18.98676026, R20s=-0.50009796 MN mm
R02c=-33.62196168, R02s=+10.14847762 MN mm
```

Coefficient-pruning and steel-cap degree sweeps confirm the signs and magnitudes are robust.

## Locked decisions

```text
CURRENT_DQC_POSTBUCKLING_MEMBRANE_COMPLETENESS = FAIL_CONFIRMED
p20_DIRECTION_ACTIVE = YES
p02_DIRECTION_ACTIVE = YES
MINIMAL_MEMBRANE_UNKNOWN_VECTOR = [c,p20,p02]^T
MEMBRANE_RESIDUAL_VECTOR = [Rc,R20,R02]^T
MEMBRANE_JACOBIAN = FLAT_3x3
ONE_CONTINUOUS_COMPLETE_HALFWAVE = RETAIN
NGUYEN_SECOND_ORDER = RETAIN
R10_N48_CAYLEY_HAMILTON = RETAIN
GENERAL_D15 = RETAIN
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
NEW_Pu = NONE
```

## Existing connected-state projection trend

```text
D=.50: R20=-19.48686, R02=-23.47348 MN mm  # certified gate state
D=.55: R20=-22.12116, R02=-28.14891 MN mm  # diagnostic
D=.60: R20=-24.68521, R02=-33.43076 MN mm  # diagnostic
```

The D=.55/.60 states remain near-equilibrium parent checkpoints; only D=.50 is used for the formal activation decision.

## Current next execution

```text
FIXED_D050_COUPLED_q_c_p20_p02_EQUILIBRIUM
```

At `D=.50`, solve

```text
Rq=0
Rc=0
R20=0
R02=0
```

using a flat `3x3` membrane Jacobian for `[c,p20,p02]` and directional/static condensation into the scalar `q` equation. No D continuation and no Pu should be released until this fixed-D checkpoint is reproduced.

## Primary artifacts

- `semantic_v2/10_governance/20260815_2144__NZSCCM__R20_R02_PROJECTION_GATE_AND_MEMBRANE_SYSTEM_ACTIVATION__LOCK.md`
- `semantic_v2/40_execution/steel_shell/20260815_2144__NZSCCM__EXISTING_STATE_R20_R02_D15_PROJECTION__REPRO.py`
- `semantic_v2/40_execution/steel_shell/20260815_2144__NZSCCM__R20_R02_D050_PROJECTION_CONVERGENCE.csv`
- `semantic_v2/40_execution/steel_shell/20260815_2144__NZSCCM__EXISTING_STATE_R20_R02_D15_PROJECTION__EXECUTION_REPORT.md`
- `semantic_v2/50_results/steel_shell/20260815_2144__NZSCCM__EXISTING_STATE_R20_R02_D15_PROJECTION__RESULT.csv`

## Parent state

The 21:34 minimum-system construction remains the immediate parent:

`20260815_2134__NZSCCM__PROJECT__CURRENT_STATE_MINIMAL_FVK_MEMBRANE_COMPLETION__SEMANTIC_INDEX.md`.