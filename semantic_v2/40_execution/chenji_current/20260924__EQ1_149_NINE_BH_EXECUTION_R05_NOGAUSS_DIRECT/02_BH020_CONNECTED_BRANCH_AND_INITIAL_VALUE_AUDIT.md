# BH020 connected-branch continuation audit

Date: 2026-09-24

## Purpose

This file records the explicit correction of the earlier BH020 large-shortening cold-start root and the subsequent zero-spatial-Gauss connected continuation.

Unknowns remain the same ten scalars:
q, Aplus, Aminus, epsx_bar, epsy_bar, ex_alpha, ey_beta, Fx, Fy, P.

No spatial Gauss points are used.

## Cold-start root versus connected root at the same target shortening

At dbar = 0.0042 (Delta = 8.4 mm):

Cold single-target start converged to the remote mathematical root:
q = 5.2129e-4,
Aplus = -0.400862 mm,
Aminus = -0.246983 mm,
P = 7.29249 MN.

This root is not on the connected path generated from the small-shortening state.

Connected continuation from the origin, using every previous converged ten-variable state as the next predictor, reaches the same dbar = 0.0042 with:
q = 3.738961115e-4,
Aplus = +1.074941069 mm,
Aminus = +1.129382116 mm,
A0+Aplus = 1.215566069 mm,
A0+Aminus = 1.270007116 mm,
P = 6.753457212 MN.

Therefore the former negative-amplitude result was a root-selection error caused by a remote cold initial guess, not evidence of a physical sign reversal on the connected branch.

## Connected continuation to the load maximum

The connected branch was continued without changing the ten governing equations.

Selected states:
dbar 0.0068: P 8.800072487 MN
dbar 0.0070: P 8.859018784 MN
dbar 0.0072: P 8.900602156 MN
dbar 0.0074: P 8.923921172 MN
dbar 0.0076: P 8.927950695 MN
dbar 0.0078: P 8.911497790 MN
dbar 0.0080: P 8.873134694 MN

The branch therefore turns between dbar = 0.0075 and 0.0076.

Direct iteration at the stationary search value dbar = 0.0075408552 gives:
Delta = 15.0817104 mm,
P = 8.928834571 MN,
q = 5.617973959e-4,
Aplus = 1.962776128 mm,
Aminus = 2.036808593 mm,
A0+Aplus = 2.103401128 mm,
A0+Aminus = 2.177433593 mm,
epsx_bar = 9.493556173e-4,
epsy_bar = -7.537000375e-3,
ex_alpha = 5.215234663e-6,
ey_beta = 8.208156872e-8,
Fx = 114145.311339,
Fy = 27943.463810,
scaled residual norm = 7.36e-14.

Neighboring directly solved states show the expected change from increasing to decreasing load.

## Wide-specimen initial-step audit

BH085 and BH100 also demonstrated the same initial-value sensitivity.

Starting directly at dbar=0.0002 failed for both. Restarting the connected path at dbar=0.00005 produced positive local amplitudes immediately:

BH085, dbar=0.00005:
P=0.379065528 MN,
q=8.239845574e-5,
A0+Aplus=0.726353075 mm,
A0+Aminus=0.740190730 mm.

BH100, dbar=0.00005:
P=0.438353125 MN,
q=1.097356358e-4,
A0+Aplus=0.874359977 mm,
A0+Aminus=0.904905378 mm.

Thus the execution rule is now strict: the first shortening increment itself must be small enough to lie in the local basin of the zero-load connected solution; it is not acceptable to use a generic finite target as the first Newton solve for the wider specimens.

## Status

These calculations are a zero-spatial-Gauss connected-branch/root-selection audit using the current analytic Fourier-polynomial residual backend. They do not change the governing ten-scalar mechanics.

The remaining formal task is to replace the current scalar constitutive polynomial expansions by the exact signed-C1 / exact current Mises regional analytic evaluation while preserving the same continuation and Newton logic.
