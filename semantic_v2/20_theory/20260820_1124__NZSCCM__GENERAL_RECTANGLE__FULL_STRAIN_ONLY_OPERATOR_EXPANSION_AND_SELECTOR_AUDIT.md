# NZ-SCCM — General rectangular plate full strain-only operator expansion and selector audit

**Date:** 2026-08-20 11:24 +08  
**Identity:** THEORY AUDIT / CORRECTION OF PREVIOUS 'STRESS REGION' WORDING

## 1. Audit question

After substituting the theta-free CC/TT/TC constitutive laws into the structural virtual-work and axial-force equations, do any stress variables or stress-defined regions remain? If not, can the entire general rectangular plate be integrated as one fixed-domain polynomial immediately?

## 2. Answer

1. **All stress symbols can indeed be eliminated.** The fully substituted operator can be written only in terms of the strain components `(epsilon_x, epsilon_y, gamma_xy)`, their generalized-coordinate derivatives, material constants, and geometry.
2. The previous phrase **'stress-region obstruction' was incorrect**. No stress-defined region is needed after explicit substitution.
3. However, with separate CC/TC/TT constitutive branches, a **strain-state selector remains**. In normalized plane-strain coordinates

```text
X = epsilon_x/epsilon0
Y = epsilon_y/epsilon0
G = gamma_xy/epsilon0
U = X+Y
V = X Y - G^2/4
```

the branch conditions are

```text
TC: V < 0
CC: V > 0 and U < 0
TT: V > 0 and U > 0
```

(up to branch boundaries and any additional cracking/crushing thresholds retained by the chosen simplified law).

Therefore the correct full-domain operator is not a simple algebraic sum of all three branch polynomials. It is a piecewise strain-only operator, or equivalently a full-domain polynomial combination multiplied by strain-state indicators.

## 3. General rectangular plate strains

The current working general-rectangle kinematics are

```text
0 <= x <= b
0 <= y <= ell
-t/2 <= z <= t/2
```

with

```text
epsilon_x = nu Delta/ell
 + pi^2(A^2-A0^2)/(2 b^2) cos^2(pi x/b) sin^2(pi y/ell)
 + pi^2 z(A-A0)/b^2 sin(pi x/b) sin(pi y/ell)
 + epsilon_m[-1/4 - nu b^2/(2 ell^2) sin^2(pi x/b)
             -1/2 sin^2(pi y/ell)
             +sin^2(pi x/b) sin^2(pi y/ell)]

epsilon_y = -Delta/ell
 + pi^2(A^2-A0^2)/(2 ell^2) sin^2(pi x/b) cos^2(pi y/ell)
 + pi^2 z(A-A0)/ell^2 sin(pi x/b) sin(pi y/ell)
 + epsilon_m[nu/4 - b^2/(2 ell^2) sin^2(pi x/b)
             -nu/2 sin^2(pi y/ell)
             +b^2/ell^2 sin^2(pi x/b) sin^2(pi y/ell)]

gamma_xy = pi^2(A^2-A0^2)/(b ell)
           sin(pi x/b)cos(pi x/b)sin(pi y/ell)cos(pi y/ell)
 -2 pi^2 z(A-A0)/(b ell) cos(pi x/b)cos(pi y/ell)
 -2 b/ell epsilon_m sin(pi x/b)cos(pi x/b)sin(pi y/ell)cos(pi y/ell).
```

## 4. TC P6 is fully strain-only

Using the provisional theta-free TC P6 family,

```text
sigma_y^TC/fc = 0.5 [S6(U,V) - (X-Y) H5(U,V)]
```

expands to the following 49-term polynomial in `(X,Y,G)`:

```text
F_y_TC =
-0.0959965000375 G^6
-0.959975874175 G^4 X^2
-1.73116011724375 G^4 X Y
-0.122300088276875 G^4 X
-1.92314224351875 G^4 Y^2
-0.642800226166875 G^4 Y
+0.599476767765625 G^4
-4.52010104698625 G^2 X^4
-10.1270581505725 G^2 X^3 Y
-3.9251649066375 G^2 X^3
-7.84287621025 G^2 X^2 Y^2
-11.1080307384475 G^2 X^2 Y
+1.90885986835125 G^2 X^2
-1.8746491078775 G^2 X Y^3
-7.2549663600775 G^2 X Y^2
+0.00882059652500011 G^2 X Y
+1.04150337798875 G^2 X
-4.24656200301375 G^2 Y^4
-4.2361016313875 G^2 Y^3
+2.89577487029875 G^2 Y^2
+1.44532366711875 G^2 Y
-0.78978434158875 G^2
-5.84865292929 X^6
-13.085925926025 X^5 Y
-8.736112414305 X^5
-12.23401004141 X^4 Y^2
-22.474234349065 X^4 Y
+0.1827277174135 X^4
-12.5033412488 X^3 Y^3
-18.94952739319 X^3 Y^2
-6.257526326168 X^3 Y
+4.02161305658 X^3
-10.20504699384 X^2 Y^4
-15.02244650861 X^2 Y^3
-6.58953753312 X^2 Y^2
+5.767944481425 X^2 Y
+0.5099307186215 X^2
+1.522267745165 X Y^5
-4.713483162335 X Y^4
-8.911181778792 X Y^3
+2.021782148545 X Y^2
+2.616859285368 X Y
-0.498000085231 X
-1.92306546752 Y^6
-3.230444318395 Y^5
+0.8297299949965 Y^4
+1.89073188022 Y^3
-1.0522087996085 Y^2
+0.209859995767 Y.
```

