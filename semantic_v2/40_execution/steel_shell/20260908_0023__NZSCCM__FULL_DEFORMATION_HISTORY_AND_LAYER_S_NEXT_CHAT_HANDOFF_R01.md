# NZ-SCCM / UCFT NEXT CHAT HANDOFF R01

Timestamp: 2026-09-08 00:23 +08:00
Branch: diagnostic/bh032-bh050-mode-projection-20260827

## 1. Current highest priority
The project goal is now explicitly split into two layers:

- Layer-S: find the correct critical / ultimate state and critical deformation mechanism.
- Layer-C: once that state is fixed, use a separate physically sourced capacity operator to recover Pu.

The same reduced operator no longer has to produce both the correct state and the exact Pu. Layer-C must never be allowed to feed back and alter the Layer-S state.

The user also relaxes the limit-state requirement: strict K=0, negative stiffness, or dP/dlambda=0 is no longer mandatory. A residual-stiffness engineering surrogate such as K/K0=0.1~0.2 is acceptable in principle, but any threshold must be validated across specimens and must not be back-fitted to FEM Pu.

The immediate task is therefore NOT to guess another shape function. It is to read the COMPLETE FEM deformation history of all nine ODBs, from Frame 0 to the FINAL frame, including all post-peak frames, and let the actual deformation evolution reveal the minimum kinematic family and the critical-state event.

## 2. Nine specimens
BH005 b=250 Pu=2.297254 MN
BH010 b=500 Pu=4.330169 MN
BH020 b=1000 Pu=7.908734 MN
BH032 b=1600 Pu=10.884984 MN
BH050 b=2500 Pu=12.572657 MN
BH060 b=3000 Pu=13.090110 MN
BH070 b=3500 Pu=13.194333 MN
BH085 b=4250 Pu=14.163914 MN
BH100 b=5000 Pu=15.454080 MN

All have a=2b, m=2, representative half-wave length b, q0=0.0025. Current ODB family commonly uses *_EXPLICIT_R02_GRID_B400.odb and loading step EXPLICIT_LOADING. Formal ODB paths, RP definitions, shell sets and load extraction must be recovered from existing GitHub provenance / scripts before extraction.

## 3. Important kinematic corrections already established
Correct mid-surface strains:

eps_x0 = u_x + 0.5*(W_x^2-w0_x^2)
eps_y0 = v_y + 0.5*(W_y^2-w0_y^2)
gamma_xy0 = u_y+v_x+W_x*W_y-w0_x*w0_y

Added curvatures:
kappa_x=-w_xx, kappa_y=-w_yy, kappa_xy=-2w_xy.

A previous center-preserving candidate was:
w=b*q*sinX*sinY*(1+lambda*cos^2Y)
which is exactly
w/b=q11*sinX*sinY+q13*sinX*sin3Y,
with q=q11-q13 and lambda=4*q13/(q11-q13).

Critical provenance correction: the historic q_FEM is essentially the single sinX sinY coefficient q11. Historic kappa_y_U2_FEM satisfies pi^2*q11/b to machine precision, so it is NOT an independent geometric curvature and must never again be used together with q11 to identify a shape parameter.

## 4. Direct capacity test results
Using the existing 01 UHPC + Multiwave R02/R06 + web backend, the following kinematics were directly tested: original M1, M1+free shape p, minimal p+U20+Vpoly, fixed parabolic w, and fixed flat-top quartic w.

No tested candidate produced an internal peak before the current UHPC compression-domain boundary. Representative last-admissible loads (not true Pu):

BH020 FEM 7.9087; M1 9.1030; free-p 9.0926; minimal 9.0981 MN.
BH060 FEM 13.0901; M1 16.5845; free-p 15.9217; minimal 15.8365 ng3 / 15.7943 ng4 MN.
BH100 FEM 15.4541; M1 26.7534; free-p 24.5965; minimal 21.8145 MN.

BH100 minimal-cover force sharing was almost identical to FEM (theory ~66.96/31.45/1.59%, FEM ~66.89/31.26/1.85% for UHPC/steel/web), but the total load was still far too high. Key conclusion: correct force sharing can exist on the wrong stable equilibrium branch.

