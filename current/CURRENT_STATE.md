# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-17 13:04 +08:00  
**Status:** CURRENT FORMAL CASE21 AIRY RELEASE ON RESTORED COMPILER+CH+D15 PATH

## Current end-to-end task

```text
CASE21_AIRY_SCALAR_FORMAL_ZERO_SPATIAL_ULTIMATE_LOAD
```

This task has now produced a formal zero-spatial Case21 ultimate-load result on the restored previously-proven implementation chain.

## Controlling governance

`semantic_v2/10_governance/20260817_1304__NZSCCM__CASE21_RESTORE_N48_CH_D15_AIRY_PRODUCTION_PATH__LOCK.md`

## Production chain

```text
frozen R10 source
 -> frozen Case21 N48-C1/MM U,C,T,T7 compiler on [-1.15,+0.12]
 -> 2x2 Cayley-Hamilton
 -> Nguyen second-order + Airy scalar r=lambda*M*a(nu)
 -> General-D15 exact structural moments
 -> exact elastic reinforcement
 -> Rq=0, RA=0 connected branch
 -> first load maximum
```

The recent raw-R10 `64/16-state -> semialgebraic period` branch is retained as research/diagnostic provenance but is no longer a prerequisite for production. The user correctly identified that it had silently strengthened the integration requirement beyond the earlier successful compiler+D15 contract.

## Formal counters

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

Material-coordinate Chebyshev compiler nodes are not structural spatial points.

## Frozen Case21 identities

```text
Pcr_exp = 336.285554 kN   # buckling only
Pf_exp  = 368.312750 kN   # failure / ultimate
```

## Current mechanics

```text
r = lambda*M*a(nu)
M = pi^2/eps0*(q0*q+0.5*q^2)
a(0.18) = [-0.295,-0.205,+0.25,-0.205,+0.25]
RA = a^T Rm = 0
Rq_base = 0
```

Airy only augments the finite trigonometric kinematic field. It does not create a new structural integration class for the accepted finite material compiler + CH + D15 architecture.

## Old-path regression

The reconstructed N48/CH/D15 evaluator at the old `lambda=0` Case21 candidate reproduces the 2026-08-12 frozen exact-moment result:

```text
D15[Syy] recreated = -13.30614551
old frozen         = -13.306145538701315

D15[Qq] recreated  = +4.47970960
old frozen         = +4.479715227945151

Pc recreated       = 336.96877664 kN
old frozen         = 336.96877733 kN
```

## Current Airy formal branch

Refined connected-branch samples:

```text
D=.775  P=365.239690 kN
D=.776  P=365.252822 kN
D=.777  P=365.255952 kN
D=.778  P=365.253582 kN
D=.779  P=365.244928 kN
D=.780  P=365.227725 kN
```

Local branch interpolation gives

```text
D_u ~= 0.7770781
Pu ~= 365.25665 kN
```

A direct formal evaluation at a refined peak coordinate gives

```text
D = 0.7771614625
q = 0.00180590635
lambda = 0.0434741730
M = 0.02902048450

Pc = 336.84063912 kN
Ps =  28.41597657 kN
P  = 365.25661569 kN
Rq = -0.00113057 kN mm
RA = +0.00000752 kN mm
```

Engineering formal release:

\[
\boxed{P_u^{N48-CH-D15}=365.257\ \mathrm{kN}}
\]

## Comparison after formal solve

```text
direct raw-R10 mechanics oracle = 366.767829 kN
formal N48-D15 difference        = -1.51118 kN = -0.4120 %
Pf_exp                           = 368.312750 kN
formal error vs Pf               = -0.82976 %
```

The remaining difference to the raw-R10 oracle is classified as material-compiler representation difference, not failure of Airy structural integration.

## Current artifacts

- `current/case21/CASE21_AIRY_N48_CH_D15_FORMAL_ZERO_SPATIAL_20260817_1304.md`
- `semantic_v2/10_governance/20260817_1304__NZSCCM__CASE21_RESTORE_N48_CH_D15_AIRY_PRODUCTION_PATH__LOCK.md`
- `semantic_v2/40_execution/case21/20260817_1304__NZSCCM__CASE21_AIRY_N48_CH_D15_FORMAL_ZERO_SPATIAL__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/case21/20260817_1304__NZSCCM__CASE21_AIRY_N48_CH_D15_FORMAL_ZERO_SPATIAL__PARAMS_AND_INTERMEDIATES.json`

## Current status

```text
CASE21_AIRY_N48_CH_D15_FORMAL_ZERO_SPATIAL = PASS
FORMAL_CASE21_Pu = 365.257 kN
RAW_R10_DIRECT_PERIOD_RUNTIME = NOT_REQUIRED_FOR_CURRENT_FORMAL_BASELINE
NEW_PROJECT_TASK_CREATED = NO
ROUTE_CHANGED_PHYSICALLY = NO
```
