# NZ-SCCM EXACT RANK-4 BRANCH KERNEL CLASSIFICATION R04

Date: 2026-08-10

## 1. User correction accepted
Production spectral qualification must NOT be defined by Swartz24 geometry.
The primary domain is the admissible spectral domain of the selected constitutive model.
Swartz/Case21 spectra are only structural reachable subdomains used after material qualification.

This is essential for UHPC portability: NC and UHPC may have different scalar strain/strength validity ranges, while the invariant structural and D15 machinery remains identical.

## 2. Source support for the ordinary-concrete domain contract
Nguyen Chapter 3 uses equivalent-uniaxial strains to represent biaxial/in-plane response.
Nguyen explicitly states Saenz Eq. (3.39) is valid for concrete strengths up to 70 MPa.
Nguyen/Foster tension stiffening has a finite transition from eps_cr to alpha1 eps_cr with alpha1=10, followed by a constant residual tensile branch.
Nguyen post-crushing response evolves from peak compression to gamma2 eps_p, then a residual plateau; the project G21 source audit records gamma2=10 for the exact source branch before the current smooth-conservative replacement.

These facts define the DOMAIN INTERFACE, but do not yet freeze final numerical lambda_min/lambda_max because the final compact NC production current operator itself remains open.

## 3. Exact primitive algebra
Eliminating R=sqrt(z^2+eta^2) from Pi_eta gives:

```text
4*eta^4*p^2 + 8*eta^2*p^2*z^2 - 4*eta^2*p*z^3 - eta^2*z^4 + 4*p^2*z^4 - 4*p*z^5 = 0
```

This is quadratic in p=Pi_eta(z), therefore Pi_eta and C are algebraic degree <=2 over the scalar lambda field.

For H, after subtracting its fixed normalization constant:

```text
hbar^2-(r-r0)hbar-eta_r^2/4=0.
```

Each H therefore adds at most one quadratic extension.

Generic scalar-field upper bounds:

```text
C(lambda):   degree <=2
T(lambda):   degree <=8
T(lambda)^8: degree <=8
U(lambda):   degree <=8
```

These are algebraic-extension upper bounds, not claims of irreducibility.

## 4. After structural spectral substitution

```text
lambda± = mu ± sqrt(Q)
```

Generic extension-degree upper bounds over the structural invariant base:

```text
U(lambda+)          <=16
C+^2 C-             <=8
C+ T-               <=32
T+ T-^8             <=128
```

The last term has the highest compositum complexity. Raising T to the 8th power does not increase the scalar field degree, but combining the two spectral branches does.

## 5. Appell/Carlson classification
Appell F1 directly closes kernels that reduce to bilinear sin^2 denominators such as

```text
1/(a+b s+c t+d s t)
```

and small parameter-derivative families.

Carlson RF/RD/RJ directly close genus-1 elliptic kernels built from one cubic/quartic square root.

The exact full Pi+H1+H10 source-shaped tension tower is generically neither class:

- it contains nested quadratic extensions;
- after lambda± substitution the generic algebraic degree is far above a single elliptic square root;
- therefore the full exact source-shaped law does NOT obtain a small direct Appell/Carlson production closure merely by recognizing the plotted surface as saddle-like.

This is a productive negative result: Appell/Carlson remain a kernel library, but not a magic wrapper for the full frozen source oracle.

## 6. Rank-4 term classification

| term | generic structural extension bound | direct named-kernel status |
|---|---:|---|
| U(lambda+) | <=16 | no generic Appell/Carlson closure |
| C+^2 C- | <=8 | simplest nonlinear term; further reduction may become elliptic |
| C+ T- | <=32 | no generic small named kernel |
| T+ T-^8 | <=128 | FAIL direct exact production complexity |

Exact rank-4 separability itself remains retained. The failure is only the attempt to integrate the full exact source tension tower by a small universal named special function.

## 7. Main consequence
The next task should NOT be another spatial integration theory.

The remaining problem is one-dimensional material design:
construct/identify compact scalar branch primitives on the MATERIAL-NATIVE spectral domain, while preserving:

- source strength/strain applicability;
- stress and same-map tangent;
- smooth conservative target philosophy;
- exact rank<=4 or invariant reconstruction;
- direct D15/Beta or small named-kernel closure.

Only after that material-domain closure is frozen should structural reachable spectra be used for verification or optional acceleration.

## 8. R04 status

```text
EXACT_RANK4_BRANCH_KERNEL_CLASSIFICATION_R04 = PASS_WITH_NEGATIVE_SPECIAL_FUNCTION_RESULT
FULL_SOURCE_EXACT_APPELL_CLOSURE = FAIL_GENERIC
FULL_SOURCE_EXACT_CARLSON_CLOSURE = FAIL_GENERIC
MATERIAL_NATIVE_SPECTRAL_DOMAIN_GOVERNANCE = PASS
SWARTZ24_AS_PRODUCTION_SPECTRAL_DOMAIN = REJECT
ROUTE_SWITCH = NO
CASE21_PU = NOT_RUN
SWARTZ24_PU = NOT_RUN
```

```text
NEXT = MATERIAL_NATIVE_1D_PRIMITIVE_REFORMULATION_R05
```
