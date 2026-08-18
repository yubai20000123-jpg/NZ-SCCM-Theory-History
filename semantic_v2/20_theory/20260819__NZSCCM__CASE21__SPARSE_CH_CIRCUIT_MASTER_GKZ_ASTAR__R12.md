# NZ-SCCM Case21 — sparse CH-circuit master GKZ A* R12

**Date:** 2026-08-19  
**Identity:** EXACT SYMBOLIC CONSTRUCTION / ZERO DISCRETIZATION / NO NEW MATERIAL THEORY

## 0. Why R12

R11 proves that a finite algebraic R10 target can be lifted to a rational period and classified by a GKZ / relative-incomplete A-hypergeometric family. A naive implementation could still create a huge expanded denominator polynomial. R12 removes that implementation risk by retaining the full 2x2 Cayley-Hamilton calculation as a **sparse polynomial circuit** and residue-lifting the circuit variables themselves.

This is another constructor switch, not a new material law.

## 1. 2x2 CH pair algebra

Represent every matrix commuting with E as

\[
X=x_0I+x_1E.
\]

For `tr(E)=tau`, `det(E)=delta`, pair multiplication is

\[
(x_0,x_1)\odot(y_0,y_1)=
(x_0y_0-\delta x_1y_1,\;x_0y_1+x_1y_0+\tau x_1y_1).
\]

Also

\[
\det X=x_0^2+\tau x_0x_1+\delta x_1^2,
\]

\[
\operatorname{adj}X=(x_0+\tau x_1)I-x_1E.
\]

Therefore every finite R10 matrix addition, multiplication, inverse, determinant, adjugate and finite power can be encoded by quadratic/bilinear polynomial relations between pair coefficients.

## 2. Do not substitute invariants into giant polynomials

Instead introduce exact auxiliary variables

```text
w, mu, de, h, tauE, deltaE, Del, Sig
```

with sparse relations

\[
w^2-r(1-r)s(1-s)=0,
\]

\[
tauE-2mu=0,
\]

\[
deltaE-mu^2+de^2+h^2=0,
\]

\[
Del^2-[deltaE^2+eta^2(tauE^2-2deltaE)+eta^4]=0,
\]

\[
Sig^2-[tauE^2-2deltaE+2eta^2+2Del]=0.
\]

The kinematic `mu,de,h` relations retain the exact Nguyen halfwave expressions in `(r,s,u,w)`; no spatial point evaluation occurs.

## 3. Sparse R10 computation graph actually constructed

The exact first-tension-branch R07 pilot was compiled into a sparse CH-pair circuit containing:

```text
polynomial/circuit relations = 78
GKZ monomial-space variables = 81
total Cayley monomial columns = 271
Cayley matrix size = 159 x 271
maximum monomials in any one relation = 13
maximum-support relation = G_h
```

The circuit includes, without global expansion:

```text
kinematic invariants
-> A = E^2 + eta^2 I
-> principal matrix square root pair R
-> exact A inverse
-> t and c projector pairs
-> compression C through K = I + (kappa-2)c + c^2
-> first-branch finite polynomial u_R(t)
-> T,U,T^7
-> det/adj operations
-> full R10 stress pair S = S0 I + S1 E
-> Syy = S0 + S1(mu-de)
```

All inverse operations are represented by sparse polynomial constraints rather than expanded rational substitution.

## 4. Key sparsity result

A direct expanded invariant denominator for the compression inverse can already contain hundreds of monomials before spatial substitution. The sparse circuit avoids this entirely. Every circuit relation has at most 13 monomials; the total Cayley support has only 271 monomial columns in the current pilot representation.

Thus the standard-function object can be defined by one finite sparse Cayley configuration A* rather than one enormous manually expanded polynomial.

## 5. Master family for P, Rq, Ralpha

`P_c`, `R_q`, and `R_alpha` use the same current-stress circuit multiplied by finite Nguyen derivative weights. Those weights change the numerator only and do not introduce a new denominator polynomial family.

Same-source derivatives differentiate the same rational circuit. They can increase denominator powers but do not introduce a new denominator **support**. Therefore

```text
P, Rq, Ralpha, J_lim entries
-> one master support family A_*
-> finite exponent/contiguity/differential shifts
```

rather than separate material series/functions for each target.

## 6. Important scope label

The printed 159x271 A* is the **R07 globally first-tension-branch pilot circuit**. It is not yet claimed to be the final full-Pu Case21 three-branch A*.

For a later state crossing `xcr` or `10*xcr`, do not discretize the plate. Add the finite threshold algebraic divisors to the relative/incomplete A-hypergeometric data. The full R10 piecewise law remains one exact global material law; threshold boundaries are relative-period data, not numerical spatial cells.

## 7. Status

```text
R11_GLOBAL_RESIDUE_GKZ_CLASSIFICATION = PASS
R12_SPARSE_CH_CIRCUIT = CONSTRUCTED
R12_PILOT_ASTAR_ROWS = 159
R12_PILOT_ASTAR_COLUMNS = 271
R12_MAX_RELATION_SUPPORT = 13
P_RQ_RALPHA_SHARED_SUPPORT = PASS FOR PILOT
J_SHARED_DENOMINATOR_SUPPORT = PASS AT DIFFERENTIAL-CLOSURE LEVEL
FULL_THREE_BRANCH_CASE21_ASTAR = OPEN
DISCRETIZATION = ZERO
MATERIAL_PREFIX = ABSENT
```

## 8. Next task

Do not return to sequential Lauricella if it becomes cumbersome. Extend the sparse circuit with the finite R10 threshold variables/divisors needed by the complete three-branch law, and construct the **full Case21 relative/incomplete-GKZ master A*** without spatial subdivision. If that direct relative-GKZ form becomes computationally inconvenient, switch evaluation representation (Mellin-Barnes / residue / differential system) while keeping the same A* support and exact finite R10 operator.