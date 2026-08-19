# NZ-SCCM — Case21 invariant-state fiber quartic derivation

**Date:** 2026-08-19 22:32 +08  
**Identity:** ROUTE-A DIRECT R10/R13 ANALYTIC STATE-SPACE DERIVATION / CHAT-LENGTH CHECKPOINT

This checkpoint continues `20260819_2142__NZSCCM__DIRECT_R10_R13_COMPLETE_LEDGER_RESUME_POINT.md`. The material law is not modified. The only purpose is to reduce the Case21 continuous kinematics to an explicit algebraic state fiber and determine whether the resulting state-space integral is elliptic or genuinely higher genus.

## 1. Case21 variables

For the controlling representative halfwave `k=1`, let

```text
U = sin^2 X
V = sin^2 Y
H = sqrt(U V)
C^2 = (1-U)(1-V)
M = pi^2/eps0 * (q0 q + q^2/2)
B = pi^2 t q / (2 eps0 b)
```

With normalized thickness coordinate `zeta=2z/t`, the R15 strain field is

```text
ex = ex0 + B H zeta
ey = ey0 + B H zeta
gamma = gamma0 - 2 B cosX cosY zeta
```

and the R10 equivalent-strain matrix is

```text
E11 = (ex + nu ey)/(1-nu^2)
E22 = (nu ex + ey)/(1-nu^2)
E12 = gamma/[2(1+nu)]
```

Write

```text
E11 = p + d zeta
E22 = qbar + d zeta
E12 = c + e zeta
```

with

```text
d = B sqrt(UV)/(1-nu)
c = (M-alpha) sqrt[UV(1-U)(1-V)]/(1+nu)
e = -B sqrt[(1-U)(1-V)]/(1+nu)
```

Define

```text
A = nu(M-alpha)/(1-nu^2)
C = [2M-alpha(1+nu^2)]/[2(1-nu^2)]
K = (alpha-M)/(1-nu)
chi = (M-alpha)^2/(1+nu)^2
```

Then the mid-thickness equivalent-strain components are explicitly

```text
p    = -alpha/4 + A U + C V + K U V
qbar = -D       + C U + A V + K U V
```

## 2. J1 = a(U,V) + b(U,V) zeta

Let `J1=tr(E)`. Then

```text
a(U,V) = -D - alpha/4
         + [2M-alpha(1+nu)]/[2(1-nu)] (U+V)
         + 2(alpha-M)/(1-nu) U V

b(U,V) = 2 B sqrt(UV)/(1-nu)
```

Thus `J1` is exactly affine in thickness.

## 3. J2 = J20 + J21 zeta + J22 zeta^2

Let `J2=det(E)`.

### 3.1 J20 fully expanded

Using the abbreviations above,

```text
J20 = C00
    + C10 U + C01 V
    + C20 (U^2+V^2)
    + C11 U V
    + C21 (U^2 V + U V^2)
    + C22 U^2 V^2
```

where

```text
C00 = alpha D/4
C10 = -alpha C/4 - D A
C01 = -alpha A/4 - D C
C20 = A C
C11 = (-alpha/4-D) K + A^2 + C^2 - chi
C21 = K(A+C) + chi
C22 = K^2 - chi
```

This is algebraically identical to

```text
J20 = p*qbar - chi U V (1-U)(1-V).
```

### 3.2 J21 fully expanded

Define

```text
L0 = (-D-alpha/4)/(1-nu) + 2(M-alpha)/(1+nu)^2
L1 = [2M-alpha(1+nu)]/[2(1-nu)^2] - 2(M-alpha)/(1+nu)^2
L2 = 2(alpha-M)/(1-nu)^2 + 2(M-alpha)/(1+nu)^2
```

Then

```text
J21 = B sqrt(UV) [ L0 + L1(U+V) + L2 U V ].
```

### 3.3 J22 fully expanded

```text
J22 = B^2/(1-nu^2)^2 * [
        -(1-nu)^2
        +(1-nu)^2(U+V)
        +4 nu U V
      ].
```

Equivalently,

```text
J22 = B^2 [ UV/(1-nu)^2 - (1-U)(1-V)/(1+nu)^2 ].
```

## 4. Eliminate thickness exactly with J1=s

For a target invariant-state coordinate `(s,t)=(J1,J2)`, if `UV>0` and `B!=0`,

```text
zeta_* = [s-a(U,V)]/b(U,V)
       = (1-nu)[s-a(U,V)]/[2 B sqrt(UV)].
```

