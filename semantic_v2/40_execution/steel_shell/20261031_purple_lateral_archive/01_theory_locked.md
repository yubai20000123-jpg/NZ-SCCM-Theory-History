# UCFT钢壳紫线L7双模态＋非线性横向平均膜力释放：当前锁定基准

**锁定日期**：2026-10-31 ；**研究性质**：可重算的钢壳降阶候选理论 / 诊断分支归档；**并非已经成立的UCFT极限承载力理论**。

## A. 来源和版本治理

原始紫线（2026-10-25）为四边固支正方板、单个鼓曲幅值、一元轴向压应变平衡，主要模块为：von Kármán增量几何、弹性能量预凝聚的面内协调、七Lagrange带符号投影、连续应力Mises二次矩投影、厚度弹塑性根与塑性端点弦线、内部顶点双弦、七节点缺失弹性抗弯矩恢复、正向独立膜虚功容量。来源参见 `source/理论重建与验收.md` 及原版紫线报告。

本版**已改变**：1) 面外从原单波改为整体正弦Φ＋局部固支子仓Ψ，幅值W/A；2) 添加与轴压方向垂直的均匀应变 e_perp，并且**在Mises非线性应力积分后**强制全板平均横向膜力为零；3) 采用六个显式Fourier面内试函数进行弹性预凝聚；4) 保留紫线原材料截面算子，重新计算全部几何矩、弹性抗弯缺失矩、两模态临界应变；5) 双模态膜容量为**未经充分验证的新候选规则**，不能称作原紫线恒等推广。

**不可混同**：原紫线七Lagrange节点不是2026-10-29 S14/B7所用七Bernstein正权重条件；不可混用投影矩或沿用旧0.4875、旧177069.9485 MPa、旧g_j。此钢壳横向平均应力零属于本次独立钢壳试算条件；迁移到完整钢壳–UHPC组合界面后是否可以对每层分别施加零横向膜力，需要根据组合结构共同横向传力重新确认，不应擅自视为逐层零横向力。

## B. 几何与完整应变（x横向，y轴压）

域 0≤x≤b，0≤y≤a，钢厚t；X=πx/b，Y=πy/a；N,m为正整数，PBL只通过局部边界与波数体现，没有独立接触和剪力自由度。

\[
\Phi=\sin X\sin Y,\quad \Psi={1\over4}(1-\cos2NX)(1-\cos2mY),\quad 0\le\Psi\le1.
\]
\[
 w_0=W_0\Phi+A_0\Psi,\qquad w_t=(W_0+W)\Phi+(A_0+A)\Psi,\qquad \Delta w=W\Phi+A\Psi.
\]

本轮数值输入W0=b/400、A0=t/60，二者均为归一化形函数最大幅值，并非固定的普适物理常数。

几何导数：
\[
\begin{aligned}
\Phi_x&=\pi\cos X\sin Y/b,&\Phi_y&=\pi\sin X\cos Y/a,\\
\Phi_{xx}&=-\pi^2\Phi/b^2,&\Phi_{yy}&=-\pi^2\Phi/a^2,&\Phi_{xy}&=\pi^2\cos X\cos Y/(ab),\\
\Psi_x&=N\pi\sin(2NX)(1-\cos2mY)/(2b),&\Psi_y&=m\pi(1-\cos2NX)\sin(2mY)/(2a),\\
\Psi_{xx}&=N^2\pi^2\cos(2NX)(1-\cos2mY)/b^2,\\
\Psi_{yy}&=m^2\pi^2(1-\cos2NX)\cos(2mY)/a^2,\\
\Psi_{xy}&=Nm\pi^2\sin(2NX)\sin(2mY)/(ab).
\end{aligned}
\]

