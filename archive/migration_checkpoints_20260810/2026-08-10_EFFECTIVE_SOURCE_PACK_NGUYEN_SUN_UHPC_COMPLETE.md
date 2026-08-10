# Checkpoint — effective-source package: Nguyen / Sun Lipeng / UHPC core

**Date:** 2026-08-10

## Policy active

Full-text migration is no longer the objective. New primary-source work follows `EFFECTIVE_SOURCE_EXCERPT_POLICY.md`: preserve only theory/material-critical equations, data, context and provenance, while retaining the authoritative PDF identity/locator.

Existing full mirrors remain in the repository and are not deleted.

## Completed in this selective batch

### Nguyen Appendix B — program provenance

`evidence/effective_excerpts/Nguyen_AppendixB/`

Archived source regions:

- concrete stability/material interface (`stab_conc`);
- CC/TC/TT/U state-modulus routines and secant/tangent helpers;
- reinforcement stability stress/tangent routine;
- stiffness + geometric/stability matrix assembly.

Purpose: preserve exact historical source mechanics needed to audit current transformations.

Boundary: these excerpts do not re-authorize Gauss/material points/history-machine FE as the formal NZ-SCCM production operator.

### Sun Lipeng — steel-shell/PBL mechanics

`evidence/effective_excerpts/Sun_Lipeng_PBL_shell/`

Archived:

- unilateral plate, four-edge-fixed idealization, elastic k=10.67 source, Bleich tangent-modulus and Ramberg–Osgood elastoplastic buckling;
- PBL-stiffened global-vs-subpanel mode mechanics, continuous-support historical derivation and limiting PBL relative stiffness;
- effective-area postbuckling source + Chapter-3 conclusions.

Boundary: retain mechanics and strong-boundary evidence; do not automatically revive explicit PBL spring energy, preclassification or historical effective-area formula as the current formal operator.

### UHPC core primary-source package

`evidence/effective_excerpts/UHPC_core_sources/`

Archived selective evidence notes for:

- Hiew 2024 — direct tension, including measured Table-6 2%-fibre parameters and Table-7 model/Eq.(17) parameters for SL-2.0, HL-2.0 and SL-HL-2.0;
- Liu 2024 — CC/TT/sequential-TC/proportional-TC strength and loading-path effects;
- Lee 2017 — independent 30-panel TC softening/tension-stiffening validation;
- Leutbecher 2020 — TC compressive-strength and stiffness reduction;
- Leutbecher Data S1 — primary specimen-level numerical-data locator;
- Shen 2020 — equi-biaial tensile strength/elastic-limit/hardening-strain evidence;
- Diab & Ferche 2026 — cross-study compression-softening synthesis;
- FHWA-HRT-23-077 — official UHPC material/design qualification terminology and parameter ranges.

A dedicated `TC_AND_MULTIAXIAL_CLOSURE_BOUNDARY.md` prevents these sources from being misrepresented as a uniquely closed general 2D/3D constitutive operator.

## Hiew 2%-fibre evidence now frozen in GitHub

### Experimental Table 6 means

- SL-2.0: Et 47.8 GPa; ft,el 9.6 MPa; ft,cr 9.8 MPa; eps_cr 0.041%; ft,peak 11.6 MPa at 0.386%; ft,loc 9.9 MPa at 0.619%; eps_lim 0.752%.
- HL-2.0: Et 48.9 GPa; ft,el 10.1 MPa; ft,cr 10.3 MPa; eps_cr 0.040%; ft,peak 11.4 MPa at 0.664%; ft,loc 10.8 MPa at 0.855%; eps_lim 0.990%.
- SL-HL-2.0: Et 48.2 GPa; ft,el 9.3 MPa; ft,cr 10.2 MPa; eps_cr 0.041%; ft,peak 11.2 MPa at 0.374%; ft,loc 10.6 MPa at 0.675%; eps_lim 0.741%.

### Constitutive Table 7

- SL-2.0: C1=0.289, C2=0.456, Eq.(17) fit R2=0.979.
- HL-2.0: C1=-1.092, C2=0.401, R2=0.987.
- SL-HL-2.0: C1=0.326, C2=0.403, R2=0.976.

This makes explicit that a generic label “2% steel-fibre UHPC” does not uniquely determine the tensile branch; fibre geometry/hybridisation materially affects strain capacity and post-peak response.

## Evidence migration status after this checkpoint

### Sufficiently preserved for new-conversation recovery

- current governance and current-state files;
- original-history locators / core recovery reports / decision ledgers;
- NC Nguyen material/stability/second-order theory plus Appendix-B source-program excerpts;
- Case21 current and historical analytical-route evidence;
- UHPC uniaxial tension, TT, TC, planar strength and triaxial/failure qualification evidence;
- Y/steel-shell source mechanics from Yun, Zhang Ning and Sun Lipeng;
- key UCFT historical Path-A/v5/Layer-0 provenance.

### Remaining optional strengthening, not a migration blocker

1. identify/recover the exact original publication behind the historical project label `Zhang 2023` UHPC compression law, if accessible; current project formula/register provenance is already preserved but the primary-paper identity can be strengthened;
2. when actual parameter identification is reopened, extract the complete Leutbecher Data-S1 31-record numeric matrix rather than merely the current locator/examples;
3. add exact page-level/formula-level excerpts from other primary papers only when a new theory decision depends on them;
4. byte-exact PDF/ZIP binary copies remain pending until a proper binary git/upload channel is available.

## Stop condition

The GitHub recovery system no longer needs bulk document migration before theory work can continue.

From this checkpoint onward, source archival should be **demand-driven**: when a derivation/material/operator decision requires a source, add the relevant evidence excerpt and provenance in the same research checkpoint.

`CORE_PROJECT_RECOVERY_ARCHIVE = SUFFICIENT_FOR_CONTINUATION`

`BULK_FULLTEXT_MIGRATION = STOPPED`

`FUTURE_SOURCE_ARCHIVAL = DEMAND_DRIVEN_EFFECTIVE_EXCERPTS`
