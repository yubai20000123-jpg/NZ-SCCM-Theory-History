# TREE DELTA — NC-M4-R123 full material contract

Time: 2026-08-20 19:58 +08:00

Current node:

`NC-M4 -> R1 tensile-scale separation -> R2 Nguyen-type cracked-TC compression softening -> R3 explicit equivalent-uniaxial Poisson coupling -> full CC/TC/CT/TT material contract -> tangent + analytic compatibility + contradiction audit`.

Locked in this draft:

1. `ft=0.1fc` when tensile strength is absent; `eps_cr=ft/E0`; `eps_t0=0.0967635 ft/E0` only for the T4 initial-tangent rule.
2. Old `beta=1/(1+0.15 t^2)` is deleted from R123.
3. R2 uses `gamma_c=1` for `epshat_t/epsc0<=10/17`, otherwise `1/(0.8+0.34 epshat_t/epsc0)`.
4. R3 uses explicit constant-dilation equivalent strains `epshat1=(eps1+nu eps2)/(1-nu^2)`, `epshat2=(eps2+nu eps1)/(1-nu^2)`; no local material Newton is introduced.
5. To maintain exactly four explicit material cells without hidden subfronts, this draft defines CC/TC/CT/TT by the signs of `(epshat1,epshat2)`, while raw `(eps1,eps2)` remain physical principal strains/directions. Retaining raw-sign cell governance would force additional `epshat_i=0` internal fronts.
6. Full principal tangent, equivalent-to-physical tangent transform, and spectral rotation derivatives are explicit.
7. Analytic integration architecture survives: no second radical, all branch laws remain rational in the same algebraic field; only a new source-derived `gamma_c` front is added. Old `99x155` master size is not assumed unchanged.
8. Open items not repaired by R1-R3: T4 reaches peak `ft` at about `0.152 eps_cr`; full Nguyen state-dependent dilation is simplified to constant `nu`; separate cracked shear-retention modulus is still omitted; compression initial slope exactly matches `E0` only when `E0 epsc0/fc=2`.

Status: `ACTIVE_MATERIAL_CANDIDATE_R123 / NOT_YET_PRODUCTION_LOCK`.
