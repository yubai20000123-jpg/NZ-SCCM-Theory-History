# NZ-SCCM semantic current state — Z6 AR2 updated-FvK direct-R10 recalculation

**Timestamp:** 2026-08-15 23:43 +08:00

## Current result identity

```text
Z6_AR2_UPDATED_FVK_R10_DIRECT_CONTINUUM_AUDIT_RECALC
```

The latest user-directed calculation is the Z6 comparison panel with `a/b=2>1`, using the updated membrane-redistribution mechanics.

## Geometry and mode

```text
a=24000 mm
b=12000 mm
a/b=2
m=2
ell=a/m=12000 mm
one continuous complete representative halfwave
q0=a/(500b)=0.004
A0=48 mm
```

## Mechanics

```text
out-of-plane: single (1,1) halfwave q
membrane coordinates: [c,p20,p02]
equilibrium: Rq=Rc=R20=R02=0
Nguyen second order: retained
R10 physical concrete current operator: retained
local steel radial cap: retained
```

## Audit path result

A complete connected direct-R10 continuum audit path was solved from low D through the descending post-peak branch.

High-order peak:

```text
D≈.8308
q≈.01712
c≈-.538
p20≈-.700
p02≈+.697
Pu≈40.97 MN
```

At `160x160x60` audit at D=.8308:

```text
P=40.9733400613 MN
lambda≈[-1.13695,+.47949]
steel trial rmax≈1.30146
```

## Comparison

```text
old AR2 direct-R10 audit without complete membrane redistribution = 44.5529191054 MN
updated complete membrane-equilibrium audit                       ≈ 40.9733400613 MN
change                                                           ≈ -8.03%
Zhou comparator                                                   = 49.4867667519 MN
Winter comparator                                                 = 50.1858541295 MN
```

Therefore membrane redistribution is strongly active but capacity-reducing for the current reduced two-face steel object.

## Identity restrictions

This calculation used Gauss-Legendre only as an audit continuum executor in order to evaluate the updated mechanics directly while the formal augmented N48/D15 path still has representation/compiler gates.

```text
FORMAL_N48_D15_ZERO_QUADRATURE_PRODUCTION_Pu = NOT RELEASED
PROJECT_FORMAL_ZERO_QUADRATURE_GOVERNANCE = UNCHANGED
PBL_WEB_LONGITUDINAL_STEEL_PHASE_IN_AUGMENTED_EQUILIBRIUM = NOT INCLUDED
FULL_ZHOU_SECTION_IDENTITY = NO
```

## Read order

1. `../10_governance/20260815_2343__NZSCCM__Z6_AR2_UPDATED_FVK_DIRECT_R10_RECALC__LOCK.md`
2. `../40_execution/steel_shell/20260815_2343__NZSCCM__Z6_AR2_UPDATED_FVK_DIRECT_R10_RECALC__EXECUTION_REPORT.md`
3. `../40_execution/steel_shell/20260815_2343__NZSCCM__Z6_AR2_UPDATED_FVK_DIRECT_R10_RECALC__PARAMS_AND_INTERMEDIATES.json`
4. `../50_results/steel_shell/20260815_2343__NZSCCM__Z6_AR2_UPDATED_FVK_DIRECT_R10_RECALC__PATH.csv`
5. `../50_results/steel_shell/20260815_2343__NZSCCM__Z6_AR2_UPDATED_FVK_DIRECT_R10_RECALC__PEAK_CONVERGENCE.csv`
6. `../50_results/steel_shell/20260815_2343__NZSCCM__Z6_AR2_UPDATED_FVK_DIRECT_R10_RECALC__RESULT.md`
7. `../40_execution/steel_shell/20260815_2343__NZSCCM__Z6_AR2_UPDATED_FVK_DIRECT_R10_RECALC__REPRO.py`

## Parent stages retained

- 23:06 D=.55 formal directional-continuation dense-CH representation gate
- 22:35 D=.50 formal directional moment-first engineering certificate
- 22:20 updated FvK theory/representation expansion audit
- 21:44 R20/R02 projection gate
- 21:34 minimum FvK membrane completion
- 19:55 historical Z6 AR1/AR2 three-way capacity audit

## Current decision frontier

The direct physical result now shows that the membrane completion itself does not explain the gap to Zhou/Winter by adding reserve. The next unresolved structural-object issue is the longitudinal PBL/web steel phase, which is known to change not only axial force but also generalized equilibrium. It must be incorporated into `Rq,Rc,R20,R02` before any full-section conclusion is drawn.
