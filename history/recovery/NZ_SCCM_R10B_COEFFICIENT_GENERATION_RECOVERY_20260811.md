# NZ-SCCM R10B 系数生成链恢复与可重复性边界

**日期：2026-08-11**  
**身份：RECOVERY / REPRODUCIBILITY NOTE；不改变 R10/R10B 当前理论与 Case21 已冻结结果。**

## 0. 重要更正

上一版将 `N=48` 进一步统计为 `3×49=147` 个所谓“一级材料编译系数”。这一统计**不应进入 R10B 的正式表述，现撤回**。

原因有二：

1. R10B 原执行报告中的 `material degree = 48` 是**统一的材料解析展开阶次**，不是“总系数个数”；
2. 已恢复的原 `00_R10B_report.md` 明确对 `U、C、T、T^7` 四个 scalar objects 给出 N=48 表示误差，因此把原执行存储结构擅自简化成 `U/C/T 三组 × 49` 没有证据基础。

正式论文/报告统一只写：

```text
material approximation order N_m = 48
```

若以后需要报告实际 coefficient-array 数量，必须以恢复的原 core / coefficient file 为准，不再从阶次自行推导“147”等总数。

---

# 1. 当前能够确定恢复的物理函数

Case21 普通混凝土参数：

\[
f_c=21.23\,\mathrm{MPa},\qquad E_0=20321\,\mathrm{MPa},\qquad
\varepsilon_0=0.00209,\qquad \nu=0.18,
\]

\[
\rho=0.1,
\qquad
\kappa=\frac{E_0\varepsilon_0}{f_c}=2.0005129533678754,
\]

\[
x_{cr}=\frac{\rho}{\kappa}=0.04998717945397425,
\qquad
\eta=\frac{x_{cr}}{20}=0.0024993589726987125.
\]

定义

\[
\Pi_\eta(z)=
\frac{z^2\left(\sqrt{z^2+\eta^2}+z\right)}{2(z^2+\eta^2)},
\]

\[
t(\lambda)=\Pi_\eta(\lambda),\qquad
c(\lambda)=\Pi_\eta(-\lambda).
\]

压缩 scalar：

\[
\boxed{
C(\lambda)=
\frac{\kappa c(\lambda)}
{1+(\kappa-2)c(\lambda)+c(\lambda)^2}
}.
\]

R10 只平滑 tensile scalar。材料功条件给出

\[
W_{src}=0.031741235181249904,
\qquad u_r=0.03,
\]

\[
\boxed{
h=\frac15\left[
\frac{W_{src}}{x_{cr}}-\frac{\rho}{10}-\frac92u_r
\right]
=0.09799750427197301.}
\]

当 \(0\le t\le x_{cr}\)，令 \(\tau=t/x_{cr}\)：

\[
\boxed{
 u_{rise}(t)=
\rho\tau+(10h-6\rho)\tau^3
+(8\rho-15h)\tau^4
+(6h-3\rho)\tau^5.
}
\]

当 \(x_{cr}\le t\le10x_{cr}\)，令

\[
\tau_f=\frac{t-x_{cr}}{9x_{cr}},
\]

则

\[
\boxed{
 u_{fall}(t)=
h+(u_r-h)(10\tau_f^3-15\tau_f^4+6\tau_f^5).
}
\]

定义 \(u_{sm}(t)\) 为上述两段函数，则

\[
\boxed{T(\lambda)=\frac{u_{sm}[t(\lambda)]}{\rho}},
\]

\[
\boxed{
U(\lambda)=
\kappa\lambda-C(\lambda)+\kappa c(\lambda)
+u_{sm}[t(\lambda)]-\kappa t(\lambda).
}
\]

R10B 原报告实际审计的四个一维对象是

\[
\boxed{F(\lambda)\in\{U(\lambda),C(\lambda),T(\lambda),T(\lambda)^7\}.}
\]

这四个对象不是四组独立物理参数；它们都由同一个冻结 R10 材料关系派生。

---

# 2. Case21 的认证谱域与统一 Chebyshev 坐标

R10B 解析认证：

\[
\lambda_+\in[-0.0956591,0.1029458],
\qquad
\lambda_-\in[-1.0029458,-0.6843409].
\]

采用安全编译带：

\[
I_+=[-0.10,0.105],
\qquad
I_-=[-1.01,-0.68].
\]

两个实际需要逼近的区域是其并集

\[
\boxed{\mathcal I=I_-\cup I_+.}
\]

为保持一个统一多项式坐标，使用外包 hull

\[
[\lambda_a,\lambda_b]=[-1.01,0.105].
\]

于是

\[
\lambda_c=\frac{\lambda_a+\lambda_b}{2}=-\frac{181}{400},
\qquad
\lambda_s=\frac{\lambda_b-\lambda_a}{2}=\frac{223}{400},
\]

\[
\boxed{
\xi(\lambda)=\frac{\lambda-\lambda_c}{\lambda_s}
=\frac{400\lambda+181}{223}.
}
\]

正式 N48 形式写为

