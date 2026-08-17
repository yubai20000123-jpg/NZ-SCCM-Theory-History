# NZ-SCCM — Case21 Airy-scalar mechanics qualification and formal T12 operator contract

**Timestamp:** 2026-08-17 11:05 +08:00  
**Status:** THEORY QUALIFICATION PASS / FORMAL NUMERIC EVALUATOR NOT YET EXECUTED

## 0. Objective and boundary

This derivation performs the planned pre-production task before any new formal Case21 ultimate-load run:

1. distinguish Case21 buckling and ultimate experimental loads;
2. qualify the retained one-coordinate Airy membrane subspace mechanically;
3. inherit the internal membrane-stability rule in scalar form;
4. correct the scope of the `lambda=1` elastic benchmark when reinforcement is present;
5. derive the smallest direct value-level structural target set needed by `P`, `RA`, and `Rq`;
6. state the finite same-source derivative contract needed by the later bordered ultimate-point equation.

It does not change R10 and does not release a new `Pu`.

Formal project counters remain

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

---

# 1. Experimental load identity

For Case21:

\[
\boxed{P_{cr,exp}=75.6\,\mathrm{kip}=336.285554\,\mathrm{kN}}
\]

is the experimental **buckling** load, whereas

\[
\boxed{P_{f,exp}=82.8\,\mathrm{kip}=368.312750\,\mathrm{kN}}
\]

is the experimental **failure / ultimate** load.

The current ultimate-load calculation must therefore be compared to `368.312750 kN`.

---

# 2. Retained complete-halfwave kinematics

Let

\[
X=\pi x/b,\qquad Y=\pi y/\ell,
\]

and for Case21 `ell=b`.

Define

\[
C_X=\cos2X,\quad C_Y=\cos2Y,
\quad S_X=\sin2X,\quad S_Y=\sin2Y.
\]

The Nguyen second-order geometric membrane driver is

\[
\boxed{M=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right)}
\]

and the bending scale is

\[
\boxed{B=\frac{\pi^2}{2\varepsilon_0}\frac tb q.}
\]

The retained Airy direction is

\[
\boxed{
 a(\nu)=
\left[-\frac{1+\nu}{4},-\frac{1-\nu}{4},\frac14,-\frac{1-\nu}{4},\frac14\right]^T
}
\]

and the current membrane coordinates are restricted to

\[
\boxed{r=\lambda M a(\nu).}
\]

The resulting normalized strains are

\[
\boxed{
\begin{aligned}
e_x={}&\nu D+\frac M4\big[
1+C_X-C_Y-C_XC_Y\\
&-\lambda(1+\nu)-\lambda(1-\nu)C_X+\lambda C_XC_Y\big]\\
&+B\sin X\sin Y\,\zeta,
\end{aligned}}
\]

\[
\boxed{
\begin{aligned}
e_y={}&-D+\frac M4\big[
1-C_X+C_Y-C_XC_Y\\
&-\lambda(1-\nu)C_Y+\lambda C_XC_Y\big]\\
&+B\sin X\sin Y\,\zeta,
\end{aligned}}
\]

\[
\boxed{
\gamma_{xy}=\frac M2(1-\lambda)S_XS_Y
-2B\cos X\cos Y\,\zeta.
}
\]

---

# 3. Exact coordinate-transformation / virtual-work identity

Let the original generalized virtual-work residuals be

\[
R_q^{base}=\delta W\,[\delta q]\quad\text{at fixed }r,
\]

and

\[
R_m=(R_{m,0},R_{m,20},R_{m,u22},R_{m,02},R_{m,v22})^T.
\]

Define

\[
R_A=a^TR_m.
\]

Because

\[
\delta r=a(M\,\delta\lambda+\lambda M_q\,\delta q),
\]

where

\[
M_q=\frac{\pi^2}{\varepsilon_0}(q_0+q),
\]

the restricted-coordinate residuals are exactly

