# NZ-SCCM Case21 NC-R1 Formal-Closure Production Contract with Tangent Gate

**Date:** 2026-08-12  
**Identity:** CURRENT GOVERNING CASE21 EXECUTION CONTRACT  
**Theory basis:** `current/theory/NZ_SCCM_NC_R1_FORMAL_CLOSURE_ZHOU_STYLE_CANONICAL_20260812.md`

This contract supersedes the pre-closure Case21 blind-execution workflow wherever that workflow conflicts with the canonical formal-closure theory, especially the D15 basis and the missing full-field current-tangent gate.

---

# 0. Isolation discipline

Only current raw Case21 input, the canonical formal theory, and coefficients freshly generated from the current R10 target may enter the calculation.

```text
HISTORICAL_CASE21_D_Q_P_Pu_ROOT_PATH = FORBIDDEN
HISTORICAL_FE_GAUSS_SIMPSON_RESULT = FORBIDDEN
EXPERIMENT_DURING_SOLVE = FORBIDDEN
EXPERIMENT_FOR_ROOT_SELECTION = FORBIDDEN
EXPERIMENT_FOR_PARAMETER_TUNING = FORBIDDEN
EXPERIMENT = FINAL COMPARISON ONLY AFTER THEORY RESULT FREEZE
```

Formal structural invariants:

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
ACTIVE_MODE = m=1
KINEMATICS = NGUYEN_SECOND_ORDER
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

The 49 N48 Chebyshev coordinates are one-dimensional **material coordinates**, not structural-space points.

---

# 1. Mandatory theory chain

The only accepted Case21 production chain is

\[
\boxed{
\text{raw material/geometric input}
\to R10
\to N48\text{-}C1/MM
\to \text{Cayley--Hamilton}
\to \text{Nguyen complete halfwave}
\to \text{general D15 exact moments}
\to P,R_q,L
\to \Gamma_0
\to \text{first }+\to-\text{ limit candidate}
\to K_Z\text{ tangent gate}
\to \text{final Case21 verdict}
}
\]

No prior Case21 theoretical value may be used to initialize, bracket, rank or select roots.

---

# 2. General D15 is mandatory for every production scalar integrand

Every final structural scalar integrand must be reduced to

\[
\boxed{
Q(X,Y,\zeta)
=\sum_{p,r,u,s,h}c_{prush}
\sin^pX\cos^rX\sin^uY\cos^sY\zeta^h
}
\]

and contracted using

\[
\boxed{J_{pr}=\int_0^\pi\sin^pX\cos^rX\,dX},
\qquad
\boxed{Z_h=\int_{-1}^{1}\zeta^h\,d\zeta},
\]

\[
\boxed{
\mathscr D[Q]
=\sum c_{prush}J_{pr}J_{us}Z_h
}.
\]

This applies without exception to

```text
Syy
Qq = S : e_,q
all same-expression derivatives used in L
all current-tangent material integrands
all current-stress geometric-stiffness integrands
all reinforcement tangent/geometric terms
```

A restricted basis containing only functions of `sin X`, `sin Y`, `zeta` may be used only when strict algebra proves equivalence for the specific final scalar integrand. It may not be silently substituted for the governing general-D15 contraction.

---

# 3. Equilibrium and limit-point gates

The current halfwave load observable is

\[
P=P_c+P_s,
\]

and the generalized amplitude residual is

\[
R_q=R_{q,c}+R_{q,s}.
\]

Production equilibrium requires

\[
R_q(D,q)=0
\]

with

\[
R_{norm}
=\frac{|R_q|}{\max(f_c\varepsilon_0J_\Omega,|R_{q,c}|+|R_{q,s}|)}
\le10^{-5}.
\]

The limit function is

\[
\boxed{L=P_DR_{q,q}-P_qR_{q,D}},
\]

with

\[
|L_{norm}|\le10^{-5}.
\]

The primary branch remains

\[
\boxed{
\Gamma_0
=\operatorname{Conn}_{(0,0)}
(\{R_q=0\}\cap\mathcal A)
}.
\]

The NC-R1 limit candidate is the first `+ -> -` load maximum encountered from `(0,0)` along `Gamma0`.

**Important:** no tangent-stability acceptance is allowed until `Gamma0` itself has been generated from the same governing general-D15 `R_q` expression.

---

# 4. Mandatory current-tangent construction

The same current material operator must generate

\[
\boxed{
\mathbb C_t(X,Y,\zeta;D,q)
=\frac{\partial\boldsymbol\sigma}{\partial\mathbf E}
}.
\]

For the basic Navier perturbation

\[
\varphi=\sin X\sin Y,
\]

define

\[
\mathbf b_\varphi
=-z\begin{bmatrix}\varphi_{,xx}\\\varphi_{,yy}\\2\varphi_{,xy}\end{bmatrix}.
\]

The concrete material-tangent contribution is

\[
\boxed{
K_{Z,c}^{mat}
=\int_{\Omega_h}
\mathbf b_\varphi^T\mathbf C_t^{eng}\mathbf b_\varphi\,dV
}.
\]

The concrete geometric contribution is

\[
\boxed{
K_{Z,c}^{geo}
=\int_{\Omega_h}
(\sigma_x\varphi_{,x}^2
+2\tau_{xy}\varphi_{,x}\varphi_{,y}
+\sigma_y\varphi_{,y}^2)\,dV
}.
\]

