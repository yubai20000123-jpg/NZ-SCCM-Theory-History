# NZ-SCCM — STEEL-SHELL COMMON R06 local-yield resultant gate V1

**Time:** 2026-08-25 15:30 +08:00  
**Parent:** `current/MILESTONE_RC_SSNC_FINAL_THEORY_20260825.md`  
**Scope:** common steel-face terminal operator shared by SSNC and SSUHPC  
**Status:** `THEORY FROZEN FOR BLIND GATE / NO COMPARATOR IN OPERATOR`

---

# 0. Scope and non-negotiable boundaries

R06 is **not** a UHPC repair. It replaces only the steel-face terminal handoff inside the common steel-shell layer.

Retained unchanged:

```text
initial full-composite ABD
Marguerre–Airy structural demand
integer half-wave selection
common terminal section strain state
R02 finite PBL/Yun elastic postbuckling amplitude and local harmonic field
NC or UHPC core N-M operator selected by parent theory
longitudinal web operator
steel-face offset stiffness included once only
R03 as Pu gate = NO
formal spatial quadrature = 0
material points = 0
effective width/area = PROHIBITED
comparator in root selection = 0
```

The only question addressed by R06 is how a locally buckled steel face reaches its full-area resultant capacity.

---

# 1. Source boundary and project extension

Yun's large-deflection theory supplies an elastic postbuckling mean-resultant path together with a nonuniform local membrane-stress field. The source ultimate construction is based on first local steel yielding and then taking the corresponding mean/resultant level; it is not an effective-width construction.

The current project steel material gate, R04, is two-dimensional ideal-EP von Mises. Therefore R06 makes one explicit project extension:

```text
Yun/R02 source concept: first local yield of the postbuckling local field
+
current R04 material surface: 2D von Mises
=
R06 finite local-Mises yield gate
```

This 2D Mises continuation is a **project extension**, not attributed verbatim to Yun. It is used because the common terminal steel face carries `(sigma_x,sigma_y,tau_xy)` and R04 already defines yielding by that same Mises surface.

---

# 2. Intrinsic branch selector — no empirical b/t switch

For each local R02 cell define the elastic local critical stress

\[
\sigma_{cr,s}^{E}
=
\frac{\pi^2 E_s t_s^2}{12(1-\nu_s^2)L_x^2}
\,k_{cr}(L_y/L_x).
\]

R06 uses the source-domain selector

\[
\boxed{
\sigma_{cr,s}^{E}\ge f_y
\;\Rightarrow\;
\text{YIELD-FIRST branch: retain R04 exactly.}
}
\]

\[
\boxed{
\sigma_{cr,s}^{E}< f_y
\;\Rightarrow\;
\text{LOCAL-BUCKLING-FIRST branch: activate R02 local-yield admissibility.}
}
\]

This is not a fitted `b/t > constant` rule. It is an event-order test computed from the steel cell itself.

Consequently, any yield-first case is an **exact non-regression** of the existing R04 operator.

---

# 3. R02 field retained without modification

For a face centroid strain vector

\[
\boldsymbol\varepsilon_f
=(\varepsilon_x,\varepsilon_y,\gamma_{xy}),
\]

R02 receives compression-positive normal strains and solves the existing cubic

\[
B_3U^3+B_1U+B_0=0
\]

with the existing nonnegative-real-root / minimum-condensed-energy rule.

It returns

\[
\bar{\boldsymbol\sigma}_{R02}
\]

and the finite local harmonic fluctuation

\[
\widetilde{\boldsymbol\sigma}_{R02}(x,y),
\]

so that

\[
\boldsymbol\sigma_{loc}(x,y)
=
\bar{\boldsymbol\sigma}_{R02}
+
\widetilde{\boldsymbol\sigma}_{R02}(x,y).
\]

R06 does not alter the R02 amplitude equation, harmonic coefficients, condensed energy, or full-area mean definition.

---

# 4. Finite-algebraic local yield functional

For the current axial terminal cases `gamma_xy=0`, introduce

\[
u=\cos(k_xx),\qquad v=\cos(k_yy).
\]

Because R02 contains only the finite harmonics

```text
(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),
```

