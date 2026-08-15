# NZ-SCCM — AR2 PF boundary membrane -> R10/N48/D15 mapping execution report

**Timestamp:** 2026-08-16 01:02 +08:00

## 1. Executed task

Executed

`AR2_PF_BOUNDARY_MEMBRANE_TO_R10_N48_D15_ZERO_QUADRATURE_MAPPING_GATE`.

No new AR2 Z6 Pu was calculated.

## 2. First decision: direct PF stress/function insertion is rejected

The 00:47 PF field contains non-integer complex-root functions and hyperbolic finite-length factors. They are an exact elastic boundary solution but are not finite members of the current integer-trigonometric General-D15 coefficient algebra.

More importantly, even if those elastic stresses could be integrated, directly feeding them into nonlinear concrete/steel would violate the frozen current-material chain.

Therefore:

```text
DIRECT_PF_ELASTIC_STRESS_AS_NONLINEAR_STRESS = PROHIBITED
DIRECT_FINITE_PF_HYPERBOLIC_FUNCTION_TO_CURRENT_D15_ARRAY = FAIL_FUNCTION_SPACE
```

## 3. Kinematic/variational bridge actually constructed

For AR2 `a=24000,b=12000,m=2,ell=b`, the physical lower half-panel is one complete out-of-plane halfwave. On `X=pi x/b`, `Y=pi y/ell`, construct the boundary-admissible integer-trigonometric in-plane family

```text
u_rs=(b/pi) U_rs cos(rX)[1-cos(sY)],  r odd,  s>=1
v_rs=(b/pi) V_rs cos(rX) sin(sY),     r even, s>=1
```

with strains

```text
u-mode:
 ex=-r U sin(rX)[1-cos(sY)]
 ey=0
 gxy=s U cos(rX)sin(sY)

v-mode:
 ex=0
 ey=s V cos(rX)cos(sY)
 gxy=-r V sin(rX)sin(sY)
```

The transverse displacement modes satisfy the actual physical-end `ux=0` condition exactly at `Y=0`; the internal `Y=pi` boundary is not assigned `ux=0`.

Every finite basis is a finite integer trig polynomial and therefore remains exactly in unchanged General D15.

## 4. Nonlinear current-material mapping

The correct nonlinear representation is

`epsilon = epsilon_D(D)+epsilon_g(q,q0)+sum_j r_j B_j + existing Nguyen curvature terms`.

For each material phase,

`sigma_p=M_p(epsilon_p)`

is evaluated by its current material law. Membrane coordinates are solved from

`R_j=sum_p int sigma_p:B_j dV=0`.

They are not assigned the elastic PF coefficients in the nonlinear regime.

At a stationary membrane state, `Rq` is the partial derivative at fixed `r`; no artificial `dr/dq` term enters first-order virtual work. The consistent tangent must include the ordinary q-r and r-r Jacobian blocks.

## 5. Elastic limit and direct connection to current D-q normalization

For the square AR2 halfwave define

`Gamma=pi^2 S/b^2`, `S=A^2+2A0A`.

The current coefficient is

`M=pi^2/eps0*(q0*q+q^2/2)`,

hence

`Gamma/eps0=2M`.

In the homogeneous elastic reference the exact finite-Ritz condensation is

`r=c_D D+c_G Gamma/eps0=c_D D+2 c_G M`.

This is a validation identity only. In R10/N48 the coordinates are independent unknowns.

The complete conforming Ritz space and the PF/Airy stress solution are two formulations of the same strictly convex elastic membrane minimization problem with the same transverse essential boundary/symmetry class. Therefore the complete-basis elastic limit is the PF/FvK solution by uniqueness.

## 6. Exact coefficient-space computation

The reproduction calculation used no spatial points. Trigonometric products were stored as finite Fourier coefficient dictionaries and integrated by

`int exp(i k theta)dtheta=(exp(i k L)-1)/(i k)`

with the exact `k=0` limit.

For `nu=.18` the following coefficient-space sequence was obtained:

