# NZ-SCCM — direct unfiltered three-variable limit solve diagnostic

**Date:** 2026-08-20 11:42 +08  
**Identity:** USER-REQUESTED DIRECT SOLVE / NO BRANCH-APPLICABILITY FILTER

## 1. User instruction

The user explicitly requested to stop debating CC/TC/TT applicability and directly solve the already integrated three-variable equations once to see the numerical result.

Accordingly, this diagnostic intentionally uses the full-domain analytically integrated branch continuations as one algebraic superposition:

- full-domain CC contribution,
- full-domain TC-P6 contribution,
- full-domain TT affine contribution,

with no spatial CC/TC/TT selector and no material-state admissibility check during the solve.

This is a deliberate algebraic diagnostic, not a claim that simultaneous physical activation of all three branches is a final constitutive rule.

## 2. General equations used

The structural unknowns remain only

\[
\Delta,\qquad A,\qquad \varepsilon_m.
\]

The already completed general-rectangle integrations provide

\[
P=P^{CC}_{full}+P^{TC}_{full}+P^{TT}_{full},
\]

\[
R_A=R_A^{CC}_{full}+R_A^{TC}_{full}+R_A^{TT}_{full}=0,
\]

\[
R_m=R_m^{CC}_{full}+R_m^{TC}_{full}+R_m^{TT}_{full}=0.
\]

The limit condition is the three-variable equilibrium-path determinant

\[
\mathcal L=
P_{,\Delta}(R_{A,A}R_{m,m}-R_{A,m}R_{m,A})
-P_{,A}(R_{A,\Delta}R_{m,m}-R_{A,m}R_{m,\Delta})
+P_{,m}(R_{A,\Delta}R_{m,A}-R_{A,A}R_{m,\Delta})=0.
\]

No spatial quadrature was used in evaluating P, R_A or R_m: all three branch ledgers had already been fully analytically integrated over x,y,z.

## 3. Numerical substitution for this one solve

To obtain a concrete numerical check, the known Case21 material/geometric numbers were substituted only after the general rectangular formulas had been integrated:

- b = 1220 mm
- ell = 1220 mm
- t = 19.30 mm
- A0 = 3.05 mm
- nu = 0.18
- fc = 21.23 MPa
- E0 = 20321 MPa
- eps0 = 0.00209
- ft = 0.10 fc
- alpha1 = 10
- alpha2 = 0.3

For numerical conditioning only, the solver internally used d=Delta/ell, q=A/b and r=eps_m/eps0. These are solver scalings only; the reported physical unknowns remain Delta,A,eps_m.

## 4. Direct three-equation solution

Solving

\[
R_A=0,\qquad R_m=0,\qquad \mathcal L=0
\]

converged from multiple nearby initial guesses to the same root:

\[
d=0.0013011865,
\]

\[
q=0.0167627340,
\]

\[
r=0.9337015454.
\]

Therefore

\[
\boxed{\Delta_u=1.5874475341\ \mathrm{mm}}
\]

\[
\boxed{A_u=20.4505354847\ \mathrm{mm}}
\]

\[
\boxed{\varepsilon_{m,u}=0.00195143623}
\]

and the direct algebraic load is

\[
\boxed{P_u=510.333747914\ \mathrm{kN}}.
\]

## 5. Residual and limit verification

At the root:

- R_A = 1.91e-11 in the assembled force residual,
- R_m = 7.34e-7 in the assembled membrane residual,
- scaled determinant residual = 1.77e-11.

The 2x2 equilibrium Jacobian with respect to (q,r) is non-singular at the root. Implicit differentiation gives

\[
\frac{dP}{dd}\approx1.8\times10^{-5}\ \mathrm{N},
\]

i.e. numerically zero at the reported scale.

Independent neighboring equilibrium solves give:

- at d=d* - 1e-7: P = 510.333601944 kN,
- at d=d*: P = 510.333747914 kN,
- at d=d* + 1e-7: P = 510.333599570 kN.

The local second derivative is negative (about -2.94e13 N per d^2), confirming this root is a local load maximum along the assembled equilibrium branch.

## 6. Algebraic contribution ledger at the root

The full-domain branch continuations contribute to P as:

- TC-P6: +276.700201601 kN
- CC: +323.319430917 kN
- TT affine extension: -89.685884603 kN

Sum:

\[
276.700201601+323.319430917-89.685884603
=510.333747914\ \mathrm{kN}.
\]

For R_A:

- TC: -4341.047623
- CC: -323.858130
- TT: +4664.905753

which cancels to numerical zero.

For R_m:

- TC: +4.84387887e5
- CC: +2.11982235e7
- TT: -2.16826114e7

which also cancels to numerical zero.

## 7. Status interpretation

This execution proves a narrow but important point:

```text
FULLY_INTEGRATED_THREE_VARIABLE_SYSTEM  = DIRECTLY_SOLVABLE
DIRECT_NUMERICAL_ROOT                    = FOUND
LOCAL_LIMIT_MAXIMUM                      = CONFIRMED
DIAGNOSTIC_LOAD                          = 510.333747914 kN
```

The result is intentionally an unfiltered algebraic superposition because that is exactly what the user requested for this diagnostic. It must not silently replace later constitutive decisions without explicit user acceptance.
