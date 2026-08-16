# NZ-SCCM — R10 exact finite-matrix source lift execution report

**Timestamp:** 2026-08-16 20:05 +08:00  
**Gate:** `UNIFIED_V1_NC_EXACT_NESTED_ATOM_MOMENT_CLOSURE_OR_STRUCTURALLY_CLOSED_COMPILER_REDESIGN_GATE`  
**Result:** `EXACT_SOURCE_LIFT_PASS / FIXED_ALGEBRAIC_ATOM_REDUCTION_PASS / STRUCTURAL_MOMENT_CLOSURE_OPEN / NO Pu RUN`

## 1. Inputs retained

```text
UNIFIED_PRODUCTION_WORKFLOW_V1
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order continuous kinematics
five compatible membrane internal coordinates
R10 physical current operator = frozen
reinforcement adapter = unchanged
Cayley-Hamilton / finite matrix lift = allowed
General-D15 zero-spatial-integration target framework = retained
P,Rq,L connected-branch topology = retained
same-state tangent/KZ requirement = retained
```

The 19:32 result is inherited:

```text
ADJOINT_CLENSHAW_ALGEBRA = PASS_EXACT
ACTIVE_RC1_NESTED_TARGET_RUNTIME = FAIL_PREFLIGHT
```

No nested RC1 flattening was attempted again.

## 2. Exact source-law reduction executed

The frozen scalar R10 source was rewritten before structural integration:

1. `pi(±lambda)` -> one exact matrix square-root source split `Pi(±E)`;
2. compression `C(c)` -> exact 2x2 rational matrix function;
3. the three-branch `uR(t)` law -> one exact degree-5 truncated-power spline with knots `t/a=1,10`;
4. `T7` -> exact matrix power `T^7`, eliminating the independent T7 material fit;
5. the two-principal-value R10 interaction -> one invariant 2x2 matrix stress identity.

No source parameter, specimen response, or experimental capacity entered this reduction.

## 3. Symbolic spline identity

The reproducer uses symbolic algebra for the truncated-power coefficients and obtains

```text
SPLINE_INTERVAL_1_TO_10_RESIDUAL = 0
SPLINE_INTERVAL_ABOVE_10_RESIDUAL = 0
```

Thus the representation is exactly the existing R10 tension-return source law, not a refit.

Dimensionless coefficients are

```text
A3 = 4*rho + (-7300*H + 10*UR)/729
A4 = 7*rho + (-32800*H - 5*UR)/2187
A5 = 3*rho + (-118100*H + 2*UR)/19683
B3 = 10*(H-UR)/729
B4 = 5*(H-UR)/2187
B5 = 2*(H-UR)/19683
```

For the frozen `rho,H,UR`:

```text
A3 = -0.5809077931212661
A4 = -0.7698071056793392
A5 = -0.28799193489407166
B3 =  0.0009327504015359809
B4 =  0.00015545840025599682
B5 =  0.000006909262233599859
```

## 4. Matrix identity audit

For every Z0-Z6 case, 500 deterministic random symmetric 2x2 states were generated with both eigenvalues inside that case's existing RC1 guard domain.

The invariant matrix stress was compared with direct evaluation of the frozen scalar principal-value R10 stress followed by rotation back to the same basis.

Maximum infinity-norm discrepancies:

|case|max R10 matrix-stress identity error|max algebraic `Pi(E)` error|
|---|---:|---:|
|Z0|6.27e-15|3.78e-12|
|Z1|6.67e-15|1.53e-11|
|Z2|5.82e-15|4.91e-11|
|Z3|5.72e-15|6.67e-11|
|Z4|5.63e-15|4.66e-12|
|Z5|8.05e-15|1.92e-11|
|Z6|4.93e-15|3.67e-11|

The stress identity is at floating roundoff. The slightly larger `Pi(E)` residual is numerical conditioning/cancellation in the explicit matrix formula near the smoothed zero split; the algebraic identity itself follows spectrally from the scalar definition.

## 5. Structural complexity consequence

The structural candidate no longer contains the RC1 fit-order hierarchy

```text
Ng,Nc,Nt
beta-lens -> Chebyshev -> beta-lens -> Chebyshev
separate T7 fit
```

The fixed non-polynomial atom families are only

```text
sqrt(E^2+eta^2 I)
inverse(I+(kappa-2)c+c^2)
(t/a-I)_+^k,   k=3..5
(t/a-10I)_+^k, k=3..5
```

All remaining source operations are finite 2x2 matrix polynomial/invariant operations.

Therefore the previous active RC1 composition degrees up to `~1.708e9` are no longer relevant to this candidate source graph.

This does **not** mean the structural moment problem is solved. The new problem is a fixed algebraic-atom target-moment problem, independent of material approximation order.

## 6. Tangent status

The consistent tangent remains in the same finite graph through exact Frechet rules:

```text
d(Q^-1) = -Q^-1 (dQ) Q^-1
R dR + dR R = dA        for R=sqrt(A)
d(T^7) = sum_{k=0}^6 T^k dT T^(6-k)
d(det X) = adj(X):dX
```

No numerical material tangent was introduced.

## 7. Formal integration counters

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
Gauss=0
Simpson=0
adaptive=0
collocation=0
material-point grid=0
```

The random matrices used in this report are a **material algebra identity audit only** and are not structural spatial points.

## 8. Capacity boundary

```text
new current membrane r(D,q) solve = NOT_RUN
new Case21 Pu = NOT_RUN
new Z0-Z6 Pu = NOT_RUN
```

Historical/current-support capacities retain their prior identities only.

## 9. Gate verdict

```text
R10_EXACT_SMOOTH_SPLIT_MATRIX_LIFT              = PASS_EXACT
UR_TRUNCATED_POWER_SPLINE                       = PASS_EXACT
R10_2D_STRESS_INVARIANT_MATRIX_IDENTITY         = PASS_EXACT
CONSISTENT_TANGENT_FINITE_GRAPH                 = PASS_FORMAL
INDEPENDENT_T7_COMPILER_CHANNEL                 = ELIMINATED
MATERIAL_FIT_ORDER_DEPENDENCE_IN_SOURCE_GRAPH   = ELIMINATED
FIXED_ALGEBRAIC_ATOM_GRAPH                      = PASS_FORMAL
GENERAL_D15_ALGEBRAIC_ATOM_MOMENT_CLOSURE      = OPEN
NEW_Pu                                          = NOT_RUN
```

## 10. Next gate

```text
UNIFIED_V1_R10_FIXED_ALGEBRAIC_ATOM_GENERAL_D15_CAS_MOMENT_CLOSURE_GATE
```

The next run should attack the fixed atom moment closure in increasing difficulty:

1. `sqrt(E^2+eta^2 I)`;
2. `inverse(I+(kappa-2)c+c^2)`;
3. `(t/a-I)_+^k`;
4. `(t/a-10I)_+^k`;
5. same target backend for `P,Rq,Rm,KZ`.

No Pu is allowed before that closure.
