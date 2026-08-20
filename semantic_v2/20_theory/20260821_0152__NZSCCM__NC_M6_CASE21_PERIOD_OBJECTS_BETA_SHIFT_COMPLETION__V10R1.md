# NZ-SCCM — NC-M6 Case21 period-object beta-shift 补齐 V10R1

时间：2026-08-21 01:52 +08:00

状态：`63_PERIOD_OBJECTS / ASTAR_SUPPORT / COEFFICIENT_MAP / FACTOR_EXPONENTS / NUMERATOR_BETA_SHIFTS / RELATIVE_CYCLES / COMPLETE_DESCRIPTOR`

V10 已生成 21 branch × 3 kernel = 63 个实际 sparse Cayley/residue objects。为避免把“numerator monomial 对应 beta shift”只留作文字规则，本节点补齐每个实际 term 的 exponent descriptor。

统一采用

\[
\mathfrak A=\int_{\mathcal C}\prod_h P_h^{\lambda_h}\prod_i x_i^{\beta_i-1}\,d\mathbf x.
\]

对 algebraic residue relations 与显式 denominator factors：

\[
\boxed{\lambda_h=-1}.
\]

若 kernel numerator monomial 为

\[
c_\mu\prod_i x_i^{m_i},
\]

则对应 period term 的 variable exponent：

\[
\boxed{\beta_i=m_i+1}.
\]

因此 Case21 每个对象现在实际包含：

1. sparse Cayley columns；
2. coefficient map \(\mathbf c(D,q,\alpha)\)；
3. factor exponents \(\boldsymbol\lambda\)；
4. 每个 numerator monomial 的 \(\boldsymbol\beta\) shift；
5. 完整半波 physical relative cycle；
6. algebraic graph residue-torus cycle；
7. CC/TC/TT 与 T-segment inequalities。

V10R1 完整 JSON SHA-256：

`b2b48737f2515dab05889d6aa2ca8f3a564e30dac908d6c1725687b236862523`

此后 `CASE21_FINITE_PERIOD_OBJECT_LIST` 不再是 schema/placeholder，而是 actual finite descriptor list。

RC numerical root 仍在第一次 relative/incomplete RGKZ **数值评价**处阻断；本节点不使用 spatial quadrature 或历史根绕过。