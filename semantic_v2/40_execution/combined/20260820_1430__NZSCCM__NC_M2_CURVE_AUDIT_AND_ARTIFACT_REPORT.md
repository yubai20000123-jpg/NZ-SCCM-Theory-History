# NZ-SCCM — NC-M2 曲线审计与产物报告

时间：2026-08-20 14:30 +08:00

## 1. 本轮执行

基于用户对 NC-M1 的否决，建立 NC-M2：每个九宫格实体象限仅使用一个显式公式，不在 CC/TC/CT/TT 内继续分段。

正式候选：

- `C(c)=2c/(1+c^2)`
- `T(t)=t/(1-t+t^2)`
- `beta(t)=1/(1+0.15t^2)`
- `eta(c1,c2)=1+0.16*C(c1)*C(c2)`

## 2. 本地可视化产物

生成目录：`NC_M2_SINGLE_FORM_20260820`

产物：

- `00_NC_M2_nine_grid.png/.svg`
- `01_compression_M2_vs_original.png/.svg`
- `02_tension_M2_vs_original.png/.svg`
- `03_TC_softening_M2_vs_original.png/.svg`
- `04_CC_enhancement_M2_vs_original.png/.svg`
- `README.md`
- `METRICS.json`

打包文件：`NC_M2_SINGLE_FORM_20260820.zip`

SHA-256：`8125012aa2ac7e2cf02030dfb393a1b232ff0a6686e2b65581d9fd8778cf038c`

## 3. 曲线级诊断

### 压缩

峰前 0≤c≤1：M2 相对当前原始参考曲线面积比约

`0.9999547368`。

M2 无峰前/峰后人工切换。

### TC 削弱

0≤t≤3：

M2 / 当前原始参考曲线面积比约

`0.9452500814`。

因此 M2 当前约保守 5.5%。

### CC 双压增强

沿 c1=1, c2=rho, 0≤rho≤1：

M2 / Foster-Kupfer 参考增强曲线面积比约

`0.9219214459`。

等双压峰值点：`eta(1,1)=1.16`。

## 4. 治理判定

- NC-M1：`REJECTED_DIAGNOSTIC_CANDIDATE`
- NC-M2：`ACTIVE_MATERIAL_CANDIDATE / NOT_YET_PRODUCTION_LOCK`
- 不使用 Case21 极限承载力反标 M2 参数。
- 下一步应检查：九宫格主应变虚功形式、旋转主方向下的代数结构、空间积分复杂度与材料级能量趋势。
