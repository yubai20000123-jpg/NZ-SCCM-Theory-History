# NZ-SCCM — MATERIAL-NATIVE SCALAR DOMAIN CONTRACT R05

**Date:** 2026-08-10  
**Status:** LOCKED FOR R05 CONTINUATION  
**Route switch:** NO

## 1. Primary rule

The production scalar material compiler is qualified first on a **material-native domain**, never on a structural test-series reachability cloud.

```text
PRIMARY   = Lambda_M(material source/model)
SECONDARY = Lambda_R(structure, D, q, geometry)
MANDATORY = Lambda_R subset of Lambda_M
```

Case21/Swartz24 spectra may be used only after material qualification for structural verification or optional efficiency diagnostics. Experimental Pu may not define, shrink or tune `Lambda_M`.

NC and UHPC use the same interface but may have different material-native domains.

## 2. Ordinary-concrete normalized scalar coordinate

Use the equivalent-uniaxial normalized coordinate

\[
\lambda=\varepsilon_u/\varepsilon_{p,c},
\]

with compression negative.

Material-source landmarks retained by the current Nguyen/Foster ordinary-concrete source chain are

\[
\lambda_{c,res}=-\gamma_2,
\qquad
\lambda_{c,peak}=-1,
\qquad
\lambda_0=0,
\]

\[
\lambda_{cr}=\frac{f_t}{E_0\varepsilon_{p,c}}
=\frac{\rho}{\kappa},
\qquad
\lambda_{t,res}=\alpha_1\lambda_{cr}.
\]

For the present source choices

```text
gamma2 = 10
alpha1 = 10
alpha2 = 0.30  # project-conservative residual tension level
```

so the source-native **active transition interval** is

\[
\boxed{
\Lambda_{M,NC}^{active}
=
[-\gamma_2,\ \alpha_1\rho/\kappa]
}
\]

For the current Case21 ordinary-concrete material instance

```text
rho   = 0.10
kappa = 2.0005129533678754
lambda_cr = 0.04998717945397425
Lambda_M,NC^active = [-10, 0.49987179453974245]
```

These numbers instantiate the ordinary-concrete material source. They are **not** Swartz-derived structural limits and are **not** transferable to UHPC.

## 3. What is frozen versus still open

Hard material landmarks:

- `sigma(0)=0`;
- initial elastic tangent;
- compressive peak location/value and zero peak tangent;
- tensile cracking/peak scale.

Source landmarks whose local form may be replaced by a governed C1/C2 conservative current-map regularization:

- postcrush evolution to the residual level at the `gamma2` scale;
- Foster tension-stiffening evolution to the `alpha1*eps_cr` scale;
- finite source handoff jumps and path-history details that cannot survive in the monotonic memoryless production current surface.

The active transition interval is frozen as the R05 material-domain contract. The final compact NC postpeak scalar law and any exact plateau/continuation policy are **not yet frozen**.

## 4. Important R05 incompatibility exposed by the material domain

A pure Saenz continuation cannot by itself serve as the final deep-postpeak scalar law over this material-native interval.

For the present material instance, at `lambda=-gamma2=-10`,

\[
\sigma_{Saenz}/f_c=-0.1980605304506671,
\]

whereas the Nguyen source postcrush residual landmark is approximately

\[
\sigma_{res}/f_c=-0.10.
\]

Thus a separate smooth conservative postpeak closure must be frozen at material level before a final scalar compiler can be promoted.

## 5. UHPC portability

UHPC must supply its own material-source landmarks and domain metadata:

```text
Lambda_M,UHPC = derived from selected UHPC constitutive source/model
```

The following are reusable without change:

- equivalent-uniaxial/invariant structural interface;
- `2x2` matrix-function/divided-difference machinery;
- low-rank/separable reconstruction logic;
- D15 exact-moment library;
- `P, Rq, tangent, L` structural kernel.

NC numerical domain limits, Saenz/Foster thresholds, `alpha1`, `gamma2`, and NC residual levels are not transferable material constants for UHPC.

## 6. Forbidden reversals

Do not:

- redefine the production material domain from Swartz24 or Case21 spectra;
- use structural Pu to select material-domain endpoints;
- silently reuse NC domain numbers for UHPC;
- treat the active-transition interval as a new TT/TC/CC runtime state partition.
