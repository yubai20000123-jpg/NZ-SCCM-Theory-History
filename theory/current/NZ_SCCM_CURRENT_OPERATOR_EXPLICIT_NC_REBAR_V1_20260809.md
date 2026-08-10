# NZ-SCCM：完整显式 current material operator 与钢筋嵌入基线
**日期：2026-08-09**  
**身份：正式材料函数/结构接口冻结候选；不包含积分器，不包含 compiler，不包含材料点离散。**

## 0. 来源边界
本文件只写当前 Case21 成功回归主线所对应的 ordinary-concrete current operator，以及 Nguyen 第3.5节/第5章明确给出的钢筋双线性（本研究中屈服后切线模量取0）关系。

**明确排除：**
- 后来 exploratory direct-quadrature 分支中的 `tanh` 双 sigmoid tension smoothing；
- material common domain；
- Chebyshev/Taylor compiler coefficient tables；
- support mask/PTDC；
- 任何空间 Gauss/Simpson/adaptive quadrature。

普通混凝土 tension law 采用成功 Case21 regression package `build_material_coeffs.py` / `reconstruct_msac_material_only.py` 对应的 **Foster 代数平滑 H(r,r0;0.05)**。

---

# 1. Ordinary concrete current operator \(M_{\rm NC}(\boldsymbol\varepsilon)\)

## 1.1 输入应变
采用工程剪应变 \(\gamma_{xy}\)：

\[
\boldsymbol\varepsilon=
(\varepsilon_x,\varepsilon_y,\gamma_{xy})^T,
\qquad
\mathbf E=
\begin{bmatrix}
\varepsilon_x & \gamma_{xy}/2\\
\gamma_{xy}/2 & \varepsilon_y
\end{bmatrix}.
\]

材料参数：

\[
f_c,\quad E_0,\quad \varepsilon_0,\quad \nu.
\]

定义

\[
\kappa=\frac{E_0\varepsilon_0}{f_c},
\qquad
\rho=0.1,
\qquad
x_{\rm cr}=\frac{\rho}{\kappa},
\qquad
\eta=\frac{x_{\rm cr}}{20}.
\]

Case21：

\[
f_c=21.23\ {\rm MPa},\quad
E_0=20321\ {\rm MPa},\quad
\varepsilon_0=0.00209,\quad
\nu=0.18,
\]

\[
\kappa=2.0005129533678754,
\quad
x_{\rm cr}=0.04998717945397425,
\quad
\eta=0.0024993589726987125.
\]

## 1.2 Equivalent-uniaxial tensor
\[
\mathbf E_u=
\frac{(1-\nu)\mathbf E+\nu\,{\rm tr}(\mathbf E)\mathbf I}
{1-\nu^2},
\]

\[
\mathbf X=\frac{\mathbf E_u}{\varepsilon_0}
=
\begin{bmatrix}
X_{11}&X_{12}\\
X_{12}&X_{22}
\end{bmatrix},
\]

即

\[
X_{11}=
\frac{\varepsilon_x+\nu\varepsilon_y}
{(1-\nu^2)\varepsilon_0},
\]

\[
X_{22}=
\frac{\nu\varepsilon_x+\varepsilon_y}
{(1-\nu^2)\varepsilon_0},
\]

\[
X_{12}=
\frac{\gamma_{xy}}
{2(1+\nu)\varepsilon_0}.
\]

## 1.3 主等效应变
\[
\mu=\frac{X_{11}+X_{22}}2,
\qquad
\delta=\frac{X_{11}-X_{22}}2,
\]

\[
r_X=\sqrt{\delta^2+X_{12}^2},
\]

\[
\lambda_+=\mu+r_X,
\qquad
\lambda_-=\mu-r_X.
\]

## 1.4 Smooth positive/negative coordinates
定义

\[
\Pi_\eta(z)=
\frac{
z^2\left(\sqrt{z^2+\eta^2}+z\right)
}{
2(z^2+\eta^2)
}.
\]

