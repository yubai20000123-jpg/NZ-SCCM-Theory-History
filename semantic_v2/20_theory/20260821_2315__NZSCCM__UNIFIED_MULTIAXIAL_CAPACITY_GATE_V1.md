# NZ-SCCM — Unified Multiaxial Capacity Gate V1

**Time:** 2026-08-21 23:15 +08:00  
**Status:** CURRENT THEORY ADDENDUM / STRUCTURAL BACKBONE FROZEN

## 0. Purpose

This addendum formalizes one common capacity interface for ordinary reinforced concrete (NC/RC), steel-shell concrete (SC), and steel-shell UHPC (SUHPC). It is not a Swartz correction factor and not a UCFT confinement multiplier.

The mandatory interface is

\[
\boxed{
\text{structural resultants}
\rightarrow
\text{phase stress recovery}
\rightarrow
\text{material admissibility}
\rightarrow
\text{section capacity}
}
\]

Material identities may differ by phase. The structural and admissibility logic may not be changed by specimen family.

## 1. Frozen structural layer

The current Marguerre–Airy structural backbone is unchanged:

\[
P_{pb}(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0),
\]

\[
n_y(s;q)=\frac{P_{pb}(q)}b+Gq(q+2q_0)(1-2s^2),
\qquad
m_y(s;q)=Jqs.
\]

The Airy solution also supplies the in-plane transverse/shear resultants required by the material gate. No experimental/FEM load is allowed to modify

\[
D_x,D_y,H,P_{cr},C,G,J,q_0,P_{pb}(q).
\]

```text
STRUCTURAL_BACKBONE_MODIFIED_BY_UMCG = NO
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
RITZ_ORDER = NONE
FORMAL_SPATIAL_QUADRATURE = 0
LOAD_PATH_TRACKING = NOT_REQUIRED
```

## 2. Generalized demand at each finite control candidate

For each algebraic control candidate \((q,s)\), define the structural demand set

\[
\mathbf R^d(q,s)=
\{N_x,N_y,N_{xy},M_x,M_y\}.
\]

For the present one-direction compression implementation, \(N_y,M_y\) are the primary section-capacity demands and \(N_x,N_{xy}\) are mandatory multiaxial admissibility demands. A candidate is not admissible merely because its uniaxial \(N_y-M_y\) interaction is satisfied.

## 3. Phase stress recovery

Let the section contain phases \(r\in\{c,s_f,s_w,r_b,\ldots\}\): concrete/UHPC, external steel faces, longitudinal webs/PBL, reinforcing bars, as present in the actual section.

At a candidate \((q,s)\), recover a compatible finite-dimensional through-thickness strain field

\[
\boldsymbol\varepsilon_r(z)=
\begin{bmatrix}
\varepsilon_x(z)\\
\varepsilon_y(z)\\
\gamma_{xy}(z)
\end{bmatrix},
\]

with common kinematic compatibility wherever phases are bonded. Each phase uses its own source-grounded current material map

\[
\boldsymbol\sigma_r(z)=\mathcal M_r\!\left[\boldsymbol\varepsilon_r(z)\right].
\]

The recovered phase stresses must satisfy section equilibrium:

\[
\sum_r\int_{A_r}\sigma_{x,r}\,dA=N_x^d,
\]

\[
\sum_r\int_{A_r}\sigma_{y,r}\,dA=N_y^d,
\]

\[
\sum_r\int_{A_r}\tau_{xy,r}\,dA=N_{xy}^d,
\]

\[
\sum_r\int_{A_r}z\sigma_{y,r}\,dA=M_y^d,
\]

and, when active in the structural branch,

\[
\sum_r\int_{A_r}z\sigma_{x,r}\,dA=M_x^d.
\]

This phase recovery is the mechanism by which a steel shell may generate confinement: shell/web compatibility creates transverse stress; the material operator then decides whether that stress strengthens or weakens the concrete/UHPC. No independent empirical confinement factor is permitted.

## 4. Material admissibility

For every material phase and every analytic through-thickness branch,

\[
\boxed{F_r(\boldsymbol\sigma_r;\boldsymbol\theta_r)\le0.}
\]

If a baseline uniaxial section solution violates any phase admissibility condition, that solution is PRE-GATE only. The capacity state must be re-solved with the active admissibility equality/equalities included; multiplying the previous capacity by a correction coefficient is prohibited.

### 4.1 Ordinary concrete / RC

NC uses the Nguyen/Foster/Kupfer-derived ordinary-concrete material identity already registered in the project:

