# NZ-SCCM — kx/ky 与 regression 术语澄清 R01

**Date:** 2026-08-30  
**Status:** `TERMINOLOGY CLARIFICATION / NO MODEL CHANGE / MAIN UNCHANGED`

## 1. kx, ky

R02 local shape:

\[
\phi(\xi,\eta)=(1-\cos k_x\xi)(1-\cos k_y\eta).
\]

For one complete local cell:

\[
\boxed{k_x=2\pi/L_x,\qquad k_y=2\pi/L_y.}
\]

They are geometric wave numbers with unit mm^{-1}. They are not empirical coefficients, not fitted material parameters, and not calibrated from FEM/test Pu.

If an integer number m of local waves is used over a longer physical length a_l, the same identity can be written

\[
k_x=2m\pi/a_l.
\]

## 2. Meaning of regression

`R02 regression`, `LL regression`, or `source regression` in the recent audit means **software/theory regression test**:

> Run the new derivation/backend on the same frozen geometry and verify that it returns the already-accepted old result.

It does NOT mean statistical regression/fitting.

Example BH032:

\[
L_x=360\,\mathrm{mm}
\Rightarrow
k_x=2\pi/360=0.01745329252\,\mathrm{mm}^{-1}.
\]

\[
L_y=355.5555556\,\mathrm{mm}
\Rightarrow
k_y=0.01767145868\,\mathrm{mm}^{-1}.
\]

Using these purely geometric wave numbers in the independently derived exact LL Airy energy gives

\[
K_A^{Airy}=1.58478790282955\times10^{-8}\,\mathrm{mm}^{-4},
\]

identical to the frozen R02 value. That equality is the regression PASS.

The preferred wording going forward is:

```text
geometric wave number kx, ky
exact-source / frozen-R02 consistency regression test
```

Avoid the ambiguous phrase `kx, ky source regression coefficient`.
