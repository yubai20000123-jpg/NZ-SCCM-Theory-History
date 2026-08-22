# NZ-SCCM — NC-M6 2D TC crack-front exact execution R01

**Time:** 2026-08-22 21:30 +08:00  
**Status:** `EXECUTED / EXPLICIT_STRUCTURAL_PATH_UNCHANGED / EXACT_SECTION_PRIMITIVE_PASS / SAME_LAW_JACOBIAN_PASS / NO_Pf_BACKFIT`

## 0. Governing boundary

The explicit structural path is unchanged. This execution reuses the frozen source-waveform operator and the full two-independent-affine-slope section interface

\[
\lambda_x(z)=a_x+b_xz,\qquad \lambda_y(z)=a_y+b_yz,
\]

with the same structural relation

\[
P_\Phi(q)=P_{cr,\Phi}\frac{q}{q+q_0}+C_\Phi q(q+2q_0).
\]

Only the NC TC material layer is changed.

```text
EXPLICIT_STRUCTURAL_PATH_CHANGED = FALSE
SOURCE_WAVEFORM_CHANGED = FALSE
TWO_INDEPENDENT_AFFINE_SLOPE_SECTION_INTERFACE = UNCHANGED
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_MATERIAL_POINTS = 0
Pf_IN_ROOT_SELECTION = 0
NC_CC_CHANGED = FALSE
NC_TT_CHANGED = FALSE
VC_GAMMA_FORM_CHANGED = FALSE
```

Reproduction script:

`semantic_v2/40_execution/rc/20260822_2130__NZSCCM__NC_M6_2D_TC_CRACK_FRONT_EXACT_SECTION.py`

---

## 1. NC-M6 material change

For a TC point, let `p0=-sigma_c0>=0` be the current undamaged compression-stress magnitude from the unchanged compression backbone. The source TC crack front is

\[
f_{cr}^{TC}(p_0)=
\begin{cases}
f_t\left(1-\dfrac{p_0}{2f_c}\right),&0\le p_0/f_c\le0.8,\\[2mm]
3f_t\left(1-\dfrac{p_0}{f_c}\right),&0.8<p_0/f_c\le1.
\end{cases}
\]

and

\[
\varepsilon_{cr}^{TC}=f_{cr}^{TC}/E_0.
\]

The baseline postcrack branch retains the existing Foster source form with

\[
\alpha_1=10,\qquad \alpha_2=0.3.
\]

Writing

\[
d=\frac{1-\alpha_2}{\alpha_1-1}=\frac{0.7}{9},
\]

the current cracked-TC tensile branch is

\[
\sigma_t=(1+d)f_{cr}^{TC}-dE_0\varepsilon_t
\]

until `epsilon_t/epsilon_cr_TC=alpha1`, followed by the current residual

\[
\sigma_t=\alpha_2 f_{cr}^{TC}.
\]

The TC source envelope is therefore a current branch-transition surface, not a terminal Pu surface.

---

## 2. Exact primitive and same-law Jacobian

On the first TC source segment,

\[
f_{cr}^{TC}=f_t+\frac{f_t}{2f_c}\sigma_c,
\]

and on the second,

\[
f_{cr}^{TC}=3f_t+\frac{3f_t}{f_c}\sigma_c.
\]

Therefore every active Foster-type cracked-TC tensile segment can be written as

\[
\boxed{\sigma_t=A+B\sigma_c(\lambda_c)+C\lambda_t},
\]

where `A,B,C` are constants on that finite source/material segment. Since `lambda_c(z)` and `lambda_t(z)` are affine and the unchanged compression backbone has the existing finite Saenz/rational primitive, the thickness resultants remain exact finite primitives:

\[
\int \sigma_t dz
=A\int dz+B\int \sigma_c dz+C\int\lambda_t dz,
\]

\[
\int z\sigma_t dz
=A\int zdz+B\int z\sigma_c dz+C\int z\lambda_t dz.
\]