\[
\boxed{R_\lambda=M R_A}
\]

and

\[
\boxed{R_q^{res}=R_q^{base}+\lambda M_q R_A.}
\]

Therefore the solver equations currently used by the direct-source evaluator,

\[
\boxed{R_q^{base}=0,\qquad R_A=0,}
\]

are not an ad-hoc replacement. For `M>0` they are exactly row-equivalent to the residual equations in `(q,lambda)` coordinates:

\[
\begin{bmatrix}R_q^{res}\\R_\lambda\end{bmatrix}
=
\underbrace{\begin{bmatrix}1&\lambda M_q\\0&M\end{bmatrix}}_{T,\;\det T=M>0}
\begin{bmatrix}R_q^{base}\\R_A\end{bmatrix}.
\]

At equilibrium the derivative of `T` multiplies the zero residual vector, so the two Jacobians differ only by the same nonsingular row operation. Consequently the zero of the bordered ultimate determinant is unchanged up to the positive factor `M`.

At the exact origin `M=0`, `lambda` is inactive because `r=0`; the meaningful branch is the `M>0` origin-connected limit.

---

# 4. Exact isotropic continuum elastic benchmark

Use the isotropic plane-stress normalized constitutive relation

\[
\frac{\sigma_x}{E\varepsilon_0}=\frac{e_x+\nu e_y}{1-\nu^2},
\]

\[
\frac{\sigma_y}{E\varepsilon_0}=\frac{\nu e_x+e_y}{1-\nu^2},
\]

\[
\frac{\tau_{xy}}{E\varepsilon_0}=\frac{\gamma_{xy}}{2(1+\nu)}.
\]

For the Airy virtual basis

\[
B_A^x=-\frac{1+\nu}{4}-\frac{1-\nu}{4}C_X+\frac14C_XC_Y,
\]

\[
B_A^y=-\frac{1-\nu}{4}C_Y+\frac14C_XC_Y,
\]

\[
B_A^\gamma=-\frac12S_XS_Y,
\]

direct orthogonal integration over the complete halfwave gives, after removing the common positive geometry/material scale,

\[
\boxed{
\widetilde R_A^c
=
\frac{\pi^2M(2\nu^2+3)}{16(1-\nu^2)}(\lambda-1).
}
\]

Therefore for every physical isotropic `|nu|<1`,

\[
\boxed{\lambda=1}
\]

is the unique scalar equilibrium and

\[
\boxed{
\frac{\partial\widetilde R_A^c}{\partial\lambda}
=
\frac{\pi^2M(2\nu^2+3)}{16(1-\nu^2)}>0.
}
\]

At `lambda=1`, the membrane stress field reduces exactly to

\[
\boxed{
\frac{\sigma_x}{E\varepsilon_0}=-\frac M4\cos2Y,
}
\]

\[
\boxed{
\frac{\sigma_y}{E\varepsilon_0}=-D+\frac M2\sin^2X,
}
\]

\[
\boxed{\tau_{xy}=0.}
\]

The center is unloaded relative to the edge in the axial compressive field, i.e. the classical edgeward redistribution structure is recovered.

For `nu=.18`, the reduced scalar stiffness coefficient is

```text
pi^2*(2*nu^2+3)/(16*(1-nu^2)) = 1.95382670838018
```

before multiplication by the positive material/geometry scales and `M`.

---

# 5. Reinforced linear scalar benchmark — correction to the old wording

The exact `lambda=1` result above belongs to the **single isotropic continuum** benchmark.

Case21 also contains two orthogonal mid-plane reinforcement phases. In the retained model each reinforcement direction is uniaxial; it therefore changes the composite in-plane residual even if both directions have equal reinforcement ratio.

For equal directional ratio `rho_s`, the reduced reinforcement Airy residual in the retained scalar subspace is

\[
\boxed{
\widetilde R_A^s
=-\frac{\pi^2\rho_sE_s}{32}
\left[
8D\nu(\nu+1)+M\{5-(4\nu^2+5)\lambda\}
\right].
}
\]

