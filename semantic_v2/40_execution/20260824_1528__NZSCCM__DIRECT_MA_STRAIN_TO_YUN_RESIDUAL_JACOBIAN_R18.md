# NZ-SCCM — Direct Marguerre–Airy strain → Yun steel-shell residual/Jacobian R18

**Time:** 2026-08-24 15:28 +08:00  
**Status:** `EXECUTED / DIRECT_STRAIN_TO_STRESS_TO_EQUILIBRIUM_KERNEL_IMPLEMENTED / ANALYTIC_JACOBIAN_VERIFIED / NO_ABD_INTERMEDIATE / FULL_Pu_RERUN_NOT_YET_EXECUTED`

## 0. Purpose

R18 executes the corrected instruction:

\[
\boxed{
\text{Marguerre–Airy explicit deformation}
\rightarrow
\varepsilon_s
\rightarrow
\text{always-on Yun steel shell}
\rightarrow
(\sigma_s,E_{t,s})
\rightarrow
\text{equilibrium residual/Jacobian}
}
\]

The previously proposed prerequisite

\[
\text{Yun state}\rightarrow A/B/D\rightarrow\text{equilibrium}
\]

is removed. No current laminate-style \(A/B/D\) matrix is required before assembling the steel-shell residual.

```text
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
YUN_ALWAYS_ON = YES
A_B_D_INTERMEDIATE = NO
WIDTH_THICKNESS_ACTIVATION_GATE = NO
SIGMA_CR_OVER_FY_ACTIVATION_GATE = NO
CC_TC_TT_GATE = NO
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
```

The high-order Gauss-Legendre integration in the executable is a **verification oracle only** for checking the direct chain rule/Jacobian. It is not the formal production integration route.

## 1. Upstream Marguerre–Airy explicit strain

The historical project relation recovered from the 2026-08-18 Yun execution is

\[
e_y
=
-D+M(q)(u^2-u^2v^2)+\alpha B_A^y(u,v)+B(q)uv\zeta,
\]

\[
M(q)=\pi^2\left(q_0q+\frac12q^2\right),
\qquad
B(q)=2\pi^2q,
\qquad
\varepsilon_y^g=\varepsilon_0e_y.
\]

R18 keeps \(B_A^y(u,v)\) as an **upstream supplied callable**. It does not invent or refit that Airy basis. For derivative verification only, the executable uses a clearly labelled manufactured harmonic \(B_A^y\); it has no production-theory identity.

## 2. Yun/Kármán steel-shell strain

For a Yun local strip,

\[
\phi_i=
\left(1-\cos\frac{2\pi x_i}{B_{s,i}}\right)
\left(1-\cos\frac{2m_i\pi y}{\ell_i}\right).
\]

The historical coupled steel axial strain is inserted directly:

\[
\boxed{
\varepsilon_{s,i}
=
\varepsilon_y^g
+
A_i(w_{0,y}^g+\Delta w_{,y}^g)\phi_{i,y}
+
A_{0i}\Delta w_{,y}^g\phi_{i,y}
+
\left(A_{0i}A_i+\frac12A_i^2\right)\phi_{i,y}^2
}.
\]

No width/thickness screening is placed before this equation. Yun geometry is always present.

The minimal current steel law remains the already-executed ideal EPP baseline:

\[
\sigma_s=\operatorname{clip}(E_s\varepsilon_s,-f_y,+f_y),
\]

\[
E_{t,s}=
\begin{cases}
E_s,&|E_s\varepsilon_s|<f_y,\\
0,&|E_s\varepsilon_s|\ge f_y.
\end{cases}
\]

Yielding changes \((\sigma_s,E_t)\), but does not delete Yun geometry.

## 3. Exact derivatives needed by equilibrium

Let \(\boldsymbol\eta_g=(D,q,\alpha)\) and let \(A\) denote the local Yun amplitude. Define

\[
g_y=w_{0,y}^g+\Delta w_{,y}^g,\qquad
d_y=\Delta w_{,y}^g.
\]

For a global coordinate \(\eta_j\),

\[
\boxed{
\varepsilon_{s,j}
=
\varepsilon_{g,j}
+
A\,g_{y,j}\phi_y
+
A_0d_{y,j}\phi_y
},
\]

while

\[
\boxed{
\varepsilon_{s,A}
=
g_y\phi_y+(A_0+A)\phi_y^2
}.
\]

For the recovered Marguerre–Airy axial field,

\[
\varepsilon_{g,D}=-\varepsilon_0,
\]

\[
\varepsilon_{g,q}
=
\varepsilon_0
\left[
\pi^2(q_0+q)(u^2-u^2v^2)+2\pi^2uv\zeta
\right],
\]

\[
\varepsilon_{g,\alpha}
=
\varepsilon_0B_A^y(u,v).
\]

The second derivatives are

\[
\boxed{
\varepsilon_{s,ij}
=
\varepsilon_{g,ij}
+
A\,g_{y,ij}\phi_y
+
A_0d_{y,ij}\phi_y
},
\]

\[
\varepsilon_{g,qq}
=
\varepsilon_0\pi^2(u^2-u^2v^2),
\]

\[
\boxed{\varepsilon_{s,jA}=g_{y,j}\phi_y},
\qquad
\boxed{\varepsilon_{s,AA}=\phi_y^2}.
\]

## 4. Direct steel equilibrium and Jacobian

For any global generalized coordinate \(\eta_i\),

\[
\boxed{
R_i^s
=
t_s\int_{\Omega_s}
\sigma_s\varepsilon_{s,i}\,d\Omega
}.
\]

