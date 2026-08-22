# NZ-SCCM — NC post-crack TC memoryless reduction R1 + alternative constitutive-model audit

**Date:** 2026-08-22 13:38 +08:00  
**Status:** `TC_R1_MATERIAL_LEVEL_PASS_CANDIDATE / LITERAL_NGUYEN_G6_FAIL / GENERAL_S_FORMAL_CERTIFICATE_OPEN / ALTERNATIVES_SCREENED`

## 0. Boundary

This step does not alter the Marguerre–Airy structural backbone and does not use Zhou/Winter/experiment/FEM values to select material parameters or roots.

```text
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_material_points = 0
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
EXPERIMENT_IN_ROOT_SELECTION = 0
FEM_IN_ROOT_SELECTION = 0
STRUCTURAL_BACKBONE_CHANGED = FALSE
```

The purpose is narrowly:

1. test whether Nguyen Ch.3 post-crack tension–compression (TC) can be reduced to a monotonic current-state operator;
2. fail fast if the literal source requires history;
3. if literal Nguyen fails G6, identify whether a cleaner literature constitutive law is a better replacement.

---

# 1. Literal Nguyen post-crack TC: source audit

Nguyen Section 3.4.2 states that when the TC biaxial envelope is breached the element changes state and cracks. The cracked TC branch then combines:

- modified-compression-field compression softening, Eq. (3.43);
- a compression stress–strain relation with a softened compressive peak;
- Foster-type tension stiffening, Eqs. (3.48)–(3.53);
- shear retention, Eqs. (3.56)–(3.57);
- a later TC -> TCX crushing transition, Eqs. (3.77)–(3.80).

The source-oriented Appendix-B implementation confirms that the literal algorithm stores at least:

```text
eps_cr1, f_cr1,
g_precrack / gt_precrack,
peak_stress2, peak_strain2,
eps1_at_crushing,
regime TC / TCX.
```

In particular, the TC routine subsequently reuses stored crack-event and softened-peak quantities. Therefore the literal Nguyen model is not a memoryless map

\[
\sigma=\mathcal M(\varepsilon)
\]

and cannot be inserted unchanged into the present zero-material-point mainline.

```text
LITERAL_NGUYEN_POSTCRACK_TC_SOURCE_FIDELITY = PASS_AS_ORACLE
LITERAL_NGUYEN_POSTCRACK_TC_G6 = FAIL
LITERAL_NGUYEN_HISTORY_STATE_MACHINE = OFF_MAINLINE
```

This is a model-architecture conflict, not a numerical failure.

---

# 2. Source-constrained memoryless reduction TC-R1

TC-R1 is explicitly a **project reduction** of the Nguyen/Vecchio–Collins post-crack physics, not a claim that Nguyen originally proposed a history-free law.

Use current NC material coordinates

\[
\lambda_t\ge0,\qquad \lambda_c<0,
\]

with the existing fixed plane-stress coordinate map and current NC scale \(\varepsilon_0\).

## 2.1 Poisson-free transverse tensile measure

Raw physical transverse strain cannot be inserted directly into Eq. (3.43), because pure uniaxial compression would then generate a false softening effect from ordinary Poisson expansion.

Define instead

\[
\boxed{
\widehat\varepsilon_t
=\frac{\varepsilon_t+\nu\varepsilon_c}{1-\nu^2}
=\varepsilon_0\lambda_t.
}
\]

Thus pure uniaxial compression has \(\lambda_t=0\), irrespective of the physical Poisson strain.

The current compression-softening factor is

\[
\boxed{
\gamma_c(\lambda_t)
=\min\left[1,\frac{1}{0.8+0.34\lambda_t}\right].
}
\]

Softening activates only for

\[
\lambda_t>\frac{0.2}{0.34}=\frac{10}{17}\approx0.5882352941.
\]

Therefore

\[
\lambda_t=0\Rightarrow\gamma_c=1,
\]

so uniaxial compression degeneration is preserved.

## 2.2 Tensile direction

Retain the already qualified bounded T5/Foster project reduction:

\[
\boxed{
\sigma_t=f_tT_5\!\left(\frac{\lambda_t}{x_{cr}}\right),
\qquad x_{cr}=\frac{f_t/f_c}{\kappa},
\qquad \kappa=\frac{E_0\varepsilon_0}{f_c}.
}
\]

No crack-event \(f_{cr}\) or \(\varepsilon_{cr}\) is stored.

## 2.3 Current softened compression peak

\[
\boxed{\sigma_{cp}=-\gamma_cf_c.}
\]

Let \(r=\gamma_c\). The Nguyen peak-strain relation is retained as a current function:

