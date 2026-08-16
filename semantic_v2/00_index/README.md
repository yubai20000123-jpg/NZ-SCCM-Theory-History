# NZ-SCCM semantic tree v2

This namespace is the **content-first, non-destructive semantic reconstruction** of the repository.

## Current operational entry

Use first:

`20260816_1912__NZSCCM__PROJECT__CURRENT_STATE_FIVE_TERM_MEMBRANE_CONDENSATION_PARTIAL_PASS__SEMANTIC_INDEX.md`

## Current locked production backbone

```text
UNIFIED_PRODUCTION_WORKFLOW_V1
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order continuous kinematics
MEMBRANE_STRESS_REDISTRIBUTION = REQUIRED
source current material operator
same-state current stress + consistent current tangent
Cayley-Hamilton / approved finite matrix lift
moment-first General-D15 exact structural moments
P,Rq,L connected-branch primary limit root
same-state material + geometric tangent/stability audit
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
structural calibration = NO
```

## Current RC membrane architecture

The historical RC global backbone remains `(D,q)`. The old Nguyen/von-Karman field already contained quadratic membrane strain; current work adds compatible membrane-stress redistribution/in-plane equilibrium.

Five exact classical leading membrane displacement components are now represented by finite internal coordinates

```text
r=[r0,r20,r22,s02,s22].
```

They are solved internally and must be consistently condensed; they are not five new global Pu paths.

## 19:12 five-term result

Exact elastic square-halfwave condensation gives

```text
r/M=[-(1+nu)/4,-(1-nu)/4,1/4,-(1-nu)/4,1/4]
fD=0
detK=pi^10*(1-nu)/32
```

and exactly recovers

```text
sigma_x/(E eps0)=-M cos2Y/4
sigma_y/(E eps0)=-D+M sin^2X/2
tau_xy=0.
```

For `nu=.18`, the five-coordinate elastic matrix has `cond2=4.87805`.

The nonlinear current-material formulation is fixed as

```text
Rm=0
Krr=dRm/dr
r_g=-Krr^-1 Rm_g
Pbar_g=P_g+P_r r_g
Rqbar_g=Rq_g+Rq_r r_g
Lbar=Pbar_D Rqbar_q-Pbar_q Rqbar_D
Kgg_cond=Kgg-Kgr Krr^-1 Krg
```

and all five `Rm` targets close in the existing General-D15 function space with zero formal spatial/thickness quadrature.

```text
FIVE_TERM_ELASTIC_CONDENSATION = PASS_EXACT
FIVE_TERM_AIRY_FVK_RECOVERY = PASS_EXACT
FIVE_TERM_GENERAL_D15_TARGET_CLOSURE = PASS
CURRENT_MATERIAL_CONDENSATION_FORM = PASS_FORMAL
```

## RC1 status

`R10-MSAC-RC1` remains material-level source-fidelity PASS for Z0-Z6. The nested factor graph is mandatory; full monomial expansion is prohibited.

The remaining implementation gap is:

```text
nested RC1
 -> arbitrary target kernel
 -> adjoint-Clenshaw/Qnm recurrence
 -> General-D15 exact contraction
```

This high-order structural target-functional runtime has not yet passed.

A legacy N48 current-material diagnostic confirmed that the classical elastic five-coordinate amplitudes are not nonlinear R10+rebar equilibrium values. That diagnostic was stopped immediately and is not used as RC1 production or to release a new Pu.

## Capacity status

```text
Case21 historical/current-support closure = 368.189 kN
Z6 51.30 MN = retained engineering baseline only
Z0-Z5 old production values = retracted/diagnostic under current governance
NEW membrane-redistributed Pu = not released
```

## Current gate verdict

```text
OVERALL_GATE = PARTIAL_PASS_TO_IMPLEMENTATION_BOUNDARY
RC1_NESTED_TARGET_FUNCTIONAL_RUNTIME = OPEN
NEW_Pu = NOT_RUN
```

## Current next gate

```text
UNIFIED_V1_RC1_ADJOINT_CLENSHAW_GENERAL_D15_TARGET_FUNCTIONAL_EXECUTION_GATE
```

The next task is to implement one common nested RC1 target-functional backend for `P,Rq,Rm1...Rm5,KZ`, validate it against direct low-order General-D15 expansion, execute it at the Z0-Z6 RC1 first-pass levels, and preserve zero structural spatial/thickness numerical integration.

## Repository semantic read order

1. `20260816_1912__NZSCCM__PROJECT__CURRENT_STATE_FIVE_TERM_MEMBRANE_CONDENSATION_PARTIAL_PASS__SEMANTIC_INDEX.md`
2. `../20_theory/nc_rebar_panel/20260816_1912__NZSCCM__FIVE_TERM_CURRENT_MEMBRANE_CONDENSATION_AND_RC1_D15__THEORY.md`
3. `../40_execution/common/20260816_1912__NZSCCM__FIVE_TERM_MEMBRANE_CONDENSATION_RC1_D15__EXECUTION_REPORT.md`
4. `../40_execution/common/20260816_1912__NZSCCM__FIVE_TERM_MEMBRANE_CONDENSATION_RC1_D15__PARAMS_AND_INTERMEDIATES.json`
5. `../40_execution/common/20260816_1912__NZSCCM__FIVE_TERM_MEMBRANE_CONDENSATION_RC1_D15__REPRO.py`
6. `../60_validation/common/20260816_1912__NZSCCM__FIVE_TERM_MEMBRANE_CONDENSATION_RC1_D15__AUDIT.md`
7. `20260816_1848__NZSCCM__PROJECT__CURRENT_STATE_RC_BACKBONE_MEMBRANE_DELTA_PASS__SEMANTIC_INDEX.md` — predecessor
8. `20260816_1734__NZSCCM__PROJECT__CURRENT_STATE_R10_MSAC_RC1_MATERIAL_PASS__SEMANTIC_INDEX.md` — compiler predecessor
9. `../20_theory/20260816_1217__NZSCCM__UNIFIED_PRODUCTION_WORKFLOW_V1__THEORY_AND_EXECUTION_CONTRACT.md`

No legacy file is deleted, moved or renamed solely from filename identity.
