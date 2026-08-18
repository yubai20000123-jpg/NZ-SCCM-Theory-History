# ERRATA R01 — 20260818_2135 CURRENT COMPLETE THEORY LEDGER

**Timestamp:** 2026-08-18 21:35 +08:00  
**Applies to:** `semantic_v2/20_theory/20260818_2135__NZSCCM__CURRENT_COMPLETE_THEORY_LEDGER_CASE21_Z6__LOCKED_HANDOFF.md`

This errata corrects only notation/LaTeX transcription in the first GitHub copy. It introduces **no theory change, no numerical change, and no model change**.

## Mandatory notation corrections

In Section 4.6 and Section 4.10, every occurrence displayed as

```text
\nu_R
\nu_R'
```

must be read as

```text
u_R
u_R'
```

where `u_R(t)` is the already-defined scalar tensile source function. In particular:

\[
u_R(t)=
\rho r+(10H_R-6\rho)r^3+(8\rho-15H_R)r^4+(6H_R-3\rho)r^5,
\]

for the first branch; the second/third branch and all derivatives are derivatives of this same `u_R(t)`.

In Section 13, the displayed symbol

```text
\nu_w
```

must be read as

```text
u_w
```

with

\[
u_w=\frac{E_s\varepsilon_y^w}{f_y},\qquad \chi_w=u_w^2.
\]

## Canonical interpretation

The local corrected handoff copy created in the same conversation uses `u_R` and `u_w` consistently. No released Case21 or Z6 value is affected.

**END ERRATA R01**
