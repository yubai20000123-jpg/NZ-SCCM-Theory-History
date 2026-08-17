# NZ-SCCM semantic index — Case21 Airy-scalar mechanics qualified / formal T12 gate next

**Timestamp:** 2026-08-17 11:05 +08:00  
**Status:** CURRENT OPERATIONAL ENTRY

## Governing qualification

`semantic_v2/10_governance/20260817_1105__NZSCCM__CASE21_AIRY_SCALAR_MECHANICS_QUALIFICATION_AND_LOAD_IDENTITY__LOCK.md`

## Theory contract

`semantic_v2/20_theory/nc_rebar_panel/20260817_1105__NZSCCM__CASE21_AIRY_SCALAR_MECHANICS_QUALIFICATION_AND_T12_OPERATOR_CONTRACT__THEORY.md`

## Execution / intermediates / reproducer

- `semantic_v2/40_execution/common/20260817_1105__NZSCCM__CASE21_AIRY_SCALAR_MECHANICS_QUALIFICATION__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/common/20260817_1105__NZSCCM__CASE21_AIRY_SCALAR_MECHANICS_QUALIFICATION__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/40_execution/common/20260817_1105__NZSCCM__CASE21_AIRY_SCALAR_MECHANICS_QUALIFICATION__REPRO.py`

## Current readable entry

`current/case21/CASE21_AIRY_SCALAR_MECHANICS_QUALIFICATION_20260817.md`

## Retained predecessor mechanics result

- `semantic_v2/10_governance/20260817_0210__NZSCCM__CASE21_AIRY_SCALAR_CURRENT_MEMBRANE_CLOSURE__LOCK.md`
- `semantic_v2/40_execution/common/20260817_0210__NZSCCM__CASE21_AIRY_SCALAR_CURRENT_R10_CONTINUATION__EXECUTION_REPORT.md`

The 02:10 direct-source result is retained as the current mechanics oracle; the 11:05 work qualifies it and prepares the formal operator but does not replace it with a new Pu.

## Current hard identities

```text
Pcr_exp_Case21 = 336.285554 kN  # buckling only
Pf_exp_Case21  = 368.312750 kN  # failure / ultimate
current_direct_source_Pu = 366.767829 kN
current_error_vs_Pf = -0.419459 %
formal_zero_spatial_numeric_release = OPEN
```

## Current mechanics qualification

```text
Airy scalar r=lambda*M*a = ACTIVE
pure isotropic Airy lambda=1 degeneration = PASS exact
reinforced linear scalar benchmark = PASS exact with lambda=A+B*D/M
scalar virtual-work residual transformation = PASS exact
scalar internal stability to current peak = PASS direct-source audit
five-free nonlinear Rm relaxation = REJECTED
```

## Formal operator preparation

```text
concrete value target = T12
stress thickness orders = 0,1
tangent thickness orders = 0,1,2
steel package = exact closed form while elastic
production thickness representation = GLOBAL_FIXED_ENDPOINT_POSITIVE_PART_FACTORISED_PERIOD
formal Gauss/Simpson/cells/material-point grid = prohibited
high-order coefficient enumeration = prohibited
```

## Unique next gate

`CASE21_AIRY_SCALAR_FORMAL_T12_FIXED_ENDPOINT_DESCRIPTOR_GATE`

No parallel route and no new Pu before that descriptor passes.