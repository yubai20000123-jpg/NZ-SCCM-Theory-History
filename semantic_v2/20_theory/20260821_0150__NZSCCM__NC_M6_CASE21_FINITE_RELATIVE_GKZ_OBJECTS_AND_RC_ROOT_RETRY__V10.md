# NZ-SCCM — NC-M6 Case21 finite relative-GKZ 对象实例化与 RC 求根重试 V10

时间：2026-08-21 01:50 +08:00

状态：`CASE21_SPECIALIZED / 21_BRANCHES / 63_ACTUAL_PERIOD_OBJECTS / SPARSE_CAYLEY_INSTANTIATED / ZERO_SPATIAL_QUADRATURE / RC_ROOT_RETRY_STOPPED_AT_PERIOD_NUMERIC_EVALUATION`

## 0. 本节点执行内容

严格执行上一节点唯一剩余项：把 V7 的通用 exact-period index/schema 真正实例化成 Case21 的有限 period object list，然后立即重新发起 NC-M6+钢筋 RC 三元极限方程求根。

没有修改 NC-M6，没有重新碰钢筋理论，没有使用 Gauss/NIntegrate/adaptive spatial quadrature，没有用历史 NC-M4/R10 根代替新根。

## 1. Case21 finite object list 已实际生成

Case21 专化：

\[
b=\ell=1220\,\mathrm{mm},\qquad t_r=19.3\,\mathrm{mm},\qquad k=1,\qquad q_0=1/400,
\]

\[
E_0=20321\,\mathrm{MPa},\quad f_c=21.23\,\mathrm{MPa},\quad f_t=f_c/10,
\quad \varepsilon_0=0.00209,\quad \nu=0.18.
\]

保留 \(D,q,\alpha\) 为结构未知量。

按

\[
1\ \mathrm{CC}+5\ \mathrm{TC}+15\ \mathrm{TT}=21
\]

个解析 branch，对 \(P_c,R_q^c,R_\alpha^c\) 三个结构核逐个生成实际 sparse Cayley/residue object，共

\[
\boxed{63}
\]

个对象。

每个对象实际包含：

- algebraic graph 的 polynomial relations；
- 每个 polynomial factor 的全部 monomial support；
- 每列 coefficient \(c(D,q,\alpha)\)；
- Cayley column exponent；
- exact rational rank/nullity；
- 对应材料 branch 的 physical relative-cycle inequalities；
- kernel numerator 的实际 monomial list，作为同一 period family 的 beta shifts。

因此 V9 所指出的 `I_P/I_q/I_alpha 仍是 placeholder schema` 缺口已经消除。

## 2. 与 NC-M4 的一致性

NC-M4 的最终无空间积分表示同样采用 sparse polynomial circuit -> Cayley construction -> relative/incomplete RGKZ。NC-M4 曾把 48 条 sparse relations 编成一个 99 x 155 global A*。

NC-M6 本次不强行拼成一个巨型 global A*，而是保持 21 个真实材料解析 branch，每个 branch 对三个 kernel 生成一个 sparse Cayley object。有限 branch sum 与单一 global Cayley object 是等价的 exact relative-period 表示；branchwise 形式更便于审计且不引入空间离散。

## 3. 实际 kernel polynomial numerators

为把唯一 \(1/R\) 显式放入 denominator factor，三个 kernel 使用：

\[
N_P=R(s_1+s_2)-(s_1-s_2)\Delta_E,
\qquad K_P=\frac{N_P}{UVR}.
\]

\[
N_\alpha=R(s_1+s_2)A_\Sigma^\#+(s_1-s_2)(\Delta_EA_\Delta^\#+GA_\gamma^\#),
\]

\[
K_\alpha=\frac{N_\alpha}{UV\mathscr D R}.
\]

\[
N_q=R(s_1+s_2)Q_\Sigma^\#+(s_1-s_2)(\Delta_EQ_\Delta^\#+GQ_\gamma^\#),
\]

