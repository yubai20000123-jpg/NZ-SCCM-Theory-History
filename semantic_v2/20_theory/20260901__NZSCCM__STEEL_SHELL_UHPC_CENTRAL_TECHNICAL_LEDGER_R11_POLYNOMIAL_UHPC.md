# SUPERSEDED — NZ-SCCM steel-shell–UHPC central ledger R11

**Date superseded:** 2026-09-01  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Production main:** unchanged

R11 introduced the current polynomial UHPC scalar section law:

```text
sixth-degree compression
+
Hiew-anchor cubic-Hermite tension
```

That material decision is retained.

R11 is superseded because it still referred to external historical markdown files for parts of the generic R02/R06 reconstruction and therefore was not a fully standalone text implementation contract.

The current complete ledger is:

`semantic_v2/20_theory/20260901__NZSCCM__STEEL_SHELL_UHPC_CENTRAL_TECHNICAL_LEDGER_R12_SELF_CONTAINED_PARAMETRIC.md`

R12 changes no accepted steel-shell mechanics. It inlines the generic R02/R06 local stress field, the finite local-Mises candidate construction, the complete R12 UHPC primitives, web integration, section closure, exact integer-mode selection, input/output contract, and anti-lookup requirements.

The original full R11 content remains recoverable from Git history before this supersession commit.

```text
R11_STATUS = SUPERSEDED_BY_R12
R11_UHPC_POLYNOMIAL_DECISION = RETAINED
CURRENT_LEDGER = R12_SELF_CONTAINED_PARAMETRIC
```