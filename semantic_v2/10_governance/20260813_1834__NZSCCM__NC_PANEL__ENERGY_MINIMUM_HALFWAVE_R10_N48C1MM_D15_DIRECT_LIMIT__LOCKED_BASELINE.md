# NZ-SCCM NC panel — energy-minimum halfwave / R10-N48-C1MM / general-D15 / direct-limit locked baseline

**Timestamp:** 2026-08-13 18:34 +08:00  
**Status:** CURRENT_PRIMARY / LOCKED GOVERNANCE  
**Supersedes where conflicting:** 2026-08-13 diagnostic interpretations that changed formal halfwave length from observed buckling shape, proposed extra in-plane Ritz coordinates as a missing membrane mechanism, or treated post-buckling membrane action as absent from Nguyen second-order kinematics.

---

## 0. Governing correction

The present successful theory is to be preserved as a predictive theory. Experimental mode-shape irregularity is **validation evidence**, not an input that is allowed to redefine the formal halfwave.

The formal structural model remains one theoretically governing complete halfwave. Its geometry is selected from the admissible theoretical halfwave family by the classical energy/minimum-capacity principle under the specimen's **design geometry and boundary conditions**, before reading experimental failure data.

```text
FORMAL_DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
ACTIVE_HALFWAVE_MODE = FUNDAMENTAL / ENERGY-MINIMUM ADMISSIBLE HALFWAVE
EXPERIMENTAL_BUCKLING_SHAPE_AS_HALFWAVE_INPUT = PROHIBITED
LONGER_OR_NONCANONICAL_EXPERIMENTAL_BULGE = INTERFERENCE / IMPERFECTION EVIDENCE, NOT THEORY REDEFINITION
```

For a classical rectangular plate the halfwave parameter is determined by minimization of the plate energy/Rayleigh quotient. For the Swartz geometry, the formal representative halfwave is therefore the minimum-energy halfwave, not the later experimentally observed long or asymmetric bulge.

If a design feature such as a stiffener/PBL/boundary restraint changes the admissible energy functional, it may change the theoretical halfwave length through that **design-side energy minimization**. Zhang et al. explicitly show this type of dependence: the local-buckling coefficient is minimized with respect to the halfwave parameter, and PBL stiffness can shift the minimizing halfwave. This is a design-parameter effect, not an experiment-driven mode fit.

---

## 1. Nguyen second-order membrane terms are already part of the theory

The current kinematics remain

\[
w_0=A_0\sin X\sin Y,\qquad w_1=A\sin X\sin Y,
\]

\[
\chi_q=q_0q+\frac12q^2.
\]

The membrane terms

\[
C_{mx}=\frac{\pi^2}{\varepsilon_0}\chi_q,
\quad
C_{my}=\frac{\pi^2b^2}{\varepsilon_0\ell^2}\chi_q,
\quad
C_{mxy}=\frac{2\pi^2b}{\varepsilon_0\ell}\chi_q
\]

are retained explicitly in the continuous strain field. Therefore the previous diagnostic statement that a missing generic "membrane stress / membrane redistribution" mechanism should be repaired by adding independent in-plane Ritz coordinates is not accepted as a production-theory deficiency.

```text
NGUYEN_SECOND_ORDER = LOCKED
SECOND_ORDER_MEMBRANE_STRAIN = PRESENT
ADD_u_v_RITZ_TO_REPAIR_MEMBRANE = REJECTED AS CURRENT NEXT STEP
HIGHER_ORDER_KINEMATICS = NOT CURRENT PRIORITY
```

The current two generalized structural variables remain `D` and `q=A/b`.

---

## 2. Concrete material target remains the energy-fitted R10 current operator

No reopening of the accepted ordinary-concrete physical target is authorized.

```text
R10_MATERIAL_TARGET = FROZEN
MATERIAL_PHYSICS_REFIT = NO
STRUCTURAL_Pu_BACKFIT = NO
CASEWISE_MATERIAL_CORRECTION = NO
```

The source physical material target remains the accepted energy-consistent R10 ordinary-concrete operator.

---

## 3. Finite analytic compiler remains current N48-C1/MM

The production compiler remains

```text
N48_ORDER = 48
U  = N48-C1
C  = N48-C1
T7 = N48-C1
T  = N48-C1-CONSTRAINED-MINIMAX
```

The 2026-08-13 BMM value+tangent formulation remains an audit candidate only and is **not** promoted by this lock.

The current T target remains the constrained minimax objective on the specimen's declared material interval:

\[
E_T^*=\min_{a\in\mathcal F_T}\|p_a-T_{R10}\|_{L^\infty([\lambda_a,\lambda_b])},
\]

followed by the existing minimum-distance tie-break within the minimax solution set.

### 3.1 Specimen-dependent compiler boundaries

The interval

\[
\boxed{\lambda\in[\lambda_a,\lambda_b]}
\]

is not a universal constant. Its boundaries may vary with specimen/design/material parameters because the reachable material domain changes with geometry, material properties, imperfection amplitude and theoretical halfwave geometry.

But the interval must be declared/derived **without experimental ultimate load or experimental mode fitting** and must then be verified by a continuous spectrum certificate.

```text
COMPILER_OBJECTIVE = LOCKED CURRENT C1/MM
COMPILER_INTERVAL = SPECIMEN/DESIGN DEPENDENT
EXPERIMENT_IN_INTERVAL_SELECTION = NO
CONTINUOUS_REACHABLE_SPECTRUM_CERTIFICATE = REQUIRED
```

