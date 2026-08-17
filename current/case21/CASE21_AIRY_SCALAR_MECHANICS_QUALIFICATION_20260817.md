# Case21 current Airy-scalar mechanics qualification — 2026-08-17 11:05 +08:00

## Current qualified state

```text
Case21 experimental buckling load Pcr_exp = 336.285554 kN
Case21 experimental failure load  Pf_exp  = 368.312750 kN
current direct-source mechanics Pu          = 366.767829 kN
ultimate-load error vs Pf_exp               = -0.419459 %
```

The active membrane closure remains

\[
r=\lambda M a(\nu),
\qquad
M=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right).
\]

Qualification completed at 11:05:

```text
load identity Pcr vs Pf = PASS / hard locked
pure isotropic continuum Airy limit = PASS exact
reinforced linear scalar benchmark = PASS exact
virtual-work coordinate transformation = PASS exact
current nonlinear scalar internal stability to peak = PASS direct-source audit
Case21 small-M scaling = PASS
steel current supported branch = elastic / closed form
formal concrete value target contract = T12
formal zero-spatial numeric release = still OPEN
```

Important benchmark correction:

```text
lambda=1 exactly
```

applies to the single isotropic continuum Airy benchmark. With reinforcement included before the solve, the exact linear scalar RC benchmark is

\[
\lambda_{lin,RC}=0.999266844854884
+0.0096124785693025\,D/M.
\]

At the current direct-source peak:

```text
D = 0.7887924801
q = 0.0018083573
lambda = 0.0862359635
M = 0.02907033478
Pu = 366.76782869 kN
dRA/dlambda (144x144x76 audit) = +25.24850924
M*dRA/dlambda                 = +0.733982616
```

so no scalar internal membrane instability is found before the current load peak.

## Controlling files

- `semantic_v2/10_governance/20260817_1105__NZSCCM__CASE21_AIRY_SCALAR_MECHANICS_QUALIFICATION_AND_LOAD_IDENTITY__LOCK.md`
- `semantic_v2/20_theory/nc_rebar_panel/20260817_1105__NZSCCM__CASE21_AIRY_SCALAR_MECHANICS_QUALIFICATION_AND_T12_OPERATOR_CONTRACT__THEORY.md`
- `semantic_v2/40_execution/common/20260817_1105__NZSCCM__CASE21_AIRY_SCALAR_MECHANICS_QUALIFICATION__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/common/20260817_1105__NZSCCM__CASE21_AIRY_SCALAR_MECHANICS_QUALIFICATION__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/40_execution/common/20260817_1105__NZSCCM__CASE21_AIRY_SCALAR_MECHANICS_QUALIFICATION__REPRO.py`

## Unique next gate

```text
CASE21_AIRY_SCALAR_FORMAL_T12_FIXED_ENDPOINT_DESCRIPTOR_GATE
```

No new formal `Pu` has been released in this qualification step.