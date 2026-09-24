# Eq.(1)–(149) R03 — STRICT EIGHT-OBJECT EXECUTION AUDIT

## User contract

No finite Fourier/Ritz/Galerkin expansion of Phi, eps_x0, eps_y0, gamma_xy0.
No added algebraic coefficients.
No x/y/z Gauss points, collocation points, material points, finite elements, or nodal discretization.
No hidden replacement of the continuous field equations.
If the strict system cannot be solved in closed/semi-closed form, stop and report that fact.

## The eight unknown objects at the direct peak

1. Phi(x,y)
2. eps_x0(x,y)
3. eps_y0(x,y)
4. gamma_xy0(x,y)
5. q
6. Aplus
7. Aminus
8. Delta

The governing equations are Eq.(28), (89), (90), (91), (109), (114), (119), (123), together with the first-sensitivity system Eq.(128),(129),(134),(136),(138),(139),(142),(143) and stationary condition Eq.(147). Eq.(148)-(149) classify the stationary point.

## Key mathematical identity

This is an eight-object system, but not an eight-scalar algebraic system. The first four unknowns are arbitrary two-dimensional fields. Eq.(89)-(91) are local nonlinear section maps and Eq.(28) is a PDE compatibility equation. Eliminating the three strain fields gives an implicit nonlinear fourth-order PDE for Phi, not a finite algebraic system.

## Analytic integration audit

Thickness direction:
- UHPC C1 normal stress is rational in an affine-through-thickness strain; piecewise analytic primitives can in principle remove z integration.
- web/PBL axial clip is affine-through-thickness with exact interval breakpoints; z integration can in principle be piecewise analytic.
- steel current Mises uses elastic affine strains followed by radial scaling fy/sigma_VM. sigma_VM is the square root of a quadratic in zeta, so thickness integrals can in principle be written using algebraic/log/asinh-type primitives after exact yield-crossing partition.

In-plane direction:
- eps_x0(x,y), eps_y0(x,y), gamma_xy0(x,y), Phi(x,y) remain unknown fields.
- nonlinear material maps compose rational/square-root/clip functions with these unknown fields.
- no finite trigonometric closure follows from the stated equations.
- the yield/tension/compression switching curves in the x-y plane depend on the unknown solution itself.
Therefore direct x-y analytic integration cannot be completed before the field solution is known, and the field solution itself is the nonlinear BVP.

## Strict execution result

Under the user's strict no-expansion/no-spatial-discretization rule, a numerical nine-BH root table cannot presently be produced from Eq.(1)-(149) alone. A finite numerical root requires at least one additional representation/solution mechanism for the four fields (spectral coefficients, collocation/grid/FEM, or an exact analytic closed-form field solution). The first two are disallowed; the third has not been derived and does not follow from the current nonlinear constitutive equations.

Therefore R03 stops without fabricating roots.

## Single-sided local admissibility

For Eq.(68)-(69) and the bottom counterpart, preserving the chosen one-sided local direction requires
A0plus + Aplus >= 0,
A0minus + Aminus >= 0.
These are inequalities only; they add no new unknowns.
They may be imposed as admissibility filters or complementarity constraints, but a new strict root cannot be computed until the continuous BVP is solved.

R02 H5 roots may be used only diagnostically to see whether an approximate root violates these inequalities; they are not formal R03 roots.
