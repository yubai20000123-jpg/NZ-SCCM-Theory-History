# TREE DELTA — NC-M4-R12 direct 2D Poisson tangent rebuild

Time: 2026-08-20 20:21 +08:00

Current node:

`R3 deleted -> restore kinematic nu*Delta/ell baseline -> direct raw-principal-strain 2D material map -> exact origin plane-stress tangent in TT/TC/CT/CC -> analytic-integration compatibility PASS`.

Locked conclusions:

1. Delete all R3 equivalent-uniaxial variables and state-grid logic.
2. Restore raw physical principal-strain material grid.
3. Restore transverse kinematic baseline `nu*Delta/ell`; `epsilon_m` is only an additional nonlinear membrane correction.
4. Enforce plane-stress Poisson coupling directly in the 2D current stress map through
   `Pi1=Knu(eps2+nu eps1)`, `Pi2=Knu(eps1+nu eps2)`, `Knu=nu E0/(1-nu^2)`.
5. Generalize the compression primitive without an empirical parameter:
   `m_c=E0 eps_c0/fc`, `C_m(c)=m_c c/[1+(m_c-2)c+c^2]`; this gives `C_m'(0)=m_c`, `C_m(1)=1`, `C_m'(1)=0`, hence exact compression initial tangent `E0`. For Case21 `m_c=2.00051295337`, almost identical to the previous `2c/(1+c^2)`.
6. All four quadrants have the exact same origin tangent `E0/(1-nu^2)[[1,nu],[nu,1]]`; engineering shear tangent is `E0/[2(1+nu)]`.
7. R2 TC softening is kept as a smooth rational candidate with symbolic `k_tc`; its old use of the T4 internal strain scale is prohibited. No min/cap front is retained at this node.
8. The half-angle/algebraic-lift/residue/relative-GKZ integration architecture remains valid; old master dimensions must be recompiled.
9. Next task: audit/choose the simplest physically acceptable `k_tc` / TC softening law under these constraints, then rewrite the full four-quadrant NC-M4-R12 operator and rerun Case21 before considering any structure-level fourth issue.
