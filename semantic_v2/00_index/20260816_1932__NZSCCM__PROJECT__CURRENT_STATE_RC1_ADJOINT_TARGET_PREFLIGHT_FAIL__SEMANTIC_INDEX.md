# NZ-SCCM current state — RC1 adjoint target preflight failure

**Timestamp:** 2026-08-16 19:32 +08:00

## Current verdict

The five-term compatible membrane condensation remains accepted. `R10-MSAC-RC1` remains material-level source-fidelity PASS. The 19:32 structural adapter gate tested target-side/adjoint Clenshaw and reached a sharper fail-fast boundary.

```text
ADJOINT_CLENSHAW_ALGEBRA = PASS_EXACT
LOW_ORDER_GENERAL_D15_NESTED_TARGET_IDENTITY = PASS_EXACT
RC1_NESTED_ATOM_CLOSED_MOMENT_RULE = ABSENT
ACTIVE_RC1_STRUCTURAL_TARGET_RUNTIME = FAIL_PREFLIGHT
NEW_Pu = NOT_RUN
```

## What passed

The transpose of the backward Clenshaw graph was derived and executed against an independent exact D15 low-order nested beta/Chebyshev example.

```text
final nested degree = 192
DIRECT_MINUS_ADJOINT = 0 exactly
functional/pi = .11633931515896061
```

Therefore the adjoint algebra is valid.

## What failed

The exact low-order execution also showed that the adjoint target kernel acquires the same nested composed degree unless multiplication by a nested material atom has its own closed exact moment rule.

At active RC1 first-pass orders, deterministic composition preflight gives:

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

These are composition-degree diagnostics, not intended theory orders. They demonstrate why resolving the nested target back into ordinary polynomial General-D15 leaves recreates the expansion swell. A giant active-order flattening was deliberately not allocated because that route is already prohibited.

## Structural interpretation

```text
forward Clenshaw field materialization = known swell
adjoint Clenshaw target propagation     = algebraically exact
adjoint + ordinary polynomial D15 leaf  = still not closed for nested RC1 atoms
```

The missing primitive is a direct exact moment transform for the nested atom, or a redesigned material basis whose structural moments are directly closed.

## Retained five-term membrane model

Internal coordinates remain

```text
r=[r0,r20,r22,s02,s22]
```

and current-material equilibrium remains

```text
Rm=0
Krr=dRm/dr
r_g=-Krr^-1 Rm_g
Pbar_g=P_g+P_r r_g
Rqbar_g=Rq_g+Rq_r r_g
Lbar=Pbar_D Rqbar_q-Pbar_q Rqbar_D
Kgg_cond=Kgg-Kgr Krr^-1 Krg
```

Global production topology remains `(D,q)` after condensation.

## Zero-integration status

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```

No spatial Gauss/Simpson/adaptive/collocation/material-point grid was introduced.

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

The next gate must either:

1. derive an exact finite moment closure for the beta/natural-coordinate RC1 atoms, or
2. redesign the NC material analytic representation at family level, preserving R10 physics, into a basis whose target moments close directly through General-D15/CAS/special-function algebra.

Repeating ordinary forward/adjoint polynomial Clenshaw without such a closure is not a new route.

## Key artifacts

1. `../20_theory/nc_rebar_panel/20260816_1932__NZSCCM__RC1_ADJOINT_CLENSHAW_GENERAL_D15_TARGET_CLOSURE__THEORY.md`
2. `../40_execution/common/20260816_1932__NZSCCM__RC1_ADJOINT_CLENSHAW_D15_TARGET__EXECUTION_REPORT.md`
3. `../40_execution/common/20260816_1932__NZSCCM__RC1_ADJOINT_CLENSHAW_D15_TARGET__PARAMS_AND_INTERMEDIATES.json`
4. `../40_execution/common/20260816_1932__NZSCCM__RC1_ADJOINT_CLENSHAW_D15_TARGET__REPRO.py`
5. `../60_validation/common/20260816_1932__NZSCCM__RC1_ADJOINT_CLENSHAW_D15_TARGET__AUDIT.md`
6. `../10_governance/20260816_1932__NZSCCM__RC1_ADJOINT_TARGET_FAILURE_AND_NEXT_CLOSURE__GATE_LOCK.md`
7. `20260816_1912__NZSCCM__PROJECT__CURRENT_STATE_FIVE_TERM_MEMBRANE_CONDENSATION_PARTIAL_PASS__SEMANTIC_INDEX.md` — predecessor
8. `20260816_1734__NZSCCM__PROJECT__CURRENT_STATE_R10_MSAC_RC1_MATERIAL_PASS__SEMANTIC_INDEX.md` — compiler predecessor
