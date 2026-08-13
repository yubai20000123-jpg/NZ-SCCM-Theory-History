# G31 原始工件定位器

## 原始工件

```text
filename = 00_G31_Case21_Pu全过程与UHPC_C0同步模型.md
ChatGPT File Library ID = file_0000000095688206bc564face5eb85fc
created = 2026-08-08T08:36:18Z
GitHub original-text copy = PENDING (File Library original is longer than current retrieval payload)
```

配套材料合同已直接复制到：

`materials/UHPC/history/10_UHPC_C0_material_contract.json`

原始 File Library ID：

`file_00000000363c82308a0144275d632d61`

## G31 工件的历史身份

G31 证明当时一条“连续应变 → 材料函数 → 解析级数 → D15 → P, RA → 平衡峰值”的计算链已经实际执行。该工件中的无裂化 Case21 基线为：

```text
D ≈ 1.22
q = 0.013820091996
A = 16.860512 mm
Pu = 476.935634 kN
Pf_exp = 368.312750 kN
error ≈ +29.492%
```

该数值的正确历史解释是：**数学求解链跑通，但故意忽略裂化/退化时材料模型显著高估试验。** 它不是当前 NC benchmark 的最终 Pu，也不是材料已经正确的证明。

工件同时明确说明：Case21 钢筋不能在 concrete-only 峰值后简单加 `As fy`，因为钢筋也改变 `RA`，因此正式 RC Pu 必须把钢筋加入同一残量后重新求根。

## 当前身份覆盖关系

```text
G31 UHPC-C0 = EXECUTED_CALCULABLE_BASELINE
G31 final visible delivery/user acceptance = historical evidence must be checked against original conversation tree
UHPC-C0 = NOT final production UHPC operator
```

当前治理以根目录 `CURRENT_STATE.md`、G16R/UHPC state ledgers 和 2026-08-10 priority reset 为准。

## 恢复规则

需要 G31 逐项公式/中间积分/完整 UHPC-C0 说明时，必须从 File Library 打开精确原件；本 locator 只保证原件不会因后续摘要而失去定位。
