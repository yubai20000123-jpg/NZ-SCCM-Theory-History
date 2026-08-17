# Case21 current formal zero-spatial release — 2026-08-17 13:04 +08:00

The current accepted implementation returns to the previously proven structural path:

```text
R10 source
 -> frozen N48-C1/MM material compiler
 -> 2x2 Cayley-Hamilton
 -> current Airy-scalar Nguyen finite trigonometric field
 -> General-D15 exact moments
 -> exact elastic reinforcement
 -> Rq=0, RA=0 connected branch
 -> first load maximum
```

Formal counters:

```text
spatial sampling = 0
spatial quadrature = 0
spatial subdomains = 1
thickness quadrature = 0
```

Current formal Airy result:

```text
D_u ~= 0.77708
q_u ~= 0.0018057
lambda_u ~= 0.0434
Pu_N48_D15 ~= 365.257 kN
```

A refined formal evaluation at

```text
D = 0.7771614625
q = 0.00180590635
lambda = 0.0434741730
```

returns

```text
Pc = 336.840639 kN
Ps =  28.415977 kN
P  = 365.256616 kN
Rq = -0.001131 kN mm
RA = +0.0000075 kN mm
```

Comparison after solve:

```text
direct raw-R10 audit oracle = 366.767829 kN
difference = -1.51118 kN = -0.4120 %
Pf_exp = 368.312750 kN
formal error vs Pf = -0.82976 %
```

Interpretation: Airy membrane redistribution does not prevent the old compiler+CH+D15 structural integration. The raw-R10 semialgebraic-period route is retained only as mathematical research/diagnostic material and is no longer a prerequisite for the current formal baseline.

Controlling records:

- `../../semantic_v2/10_governance/20260817_1304__NZSCCM__CASE21_RESTORE_N48_CH_D15_AIRY_PRODUCTION_PATH__LOCK.md`
- `../../semantic_v2/40_execution/case21/20260817_1304__NZSCCM__CASE21_AIRY_N48_CH_D15_FORMAL_ZERO_SPATIAL__EXECUTION_REPORT.md`
- `../../semantic_v2/40_execution/case21/20260817_1304__NZSCCM__CASE21_AIRY_N48_CH_D15_FORMAL_ZERO_SPATIAL__PARAMS_AND_INTERMEDIATES.json`
