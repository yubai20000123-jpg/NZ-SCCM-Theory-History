# NZ-SCCM Marguerre–Airy origin recovery archive

Canonical branch: `archive/ma-origin-recovery-20260823`

This is a deliberately isolated historical recovery package. It preserves the selected source chain requested by the user and is **not** a "latest theory" branch.

## 1. Recovered scope

1. Airy literature discovery / research process and formalization.
2. First explicit trial calculations.
3. Combined reinforced-concrete + steel-shell-concrete explicit calculation stage.
4. Corrected-geometry steel-shell-UHPC stage.
5. Normal-concrete constitutive research.
6. UHPC constitutive research.

## 2. Architecture identity preserved

The recovered route is a **common mechanics architecture, not a single unified theory** across all materials/structural families:

`geometry / elastic A,D -> Marguerre–Airy theoretical structural demand -> material-/section-specific capacity constraint -> Pu`

Different RC, steel-shell-concrete, and steel-shell-UHPC cases may use different material laws, section compositions, local steel-panel modules, and multiaxial capacity relations.

What is intended to remain common is the structural-demand architecture.

## 3. Empirical-content boundary

Empirical/semi-empirical content is admissible in material constitutive or material-strength/capacity relations.

The target architecture does not rely on specimen-level empirical structural-strength reduction to replace the mechanics-derived postbuckling demand. This distinction is essential when comparing the project with Swartz-type or other semi-empirical ultimate-strength methods.

See:

- `ARCHITECTURE_POSITIONING_LOCK.md`
- `RESEARCH_OVERLAP_AUDIT_CRITERIA.md`

## 4. Material does not re-enter Airy

Nonlinear concrete/UHPC constitutive laws are terminal capacity/failure constraints; they are not inserted back into the Airy compatibility operator.

The later 2026-08-23 detour that attempted to interpret `dPpb/dq=0` as the ultimate condition, or to insert nonlinear current material into the Airy global residual, is intentionally excluded from this archive.

## 5. Historical completeness status

Machine/governance archive completeness is PASS, but file-by-file historical continuity is PARTIAL. Known gaps and intentional omissions are recorded in:

- `audit/HISTORICAL_CONTINUITY_AUDIT_20260823.md`
- `KNOWN_GAPS_AND_INTENTIONAL_OMISSIONS.md`

Do not reconstruct missing historical nodes from hindsight and relabel them as contemporaneous source files.

## 6. Payload purity

Only canonical historical payload files listed in `MANIFEST.json` are source payload. Exact duplicate blobs are represented by cross-stage references rather than duplicate physical copies where possible.

README, governance locks, overlap criteria, audits, audit programs, workflow files, and generated ZIP are support/governance material, not historical payload.

See `RECOVERY_SCOPE_LOCK.md` and `MANIFEST.json` for the binding read/provenance rules.
