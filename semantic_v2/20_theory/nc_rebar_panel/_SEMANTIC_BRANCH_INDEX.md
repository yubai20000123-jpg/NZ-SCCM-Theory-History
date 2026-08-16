# NC + rebar panel theory semantic branch

## Current production identity

Case21 current production result is now closed under the already reproduced Case21-local N48-C1/MM + Cayley-Hamilton + General-D15 evaluator with five-term membrane redistribution.

Current governance: `UNIFIED_PRODUCTION_WORKFLOW_V1` + anti-loop lock + N48 scope clarification.

## Active mechanics

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
 -> global (D,q), A=bq
 -> Nguyen second-order continuous strain
 -> five internal compatible membrane coordinates r=[r0,r20,r22,s02,s22]
 -> same-state R10 concrete + reinforcement
 -> solve five Rm + total Rq
 -> eliminate internal membrane response / follow connected equilibrium set
 -> first connected load maximum
 -> same-state KZ
```

## Case21 result

```text
D_u=0.4597278541813354
q_u=0.0018330938013757293
A_u=2.2363744376783896 mm
r0 =-0.012475802483156403
r20=-0.007141864103343101
r22=+0.04699488414266459
s02=+0.041946118067216
s22=-0.09983629747628982
Pc=304.05427812103903 kN
Ps=16.69490720454312 kN
Pu=320.7491853255822 kN
KZ(Pu)=+260.1709056728 N/mm
CONTROL=FIRST_CONNECTED_LOAD_MAXIMUM
```

Rounded current Case21 capacity: `320.75 kN`.

## Case21-local compiler identity

```text
interval=[-1.15,+0.12]
N=48
U=N48-C1
C=N48-C1
T=N48-C1-CONSTRAINED-MINIMAX
T7=N48-C1
```

The final membrane state passes a continuous Bernstein domain certificate inside this interval. The old 18:02 r=0 load fingerprint was reproduced to `6.4e-7 kN`.

## Critical N48 scope clarification

The above does **not** make N48 a universal NC family compiler.

12:29 broad family source-fidelity gate:

```text
core=[-2.35,+1.90]
guard=[-2.60,+2.15]
N48 E_sigma=0.817103, E_tan=0.954681 -> FAIL
first passing source-fidelity candidate=N3584
```

12:48 then found the present N3584 coefficient-tensor structural backend impractical for Z6. Both results remain valid.

Therefore:

```text
CASE21_LOCAL_N48=ALLOWED
N48_UNIVERSAL_NC_FAMILY=NOT_ALLOWED
CASE21_N48_COEFFICIENTS_FOR_Z6=PROHIBITED
```

## Formal zero-integration identity

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```

## Capacity comparison

```text
old Case21 r=0=365.5804275653 kN
new membrane Case21=320.7491853256 kN
change=-12.2630%
experiment=336 kN
new error=-4.5389%
```

## Next task

`Z6_MEMBRANE_REDISTRIBUTED_CAPACITY_EXECUTION_WITH_EXISTING_FAMILY_EVIDENCE`

Do not restart a new symbolic backend automatically. Try the existing family-level route; if common tractability remains the hard blocker, record the blocker and stop rather than silently falling back to the Case21-local N48 compiler.

## Current artifacts

- `../../00_index/20260816_2253__NZSCCM__PROJECT__CURRENT_STATE_CASE21_MEMBRANE_PU_320P75_N48_SCOPE_CLARIFIED__SEMANTIC_INDEX.md`
- `../../40_execution/common/20260816_2253__NZSCCM__CASE21_MEMBRANE_REDISTRIBUTED_N48_LIMIT__EXECUTION_REPORT.md`
- `../../40_execution/common/20260816_2253__NZSCCM__CASE21_MEMBRANE_REDISTRIBUTED_N48_LIMIT__PARAMS_AND_INTERMEDIATES.json`
- `../../40_execution/common/20260816_2253__NZSCCM__CASE21_MEMBRANE_REDISTRIBUTED_N48_LIMIT__REPRO.py`
- `../../60_validation/common/20260816_2253__NZSCCM__CASE21_MEMBRANE_REDISTRIBUTED_N48_LIMIT__AUDIT.md`
- `../../10_governance/20260816_2253__NZSCCM__N48_SCOPE_CLARIFICATION_CASE21_VS_NC_FAMILY__LOCK.md`
