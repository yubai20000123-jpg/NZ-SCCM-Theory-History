# NZ-SCCM — R10 global-order historical reconnection and intrinsic-scale governance lock

**Timestamp:** 2026-08-16 13:55 +08:00  
**Status:** `ACTIVE_GOVERNANCE / NO Pu RUN`

## 1. Scope

This gate was opened because a 3584-degree single-global Chebyshev representation is neither physically transparent nor structurally economical even if its source-fidelity gate can be passed.

The gate does **not** reopen the frozen R10 physical current operator and does not alter the project-wide mechanics:

```text
UNIFIED_PRODUCTION_WORKFLOW_V1
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order continuous kinematics
MEMBRANE_STRESS_REDISTRIBUTION = REQUIRED
same-state current stress + consistent tangent
General-D15 / approved exact-moment contraction
P,Rq,L connected-branch topology
same-state material + geometric KZ
formal structural spatial sampling = 0
formal structural spatial quadrature = 0
formal structural subdomains = 1
formal thickness quadrature = 0
```

No Z0-Z6 load, experiment, Zhou or Winter value is used in the material representation diagnosis.

## 2. Historical reconnection

The following earlier project events are controlling evidence:

1. **R5 material compiler:** an N600 factorized material object was material-faithful, but naive nested expansion into D15 caused expression swell. The accepted lesson was target-functional / moment-first contraction, not reintroduction of spatial quadrature.
2. **M1R/PF1/P2A:** rational, algebraic-period and single-global-polynomial compiler experiments were representation experiments inside the same current-map route. Their failure did not imply a material-architecture failure.
3. **NC energy-potential gate:** the project explicitly rejected rescue by hidden high-degree/global coefficient inflation after low-order global polynomial grammars produced unacceptable stress/tangent behavior.
4. **R10:** the successful material simplification was a low-parameter one-dimensional C2 quintic energy smoothing reinserted into the same multidimensional current operator, not a large free coefficient surface.

Therefore the project shall not interpret `N=3584` as a reason to build a 3584-order production theory if a lower-complexity intrinsic material factorization exists.

## 3. Quantitative intrinsic-scale diagnosis

For the current R10 reference:

```text
kappa = 2.0005129533678754
rho   = .1
xcr   = .04998717945397425
eta   = xcr/20 = .0024993589726987125
core  = [-2.35,+1.90]   width = 4.25
guard = [-2.60,+2.15]   width = 4.75
```

Hence

```text
core_width / eta  = 1700.4360
guard_width / eta = 1900.4873
```

The global polynomial is therefore being asked to resolve a material transition scale about three orders of magnitude smaller than the family interval.

The R10 tensile scalar itself is locally simple. In the natural coordinates `tau=t/xcr` and `s=(t-xcr)/(9*xcr)` it is only two quintics plus a constant branch:

```text
u1(tau) coefficients = [0, .1, 0, .37997504272, -.66996256408, .28798502563]
u2(s)   coefficients = [.09799750427, 0, 0, -.67997504272, 1.01996256408, -.40798502563]
```

It is C2 at the two joins, while the third derivative jumps are approximately

```text
at t=xcr:    -2.7905034e4
at t=10xcr:  +4.4806477e1
```

Thus a single global polynomial must resolve both the narrow algebraic sign split `Pi_eta` and finite-smoothness C2 joins even though the underlying source description has very few parameters.

## 4. Direct numerical localization of the global-order pressure

On the frozen wide family interval, the `Pi_eta` sign-split alone remains difficult for a single lambda-space polynomial. At N=3584 its maximum derivative error is still approximately

```text
t(lambda)=Pi_eta(lambda):       5.8583e-2
c(lambda)=Pi_eta(-lambda):      5.8308e-2
```

For the full primitive channels at N=3584:

```text
C derivative max error  ~= 1.3771e-1   near lambda ~= -0.00283
T derivative max error  ~= 1.3749      near lambda ~= +0.00291
T7 derivative max error ~= 9.3684e-2   near lambda ~= +0.04955
```

The largest C/T derivative errors therefore localize around the intrinsic `eta` transition, not throughout the compression range.

## 5. Natural-coordinate counterfactual screen

A material-only counterfactual was executed to determine whether R10 itself intrinsically requires thousands of polynomial coefficients.

The screen keeps `Pi_eta` **exact** and approximates only smooth source factors in their own natural coordinates:

- `C(c)` on the physical compression coordinate `c`;
- `u_R(t)` on the tensile coordinate `t`;
- reconstruct `T=u_R/rho`, `T7=T^7`, and `U` from the same factors.

No structural integration is performed in this screen.

Results:

```text
C(c), N=6:   derivative error / peak derivative ~= 3.8826%
C(c), N=10:  derivative error / peak derivative ~= 0.1729%

u_R(t), N=64: derivative error / peak derivative ~= 3.5857%
```

A combined material-only screen with exact `Pi_eta`, `N_C=6` and `N_u=64` gives the assembled current-map errors

```text
E_sigma = 0.003337
E_tangent = 0.030469
E_divided_difference = 0.046869
```

which passes the same material gates

```text
E_sigma <= .005
E_tangent <= .05
E_divided_difference <= .05
```

using only `7 + 65 = 72` fitted scalar coefficients, versus `4*(3584+1)=14340` coefficients in the single-global four-channel representation.

This 72-coefficient object is **not** a production compiler because exact `Pi_eta` has not yet been contracted through the formal zero-spatial-integration structural backend. It is a diagnostic proof that the 3584 order is primarily a representation-coordinate problem rather than intrinsic R10 material complexity.

## 6. Governance decision

Effective immediately:

```text
R10_PHYSICAL_OPERATOR = UNCHANGED
N3584_SOURCE_FIDELITY_EVIDENCE = RETAINED
N3584_AS_NEXT_PRODUCTION_BASIS = REJECTED
N3584_GLOBAL_LAMBDA_COMPILER = DIAGNOSTIC_ONLY
NEW_Z0_Z6_Pu = NOT_RUN
```

The earlier 12:29 N3584 result remains valid as an **upper-bound representability/source-fidelity witness**. It is no longer the preferred basis for production backend engineering.

## 7. New unique next gate

```text
UNIFIED_V1_R10_INTRINSIC_SCALE_FACTORIZED_PI_ADAPTER_GATE
```

The next gate must:

1. keep R10 physical equations unchanged;
2. preserve one common NC method for NC+rebar, NC+shell and Z0-Z6;
3. organize the material representation around intrinsic source factors and material coordinates rather than one wide lambda-space global polynomial;
4. specifically solve the `Pi_eta` / sign-split-to-exact-moment adapter problem;
5. retain the same stress/tangent/divided-difference material gates;
6. demonstrate General-D15 or another already-approved zero-spatial-integration contraction before any Pu run;
7. remain low-parameter and auditable;
8. prohibit case-specific intervals/orders, Z6-only fallbacks and structural-response calibration.

If exact R10 cannot be contracted in this low-complexity factorized form, only then may a separate user-authorized material-regularization gate reopen the width/shape of the tensile transition corridor. That is not authorized by this lock.