Thus no stress ratio, theta, principal radical, or local material iteration remains inside the TC branch.

The x-stress is obtained by the exact symmetry

```text
F_x_TC(X,Y,G) = F_y_TC(Y,X,G)
```

and

```text
F_tau_TC = (G/2) H5(X+Y, X Y-G^2/4),
```

which is also a finite polynomial.

## 5. CC and TT are likewise strain-only

For the current cubic compression replacement and lambda=13/80 CC coupling, define `kappa=E0 epsilon0/fc`. The y-stress normalized by `fc` expands as

```text
F_y_CC =
-13 G^4 X kappa/1280 + 13 G^4 X/640
-13 G^4 Y kappa/640 + 13 G^4 Y/320
-13 G^4 kappa/640 + 39 G^4/1280
+13 G^2 X^2 Y kappa/320 -13 G^2 X^2 Y/160
+13 G^2 X Y^2 kappa/160 -13 G^2 X Y^2/80
+13 G^2 X Y kappa/160 -39 G^2 X Y/320
+G^2 X kappa/4 -G^2 X/2
-13 G^2 Y^3 kappa/320 +13 G^2 Y^3/160
-13 G^2 Y^2 kappa/160 +39 G^2 Y^2/320
+147 G^2 Y kappa/320 -G^2 Y
+G^2 kappa/2 -3 G^2/4
+13 X Y^4 kappa/80 -13 X Y^4/40
+13 X Y^3 kappa/40 -39 X Y^3/80
+13 X Y^2 kappa/80
+Y^3 kappa -2 Y^3
+2 Y^2 kappa -3 Y^2
+Y kappa.
```

`F_x_CC(X,Y,G)=F_y_CC(Y,X,G)`; the corresponding shear stress is also a finite polynomial obtained from the same theta-free invariant factor.

For an affine TT segment,

```text
sigma_i = C_t - K_t epsilon_i
```

gives directly

```text
F_y_TT = C_t/fc - (K_t epsilon0/fc) Y,
F_x_TT = C_t/fc - (K_t epsilon0/fc) X,
F_tau_TT = -(K_t epsilon0/fc) G/2
```

with no principal-direction variable.

## 6. Fully substituted axial force and virtual work

Let the strain-only normalized branch polynomials be `F_x^j,F_y^j,F_tau^j`, j in `{CC,TC,TT}`. Then after stress elimination

```text
P = -(fc/ell) ∫∫∫ [ chi_CC F_y_CC + chi_TC F_y_TC + chi_TT F_y_TT ] dz dx dy
```

and, for p in `{A,epsilon_m}`,

```text
R_p = fc epsilon0 ∫∫∫ {
  chi_CC [F_x_CC X_p + F_y_CC Y_p + F_tau_CC G_p]
 +chi_TC [F_x_TC X_p + F_y_TC Y_p + F_tau_TC G_p]
 +chi_TT [F_x_TT X_p + F_y_TT Y_p + F_tau_TT G_p]
} dz dx dy.
```

The selectors are strain-only:

```text
chi_TC = 1 if V<0 else 0
chi_CC = 1 if V>0 and U<0 else 0
chi_TT = 1 if V>0 and U>0 else 0.
```

Thus the user is correct that **no stress symbol and no stress-defined region survives**. The only remaining non-polynomial object, if the three branches are kept separate, is the strain-state selector itself.

## 7. Consequence

- If pointwise numerical evaluation/quadrature were allowed, the system is directly computable immediately: evaluate `(X,Y,G)`, choose the branch from `(U,V)`, evaluate the polynomial, accumulate the integral.
- Under the project's formal `N_formal_spatial_quadrature=0` requirement, the selector prevents treating the whole rectangular domain as one single fixed-domain polynomial moment unless:
  1. the strain-state subdomains are integrated analytically, or
  2. the material law is replaced by one global polynomial valid across CC/TC/TT so no selector is needed.

Therefore the corrected status is

```text
STRESS_SYMBOL_ELIMINATION = PASS
STRESS_REGION_REQUIREMENT = NONE
BRANCH_INTERNAL_POLYNOMIAL_CLOSURE = PASS
THREE_VARIABLE_EQUATION_DEFINITION = PASS
GLOBAL_SINGLE_POLYNOMIAL_FIXED_DOMAIN_CLOSURE = NOT YET, because strain-state selectors remain
```

This file does not claim that the selector is impossible to integrate analytically; it only establishes that it survives full stress elimination and must be treated explicitly before a one-shot fixed-domain D15 closure can be claimed.