Combining this with the isotropic concrete elastic residual gives

\[
\boxed{\lambda_{lin,RC}=A_{RC}+B_{RC}\frac DM}
\]

where

\[
H=4E_c\nu^2+6E_c
-4\rho_sE_s\nu^4-\rho_sE_s\nu^2+5\rho_sE_s,
\]

\[
\boxed{
A_{RC}
=\frac{4E_c\nu^2+6E_c-5\rho_sE_s\nu^2+5\rho_sE_s}{H},
}
\]

\[
\boxed{
B_{RC}
=\frac{8\rho_sE_s\nu(1-\nu)(1+\nu)^2}{H}.
}
\]

For the actual Case21 data

```text
Ec = 20321 MPa
Es = 200000 MPa
rho_s = .00375 per direction
nu = .18
```

this becomes

\[
\boxed{
\lambda_{lin,RC}
=0.999266844854884
+0.0096124785693025\frac DM.
}
\]

Thus the correct benchmark hierarchy is:

```text
pure isotropic continuum -> lambda = 1 exactly
reinforced scalar composite -> lambda follows the exact RC scalar formula above
rho_s Es -> 0 -> lambda -> 1
```

This is important because a low-load RC value `lambda != 1` is physically expected in the current one-coordinate subspace and must not be misclassified as a failure of the Airy shape.

As an audit-only low-load regression, at `D=.001` the direct-source branch gives approximately

```text
q = 6.15768024e-6
M = 7.27855421e-5
lambda_direct_R10 = 1.13129363
lambda_linear_RC  = 1.13133261
absolute difference ~= 3.90e-5
```

showing the direct current operator approaches the derived RC scalar linear limit.

---

# 6. Scalar internal-stability condition

The 2026-08-17 00:10 five-coordinate stability gate required positive internal tangent before static condensation.

For the retained coordinate

\[
r=\lambda Ma,
\]

we have

\[
\boxed{
R_{A,\lambda}=M a^T K_{rr}a.
}
\]

Since the actual residual conjugate to `lambda` is `R_lambda=M RA`, its tangent at equilibrium is

\[
\boxed{
K_{\lambda\lambda}=M R_{A,\lambda}=M^2a^TK_{rr}a.
}
\]

For every active `M>0` state, the admissibility condition is therefore

\[
\boxed{R_{A,\lambda}>0.}
\]

The companion direct-source audit evaluates this derivative without promoting the Gauss grid to a formal operator. It stays positive through the present Case21 peak.

---

# 7. Exact reinforcement structural contribution in the current elastic branch

At the current Case21 peak the reinforcement is elastic, so its formal contribution requires no numerical quadrature.

Let

\[
C_s=\frac{\rho_{s,y}tbE_s\varepsilon_0}{1000}
\]

for load in kN. For Case21

```text
C_s = 36.908355 kN
```

and

\[
\boxed{P_s=C_s\left(D-\frac M4\right).}
\]

Hence

\[
\boxed{P_{s,D}=C_s,\qquad
P_{s,q}=-\frac{C_sM_q}{4},\qquad
P_{s,\lambda}=0.}
\]

At the direct-source peak this gives

```text
Ps = 28.84479831 kN
```

consistent with the current oracle.

For the generalized residual scale define

\[
C_R=\frac{\rho_sE_s\varepsilon_0^2b\ell t}{32\times1000}.
\]

For Case21

```text
C_R = 2.94090386184375
```

and the exact elastic steel terms are

\[
\boxed{
R_A^s=-C_R\left[8D\nu(\nu+1)+M\{5-(4\nu^2+5)\lambda\}\right],
}
\]

\[
\boxed{
R_q^s=C_R M_q\left[8D(\nu-1)+M(9-5\lambda)\right].
}
\]

