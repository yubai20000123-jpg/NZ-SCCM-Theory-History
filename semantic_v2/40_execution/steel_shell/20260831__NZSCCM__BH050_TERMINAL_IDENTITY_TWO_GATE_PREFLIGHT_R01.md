# NZ-SCCM — BH050 terminal identity / two-gate preflight R01

**Date:** 2026-08-31  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Status:** `DIAGNOSTIC ONLY / MAIN UNCHANGED / NO COMPARATOR IN ROOT SELECTION`

## 0. Governance correction before execution

This note inherits `20260831__NZSCCM__CURVATURE_CAPACITY_COORDINATE_CORRECTION_AND_BH050_RECALC_R02.md`.

The current identities are:

```text
q = sole global structural postbuckling amplitude
kappa_geo(q) = actual physical structural curvature from w_d
Bx_cap, By_cap = affine coordinates on the terminal N-M capacity surface
Bx_cap, By_cap != physical global curvature
```

Therefore the old proposal `Bcap = kappa_geo` is not executed as a correction of the current Airy-capacity-contact theory. It would define a new deformation-compatible theory and requires a new equilibrium derivation.

The present diagnostic instead audits a different issue: whether the existing `J4` section-capacity fold has been given the same physical identity as a full-structure stability/peak condition without an independent proof.

---

## 1. Existing section-capacity terminal

For the frozen BH050 Airy front:

\[
P^A(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0),
\]

with

```text
Pcr = 19.5818772367311 MN
C   = 10841.3718065234 MN
q0  = 0.0025
b   = 2500 mm
```

the source-audited capacity-contact terminal is

\[
q_{J4}=0.004772819645833164,
\]

\[
P_{J4}=13.3563763545430\;MN.
\]

Its physical q-derived antinode curvature is

\[
\kappa_{geo,J4}=\frac{\pi^2q_{J4}}{b}
=1.88423367128\times10^{-5}\;mm^{-1}.
\]

This remains a valid **Airy demand / section N-M capacity-contact terminal**. This note does not invalidate its algebraic closure.

---

## 2. What `J4` actually differentiates

The capacity-contact equations have the form

\[
\mathbf R_4(\mathbf x,q)
=\mathbf S^{cap}(\mathbf x)-\mathbf D^A(q)=\mathbf0,
\]

where the four coordinates `x` parameterize the section N-M capacity surface.

Because `D^A(q)` does not depend on these section-capacity coordinates,

\[
\boxed{
\mathbf J_4
=\frac{\partial\mathbf R_4}{\partial\mathbf x}
=\frac{\partial\mathbf S^{cap}}{\partial\mathbf x}.
}
\]

Consequently

\[
\det\mathbf J_4=0
\]

is rigorously a rank-loss / fold condition of the **section resultant-capacity map**.

It is not, by definition alone, the determinant of the tangential stiffness matrix of the whole plate/column structural system.

Hence the implication

\[
\det J_4=0
\quad\Longrightarrow\quad
\text{first global/local structural instability or first load peak}
\]

requires an additional proof. That proof is not present in the current R4-J4 capacity-contact construction.

---

## 3. Independent source identity for a structural stability terminal

Nguyen's stability formulation identifies `q` as the generalized freedom vector of the whole wall and forms a **structure tangential stiffness matrix** `KT` from current material tangential moduli/stresses and element tangent/stability matrices. Instability is located when the determinant of that structure tangential matrix becomes zero.

This establishes a clean conceptual distinction:

```text
section-capacity fold:  det(J4) = 0
structural stability:   det(KT_struct) = 0  (or equivalent modal tangent = 0)
```

The two conditions may coincide in some parameter range, but their equivalence cannot be assumed.

---

## 4. Same-load BH050 post-check — executed without changing any root

The canonical BH050 FE reaction peak `12.591227 MN` is used here **only as an external post-check coordinate**. It is not used to fit a material parameter, select a theory root, alter `J4`, or define a new terminal.

Solve the unchanged Airy equation

\[
19.5818772367311\frac{q}{q+0.0025}
+10841.3718065234\,q(q+0.005)
=12.591227.
\]

The positive connected solution is

\[
\boxed{q_{same-load}=0.004117589557476763}.
\]

Therefore

\[
\boxed{
\frac{q_{same-load}}{q_{J4}}
=0.862716352811
}
\]

and the external peak lies, on the unchanged Airy amplitude coordinate, about

\[
\boxed{13.7284\%}
\]

before the J4 capacity fold.

The load difference is

\[
\boxed{
P_{J4}-P_{same-load}
=0.765149354543\;MN
}
\]

which is

\[
5.72872\%\text{ of }P_{J4},
\qquad
6.07685\%\text{ of }P_{same-load}.
\]

The corresponding physical curvature is

