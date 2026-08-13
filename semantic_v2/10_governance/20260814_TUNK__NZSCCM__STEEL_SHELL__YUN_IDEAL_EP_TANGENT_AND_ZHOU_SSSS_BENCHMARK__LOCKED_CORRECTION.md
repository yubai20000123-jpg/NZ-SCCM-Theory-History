# NZ-SCCM steel-shell governance correction

Date: 2026-08-14
Status: CURRENT_PRIMARY / LOCKED GOVERNANCE CORRECTION

## Sun A5

SUN_A5_ACTIVE_BENCHMARK = NO
SUN_A5_RETAINED_HISTORY = YES
Reason: its boundary/loading system does not match the current four-edge simply-supported uniform axial-compression target. Old files remain historical diagnostics and are not deleted.

## Ideal elastic-perfectly-plastic + Yun-Lu tangent rule

Steel has no strain hardening.

1. Before local buckling and before yield: E_t,eff = E_s.
2. If elastic local buckling occurs first (sigma_cr,E < fy): activate the Yun-Lu large-deflection postbuckling branch. Before first yield, E_t,eff = d sigma_Yun / d epsilon_Yun from that current postbuckling branch.
3. At first yield and during continuing plastic loading: E_t,eff = 0 and |sigma_s| shall not exceed fy through fictitious hardening.
4. If yield occurs before elastic local buckling: E_t,eff becomes 0 at yield; do not force an elastic Yun branch ahead of yield.
5. If a previously yielded part unloads/redistributes so that |sigma_s| < fy, its physical material tangent is elastic again. If the local buckling mode is still active, the effective shell tangent remains the current elastic Yun postbuckling tangent; if the local mode is inactive, it is E_s.

The current monotonic Pu solver is not converted into a general cyclic plasticity solver by this rule.

## Event identity

B_s, Y_s, K_Z=0 and L=0 are distinct events. Local shell buckling does not terminate the global branch.

## First active benchmark

The first active benchmark shall use a real four-edge simply-supported specimen/design under uniform axial compression and satisfy sigma_cr,s^E < fy so that B_s -> Yun S1 -> Y_s can actually be exercised.

Preferred source family: Zhou Siming's four-edge simply-supported MCFSTW axial-compression parametric series. A directly tabulated FE ultimate value is preferred. If it is unavailable for the exact selected point, Zhou's source four-edge stability/design curve may be used only as an external comparator and never as an input to the NZ-SCCM solution.

## Parent theory unchanged

R10 = FROZEN
N48-C1/MM = FROZEN
NGUYEN_SECOND_ORDER = FROZEN
GENERAL_D15 = FROZEN
ONE_THEORETICAL_COMPLETE_HALFWAVE = FROZEN
FORMAL_SPATIAL_QUADRATURE = 0
STRUCTURAL_CALIBRATION = NO
