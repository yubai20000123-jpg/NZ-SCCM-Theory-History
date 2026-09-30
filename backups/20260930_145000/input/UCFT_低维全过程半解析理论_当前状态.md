# UCFT 低维全过程半解析理论 当前状态

更新时间：2026-09-30 14:17 +08:00

## 1. 路线合同

当前最高优先级合同：本轮上传《指示词(1).md》。

结构级外层保持：
[
q 	ext{给定}Rightarrow{P,A^+,A^-},
]
并满足
[
R_q=0,qquad R_{A^+}=0,qquad R_{A^-}=0.
]

端缩仍为平衡后派生量，不作为主控制变量。

## 2. 当前几何与 C0/C1

[
W_0=bq_0sin(pi x/b)sin(pi y/a_h),
]
[
W=b(q_0+q)sin(pi x/b)sin(pi y/a_h),
]
[
Q=q^2+2q_0q,qquad C_q=pi^2Q/8.
]

C0：
[
arepsilon_x^0=E_x+B_xcos2X-C_qcos2Y,
]
[
arepsilon_y^0=E_y-C_q(b^2/a_h^2)cos2X+B_ycos2Y,
]
[
gamma_{xy}^0=0,quad N_{xy}=0.
]

C1：
[
arepsilon_x^0supset H_xcos2Xcos2Y,
]
[
arepsilon_y^0supset H_ycos2Xcos2Y,
]
[
gamma_{xy}^0=
-[(b/a_h)H_x+(a_h/b)H_y]sin2Xsin2Y.
]

M0 compatible basis / compatibility identity：PASS。

## 3. Gate 状态

### Gate 1
PASS。

线弹性、A+=A−=0 时：
[
H_x=H_y=0,
quad
N_{xy}=0,
]
严格退化到 Chen–Ji/Airy 分离结构。

### Gate 2
PASS at model-class / diagnostic level。

条件：
[
A^+=A^-=0,
]
打开 UHPC tension/compression polynomial active-set；上下钢壳保持线弹性对称以隔离 UHPC 非线性。

BH050 代表半波诊断：
[
b=a_h=2500 {m mm}, q_0=0.0025, t_c=42 {m mm}, t_s=4 {m mm}.
]

三组非拟合 7 MPa 拉伸多项式族均获得连续 q->P branch。

中央族：
[
f_t=7.0 {m MPa}, r_t=2, arepsilon_{tu}/arepsilon_{tp}=5.
]

q=0~0.02，41 点：
[
max |P_{C1}/P_{C0}-1|=0.04821%.
]

C0 omitted mixed/shear residual：
[
maxeta_H=0.004939=0.4939%.
]

三组拉伸多项式敏感性范围：
[
max |P_{C1}/P_{C0}-1|le0.10898%,
]
[
maxeta_Hle0.004939.
]

结论：
UHPC 材料非线性单独存在时，C1 mixed/shear-compatible channel 确实被激活，但对总 P(q) 的影响在本轮诊断范围内极小。由于 Hx/Cq 在部分 q 区间可达到约 0.22，尚不能宣布 Nxy 严格可删；最终决定推迟至 M3 steel-local mixed-harmonic audit。

Gate 3：NOT STARTED。

## 4. M2 active-set kernel

方向性输入：
[
e_x=(arepsilon_x^U+
u_carepsilon_y^U)/(1-
u_c^2),
]
[
e_y=(arepsilon_y^U+
u_carepsilon_x^U)/(1-
u_c^2).
]

厚度：
[
e=e_m+chi z.
]

阈值：
[
z_j=(e_j-e_m)/chi.
]

每个材料多项式区间均已使用原函数完成：
[
intsigma dz,qquadint zsigma dz
]
闭式积分。

面内 X-Y 方向在本轮只以 Gauss-Legendre 作为 diagnostic numerical evaluator；它不定义 production residual。M4 继续完成正式 moving-boundary 面内解析集成。

## 5. M2 关键修正：q external virtual work

M0 compatible displacement basis 在 y=a_h 给：
[
v(x,a_h)=a_h[E_y-C_q(b^2/a_h^2)].
]

故 q 虚位移改变加载边轴向位移，正式 Rq 必须包含外载虚功：

[
oxed{
R_q=
int_Omega
[N_xarepsilon_{x,q}^0+N_yarepsilon_{y,q}^0+N_{xy}gamma_{xy,q}^0+
M_xkappa_{x,q}+M_ykappa_{y,q}+M_{xy}kappa_{xy,q}],dA
-
P a_h(b^2/a_h^2)C_q'
=0.
}
]

[
C_q'=pi^2(q+q_0)/4.
]

这是“需要修正”的坐标一致性问题，不是路线级失败。

修正后线弹性极限严格恢复：
[
P(q)=P_{cr}rac{q}{q+q_0}+C_A(q^2+2q_0q).
]

M0 compatibility 和 Gate1 membrane condensation 不受影响。

## 6. 当前材料合同

UHPC：
- tension/compression 分开有限阶/分段有限阶多项式；
- 厚度 active-set 解析；
- 当前合同只锁定 tensile peak 约 7 MPa，尚未冻结唯一生产版 tensile peak strain / softening endpoint；
- M2 使用三组不拟合试件的 admissible 7 MPa polynomial family 做鲁棒性诊断，不作为生产参数。

Steel：
- M2 steel-local 关闭，两个钢壳保持线弹性；
- M3 打开 A+/A− 后继续按当前 route；
- M5 再完成 deformation-theory elastic/plastic active-set 正式模块。

## 7. 诊断计算成本

未优化 Python：
- C0 12×12 evaluator 平均约 0.39 s/q点；
- C1 平均约 0.54 s/q点；
- continuation 一般 nfev=3，最大 4。

8×8 与 12×12 的 P(q) 差异在 q<=0.02 的抽查点均小于约 0.003%。

16×16 全路径复核一次尝试超过当前 60 s 单次执行限制，被中止；未完成结果未被采用。

## 8. 持久化数据

Library：
- /UCFT_backups/20260930_141737/output/UCFT_M2_BH050_C0_C1_诊断路径.csv
- /UCFT_backups/20260930_141737/output/UCFT_M2_UHPC拉伸多项式敏感性.csv
- /UCFT_backups/20260930_141737/output/UCFT_M2_面积求积独立核验.csv
- /UCFT_backups/20260930_141737/output/UCFT_M2_nonlinear_membrane_诊断计算器.py

完整正式推导：
- semantic_v2/40_execution/ucft_low_dim_semianalytical/UCFT_nonlinear_membrane_condensation_当前推导.md

## 9. 九试件进度

未进入 M8；M2 只用 BH050 作为代表半波做 mechanism/gate diagnostic，没有使用 FEM 目标值求根。

## 10. NEXT_ACTION

M3：

打开
[
A^+, A^-.
]

不增加额外 membrane modes。

先从 whole-face multiwave steel-local 几何完整展开：
- qA mixed terms；
- A² terms；

建立其有限 mixed-harmonic frequency set，并对 C0/C1 当前 basis 计算 omitted generalized residual spectrum。

只有显著频率才允许激活对应：
[
(H_{x,kl},H_{y,kl})
]
compatible pair。
