# NZ-SCCM — Plate stress-control decomposition audit R01

**Time:** 2026-08-23 15:18 +08:00  
**Status:** `DIAGNOSTIC_ONLY / NO_CURRENT_STATE_CHANGE / NO_SWARTZ_Pu_EXECUTION`

## 0. Scope

This audit does **not** create a new RC production terminal rule and does not recompute any Swartz panel ultimate load. It tests whether the frozen Marguerre–Airy structural resultants can be decomposed into a two-dimensional membrane state plus through-thickness bending-induced layer/face states, and whether the existing Nguyen/Foster source relations provide finite local event functions without introducing a four-dimensional `Nx-Ny-Mx-My` section-capacity surface.

Governing structural architecture remains

\[
\text{Airy/Galerkin demand}\to\text{terminal material/capacity layer}\to P_u.
\]

No `det J_sec` terminal and no experimental load in any criterion.

---

## 1. Exact Kirchhoff–Nguyen decomposition

Use engineering-strain vectors

\[
\mathbf e(z)=
\begin{bmatrix}\varepsilon_x(z)\\\varepsilon_y(z)\\\gamma_{xy}(z)\end{bmatrix},
\qquad
\mathbf e^m=
\begin{bmatrix}\varepsilon_x^m\\\varepsilon_y^m\\\gamma_{xy}^m\end{bmatrix},
\qquad
\boldsymbol\kappa=
\begin{bmatrix}\kappa_x\\\kappa_y\\\kappa_{xy}\end{bmatrix}.
\]

Nguyen Eq. (6.3), with stress-free initial imperfection and load-induced deflection `w_m`, gives exactly

\[
\boxed{\mathbf e(z)=\mathbf e^m+z\boldsymbol\kappa},
\]

with

\[
\boxed{\kappa_x=-w_{m,xx},\qquad \kappa_y=-w_{m,yy},\qquad \kappa_{xy}=-2w_{m,xy}}.
\]

The initial imperfection enters only the nonlinear middle-surface membrane strain through the `w_0 w_m` terms; it does not enter the bending curvature increment. This matches the frozen V1 rule that membrane geometry uses `q(q+2q0)` while bending uses `q`.

For the orthotropic extensional matrix

\[
\mathbf A=
\begin{bmatrix}
A_{11}&A_{12}&0\\
A_{12}&A_{22}&0\\
0&0&A_{66}
\end{bmatrix},
\qquad
\Delta_A=A_{11}A_{22}-A_{12}^2,
\]

the current V1 Airy compatibility uses the same initial elastic `A`, therefore the membrane strain associated with the Airy membrane resultants is

\[
\boxed{\mathbf e^m=\mathbf A^{-1}\mathbf N},
\qquad
\mathbf N=
\begin{bmatrix}N_x\\N_y\\N_{xy}\end{bmatrix},
\]

or explicitly

\[
\boxed{\varepsilon_x^m=\frac{A_{22}N_x-A_{12}N_y}{\Delta_A}},
\]

\[
\boxed{\varepsilon_y^m=\frac{-A_{12}N_x+A_{11}N_y}{\Delta_A}},
\]

\[
\boxed{\gamma_{xy}^m=\frac{N_{xy}}{A_{66}}}.
\]

For a general frozen finite longitudinal waveform

\[
w_m=bq\sin(\alpha x)\Phi(y),
\]

the curvature demand is exactly

\[
\boxed{\kappa_x=bq\alpha^2\sin(\alpha x)\Phi(y)},
\]

\[
\boxed{\kappa_y=-bq\sin(\alpha x)\Phi''(y)},
\]

