# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-16 23:50 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

## Current operational entry

`semantic_v2/00_index/20260816_2350__NZSCCM__PROJECT__CURRENT_STATE_Z6_FIVE_MEMBRANE_DOWNSHIFT_DIAGNOSTIC__SEMANTIC_INDEX.md`

## Frozen backbone

```text
UNIFIED_PRODUCTION_WORKFLOW_V1=ACTIVE
ONE_CONTINUOUS_COMPLETE_HALFWAVE=ACTIVE
Nguyen second-order continuous kinematics=ACTIVE
R10=FROZEN
five-term membrane redistribution=REQUIRED BUT NOW UNDER PHYSICAL-ADMISSIBILITY AUDIT
reinforcement before root solve=REQUIRED
General-D15 exact structural moments=ACTIVE
same-state KZ before formal Pu release=REQUIRED
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```

## Case21 current formal five-membrane result

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
KZ=+260.1709056728 N/mm
CONTROL=FIRST_CONNECTED_LOAD_MAXIMUM
```

Comparison:

```text
old r=0 Case21=365.5804275653 kN
five-membrane Case21=320.7491853256 kN
shift=-12.2630%
experiment=336 kN
new error=-4.5389%
```

## Z6 five-membrane direct-R10 diagnostic

A controlled same-evaluator full-section audit was executed to isolate the membrane-release effect.

```text
METHOD = direct frozen R10 + independent Gauss-Legendre oracle
FORMAL_PRODUCTION = NO
```

Same direct-R10 evaluator, r=0 peak:

```text
D~=1.59388703
q~=0.021556525
P~=51.480540 MN
Pc~=20.585826 MN
Ps~=21.876769 MN
Pw~=9.017946 MN
```

Same direct-R10 evaluator, five membrane coordinates free:

```text
D~=1.15617344
q~=0.024015334
A_increment~=288.184 mm
r=[-0.37472588,-0.37684276,+0.39596319,-0.25455699,+0.67363743]
P~=43.762840 MN
Pc~=19.982876 MN
Ps~=17.392895 MN
Pw~=6.387069 MN
lambda~=[-1.54031,+1.36017]
```

Isolated effect:

```text
Z6 r=0 -> five-membrane shift = -14.9915%
```

External audit-only comparison:

```text
vs Zhou = -11.5666%
vs Winter = -12.7985%
```

## Current interpretation

```text
SYSTEMATIC_DOWNSHIFT_RELATIVE_TO_PREVIOUS_CONSTRAINED_MEMBRANE_MODEL = EVIDENCE_PRESENT
CASE21 shift = -12.2630%
Z6 same-evaluator shift = -14.9915%
SYSTEMATIC_EXPERIMENTAL_UNDERPREDICTION = NOT_YET_PROVEN
```

The Z6 result `43.762840 MN` is AUDIT-ONLY and must NOT be cited as formal Z6 Pu.

The similarity of the Case21 and Z6 capacity reductions makes a one-off numerical accident unlikely. The five membrane coordinates, especially the large Z6 `s22`, substantially redistribute axial strain and unload face-steel/web participation. The membrane module must therefore be audited before any material recalibration.

## Compiler / formal Z6 boundary

```text
CASE21_LOCAL_N48=ALLOWED / REPRODUCED / DOMAIN_CERTIFIED
N48_AS_UNIVERSAL_NC_FAMILY_COMPILER=NOT_ALLOWED
wide-family N48 source fidelity=FAIL
N3584 source fidelity candidate=PASS
current N3584 coefficient-tensor structural backend=FAIL_COMMON_TRACTABILITY
NEW_FORMAL_Z6_FIVE_MEMBRANE_Pu=NOT_RELEASED
```

## Anti-loop / anti-calibration rule

```text
DO_NOT_REOPEN_R10=YES
DO_NOT_TUNE_R10_TO_RECOVER_CAPACITY=YES
DO_NOT_TUNE_MEMBRANE_COEFFICIENTS_TO_CASE21_OR_Z6=YES
DO_NOT_REUSE_CASE21_LOCAL_N48_FOR_Z6=YES
DO_NOT_RELEASE_AUDIT_GAUSS_RESULT_AS_FORMAL=YES
DO_NOT_START_ANOTHER_UNBOUNDED_SYMBOLIC_BACKEND_LOOP=YES
```

## Current unique next gate

`FIVE_MEMBRANE_PARENT_DISPLACEMENT_BOUNDARY_WORK_AND_CONDENSATION_AUDIT`

Trace each of `r0,r20,r22,s02,s22` back to its parent in-plane displacement field and verify:

1. four-edge in-plane boundary admissibility under the intended theoretical SSSS scope;
2. generalized external work at loaded edges;
3. no duplication of free-Poisson or global loading coordinates;
4. coordinate independence;
5. correct classification as internal condensable coordinates rather than imposed/global coordinates.

Only after this gate should a new formal Z6 capacity solve be pursued.

## Current key artifacts

- `semantic_v2/00_index/20260816_2350__NZSCCM__PROJECT__CURRENT_STATE_Z6_FIVE_MEMBRANE_DOWNSHIFT_DIAGNOSTIC__SEMANTIC_INDEX.md`
- `semantic_v2/40_execution/steel_shell/20260816_2350__NZSCCM__Z6_FIVE_MEMBRANE_DIRECT_R10_DIAGNOSTIC__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/steel_shell/20260816_2350__NZSCCM__Z6_FIVE_MEMBRANE_DIRECT_R10_DIAGNOSTIC__PARAMS_AND_INTERMEDIATES.json`
- `semantic_v2/60_validation/steel_shell/20260816_2350__NZSCCM__Z6_FIVE_MEMBRANE_SYSTEMATIC_DOWNSHIFT__AUDIT.md`
- `semantic_v2/10_governance/20260816_2350__NZSCCM__MEMBRANE_REDISTRIBUTION_DOWNSHIFT_DIAGNOSTIC__GATE_LOCK.md`
