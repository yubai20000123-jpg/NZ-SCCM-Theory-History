# TREE DELTA — R_m integral symbol removed

时间：2026-08-20 18:10 +08:00

## Current route

`Nguyen second-order -> globally equivalent unified NC-M4 operator -> sparse CH/current circuit -> exact relative-GKZ standard function -> R_m(Delta,A,epsilon_m)`.

## New locked facts

- The CC/TC/CT/TT nine-grid operator has an exactly equivalent global form using positive/negative current-strain tensors:
  `Sigma = ft*T(E_+/eps_t0) - fc*[beta(tr(E_+)/eps_t0)+0.16 det C(E_c/eps_c0)] C(E_c/eps_c0)`.
- This is representation-only; no material law or parameter changed.
- It removes internal state-domain decomposition from the integration backend.
- The R_m compiler uses 45 variables and 42 polynomial circuit relations.
- Cayley support: `A*_(M4,Rm) in Z^(87 x 137)`, max relation support = 5.
- The 137 coefficient/monomial columns are machine-readable in `semantic_v2/40_execution/combined/20260820_1810__NZSCCM__RM_UNIFIED_GKZ_ASTAR_137_COLUMNS.csv`.
- Euler exponent vector:
  `nu_m=(1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,2)`.
- GKZ parameter: `beta_m=(-1_42,-nu_m)`.
- Exact final standard-function form:
  `R_m = (2 b ell h/pi^2) RGKZ_(A*_(M4,Rm))(beta_m; c(Delta,A,epsilon_m,b,ell,h,A0,fc,ft,eps_c0,eps_t0) | Gamma_phys)`.
- No uncomputed spatial integral sign remains in the formal R_m result.

## Status correction

`RM_INTEGRAL_SYMBOL_REMOVED_TO_EXPLICIT_RELATIVE_GKZ = PASS`.

This does **not** assert reduction to elementary/Appell/Lauricella functions for generic symbolic parameters.

## Next unique task

Use the same globally unified operator/circuit philosophy to compile `P` and `R_A` to explicit no-integral standard-function forms, then form same-source derivatives and the final limit determinant.