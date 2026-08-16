# NZ-SCCM — unified material-compiler / structural-solver workflow across NC, UHPC, rebar and steel shell

**Timestamp:** 2026-08-16 11:52 +08:00  
**Status:** CURRENT GOVERNANCE LOCK / supersedes the over-literal fixed-N48 hard lock as project-wide compiler governance

## User correction

The project objective is **not** to force polynomial order 48 for its own sake. The governing requirement is that the calculation workflow remain the same across specimens and across the four intended material/section combinations:

1. ordinary concrete + reinforcement;
2. ordinary concrete + steel shell;
3. UHPC + reinforcement;
4. UHPC + steel shell.

A different specimen must not trigger a bespoke calculation method, bespoke material surrogate family, bespoke spatial integration scheme, or specimen-tuned solver.

## Universal production architecture

The common architecture is

```text
source material current operator M(theta; epsilon)
-> source-only analytic compiler
-> matrix/spectral lift (Cayley-Hamilton or the same approved finite matrix identity)
-> continuous Nguyen second-order one-complete-halfwave strain field
-> moment-first General-D15 exact structural moments
-> phase assembly (concrete/UHPC + rebar or shell/web)
-> common generalized resultants P, Rq and same-expression derivatives/tangent
-> connected branch solution
-> first admissible +->- ultimate-load maximum / same-branch stability audit
```

Formal structural spatial identity remains

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

No Gauss/Simpson/adaptive quadrature, spatial collocation, material-point grid, panel cells, or specimen-specific surrogate is permitted in formal production.

## What may differ and what may not

### May differ because it is physical input

- NC versus UHPC source constitutive/current operator and its physical parameters;
- steel reinforcement versus finite-thickness steel-shell phase geometry and constitutive parameters;
- panel geometry, reinforcement ratio, shell thickness, yield strength, initial imperfection and halfwave length;
- the numerical polynomial/order parameter **only if it is selected by the same source-only convergence rule defined below**, not by specimen response.

### Must remain the same calculation method

- compiler family / analytic representation architecture;
- source-fidelity metrics and pass/fail rules;
- order-selection algorithm;
- material-domain declaration/enlargement rule;
- matrix lift;
- Nguyen strain construction;
- General-D15 moment engine;
- generalized residual / tangent definitions;
- branch/root/peak selection rules;
- zero-spatial-integration governance.

## Order governance — corrected

```text
POLYNOMIAL_ORDER_IS_NOT_A_THEORY_IDENTITY
N48_IS_NOT_A_PROJECT-WIDE_HARD_REQUIREMENT
CASE_BY_CASE_MANUAL_ORDER_TUNING = PROHIBITED
```

The 11:31 hard statement "no order change without explicit user authorization" is superseded as a project-wide compiler principle.

The correct rule is:

1. define one source-only fidelity contract, independent of experiment, Zhou/Winter, desired Pu, or specimen error;
2. apply the **same deterministic order-selection/convergence procedure** to the material operator family;
3. freeze the resulting compiler for that material family/domain;
4. reuse that same compiler unchanged for all specimens using that material family, whether paired with rebar or steel shell;
5. if a later specimen lies outside the frozen material domain, enlarge the **family domain and recompile the family consistently**; do not create a one-off specimen compiler.

Thus NC may ultimately require a different numerical order from UHPC because their source functions differ, but the **algorithm deciding that order is identical**. Likewise, NC+rebar and NC+steel-shell must use the same NC current-material compiler.

## Material-domain governance

The compiler domain is a material-family contract, not a fitted specimen property.

```text
SPECIMEN_ID_IN_COMPILER_OBJECTIVE = NO
EXPERIMENT_IN_COMPILER_OBJECTIVE = NO
ZHOU_WINTER_IN_COMPILER_OBJECTIVE = NO
DESIRED_Pu_IN_COMPILER_OBJECTIVE = NO
```

The domain must be declared from source-material validity plus a conservative equation-derived reachable envelope under a common self-consistency rule. If an admissible calculation exits the domain, the remedy is family-level domain enlargement and recompilation under the same algorithm.

## Interpretation of prior fixed-N48 diagnostics

The 11:34 result remains valid evidence:

```text
single global degree-48 C1 polynomial per primitive
+ current broad NC transition range
= insufficient source/current-map fidelity
```

But its consequence is **not** "invent a special Z0-Z5 multiscale method" and is **not** "N48 must be retained forever".

Its correct consequence is:

```text
THE_UNIVERSAL_COMPILER_ARCHITECTURE_MUST_BE_CHOSEN_SO_THAT_THE_SAME_SOURCE_FIDELITY_CONTRACT_CAN_BE_MET_FOR_NC_AND_LATER_UHPC_WITHOUT_SPECIMEN-SPECIFIC_METHOD_CHANGES
```

## Current next gate

`UNIFIED_CURRENT_OPERATOR_ANALYTIC_COMPILER_ARCHITECTURE_NC_UHPC_REBAR_SHELL_GATE`

This gate must, before any new Z0-Z5 Pu is released:

1. define one compiler architecture/interface applicable to a generic current operator `M(epsilon;theta)`;
2. define one source-only value+tangent fidelity contract;
3. define one deterministic order/domain convergence policy;
4. demonstrate the architecture on frozen NC R10 without specimen-response tuning;
5. show that the same interface is directly reusable for UHPC once its source current operator is frozen;
6. show that rebar/shell are phase adapters only and do not change the material compiler or structural D15/root architecture;
7. retain zero structural spatial numerical integration.

Only after this architecture is frozen may Z0-Z5 be recalculated and later NC+rebar / UHPC+rebar / UHPC+shell be executed through the same production path.
