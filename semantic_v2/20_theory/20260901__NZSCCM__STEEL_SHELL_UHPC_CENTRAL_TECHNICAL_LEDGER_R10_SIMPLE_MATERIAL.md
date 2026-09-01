# DEPRECATED — NZ-SCCM 钢壳–UHPC 集中技术总账 R10 SIMPLE MATERIAL

**Date deprecated:** 2026-09-01  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Production main:** unchanged  
**Original full-content blob:** `b76031f004765b25a80c24acc80a3c3442781a61`

R10 is retained only as historical evidence of an over-simplification experiment.

## Why deprecated

R10 replaced UHPC by:

```text
compression: linear elastic -> constant -fc plateau
tension: zero
```

This removed too much of the available source-supported UHPC nonlinearity. The structural Airy/R02/R04/R06/web/section chain itself is not rejected by this tombstone.

The objection is specifically:

```text
R10_UHPC_EP_COMPRESSION = RETIRED
R10_UHPC_ZERO_TENSION   = RETIRED
```

The separately defined steel-face/web ideal elastic-perfectly-plastic law is not revoked by this UHPC correction.

## Current replacement

Use:

`20260901__NZSCCM__STEEL_SHELL_UHPC_CENTRAL_TECHNICAL_LEDGER_R11_POLYNOMIAL_UHPC.md`

R11 retains the structural chain but replaces the UHPC law by:

```text
compression:
  sixth-degree source-anchored polynomial
  sigma/fc = -[Ac*xi + (6-5Ac)*xi^5 + (4Ac-5)*xi^6]
  Ac = Ec*eps_c0/fc
  0 <= xi <= 1

tension:
  Hiew 2%-fibre source anchors
  -> deterministic finite cubic-Hermite polynomial pieces
```

with exact polynomial thickness primitives and no material special functions in the active scalar section operator.

```text
R10_FORMAL_STATUS = DEPRECATED_OVERSIMPLIFIED_UHPC_MATERIAL
CURRENT_TRANSFER_BASELINE = R11_POLYNOMIAL_UHPC
```
