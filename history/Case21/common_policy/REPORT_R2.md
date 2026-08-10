# NZ-SCCM Swartz24 common state-independent nested support policy + Case21 gate R2

**Date:** 2026-08-09  
**Scope:** support/compiler-policy closure and Case21 regression only. No NC physics change, no reinforcement physics change, no spatial numerical integration in the formal operator.

## 1. Result

The Case21-only magnitude mask has been replaced by one fixed **parity-total-degree closure (PTDC)** support policy. The policy has 2021 operation masks and 1,962,295 retained keys, versus 1,342,030 keys in the Case21-local seed (+46.2%). It is identical for all panels/states.

The generalized halfwave generator now supports both Swartz source groups:

- cases 1–16: `ell=2440 mm`, `r=b/ell=0.5`;
- cases 17–24: `ell=1220 mm`, `r=1`;
- one complete representative halfwave, active `m=1` within that halfwave.

The r=1 reduction reproduces the R1 Case21 generator exactly.

## 2. Common-policy numerical qualification

Against independent high-order quadrature of the **same finite N60 material series** (audit only), 13 completed qualification states spanning both halfwave groups and the Swartz material-kappa extrema give:

- max relative axial integral error: `0.0053431 %`;
- max absolute amplitude-residual integral error: `0.01975435`;
- principal normalized strain actually covered by the completed qualification set: approximately `[-1.24929, +0.13636]`;
- `kappa` extrema tested: `1.9993148515` to `2.0008935611`.

The raw state-by-state values are frozen in `audit_only/common_policy_qualification.csv`; no experimental load was used to construct or tune the mask.

## 3. Case21 common-policy regression

Three reclosed equilibrium roots around the peak are:

| D | q | P/kN | total R |
|---:|---:|---:|---:|
|0.704000000|0.002189971407|342.100678762|-1.26e-7|
|0.705400327|0.002194466440|342.102040052|-1.04e-7|
|0.706000000|0.002196398532|342.101790217|-9.51e-8|

Local quadratic peak location: `D=0.705400166`; the explicitly reclosed center point differs negligibly and is adopted.

Final common-policy Case21 result:

- `D_u = 0.7054003270`;
- `q_u = 0.002194466440`;
- `A_u = 2.677249 mm`;
- `A0+A_u = 5.727249 mm`;
- `Pc = 316.410841 kN`;
- `Ps = 25.691200 kN`;
- `Pu = 342.102040 kN`;
- `R_total = -1.04e-7`;
- versus `Pf_exp=368.312750 kN`: `-7.11643 %`.

Comparison:

- legacy old ZIP: `342.10774 kN`; common-policy difference `-0.00570 kN` (`-0.0017%`);
- R1 Case21-local mask: `342.33835352 kN`; common-policy difference `-0.23631 kN`;
- old direct physical-operator quadrature audit: `342.32988 kN`; common-policy difference `-0.22784 kN` (`~ -0.067%`).

This resolves the previous ambiguity: the R1 local-mask value is **not** the stable target after removing state-specific support holes. The common policy returns essentially to the legacy 342.108 kN level. The remaining ~0.067% gap to the direct physical target belongs to the **N60 material-series representation/convergence layer**, not the support topology.

## 4. TT pre-bound

The exact frozen TT interaction was recovered as `tau_i*=tau_i[1-a_tt*tau_j^8]`, `a_tt=1-2^(-1/8)`. A common-domain analytic trace bound gives at least one principal normalized strain `<= -0.197745` everywhere in the qualified Swartz windows. The resulting common certificate is `|Delta s_TT|<1.18e-6`, `|Delta P_TT|<8.35e-4 kN`, and conservative `|Delta Rq_TT|<6.95e-3`. TT is therefore closed by an analytic common-domain error certificate rather than by deleting the term.

## 5. Gate decision

```text
GENERALIZED_2_GROUP_KINEMATICS              = PASS
R1_R_EQUALS_1_GENERATOR_EQUIVALENCE         = PASS
FIXED_MASK_FAST_EVALUATOR_EQUIVALENCE       = PASS
SWARTZ24_COMMON_STATE_INDEPENDENT_PTDC_MASK = PASS_R2
CASE21_COMMON_POLICY_RQ_ROOT                 = PASS
CASE21_COMMON_POLICY_PEAK_BRACKET            = PASS
CASE21_COMMON_POLICY_Pu_kN                   = 342.102040052
FORMAL_SPATIAL_QUADRATURE                    = 0

TT_COMMON_DOMAIN_ANALYTIC_CERTIFICATE        = CLOSED_R2
N_ORDER_STRESS_TANGENT_RQ_L_CONVERGENCE      = OPEN
SWARTZ24_FORMAL_PRODUCTION_BATCH             = NOT_YET_AUTHORIZED
```

The support-policy gate and the TT common-domain certificate are now closed. The **only remaining mandatory pre-production gate** is N-order convergence for total stress + consistent tangent + `Rq/L`. The scalar audit already shows why this cannot be waived: N60 stress values are accurate, but the material derivative/tangent series is not yet demonstrably converged. The 24-panel formal batch must remain unreleased until that derivative-level gate is repaired and passed.