## 5. Second-variation / tangent audit
For a=[lambda,epsbar_x,q,p,U,V], the current reduced tangent remained strongly positive near FEM Pu:

BH020: theory P~7.8687 vs FEM7.9087, min eig(H6)~+4.68e4, dP/dlambda~+1.83e3 MN.
BH060: theory P~13.1684 vs FEM13.0901, min eig(H6)~+7.12e3, dP/dlambda~+3.94e3 MN.
BH100: theory P~15.2281 vs FEM15.4541, min eig(H6)~+6.31e3, dP/dlambda~+7.0e3 MN.

Therefore the current reduced subspace genuinely does not contain the desired limit point. This is not merely a Newton/root-finding failure.

## 6. Full-half-wave critical disturbance probe
The disturbance search was expanded from quarter-domain / center-even kinematics to a complete representative half-wave 0<=X<=pi, 0<=Y<=pi with low-order Fourier w/u/v disturbances.

BH060 and BH100 independently selected the same dominant missing soft direction:

delta w_cr ~ sinX*sin2Y.

BH100 near FEM Pu (ng7), normalized approximately:
dw/b ~ sinX*sin2Y + 0.074*sin3X*sin2Y,
dv/b ~ -0.052*sinX*sinY -0.026*cos2X*sinY + ...,
du/b ~ -0.012*sin2X*cosY + ... .

This mode is longitudinal-center antisymmetric. It is not merely flattening/sharpening; it permits peak migration, half-wave internal redistribution and center-symmetry breaking. Thus the old quarter-domain / center-even assumption structurally deleted an entire possible limit-state channel.

BH100 showed substantial softening along this mode, but ng6/ng7 did not reach zero before the material boundary. An apparent ng5 zero crossing around 17.4~17.9 MN disappeared at ng6/ng7 and is formally rejected as a false instability.

## 7. Residual stiffness surrogate
For r: dw/b=sinX*sin2Y, define the statically condensed channel stiffness:
K_r,eff=K_rr-K_rz*K_zz^{-1}*K_zr,
eta_K=K_r,eff/K_r,eff,0.

Results near FEM Pu / at last admissible state:
BH020: eta~0.384 / 0.263; does not reach 0.20.
BH060: eta~0.307 / 0.291; does not reach 0.20.
BH100: eta~0.300 / 0.158; reaches 0.20 but not 0.10.

BH100 eta=0.20 occurred at ~19.5446 MN, still +26.47% above FEM Pu, with q still high and c1x still the wrong sign. Therefore a residual-stiffness threshold is a reasonable stopping rule but is not a correction for an incorrect current stiffness operator. The fact that BH060/BH100 are both ~0.30 near FEM Pu is only an observation; do NOT back-fit eta_c=0.30.

## 8. Next execution: full deformation history, not peak-frame extraction
The user now requires all nine ODBs to be read from calculation start to calculation end. Pu is only an event label and must never be the extraction stop.

Use a two-track extraction:

A. EVERY frame: cheap scalar history
- frame/time
- axial load
- end shortening / RP displacement
- P/Pu and pre/post-peak label
- ALLIE, ALLKE, ALLAE, ETOTAL, ALLWK if available
- ALLKE/ALLIE
- secant and tangent stiffness from the full P-Delta history
- normalized tangent stiffness

B. Full spatial snapshots: every 20 frames PLUS the union of event frames
- Frame0
- every 20th frame
- ascending first crossings 0.1Pu...1.0Pu
- Pmax frame
- descending post-peak crossings 0.9Pu...0.1Pu
- local load peaks/valleys
- maximum out-of-plane displacement
- maximum peak migration
- suspected mode-switch / symmetry-breaking frames
- final frame

If a model has fewer than ~300 frames, full spatial extraction for every frame is acceptable.

## 9. Mandatory deformation analysis
Do not compress the field to one q at the beginning. Save coordinates, U1/U2/U3, paired shell-face U2 mean and rigid-plane-removed w.

Analyze BOTH half-waves of the full a=2b specimen. Do not enforce quarter-domain or w(X,pi-Y)=w(X,Y).

Perform both:
1. simultaneous Fourier least-squares, at least sin(mX)sin(nY), m,n=1..5 (expand to 7 if necessary), explicitly storing q11,q12,q13,q31,q32,q33 plus R2/RMS/unexplained energy;
2. POD/SVD for each specimen, all specimens jointly, pre-peak, post-peak and near-Pu snapshots.

