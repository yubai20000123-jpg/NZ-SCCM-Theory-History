# H1 STEP-10：Kp^mat phase-period 收敛与 history-aware 局部塑性铰支路 R01

## 0. 本步结论

本步完成两个动作：

1. 将 STEP-9 已经 exact-z 化的 Kp^mat 在 BH050/BH060/BH100 frozen states 上推进到高分辨率 periodic phase evaluator；
2. 将 perfect-plastic stress history transport 以 diagnostic 形式嵌入固定 critical strip，比较 history-aware 与 instantaneous active-set 的局部铰特征值。

未修改 A20、finite-force law、A24 权重或 global R1～R8，也未使用 FEM 拟合系数。

## 1. Kp^mat phase-period 数值收敛

formal identity：

Kp^mat = (1/4pi^2) int_0^{2pi} int_0^{2pi} I(xi,psi) dxi dpsi.

每个 phase 点的 thickness active set 和 z 积分均已 exact。

96→128 的 matrix Frobenius change：

- BH050: active plastic fraction = 0.3461; change = 0.056%
- BH060: active plastic fraction = 0.3456; change = 0.026%
- BH100: active plastic fraction = 0.3144; change = 0.030%

因此三个 frozen states 标记为 HIGH_CONFIDENCE_NUMERICAL_PHASE_PERIOD，但不是 theorem-level interval certificate。

## 2. History transport 材料更新

quadratic Mises perfect-plastic return：

sigma_{n+1} = sigma_tr - Delta_lambda C_e n_{n+1}.

令 alpha = Delta_lambda/f_y，则

(I + alpha C_e M) sigma_{n+1} = sigma_tr.

通过 C_e^(1/2) M C_e^(1/2) 的特征分解，return mapping 退化为单调 scalar equation：

sum_i beta_i y_tr,i^2 / (1 + alpha beta_i)^2 = f_y^2.

没有使用经验 radial stress reduction coefficient。

## 3. History-aware stability 结果

在 FEM-peak controlling strip 的固定 outer/global phase 位置，沿 10 个 selected H1 states 做 connected stress transport。注意这是对当前 H1 deformation path 的 post-processing，塑性后没有重新求解 U、q、R1～R8，因此是因果审计，不是完整新分支。

| Case | history lambda=0 load/FEM Pu | history lambda=0 Delta/FEM peak Delta | instantaneous lambda=0 load/FEM Pu | lambda_hist @ FEM peak | lambda_inst @ FEM peak | ever-plastic frac @ peak | unloading frac @ peak |
|---|---:|---:|---:|---:|---:|---:|---:|
| BH032 | 0.863 | 0.621 | — | -0.294 | +0.250 | 0.980 | 0.000 |
| BH050 | 1.053 | 0.976 | — | -0.021 | +0.012 | 0.397 | 0.000 |
| BH060 | 0.871 | 0.832 | 0.949 | -0.142 | -0.002 | 0.522 | 0.000 |
| BH070 | 0.832 | 0.741 | 0.833 | -0.091 | -0.084 | 0.348 | 0.000 |
| BH085 | 0.692 | 0.563 | 0.692 | -0.154 | -0.153 | 0.232 | 0.000 |
| BH100 | 0.556 | 0.389 | 0.556 | -0.269 | -0.265 | 0.328 | 0.000 |

## 4. 解释

Transition family 的 history correction 很重要：
- BH032: lambda_inst = +0.250，而 lambda_hist = -0.294；
- BH050: +0.012 → -0.021；
- BH060: -0.002 → -0.142。

因此 Kp^(hist-g) 不是冗余项。在过渡宽度中，如果只用 current active-set tangent、不携带先前塑性 stress history，会显著高估局部稳定刚度。

Wide family BH070/BH085/BH100 中，history 与 instantaneous 差异很小，说明这些试件主要由 current geometric/local-mode instability 与 current plastic tangent localization 控制。

固定 critical strip / fixed outer phase 在 FEM peak 时，本步记录的 elastic unloading history fraction 基本为 0。因此当前可确定的是 plastic history 已经改变 current finite stress，即使该处仍可能处于继续塑性加载。不能据此宣称 controlling strip 在峰值前已经大面积弹性卸载。真实卸载可能在其他 outer/global phase、其他 strip 或更晚 post-peak。

## 5. 当前正式算子

K_h = K_e + K_g^trial - K_p^mat - K_p^(hist-g).

- K_p^mat：不能平均；
- K_p^(hist-g)：不能删除；
- BH032～BH060 中 history term 可能决定 lambda_h 是否过零；
- BH070～BH100 中 first lambda_h=0 仍明显早于 whole-plate Pu，所以 local hinge onset 不能直接作为最终极限点。

## 6. 假定状态

- A17 finite resultants：LOCKED
- A20：不改
- A22：必须向 A23-LH 提供 history-consistent current sigma^ep，而不只是 scalar r_h
- A23-LH：FORMAL IDENTITY ESTABLISHED；phase-period numerical evaluator 已在三个 frozen states 高置信收敛
- K_p^(hist-g)：物理必要性得到 transition-family 支持，但 formal continuous history-period evaluator 仍 OPEN
- A07/A08/A26-A29：继续冻结

## 7. 下一步

1. 将 history transport 扩展到全部现有 Multiwave strips 与 outer/global phase field；
2. 每一状态先得到 history-consistent local K_h；
3. finite force 与 tangent 分开处理后进入 steel-face / section condensation；
4. 第一次重算 BH050/BH060/BH100 coupled branch，检查峰值和下降段是否自动软化；
5. 若三件通过，再扩九件。
