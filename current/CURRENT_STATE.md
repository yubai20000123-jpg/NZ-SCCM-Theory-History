# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-15 22:35 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

## Current operational entry

`semantic_v2/00_index/20260815_2235__NZSCCM__PROJECT__CURRENT_STATE_D050_DIRECTIONAL_MOMENT_FIRST_CERTIFICATE__SEMANTIC_INDEX.md`

## 22:35 D=.50 directional moment-first certificate

This stage executed **no Pu and no D>.50 continuation**.

Frozen identity remains:

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order kinematics
R10 / N48-C1-MM / Cayley-Hamilton / General D15 unchanged
A0=a/500
membrane m=[c,p20,p02]^T
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
no Zhou/Winter calibration
no out-of-plane multimode production expansion
```

### Directional moment-first implementation

The current evaluator retains the same Cayley-Hamilton material pair `S=A I+B Y`, but contracts A/B directly with the low-order q,c,p20,p02 virtual-strain weights using exact Chebyshev product moments. It no longer materializes full `Sxx,Syy` and full stress-direction product fields for every residual.

The formal structural integral remains General D15. No spatial quadrature was introduced.

### Parent reproduction at inherited tolerance

At `D=.50`, `q=.007244278905`, `c=-.0154563484942`, `p20=p02=0`, concrete pruning `7e-7`:

```text
P=37.3451401318 MN
Rq=+0.0013815858 MN mm
Rc=+0.0000996113 MN mm
R20=-19.4868584406 MN mm
R02=-23.4734835682 MN mm
```

Thus the old q+c state remains non-stationary in the FvK membrane directions.

### Parent-tolerance augmented certificate

At the same inherited `7e-7` concrete pruning tolerance:

```text
D=.50
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

Residual/internal-cancellation ratios:

```text
Rq  =0.00581744%
Rc  =0.02082154%
R20 =0.09636847%
R02 =0.00986352%
```

Locked status:

```text
D050_PARENT_TOLERANCE_DIRECTIONAL_EQUILIBRIUM_CERTIFICATE = PASS
engineering gate = max normalized residual < 0.1%
THEOREM_LEVEL_EXACT_ZERO_RESIDUAL = NOT CLAIMED
```

Current-runtime certificate evaluation at `7e-7` completed in about `36.7 s`; the previous augmented full-stress implementation had exceeded the 90 s execution window near this tolerance. The D=.50 representation/runtime gate is therefore cleared for the current engineering gate, although dense `buildS(K1,K2)` fill-in still remains internally.

### Why the load has not jumped dramatically

The valid comparison is at the **same D=.50**:

```text
parent D+q+c            P=37.3451401318 MN
augmented certificate   P=37.6899290259 MN
Delta P=+0.3447888941 MN = +0.92325%
```

Internally the redistribution is larger:

```text
Pc: +0.80833 MN
Ps: -0.46354 MN
```

so concrete and steel changes partially cancel in the global axial resultant. The historical old reduced-branch `Pu≈37.50943 MN` is a peak on another state/path and is not the same quantity as the present fixed-D checkpoint. Its numerical closeness to `37.69 MN` is not evidence that the FvK correction has no effect.

Corrected Pu remains **NOT SOLVED**.

## Current next execution

```text
D055_AUGMENTED_DIRECTIONAL_MOMENT_FIRST_CONNECTED_CHECKPOINT
```

Use the certified D=.50 q,c,p20,p02 state as the connected initial state. Only after a connected D-path is rebuilt may a new Pu be identified.

## 22:35 artifacts

- `semantic_v2/10_governance/20260815_2235__NZSCCM__D050_DIRECTIONAL_MOMENT_FIRST_CERTIFICATE__LOCK.md`
- `semantic_v2/20_theory/nc_steel_shell_panel/20260815_2235__NZSCCM__DIRECTIONAL_MOMENT_FIRST_AUGMENTED_FVK_RESIDUAL_CONTRACTION__THEORY.md`
- `semantic_v2/40_execution/steel_shell/20260815_2235__NZSCCM__D050_DIRECTIONAL_MOMENT_FIRST__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/steel_shell/20260815_2235__NZSCCM__D050_DIRECTIONAL_MOMENT_FIRST__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/40_execution/steel_shell/20260815_2235__NZSCCM__D050_DIRECTIONAL_MOMENT_FIRST__TOLERANCE_CONVERGENCE.csv`
- `semantic_v2/40_execution/steel_shell/20260815_2235__NZSCCM__D050_DIRECTIONAL_MOMENT_FIRST__REPRO.py`
- `semantic_v2/50_results/steel_shell/20260815_2235__NZSCCM__D050_DIRECTIONAL_MOMENT_FIRST__RESULT.csv`

## Parent stages retained

- 22:20 updated FvK theory and expansion audit
- 21:53 fixed-D augmented near-equilibrium/runtime gate
- 21:44 R20/R02 projection gate
- 21:34 minimum FvK membrane completion
- 21:18 Nguyen/FvK membrane compatibility audit
