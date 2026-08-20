# NZ-SCCM semantic tree delta — full strain-only operator expansion result

**Date:** 2026-08-20 11:24 +08

## New theory audit

- `semantic_v2/20_theory/20260820_1124__NZSCCM__GENERAL_RECTANGLE__FULL_STRAIN_ONLY_OPERATOR_EXPANSION_AND_SELECTOR_AUDIT.md`
  - status: ACTIVE THEORY AUDIT
  - purpose: fully eliminate stress symbols from the general rectangular-plate CC/TC/TT operator and determine what actually remains.

## Corrected frontier

```text
stress symbols                    -> eliminated
stress-defined regions            -> none
CC branch internal algebra        -> finite polynomial
TT branch internal algebra        -> finite polynomial / affine for retained segment
TC P6 branch internal algebra     -> finite polynomial, theta-free
structural variables              -> (Delta,A,epsilon_m)
general rectangle                 -> b,ell independent
```

If separate CC/TC/TT laws are retained, the remaining full-domain object is the **strain-state selector**:

```text
V = (epsilon_x epsilon_y - gamma_xy^2/4)/epsilon0^2
U = (epsilon_x+epsilon_y)/epsilon0
TC: V<0
CC: V>0 and U<0
TT: V>0 and U>0
```

This is not a stress-region condition. It is a constitutive branch selector expressed entirely through current strains.

## Current exact status

```text
FULL_STRESS_ELIMINATION                         = PASS
THETA_ELIMINATION                               = PASS
BRANCH_POLYNOMIAL_INTEGRABILITY                 = PASS
THREE_VARIABLE_LIMIT_SYSTEM_DEFINITION          = PASS
GLOBAL_ONE_POLYNOMIAL_FIXED_DOMAIN_OPERATOR     = NOT YET ESTABLISHED
REMAINING_REASON                                = STRAIN-STATE SELECTOR IF BRANCHES REMAIN SEPARATE
SELECTOR_ANALYTIC_INTEGRABILITY                 = NOT YET PROVED IMPOSSIBLE
```

Do not describe the remaining issue as a moving 'stress region'.
