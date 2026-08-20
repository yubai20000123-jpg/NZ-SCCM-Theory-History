# TREE DELTA — NC-M4 直接多重积分展开

时间：2026-08-20 16:28 +08:00

## 新增当前节点

`Nguyen 一般矩形二阶运动学 -> 中面膜应变 epsilon^0 + 曲率 kappa -> 穿厚应变 -> 派生 theta + 未排序方向1/2主应变 -> NC-M4 九宫格唯一 current operator -> 主应力 -> 板坐标应力 -> 膜力 N / 弯矩 M -> R_m, P, R_A`

## 当前锁定

- b 与 ell 独立。
- 三结构未知量仍为 `(Delta,A,epsilon_m)`。
- theta 为局部派生方向，不是结构未知量。
- 方向1/2按连续方向标签保留，不以 epsilon1>=epsilon2 排序；TC/CT 均保留。
- 中面膜应变、膜力 N 与弯矩 M 显式保留。
- R_A = 膜力二阶几何项 + 弯矩曲率项。
- 每个空间点只调用 CC/TC/CT/TT 中唯一一个 NC-M4 实体关系。
- 不建立 I1/I2 正式理论层。
- 不做 spatial cell / Gauss / Simpson / material-point grid。

## 已完成的 explicit integrands

- `R_m = ∭ sigma_x dV`，sigma_x 已按四实体区展开。
- `P = -(1/ell) ∭ sigma_y dV`，sigma_y 已按四实体区展开。
- `R_A = ∭(sigma_x G_x + sigma_y G_y + tau_xy G_gamma)dV`。
- `R_A` 在主方向中仅 6 个物理组；保持 H=A0+A 时完全拆开为 12 个加法项。

## 下一执行节点

直接对上述 explicit NC-M4 integrands 做解析积分后端执行；theta 若在 CAS 内部被消元为代数根式，只是后端表示，不升级为理论变量。