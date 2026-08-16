# NC + rebar panel theory semantic branch

## Current production identity

Historical/current-support anchor:
`20260812_2245__NZSCCM__NC_REBAR_PANEL__R10_N48C1MM_CH_NGUYEN_GENERAL_D15__THEORY_EXECUTION_CONTRACT.LOCATOR.md`

Current governance is `UNIFIED_PRODUCTION_WORKFLOW_V1`. The successful historical RC skeleton is retained and is being refined by compatible membrane-stress redistribution plus the current material/compiler architecture.

## Historical RC skeleton retained

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
 -> global (D,q), A=bq
 -> Nguyen second-order continuous strain
 -> R10 concrete current operator
 -> reinforcement current law on same continuous strain field
 -> analytic/CH material representation
 -> General-D15 exact target moments
 -> Pc,Rq,c,Ps,Rq,s
 -> P,Rq,L connected branch
 -> first +->- limit
 -> same-state KZ
```

## Membrane clarification

The old RC model already has Nguyen/von-Karman quadratic membrane strain. Current additional physics is

```text
MEMBRANE_STRESS_REDISTRIBUTION / IN-PLANE EQUILIBRIUM REFINEMENT
```

not “adding membrane effect for the first time”.

The 18:48 gate isolated the exact classical complete-halfwave Airy/FvK redistribution and showed that its leading compatible displacement space contains five physically interpretable components rather than free `p20,p02` variables.

## 19:12 five internal coordinates

The leading internal membrane coordinates are now

```text
r=[r0,r20,r22,s02,s22]
```

with compatible basis strains

```text
B0   =(1,0,0)
B20  =(cos2X,0,0)
Bu22 =(cos2X cos2Y,0,-sin2X sin2Y)
B02  =(0,cos2Y,0)
Bv22 =(0,cos2X cos2Y,-sin2X sin2Y)
```

They are finite internal response coordinates. After consistent condensation, global production remains `(D,q)`.

## Exact elastic condensation

For a square halfwave:

```text
r/M=[-(1+nu)/4,-(1-nu)/4,1/4,-(1-nu)/4,1/4]
fD=0
detK=pi^10*(1-nu)/32
```

At `nu=.18`, `cond2(K)=4.87805`.

The reconstructed elastic stresses are exactly

```text
sigma_x/(E eps0)=-M cos2Y/4
sigma_y/(E eps0)=-D+M sin^2X/2
tau_xy=0
```

and therefore reproduce the classical Airy/FvK limit exactly.

```text
FIVE_TERM_ELASTIC_CONDENSATION = PASS_EXACT
FIVE_TERM_AIRY_FVK_RECOVERY = PASS_EXACT
```

## Current-material formulation

In nonlinear R10 + rebar, the elastic amplitudes are not imposed. Instead:

```text
Rm_j=sum_p int sigma_p:B_j dV=0
Krr=dRm/dr
r_g=-Krr^-1 Rm_g
Pbar_g=P_g+P_r r_g
Rqbar_g=Rq_g+Rq_r r_g
Lbar=Pbar_D Rqbar_q-Pbar_q Rqbar_D
Kgg_cond=Kgg-Kgr Krr^-1 Krg
```

Concrete and reinforcement participate in the same internal equilibrium. No second Pu solver is introduced.

## General-D15 closure

All five membrane residuals are finite target functionals of the same current stress:

```text
D15[Sxx]
D15[Sxx cos2X]
D15[Sxx cos2X cos2Y-Sxy sin2X sin2Y]
D15[Syy cos2Y]
D15[Syy cos2X cos2Y-Sxy sin2X sin2Y]
```

Using the exact trigonometric identities, the final scalar integrands remain in the current General-D15 finite integer-trigonometric/thickness polynomial family.

```text
FIVE_TERM_GENERAL_D15_TARGET_CLOSURE = PASS
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

## Reinforcement adapter

Rebar uses the same redistributed continuous strain field. It contributes to

```text
P_s
Rq_s
Rm_j
Krr and cross tangent blocks
KZ_s^mat / KZ_s^geo
```

under its frozen directional/layer current law. Steel is never added after a concrete peak as a scalar capacity.

## Material/compiler status

R10 remains frozen. Specimen-parameter-derived material domains remain active. `R10-MSAC-RC1` is material source-fidelity PASS for Z0-Z6.

The RC1 graph must remain nested; full monomial expansion is prohibited.

## 19:12 fail-fast diagnostic

A legacy Case21 N48-C1 CH/D15 kernel was used only to test the nonlinear membrane residual at the classical elastic five-coordinate state. The residuals were clearly nonzero, proving that the elastic Airy amplitudes cannot simply be imposed in nonlinear current material. A first generalized-coordinate Newton diagnostic was not suitable for promotion, and because the kernel is not RC1 the route was stopped immediately.

```text
LEGACY_N48_AS_CURRENT_PRODUCTION = NO
NEW_Pu_FROM_THIS_DIAGNOSTIC = NO
```

## Current numerical boundary

```text
Case21 historical/current-support fresh closure = 368.189 kN
Z6 51.30 MN = retained engineering baseline only
Z0-Z5 old production values = RETRACTED/DIAGNOSTIC under current governance
NEW membrane-redistributed Pu = NOT RELEASED
```

## Current gate verdict

```text
FIVE_TERM_ELASTIC_CONDENSATION = PASS_EXACT
FIVE_TERM_AIRY_FVK_RECOVERY = PASS_EXACT
FIVE_TERM_GENERAL_D15_TARGET_CLOSURE = PASS
CURRENT_MATERIAL_CONDENSATION_FORM = PASS_FORMAL
RC1_NESTED_TARGET_FUNCTIONAL_RUNTIME = OPEN
OVERALL_GATE = PARTIAL_PASS_TO_IMPLEMENTATION_BOUNDARY
```

## Current next gate

```text
UNIFIED_V1_RC1_ADJOINT_CLENSHAW_GENERAL_D15_TARGET_FUNCTIONAL_EXECUTION_GATE
```

Required:

1. implement one common `contract(state,target_kernel)` backend for the nested RC1 graph;
2. preserve factorization and never form the full high-degree stress polynomial;
3. validate low-order nested output against direct General-D15 expansion;
4. support `P,Rq,Rm1...Rm5` first, then the same-state KZ targets;
5. benchmark time/memory/moment-state count at Z0-Z6 RC1 first-pass levels;
6. keep all structural spatial/thickness quadrature counters at zero;
7. only after this backend passes solve current `r(D,q)`, Schur-condense and produce new Pu.

## Current artifacts

- `20260816_1912__NZSCCM__FIVE_TERM_CURRENT_MEMBRANE_CONDENSATION_AND_RC1_D15__THEORY.md`
- `../../40_execution/common/20260816_1912__NZSCCM__FIVE_TERM_MEMBRANE_CONDENSATION_RC1_D15__EXECUTION_REPORT.md`
- `../../40_execution/common/20260816_1912__NZSCCM__FIVE_TERM_MEMBRANE_CONDENSATION_RC1_D15__PARAMS_AND_INTERMEDIATES.json`
- `../../40_execution/common/20260816_1912__NZSCCM__FIVE_TERM_MEMBRANE_CONDENSATION_RC1_D15__REPRO.py`
- `../../60_validation/common/20260816_1912__NZSCCM__FIVE_TERM_MEMBRANE_CONDENSATION_RC1_D15__AUDIT.md`
- `../../00_index/20260816_1912__NZSCCM__PROJECT__CURRENT_STATE_FIVE_TERM_MEMBRANE_CONDENSATION_PARTIAL_PASS__SEMANTIC_INDEX.md`
