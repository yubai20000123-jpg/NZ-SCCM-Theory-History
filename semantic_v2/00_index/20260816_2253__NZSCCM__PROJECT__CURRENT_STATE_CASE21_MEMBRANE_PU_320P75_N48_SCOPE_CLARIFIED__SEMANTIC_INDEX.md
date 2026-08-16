# NZ-SCCM CURRENT STATE — Case21 membrane Pu closed / N48 scope clarified

**Updated:** 2026-08-16 22:53 +08:00

## Current result

The five-term membrane redistribution theory has now been executed through a complete Case21 limit calculation under the reproduced Case21-local N48-C1/MM + CH + General-D15 production evaluator.

```text
CASE21_MEMBRANE_REDISTRIBUTED_Pu = 320.75 kN
D_u = 0.4597278541813354
q_u = 0.0018330938013757293
A_u = 2.2363744376783896 mm
Pc = 304.05427812103903 kN
Ps = 16.69490720454312 kN
Rq = 2.33356e-4 kN mm
||Rm||2 = 3.48901e-6
KZ(Pu) = +260.1709056728 N/mm
CONTROL = FIRST_CONNECTED_LOAD_MAXIMUM
```

Five membrane coordinates at the limit:

```text
r0  = -0.012475802483156403
r20 = -0.007141864103343101
r22 = +0.04699488414266459
s02 = +0.041946118067216
s22 = -0.09983629747628982
```

## Domain and steel gates

Continuous Bernstein certificate:

```text
min B[0.12-X11]         = 0.0198184192764
min B[det(0.12I-X)]     = 0.0125848299978
min B[X11+1.15]         = 1.0807409482495
min B[det(X+1.15I)]     = 0.5069185061517
```

Therefore the full complete halfwave remains inside the Case21-local compiler interval `[-1.15,+0.12]`.

Reinforcement remains elastic:

```text
max |epsilon_s| ~= 0.00125716 < 0.00265
```

## Comparison

```text
old r=0 Case21 = 365.5804275653 kN
new membrane Case21 = 320.7491853256 kN
change = -12.2630 %
experiment-only source = 336 kN
new error = -4.5389 %
```

## N48 scope — critical clarification

```text
CASE21_LOCAL_N48 = ALLOWED / REPRODUCED / DOMAIN_CERTIFIED
N48_AS_UNIVERSAL_NC_FAMILY_COMPILER = NOT ALLOWED
```

The 12:29 broad family gate on core/guard `[-2.35,+1.90] / [-2.60,+2.15]` found:

```text
N48 E_sigma=0.817103, E_tan=0.954681 -> FAIL
first source-fidelity pass on declared ladder = N3584
```

The 12:48 N3584 structural run then stopped at common coefficient-tensor tractability, especially Z6. Therefore using N48 for this Case21 does not erase either historical result. It is a scoped use of an already validated Case21-local evaluator.

## Formal zero-integration identity

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```

## Z6 boundary / next task

Do not reuse the Case21 49x4 coefficients for Z6. Historical Z6 principal envelope is approximately `[-2.2937,+1.8232]`, far outside the Case21-local compiler interval.

Current next task:

`Z6_MEMBRANE_REDISTRIBUTED_CAPACITY_EXECUTION_WITH_EXISTING_FAMILY_EVIDENCE`

Execution rule: attempt the direct Z6 membrane-redistributed capacity calculation using existing family-level evidence/representations. If the existing common high-order backend still fails tractability, stop with a concrete reproducible `Z6_PRODUCTION_BLOCKED_BY_COMMON_BACKEND_TRACTABILITY`; do not automatically open another symbolic integration/backend loop.

## New artifacts

- `../40_execution/common/20260816_2253__NZSCCM__CASE21_MEMBRANE_REDISTRIBUTED_N48_LIMIT__EXECUTION_REPORT.md`
- `../40_execution/common/20260816_2253__NZSCCM__CASE21_MEMBRANE_REDISTRIBUTED_N48_LIMIT__PARAMS_AND_INTERMEDIATES.json`
- `../40_execution/common/20260816_2253__NZSCCM__CASE21_MEMBRANE_REDISTRIBUTED_N48_LIMIT__REPRO.py`
- `../60_validation/common/20260816_2253__NZSCCM__CASE21_MEMBRANE_REDISTRIBUTED_N48_LIMIT__AUDIT.md`
- `../10_governance/20260816_2253__NZSCCM__N48_SCOPE_CLARIFICATION_CASE21_VS_NC_FAMILY__LOCK.md`
