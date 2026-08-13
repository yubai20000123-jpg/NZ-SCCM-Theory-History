# NZ-SCCM concrete + steel-shell panel — reinforcement replacement / finite-thickness shell / general-D15 theory extension

**Timestamp:** 2026-08-13 18:34 +08:00  
**Status:** CURRENT_EXTENSION_DRAFT / STRUCTURAL OPERATOR CLOSED / STEEL MATERIAL OPERATOR FREEZE PENDING  
**Parent lock:** `20260813_1834__NZSCCM__NC_PANEL__ENERGY_MINIMUM_HALFWAVE_R10_N48C1MM_D15_DIRECT_LIMIT__LOCKED_BASELINE.md`

---

## 0. Purpose

The next extension does **not** modify the successful concrete panel theory. It removes the smeared/discrete reinforcement contribution and replaces it with one or more continuous finite-thickness steel-shell layers.

```text
CONCRETE_OPERATOR = UNCHANGED
HALFWAVE_RULE = UNCHANGED
NGUYEN_SECOND_ORDER = UNCHANGED
R10_N48_C1MM = UNCHANGED
CH_GENERAL_D15 = UNCHANGED
DIRECT_LIMIT_SOLVER = UNCHANGED
REBAR_MODULE = REMOVED IN STEEL-SHELL VERSION
STEEL_SHELL_MODULE = ADDED
```

The target architecture is

```text
concrete continuous volume
+ bonded continuous steel shell layer(s)
-> same D,q strain field
-> concrete current map + steel-shell current map
-> exact multiple moments
-> Pc + Psh
-> Rq,c + Rq,sh
-> direct Rq=0, L=0 limit
-> same-branch anisotropic current-tangent KZ
```

---

## 1. Source-grounded steel-shell mechanics

### 1.1 Zhang et al.

Zhang et al. formulate rectangular concrete-filled steel-tube wall local buckling by an energy method. The steel-wall bending rigidity is

\[
D_s=\frac{E_st_s^3}{12(1-\nu_s^2)},
\]

and the total potential contains steel-plate bending energy plus work of axial compression. They explicitly introduce a halfwave parameter and determine the local-buckling coefficient by minimization with respect to the halfwave parameter. Their analysis also shows that a PBL/stiffener stiffness changes the minimizing halfwave and boundary behavior.

This supports the present lock that formal halfwave selection is a **design-side energy minimum**, not an experimental mode fit.

### 1.2 Sun Lipeng

Sun's Chapter 3 treats the concrete-supported steel wall as a plate whose elastic/inelastic local buckling depends on directional stiffness. For inelastic buckling, the Bleich approximation replaces the loading-direction stiffness by a tangent-modulus-dependent value and retains different stiffnesses in different plate directions. Sun uses a Ramberg-Osgood uniaxial source relation

\[
\varepsilon=\frac{\sigma}{E_s}+p\left(\frac{\sigma}{f_y}\right)^n,
\]

with tangent

\[
E_t=\left[\frac1{E_s}+\frac{np}{f_y}\left(\frac{\sigma}{f_y}\right)^{n-1}\right]^{-1}.
\]

For finite-element verification Sun additionally adopts source-based multilinear steel constitutive laws with von Mises yield and isotropic hardening.

These sources establish two requirements for NZ-SCCM steel-shell extension:

1. the shell is a continuous plate, not a smeared rebar line contribution;
2. its current directional tangent cannot in general be replaced by one scalar elastic modulus once inelasticity is relevant.

No effective-width formula, empirical local-buckling reduction or specimen-fitted steel factor from these sources is imported into the NZ-SCCM direct-limit operator.

---

## 2. Shell geometry

Let the concrete reference mid-surface be `z=0`. Steel-shell layer `k` has

\[
\boxed{t_{s,k},\quad z_{s,k}},
\]

where `z_{s,k}` is the centroid coordinate of the shell thickness relative to the concrete reference surface.

Introduce a local shell-thickness coordinate

\[
\eta\in[-1,1],\qquad
z=z_{s,k}+\frac{t_{s,k}}2\eta.
\]

The theory permits one shell layer or multiple bonded shell skins:

```text
ONE_SIDE_STEEL_SHELL = allowed
TWO_SIDE_STEEL_SKINS = allowed
GENERAL_FINITE_NUMBER_OF_SHELL_LAYERS = allowed
```

Each shell layer remains one continuous analytic domain; it is not discretized through thickness.

---

## 3. Bonded shell kinematics: same Nguyen second-order field

The steel shell shares the same mid-surface deformation and curvature field as the concrete core under perfect bond. No new shell displacement degree of freedom is introduced at this stage.

Write the physical engineering strain vector as

\[
\boldsymbol\varepsilon^s=
\begin{bmatrix}
\varepsilon_x^s\\
\varepsilon_y^s\\
\gamma_{xy}^s
\end{bmatrix}
=
\boldsymbol\varepsilon_m(D,q;X,Y)
+z\,\boldsymbol\kappa(q;X,Y).
\]