The latter is the existing `Rq_base` representation; the row-equivalent restricted residual adds `lambda M_q RA` and therefore has the same equilibrium and bordered-limit locus.

All steel derivatives are closed algebraically. No steel spatial target compiler is needed while the supported elastic branch remains valid.

---

# 8. Concrete thickness-resultant interface

Define complete-thickness stress moments

\[
N_x^{(k)}(X,Y)=\int_{-1}^{1}\zeta^k\sigma_x\,d\zeta,
\]

\[
N_y^{(k)}(X,Y)=\int_{-1}^{1}\zeta^k\sigma_y\,d\zeta,
\]

\[
N_{xy}^{(k)}(X,Y)=\int_{-1}^{1}\zeta^k\tau_{xy}\,d\zeta.
\]

The production thickness representation remains the already-selected

```text
GLOBAL_FIXED_ENDPOINT_POSITIVE_PART_FACTORISED_PERIOD
```

with physical endpoints `zeta=-1,+1`. Moving event roots are not exposed to the in-plane layer.

For concrete values:

- `P` and `RA` need only `k=0` stress resultants;
- `Rq` additionally needs `k=1` stress resultants.

---

# 9. Minimal direct value-level in-plane target contract

For any component define

\[
J_{\alpha,k}[w]
=\int_0^\pi\int_0^\pi w(X,Y)N_\alpha^{(k)}(X,Y)\,dYdX.
\]

For arbitrary nonlinear R10 stress resultants no constitutive identity is available that equates distinct stress components or distinct Fourier weights. Over the complete halfwave, the required Fourier weights are linearly independent. Therefore the direct linear-contraction value contract contains the following 12 independent component/order/weight functionals:

\[
\boxed{
\begin{aligned}
T_{12}=\{&J_{x,0}[1],J_{x,0}[C_X],J_{x,0}[C_Y],J_{x,0}[C_XC_Y],\\
&J_{y,0}[1],J_{y,0}[C_X],J_{y,0}[C_Y],J_{y,0}[C_XC_Y],\\
&J_{xy,0}[S_XS_Y],\\
&J_{x,1}[\sin X\sin Y],
J_{y,1}[\sin X\sin Y],
J_{xy,1}[\cos X\cos Y]\}.
\end{aligned}}
\]

This is the minimal **direct value-level** contract unless an additional exact R10-specific identity is later proved. No such identity is assumed here.

Use shorthand

```text
Jx00, Jx20, Jx02, Jx22c
Jy00, Jy20, Jy02, Jy22c
Jxy22s
Jx11s_1, Jy11s_1, Jxy11c_1
```

Then

\[
\boxed{P_c=-\frac{bt}{2\pi^2}J_{y00}.}
\]

The Airy residual is

\[
\boxed{
R_A^c=C_{vol}\left[
-\frac{1+\nu}{4}J_{x00}
-\frac{1-\nu}{4}J_{x20}
+\frac14J_{x22c}
-\frac{1-\nu}{4}J_{y02}
+\frac14J_{y22c}
-\frac12J_{xy22s}
\right]
}
\]

where

\[
C_{vol}=\frac{\varepsilon_0b\ell t}{2\pi^2\times1000}
\]

when residual reporting is in the current kN-based convention.

Define

\[
F_0=
J_{x00}+J_{x20}-J_{x02}-J_{x22c}
+J_{y00}-J_{y20}+J_{y02}-J_{y22c}
+2J_{xy22s},
\]

\[
F_1=J_{x11s}^{(1)}+J_{y11s}^{(1)}-2J_{xy11c}^{(1)}.
\]

Then

\[
\boxed{
R_q^c=C_{vol}\left(\frac{M_q}{4}F_0+B_qF_1\right)
}
\]

with

\[
B_q=\frac{\pi^2}{2\varepsilon_0}\frac tb.
\]

No reconstructed stress surface is required at the structural interface.

---

# 10. Same-source derivative contract

The formal ultimate point requires derivatives of

\[
P,\quad R_q,\quad R_A
\]

