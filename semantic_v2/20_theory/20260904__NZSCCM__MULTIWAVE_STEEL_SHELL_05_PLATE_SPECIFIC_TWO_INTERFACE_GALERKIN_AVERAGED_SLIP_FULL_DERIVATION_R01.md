# NZ-SCCM 多波钢壳05——板专用双界面平均剪切滑移版本：完整推导 R01

> 日期：2026-09-04  
> 分支：`diagnostic/bh032-bh050-mode-projection-20260827`  
> 身份：`DIAGNOSTIC THEORY / THEORY-DEVELOPMENT / NOT PRODUCTION R14`  
> 父体系：R14 整体稳定骨架 + Multiwave Steel Shell 01 局部钢壳 + R02/R06 + UHPC/web 解析截面积分 + R4  
> 取代范围：仅取代 02/04 中“连接刚度 → 平均滑移/组合程度”的构造。  
> 明确撤回：旧02的 `Kr=75.835 kN/mm/rib` 物理刚度身份、`gamma=KP/(KP+Keq)`；04-R01 直接移植组合梁 SLS 刚度折减公式的 `0.81,36,0.4,3` 系数链。  
> 不修改：production R14。

---

## 0. 方法论：从具体物理对象出发，而不是从既有公式出发

05采用以下证据顺序：

1. 先固定真实对象：双钢面、UHPC核心、纵向无孔加劲肋、轴向受压、板局部/整体屈曲、上下两界面可能发生有限滑移。
2. 再写守恒与兼容：总轴力守恒、界面剪流与滑移关系、钢面与核心的纵向应变兼容。
3. 再写数学降阶：只把已经由原板稳定方程算出的整体模态作为已知空间基，做Galerkin平均；不让滑移模块自行选择整体模态。
4. 最后才引用文献：Nie & Cai (2003) 只作为“partial interaction 可由平衡+兼容凝聚成等效刚度”的一般依据；不复制其组合梁最终经验/半经验系数。钢-UHPC界面试验只提供界面本构类型和参数量级，不把不同表面处理的数值冒充当前无孔肋的实测参数。

因此05的最终平均系数必须由本结构自己的方程推导出来，而不是先指定一个 `gamma` 或 `chi`。

---

# Part I 原整体板稳定：m 必须算出来，不允许直接指定

## 1. 几何与初始板刚度

定义：

\[
\rho_w=\frac{A_w}{b t_c}.
\]

钢面 plane-stress 刚度：

\[
Q_s=\frac{E_s}{1-\nu_s^2}.
\]

UHPC 初始 plane-stress 刚度：

\[
Q_c=\frac{E_c}{1-\nu_c^2}.
\]

剪切模量：

\[
G_s=\frac{E_s}{2(1+\nu_s)},
\qquad
G_c=\frac{E_c}{2(1+\nu_c)}.
\]

钢面中面距截面中面：

\[
z_f=\frac{t_c+t_s}{2}.
\]

膜刚度：

\[
A_{11}=2t_sQ_s+(1-\rho_w)t_cQ_c,
\]

\[
A_{22}=2t_sQ_s+(1-\rho_w)t_cQ_c+\rho_w t_c E_s,
\]

\[
A_{12}=2t_s\nu_sQ_s+(1-\rho_w)t_c\nu_cQ_c.
\]

钢面弯曲贡献：

\[
D_f=2Q_s\left(\frac{t_s^3}{12}+t_s z_f^2\right).
\]

UHPC弯曲贡献：

\[
D_c=(1-\rho_w)Q_c\frac{t_c^3}{12}.
\]

纵向web/PBL钢面积在原R14初始刚度中的贡献：

\[
D_w=\rho_w E_s\frac{t_c^3}{12}.
\]

因此：

\[
D_x=D_f+D_c,
\]

\[
D_y=D_f+D_c+D_w,
\]

\[
D_\mu=\nu_sD_f+\nu_cD_c.
\]

扭转刚度：

\[
D_{66}=2G_s\left(\frac{t_s^3}{12}+t_s z_f^2\right)+(1-\rho_w)G_c\frac{t_c^3}{12}.
\]

定义：

\[
H=D_\mu+2D_{66}.
\]

## 2. 整体候选模态

横向只取一个整板半波：

\[
\alpha=\frac{\pi}{b}.
\]

纵向候选整数半波数为：

\[
m=1,2,3,\ldots
\]

对应：

\[
\beta_m=\frac{m\pi}{a}.
\]

原板稳定临界纵向膜力：

\[
N_{y,cr}^{(m)}=
\frac{D_x\alpha^4+2H\alpha^2\beta_m^2+D_y\beta_m^4}{\beta_m^2}.
\]

整板临界荷载：

\[
P_{cr}^{(m)}=bN_{y,cr}^{(m)}.
\]

因此真实整体模态定义为：

\[
\boxed{m^*=\arg\min_{m\in\mathbb N^+}P_{cr}^{(m)}}.
\]

05绝不把 `m=2` 当输入常数。

## 3. 长宽比只解释趋势，不替代求解

令：

\[
\lambda=\frac{a}{b}.
\]

则：

\[
N_{y,cr}^{(m)}=
\frac{\pi^2}{b^2}
\left[
\frac{\lambda^2D_x}{m^2}+2H+\frac{m^2D_y}{\lambda^2}
\right].
\]

若暂把m连续化：

\[
\frac{dN_{y,cr}}{dm}=0
\]

给出：

\[
-\frac{2\lambda^2D_x}{m^3}+\frac{2mD_y}{\lambda^2}=0,
\]

即：

