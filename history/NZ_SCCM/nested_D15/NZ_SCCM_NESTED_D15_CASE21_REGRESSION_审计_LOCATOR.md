# Nested-D15 Case21 regression：原始审计报告定位器

## 原件

```text
filename = NZ_SCCM_NESTED_D15_CASE21_REGRESSION_完整审计报告_20260809.md
ChatGPT File Library ID = file_00000000a2dc8211b82832afebbed753
local R2 copy SHA-256 = 26ca53df30fd882eb0954cc298c1487917c7e78578d3d6e1195556cd9cf6cd24
GitHub byte-exact original = PENDING
```

## 报告的主要历史裁决

该审计报告并没有否定 nested moment-first D15 的理论方向；它把当时 ZIP 登记为局部 Case21 validation，并指出：

```text
THEORY_ROUTE = RETAINED
FORMAL_SPATIAL_QUADRATURE = ZERO_CONFIRMED
CASE21_REPORTED_PU_KN ≈ 342.10774
CASE21_NUMERICAL_PLAUSIBILITY = PASS
CASE21_BITWISE/PROVENANCE_REPRODUCIBILITY = FAIL
FULL_CASE21_END_TO_END_REPRODUCIBILITY = FAIL
COMMON_SWARTZ24_COMPILER_DOMAIN = OPEN
PRODUCTION_ADOPTION = NOT_AUTHORIZED
```

关键软件/证据问题包括：
- fixed mask 与 N/TOL/coefficients/compiler hash 未形成强绑定 metadata；
- N<60 可静默误用固定 mask；
- 默认入口不是 README 所定义的 N=60/fixed 正式模式；
- hard-coded temporary path / mask filename mismatch；
- `final_case21_out.txt` 的 exact generating state/version 未完全闭合；
- package 缺完整 concrete+rebar total residual/root/limit driver；
- independent high-order quadrature audit 未随包完整交付；
- N=60 primitive stress values 尚可，但 total consistent tangent / Rq / L convergence 没有完成 production certificate。

## 后续身份

2026-08-10 priority reset 以后，不再把 theorem-level tight remainder/certificate 当工程生产硬门槛；但 **provenance closure、正式 evaluator identity、不得用 audit 选阶、不得恢复空间离散** 等问题仍然有效。

因此该审计的长期价值是：

```text
RETAIN nested/moment-first insight
RETAIN reproducibility/provenance warnings
DO NOT automatically reactivate fixed-mask/compiler implementation as current production route
```
