# NZ-SCCM — R14 minimal terminal correction + BH005–BH100 recalculation + Excel transfer R01

Date: 2026-09-02  
Branch: `diagnostic/bh032-bh050-mode-projection-20260827`  
Production main: unchanged.

## 1. Correction boundary

This checkpoint corrects exactly one R13 regression:

```text
REMOVE: mandatory universal eps_y^{U,-} = -eps_c0 fifth terminal equation
RESTORE: R4(x;q)=0 connected equilibrium branch
MONITOR: current UHPC material-domain margins + J4 structural fold
SELECT: first admissible closed terminal on the q=0-connected branch
```

Unchanged:

```text
initial A/D
integer mode
Marguerre–Airy P(q)
R04
R02
R06
R13 sixth-degree UHPC compression
R13 Hiew cubic-Hermite tension
UHPC F0/F1 exact thickness integration
web exact yield-crossing integration
section Nx,Mx,Ny,My
```

Therefore this is a terminal/closure correction, not a material or local-buckling redevelopment.

## 2. Corrected BH005–BH100 results

Inputs use the frozen equal-contract BH mapping: `tc=42`, `ts=4`, `a=2B`, `A0g=B/400`, `Aw=1332`, common steel/UHPC material, `Lx=0.225B`, `Ly=a/9`, `A0_local=Lx/1600`.

| Case | m* | branch | first terminal | q_u | Pu MN |
|---|---:|---|---|---:|---:|
| BH005 | 2 | R04 | UHPC_COMPRESSION_DOMAIN_BOUNDARY | 3.19945662424E-05 | 2.4834273310 |
| BH010 | 2 | R04 | UHPC_COMPRESSION_DOMAIN_BOUNDARY | 1.23780108540E-04 | 4.6277691769 |
| BH020 | 2 | R04 | UHPC_COMPRESSION_DOMAIN_BOUNDARY | 5.36391923495E-04 | 8.6662850801 |
| BH032 | 2 | R06 | UHPC_COMPRESSION_DOMAIN_BOUNDARY | 1.41287380195E-03 | 11.1136415727 |
| BH050 | 2 | R06 | UHPC_COMPRESSION_DOMAIN_BOUNDARY | 4.93091069216E-03 | 13.5247819548 |
| BH060 | 2 | R06 | UHPC_COMPRESSION_DOMAIN_BOUNDARY | 8.50596056702E-03 | 14.1028033934 |
| BH070 | 2 | R06 | UHPC_COMPRESSION_DOMAIN_BOUNDARY | 1.25834688563E-02 | 15.0161991015 |
| BH085 | 2 | R06 | J4_FOLD | 1.47536851815E-02 | 15.1974489804 |
| BH100 | 2 | R06 | J4_FOLD | 1.61195266866E-02 | 15.8195434201 |

BH005–BH070 numerical values remain unchanged because their q=0-connected R4 branch reaches the current R13 UHPC compression material-domain boundary before J4 singularity. Only the terminal identity is corrected: this is an observed first event on those branches, not a universal equation.

BH085/BH100 recover valid high-B/H results because J4 fold occurs before compression contact.

BH085 fold longitudinal lower endpoint:

```text
eps_y- = -0.00290287678653
g_y-    = +0.00059712321347 > 0
```

BH100 fold longitudinal lower endpoint:

```text
eps_y- = -0.00231294587765
g_y-    = +0.00118705412235 > 0
```

Thus both folds are inside the current UHPC compression domain.

The earlier Sep-02 outputs

```text
BH085 NO_ADMISSIBLE_COMPRESSION_CONTACT_ROOT_FOUND
BH100 NO_ADMISSIBLE_COMPRESSION_CONTACT_ROOT_FOUND
B/H ~ 74.6 root-existence boundary
```

are withdrawn. The ~74.6 boundary was only the disappearance of the artificially constrained compression-contact intersection.

## 3. Relation to the 2026-08-28 high-B/H fold ledger

The terminal logic is restored from the already validated R4/J4 route, but the current Sep-01 R13 material functions are intentionally retained.

Therefore the new current-material values do not need to reproduce the older-material results `BH085=14.530920 MN`, `BH100=15.019180 MN`.

This is deliberate minimal correction: no material rollback was used to force historical numerical agreement.

## 4. New transfer artifacts

Generated locally:

```text
NZSCCM_R14_UCFT_BH005_BH100_重算结果_R01_20260902.md
SHA256 fa346c6280f3ffcc7d1b2a32cba86835861640bff80b4a2cff92ef1eca8cfbeb

20260902__NZSCCM__STEEL_SHELL_UHPC_CENTRAL_TECHNICAL_LEDGER_R14_MINIMAL_TERMINAL_CORRECTION.md
SHA256 a763894221232e5a5a4a7d27abd5b8345ba5f1e35c18f0821d9a893e4d31618c

NZSCCM_R14_技术总账使用说明_R01_20260902.md
SHA256 62b5e2f478cd3d382e34d7c59cd35b958d2bcbfd6c6949821e09dd73bb39b33e

NZSCCM_R14_R4J4_人工联立求根助手_R01_20260902.xlsx
SHA256 ff610aed751feffba847fcb93f1e295440ee3ab5fdd28cfc7f63f28f3756cbe9

NZSCCM_R14_R4J4_人工联立求根Excel_逐格使用说明_R01_20260902.md
SHA256 2f84fe397d60a29f7223781d1014c8d2f3c927055f9d57949545a716a84c6c17
```

The updated helper workbook uses four outer variables per q:

```text
eps_x0
chi_x = tc*kappa_x/2
eps_y0
chi_y = tc*kappa_y/2
```

and four R4 residuals. It computes the visible 4x4 finite-difference J4, simultaneous Newton correction, full/half/quarter/eighth recommendations, q-path log, and terminal monitoring. The existing R06 lambda/u/v helper is retained unchanged mechanically.

## 5. Main one-page source workbook boundary

The exact source binary

`NZSCCM_钢壳UHPC_R13_单页显式公式_自动R06内部极值_20260901.xlsx`

is not mounted in the current runtime. Therefore no claim is made that its binary formulas were patched in place. A fake same-name workbook was not created.

The exact minimal patch required for that source workbook is recorded in sheet `07_主表最小修改清单` of the new helper workbook:

```text
3-variable mandatory-contact outer state -> q + 4-variable R4 state
remove eps_y-=-eps_c0 identity
3 residuals -> four original N/M residuals
3x3 recommendation -> 4x4 J4
contact-root min-positive-q -> connected-branch first-terminal selection
retain R04/R02/R06/UHPC/web unchanged
```

When the exact source xlsx binary is uploaded into an active conversation/runtime, it can be patched in place without reopening any other theory layer.