\[
m^4=\lambda^4\frac{D_x}{D_y}.
\]

故连续极小点：

\[
\boxed{m_c=\lambda\left(\frac{D_x}{D_y}\right)^{1/4}}.
\]

BH系列中 \(\lambda=2\) 且 \(D_x\approx D_y\)，所以 `m_c≈2`，但最终仍必须逐个整数比较。

当前已复核：BH032 `m_c=1.98991`，整数候选 `Pcr(m=1,2,3,4)=47.61390, 30.60352, 36.08402, 48.19705 MN`，故 `m*=2`；BH050 `m_c=1.99353`，候选 `30.51308, 19.58188, 23.05007, 30.75194 MN`，故 `m*=2`。T120/T360同样由公式得到 `m*=2`，不是先验指定。

## 4. 代表完整整体半波与局部波数

一旦 `m*` 已由上式算出：

\[
L_G=\frac{a}{m^*}.
\]

标准同宽格室宽度为：

\[
L_x=s.
\]

基本局部鼓波数：

\[
\boxed{n_0=\left\lfloor\frac{L_G}{s}\right\rfloor}.
\]

候选：

\[
\boxed{n\in\{n_0-1,n_0,n_0+1\}}.
\]

对当前BH，`m*=2`、`a=2b`，故 `L_G=b`，且 `s=0.225b`，因此 `n0=4`，候选为 `3/4/5`。

此处先完成整体稳定和局部波数选择，然后才进入界面滑移。05中的滑移模块不能反过来改变 `m*` 或 `n`。

---

# Part II 连接器物理模块：只把真实连接构造转换成单位长度剪切刚度

## 5. 当前无孔纵向肋

当前加劲肋没有开孔。采用局部线性界面关系：

\[
\boxed{\tau=K_t s}
\]

其中：

- \(\tau\)：钢-UHPC界面切向应力，N/mm²；
- \(s\)：界面相对滑移，mm；
- \(K_t\)：单位界面面积切向刚度，N/mm³。

一根纵肋净高 \(h_r\)，只计其两个侧面。纵向微段 \(dy\) 的有效接触面积：

\[
dA_b=2h_r\,dy.
\]

微段剪力：

\[
dV=\tau dA_b=2h_rK_t s\,dy.
\]

单位长度剪流：

\[
q_r=\frac{dV}{dy}=2h_rK_t s.
\]

因此一根无孔肋的单位长度连接刚度：

\[
\boxed{k_{\ell,r}^{plain}=2h_rK_t}.
\]

量纲：

\[
[k_{\ell,r}]=\mathrm{N/mm^2}.
\]

TOP与BOTTOM：

\[
\boxed{k_+=N_r^+ k_{\ell,r}},
\qquad
\boxed{k_-=N_r^- k_{\ell,r}}.
\]

05-R01不把钢面整幅内表面自然粘结面积额外并入，避免在没有来源锁定前放大连接能力；当前只隔离“纵向无孔肋两个侧面”的连接贡献。

## 6. 未来PBL接口

若改成开孔PBL，一孔初始剪切刚度：

\[
k_{ps}\quad [\mathrm{N/mm/hole}].
\]

孔距：

\[
p_h.
\]

则一条PBL肋的单位长度刚度：

\[
\boxed{k_{\ell,r}^{PBL}=\frac{k_{ps}}{p_h}}.
\]

用户给出的开孔连接件公式可作为PBL连接器源之一：

\[
k_{ps}=23.4\sqrt{(d-d_s)d_sE_cf_{ck}}.
\]

只有当该 `kps` 的试验/公式定义不已包含额外自然粘结、摩擦等总效应时，才允许与 `2hrKt` 独立相加；否则只替换 connector-source block，防止重复计算。

---

# Part III 05核心：从本板自己的守恒、兼容和界面本构推导双界面滑移方程

## 7. 三个轴向相：TOP钢面、核心、BOTTOM钢面

定义三个相的纵向轴向位移修正：

\[
r_+(y),\qquad r_c(y),\qquad r_-(y).
\]

它们不是总位移，而是相对于原R14完全组合板运动学的附加轴向位移。

原R14完全组合的纵向应变场在三个相形心处为：

\[
\varepsilon_{y,+}^{FC}=\varepsilon_y^0+z_f\kappa_y(y),
\]

\[
\varepsilon_{y,c}^{FC}=\varepsilon_y^0,
\]

\[
\varepsilon_{y,-}^{FC}=\varepsilon_y^0-z_f\kappa_y(y).
\]

加入滑移修正后：

