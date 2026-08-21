# NZ-SCCM — H12→H14 无试验值连续阶收敛门禁（结果前冻结）

时间：2026-08-21 13:54 +08:00
状态：`PREFROZEN_BEFORE_ANY_H14_RESULT`

## 1. 前置状态

统一 origin-connected / full-panel first-control 复算已经得到：

- H6 rejected;
- H8 rejected;
- H10 rejected;
- H12 = next minimum candidate.

本文件在任何 H14 numerical result 出现以前冻结 H12→H14 gate。

## 2. 理论边界

- `RITZ_THEORY_ENDPOINT = LOCKED`；full-panel mother space 仍为已冻结 `F_N`。
- H12=N=6；H14=N=7；只是同一 nested full-panel Ritz family 的连续截断。
- ideal full-panel out-of-plane sector 固定为 `a/b=2` 两完整半波。
- 每阶先求 representative `r=0 mod 4` origin-connected nonlinear branch，再检查所有 complementary sectors 的 source-consistent `J_perp,N`。
- full-panel first control point 是沿同一路径最先出现的 representative control 或 complementary rank loss。
- NC-M6 frozen；M7 prohibited。
- FE/test ultimate loads 不得用于选根、选阶、阈值或 continuation。
- direct-current quadrature 仅 AUDIT/DECIMAL LOCALIZER；正式空间 sampling/quadrature/material points 均为零。

## 3. acceptance gate

保持全部既有阈值，不因 H10→H12 结果修改：

- `delta_P(H12,H14) <= 0.5%`
- `delta_D <= 0.5%`
- `delta_w <= 1.0%`
- `delta_epsilon <= 2.0%`
- same ideal full-panel mode
- same origin-connected path identity
- complementary-sector ordering included in each order's full-panel first-control definition
- audit-localizer marginal peak-load refinement `< 0.05%`

## 4. decision rule

若 Z0 的 H12→H14 任一决定性 gate 失败：

`H12_PRODUCTION_FREEZE = NO`

并在任何 H16 result 以前预冻结 H14→H16 gate。

若 Z0 通过，不足以单独授权 H12 production；继续 Z1–Z5，再按项目既定顺序检查其他要求的结构族。

## 5. additional diagnostics（不改变 gate）

记录：

- H14 representative first-control path;
- H14 complementary-sector ordering;
- newest ring strain-weighted contribution;
- H12→H14 load/deformation/field corrections。

这些只用于解释收敛速度，不能改变 acceptance thresholds。
