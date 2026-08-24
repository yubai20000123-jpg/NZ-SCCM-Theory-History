# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-24 15:28 +08:00  
**Status:** `MARGUERRE_AIRY_EXPLICIT / Ny_My_RESULTANT_TERMINAL / R18_DIRECT_MA_TO_YUN_RESIDUAL_JACOBIAN_IMPLEMENTED / ANALYTIC_JACOBIAN_VERIFIED / NO_ABD_INTERMEDIATE / YUN_ALWAYS_ON / R07_R14_PRE_YUN_BASELINES / MULTI_UHPC_RERUN_NEXT / TC_ROUTE_WITHDRAWN / USER_ACCEPTANCE_PENDING`

> R18 executes the direct coupling requested after R17. The steel-shell path is now explicitly `Marguerre–Airy deformation -> steel strain -> Yun/Karman steel state -> sigma_s, Et,s -> equilibrium residual/Jacobian`. The previously introduced prerequisite `Yun -> current A/B/D -> equilibrium` is withdrawn. No specimen-level Yun activation gate exists.

## 0. Frozen architecture

```text
STRUCTURAL_FRONT = FULL_2D_MARGUERRE_AIRY
TERMINAL_OBJECT = AXIAL_Y_NORMAL_Ny_My
FORMAL_SPATIAL_QUADRATURE = 0
THICKNESS_QUADRATURE = 0
MATERIAL_POINTS = 0
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
TC_CC_TT_ROUTE = OFF_MAINLINE
YUN_STEEL_SHELL_MODULE = ALWAYS_ON
A_B_D_INTERMEDIATE_BEFORE_EQUILIBRIUM = NO
```

Current chain:

\[
\boxed{
(q,\alpha,\ldots)
\xrightarrow{\text{Marguerre--Airy explicit deformation}}
\varepsilon_s
\xrightarrow{\text{Yun steel shell}}
(\sigma_s,E_{t,s},A_i)
\xrightarrow{\text{direct virtual work}}
\mathbf R,\mathbf J
\rightarrow
(N_y,M_y)
\rightarrow P_u.
}
\]

No width/thickness ratio, `sigma_cr/f_y`, concrete `CC/TC/TT`, experiment, FEM or comparator is allowed to decide whether Yun is active.

---

## 1. R18 implementation

Report:

`semantic_v2/40_execution/20260824_1528__NZSCCM__DIRECT_MA_STRAIN_TO_YUN_RESIDUAL_JACOBIAN_R18.md`

Executable:

`semantic_v2/40_execution/steel_shell/20260824_1528__NZSCCM__DIRECT_MA_STRAIN_TO_YUN_RESIDUAL_JACOBIAN_R18.py`

Verification CSV:

`semantic_v2/40_execution/steel_shell/20260824_1528__NZSCCM__DIRECT_MA_STRAIN_TO_YUN_RESIDUAL_JACOBIAN_R18_RESULTS.csv`

The recovered historical Marguerre--Airy axial field is retained in the direct interface:

\[
e_y=-D+M(q)(u^2-u^2v^2)+\alpha B_A^y(u,v)+B(q)uv\zeta,
\]

\[
M(q)=\pi^2\left(q_0q+\frac12q^2\right),\qquad B(q)=2\pi^2q.
\]

The exact project `B_A^y` basis is supplied upstream; R18 does not invent or refit it.

The historical Yun/Karman steel strain is inserted directly:

\[
\varepsilon_s
=
\varepsilon_y^g
+A(w_{0,y}^g+\Delta w_{,y}^g)\phi_y
+A_0\Delta w_{,y}^g\phi_y
+\left(A_0A+\frac12A^2\right)\phi_y^2.
\]

Current minimal steel law:

\[
\sigma_s=\operatorname{clip}(E_s\varepsilon_s,-f_y,+f_y),
\qquad
E_{t,s}=\frac{d\sigma_s}{d\varepsilon_s}.
\]

Yielding changes the current steel constitutive state but does not delete Yun geometry or the local amplitude row.

---

## 2. Direct steel residual and Jacobian

For any global generalized coordinate `eta_i`, R18 now assembles the steel-shell contribution directly as

\[
\boxed{
R_i^s=t_s\int_{\Omega_s}\sigma_s\varepsilon_{s,i}\,d\Omega
}.
\]

