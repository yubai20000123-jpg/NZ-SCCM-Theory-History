# NZ-SCCM — SSNC-R04 Airy initial-ABD offset-stiffness + ideal-EP 2D terminal-resultant gate

**Time:** 2026-08-25 08:51 +08:00  
**Status:** `EXECUTED / ARCHITECTURE_CORRECTED / INITIAL_OFFSET_STIFFNESS_LOCKED / IDEAL-EP 2D TERMINAL GATE PASS / CURRENT-TANGENT NO LONGER A Pu PRE-GATE / Pu NOT YET RECALCULATED`

## 0. Decision first

The current production architecture is now fixed as

\[
\boxed{
\text{initial full-section elastic }(\mathbf A^0,\mathbf B^0,\mathbf D^0)
\to
\text{explicit Marguerre--Airy structural demand}
\to
\text{current terminal resultants/capacity}
\to P_u.
}
\]

The steel shell therefore enters **twice, in two different roles**:

1. **Structural-demand role:** its *initial elastic* stiffness contributes to the composite `A0,B0,D0` used by the Airy/Galerkin coefficients.
2. **Terminal-capacity role:** its local postbuckling/yield behavior supplies current/capped `N` and `M` resultants at the terminal intersection.

These roles are not double counting.  The first generates the structural demand family; the second limits that demand.

The SSNC-R03 current 6x6 postbuckling tangent remains a valid diagnostic/future extension but is **not** required by the accepted explicit Airy `Pu` route and shall not block Z0--Z6 terminal calculations.

```text
CURRENT_MATERIAL_TANGENT_INTO_AIRY = NO
INITIAL_ELASTIC_ABD_INTO_AIRY = YES
R03_CURRENT_6X6_TANGENT_AS_Pu_GATE = NO
R03_CURRENT_6X6_TANGENT_AS_DIAGNOSTIC = YES
```

---

## 1. The steel-face offset stiffness is mandatory and is now explicitly locked

For a uniform layer with plane-stress constitutive matrix `Q`, thickness `t`, and centroid offset `z_c` from the Airy/global reference surface,

\[
\boxed{\mathbf A=\mathbf Q t},
\]

\[
\boxed{\mathbf B=\mathbf Q t z_c},
\]

\[
\boxed{
\mathbf D=\mathbf Q\left(tz_c^2+\frac{t^3}{12}\right).
}
\]

Thus the two external steel faces at `z_+=+z_f`, `z_-=-z_f` contribute

\[
\boxed{
\mathbf D_s^0
=2\mathbf Q_s\left(t_s z_f^2+\frac{t_s^3}{12}\right).
}
\]

The first term

\[
\boxed{2\mathbf Q_st_sz_f^2}
\]

is the offset/parallel-axis contribution. It is not optional and must be included in the initial Airy bending stiffness.

For a symmetric top/bottom shell,

\[
\mathbf B_s^0
=\mathbf Q_st_sz_f+\mathbf Q_st_s(-z_f)=\mathbf0.
\]

So the offset does **not** create initial membrane-bending coupling in a geometrically/materially symmetric shell, but it strongly increases the initial `D` matrix.

---

## 2. Independent offset-stiffness audit

The executable uses the already source-audited reduced DSCW geometry only as a gate state:

```text
h = 130 mm
ts = 4 mm / face
tc = 122 mm
zf = 63 mm
Es = 206000 MPa
nu_s = 0.30
Ec = 32500 MPa
nu_c = 0.20
```

With plane-stress `Q` convention it gives

```text
B0_sym_abs                    = 0.000000000000e+00
Dsteel_parallel_axis_abs      = 4.768371582031e-07
Dsteel_direct_integral_abs    = 9.536743164062e-07
Dsteel11_full_Nmm             = 7.190230036630e+09
Dsteel11_offset_Nmm           = 7.187815384615e+09
Dsteel11_own_skin_Nmm         = 2.414652014652e+06
offset_fraction_of_steel_D11  = 9.996641759718e-01
steel_fraction_of_total_D11   = 5.839512724645e-01
```

Hence in this representative geometry, about

\[
\boxed{99.9664\%}
\]

