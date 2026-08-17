# NZ-SCCM — Unified end-to-end theory chain canonical lock

**Timestamp:** 2026-08-17 14:42 +08:00  
**Status:** CONTROLLING CANONICAL GOVERNANCE

This file records the user's complete end-to-end formulation and supersedes interpretations that over-amplify any isolated intermediate correction into a new project route.

## Canonical chain

The production theory is one continuous chain:

```text
specimen / panel geometry and material inputs
 -> geometry-specific analytical boundary / complete-halfwave definition
 -> ONE unified physical target material operator
      ordinary concrete: frozen R10
      UHPC: one unified UHPC current material operator of the same theoretical status
 -> N48-prototype convergent analytic material series
      N48 is the prototype / refinement quantum, not a permanently fixed single degree
      the conceptual material representation may be an infinite convergent series
      production uses a finite partial sum after source/target convergence
 -> compose with Nguyen second-order complete-halfwave kinematics
 -> include membrane-stress redistribution in the same continuous field
 -> include the full directional consistent tangent stiffness from the same current material operator
 -> exact multiple structural integration
      every retained series term has a finite analytic integral
      sum/integration is contracted to finite converged target functionals
 -> General-D15 exact-moment evaluation / finite integral solution
 -> solve the coupled nonlinear equilibrium + tangent/limit equations
 -> obtain ultimate load Pu
 -> only after the solve, compare to the correct external reference
```

## Geometry and boundary come first

The analytical domain, halfwave length, admissible membrane redistribution and boundary functions are determined from the actual specimen/panel geometry and boundary conditions before material compilation.

The one-complete-halfwave rule means:

```text
physical panel may contain multiple repeated halfwaves
formal calculation domain = one physically complete representative halfwave
repeated halfwaves are not independent spatial subdomains
```

For Z6:

```text
a = 24000 mm
b = 12000 mm
m* = 2
ell = 12000 mm
```

For Case21, use its own geometry-defined complete halfwave.

## Unified target material operator

The physical material law is not regenerated for each geometry.

Ordinary concrete:

```text
M_NC = frozen R10 current material operator
```

UHPC:

```text
M_UHPC = one unified UHPC current material operator
```

Geometry changes the strain-state domain on which the operator must be represented; it does not create a new material law.

## N48 prototype means convergent series, not literal fixed N48

N48 is the successful prototype architecture for turning the source material operator into an analytic coefficient representation compatible with exact structural moments.

The intended generalized representation is conceptually

\[
\mathcal M(\varepsilon)=\sum_{n=0}^{\infty} \mathcal M_n(\varepsilon),
\]

with a convergent source representation on the geometry-certified material domain.

Production evaluates a finite partial sum

\[
\mathcal M^{(N)}=\sum_{n=0}^{N}\mathcal M_n
\]

when the actual structural target functionals and required tangents have converged to engineering accuracy.

Therefore:

```text
N48 = prototype / base refinement block
N48 literal fixed degree for every panel = NO
blind global N escalation = NO
convergent material-series refinement = YES
```

Different scalar primitives may use different orders or factorized expansions if this improves source-consistent convergence. No order is selected by matching experiment, Zhou or Winter.

## Membrane stress redistribution is inside the operator chain

Membrane redistribution is not a post-processing correction and is not optional in the current production theory.

It modifies the continuous strain field before material evaluation:

\[
\varepsilon=\varepsilon(D,q,\text{membrane coordinates};X,Y,\zeta).
\]

The membrane coordinates must satisfy the geometry/boundary-derived admissible equilibrium representation. They may not be set to zero by default, and they may not be released as arbitrary independent coordinates without a mechanics/boundary justification.

The same current material operator is then evaluated on this redistributed strain field.

## Directional consistent tangent stiffness is mandatory

The theory must retain the full directional consistent current tangent from the same material operator:

\[
\mathbf D_t=\partial\boldsymbol\sigma/\partial\boldsymbol\varepsilon.
\]

This tangent participates in the coupled equilibrium/limit/stability equations. A scalar secant modulus, isotropic replacement, or independently fitted stiffness is not an admissible substitute.

The material-value representation and its tangent representation must converge consistently.

## Multiple integration and D15

After material-series composition with the finite trigonometric-thickness kinematics, each retained term is a finite analytic combination of complete-halfwave trigonometric functions and thickness powers/factors.

The formal structural integrations are evaluated exactly term-by-term and contracted to the finite target functionals needed by the coupled equations.

Conceptually:

\[
J[\mathcal M]
=J\left[\sum_{n=0}^{\infty}\mathcal M_n\right]
=\sum_{n=0}^{\infty}J[\mathcal M_n],
\]

under the required convergence conditions. Production uses the converged finite partial sum.

In project terminology, `D15` is the exact-moment / finite-integral engine inside this full chain. For audit clarity the implementation remains separated into:

```text
material compiler -> CH/current-map composition -> D15 exact target moments -> coupled solver
```

but these are stages of ONE theory, not competing routes.

Formal counters remain:

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

## Coupled solution and ultimate load

The finite integral target functions are inserted into one coupled nonlinear system containing the retained equilibrium variables, membrane redistribution variables, and the consistent tangent/limit condition.

The ultimate load is obtained from that coupled system. It is not obtained by:

- appending steel/web strength after solving;
- selecting the root closest to experiment;
- maximizing a disconnected root cloud;
- using a separate Pu-only material model;
- treating buckling and ultimate load as interchangeable.

## External comparison is case-specific and post-solve only

### Case21

The ultimate prediction is compared with the experimental failure load

\[
P_{f,exp}=368.312750\ \mathrm{kN},
\]

not with the experimental buckling load.

### Z6 (a=24000 mm)

The ultimate prediction is compared after the solve with:

```text
Zhou empirical axial-stability formula
Winter formula
```

These external formulas are comparators only. They do not determine the material-series order, membrane field, parameters, root or capacity.

## Prohibited future misinterpretations

Do not turn one local correction into a new theory branch. In particular:

- discovering a wider material domain does not mean the structural integration method changed;
- adding membrane redistribution does not mean the material law changed;
- increasing analytic material resolution does not mean a new material model was created;
- changing specimen geometry does not authorize importing another specimen's boundary representation blindly;
- the raw-R10 numerical continuum oracle does not become production spatial quadrature;
- D15 is not a second physical theory; it is the exact structural integration stage of the unified chain.

## Canonical one-line statement

```text
actual geometry -> analytical boundary/complete halfwave -> unified R10 or unified UHPC current operator -> N48-prototype convergent analytic material series -> membrane-redistributed Nguyen field + same-source directional tangent -> exact multiple integration / D15 finite target moments -> coupled equilibrium-limit solve -> Pu -> case-specific post-solve comparison
```
