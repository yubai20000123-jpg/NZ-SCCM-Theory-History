# NZ-SCCM — NC TC Appendix-B source correction addendum

**Date:** 2026-08-22 12:05 +08:00  
**Applies to:** `20260822_1151__NZSCCM__NC_UHPC_7GATE_EXPLICIT_MATERIAL_REORGANIZATION_V1.md`

## 0. Reason for this addendum

The 11:51 report correctly reduced Nguyen Eqs. (3.18)–(3.19) to a finite two-segment **major tensile peak** capacity relation in the tension-compression quadrant. A subsequent direct Appendix-B check shows that Nguyen's executed `stmoduc` TC route also computes the **minor compressive peak** from an additional Foster envelope branch. Therefore the 11:51 wording `NC_TC_CT_SOURCE_CAPACITY_GATE = PASS` is too broad if interpreted as the complete Appendix-B TC peak pair.

This addendum narrows the accepted identity without changing any structural calculation.

## 1. Executed Appendix-B TC peak pair

With Nguyen sign convention:

\[
\sigma_1>0,\qquad \sigma_2<0,\qquad
\alpha=\sigma_1/\sigma_2<0,
\]

Appendix-B computes the major tensile peak as

\[
\sigma_{1p}
=
\begin{cases}
\dfrac{f_c}{\alpha f_c/f_t+0.5}\,\alpha,
&\alpha\le0.75f_t/f_c,\\[3mm]
\dfrac{3f_c}{\alpha f_c/f_t+3}\,\alpha,
&\alpha>0.75f_t/f_c,
\end{cases}
\]

which is the Eqs. (3.18)–(3.19) object reduced in the 11:51 report.

But the same executed TC route also computes

\[
\boxed{
\sigma_{2p}
=
\begin{cases}
\dfrac{1-3.28\alpha}{(1-\alpha)^2}f_c,
&\alpha>-0.2,\\[3mm]
0.5375f_c,
&\alpha\le-0.2.
\end{cases}}
\]

for the minor compressive peak.

Hence the source peak pair is not exhausted by Eqs. (3.18)–(3.19) alone.

## 2. G6 status

The additional compressive-side branch is itself finite and explicit once the current stress ratio \(\alpha\) is known. Therefore it does **not** threaten G6.

However, the physical interpretation and combined admissibility rule for the pair

\[
(\sigma_{1p}(\alpha),\sigma_{2p}(\alpha))
\]

must be source-audited before declaring the complete NC TC capacity gate closed, because the two directional peak values are computed separately in Appendix-B and are then used inside the equivalent-uniaxial material update.

No new heuristic `min()` rule is introduced in this addendum.

## 3. Corrected status

```text
NC_CC_SOURCE_CAPACITY_GATE = PASS
NC_TC_EQ318_319_TENSILE_PEAK_GATE = PASS_G6
NC_TC_APPENDIXB_COMPRESSIVE_PEAK_BRANCH = RECOVERED_G6
NC_TC_COMPLETE_PEAK_PAIR_CAPACITY_INTERPRETATION = SOURCE_AUDIT_PENDING
NC_FULL_INCREMENTAL_NGUYEN = ORACLE_ONLY
```

The old project rule `c*=c(1-tau)` remains demoted from source identity.

## 4. Governance

```text
STRUCTURAL_BACKBONE_CHANGED = FALSE
STRUCTURAL_PU_RERUN = NOT_AUTHORIZED
N_material_points = 0
LOAD_PATH_TRACKING = 0
HISTORY_STATE_MACHINE = OFF_MAINLINE
```

This correction strengthens source fidelity while preserving the seven-gate explicit architecture.