\[
\boxed{\varepsilon_{y,+}=\varepsilon_y^0+z_f\kappa_y+r_+'},
\]

\[
\boxed{\varepsilon_{y,c}=\varepsilon_y^0+r_c'},
\]

\[
\boxed{\varepsilon_{y,-}=\varepsilon_y^0-z_f\kappa_y+r_-'}.
\]

这里 `'` 表示对纵向坐标y求导。

## 8. 两个界面滑移

因为 `r_i` 已经是相对于完全组合基准的修正，所以界面实际附加滑移就是：

\[
\boxed{s_+=r_+-r_c},
\]

\[
\boxed{s_-=r_--r_c}.
\]

界面剪流：

\[
\boxed{q_+=k_+s_+},
\]

\[
\boxed{q_-=k_-s_-}.
\]

## 9. 三相纵向切线刚度

05-R01先采用初始弹性纵向相刚度，保持理论身份清楚，不把尚未闭合的current material tangent偷偷塞进连接层。

一般形式：

\[
\mathcal K_+>0,\qquad \mathcal K_c>0,\qquad \mathcal K_->0,
\]

单位均为N。

当前R01的基础分配采用：

\[
\boxed{\mathcal K_+=Q_sbt_s},
\qquad
\boxed{\mathcal K_-=Q_sbt_s}.
\]

核心纵向刚度沿用R14截面分解：

\[
\boxed{\mathcal K_c=(1-\rho_w)Q_cbt_c+E_sA_w}.
\]

这一选择的含义是：05-R01不重新分配原R14的纵向web/PBL钢面积；它继续属于原核心/纵向web模块。若后续来源锁定表明具体纵肋轴向刚度应归入TOP/BOTTOM钢相，则只修改 `K+`,`K-`,`Kc` 的相分配，不改后面的守恒—兼容结构。

## 10. 只保留与滑移有关的轴向能量

除去共同中面应变 \(\varepsilon_y^0\) 所对应且与相对滑移无关的常数能量，05的相对轴向—连接能量写为：

\[
\boxed{
\begin{aligned}
\Pi_{PI}=
\frac12\int
&\mathcal K_+\left(r_+'+z_f\kappa_y\right)^2
+\mathcal K_c(r_c')^2
+\mathcal K_-\left(r_-'-z_f\kappa_y\right)^2\\
&+k_+(r_+-r_c)^2
+k_-(r_--r_c)^2
\,dy.
\end{aligned}}
\]

这个能量式直接来自三相轴向应变能加两个界面弹簧能；没有组合梁规范系数。

## 11. 对 r+ 变分

拉格朗日密度对 \(r_+'\) 的导数：

\[
\frac{\partial\mathcal L}{\partial r_+'}=\mathcal K_+(r_+'+z_f\kappa_y).
\]

对 \(r_+\) 的导数：

\[
\frac{\partial\mathcal L}{\partial r_+}=k_+(r_+-r_c).
\]

Euler-Lagrange：

\[
\frac{d}{dy}\frac{\partial\mathcal L}{\partial r_+'}-\frac{\partial\mathcal L}{\partial r_+}=0.
\]

所以：

\[
\mathcal K_+(r_+''+z_f\kappa_y')-k_+(r_+-r_c)=0.
\]

即：

\[
\boxed{r_+''-\frac{k_+}{\mathcal K_+}(r_+-r_c)=-z_f\kappa_y'}.
\]

## 12. 对 rc 变分

\[
\frac{\partial\mathcal L}{\partial r_c'}=\mathcal K_c r_c'.
\]

\[
\frac{\partial\mathcal L}{\partial r_c}=-k_+(r_+-r_c)-k_-(r_--r_c).
\]

因此：

\[
\boxed{
\mathcal K_c r_c''+k_+(r_+-r_c)+k_-(r_--r_c)=0
}.
\]

即：

\[
\boxed{r_c''=-\frac{k_+}{\mathcal K_c}s_+-\frac{k_-}{\mathcal K_c}s_-}.
\]

## 13. 对 r- 变分

\[
\frac{\partial\mathcal L}{\partial r_-'}=\mathcal K_-(r_-'-z_f\kappa_y).
\]

\[
\frac{\partial\mathcal L}{\partial r_-}=k_-(r_--r_c).
\]

所以：

\[
\mathcal K_-(r_-''-z_f\kappa_y')-k_-(r_--r_c)=0.
\]

即：

\[
\boxed{r_-''-\frac{k_-}{\mathcal K_-}(r_--r_c)=+z_f\kappa_y'}.
\]

## 14. 两界面滑移微分方程

由：

\[
s_+''=r_+''-r_c'',
\qquad
s_-''=r_-''-r_c'',
\]

代入上述三式，得到：

\[
\boxed{
s_+''-B_{11}s_+-B_{12}s_-=-z_f\kappa_y'
},
\]

\[
\boxed{
s_-''-B_{21}s_+-B_{22}s_-=+z_f\kappa_y'
}.
\]

四个系数逐项为：

\[
\boxed{B_{11}=k_+\left(\frac1{\mathcal K_+}+\frac1{\mathcal K_c}\right)},
\]

\[
\boxed{B_{12}=\frac{k_-}{\mathcal K_c}},
\]

\[
\boxed{B_{21}=\frac{k_+}{\mathcal K_c}},
\]

\[
\boxed{B_{22}=k_-\left(\frac1{\mathcal K_-}+\frac1{\mathcal K_c}\right)}.
\]

量纲：

\[
[B_{ij}]=1/\mathrm{mm^2}.
\]

这是05真正的双界面partial-interaction控制方程。它由当前板自身的三相能量导出，不含组合梁设计经验系数。

---

# Part IV 只对已经算出的整体模态做Galerkin平均，不让滑移重新选模态

## 15. 已知整体曲率基

`m*` 已在Part I算出。定义：

\[
\beta=\frac{m^*\pi}{a}=\frac{\pi}{L_G}.
\]

在一个完整代表半波内，采用父R14已有整体模态的纵向曲率：

\[
\boxed{\kappa_y(y)=\widehat\kappa_y\sin(\beta y)}.
\]

因此：

\[
\boxed{\kappa_y'(y)=\beta\widehat\kappa_y\cos(\beta y)}.
\]

这里的beta来自先前算出的整体模态；不是由滑移方程反推，也与局部3/4/5鼓波数无关。

## 16. 05的“平均”定义

05不是假装逐点求完整端部边界层；它采用与父R14相同的单模态Galerkin思想，把两界面滑移投影到已知整体模态的正交伴随函数：

\[
\boxed{s_+(y)=S_+\cos(\beta y)},
\]

\[
\boxed{s_-(y)=S_-\cos(\beta y)}.
\]

这一步的物理含义是：只保留与已知整体曲率梯度同频的平均滑移分量。它不是“局部鼓波型滑移”，因为beta已经在进入滑移模块前确定。

## 17. Galerkin投影第一式

第一滑移残量：

\[
\mathcal R_+=s_+''-B_{11}s_+-B_{12}s_-+z_f\kappa_y'.
\]

要求：

\[
\int \mathcal R_+\cos(\beta y)\,dy=0.
\]

因为：

\[
s_+''=-\beta^2S_+\cos(\beta y),
\]

\[
s_- =S_-\cos(\beta y),
\]

\[
\kappa_y'=\beta\widehat\kappa_y\cos(\beta y),
\]

且在完整正交区间：

\[
\int \cos^2(\beta y)dy\neq0,
\]

约去公共积分因子，得到：

\[
\boxed{(\beta^2+B_{11})S_+ + B_{12}S_-=z_f\beta\widehat\kappa_y}.
\]

## 18. Galerkin投影第二式

同理：

\[
\boxed{B_{21}S_+ +(\beta^2+B_{22})S_-=-z_f\beta\widehat\kappa_y}.
\]

定义：

\[
A_{11}=\beta^2+B_{11},
\]

\[
A_{12}=B_{12},
\]

\[
A_{21}=B_{21},
\]

\[
A_{22}=\beta^2+B_{22}.
\]

于是：

\[
\begin{bmatrix}
A_{11}&A_{12}\\
A_{21}&A_{22}
\end{bmatrix}
\begin{bmatrix}S_+\\S_-\end{bmatrix}
=
z_f\beta\widehat\kappa_y
\begin{bmatrix}1\\-1\end{bmatrix}.
\]

## 19. 不隐藏矩阵逆：显式解S+和S-

定义行列式：

\[
\boxed{\Delta_\beta=A_{11}A_{22}-A_{12}A_{21}}.
\]

逆矩阵：

\[
\begin{bmatrix}
A_{11}&A_{12}\\
A_{21}&A_{22}
\end{bmatrix}^{-1}
=
\frac1{\Delta_\beta}
\begin{bmatrix}
A_{22}&-A_{12}\\
-A_{21}&A_{11}
\end{bmatrix}.
\]

因此：

\[
\boxed{
S_+=z_f\beta\widehat\kappa_y\frac{A_{22}+A_{12}}{\Delta_\beta}
},
\]

\[
\boxed{
S_-=-z_f\beta\widehat\kappa_y\frac{A_{11}+A_{21}}{\Delta_\beta}
}.
\]

## 20. 从滑移幅值推导平均组合传递系数

TOP实际相对纵向应变：

\[
\varepsilon_{y,+}-\varepsilon_{y,c}
=z_f\kappa_y+s_+'.
\]

在整体曲率峰值 `sin(beta y)=1` 处：

\[
s_+'=-\beta S_+.
\]

所以：

\[
\varepsilon_{y,+}-\varepsilon_{y,c}
=z_f\widehat\kappa_y-\beta S_+.
\]

定义05 TOP平均组合传递系数：

\[
\boxed{
c_+=\frac{z_f\widehat\kappa_y-\beta S_+}{z_f\widehat\kappa_y}
}.
\]

代入S+：

\[
\boxed{
c_+=1-\beta^2\frac{A_{22}+A_{12}}{\Delta_\beta}
}.
\]

BOTTOM：

\[
\varepsilon_{y,-}-\varepsilon_{y,c}
=-z_f\kappa_y+s_-'.
\]

峰值处：

\[
s_-'=-\beta S_-.
\]

定义其相对弯曲应变保留比例：

\[
\boxed{
c_-=\frac{z_f\widehat\kappa_y+\beta S_-}{z_f\widehat\kappa_y}
}.
\]

代入S-：

\[
\boxed{
c_-=1-\beta^2\frac{A_{11}+A_{21}}{\Delta_\beta}
}.
\]

这两个 `c+`,`c-` 就是05从当前板自身的守恒—兼容—界面本构推导出的平均组合系数。没有经验常数0.81、36、0.4、3，也没有旧02的 `gamma=KP/(KP+Keq)`。

---

# Part V 从相对组合程度恢复三个相的绝对应变

## 21. 为什么不能只改钢面而不改core

有了 `c+`,`c-`，相对弯曲应变满足：

\[
\varepsilon_{y,+}-\varepsilon_{y,c}=c_+z_f\kappa_y,
\]

\[
\varepsilon_{y,-}-\varepsilon_{y,c}=-c_-z_f\kappa_y.
\]

但是核心形心本身的附加轴向应变仍未知。必须用总轴力守恒确定，不能像旧02一样只缩放钢面。

令核心形心由partial interaction产生的弯曲型附加应变为：

\[
\delta_c=z_c^{PI}\kappa_y.
\]

则：

\[
\varepsilon_{y,c}=\varepsilon_y^0+z_c^{PI}\kappa_y.
\]

TOP：

\[
\varepsilon_{y,+}=\varepsilon_y^0+(z_c^{PI}+c_+z_f)\kappa_y.
\]

BOTTOM：

\[
\varepsilon_{y,-}=\varepsilon_y^0+(z_c^{PI}-c_-z_f)\kappa_y.
\]

## 22. 用零附加轴力条件求 zcPI

纯弯曲型partial-interaction修正不能凭空产生总轴力，因此：

\[
\mathcal K_+(z_c^{PI}+c_+z_f)
+\mathcal K_c z_c^{PI}
+\mathcal K_-(z_c^{PI}-c_-z_f)=0.
\]

整理：

\[
(\mathcal K_++\mathcal K_c+\mathcal K_-)z_c^{PI}
+z_f(\mathcal K_+c_+-\mathcal K_-c_-)=0.
\]

所以：

\[
\boxed{
z_c^{PI}=-z_f\frac{\mathcal K_+c_+-\mathcal K_-c_-}{\mathcal K_++\mathcal K_c+\mathcal K_-}
}.
\]

定义TOP、BOTTOM实际等效纵向杠杆：

\[
\boxed{z_+^{PI}=z_c^{PI}+c_+z_f},
\]

\[
\boxed{z_-^{PI}=z_c^{PI}-c_-z_f}.
\]

最终：

\[
\boxed{\varepsilon_{y,s}^+=\varepsilon_y^0+z_+^{PI}\kappa_y},
\]

\[
\boxed{\varepsilon_{y,s}^-=\varepsilon_y^0+z_-^{PI}\kappa_y}.
\]

核心：

\[
\boxed{\varepsilon_y^U(z)=\varepsilon_y^0+(z_c^{PI}+z)\kappa_y}.
\]

R14中属于核心/纵向web模块的纵向钢面积，在05-R01相分配下同样使用：

\[
\boxed{\varepsilon_y^w(z)=\varepsilon_y^0+(z_c^{PI}+z)\kappa_y}.
\]

横向不存在本版本所定义的纵向界面滑移修正：

\[
\boxed{\varepsilon_{x,s}^+=\varepsilon_x^0+z_f\kappa_x},
\]

\[
\boxed{\varepsilon_{x,s}^-=\varepsilon_x^0-z_f\kappa_x},
\]

\[
\boxed{\varepsilon_x^U(z)=\varepsilon_x^0+z\kappa_x}.
\]

---

# Part VI 必须通过的极限与量纲检查

## 23. 刚性连接极限

当：

\[
k_+,k_-\rightarrow\infty,
\]

有：

\[
c_+\rightarrow1,\qquad c_-\rightarrow1.
\]

若上下钢面刚度相同：

\[
\mathcal K_+=\mathcal K_-,
\]

则：

\[
z_c^{PI}\rightarrow0.
\]

所以：

\[
z_+^{PI}\rightarrow+z_f,
\qquad
z_-^{PI}\rightarrow-z_f.
\]

严格恢复Multiwave 01完全组合运动学。

## 24. 零连接极限

当：

\[
k_+,k_-\rightarrow0,
\]

有：

\[
B_{ij}\rightarrow0,
\]

\[
A_{11}=A_{22}=\beta^2,
\quad
A_{12}=A_{21}=0,
\]

\[
\Delta_\beta=\beta^4.
\]

于是：

\[
c_+=1-\frac{\beta^4}{\beta^4}=0,
\]

\[
c_-=0.
\]

并有：

\[
z_c^{PI}=0,
\quad
z_+^{PI}=0,
\quad
z_-^{PI}=0.
\]

即钢面与core之间不再传递由形心分离产生的轴力偶；各钢面仍保留自身厚度弯曲和后续局部板作用，这符合弱组合极限。

## 25. 对称双界面的退化式

若：

\[
\mathcal K_+=\mathcal K_-=\mathcal K_s,
\qquad
k_+=k_-=k,
\]

则反对称驱动 `[1,-1]` 下核心形心修正为0，并可直接化简：

\[
\boxed{c_+=c_-=c=\frac{k}{k+\mathcal K_s\beta^2}}.
\]

这一退化式特别重要，因为它显示真实控制参数是：

\[
\boxed{\frac{k}{\mathcal K_s\beta^2}}.
\]

其中 `beta` 是已经由原板稳定求出的整体应变变化尺度，而不是局部3/4/5鼓波数。

## 26. 传递长度

对单界面退化方程：

\[
s''-\lambda_t^2s=g',
\]

有：

\[
\boxed{\lambda_t^2=k_\ell\left(\frac1{\mathcal K_s}+\frac1{\mathcal K_c}\right)}.
\]

因此：

\[
\boxed{\ell_t=\frac1{\lambda_t}}.
\]

这说明滑移效应必然具有由材料轴向刚度和连接刚度决定的物理长度尺度。05没有把该长度尺度伪装成局部鼓波数量。

---

# Part VII 局部多波钢壳：继承01/R02/R06，不让滑移模块重建局部理论

## 27. 标准格室

对任意真实格室：

\[
L_y=\frac{L_G}{n}.
\]

\[
\boxed{k_x=\frac{2\pi}{L_x}},
\qquad
\boxed{k_y=\frac{2\pi}{L_y}}.
\]

局部形函数：

\[
\boxed{\phi=(1-\cos k_x\xi)(1-\cos k_yy)}.
\]

局部初缺陷：

\[
\boxed{A_{0\ell}=\frac{L_x}{1600}}.
\]

当前局部鼓波：

\[
w_\ell=U\phi.
\]

## 28. 局部屈曲门

纵横比：

\[
r_c=\frac{L_y}{L_x}.
\]

\[
\boxed{k_{cr}=\frac{4(3r_c^4+2r_c^2+3)}{3r_c^2}}.
\]

\[
\boxed{\sigma_{cr}^{E}=\frac{\pi^2E_st_s^2}{12(1-\nu_s^2)L_x^2}k_{cr}}.
\]

若：

\[
\sigma_{cr}^{E}\ge f_y,
\]

则该格室走完整厚度 ideal-EP/yield-first。

若：

\[
\sigma_{cr}^{E}<f_y,
\]

进入R02/R06 local-first。

## 29. R02压缩正号转换

\[
\boxed{e_x^c=-\varepsilon_{x,s}},
\qquad
\boxed{e_y^c=-\varepsilon_{y,s}}.
\]

\[
\boxed{d=U^2-A_{0\ell}^2}.
\]

\[
\boxed{c_x=\frac{3k_x^2}{8}},
\qquad
\boxed{c_y=\frac{3k_y^2}{8}}.
\]

\[
\boxed{m_x=e_x^c-c_xd},
\qquad
\boxed{m_y=e_y^c-c_yd}.
\]

注意 `m_x,m_y` 只是R02中间代数量，不是实体板弯矩。

## 30. R02弯曲与Airy系数

\[
D_s=\frac{E_st_s^3}{12(1-\nu_s^2)}.
\]

\[
\boxed{K_b=D_s\left[\frac34(k_x^4+k_y^4)+\frac12k_x^2k_y^2\right]}.
\]

\[
r_k=\frac{k_x}{k_y}.
\]

\[
\begin{aligned}
P_{16}(r)=&272r^{16}+2856r^{14}+11273r^{12}+23146r^{10}\\
&+31506r^8+23146r^6+11273r^4+2856r^2+272.
\end{aligned}
\]

\[
\boxed{K_A=k_y^4\frac{P_{16}(r_k)}{256(r_k^2+1)^2(r_k^2+4)^2(4r_k^2+1)^2}}.
\]

## 31. R02三次方程全部系数

\[
\boxed{L_0=Q_s[c_x(e_x^c+\nu_se_y^c)+c_y(e_y^c+\nu_se_x^c)]}.
\]

\[
\boxed{C_g=Q_s(c_x^2+c_y^2+2\nu_sc_xc_y)}.
\]

\[
\boxed{B_3=4t_sE_sK_A+2t_sC_g}.
\]

\[
\boxed{B_1=K_b-2t_sL_0-B_3A_{0\ell}^2}.
\]

\[
\boxed{B_0=-K_bA_{0\ell}}.
\]

局部幅值：

\[
\boxed{B_3U^3+B_1U+B_0=0}.
\]

所有非负实根均计算能量：

\[
\boxed{
\Pi(U)=\frac12K_b(U-A_{0\ell})^2
+\frac12t_sQ_s(m_x^2+m_y^2+2\nu_sm_xm_y)
+t_sE_sK_Ad^2
}.
\]

取：

\[
\boxed{U^*=\arg\min_{U\ge0}\Pi(U)}.
\]

平均应力：

\[
\boxed{\bar\sigma_x^{R02}=-Q_s(m_x+\nu_sm_y)},
\]

\[
\boxed{\bar\sigma_y^{R02}=-Q_s(m_y+\nu_sm_x)}.
\]

## 32. R06七谐波

集合：

\[
\mathcal H=\{(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1)\}.
\]

系数：

\[
h_{01}=1/2,
\ h_{02}=-1/2,
\ h_{10}=1/2,
\ h_{11}=-1,
\ h_{12}=1/2,
\ h_{20}=-1/2,
\ h_{21}=1/2.
\]

\[
\boxed{A_{pq}=E_sd\,h_{pq}\frac{k_x^2k_y^2}{[(pk_x)^2+(qk_y)^2]^2}}.
\]

\[
\boxed{\widetilde\sigma_x=-\sum(qk_y)^2A_{pq}\cos(p\theta_x)\cos(q\theta_y)}.
\]

\[
\boxed{\widetilde\sigma_y=-\sum(pk_x)^2A_{pq}\cos(p\theta_x)\cos(q\theta_y)}.
\]

\[
\boxed{\widetilde\tau_{xy}=-\sum(pk_x)(qk_y)A_{pq}\sin(p\theta_x)\sin(q\theta_y)}.
\]

总应力：

\[
\sigma_x=\bar\sigma_x^{R02}+\widetilde\sigma_x,
\]

\[
\sigma_y=\bar\sigma_y^{R02}+\widetilde\sigma_y,
\]

\[
\tau_{xy}=\widetilde\tau_{xy}.
\]

Mises函数：

\[
\boxed{\Phi=\sigma_x^2-\sigma_x\sigma_y+\sigma_y^2+3\tau_{xy}^2}.
\]

在完整 `(u,v)=(cos theta_x, cos theta_y) in [-1,1]^2` 上求最大值。若 \(\Phi_{max}>f_y^2\)，求 \(0<\eta_\ell\le1\) 使：

\[
\boxed{\Phi_{max}(\eta_\ell\varepsilon_{x,s},\eta_\ell\varepsilon_{y,s})=f_y^2}.
\]

然后使用该首次局部屈服状态对应的R02平均应力。正式名称继续为：`FIRST-LOCAL-YIELD CAPPED REDUCED OPERATOR`，不冒充完整J2塑性区扩展。

## 33. 边缘格室

每一个非标准边缘格室都使用自己的真实 \(L_x\) 和：

\[
n_e=\left\lfloor\frac{L_G}{L_{x,e}}\right\rfloor
\]

重新计算 `sigma_cr^E`，不再自动按E/yield-first。

当前BH：TOP两边各 `0.1625b`，故 `n_e=6`；BOTTOM两边各 `0.05b`，故 `n_e=20`。BH032 TOP edge约470.5 MPa>355，yield-first；BH050约192.7 MPa<355，local-first。

---

# Part VIII 截面N/M与材料积分

## 34. 上下钢面面积平均

按真实格室宽度加权得到：

\[
\bar\sigma_x^+,\ \bar\sigma_y^+,
\qquad
\bar\sigma_x^-,\ \bar\sigma_y^-.
\]

钢壳膜力：

\[
\boxed{N_x^s=t_s(\bar\sigma_x^++\bar\sigma_x^-)},
\]

\[
\boxed{N_y^s=t_s(\bar\sigma_y^++\bar\sigma_y^-)}.
\]

钢面真实位置仍为 \(\pm z_f\)，因此：

\[
\boxed{M_x^s=t_sz_f(\bar\sigma_x^+-\bar\sigma_x^-)},
\]

\[
\boxed{M_y^s=t_sz_f(\bar\sigma_y^+-\bar\sigma_y^-)}.
\]

05不使用有效宽度或有效面积。

## 35. UHPC纵向应变中心的05修正

定义：

\[
\bar\varepsilon_{y,c}^0=\varepsilon_y^0+z_c^{PI}\kappa_y.
\]

则：

\[
\varepsilon_y^U(z)=\bar\varepsilon_{y,c}^0+z\kappa_y.
\]

横向仍为：

\[
\varepsilon_x^U(z)=\varepsilon_x^0+z\kappa_x.
\]

## 36. UHPC压缩显式材料函数

\[
\xi=-\frac{\varepsilon}{\varepsilon_{c0}},
\]

\[
a_c=\frac{E_c\varepsilon_{c0}}{f_c},
\qquad
b_c=6-5a_c,
\qquad
c_c=4a_c-5.
\]

\[
\boxed{\sigma_c=-f_c(a_c\xi+b_c\xi^5+c_c\xi^6)}.
\]

第一原函数：

\[
\boxed{F_0^c=f_c\varepsilon_{c0}\left[\frac{a_c}{2}\xi^2+\frac{b_c}{6}\xi^6+\frac{c_c}{7}\xi^7\right]}.
\]

第二原函数：

\[
\boxed{F_1^c=-f_c\varepsilon_{c0}^2\left[\frac{a_c}{3}\xi^3+\frac{b_c}{7}\xi^7+\frac{c_c}{8}\xi^8\right]}.
\]

拉伸继续使用现有冻结的四段显式三次多项式，每段均写为：

\[
\sigma=a_j+b_js+c_js^2+d_js^3,
\qquad s=\varepsilon-\varepsilon_j,
\]

\[
\Delta F_0=a_js+\frac{b_j}{2}s^2+\frac{c_j}{3}s^3+\frac{d_j}{4}s^4,
\]

\[
\Delta F_1=\varepsilon_j\Delta F_0+\frac{a_j}{2}s^2+\frac{b_j}{3}s^3+\frac{c_j}{4}s^4+\frac{d_j}{5}s^5.
\]

05不修改这些材料系数。

## 37. UHPC纵向N/M

纵向两表面应变：

\[
\varepsilon_y^{U,+}=\bar\varepsilon_{y,c}^0+\kappa_y\frac{t_c}{2},
\]

\[
\varepsilon_y^{U,-}=\bar\varepsilon_{y,c}^0-\kappa_y\frac{t_c}{2}.
\]

定义：

\[
\Delta F_0^y=F_0(\varepsilon_y^{U,+})-F_0(\varepsilon_y^{U,-}),
\]

\[
\Delta F_1^y=F_1(\varepsilon_y^{U,+})-F_1(\varepsilon_y^{U,-}).
\]

则：

\[
\boxed{N_y^U=(1-\rho_w)\frac{\Delta F_0^y}{\kappa_y}}.
\]

\[
\boxed{M_y^U=(1-\rho_w)\frac{\Delta F_1^y-\bar\varepsilon_{y,c}^0\Delta F_0^y}{\kappa_y^2}}.
\]

横向同理，只是中心应变仍为 \(\varepsilon_x^0\)。

## 38. web纵向积分

05-R01中web使用与核心相同的中心修正：

\[
\varepsilon_y^w(z)=\bar\varepsilon_{y,c}^0+z\kappa_y.
\]

屈服应变：

\[
\varepsilon_Y=\frac{f_y}{E_s}.
\]

\[
\sigma_w=
\begin{cases}
-f_y,&\varepsilon_w\le-\varepsilon_Y,\\
E_s\varepsilon_w,&|\varepsilon_w|<\varepsilon_Y,\\
+f_y,&\varepsilon_w\ge+\varepsilon_Y.
\end{cases}
\]

各弹性/塑性厚度段继续解析积分，得到：

\[
N_y^w,\qquad M_y^w.
\]

---

# Part IX 原R14外层保持不变

## 39. q与Airy demand

\[
\boxed{Q=q(q+2q_0)}.
\]

\[
\boxed{P(q)=P_{cr}\frac{q}{q+q_0}+C_AQ}.
\]

Airy demand：

\[
N_x^A=K_xQ,
\]

\[
M_x^A=J_xq,
\]

\[
N_y^A=-\left[\frac{P(q)}{b}-GQ\right],
\]

\[
M_y^A=J_yq.
\]

## 40. 总截面力

\[
N_x=N_x^U+N_x^s,
\]

\[
M_x=M_x^U+M_x^s,
\]

\[
N_y=N_y^U+N_y^s+N_y^w,
\]

\[
M_y=M_y^U+M_y^s+M_y^w.
\]

## 41. 四个外层平衡

\[
\boxed{R_{N_x}=N_x-N_x^A=0},
\]

\[
\boxed{R_{M_x}=M_x-M_x^A=0},
\]

\[
\boxed{R_{N_y}=N_y-N_y^A=0},
\]

\[
\boxed{R_{M_y}=M_y-M_y^A=0}.
\]

05不增加外层滑移未知量。对每个q，仍只求：

\[
\varepsilon_x^0,\quad\kappa_x,\quad\varepsilon_y^0,\quad\kappa_y.
\]

物理支仍定义为从未加载状态连续连接的解支。终点仍为第一合法材料域闭合事件或第一合法J4 fold。

---

# Part X 05的适用边界与门禁

## 42. 05为什么不会再出现“滑移把m=2改成3”

因为执行顺序明确：

1. 用原R14初始板稳定方程独立计算 `m*`；
2. 得到 `beta=m*pi/a`；
3. 只把这个已知beta作为partial-interaction方程的驱动空间尺度；
4. 解析凝聚得到 `c+`,`c-`；
5. 不把 `c+`,`c-` 回写到Part I重新选m。

这是有意的单向耦合层级。05因此属于 `post-eigenmode / branch-section slip correction`，不是“完全耦合partial-interaction特征值理论”。

## 43. 何时05自身应判HOLD

如果来源锁定后的真实连接刚度使 `c+`,`c-` 显著远离1，说明界面柔度可能在初始线性屈曲阶段已不可忽略。05不人为规定一个百分比阈值；此时必须依据独立FE模态或建立完整耦合特征值方程判断parent R14的 `m*` 是否仍有效。未经该证据，不得用05反过来宣称新m，也不得假设旧m绝对不变。

## 44. 当前界面参数身份

现有公开无机械连接钢-UHPC界面研究可提供 `Kt` 量级参考，但不同表面处理差异巨大。喷砂和环氧+骨料界面报告的切向刚度分别约696和13 N/mm³，并且这些参数由推出试验FE反演得到；它们都不是当前无孔薄肋的source-locked参数。因此05只锁定 `Kt` 的物理接口，不锁定当前production数值。

## 45. current tangent边界

05-R01的partial-interaction核使用初始弹性相刚度 `K+,Kc,K-` 和线性界面刚度 `k+,k-`。它没有假装已经包含材料软化后的current connector/material tangent。如果以后需要production级current PI，则必须把：

\[
\mathcal K_i\rightarrow\mathcal K_i^t(\text{current state}),
\qquad
k_\pm\rightarrow k_\pm^t(\text{current slip state})
\]

再从同一套能量/守恒方程重新凝聚；不得用secant或FEM反标替代exact current tangent。

---

# Part XI 05相对于01/02/04的裁决

- Multiwave 01：无滑移基线，保留。
- Multiwave 02：保留“平均partial interaction”思想；废止旧Kr来源和旧gamma公式。
- Multiwave 04-R01：connector-source接口保留；直接移植组合梁SLS折减公式的 `alpha/eta/zeta/chi` 链正式HOLD，不作为05依据。
- Multiwave 05：从当前双钢面-UHPC板自己的能量、平衡、兼容、界面本构出发，得到双界面微分方程，再对父R14已算出的整体模态做单项Galerkin平均，显式得到 `c+`,`c-` 和三个相的实际纵向应变。

---

# Part XII 文献角色

1. Nie, J.G. & Cai, C.S. (2003), *Steel–Concrete Composite Beams Considering Shear Slip Effects*, Journal of Structural Engineering 129(4), 495–506. DOI 10.1061/(ASCE)0733-9445(2003)129:4(495). 只用于支持“从平衡/兼容出发、再凝聚成等效刚度”的partial-interaction一般思想，不复制其梁公式到本板。
2. *Buckling Behaviors of Steel-Concrete Composite Plate* (2013), DOI 10.4028/www.scientific.net/AMM.405-408.2544. 其摘要表明已有钢-混凝土组合板在轴压屈曲中把柔性界面建模为薄剪切层并推导临界屈曲荷载，说明“板+界面滑移+轴压屈曲”应使用板自身理论，而不是直接套组合梁SLS公式。
3. *Constitutive Behavior of the Interface between UHPC and Steel Plate without Shear Connector: From Experimental to Numerical Study* (2024), DOI 10.32604/cmes.2024.048217. 用于支持无机械连接钢-UHPC界面可用traction-separation/切向刚度描述，以及不同表面处理的刚度/强度差异；不把其具体Kt冒充当前纵肋实测值。

---

# 最终05计算链

\[
\boxed{
\text{R14初始板刚度}
\to P_{cr}^{(m)}
\to m^*
\to L_G
\to n_0,n_0\pm1
}
\]

与连接源并行：

\[
\boxed{
\text{plain-rib }K_t\ \text{or PBL }k_{ps}
\to k_{\ell,r}
\to k_+,k_-
}
\]

随后：

\[
\boxed{
(\mathcal K_+,\mathcal K_c,\mathcal K_-,k_+,k_-,\beta)
\to B_{ij}
\to A_{ij}
\to \Delta_\beta
\to c_+,c_-
\to z_c^{PI},z_+^{PI},z_-^{PI}
}
\]

再进入：

\[
\boxed{
\varepsilon_{y,s}^{\pm},\varepsilon_y^U,\varepsilon_y^w
\to R02/R06
\to N_s,M_s,N_U,M_U,N_w,M_w
\to R_4=0
\to \text{connected branch}
\to \text{first material event or J4 fold}
}.
\]

该文件为05 R01理论锁定稿，但仍为diagnostic/theory-development；在当前无孔纵肋 `Kt` source-lock、05模态一致性门禁和current tangent扩展完成前，不得升级production R14。
