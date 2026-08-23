# NZ-SCCM — RC wall/panel ultimate-terminal precedent audit R01

**Time:** 2026-08-23 15:35 +08:00  
**Status:** `LITERATURE_AUDIT / DIAGNOSTIC_ONLY / NO_CURRENT_STATE_CHANGE / NO_SWARTZ_Pu_EXECUTION`

## 0. Question

This audit asks which local material events are actually promoted to wall/panel ultimate failure in mature reinforced-concrete wall analyses, with emphasis on axially compressed two-way wall panels and methods structurally close to the current Marguerre–Airy branch.

The target is not to invent a new RC terminal rule. The target is to classify precedent into: global ultimate definition, primary-direction section check, transverse-direction check, and local material events that remain internal state transitions.

---

## 1. Attard 1994/1995: closest analytical precedent to current architecture

Attard's approximate two-way wall method does **not** form one four-dimensional `Nx-Ny-Mx-My` capacity surface.

The workflow is:

1. calculate wall buckling load;
2. use buckling to estimate amplified longitudinal and transverse moments;
3. check the loaded-direction axial force plus amplified moment against a wall/column interaction diagram;
4. check the transverse amplified moment against a transverse yield-moment capacity.

Attard states that the design axial force and amplified moments are checked against wall ultimate capacity through an interaction diagram. Later he makes the directional split explicit: the design actions `Nx` and `Mxx*` are compared to the wall ultimate capacity by a column interaction diagram, while `Myy*` must remain below the yield moment.

Hence the mature analytical precedent is asymmetric:

\[
F_{L}(N_L,M_L)=0,
\qquad
F_T(M_T)=0,
\]

not

\[
\Phi(N_x,N_y,M_x,M_y)=0.
\]

This is especially relevant because Attard's purpose is precisely two-way bending of slender RC core walls.

Limits of direct transfer: Attard assumes the wall remains in compression for the derivation, uses a simplified transverse modulus/cracking treatment, and estimates amplified moments rather than a fully nonlinear postbuckling material redistribution.

---

## 2. Nguyen 1996: same hierarchy is retained in Chapter 7 examples

Nguyen's Chapter 6 material model contains cracking, crushing and reinforcement yielding as continuing constitutive states. For inelastic walls he explicitly notes that in-plane and out-of-plane behavior are generally coupled; his later uncoupling is justified only when stress is predominantly axial, bending contribution is small, and the section is assumed uncracked.

In the Chapter 7 wall examples Nguyen does not identify first local cracking/crushing as wall ultimate. Instead he evaluates:

- loaded-direction `Nyy-Myy` against the Attard wall-section interaction diagram;
- unloaded-direction `Mxx` against the cracking moment where appropriate;
- whether the wall remains uncracked / uncrushed in the relevant direction.

This is again a hierarchy of directional checks, not a four-resultant terminal surface.

Therefore the previous diagnostic conclusion remains valid:

```text
FIRST_CRACK_AS_WALL_Pu = NOT_SUPPORTED
FIRST_LOCAL_CRUSHING_AS_WALL_Pu = NOT_SUPPORTED_BY_NGUYEN_CONSTITUTIVE_PATH
FIRST_STEEL_YIELD_AS_WALL_Pu = NOT_SUPPORTED
```

---

## 3. Saheb–Desayi / Doh–Fragomeni experimental wall-panel tradition

The two-way wall-panel literature distinguishes cracking load from ultimate/failure load. Saheb and Desayi report both cracking and ultimate loads separately, and derive ultimate-load equations directly from global test capacity rather than from first local material events.

Doh and Fragomeni similarly trace load–deflection histories to failure. For their two-way panels the response becomes strongly nonlinear approaching failure; the brittle specimens cease to sustain additional loading after the maximum load. Thus the experimentally observed ultimate is a **global maximum/failure load**, not first crack, first steel yield, or first local concrete peak strain.

The implication for the current project is structural: a local material event can be a state gate, but experimental `Pu` corresponds to the global load-carrying maximum or loss of load-carrying ability.