设Z=2W0W+W²，H=W0A+A0W+WA，J=2A0A+A²，三个完整几何膜应变：
\[
\begin{aligned}
\epsilon_{x,g}&={Z\over2}\Phi_x^2+H\Phi_x\Psi_x+{J\over2}\Psi_x^2,\\
\epsilon_{y,g}&={Z\over2}\Phi_y^2+H\Phi_y\Psi_y+{J\over2}\Psi_y^2,\\
\gamma_{xy,g}&=Z\Phi_x\Phi_y+H(\Phi_x\Psi_y+\Phi_y\Psi_x)+J\Psi_x\Psi_y.
\end{aligned}
\]

面内位移：u=e_perp x+Σ(c_i U_i)，v=−d y+Σ(c_i V_i)，其中d>0为规定端缩率。原六个(U_i,V_i)固定为：

1. U1=b sin2X/(2π), V1=0；2. U2=b sin2X cos2Y/(2π), V2=0；3. U3=0, V3=a sin2Y/(2π)；4. U4=0, V4=a cos2X sin2Y/(2π)；5. U5=b sin2NX(1−cos2mY)/(2πN),V5=0；6. U6=0,V6=a(1−cos2NX)sin2mY/(2πm)。

记β_i=(U_{i,x},V_{i,y},U_{i,y}+V_{i,x})^T，C=E/(1−ν²)[[1,ν,0],[ν,1,0],[0,0,(1−ν)/2]]，则线弹性预凝聚：
\[
K_{ij}=\langle\beta_i^TC\beta_j\rangle,\quad f_i=\langle\beta_i^TC[(e_\perp,-d,0)^T+\epsilon_g]\rangle,\quad \mathbf c=-K^{-1}\mathbf f.
\]
这里c_i通过**常系数6×6线性代数**直接求得，不作为每一状态的非线性全局未知量。

中面\(\epsilon_m=(e_\perp,-d,0)^T+\sum_i c_i\beta_i+\epsilon_g\)；\(\xi=z/t\in[-1/2,1/2]\)；穿厚应变
\[
\epsilon(x,y,\xi)=\epsilon_m(x,y)-\xi t\left\{W(\Phi_{xx},\Phi_{yy},2\Phi_{xy})^T+A(\Psi_{xx},\Psi_{yy},2\Psi_{xy})^T\right\}.
\]
这条式子中整体—局部交叉项与初始缺陷项不得删除。

## C. 原紫线七Lagrange、Mises和弹性核心抗弯

\[T=\Psi^2=\sin^4(NX)\sin^4(mY),\quad q_j=[1-\cos((j-1)\pi/6)]/2,\quad L_j(T)=\prod_{i\neq j}(T-q_i)/(q_j-q_i).\]
\[\omega_j=\langle L_j\rangle,\quad\langle g\rangle=(ab)^{-1}\int_0^b\int_0^a g\,dx\,dy,\quad\sum_j\omega_j=1.\]
在整数N,m且整周期板面下，七权重恰为（与原单波相同）：0.500219492096、0.237107230231、0.114016222166、0.079537631614、0.0443196591805、0.0234455367735、0.00135422793877。其他几何矩**不能**沿用原数值。

给定当前\(\epsilon_m\)和曲率\(k_t=-t[W\operatorname{Hess}\Phi+A\operatorname{Hess}\Psi]\)（工程剪曲率含2），先由完整连续试应力\(s^0=C\epsilon_m\)和\(s^1=Ck_t\)计算：
\[
Q_j(\xi)=\frac{\langle L_j(s^0+\xi s^1)^T H_M(s^0+\xi s^1)\rangle}{\omega_j}=q_{0j}+q_{1j}\xi+q_{2j}\xi^2,
\]
\[H_M=\begin{bmatrix}1&-1/2&0\\-1/2&1&0\\0&0&3\end{bmatrix}.\]
代表试应力\(\widehat s_j(\xi)=\langle L_j(s^0+\xi s^1)\rangle/\omega_j\)。厚度屈服界面\(Q_j(\xi)=f_y^2\)，子段中Q≤fy²采用仿射弹性应力精确积分；超限段在两端采用\(\widehat s_j(\xi)f_y/\sqrt{Q_j(\xi)}\)，两端之间以一次弦线积分。当整个厚度均超限且内部凸二次顶点\(\xi_*=-q_1/(2q_2)\in(-1/2,1/2)\)时，采用\([-1/2,\xi_*]\)和\([\xi_*,1/2]\)两塑性弦线。全部得到三向\(n_j=\int\widehat\sigma_jd\xi\)和\(m_j=\int\xi\widehat\sigma_jd\xi\)。当Lagrange带符号投影使Q_j为负时，应标记非物理代理状态，不得冒充真实材料点。

