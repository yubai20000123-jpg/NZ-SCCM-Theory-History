# NZ-SCCM — parameter-derived domain and global compiler audit

**Timestamp:** 2026-08-16 17:20 +08:00

## Audit question

Does restoring specimen-parameter-derived material domains remove the previously observed thousands-order compiler problem without changing R10 physics or the common structural workflow?

## Findings

### A. Governance correction is validated

The production domain can be generated from one common source/design-side rule and need not be identical for every specimen.

The current Z0-Z6 generated cores are distinct:

```text
Z0 [-2.326966,+.398162]
Z1 [-2.246565,+.304377]
Z2 [-2.326966,+.398162]
Z3 [-2.241404,+.293969]
Z4 [-2.385927,+.469962]
Z5 [-2.980899,+1.194486]
Z6 [-2.768805,+2.128027]
```

Generation uses geometry, `tc/b`, source `eps0/kappa`, theoretical `Pcr/Pyth`, the common SSSS/halfwave rule and declared generalized-coordinate bounds. No experimental capacity is used.

### B. Historical states are contained without having generated the domains

All previously stored Z0-Z5 diagnostic envelopes and the retained Z6 engineering envelope lie inside the generated domains. This check is performed after domain generation and therefore does not constitute tuning.

### C. The fixed family-wide interval was not the sole source of high order

Using one identical source-fidelity convergence policy on each corrected domain gives first-pass orders:

```text
Z0 1792
Z1 1536
Z2 1792
Z3 1536
Z4 1792
Z5 3072
Z6 3840
```

Thus the former `N=3584` family-wide result was partly influenced by an over-broad common interval, but the deeper issue remains: a **single global lambda-space polynomial** must resolve the narrow R10 sign/tension transitions over a much broader specimen-level reachable interval.

### D. No production Pu is authorized by this gate

The current numbers are material-compiler convergence results only. They do not close structural tractability, same-expression `L`, same-state `KZ`, or a new Z0-Z6 production rerun.

## Audit verdict

```text
PARAMETER_DERIVED_DOMAIN_GOVERNANCE = PASS
DOMAIN_CERTIFICATE_WITH_ZERO_SPATIAL_SAMPLING = PASS
COMMON_SOURCE_FIDELITY_POLICY = PASS_AS_A_DIAGNOSTIC_BASELINE
ONE_GLOBAL_LAMBDA_POLYNOMIAL_AS_LOW_COMPLEXITY_PRODUCTION_GRAMMAR = FAIL
R10_MATERIAL_CHANGE = NOT JUSTIFIED BY THIS GATE
PI_REGULARIZATION = NOT CURRENT MANDATORY NEXT STEP
```

## Required next direction

Reconnect the earlier historical multiscale analytic compiler / source-landmark strategy on these corrected parameter-derived domains. The test must keep a common algorithm across specimens while allowing domain/order outputs to differ as deterministic consequences of specimen parameters.
