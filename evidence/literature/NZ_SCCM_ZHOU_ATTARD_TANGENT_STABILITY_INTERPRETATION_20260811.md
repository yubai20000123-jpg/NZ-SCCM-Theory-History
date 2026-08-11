# Zhou–Attard tangent-stability interpretation for NZ-SCCM P1

**Date:** 2026-08-11  
**Identity:** SOURCE-BASED INTERPRETATION / DIAGNOSTIC ONLY  
**Material change:** NONE

## 1. Attard source role

Attard, *Buckling of Reinforced Concrete Walls* (UNICIV Report, 1994), formulates the out-of-plane perturbation of a simply supported reinforced-concrete wall as an orthotropic tangent-plate problem. In source notation the governing form is

\[
D_{xt}w_{,xxxx}+2D_{xyt}w_{,xxyy}+D_{yt}w_{,yyyy}=-N_xw_{,xx}.
\]

The directional bending tangent rigidities depend on directional tangent moduli. Attard takes the loaded direction as the current concrete tangent modulus and, for the unloaded transverse direction, introduces the approximate bending/cracking value

\[
E_{xt}=E_t,\qquad E_{yt}\approx0.4E_c.
\]

For the Navier shape

\[
w=C_1\sin\frac{m\pi x}{a}\sin\frac{\pi y}{b},
\]

the orthotropic buckling coefficient depends on the ratio \(E_{yt}/E_{xt}\); minimizing with respect to the longitudinal half-wave number gives the well-known fourth-root half-wave dependence and a minimum coefficient proportional to \(4\sqrt{E_{yt}/E_{xt}}\).

### NZ-SCCM use boundary

Attard is used only as an **independent tangent-stability diagnostic**. The assumption \(E_{yt}=0.4E_c\) is NOT imported into R10, N48, or the current multidimensional material map.

At a finite-amplitude NZ-SCCM ultimate state, the Attard formula is not treated as a second solver. It is used to ask whether the local current tangent still resembles the positive-tangent orthotropic regime for which the perturbation formula was developed.

---

## 2. Zhou Siming source role

Zhou Siming, *Stability performance of multi-celled concrete-filled steel tubular walls under complex boundary conditions* (Zhejiang University doctoral dissertation, 2022), derives three-edge and four-edge simply-supported orthotropic plate/shell stability theories by an energy method.

The source explicitly separates and defines directional and torsional stiffness constants, including

- primary-direction bending stiffness \(D_y\);
- secondary-direction bending stiffness \(D_x\);
- free torsional stiffness \(D_{xy}\);
- Poisson-related additional torsional stiffness \(D_\mu\);
- combined torsional/Poisson stiffness \(H\), with the source relation

\[
H=D_{xy}+D_\mu.
\]

For four-edge simply-supported walls, Zhou's conclusions emphasize that axial stability is jointly contributed by

\[
D_y,\qquad D_x,\qquad H,
\]

rather than by one loaded-direction elastic modulus alone. The dissertation also shows that the boundary between strength control and stability control shifts strongly when moving from elastic to elastoplastic response: for the investigated composite-wall system the critical width/thickness scale changes substantially between elastic and elastoplastic states.

### NZ-SCCM use boundary

The present P1 audit does NOT import Zhou's composite-wall section formulas into the Swartz RC wall material model. Instead, Zhou's decomposition is used as a **theoretical language for auditing the current tangent**.

For the current RC tangent matrix, define the diagnostic mapping

\[
D_x^{eq}=C_{xx,t}\frac{t^3}{12},\qquad
D_y^{eq}=C_{yy,t}\frac{t^3}{12},
\]

\[
D_\mu^{eq}=\frac{C_{xy,t}+C_{yx,t}}{2}\frac{t^3}{12},\qquad
D_{66}^{eq}=G_t\frac{t^3}{12},
\]

\[
H^{eq}=D_\mu^{eq}+2D_{66}^{eq}.
\]

For one square representative half-wave,

\[
N_{cr,Z}^{proxy}
=
\frac{
D_x^{eq}\alpha^4+2H^{eq}\alpha^2\beta^2+D_y^{eq}\beta^4
}{\beta^2}.
\]

This is a **Zhou-form equivalent audit mapping**, not a new production equation and not a claim that Zhou used these RC current-tangent definitions.

---

## 3. Why Zhou's framing matters to the P1 result

The P1 audit shows that the exact R10 material-target tangent and the current N48 derivative produce very different stiffness decompositions at the theoretical ultimate states.

Using the R10 target tangent, the three Swartz groups have approximately the following average contribution structure in the square-halfwave Zhou-form proxy:

```text
R10 target:
Dx      ~ 47–50%
2H      ~ 46–51%
Dy      ~ -2% to +3%
steel   = small
```

This is physically interpretable near the compression peak: the loaded-direction tangent \(D_y\) can collapse or become slightly negative while transverse bending and torsional/Poisson coupling still contribute materially to stability.

Using the current N48 derivative, the structure changes to approximately

```text
N48 tangent:
Dx      ~ 12–13%
2H      ~ 75%
Dy      ~ 11%
steel   = small
```

Across the 24 panels, the N48-based equivalent \(H\) is about 4.72–6.79 times the R10-target value, with an average factor about 6.21. The corresponding center-state Zhou-form stability margin is inflated by about 3.28–4.42 times, average about 3.97.

Therefore Zhou's key theoretical point — **stability is a stiffness-combination problem, not a single-modulus problem** — makes the N48 issue clearer: the discrepancy is not merely an error in one loaded-direction tangent modulus. The compiler derivative changes the entire \(D_x-D_y-H\) balance, with especially strong inflation of the mixed/torsional contribution.

---

## 4. Current source-based decision

```text
ATTARD = INDEPENDENT_ORTHOTROPIC_TANGENT_DIAGNOSTIC
ZHOU = DIRECTIONAL_STIFFNESS_AND_NAVIER_STABILITY_AUDIT_LANGUAGE
ATTARD_0p4Ec_IMPORTED_INTO_R10 = NO
ZHOU_COMPOSITE_WALL_SECTION_FORMULAS_IMPORTED_INTO_RC_MATERIAL = NO
R10_MATERIAL_CHANGED = NO
N48_TANGENT_FIDELITY = FAIL_DIAGNOSTIC
```

The source review therefore supports the following order of diagnosis:

```text
R10 target tangent
-> N48 derivative fidelity
-> directional stiffness decomposition (Dx, Dy, H)
-> full-field generalized tangent
-> only after those pass, diagnose missing post-buckling structural freedom or material physics.
```

This ordering prevents a compiler-derivative defect from being misidentified as a new concrete material mechanism.