The exact current Jacobian is

\[
\boxed{
K_{ij}^s
=t_s\int_{\Omega_s}
\left[
E_{t,s}\varepsilon_{s,i}\varepsilon_{s,j}
+\sigma_s\varepsilon_{s,ij}
\right]d\Omega
}.
\]

Therefore:

```text
CURRENT_A_B_D_MATRIX_AS_PREREQUISITE = REMOVED
DIRECT_SIGMA_TO_EQUILIBRIUM = IMPLEMENTED
DIRECT_ET_TO_JACOBIAN = IMPLEMENTED
CURRENT_STRESS_GEOMETRIC_TERM = IMPLEMENTED
```

The Yun local-amplitude equation is retained and coupled through the same current steel stress:

\[
R_A=C_\sigma[k_{cr}A+H(2A_0A+A^2)(A+A_0)]-\bar\sigma_c(A+A_0)=0.
\]

Its derivatives with respect to global coordinates and `A` are included analytically.

---

## 3. R18 verification result

High-order Gauss-Legendre integration is used only as a numerical derivative/oracle check. Formal production spatial quadrature remains zero.

### Entire strip elastic

```text
relative Jacobian error      = 8.379031701877e-11
max scaled entry error       = 4.753291751317e-08
global-global symmetry error = 2.201989822615e-18
PASS = TRUE
```

### Entire strip compressive-yielded

```text
relative Jacobian error      = 8.946410968662e-10
max scaled entry error       = 2.883829551726e-09
elastic fraction             = 0
global steel Jacobian norm   = 6625.932107842
PASS = TRUE
```

The yielded test proves the intended structural rule: even when ideal-EPP gives `Et=0`, the Yun steel shell remains in the equilibrium/Jacobian because the current-stress term

\[
\sigma_s\varepsilon_{s,ij}
\]

survives.

```text
ANALYTIC_JACOBIAN_VS_FINITE_DIFFERENCE = PASS
YIELDING_DELETES_YUN_GEOMETRY = NO
YIELDING_DELETES_STEEL_GEOMETRIC_TANGENT = NO
```

---

## 4. Production baselines and scope

R07 ordinary-concrete steel-shell and R14 UHPC steel-shell values remain available only as **PRE-YUN-REWIRE regression baselines**. R18 has not changed any production `Pu` yet.

```text
R07_PRE_YUN_BASELINE = RETAIN_FOR_REGRESSION_ONLY
R14_PRE_YUN_BASELINE = RETAIN_FOR_REGRESSION_ONLY
PRODUCTION_Pu_CHANGED_IN_R18 = NO
```

The direct steel kernel is now implemented; the remaining production work is to insert the exact existing project Marguerre--Airy basis/slopes, compile the finite analytic direct-steel terms with D15, and then solve the full coupled system.

---

## 5. UHPC adapter policy

Under the **same always-on Yun structural front**, the following existing UHPC core functions are to be tested in parallel:

```text
R08  full-fc block
R10A 0.85fc block
R11  FHWA strain-compatible
R12  R11 + Hiew tension
R14  Zhang peak strain-compatible
```

Two criteria are kept separate:

```text
IMPLEMENTATION_EASE != PHYSICAL_SUITABILITY
```

R10A is expected to be the simplest adapter; R14 remains the strongest current physical candidate. Neither is selected by implementation convenience or by test-value fitting.

---

## 6. Next task

```text
NEXT_TASK =
PROJECT_EXACT_MARGUERRE_AIRY_FIELD_ADAPTER
+ D15_COMPILE_DIRECT_YUN_STEEL_RESIDUAL_JACOBIAN
+ HISTORICAL_Z1_Z4_REGRESSION
+ Z0_Z6_RERUN
+ R08_R10A_R11_R12_R14_UHPC_ADAPTER_RERUN
```

Required order:

1. plug the exact project `B_A^y`, global slopes and generalized derivatives into the R18 operator;
2. D15-compile the direct steel residual/Jacobian so formal spatial quadrature remains zero;
3. reproduce historical Yun Z1/Z4 states as regression checks;
4. rerun Z0--Z6;
5. rerun T120/T360/BH under the same Yun front while switching only the UHPC core adapter;
6. report convergence/implementation complexity and physical prediction separately.

```text
USER_ACCEPTANCE = PENDING
```
