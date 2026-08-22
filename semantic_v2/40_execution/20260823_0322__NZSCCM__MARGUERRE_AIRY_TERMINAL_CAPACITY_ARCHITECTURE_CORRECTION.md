# NZ-SCCM — Marguerre–Airy terminal-capacity architecture correction

**Time:** 2026-08-23 03:22 +08:00  
**Status:** `ARCHITECTURE_CORRECTION / USER_CLARIFICATION_ACCEPTED`

## 0. Correction

The 20260823_0246 audit correctly proved that the reduced elastic Marguerre–Airy postbuckling law

\[
P_{pb}(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0)
\]

is monotone for admissible `q>=0`.  However its subsequent interpretation was wrong.

The locked explicit theory never required a geometric load fold `dPpb/dq=0` to define `Pu`.  Section 12 of the governing V1 explicitly proves `Ppb'(q)>0` in order to eliminate load-path tracking.  The ultimate load is obtained by intersecting the Airy/Galerkin structural demand with a terminal material/capacity constraint.

Therefore:

```text
MA_V1_MONOTONE_POSTBUCKLING = CORRECT
MA_V1_GLOBAL_FOLD_REQUIRED = FALSE
NO_FINITE_Pu_BECAUSE_NO_GLOBAL_FOLD = RETRACTED
CURRENT_MATERIAL_INTO_AIRY_COMPATIBILITY = NOT_REQUIRED
NONLINEAR_CURRENT_MATERIAL_GLOBAL_WORK_CLOSURE = RETRACTED_AS_NEXT_TASK
```

## 1. Correct separation of roles

### Structural layer — Marguerre–Airy

The structure is solved first from geometry and initial elastic stiffness:

\[
w_i=bq_0\phi,\qquad w=bq\phi,
\]

\[
N_x=\theta_{,yy},\qquad N_y=\theta_{,xx},\qquad N_{xy}=-\theta_{,xy},
\]

followed by the Airy compatibility solution and Galerkin projection.  This gives the complete structural demand family, including

\[
P=P_{pb}(q),
\]

and, for the single-halfwave V1 section,

\[
n(s;q)=\frac{P_{pb}(q)}b+Gq(q+2q_0)(1-2s^2),
\]

\[
m(s;q)=Jqs.
\]

The nonlinear NC-M6 current law is **not** inserted into the Airy compatibility operator.  Initial elastic properties still enter the initial `A,D` stiffnesses; this is distinct from the nonlinear terminal material law.

### Terminal material/capacity layer

Material acts after the structural demand has been obtained.  Its role is to determine whether the current resultant demand is admissible or has reached a failure/capacity surface.

For the original uniaxial RC `N-M` formulation, the governing V1 already gives

\[
F_N(q,s,c)=n_d(s,q)-n_u(c)=0,
\]

\[
F_M(q,s,c)=m_d(s,q)-m_u(c)=0,
\]

and for an interior controlling location

\[
F_S(q,s,c)=0.
\]

Thus

\[
\boxed{F_N=F_M=F_S=0}
\]

(or the corresponding endpoint / active-set boundary equations) directly determines the finite algebraic candidates.  `P` is already eliminated by `P=P_pb(q)`.

For a biaxial terminal material model, the same architecture is retained: the Airy solution supplies longitudinal and transverse resultants, while the terminal material constraint must include the additional transverse resultant components.  The two-affine-thickness interface

\[
\lambda_x(z)=a_x+b_xz,\qquad \lambda_y(z)=a_y+b_yz
\]

belongs to this terminal capacity layer, not to the Airy equilibrium layer.

## 2. Meaning of “global” after the Panel21 regression

The rejected architecture is the later local current-section singularity

\[
\det J_{sec}=0
\]

used as an automatic plate-ultimate criterion.  The Panel21 A/B/D regression showed that this local fold can reduce the predicted plate load by roughly one half.

The required correction is **not** to make the Airy backbone material-nonlinear.  It is to restore the original explicit architecture:

\[
\boxed{
\text{Airy/Galerkin global structural demand}
\;\to\;
\text{terminal resultant-capacity constraint}
\;\to\;
P_u
}
\]

For one-axis bending this terminal constraint is `N-M`.  For a true biaxial state it must additionally enforce the transverse resultant/capacity conditions (and shear components when nonzero).

## 3. Status of NC-M6

The 20260822 NC-M6 execution itself stated that the explicit structural path was unchanged and used the two-independent-affine-slope section interface only in the material layer.  What is now rejected is the later choice of `current-map section fold / det Jsec=0` as the plate terminal.

Hence:

```text
AIRY_STRUCTURAL_BACKBONE = RETAIN
NC_M6_IN_AIRY_OPERATOR = NO
NC_M6_AS_TERMINAL_MATERIAL_CONSTRAINT = YES
LOCAL_detJsec_AS_PLATE_Pu = REJECTED
ORIGINAL_EXPLICIT_DEMAND_CAPACITY_INTERSECTION = RESTORED
```

## 4. Next task

Recompute Panels 1, 14 and 21 on one common architecture:

1. generate the Airy/Galerkin structural demand from the specimen geometry and initial elastic stiffness;
2. use the prescribed/source waveform version where that branch is frozen;
3. apply NC-M6 only at the final terminal resultant-capacity layer;
4. for the uniaxial reduction use the `N-M` contact equations; for the full two-axis state include the transverse resultant constraints;
5. do not use `det Jsec=0` as the primary plate-ultimate criterion;
6. no formal spatial quadrature/material points and no experimental load in root selection.

The 20260823_0246 file is retained as provenance for the monotonicity proof only; its `nonlinear-current-material-in-Airy` next-step interpretation is superseded by this correction.
