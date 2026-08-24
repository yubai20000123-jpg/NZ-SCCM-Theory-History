# NZ-SCCM — R20-1 direct Yun -> axial y-normal Ny-My source-closure gate

**Time:** 2026-08-24 23:05 +08:00  
**Status:** `EXECUTED / SOURCE_CLOSURE_FAIL_EXACT / NO_NEW_SECTION_LAW_INVENTED / R20_2_BLOCKED / R20_3_HOLD`

## 0. Scope

R20-1 executes the fail-fast gate frozen in R20-0. It asks only whether the existing repository/source chain uniquely defines a direct map

\[
\boxed{
\text{historical current Yun steel field}
\longrightarrow
\text{work-conjugate axial y-normal }(N_y,M_y)\text{ terminal}
}
\]

while keeping the user-approved structural architecture

\[
\text{Marguerre--Airy demand}\rightarrow\text{direct terminal contact}\rightarrow P_u
\]

and without restoring D15 or a global material virtual-work residual/Jacobian as the structural mainline.

No comparator is opened. No new `Pu` is calculated.

## 1. Source chain recovered

### 1.1 Airy structural terminal architecture

Retained from the 2026-08-23 architecture correction and R07:

\[
P_{pb}(q)=P_{cr}\frac{q}{q+q_0}+Cq(q+2q_0),
\]

\[
n_d(s;q)=\frac{P_{pb}(q)}b+Gq(q+2q_0)(1-2s^2),
\qquad
m_d(s;q)=J_yqs.
\]

The selected hard terminal is the axial y-normal resultant contact.

### 1.2 Work-conjugate finite terminal projection

The 2026-08-23 projected-moment gate proves that a single frozen Airy bending mode has only one work-conjugate bending coordinate. If the Airy curvature direction is

\[
\mathbf d=(d_x,d_y)^T,
\]

then

\[
\boxed{M_\parallel=d_xM_x+d_yM_y}
\]

is the unique bending terminal equation for that mode; `M_perp` is a reaction to the prohibited orthogonal curvature, not a second equilibrium row.

That gate defines section resultants from a **thickness-line material field at one finite control location**:

\[
N_j=\int \sigma_j(z)\,dz+\text{phase corrections},
\qquad
M_j=\int z\sigma_j(z)\,dz+\text{phase corrections}.
\]

This closure is exact for the finite terminal-section family it defines.

### 1.3 Historical current Yun + ideal-EP field

The 2026-08-18 unified Yun execution instead defines a two-dimensional local steel field for every local strip:

\[
\varepsilon_{s,i}(x_i,y)
=\varepsilon_y^g(D,q,\alpha;x_g,y,z_f)
+A_i(w_{0,y}^g+\Delta w_{,y}^g)\phi_{i,y}
+A_{0i}\Delta w_{,y}^g\phi_{i,y}
+\left(A_{0i}A_i+\frac12A_i^2\right)\phi_{i,y}^2,
\]

\[
\sigma_{s,i}=\operatorname{clip}(E_s\varepsilon_{s,i},-f_y,+f_y),
\]

with the R19-corrected global/local coordinate map

\[
\boxed{x_g=iB_s+x_i}.
\]

Each local amplitude is determined by

\[
R_{A_i}=C_\sigma\left[k_{cr}A_i+H(2A_{0i}A_i+A_i^2)(A_i+A_{0i})\right]
-\bar\sigma_{c,i}(A_i+A_{0i})=0,
\]

where

\[
\boxed{\bar\sigma_{c,i}
=-\frac1{\Omega_i}\int_{\Omega_i}\sigma_{s,i}\,d\Omega}
\]

is a **subpanel area average**.

The same historical execution reports steel-face axial force as

\[
\boxed{
P_{face}=-\frac{t_s}{\ell}\sum_{\pm}\sum_i\int_{\Omega_i}\sigma_s\,d\Omega,
}
\]

again an area-integrated/global phase quantity.

### 1.4 Yun Chapter-2 exact source formulas