\[
\boxed{
F_{48}(\lambda)=\sum_{n=0}^{48}a_n^{(F)}T_n[\xi(\lambda)].
}
\]

这里 `48` 是最高 Chebyshev degree。论文正文不再把它改写成一个“总 coefficient count”。

---

# 3. 系数生成问题的完整数学形式

当前原执行报告明确说明：material-coordinate samples 只用于生成有限解析 coefficients，不是空间样点；但原 `07_R10B_zero_spatial_compiler_core.py` 与原 coefficient arrays 尚未恢复。因此原执行中**样点数、样点权重、线性求解/正则化细节**仍不能逐字确认。

但是系数生成的数学问题可以完整写到下列层次。

设编译材料坐标样本为

\[
\Lambda=\{\lambda_j\}_{j=1}^{M}\subset\mathcal I,
\]

权重为 \(w_j>0\)。定义

\[
\xi_j=\frac{400\lambda_j+181}{223},
\]

以及 Chebyshev 设计矩阵

\[
\boxed{V_{jn}=T_n(\xi_j),\qquad n=0,\ldots,48.}
\]

对任一

\[
F\in\{U,C,T,T^7\},
\]

材料向量为

\[
f_j^{(F)}=F(\lambda_j).
\]

若采用与原执行数值指纹一致的离散加权最小二乘结构，则系数向量

\[
\mathbf a^{(F)}=
[a_0^{(F)},a_1^{(F)},\ldots,a_{48}^{(F)}]^T
\]

由

\[
\boxed{
\mathbf a^{(F)}
=\arg\min_{\mathbf a}
\sum_{j=1}^{M}w_j
\left[
F(\lambda_j)-\sum_{n=0}^{48}a_nT_n(\xi_j)
\right]^2
}
\]

确定。

令

\[
W=\operatorname{diag}(w_1,\ldots,w_M),
\]

则正规方程为

\[
\boxed{(V^TWV)\mathbf a^{(F)}=V^TW\mathbf f^{(F)}.}
\]

逐项完全展开为

\[
\boxed{
\sum_{m=0}^{48}G_{nm}a_m^{(F)}=b_n^{(F)},
\qquad n=0,1,\ldots,48,
}
\]

其中

\[
\boxed{
G_{nm}=\sum_{j=1}^{M}w_jT_n(\xi_j)T_m(\xi_j),
}
\]

\[
\boxed{
b_n^{(F)}=\sum_{j=1}^{M}w_jF(\lambda_j)T_n(\xi_j).}
\]

因此 49 条方程的首、次、末行分别是

\[
G_{00}a_0+G_{01}a_1+\cdots+G_{0,48}a_{48}=b_0,
\]

\[
G_{10}a_0+G_{11}a_1+\cdots+G_{1,48}a_{48}=b_1,
\]

\[
\vdots
\]

\[
G_{48,0}a_0+G_{48,1}a_1+\cdots+G_{48,48}a_{48}=b_{48}.
\]

这不是“黑箱拟合”：一旦 \(\lambda_j,w_j\) 被固定，每个 \(G_{nm}\)、每个 \(b_n^{(F)}\)、每个 \(a_n^{(F)}\) 都由材料参数唯一生成。

数值实现应采用 QR/SVD 解最小二乘而不是显式求 \((V^TWV)^{-1}\)，但论文中的定义式仍是上面的正规方程。

---

# 4. 每个右端项如何由材料参数逐层生成

对任意样本 \(\lambda_j\)，先计算

\[
A_j=\sqrt{\lambda_j^2+\eta^2},
\]

\[
\boxed{
c_j=
\frac{\lambda_j^2(A_j-\lambda_j)}{2(\lambda_j^2+\eta^2)},
\qquad
t_j=
\frac{\lambda_j^2(A_j+\lambda_j)}{2(\lambda_j^2+\eta^2)}.}
\]

然后

\[
\boxed{
C_j=\frac{\kappa c_j}
{1+(\kappa-2)c_j+c_j^2}.}
\]

若 \(t_j\le x_{cr}\)，令

\[
\tau_j=\frac{t_j}{x_{cr}},
\]

则

\[
\boxed{
u_j=
\rho\tau_j+(10h-6\rho)\tau_j^3
+(8\rho-15h)\tau_j^4
+(6h-3\rho)\tau_j^5.}
\]

若 \(x_{cr}<t_j\le10x_{cr}\)，令

\[
\tau_{f,j}=\frac{t_j-x_{cr}}{9x_{cr}},
\]

则

\[
\boxed{
u_j=
h+(u_r-h)(10\tau_{f,j}^3-15\tau_{f,j}^4+6\tau_{f,j}^5).}
\]

随后

\[
\boxed{T_j=\frac{u_j}{\rho},}
\]

\[
\boxed{
U_j=\kappa\lambda_j-C_j+\kappa c_j+u_j-\kappa t_j,
}
\]

\[
\boxed{T_j^{(7)}=T_j^7.}
\]

于是四组右端项完全写为

\[
\boxed{
b_n^{(U)}=\sum_jw_jU_jT_n(\xi_j),}
\]

\[
\boxed{
b_n^{(C)}=\sum_jw_jC_jT_n(\xi_j),}
\]

