# NZ-SCCM — ENERGY-POTENTIAL-FIRST MATERIAL AND STRUCTURAL TARGET RULE

Date: 2026-08-10

## 1. User clarification

Material constitutive simplification may be performed at the energy/potential level. The project is not required to fit sharp local stress peaks pointwise. The final non-negotiable requirement remains:

- limit capacity from an explicit finite formula;
- all derivatives used in equilibrium/stability must come from the same explicit representation.

## 2. Material level

Prefer a scalar current work-potential / pseudo-potential

\[\Psi(\varepsilon_1,\varepsilon_2)\]

and define

\[\sigma_i=\partial \Psi/\partial\varepsilon_i.\]

Then the consistent tangent is

\[D_{ij}=\partial^2\Psi/(\partial\varepsilon_i\partial\varepsilon_j).\]

This automatically enforces the cross-derivative symmetry required by a potential representation.

For dissipative concrete softening/cracking this object is a monotonic current work-potential / phenomenological pseudo-potential, not necessarily recoverable thermodynamic stored energy. This is consistent with the current memoryless monotonic-loading scope, but it must not be mislabelled as general unloading/reloading energy.

## 3. Structural level

Do NOT fit P(D,q) and Rq(D,q) independently if a global target is used.

Prefer one explicit structural internal-work potential

\[\mathcal W(D,q).\]

Let the axial generalized shortening be

\[\Delta=c_D D\]

with known constant c_D (for the current normalization, c_D is proportional to eps0*ell; sign follows the adopted compression convention).

Then

\[P(D,q)=\frac{1}{c_D}\mathcal W_{,D},\]

\[R_q(D,q)=\mathcal W_{,q}.\]

Therefore

\[P_{,D}=\frac1{c_D}\mathcal W_{,DD},\quad P_{,q}=\frac1{c_D}\mathcal W_{,Dq},\]

\[R_{q,D}=\mathcal W_{,Dq},\quad R_{q,q}=\mathcal W_{,qq}.\]

The existing limit determinant becomes

\[L=P_{,D}R_{q,q}-P_{,q}R_{q,D}
=\frac1{c_D}\left(\mathcal W_{,DD}\mathcal W_{,qq}-\mathcal W_{,Dq}^2\right).\]

Hence the stationary limit condition is the Hessian degeneracy of ONE scalar structural potential, rather than a consistency condition between two separately fitted surfaces.

## 4. Fitting / identification rule for a global structural potential

If a global explicit target is used, fitting only potential values is NOT sufficient because derivative error can be amplified.

Use derivative-aware/Sobolev-Hermite identification of one scalar potential. A candidate may be

\[\widehat{\mathcal W}(D,q)=\sum_{i=0}^{m}\sum_{j=0}^{n}c_{ij}T_i(\xi_D)T_j(\xi_q).\]

Determine the same coefficient set by a weighted objective containing, when available:

- W values;
- c_D P = W_D;
- Rq = W_q;
- optionally selected tangent/Hessian entries.

The production quantities are then exact analytic derivatives of the same coefficient array.

## 5. Production hierarchy

Preferred order:

1. fit/construct material potential Psi;
2. derive stress and tangent from Psi;
3. substitute Nguyen second-order kinematics;
4. construct one structural potential W(D,q) by analytic contraction when feasible;
5. if using a global explicit target, fit only W, never P and Rq independently;
6. obtain P, Rq, all tangent derivatives and L by differentiation of W;
7. solve only the resulting finite explicit equations numerically.

## 6. Zero-quadrature boundary

The potential formulation does not by itself decide how W coefficients are generated.

- D15 / named-kernel analytic generation preserves the older formal zero-spatial-quadrature doctrine.
- Offline spatial coefficient identification may be used as a proof-of-concept only unless explicitly accepted as production data processing.

## 7. NC -> UHPC portability

The shared architecture is the potential construction and differentiation rule, not NC numerical parameters.

NC and UHPC may have different material-native domains and different potential parameters. Each material must derive its own Psi from its source evidence / declared conservative simplification.

## 8. Current decision

ENERGY_POTENTIAL_FIRST_MATERIAL = PROMOTED
FIT_P_AND_RQ_INDEPENDENTLY = DISCOURAGED / NOT PREFERRED
ONE_STRUCTURAL_POTENTIAL_TARGET = PROMOTED_FOR_NEXT PRECHECK
POTENTIAL_ONLY_VALUE_FIT_WITHOUT_DERIVATIVE_CONSTRAINTS = REJECT

Next recommended task:

ENERGY_POTENTIAL_STRUCTURAL_TARGET_PRECHECK_R09C

Goal: use the current NC compression branch + energy-equivalent simplified tension + analytic reinforcement to test whether one explicit W(D,q) can reproduce P, Rq and the limit root with derivative consistency better and more compactly than the current separate Pc/Rc target surfaces.