The Yun Chapter-2 source audit supplies a finite harmonic local Airy stress field and the exact local mean shortening relation. It also supplies the average axial stress / effective-width lineage.

This is sufficient to define local elastic large-deflection redistribution and average local plate resistance, but it does not prescribe how the **2026-08-18 ideal-EP current area field** must be projected into the later R07/R20 work-conjugate control-line terminal.

## 2. Exact closure test

For R20-2 to be well posed under the approved architecture, the repository must determine a unique operator of the form

\[
\boxed{
\mathcal H_Y:
\{\sigma_{s,i}(x_i,y;D,q,\alpha,A_i)\}_{i,\pm}
\mapsto
\{N_y^{s,Yun}(s;q),M_\parallel^{s,Yun}(s;q)\}.
}
\]

It must also determine all state variables required by the left side from the direct Airy terminal state.

The recovered sources do **not** close either requirement uniquely.

## 3. Blocker A — in-plane Yun field -> terminal section resultant is underdetermined

The available sources provide three different but non-equivalent objects:

1. **point/local-cut steel stress** `sigma_s(x_i,y)`;
2. **subpanel area-average stress** `bar_sigma_c,i`, used by `R_Ai`;
3. **global/phase area-integrated face force** `P_face`.

The later R07/R20 terminal requires a work-conjugate **finite control-section** resultant `Ny` and one projected bending resultant `M_parallel`.

No frozen repository/source identity selects one of the following possible bridges:

```text
A. evaluate the local Yun field at the terminal control cut;
B. replace the cut field by the subpanel area average;
C. use a Yun effective-width / homogenized average law;
D. phase-average all strips before constructing the terminal;
E. introduce another localization/homogenization operator.
```

These choices are mechanically different. In particular, the Yun local field is high-frequency in the local longitudinal coordinate, so a point cut can coincide with a local-wave node while the subpanel average and global face force remain nonzero.

Choosing A--E would therefore be a **new modelling law**, not a retrieval of an already-frozen equation.

Hence

\[
\boxed{
\text{Yun area field}\not\xRightarrow[\text{current frozen sources}]{\text{unique}}
(N_y^{s,Yun},M_\parallel^{s,Yun})_{\text{R20 terminal}}.
}
\]

## 4. Blocker B — R19 current steel strain still requires D and alpha

The R19-corrected global steel strain entering the historical Yun field is

\[
e_y=-D+\alpha A_y
+\frac{\pi^2k^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right)F_y
+\frac{\pi^2t_rk^2}{2\varepsilon_0b}qH_s\zeta.
\]

Thus the historical current Yun stress is not a function of `q` alone; it requires the membrane/generalized state `(D,alpha)`.

In the 2026-08-18 execution those variables were closed by the global coupled equations

\[
R_q=0,\qquad R_A^\Delta=0,
\]

with all material phases assembled.

R20-0 explicitly supersedes that global material virtual-work residual/Jacobian as the R20 structural mainline. The frozen direct Airy demand law supplies `Ppb(q), nd(s;q), md(s;q)` but does not supply a replacement unique map

\[
\boxed{q\mapsto(D,\alpha)}
\]

for the historical ideal-EP Yun current field.

Therefore even before choosing an in-plane homogenization/cut rule, the current steel stress field required by the historical 2026-08-18 equations is not uniquely determined by the accepted R20 terminal variables.

## 5. Blocker C — full-coupling versus terminal-only interpretation

R17 correctly notes that if current Yun stress/tangent is fed back into structural stiffness/equilibrium, pre-Yun constants `Pcr,C,G,Jy` cannot simultaneously be treated as globally frozen full-coupling coefficients.

R20-0 deliberately chooses the earlier Airy-demand -> terminal-capacity architecture instead of that full material-feedback rewire. This is a valid governance choice only if the Yun steel phase can be represented by a separately source-closed terminal resultant law.

Blockers A and B show that such a terminal law has not yet been frozen in the repository.

Therefore R20 may not claim both

