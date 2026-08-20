# NZ-SCCM — Q&A history and current frontier: direct kinematics → theta-free TC P6 → full-expansion audit

**Date:** 2026-08-20 11:16 +08  
**Identity:** USER-REQUESTED SAFETY BACKUP / CURRENT FRONTIER BEFORE FULL EXPANSION AUDIT

## 1. Why this checkpoint exists

The user requested an immediate GitHub backup before continuing the derivation. This file records the causal path and the exact current open question so a later chat does not restart obsolete routes.

## 2. Q&A progression since the 20260820_0048 pause checkpoint

The user deliberately stepped backward from R10/R13 abstractions and rebuilt the structural theory from physical variables.

### 2.1 Direct continuous second-order kinematics

The working physical variables were reduced to axial shortening `Delta`, current total deflection amplitude `A`, initial imperfection `A0`, geometry `(b, ell, t)`, and Poisson ratio `nu`; old transformed coordinates such as `q`, `alpha`, `D` were intentionally avoided in the Q&A derivation.

Base fields:

```text
w0 = A0 sin(pi x/b) sin(pi y/ell)
w  = A  sin(pi x/b) sin(pi y/ell)
```

The von-Karman/Nguyen continuous strains were written explicitly over

```text
0 <= x <= b
0 <= y <= ell
-t/2 <= z <= t/2
```

and then augmented by one membrane-redistribution amplitude `epsilon_m`, giving a three-variable structural state

```text
(Delta, A, epsilon_m).
```

This is a structural generalized coordinate set only; no spatial material points or quadrature were introduced.

### 2.2 Limit-state equations

The structural equilibrium/limit formulation was written as

```text
R_A(Delta,A,epsilon_m) = 0
R_m(Delta,A,epsilon_m) = 0
L(Delta,A,epsilon_m)   = 0
Pu = P(Delta_u,A_u,epsilon_m,u)
```

with

```text
L = P_Delta (R_A,A R_m,m - R_A,m R_m,A)
  - P_A     (R_A,Delta R_m,m - R_A,m R_m,Delta)
  + P_m     (R_A,Delta R_m,A - R_A,A R_m,Delta).
```

Thus the structural limit-state definition itself is no longer the unresolved issue.

### 2.3 Principal-direction diagnostic

Independent Gauss diagnostics were used only as a diagnostic, not as formal theory. The diagnostic showed that forcing x/y to remain principal material directions changes Case21 capacity materially (roughly -14% RC and roughly -22% to -23% concrete-only), therefore physical principal-direction rotation cannot be discarded.

### 2.4 Angle formulation and exact cancellation

Instead of immediately using the eigenvalue radical, the principal strain transformation was retained as

```text
e1 = (ex+ey)/2 + [(ex-ey) cos(2theta) + gamma sin(2theta)]/2
e2 = (ex+ey)/2 - [(ex-ey) cos(2theta) + gamma sin(2theta)]/2
```

with

```text
(ex-ey) sin(2theta) - gamma cos(2theta) = 0
cos^2(2theta) + sin^2(2theta) = 1.
```

For constitutive branches satisfying

```text
sigma1 - sigma2 = (e1-e2) H(symmetry invariants),
```

the identities

```text
(e1-e2) cos(2theta) = ex-ey
(e1-e2) sin(2theta) = gamma
```

remove `theta` exactly from stresses and virtual work. This is a true elimination, not a hidden square root.

### 2.5 CC and TT status

A low-degree conservative compression replacement was constructed for the Saenz peak-before branch. The scalar cubic candidate

```text
psi_P(c) = kappa c + (3-2 kappa)c^2 + (kappa-2)c^3
```

matches origin, initial tangent, peak value, and zero peak tangent. A simple CC coupling candidate

```text
g_CC = 1 + (13/80)c1 c2
```

was constructed to remain below the Foster/Kupfer biaxial envelope in the audited normalized range. In invariant form the CC branch becomes finite polynomial and theta-free.

The affine TT tension-stiffening branch also removes theta exactly because both principal directions use the same affine spectral law.

### 2.6 Rejection of the first TC simplification

Earlier TC-12 / TC-19 candidates of the form

```text
compression = source-like compression polynomial × (1-k tensile strain)
```

were useful only as work/area targets. They were rejected as final analytic TC laws because they still left the local principal-direction field `theta` in the structural equations. The user explicitly ruled this out: a TC simplification that preserves theta is a failed simplification even if its material work is acceptable.

### 2.7 Theta-free TC polynomial family

The TC branch was then constrained to the form

```text
(sigma1+sigma2)/fc = S(u,v)
(sigma1-sigma2)/fc = ((e1-e2)/epsilon0) H(u,v)
```

where, purely as algebraic abbreviations,

```text
u = (ex+ey)/epsilon0
v = (ex ey - gamma^2/4)/epsilon0^2.
```

This guarantees

```text
sigma_x = fc/2 [ S + (ex-ey)/epsilon0 H ]
sigma_y = fc/2 [ S - (ex-ey)/epsilon0 H ]
tau_xy  = fc/2 [ gamma/epsilon0 H ]
```

