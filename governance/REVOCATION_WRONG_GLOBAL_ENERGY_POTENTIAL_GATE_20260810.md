# REVOCATION — WRONG GLOBAL ENERGY-POTENTIAL GATE INTERPRETATION

Date: 2026-08-10

## Decision

The execution recorded as `NC_ENERGY_POTENTIAL_AND_D15_FEASIBILITY_GATE = FAIL__STOP_AT_GATE` tested the wrong mathematical object for the user's intended route and is therefore **revoked as a governing blocker**.

The numerical calculations in that gate remain historical evidence only: they show that a single low-order global energy polynomial over the entire scalar strain domain is a poor representation. They do **not** show that the intended NZ-SCCM scalar-smoothing route fails.

```text
NC_GLOBAL_ENERGY_POTENTIAL_GATE = REVOKED_AS_WRONG_ROUTE_TEST
D15_EXACT_MOMENT_ENGINE = RETAINED
CASE21_ZERO_SPATIAL_ANALYTIC_ROUTE = RETAINED
```

## Correct route restored

The intended architecture is not

```text
full multidimensional constitutive law
 -> replace everything by one global energy potential
 -> differentiate potential
 -> structural integration
```

It is

```text
multidimensional/current constitutive relation
 -> principal/equivalent scalar coordinates lambda_+, lambda_-
 -> one-dimensional scalar master material functions
 -> smooth only the narrow scalar peak/kink/boundary-layer using a material-energy rule
 -> reinsert the smoothed scalar function into the existing low-parameter multidimensional interaction/spectral reconstruction
 -> Nguyen continuous second-order strain field
 -> zero-spatial analytic/D15 target contraction
 -> P(D,q), Rq(D,q) and same-expression derivatives
 -> solve Rq=0 and L=0
 -> Pu
```

## Why this correction is required

Historical G19 had already localized the unresolved NC problem to the **one-dimensional cracking/peak boundary layer**, not to the two-dimensional interaction surface. Its governing conclusion was that the next work should regularize the one-dimensional scalar function rather than increase 2D interaction degree.

The explicit Case21 zero-spatial analytic-series execution later demonstrated that the scalar-material/current-map -> continuous kinematics -> analytic moment contraction -> equilibrium/limit-root chain is calculable with formal spatial sampling and quadrature equal to zero. The remaining strict-certificate issue did not invalidate the central analytic solution.

## Energy rule location

Energy is used only to select/regularize the one-dimensional scalar patch. A generic admissible condition is

\[
\int_{\lambda_a}^{\lambda_b} u_{smooth}(\lambda)\,d\lambda
=\eta_E\int_{\lambda_a}^{\lambda_b}u_{source}(\lambda)\,d\lambda,
\]

combined with the required physical anchors, monotonicity and derivative continuity. The rest of the multidimensional current-map architecture is not replaced by a global material potential.

## Prohibitions retained

- no spatial Gauss/Simpson/adaptive quadrature in the formal operator;
- no material-point grid;
- no moving spatial TT/TC/CC cells;
- no whole-structure P/R/U surface fitted from spatial numerical integration;
- no large bank of free material coefficients;
- no Case21/Swartz Pu calibration of the scalar smoothing;
- no 2D interaction-degree escalation to repair a 1D scalar kink;
- no finite-difference production derivatives.

## Correct next gate

```text
CURRENT_RECOMMENDED_NEXT_TASK
= R10_1D_ENERGY_SMOOTHING_REINSERTION_CASE21
```

Before any Swartz24 batch, R10 must:

1. recover the one-dimensional scalar master branch used by the accepted/current NC operator;
2. identify the narrow peak/kink interval to be regularized;
3. construct a low-parameter analytic smoothing using material energy and physical anchors only;
4. verify scalar stress and derivative behavior;
5. reinsert that scalar function into the existing multidimensional interaction/spectral current map without changing the interaction architecture;
6. pass a material-surface audit;
7. reuse the proven zero-spatial analytic/D15 Case21 chain;
8. solve the reinforced Case21 equilibrium/limit equations with steel embedded before root solving;
9. compare against prior Case21 analytic results and experiment only after the new material target is frozen.
