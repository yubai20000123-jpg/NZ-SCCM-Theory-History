# Zhou empirical ultimate-capacity comparator correction

Date: 2026-08-14 14:48 Asia/Tokyo

## Superseding correction

This file supersedes the **ultimate-capacity interpretation** of the raw `Pyth` comparison in:

- `20260814_1405__NZSCCM__ZHOU_TABLE5_1__BS_TS_SCREEN_AND_FORMULA_COMPARISON__VALIDATION.md`
- `20260814_1405__NZSCCM__ZHOU_TABLE5_1__SCREEN_AND_COMPARISON__EXECUTION_CHECKPOINT.md`

Those earlier arithmetic values are retained as historical same-object section-strength diagnostics, but `Pyth` is no longer treated as Zhou's ultimate-capacity prediction.

## Correct Zhou identity

Zhou defines the axial stable/ultimate bearing capacity by

\[
\boxed{P_u=\varphi_N P_{yth}}.
\]

For the four-edge simply-supported axial-compression case, the proposed stability curve is Zhou Eqs. (5-87)-(5-88):

\[
\varphi_N=1,\qquad \lambda_n\le0.55,
\]

\[
\varphi_N=\frac{1}{\Phi+\sqrt{\Phi^2-\lambda_n^2}},\qquad \lambda_n>0.55,
\]

with

\[
\Phi=0.454+0.192\lambda_n+0.416\lambda_n^2,\qquad \lambda_n\le1.0,
\]

\[
\Phi=-0.140+1.387\lambda_n-0.186\lambda_n^2,\qquad \lambda_n>1.0.
\]

Therefore the comparison required for a final NZ-SCCM ultimate root is

\[
\boxed{P_{u,NZ}\;\text{vs}\;P_{u,Zhou,emp}=\varphi_N(\lambda_n)P_{yth}}.
\]

## Status of the previous numeric value

For the previously reduced two-faceplate object:

```text
Pyth_reduced = 39.2928 MN
```

remains a valid replay of Zhou's cross-section strength expression on that reduced section, but its identity is now:

```text
SECTION_STRENGTH_BASELINE_ONLY
NOT_ZHOU_ULTIMATE_CAPACITY
```

The preceding NZ value `26.1085 MN` also remains a diagnostic branch-peak neighbourhood, not a frozen production `Rq=0 + L=0` root.

## Numeric empirical Pu gate

A numerical `phi_N` and `Pu_Zhou,emp` are not released in this correction because the source-exact definition of Zhou's `lambda_n` has not yet been recovered into the current execution evidence. The project will not silently assume a normalized-slenderness formula even if it resembles standard forms.

Required next evidence:

```text
1. recover exact Zhou definition of lambda_n;
2. evaluate its Pcr/reference quantities on exactly the same structural object;
3. compute phi_N from Eq.5-87/5-88;
4. compare final NZ production Pu against phi_N*Pyth.
```

## Locked status

```text
ZHOU_RAW_PYTH_AS_ULTIMATE_COMPARATOR = RETIRED
ZHOU_PYTH_REDUCED = RETAINED_SECTION_STRENGTH_BASELINE
ZHOU_EMPIRICAL_ULTIMATE_CURVE = ACTIVE
ZHOU_NUMERIC_EMPIRICAL_PU = PENDING_EXACT_lambda_n_SOURCE_RECOVERY
NO_ASSUMED_lambda_n = PASS
```