with zero occurrence of `theta`, principal-value square roots, or local material Newton iterations.

### 2.8 P5 rejected; P6 retained only as current candidate

A degree-5 family was judged insufficient under the combined shape/monotonicity/conservatism gates. A degree-6 stress family, written as `S6(u,v)` and `H5(u,v)`, was obtained as the first current candidate family able to satisfy the imposed theta-free structure and the tested material-shape gates.

The current coefficient list used in the Q&A is:

```text
S6 =
-0.288140089464 u
-0.542278080987 u^2
+6.31827473271 v
+5.91234493680 u^3
-9.94730818043 u v
+1.01245771241 u^4
-19.2185389546 u^2 v
+19.1832565685 v^2
-11.9665567327 u^5
+32.6450661521 u^3 v
-12.2416050311 u v^2
-7.77171839681 u^6
+35.0666522000 u^4 v
-46.1298898831 u^2 v^2
+12.2875520048 v^3

H5 =
+0.707860080998
-1.56213951823 u
-2.13088117636 u^2
-1.61528115652 v
+0.647002277583 u^3
-3.94766000779 u v
+5.50566809591 u^4
+1.24374689900 u^2 v
-8.32800220624 v^2
+3.92558746177 u^5
-1.09415617589 u^3 v
-15.4106619095 u v^2.
```

Important governance status: these numbers are **not yet frozen production constants**. Their stated origin is a constrained material-space polynomial regression against the Nguyen TC reference family, but the complete final optimization ledger (`B`, target vector, weights, all sample points, all inequality rows, solver tolerances) was not yet committed as a reproducibility package. Therefore their current identity is

```text
TC_THETAFREE_P6_COEFFICIENTS = PROVISIONAL / NOT FULLY REPRODUCIBLE YET.
```

### 2.9 General rectangular plate requirement

The user explicitly rejected treating `b=ell` as theory. From this checkpoint forward, derivations must keep

```text
b != ell in general
```

and use the full domain

```text
0 <= x <= b
0 <= y <= ell
-t/2 <= z <= t/2.
```

Case21 `b=ell` is validation-only and cannot be used to simplify the general theory.

## 3. Current active dispute / audit target

The immediately preceding assistant answer claimed that, although each CC/TC/TT branch is polynomial after theta elimination, moving CC/TC/TT state regions might still obstruct one-shot fixed-domain integration.

The user correctly challenged the wording and demanded a direct algebraic test:

```text
After complete substitution there are no stress symbols left, only strain expressions.
Do not invoke a vague 'stress-region' blocker.
Fully expand the actual coupled equations first and see whether any branch/state selector really remains.
```

Therefore the unique next audit is:

1. substitute the theta-free TC P6, polynomial CC, and affine TT expressions all the way into `P`, `R_A`, and `R_m` for a general rectangle `(b,ell,t)`;
2. distinguish carefully between
   - stress symbols, which should indeed disappear, and
   - constitutive branch selection, which may or may not remain as strain-sign conditions;
3. do **not** assume a moving-state-front obstruction in advance;
4. if the fully expanded operator is a single global polynomial in `(ex,ey,gamma)`, integrate it directly by exact trigonometric/thickness moments;
5. if piecewise selectors remain, identify the exact unreduced selector and prove why it cannot be removed by the current formulas.

## 4. Current status flags

```text
GENERAL_RECTANGLE_KINEMATICS                 = ACTIVE
STRUCTURAL_STATE_VARIABLES                   = (Delta,A,epsilon_m)
PRINCIPAL_ROTATION_PHYSICS                   = MUST_RETAIN
CC_THETA_ELIMINATION                         = PASS
TT_THETA_ELIMINATION                         = PASS
TC_THETA_ELIMINATION                         = PASS FOR P6 FORM
TC_P6_COEFFICIENTS                           = PROVISIONAL
TC_P6_FULL_REPRODUCIBILITY_LEDGER            = MISSING
FORMAL_SPATIAL_QUADRATURE                    = 0 REQUIRED
FORMAL_MATERIAL_POINTS                       = 0 REQUIRED
CASE21_B_EQUALS_ELL_AS_THEORY                 = PROHIBITED
FULLY_EXPANDED_GLOBAL_OPERATOR_AUDIT          = NEXT / ACTIVE
MOVING_STATE_FRONT_AS_PROVED_BLOCKER          = NOT YET ESTABLISHED
FINAL_GENERAL_PLATE_CLOSED_FORM_SYSTEM        = NOT YET CLAIMED
FINAL_CASE21_Pu                               = NOT RELEASED
```

## 5. Do-not-restart list

Do not restart genus-3 machinery, explicit principal-value radical integration, principal-direction suppression, spatial Gauss/Simpson/cells, or specimen-specific material fitting. The current question is narrower: fully expand the already theta-free material branches inside the general rectangular-plate equilibrium/limit equations and determine what, if anything, still prevents exact fixed-domain closure.
