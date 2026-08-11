# GOVERNANCE DECISION — R10A MATERIAL-TARGET INTENT RECONCILIATION

**Date:** 2026-08-11 15:53 +08:00

## Decision

R10A resolves the material-target identity in favor of a local source-preserving regularization.

```text
R10A_MATERIAL_TARGET_INTENT_RECONCILIATION = PASS_DECISION

SELECTED_TARGET
= B_LOCAL_SOURCE_PRESERVING_REGULARIZATION

A_WHOLE_RETAINED_BRANCH_C2_REBUILD
= RETAINED_EXECUTED_REFERENCE_ONLY

STRUCTURAL_Pu_CALIBRATION = NO
```

The decision is based only on source fidelity, minimum material intervention, local material-work preservation, absence of free structural calibration, and compatibility with the retained analytic architecture.

No Case21 or Swartz capacity is used to choose between A and B.

---

## Governing material identity after R10A

The source Foster tensile scalar remains the governing material reference outside source-defined local regularization neighborhoods.

For the future R10A local target,

\[
 u_{local}(t)=u_{src}(t)
\]

must hold exactly outside the frozen regularization interval(s).

Inside each interval \([a_k,b_k]\), the patch must at minimum satisfy source value, first derivative and second derivative matching at both endpoints plus local work equality:

\[
\int_{a_k}^{b_k}u_{local}(t)dt
=
\int_{a_k}^{b_k}u_{src}(t)dt.
\]

This gives seven deterministic constraints. A degree-6 polynomial is the minimum polynomial order capable of satisfying that complete C2 + local-work contract without a free coefficient. The actual patch order may be increased only if a material-only monotonicity/shape/analytic gate requires it; no coefficient may be selected from structural capacity.

The exact patch interval endpoints are not frozen by this decision. They must be derived in R10A1 from the source Foster transition scale/curvature and analytic-compilation requirement only.

---

## Status of prior R10 and R10B

The previously executed whole-branch R10 target and its zero-spatial R10B Case21 result remain valid execution records, but their identity changes to reference baseline:

```text
R10_WHOLE_BRANCH_C2_TARGET
= EXECUTED_REFERENCE_BASELINE

R10B_ZERO_SPATIAL_CASE21_FOR_WHOLE_BRANCH_TARGET
= EXECUTED_REFERENCE_BASELINE
```

They continue to demonstrate that the same multidimensional current-map -> coefficient algebra -> exact complete-halfwave moment -> reinforced limit-root architecture can close numerically.

However, after R10A they must not be represented as the final material target or final production capacity of the selected local source-preserving branch.

The recorded value

\[
P_u=368.31955249587696\ \mathrm{kN}
\]

therefore remains a benchmark for the executed whole-branch R10 target only.

---

## Architecture retained

R10A does not reopen:

- one continuous complete halfwave;
- m=1;
- Nguyen second-order kinematics;
- same U/C/T + CC/TC/TT multidimensional interaction;
- same spectral return;
- Cayley-Hamilton coefficient algebra;
- D15 exact complete-halfwave moments;
- same-expression derivatives;
- reinforcement before root solving;
- zero formal spatial sampling/quadrature/subdomains=1.

The only governing change is the required 1D tensile target to be compiled in the next branch.

---

## Prohibitions after R10A

- do not use Case21 or Swartz Pu to choose patch width, order or coefficients;
- do not retune the former R10 peak `h` to recover the previous Case21 agreement;
- do not modify CC/TC/TT interaction during local scalar construction;
- do not use a global material-energy potential;
- do not preserve the whole-branch R10 target merely because it gave a close Case21 value;
- do not publish historical R10B N48 coefficients as the compiler for the new local target;
- do not start Swartz24 while the active material target has not been locally constructed and recompiled.

---

## Immediate next task

```text
CURRENT_ACTIVE_NEXT_TASK
= R10A1_LOCAL_SOURCE_PRESERVING_PATCH_CONSTRUCTION_AND_MATERIAL_GATE
```

R10A1 must determine the local interval(s), construct the deterministic local patch, execute material-only stress/derivative/shape/work/analytic-quality gates, and either freeze or reject that patch before any structural re-solution.

After R10A1 passes, the subsequent task is a fresh R10B-style analytic recompilation of the newly frozen local target, with a transparent reproducibility contract.

The prior production-stage R11 Swartz24 precheck is deferred until the local target and its zero-spatial Case21 closure are re-established.
