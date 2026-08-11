# NZ-SCCM 计算过程模板 V1 —— 以 Case21 全新闭合作为唯一格式范例

**日期：2026-08-11**  
**身份：CURRENT CALCULATION PROCESS TEMPLATE**  
**用途：把已经闭合的 Case21 计算过程固化为后续板件计算的统一执行模板。它不是新材料阶段，不修改 R10，不修改 N48，不修改 D15。**

---

# 0. 不可变执行纪律

后续任一板件必须按下列顺序执行：

```text
原始板件输入
-> 闭式 R10 材料参数代入
-> 连续主等效应变范围解析证书
-> N48 系数由统一公式重新生成
-> Nguyen 连续二阶运动学
-> Cayley-Hamilton 二维 current-map
-> D15 完整半波精确矩
-> 钢筋闭式贡献与材料支检查
-> 解 Rq(D,q)=0 平衡支
-> 解 L(D,q)=0 极限点
-> 残量与材料支自洽检查
-> 最后才引入试验值比较
```

禁止：

```text
历史 CaseXX 计算荷载作为输入 = NO
历史 CaseXX 根作为初值目标 = NO
历史 CaseXX 荷载路径作为选根依据 = NO
试验荷载参与求解/调参 = NO
空间 Gauss = NO
空间 Simpson = NO
空间 collocation = NO
材料点网格 = NO
自动提高 N48 阶次 = NO
重新打开 R10 材料路线 = NO
```

正式空间身份始终为

```text
DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
N_formal_spatial_sampling = 0
N_formal_spatial_quadrature = 0
N_formal_spatial_subdomains = 1
```

---

# 1. STEP-1：建立板件原始输入表

每块板首先只登记来源输入，不做理论调整。

必须登记：

\[
a,\quad b,\quad \ell,\quad t_p,
\]

\[
f_c,\quad E_0,\quad \varepsilon_0,\quad \nu,
\]

\[
\rho_{s,x},\quad \rho_{s,y},\quad z_s,
\]

\[
E_s,\quad \varepsilon_y,\quad f_y,
\]

\[
q_0=\frac{A_0}{b}.
\]

式中：

- \(a\) —— 整板轴向长度；
- \(b\) —— 板宽；
- \(\ell\) —— 当前已批准的一个连续完整代表半波长度；
- \(t_p\) —— 混凝土板厚；
- \(f_c\) —— 混凝土单轴抗压强度；
- \(E_0\) —— 混凝土初始弹性模量；
- \(\varepsilon_0\) —— 混凝土参考压缩应变；
- \(\nu\) —— 泊松比；
- \(\rho_{s,x},\rho_{s,y}\) —— 两个正交方向配筋率；
- \(z_s\) —— 钢筋层相对中面的厚度坐标；
- \(E_s\) —— 钢筋弹性模量；
- \(\varepsilon_y\) —— 钢筋屈服应变；
- \(f_y\) —— 钢筋屈服强度；
- \(A_0\) —— 初始缺陷幅值；
- \(q_0\) —— 初始缺陷无量纲幅值。

**输出：** 一张输入表，并给出每个输入的来源。  
**PASS：** 所有输入均来自试件/材料来源或已冻结项目合同。  
**FAIL：** 缺少关键输入时停止，不用试验承载力反推。

---

# 2. STEP-2：直接代入闭式 R10 材料公式

计算

\[
\boxed{\kappa=\frac{E_0\varepsilon_0}{f_c}},
\]

\[
\boxed{x_{cr}=\frac{\rho}{\kappa}},
\qquad
\boxed{\eta=\frac{x_{cr}}{20}},
\]

其中 \(\rho=0.1\)。

源 Foster 标量：

\[
r=\frac{t}{x_{cr}},
\qquad
m_t=-\frac7{90},
\qquad
\eta_r=0.05,
\]

\[
H(r,r_0)=
\frac12\left[(r-r_0)+\sqrt{(r-r_0)^2+\eta_r^2}\right]
-
\frac12\left[-r_0+\sqrt{r_0^2+\eta_r^2}\right],
\]

\[
\boxed{T_{src}(r)=r+(m_t-1)H(r,1)-m_tH(r,10)}.
\]

材料功：

\[
\boxed{W_{src}=\rho x_{cr}\int_0^{10}T_{src}(r)\,dr}.
\]