\[
\varepsilon_{cp}
=-\varepsilon_0
\begin{cases}
3r-2, & r\ge1,\\
0.35r+2.25r^2-1.6r^3, & 0<r<1,
\end{cases}
\]

with the source elastic-limit correction

\[
\varepsilon_{cp}\leftarrow\min_{|\cdot|}\left(\varepsilon_{cp},\frac{2\sigma_{cp}}{E_0}\right)
\]

implemented with the original compression sign convention.

The current compression equivalent strain is

\[
\varepsilon_c^u=\varepsilon_0\lambda_c.
\]

## 2.4 Ascending compression

Retain Saenz with the current softened peak:

\[
\boxed{
\sigma_c
=\frac{E_0\varepsilon_c^u}
{1+(E_0/E_{sp}-2)\xi+\xi^2},
}
\]

where

\[
E_{sp}=\frac{\sigma_{cp}}{\varepsilon_{cp}},
\qquad
\xi=\frac{\varepsilon_c^u}{\varepsilon_{cp}}.
\]

## 2.5 TCX / postpeak bounded continuation

After the current softened peak, retain the source-style bilinear post-crushing continuation to \(0.1\sigma_{cp}\) at \(\gamma_2=10\):

\[
\sigma_c
=\sigma_{cp}
-0.9\sigma_{cp}
\frac{\varepsilon_c^u-\varepsilon_{cp}}
{\varepsilon_{cp}(\gamma_2-1)},
\qquad
|\varepsilon_c^u|<\gamma_2|\varepsilon_{cp}|,
\]

and

\[
\sigma_c=0.1\sigma_{cp}
\]

thereafter.

No independent `TCX` history flag is required; the branch is selected directly from the current \((\lambda_t,\lambda_c)\).

---

# 3. Transition continuity

The previously solved Z0–Z6 first Nguyen TC-transition coordinates are:

|Case|lambda_t at transition|
|---|---:|
|Z0|0.0310131|
|Z1|0.0345810|
|Z2|0.0310131|
|Z3|0.0317598|
|Z4|0.0259798|
|Z5|0.0226245|
|Z6|0.0400238|

All satisfy

\[
\lambda_t\ll10/17.
\]

Hence

\[
\gamma_c=1
\]

exactly in a finite neighbourhood of each first TC transition. TC-R1 therefore reduces there to the already current T5 + unsoftened Saenz axis laws.

```text
TC_R1_AT_NGUYEN_TC_TRANSITION_STRESS_C0 = PASS
TC_R1_AT_NGUYEN_TC_TRANSITION_LOCAL_TANGENT_COMPATIBILITY = PASS
NO_STORED_CRACK_EVENT_REQUIRED = TRUE
```

The original Nguyen envelope remains useful as a source-identified cracking/state-transition marker, but TC-R1 provides the monotonic current continuation after that marker.

---

# 4. Material-level seven-gate audit

|Gate|TC-R1 status|Reason|
|---|---|---|
|G1 uniaxial compression|PASS|Poisson-free measure gives lambda_t=0 -> gamma_c=1|
|G2 uniaxial tension|PASS_WITH_EXISTING_T5_PROJECT_REDUCTION|same T5 as current NC|
|G3 TC support|PASS_CANDIDATE|Nguyen Eq3.43 + tension-stiffening lineage; project removes history variables|
|G4 plane stress / Poisson|PASS|softening uses excess/material-coordinate tension, not raw Poisson expansion|
|G5 stress/tangent|PASS_ANALYTIC_WITHIN_BRANCHES|all branches are direct differentiable functions; finite kinks retained|
|G6 finite direct|PASS_AT_MATERIAL_POINTLESS_OPERATOR_LEVEL|no history state or local Newton needed|
|G7 no Pu fit|PASS|all coefficients are source/current material coefficients|

Full-domain stress boundedness follows from bounded T5, \(0<\gamma_c\le1\), bounded Saenz branch and the 0.1 postcrush floor.

```text
NC_TC_R1_MATERIAL_7GATE = PASS_CANDIDATE
NC_TC_R1_PRODUCTION_FREEZE = NOT_YET
```

The remaining blocker is not the local material map; it is the **general-s section reduction** under nonzero bending.

---

# 5. Why the general-s certificate is still open

At \(s=0\), \(m=Jqs=0\) and the phase strains are uniform through thickness, so TC-R1 remains a small finite algebraic system.

For \(s>0\), the axial strain is linear through thickness. Then:

- T5 is a rational function of a linear tensile coordinate;
- \(\gamma_c\) is a rational function after activation;
- the softened peak strain is polynomial in \(\gamma_c\);
- Saenz therefore becomes a higher rational composition;
- steel radial-cap stress contains linear-over-square-root-quadratic primitives;
- web clipping introduces finite yield fronts.

