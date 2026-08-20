# NZ-SCCM — NC-M6 精确积分执行节点 V5

时间：2026-08-21 01:15 +08:00

状态：
`NC_M6_FROZEN / ONE_CONTINUOUS_COMPLETE_HALFWAVE / THICKNESS_EXACT_OPERATOR_PASS / 2D_PERIOD_REDUCED / 2D_PERIOD_EVALUATOR_NOT_YET_INSTANTIATED / CASE21_NOT_RUN`

## 1. 本轮实际执行

本轮没有再次改材料，也没有引入 G18。首先按当前 NC-M6 冻结小数重新生成 T2/T4，避免上一版把近似循环小数擅自改写成简单分数。

厚度方向采用统一二次扩张
\[
R^2=Q_2\zeta^2+Q_1\zeta+Q_0.
\]

所有 branch-local kernel 在共轭归约后写成
\[
K=K_0(\zeta)+K_1(\zeta)R.
\]

Euler 变换
\[
\omega=R+\sqrt{Q_2}\zeta
\]
给出
\[
\zeta=\frac{\omega^2-Q_0}{2\sqrt{Q_2}\omega+Q_1},
\]
\[
R=
\frac{\sqrt{Q_2}\omega^2+Q_1\omega+\sqrt{Q_2}Q_0}
{2\sqrt{Q_2}\omega+Q_1}.
\]

因此每个厚度 kernel 严格成为普通有理函数
\[
K\,d\zeta=\frac{N(\omega)}{D(\omega)}\,d\omega.
\]

Wolfram 对一般测试核
\[
\frac{a_0+a_1\zeta+(b_0+b_1\zeta)R}
{c_0+c_1\zeta+c_2\zeta^2}
\]
进行了符号检查；Euler 后不存在 \(\zeta\)-依赖平方根，示例 rational numerator/denominator 关于 \(\omega\) 均为 6 次。这是厚度积分骨架的独立 CAS 验证。

提供 `nc_m6_exact_thickness_engine_v5.py`，其中：
- 冻结 T2/T4 小数按有限十进制精确有理数保存；
- 实现 \(A+BR\) pair algebra；
- 实现 compression 共轭归约；
- 实现 Euler map；
- 实现 exact rational primitive (`sympy.integrals.rationaltools.ratint`)。

## 2. 本轮必须诚实保留的边界

厚度方向已经得到可执行 exact operator。

但全空间积分不能仅因为“可归类为 GKZ period”就宣称已可直接用于数值根求解。厚度凝聚后的二维板面积分已经完成到 relative/incomplete Aomoto-Gelfand/GKZ exact-period 表示，但当前尚未实例化一个不使用空间数值求积的 period evaluator。

因此当前状态必须写成：

\[
\boxed{\texttt{THICKNESS\_EXACT\_INTEGRATION = PASS}}
\]

\[
\boxed{\texttt{2D\_EXACT\_PERIOD\_REDUCTION = PASS}}
\]

\[
\boxed{\texttt{2D\_PERIOD\_EVALUATOR = NOT\ YET\ INSTANTIATED}}
\]

\[
\boxed{\texttt{ROOT\_SOLVE\_READY = NO}}
\]

下一步不应做 Jacobian 或 Case21，而应只完成这一个缺口：给当前 exact-period descriptors 建立可高精度评价、零空间 quadrature 的 evaluator。完成后才真正得到可直接调用的
\[
P(D,q,\alpha),\quad R_q(D,q,\alpha),\quad R_\alpha(D,q,\alpha),
\]
随后即可进入同源极限条件和三方程联立。