R10 峰值：

\[
\boxed{
h=\frac15\left(\frac{W_{src}}{x_{cr}}-\frac{\rho}{10}-\frac92u_r\right)},
\qquad u_r=0.03.
\]

上升支：

\[
\boxed{
u_1(\tau)=
\rho\tau+(10h-6\rho)\tau^3+(8\rho-15h)\tau^4+(6h-3\rho)\tau^5},
\]

\[
\tau=\frac{t}{x_{cr}}.
\]

下降支：

\[
\boxed{
u_2(s)=h+(u_r-h)(10s^3-15s^4+6s^5)},
\]

\[
s=\frac{t-x_{cr}}{9x_{cr}}.
\]

**输出：** \(\kappa,x_{cr},\eta,W_{src},h\) 和上、下降支的参数组合。  
**PASS：** 只由材料输入得到。  
**FAIL：** 不允许通过结构试验值调整 \(h\)、\(u_r\) 或其他参数。

---

# 3. STEP-3：连续主等效应变范围解析证书

先写当前板件的 Nguyen 连续二阶应变场，再由整个连续半波上的解析上下界得到

\[
\lambda_-\ge\lambda_a,
\qquad
\lambda_+\le\lambda_b.
\]

这里 \([\lambda_a,\lambda_b]\) 是本板件 N48 编译所需的一维主等效应变包络。

**重要：** 这个包络必须来自连续场解析界或已批准的解析搜索域，不能通过空间采样点扫描获得。

定义

\[
\lambda_c=\frac{\lambda_a+\lambda_b}{2},
\qquad
\lambda_h=\frac{\lambda_b-\lambda_a}{2},
\qquad
\xi=\frac{\lambda-\lambda_c}{\lambda_h}.
\]

**输出：** \(\lambda_a,\lambda_b,\lambda_c,\lambda_h\)。  
**PASS：** 连续场解析证书覆盖求解域。  
**FAIL：** 若不能覆盖，只修正解析包络，不改变 R10 或 N48 阶次。

---

# 4. STEP-4：用一个公式重新生成 N48

对

\[
F\in\{U,C,T,T^7\}
\]

写

\[
\boxed{F_{48}(\lambda)=\sum_{n=0}^{48}a_n^{(F)}\mathcal C_n(\xi)}.
\]

根点：

\[
\theta_j=\frac{(j+\tfrac12)\pi}{49},
\qquad
\lambda_j=\lambda_c+\lambda_h\cos\theta_j,
\qquad j=0,\ldots,48.
\]

所有系数统一由

\[
\boxed{
a_n^{(F)}=
\frac{2-\delta_{n0}}{49}
\sum_{j=0}^{48}F(\lambda_j)\cos(n\theta_j),
\quad n=0,\ldots,48}
\]

生成。

**输出：** 理论正文只给通式；计算审计可给 \(a_0,a_1,a_2\) 等少量代表系数。  
**PASS：** 系数从本板件闭式材料重新生成。  
**FAIL：** 不允许用旧板件 coefficient array 代替。

---

# 5. STEP-5：代入 Nguyen 连续二阶运动学

统一坐标：

\[
X=\frac{\pi x}{b},
\qquad
Y=\frac{\pi y}{\ell},
\qquad
\zeta=\frac{2z}{t_p},
\qquad
q=\frac{A}{b}.
\]

然后使用当前已冻结的 Nguyen 二阶运动学建立

\[
\boxed{\mathbf E=\mathbf E(X,Y,\zeta;D,q)}.
\]

**Case21 特例说明：** Case21 中 \(\ell=b\)，因此其已展示的 \(C_m,C_b,e_x,e_y,g_{xy}\) 形式含有 \(\ell/b=1\) 的特化。后续若 \(\ell/b\neq1\)，不得机械复制 Case21 的 \(\ell=b\) 简化式；必须使用同一冻结 Nguyen 运动学的一般 \(\ell/b\) 形式，然后继续执行完全相同的后续步骤。这个区别是几何代入，不是重新打开理论。

**输出：** 显式 \(e_x,e_y,g_{xy}\) 或等价 \(\mathbf E\) 公式，并列出该板件的所有数值系数组合。  
**PASS：** 整个半波仍是一个连续解析场。

---

# 6. STEP-6：二维等效应变与 current-map

由

