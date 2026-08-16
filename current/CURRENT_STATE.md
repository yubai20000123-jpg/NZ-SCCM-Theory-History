# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-17 00:02 +08:00  
**Status:** LEGACY MUTABLE POINTER ONLY

## Current operational entry

`semantic_v2/00_index/20260817_0002__NZSCCM__PROJECT__CURRENT_STATE_MEMBRANE_HISTORY_RECOVERED_DOWNSHIFT_RETRACTED__SEMANTIC_INDEX.md`

## Frozen backbone

```text
UNIFIED_PRODUCTION_WORKFLOW_V1=ACTIVE
ONE_CONTINUOUS_COMPLETE_HALFWAVE=ACTIVE
Nguyen second-order continuous kinematics=ACTIVE
R10=FROZEN
General-D15 exact structural moments=ACTIVE
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
N_formal_thickness_quadrature=0
```

## Membrane-history correction

The 2026-08-16 23:50 state that interpreted Case21/Z6 capacity reductions as physical membrane-redistribution behavior is superseded.

Recovered higher-priority project evidence establishes:

```text
CLASSICAL_FVK_MEMBRANE_POSTBUCKLING_SIGN = POSITIVE
EDGEWARD_AXIAL_STRESS_REDISTRIBUTION = REQUIRED
p20,p02 INDEPENDENT FREE RELAXATION = RETIRED
FIVE_TERM_ELASTIC_AIRY_LIMIT = EXACT / RETAINED
UNCONSTRAINED_NONLINEAR_FIVE_COORDINATE_CONDENSATION = REOPENED
```

The exact classical one-halfwave relation contains a positive membrane term proportional to `A^2+2*A0*A`; the postbuckling load is increasing in the elastic degeneration.

## Recovered scale hierarchy

At historical frozen reference states:

```text
Case21:
M=.02869338081
(M/4)/D=.00858140 = .85814%

Z6:
M=1.69487261562
(M/4)/D=.26727511 = 26.7275%

M_Z6/M_Case21=59.0684
```

Therefore the recovered project expectation is:

```text
CASE21_MEMBRANE_REDISTRIBUTION = SMALL PERTURBATION
Z6_MEMBRANE_REDISTRIBUTION = FIRST-ORDER / STRONG EFFECT
HIGH b/t MEMBRANE EFFECT > LOW b/t MEMBRANE EFFECT
```

This is a physics/source constraint, not a calibration target.

## Retracted recent membrane Pu interpretations

```text
Case21 five-free-coordinate 320.749185 kN
= RETRACTED_AS_PHYSICAL_MEMBRANE_Pu
= OVERRELAXATION_DIAGNOSTIC_ONLY

Z6 direct-R10 five-free-coordinate 43.762840 MN
= RETRACTED_AS_PHYSICAL_MEMBRANE_Pu
= OVERRELAXATION_DIAGNOSTIC_ONLY
```

These values remain preserved as implementation-error evidence but must not be used to argue that correct membrane redistribution lowers capacity.

## Retained support baselines pending corrected closure

```text
Case21 historical/current-support closure = 368.189 kN
Z6 retained engineering baseline = 51.30 MN
NEW_CORRECTED_MEMBRANE_REDISTRIBUTED_Pu = NOT RELEASED
```

## Current error hypothesis

The five-term displacement/strain basis itself is retained because its linear-elastic condensation exactly recovers the Airy/FvK redistribution.

The reopened element is the nonlinear promotion in which all five amplitudes were solved as unrestricted current-material `Rm=0` internal relaxation coordinates. The recent Case21 solution moved far outside the small classical leading-direction scale and produced sign reversals/large amplification in several coordinates, indicating over-relaxation or loss of compatibility/boundary/external-work coupling.

## Anti-loop / anti-calibration rule

```text
DO_NOT_REOPEN_R10=YES
DO_NOT_TUNE_R10_TO_RECOVER_CAPACITY=YES
DO_NOT_FIT_MEMBRANE_AMPLITUDES_TO_CASE21_OR_Z6=YES
DO_NOT_REINTERPRET_RECENT_DOWNSHIFT_AS_NEW_PHYSICS=YES
DO_NOT_START_ANOTHER_UNBOUNDED_SYMBOLIC_BACKEND_LOOP=YES
DO_NOT_COMPUTE_NEW_MEMBRANE_Pu_BEFORE_CLOSURE_RECOVERY=YES
```

## Current unique next gate

`RECOVER_COMPATIBILITY_COUPLED_CURRENT_MEMBRANE_CLOSURE_FROM_1848_1912_TRANSITION`

Trace the exact transition from the 18:48 historical-backbone + compatibility-coupled membrane delta to the 19:12 five-term current-material condensation and later runtime. Determine exactly where the classical coupling / boundary work / admissibility constraints were lost, while retaining the five-term basis and the low-dimensional `(D,q)` outer topology.

Acceptance requires:

1. exact elastic Airy/FvK degeneration;
2. positive classical postbuckling stiffness;
3. correct edgeward axial stress redistribution;
4. no arbitrary independent free harmonic relaxation;
5. Case21 correction commensurate with its small membrane-driver scale;
6. Z6/high-b/t effect much stronger than Case21/low-b/t;
7. zero formal structural spatial/thickness numerical integration.

## Current key artifacts

- `semantic_v2/00_index/20260817_0002__NZSCCM__PROJECT__CURRENT_STATE_MEMBRANE_HISTORY_RECOVERED_DOWNSHIFT_RETRACTED__SEMANTIC_INDEX.md`
- `semantic_v2/60_validation/common/20260817_0002__NZSCCM__MEMBRANE_HISTORY_RECOVERY_AND_DOWNSHIFT_RETRACTION__AUDIT.md`
- `semantic_v2/10_governance/20260817_0002__NZSCCM__POSITIVE_MEMBRANE_POSTBUCKLING_SIGN_AND_SCALE_RECOVERY__LOCK.md`
- historical controlling evidence: `20260815_2358`, `20260816_0007`, `20260816_0016`, `20260816_1848`, `20260816_1912` membrane records.
