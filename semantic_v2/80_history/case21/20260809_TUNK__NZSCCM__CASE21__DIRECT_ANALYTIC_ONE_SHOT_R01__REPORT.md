# NZ-SCCM Case21 原始目标函数“一次性整体解析求值”测试 R01

**日期：2026-08-09**  
**身份：执行报告；不是新的材料模型，不是 compiler，不改变结构理论。**

## 1. 本轮只测试一个问题

对已经显式展开的 Case21 原始连续目标函数，直接交给现成 CAS 做整体解析积分，检查能否不再人工拆 Lauricella、也不建立材料 compiler，而直接得到可计算的 \(P_c(D,q)\)、\(R_{q,c}(D,q)\)。

正式空间数值积分仍为 0。Gauss/Simpson/adaptive quadrature 未参与本轮正式测试。

## 2. Case21 原始连续函数

采用

\[
C_m=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right),\qquad
C_b=\frac{\pi^2}{2\varepsilon_0}\frac tb q,
\]

\[
e_x=\nu D+C_m\cos^2X\sin^2Y+C_b\sin X\sin Y\,\zeta,
\]
\[
e_y=-D+C_m\sin^2X\cos^2Y+C_b\sin X\sin Y\,\zeta,
\]
\[
g_{xy}=2C_m\sin X\cos X\sin Y\cos Y-2C_b\cos X\cos Y\,\zeta.
\]

\[
X_{11}=\frac{e_x+\nu e_y}{1-\nu^2},\quad
X_{22}=\frac{\nu e_x+e_y}{1-\nu^2},\quad
X_{12}=\frac{g_{xy}}{2(1+\nu)}.
\]

\[
\mu=\frac{X_{11}+X_{22}}2,\quad
\delta=\frac{X_{11}-X_{22}}2,\quad
r=\sqrt{\delta^2+X_{12}^2},\quad
\lambda_\pm=\mu\pm r.
\]

平滑正负坐标

\[
\Pi_\eta(z)=\frac{z^2\bigl(\sqrt{z^2+\eta^2}+z\bigr)}{2(z^2+\eta^2)},
\]

\[
c_i=\Pi_\eta(-\lambda_i),\qquad t_i=\Pi_\eta(\lambda_i),
\]

Saenz 压缩

\[
C_i=\frac{\kappa c_i}{1+(\kappa-2)c_i+c_i^2}.
\]

本轮按较早 Case21 regression package 中 `build_material_coeffs.py` 的来源，采用 Foster 的代数平滑：

\[
H(r,r_0)=\frac12\left[(r-r_0)+\sqrt{(r-r_0)^2+0.05^2}\right]
-\frac12\left[-r_0+\sqrt{r_0^2+0.05^2}\right],
\]

\[
T_i=r_i+(m-1)H(r_i,1)-mH(r_i,10),\qquad r_i=t_i/x_{cr},\qquad m=-7/90.
\]

\[
U_i=\kappa\lambda_i-C_i+\kappa c_i+\rho T_i-\kappa t_i.
\]

二维 interaction：

\[
s_+=U_+-a_{cc}C_+^2C_-+C_+T_- -\rho a_tT_+T_-^8,
\]
\[
s_-=U_--a_{cc}C_-^2C_++C_-T_+ -\rho a_tT_-T_+^8.
\]

因此实际轴向被积函数不是符号占位，而是

\[
\boxed{
\sigma_y=f_c\left[
\frac{s_++s_-}{2}
-\frac{s_+-s_-}{2}
\frac{\delta}{\sqrt{\delta^2+X_{12}^2}}
\right].
}
\]

正式目标

\[
P_c(D,q)=-\frac{bt}{2\pi^2}\iiint\sigma_y\,d\zeta\,dY\,dX,
\]

\[
R_{q,c}(D,q)=\frac{f_c\varepsilon_0b\ell t}{2\pi^2}
\iiint(S_xe_{x,q}+S_ye_{y,q}+T_{xy}g_{xy,q})\,d\zeta\,dY\,dX.
\]

