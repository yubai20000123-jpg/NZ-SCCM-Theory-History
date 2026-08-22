# RECOVERY SCOPE LOCK

## Canonical source branch

`archive/ma-origin-recovery-20260823`

This branch is the exclusive source basis for the recovered Marguerre–Airy historical package unless the user explicitly authorizes another source.

## Strict read boundary

Without explicit user override, do NOT read, infer from, reconcile against, or silently import content from:

- `main`;
- any other Git branch or tag;
- repository ancestry outside the archive tree;
- File Library/project uploads not physically copied into this archive;
- later current-state or diagnostic files outside this archive.

Source commit/path references in `MANIFEST.json` are provenance metadata only. They do not authorize future reads outside this branch.

## Admitted historical architecture

`elastic/initial A,D + Marguerre–Airy structural demand -> explicit N/M resultants -> material-/section-specific failure-capacity constraint -> finite admissible-root Pu`

This is a **unified/common analytical architecture**, not a claim of one unified material theory or one identical governing formula for RC, steel-shell-concrete, and steel-shell-UHPC panels.

Different families may retain different material laws, section compositions, local steel-panel modules, and multiaxial capacity relations.

## Empirical-content boundary

Material constitutive or material-strength/capacity input may be empirical or semi-empirical.

The target structural front end is not to be replaced by specimen-level empirical structural-strength reductions, fitted effective-width rules, FE/test-calibrated postbuckling coefficients, or direct fitted Pu formulas unless the user explicitly opens a comparison branch.

Accordingly, methods with structural-level empirical simplifications are not automatically methodologically equivalent to this architecture even if they also predict postbuckling ultimate strength.

See `ARCHITECTURE_POSITIONING_LOCK.md` and `RESEARCH_OVERLAP_AUDIT_CRITERIA.md`.

## Material/Airy separation

Material nonlinearities stay in the terminal capacity/failure layer. They do not enter the Airy compatibility operator.

## Explicit exclusions

The following later detour is excluded and must not contaminate this archive:

- `20260823_0246__NZSCCM__MARGUERRE_AIRY_GLOBAL_LIMIT_GATE_PANEL21_R01`;
- `MA_V1_GLOBAL_FOLD` as a plate ultimate criterion;
- `NONLINEAR_CURRENT_MATERIAL_GLOBAL_WORK_CLOSURE_UNDER_MARGUERRE_AIRY`;
- `CURRENT_MATERIAL_PARTICIPATES_IN_GLOBAL_RESIDUAL_AND_TANGENT`;
- the commits `b04da5b2ba37eb1ea6cea172da14ae30f4a5dc8f`, `c23402098911d997a2ed0f28bf435fb9c49b851e`, and `50c1ce9db17e9d813ed8e520fe25f9286f0260eb` as theory sources.

Also excluded from the clean active recovery baseline unless separately requested:

- temporary superseded diagnostic interpretations that do not alter the final recovered architecture;
- exact duplicate copies of an already preserved historical blob;
- retrospective reconstructions presented as if they were contemporaneous historical files.

## Historical continuity

Machine/governance archive completeness and historical-continuity completeness are separate concepts.

Known missing or intentionally omitted nodes are recorded in `KNOWN_GAPS_AND_INTENTIONAL_OMISSIONS.md` and must not be silently filled from hindsight.

## Purity rule

Only files listed in `MANIFEST.json` under `payload` are historical payload. Cross-stage references may point to one canonical payload blob without creating duplicate physical files.

README, locks, overlap criteria, audit programs, audit reports, workflow, and generated ZIP are governance/support files only.

This lock remains in force until the user explicitly changes it.
