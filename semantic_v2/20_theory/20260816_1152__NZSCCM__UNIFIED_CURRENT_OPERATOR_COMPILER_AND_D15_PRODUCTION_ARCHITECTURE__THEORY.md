# NZ-SCCM unified current-operator compiler and D15 production architecture

**Timestamp:** 2026-08-16 11:52 +08:00  
**Identity:** CURRENT PROJECT-WIDE ARCHITECTURE CONTRACT

## 1. Purpose

The solver must not become a collection of specimen-specific methods. Ordinary concrete, UHPC, rebar and steel shell are physical modules plugged into one calculation architecture.

The same execution graph is required for:

- NC + rebar;
- NC + steel shell;
- UHPC + rebar;
- UHPC + steel shell.

## 2. Generic interfaces

### 2.1 Material interface

Each continuum material family supplies only its source current operator

\[
\boldsymbol\sigma=\mathcal M_{\theta}(\boldsymbol\varepsilon),
\qquad
\mathbf D=\partial\mathcal M_{\theta}/\partial\boldsymbol\varepsilon,
\]

with source parameters `theta`.

The compiler accepts this source operator through a common interface and produces a finite analytic representation with explicit source-value and source-tangent error metrics. The compiler is not allowed to know the specimen's experiment, desired Pu, Zhou/Winter result, or error sign.

### 2.2 Structural phase interface

Each phase contributes the same pair of generalized analytic objects:

\[
P_p(D,q,\mathbf a),\qquad R_{q,p}(D,q,\mathbf a),
\]

and consistent derivatives/tangent terms. Rebar and steel shell differ only in their phase kinematics/volume geometry and steel constitutive law; they do not change the parent root topology or integration engine.

Total quantities are assembled additively:

\[
P=\sum_pP_p,\qquad R_q=\sum_pR_{q,p}.
\]

## 3. Common structural backbone

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order kinematics
theoretical four-edge simply-supported production boundary where applicable
source current material operator
universal analytic compiler
Cayley-Hamilton / approved finite matrix lift
moment-first General-D15 exact moments
zero formal spatial numerical integration
common P,Rq,L / connected-branch root logic
first admissible +->- ultimate-load maximum
same-branch tangent/stability audit
```

No material family or specimen is allowed to substitute a different structural integration method.

## 4. Order is an implementation parameter, not a separate theory

The compiler order `N` is analogous to an algebraic truncation/representation resolution. It is not allowed to define different theories case by case.

The universal rule is:

```text
same compiler architecture
+ same source-fidelity metrics
+ same deterministic convergence/order rule
+ same domain policy
= same calculation method
```

Therefore:

- `N=48` is a historical/current candidate resolution, not an inviolable project identity;
- arbitrary per-specimen manual `N` changes are prohibited;
- a material family may require a different converged `N` from another material family because the source functions differ;
- once a material-family compiler/domain is frozen, all specimens using that material family reuse it, regardless of whether the structural steel phase is rebar or shell.

## 5. Universal order-selection contract to be frozen next

The next gate must turn the following into explicit numerical pass/fail thresholds and a reproducible algorithm:

1. declare a conservative material-family source domain;
2. generate an analytic compiler at candidate order `N` using the common compiler family;
3. evaluate source operator value error and first-tangent error using material-coordinate-only coefficient/audit operations;
4. increase `N` by the same deterministic rule until both source metrics pass;
5. freeze `(compiler architecture, N, domain)` for that material family;
6. run structural production blindly;
7. certify the continuous reachable material spectrum remains inside the frozen family domain;
8. if it exits, enlarge the family domain and repeat for the **whole family**, not only for the offending specimen.

No experiment or structural comparator is allowed in steps 1–5.

## 6. NC and UHPC distinction

The same compiler architecture does not mean the same constitutive formula.

For NC:

```text
source operator = frozen R10 current operator
```

For UHPC:

```text
source operator = future/source-frozen UHPC multidimensional current operator
```

UHPC may have different physical parameters, transition scales and therefore a different converged compiler order. This is still the same method if the compiler algorithm, fidelity contract and structural backend are unchanged.

The current UHPC branch does not yet contain a final production source operator, so no UHPC order is frozen by this architecture document.

## 7. Rebar and shell distinction

Rebar and shell are structural phase adapters.

They may have different exact strain projections, thickness integration identities and yield-cap algebra, but both must deliver finite analytic `P_p,Rq_p` contributions to the same General-D15/root framework. A steel phase is not allowed to trigger a different concrete/UHPC compiler.

Consequently:

```text
NC+rebar and NC+shell -> same frozen NC material compiler
UHPC+rebar and UHPC+shell -> same frozen UHPC material compiler
```

## 8. Status of earlier results

- user-accepted Z6 AR2 `Pu=51.30 MN` remains retained as an accepted calculation result;
- challenged 10:43 Z0-Z5 results remain retracted pending recalculation;
- 11:34 fixed-global-N48 failure remains useful representation-capacity evidence;
- 11:31 hard project-wide N48 lock is superseded by this universal-workflow governance;
- 11:10 multirate orders are not promoted; they remain diagnostic only because they were introduced without the now-required universal order-selection contract.

## 9. Current next gate

`UNIFIED_CURRENT_OPERATOR_ANALYTIC_COMPILER_ARCHITECTURE_NC_UHPC_REBAR_SHELL_GATE`

No new Z0-Z5 Pu is released before this common compiler contract is frozen and demonstrated on NC R10.
