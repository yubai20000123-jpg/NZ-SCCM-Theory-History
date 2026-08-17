# NZ-SCCM — true infinite-series -> finite-integral-solution canonical correction

**Timestamp:** 2026-08-17 14:49 +08:00  
**Status:** CONTROLLING CANONICAL CORRECTION / SUPERSEDES THE 14:42 FINITE-PARTIAL-SUM INTERPRETATION

## 0. Why this correction is necessary

The 14:42 canonical lock still contained a material misinterpretation: it described the N48-derived representation as an infinite series in principle but a production method based on testing finite orders `N=48,96,144,...` until engineering convergence. That is NOT the user's intended theory.

The controlling interpretation is now:

```text
N48 = prototype that reveals the analytic series architecture
NOT = a fixed degree
NOT = a refinement quantum to be stacked as 48,96,144,...
NOT = trial-order escalation until the answer looks converged
```

The intended formal material representation is a **genuine infinite convergent analytic series** with a discoverable coefficient law / recurrence / generating relation and a dedicated convergence expression, analogous in mathematical architecture to classical infinite-series plate solutions: after exact termwise structural integration, the infinite series is summed or taken to its mathematical limit to produce a finite target function.

## 1. Canonical end-to-end chain

The theory is one continuous chain:

```text
actual specimen dimensions + physical boundary conditions
 -> geometry-specific analytic domain / admissible boundary representation / complete representative halfwave
 -> one unified physical current material target
      ordinary concrete: frozen R10
      UHPC: one unified UHPC current operator
 -> derive an N48-prototype TRUE INFINITE analytic series representation of that material target
      identify basis
      identify coefficient sequence law / recurrence / generating formula
      prove/establish convergence on the geometry-certified material domain
 -> compose the infinite material series with Nguyen second-order complete-halfwave kinematics
 -> include physically admissible membrane-stress redistribution BEFORE material evaluation
 -> derive the same-source full directional consistent tangent as the derivative of the SAME infinite material series
 -> exact multiple integration term-by-term over the one complete representative halfwave and thickness
 -> transform the infinite material series into an infinite sequence of exact D15 structural moments
 -> sum that moment series analytically or evaluate its n->infinity limit by its convergence law
 -> obtain finite closed / limit-evaluable target functions P, R, tangent/stability terms
 -> solve the coupled finite system for D, q, membrane coordinates, and ultimate condition
 -> obtain Pu
 -> post-solve comparison only
```

## 2. Geometry first

The specimen dimensions determine the analytical boundaries before the material-series representation is instantiated for that specimen.

This includes:

- complete representative halfwave length;
- aspect ratio and trigonometric basis;
- admissible membrane-stress-redistribution coordinates/shapes;
- strain-domain bounds / invariant-domain bounds needed to certify convergence of the unified material series;
- shell/rebar/web phase geometry and their exact integration bounds.

For Z6:

```text
a = 24000 mm
b = 12000 mm
m* = 2
ell = 12000 mm = b
A0 = 48 mm
q0 = 0.004
```

The physical plate contains two repeated halfwaves, but the formal structural domain is one complete 12000-mm representative halfwave.

## 3. Unified material target does not change with the specimen

Ordinary concrete physical target:

```text
M_NC = frozen R10 current operator
```

UHPC physical target:

```text
M_UHPC = one unified UHPC current operator
```

The specimen changes only the analytic domain on which the material target must be represented and integrated. It does not authorize a specimen-specific physical material law.

## 4. Correct mathematical meaning of “N48 as prototype”

N48 is historical evidence that the R10 source can be represented in an analytic spectral/polynomial-type basis compatible with Cayley-Hamilton and D15. The formal theory must now lift that finite prototype into an infinite sequence.

The intended scalar prototype is of the form

\[
F(\lambda)=\sum_{n=0}^{\infty} a_n\,\phi_n(\lambda),
\]

where the important object is not a chosen cutoff `N`, but the **sequence law**

\[
a_n = \mathcal A(n;\text{R10 parameters})
\]

or an equivalent recurrence / generating relation

\[
\mathcal R(a_{n+r},\ldots,a_n;n)=0,
\]

plus a convergence law / remainder relation that establishes the infinite limit on the certified domain.

The exact basis `phi_n` may be Chebyshev-like, power/rational, Fourier-like, or another source-regular analytic basis. It must be chosen from the frozen material source and the required analytic domain, not from matching capacity data.

The target is therefore:

```text
finite prototype -> infer/derive infinite coefficient structure -> infinite convergent material identity
```

not

```text
N48 failed -> try N96 -> try N144 -> ...
```

The latter may remain a development diagnostic but is not the governing formal theory.

## 5. Membrane redistribution enters before the infinite-series composition

The continuous strain field is