弹性抗弯缺失采用\(\Delta D_{pq}=\langle\kappa_p^T C\kappa_q\rangle-\sum_j\omega_j\widehat\kappa_{p,j}^TC\widehat\kappa_{q,j}\)，p,q∈{W,A}，\(\chi_D=12\sum_j\omega_j\sum_{[l,h]\in E_j}(h^3-l^3)/3\)，\(R_{D,p}=\chi_D(\Delta D_{pW}W+\Delta D_{pA}A)/12\)。只修正紫线原有的**弯曲能遗漏项**，不额外补膜能。

**未锁定为物理定律的部分：双模态膜容量。** 当前代码用\(g_{j,p}=\max(0,1-\varepsilon_{cr,p}/E_j)\)和\(R_{cap,p}=-\sum_j\omega_jg_{j,p}\max(B_{j,p},0)\)，其中E_j和B_j来自当前方向的平均正交膜虚功。它从原紫线单模态容量推广，但仍属于**新候选假定**；现有纯钢壳试算未实现合理局部波发展的全过程。保持原程序行为以便审计，不能据此声称已经得到准确Pu。

## D. 三条平衡、输出和性质

给定端缩率d，求W≥0、A≥0、e_perp：
\[
R_W=\sum_j\omega_j[n_j\cdot(\partial\widehat\epsilon_{m,j}/\partial W)+m_j\cdot\widehat\kappa_{W,j}]+R_{D,W}+R_{cap,W}=0,
\]
\[
R_A=\sum_j\omega_j[n_j\cdot(\partial\widehat\epsilon_{m,j}/\partial A)+m_j\cdot\widehat\kappa_{A,j}]+R_{D,A}+R_{cap,A}=0\quad(A>0),
\]
\[R_\perp=\sum_j\omega_jn_{x,j}=0.\]
当A=0时检查单侧不等式R_A≥0；当前压力试算的总轴向荷载由截面平均代理\(P=-bt\sum_j\omega_jn_{y,j}\)输出，不再从P中重复扣除膜容量。若将来增设对d依赖的非均匀面内位移，必须另外核验该轴力与端缩共轭反力的一致性。

**代数维数**：外层W/A二元，内层横向应变一元；严格代数未知三元。六个面内c_i只涉及固定线性系统，无板面Gauss、Simpson或空间网格。代码中求根扫描和候选枝跟踪是数值求方程，不是积分离散。

## E. 已执行验收与明确未解决项

执行 source/check_geometry_energy.py 和 source/rebuild_lateral.py，两种b=a分别2500/5000mm、t=4mm、E=206000MPa、ν=.3、fy=355MPa、N=5,m=4，W0=b/400、A0=t/60。七节点权重和偏离1≈1.4×10⁻¹⁴；弹性投影膜能＋连续抗弯能的W/A/e_perp虚功导数误差最高约1.7×10⁻⁹；给定(d,W,A)时非线性\(R_\perp\)可达1e−14 MPa量级。

source/trial_fixed_20261031.csv、source/phase_scan_20261031.csv：主搜索解绝大部分A=0；2500mm和5000mm已搜索分支峰值约0.013718445 MN/0.006842382 MN，仅为采样极值，不是连续根支稳定性验证后的Pu；峰后突降伴随χD急剧降低。尚未形成可信多波局部后屈曲曲线，也没有UHPC、PBL真实界面或完整UCFT极限承载力。

**冻结策略**：当前源代码与数据只归档不覆盖原2026-10-25纯钢板紫线；未来修改UHPC或膜容量从此独立分支起步；任何后续新曲线标明改变了哪个模块，保留原样可复算输出。