```text
R=S  nmem   Q_GG             Q_DD             Q_DG
1      2    .710327899673    9.716401029828   -1.359305267256
2      8    .380985323731    9.661181203174   -1.280790283542
3     18    .338757150201    9.639425364487   -1.257398206363
4     32    .318834041670    9.628042047630   -1.246067137428
5     50    .307201717849    9.621103682835   -1.239421762215
6     72    .299568422262    9.616453853076   -1.235062292357
8    128    .290150329916    9.610639322927   -1.229696366445
10   200    .284558250341    9.607163461818   -1.226522139050
12   288    .280851744614    9.604857758524   -1.224424967309
```

All `Q_GG` are positive. Thus the D15-compatible lift preserves the positive postbuckling membrane-energy sign.

The pre-buckling D-driven correction is also captured automatically, not appended as a postbuckling-only correction. For `nu=.18`:

```text
fully free Poisson: Q_DD=(1-nu^2)pi^2=9.549829218494
fully transverse restrained: Q_DD=pi^2=9.869604401089
R=S=12 mixed-end Ritz: Q_DD=9.604857758524
```

The mixed-end value lies between the free and fully restrained limits, which is the expected physical ordering.

## 7. Intermediate elastic coefficient example

The companion JSON stores all 32 `R=S=4` coefficients separately for unit `Gamma/eps0` and unit D. They show explicitly that the boundary field is driven by **both** the pre-buckling axial shortening and the FvK nonlinear source.

This corrects an important incompleteness of treating the PF correction as only an S-driven postbuckling field: the same boundary-admissible membrane coordinates must respond to D already at q=0.

## 8. What passed

```text
NONLINEAR_KINEMATIC_MAPPING_ARCHITECTURE = PASS
PF_TO_CONFORMING_INTEGER_TRIG_RITZ_LIFT = PASS_FORMAL
GENERAL_D15_CLOSURE_FOR_EACH_FINITE_RITZ_LEVEL = PASS
ELASTIC_LIMIT_TO_PF/FVK = PASS_FORMAL_COMPLETE_BASIS
PREBUCKLING_D_DRIVEN_END_RESTRAINT = INCLUDED_IN_MAPPING
POSTBUCKLING_S_DRIVEN_REDISTRIBUTION = INCLUDED_IN_MAPPING
ZERO_SPATIAL_NUMERICAL_INTEGRATION = PASS
```

## 9. What did not pass yet

The gate does **not** release production nonlinear calculation:

```text
CURRENT_REDUCED_R10_N48_CODE_SUPPORTS_ARBITRARY_MEMBRANE_VECTOR = NO
PRODUCTION_MEMBRANE_RANK = NOT_FROZEN
FULL_ZHOU_ALL_INPLANE_END_DOF_EQUIVALENCE = OPEN
NEW_AR2_Z6_Pu = NOT_CALCULATED
```

The current reduced D15 implementation is specialized to the historical low-rank D-q(/c) algebra. General D15 as a theory can integrate the new finite trig basis, but the current R10/N48 code has not yet been rewritten to accept a vector of membrane coordinates and its generalized residual/Jacobian family.

Also, Zhou's `bottom uy=0` versus `top uy=unset` condition remains a separate asymmetric in-plane-end issue. The present Ritz lift closes the transverse `ux=0` end-restraint family and its symmetric one-halfwave mapping; it must not be relabelled as full all-DOF Zhou equivalence.

## 10. Fail-fast decision and next task

Because the all-in-plane boundary identity can change what one-halfwave kinematic space is admissible, it must be resolved **before** investing in the multi-coordinate nonlinear compiler.

Next gate:

`ZHOU_BOTTOM_UY0_TOP_UYFREE_ONE_HALFWAVE_COMPATIBILITY_ZERO_QUADRATURE_GATE`

Only if that gate permits a one-halfwave kinematic condensation should the project implement the generic multi-coordinate R10/N48/D15 membrane compiler and then perform coefficient-rank convergence before any new Pu.