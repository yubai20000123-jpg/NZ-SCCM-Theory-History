# TREE DELTA — global R_m, P, R_A no-integral shared master

时间：2026-08-20 18:25 +08:00

## Production integration identity

`Nguyen second-order -> exact globally equivalent NC-M4 positive/negative strain operator -> shared sparse CH/current circuit -> one explicit relative-GKZ master -> R_m, P, R_A`.

## Locked status

- No material law was changed.
- The global operator is statewise identical to CC / TC / CT / TT and removes internal state decomposition only from the integration backend.
- Shared variables = 51.
- Shared polynomial relations = 48.
- Shared Cayley configuration = `A*_(M4,global) in Z^(99 x 155)`.
- Maximum support of any one polynomial relation = 5 monomials.
- All three targets are single numerator-monomial shifts of the same master:
  - `Jaux*sx` -> R_m,
  - `Jaux*sy` -> P,
  - `Jaux*rA` -> R_A.
- `R_m = (2 b ell h/pi^2) RGKZ(A*, beta_m; c | Gamma_phys)`.
- `P = -(2 b h/pi^2) RGKZ(A*, beta_P; c | Gamma_phys)`.
- `R_A = (2 b ell h/pi^2) RGKZ(A*, beta_A; c | Gamma_phys)`.
- No unevaluated spatial integral operator remains in these formal exact results.
- Formal spatial quadrature/material points remain zero.

## Supersession labels

- `61 x 84`: state-split diagnostic pilot; not production global master.
- `87 x 137`: R_m-only unified compiler; superseded by the shared target master.
- `99 x 155`: current production shared R_m/P/R_A master.

## Next unique task

Same-source coefficient differentiation of the `99 x 155` master to produce the nine entries of the limit Jacobian and then the fully expanded determinant equation.