Using the locked complete-halfwave kinematics,

\[
\varepsilon_x^s
=\varepsilon_0\left[\nu D+C_{mx}\cos^2X\sin^2Y\right]
+z\frac{\pi^2A}{b^2}\sin X\sin Y,
\]

\[
\varepsilon_y^s
=\varepsilon_0\left[-D+C_{my}\sin^2X\cos^2Y\right]
+z\frac{\pi^2A}{\ell^2}\sin X\sin Y,
\]

\[
\gamma_{xy}^s
=\varepsilon_0 C_{mxy}\sin X\cos X\sin Y\cos Y
-2z\frac{\pi^2A}{b\ell}\cos X\cos Y.
\]

Thus both the membrane terms and shell bending strain are already contained in the same second-order kinematic operator.

For each shell layer the exact derivative

\[
\boxed{\boldsymbol\varepsilon^s_{,q}}
\]

is obtained analytically from the same expression.

---

## 4. Steel-shell current material interface

The structural extension requires a plane-stress current operator

\[
\boxed{\boldsymbol\sigma^s=M_s(\boldsymbol\varepsilon^s)},
\]

\[
\boxed{\mathbb C_t^s=\frac{\partial\boldsymbol\sigma^s}{\partial\boldsymbol\varepsilon^s}}.
\]

with

\[
\boldsymbol\sigma^s=
\begin{bmatrix}
\sigma_x^s\\
\sigma_y^s\\
\tau_{xy}^s
\end{bmatrix}.
\]

The final production steel operator must satisfy:

```text
PLANE_STRESS = YES
FULL_2D_CURRENT_STRESS = YES
FULL_DIRECTIONAL_CONSISTENT_TANGENT = YES
PATH_STEPS_IN_STRUCTURAL_SPACE = NO
FINITE_ANALYTIC_COMPILABILITY = REQUIRED
GENERAL_D15_COMPATIBILITY = REQUIRED
STRUCTURAL_TEST_CALIBRATION = NO
```

### 4.1 What is already source-supported

Sun supports:

- elastic steel plate stiffness;
- tangent-modulus-sensitive directional local-buckling stiffness;
- Ramberg-Osgood material relation in the low-plastic-strain inelastic-buckling range;
- multilinear von-Mises/isotropic-hardening steel models for high-strength and ordinary-strength steel in FE verification.

### 4.2 What remains to freeze before production Pu

The existing sources do **not by themselves** define a unique path-independent full 2D plane-stress current map for the NZ-SCCM no-load-step formalism. Therefore the structural shell operator is closed, but production calculation must not silently invent a 2D plastic law.

The immediate steel-material task is to freeze one source-consistent 2D current operator and its finite analytic compiler. Candidate routes to audit are:

1. a source-consistent J2/deformation-theory total-strain lift of the approved uniaxial steel curve;
2. an equivalent source-grounded analytic plane-stress map that reproduces the uniaxial curve and consistent directional tangent;
3. elastic branch as an exact degeneration when the entire reachable shell field remains below the source proportional/yield boundary.

No option may be selected because it improves a structural specimen's Pu.

---

## 5. Steel-shell axial load contribution

For shell layer `k`, define

\[
J_{s,k}=\frac{b\ell t_{s,k}}{2\pi^2}.
\]

The representative complete-halfwave axial load contribution is

\[
\boxed{
P_{sh,k}
=-\frac1\ell\int_{\Omega_{sh,k}}\sigma_y^s\,dV
=-\frac{b t_{s,k}}{2\pi^2}\,\mathscr D_{s,k}[\sigma_y^s]
}.
\]

Hence

\[
\boxed{P_{sh}=\sum_kP_{sh,k}}.
\]

This replaces the previous reinforcement axial-load expression.

---

## 6. Steel-shell q-equilibrium contribution

The virtual-work/residual contribution of shell layer `k` is

\[
\boxed{
R_{q,sh,k}
=\int_{\Omega_{sh,k}}
(\boldsymbol\sigma^s)^T
\boldsymbol\varepsilon^s_{,q}\,dV
}.
\]

Using the shell local thickness coordinate,

\[
\boxed{
R_{q,sh,k}
=J_{s,k}\,\mathscr D_{s,k}
\left[(\boldsymbol\sigma^s)^T\boldsymbol\varepsilon^s_{,q}\right]
}.
\]

and

\[
\boxed{R_{q,sh}=\sum_kR_{q,sh,k}}.
\]

This is the exact finite-thickness analogue of the reinforcement virtual-work term; it is not an empirical steel capacity add-on.

---

## 7. Total concrete + steel-shell equilibrium and limit equations

The reinforcement contribution is removed. The new production identities become

\[
\boxed{P(D,q)=P_c(D,q)+P_{sh}(D,q)},
\]

\[
\boxed{R_q(D,q)=R_{q,c}(D,q)+R_{q,sh}(D,q)}.
\]

The exact same-expression derivatives remain

