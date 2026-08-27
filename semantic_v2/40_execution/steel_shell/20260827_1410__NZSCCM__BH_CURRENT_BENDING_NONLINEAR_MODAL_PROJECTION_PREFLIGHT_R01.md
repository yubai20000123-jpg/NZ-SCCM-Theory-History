# NZ-SCCM — BH current-bending nonlinear modal-projection preflight R01

**Time:** 2026-08-27 14:10 +08:00  
**Parent theory:** `20260827_1400__NZSCCM__CURRENT_BENDING_GLOBAL_RQ_AND_ELASTIC_AIRY_REGRESSION_R01.md`  
**Status:** `ELASTIC_GATE PASSED / BH032_BH050 NONLINEAR RERUN NOT FABRICATED / EXACT MODAL CURRENT-MOMENT PROJECTOR REQUIRED`

---

## 0. Purpose

The user-requested order is:

1. derive the full-halfwave current-bending `Rq`;
2. prove exact elastic degeneration to the original `Pcr/Airy` law;
3. only after that, reconnect frozen UHPC + qU-augmented R02/R06 and rerun BH032/BH050.

Steps 1–2 are complete and passed exactly.

This preflight attempts step 3 under the still-frozen rules

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = YES
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
SPATIAL_COLLOCATION = 0
INDEPENDENT_KAPPA_X_KAPPA_Y = 0
UHPC_NM_CHANGE = 0
R02_R06_PARAMETER_FIT = 0
```

---

# 1. What a nonlinear BH solve now actually needs

The current-bending equation is

\[
R_q^{CB}
=B_{cur}
+K_mb^3q(q+q_0)(q+2q_0)
-P\beta^2(q+q_0)=0,
\]

with

\[
B_{cur}
=\alpha^2\widehat M_x^{cur}
+\beta^2\widehat M_y^{cur}
-2\alpha\beta\widehat M_{xy}^{cur}.
\]

Therefore a BH nonlinear solve must evaluate, over the **entire** complete halfwave,

\[
\boxed{
\widehat M_x^{cur}
=\frac4{b\ell}\int_{\Omega_h}M_x^{cur}(x,y)\psi(x,y)dA,
}
\]

\[
\boxed{
\widehat M_y^{cur}
=\frac4{b\ell}\int_{\Omega_h}M_y^{cur}(x,y)\psi(x,y)dA.
}
\]

For the source-faithful staged closure `CB1`, gross twist may remain initial-elastic:

\[
M_{xy}^{CB1}=D_{66}^{0}\kappa_{xy}^{g},
\]

so no new nonlinear UHPC shear law is needed for this preflight.

The remaining mandatory objects are therefore the two **normal current modal moments** above.

---

# 2. Why the antinode terminal result cannot be reused

The rejected first-repair calculation evaluated the current section only at the controlling antinode.

Its values such as

\[
M_x^{sec}(s=1),\qquad M_y^{sec}(s=1)
\]

are pointwise section resultants.

The new generalized force requires weighted full-halfwave quantities

\[
\widehat M_x^{cur},\qquad\widehat M_y^{cur}.
\]

In general

\[
\boxed{
M_i^{sec}(s=1)\ne\widehat M_i^{cur}.
}
\]

Substituting the antinode value would silently replace a Galerkin projection by a one-point spatial rule, violating both the mechanics and the project zero-spatial-discretization rule.

Thus

```text
ANTINODE_ONE_POINT_REPLACEMENT = REJECTED
```

---

# 3. Full common strain field that must feed the current material operators

The already-recovered explicit halfwave kinematics uses the global coordinates

\[
(D,a_{\parallel},q)
\]

rather than terminal constants alone.

With

\[
X=\pi x/b,
\qquad Y=\pi y/\ell,
\qquad k=b/\ell,
\]

\[
H_s=\sin X\sin Y,
\qquad S_q=q_0q+\frac12q^2,
\]

its normal strain fields contain both finite membrane trigonometric terms and the common bending terms

\[
\varepsilon_x^g=A_x^g(X,Y;D,a_{\parallel},q)
+z\frac{\pi^2q}{b}H_s,
\]

\[
\varepsilon_y^g=A_y^g(X,Y;D,a_{\parallel},q)
+z\frac{\pi^2k^2q}{b}H_s.
\]

Therefore the directional affine-through-thickness inputs to the frozen current UHPC N-M maps are

\[
A_i=A_i(X,Y;D,a_{\parallel},q),
\qquad
B_i=B_i(X,Y;q).
\]

The steel faces additionally carry the already-derived local `qU` GL and `U^2` LL subscale, with local `U` condensed from R02/R06.

---

# 4. Exact-thickness integration is not the missing step

The frozen UHPC material already provides exact thickness primitives:

\[
(A_i,B_i)\mapsto(N_i^{UHPC},M_i^{UHPC})
\]

without thickness quadrature.

For compression, those primitives contain rational terms plus

\[
\ln(1+a_h\xi).
\]

For tension they contain lower incomplete gamma functions.

Thus at each spatial point the UHPC section moment is already exact.

The present gap is **not** thickness integration and **not** a missing UHPC constitutive law.

It is the next operation:

\[
M_i^{UHPC}(X,Y)\longrightarrow
\int_{0}^{\pi}\int_{0}^{\pi}
M_i^{UHPC}(X,Y)\sin X\sin Y\,dX\,dY.
\]

---

# 5. Why the existing finite harmonic qU backend does not immediately close this integral

The qU/LL steel Airy sources are finite products of trigonometric polynomials. Their exact integrals therefore reduce to finite harmonic moments.

The nonlinear current UHPC moment field is different.

After the frozen exact material primitive is composed with the full spatial strain field, a representative compression term has the form

\[
\ln\left[
1+a_h\,\Xi(A_i(X,Y)\pm h_cB_i(X,Y))
\right],
\]

and the tensile branch contains

\[
\gamma\left(s,
\frac{\Xi(X,Y)^{m_t}}{m_t}
\right).
\]

These are not, in general, finite trigonometric polynomials. Consequently the finite Fourier moment machinery that exactly closed `GG/GL/LL` cannot simply be reused by replacing its coefficients.

The qU R02/R06 operator adds another nonlinear algebraic layer because `U` is a condensed cubic root and the R06 active projection may change over the halfwave.

This observation is a backend classification only. It does **not** prove that no closed special-function or finite analytic-series representation exists.

---

# 6. Repository/source audit performed in this execution

The current repository was searched for an already-frozen full-halfwave engine that directly evaluates nonlinear current-material modal moments under the present SSUHPC material identity.

The search covered the current explicit/current-operator/D15/moment-first vocabulary and the available steel-shell execution tree.

A Yun-Lu local `D15` symbolic audit exists, but it addresses local steel-shell symbolic integrals; it is not a demonstrated full-halfwave nonlinear UHPC current-moment projector for the present SSUHPC operator.

No current repository artifact was located that can presently be invoked as a validated drop-in evaluator for

\[
\widehat M_x^{cur},\widehat M_y^{cur}
\]

with the exact frozen UHPC primitives plus spatially varying qU-augmented R02/R06, while keeping formal spatial quadrature zero.

Therefore an unrelated historical Case21 compiler is not silently imported merely because it used the name `D15`.

---

# 7. Exact status of the BH rerun

The requested structural gate is passed:

```text
CURRENT_BENDING_RQ = PASS
ELASTIC_AIRY_REGRESSION = EXACT_PASS
```

The nonlinear BH solve is **not** executed by any of the following forbidden shortcuts:

```text
ANTINODE_MOMENT_SUBSTITUTION = NO
GAUSS = NO
SIMPSON = NO
ADAPTIVE_QUADRATURE = NO
SPATIAL_MATERIAL_GRID = NO
CHEBYSHEV_COLLOCATION = NO
NEW_UHPC_SHEAR_LAW = NO
OLD_LAYER0_IMPORT = NO
FITTED_CURRENT_STIFFNESS_FACTOR = NO
```

Hence

```text
BH032_CURRENT_BENDING_NEW_ROOT = NOT_FABRICATED
BH050_CURRENT_BENDING_NEW_ROOT = NOT_FABRICATED
```

The current narrow gate is

\[
\boxed{
\text{exact zero-spatial-quadrature projection of nonlinear current normal moments over one complete halfwave}.
}
\]

This is substantially narrower than the previously suspected material/curvature/qU gaps.

---

# 8. Next admissible mathematical task

Without reopening material identity, the next task is to build or recover an analytic projector for

\[
\widehat M_x^{cur},\qquad\widehat M_y^{cur}
\]

from the already-frozen spatial strain basis and current material maps.

It must pass, in order:

1. **elastic regression** — return the exact modal moments already proved in the parent file;
2. **UHPC-only regression** — exact/controlled analytic projection of the frozen UHPC N-M moment field;
3. **steel R02 regression** — GL→0 returns the frozen R02/LL result;
4. **qU regression** — finite GL harmonic terms are reproduced exactly;
5. **R06 active-set audit** — any spatial active-set partition must be represented analytically, not by a material-point grid;
6. only then solve the coupled full-halfwave `(D,a_parallel,q)` system and report BH032/BH050 roots blind.

Until that projector exists, reporting new BH `Pu` from the current-bending theory would be less rigorous than stopping at this gate.
