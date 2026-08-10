# NZ-SCCM — EXPLICIT END-TO-END CAPACITY DOCTRINE

**Date:** 2026-08-10 20:56 +08:00

## 1. User clarification / priority reset

The material-data representation is not required to reproduce every measured/local peak, cusp, ridge, abrupt corner or narrow oscillatory feature. Such features may be deliberately under-used, trimmed, rounded, smoothed or replaced by a simpler conservative/controlled analytic patch, exactly as one may measure a sharp experimental peak but intentionally choose not to use the full peak value in a design model.

This is a **data-processing / constitutive-target choice**, not automatically a change of structural mechanics route.

## 2. Highest-priority requirement

The overriding requirement is now:

```text
FINAL_THEORY_MUST_PRODUCE_ULTIMATE_CAPACITY_FROM_EXPLICIT_FORMULAS
AND_EXPLICIT_DERIVATIVES_OF_THE_SAME_FORMULAS.
```

Allowed mathematical representations are not pre-restricted to one current-map grammar. Any of the following may be used if they satisfy the end-to-end explicitness requirement:

- direct 4D stress-strain manifold representation;
- invariant current map;
- principal-spectral representation;
- whole-domain/global target function;
- low-rank/separable surface;
- polynomial/rational/algebraic representation;
- named special functions with explicit derivative identities;
- local analytic smoothing patches;
- other mathematically explicit representations.

No representation receives theory identity merely because it is elegant. The governing test is whether it yields a transparent explicit chain to the capacity equations.

## 3. Material simplification permission

A sharp material feature may be intentionally rounded or lowered when all of the following are reported explicitly:

1. the original source/measurement feature;
2. the retained anchor quantities (for example origin tangent, compression peak, tensile peak, residual level, biaxial landmarks);
3. the modified analytic formula;
4. the sign and magnitude of the induced strength change (compression, tension, TT, TC, etc.);
5. the derivative change;
6. whether the modification is conservative, enhancing, or mixed over the affected region;
7. the resulting effect on the final structural prediction, checked only after the analytic material target is frozen.

The objective is **not minimum pointwise material regression error**. The objective is a sufficiently faithful, physically controlled, explicitly differentiable material representation suitable for direct ultimate-capacity theory.

## 4. End-to-end explicitness contract

The accepted production chain must have the form

\[
\boldsymbol\sigma = \mathcal M(\boldsymbol\varepsilon;\mathbf p),
\qquad
\mathbf C_t=\partial\boldsymbol\sigma/\partial\boldsymbol\varepsilon
\]

or an equivalent explicit global representation, and then

\[
P=P(D,q;\mathbf p),\qquad R_q=R_q(D,q;\mathbf p),
\]

with derivatives from the same formulas,

\[
P_{,D},\ P_{,q},\ R_{q,D},\ R_{q,q}.
\]

Ultimate capacity is obtained from explicit stationarity/equilibrium equations, currently represented by

\[
R_q(D,q)=0,
\]

\[
L(D,q)=P_{,D}R_{q,q}-P_{,q}R_{q,D}=0,
\]

followed by admissible real-root selection and

\[
P_u=P(D^*,q^*).
\]

The exact representation of `M`, `P`, or the intermediate surface may change; the end-to-end explicit derivative chain may not be replaced by hidden material-point propagation, opaque numerical differentiation, or a black-box numerical integral used as the production operator.

## 5. What is no longer a hard objective

The following are explicitly demoted from hard goals:

- pointwise reproduction of every cusp/transition ridge of the frozen source oracle;
- preservation of the full measured/local material peak when a controlled lower analytic target is preferred;
- preservation of a particular `C,T,T^8`, Möbius, softsign, polynomial, invariant, spectral, or saddle-like representation;
- minimizing material regression error at the expense of formula complexity.

## 6. What remains mandatory

- The final capacity model must be explicit and differentiable end-to-end.
- Material simplification must be transparent and its mechanical consequence quantified.
- NC and UHPC may use different material targets/parameters, but the same explicit-capacity methodology should be portable where possible.
- Experimental structural capacities may be used for **validation after the analytic material target is defined**, not to hide undocumented local tuning.
- Historical failed compiler experiments remain evidence; they do not constrain the choice of the next explicit representation.

## 7. Immediate workflow consequence

The next work should return to **visual / mechanical surface simplification first**:

1. plot the NC current surface and, once source-complete, the UHPC surface;
2. identify sharp/high-curvature features that are candidates for deliberate under-use or smoothing;
3. propose a small number of explicit analytic surface/curve replacements;
4. label the induced change as compression reduction / tension reduction / enhancement / mixed;
5. keep only candidates whose explicit derivatives are compact enough to propagate to `P,Rq,L`;
6. only then perform structural validation.

`R07_HEAD_TO_HEAD_KERNEL_COMPLEXITY_DECISION_GLOBAL_POLY64_VS_MOBIUS24` is therefore no longer the unique next step and is placed on HOLD pending this simplified end-to-end explicit representation study.