This is the R18 replacement: Yun returns the current \(\sigma_s\), and that stress enters equilibrium directly. No current \(A/B/D\) matrix is constructed first.

The exact current Jacobian is

\[
\boxed{
K_{ij}^s
=
t_s\int_{\Omega_s}
\left[
E_{t,s}\varepsilon_{s,i}\varepsilon_{s,j}
+
\sigma_s\varepsilon_{s,ij}
\right]d\Omega
}.
\]

The first term is the material/current-tangent contribution; the second is the current-stress/geometric contribution. The second term remains after ideal-EPP yielding even when \(E_{t,s}=0\).

## 5. Always-on Yun amplitude row

R18 also retains the historical local-amplitude equilibrium

\[
R_A
=
C_\sigma
\left[
k_{cr}A+H(2A_0A+A^2)(A+A_0)
\right]
-
\bar\sigma_c(A+A_0).
\]

Here \(\bar\sigma_c\) is evaluated from the **same current Yun/EPP steel stress field**, not from an independent terminal steel cap.

Let

\[
F=2A_0A+A^2,\qquad G=A+A_0.
\]

Then

\[
\boxed{
\frac{\partial R_A}{\partial\eta_j}
=
-G\frac{\partial\bar\sigma_c}{\partial\eta_j}
},
\]

and

\[
\boxed{
\frac{\partial R_A}{\partial A}
=
C_\sigma
\left[
k_{cr}+H\left(2(A_0+A)G+F\right)
\right]
-
\bar\sigma_c
-
G\frac{\partial\bar\sigma_c}{\partial A}
}.
\]

Thus the Yun amplitude row is coupled back to the same explicit global deformation and current steel stress.

## 6. Numerical Jacobian verification

The executable assembled

\[
\mathbf R=(R_D,R_q,R_\alpha,R_A)
\]

and its analytic \(4\times4\) Jacobian, then compared it with centered finite differences.

### Elastic strip

```text
relative Jacobian error       = 8.379031701877e-11
max scaled entry error        = 4.753291751317e-08
global-global symmetry error  = 2.201989822615e-18
elastic fraction              = 1.000000000000
bar sigma_c                   = 32.534852072 MPa
PASS                           = True
```

### Fully compressive-yielded strip

```text
relative Jacobian error       = 8.946410968662e-10
max scaled entry error        = 2.883829551726e-09
global-global symmetry error  = 0.000000000000e+00
elastic fraction              = 0.000000000000
bar sigma_c                   = 355.000000000 MPa
global Jacobian norm          = 6625.932107842
PASS                           = True
```

The yielded test is the decisive architecture check: \(E_t=0\) everywhere, but the global steel Jacobian remains nonzero because

\[
\sigma_s\varepsilon_{s,ij}
\]

survives.

```text
YIELDING_CHANGES_SIGMA_ET = YES
YIELDING_DELETES_YUN_GEOMETRY = NO
YIELDING_DELETES_STEEL_GEOMETRIC_TANGENT = NO
```

## 7. R18 decision

Completed:

```text
DIRECT_MA_EXPLICIT_STRAIN_INTERFACE = IMPLEMENTED
YUN_STEEL_STRAIN_COMPOSITION = IMPLEMENTED
IDEAL_EPP_SIGMA_ET = IMPLEMENTED
DIRECT_GLOBAL_STEEL_RESIDUAL = IMPLEMENTED
DIRECT_GLOBAL_STEEL_JACOBIAN = IMPLEMENTED
YUN_LOCAL_AMPLITUDE_ROW = IMPLEMENTED
YUN_LOCAL_ROW_CHAIN_RULE = IMPLEMENTED
ANALYTIC_JACOBIAN_VS_FINITE_DIFFERENCE = PASS
A_B_D_INTERMEDIATE = REMOVED
YUN_PARAMETER_ACTIVATION_GATE = ABSENT
```

Not claimed yet:

```text
PROJECT_FULL_BAy_UPSTREAM_BASIS_REINSERTED = NOT_YET
FORMAL_D15_ZERO_QUADRATURE_COMPILATION_OF_NEW_STEEL_TERMS = NOT_YET
Z0_Z6_FULL_Pu_RERUN = NOT_YET
T120_T360_BH_FULL_Pu_RERUN = NOT_YET
R08_R10A_R11_R12_R14_MULTI_UHPC_COMPARISON = NOT_YET
```

The remaining production step is now direct rather than architectural: plug the exact existing project Marguerre–Airy basis/slopes into this verified operator, compile the resulting finite analytic terms into the zero-spatial-quadrature moment engine, and solve the coupled global + Yun-amplitude equations.

## 8. Next task

```text
NEXT_TASK =
PROJECT_EXACT_MARGUERRE_AIRY_FIELD_ADAPTER
+ D15_COMPILE_DIRECT_YUN_STEEL_RESIDUAL_JACOBIAN
+ R08_R10A_R11_R12_R14_UHPC_ADAPTER_RERUN
```

Execution order:

1. insert the exact project \(B_A^y\), slopes and generalized derivatives;
2. D15-compile the direct Yun steel residual/Jacobian;
3. reproduce historical Yun Z1/Z4 states as regression checks;
4. rerun Z0–Z6;
5. under the same Yun structural front, switch only the UHPC core adapter among R08/R10A/R11/R12/R14;
6. compare implementation complexity and physical prediction separately.

```text
R07_R14_PRE_YUN_BASELINES = RETAIN_FOR_REGRESSION_ONLY
PRODUCTION_Pu_CHANGED_IN_R18 = NO
USER_ACCEPTANCE = PENDING
```