The cross-coupled same-law Jacobian is also exact. The required compression-tangent moments are obtained from endpoint identities,

\[
\int D_c dz,\qquad \int zD_c dz,\qquad \int z^2D_c dz,
\]

rather than through-thickness finite differences or quadrature.

Moving TC crack fronts and the `p/fc=0.8` source kink are localized by finite scalar root solves in `z`. These are material branch-front events, not spatial integration points.

Independent finite-difference audit of the final analytic Jacobian gave relative matrix discrepancies of approximately

\[
3.3\times10^{-8}\quad\text{(Panel 1)},
\]

and

\[
2.6\times10^{-9}\quad\text{(Panel 21)}.
\]

Panel 14 lies on the existing one-sided reinforcement active-set kink, so a central finite-difference Jacobian is not the appropriate gate there; its one-sided active-set treatment is unchanged from the prior explicit path.

```text
EXACT_SECTION_PRIMITIVE = PASS
SAME_LAW_JACOBIAN = PASS
N_formal_spatial_quadrature = 0
N_formal_material_points = 0
```

---

## 3. NC-M6/F03 three-panel execution

The following values are theoretical events fixed without using `Pf`. Experimental values are inserted only afterward as a diagnostic.

| Panel | controlling `u` | `q_event` | event | NC-M6/F03 event / kN | previous fixed-front event / kN | post-check vs `Pf` |
|---:|---:|---:|---|---:|---:|---:|
| 1 | 0.63206209 | 0.001067733 | current-map section fold | **462.6313** | 589.0817 | **-5.623%** |
| 14 | 0.74898294 | 0.000934941 | lower y-rebar compression-yield active-set terminal | **770.7674** | 770.5483 | **+7.624%** |
| 21 | 0.35584985 | 0.001428230 | current-map section fold | **180.1593** | 192.6906 | **-51.085%** |

### Panel 1

At the new fold,

\[
(a_x,a_y,b_x,b_y)\approx(0.035560,-0.363255,0.009759,0.002694).
\]

Face coordinates are approximately

\[
\lambda_x:-0.08838\to+0.15950,
\]

\[
\lambda_y:-0.39747\to-0.32904.
\]

The section remains `CC -> TC`, and the maximum positive coordinate is only `0.1595`, so the literal Vecchio-Collins gamma remains inactive. The singular Jacobian mode remains overwhelmingly transverse-tension controlled.

The earlier fixed-front overprediction is removed in direction and magnitude without changing the structural path: the event moves from 589.08 kN to 462.63 kN. This is direct evidence that the 2D TC crack-front omission was material to Panel 1.

### Panel 14

The first terminal remains the lower longitudinal reinforcement compression-yield active-set boundary. NC-M6 changes the load by only about `+0.22 kN` relative to the previous 770.55 kN event. Panel 14 therefore remains a steel-active-set-limited discriminator rather than a clean NC TC test.

### Panel 21

At the new fold,

\[
(a_x,a_y,b_x,b_y)\approx(0.072558,-0.168264,-0.021190,-0.011843).
\]

Face coordinates are approximately

\[
\lambda_x:+0.27704\to-0.13193,
\]

\[
\lambda_y:-0.05398\to-0.28255.
\]

The topology remains `TC -> CC`; TT is still not controlling. The maximum positive coordinate is about `0.2770`, again below `10/17`, so gamma is inactive.

However the corrected earlier TC crack front moves the fold still lower, from 192.69 kN to 180.16 kN. Therefore Panel 21 is not repaired by the crack-front correction. Instead NC-M6 strengthens the earlier diagnosis that the transverse postcrack tension-stiffening representation is insufficient for this reinforcement state.

---

## 4. Foster alpha2 source-range sensitivity after the corrected crack front

No `alpha2` value is identified from `Pf`.

For the same exact NC-M6 map:

