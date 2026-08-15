# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-15 15:00 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

The operational project entry is now:

`semantic_v2/00_index/20260815_1500__NZSCCM__PROJECT__CURRENT_STATE_AND_OPEN_GAPS__SEMANTIC_INDEX.md`

Current comparison identity:

```text
ZHOU LOWER = Eqs.5-87/5-88 FE-informed conservative design/lower-envelope curve
UPPER ENGINEERING ENVELOPE = Winter curve
CURRENT FOCUS = WHY Z6 IS SIGNIFICANTLY BELOW ZHOU LOWER ENVELOPE
```

Current mechanism / gate decisions:

```text
old omitted web-steel axial material = confirmed major partial cause
H0 Dy = Zhou Dy exactly; large elastic web-stiffness omission rejected as dominant cause
old H0 state immediate steel-tangent collapse = not supported
analytic concrete material-domain preflight = PASS
old Z6 N48 interval [-1.15,0.23] fails mainly on positive lambda side
minimal same-D interval [-1.15,0.30] and unified diagnostic interval [-1.30,0.40] established without R10/order retune
H0 connected Rq=0 branch recovered to about D=.78; P rises only to about 42.26 MN
material-domain widening does not close Z6 gap to Zhou lower 49.6724 MN
outer-shell radial-cap scalar r-domain remains covered
outer-shell high-degree coefficient-space composition becomes ill-conditioned near D~.80, q>=.0081
full KZ/L/final Pu = NOT RELEASED
CURRENT_NEXT_TASK = Z6_H0_SHELL_RADIAL_CAP_ANALYTIC_COMPILER_STABILIZATION_THEN_FULL_KZ
```

Latest artifacts:

- `semantic_v2/10_governance/20260815_1500__Z6_H0_CONCRETE_DOMAIN_PASS_SHELL_COMPILER_FAILFAST__LOCK.md`
- `semantic_v2/20_theory/nc_steel_shell_panel/20260815_1500__NZSCCM__Z6_H0__ANALYTIC_MATERIAL_DOMAIN_AND_COMPILER_STABILITY__THEORY_AUDIT.md`
- `semantic_v2/40_execution/steel_shell/20260815_1500__NZSCCM__Z6_H0__ANALYTIC_DOMAIN_BRANCH_AND_SHELL_COMPILER_GATE__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/steel_shell/20260815_1500__NZSCCM__Z6_H0__ANALYTIC_DOMAIN_BRANCH_INTERMEDIATES.json`
- `semantic_v2/40_execution/steel_shell/20260815_1500__NZSCCM__Z6_H0__ANALYTIC_DOMAIN_AND_SHELL_COMPILER_GATE__REPRO.py`
- `semantic_v2/50_results/steel_shell/20260815_1500__NZSCCM__Z6_H0__CONNECTED_BRANCH_DIAGNOSTIC__RESULT.csv`
- `semantic_v2/50_results/steel_shell/20260815_1500__NZSCCM__Z6_H0__SHELL_RADIAL_CAP_DEGREE_STABILITY__RESULT.csv`

Parent R10/N48/D15 theory is unchanged. No empirical Z6 factor, no Winter/Zhou calibration, no observed-mode fitting and no structural spatial discretization are authorized.
