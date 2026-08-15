# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-15 14:36 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

The operational project entry is now:

`semantic_v2/00_index/20260815_1436__NZSCCM__PROJECT__CURRENT_STATE_AND_OPEN_GAPS__SEMANTIC_INDEX.md`

Current comparison identity:

```text
ZHOU LOWER = Eqs.5-87/5-88 FE-informed conservative design/lower-envelope curve
UPPER ENGINEERING ENVELOPE = Winter curve
CURRENT FOCUS = WHY Z6 IS SIGNIFICANTLY BELOW ZHOU LOWER ENVELOPE
```

Current mechanism decisions:

```text
old omitted web-steel axial material = confirmed major partial cause
H0 restores section Pyth exactly
H0 elastic Dy = Zhou elastic Dy exactly
H0 Z6 elastic Pcr is only 1.137% below Zhou
H0 lower-envelope-equivalent load is only 0.112% below Zhou lower curve
large missing elastic web/orthotropic stiffness as dominant Z6 cause = rejected
old H0 state longitudinal steel tangent retention ~= 98.96%; immediate steel tangent collapse = not supported
Z6 deep finite-amplitude equilibrium relocation = primary active axis
full current tangent/geometric stiffness balance on new H0 branch = primary open causal target
Z6 H0 N48 material-domain exhaustion = current representation gate
CURRENT_NEXT_TASK = Z6_H0_ANALYTIC_DOMAIN_AND_FULL_DIRECTIONAL_TANGENT_KZ_GATE
```

Latest artifacts:

- `semantic_v2/10_governance/20260815_1436__Z6_H0_ELASTIC_STIFFNESS_CAUSAL_CORRECTION__LOCK.md`
- `semantic_v2/40_execution/steel_shell/20260815_1436__NZSCCM__Z6_H0__STABILITY_CAUSAL_INTERMEDIATES.json`
- `semantic_v2/40_execution/steel_shell/20260815_1436__NZSCCM__Z6_H0__SAME_BRANCH_STABILITY_CAUSAL_DECOMPOSITION__EXECUTION_REPORT.md`
- `semantic_v2/50_results/steel_shell/20260815_1436__NZSCCM__Z4_Z6_H0__ELASTIC_STIFFNESS_CAUSAL_DECOMPOSITION__RESULT.csv`

Parent R10/N48/D15 theory is unchanged. No empirical Z6 factor, no Winter/Zhou calibration, and no structural spatial discretization are authorized.
