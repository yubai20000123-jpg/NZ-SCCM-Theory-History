# NZ-SCCM — formal series vs solve order, and RC backbone equivalence lock

**Timestamp:** 2026-08-16 18:41 +08:00

## 1. Core clarification

A formally infinite or very high-order analytic series is allowed as an intermediate representation. It must not be confused with the dimension of the nonlinear structural solve.

Three orders are distinct:

1. **formal structural modal series order** — e.g. a Navier/Ritz expansion \(\sum_m\sum_n A_{mn}\phi_{mn}\); this may be written to infinity and individual terms may be expanded for interpretation/audit;
2. **material analytic compiler order** — e.g. Chebyshev/MSAC coefficients used to represent a frozen material function; these coefficients are known after material compilation and are not structural unknowns;
3. **structural generalized-coordinate dimension** — the actual nonlinear unknowns solved for. In the current one-complete-halfwave RC baseline these remain \((D,q)\), plus only finite source-grounded internal coordinates when physically required.

Therefore a compiler containing hundreds or thousands of known coefficients does **not** authorize or imply a nonlinear solve with hundreds or thousands of unknowns.

The preferred implementation is a formal/nested series plus exact recurrence or target-functional moment contraction. `expand-all-then-solve-thousands-of-orders` is prohibited.

## 2. Historical RC Case21 backbone recovered

The accepted old RC calculation chain is:

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
 -> generalized coordinates (D,q), A=bq
 -> Nguyen second-order continuous strain field
 -> NC current operator M_NC(epsilon)
 -> analytic representation / CH matrix lift
 -> moment-first D15 -> Pc(D,q), Rq,c(D,q)
 -> directional reinforcement strain from the SAME strain field
 -> bilinear reinforcement current law Ms(epsilon_s)
 -> Ps(D,q), Rq,s(D,q)
 -> P=Pc+Ps, Rq=Rq,c+Rq,s
 -> connected physical branch Rq=0
 -> L=P_D Rq_q-P_q Rq_D=0
 -> Pu
```

Steel is not added after the concrete peak; it participates in `P` and `Rq` before the coupled root/limit solve.

No formal structural spatial Gauss/Simpson/adaptive/material-point grid belongs to this chain.

## 3. Membrane-effect wording correction

The old RC route already contained **Nguyen/von-Karman second-order membrane strain terms**, for example the `Cm(q)` terms in the continuous strain field. Therefore it is incorrect to describe the old route as having "no membrane effect".

The current refinement concerns **membrane stress redistribution/equilibrium beyond the previously prescribed fixed in-plane strain pattern**, not the existence of second-order membrane strain itself.

Hence the current theory should be understood as:

```text
historical accepted RC computational skeleton
+ explicit/current membrane-stress redistribution refinement
```

not as a new high-dimensional structural theory.

The redistribution refinement must preserve:

```text
one complete halfwave
low-dimensional physical generalized coordinates
same current material operator
same reinforcement embedding logic
same moment-first D15 philosophy
same P/Rq/L connected-branch topology
zero formal spatial/thickness numerical integration
```

It must not reactivate free arbitrary `p20,p02` fields, spatial cells, material points, or thousands of modal unknowns.

## 4. Relation to formal infinite Navier/Ritz expressions

A classical energy expression may be written with

\[
w(x,y)=\sum_{m=1}^{\infty}\sum_{n=1}^{\infty} A_{mn}\phi_{mn}(x,y).
\]

This is a formal completeness statement and a useful term-by-term audit device. It does not require the current production model to solve every \(A_{mn}\).

Under the project lock `ONE_CONTINUOUS_COMPLETE_HALFWAVE`, the production structural mode is selected physically/theoretically first; the structural solve remains low-dimensional. High-order material series are then treated as known analytic operators and contracted into the required exact moments.

## 5. Governance consequence

Before advancing the RC1 nested-D15 implementation, the next gate must explicitly perform an **old-RC-backbone equivalence audit** and identify the membrane-redistribution delta term by term. Only after that delta is isolated should the nested MSAC/Clenshaw/Qnm adapter be connected.

```text
FORMAL_INFINITE_SERIES = ALLOWED_AS_REPRESENTATION
TERM_BY_TERM_EXPANSION_FOR_AUDIT = ALLOWED
THOUSANDS_OF_SERIES_COEFFICIENTS_AS_NONLINEAR_UNKNOWNS = PROHIBITED
OLD_RC_BACKBONE = RETAIN
MEMBRANE_STRAIN_ALREADY_PRESENT_IN_OLD_RC = YES
NEW_DELTA = MEMBRANE_STRESS_REDISTRIBUTION_REFINEMENT
```
