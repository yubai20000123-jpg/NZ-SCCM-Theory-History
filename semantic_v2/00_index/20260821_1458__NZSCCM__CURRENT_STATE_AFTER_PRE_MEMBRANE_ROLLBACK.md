# NZ-SCCM — CURRENT STATE AFTER PRE-MEMBRANE ROLLBACK

时间：2026-08-21 14:58 +08:00

## Current production direction

`PRE_MEMBRANE_PARENT_BACKBONE = ACTIVE_PRODUCTION_CANDIDATE`

Common backbone:

- one continuous complete representative halfwave;
- Nguyen second-order kinematics;
- R10 material target;
- N48-C1/MM;
- Cayley-Hamilton current map;
- General-D15 exact moments;
- formal spatial sampling/quadrature = 0;
- D,q low-dimensional generalized coordinates;
- structure-family-specific steel/rebar treatment retained from the historical validated branch.

## Retired from current production path

- Ritz H2/H4/H6/H8/H10/H12/H14 order escalation;
- new membrane-redistribution field as a mandatory production layer;
- pseudo-arclength / path-tracking as production Pu definition;
- Z6-driven theory expansion.

These remain historical/research artifacts only unless the user explicitly reopens them.

## Validation status

Steel-shell:
- Z0–Z4: strong support, errors versus corrected Zhou original within about ±5%;
- Z5: conservative ~-10.24%; retained at current envelope edge;
- Z6: ~-24.49%, and clearly outside Z0–Z5 geometric/flexibility envelope; `OUT_OF_CURRENT_VALIDATED_DOMAIN_DIAGNOSTIC`.

Swartz24:
- historical blind R10/N48/D15 predictions are preserved and non-calibrated;
- mean signed error near -2.81%, but MAE ~12.06% and substantial sign-changing scatter;
- retain as experimental robustness/specimen-realization validation set; do not reopen membrane/Ritz merely to chase individual specimen errors.

## Governing audit

See:
`semantic_v2/90_audit/20260821_1458__NZSCCM__PRE_MEMBRANE_BASELINE_RECOVERY_AUDIT.md`

## Next task

No new theory expansion. If continued, only:
1. specimen-realization audit for Swartz24 independent of theory error;
2. consolidate the recovered pre-membrane candidate into one formula/calculation-process document with explicit steel-shell applicability envelope.
