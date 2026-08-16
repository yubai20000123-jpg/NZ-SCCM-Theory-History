# NZ-SCCM audit — dual-holonomic regularity / anti-loop production pivot

**Timestamp:** 2026-08-16 21:36 +08:00

## Audit checks

```text
CHECK 1: local differential equations versus displayed 4x4 matrix
RESULT : prior display error found; corrected matrix issued

CHECK 2: corrected local matrix against exact derivatives of (1,q,s,qs)
RESULT : PASS at exact rational audit fibers -1/2, 0, 1/2
NOTE   : audit fibers are algebraic identity checks, not structural quadrature

CHECK 3: denominator-gauge identity
RESULT : PASS_EXACT by direct differentiation

CHECK 4: complete-thickness global regularity of rationalized smooth basis
RESULT : FAIL_APPARENT_INTERIOR_POLE
x*     : 21/260 inside [-1,1]

CHECK 5: physical smooth atom at x*
RESULT : PASS_REGULAR
s(x*)  : 0.554201506553309739021547866043520...

CHECK 6: removable-cancellation diagnostic
RESULT : PASS_EXACT
lim(c0+c1*q) = 29577184/61042095

CHECK 7: regular denominator-gauge recurrence away from apparent poles
RESULT : PASS; audit-only relative residuals about 1e-15 for n=0..2

CHECK 8: formal spatial/thickness numerical quadrature counters
RESULT : PASS_ZERO
```

## Erratum scope

The 20:59 **equations**

```text
q'=ell*q
s'=c0*s+c1*q*s
(qs)'=c1*Q*s+(ell+c0)*q*s
```

were correct. Only the displayed matrix placement of `c1` versus `c1*Q` was wrong. Consequently the 64-state dimension and nonzero-pattern count remain valid, while future x-dependent derivative implementations must use the corrected matrix.

The 21:18 adjoint/CH fiber audit remains valid because it did not use the x-dependent derivative matrix.

## Anti-loop audit decision

Continuing the exact-algebraic production path robustly would require a regular algebraic basis or Hermite/integral-basis reduction to cancel representation-induced apparent poles before integration. That is a new symbolic backend layer.

Under the current anti-loop execution rule, that layer is not opened automatically. This is a governance stop, not a claim that such mathematics is impossible.

```text
EXACT_ALGEBRAIC_HOLONOMIC_BRANCH = RETAINED_RESEARCH_PAUSED
N48_C1_MM_GENERAL_D15 = REACTIVATED_PRODUCTION
FIVE_TERM_MEMBRANE_REDISTRIBUTION = REQUIRED
NEXT = ACTUAL CASE21 PRODUCTION CALCULATION
```

No new Pu is released in this audit.
