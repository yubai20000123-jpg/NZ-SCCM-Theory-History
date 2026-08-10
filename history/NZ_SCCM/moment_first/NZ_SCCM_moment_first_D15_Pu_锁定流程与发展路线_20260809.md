# NZ-SCCM：moment-first D15 极限承载力流程锁定稿  
## ——普通混凝土 / UHPC current material operator、Case21 concrete-only \(P_u\)、解析积分核与后续钢筋/钢壳扩展

**版本日期：2026-08-09**  
**状态：历史阶段锁定稿；后续身份以 CURRENT_STATE / 2026-08-10 priority reset 为准。**

## 0. 本文件的用途

本文件用于保存 2026-08-09 时点 NZ-SCCM 极限承载力理论的计算主线、材料接口、数学实现方式、Case21 验收结果和当时未来扩展方向。它是历史证据，不应覆盖后来的 priority reset。

# 1. 研究目标与用户约束

本项目真正关心的是有限幅值平衡路径上的极限承载力：

\[
P_u=\max_{\text{可达平衡路径}} P .
\]

在光滑极限点处，当时采用：

\[
R_A(D,A)=0
\]

与

\[
L(D,A)=P_{,D}R_{A,A}-P_{,A}R_{A,D}=0
\]

共同确定极限状态。材料非光滑事件控制时比较事件两侧 one-sided states。

当时锁定要求包括：正式空间积分零数值积分；不允许连续板切成材料点云再用 Gauss/Simpson/adaptive quadrature；不采用板级 Chebyshev surrogate；材料 current operator 写为 \(\sigma=M(\varepsilon)\)；不使用运行时 TT/TC/CC 分类作为生产主线；不以材料点 Newton/history array/load-step history 为正式主线；切线由同一 current map 求导；材料拟合优先面向文献公式而非结构 Pu；结构试验不得反标材料；理论必须人工可审计。

# 2. 为什么采用 current material operator

在单调轴压、固定边界、一个连续完整代表半波、不研究循环卸载、结构未知量有限的限定下，给定 \(D,A\) 后连续应变场已知，因此直接使用：

\[
(D,A)\rightarrow\varepsilon(X,Y,\zeta)\rightarrow M(\varepsilon)\rightarrow\sigma(X,Y,\zeta)\rightarrow P,R_A,L.
\]

其目的在当时是切断传统 FE 式“空间点→状态分类→历史变量→材料点迭代→应力”链条。

# 3. 当前结构运动学（该历史阶段）

固定一个连续完整代表半波、active mode \(m=1\)、Nguyen 二阶运动学、初始缺陷与加载后幅值分开。

\[
X=\pi x/b,\qquad Y=\pi y/\ell,\qquad\zeta=2z/t,
\]

\[
\phi=\sin X\sin Y,\qquad w=(A_0+A)\phi,
\]

\[
q=A/b,\qquad q_0=A_0/b,
\]

\[
S=q_0q+\frac12q^2.
\]

Case21 \(b=\ell\) 时：

\[
e_x=\nu D+C_m\cos^2X\sin^2Y+C_b\sin X\sin Y\,\zeta,
\]

\[
e_y=-D+C_m\sin^2X\cos^2Y+C_b\sin X\sin Y\,\zeta,
\]

\[
g_{xy}=\cos X\cos Y[2C_m\sin X\sin Y-2C_b\zeta],
\]

\[
C_m=\frac{\pi^2}{\varepsilon_0}(q_0q+\tfrac12q^2),
\qquad
C_b=\frac{\pi^2}{2\varepsilon_0}\frac tbq.
\]

物理应变为 \(\varepsilon_0(e_x,e_y,g_{xy})\)。

# 4. 普通混凝土 NC 来源背景

Nguyen Chapter 3 / Appendix B 提供 biaxial peak envelope、equivalent-uniaxial secant/tangent、Saenz compression、tension stiffening、shear retention、TC、TT、CC、TCX、bilinear reinforcement。项目 equation-to-code registry 曾逐项登记这些来源。

当时 current 约化保留 Saenz 型压缩骨架、Nguyen/Foster 拉伸结构及低参数 CC/TC/TT interaction。参数必须是材料级来源，不用 Case21/Swartz Pu 反标。

# 5. UHPC 来源背景（历史阶段身份）

该阶段曾组织：Zhang 2023 compression、Hiew 2024 tension、Liu 2023 TC、Liu 2024 biaxial strength、Wang/周俊三轴资格审计。后续已经明确：这套 UHPC 组织属于历史可计算/候选链，不等于最终冻结的完整 UHPC 多轴/history operator。

# 6. 统一 current tensor 接口

\[
\mathbf E=\begin{bmatrix}\varepsilon_x&\gamma_{xy}/2\\\gamma_{xy}/2&\varepsilon_y\end{bmatrix},
\]

\[
\mathbf E_u=\frac{(1-\nu)\mathbf E+\nu\operatorname{tr}(\mathbf E)\mathbf I}{1-\nu^2},
\qquad
\mathbf X_M=\mathbf E_u/\varepsilon_{0,M}.
\]

随后 \(\sigma_M=M_M(\mathbf X_M)\)，切线由同一 operator 求导。

