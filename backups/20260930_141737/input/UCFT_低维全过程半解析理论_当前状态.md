# UCFT 低维全过程半解析理论 当前状态

更新时间：2026-09-30 13:31 +08:00

## 1. 路线合同

当前最高优先级合同为本轮上传的《指示词.md》。核心身份：
- single-q 主导；
- steel-local A+/A− 从属响应；
- nonlinear membrane condensation；
- UHPC 拉压解析活动集；
- steel Mises deformation theory；
- q-continuation 全过程低维半解析路径。

结构级外层：
\[
q\ \text{给定}\Rightarrow\{P,A^+,A^-\}
\]
并满足：
\[
R_q=0,\qquad R_{A^+}=0,\qquad R_{A^-}=0.
\]

端缩不作为主路径控制变量，Delta(x,q) 后处理恢复。

## 2. 当前锁定几何

\[
W_0=bq_0\sin(\pi x/b)\sin(\pi y/a_h),
\]
\[
W=b(q_0+q)\sin(\pi x/b)\sin(\pi y/a_h),
\]
\[
Q=q^2+2q_0q.
\]

steel-local 保留 qA、A^2 和初始缺陷交叉项，不删除。

## 3. 加劲肋/PBL

不作为独立结构自由度、弹簧或独立轴向承载模块。
报告反力采用：
\[
\chi_w=1+\frac{A_w}{bt_c}\left(\frac{E_s}{E_c}-1\right),
\]
\[
P_{report}=\chi_wP_c+P_s^++P_s^-.
\]
chi_w 只作为工程 reaction correction，不进入 q/A 平衡。

## 4. nonlinear membrane condensation 当前状态

M0：完成并通过。

C0 inner variables：
\[
(E_x,E_y,B_x,B_y),
\]
\[
\varepsilon_x^0=E_x+B_x\cos2X-C_q\cos2Y,
\]
\[
\varepsilon_y^0=E_y-C_q(b^2/a_h^2)\cos2X+B_y\cos2Y,
\]
\[
\gamma_{xy}^0=0,\quad N_{xy}=0.
\]

C1 在 C0 上增加：
\[
H_x,H_y,
\]
\[
\varepsilon_x^0\supset H_x\cos2X\cos2Y,
\]
\[
\varepsilon_y^0\supset H_y\cos2X\cos2Y,
\]
\[
\gamma_{xy}^0
=
-[(b/a_h)H_x+(a_h/b)H_y]\sin2X\sin2Y.
\]

已由 compatible u,v basis 显式生成并解析证明 Hx/Hy 对 compatibility source 的贡献严格为零。

C1 inner residual：
\[
G_{E_x}=G_{E_y}=G_{B_x}=G_{B_y}=G_{H_x}=G_{H_y}=0.
\]

## 5. Gate 状态

Gate 1：PASS。

条件：
- A+=A−=0；
- 全材料退回线弹性；
- 上下对称线弹性 UCFT benchmark。

得到：
\[
H_x=H_y=0,
\]
并严格恢复 Chen–Ji/Airy：
\[
N_{xy}=0,\quad N_x=N_x(y),\quad N_y=N_y(x).
\]

闭式结果已保存于《UCFT_nonlinear_membrane_condensation_当前推导.md》。

Gate 2：NOT STARTED。
Gate 3：NOT STARTED。

## 6. 材料当前合同

UHPC：
- compression/tension 分开；
- 两者用有限阶或分段有限阶多项式；
- 活动区解析识别；
- 不用历史约 10 MPa 旧 PCHIP；
- tensile peak 按最新真实输入，当前认知约 7 MPa 量级；
- 允许 tension softening。

Steel：
- 原 algebraic Mises limiter 仅保留为 baseline；
- 主线为 Chen–Ji-style Mises deformation theory；
- equivalent uniaxial polynomial；
- E_sec/E_tan 分离；
- 局部 elastic/plastic active-set；
- 若主要塑性承载区出现大范围真实卸载，再局部升级 plane-stress J2 flow theory。

## 7. 当前理论问题

无致命矛盾。

记录一个适用边界：
Gate 1 的严格 Chen–Ji 退化针对上下对称线弹性 UCFT benchmark；若人为引入上下不对称产生 extensional-bending coupling，不应要求严格退化为对称单层 Chen–Ji 解。

## 8. 九试件进度

本轮未进入九试件正式计算。

## 9. 已排除/禁止回开的路线

遵循《指示词.md》：
- 31/41/57DOF 作为主理论；
- 独立 curvature unknowns；
- FEM 拟合 q/Pu；
- 经验 A(q)；
- 高维 Gauss integration 定义理论 residual；
- 为制造下降段添加负刚度等。

## 10. NEXT_ACTION

M2：

\[
A^+=A^-=0
\]

打开 UHPC nonlinear tension/compression polynomial active-set。

任务：
1. 构造 C0/C1 current composite membrane kernel；
2. 解析完成厚度方向拉压 active-set；
3. 推导面内活动边界的显式判别；
4. 建立 C0 与 C1 的 nonlinear residual/Jacobian 接口；
5. 在材料参数保持符号化的阶段先完成理论闭合；
6. 随后再进入具体 q-path 数值计算，比较 Hx/Hy 与 omitted shear residual。