of the steel-face `D11` contribution comes from the physical offset `z_f`, not the small `t_s^3/12` own-skin term.

This is fully consistent with the earlier source-grounded `E_sI_s+E_cI_c` diagnostic, which found that the outer steel faces carry roughly 57% of the reduced object's elastic bending rigidity because they lie at the outer fibres.

### Governance consequence

Any Airy coefficient generator that uses only

\[
E_st_s^3/12
\]

for the two external faces is invalid.

The production initial stiffness must be generated from the full layer integral / parallel-axis form above before `Pcr,C,G,J` are accepted.

---

## 3. What Airy does and does not calculate

The phrase “steel shell is calculated explicitly by Airy” is accepted only with this precise meaning:

### Airy calculates the full composite **structural demand field**

Using initial full-section stiffness,

\[
(\mathbf A^0,\mathbf B^0,\mathbf D^0)
\to
P_{pb}(q),\ N_x,N_y,N_{xy},\ M_x,M_y,M_{xy}.
\]

The steel shell is already represented in these structural coefficients through its initial elastic stiffness, including the offset term.

### Airy does **not** directly supply the nonlinear steel capacity law

Local steel postbuckling and yielding remain on the terminal side:

\[
\text{Airy demand}
\leftrightarrow
\text{steel + concrete current/capacity resultants}.
\]

Therefore current steel tangent loss is not fed back to regenerate the Airy demand curve in the present production route.

---

## 4. Simplified ideal elastic-perfectly-plastic 2D steel terminal

The user-authorized simplification is now adopted for the **terminal layer only**.

### 4.1 No through-thickness elastic/plastic partition

Each external steel face is treated as one homogenized membrane layer at its physical centroid `z_f`.

No plastic-front depth inside the 4-mm skin is introduced.

The gross terminal moment from the face is therefore

\[
\boxed{\mathbf M_f=z_f\mathbf N_f}.
\]

This retains the dominant physical lever arm exactly.

The own-skin `Et^3/12` term is retained in the **initial Airy `D0`**, but no separate post-yield through-thickness plastic bending block is introduced at the simplified terminal.

### 4.2 2D Mises ideal-EP cap

Let a source/analytical pre-yield steel-shell branch provide a trial mean plane-stress state

\[
\boldsymbol\sigma^{tr}
=(\sigma_x^{tr},\sigma_y^{tr},\tau_{xy}^{tr})^T.
\]

Define

\[
\sigma_{vm}^{tr}
=\sqrt{(\sigma_x^{tr})^2
-\sigma_x^{tr}\sigma_y^{tr}
+(\sigma_y^{tr})^2
+3(\tau_{xy}^{tr})^2}.
\]

The simplified path-free terminal cap is

\[
\boxed{
\lambda
=\min\left(1,\frac{f_y}{\sigma_{vm}^{tr}}\right),
\qquad
\boldsymbol\sigma^{cap}=\lambda\boldsymbol\sigma^{tr}.
}
\]

Then

\[
\boxed{\mathbf N_f=t_s\boldsymbol\sigma^{cap}},
\qquad
\boxed{\mathbf M_f=z_f\mathbf N_f}.
\]

This is:

- exact for the uniaxial ideal-perfectly-plastic degeneration;
- exactly `x<->y` symmetric;
- Mises bounded;
- a **proportional-loading analytical approximation** for the full biaxial/shear post-yield face terminal;
- not claimed to be a full associated J2 return-mapping history law.

That limitation is acceptable in the current zero-history, explicit terminal architecture and is clearly labelled rather than hidden.

### 4.3 Tangent convention

For theory,

\[
E_t=0
\]

after ideal-plastic yielding.

If a numerical root/Jacobian implementation requires nonzero regularization, a tiny

\[
E_t=\eta E_s,\qquad \eta\sim10^{-8}\text{--}10^{-6}
\]

may be used **only as numerical regularization**.

Crucially,

```text
POST_YIELD_TANGENT -> NOT FED INTO AIRY
POST_YIELD_STRESS/RESULTANT -> RETAINED AT THE TERMINAL
```

so setting `Et=0` never means that the yielded steel force is deleted.

---

