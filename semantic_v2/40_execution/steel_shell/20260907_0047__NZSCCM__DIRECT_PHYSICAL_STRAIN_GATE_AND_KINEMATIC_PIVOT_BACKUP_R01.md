# NZ-SCCM — Direct physical-strain gate and kinematic pivot backup R01

**Date:** 2026-09-07 00:47 +08:00  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Status:** `BACKUP / DIAGNOSTIC / NO FEM CALIBRATION / NO PRODUCTION CHANGE`

## 0. Why this checkpoint exists

This file backs up the full conceptual pivot reached in the current conversation before the next calculation is executed. The main conclusion is that the recent failure of the 01 route should no longer be attributed first to the UHPC compression backbone or to the frozen Multiwave steel operator. The dominant suspect is now the upstream kinematic/generalized-strain closure.

The current evidence chain is:

\[
\text{FEM physical strain field}
\rightarrow
\text{01 UHPC / frozen Multiwave}
\rightarrow
\text{responses close to FEM}
\]

whereas the old route was effectively

\[
q\rightarrow N,M\rightarrow (\varepsilon_0,\kappa)\rightarrow \varepsilon(z)
\]

and produced wrong force allocation and one-face steel unloading.

## 1. Conceptual pivot: return to steel postbuckling logic

The route was reframed by asking why steel postbuckling can be compressed into a small structural model. For steel before yield, material behavior is simple and most nonlinearity comes from geometry/postbuckling. UHPC was therefore considered not as a large Nguyen-style material-point state machine, but as a source-derived structural section operator.

The successive candidate identities were:

1. `UHPC-GS0/U`: one-dimensional current section
   \[
   (\varepsilon_0,\kappa)\to(N_U,M_U,A_U^t,B_U^t,D_U^t).
   \]
2. `UHPC-GS1/TC`: same section plus a transverse-state softening scalar when independently supported by UHPC biaxial evidence.
3. `UHPC-GS2/MNphi`: reduced 2D current section operator for compatibility with an Aghayere–MacGregor-type \(M-N-\phi\) equilibrium path.

These were diagnostic abstractions, not new constitutive laws. The material source was always intended to remain existing UHPC research plus the project’s already frozen 01 compression backbone.

## 2. Direct-state extraction and physical-coordinate correction

The nine ODB peak states were re-extracted read-only under a unified physical-coordinate contract. The crucial coordinate mapping is:

\[
\boxed{
\text{FE global X}=\text{plate width/physical }x,
\quad
\text{FE global Z}=\text{axial loading/physical }y,
\quad
\text{FE global Y}=\text{thickness/out-of-plane/physical }z.
}
\]

The physical-direction workbook confirms this mapping case-by-case and transforms shell tensors from their actual local bases rather than equating Abaqus component labels with physical directions.

This makes a major historical warning necessary: earlier direct extraction notes treated UHPC solid `LE22` as axial `eps_y`, even though the verified physical contract shows FE global Y is the thickness direction and FE global Z is axial. Therefore all old FEM-derived `epsilon0/kappa` ledgers that were built from that `LE22` interpretation must be re-audited before being used as evidence. They are not automatically valid axial strain/curvature observables.

## 3. UHPC direct physical-strain gate

Using the corrected physical axial strain \(\varepsilon_y^{FEM}\) record-by-record and the unchanged 01 compression backbone gives very good axial stress recovery for the cases remaining inside the 01 peak-front domain.

For BH032–BH100, the weighted average axial-stress errors from direct physical strain were approximately:

- BH032: +6.92%
- BH050: -0.37%
- BH060: -1.46%
- BH070: -2.15%
- BH085: -3.70%
- BH100: -5.44%

For BH050–BH100 the pointwise weighted \(R^2\) values are about 0.966–0.982, with RMSE only about 1–3.5 MPa.

Thus the current evidence supports:

\[
\boxed{
\varepsilon_y^{FEM}\to\sigma_{01}(\varepsilon_y^{FEM})
\text{ is already very accurate for BH050--BH100.}
}
\]

This directly supersedes the earlier interpretation that the UHPC backbone itself must be reduced by 15–60% based on old `epsilon0/kappa` force mismatch.

BH005/BH010/BH020 are different because much/all of the peak section exceeds the current 01 peak-front domain \(|\varepsilon|\le0.0035\). Their remaining material gap is primarily a legitimate peak/post-peak extension problem, not evidence that the whole nine-case pre-peak backbone is wrong.

## 4. Thickness linearity versus widthwise membrane field

At each physical width station, the corrected FEM axial strain was fitted through thickness as