\[
\mathbf E_u=
\frac{(1-\nu)\mathbf E+\nu\operatorname{tr}(\mathbf E)\mathbf I}{1-\nu^2},
\qquad
\mathbf X=\frac{\mathbf E_u}{\varepsilon_0},
\]

建立

\[
\mathbf Y=\frac{\mathbf X-\lambda_c\mathbf I}{\lambda_h}.
\]

定义

\[
K_1=\operatorname{tr}\mathbf Y,
\qquad
K_2=\det\mathbf Y.
\]

二维 Cayley-Hamilton：

\[
\mathbf Y^2-K_1\mathbf Y+K_2\mathbf I=0.
\]

矩阵 Chebyshev 递推：

\[
\mathcal C_n(\mathbf Y)=A_n\mathbf I+B_n\mathbf Y,
\]

\[
A_{n+1}=-2K_2B_n-A_{n-1},
\]

\[
B_{n+1}=2A_n+2K_1B_n-B_{n-1}.
\]

得到

\[
\mathbf U,\quad\mathbf C,\quad\mathbf T,\quad\mathbf T^{(7)},
\]

再计算

\[
\mathbf{CC}=\det(\mathbf C)\mathbf C,
\]

\[
\mathbf{TC}=\mathbf C[\operatorname{tr}(\mathbf T)\mathbf I-\mathbf T],
\]

\[
\mathbf{TT}=\det(\mathbf T)[\operatorname{tr}(\mathbf T^{(7)})\mathbf I-\mathbf T^{(7)}],
\]

\[
\boxed{\mathbf S=\mathbf U-a_{cc}\mathbf{CC}+\mathbf{TC}-\rho a_t\mathbf{TT}}.
\]

**输出：** 不需要打印大数组，只需记录系数代数已闭合及必要人工校核项。  
**PASS：** 无二维材料面重新拟合。

---

# 7. STEP-7：D15 完整半波精确矩

任一待积分量写成

\[
Q(X,Y,\zeta)=\sum_{i,j,k}c_{ijk}
\mathcal C_i(\sin X)\mathcal C_j(\sin Y)\mathcal C_k(\zeta).
\]

基础矩：

\[
M_n=\begin{cases}
\pi,&n=0,\\
2\sin(n\pi/2)/n,&n\ge1,
\end{cases}
\]

\[
Z_k=\begin{cases}
0,&k\text{ odd},\\
2/(1-k^2),&k\text{ even}.
\end{cases}
\]

因此

\[
\boxed{\mathscr D[Q]=\sum c_{ijk}M_iM_jZ_k}.
\]

直接混凝土轴力：

\[
\boxed{
P_c=-\frac{f_cb t_p}{2\pi^2}\mathscr D[S_{yy}]}
\]

（若单位为 N、mm，则最终除以 1000 得 kN）。

幅值广义功采用物理归一化应变

\[
\mathbf e=\frac{\mathbf E}{\varepsilon_0}
=(1+\nu)\mathbf X-\nu\operatorname{tr}(\mathbf X)\mathbf I,
\]

\[
\boxed{Q_q=\mathbf S:\mathbf e_{,q}},
\]

\[
\boxed{
R_{q,c}=f_c\varepsilon_0J_\Omega\mathscr D[Q_q]},
\qquad
J_\Omega=\frac{b\ell t_p}{2\pi^2}.
\]

**输出：** 至少给出 \(\mathscr D[S_{yy}]\)、轴力前因子、\(P_c\)、\(\mathscr D[Q_q]\)、广义功前因子和 \(R_{q,c}\)。  
**PASS：** 结果由解析系数乘精确矩得到，而非空间点求和。

---

# 8. STEP-8：钢筋先检查材料支，再计算贡献

必须先从连续钢筋应变场得到

\[
\varepsilon_{s,\min},\qquad\varepsilon_{s,\max}.
\]

若

\[
|\varepsilon_s|<\varepsilon_y,
\]

则使用

\[
\sigma_s=E_s\varepsilon_s.
\]

若达到屈服，则按冻结钢筋本构切换对应解析支；不得事后直接加 \(A_sf_y\)。

计算

\[
P_s(D,q),\qquad R_{q,s}(D,q),
\]

并在求根前组成

\[
\boxed{P=P_c+P_s},
\qquad
\boxed{R_q=R_{q,c}+R_{q,s}}.
\]

