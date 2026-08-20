# NZ-SCCM — NC-M5: T_NC -> T5 单式化 + 完整九宫格 stress/tangent/边界/有界性审计

时间：2026-08-20 21:25 +08:00

状态：`T5_SINGLE_RATIONAL = PASS`; `FULL_DOMAIN_STRESS_BOUNDEDNESS = PASS`; `COMMON_ORIGIN_TANGENT = PASS`; `FINITE_FRONT_TANGENT_CONTINUITY = FAIL_PENDING_REGISTERED_C1_C2_REGULARIZATION`

## 0. 治理边界

唯一参考保持为 `NC-基准本构`。本轮只做 `T_NC -> T5` 的单式化；CC/TC/CT/TT 冻结 target、不修改 Poisson/NC material-coordinate 架构、不使用 Case21 Pu 或试验荷载拟合任何系数。

G21 冻结普通混凝土物理目标：

- CC: `c_i*=c_i(1+a_cc c1 c2)`, `a_cc=0.10723292493624159`;
- TC/CT: `c*=c(1-tau)`;
- TT: `tau_i*=tau_i(1-a_t tau_j^8)`, `a_t=0.08299595679532878`;
- `alpha2=0.3` conservative tension stiffening;
- C1/C2 regularization is an already registered project approximation.

## 1. 实际固定 NC 拉伸 reference

不是未经平滑的折线，而是 G20/G21 已存在的 C2-regularized target。令

\[
r=\lambda/x_{cr},\qquad \tau=\sigma_t/f_t.
\]

在 benchmark normalization `rho=ft/fc=0.1`, `kappa=2`, `xcr=rho/kappa=0.05` 下，对应：

- `r <= 0.7`: `tau=r`;
- `0.7<r<1.5`: quintic C2 bridge, from `(0.7, slope 1)` to `(0.961111..., slope -7/90)`;
- `1.5<=r<=9`: `tau=1-(7/90)(r-1)`;
- `9<r<11`: quintic C2 bridge to `(0.3, slope 0)`;
- `r>=11`: `tau=0.3`.

该 target 记为 `T_NC(r)`。

## 2. NC-M5 单一拉伸式 T5

采用单一 [8/8] rational：

\[
\boxed{T_5(r)=P_8(r)/Q_8(r)}.
\]

升幂系数：

\[
\begin{aligned}
P_8(r)=\;&r
-1.75097804029r^2
+1.13048200179r^3
-0.0846335376902r^4\\
&-0.0337140826189r^5
+0.00762023069439r^6
-0.000634513017411r^7\\
&+0.0000201154758756r^8,
\end{aligned}
\]

\[
\begin{aligned}
Q_8(r)=\;&1
-1.83488765925r
+1.61630171237r^2
-1.05371536507r^3\\
&+0.738658387222r^4
-0.206491596446r^5
+0.0293277836449r^6\\
&-0.00217520309897r^7
+0.0000670515862521r^8.
\end{aligned}
\]

Built-in identities:

\[
T_5(0)=0,\qquad T_5'(0)=1,
\]

and

\[
\lim_{r\to\infty}T_5(r)
=\frac{0.0000201154758756}{0.0000670515862521}=0.3.
\]

这些系数是固定 NC reference 的材料级编译常数；不是 Case21 输入、不是板级拟合、没有使用 Pu。

## 3. T5 stress/tangent 资格证书

在 G21 tensile qualification domain `r in [0,34]`：

\[
\mathrm{RMS}(T_5-T_{NC})=7.13901301334\times10^{-4},
\]

\[
\max|T_5-T_{NC}|=1.4417512854\times10^{-3}.
\]

对材料 tangent：

\[
\mathrm{RMS}(T_5'-T_{NC}')=1.8042476837\times10^{-3},
\]

\[
\max|T_5'-T_{NC}'|=1.326262042\times10^{-2}.
\]

Reference peak:

\[
T_{NC,max}=0.977862112142\quad(r\approx1.2353).
\]

T5 peak:

\[
T_{5,max}=0.977286695152\quad(r\approx1.2415).
\]

因此：`T5_STRESS_GATE=PASS`, `T5_TANGENT_GATE=PASS`。

## 4. T5 full-domain boundedness

`Q8(r)` 在 `r>=0` 无正实根，`P8(r)` 除 `r=0` 外无正实根；`Q8(0)=1` 且最高项系数正，因此 `Q8(r)>0` on `r>=0`。

正实临界点：

\[
1.24147506185,\ 11.1288396233,\ 13.0839965137,\ 18.9730275904,\ 59.1864165939.
\]

对应 T5：

\[
0.977286695419,\ 0.298967319895,\ 0.301300707593,\ 0.299030053539,\ 0.302167321491.
\]