对 \(i\in\{+,-\}\)：

\[
c_i=\Pi_\eta(-\lambda_i),
\qquad
t_i=\Pi_\eta(\lambda_i).
\]

## 1.5 Saenz compression
\[
C_i=
\frac{\kappa c_i}
{1+(\kappa-2)c_i+c_i^2}.
\]

这里 \(C_i\) 为归一化压缩应力幅值。

## 1.6 Foster algebraic tension smoothing
定义固定平滑宽度

\[
\eta_r=0.05.
\]

\[
H(r,r_0)=
\frac12
\left[
(r-r_0)+\sqrt{(r-r_0)^2+\eta_r^2}
\right]
-
\frac12
\left[
-r_0+\sqrt{r_0^2+\eta_r^2}
\right].
\]

定义

\[
m_t=-\frac{1-0.3}{10-1}=-\frac7{90}.
\]

对每个主方向：

\[
r_i=\frac{t_i}{x_{\rm cr}},
\]

\[
T_i=
r_i+(m_t-1)H(r_i,1)-m_tH(r_i,10).
\]

\(T_i\) 是 dimensionless tensile utilization；其归一化 tensile stress 为

\[
\rho T_i.
\]

## 1.7 Uniaxial current master
\[
U_i=
\kappa\lambda_i
-C_i
+\kappa c_i
+\rho T_i
-\kappa t_i.
\]

## 1.8 Biaxial interaction
固定参数：

\[
a_{cc}=0.1072329249362415,
\]

\[
a_t=1-2^{-1/8}
=0.08299595679532878.
\]

主方向归一化应力：

\[
s_+
=
U_+
-a_{cc}C_+^2C_-
+C_+T_-
-\rho a_tT_+T_-^8,
\]

\[
s_-
=
U_-
-a_{cc}C_-^2C_+
+C_-T_+
-\rho a_tT_-T_+^8.
\]

至此 ordinary-concrete material physics 已全部写完；不存在另外的 \(M(\varepsilon)\) 黑箱。

## 1.9 从主方向返回全局应力
当 \(r_X>0\)：

\[
S_{xx}
=
\frac{s_++s_-}{2}
+
\frac{s_+-s_-}{2}
\frac{\delta}{r_X},
\]

\[
S_{yy}
=
\frac{s_++s_-}{2}
-
\frac{s_+-s_-}{2}
\frac{\delta}{r_X},
\]

\[
S_{xy}
=
\frac{s_+-s_-}{2}
\frac{X_{12}}{r_X}.
\]

物理应力：

\[
\boxed{
\sigma_x=f_cS_{xx},\qquad
\sigma_y=f_cS_{yy},\qquad
\tau_{xy}=f_cS_{xy}.
}
\]

因此

\[
\boxed{
M_{\rm NC}:
(\varepsilon_x,\varepsilon_y,\gamma_{xy})
\mapsto
(\sigma_x,\sigma_y,\tau_{xy})
}
\]

就是上面 1.1--1.9 的完整复合函数。

当 \(r_X=0\) 时，\(\lambda_+=\lambda_-=\mu\)，两主方向材料响应相同；采用上述谱函数的连续极限：

\[
\sigma_x=\sigma_y=f_c\,s(\mu,\mu),
\qquad
\tau_{xy}=0.
\]

---

# 2. Case21 连续运动学嵌入

\[
X=\frac{\pi x}{b},
\qquad
Y=\frac{\pi y}{\ell},
\qquad
\zeta=\frac{2z}{t},
\]

\[
q=\frac Ab,\qquad q_0=\frac{A_0}{b},
\]

\[
C_m=
\frac{\pi^2}{\varepsilon_0}
\left(q_0q+\frac12q^2\right),
\]

\[
C_b=
\frac{\pi^2}{2\varepsilon_0}\frac tb q
\qquad (b=\ell\ {\rm for\ Case21}),
\]

