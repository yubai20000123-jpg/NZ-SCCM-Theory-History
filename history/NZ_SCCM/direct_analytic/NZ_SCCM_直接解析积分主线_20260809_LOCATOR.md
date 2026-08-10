# 2026-08-09 直接解析积分主线：原始文件定位与身份边界

## 原件

```text
filename = NZ_SCCM_直接解析积分主线_Case21到Swartz24_阶段锁定稿_20260809.md
ChatGPT File Library ID = file_00000000e0688230b6dcf613472b6798
local R2 copy SHA-256 = 439a278738e953a2933f35cfc917e8427b89341b76d7d9c6b24c2524998ebba1
GitHub byte-exact original = PENDING
```

## 历史角色

该文件冻结过“原始目标函数显式化 + 面向实际 integrand 临时选择数学工具”的直接解析思想，并明确：

```text
N_formal_spatial_quadrature = 0
```

以及不能只写 `M(epsilon)` / `Q_nm` 后停止，正式推导应把应力内部材料关系继续展开到实际函数。

## 必须保留的 supersession 边界

该历史文件中的 tension law 使用过 `tanh` / sigmoid transition 形式。这不是 2026-08-09 后续恢复出来的当前 NC benchmark tension identity。

当前 NC/rebar benchmark 以：

`theory/current/NZ_SCCM_CURRENT_OPERATOR_EXPLICIT_NC_REBAR_V1_20260809.md`

为准，其中 tension law 是 **algebraic Foster H(r,r0;0.05)**，不是 tanh variant。

因此：

```text
DIRECT_ANALYTIC_EXPLICIT_INTEGRAND_PHILOSOPHY = RETAINED
TANH_TENSION_VARIANT_AS_CURRENT_NC_BENCHMARK = SUPERSEDED / EXCLUDED
```

该文件仍是重要历史证据，因为它记录了从“material compiler 中心”转向“直接面对真实连续目标积分”的思想转折，但不得因文件名含“阶段锁定稿”就覆盖后续 material identity correction。
