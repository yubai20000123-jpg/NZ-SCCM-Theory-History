# NZ-SCCM — 严格零空间积分与 23:43 AR2 结果撤回锁

**Timestamp:** 2026-08-15 23:58 +08:00

## 1. 用户最新边界

正式锁定：

```text
ANY_SPATIAL_GAUSS = PROHIBITED
ANY_SPATIAL_SIMPSON = PROHIBITED
ANY_SPATIAL_ADAPTIVE_QUADRATURE = PROHIBITED
ANY_SPATIAL_COLLOCATION = PROHIBITED
ANY_SPATIAL_MATERIAL_POINT_GRID = PROHIBITED
AUDIT_ONLY_SPATIAL_QUADRATURE = ALSO_PROHIBITED
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

零空间积分不是“production only”的标签要求，而是当前 NZ-SCCM 理论和计算的硬边界。后续即使只用于 audit，也不得用空间 Gauss/Simpson/离散点来生成承载力路径或峰值。

## 2. 23:43 AR2 direct-continuum 结果身份

23:43 阶段使用了高阶 Gauss-Legendre 空间积分，因此：

```text
Pu_AR2_40.97334_MN = RETRACTED_FROM_CURRENT_EVIDENCE
2343_AR2_PATH = HISTORICAL_INVALID_UNDER_CURRENT_GOVERNANCE
2343_AR2_PEAK = MUST_NOT_BE_USED_FOR_THEORY_VALIDATION
```

相关文件保留作历史错误证据，不删除、不改写为正式结果。

## 3. 膜力重分布理论重新打开的范围

经典薄板大挠度后屈曲的膜应力重分布应由 Föppl–von Kármán / Kármán 大挠度相容—平衡系统产生。当前 `p20,p02` 最小坐标来自“二阶几何源的函数空间跨度补全”，这只能证明原 D+q+c 空间不完备，**不能单独证明该两坐标构成了经典后屈曲膜应力场的正确闭合**。

尤其必须重新核查：

- 是否应从 Airy 应力函数 / 面内平衡方程出发得到膜力谐波，而不是先指定任意位移补全；
- `p20,p02` 的系数、相互约束、边界条件与外功是否与经典 FvK 兼容；
- 对高宽厚比板，更新理论是否能够恢复经典稳定后屈曲承载储备这一基本极限；
- 在进入 nonlinear material operator 前，弹性薄板退化极限必须先通过经典解析解校验。

## 4. 新的理论门禁

在任何新的 Z6 Pu 计算之前，必须先完成：

```text
CLASSICAL_ELASTIC_THIN_PLATE_POSTBUCKLING_LIMIT_GATE
```

要求在同一单完整半波、同一边界条件下，零空间积分地恢复经典 Kármán/FvK 后屈曲关系及膜应力重分布。只有该退化极限通过，才允许把相同膜力闭合并入 R10/N48 current material operator。

## 5. 当前禁止事项

```text
NO new Pu
NO direct-continuum spatial quadrature
NO use of 40.97334 MN as evidence
NO ad-hoc new membrane coordinates before classical limit derivation
NO web/PBL force-only correction
NO out-of-plane multimode expansion
```
