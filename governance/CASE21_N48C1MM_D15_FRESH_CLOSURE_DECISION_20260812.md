# CASE21 N48-C1/MM + D15 fresh closure decision — 2026-08-12

## Decision identity

This decision records a **fresh updated-compiler Case21 calculation**. It does not overwrite or use any earlier Case21 computed load, root, path, FE/Gauss history, or experiment-derived target.

```text
CASE21_N48C1MM_D15_FRESH_BLIND = PASS_ENGINEERING
R10_MATERIAL_TARGET = FROZEN
MATERIAL_COMPILER_ORDER = 48
U_COMPILER = N48-C1
C_COMPILER = N48-C1
T7_COMPILER = N48-C1
T_COMPILER = N48-C1-CONSTRAINED-MINIMAX
HISTORICAL_CASE21_COMPUTED_VALUES_USED = NO
HISTORICAL_CASE21_ROOTS_OR_PATHS_USED = NO
HISTORICAL_GAUSS_HISTORY_USED = NO
EXPERIMENT_USED_DURING_SOLVE = NO
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_SPATIAL_SUBDOMAINS = 1
```

## Fresh source inputs

\[
b=\ell=1220\ {\rm mm},\quad t_p=19.30\ {\rm mm},
\]
\[
f_c=21.23\ {\rm MPa},\quad E_0=20321\ {\rm MPa},\quad
\varepsilon_0=0.00209,\quad \nu=0.18,
\]
\[
q_0=1/400.
\]

Total two-way reinforcement ratio is 0.75%, split equally between the two directions; one layer is at the mid-plane. Steel parameters are \(E_s=200000\) MPa, \(\varepsilon_y=0.00265\), \(f_y=530\) MPa.

## Fresh compiler and certificates

The material compiler interval was fixed before solving as

\[
\boxed{\lambda\in[-1.15,0.12]}.
\]

The final continuous spectral certificate is

\[
-0.874981134\le\lambda\le0.092641134,
\]

therefore

```text
CONTINUOUS_SPECTRAL_CERTIFICATE = PASS
COMPILER_DOMAIN_CERTIFICATE = PASS
```

The final continuous steel-strain bound is

\[
\max|\varepsilon_s|=0.001635091<0.00265,
\]

therefore

```text
STEEL_BRANCH = ELASTIC
```

## Fresh blind theoretical result

\[
D_u\approx0.78234,\qquad
q_u\approx0.00177047,
\]
\[
\boxed{P_{u,th}\approx365.61\ {\rm kN}}.
\]

At the reported state,

\[
R_q=1.315371\times10^{-2}\ {\rm kN\,mm},
\]

with normalized equilibrium residual

\[
2.273568\times10^{-5}.
\]

The same-expression limit diagnostic gives

\[
L_{norm}=-2.350613\times10^{-4},
\]

and along the equilibrium path

\[
(dP/dD)_{R_q=0}=-0.068049\ {\rm kN}.
\]

Thus

```text
Rq_EQUILIBRIUM = PASS_ENGINEERING
LIMIT_L = PASS_ENGINEERING
```

The result is reported to approximately 0.1 kN engineering precision because the generalized-work equilibrium contains cancellation of two terms of roughly 289 kN·mm and the coefficient-convolution backend removes only floating coefficient noise.

## Experiment comparison — attached after blind freeze

Only after the blind result was committed was the Swartz Case21 experimental failure load attached:

\[
P_{f,exp}=82.8\ {\rm kip}=368.312750\ {\rm kN}.
\]

The fresh comparison is

\[
\frac{P_{u,th}}{P_{f,exp}}=0.992655769,
\]

\[
\boxed{\text{signed error}=-0.734423\%}.
\]

```text
EXPERIMENT_COMPARISON_AFTER_BLIND_FREEZE = COMPLETE
STRUCTURAL_CALIBRATION = NO
```

## Canonical evidence

- `current/results/NZ_SCCM_CASE21_N48C1MM_D15_FRESH_BLIND_RESULT_20260812.md`
- `current/results/NZ_SCCM_CASE21_N48C1MM_D15_FRESH_COEFFICIENTS_20260812.csv`
- `current/results/NZ_SCCM_CASE21_N48C1MM_D15_FRESH_FULL_CALCULATION_20260812.md`
- `current/results/NZ_SCCM_CASE21_N48C1MM_D15_FRESH_THEORY_VS_EXPERIMENT_20260812.md`
- `current/workflows/NZ_SCCM_CASE21_N48C1MM_D15_BLIND_AUDIT_INPUT_20260812.md`
- `current/workflows/NZ_SCCM_CASE21_N48C1MM_D15_BLIND_AUDIT_PROMPT_20260812.txt`

The blind-result commit precedes the experiment-comparison commit in repository history.
