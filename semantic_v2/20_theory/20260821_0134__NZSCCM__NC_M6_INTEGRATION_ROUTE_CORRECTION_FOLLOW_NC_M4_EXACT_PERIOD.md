# NZ-SCCM — NC-M6 积分路线纠正：严格复制 NC-M4 exact-period 闭合

时间：2026-08-21 01:34 +08:00

状态：`NC_M6_FROZEN / FOLLOW_NC_M4_INTEGRATION_ROUTE / NO_ELEMENTARY_REDUCTION_REQUIREMENT / NO_SEPARATE_PERIOD_EVALUATOR_THEORY / EXACT_PERIOD_IS_INTEGRATED_RESULT / CASE21_NOT_RUN`

## 1. 纠正

撤回此前“板面双重积分还必须先建立独立 2D period evaluator 才算积分完成”以及“先检查能否进一步约成 elementary/Appell/Lauricella”的额外门槛。

这些都不是 NC-M4 正式路线的必要步骤。

NC-M4 的正式闭合是：

1. 半角有理化；
2. 唯一二次根式；
3. 厚度 Euler 精确积分；
4. 厚度凝聚后的板面积分直接识别并写成 finite relative/incomplete Aomoto-Gelfand / GKZ exact periods；
5. 以这些 exact-period objects 作为已经完成积分后的全局函数；
6. 对全局函数求同源导数并组成极限条件；
7. 联立求解极限状态。

NC-M6 后续严格照搬这一积分骨架，不增加额外理论层。

## 2. NC-M6 当前三函数的正式积分终点

厚度积分完成后，记三个厚度凝聚函数为

\[
\mathcal T_P(\xi,\eta;D,q,\alpha),\qquad
\mathcal T_q(\xi,\eta;D,q,\alpha),\qquad
\mathcal T_\alpha(\xi,\eta;D,q,\alpha).
\]

板面双重积分直接按 NC-M4 处理：经

\[
\xi=\frac r{1-r},\qquad \eta=\frac s{1-s}
\]

紧化后，把有限 rational/algebraic/log/arctan 项写成 finite relative/incomplete Aomoto-Gelfand / GKZ exact-period objects。无需要求继续降成 elementary functions，也无需把“period evaluator”提升成新的理论门槛。

因此积分后的三个正式函数直接写为

\[
\boxed{
P(D,q,\alpha)=\sum_\nu c_{P\nu}(D,q,\alpha)\,\mathfrak A_{P\nu}(D,q,\alpha),
}
\]

\[
\boxed{
R_q(D,q,\alpha)=\sum_\nu c_{q\nu}(D,q,\alpha)\,\mathfrak A_{q\nu}(D,q,\alpha),
}
\]

\[
\boxed{
R_\alpha(D,q,\alpha)=\sum_\nu c_{\alpha\nu}(D,q,\alpha)\,\mathfrak A_{\alpha\nu}(D,q,\alpha).
}
\]

其中所有系数按 V6 普适系数生成规则由结构、几何、NC-M6 材料参数恒等产生；不硬编码 Case 数字。

这三个式子已经没有任何正式空间积分变量，因此按 NC-M4 的口径属于 `INTEGRATION_COMPLETED_AS_EXACT_PERIOD_REPRESENTATION`。

## 3. 后续唯一顺序

\[
\boxed{
\text{NC-M6 actual kernels}
\to
\text{exact thickness primitives}
\to
\text{finite exact-period global functions }(P,R_q,R_\alpha)
\to
\text{same-source derivatives}
\to
\text{limit condition}
\to
\text{coupled solve}.
}
\]

不再增加：

- elementary-function reduction gate；
- Appell/Lauricella reduction gate；
- separate period-evaluator theory gate；
- spatial quadrature；
- material-point grid；
- 新材料模型或 G18 回溯。

## 4. 治理锁定

`FOLLOW_NC_M4_EXACT_PERIOD_CLOSURE = LOCKED`

`EXACT_PERIOD_OBJECT_COUNTS_AS_COMPLETED_ANALYTIC_INTEGRAL = YES`

`ELEMENTARY_REDUCTION_REQUIRED = NO`

`SEPARATE_2D_PERIOD_EVALUATOR_GATE = RETRACTED`

`FORMAL_SPATIAL_SAMPLING = 0`

`FORMAL_SPATIAL_QUADRATURE = 0`

`FORMAL_SPATIAL_SUBDOMAINS = 1`

`CASE21 = NOT_RUN`