连同 `T5(0)=0` 和 `T5(infinity)=0.3`，得到：

\[
\boxed{0\le T_5(r)<1\quad\forall r\ge0.}
\]

这保证 TC 中 `c*=c(1-tau)>=0`，TT correction 亦全域有界。

## 5. 完整 NC-M5 九宫格（只替换 T_NC -> T5）

令

\[
C(c)=\frac{\kappa c}{1+(\kappa-2)c+c^2},\qquad
\rho=f_t/f_c,\qquad x_{cr}=\rho/\kappa.
\]

CC (`lambda1<0,lambda2<0`):

\[
c_i=-\lambda_i,\qquad h=1+a_{cc}c_1c_2,
\]

\[
s_1=-C(c_1h),\qquad s_2=-C(c_2h).
\]

TC (`lambda1>=0,lambda2<0`):

\[
\tau_1=T_5(\lambda_1/x_{cr}),\qquad c_2=-\lambda_2,
\]

\[
s_1=\rho\tau_1,\qquad s_2=-C[c_2(1-\tau_1)].
\]

CT symmetric.

TT (`lambda1>=0,lambda2>=0`):

\[
\tau_i=T_5(\lambda_i/x_{cr}),
\]

\[
s_1=\rho\tau_1(1-a_t\tau_2^8),\qquad
s_2=\rho\tau_2(1-a_t\tau_1^8).
\]

## 6. 原点 tangent

因为

\[
C(c)=\kappa c+O(c^2),\qquad
\rho T_5(\lambda/x_{cr})=\kappa\lambda+O(\lambda^2),
\]

且 CC correction 为 `O(lambda^3)`, TC correction 为 `O(lambda^2)`, TT correction 为 `O(lambda^9)`，所以四区均有

\[
\boxed{\mathbf K_\lambda(0)=\kappa\mathbf I.}
\]

经过固定 NC plane-stress coordinate map

\[
\mathbf X=\frac{(1-\nu)\mathbf E+\nu\,tr(\mathbf E)\mathbf I}
{(1-\nu^2)\varepsilon_{c0}},
\]

四区统一恢复

\[
\boxed{
\mathbf D_0=\frac{E_0}{1-\nu^2}
\begin{bmatrix}
1&\nu&0\\
\nu&1&0\\
0&0&(1-\nu)/2
\end{bmatrix}.}
\]

`COMMON_ORIGIN_TANGENT=PASS`。

## 7. 有限状态边界：stress continuity PASS

例如 CC-TC 边界 `lambda1=0`, `c=-lambda2>0`：

CC:

\[
s_1=0,\qquad s_2=-C(c).
\]

TC 因 `T5(0)=0`：

\[
s_1=0,\qquad s_2=-C[c(1-0)]=-C(c).
\]

故 stress 精确连续。CC-CT、TC-TT、CT-TT 同理。

## 8. 有限状态边界：tangent continuity FAIL（预登记问题）

该 FAIL 不是 T5 新引入，而是冻结 sector target 未施加 G21 已登记 C1/C2 transition regularization 时的原始 one-sided derivative mismatch。

### 8.1 CC-TC, lambda1=0

CC side:

\[
\boxed{K_{21}^{CC,-}=a_{cc}c^2C'(c).}
\]

TC side，因 `T5'(0)=1`：

\[
\boxed{K_{21}^{TC,+}=\frac{c}{x_{cr}}C'(c).}
\]

一般不相等。

### 8.2 TC-TT, lambda2=0

令 `tau1=T5(lambda1/xcr)`。

TC side:

\[
\boxed{K_{22}^{TC,-}=\kappa(1-\tau_1).}
\]

TT side:

\[
\boxed{K_{22}^{TT,+}=\kappa(1-a_t\tau_1^8).}
\]

一般不相等。

因此：

- `FINITE_FRONT_STRESS_CONTINUITY=PASS`;
- `FINITE_FRONT_TANGENT_CONTINUITY=FAIL` before C1/C2 regularization.

下一步若继续，只能处理已预登记的 sector-front C1/C2 regularization；不能重开 T5/reference/CC/TC/TT/Poisson architecture。

## 9. full-domain gates

- `T5_FULL_DOMAIN_BOUNDEDNESS=PASS`;
- `WITHIN_SECTOR_STRESS_BOUNDEDNESS=PASS`;
- `WITHIN_SECTOR_TANGENT_BOUNDEDNESS=PASS`;
- `FINITE_FRONT_TANGENT_CONTINUITY=FAIL_PENDING_REGISTERED_C1_C2_REGULARIZATION`.

本轮没有计算 Case21 Pu。