**输出：** 钢筋应变范围、材料支判定、\(P_s,R_{q,s}\)。  
**PASS：** 钢筋从求解开始就在总方程中，不事后追加。

---

# 9. STEP-9：求平衡支 Rq=0

对若干广义压缩变量 \(D\)，只在低维未知量 \(q\) 上解

\[
\boxed{R_q(D,q)=0}.
\]

生成表格：

| \(D\) | 平衡根 \(q\) | \(A=bq\) | \(P_c\) | \(P_s\) | \(P\) |
|---:|---:|---:|---:|---:|---:|
| ... | ... | ... | ... | ... | ... |

这里允许对低维广义变量做少量插值、二分或 Newton；这不是空间离散。

**PASS：** 平衡支连续、根可追踪。  
**FAIL：** 若不存在合法根，报告该板件失败，不通过历史结果选一个根。

---

# 10. STEP-10：求极限状态

在平衡支极值附近，用同一解析表达求

\[
P_{,D},\quad P_{,q},\quad R_{q,D},\quad R_{q,q}.
\]

极限条件

\[
\boxed{L=P_{,D}R_{q,q}-P_{,q}R_{q,D}=0}.
\]

最终同时闭合

\[
\boxed{R_q(D_u,q_u)=0},
\]

\[
\boxed{L(D_u,q_u)=0}.
\]

并给出

\[
A_u=bq_u,
\qquad
P_u=P(D_u,q_u).
\]

**输出：** \(D_u,q_u,A_u,P_c,P_s,P_u,R_q,L\) 及归一化残量。  
**PASS：** 平衡条件和极限条件同时满足。

---

# 11. STEP-11：计算后自洽检查

在最终 \((D_u,q_u)\) 重新检查：

1. 主等效应变是否仍位于 N48 编译包络；
2. 钢筋材料支是否仍正确；
3. \(R_q\) 是否闭合；
4. \(L\) 是否达到工程容差；
5. 所有空间积分是否仍只使用 D15 精确矩；
6. 是否存在任何试验荷载参与求解。

只有全部通过，才进入最终比较。

---

# 12. STEP-12：最后才与试验值比较

求解全部结束后，才读取试验失效荷载

\[
P_{f,exp}.
\]

仅计算

\[
\boxed{\Delta P=P_u-P_{f,exp}},
\]

\[
\boxed{
\varepsilon_P=
\frac{P_u-P_{f,exp}}{P_{f,exp}}\times100\%}.
\]

不得把误差反向用于修改任何材料参数、N48 系数或根。

标准输出表：

| 板件 | \(P_u\) 理论值 / kN | \(P_{f,exp}\) / kN | 差值 / kN | 相对误差 / % |
|---|---:|---:|---:|---:|
| CaseXX | ... | ... | ... | ... |

---

# 13. Case21 在本模板中的身份

Case21 仅承担两个作用：

1. **已闭合的计算过程范例**：证明上述 12 步可以从输入一路闭合到 \(P_u\)；
2. **输出格式范例**：后续每块板都应按同样层级记录中间量、残量和最终比较。

Case21 不再承担：

- 材料参数校准目标；
- 后续板件根的初值目标；
- 后续板件荷载预测目标；
- 误差修正基准。

因此后续板件的计算是

\[
\boxed{
\text{same process}\neq\text{reuse Case21 numerical result}.
}
\]

---

# 14. 最小正式交付包

以后每计算一块板，至少输出：

1. `INPUT`：原始输入与来源；
2. `R10`：\(\kappa,x_{cr},\eta,W_{src},h\)；
3. `SPECTRAL`：\([\lambda_a,\lambda_b]\) 连续解析证书；
4. `N48`：统一系数公式与少量代表系数审计；
5. `KINEMATICS`：该板的连续 Nguyen 应变场；
6. `D15`：关键精确矩收缩值；
7. `STEEL`：钢筋支判定和闭式贡献；
8. `EQUILIBRIUM`：\(R_q=0\) 平衡支；
9. `LIMIT`：\(R_q=0,L=0\) 最终状态；
10. `CHECKS`：材料域、钢筋支、残量、零空间积分检查；
11. `EXPERIMENT`：最后单独与试验失效荷载比较。

这个 11 项交付包就是后续统一的“计算闭合”判据。