the two normal stresses are finite polynomials in `(u,v)` and the local shear has the form

\[
\tau_{xy}
=\sqrt{1-u^2}\sqrt{1-v^2}\,P_\tau(u,v).
\]

Hence

\[
\boxed{
\Phi(u,v)
=
\sigma_x^2-\sigma_x\sigma_y+\sigma_y^2+3\tau_{xy}^2
}
\]

is a finite polynomial of total degree no greater than six on

\[
(u,v)\in[-1,1]^2.
\]

The global maximum is obtained from the finite candidate set:

1. interior algebraic roots of `dPhi/du = dPhi/dv = 0`;
2. stationary roots on `u=+/-1`;
3. stationary roots on `v=+/-1`;
4. the four corners.

No spatial grid, Gauss point, collocation point, or effective width is introduced.

Thus

```text
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
```

For future nonzero uniform shear, the same rule can be lifted to finite algebraic variables `(cosX,sinX,cosY,sinY)` with the two unit-circle constraints. That extension is not needed by the present Z6/T360/BH032 axial terminal gate.

---

# 5. Path-free radial local-yield projection

The common terminal theory is a direct capacity-contact theory rather than an incremental material history model. Therefore R06 must remain path-free.

For a fixed current face strain direction `epsilon_f`, define the radial family

\[
\boldsymbol\varepsilon_f(\eta)
=\eta\boldsymbol\varepsilon_f,
\qquad 0\le\eta\le1.
\]

At each `eta`, R02 is re-condensed from its own cubic and finite local field. Define

\[
\Psi(\eta)
=
\max_{[-1,1]^2}\Phi(u,v;\eta)-f_y^2.
\]

For a local-buckling-first cell:

- if `Psi(1)<=0`, the face remains on the current R02 elastic-postbuckling mean state;
- if `Psi(1)>0`, define the first radial local-yield boundary

\[
\boxed{
\eta_y
=
\min\{\eta\in(0,1]:\Psi(\eta)=0\}.
}
\]

The R06 full-area face stress is then

\[
\boxed{
\bar{\boldsymbol\sigma}_{R06}(\boldsymbol\varepsilon_f)
=
\bar{\boldsymbol\sigma}_{R02}(\eta_y\boldsymbol\varepsilon_f).
}
\]

The face resultants are still the gross/full-area resultants

\[
\boxed{
\mathbf N_f=t_s\bar{\boldsymbol\sigma}_{R06},
\qquad
\mathbf M_f=z_f\mathbf N_f.
}
\]

No reduced width or reduced area appears anywhere.

The projection is frozen only after local yield; R06 does not invent a post-yield local-amplitude evolution law. This is consistent with the current direct terminal-capacity architecture.

---

# 6. Exact non-regression requirement

R06 is admissible only if

\[
\sigma_{cr,s}^{E}\ge f_y
\]

causes an exact operator degeneration

\[
\boxed{
R06\equiv R04.
}
\]

Therefore Z6 R05 is the mandatory first gate. Its current root and all steel-face resultants must remain bit-for-bit/theory-identical apart from ordinary floating-point representation.

---

# 7. Blind execution order

The production-promotion gate is fixed as:

```text
G1  Z6 strict non-regression
G2  T360 blind R06 root
G3  BH032 blind R06 root
G4  finite-algebraic global-max certificate at the fixed R06 states
G5  freeze all roots and branch identities
G6  only then reopen Abaqus/comparators
```

No comparator may modify `sigma_cr/fy`, R02 coefficients, R06 radial projection, active algebraic local maximum, or root selection.

---

# 8. Promotion criteria

R06 may supersede R04 as the common steel-face production gate only if:

```text
Z6_NONREGRESSION = PASS
T360_BLIND_ROOT = UNIQUE/ADMISSIBLE
BH032_BLIND_ROOT = UNIQUE/ADMISSIBLE
LOCAL_MAX_CERTIFICATE = FINITE-ALGEBRAIC / NO SPATIAL GRID
RESULTANT_CLOSURE = PASS
COMPARATOR_IN_ROOT_SELECTION = 0
```

If these pass, the change belongs to the **steel-shell common layer** and is inherited identically by SSNC and SSUHPC.
