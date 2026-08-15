# NZ-SCCM project current state and open gaps — semantic index

**Timestamp:** 2026-08-15 15:00 +08:00  
**Status:** CURRENT OPERATIONAL STATE

## 1. Frozen parent identity

```text
FORMAL_DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
GENERALIZED_COORDINATES = D,q
KINEMATICS = NGUYEN_SECOND_ORDER
R10 = FROZEN
N48-C1/MM DEGREE = 48 FROZEN
CAYLEY_HAMILTON = GOVERNING
GENERAL_D15 = GOVERNING
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
STRUCTURAL_CALIBRATION = NO
A0 = a/500
```

Comparison bracket remains:

```text
LOWER = Zhou Eqs.(5-87)-(5-88) FE-informed conservative design curve
UPPER = Winter engineering envelope
Z6 Zhou lower = 49.67243594 MN
```

## 2. Stage-A conclusions remain valid

```text
old omitted web-steel axial material = confirmed major partial cause
H0 section Pyth = Zhou full Pyth exactly
H0 Dy = Zhou Dy exactly
Z6 H0 elastic Pcr = 42.34444 MN vs Zhou 42.83148 MN (-1.137%)
H0 lower-envelope equivalent = 49.61683 MN vs Zhou 49.67244 MN (-0.112%)
large missing elastic web rigidity = rejected as dominant Z6 cause
old-state steel longitudinal tangent retention ~=98.96%; immediate steel-tangent collapse not supported
```

## 3. New analytic concrete-domain result

The N48 scalar coordinate on the larger-q H0 branch is bounded analytically by

\[
\lambda_{min}=-D-\frac{\nu+k^2}{1-\nu^2}B,
\]

and for the active positive branch

\[
\lambda_{max}=\frac{M+(1+\nu k^2)^2B^2/(4M)}{1-\nu^2}.
\]

The old Z6 interval `[-1.15,0.23]` becomes insufficient primarily on the positive side. Same-R10, same-degree coverage gives:

```text
minimal same-D interval = [-1.15,0.30]
unified diagnostic interval = [-1.30,0.40]
CONCRETE_ANALYTIC_DOMAIN_PREFLIGHT = PASS
```

No R10 refit and no N48 order increase occurred.

## 4. New H0 connected branch recovered

The old H0 state remains

```text
D=0.705
q=0.0058975999
P=44.5061842 MN
Rq=-1.658145e9 N mm
NOT equilibrium / NOT Pu
```

After justified material-domain coverage, the same-D equilibrium relocates to approximately

```text
D=0.705
q≈0.00735
P≈40.23–40.38 MN
```

The connected H0 branch continues upward approximately as:

```text
D=.65  -> P≈39.56 MN
D=.705 -> P≈40.38 MN
D=.72  -> P≈40.45 MN
D=.74  -> P≈40.84 MN
D=.76  -> P≈41.72 MN
D=.78  -> P≈42.26 MN
```

These are engineering connected-branch locators, not final Pu and not strict `Rq,L` certificates.

The material-domain correction therefore removes the extrapolation blocker but does not close the Z6 gap to the Zhou lower envelope.

## 5. New fail-fast gate: outer-shell radial-cap coefficient composition

Near `D≈0.80,q>=0.0081`, the concrete lambda range remains inside `[-1.30,0.40]`, and the shell scalar radial-cap material coordinate remains inside `[0,4]`. Nevertheless the high-degree coefficient-space composition becomes ill-conditioned.

Representative `D=0.80,q=0.009` shell-only diagnostics:

```text
deg16: Psh≈24.0507 MN, Rq_sh≈+1.856e9 N mm
deg18: Psh≈23.9975 MN, Rq_sh≈+1.822e9 N mm
deg20: Rq_sh begins to lose conditioning
deg22: Rq_sh≈+73.1e9 N mm
deg24: Psh≈-159.8 MN, Rq_sh≈+205e9 N mm -> rejected
```

Thus:

```text
SHELL_RADIAL_CAP_MATERIAL_DOMAIN_EXHAUSTION = NO
SHELL_RADIAL_CAP_COEFFICIENT_COMPOSITION_STABILITY = FAIL AT DEEP q
LOWER DEGREE AS SILENT PRODUCTION SUBSTITUTE = PROHIBITED
```

This is a numerical analytic-representation gate, not a physical shell failure mechanism.

## 6. Full KZ status

Not released:

```text
KZ_c^mat
KZ_w^mat
KZ_sh^mat
KZ_geo
KZ total
L event
first-yield -> KZ=0 -> load maximum/fold ordering
final H0 Pu
```

Reason: the full directional tangent must use a numerically valid current shell map on the same connected branch. No KZ number is fabricated after the shell coefficient gate fails.

## 7. Current causal hierarchy

```text
OLD WEB-STEEL AXIAL OMISSION = MAJOR PARTIAL CAUSE
LARGE ELASTIC WEB-STIFFNESS OMISSION = REJECTED AS DOMINANT
IMMEDIATE STEEL-TANGENT COLLAPSE = NOT SUPPORTED AT OLD STATE
CONCRETE N48 OLD INTERVAL EXHAUSTION = RESOLVED AS DOMAIN-COVERAGE BLOCKER
DEEP FINITE-AMPLITUDE H0 EQUILIBRIUM RELOCATION = CONFIRMED
NONLINEAR CURRENT-TANGENT / GEOMETRIC-STIFFNESS BALANCE = PRIMARY PHYSICAL TARGET
OUTER-SHELL COEFFICIENT COMPOSITION = NEW COMPUTATIONAL GATE BEFORE FULL KZ
```

## 8. Current next task

```text
CURRENT_NEXT_TASK = Z6_H0_SHELL_RADIAL_CAP_ANALYTIC_COMPILER_STABILIZATION_THEN_FULL_KZ
```

The scalar `alpha_loc(r)` target must remain unchanged. The next work may change only the stable analytic evaluation/compilation architecture; it may not add structural points, Gauss integration, empirical Z6 correction, Zhou/Winter fitting or observed-mode calibration.

## 9. New artifacts

- `semantic_v2/10_governance/20260815_1500__Z6_H0_CONCRETE_DOMAIN_PASS_SHELL_COMPILER_FAILFAST__LOCK.md`
- `semantic_v2/20_theory/nc_steel_shell_panel/20260815_1500__NZSCCM__Z6_H0__ANALYTIC_MATERIAL_DOMAIN_AND_COMPILER_STABILITY__THEORY_AUDIT.md`
- `semantic_v2/40_execution/steel_shell/20260815_1500__NZSCCM__Z6_H0__ANALYTIC_DOMAIN_BRANCH_AND_SHELL_COMPILER_GATE__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/steel_shell/20260815_1500__NZSCCM__Z6_H0__ANALYTIC_DOMAIN_BRANCH_INTERMEDIATES.json`
- `semantic_v2/40_execution/steel_shell/20260815_1500__NZSCCM__Z6_H0__ANALYTIC_DOMAIN_AND_SHELL_COMPILER_GATE__REPRO.py`
- `semantic_v2/50_results/steel_shell/20260815_1500__NZSCCM__Z6_H0__CONNECTED_BRANCH_DIAGNOSTIC__RESULT.csv`
- `semantic_v2/50_results/steel_shell/20260815_1500__NZSCCM__Z6_H0__SHELL_RADIAL_CAP_DEGREE_STABILITY__RESULT.csv`