These objects are analytically integrable in principle after finite branch-front decomposition, but the resulting primitive family is substantially larger than the present low-order section formulas.

A diagnostic numerical-through-thickness scan is permitted only as an off-mainline audit; it is not a formal operator. That diagnostic indicates that the controlling Z6 location may shift slightly away from exactly \(s=0\). Consequently the exact endpoint result must not be promoted as final Z6 Pu before a finite general-s proof.

```text
TC_R1_GENERAL_S_ANALYTIC_PRIMITIVE_EXISTS_IN_PRINCIPLE = YES
TC_R1_GENERAL_S_COMPACTNESS = POOR
TC_R1_GENERAL_S_FORMAL_CERTIFICATE = OPEN
Z6_FINAL_POSTCRACK_2D_PU = OPEN
```

---

# 6. Alternative constitutive-model screen — do not stay on one model by default

A fresh external literature screen was performed specifically for alternatives with a natural G6-compatible total-strain form.

## 6.1 Cedolin & Mulas (1984)

`Biaxial Stress-Strain Relation for Concrete`, J. Eng. Mech. 110(2), 187–206, DOI 10.1061/(ASCE)0733-9399(1984)110:2(187).

Strong points:

- explicitly described by the authors as a **total, explicit stress–strain relation**;
- monotonic biaxial loading;
- nonlinear bulk/shear moduli expressed in strain invariants;
- plane-stress transverse strain eliminated by an explicit empirical expression;
- only three concrete parameters.

This is unusually well aligned with G4/G6.

Blocking point for the present problem:

- the published 1984 model is stated as valid **up to peak stress**;
- it is not, from the currently recovered source text, a source-closed post-transverse-crack continuation comparable to Nguyen/MCFT TC.

```text
CEDOLIN_MULAS_1984_G6_ARCHITECTURE = VERY_PROMISING
CEDOLIN_MULAS_1984_POSTCRACK_TC_CLOSURE = NOT_ESTABLISHED
CEDOLIN_MULAS_1984_CURRENT_DECISION = ALTERNATIVE_AUDIT_1 / NOT_DROP_IN_REPLACEMENT_YET
```

## 6.2 Bažant & Tsubaki (1980)

`Total Strain Theory and Path-Dependence of Concrete`, J. Eng. Mech. Div. 106(6), 1151–1173.

Strong points:

- algebraic total-strain to stress relation;
- monotonic loading;
- includes peak, strain softening, inelastic dilatancy and failure envelopes;
- path-dependent correction terms are additional to a total-strain core.

Blocking point:

- the source explicitly frames the total-strain model for plain concrete **free of continuous cracks**.

The current Z problem is precisely continuation after a transverse TC crack marker, so this is not a clean source-identical substitute.

```text
BAZANT_TSUBAKI_1980_TOTAL_STRAIN_G6 = PROMISING
BAZANT_TSUBAKI_1980_CRACKED_TC_DOMAIN_MATCH = FAIL_OR_UNPROVEN
```

## 6.3 Darwin & Pecknold (1977)

The model is a strong monotonic biaxial reference and reproduces biaxial curves from equivalent-uniaxial curves, but its equivalent-uniaxial/secant machinery is not simpler than TC-R1 for the present finite explicit section reduction.

```text
DARWIN_PECKNOLD_1977 = ORACLE_OR_SECONDARY_ALTERNATIVE
```

## 6.4 MCFT / softened membrane models

Vecchio–Collins MCFT is exactly the source family already entering Nguyen Eq. (3.43). Later softened-membrane models model the complete cracked RC membrane response more fully, but bring rotating crack/steel coupling and state/path machinery. They are useful source oracles, not a simpler G6 drop-in law for steel-shell concrete.

---

# 7. Decision

Literal Nguyen is **not** retained at all costs:

```text
LITERAL_NGUYEN_POSTCRACK_TC = REJECTED_FROM_PRODUCTION_MAINLINE
```

The source-constrained TC-R1 reduction is materially viable enough that an immediate wholesale constitutive-model replacement is not justified yet:

```text
NC_TC_R1 = ACTIVE_CANDIDATE
```

but it is not frozen as final because its general-s section closure is not yet compactly certified.

The replacement trigger is now explicit:

```text
IF TC_R1_GENERAL_S_REDUCTION requires a large opaque primitive/compiler layer
OR fails branch/admissibility certification
THEN pivot first to CEDOLIN_MULAS_1984 equation-level audit,
with BAZANT_TSUBAKI_1980 as a postpeak total-strain oracle,
without fitting any structural Pu.
```

This keeps the project from becoming dependent on Nguyen while also avoiding a premature switch to a literature model that does not actually close the cracked-TC domain.
