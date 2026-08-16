# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-16 21:36 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

## Current operational entry

`semantic_v2/00_index/20260816_2136__NZSCCM__PROJECT__CURRENT_STATE_ANTI_LOOP_N48_MEMBRANE_PRODUCTION_REACTIVATED__SEMANTIC_INDEX.md`

## Frozen project-wide backbone

```text
UNIFIED_PRODUCTION_WORKFLOW_V1 = ACTIVE
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
Nguyen second-order continuous kinematics = ACTIVE
MEMBRANE_STRESS_REDISTRIBUTION = REQUIRED
R10 source current material operator = FROZEN
reinforcement/steel phase before root solve = REQUIRED
same-state current stress + consistent tangent = REQUIRED
General-D15 moment-first target framework = ACTIVE
P,Rq,L connected-branch topology = ACTIVE
same-state material + geometric KZ audit = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
Gauss/Simpson/adaptive/collocation/material-point-grid = PROHIBITED
experiment/Zhou/Winter response calibration = PROHIBITED
```

## Structural coordinates

```text
global coordinates = (D,q), A=bq
internal membrane coordinates = [r0,r20,r22,s02,s22]
```

with `Rm=0` and consistent Schur condensation.

## 21:36 decisive dual-holonomic audit

The denominator-gauge identity is exact:

```text
d V' = B V
W = V/G
=> (dG) W' = (BG-dG'I) W
```

so regular rational dual-target signatures admit exact polynomial vector-moment recurrences.

However the currently rationalized quadratic-tower basis has an interior apparent pole even for the retained smooth noncommuting prototype:

```text
A^2-4Q=(260*x-21)^2*(28624*x^2+47880*x+50121)/31116960000
x*=21/260=0.080769230769... in [-1,1]
```

while the physical atom is regular:

```text
q(x*)=0.07678482746648955...
s(x*)=0.55420150655330974...
lim(c0+c1*q)=29577184/61042095=0.48453749826246953...
```

Thus the pole belongs to the rationalized basis representation, not to the physical R10 source.

## 64-state local-matrix erratum

For basis `[1,q,s,q*s]`, the correct local matrix is

```text
[0, 0,   0,        0]
[0, ell, 0,        0]
[0, 0,   c0,       c1]
[0, 0,   c1*Q,     ell+c0]
```

The 20:59 displayed matrix interchanged `c1` and `c1*Q`. The stated differential equations were correct. The full state dimension remains `64` and the nonzero-pattern count remains `159/4096`. The 21:18 x-fiber target audit is unaffected because it did not use the x-dependent derivative matrix.

## Anti-loop production decision

A globally robust continuation of the exact-algebraic route would require an additional algebraic regularization layer such as an integral basis / Hermite reduction. Under the explicit anti-loop rule, that new backend is not opened automatically.

```text
EXACT_ALGEBRAIC_HOLONOMIC_Pu_ROUTE = PAUSED_RESEARCH_BRANCH
NO_FURTHER_EXACT_INTEGRATION_MICRO_GATE = YES
N48_C1_MM_GENERAL_D15_PRODUCTION = REACTIVATED
FIVE_TERM_MEMBRANE_REDISTRIBUTION = REQUIRED
```

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

N48 roots are material-coordinate compiler roots, not spatial integration points.

## Capacity status

```text
Case21 368.189 kN = historical/current-support closure only
Z6 51.30 MN = retained engineering baseline only
NEW membrane-redistributed Case21 Pu = NOT YET RUN
```

## Current unique next gate

```text
UNIFIED_V1_CASE21_MEMBRANE_REDISTRIBUTED_N48_PRODUCTION_GATE
```

This is an actual structural production calculation gate: solve five-term `Rm=0`, Schur-condense, solve the connected `(D,q)` limit state, and run same-state `KZ`. Do not reopen another symbolic-integration backend automatically.

## Current key artifacts

- `semantic_v2/00_index/20260816_2136__NZSCCM__PROJECT__CURRENT_STATE_ANTI_LOOP_N48_MEMBRANE_PRODUCTION_REACTIVATED__SEMANTIC_INDEX.md`
- `semantic_v2/20_theory/nc_rebar_panel/20260816_2136__NZSCCM__DUAL_HOLONOMIC_REGULARITY_ERRATUM_AND_PRODUCTION_PIVOT__THEORY.md`
- `semantic_v2/40_execution/common/20260816_2136__NZSCCM__DUAL_HOLONOMIC_REGULARITY_AND_PRODUCTION_PIVOT__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/common/20260816_2136__NZSCCM__DUAL_HOLONOMIC_REGULARITY_AND_PRODUCTION_PIVOT__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/40_execution/common/20260816_2136__NZSCCM__DUAL_HOLONOMIC_REGULARITY_AND_PRODUCTION_PIVOT__REPRO.py`
- `semantic_v2/60_validation/common/20260816_2136__NZSCCM__DUAL_HOLONOMIC_REGULARITY_AND_PRODUCTION_PIVOT__AUDIT.md`
- `semantic_v2/10_governance/20260816_2136__NZSCCM__ANTI_LOOP_EXACT_BRANCH_PAUSE_AND_N48_MEMBRANE_PRODUCTION__LOCK.md`
