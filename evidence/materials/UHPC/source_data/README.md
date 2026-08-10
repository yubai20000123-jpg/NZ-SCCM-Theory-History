# UHPC source-data provenance

This directory contains **source locators and historical extracted datasets**, not the authoritative PDF originals and not a frozen production constitutive model.

Evidence order:

`original PDF > mechanically/reproducibly extracted source table > source-role ledger > project interpretation > historical fitted/current operator`.

## Historical G12 extracted datasets

The following small CSV files were recovered from the original 2026-08-07 G12 execution trail and are archived here without silently converting them into current model parameters:

- `G12_source_Hiew_2pct_summary.csv`
- `G12_source_Leutbecher_key_MRC2_biaxial.csv`
- `G12_source_Liu2024_sequential_TC.csv`
- `G12_source_Diab_beta_table.csv`
- `G12_SOURCE_ROLE_LEDGER_RECOVERED.csv`

The corresponding PDF/File-Library identities are recorded in `PRIMARY_SOURCE_LOCATOR_20260810.md`.

## Critical modelling boundaries

1. **Hiew 2024** rows are direct-tension source anchors. They do not permanently freeze project `Ec`, `ft`, peak strain, localization strain or tensile limit.
2. **Liu 2024 sequential TC** rows are loading-path-dependent evidence. They must not be imposed as exact pointwise constraints on a path-independent current-state map without an explicit modelling decision.
3. **Leutbecher** rows are external TC strength/stiffness validation data from a different specimen/material setup.
4. **Diab/Ferche beta** is a historical synthesis-oracle table. Its use in a later smooth current operator is a modelling choice, not an original experimental constitutive identity.
5. The historical `G12_source_Liu2024_peak_coordinates.csv` is **not archived yet** because only partial rows have been recovered in the current session. No incomplete reconstruction will be presented as the original file.

## Current UHPC parameter governance

Only the user-required project compressive strength `fc = 141.1 MPa` is mandatory. Previously paired `Ec`, `eps_c0`, `ft`, `nu` values are not immutable and may be replaced when the selected UHPC constitutive framework/source chain requires it.