---

## 4. Nonlinear FE wall literature

Modern nonlinear wall analyses generally continue the constitutive solution through cracking, yielding, crushing and softening. Ultimate capacity is identified from the global load–displacement response / peak load and validated together with observed failure modes.

Examples reviewed here include:

- nonlinear layered FE analyses of two-way concrete wall panels, which compare predicted ultimate loads, load–deflection response up to failure, deflected shapes and crack patterns against tests;
- displacement-controlled concrete wall-panel analyses used specifically to pass into nonlinear response and trigger failure;
- state-of-the-art nonlinear RC wall models, where peak load capacity is a principal validation target while individual strength-degradation mechanisms (concrete crushing, reinforcement buckling/fracture, etc.) determine how post-peak loss occurs.

For flexure-controlled structural walls, compression-controlled failure is commonly characterized by concrete crushing together with reinforcement instability, but the wall failure definition is associated with degradation/loss of global load-carrying capacity rather than the instant at which the first integration point reaches a local crushing threshold.

---

## 5. Precedent classification

### Class A — source-valid wall/panel ultimate definitions

1. **Global maximum load / loss of load-carrying capacity** in experiments and full nonlinear analysis.
2. **Primary loaded-direction section interaction capacity** in Attard-type analytical design.
3. **Transverse yield-moment limit** as a separate directional check in Attard's two-way wall method.

### Class B — source-valid state/control events but not universal wall ultimate

- first tensile cracking;
- first TC/TT transition;
- first concrete peak compressive strain / crushing onset;
- first reinforcement yield;
- entry into post-crushing softening/residual branches.

These can modify stiffness/material state and may become part of a failure mechanism, but the reviewed sources do not justify universally setting wall `Pu` equal to the first occurrence.

### Class C — terminal events that may be physical failure modes in specific models

- reinforcement rupture / prescribed steel ultimate strain;
- severe concrete crushing with associated global strength degradation;
- reinforcement buckling plus concrete crushing in compression-controlled wall failure;
- global instability / maximum-load point.

Whether any Class C event is a standalone algebraic terminal for the present Swartz panels remains to be demonstrated.

---

## 6. Consequence for NZ-SCCM

The literature does **not** support replacing the current one-dimensional `N-M` terminal by

\[
P_u=\min\{P_{first\ crack},P_{first\ crush},P_{first\ yield}\}.
\]

Nor does it support a mechanically automatic four-dimensional section surface.

The strongest precedent compatible with the current explicit branch is Attard-like hierarchical capacity checking:

\[
\boxed{
\text{global plate demand}
\to
\begin{cases}
\text{loaded-direction }N-M\text{ interaction},\\
\text{transverse physical bending/material gate},\\
\text{finite local state events for validity/state tracking}
\end{cases}
}
\]

with the ultimate candidate selected from physically terminal modes only.

For a fully nonlinear reference model, the more fundamental definition remains the global peak-load / loss-of-capacity condition. However, the current frozen elastic-Air y backbone is strictly monotone and has no material redistribution feedback; therefore it cannot reproduce a global load maximum by itself. Any explicit replacement must be a source-justified terminal approximation, not a relabeling of the first local material event.

---

## 7. Next narrow gate

Before changing the production theory, test an **Attard-inspired directional hierarchy** on the current analytical demand, without inventing new material coefficients:

1. retain the current loaded-direction `N_y-M_y` terminal exactly as one candidate;
2. derive only the transverse **cracking/yield/severe-material-state** demand checks from the same current curvature and reinforcement layout;
3. classify each transverse event as `STATE_ONLY` or `POTENTIAL_TERMINAL` from source meaning;
4. do not use first crack/yield/crush automatically as `Pu`;
5. compare event ordering for the accepted Swartz analysis set before any new ultimate-load formula is adopted.

This gate is intentionally diagnostic. It tests whether Case21's previously large transverse demand represents an actual terminal mechanism or merely an early local/state event that mature RC wall methods would allow to redistribute through.
