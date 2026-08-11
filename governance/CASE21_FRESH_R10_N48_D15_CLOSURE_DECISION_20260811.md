# GOVERNANCE DECISION — CASE21 FRESH R10 → N48 → D15 CLOSURE

**Date:** 2026-08-11

## Decision

The fresh Case21 calculation documented in

- `current/theory/NZ_SCCM_CASE21_FRESH_R10_N48_D15_CLOSURE_20260811.md`
- `current/theory/NZ_SCCM_CASE21_FRESH_R10_N48_D15_CLOSURE_results.json`

is accepted as the current calculation closure of the paper-style R10 → N48 → D15 theory chain.

The calculation obeys:

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = YES
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
MATERIAL_COMPILER_ORDER = 48
HISTORICAL_CASE21_COMPUTED_RESULTS_USED = NO
FINAL_NUMERICAL_COMPARISON = EXPERIMENT_ONLY
```

The resulting fresh limit state is

\[
D_u\approx0.835918,\qquad
q_u\approx0.00178979,
\]

\[
P_c\approx337.60174\ \mathrm{kN},\qquad
P_s\approx30.58760\ \mathrm{kN},
\]

\[
\boxed{P_u\approx368.18934\ \mathrm{kN}}.
\]

Total amplitude equilibrium is closed to approximately

\[
R_q\approx2.3\times10^{-12}\ \mathrm{kN\,mm},
\]

and the same-expression limit determinant has normalized residual approximately

\[
4.4\times10^{-9}.
\]

The only post-calculation comparison is to the experimental Case21 failure load:

\[
P_{f,exp}=368.31275\ \mathrm{kN},
\]

giving

\[
\frac{P_u-P_{f,exp}}{P_{f,exp}}\times100\%\approx-0.0335\%.
\]

## Dimensional/conjugacy clarification

For direct axial force, the governing force expression is

\[
P_c=-\frac{f_cb t_p}{2\pi^2}\mathscr D[S_{yy}],
\]

which is equivalent to using the complete-halfwave volume integral divided by \(\ell\).

For generalized amplitude work, physical stress is conjugate to normalized physical strain

\[
\mathbf e=\frac{\mathbf E}{\varepsilon_0}
=(1+\nu)\mathbf X-\nu\operatorname{tr}(\mathbf X)\mathbf I,
\]

so the formal work density is

\[
Q_q=\mathbf S:\mathbf e_{,q}.
\]

These are notation/dimensional corrections to the explanatory derivation; they do not change the R10 material target, N48 compiler, Nguyen kinematics, or D15 exact-moment architecture.

No historical computed Case21 result is admissible as an input, verification target, root guide, or calibration quantity for this closure.
