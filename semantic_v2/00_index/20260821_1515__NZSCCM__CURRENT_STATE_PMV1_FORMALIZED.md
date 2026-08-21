# NZ-SCCM — CURRENT STATE: PMV1 FORMALIZED

时间：2026-08-21 15:15 +08:00

## Active structural candidate

`PMV1 = PRE-MEMBRANE MULTIPHASE VOLUME-CONSERVING THEORY V1`

Formal contract:
`semantic_v2/20_theory/20260821_1515__NZSCCM__PRE_MEMBRANE_MULTIPHASE_VOLUME_CONSERVING_THEORY_V1.md`

## Locked candidate content

- one continuous complete halfwave;
- Nguyen second-order pre-membrane kinematics;
- R10 -> N48 -> Cayley-Hamilton concrete current map;
- General-D15 exact moments;
- outer steel local ideal-EP radial-cap phase;
- MCFSTW web material phase with `rho_w=ts/ls` and concrete-volume replacement;
- RC rebar phase with `rho_s,tot=rho_sx+rho_sy` and concrete-volume replacement;
- `Rq=0`, `L=P_D Rq_q-P_q Rq_D=0`, `Pu=P(Du,qu)`;
- no empirical load correction.

## Validation result

Steel-shell Z0-Z5 after full web material phase:

- all six signed errors positive;
- mean signed = +6.898%;
- sample std = 3.798 percentage points;
- max absolute = 9.973%;
- Z6 remains out-of-current-validated-domain diagnostic.

Swartz24 phase-volume audit:

- phase-volume correction is only ~0.2-1.0% load scale;
- MAE remains ~12%;
- therefore it cannot explain specimen-to-specimen scatter and does not justify reopening membrane/Ritz.

Case21 full reclosure verifies phase-volume first-order KKT audit to ~5.5e-5% relative in Pu.

## Not yet production-locked implementation detail

The exact steel ideal-EP current law is fixed, but the material-coordinate Chebyshev compiler degree is not yet a production constant because current degree16/24/32 Z0-Z5 Pu spread is about 0.3-1.6%.

Next task, if continued: freeze steel material compiler by material-function approximation/convergence only, not by Zhou/test loads; then package PMV1 into a final hand-calculation / reference implementation ledger.
