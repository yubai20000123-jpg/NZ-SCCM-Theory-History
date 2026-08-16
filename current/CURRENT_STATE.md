# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-16 19:32 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

## Current operational entry

`semantic_v2/00_index/20260816_1932__NZSCCM__PROJECT__CURRENT_STATE_RC1_ADJOINT_TARGET_PREFLIGHT_FAIL__SEMANTIC_INDEX.md`

## Frozen project-wide backbone

```text
UNIFIED_PRODUCTION_WORKFLOW_V1 = ACTIVE
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
Nguyen second-order continuous kinematics = ACTIVE
MEMBRANE_STRESS_REDISTRIBUTION = REQUIRED
source current material operator = REQUIRED
same-state current stress + consistent tangent = REQUIRED
Cayley-Hamilton / approved finite matrix lift = ACTIVE
General D15 moment-first exact moments = ACTIVE
P,Rq,L connected-branch topology = ACTIVE
same-state material + geometric KZ audit = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
Gauss/Simpson/adaptive/collocation/material-point-grid = PROHIBITED
experiment/Zhou/Winter calibration = PROHIBITED
```

## Structural unknowns

Global production coordinates remain

```text
(D,q), A=bq
```

The compatible membrane-stress redistribution uses five finite internal coordinates

```text
r=[r0,r20,r22,s02,s22]
```

which are solved internally and consistently condensed. They do not change the outer `(D,q)` root topology.

## Five-term membrane status retained

The exact elastic square-halfwave condensation remains:

```text
r/M=[-(1+nu)/4,-(1-nu)/4,1/4,-(1-nu)/4,1/4]
fD=0
detK=pi^10*(1-nu)/32
```

and exactly recovers

```text
sigma_x/(E eps0)=-M cos2Y/4
sigma_y/(E eps0)=-D+M sin^2X/2
tau_xy=0
```

Current-material equations remain

```text
Rm=0
Krr=dRm/dr
r_g=-Krr^-1 Rm_g
Pbar_g=P_g+P_r r_g
Rqbar_g=Rq_g+Rq_r r_g
Lbar=Pbar_D Rqbar_q-Pbar_q Rqbar_D
Kgg_cond=Kgg-Kgr Krr^-1 Krg
```

```text
FIVE_TERM_ELASTIC_CONDENSATION = PASS_EXACT
FIVE_TERM_AIRY_FVK_RECOVERY = PASS_EXACT
FIVE_TERM_GENERAL_D15_TARGET_CLOSURE = PASS
```

## R10-MSAC-RC1 material status retained

The physical R10 current law is unchanged. `R10-MSAC-RC1` remains material-level source-fidelity PASS for Z0-Z6 with specimen-parameter-derived domains and the same family-level construction rule.

First-pass levels remain:

```text
Z0 L2: Ng=512,  Nc=14, Nt=256
Z1 L3: Ng=640,  Nc=14, Nt=320
Z2 L2: Ng=512,  Nc=14, Nt=256
Z3 L2: Ng=512,  Nc=14, Nt=256
Z4 L2: Ng=512,  Nc=14, Nt=256
Z5 L6: Ng=1024, Nc=14, Nt=512
Z6 L7: Ng=1152, Nc=16, Nt=576
```

The nested factor graph remains required; full monomial expansion remains prohibited.

## 19:32 adjoint-Clenshaw target gate

The transpose of backward Clenshaw was derived for an exact target functional `L_K`.

A fully exact rational low-order nested beta/Chebyshev test used the closed D15 moment

```text
int_0^pi sin^(2m)X dX=pi*C(2m,m)/4^m
```

and produced

```text
first warp degree       = 4
first composed degree   = 16
second warp degree      = 64
final nested degree     = 192
DIRECT_MINUS_ADJOINT    = 0 exactly
functional/pi           = .11633931515896061
```

The contributing adjoint target kernels reached degrees

```text
65,129,193
```

so the adjoint algebra is correct, but target support still inherits nested composition degree unless the nested atom has its own closed exact moment rule.

```text
ADJOINT_CLENSHAW_ALGEBRA = PASS_EXACT
LOW_ORDER_GENERAL_D15_NESTED_TARGET_IDENTITY = PASS_EXACT
```