| `alpha2` | Panel 1 event / kN | Panel 14 first event / kN | Panel 21 same connected stationary-fold branch |
|---:|---:|---:|---|
| 0.3 | 462.631 | 770.767 | 180.159 kN |
| 0.5 | 475.216 | 770.763 | prior connected fold no longer continuously recoverable |
| 0.7 | 494.749 | 770.758 | prior connected fold no longer continuously recoverable |

A continuation of the Panel 21 stationary fold from `alpha2=0.30` remains smooth through approximately `alpha2=0.464`, where the event is about 187.75 kN. The same fold is no longer recovered by approximately `alpha2=0.466`. This is a material-map topology change, not permission to switch to another root merely because it is closer to the experiment.

Hence the coupled crack-front calculation makes the source-closure problem sharper:

\[
\boxed{\text{alpha2 cannot be selected globally or by Pf proximity.}}
\]

The Foster source states reinforcement/bond dependence, but the available source chain still does not provide a deterministic transferable `alpha2(rho,phi,bond)` rule.

---

## 5. BH04 gate under the coupled current crack front

The earlier `BH04-anchor` diagnostic had a fixed uniaxial crack anchor, for which

\[
\sigma_t=f_{cr}(\varepsilon_{cr}/\varepsilon_t)^{0.4}
\]

has an elementary affine-strain primitive.

That exact-primitive statement does **not** transfer automatically to NC-M6. Under the coupled current crack front,

\[
f_{cr}=f_{cr}^{TC}(p_0(z))
\]

varies through the thickness with the compression state, so the direct BH04 composition becomes

\[
\sigma_t(z)=\left[f_{cr}^{TC}(p_0(z))\right]^{1.4}
\left[E_0\varepsilon_t(z)\right]^{-0.4}.
\]

With the Saenz rational compression backbone this is no longer in the present finite rational/affine primitive family. Executing it by numerical thickness quadrature would violate the locked explicit path. Therefore BH04 is **not** rerun as NC-M6 in this execution.

```text
BH04_FIXED_FRONT_DIAGNOSTIC = RETAINED_AS_HISTORY
BH04_COUPLED_TC_EXACT_PRIMITIVE = NOT_YET_DERIVED
BH04_NUMERICAL_THICKNESS_QUADRATURE = PROHIBITED
```

---

## 6. Verdict

NC-M6 passes the requested structural-path constraint:

\[
\boxed{\text{the explicit structural calculation path is unchanged.}}
\]

It also passes the exact section primitive and same-law Jacobian gates for the active F03 execution.

The three-panel outcome separates the remaining mechanisms more clearly:

1. **Panel 1:** the 2D TC crack-front correction is necessary and removes most of the previous overprediction without any structural change.
2. **Panel 14:** the first terminal remains the reinforcement compression-yield active-set boundary; this panel still cannot isolate the concrete TC law.
3. **Panel 21:** the correct earlier TC crack front makes the premature tension-controlled fold worse, confirming that reinforcement-dependent postcrack tension stiffening remains the main unresolved material layer.

No evidence from this execution requires reopening NC CC or TT first, and no reason appears to alter the explicit structural path.

```text
NC_M6_2D_TC_CRACK_FRONT = EXECUTED_DIAGNOSTIC_PASS
EXPLICIT_STRUCTURAL_PATH = LOCKED_UNCHANGED
NC_CC_REOPEN = NO_FIRST_PRIORITY
NC_TT_REOPEN = NO_FIRST_PRIORITY
VC_GAMMA = RETAIN_SOURCE_FORM
PANEL14_STEEL_ACTIVESET = STILL_OPEN
FOSTER_ALPHA2_TRANSFER_RULE = UNRESOLVED
NEXT_RC_TASK = SOURCE_CLOSE_REINFORCEMENT_DEPENDENT_POSTCRACK_TENSION_WITHIN_NC_M6_EXACT_PRIMITIVE
```