\[
K_q=\frac{N_q}{UV\mathscr D R}.
\]

共同 algebraic graph 至少包含：

\[
R^2-(E_x-E_y)^2-G^2=0,
\]

\[
2(1-\nu^2)\mathscr D\lambda_1-(1+\nu)(E_x+E_y)-(1-\nu)R=0,
\]

\[
2(1-\nu^2)\mathscr D\lambda_2-(1+\nu)(E_x+E_y)+(1-\nu)R=0,
\]

并按 CC/TC/TT 加入各自 compression/tension/interaction sparse relations。

## 4. 本次机器实例化规模

63 个对象的 Cayley row 数范围：

\[
20\ \text{到}\ 31.
\]

Cayley column 数范围：

\[
112\ \text{到}\ 134.
\]

exact rank 范围：

\[
20\ \text{到}\ 31.
\]

每个 kernel numerator 的实际 monomial 数范围：

\[
20\ \text{到}\ 110.
\]

实际不同 support SHA-256 数：42。

完整对象 JSON 的 SHA-256：

`7dc7275efbfc95b8bd1d665aa1266584182aea0660770f8b57b17afa4e8fd177`

这些规模数字是 symbolic compiler 输出，不是物理参数。

## 5. RC 求根已经立即重新发起

钢筋沿用 V9 已闭式装配：

\[
P=P_c+P_s,\qquad R_q=R_q^c+R_q^s,\qquad R_\alpha=R_\alpha^c+R_\alpha^s,
\]

\[
\mathcal L=\det J_{lim}^{RC}.
\]

求根系统：

\[
\boxed{
R_q=0,\qquad R_\alpha=0,\qquad \mathcal L=0.
}
\]

本次求根没有停在 object-list 实例化之前；63 个 Case21 concrete period objects 已经存在。

但是第一次真正需要把其中一个 **physical relative/incomplete RGKZ object 数值化** 时，仓库现有 exact backend 审计显示：

- A* exact audit：构造 support/rank/nullity，报告自身仍标记 `FULL_PHYSICAL_RELATIVE_GKZ_EVALUATOR = NOT_YET_INSTANTIATED`；
- Oaku backend：可构造 semialgebraic D-module / bounded integration ideal，但不是 physical period value evaluator；
- Sage/ore_algebra backend：构造 annihilator/tower，同样不是 relative-cycle period value evaluator。

因此求根在第一个 concrete RGKZ numerical-value call 处 fail-fast 停止。

当前没有合法路径把

\[
\mathrm{RGKZ}_{A^*}(\beta;\mathbf c\mid\Gamma_{phys})
\]

转换成数值，同时又不引入新的评价后端或空间数值求积。

## 6. 本轮明确没有使用的替代路径

没有使用：

- spatial Gauss quadrature；
- adaptive spatial quadrature；
- `NIntegrate` 板面/厚度数值积分；
- historical NC-M4/R10 roots；
- trial-load calibration；
- material-point grid。

所以没有伪造 \(D_u,q_u,\alpha_u,P_u\)。

## 7. 当前真实门禁

\[
\boxed{\texttt{CASE21\_FINITE\_PERIOD\_OBJECT\_LIST = PASS}}
\]

\[
\boxed{\texttt{CASE21\_63\_SPARSE\_CAYLEY\_OBJECTS = PASS}}
\]

\[
\boxed{\texttt{RC\_FINAL\_3EQ\_ASSEMBLED = PASS}}
\]

\[
\boxed{\texttt{RC\_ROOT\_RETRY = STARTED}}
\]

\[
\boxed{\texttt{PHYSICAL\_RELATIVE\_GKZ\_NUMERIC\_EVALUATOR = ABSENT}}
\]

\[
\boxed{\texttt{CASE21\_NC\_M6\_RC\_NUMERIC\_ROOT = BLOCKED}}
\]

阻断点现在已经不是 V7 object schema，而是 exact special-function **数值评价后端本身**。