---

## 4. Multiaxial current tangent and multi-order analytic representation remain mandatory

The current two-dimensional material response continues to be lifted through Cayley-Hamilton and differentiated consistently:

\[
\sigma=M(E),\qquad \mathbb C_t=\frac{\partial\sigma}{\partial E}.
\]

No scalar tangent-modulus substitution is allowed to replace the existing full current-map in the concrete part.

```text
CAYLEY_HAMILTON_2D_LIFT = LOCKED
FULL_DIRECTIONAL_CURRENT_TANGENT = LOCKED
MULTI_ORDER_ANALYTIC_COEFFICIENTS = LOCKED
```

---

## 5. Exact multiple integrals remain the formal structural operator

All stress, residual, derivative and tangent-stability integrands remain finite analytic trigonometric-thickness expansions and are integrated by general-D15 exact moments:

\[
Q(X,Y,\zeta)=\sum c_{prush}\sin^pX\cos^rX\sin^uY\cos^sY\zeta^h,
\]

\[
\mathscr D[Q]=\sum c_{prush}J_{pr}J_{us}Z_h.
\]

```text
EXACT_MOMENT_ENGINE = D15_GENERAL_TRIG_MOMENTS
MULTIPLE_INTEGRALS = RETAINED
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_SPATIAL_SUBDOMAINS = 1
GAUSS_SIMPSON_ADAPTIVE_CELLS = PROHIBITED IN PRODUCTION
```

---

## 6. Extreme capacity remains a direct coupled-equation problem

For the current RC version,

\[
P=P_c+P_s,
\qquad
R_q=R_{q,c}+R_{q,s},
\]

with same-expression derivatives

\[
P_D,P_q,R_{q,D},R_{q,q},
\]

and

\[
L=P_DR_{q,q}-P_qR_{q,D}.
\]

The production limit is still the first admissible load maximum on the equilibrium branch connected to `(0,0)`:

\[
\boxed{R_q=0,\qquad L=0,\qquad g:+\to-}.
\]

The solution remains direct simultaneous nonlinear algebraic solution, not load stepping, material-point history integration or an empirical Pu formula.

```text
DIRECT_COUPLED_LIMIT_SOLVE = LOCKED
LOAD_STEP_HISTORY = NO
SECOND_Pu_SOLVER = NO
EXPERIMENT_DRIVEN_ROOT_SELECTION = NO
```

---

## 7. Zhou/Navier current-tangent stability remains an acceptance/control layer

The anisotropic/full-direction tangent stability operator remains

\[
K_Z=K_Z^{mat}+K_Z^{geo}
\]

with concrete and steel contributions assembled from their current stress and consistent tangent fields.

This is retained as a same-branch stability/control-ordering check. It is not a replacement for the direct `R_q=0, L=0` extreme-capacity solver.

---

## 8. Formal halfwave selection rule for future NC+steel-shell work

The theory must distinguish:

1. **full physical member/panel length**;
2. **formal representative complete halfwave length** `ell`;
3. **experimental observed bulge length/location**.

Only item 2 enters the production structural operator, and it is determined from the theoretical minimum under design-side data.

For an admissible halfwave family parameterized by `beta=ell/b`, the governing formal halfwave is

\[
\boxed{\beta_* = \arg\min_{\beta\in\mathcal B(\text{design,boundary})} \mathcal J(\beta)}
\]

where `J` is the appropriate theoretical energy/critical-capacity functional of the locked model. For an interior minimum, the associated stationarity and positive-curvature conditions apply.

For a nonlinear ultimate calculation, the selected theoretical halfwave is then used unchanged in the direct `D-q` coupled limit equations. An experimental longer/asymmetric/localized mode does not overwrite `beta_*`; it is interpreted as evidence of geometric imperfection, eccentricity, thickness variation, support imperfection or other real-test interference.

This restores the classical minimum-halfwave interpretation and removes the 2026-08-13 diagnostic mistake that treated the observed/FE long wave of Cases 1-16 as the formal production halfwave input.

---

## 9. Locked production identity before steel-shell extension

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
HALFWAVE_SELECTION = THEORETICAL ENERGY/MINIMUM PRINCIPLE FROM DESIGN DATA
OBSERVED_TEST_MODE_AS_INPUT = NO
GENERALIZED_COORDINATES = D,q
KINEMATICS = NGUYEN_SECOND_ORDER
SECOND_ORDER_MEMBRANE_TERMS = INCLUDED
R10 = FROZEN ENERGY-FITTED MATERIAL TARGET
COMPILER = N48-C1/MM
COMPILER_INTERVAL = SPECIMEN-DEPENDENT / EXPERIMENT-INDEPENDENT
CAYLEY_HAMILTON = YES
FULL_DIRECTIONAL_TANGENT = YES
EXACT_MOMENTS = GENERAL-D15
MULTIPLE_INTEGRALS = YES
DIRECT_LIMIT_EQUATIONS = Rq=0 + L=0 + FIRST +->- MAXIMUM
CURRENT_TANGENT_STABILITY = ZHOU/NAVIER SAME-BRANCH CHECK
FORMAL_SPATIAL_QUADRATURE = 0
STRUCTURAL_CALIBRATION = NO
```

This locked identity is the parent theory for the next `CONCRETE + STEEL SHELL` extension. The extension is allowed to replace the reinforcement contribution only; it is not allowed to reopen the concrete/kinematic/compiler/half-wave/limit-solver identities above.