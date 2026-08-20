# TREE DELTA — NC-M6 architecture + constitutive gate audit

Time: 2026-08-20 22:11 +08:00

Current material mainline:

`NC-基准本构 (frozen) -> NC-M6 direct physical-strain current operator -> exact physical consistent tangent -> virtual-work interface`.

Locked:

1. `NC_M6_ARCHITECTURE_CANDIDATE = LOCKED`.
2. NC-M6 keeps NC-M4/NC-M4-R12 external form: physical strain -> physical principal strains -> explicit principal stresses -> physical rotation -> consistent tangent -> virtual work.
3. Frozen NC physics unchanged: CC `c_i*=c_i(1+a_cc c1 c2)`, TC/CT `c*=c(1-tau)`, TT `tau_i*=tau_i(1-a_t tau_j^8)`.
4. Old NC-M4 `beta=1/(1+0.15t^2)` is excluded; additive `Pi_i` is excluded.
5. Poisson coupling is an explicit algebraic elimination `epsbar_i=(eps_i+nu eps_j)/(1-nu^2)`; no new material DOF, second angle, second radical, or material Newton.
6. Physical principal-normal tangent is `A=(fc/eps_c0) J_lambda H_nu`.
7. Full engineering tangent must also include the spectral shear term `G_sp=(sigma1-sigma2)/(2(eps1-eps2))`, with the exchange-symmetric limit at repeated eigenvalues. This is exact differentiation, not a new repair term.
8. Gates passed: stress continuity, physical consistent tangent, origin plane-stress tangent, exact uniaxial degeneration, virtual-work conjugacy, full-domain stress boundedness, full one-sided tangent boundedness.
9. Finite sector-front tangent equality is no longer a physical hard gate; finite one-sided tangent + stress continuity are sufficient for the virtual-work formulation. No C1/C2 material repair is added.
10. NC-M6 branch tangent is not assumed major-symmetric; use virtual-work residual + exact Jacobian, not an unproved total-potential minimization.
11. No Case21 solve, no T5 refit, no new material repair terms.

Next allowed task:

`NC-M6 -> continuous structural virtual-work field -> generalized internal virtual work + exact Jacobian symbolic interface`.