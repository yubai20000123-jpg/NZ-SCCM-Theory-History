# Swartz24 validation semantic branch

Current validation entry:

- the stored 24-row C1/MM + general-D15 load-maximum comparison is located in `semantic_v2/50_results/swartz24/`.

## 2026-08-13 16:47 control-ordering correction

The 24 stored loads are **equilibrium first-load-maximum candidates**. Governing physical capacity additionally requires the same-branch full current-tangent ordering required by the current theory contract:

```text
first KZ=0 vs first L=0, g:+->- maximum
```

Only Case21 presently has this full ordering completed. The other 23 panels remain `KZ_ORDERING_PENDING` and their stored load maxima must not be treated as certified governing capacities.

Priority evidence:

- `20260813_1647__NZSCCM__SWARTZ24__LIMIT_POINT_VS_TANGENT_LOSS_CONTROL_ORDERING__AUDIT.md`
- `20260813_1035__NZSCCM__SWARTZ24__FULL_SAME_EXPRESSION_L_KZ_BULK_GATE__EXECUTION_AUDIT.md`
- `20260811_TUNK__NZSCCM__SWARTZ24__C1_TANGENT_REPAIR_AT_DIRECT_N48_STATES__AUDIT_TABLE.csv`

For Case1, the direct-N48 load maximum was 599.515895 kN while the stored current load maximum is 608.925 kN. At the old direct-N48 state, repairing the tangent to C1 changes the Zhou-form margin from 3.5861 to 0.8317. This does not itself produce a current KZ control load, but it makes the missing same-branch KZ ordering a substantive mechanical gate rather than a bookkeeping detail.

Historical mechanism/source audits from 2026-08-11 are partially superseded because their Pu/error columns use old direct-N48 predictions. Their source-observation columns remain usable within provenance limits.

Experimental buckling/critical load and experimental failure/ultimate load must remain distinct quantities, but that distinction does not explain the Case1 +22.30% -> +24.22% load-maximum worsening addressed here.