```text
PRE-YUN AIRY DEMAND CONSTANTS = FROZEN
```

and

```text
HISTORICAL 2026-08-18 FULL CURRENT YUN FIELD = TRANSPLANTED WITHOUT AN EXTRA BRIDGE
```

without adding a new constitutive/homogenization assumption.

## 6. Why the 2026-08-23 projected-moment gate does not by itself solve this

The projected-moment gate is retained and important:

\[
M_\parallel=\mathbf d^T\mathbf M
\]

is the correct work-conjugate bending resultant for a single Airy bending DOF.

But that gate begins from a material stress field already defined on one thickness line at a control location. It does not specify how a separate two-dimensional local steel-subpanel field should be collapsed onto that thickness line.

Thus

```text
PROJECTED_MOMENT_WORK_CONJUGACY = CLOSED
YUN_IN_PLANE_TO_TERMINAL_SECTION_PROJECTION = NOT_CLOSED
```

## 7. Why Yun effective width is not silently substituted

Yun Chapter 5 and Sun provide source precedent for effective-width/effective-area steel resultants. R15 also proved that a **constant ultimate effective width** belongs to the same resultant-cap class as a scalar face cap.

A progressive Yun effective-width/homogenized law could in principle become the missing bridge, but the current project has not frozen which current Yun quantity drives that homogenization under the 2026-08-18 ideal-EP field, nor how it maps to top/bottom face `Ny` and `M_parallel` without double counting the gross Airy mode.

Therefore R20-1 does not silently activate such a law.

## 8. R20-1 decision

```text
R20_1_EXECUTION = COMPLETE
R20_1_SOURCE_CLOSURE = FAIL_EXACT

AIRY_DEMAND_ARCHITECTURE = RETAIN
AXIAL_Y_NORMAL_TERMINAL = RETAIN
PROJECTED_MOMENT_Mparallel = RETAIN_WHEN_NEEDED
YUN_ALWAYS_ON = RETAIN
R19_KINEMATIC_SCALING_COORDINATE_BRIDGE = RETAIN

MISSING_IDENTITY_1 = YUN_IN_PLANE_CURRENT_FIELD -> WORK_CONJUGATE_TERMINAL_Ny_Mparallel
MISSING_IDENTITY_2 = DIRECT_R20_TERMINAL_STATE -> (D,alpha) REQUIRED_BY_HISTORICAL_CURRENT_YUN_FIELD

NEW_HOMOGENIZATION_ASSUMPTION = NOT_AUTHORIZED
NEW_SECTION_LAW = NOT_INVENTED
D15_R20_ROUTE = NO
GLOBAL_MATERIAL_VIRTUAL_WORK_RJ_R20_ROUTE = NO

NEW_Pu_Z1 = NOT_CALCULATED
NEW_Pu_Z4 = NOT_CALCULATED
HISTORICAL_14P44689544_52P43155584 = REGRESSION_ONLY / NOT_RELABELED

R20_2 = BLOCKED_BY_R20_1_SOURCE_CLOSURE
R20_3 = HOLD
```

## 9. Minimum admissible ways to reopen R20-2 later

R20-2 can be reopened only by an explicit user-approved choice among source-backed architecture options, for example:

### Option H — source-backed homogenized Yun terminal

Derive/freeze one local-to-terminal homogenization directly from Yun Chapter 2/5 and Sun effective-area precedent, including:

- the exact current driving quantity;
- top/bottom-face axial resultant;
- work-conjugate projected moment;
- local-amplitude elimination;
- no-double-counting proof with gross Airy;
- exact zero-formal-spatial-integration representation.

This changes the terminal steel law but keeps Airy demand frozen.

### Option G — retain historical current Yun state closure

Retain the 2026-08-18 `(D,q,alpha,A_i)` current field and its global state equations, then recover `Ny,My` after solving. This is closer to R17/R19 full-coupling architecture, but it reopens the global equilibrium route that R20-0 intentionally superseded.

Neither option is selected inside R20-1.
