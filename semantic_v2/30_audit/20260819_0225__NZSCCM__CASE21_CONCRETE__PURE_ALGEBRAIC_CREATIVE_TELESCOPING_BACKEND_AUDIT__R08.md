# NZ-SCCM Case21 concrete：纯代数 Creative-Telescoping 后端执行审计 R08

**时间：2026-08-19 02:25 +08:00**  
**身份：R07 NEXT STEP ATTEMPTED / EXACT BACKEND BLOCK IDENTIFIED / NO DISCRETIZATION**

---

## 0. 执行对象

R07 已把选定 Case21 pilot 的完整 concrete axial period 收缩为纯 algebraic form：

\[
P_c(\tau)
=-\frac{f_cbt}{2\pi^2}
\int_0^1\int_0^1\int_{-1}^{1}
F(r,s,\zeta,\tau)\,d\zeta\,ds\,dr,
\]

其中 `F=S_yy/omega`，完整 R10 在 `0<=tau<=1` 全域严格停留于第一拉伸多项式分支；最小 radical generators 为

\[
\boxed{\{\omega,\Delta_A,s_A\}}
\]

及关系

\[
\omega^2=r(1-r)s(1-s),
\]

\[
\Delta_A^2=\det(\mathbf E^2+\eta^2\mathbf I),
\]

\[
s_A^2=\operatorname{tr}(\mathbf E^2+\eta^2\mathbf I)+2\Delta_A.
\]

本轮尝试的唯一操作是：生成 `tau` 方向 finite telescoper。

---

# 1. 所需的严格 Creative-Telescoping 身份

目标不是对 `tau` 作数值积分，而是寻找有限阶微分算子

\[
\boxed{
L_\tau=\sum_{k=0}^{m}p_k(\tau)\partial_\tau^k
}
\]

和 certificates `C_r,C_s,C_zeta`，使完整代数恒等式

\[
\boxed{
L_\tau F
=\partial_r C_r+\partial_s C_s+\partial_\zeta C_\zeta
}
\]

成立。

在固定积分边界处理完成后，由此得到 `P_c(tau)` 的有限 Picard–Fuchs / holonomic equation。

这才是 R07 下一步所需的算法能力。

---

# 2. 当前运行环境的符号后端实际检查

当前 Python/SymPy 环境：

```text
SymPy = 1.14.0
sympy.holonomic = AVAILABLE
```

但对实际 API/source 检查后，SymPy `HolonomicFunction` 是**单自变量 holonomic object**。

其 `integrate(self, limits)` 实现的核心是：

```text
for indefinite integration in the SAME independent variable:
annihilator_new = annihilator * D
```

definite integration 也要求 `limits[0] == self.x`；它并不实现下面这个多变量参数消元问题：

```text
independent parameter = tau
integration variables = r,s,zeta
find telescoper in d/dtau
eliminate d/dr, d/ds, d/dzeta
```

对已安装 SymPy 源码搜索也没有发现可调用的 general multivariate `creative telescoping` / `telescoper` 实现。

当前环境同时没有可执行的：

```text
SageMath / ore_algebra
Mathematica + HolonomicFunctions
FriCAS
GIAC/Xcas
```

因此不能在当前后端内诚实地声称已经生成 full `P_c(tau)` telescoper。

---

# 3. 精确阻断点

阻断发生在以下**唯一、明确的符号操作**：

\[
\boxed{
F(r,s,\zeta,\tau)
\longrightarrow
L_\tau(\tau,\partial_\tau)
}
\]

其中要求同时消去三个积分变量的 derivative ideal。

这不是：

- 材料公式缺失；
- 运动学缺失；
- 级数不收敛；
- 积分域不明确；
- 需要空间离散。

R07 已经把这些前置问题全部消除为 pure algebraic period。

当前结论：

```text
THEORY_CLASSIFICATION_BLOCK = NO
FINITE_R10_INPUT_BLOCK = NO
MATERIAL_BRANCH_BLOCK = NO
ALGEBRAIC_IDEAL_BLOCK = NO
ANALYTIC_CLOSURE_BACKEND_BLOCK = YES
DISCRETE_FALLBACK = PROHIBITED
```

---

# 4. 为什么不能用现有 SymPy holonomic “假装”完成

如果把 `F` 对 `tau` 转成一个单变量 HolonomicFunction，把 `r,s,zeta` 当作 coefficient symbols，随后调用 SymPy `.integrate()`，该方法只会对 `tau` 本身积分；它不会产生参数 definite integral 所需的 telescoper。

反过来若把 `zeta` 作为单自变量进行 holonomic integration，则积分后得到的对象仍不是自动转化为以 `tau` 为独立变量、已消去 `zeta` 的 Ore ideal；顺序重复也不能替代真正的 multivariate creative telescoping。

因此这种调用不满足 R08 §1 的 certificate identity，不能作为正式结果。

---

# 5. 当前可恢复的 exact input

若后续获得 `ore_algebra` / HolonomicFunctions / Oaku D-module / Griffiths–Dwork backend，不需要重做 R06/R07。

直接输入：

1. Case21 `E(r,s,zeta,tau)`；
2. `omega^2-r(1-r)s(1-s)=0`；
3. `Delta_A^2-det(E^2+eta^2 I)=0`；
4. `s_A^2-tr(E^2+eta^2 I)-2Delta_A=0`；
5. R07 已证全域 first tension branch，因此 `u_R(t)` 直接使用固定五次矩阵多项式；
6. R06 exact initial jet `Pc(0),Pc'(0),Pc''(0)`。

下一后端应首先尝试最小阶 `L_tau`，并输出 telescoper + certificates；不得只输出数值 `Pc(1)`。

---

# 6. 当前状态

```text
R06_P0_P1_INITIAL_JET = PASS
R07_GLOBAL_BRANCH_CERTIFICATE = PASS
R07_PURE_ALGEBRAIC_PERIOD = PASS
R08_MULTIVARIATE_CT_ATTEMPT = EXECUTED
FULL_Pc_TAU_TELESCOPER_GENERATED = NO
ANALYTIC_CLOSURE_BACKEND_BLOCK = YES
```

当前应停在这里，等待/寻找具备真正 multivariate algebraic creative telescoping 能力的符号后端；根据项目零离散治理，不允许改用任何离散方法继续。
