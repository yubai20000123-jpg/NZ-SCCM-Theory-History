# NZ-SCCM — 双层钢筋常规化与 Case21 `h_r=0` 退化规则

时间：2026-08-20 19:19 +08:00

状态：`LOCKED_MODELING_RULE`

## 1. 一般理论

后续钢筋模块统一采用双层写法，层位置

\[
z_r^{(+)}=+h_r,\qquad z_r^{(-)}=-h_r.
\]

这是为了统一处理一般板的上下两层配筋，不代表所有试件都必须存在非零层间距。

若某一方向总配筋面积（或总等效厚度）为 `A_{s,d}`（或 `t_{s,d}`），则一般双层在无其他来源说明时按两层分配：

\[
A_{s,d}^{(+)}+A_{s,d}^{(-)}=A_{s,d},
\]

对称双层时

\[
A_{s,d}^{(+)}=A_{s,d}^{(-)}=A_{s,d}/2.
\]

这样不会因采用双层通用公式而把总钢筋面积重复计算两次。

## 2. Case21 特殊退化

Case21 来源钢筋层位于中面，因此正式取

\[
\boxed{h_r=0}.
\]

于是

\[
z_r^{(+)}=z_r^{(-)}=0.
\]

双层通用公式在 Case21 上严格退化为两个重合的半面积钢筋层，其合力与原单层中置钢筋完全相同。

对 x 向钢筋：

\[
\varepsilon_{sx}^{(+)}=\varepsilon_{sx}^{(-)}
=\varepsilon_m+S\frac{\pi^2}{b^2}\cos^2\frac{\pi x}{b}\sin^2\frac{\pi y}{\ell},
\]

\[
G_{sx}^{(+)}=G_{sx}^{(-)}
=(A_0+A)\frac{\pi^2}{b^2}\cos^2\frac{\pi x}{b}\sin^2\frac{\pi y}{\ell}.
\]

对 y 向钢筋：

\[
\varepsilon_{sy}^{(+)}=\varepsilon_{sy}^{(-)}
=-\frac{\Delta}{\ell}+S\frac{\pi^2}{\ell^2}\sin^2\frac{\pi x}{b}\cos^2\frac{\pi y}{\ell},
\]

\[
G_{sy}^{(+)}=G_{sy}^{(-)}
=(A_0+A)\frac{\pi^2}{\ell^2}\sin^2\frac{\pi x}{b}\cos^2\frac{\pi y}{\ell}.
\]

因此上下两层的纯弯曲杠杆项 `±h_r (...)` 严格消失；但由 von Karman 几何非线性产生的 `S=A_0A+A^2/2` 膜应变项以及 `H=A_0+A` 对 `A` 的导数项仍保留。

若两层各取总该方向钢筋的一半，则

\[
P_{s,d}^{(+)}+P_{s,d}^{(-)}=P_{s,d}^{single},
\]

\[
R_{m,s,d}^{(+)}+R_{m,s,d}^{(-)}=R_{m,s,d}^{single},
\]

\[
R_{A,s,d}^{(+)}+R_{A,s,d}^{(-)}=R_{A,s,d}^{single}.
\]

所以：

`DOUBLE_LAYER_GENERAL_FORM` 与 `CASE21_SOURCE_GEOMETRY` 完全兼容；Case21 不需要人为设置非零 cover 或层距。

## 3. 后续执行纪律

- 一般钢筋理论继续保持双层形式。
- 对 Case21：固定 `h_r=0`，不得为了形式上的“双层”人为引入非零层间距。
- 双层只是 bookkeeping/generalization；总钢筋面积必须守恒，禁止因两层重合而 double-count reinforcement.
- 钢壳若采用双层壳面表示，则其 `z_sh^{±}` 按实际壳面/形心位置输入，不照搬 Case21 钢筋的 `h_r=0`。