\[
\boxed{
b_n^{(T)}=\sum_jw_jT_jT_n(\xi_j),}
\]

\[
\boxed{
b_n^{(T^7)}=\sum_jw_jT_j^7T_n(\xi_j).}
\]

这已经把“材料参数 -> N48 系数”的代数链完全展开到唯一尚缺的历史实现数据 \(\{\lambda_j,w_j\}\)。

---

# 5. 本次 forensic numerical fingerprint

在不使用任何 Case21 试验荷载的前提下，本次独立重建做了以下检查：

- 使用同一个 hull `[-1.01,0.105]` 定义 Chebyshev 坐标；
- 只在两个认证谱带 `I_- ∪ I_+` 上给材料函数值；
- 对 `U,C,T,T^7` 各做 degree-48 Chebyshev least-squares；
- 在两个认证带上独立密集验证。

得到的误差与原 R10B 报告非常接近：

| scalar | 原 R10B max | forensic LS max | 原 R10B P95 | forensic LS P95 |
|---|---:|---:|---:|---:|
| U | 0.000200 | 0.000197 | 0.000138 | 0.000139 |
| C | 0.002895 | 0.002823 | 0.000712 | 0.000686 |
| T | 0.027887 | 0.027194 | 0.006928 | 0.006638 |
| T^7 | 0.027497 | 0.026180 | 0.017399 | 0.016341 |

这构成了一个很强的**数值指纹证据**：原 R10B 的 N48 material compiler 与“在两条认证谱带并集上建立一个统一 hull-coordinate 的 degree-48 Chebyshev least-squares representation”高度一致。

但因为误差没有逐位重合，所以在找回原 core 前，仍不得把本次 forensic LS 的具体样点数/权重冒充原执行设置。

正式证据身份：

```text
R10B_N48_LEAST_SQUARES_UNION_BAND_ARCHITECTURE = STRONGLY_SUPPORTED
ORIGINAL_SAMPLE_COUNT_AND_WEIGHTING             = UNRESOLVED
ORIGINAL_COEFFICIENT_ARRAYS                      = UNRECOVERED
BYTE_IDENTICAL_R10B_COMPILER_CORE                = UNRECOVERED
```

---

# 6. N48 后如何进入二维 current map

对任一 scalar polynomial

\[
F_{48}(Y)=\sum_{n=0}^{48}a_n^{(F)}T_n(Y),
\]

令

\[
K_1=\operatorname{tr}Y,\qquad K_2=\det Y,
\]

二维 Cayley-Hamilton：

\[
Y^2-K_1Y+K_2I=0.
\]

写

\[
T_n(Y)=A_nI+B_nY.
\]

初值

\[
(A_0,B_0)=(1,0),\qquad(A_1,B_1)=(0,1),
\]

递推

\[
\boxed{A_{n+1}=-2K_2B_n-A_{n-1},}
\]

\[
\boxed{B_{n+1}=2A_n+2K_1B_n-B_{n-1}.}
\]

因此

\[
\boxed{
F_{48}(Y)=
\left(\sum_{n=0}^{48}a_n^{(F)}A_n\right)I+
\left(\sum_{n=0}^{48}a_n^{(F)}B_n\right)Y.}
\]

后续采用原 R10B pair algebra：

\[
(A,B)(C,D)=
(AC-BDK_2,\ AD+BC+BDK_1),
\]

\[
CC=\det(C)C,
\]

\[
TC=C[\operatorname{tr}(T)I-T],
\]

\[
TT=\det(T)[\operatorname{tr}(T^7)I-T^7],
\]

\[
\boxed{S=U-a_{cc}CC+TC-\rho a_tTT.}
\]

该步骤不做二维材料面重新拟合。

---

# 7. 正式论文/报告的最低可重复性要求

若 R10B 要作为正式论文计算方法，而不是仅作为历史成功计算记录，则材料 N48 部分至少必须公开：

1. \(I_-\)、\(I_+\) 与统一 hull；
2. \(\xi(\lambda)\) 的坐标映射；
3. `U,C,T,T^7` 的材料来源公式；
4. 完整 coefficient equation，即本文件第 3–4 节；
5. 原样点生成式 \(\lambda_j\)、样点数 \(M\)、权重 \(w_j\)；
6. N48 numerical coefficient table（可放 Supplementary Material，不必塞进正文）；
7. N48 material error table；
8. coefficient -> Cayley-Hamilton -> D15 moment 的递推式。

因此，**当前还不能声称“R10B 系数生成已达到论文级完全可重复”**。现在已经恢复的是除第 5–6 项外的全部数学链，并通过数值指纹把原生成器强烈定位到 two-band unified-hull Chebyshev least-squares family。

下一步若找不到原 `07_R10B_zero_spatial_compiler_core.py`，则必须在不改变 R10 材料物理的前提下，重新冻结一个显式 \(\lambda_j,w_j\) contract，重编译 N48、重算 Case21，并要求其 P/R/root 与当前 R10B 工程基线一致后，才能把新的 fully reproducible coefficient table 作为正式论文版本。