## 5. Executed terminal gates

The executable

`semantic_v2/40_execution/steel_shell/20260825_0851__NZSCCM__SSNC_R04_IDEAL_EP_2D_TERMINAL_RESULTANT_GATE.py`

returns

```text
SSNC_R04_IDEAL_EP_2D_TERMINAL_RESULTANT_GATE = PASS
AIRY_USES_INITIAL_ABD_ONLY = True
INITIAL_STEEL_OFFSET_STIFFNESS_INCLUDED = True
CURRENT_TANGENT_FEEDBACK_TO_AIRY = False
THROUGH_THICKNESS_PLASTIC_PARTITION = False
POST_YIELD_TANGENT_THEORY = 0.0
POST_YIELD_TANGENT_NUMERICAL_REGULARIZATION = optional
zf_mm = 63.000000000000
B0_sym_abs = 0.000000000000e+00
Dsteel_parallel_axis_abs = 4.768371582031e-07
Dsteel_direct_integral_abs = 9.536743164062e-07
Dsteel11_full_Nmm = 7.190230036630e+09
Dsteel11_offset_Nmm = 7.187815384615e+09
Dsteel11_own_skin_Nmm = 2.414652014652e+06
offset_fraction_of_steel_D11 = 9.996641759718e-01
steel_fraction_of_total_D11 = 5.839512724645e-01
trial_vm_MPa = 374.032084185301
plastic_scale_lambda = 0.949116439498
capped_vm_MPa = 355.000000000000
uniaxial_capped_sy_MPa = 355.000000000000
xy_sym_abs = 0.000000000000e+00
```

The arbitrary 2D stress vector used here is a gate state only, not a Z-series prediction.

---

## 6. Double-counting audit

The same face offset appears in two mathematically different quantities:

### Initial structural stiffness

\[
\mathbf D_f^0
=\mathbf Q_s\left(t_sz_f^2+\frac{t_s^3}{12}\right).
\]

This is used once in the Airy structural demand.

### Terminal resisting moment

\[
\mathbf M_f^{cap}=z_f\mathbf N_f^{cap}.
\]

This is used once in the material/capacity terminal.

These are not the same contribution and do not double count each other. One is a derivative/elastic stiffness used to generate the demand path; the other is a force lever arm in the terminal resistance state.

---

## 7. Corrected production status

```text
STRUCTURAL_FRONT = FULL_2D_MARGUERRE_AIRY
AIRY_STIFFNESS = INITIAL_FULL_COMPOSITE_ABD
STEEL_OFFSET_STIFFNESS = INCLUDED_EXACTLY
SYMMETRIC_INITIAL_B = ZERO
CURRENT_STEEL_TANGENT_FEEDBACK = NO
R03_CURRENT_6X6_TANGENT = DIAGNOSTIC_ONLY

STEEL_TERMINAL = 2D_FULL_RESULTANT / IDEAL-EP SIMPLIFICATION
THROUGH_THICKNESS_PLASTIC_PARTITION = NO
POST_YIELD_THEORETICAL_TANGENT = ZERO
POST_YIELD_NUMERICAL_TANGENT = OPTIONAL_TINY_REGULARIZATION
TERMINAL_FACE_MOMENT = z_f * N_f
OWN_SKIN_PLASTIC_BENDING_BLOCK = NOT_INTRODUCED

GLOBAL_MARGUERRE_AIRY = UNCHANGED
GLOBAL_ULTIMATE_STATE = UNCHANGED
EFFECTIVE_WIDTH_OR_AREA_PRODUCTION = FALSE
FORMAL_SPATIAL_QUADRATURE = 0
MATERIAL_POINTS = 0
Pu_CALCULATED_IN_R04 = FALSE
```

## 8. Next executable task

Before a new Z0--Z6 `Pu` batch is accepted, regenerate/audit each specimen's initial Airy coefficients using the explicit full-section `ABD` formula above.  Then connect the R02 biaxial postbuckling trial-resultant branch to this R04 ideal-EP terminal cap and solve the unchanged Airy demand/resultant-capacity intersection.

No post-first-yield 6x6 tangent derivation is required as a prerequisite.
