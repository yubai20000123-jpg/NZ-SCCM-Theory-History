# TREE DELTA — TC θ 代换精确厚度积分

时间：2026-08-20 17:16 +08:00

## 新增锁定节点

`Nguyen current strains -> theta -> chi=tan(theta) -> zeta(chi) rational -> epsilon1/epsilon2 rational -> NC-M4 fixed-pole decomposition -> Rm/P/RA TC thickness kernels rational -> quadratic partial fractions -> rational + log + arctan/artanh primitives`.

## 关键修正

- 不再把 TC 厚度积分描述成必须通过 `I1/I2 -> sqrt(quadratic)` 才能处理。
- theta 不只是方向解释工具；直接以 `chi=tan(theta)` 作为厚度积分代换后，`zeta`、`epsilon1`、`epsilon2`、`Gx/Gy/Ggamma` 全部成为低阶有理函数。
- NC-M4 的 T4 三次分母先按三个固定材料极点分解；beta 与 C 用共轭固定极点分解。结构参数只进入二次多项式，不进入高次通用代数根。
- TC 的 Rm/P 每个厚度项仅含两个二次分母；RA 每项最多三个二次分母或一个重复二次分母。
- TC 厚度原函数仅需要 `rational + log + arctan/artanh`。
- `TC_THICKNESS_ANALYTIC_GATE = PASS`。

## 同步补交

已同时补交上一轮尚未单独建档的“最终三元方程组显式积分版（无 abstract period placeholders）”。

## 下一唯一任务

1. CT：方向 1/2 交换，按同一 theta-rational 路径补齐；
2. CC / TT：按同一 `chi=tan theta` 路径写出厚度有理原函数；
3. 将四状态厚度原函数按当前状态连续段端点求值后，进入一般矩形 `X,Y` 外层解析积分。

仍保持：`N_formal_spatial_sampling=0`, `N_formal_spatial_quadrature=0`, `ONE_CONTINUOUS_COMPLETE_HALFWAVE`, `b` 与 `ell` 独立。