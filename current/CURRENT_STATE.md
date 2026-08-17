# CURRENT STATE — NZ-SCCM

**Updated:** 2026-08-17 14:07 +08:00  
**Status:** Z6 a=24000 CORRECTED / AIRY MEMBRANE REDISTRIBUTION ACTIVE / N48-FAMILY MATERIAL REBUILD CALCULATED

## Current operational entry

`semantic_v2/10_governance/20260817_1407__NZSCCM__Z6_LENGTH24000_COMPLETE_HALFWAVE_AND_N48_FAMILY_REBUILD__CORRECTION_LOCK.md`

## Critical source correction

The 13:37 `a=9000 mm` Z6 interpretation is **superseded and wrong**.

The backup Z6 production record explicitly fixes

```text
a = 24000 mm
b = 12000 mm
a/b = 2
m* = 2
ell = a/m* = 12000 mm = b
A0 = a/500 = 48 mm
q0 = .004
```

Therefore the full physical plate has two repeated halfwaves, while the formal structural domain remains one continuous complete halfwave of length `12000 mm`.

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE = ACTIVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
N_formal_thickness_quadrature = 0
```

## Membrane redistribution

Current production-direction membrane closure is

\[
r=\lambda M a(\nu),
\qquad
M=\frac{\pi^2}{\varepsilon_0}(q_0q+q^2/2),
\]

with the square-halfwave Airy direction

```text
a(.18)=[-.295,-.205,+.25,-.205,+.25]
```

and branch equations

```text
Rq_base = 0
RA = a^T Rm = 0
```

Neither `r=0` nor the five fully independent membrane amplitudes is the current production closure. The historical free-five direct-R10 value `43.76284 MN` remains diagnostic history and is not the current Z6 prediction.

## Corrected Z6 direct mechanics

Full phases are active before solving:

```text
effective R10 concrete = .98 core
face steel plates = two local ideal-EP radial-cap phases
longitudinal web/PBL phase = rho_w=.02
```

High-resolution raw-R10 Airy branch peak:

```text
D ~= 1.36180798
q ~= 0.026485404
lambda_Airy ~= 0.786915819
P ~= 48.4061215 MN
Pc_eff ~= 22.8171044 MN
Ps_face ~= 18.5564373 MN
Pw ~= 7.0325797 MN
material lambda range ~= [-1.66417,+1.35392]
face VM/fy max ~= 1.9474
```

Thus the corrected mechanics oracle is

\[
\boxed{P_u^{raw\ R10}\approx48.41\ \mathrm{MN}.}
\]

The same-evaluator old `r=0` peak was about `51.48054 MN`; the constrained Airy redistribution therefore lowers the peak by about `5.97%`, not by the roughly 15% produced by the over-released free-five branch.

## N48-family material rebuild

N48 is retained as the source-compiler prototype/refinement quantum rather than copied once over an excessively broad domain.

Current source interval:

```text
[-1.75,+1.45]
```

Current convergence family:

```text
N=48,96,144,192,240,288
```

All `U,C,T,T7` material representations retain the frozen R10 source and C1 origin constraints. No Zhou/Winter value enters coefficient generation or order selection.

Common-resolution capacity convergence versus the same raw-R10 evaluator:

```text
N48  : 48.96003 MN  (+1.0743%)
N96  : 48.60848 MN  (+0.3485%)
N144 : 48.50931 MN  (+0.1438%)
N192 : 48.46889 MN  (+0.0603%)
N240 : 48.46413 MN  (+0.0505%)
N288 : 48.45880 MN  (+0.0395%)
```

Higher-resolution gate:

```text
raw R10 = 48.40515087 MN
N192    = 48.42896188 MN  (+0.0492%)
N240    = 48.42159977 MN  (+0.0340%)
N288    = 48.41599214 MN  (+0.0224%)
```

Representative N240 state:

```text
D = 1.36084551
q = 0.0264712930
lambda_Airy = 0.786756642
P = 48.4215998 MN
Pc_eff = 22.8331231 MN
Ps_face = 18.5563166 MN
Pw = 7.0321601 MN
material lambda range = [-1.66254,+1.35182]
```

Current corrected engineering result:

\[
\boxed{P_u(Z6,a=24000)\approx48.42\ \mathrm{MN}.}
\]

## Comparator — post solve only

```text
Pcr_AR2 = 39.2880147150 MN
Zhou Eq.(5-87)/(5-88) = 49.4867667519 MN
Winter = 50.1858541295 MN
```

Using the N240 engineering value:

```text
vs Zhou ~= -2.15%
vs Winter ~= -3.52%
```

These comparators did not participate in the solve.

## Formal exact-moment identity

Every finite N48-family member remains a finite source polynomial. After 2x2 Cayley-Hamilton lifting, each retained term has finite General-D15 exact structural moments. The direct-continuum grids used above remain **audit-only** and are not promoted to formal spatial quadrature.

The high-block N192-N288 exact-D15 contraction has not yet been separately promoted as a formal runtime result; therefore the current `48.42 MN` is the corrected engineering material-compiler/mechanics result, not falsely labelled as a completed high-block formal certificate.

## Current artifacts

- `semantic_v2/10_governance/20260817_1407__NZSCCM__Z6_LENGTH24000_COMPLETE_HALFWAVE_AND_N48_FAMILY_REBUILD__CORRECTION_LOCK.md`
- `semantic_v2/20_theory/nc_steel_shell_panel/20260817_1407__NZSCCM__Z6_N48_FAMILY_SOURCE_COMPILER_AND_AIRY_MEMBRANE_REDIStribution__THEORY.md`
- `semantic_v2/40_execution/steel_shell/20260817_1407__NZSCCM__Z6_A24000_AIRY_N48_FAMILY_REBUILD_AND_CAPACITY__EXECUTION_REPORT.md`
- `semantic_v2/40_execution/steel_shell/20260817_1407__NZSCCM__Z6_A24000_AIRY_N48_FAMILY__PARAMS_AND_INTERMEDIATES.json`

## Current next implementation step

```text
HIGH_BLOCK_N48_FAMILY -> 2x2 CH -> TARGET_FIRST_GENERAL_D15 EXACT CONTRACTION
```

This is an implementation promotion of the already selected material/physical path; it is not a new mechanics route and must not reopen the 9000-mm geometry or free-five membrane model.
