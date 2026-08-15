# Z6 H0 concrete-domain pass / shell-compiler fail-fast lock

**Timestamp:** 2026-08-15 15:00 +08:00  
**Status:** CURRENT GOVERNANCE DECISION

The Z6 H0 analytic material-domain preflight has separated two issues that must no longer be conflated.

```text
PARENT R10 = UNCHANGED
N48 DEGREE = 48 UNCHANGED
ONE_CONTINUOUS_COMPLETE_HALFWAVE = UNCHANGED
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
A0 = a/500
```

## Decision A — concrete material domain

The larger-q H0 branch requires a wider scalar concrete compiler interval mainly on the positive-lambda side. Analytic Nguyen/Cayley-Hamilton bounds show that the old Z6 interval `[-1.15,0.23]` is insufficient, while `[-1.15,0.30]` covers the same-D `D=0.705` equilibrium and `[-1.30,0.40]` covers the exploratory branch box through approximately `D<=0.80, q<=0.009`.

```text
CONCRETE_DOMAIN_EXTRAPOLATION = PROHIBITED
SAME_R10_DOMAIN_COVERAGE = AUTHORIZED FOR DIAGNOSTIC CONTINUATION
R10 REFIT = PROHIBITED
N48 ORDER CHANGE AS LOAD FIT = PROHIBITED
CONCRETE_ANALYTIC_DOMAIN_PREFLIGHT = PASS
```

The enlarged interval has a measurable scalar approximation-error cost and is therefore an engineering continuation compiler, not a new strict material theorem certificate.

## Decision B — recovered H0 branch

With the justified material domain, the connected H0 `Rq=0` branch can be recovered beyond the old `D=0.705` state. At `D=0.705`, the equilibrium relocates to approximately `q=0.00735` with `P≈40.2–40.4 MN`, depending slightly on the admissible compiler interval. The branch remains rising through approximately `D=0.78`, where `P≈42.3 MN`.

These are connected-branch diagnostics, not final Pu and not strict `Rq,L` certificates.

## Decision C — new shell compiler gate

At deeper q near `D≈0.80`, the outer-shell local radial-cap scalar material coordinate remains inside its existing `[0,4]` domain, but high-degree coefficient-space composition loses numerical conditioning. Degree 24+ produces non-smooth or physically impossible shell `Rq`/force resultants while lower degrees remain mutually close for a while.

```text
SHELL_RADIAL_CAP_MATERIAL_DOMAIN_EXHAUSTION = NO
SHELL_RADIAL_CAP_COEFFICIENT_COMPOSITION_STABILITY = FAIL
SILENT_SWITCH_TO_LOWER_DEGREE_PRODUCTION = PROHIBITED
FABRICATED_FULL_KZ = PROHIBITED
```

This is a computational analytic-representation gate, not evidence of a physical loss of shell strength or tangent.

## Current next task

```text
CURRENT_NEXT_TASK = Z6_H0_SHELL_RADIAL_CAP_ANALYTIC_COMPILER_STABILIZATION_THEN_FULL_KZ
```

The stabilization must preserve the same scalar current map and zero structural discretization. Only after the shell analytic composition is stable may the connected H0 branch be continued and the full directional `KZ_c^mat, KZ_w^mat, KZ_sh^mat, KZ_geo, KZ` and `L` event ordering be released.
