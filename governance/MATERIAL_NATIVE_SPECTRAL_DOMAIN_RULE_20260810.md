# MATERIAL-NATIVE SPECTRAL DOMAIN RULE — 2026-08-10

**Status:** ACTIVE / CROSS-MATERIAL GOVERNANCE

## 1. Primary correction

Production spectral qualification shall be defined by the **admissible spectral domain of the selected constitutive model**, not by Case21 or Swartz24 reachable spectra.

```text
PRIMARY_DOMAIN   = MATERIAL_ADMISSIBLE_SPECTRAL_DOMAIN
SECONDARY_DOMAIN = STRUCTURAL_REACHABLE_SUBDOMAIN
```

The material compiler must first be valid on the constitutive-model domain. Case21/Swartz reachable spectra may only be used afterwards for structural verification and optional efficiency diagnostics.

## 2. Reason

Using Swartz24 to define the production material domain would make the material/compiler identity specimen-dependent and would block clean transfer to UHPC. The structural theory must instead accept material-specific domain metadata:

```text
NC   -> Lambda_M_NC  -> same invariant/D15 architecture
UHPC -> Lambda_M_UHPC -> same invariant/D15 architecture
```

The numerical spectral bounds for NC and UHPC may differ. The structural invariant machinery, exact-rank/separable compilation logic, D15 moment engine, and analytic root kernel do not change.

## 3. Source-supported ordinary-concrete domain landmarks

Nguyen Chapter 3 uses the equivalent-uniaxial strain framework for biaxial/in-plane concrete response. Source facts retained for domain construction:

- Saenz Eq. (3.39) is stated by Nguyen to be valid for concrete strengths up to 70 MPa.
- Foster/Nguyen tension stiffening contains a finite nontrivial transition from cracking strain `eps_cr` to `alpha1*eps_cr`, with `alpha1=10`, followed by a constant residual tensile branch.
- Nguyen post-crushing compression evolves from peak strain `eps_p` to `gamma2*eps_p`, followed by a residual plateau; the project G21 source audit records `gamma2=10` for the exact source branch before the smooth-conservative production approximation.

These landmarks define a **material-domain interface**. They do not yet freeze final numerical `lambda_min/lambda_max`, because the final compact NC production current operator is still open.

## 4. UHPC transfer rule

UHPC must obtain its spectral/admissible domain from the finally selected UHPC constitutive source/model itself.

Allowed to reuse from NC:

```text
Eu/J1/J2 invariant architecture
coalescence-safe 2x2 matrix-function reconstruction
exact-rank / separated compilation logic
D15 / named analytic kernel library
P,Rq,L structural solver
material-domain governance interface
```

Not allowed to inherit from NC:

```text
NC numerical lambda bounds
NC cracking thresholds
NC post-crushing thresholds
NC source strength-validity range
```

## 5. Structural reachability role

For a fixed structure family, a reachable set `Lambda_R(D,q,geometry)` is useful only after material closure. The mandatory relation is

```text
Lambda_R subset of Lambda_M
```

If the structural set is smaller, it may be used for verification, conditioning estimates, or optional acceleration, but it may not determine material coefficients, truncation order, or the production validity claim.

## 6. Calibration prohibition

Experimental or computed structural ultimate loads shall not be used to shrink, tune, or select `Lambda_M`.

```text
Pu -> material spectral domain = PROHIBITED
```

## 7. Consequence for R03

The R03 Swartz24 spectral certificate remains valid as a **structural diagnostic theorem inside its stated D-q box**. It is not the production material spectral domain.

## 8. Current consequence

All post-R04 scalar-primitive or special-function screens must be posed on a material-native admissible domain, with structural reachable domains reported separately.