## 3. 一次性 CAS 测试

测试状态取历史 Case21 concrete-only 峰值附近：

\[
D=0.7955,\qquad q=0.001974.
\]

把上述关系逐层真正代入后，`SymPy` 构造出的完整无量纲 \(S_y\) 表达式约含 **29,088 个 symbolic operations**。

第一轮直接执行

```python
sympy.integrate(Syy, (zeta, -1, 1))
```

并保留 \(X,Y\) 为符号变量。此前长测试在约 **120 s** 内没有返回解析结果。

为排除“只是因为 \(X,Y\) 仍为符号”的影响，又把

\[
X=Y=\pi/4
\]

直接代入。此时 \(S_y(\zeta)\) 仍约含 **8,984 个 symbolic operations**；直接厚度积分此前约 **60 s** 仍未返回。2026-08-09 的短重复测试在 15 s 限时内同样未返回，两者均先成功完成表达式构造。

因此，本轮结论不是“积分不存在”，而是：

\[
\boxed{
\text{把完整原函数一次性交给当前 SymPy `integrate`，不能形成可用的实时解析求值器。}
}
\]

而且这已经在比完整 \(P_c,R_{q,c}\) 更简单的子问题——单个 \(\sigma_y\) 的 \(\zeta\) 定积分——上失败，所以没有必要继续让完整三重积分空转。

## 4. 本轮同时发现的来源漂移

当前项目文件中存在两种 tension smoothing 实现：

1. 较早 Case21 regression package：上面的 **代数 Foster 平滑** \(H(r,r_0;0.05)\)；
2. 后来的 direct-quadrature / Swartz24 exploration：用 \(\tfrac12[1+\tanh((t-t_0)/\eta)]\) 做两个 sigmoid blend。

两者不是同一个函数。最近的“直接解析积分阶段稿”把后者写成了当前 NC 原函数，这一步不能继续静默继承。就现有 provenance 而言，较早 regression package 与此前 MSAC 重建所针对的是代数 Foster 平滑；tanh 版本应暂时只登记为后来 exploratory variant，不能混进新的 direct-analytic \(P_u\)。

## 5. 对 \(P_u\) 的处理

用户给出的执行条件是：“如果一次性整体解析求值跑通，就立即求新的 direct-analytic Case21 \(P_u\)。”

本轮 one-shot CAS 没有跑通，因此 **没有生成或宣称新的 formal direct-analytic \(P_u\)**。历史 concrete-only D15 数值 \(P_u\approx339.099\,\mathrm{kN}\) 只保留为历史基线，不冒充本轮结果。

下一次执行不应再人工把每个项一路拆成 Lauricella，也不应重建材料 compiler。正确的最小动作是：仍以这份完整原函数为唯一输入，换用“现成 CAS 能直接接受的局部解析处理”作为求值后端；只在某个具体积分无法闭式返回时对**该实际被积函数**临时做带严格余项的解析展开。该展开无材料身份、无公共材料域、无永久系数表、无 support mask。

## 6. 当前状态

```text
RAW_CASE21_PC_INTEGRAND_EXPLICIT       = YES
RAW_CASE21_RQ_FORMULA_EXPLICIT         = YES
MATERIAL_COMPILER                      = NONE
COMMON_MATERIAL_DOMAIN                 = NONE
SUPPORT_MASK                           = NONE
FORMAL_SPATIAL_QUADRATURE              = 0
ONE_SHOT_SYMPY_FULL_XY_ZETA            = NOT PRACTICALLY EVALUATED
ONE_SHOT_SYMPY_CENTERLINE_ZETA         = NOT PRACTICALLY EVALUATED
NEW_DIRECT_ANALYTIC_CASE21_PU          = NOT GENERATED
HISTORICAL_339.099_KN                  = RETAINED AS BASELINE ONLY
```
