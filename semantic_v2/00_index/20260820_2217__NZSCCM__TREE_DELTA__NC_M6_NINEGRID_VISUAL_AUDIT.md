# TREE DELTA — NC-M6 nine-grid visual audit

Time: 2026-08-20 22:17 +08:00

Current material node:

`NC-基准本构 (frozen) -> NC-M6 NC-M4-R12-style direct physical-principal current operator -> explicit Poisson algebraic elimination -> frozen CC/TC/CT/TT interactions -> physical stress + exact consistent tangent -> virtual-work field`.

Locked this turn:

1. `NC_M6_ARCHITECTURE_CANDIDATE = LOCKED` remains the active material candidate.
2. No Case21 solve was performed.
3. No T5 refit was performed; physical material definition remains `T_NC`; T5 is only a future analytic compilation candidate.
4. No new repair term, beta, additive Pi, or C1/C2 sector-front patch was added.
5. Nine-grid material visualization was executed using the same ordinary-concrete material scale previously used only for curve auditing (`fc=21.23 MPa`, `E0=20321 MPa`, `eps_c0=0.00209`, `nu=0.18`, `ft=0.1fc`), with no structural calibration.
6. Nine panels cover compression primitive, tensile `T_NC`, primitive tangent, exact free-uniaxial compression degeneration, TC compression family, exact free-uniaxial tension degeneration, equal-CC, equal-TT, and finite one-sided sector-front tangent traces.
7. Curve audit status: stress boundedness PASS; primitive/one-sided tangent boundedness PASS; uniaxial degeneration PASS; frozen TC/CC/TT target curves PASS; sector-front stress continuity PASS.
8. Finite sector-front tangent equality is not a physical hard gate for NC-M6. One-sided tangents are allowed to differ provided stress is continuous and both tangents remain finite.
9. `VIRTUAL_WORK_INTERFACE = READY`.

Detailed state file:

`semantic_v2/20_theory/20260820_2217__NZSCCM__NC_M6_NINEGRID_VISUAL_AUDIT_AND_STATE_LOCK.md`

Next allowed task: leave the material layer and construct the continuous structural virtual-work residual/Jacobian field. Do not reopen NC-M6 material physics unless a direct mathematical contradiction is demonstrated.