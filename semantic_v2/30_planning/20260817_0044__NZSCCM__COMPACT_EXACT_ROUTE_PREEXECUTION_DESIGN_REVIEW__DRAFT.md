# NZ-SCCM compact-exact route — pre-execution design review

**Timestamp:** 2026-08-17 00:44 +08:00  
**Status:** DRAFT / NOT LOCKED / NO EXECUTION AUTHORIZATION  
**Purpose:** user review before any new derivation, regularization, target-runtime implementation, or Pu calculation.

## 0. Review premise

Current accepted direction is not a high-order finite Chebyshev escape and not a return to legacy N48. Formal infinite/high-order analytic representations are allowed for theory and termwise audit; production computation must use compact exact/bounded-state recurrence or target-functional contraction and must not enumerate thousands of coefficients.

Historical compact-exact progress retained:

- five-term membrane physics and General-D15 target definition: passed;
- ordinary nested polynomial/adjoint-Clenshaw flattening: rejected because degree still propagates;
- R10 three-generator quadratic tower: fixed 64-state algebraic field, 159/4096 derivative sparsity;
- 2x2 Cayley-Hamilton eliminates explicit T^7 matrix power and derivative nodes;
- compact stress/tangent target DAG and field-product adjoint pullback: passed;
- current blocker: rationalized local connection contains removable apparent poles although the physical atom is regular.

No new computation is authorized by this draft.

## 1. Proposed operation sequence if later approved

### Stage A — source-level regularity classification before any implementation

For every R10 algebraic atom used by the 64-state representation, classify singular loci into:

1. `REMOVABLE_BASIS_SINGULARITY`: physical source function and required tangent are regular; only the chosen rationalized basis/connection is singular;
2. `TRUE_SOURCE_KNOT`: the frozen R10 source itself has a real non-smooth material event;
3. `EIGENVALUE_COALESCENCE`: scalar spectral formula appears singular but the 2x2 matrix function has a finite divided-difference/Frechet limit;
4. `OUTSIDE_REACHABLE_DOMAIN`: irrelevant to actual Case21/Z6 state domains but still recorded.

Pass condition: no singularity may be treated by spatial/thickness subdivision merely to make the algebra work.

### Stage B — construct a globally regular fixed-state thickness connection

Preferred first candidate is **source/matrix-level regularization**, not denominator-by-denominator scalar rationalization.

For a smooth matrix square-root atom `R=sqrt(G)`, use the source identity

`R R' + R' R = G'`

rather than separately rationalizing scalar coefficients such as `c0,c1`. For positive-definite smooth atoms this Sylvester map is globally invertible even when a scalar spectral basis degenerates. For general 2x2 matrix functions, use Cayley-Hamilton/divided-difference forms with their repeated-eigenvalue limits retained explicitly.

For any atom that contains a true R10 knot, do not silently smooth or approximate it. The theory must state whether the compact operator carries the knot exactly through an algebraic absolute-value/sign/divided-difference state or whether a genuine material event requires an additional source-level event rule.

Required pre-implementation output:

- exact state vector definition;
- exact state dimension `r_state`;
- exact/nonzero structure of the connection operator;
- proof that `r_state` does not increase with any series truncation order;
- proof that the known apparent pole `x=21/260` is removed in the physical connection;
- no enumeration of high-order coefficients.

If regularization requires an ever-growing basis, the route fails here.

### Stage C — close actual thickness targets, not a generic integration backend

After Stage B, immediately contract one **real structural target**, first `Pc` or one membrane residual `Rm_j`.

Let the fixed algebraic state be `V(zeta)` and target moments be

`M_n = integral_{-1}^{1} zeta^n V(zeta) dzeta`.

Derive a finite moment system/recurrence directly from the regular fixed-state connection and endpoint algebraic data. Do not canonicalize every component into a huge rational expression.

Before implementation, report:

- moment-state dimension;
- recurrence bandwidth/order;
- number of endpoint quantities;
- sparse solve size actually required for `Pc` and one `Rm_j`;
- expected per-state evaluation cost.

Important risk: a fixed 64-state field can still create a large moment system if the recurrence bandwidth is high. This is acceptable only if represented/solved as a compact sparse operator; materializing hundreds/thousands of symbolic scalar formulas is not acceptable.

### Stage D — derivative/tangent closure must be solved before Pu root work

Do not stop after obtaining `P` values. The same compact operator must return the derivatives required by the nonlinear solve:

- `dP/dD`, `dP/dq`, `dP/dr_j`;
- `dRq/dD`, `dRq/dq`, `dRq/dr_j`;
- `Krr=dRm/dr` and mixed derivatives;
- same-state material tangent contribution needed by `KZ`.

Preferred implementation is adjoint/Frechet pullback through the same fixed target DAG, or a bounded sensitivity-state augmentation. If derivatives require a second high-order enumerated representation, Stage C is not considered passed.

### Stage E — beta-weighted X,Y exact contraction

Only after thickness target closure passes, address the remaining in-plane contraction. The structural halfwave kinematics reduce the polynomial/trigonometric part to finite kernels; the material state remains compact.

The in-plane operator must directly contract the actual kernels needed by `P,Rq,Rm,KZ`, not build a universal symbolic integrator.

Possible mathematical form: beta-weighted moment recurrence / creative telescoping / finite holonomic operator after `u=sin^2 X`, `v=sin^2 Y`.

Mandatory preflight before implementation:

- telescoper/recurrence order for actual `P` and one `Rm_j` kernel;
- resulting state dimension after coupling to the 64-state material field;
- proof that this dimension is bounded and does not scale with a chosen Chebyshev truncation;
- endpoint/singularity handling at `u,v=0,1`;
- estimated evaluation cost.

If the required order explodes or requires thousands of enumerated coefficients, fail without opening a new backend chain.

