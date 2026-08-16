# NZ-SCCM — full R10 64-state adjoint/CH target execution report

**Timestamp:** 2026-08-16 21:18 +08:00  
**Gate:** `UNIFIED_V1_FULL_R10_64_STATE_ADJOINT_RATIONAL_TARGET_REDUCTION_GATE`

## 1. Execution objective

Continue from the 20:59 fixed 64-state quadratic-tower field without flattening/canonicalizing the 64 rational coefficient functions. The execution tested whether the actual R10 structural stress target can be reduced target-side.

No `P`, `Rq`, `Rm`, `KZ` or `Pu` root solve is performed in this gate.

## 2. Exact algebraic changes executed

The 2x2 Cayley–Hamilton recurrence

```text
b0=0
b1=1
bn=t*b(n-1)-d*b(n-2)
T^n=bn*T-d*b(n-1)*I
```

was specialized to `n=7` and the exact identity

```text
adj(T^7)=b8*I-b7*T
```

was substituted into the frozen R10 stress graph.

This removes the full matrix `T7` node from the production target DAG.

The compact stress used in the execution is

```text
S=U-ACC*det(C)*C+C*adj(T)-rho*AT*det(T)*(b8*I-b7*T)
```

with component formulas recorded in the theory file.

## 3. Adjoint field-product runtime

For field basis products

```text
e_i*e_j=sum_k m_ij^k e_k
```

a target row is pulled through a multiplication node by the exact transpose action of the multiplication tensor. The implementation therefore contracts the target before a final product coefficient vector is canonicalized.

For the `Syy` target the executed contraction was

```text
lambda(Uyy)
-ACC*lambda(detC*Cyy)
+lambda(Cyy*Txx)
-lambda(Cxy*Txy)
-rho*AT*lambda(detT*b8)
+rho*AT*lambda(detT*b7*Tyy)
```

where each product target is evaluated by repeated field-product pullback.

## 4. Prototype and audit fibers

Retained noncommuting prototype:

```text
E(x)=[[1/5+x/3,1/7+x/5],
      [1/7+x/5,-1/4+2*x/7]]
```

Runtime material constants:

```text
rho=1/10
kappa=2
eta=1/400
```

As in the 20:59 timing probe, knot locations were rationalized only for deterministic exact-rational execution. Formal theory retains the exact R10 roots.

Exact rational audit fibers:

```text
x=0
x=1/2
```

Deterministic dual seed:

```text
lambda_i=((i mod 7)-3)/11
```

At both fibers:

```text
Syy field support = 60/64
b7 support        = 64/64
b8 support        = 64/64
Syy adjoint - direct materialized Syy = 0 exactly
```

At `x=0`, the complete 2x2 CH stress and the previously materialized matrix-`T7` stress agreed entry-by-entry with exact zero field residual.

## 5. Runtime diagnostics

```text
x=0
old binary-T7 forward+reverse target = 14.896949290531248 s
CH b7/b8 build                       =  3.802583932876587 s
compact target pullback              =  1.3008992671966553 s
CH total                             =  5.103483200073242 s
old/CH                               =  2.9189768452682388

x=1/2
old binary-T7 forward+reverse target = 17.459341049194336 s
CH b7/b8 build                       =  4.015377521514893 s
compact target pullback              =  1.6652381420135498 s
CH total                             =  5.680615663528442 s
old/CH                               =  3.0734945089296337
```

These times are implementation diagnostics only. The formal result is the exact reduction and exact zero audit residual.

## 6. Formal structural counters

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
Gauss=0
Simpson=0
adaptive_spatial_quadrature=0
collocation=0
material_point_grid=0
```

The two rational thickness fibers are algebraic implementation audits. They are not structural quadrature points and are not used to evaluate any resultant or capacity.

## 7. Fail-fast boundary

The algebraic target graph is now compact and no final 64-coefficient `cancel` pass is required. However the actual thickness functional contains x-dependent rational coefficient actions. A target pullback over the algebraic field is not yet, by itself, a completed holonomic thickness integral.

Therefore the gate stops before any new structural resultant.

```text
FULL_R10_ALGEBRAIC_TARGET_REDUCTION = PASS_EXACT
FULL_R10_DUAL_HOLONOMIC_THICKNESS_MOMENT_RUNTIME = OPEN
BETA_WEIGHTED_XY_RUNTIME = OPEN
NEW_CURRENT_MEMBRANE_r_SOLVE = NOT_RUN
NEW_Pu = NOT_RUN
```

## 8. Next gate

```text
UNIFIED_V1_FULL_R10_DUAL_HOLONOMIC_THICKNESS_MOMENT_RUNTIME_GATE
```