\[
\boxed{\kappa_{xy}=-2bq\alpha\cos(\alpha x)\Phi'(y)}.
\]

For the single sine V1, `Phi=sin(beta y)`, these reduce to the familiar single-halfwave expressions.

Hence the two physical faces are

\[
\boxed{\mathbf e^\pm=\mathbf e^m\pm\frac{t}{2}\boldsymbol\kappa}.
\]

At reinforcement layer `z_l`, aligned with x/y,

\[
\boxed{\varepsilon_{sx,l}=\varepsilon_x^m+z_l\kappa_x},
\qquad
\boxed{\varepsilon_{sy,l}=\varepsilon_y^m+z_l\kappa_y}.
\]

No independent transverse `N-M` section is introduced. `Mx,My,Mxy` act through curvature/layer strain.

---

## 2. Principal layer state remains finite analytic

At any fixed `(q,x,y)`, each Cartesian strain component is affine in `z`:

\[
\varepsilon_x=a_x+b_xz,\quad
\varepsilon_y=a_y+b_yz,\quad
\gamma_{xy}=a_g+b_gz.
\]

The in-plane principal strains are

\[
\boxed{
\varepsilon_{1,2}(z)
=\frac{\varepsilon_x+\varepsilon_y}{2}
\pm
\sqrt{
\left(\frac{\varepsilon_x-\varepsilon_y}{2}\right)^2
+\left(\frac{\gamma_{xy}}{2}\right)^2
}}
\]

and therefore have the form

\[
L_0+L_1z\pm\sqrt{Q_0+Q_1z+Q_2z^2}.
\]

Thus layer-state thresholds are finite algebraic scalar-root problems in `z`; no through-thickness Gauss/material-point grid is required. Face checks are the two explicit endpoints `z=+-t/2`, while any source branch front in the interior can be localized by its finite scalar threshold equation.

---

## 3. Candidate source-event functions available from Nguyen/Foster

### 3.1 Membrane two-dimensional source state

At `z=0`, evaluate the full membrane tensor from `e^m`, rotate to principal axes, and apply the existing Nguyen/Foster biaxial material relations.

A membrane source-event function can be defined generically as

\[
F_{mem,event}(q,x,y)=0
\]

when the current undamaged principal stress state first reaches the Nguyen Eqs. (3.17)-(3.20) biaxial envelope. This is a **cracking/crushing state-transition event**, not automatically a plate ultimate condition.

### 3.2 Concrete compression-face events

For each face `s=+,-`, feed `e^s` into the same principal-state map.

For an undamaged CC route, the source peak stresses come from the biaxial envelope and the corresponding peak compressive strains from Nguyen Eqs. (3.41)-(3.42). The Appendix-B/source implementation hands off to crushed CC when the controlling equivalent-uniaxial compressive strain reaches its source peak. A face event may therefore be written schematically

\[
\boxed{F_{face,CC}^{s}=\frac{|\varepsilon_{c,u}^{s}|}{|\varepsilon_{c,p}^{s}|}-1}.
\]

For cracked TC, Nguyen Sec. 3.4.5 states that crushing begins when the magnitude of the minor compressive strain reaches the peak compressive strain, so

\[
\boxed{F_{face,TCX}^{s}=\frac{|\varepsilon_{c}^{s}|}{|\varepsilon_{c,p}^{s}|}-1}.
\]

Post-crushing continues to the bilinear residual plateau; the source therefore does **not** identify first crushing onset as wall ultimate failure.

A later severe-degradation event can be recorded at the source post-crushing plateau threshold

\[
\boxed{F_{face,res}^{s}=\frac{|\varepsilon_c^{s}|}{\gamma_2|\varepsilon_{c,p}^{s}|}-1},
\]

where the stress has fallen to the Nguyen/Foster `0.1 sigma_p` residual branch. This is a finite source event but still is not explicitly labelled by Nguyen as the wall-level `Pu` terminal.

### 3.3 Tension/cracking events

Nguyen/Foster supplies TC and TT cracking and tension-stiffening transitions. They can be evaluated at the membrane state, each face, or any finite branch-front root through thickness. These are material-state events (`U->TC`, `U->TT`, softening-to-residual, etc.), but cracking itself is not a justified plate-ultimate condition.

### 3.4 Reinforcement events

For every discrete reinforcement layer and direction,

\[
F_{s,y}^{(l,d)}=\frac{|\varepsilon_{s,l,d}|}{\varepsilon_y}-1,
\]

is the steel yield event. Nguyen uses a bilinear post-yield law, and for the Swartz24 analyses the post-yield tangent is zero, so yield is a state change rather than automatic wall failure.

Nguyen's Swartz analysis also specifies a reinforcement failure strain `epsilon_su=0.04`, so a source-explicit terminal candidate exists:

\[
\boxed{F_{s,u}^{(l,d)}=\frac{|\varepsilon_{s,l,d}|}{0.04}-1}.
\]

This is finite because the number of reinforcement layers/directions is finite.

---

## 4. What is and is not closed

### PASS — kinematic decomposition

`Nx,Ny,Nxy` map uniquely to the V1 membrane strain through `A^{-1}`, while `Mx,My,Mxy` are represented through the exact load-induced curvature from `w_m`. The total layer strain is `e^m+z kappa`.

### PASS — no second beam-like transverse capacity is required

The bending resultants affect local concrete/steel states through the curvature term. A separate `Nx-Mx` section-capacity curve is not mathematically required to inspect two-dimensional material states.

### PASS — finite material-event family exists

Nguyen/Foster directly supplies finite events for biaxial-envelope crossing, TC/TT cracking, CC/TCX crushing onset, post-crushing residual-plateau entry, steel yield, and steel failure.

### PASS — zero through-thickness quadrature can be retained

Because the layer strain tensor is affine in `z`, principal strain thresholds reduce to algebraic scalar root localization. No formal layer grid is necessary.

### FAIL / OPEN — complete new plate `Pu` terminal is not source-closed

The source does **not** authorize

\[
P_u=\min\{P_{first\ crack},P_{first\ crush},P_{first\ steel\ yield}\}.
\]

Nguyen explicitly continues cracked concrete, crushed concrete and yielded reinforcement after these events. Therefore `F_membrane`, `F_face,C` and `F_steel,yield` are source-valid **state-control events**, but not all are source-valid **ultimate terminals**.

The only clearly terminal reinforcement datum in the Swartz setup is the steel failure strain. Concrete has a post-crushing residual branch rather than a separately declared wall-failure strain.

### OPEN — one-way Airy demand after major material degradation

Nguyen Chapter 6 states that inelastic walls generally couple in-plane and out-of-plane behaviour. Its later uncoupling is made only for predominantly axial stress, small bending contribution and an uncracked section. Hence once a proposed face gate indicates substantial cracking/crushing, continuing to use the unchanged initial-elastic Airy demand without redistribution is an additional modelling assumption, not a direct Nguyen result.

---

## 5. Minimal architecture supported by this audit

The following is admissible as a **diagnostic/event architecture**:

\[
\boxed{
\mathbf N(q,x,y)
\xrightarrow{A^{-1}}
\mathbf e^m(q,x,y)
}
\]

\[
\boxed{
\mathbf M(q,x,y)\leftrightarrow\boldsymbol\kappa(q,x,y)
}
\]

\[
\boxed{
\mathbf e(z)=\mathbf e^m+z\boldsymbol\kappa
}
\]

followed by a finite family

\[
\{F_{mem,event},F_{face,CC}^{\pm},F_{face,TCX}^{\pm},F_{face,res}^{\pm},F_{s,y}^{l,d},F_{s,u}^{l,d},\ldots\}.
\]

Each `F_i=0` can be solved along the monotone structural parameter `q` without loading steps. But the production rule

\[
q_u=\min_i q_i
\]

is **not yet authorized**, because the terminal/nonterminal identity of several concrete events is unresolved.

The existing one-dimensional `N_y-M_y` capacity may therefore be retained as the current production terminal while these new two-dimensional plate-state events are treated as diagnostics only.

---

## 6. Verdict

```text
PLATE_STRESS_DECOMPOSITION = PASS
MEMBRANE_2D_STATE_FROM_AIRY = PASS
BENDING_TO_LAYER_STRAIN = PASS
SEPARATE_TRANSVERSE_N_M_CAPACITY_REQUIRED = NO
NGUYEN_FINITE_EVENT_FUNCTIONS = PASS
ZERO_THICKNESS_QUADRATURE = RETAINABLE
FIRST_CRACK_AS_Pu = REJECT
FIRST_CRUSH_AS_Pu = NOT_SOURCE_AUTHORIZED
FIRST_STEEL_YIELD_AS_Pu = REJECT
STEEL_FAILURE_STRAIN_TERMINAL = SOURCE_AVAILABLE
COMPLETE_NEW_2D_Pu_RULE = OPEN
CURRENT_GITHUB_STATE = NOT_CHANGED
```

The next theoretical question is no longer how to manufacture a four-dimensional section-capacity surface. It is which finite local material events, if any, can legitimately be promoted from **state transitions** to **plate-level ultimate terminals**, and under what conditions the one-way elastic Airy demand remains admissible after those events.