\[
P_D,\quad P_q,\quad R_{q,D},\quad R_{q,q},
\]

and therefore

\[
\boxed{L=P_DR_{q,q}-P_qR_{q,D}}.
\]

The ultimate candidate remains the first admissible connected-branch solution

\[
\boxed{R_q=0,\qquad L=0,\qquad g:+\rightarrow-}.
\]

No separate steel-shell strength formula is added to Pu.

---

## 8. Steel-shell current-tangent stability contribution

For the same Navier/halfwave mode `phi`, the shell material contribution is

\[
\boxed{
K_{Z,sh}^{mat}
=\sum_k\int_{\Omega_{sh,k}}
 b_\varphi^T\mathbb C_{t,k}^{s,eng}b_\varphi\,dV
}.
\]

The shell current-stress geometric contribution is

\[
\boxed{
K_{Z,sh}^{geo}
=\sum_k\int_{\Omega_{sh,k}}
\left[
\sigma_x^s\varphi_{,x}^2
+2\tau_{xy}^s\varphi_{,x}\varphi_{,y}
+\sigma_y^s\varphi_{,y}^2
\right]dV
}.
\]

Total stability becomes

\[
\boxed{
K_Z
=K_{Z,c}^{mat}+K_{Z,c}^{geo}
+K_{Z,sh}^{mat}+K_{Z,sh}^{geo}
}.
\]

Thus the old rebar tangent/geometric terms are replaced exactly by finite-thickness shell terms.

---

## 9. Exact multiple-integral closure

Once `M_s` is represented by a finite analytic material compiler, every steel-shell scalar integrand is again a finite expansion in

\[
\sin X,\cos X,\sin Y,\cos Y,\eta,
\]

and therefore closes through the same general-D15 moment engine.

For each layer:

\[
Q_s=\sum c_{prush}^{(s)}\sin^pX\cos^rX\sin^uY\cos^sY\eta^h,
\]

\[
\mathscr D_s[Q_s]=\sum c_{prush}^{(s)}J_{pr}J_{us}Z_h.
\]

```text
STEEL_SHELL_SPATIAL_POINTS = 0
STEEL_SHELL_THICKNESS_POINTS = 0
STEEL_SHELL_GAUSS = 0
STEEL_SHELL_MATERIAL_POINT_GRID = 0
```

The extra shell thickness is an exact third integration coordinate, not a discretized layer stack.

---

## 10. Halfwave and PBL/stiffener handling in the shell extension

The steel-shell extension inherits the locked theoretical minimum-halfwave rule.

For an unstiffened wall, the admissible halfwave is selected from the classical/design boundary energy minimum.

For a PBL/stiffened wall, Zhang et al. show that stiffener support changes the energy functional and may shift the minimizing halfwave. Therefore the halfwave may change **only because the design stiffness/boundary data change**.

For the current UCFT/PBL governance, PBL is not automatically added as an independent axial steel load term. Its primary formal role remains boundary/stiffener control of the shell panel unless a later explicit source contract authorizes another load-carrying contribution.

```text
PBL_AS_EXPERIMENT_FITTED_MODE_SELECTOR = NO
PBL_AS_AUTOMATIC_AXIAL_STEEL_AREA = NO
PBL_DESIGN_BOUNDARY_EFFECT = YES
```

---

## 11. Direct replacement map from RC to concrete + steel shell

Old RC chain:

```text
Pc + Ps(rebar)
Rq,c + Rq,s(rebar)
KZ,c + KZ,s(rebar)
```

New shell chain:

```text
Pc + Psh(finite-thickness shell)
Rq,c + Rq,sh(finite-thickness shell)
KZ,c + KZ,sh(finite-thickness shell)
```

Everything upstream and downstream is unchanged:

```text
energy-minimum halfwave
-> Nguyen second-order D,q field
-> R10 concrete current operator
-> N48-C1/MM
-> Cayley-Hamilton
-> steel-shell current operator
-> finite analytic coefficients
-> general-D15 exact multiple integrals
-> P,Rq and same-expression derivatives
-> Rq=0,L=0 direct simultaneous limit solve
-> same-branch full directional KZ
```

---

## 12. Immediate execution gate

Before a numerical `CONCRETE + STEEL SHELL` Pu can become production, only the following new material-layer item remains to be frozen:

```text
STEEL_SHELL_2D_CURRENT_OPERATOR = PENDING SOURCE-CONSISTENT FREEZE
```

The concrete theory, halfwave selection, kinematics, compiler, moment engine, direct limit equations and tangent-stability structure are **not open questions**.

Required next output:

1. freeze ordinary/high-strength steel uniaxial source curve by grade;
2. derive one full plane-stress current operator `M_s(E)` consistent with that curve and the no-load-step formalism;
3. derive `C_t^s` analytically;
4. compile it into a finite analytic basis with a design-dependent material interval/domain;
5. substitute into the shell equations above;
6. first calculate a concrete + steel-shell benchmark with no use of experimental Pu in coefficient generation or root selection.