\[
e_x=
\nu D+
C_m\cos^2X\sin^2Y+
C_b\sin X\sin Y\,\zeta,
\]

\[
e_y=
-D+
C_m\sin^2X\cos^2Y+
C_b\sin X\sin Y\,\zeta,
\]

\[
g_{xy}
=
2C_m\sin X\cos X\sin Y\cos Y
-
2C_b\cos X\cos Y\,\zeta.
\]

\[
\varepsilon_x=\varepsilon_0e_x,\qquad
\varepsilon_y=\varepsilon_0e_y,\qquad
\gamma_{xy}=\varepsilon_0g_{xy}.
\]

将这三个显式函数直接代入第1节 \(M_{\rm NC}\)，即得到完整连续应力场；无需 material points。

---

# 3. Concrete structural contributions

轴向荷载：

\[
\boxed{
P_c(D,q)=
-\frac{bt}{2\pi^2}
\int_0^\pi\int_0^\pi\int_{-1}^{1}
\sigma_y(X,Y,\zeta;D,q)
\,d\zeta\,dY\,dX.
}
\]

这里 \(\sigma_y\) 不是未定义函数，而是第1节全部复合关系代入第2节运动学后的显式函数。

定义

\[
C_{m,q}=
\frac{\pi^2}{\varepsilon_0}(q_0+q),
\qquad
C_{b,q}=
\frac{\pi^2}{2\varepsilon_0}\frac tb,
\]

\[
e_{x,q}
=
C_{m,q}\cos^2X\sin^2Y
+
C_{b,q}\sin X\sin Y\,\zeta,
\]

\[
e_{y,q}
=
C_{m,q}\sin^2X\cos^2Y
+
C_{b,q}\sin X\sin Y\,\zeta,
\]

\[
g_{xy,q}
=
2C_{m,q}\sin X\cos X\sin Y\cos Y
-
2C_{b,q}\cos X\cos Y\,\zeta.
\]

则

\[
\boxed{
R_{q,c}(D,q)=
\frac{\varepsilon_0b\ell t}{2\pi^2}
\int_0^\pi\int_0^\pi\int_{-1}^{1}
\left[
\sigma_x e_{x,q}
+\sigma_y e_{y,q}
+\tau_{xy}g_{xy,q}
\right]
\,d\zeta\,dY\,dX.
}
\]

正式空间 quadrature 点数：

\[
\boxed{N_{\rm formal\ spatial\ quadrature}=0.}
\]

---

# 4. Reinforcement current operator \(M_s(\varepsilon_s)\)

Nguyen 第3.5节给出 bilinear reinforcement law；本研究取 post-yield tangent modulus

\[
E_w=0.
\]

Swartz 24 板统一钢筋参数：

\[
E_s=200000\ {\rm MPa},
\]

\[
\varepsilon_y=0.00265,
\]

\[
f_y=E_s\varepsilon_y=530\ {\rm MPa},
\]

\[
\varepsilon_f=0.04.
\]

因此在 source-defined range \(|\varepsilon_s|\le\varepsilon_f\)：

\[
\boxed{
M_s(\varepsilon_s)=
\sigma_s(\varepsilon_s)=
\begin{cases}
E_s\varepsilon_s,
&
|\varepsilon_s|\le\varepsilon_y,
\\[2mm]
f_y\,{\rm sgn}(\varepsilon_s),
&
\varepsilon_y<|\varepsilon_s|\le\varepsilon_f.
\end{cases}
}
\]

Nguyen 给出了 failure strain \(0.04\)，但没有在这一来源关系中定义 \(|\varepsilon_s|>\varepsilon_f\) 后的新应力支；因此这里**不添加 post-failure branch**。若达到该事件，求解器必须显式报告 source-defined steel range exhausted。

对任意钢筋方向

\[
\mathbf n=(\cos\theta,\sin\theta)^T,
\]

连续钢筋应变：

