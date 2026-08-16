# NZ-SCCM — historical RC calculation method versus current exact-algebraic route

**Timestamp:** 2026-08-16 20:34 +08:00

This note isolates calculation-method changes from the separately introduced five-term membrane-stress redistribution.

## 1. What has NOT changed

The structural backbone remains:

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order continuous kinematics
R10 ordinary-concrete physical current law
reinforcement on the same continuous strain field
General-D15 exact target philosophy
P,Rq,L connected-branch limit condition
same-state tangent/KZ requirement
outer global coordinates (D,q)
zero formal spatial numerical quadrature
```

After membrane redistribution is introduced, the five coordinates

`[r0,r20,r22,s02,s22]`

are internal and Schur-condensed; the outer root topology remains `(D,q)`.

## 2. Historical/current-support RC calculation method

The historical successful RC route first converted the frozen R10 scalar source functions into finite Chebyshev material-coordinate polynomials, e.g. the N48 family:

```text
R10 source U,C,T,T7
 -> choose compiler interval [lambda_a,lambda_b]
 -> 49 material-coordinate nodes
 -> finite Chebyshev coefficients
 -> C1/minimax repairs
 -> Cayley-Hamilton polynomial matrix lift
 -> finite trigonometric/thickness polynomial stress field
 -> General-D15 elementary moments
 -> P,Rq,L,KZ
```

The key computational property was that once the material source was replaced by a finite polynomial, all structural integrands became finite polynomial/trigonometric expressions and D15 could integrate them by elementary beta/thickness moments.

The price was material-representation error and a material polynomial order. Later source-fidelity work increased or multiscaled those orders; RC1 reduced material error but its nested structural expansion became impractical.

## 3. Current preferred exact-algebraic calculation method

The current route does not first approximate R10 by a material polynomial. It carries the same frozen R10 source directly as an exact finite matrix/algebraic graph:

```text
continuous strain E
 -> exact R10 smooth split / compression / tension spline matrix functions
 -> exact 2x2 invariant reduction
 -> scalar algebraic generators s_eta,s_1,s_10
 -> finite holonomic/special-function target moments
 -> General-D15 target contraction
 -> P,Rq,L,KZ
```

Consequences:

```text
N48 material compiler order     -> absent from preferred candidate
Ng,Nc,Nt RC1 fit orders         -> absent from preferred candidate
49/N material-coordinate roots  -> absent from preferred production source graph
independent fitted T7 channel   -> eliminated; T7=T^7 exactly
material-fit interval error     -> not the structural approximation mechanism
```

The exact R10 physical current law itself is unchanged.

## 4. Change in the role of Cayley-Hamilton

Historical route:

```text
Cayley-Hamilton = efficient lift/evaluation of a finite polynomial material compiler.
```

Current route:

```text
2x2 Cayley-Hamilton/invariants = exact reduction of matrix square roots, inverses,
traces, determinants and powers to a fixed low-degree scalar algebraic field.
```

Thus CH moves from mainly managing a polynomial approximation to managing the exact 2x2 matrix algebra.

## 5. Change in the role of D15

Historical route:

```text
D15 leaf = finite monomial sin^p cos^r sin^u cos^s zeta^h
 -> beta functions + elementary Z_h.
```

Current route:

```text
D15 retains the same elementary polynomial leaves,
but algebraic R10 factors require an added holonomic/special-function leaf:
polynomial target * algebraic atom -> finite differential/moment state.
```

The 20:34 gate proves this exactly for the generic noncommuting smooth quartic thickness atom: an order-2 annihilator and an exact recurrence for polynomial thickness moments now exist.

## 6. Change in complexity

Historical finite-polynomial route:

```text
cost/complexity depends strongly on material compiler degree and coefficient support.
```

RC1 showed that high source fidelity can create enormous composed polynomial degrees if flattened structurally.

Current exact-algebraic route:

```text
material representation complexity is fixed by algebraic field degree,
not by N48/Ng/Nc/Nt and not by a spatial point count.
```

The current full R10 source/tangent field has a conservative algebraic-degree upper bound `<=64`; the smooth quartic generator alone has a thickness ODE of order `<=2`.

## 7. What remains unfinished

The exact-algebraic route is not yet the released production Pu backend.

Open items are:

```text
full s_eta+s_1+s_10 compositum annihilator/runtime
complete thickness contraction for full R10 stress/tangent targets
beta-weighted two-coordinate (X,Y) creative telescoping
then five-term current-material internal solve and Schur condensation
then new P,Rq,L,KZ and Pu
```

Therefore the historical RC result remains only the current-support capacity baseline until this exact-algebraic target runtime closes.
