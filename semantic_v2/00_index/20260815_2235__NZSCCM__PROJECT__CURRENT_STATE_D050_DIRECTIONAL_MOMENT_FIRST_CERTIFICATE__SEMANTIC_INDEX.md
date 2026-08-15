# NZ-SCCM — Current state semantic index: D=.50 directional moment-first certificate

**Timestamp:** 2026-08-15 22:35 +08:00

## Current stage

```text
D050_PARENT_TOLERANCE_DIRECTIONAL_EQUILIBRIUM_CERTIFICATE = PASS
Pu = NOT SOLVED
D > .50 continuation = NOT EXECUTED THIS STAGE
```

Frozen theory remains:

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order kinematics
R10 / N48-C1-MM / Cayley-Hamilton / General D15 unchanged
A0=a/500
m=[c,p20,p02]^T
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
no Zhou/Winter calibration
no out-of-plane multimode production expansion
```

## Certificate state

At `D=.50`, inherited concrete pruning tolerance `7e-7`:

```text
q=0.008003063422252722
c=-0.07766034129851779
p20=-0.06065823792663306
p02=0.16525678113314005
P=37.6899290259 MN
Pc=21.8783795851 MN
Ps=15.8115494408 MN
Rq=-0.3465589605 MN mm
Rc=-0.0055395219 MN mm
R20=+0.0076892296 MN mm
R02=+0.0024794016 MN mm
```

Residual/internal cancellation percentages:

```text
Rq  0.00581744%
Rc  0.02082154%
R20 0.09636847%
R02 0.00986352%
```

All are below the locked engineering same-expression gate `0.1%`. This is not a theorem-level exact-zero certificate.

## Directional moment-first V1

The evaluator keeps the frozen dense Cayley-Hamilton material pair `S=A I+B Y` but does not first materialize full `Sxx,Syy` fields and then full `stress * virtual-strain` fields for each residual. It contracts A/B directly with q,c,p20,p02 virtual-strain weights using the exact Chebyshev product identity and the same General-D15 analytic moments.

At the certificate state and `7e-7`, current-runtime evaluation completed in about `36.7 s`; the prior augmented full-stress implementation had exceeded the 90 s execution window near parent tolerance.

Thus:

```text
D050_REPRESENTATION_RUNTIME_GATE = CLEARED_FOR_CURRENT_ENGINEERING_GATE
remaining dense buildS fill-in = YES
formal D15 change = NO
```

## Why P appears close to historical values

At the valid same-D comparison:

```text
D=.50 parent D+q+c:       P=37.3451401318 MN
D=.50 augmented certificate: P=37.6899290259 MN
Delta = +0.3447888941 MN = +0.92325%
```

Internally:

```text
Pc increases by about +0.80833 MN
Ps decreases by about -0.46354 MN
```

so substantial load redistribution partially cancels in the total axial resultant. The historical old reduced-branch `Pu≈37.50943 MN` is a peak at another state/branch and is not the same quantity as the present fixed-D checkpoint.

## Artifacts

- `../10_governance/20260815_2235__NZSCCM__D050_DIRECTIONAL_MOMENT_FIRST_CERTIFICATE__LOCK.md`
- `../20_theory/nc_steel_shell_panel/20260815_2235__NZSCCM__DIRECTIONAL_MOMENT_FIRST_AUGMENTED_FVK_RESIDUAL_CONTRACTION__THEORY.md`
- `../40_execution/steel_shell/20260815_2235__NZSCCM__D050_DIRECTIONAL_MOMENT_FIRST__EXECUTION_REPORT.md`
- `../40_execution/steel_shell/20260815_2235__NZSCCM__D050_DIRECTIONAL_MOMENT_FIRST__PARAMS_AND_INTERMEDIATES.json`
- `../40_execution/steel_shell/20260815_2235__NZSCCM__D050_DIRECTIONAL_MOMENT_FIRST__TOLERANCE_CONVERGENCE.csv`
- `../40_execution/steel_shell/20260815_2235__NZSCCM__D050_DIRECTIONAL_MOMENT_FIRST__REPRO.py`
- `../50_results/steel_shell/20260815_2235__NZSCCM__D050_DIRECTIONAL_MOMENT_FIRST__RESULT.csv`

## Parent stages

- 22:20 updated augmented FvK theory / expansion audit
- 21:53 augmented D=.50 near-equilibrium/runtime gate
- 21:44 R20/R02 projection gate
- 21:34 minimum FvK membrane completion
- 21:18 Nguyen/FvK compatibility audit

## Current next execution

```text
D055_AUGMENTED_DIRECTIONAL_MOMENT_FIRST_CONNECTED_CHECKPOINT
```

Use the D=.50 certificate state as the connected initial state. Do not infer Pu before a connected D-path is rebuilt.