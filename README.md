# NZ-SCCM Marguerre–Airy origin recovery archive

Canonical branch: `archive/ma-origin-recovery-20260823`

This is a deliberately isolated historical recovery package. It preserves the source chain requested by the user and is not a "latest theory" branch.

## Recovered scope

1. Airy literature discovery / research process and formalization.
2. First explicit trial calculations.
3. Combined reinforced-concrete + steel-shell-concrete explicit calculation stage.
4. Corrected-geometry steel-shell-UHPC stage.
5. Normal-concrete constitutive research.
6. UHPC constitutive research.

## Architecture identity preserved

The historical Marguerre–Airy route separates two layers:

`geometry / elastic A,D -> Marguerre–Airy structural demand -> material / section capacity constraint -> Pu`

Nonlinear concrete/UHPC constitutive laws are terminal capacity/failure constraints; they are not inserted back into the Airy compatibility operator.

The later 2026-08-23 detour that attempted to interpret `dPpb/dq=0` as the ultimate condition, or to insert nonlinear current material into the Airy global residual, is intentionally excluded from this archive.

See `RECOVERY_SCOPE_LOCK.md` and `MANIFEST.json` for the binding scope and provenance rules.