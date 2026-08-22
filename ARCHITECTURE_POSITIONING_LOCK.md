# ARCHITECTURE POSITIONING LOCK

Canonical branch: `archive/ma-origin-recovery-20260823`
Status: `BINDING_GOVERNANCE / NOT_HISTORICAL_PAYLOAD`

## 1. What is unified

The project does **not** claim one unified material theory or one identical formula for reinforced-concrete, steel-shell-concrete, and steel-shell-UHPC panels.

What is unified is only the **mechanics architecture**:

`geometry + elastic/initial section stiffness A,D`
`-> Marguerre / von-Karman + Airy structural solution`
`-> theoretical postbuckling demand P(q), N_x, N_y, N_xy, M_x, M_y, M_xy as applicable`
`-> material-/section-specific capacity or failure constraint`
`-> simultaneous demand-capacity solution for Pu`

Different structural families may use different section composition, material laws, local steel-panel capacity modules, and multiaxial material criteria. Those differences do not break the common architecture.

## 2. Allowed empirical content

Empirical or semi-empirical relations are allowed at the **material property / material strength layer**, for example:

- concrete or UHPC stress-strain law;
- tensile/compressive strength relation;
- multiaxial material failure surface;
- steel constitutive/yield relation;
- experimentally sourced local material-capacity relation where its identity is explicitly material/local-capacity rather than a whole-structure strength reduction.

The presence of such material empirical input does not make the structural postbuckling operator empirical.

## 3. Structural-theory purity target

For the target architecture, the following structural quantities are to be obtained from mechanics rather than specimen-level strength fitting:

- kinematics / initial imperfection representation;
- in-plane equilibrium through the Airy stress function;
- compatibility;
- postbuckling amplitude-load relation;
- structural membrane and bending resultants;
- demand location/candidate equations where analytically derived.

The target architecture does **not** introduce a specimen-level empirical structural-strength reduction such as an effective-width factor, fitted slenderness reduction, FE/test-calibrated postbuckling coefficient, or direct fitted Pu formula unless the user explicitly opens such a comparison branch.

## 4. Difference from Swartz-type empirical simplification

A method is not considered equivalent to the target architecture merely because it predicts postbuckling ultimate strength.

If a Swartz-type or other method introduces empirical simplification at the **structural response / structural strength** level, it belongs to a different methodological class even when its material inputs are also empirical.

Therefore the relevant distinction is:

`TARGET: theoretical structural demand + material-specific empirical/theoretical capacity`

versus

`STRUCTURALLY SEMI-EMPIRICAL: theoretical backbone + empirical structural simplification/reduction + material input`.

This distinction must be preserved in all future literature-overlap and novelty audits.

## 5. No overclaim

Do not describe the project as a "fully unified theory" across RC / steel-shell concrete / steel-shell UHPC.

Preferred wording:

- unified analytical architecture;
- common mechanics architecture with material-specific capacity modules;
- theoretical structural-demand framework with replaceable material/section capacity models.

## 6. Research-overlap consequence

The duplication question is not:

> Has anyone studied postbuckling ultimate strength?

It is:

> Has anyone already derived, for the same or closely related composite-panel class, the structural postbuckling demand from mechanics without a structural empirical strength reduction, while confining empirical input to material/capacity relations and obtaining Pu from direct demand-capacity closure?

Only that level of overlap is potentially methodologically duplicative.