The physical occupancy condition remains `|zeta_*|<=1`. The lines `U=0` or `V=0` are elimination-boundary sets where `b=0`; they are not spatial subdomains and have zero volume measure, but must be retained as boundary/limit cases.

## 5. Exact state-fiber equation

Substitution in `J2=t` gives

```text
F_{s,t}(U,V)
 = J20 - t
 + (J21/b)(s-a)
 + (J22/b^2)(s-a)^2
 = 0.
```

Let

```text
S(U,V;s) = s-a(U,V)
rho_nu = [(1-nu)/(1+nu)]^2
L(U,V) = L0 + L1(U+V) + L2 U V.
```

The useful ratios are

```text
J21/b  = (1-nu)L/2
J22/b^2 = 1/4 * [1-rho_nu (1-U)(1-V)/(UV)].
```

Clearing the single `UV` denominator yields the exact polynomial state fiber

```text
G_{s,t}(U,V)
 = 4 U V [J20(U,V)-t]
 + 2 U V (1-nu) L(U,V) S(U,V;s)
 + [U V-rho_nu(1-U)(1-V)] S(U,V;s)^2
 = 0.
```

No material coordinate, sampling, spatial cell or quadrature has been introduced.

## 6. Degree audit: cancellation reduces the apparent (3,3) form to a plane quartic

Before expansion, the cleared form has bidegree at most `(3,3)`. Direct symbolic expansion shows exact cancellation of the `U^3V^3`, `U^3V^2`, and `U^2V^3` terms. The surviving monomials are

```text
U^3 V, U^3,
U^2 V^2, U^2 V, U^2,
U V^3, U V^2, U V, U,
V^3, V^2, V, 1.
```

Hence

```text
total degree G_{s,t} = 4
```

for a generic nontrivial state. In particular,

```text
g31 = g13
    = -[(2M-alpha)^2 + alpha^2 nu^2]/[2(1+nu)^2],
```

which is nonzero for generic physical `(M,alpha)`, so the quartic degree is not an artifact of loose degree counting.

## 7. Cubic representation and the actual radicals

For fixed `U`, the same quartic is cubic in `V`:

```text
A3(U) V^3 + A2(U) V^2 + A1(U) V + A0(U) = 0
```

with

```text
deg A3 = 1
deg A2 = 2
deg A1 = 3
deg A0 = 3.
```

Therefore `V(U)` is a three-sheeted algebraic function. Its Cardano form necessarily contains

```text
Delta0 = A2^2 - 3 A3 A1
Delta1 = 2 A2^3 - 9 A3 A2 A1 + 27 A3^2 A0
C(U) = [ (Delta1 +/- sqrt(Delta1^2-4 Delta0^3))/2 ]^(1/3)
V(U) = -(A2 + C + Delta0/C)/(3 A3)
```

(up to the three cubic-root branches). Thus the explicit radical obstruction is not merely one quadratic root: it is the square root of the cubic discriminant followed by a cubic root.

A generic rational specialization of the parameters gives a degree-10 discriminant in `U`, with simple roots, confirming that this family is not identically singular/reducible.

## 8. Genus conclusion

A nonsingular plane quartic has genus

```text
g = (4-1)(4-2)/2 = 3.
```

A direct generic rational specialization of this family was checked to have no affine or projective singularity and no factorization, so the generic Case21 invariant-state fiber is a smooth genus-3 quartic, not an elliptic (`g=1`) curve.

Special parameter/state values can degenerate by singularity or factorization and then drop to genus 1 or 0, but the production integral must handle the generic genus-3 fibers. Therefore Route A has now crossed the precise mathematical threshold:

```text
GENERIC STATE FIBER = higher-genus Abelian (genus 3)
NOT merely elliptic.
```

Moreover, changing from `(X,Y)` to `(U,V)=(sin^2 X,sin^2 Y)` adds the coordinate Jacobian factor

```text
1/sqrt[U(1-U)V(1-V)]
```

(up to symmetry multiplicity). Thus the actual state-occupancy differential lives on an algebraic cover of the quartic and is not simpler than the genus-3 fiber itself.

## 9. Execution consequence

This is not a reason to modify R10/R13. It identifies exactly where Route A becomes mathematically expensive. The next Route-A step, if pursued, is to build/evaluate the genus-3 Abelian fiber periods and state-occupancy kernel. Per the active two-level strategy, if that cannot be made into a transparent Excel-evaluable production ledger, switch to Route B: source-constrained conservative simplification of the one-dimensional scalar material chains while retaining the R10 multiaxial CC/TC/TT assembly.
