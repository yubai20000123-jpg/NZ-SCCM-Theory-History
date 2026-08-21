# NZ-SCCM — Z0–Z5 / Swartz24 试件有效性分类（误差分析前冻结）

时间：2026-08-21 12:41 +08:00

## 1. 原则

本分类在继续 H8→H10 收敛计算和查看新的理论误差以前冻结。不得根据理论误差大小反推某个试件为异常试件。

分类：

- `A_STANDARD_TEST`：物理试验，破坏机制属于当前理论验证对象；进入 primary experimental validation set。
- `B_PERTURBED_TEST`：物理试验，机制仍相关但有明确非理想扰动；只进入 robustness set。
- `C_NONSTANDARD_TEST`：物理试验由当前理论未描述的异常机制控制；保留报告但不进入 primary error statistics。
- `V_VIRTUAL_BENCHMARK`：不是物理试件，不做试件随机性分类，只用于理论/数学/跨结构族验证。

## 2. Swartz Case1–Case24

原始 Swartz–Rosebraugh–Berman 24 块矩形 RC 板均为四边简支、单向轴压试验；原始论文摘要明确：24 块均加载至破坏；每一块的最终破坏以前均先发生板屈曲（双曲率）；所有试件最终均形成类似四边简支板受均布横向荷载时的塌落机制。Nguyen 后续复核同样记录了 Case17–24 的两半波屈曲形状，并指出 Case21 计算屈曲形状与 Swartz 实测形状相似；较厚两组则为近似单半波。

因此在当前可得源证据下：

`Case1–Case24 = A_STANDARD_TEST`。

Southwell / strain / deflection-profile 只是不同的“初始屈曲荷载识别方法”，不是最终破坏机制异常，不能据此降级为 B/C。

当前证据没有支持把任何单个 Swartz case 事先标成 B 或 C；若以后获得原始逐板试验日志显示明确夹具滑移、加载偏心、端部破坏等，才允许基于新源证据更新分类，而且仍不得参考理论误差大小。

## 3. Z0–Z5

当前 Z0–Z5 是 2026-08-17 后统一修改为 `a=2b / m*=2 / ell=b / k=1 / SSSS` 的理论参数对象。现有计算书把它们明确作为与 Zhou/Winter 理论值进行后验比较的 modified AR2/SSSS 系列；它们不是六个具有独立破坏记录的物理试件。

因此：

`Z0–Z5 = V_VIRTUAL_BENCHMARK`。

它们可以用于：

- H2N Ritz 阶次收敛；
- 多相 reference/membrane equilibrium；
- NC-M6 + steel face + web 的跨结构族数学验证；
- 对 Zhou/Winter comparator 的理论间比较。

它们不得用于估计：

- 试件随机误差；
- physical specimen scatter；
- A/B/C 试验破坏有效性比例。

## 4. 冻结后的误差统计口径

- `Swartz24`：可作为 primary experimental validation set；理论冻结后再统计 signed bias、MAE/RMSE、去中心 residual scatter、MAD 等。
- `Z0–Z5`：只报告理论 comparator deviation 和连续阶收敛，不与 Swartz24 混合计算“试验随机误差”。

本分类不改变 NC-M6、不改变 H2N 运动学、不使用任何理论预测误差作为分类依据。