Perform parity decomposition about X=pi/2,Y=pi/2 into EE/EO/OE/OO energy. Track especially the longitudinal-center-antisymmetric channel containing sinX*sin2Y.

Track peak location and peak_shift=Y_peak/pi-0.5 and compare it with q12 growth.

Compute geometric kappa_x/kappa_y/kappa_xy independently from the actual w field using local polynomial/spline/least-squares Hessian with neighborhood/order sensitivity checks. Never synthesize independent curvature from q11.

Recover the historical c0x/c1x/c0y/c1y protocol from GitHub before use. If provenance cannot be recovered, define a NEW_DIAGNOSTIC_PROTOCOL explicitly. Remember centered-width phase: cos(2*pi*x_c/B)=-cos2X.

Analyze u/v redistribution as well as w; use POD if necessary.

## 10. Limit-state discovery, not threshold fitting
For every specimen track possible state indicators through the ENTIRE history:
Pmax, Ktan/K0, q12/q11, EO energy ratio, peak_shift, dq12/dDelta, dEO/dDelta, curvature/deflection ratios, c1x/c1y changes, POD amplitudes, dynamic energy ratio, residual after a symmetric basis.

For each indicator identify onset, rapid-growth point, value at Pu, and post-Pu continuation.

Any proposed threshold must be tested across all nine specimens with leave-one-out cross-validation. Do not fit a universal threshold directly to all FEM Pu values.

## 11. Required final workbook
Create:
NZSCCM_NINE_SPECIMEN_FULL_DEFORMATION_HISTORY_R01.xlsx

Minimum sheets:
00_README
01_SOURCE_LEDGER
02_ODB_INDEX
03_FRAME_INDEX
04_MASTER_HISTORY
05_LIMIT_SUMMARY
06_MODAL_COEFFICIENTS
07_PARITY_ENERGY
08_PEAK_MIGRATION
09_CURVATURE
10_STRAIN_HARMONICS
11_STIFFNESS
12_POD_SUMMARY
13_CHANGE_POINTS
14_LIMIT_CRITERIA_CV
15_KINEMATIC_RECOMMENDATION

Also create BH005_HISTORY.csv ... BH100_HISTORY.csv.

## 12. Questions the next report must answer
1. How does the real FEM deformation mode evolve from Frame0 to the final frame?
2. Is the early mode essentially sinX*sinY?
3. When does sinX*sin2Y actually appear and grow?
4. What happens near Pu: flatten/sharpen, peak migration, half-wave competition, symmetry breaking, material localization, or a combination?
5. What is the real role of sinX*sin3Y?
6. How much FEM deformation energy was lost by quarter-domain / center-even assumptions?
7. How many analytic modes explain 95% / 99% of the pre-Pu w field?
8. How many u/v coordinates are needed for c0/c1?
9. Is there a common state indicator at Pu across the nine specimens?
10. What is the most defensible Layer-S limit-state criterion?
11. Do small-BH and large-BH specimens require different branches?
12. If rebuilding the kinematics, what is the minimum function family and why does each basis function exist?

## 13. Do not reopen these loops
Do NOT:
- keep guessing more center-even w functions to hit Pu;
- use FEM peak q as a state equation input;
- call pi^2*q11/b an independent FEM curvature;
- return to quarter-domain-only analysis;
- declare eta_c=0.30 because BH060/BH100 happen to be near it;
- use the rejected ng5 false zero crossing;
- stop ODB reading at Pu;
- analyze only peak frames;
- hide post-peak evolution;
- treat a numerical POD mode as the final theoretical shape function;
- alter fixed coefficients to match Pu.

## 14. New-chat entry
Read this handoff first. Do not reopen the old current-operator / center-even shape-function loop. Continue directly with the nine-ODB Frame0-to-final full-deformation-history extraction and the Fourier + POD + parity + peak-migration + independent-curvature + c0/c1/u/v + stiffness + change-point + leave-one-out analysis. The target is the minimum physically justified kinematic family and Layer-S critical state; exact Pu recovery can be handled later by Layer-C.
