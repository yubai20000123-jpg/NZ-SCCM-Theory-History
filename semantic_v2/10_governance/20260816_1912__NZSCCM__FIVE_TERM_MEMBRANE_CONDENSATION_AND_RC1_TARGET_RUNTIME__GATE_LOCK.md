# NZ-SCCM governance lock — five-term membrane condensation / RC1 target runtime

**Timestamp:** 2026-08-16 19:12 +08:00

## Locked decisions

```text
GLOBAL_RC_COORDINATES = (D,q)
FIVE_MEMBRANE_COORDINATES = FINITE_INTERNAL_RESPONSE_COORDINATES
FIVE_TERM_ELASTIC_AIRY_LIMIT = PASS_EXACT
FIVE_TERM_GENERAL_D15_FUNCTION_SPACE = PASS
NONLINEAR_ELASTIC_AIRY_AMPLITUDES_IMPOSED_DIRECTLY = NO
CURRENT_MATERIAL_Rm_EQUILIBRIUM = REQUIRED
CONSISTENT_Krr_AND_SCHUR_CONDENSATION = REQUIRED
FREE_p20_p02 = PROHIBITED
THOUSANDS_OF_FORMAL_MODES_AS_GLOBAL_UNKNOWNS = PROHIBITED
FULL_RC1_MONOMIAL_EXPANSION = PROHIBITED
NEW_Pu_BEFORE_RC1_TARGET_RUNTIME_PASS = PROHIBITED
```

## Exact elastic benchmark

For square complete halfwave:

```text
r/M=[-(1+nu)/4,-(1-nu)/4,1/4,-(1-nu)/4,1/4]
fD=0
detK=pi^10*(1-nu)/32
```

This is a required elastic-limit check, not a nonlinear R10 coefficient prescription.

## Current-material contract

```text
Rm(D,q,r)=0
Krr=dRm/dr from same current tangent
r_g=-Krr^-1 Rm_g
Pbar_g=P_g+P_r r_g
Rqbar_g=Rq_g+Rq_r r_g
Lbar=Pbar_D Rqbar_q-Pbar_q Rqbar_D
Kgg_cond=Kgg-Kgr Krr^-1 Krg
```

Outer limit topology remains the origin-connected `(D,q)` branch and its first admissible `+->-` maximum.

## Zero-integration lock

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```

No audit-only spatial quadrature exception is created.

## RC1 implementation boundary

`R10-MSAC-RC1` material source fidelity remains passed, but a production structural promotion requires one factorized target-functional runtime:

```text
nested RC1
 -> contract(state,target_kernel)
 -> adjoint-Clenshaw/Qnm or mathematically equivalent recurrence
 -> General-D15 exact contraction
```

The runtime must accept at least `P,Rq,Rm1...Rm5`, then the same-state KZ targets, without full stress-field expansion.

## Legacy diagnostic governance

The 19:12 N48 five-term diagnostic is non-production evidence only. It may not be used to select RC1 coefficients, solve a new Pu, or calibrate a membrane correction.

## Current unique next gate

```text
UNIFIED_V1_RC1_ADJOINT_CLENSHAW_GENERAL_D15_TARGET_FUNCTIONAL_EXECUTION_GATE
```

No membrane-redistributed Pu may be released before this gate passes.
