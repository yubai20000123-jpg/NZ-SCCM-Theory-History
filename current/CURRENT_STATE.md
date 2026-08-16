# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-16 22:53 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

## Current operational entry

`semantic_v2/00_index/20260816_2253__NZSCCM__PROJECT__CURRENT_STATE_CASE21_MEMBRANE_PU_320P75_N48_SCOPE_CLARIFIED__SEMANTIC_INDEX.md`

## Frozen backbone

```text
UNIFIED_PRODUCTION_WORKFLOW_V1=ACTIVE
ONE_CONTINUOUS_COMPLETE_HALFWAVE=ACTIVE
Nguyen second-order continuous kinematics=ACTIVE
R10=FROZEN
five-term membrane redistribution=REQUIRED
reinforcement before root solve=REQUIRED
General-D15 exact structural moments=ACTIVE
same-state KZ before Pu release=REQUIRED
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```

## Case21 membrane-redistributed result

```text
D_u=0.4597278541813354
q_u=0.0018330938013757293
A_u=2.2363744376783896 mm
r=[-0.012475802483156403,
   -0.007141864103343101,
   +0.04699488414266459,
   +0.041946118067216,
   -0.09983629747628982]
Pc=304.05427812103903 kN
Ps=16.69490720454312 kN
Pu=320.7491853255822 kN
Rq=2.33356e-4 kN mm
||Rm||2=3.48901e-6
KZ=+260.1709056728 N/mm
CONTROL=FIRST_CONNECTED_LOAD_MAXIMUM
```

Case21 current rounded capacity:

`CASE21_MEMBRANE_REDISTRIBUTED_Pu=320.75 kN`

## Case21 gates

```text
18:02 N48 fingerprint=PASS
five membrane equilibrium=PASS
total Rq=PASS
first connected load maximum=PASS
continuous compiler-domain Bernstein certificate=PASS
rebar elastic branch=PASS
same-state KZ=PASS positive
```

Continuous final domain remains inside `[-1.15,+0.12]`.

## Comparison

```text
old r=0 Case21=365.5804275653 kN
new membrane Case21=320.7491853256 kN
change=-12.2630%
experiment-only source=336 kN
new error=-4.5389%
```

## N48 scope clarification

```text
CASE21_LOCAL_N48=ALLOWED / REPRODUCED / DOMAIN_CERTIFIED
N48_AS_UNIVERSAL_NC_FAMILY_COMPILER=NOT_ALLOWED
```

The 12:29 broad family source-fidelity gate still stands:

```text
N48: E_sigma=0.817103, E_tan=0.954681 -> FAIL
N3584: first passing source-fidelity candidate on declared ladder
```

The 12:48 N3584 structural coefficient-tensor backend still stands as `FAIL_COMMON_TRACTABILITY`, especially for Z6. The current Case21 use of N48 is scoped to the already validated narrow Case21 compiler and does not erase the family audit.

## Anti-loop rule

```text
EXACT_ALGEBRAIC_HOLONOMIC_Pu_ROUTE=PAUSED_RESEARCH_BRANCH
DO_NOT_REOPEN_R10=YES
DO_NOT_REUSE_CASE21_N48_COEFFICIENTS_FOR_Z6=YES
DO_NOT_START_ANOTHER_SYMBOLIC_BACKEND_AUTOMATICALLY=YES
```

## Current next task

`Z6_MEMBRANE_REDISTRIBUTED_CAPACITY_EXECUTION_WITH_EXISTING_FAMILY_EVIDENCE`

Attempt the actual Z6 capacity calculation using existing family-level representations/evidence. If common high-order structural tractability remains the blocker, stop and report it concretely; do not open an endless new backend chain.

## Current key artifacts

- `semantic_v2/00_index/20260816_2253__NZSCCM__PROJECT__CURRENT_STATE_CASE21_MEMBRANE_PU_320P75_N48_SCOPE_CLARIFIED__SEMANTIC_INDEX.md`
- `semantic_v2/40_execution/common/20260816_2253__NZSCCM__CASE21_MEMBRANE_REDISTRIBUTED_N48_LIMIT__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/common/20260816_2253__NZSCCM__CASE21_MEMBRANE_REDISTRIBUTED_N48_LIMIT__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/40_execution/common/20260816_2253__NZSCCM__CASE21_MEMBRANE_REDISTRIBUTED_N48_LIMIT__REPRO.py`
- `semantic_v2/60_validation/common/20260816_2253__NZSCCM__CASE21_MEMBRANE_REDISTRIBUTED_N48_LIMIT__AUDIT.md`
- `semantic_v2/10_governance/20260816_2253__NZSCCM__N48_SCOPE_CLARIFICATION_CASE21_VS_NC_FAMILY__LOCK.md`