\[
\boxed{
\kappa_{geo,same-load}
=\frac{\pi^2q_{same-load}}{2500}
=1.62555920073409\times10^{-5}\;mm^{-1}
}.
\]

Again, this does **not** prove that structural stability is lost at this q. It only locates the external peak relative to the current section-capacity terminal on the unchanged Airy coordinate.

---

## 5. Exact unchanged Airy demand at the same-load coordinate

At

\[
q=0.004117589557476763
\]

\[
Q_q=q(q+2q_0)=3.75424915512255\times10^{-5}.
\]

Using the frozen coefficients

```text
Kx = 4.272925966136171e6 N/mm
G  = 4.400171479082513e6 N/mm
Jx = 6.234616244717026e6 N
Jy = 6.298311709061200e6 N
s  = 1
```

gives

\[
\boxed{N_x^A=160.416286983\;N/mm},
\]

\[
\boxed{N_y^A=-4871.297399423\;N/mm},
\]

\[
\boxed{M_x^A=25671.5907441\;N},
\]

\[
\boxed{M_y^A=25933.8625230\;N}.
\]

These are pure evaluations of the already-frozen Airy formulas; no FEM quantity enters except the chosen post-check load level.

---

## 6. What this execution proves and what it does not

### Proven now

1. `J4` is mathematically a Jacobian of the section resultant-capacity map, not automatically the whole-structure tangent stiffness matrix.
2. The current theory has no demonstrated identity theorem `det(J4)=0 <=> first structural instability/peak`.
3. The external BH050 peak, when mapped onto the unchanged Airy load-amplitude law, occurs at `q=0.00411758955748`, substantially before the current `q_J4=0.00477281964583` section-capacity fold.
4. Therefore a **too-late terminal-gate hypothesis** is now a well-posed, discriminating hypothesis and is distinct from the superseded `Bcap as physical curvature` interpretation.

### Not proven yet

1. It is not yet proven that an independently assembled current structural tangent actually becomes singular at `q < q_J4`.
2. `sigma_min(J4)` at `q_same-load` has not been evaluated because an archived/accessible continuous `J4(q)` branch evaluator has not yet been recovered.
3. A current global modal tangent cannot be obtained by simply renaming `J4`; it must use actual physical virtual strains/curvatures and current constituent consistent tangents.
4. No new `Pu` is reported from this diagnostic.

---

## 7. Next executable two-gate audit

Keep the current Airy branch and all current material operators unchanged. Do not feed the diagnostic back into the root.

For states along the existing connected branch evaluate two separate indicators:

### Gate A — section capacity reserve

\[
g_{cap}(q)=\sigma_{min}[J_4(q)].
\]

Normalize by a fixed reference tangent scale so that values at different q are comparable.

### Gate B — structural modal tangent reserve

Construct a scalar retained-mode tangent

\[
g_{str}(q)
=\delta^2\Pi_{int}^{cur}[\phi]
-\delta^2W_{geom}^{cur}[\phi],
\]

or the exactly equivalent projected structure tangent, from:

```text
physical retained global mode phi
actual q-derived virtual strain/curvature perturbation
current UHPC consistent tangent
upper steel R02 consistent tangent
lower steel R06 active-set consistent tangent
web tangent
current membrane resultants entering geometric stiffness
```

No `Bcap` derivative may be interpreted as physical curvature stiffness.

The decisive condition is:

```text
if g_str(q_s)=0 at q_s < q_J4
and g_cap(q_s) > 0,
then STRUCTURAL_INSTABILITY_PRECEDES_SECTION_CAPACITY_FOLD = PASS.
```

If instead both indicators vanish together within derivation/numerical tolerance, the current J4 terminal gains an independent structural justification.

---

## 8. Status ledger

```text
TERMINAL_IDENTITY_DISTINCTION = PROVEN
J4_IDENTITY = SECTION_NM_CAPACITY_MAP_JACOBIAN
J4_AS_GLOBAL_STRUCTURAL_TANGENT = NOT_PROVEN
SAME_LOAD_AIRY_Q_POSTCHECK = EXECUTED
q_same_load = 0.004117589557476763
q_J4 = 0.004772819645833164
q_same_load/q_J4 = 0.862716352811
P_gap = 0.765149354543 MN
FIXED_BCAP_EQUALS_KAPPA_AS_EXISTING_THEORY_CORRECTION = PROHIBITED
J4_RESERVE_AT_SAME_LOAD = NOT_YET_AVAILABLE
CURRENT_STRUCTURAL_TANGENT_INDICATOR = NOT_YET_ASSEMBLED
STRUCTURAL_TANGENT_ZERO_CROSSING = NOT_YET_EXECUTED
NEW_Pu = NOT_REPORTED
COMPARATOR_IN_ROOT_SELECTION = 0
PRODUCTION_MAIN_CHANGED = NO
```
