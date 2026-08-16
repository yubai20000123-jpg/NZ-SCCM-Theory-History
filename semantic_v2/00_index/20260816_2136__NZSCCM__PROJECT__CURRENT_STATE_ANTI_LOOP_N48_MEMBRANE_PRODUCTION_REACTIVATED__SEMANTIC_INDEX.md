# NZ-SCCM current state — exact-backend research pause / N48 membrane production reactivated

**Timestamp:** 2026-08-16 21:36 +08:00

## Current verdict

The full exact-algebraic branch remains retained, but the current rationalized quadratic-tower basis has an interior apparent pole that requires an additional algebraic regularization layer before it can serve as a globally robust thickness-production backend.

Under the explicit anti-loop rule, that extra backend layer is not opened. The production route returns to the already successful zero-spatial N48-C1/MM + General-D15 contract and immediately carries forward the five-term membrane-stress redistribution.

```text
64_STATE_LOCAL_MATRIX_ERRATUM = ISSUED
DUAL_DENOMINATOR_GAUGE = PASS_EXACT_FOR_REGULAR_SIGNATURES
RATIONALIZED_QUADRATIC_TOWER_GLOBAL_REGULARITY = FAIL_APPARENT_INTERIOR_POLE
PHYSICAL_SMOOTH_ATOM_REGULAR_AT_POLE = PASS
EXACT_ALGEBRAIC_HOLONOMIC_Pu_ROUTE = PAUSED_RESEARCH_BRANCH
N48_C1_MM_GENERAL_D15_PRODUCTION = REACTIVATED
FIVE_TERM_MEMBRANE_REDISTRIBUTION = REQUIRED
NEW_Pu = NOT_RUN_IN_THIS_GATE
```

## Correct 64-state local block

For local basis `[1,q,s,q*s]`:

```text
q'    = ell*q
s'    = c0*s+c1*q*s
(qs)' = c1*Q*s+(ell+c0)*q*s
```

and the accepted matrix is

```text
[0, 0,   0,        0]
[0, ell, 0,        0]
[0, 0,   c0,       c1]
[0, 0,   c1*Q,     ell+c0]
```

The prior 20:59 displayed matrix interchanged `c1` and `c1*Q`. State dimension `64` and sparsity count `159/4096` remain unchanged.

## Decisive apparent-pole audit

For the retained noncommuting smooth prototype,

```text
A^2-4Q=(260*x-21)^2*(28624*x^2+47880*x+50121)/31116960000
x*=21/260=0.080769230769...
```

lies inside `[-1,1]`, while

```text
q(x*)=0.07678482746648955...
s(x*)=0.55420150655330974...
lim(c0+c1*q)=29577184/61042095=0.48453749826246953...
```

so the physical atom is regular and only the rationalized basis is singular.

## Exact dual gauge result

For

```text
d V' = B V
W = V/G
```

there is an exact polynomial gauged system

```text
(dG) W' = (BG-dG'I) W
```

and therefore an exact vector moment recurrence for any denominator signature `G` that is globally nonzero on the complete thickness interval.

The obstruction is not this identity; it is the apparent-pole regularity of the rationalized field representation.

## Anti-loop production decision

No new integral-basis/Hermite symbolic backend is opened automatically. No further exact-integration micro-gate is allowed to delay Pu production unless explicitly reopened later.

The active production contract is again

`current/theory/NZ_SCCM_NC_REBAR_ZERO_SPATIAL_PRODUCTION_THEORY_CONTRACT_20260812_2245.md`

with

```text
N48_ORDER=48
U=N48-C1
C=N48-C1
T7=N48-C1
T=N48-C1-CONSTRAINED-MINIMAX
CAYLEY_HAMILTON=GOVERNING
D15_GENERAL_TRIG_MOMENTS=ACTIVE
```

and the five membrane coordinates

```text
r=[r0,r20,r22,s02,s22]
```

solved from `Rm=0` and Schur-condensed before the outer `(D,q)` root solve.

## Zero-integration status

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```

N48 material-coordinate roots are not spatial integration points.

## Capacity boundary

```text
Case21 368.189 kN = historical/current-support closure only
Z6 51.30 MN = retained engineering baseline only
NEW membrane-redistributed Case21 Pu = NOT YET RUN
```

## Current unique next gate

```text
UNIFIED_V1_CASE21_MEMBRANE_REDISTRIBUTED_N48_PRODUCTION_GATE
```

This gate must perform the actual five-variable internal membrane equilibrium, Schur condensation, `(D,q)` connected limit solve and same-state KZ audit. It is not another backend-development gate.

## Key artifacts

1. `../20_theory/nc_rebar_panel/20260816_2136__NZSCCM__DUAL_HOLONOMIC_REGULARITY_ERRATUM_AND_PRODUCTION_PIVOT__THEORY.md`
2. `../40_execution/common/20260816_2136__NZSCCM__DUAL_HOLONOMIC_REGULARITY_AND_PRODUCTION_PIVOT__EXECUTION_REPORT.md`
3. `../40_execution/common/20260816_2136__NZSCCM__DUAL_HOLONOMIC_REGULARITY_AND_PRODUCTION_PIVOT__PARAMS_AND_INTERMEDIATES.json`
4. `../40_execution/common/20260816_2136__NZSCCM__DUAL_HOLONOMIC_REGULARITY_AND_PRODUCTION_PIVOT__REPRO.py`
5. `../60_validation/common/20260816_2136__NZSCCM__DUAL_HOLONOMIC_REGULARITY_AND_PRODUCTION_PIVOT__AUDIT.md`
6. `../10_governance/20260816_2136__NZSCCM__ANTI_LOOP_EXACT_BRANCH_PAUSE_AND_N48_MEMBRANE_PRODUCTION__LOCK.md`
7. `20260816_2118__NZSCCM__PROJECT__CURRENT_STATE_ADJOINT_CH_TARGET_PASS_DUAL_HOLONOMIC_THICKNESS_OPEN__SEMANTIC_INDEX.md` — predecessor
