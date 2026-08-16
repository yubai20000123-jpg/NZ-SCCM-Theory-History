# NC + rebar panel theory semantic branch

## Current production identity

Historical/current-support anchor:
`20260812_2245__NZSCCM__NC_REBAR_PANEL__R10_N48C1MM_CH_NGUYEN_GENERAL_D15__THEORY_EXECUTION_CONTRACT.LOCATOR.md`

Current governance is `UNIFIED_PRODUCTION_WORKFLOW_V1`.

## Retained global RC skeleton

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
 -> global (D,q), A=bq
 -> Nguyen second-order continuous strain
 -> R10 concrete + reinforcement current laws
 -> compatible membrane redistribution internal solve
 -> analytic/CH material representation
 -> General-D15 exact target moments
 -> P,Rq,L connected branch
 -> first +->- limit
 -> same-state KZ
```

## Five internal membrane coordinates

```text
r=[r0,r20,r22,s02,s22]
```

remain finite internal response coordinates. The exact elastic Airy/FvK recovery and the five General-D15 residual kernels remain PASS. Current-material equilibrium and condensation remain

```text
Rm=0
Krr=dRm/dr
r_g=-Krr^-1 Rm_g
Pbar_g=P_g+P_r r_g
Rqbar_g=Rq_g+Rq_r r_g
Lbar=Pbar_D Rqbar_q-Pbar_q Rqbar_D
Kgg_cond=Kgg-Kgr Krr^-1 Krg
```

Global root topology remains `(D,q)`.

## R10-MSAC-RC1 material status

R10 physics is frozen. `R10-MSAC-RC1` remains material-level source-fidelity PASS for Z0-Z6 under the existing parameter-derived domain rule. The nested factor graph is mandatory and full monomial expansion is prohibited.

## 19:32 structural target gate

The transpose/adjoint Clenshaw recurrence was derived and executed with an exact low-order nested beta/Chebyshev D15 oracle.

```text
final nested degree=192
DIRECT_MINUS_ADJOINT=0 exactly
functional/pi=.11633931515896061
```

Therefore:

```text
ADJOINT_CLENSHAW_ALGEBRA = PASS_EXACT
LOW_ORDER_GENERAL_D15_TARGET_IDENTITY = PASS_EXACT
```

But target kernels reached degrees `65,129,193`. Hence target-side recurrence alone does not provide a closed moment algebra for nested RC1 atoms.

At active first-pass orders the composition preflight reaches:

```text
Z0 DuR=125,435,904; DTT~376,307,712
Z1 DuR= 77,414,400; DTT~232,243,200
Z2 DuR=125,435,904; DTT~376,307,712
Z3 DuR= 71,565,312; DTT~214,695,936
Z4 DuR=117,440,512; DTT~352,321,536
Z5 DuR=364,904,448; DTT~1,094,713,344
Z6 DuR=569,327,616; DTT~1,707,982,848
```

These are composition-degree diagnostics, not production orders. They show that reducing nested atoms back to the ordinary polynomial D15 leaf recreates expression swell.

```text
RC1_NESTED_ATOM_CLOSED_MOMENT_RULE = ABSENT
ACTIVE_RC1_STRUCTURAL_TARGET_RUNTIME = FAIL_PREFLIGHT
```

This does not reject R10 or revoke RC1 material source fidelity.

## Reinforcement adapter

Rebar continues to use the same redistributed continuous strain field and participates in `P_s,Rq_s,Rm,Krr,KZ` before condensation/root solve. No post-hoc `As*fy` capacity addition is introduced.

## Zero-integration lock

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```

## Capacity boundary

```text
Case21 368.189 kN = historical/current-support closure only
Z6 51.30 MN = retained engineering baseline only
Z0-Z5 old values = retracted/diagnostic under current governance
NEW membrane-redistributed Pu = NOT RELEASED
```

## Current unique next gate

```text
UNIFIED_V1_NC_EXACT_NESTED_ATOM_MOMENT_CLOSURE_OR_STRUCTURALLY_CLOSED_COMPILER_REDESIGN_GATE
```

Required next direction:

1. derive a direct exact finite moment transform for the beta/natural-coordinate RC1 atoms under `P,Rq,Rm,KZ` targets; **or**
2. redesign the NC analytic compiler at family level, preserving R10 physics, into a source-faithful analytic/rational/special-function basis whose target moments close directly by General-D15/CAS.

Repeating forward or adjoint ordinary polynomial Clenshaw without a new moment closure is prohibited as a duplicate route.

## Current artifacts

- `20260816_1932__NZSCCM__RC1_ADJOINT_CLENSHAW_GENERAL_D15_TARGET_CLOSURE__THEORY.md`
- `../../40_execution/common/20260816_1932__NZSCCM__RC1_ADJOINT_CLENSHAW_D15_TARGET__EXECUTION_REPORT.md`
- `../../40_execution/common/20260816_1932__NZSCCM__RC1_ADJOINT_CLENSHAW_D15_TARGET__PARAMS_AND_INTERMEDIATES.json`
- `../../40_execution/common/20260816_1932__NZSCCM__RC1_ADJOINT_CLENSHAW_D15_TARGET__REPRO.py`
- `../../60_validation/common/20260816_1932__NZSCCM__RC1_ADJOINT_CLENSHAW_D15_TARGET__AUDIT.md`
- `../../10_governance/20260816_1932__NZSCCM__RC1_ADJOINT_TARGET_FAILURE_AND_NEXT_CLOSURE__GATE_LOCK.md`
- `../../00_index/20260816_1932__NZSCCM__PROJECT__CURRENT_STATE_RC1_ADJOINT_TARGET_PREFLIGHT_FAIL__SEMANTIC_INDEX.md`