### Stage F — only then start structural solution

First structural use is a low-cost control state, not a full Pu sweep. At one prescribed `(D,q,r)` state evaluate simultaneously:

`P, Rq, Rm_1...Rm_5, full required Jacobian/tangent pieces, KZ ingredients`.

Then perform independent audit against a high-precision numerical oracle that is explicitly non-formal. Formal counters remain zero.

Only after value + tangent identity/accuracy and runtime are acceptable may a connected branch/root solve begin.

## 2. Problems that may appear only when theory meets the actual nonlinear calculation

### P1. Apparent singularity is not the only singularity

The current known pole is removable, but shifted absolute-value/knot atoms may introduce true source non-smoothness. A basis that is globally regular for the smooth `eta` atom may still fail at a material knot. The source-level regularity classification in Stage A is therefore mandatory.

### P2. Moment recurrence may be finite but underdetermined or ill-conditioned

A holonomic moment relation can be exact yet fail to determine the required low moments uniquely from endpoints. Rank deficiency, nearly dependent equations, or very poor conditioning may appear only for actual `(D,q,r)` states.

Feedback to theory: change basis/normalization or use a different regular connection; do not increase truncation order.

### P3. Exact symbolic formulas may be compact on paper but slow numerically

Repeated root solves require many target evaluations. A method that takes tens of seconds/minutes per state is not a viable Pu engine even if mathematically exact.

Before root solving, benchmark one full target vector and derivative package. Caching/precompilation of state-independent operators should be part of the design.

### P4. Value closure may pass while tangent closure fails

This has already happened historically with N48. Therefore no target evaluator is accepted on stress/load values alone. The current material tangent and all generalized-coordinate derivatives must come from the same compact representation.

### P5. Branch choice of algebraic roots can change during continuation

Square roots, absolute values and divided differences require physical branch consistency. A branch label chosen at one state must not silently flip as `D,q,r` change. The runtime needs explicit branch-invariance/event checks derived from the source operator, not spatial sampling.

### P6. Five membrane coordinates are not the only future structural complication

Even with a correct material target engine, Z6 requires its mixed in-plane boundary-admissible Airy/homogeneous-biharmonic correction. This is a separate structural-physics task, not an excuse to alter the material backend.

The Z6 correction itself must obey the same anti-enumeration rule: a formal infinite Levy/Navier representation is acceptable, but production may not sum thousands of boundary harmonics. Before Z6 calculation, the boundary correction must be reduced to a compact finite harmonic/transfer representation or another bounded recurrence.

### P7. Reinforcement/steel branch events

Case21 steel may remain elastic, but other panels/Z6 can reach yield. A bilinear steel map introduces true material knots. The target architecture must allow exact/consistent branch handling without creating a spatial material-point grid.

### P8. Current ordinary-concrete compact state is R10-specific

The structural target API should not hard-code `64` as a universal material theory. For UHPC, the material compact state may be different. Reusable object should be:

`material compact state -> target functional interface -> General-D15 structural kernels`,

not the particular R10 quadratic tower itself.

### P9. Error certification must remain proportional to engineering need

Tight theorem-level remainder certificates are not a hard gate, but this does not mean unchecked numerics. Use source identities, residuals, value/tangent cross-checks and high-precision oracle comparisons sufficient to show target error is negligible relative to model/experimental uncertainty.

### P10. A future negative/implausible Pu must first trigger operator audit, not parameter tuning

If Case21/Z6 later gives the wrong membrane-effect trend, first inspect:

- target value/tangent consistency;
- algebraic branch selection;
- boundary-admissible membrane field;
- root/continuation identity;
- material event handling.

Do not retune R10 or fit membrane amplitudes to experiment.

## 3. Suggested approval gates for the user

No new work should start unless the user accepts the following sequence:

**Gate A:** approve source-level regularity classification and a bounded regular fixed-state connection design only. No target runtime yet.

**Gate B:** after seeing the exact state dimension and operator structure, approve implementation of one real thickness target (`Pc` or `Rm_j`) plus its derivative.

**Gate C:** after seeing actual runtime, rank/conditioning and oracle comparison, approve in-plane beta-weighted target contraction.

**Gate D:** after full target vector + tangent package passes at prescribed states, approve nonlinear branch/Pu calculation.

This prevents a local algebra problem from automatically authorizing another mathematical backend layer.

## 4. Items that should be explicitly decided before execution

1. Is matrix/source-level regularization (Sylvester + CH/divided-difference limits) preferred over a general algebraic integral-basis/Hermite algorithm?
2. What maximum compact state/moment operator size is acceptable before the route should be judged too cumbersome for the theory? This should be decided before implementation rather than after seeing a large system.
3. Is a high-precision numerical integration oracle allowed strictly for validation of a fixed state/target, while formal production counters remain zero?
4. For true material knots, should the formal theory retain exact absolute-value/sign operators with algebraic event logic, or is a source-supported smooth equivalent required? No decision is made in this draft.
5. Should Z6 mixed-boundary compact closure be completed before any new Case21 Pu, so the chosen target architecture is tested against the harder intended application rather than over-optimized for Case21?

## 5. Current draft recommendation

The highest-value next action, if approved, is **not** to write the final regularization immediately. It is to execute Gate A only: classify all three R10 generator singularities and derive two candidate globally regular fixed-state connections on paper, with exact state dimension and downstream moment complexity estimates. The candidates should include at least:

- source/matrix-level Sylvester + CH/divided-difference connection;
- a polynomial implicit/descriptor connection that avoids dividing by the removable discriminant.

Then compare them on: global regularity, fixed dimension, derivative availability, moment-recursion size, true-knot handling, and compatibility with later X,Y contraction.

Only one candidate should be selected for implementation after user review.
