# UCFT v5 / v5-all-buckling source locator

本文件只做历史来源定位，不把 v5 恢复为当前 NZ-SCCM production 主线。

## 原始模块

| 模块 | File Library ID | 已有独立完整性审计 SHA-256 | 历史角色 |
|---|---|---|---|
| `UCFT板轴压承载力理论体系_v5_局部钢壳屈曲判别与有效纵向应力闭合模块.md` | `file_00000000db2872069ee416c3cbb9c68a` | `cdbfea27fbdd2f14a63b6c18f1b24a6cc8ed65c10d76f5e619bbb27bb554f2e0` | 局部钢壳屈曲、云露弹性大挠度屈后、孙立鹏 Bleich–R-O、分区分侧有效应力 |
| `UCFT板轴压承载力理论体系_v5_材料模块与上下钢壳非对称模块.md` | `file_00000000b8f8720684fe5da6ac6b6875` | `f7e7f90b0da2c5130d5b6a9a112863e1305aae9919d60266b783760cd361554a` | 当时 UHPC 单轴本构、R-O 钢材、上下钢壳非对称、材料切线接口 |
| `UCFT板轴压承载力理论体系_v5_四边简支整板稳定矩阵元素积分与后屈曲路径闭合模块.md` | `file_000000001d5072068196284a9fda1703` | `10ec572ed920852fe8b192af089232c98545247630b58aa8564b76350c84fc8b` | 四边简支整板形函数、局部—整体耦合、矩阵积分、后屈曲路径 |
| `UCFT板轴压承载力理论体系_v5-all-buckling_总集成与一致性校核模块.md` | `file_00000000f22c72099a3b0caa4222a431` | `31d8e9b7051d31c98a41150efef87cc12f0c55e7b82a473b90d9436a79515c8c` | 三模块总集成；历史 `Nu=max_lambda N(lambda)` 路径定义 |
| `UCFT板轴压承载力理论体系_v4-locked-B1_原则边界.md.txt` | `file_0000000086247206b0046d62f398e7c9` | `ef81de2949c3a2a1eb4c1d5c608734c2deef56968a98e728ce5dfb16caad9a1a` | v5 的历史上位原则边界 |

上述 SHA 来自 `BLIND12_THEORY_SOURCE_AUDIT.md` 对这些文件的全文行数/哈希审计，不是本轮重新计算的 GitHub blob SHA。

## 必须保留的历史力学含义

v5 曾明确锁定：

- PBL 主要以钢壳局部子板强固支边界体现；
- PBL 不单独作为轴压承载项；
- PBL 不作为显式弹簧能量项；
- 总承载力路径历史表达为 `N(lambda)=Nc+Ns+ + Ns-`，`Nu=max_lambda N(lambda)`；
- 局部屈曲事件、整板稳定事件、材料破坏事件均不自动等同于总承载力峰值；
- 云露只提供 Kármán 大挠度/薄膜效应/Galerkin 局部钢壁板思想，UCFT 整板矩阵是项目重建，不得冒充云露原文。

## 当前身份

这些文件属于 `HISTORICAL_THEORY_SOURCE`。

它们必须保留以恢复 steel-shell/Y、PBL、UHPC 材料来源和 UCFT 局部—整体耦合思想，但不能覆盖后来的完整 Layer-0 / N–Y / NZ-SCCM 治理。

特别是其中早期 UHPC 单轴材料闭合不能恢复为当前最终 UHPC 多轴 production operator。