\[
\varepsilon=\varepsilon(D,q,\mathbf r;X,Y,\zeta),
\]

where `r` denotes the geometry/boundary-admissible membrane redistribution coordinates.

The infinite material representation is evaluated on this redistributed strain field:

\[
\sigma(X,Y,\zeta)
=\mathcal M\!\left(\varepsilon(D,q,\mathbf r;X,Y,\zeta)\right)
=\sum_{n=0}^{\infty}\sigma_n(D,q,\mathbf r;X,Y,\zeta).
\]

Membrane redistribution is therefore neither a post-processing correction nor a separate capacity-reduction factor.

## 6. Same-source directional tangent is part of the same infinite series

The current tangent must be derived from the same material identity:

\[
\mathbf D_t
=\frac{\partial\sigma}{\partial\varepsilon}.
\]

If

\[
\sigma=\sum_{n=0}^{\infty}\sigma_n,
\]

then, under the required uniform/normal convergence conditions for the derivative series,

\[
\boxed{
\mathbf D_t
=\sum_{n=0}^{\infty}
\frac{\partial\sigma_n}{\partial\varepsilon}
}.
\]

Thus value and tangent are not compiled independently and are not fitted with unrelated approximants.

## 7. Exact multiple integration transforms the infinite material series into an infinite moment series

For any required structural target functional `J` (load, residual, tangent element, stability element),

\[
J[\sigma]
=\iiint_{\Omega} W(X,Y,\zeta)\,\sigma\,d\Omega.
\]

After composition with the finite trigonometric-thickness kinematics, every individual series term has a finite exact structural integral:

\[
J_n
=\iiint_{\Omega}W\,\sigma_n\,d\Omega,
\]

which is evaluated by exact General-D15 moments.

Under the convergence conditions that justify exchanging sum and integral,

\[
\boxed{
J
=\sum_{n=0}^{\infty}J_n.
}
\]

The formal target is the **limit of this exact moment series**:

\[
\boxed{
J=\lim_{N\to\infty}\sum_{n=0}^{N}J_n.
}
\]

The preferred endpoint is a closed summation / generating-function expression where available. Otherwise the limit is evaluated from the mathematically derived convergence recurrence / tail law. This is not spatial numerical quadrature and does not create material points or spatial cells.

## 8. D15 meaning under the corrected interpretation

D15 is not “evaluate one finite N polynomial and stop”. It is the exact structural moment transform acting term-by-term on the infinite material series.

Conceptually:

\[
\mathscr D_{15}:\quad
\sum_{n=0}^{\infty}\sigma_n
\mapsto
\sum_{n=0}^{\infty}J_n
\mapsto
J_{\infty}.
\]

The output is a finite target function of the finite generalized coordinates, e.g.

\[
P=P(D,q,\mathbf r),
\]

\[
R_q=R_q(D,q,\mathbf r),
\]

\[
R_m=R_m(D,q,\mathbf r),
\]

and finite tangent/stability matrix entries.

## 9. Coupled finite solve

After the infinite material/moment series has been summed to finite target functions, the remaining unknowns are finite generalized coordinates only. The ultimate solution is obtained by solving the coupled equations, schematically

\[
R_q=0,
\qquad
R_m=0\ \text{or the retained admissible membrane-equilibrium projection},
\]

plus the same-source tangent/limit condition defining the first reachable ultimate point.

The series index `n` is NOT a structural degree of freedom and is NOT a spatial discretization.

## 10. Case-specific validation only after solving

### Z6 (a=24000 mm)

After the unified chain produces Pu, compare to:

- Zhou empirical axial-stability formula;
- Winter formula.

These are post-solve comparators only.

### Case21

After the unified chain produces Pu, compare to

\[
P_{f,exp}=368.312750\ \mathrm{kN}.
\]

The experimental buckling load is not the ultimate-load comparator.

## 11. Formal counters remain

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

## 12. Explicitly superseded interpretations

The following are now explicitly superseded:

```text
N48 = final universal order                         -> WRONG
N48 = block, then test 96/144/192 until converged -> DEVELOPMENT ONLY, NOT FORMAL THEORY
production = arbitrary finite truncation          -> WRONG
membrane redistribution after material evaluation -> WRONG
independent tangent fit                            -> WRONG
D15 = one finite polynomial integral              -> TOO NARROW
```

The controlling statement is:

```text
actual geometry -> analytic boundary/domain -> unified R10 or unified UHPC current target -> derive true infinite convergent N48-prototype material series with coefficient/convergence law -> membrane-redistributed Nguyen field + same-source directional tangent -> exact multiple integration term-by-term -> D15 exact infinite moment series -> analytic/limit summation to finite target functions -> coupled finite equilibrium/limit solve -> Pu -> case-specific post-solve comparison
```
