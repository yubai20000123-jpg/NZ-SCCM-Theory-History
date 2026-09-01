# NZ-SCCM — R12 self-contained ledger + generic Excel no-lookup audit

**Date:** 2026-09-01  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Production main:** unchanged

## 1. Current ledger

Current standalone theory contract:

`semantic_v2/20_theory/20260901__NZSCCM__STEEL_SHELL_UHPC_CENTRAL_TECHNICAL_LEDGER_R12_SELF_CONTAINED_PARAMETRIC.md`

R12 inlines the previously external generic R02/R06 local stress field:

- seven LL Airy harmonics;
- `A_pq` biharmonic coefficients;
- complete `sigma_x(u,v), sigma_y(u,v), tau_xy(u,v)`;
- polynomial Mises functional `Phi(u,v)`;
- interior, edge and corner candidate rules;
- R06 radial first-yield definition;
- R12 UHPC polynomial stress and exact F0/F1 primitives;
- web exact yield-crossing integration;
- total section closure and terminal;
- standalone input/output/fail-fast contract.

Historical markdown files are provenance only and are not required to re-code the current theory.

## 2. Generic Excel artifact

Artifact:

`NZSCCM_钢壳UHPC_R12_通用参数化_无试件预存_20260901.xlsx`

SHA-256:

`41bde1f68467b5fe542ce80193a7bf63d01775924e5cad17f116961a5819c023`

The workbook contains one active input set only.

Audit results:

```text
reference specimen name scan = 0 matches
specimen_id dependency in engine = 0 matches
reference Pu lookup = NONE
formula error scan = 0 matches
```

`specimen_id=USER_DEFINED` is a label only. The engine does not read `01_INPUT!B5`.

## 3. Exact integer global-mode selection

The generic workbook no longer uses a fixed mode scan such as 1..12 or 1..40.

It computes

`m_cont = (a/b)*(Dx/Dy)^(1/4)`

and evaluates the exact two adjacent positive integers

`m1=max(1,floor(m_cont))`, `m2=m1+1`.

Because `Pcr(m)=A/m^2+constant+B*m^2`, this is the exact positive-integer minimum and has no aspect-ratio-specific cutoff.

## 4. Generic R06 implementation

The workbook no longer hard-codes the previously audited `v=-1` active edge.

For every R06 face state it reconstructs the full two-dimensional LL polynomial Mises field over `(u,v) in [-1,1]^2`.

The executable evaluator includes:

- exact univariate edge stationary roots;
- four corners;
- exact interior derivative equations `Phi_u=Phi_v=0`, numerically solved and residual-checked for the Excel execution backend;
- the exact scalar `Psi(eta)=0` first-crossing equation.

This is an execution evaluator of the R12 equations, not a new mechanical theory. The formal ledger retains the resultant/all-root definition.

## 5. Exact embedded-PY validation

The Python text extracted from the actual stored `03_ENGINE!A5` Excel formula was executed with a mock `xl()` cell reader. This validates the stored formula itself, not merely an external copy of the equations.

The embedded code does not contain reference specimen names or result lookup branches.

### USER_A — arbitrary R04 pressure test

Input subset:

```text
b=900
a=1700
tc=45
ts=5
A0g=1.8
Aw=1000
Lx=180
Ly=160
A0local=0.10
```

Result from the exact stored engine:

```text
branch = R04_YIELD_FIRST
m* = 2
Pcr = 77.68208281301811 MN
q = 0.00025910847655128517
Pu = 8.914815319286488 MN
Rmax = 5.093170329928398e-11
status = PASS
```

### USER_B — arbitrary R06 pressure test

Input subset:

```text
b=1800
a=3000
tc=50
ts=4.5
A0g=3.6
Aw=1500
Lx=450
Ly=410
A0local=0.25
```

Result from the exact stored engine:

```text
branch = R06_LOCAL_FIRST
m* = 2
Pcr = 45.1541579238774 MN
q = 0.0009422771490097644
Pu = 14.50626175137054 MN
R06 upper active-local candidate = (u,v)=(0.7012859942119918,-1.0)
R06 lower active-local candidate = (u,v)=(0.7463563920989347,-1.0)
Rmax = 3.8198777474462986e-11
status = PASS
```

USER_A/USER_B are synthetic pressure tests created for this audit. They are not historical specimens and are not runtime lookup data.

## 6. Parameter-driven verdict

```text
ONE_ACTIVE_INPUT_SET = PASS
REFERENCE_SPECIMEN_DATABASE = NONE
REFERENCE_PU_DATABASE = NONE
SPECIMEN_ID_READ_BY_ENGINE = NO
PARAMETER_PROPAGATION = PASS
R04_GENERIC_INPUT = PASS
R06_GENERIC_INPUT = PASS
GENERIC_FULL_2D_R06 = PASS_EXECUTION_EVALUATOR
SELF_CONTAINED_LEDGER = PASS
```

Domain caveat:

The workbook can calculate a user-defined parameter set when the inputs satisfy the R12 geometry/material contracts and an admissible compression-contact root exists. If the theory has no admissible root or a tension-first terminal is reached, the required behavior is explicit failure, not substitution of a stored result.