For reinforcement,

\[
\boxed{
K_{Z,s}^{mat}
=\sum_{r,\alpha}t_{s,\alpha}^{(r)}
\int_A E_{s,t}^{(r,\alpha)}
[z_s^{(r)}\mathbf n_\alpha^T\boldsymbol\kappa_\varphi\mathbf n_\alpha]^2dA
},
\]

\[
\boxed{
K_{Z,s}^{geo}
=\sum_{r,\alpha}t_{s,\alpha}^{(r)}
\int_A\sigma_{s,\alpha}^{(r)}
(\mathbf n_\alpha\cdot\nabla\varphi)^2dA
}.
\]

Total modal current tangent:

\[
\boxed{
K_Z
=K_{Z,c}^{mat}+K_{Z,c}^{geo}+K_{Z,s}^{mat}+K_{Z,s}^{geo}
}.
\]

Every integral above is a general-D15 exact-moment contraction. Spatial Gauss/collocation/cells are prohibited.

---

# 5. Mandatory `1/epsilon_0` tangent scaling

Because

\[
\mathbf X=\mathbf E_u/\varepsilon_0,
\]

directional differentiation must include

\[
\boxed{
\delta\mathbf X=\delta\mathbf E_u/\varepsilon_0
}.
\]

Omitting `1/epsilon_0` invalidates the material tangent by a constant scale factor.

For Case21 the mandatory unloaded-state regression is

\[
\boxed{
K_Z(0,0)
=\frac{E_0t_p^3\pi^4}{12(1-\nu^2)b^2}
=823.416805665\ \mathrm{N/mm}
}.
\]

Production requirement:

```text
ZERO_STATE_TANGENT_REGRESSION = PASS
```

before any finite-amplitude tangent state is accepted.

---

# 6. Tangent gate along the corrected primary branch

After the general-D15 primary branch `Gamma0` has been rebuilt, evaluate `K_Z` on that same branch using analytic coefficient contraction.

The governing classifications are:

### 6.1 Limit-point admissible

If

\[
K_Z>0
\]

from the unloaded state up to the first `+ -> -` NC-R1 maximum and no earlier admissible zero of `K_Z` exists, then

```text
PRELIMIT_TANGENT_STABILITY = PASS
LIMIT_POINT_CONTROL_CANDIDATE = ACCEPTABLE
```

subject to all other Case21 gates.

### 6.2 Pre-limit tangent loss

If an admissible state on the same connected primary branch satisfies

\[
K_Z=0
\]

before the first `+ -> -` load maximum, then the later NC-R1 limit root **must not** be frozen as final Case21 `Pu`.

The execution status is

```text
BLOCKED_AT_PRELIMIT_TANGENT_LOSS
```

unless and until a separate governing decision explicitly defines how a pre-limit tangent-stability root is to be promoted to the final capacity identity. This contract does **not** silently create a second Pu solver.

### 6.3 Coincident control

If the first admissible `K_Z=0` and first `+ -> -` load maximum coincide within the frozen root-repeatability tolerances, report

```text
COUPLED_LIMIT_TANGENT_CONTROL
```

and preserve both residual records.

---

# 7. Case21-specific reinforcement tangent gate

For the current mid-surface single reinforcement layer,

\[
z_s=0,
\]

so

\[
K_{Z,s}^{mat}=0
\]

for the basic bending perturbation. The geometric reinforcement term remains active.

Before this simplification is used, the complete reinforcement field must remain on one supported material branch. If it does not,

```text
BLOCKED_AT_STEEL_BRANCH
```

and no spatial steel material-point partition is allowed.

---

# 8. Required output sequence for a complete Case21 calculation

A Case21 calculation may receive

```text
CALCULATION_CLOSURE = PASS
```

only after all of the following have been explicitly reported:

```text
1. raw Case21 inputs
2. R10 derived parameters
3. freshly generated 49x4 N48 coefficient table
4. C1/MM material fidelity records
5. continuous compiler-domain certificate
6. general-D15 Syy contraction
7. general-D15 Qq contraction
8. rebar branch certificate
9. corrected Rq=0 primary branch Gamma0
10. first +->- limit candidate and R_norm/L_norm
11. zero-state K_Z regression
12. KZ,c^mat
13. KZ,c^geo
14. KZ,s^mat
15. KZ,s^geo
16. total K_Z along the corrected branch
17. proof whether a K_Z=0 state occurs before the first limit maximum
18. final theory result freeze
19. only then experimental comparison
```

Missing item 11–17 means the calculation is not tangent-closed.

---

# 9. Current Case21 status under this contract

The audit

`current/audits/NZ_SCCM_CASE21_TANGENT_GATE_AND_GENERAL_D15_RECHECK_20260812.md`

found that the previously reported fresh Case21 branch does not reproduce the canonical general-D15 `Q_q` contraction. Therefore the current status is

```text
PREVIOUS_FRESH_CASE21_LIMIT_RESULT = AUDIT RECORD ONLY
GENERAL_D15_Rq_BRANCH = MUST BE REBUILT
PRODUCTION_TANGENT_GATE = NOT YET REACHED
CASE21_COMPLETE_CLOSURE = BLOCKED
```

The next calculation must restart only from the current raw Case21 input + canonical theory + freshly generated material coefficients. No historical Gauss or previous root/path values are allowed as targets.