- CC: biaxial compression enhancement;
- TC/CT: tension-compression weakening;
- TT: tensile admissibility;
- reinforcement is a separate steel phase;
- both reinforcement directions displace concrete volume, but only the loading-direction reinforcement directly contributes to loading-direction axial force.

The low-parameter current targets remain material-level targets, not Swartz backfits. Specimen-specific \(f_t\) must not be inferred from \(P_f\).

### 4.2 UHPC

UHPC uses the same gate architecture but not the NC numerical law.

- UHPC CC uses the UHPC-specific biaxial compression source/target;
- UHPC tensile response uses the UHPC fibre-bridged tensile backbone;
- UHPC TC must use the UHPC-specific Liu-source softening law/regularization when source-closed;
- the NC rule \(c^*=c(1-\tau)\) is not transferred as a UHPC production law.

Current source status requires a distinction between architecture closure and sector closure: the UHPC TC compression sub-branch is source-supported, while a general arbitrary-path full TC vector law remains incomplete.

### 4.3 Steel faces, webs and rebars

Steel faces use their source constitutive law together with plane-stress von-Mises/yield admissibility. Longitudinal web/PBL and reinforcement phases use their source axial/yield laws; if a phase is assigned a two-dimensional stress state, the same steel yield surface must be respected.

A uniaxial fully plastic face pattern cannot simultaneously be assumed to carry arbitrary transverse membrane force. Transverse demand must be recovered consistently; if this requires reduction of axial plastic stress, the section axial capacity is correspondingly reduced.

## 5. Current dimensionality

The current explicit plate theory is a plane-stress theory. Therefore V1 formally uses

\[
(\sigma_x,\sigma_y,\tau_{xy}),\qquad \sigma_z=0.
\]

UHPC triaxial sources remain qualification/reference evidence. They are not activated as a hard three-dimensional cap until a source-consistent structural recovery of \(\sigma_z\) exists.

```text
UMCG_DIMENSION = PLANE_STRESS_2D
SIGMA_Z_RECOVERY = NOT_ACTIVATED
TRIAXIAL_SURFACE_AS_2D_HARD_CAP = PROHIBITED
```

## 6. Algebraic ultimate rule

For every finite structural candidate generated by the explicit theory:

1. compute \(\mathbf R^d(q,s)\);
2. solve phase-compatible section equilibrium;
3. evaluate every active material admissibility condition;
4. reject inadmissible candidate states;
5. if a material boundary becomes active first, solve the finite augmented algebraic system including \(F_r=0\);
6. among all admissible candidate families, choose the smallest positive \(q\).

Experimental/FEM values are opened only after the theoretical root is fixed.

## 7. Validation philosophy

The target is not exact fitting of each Swartz specimen or each Abaqus model. The gate passes conceptually if one material/constraint architecture:

- reduces systematic over-capacity where TC or steel multiaxial interaction requires it;
- permits source-grounded CC enhancement where confinement is actually recovered;
- leaves nearly uniaxial cases nearly unchanged;
- transfers without structure-specific multipliers from RC to SC and SUHPC;
- leaves residual specimen/material scatter visible rather than absorbing it into calibration.

```text
SWARTZ_SPECIFIC_K = PROHIBITED
SC_SPECIFIC_CAPACITY_FACTOR = PROHIBITED
SUHPC_CONFINEMENT_MULTIPLIER = PROHIBITED
STRUCTURAL_PU_BACKFIT_TO_MATERIAL = PROHIBITED
RESIDUAL_EXPLAINABLE_ERROR = ACCEPTABLE
```

## 8. Current closure matrix

| Object | Gate architecture | Material sector | Current status |
|---|---|---|---|
| Swartz RC | same UMCG | NC CC/TC/TT + rebar | architecture PASS; specimen ft remains open for exact TC Pu |
| Steel-shell concrete Z family | same UMCG | NC + steel faces/web | architecture PASS; phase-recovery active-gate solution to be executed casewise |
| T120/T360 | same UMCG | UHPC + Q355 faces/web | 2D precheck exists; material/FEM contract mismatches remain |
| BH005–BH050 | same UMCG | UHPC + Q355 faces/web | geometry contract must be re-frozen before quantitative gate validation |

## 9. Governing principle

\[
\boxed{
\text{Prefer a transferable NC--SC--SUHPC constraint law with explainable residual error}
\;>\;
\text{dataset-specific perfect fit}
}
\]

This principle supersedes any temptation to introduce a Swartz-only correction, an SC-only scale factor, or an SUHPC-only empirical confinement multiplier.