# 7. 为什么不再生成自由二维大系数表

几十乃至更多二维 Chebyshev 自由系数会造成物理意义不清、stress/tangent 同时约束困难、高阶内部振荡、来源关系难保持以及空间展开项数爆炸。因此当时转向“少数一维来源函数 + 少数低参数 tensor interaction”。

# 8. D15 精确矩

基本空间矩：

\[
\mathcal I_{abh}=\int_0^\pi\sin^aX\,dX\int_0^\pi\sin^bY\,dY\int_{-1}^{1}\zeta^h\,d\zeta.
\]

\[
\int_0^\pi\sin^nX\,dX=\sqrt\pi\frac{\Gamma((n+1)/2)}{\Gamma((n+2)/2)},
\]

\[
\int_{-1}^1\zeta^h\,d\zeta=0\;(h\text{ odd}),\qquad=2/(h+1)\;(h\text{ even}).
\]

只要 integrand 写成有限三角—厚度代数组合，空间积分可由解析矩完成。

# 9. expand-all then D15 的淘汰

错误组织是完整展开巨大 \(\sigma(X,Y,\zeta)\) 后再 D15，导致表达爆炸、内存急剧增长和人工不可审计。由此转为 moment-first contraction：每生成一个结构真正需要的解析材料矩对象，立即施加目标积分泛函，不保留不必要的巨大空间展开。

# 10. Q_nm 与 moment-first 的严格意义

对解析基函数 \(T_n,T_m\)，定义连续场：

\[
Q_{nm}(X,Y,\zeta;D,q)=\mathcal C[T_n,T_m].
\]

它不是空间点。通过二维 Cayley-Hamilton 可写成：

\[
Q_{nm}=\frac12(S_{nm}-K_1A_{nm})\mathbf I+A_{nm}\mathbf Z.
\]

对轴力和幅值平衡分别施加解析线性泛函：

\[
M_{nm}^{P}=\mathscr L_P[Q_{nm}],
\qquad
M_{nm}^{R}=\mathscr L_R[Q_{nm}].
\]

所谓“立即积分并删除空间变量”是完成解析积分后的代数收缩，不是离散化。与 Gauss 求和的区别是正式成本依赖解析项数而不是空间点数。

# 11. Case21 concrete-only 历史验收

输入：

\[
a=2440\text{ mm},\;b=\ell=1220\text{ mm},\;t=19.30\text{ mm},
\]

\[
f_c=21.23\text{ MPa},\;E_0=20321\text{ MPa},\;\varepsilon_0=0.00209,\;\nu=0.18,
\]

\[
A_0=b/400=3.05\text{ mm}.
\]

试验失效荷载：

\[
P_{f,\exp}=368.312750\text{ kN}.
\]

该历史阶段 concrete-only moment-first D15 得到约：

\[
P_{u,c}^{D15}\approx339.1\text{ kN},\quad D_u\approx0.7955,\quad q_u\approx1.974\times10^{-3},\quad A_u\approx2.41\text{ mm}.
\]

独立高阶空间数值积分 audit 对同一 current operator/运动学约得 \(339.6\) kN，差约 0.15%。数值积分仅是 audit，不是正式生产积分。

后续更高精度 current-operator 实现产生约 338.318 kN concrete / 342.334 kN RC 的 verification references；因此 339.1 kN 应保留为这一 moment-first 历史阶段结果，不要误写成当前唯一数值真值。

# 12. 钢筋扩展的长期有效原则

钢筋连续应变：

\[
\varepsilon_s^{(r)}=\mathbf n_r^T\mathbf E\mathbf n_r,
\]

钢筋贡献必须进入 \(P_s\) 和 \(R_{A,s}\)：

\[
P=P_c+P_s,\qquad R_A=R_{A,c}+R_{A,s}.
\]

然后重新联立极限条件。禁止先求 concrete-only Pu 再事后加 \(A_sf_y\)。这一原则在后续当前理论中仍有效。

# 13. 钢壳 / UCFT 扩展思想

历史上提出钢壳区域也进入同一结构残量/荷载积分，并由来源明确的 steel law 提供应力。后续当前严格 benchmark 尚未最终冻结 \(M_{shell}\)，因此本节只保留为历史扩展思想；云露/张宁/孙立鹏等来源需在新 shell operator 冻结前重新恢复。

# 14. 当时的后续顺序与后来修正

当时建议顺序为：Case21 钢筋 → Swartz24 → UHPC → shell/UCFT。2026-08-10 priority reset 后，strict theorem certificate 已降级，当前 Nguyen/Foster 仅作为 benchmark，并允许 final-attempt 失败后重新建立 material/target/solution operator。因此本文件不得独立覆盖当前治理。

# 15. 长期仍有效的核心

即使后续材料 operator 重新设计，以下思路仍是重要历史遗产：

\[
\boxed{\text{连续运动学}\rightarrow\text{材料 operator}\rightarrow\text{解析矩/全局收缩}\rightarrow P,R,L\rightarrow P_u}
\]

并且正式理论不得把空间材料点、Gauss/Simpson、自适应空间积分或板级 Pu 拟合偷偷恢复为核心理论单位。
