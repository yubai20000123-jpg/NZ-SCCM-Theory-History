# NZ-SCCM current state — D=.50 augmented FvK membrane equilibrium

**Timestamp:** 2026-08-15 21:53 +08:00

## What was executed

The active 21:44 gate was executed. At fixed `D=.50`, the minimum single-halfwave FvK membrane system

```text
Rq=0
Rc=0
R20=0
R02=0
```

was solved toward a coupled state in `[q,c,p20,p02]` with the frozen R10/N48/Cayley-Hamilton + local steel + General D15 operator.

No Pu and no D continuation were executed.

## Main result

The former parent state had

```text
q=.007244278905
c=-.0154563484942
p20=p02=0
R20=-19.48685822
R02=-23.47348406 MN mm
```

so it was not stationary in the newly admitted FvK membrane directions.

The best released fixed-D near-equilibrium found is

```text
D=.50
q=.008002
c=-.077622
p20=-.060657
p02=.165133
P=37.69591555 MN
```

with coefficient-pruning tolerance `2e-4`:

```text
Rq = -3.06330915 MN mm
Rc = +0.01005384 MN mm
R20= -0.05300744 MN mm
R02= -0.02373140 MN mm
```

and residual/internal-cancellation ratios:

```text
Rq  0.0514%
Rc  0.0379%
R20 0.6620%
R02 0.0945%
```

This demonstrates that releasing `p20,p02` actually removes the large postbuckling membrane residuals and strongly readjusts q,c. Therefore the minimum FvK membrane completion is mechanically active, not a formal redundancy.

## Identity of this result

```text
FIXED_D050_AUGMENTED_NEAR_EQUILIBRIUM = FOUND
STRICT_FIXED_D050_CERTIFICATE = NOT REACHED
```

The strict certificate is blocked by representation/runtime growth of the dense coefficient-space N48 composition after introducing p20/p02. Tightening the coefficient pruning toward the parent implementation level causes individual current-map evaluations near the augmented root to exceed the available execution window.

This is a representation/runtime gate, not evidence that the added membrane system is physically illegal. A non-integral domain audit gives normalized principal material coordinates approximately inside `[-0.8212,+0.1852]`, safely within the inherited N48 interval `[-1.75,+0.45]`; the steel trial radial ratio remains below one (`rmax≈0.786`).

## Same-D load change

The parent c-only state had `P≈37.34514 MN`; the augmented near-equilibrium has `P≈37.69592 MN`, an increase of about `0.939%` at the same D. This is only a state comparison and is **not** a Pu prediction.

## Formal integral identity remains unchanged

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order kinematics
General D15 exact moments
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
```

No Gauss/Simpson/cells/material-point grid was introduced into the formal structural operator.

## Current next execution

```text
DIRECTIONAL_MOMENT_FIRST_AUGMENTED_MEMBRANE_EVALUATOR_AT_D050
```

The next implementation must keep the same physical equations and integration identity, but evaluate `P,Rq,Rc,R20,R02` and the flat Jacobian by directional/moment-first contraction rather than naive full dense stress-tensor expansion. It must first reproduce/certify the fixed-D=.50 root before any D continuation or Pu search resumes.

## Artifacts

- `../10_governance/20260815_2153__NZSCCM__D050_AUGMENTED_FVK_MEMBRANE_EQUILIBRIUM_RUNTIME_GATE__LOCK.md`
- `../40_execution/steel_shell/20260815_2153__NZSCCM__D050_AUGMENTED_FVK_MEMBRANE_EQUILIBRIUM__PARAMS_AND_INTERMEDIATES.json`
- `../40_execution/steel_shell/20260815_2153__NZSCCM__D050_AUGMENTED_FVK_MEMBRANE_EQUILIBRIUM__JACOBIAN.csv`
- `../40_execution/steel_shell/20260815_2153__NZSCCM__D050_AUGMENTED_FVK_MEMBRANE_EQUILIBRIUM__REPRO.py`
- `../40_execution/steel_shell/20260815_2153__NZSCCM__D050_AUGMENTED_FVK_MEMBRANE_EQUILIBRIUM__EXECUTION_REPORT.md`
- `../50_results/steel_shell/20260815_2153__NZSCCM__D050_AUGMENTED_FVK_MEMBRANE_EQUILIBRIUM__RESULT.csv`

## Parent stages retained

- 21:44 R20/R02 projection gate
- 21:34 minimal FvK membrane completion
- 21:18 Nguyen/FvK postbuckling membrane compatibility audit