\[
\varepsilon_y(x,z)\approx\varepsilon_y^0(x)+z\kappa_y(x).
\]

Replacing the raw through-thickness records by this local linear fit changed the resulting 01 UHPC axial force by essentially zero for BH032–BH100 (order \(10^{-2}\%\) or less in the previously executed audit).

Therefore the section-through-thickness linearity assumption itself is not the dominant error.

The critical missing structure is widthwise variation:

\[
\boxed{
\varepsilon_y^{0}=\varepsilon_y^{0}(x),
\quad\text{not one global }\varepsilon_0.
}
\]

The prior variance decomposition indicated that roughly 94–98% of the spatial variation of the physical axial strain at the audited peak section is associated with widthwise variation, while the through-thickness curvature contribution is much smaller.

## 5. Steel direct-state gate

Using the physically transformed FEM in-plane strain pair as input to the frozen Multiwave/R02-R06 operator recovers the two steel-face axial response far better than the old coupled route. The current diagnostic two-face axial-stress-sum errors were approximately:

- BH005: -4.8%
- BH010: -5.6%
- BH020: -3.3%
- BH032: +18.1%
- BH050: +5.8%
- BH060: +2.6%
- BH070: -7.1%
- BH085: -1.7%
- BH100: -3.2%

BH032 remains the main steel anomaly. The large BH050–BH100 steel under-participation seen in the old coupled path is therefore not sufficient evidence to modify Multiwave. Current status:

\[
\boxed{
\text{MULTIWAVE STEEL = FROZEN UNDER DIRECT-STATE AUDIT.}
}
\]

## 6. Key kinematic conclusion

For a prescribed out-of-plane shape

\[
w=A\psi(x,y),
\]

once \(A\) is known the curvature field derived from second derivatives of \(w\) is fixed, but the membrane strain field is not. In von Kármán kinematics,

\[
\varepsilon_x^0=u_{,x}+\tfrac12 w_{,x}^2,
\]
\[
\varepsilon_y^0=v_{,y}+\tfrac12 w_{,y}^2,
\]
\[
\gamma_{xy}^0=u_{,y}+v_{,x}+w_{,x}w_{,y}.
\]

Therefore \(q\) or \(w(q)\) alone cannot determine the force. Additional membrane variables (or a statically admissible stress/Airy field) plus equilibrium/generalized work are required.

This is the current interpretation of why finite elements obtain a reproducible solution: FE solves \(u,v,w\) simultaneously under compatibility, constitutive laws, boundary conditions and equilibrium; uniqueness does not come from Gauss points.

## 7. Consequence for Aghayere–MacGregor route

The Aghayere–MacGregor \(M-N-\phi\) idea is now retained primarily as a low-dimensional equilibrium/generalized-work closure, not as a replacement material model.

The intended architecture is:

\[
(u,v,w)
\to
\varepsilon_m(x,y),\kappa(x,y)
\to
\begin{cases}
\text{01 UHPC backend},\\
\text{frozen Multiwave steel}
\end{cases}
\to
\delta W=0
\to
P(\lambda).
\]

The next calculation must therefore answer one narrow question:

\[
\boxed{
\text{How many membrane DOFs/basis functions are minimally required to reconstruct the FEM }\varepsilon_y^0(x)\text{ profile?}
}
\]

This is a kinematic basis audit, not a force fit and not FEM calibration of material parameters.

## 8. Do not reopen at this checkpoint

Do not reopen without new contradictory evidence:

- fixed empirical UHPC reduction factors such as 0.68/0.8;
- replacing the 01 pre-peak UHPC backbone for BH050–BH100;
- modifying Multiwave before a direct-state failure is demonstrated;
- treating a single global `epsilon0,kappa` pair as the full FEM section state;
- equating Abaqus `11/22/33` labels with physical directions without coordinate verification;
- old R4 force-to-section inversion as the preferred closure.

## 9. Immediate next step

At the physical peak mid-gauge section, collapse the 864 UHPC records per case into a widthwise membrane-strain profile by fitting the through-thickness field locally:

\[
\varepsilon_y(x,z)=\varepsilon_y^0(x)+z\kappa_y(x).
\]

Then fit \(\varepsilon_y^0(x)\) using successively enriched symmetric low-order bases that can be generated by a small set of in-plane displacement amplitudes. Compare one constant mode, one even harmonic, two even harmonics, etc., across all nine cases. Select the smallest common basis meeting an explicit reconstruction gate. The fit coefficients are diagnostic only; they must later be solved from equilibrium/generalized work, never prescribed from FEM in production.