with respect to

\[
\theta\in\{D,q,\lambda\}.
\]

The value-level Fourier target set does not need to grow. The same 12 functionals are differentiated through the same source-level R10 tangent.

Define

\[
J_{\alpha,k;\theta}[w]
=\frac{\partial}{\partial\theta}J_{\alpha,k}[w].
\]

The finite through-thickness tangent requirement is:

```text
D or lambda perturbation:
  derivative of k=0 stress resultants -> tangent moments through k=0
  derivative of k=1 stress resultants -> tangent moments through k=1

q perturbation:
  epsilon_,q contains zeta^0 and zeta^1 pieces
  derivative of k=0 stress resultants -> tangent moments through k=1
  derivative of k=1 stress resultants -> tangent moments through k=2
```

Therefore the already-established finite API bound remains exactly

\[
\boxed{
\text{stress moments }k=0,1;\qquad
\text{tangent kernels }k=0,1,2.
}
\]

There is no unbounded thickness-moment sequence.

For `q`, because `M_q` depends on `q`,

\[
M_{qq}=\frac{\pi^2}{\varepsilon_0}
\]

and

\[
\boxed{
R_{q,q}^c
=C_{vol}\left[
\frac{M_{qq}}4F_0
+\frac{M_q}{4}F_{0,q}
+B_qF_{1,q}
\right].
}
\]

All remaining first derivatives are direct linear combinations of the corresponding `J_;theta` target derivatives plus the closed-form steel derivatives.

---

# 11. Formal ultimate-point system

Use the row-equivalent solver residuals

\[
F_1=R_q^{base}(D,q,\lambda),
\qquad
F_2=R_A(D,q,\lambda).
\]

Along the connected branch, the first stationary load point satisfies

\[
\frac{dP}{dD}=0.
\]

The bordered determinant is

\[
\boxed{
L_3=
\det\begin{bmatrix}
P_{,D}&P_{,q}&P_{,\lambda}\\
R_{q,D}&R_{q,q}&R_{q,\lambda}\\
R_{A,D}&R_{A,q}&R_{A,\lambda}
\end{bmatrix}=0.
}
\]

Because the physical restricted-coordinate residual pair is related by a nonsingular row transformation of determinant `M>0`, the same `L3=0` locus is obtained at equilibrium.

The formal Case21 solve after the descriptor gate will therefore be

\[
\boxed{R_q=0,\qquad R_A=0,\qquad L_3=0}
\]

subject also to

\[
\boxed{R_{A,\lambda}>0}
\]

and the supported reinforcement/material branch checks.

---

# 12. Decision and unique next task

```text
CASE21_LOAD_IDENTITY = PASS
AIRY_SCALAR_COORDINATE_TRANSFORMATION = PASS_EXACT
PURE_CONTINUUM_ELASTIC_AIRY_LIMIT = PASS_EXACT
RC_LINEAR_SCALAR_BENCHMARK = PASS_EXACT
CURRENT_NONLINEAR_INTERNAL_STABILITY = PASS_DIRECT_SOURCE_AUDIT_TO_PEAK
STEEL_VALUE_AND_DERIVATIVE_PACKAGE = CLOSED_FORM
VALUE_LEVEL_CONCRETE_TARGET_DIMENSION = 12
STRESS_THICKNESS_ORDER = 0,1
TANGENT_THICKNESS_ORDER = 0,1,2
FORMAL_ZERO_SPATIAL_NUMERIC_RELEASE = OPEN
NEW_Pu = NOT_RUN
```

Unique next gate:

```text
CASE21_AIRY_SCALAR_FORMAL_T12_FIXED_ENDPOINT_DESCRIPTOR_GATE
```

It must construct the fixed-endpoint source-regular R10 evaluator for `T12` and all same-source `(D,q,lambda)` derivatives without spatial quadrature, spatial subdivision, material-point grids, or explicit high-order coefficient enumeration.