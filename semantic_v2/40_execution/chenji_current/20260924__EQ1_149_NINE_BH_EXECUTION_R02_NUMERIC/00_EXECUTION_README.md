# Eq.(1)–(149) nine-BH numerical execution — R02

Date: 2026-09-24

## Identity

The uploaded Eq.(1)–(149) formulation is kept unchanged through Eq.(149). The corrected UHPC tension input is the Abaqus stress–cracking-strain table converted to total tensile strain by eps_total = eps_ck + sigma/Ec.

Formal tensile C1 anchors used:
- ft = 7.3 MPa
- eps_tp = 9.722027649769585e-4
- ft_half = 6.632167188513625 MPa
- ft_2 = 6.487368472559167 MPa
- at = 2.1176777744062334
- bt = 4.5344984475477235
- ct = 1.6085712902696916
- dt = 0.7545532420682709

## Post-Eq.(149) closure actually used

After Eq.(149), the compatible in-plane fields are approximated by an H5 trigonometric Ritz space:
- u/b = ebar_x*xi + U_ij sin(2*pi*i*xi) cos(2*pi*j*eta), i=1..5, j=0..5
- v/b = -dbar*eta + V_ij cos(2*pi*i*xi) sin(2*pi*j*eta), i=0..5, j=1..5
- 64 algebraic unknowns: ebar_x + 30 U + 30 V + q + A+ + A-.

Weak virtual work closes in-plane equilibrium and the q/A+/A- equations. Current execution uses Gauss-Legendre quadrature only to evaluate integrals (24x24 in-plane, 12 UHPC-thickness, 10 steel-thickness per shell). These are not nodal/collocation field DOFs, but this is not the stronger fully analytic integration backend originally preferred. Reported values are therefore R02-H5 numerical roots, not exact closed-form continuous-field roots.

Stationary roots are locally refined from neighboring converged equilibrium states; all listed roots have d2P/dDelta2 < 0.

## Connectivity

BH005–BH050: stationary root lies on one continuously resolved segment.
BH060: first connected segment has a stationary maximum; later segment is separated by a continuation gap.
BH070: first connected maximum is resolved; a later maximum also exists but connectivity across the gap is not proven.
BH085/BH100: early direct-displacement continuation is lost before an early stationary maximum is resolved; only later mathematical stationary roots are reported.

Some later roots reverse the signed local amplitude relative to the initial local mode. Eq.(114)/(119) impose no unilateral sign inequality, so those are mathematical roots of the stated equations but are not automatically accepted as physical one-sided local-buckling states.

Main result: correcting the C1 tensile input removes the former material-definition blocker, but does not remove the systematic wide-specimen overprediction.