## Active RC1 complexity preflight

For an integer beta lens, exact polynomial degree is

```text
d_beta=p+q+1
```

and the active nested representation has diagnostic composition degrees

```text
Dg=Ng*dg
DC=Nc*Dg
Dt_nat=Nt*dt
DuR=DT7=Dg*Dt_nat
DTT_nominal=3*DuR
```

The resulting first-pass ledger is:

```text
case   Dg       DC       DuR/DT7       DTT nominal
Z0   14,848   207,872   125,435,904     376,307,712
Z1    8,960   125,440    77,414,400     232,243,200
Z2   14,848   207,872   125,435,904     376,307,712
Z3   10,752   150,528    71,565,312     214,695,936
Z4   16,384   229,376   117,440,512     352,321,536
Z5   24,576   344,064   364,904,448   1,094,713,344
Z6   29,952   479,232   569,327,616   1,707,982,848
```

These are composition-degree diagnostics, not proposed production polynomial orders.

They establish that an adjoint recurrence whose only leaf rule is ordinary polynomial General-D15 still recreates the expansion hierarchy. Delaying expansion in an expression DAG is not a closed moment rule.

For Z6 a single one-dimensional dense float64 degree-index equivalent of the nominal TT scale would already be about `13.66 GB`; actual CH/invariant/D15 state is more structured and this number is not an actual production memory estimate. A forbidden giant flattening was therefore not allocated.

## 19:32 gate verdict

```text
R10_MSAC_RC1_MATERIAL_SOURCE_FIDELITY = RETAIN_PASS
FIVE_TERM_MEMBRANE_D15_TARGETS = RETAIN_PASS
ADJOINT_CLENSHAW_TARGET_RECURRENCE = PASS_EXACT_ALGEBRA
LOW_ORDER_NESTED_TARGET_IDENTITY = PASS_EXACT
RC1_NESTED_ATOM_CLOSED_MOMENT_RULE = ABSENT
ACTIVE_RC1_NESTED_TARGET_RUNTIME = FAIL_PREFLIGHT
RC1_STRUCTURAL_PRODUCTION_PROMOTION = FAIL_AT_THIS_GATE
NEW_CURRENT_MEMBRANE_r_SOLVE = NOT_RUN
NEW_Pu = NOT_RUN
```

This does not reject R10 physics and does not revoke the RC1 material-only source-fidelity pass.

## Capacity status

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

The next work must either:

1. derive a direct exact finite moment transform for the existing beta/natural-coordinate RC1 atoms, avoiding base-polynomial flattening; or
2. redesign the NC finite analytic representation at family level, preserving the R10 physical law, into a source-faithful basis whose target moments close directly with General-D15/CAS/special-function algebra.

Repeating forward or adjoint ordinary polynomial Clenshaw without such a closure is not a new route.

## Current key artifacts

- `semantic_v2/00_index/20260816_1932__NZSCCM__PROJECT__CURRENT_STATE_RC1_ADJOINT_TARGET_PREFLIGHT_FAIL__SEMANTIC_INDEX.md`
- `semantic_v2/20_theory/nc_rebar_panel/20260816_1932__NZSCCM__RC1_ADJOINT_CLENSHAW_GENERAL_D15_TARGET_CLOSURE__THEORY.md`
- `semantic_v2/40_execution/common/20260816_1932__NZSCCM__RC1_ADJOINT_CLENSHAW_D15_TARGET__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/common/20260816_1932__NZSCCM__RC1_ADJOINT_CLENSHAW_D15_TARGET__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/40_execution/common/20260816_1932__NZSCCM__RC1_ADJOINT_CLENSHAW_D15_TARGET__REPRO.py`
- `semantic_v2/60_validation/common/20260816_1932__NZSCCM__RC1_ADJOINT_CLENSHAW_D15_TARGET__AUDIT.md`
- `semantic_v2/10_governance/20260816_1932__NZSCCM__RC1_ADJOINT_TARGET_FAILURE_AND_NEXT_CLOSURE__GATE_LOCK.md`
