# NZ-SCCM H4→H6 pre-frozen no-experiment convergence gate

Timestamp: 2026-08-21 10:49 +08:00
Status: PRE-FROZEN BEFORE H6 RESULTS
Material operator: NC-M6 FROZEN

## 1. Purpose

The sole purpose of H4→H6 is to decide whether H4 is a sufficient production membrane subspace. Experimental ultimate loads are prohibited from order selection, mode selection, root selection, or tolerance adjustment.

No H4 production claim is authorized before this gate is evaluated.

## 2. Nested spectral spaces

Use the same admissible even-harmonic family. Let p denote the spectral level with maximum even harmonic 2p.

H2 corresponds to p=1.
H4 corresponds to p=2.
H6 corresponds to p=3.

The general in-plane fields are

u(x,y) notation avoided here; use u and v:

u_u = eps0 [ eta*x + sum_{m=1..p} sum_{n=0..p} b/(2 m pi) a_{2m,2n} sin(2mX) cos(2nY) ]

v = eps0 [ -D*y + sum_{m=0..p} sum_{n=1..p} ell/(2 n pi) b_{2m,2n} cos(2mX) sin(2nY) ]

with the family-specific essential boundary treatment retained exactly.

The spaces are nested:
H2 subset H4 subset H6 subset ...

No empirical coefficient is introduced by increasing p.

## 3. Formal identities that may not change during this audit

- NC-M6 material operator
- ONE_CONTINUOUS_COMPLETE_HALFWAVE
- active out-of-plane halfwave and Nguyen second-order/von-Karman kinematics
- section/phase definitions
- actual in-plane boundary conditions for each structural family
- exact formal moment engine / zero formal spatial quadrature identity
- source-consistent material tangent
- consistent residual and Jacobian construction
- origin-connected branch identity
- experimental data excluded from the order gate

## 4. H4→H6 acceptance observables

The H4 order is accepted only if H4 and H6 agree on the same origin-connected branch within ALL of the following pre-frozen tolerances:

1. Ultimate load:
   delta_P(H4,H6) <= 0.5%

2. Ultimate axial generalized state:
   delta_D(H4,H6) <= 0.5%

3. Ultimate out-of-plane amplitude:
   delta_w(H4,H6) <= 1.0%

4. Midsurface membrane strain field:
   delta_epsilon(H4,H6) <= 2.0%

5. Branch identity:
   no branch jump, disconnected root switch, or different fold branch may be used to manufacture convergence.

6. Audit-localizer stability:
   decimal-localizer refinement must change Pu by less than 0.05% for any specimen used to reject H4 on the basis of a small H4/H6 difference.

## 5. Field metric

Use a normalized full-domain L2 metric on the midsurface membrane strain vector e_m=[e_x,e_y,gamma]^T:

Delta_epsilon = ||e_m^(H6)-e_m^(H4)||_L2 / max(||e_m^(H6)||_L2, epsilon_floor).

The same physical domain and normalization must be used for all specimens. The metric is evaluated from the continuous analytic fields; audit quadrature may localize its decimal value but is not part of the formal operator.

## 6. Decision logic

H4 may be frozen as the production membrane subspace only if every required structural family/sample satisfies all pre-frozen criteria.

If any decisive specimen fails a criterion after audit-localizer independence is established:
- H4_PRODUCTION_FREEZE = NO
- advance exactly one level to H6→H8
- do not modify NC-M6
- do not modify the tolerances after viewing results
- do not insert empirical restraint factors or fitted harmonic weights

If all pass:
- H4_PRODUCTION_FREEZE = YES
- stop spectral enrichment
- H6 remains an audit reference, not a production DOF set

## 7. Computational discipline

The order study may exploit block structure, parity, exact moments, and symbolic index algebra. It may not use experimental ultimate load as a convergence target.

A pseudo-arclength/augmented continuation coordinate is allowed solely to trace the same equilibrium manifold through folds. It is not a structural generalized coordinate and is not included in the physical Ritz order.

## 8. Current status at freeze time

H2_GLOBAL_FREEZE = NO
H4 = ACTIVE CANDIDATE
H6 = NEXT AUDIT SPACE
H4_PRODUCTION_FREEZE = UNRESOLVED
H4_TO_H6_GATE = FROZEN BEFORE RESULTS