\[
\boxed{
\varepsilon_s=
\mathbf n^T\mathbf E\,\mathbf n
=
\varepsilon_x\cos^2\theta
+\varepsilon_y\sin^2\theta
+\gamma_{xy}\sin\theta\cos\theta.
}
\]

---

# 5. 钢筋贡献直接嵌入总体系

对第 \(r\) 根/族钢筋 \(\Gamma_r\)，面积 \(A_{s,r}\)、方向 \(\mathbf n_r\)：

\[
\varepsilon_s^{(r)}
=
\mathbf n_r^T\mathbf E\,\mathbf n_r,
\]

\[
\sigma_s^{(r)}
=
M_s(\varepsilon_s^{(r)}).
\]

对加载方向 \(y\) 的钢筋族：

\[
\boxed{
P_s=
-\sum_{r\parallel y}
\frac{A_{s,r}}{\ell}
\int_{\Gamma_r}
\sigma_s^{(r)}\,ds.
}
\]

所有 \(x/y\) 钢筋族共同进入幅值平衡：

\[
\boxed{
R_{q,s}
=
\sum_r A_{s,r}
\int_{\Gamma_r}
\sigma_s^{(r)}
\frac{\partial\varepsilon_s^{(r)}}{\partial q}
\,ds.
}
\]

总 RC 体系直接写成

\[
\boxed{
P=P_c+P_s,
\qquad
R_q=R_{q,c}+R_{q,s}.
}
\]

极限条件：

\[
\boxed{
R_q(D,q)=0,
}
\]

\[
\boxed{
L(D,q)
=
P_{,D}R_{q,q}
-
P_{,q}R_{q,D}
=0.
}
\]

不得使用

\[
P_u=P_{u,c}+A_sf_y
\]

作为正式极限承载力。

---

# 6. Case21 reinforcement mapping

Swartz/Nguyen：reinforcement 为 isotropic two-way mesh。Table 5.1 的

\[
p=0.75\%
\]

是 nominal total steel ratio；Case21 为一层、\(h_r=0\)。

项目统一映射：

\[
\rho_{s,{\rm dir,layer}}
=
\frac{p}{2n_{\rm layers}}.
\]

所以 Case21：

\[
\boxed{
\rho_{s,x}=\rho_{s,y}=0.00375,
\qquad z_s=0.
}
\]

这只确定钢筋材料/面积密度接口；具体连续线族的积分仍由同一板运动学直接生成，不引入钢筋 Gauss points。

---

# 7. Steel-shell slot

当前 NZ-SCCM 主线尚未冻结一个来源明确的 steel-shell current law \(M_{\rm shell}\)。  
因此本文件**不擅自填入**理想弹塑、Ramberg--Osgood 或其他钢壳本构。

结构接口保留为

\[
P_{\rm shell}
=
-\int_{\Omega_s}\sigma_{y,s}\,dA,
\]

\[
R_{q,\rm shell}
=
\int_{\Omega_s}
\boldsymbol\sigma_s^T
\boldsymbol\varepsilon_{,q}\,dA,
\]

但在 \(M_{\rm shell}\) 来源冻结以前：

\[
\boxed{M_{\rm shell}=\text{UNSPECIFIED BY CURRENT LOCKED SOURCE}.}
\]

这不是遗漏，而是为了遵守“不添加”。

---

# 8. 以后数学求解器的输入

求解工具只能接收以上已显式定义的函数：

\[
\boxed{
M_{\rm NC},\quad M_s,\quad
P_c,\quad R_{q,c},\quad
P_s,\quad R_{q,s}.
}
\]

工具可以使用：
- 直接符号积分；
- 已有特殊函数；
- rule-based integration；
- 精确代数化简；
- 任意精度特殊函数评价；
- 严格 ball/interval arithmetic 作为误差证书；
- 必要时对当前实际 integrand 做临时有限解析展开并给余项。

工具不得把正式结果替换为空间材料点求和。
