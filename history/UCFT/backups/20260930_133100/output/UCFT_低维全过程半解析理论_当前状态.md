# UCFT 低维全过程半解析理论 — 当前状态

**更新时间：2026-09-30 13:31 +08:00**  
**最高层路线合同：用户上传《指示词.md》**  
**当前主攻方向：nonlinear membrane condensation**

## 1. 当前结构级变量

整体路径参数：

[
q
]

每个给定 (q) 上的外层未知量：

[
P,qquad A^+,qquad A^-.
]

不得重新把统一端缩 (Delta) 作为路径控制量。

端部位移、平均端缩和 RP 位移均在平衡后恢复。

## 2. 当前整体几何

[
W_0=bq_0sinrac{pi x}{b}sinrac{pi y}{a_h},
]

[
W=b(q_0+q)sinrac{pi x}{b}sinrac{pi y}{a_h}.
]

Kármán/Marguerre 增量几何源：

[
Q(q)=q^2+2q_0q.
]

## 3. steel-local

[
W_s^+=W+(A_0^++A^+)psi_ell^+,
]

[
W_s^-=W-(A_0^-+A^-)psi_ell^-.
]

必须保留 (qA)、(A^2) 及初始缺陷交叉项。

## 4. PBL/加劲肋

不作为独立轴向力、弹簧、自由度或材料模块。

UHPC 报告反力修正：

[
chi_w
=
1+rac{A_w}{bt_c}left(rac{E_s}{E_c}-1ight).
]

[
P_{m report}
=
chi_wP_c+P_s^++P_s^-.
]

该项为工程 reaction correction，不反向定义 (q,A^pm)。

## 5. nonlinear membrane condensation

### C0

[
arepsilon_x^0
=
E_x+B_xcos2X-C_qcos2Y,
]

[
arepsilon_y^0
=
E_y-C_qrac{b^2}{a_h^2}cos2X+B_ycos2Y,
]

[
gamma_{xy}^0=0,qquad N_{xy}=0.
]

inner variables：

[
E_x,E_y,B_x,B_y.
]

### C1

新增：

[
H_x,H_y
]

并使用：

[
arepsilon_x^0
=
E_x+B_xcos2X-C_qcos2Y
+H_xcos2Xcos2Y,
]

[
arepsilon_y^0
=
E_y-C_qrac{b^2}{a_h^2}cos2X
+B_ycos2Y
+H_ycos2Xcos2Y,
]

[
gamma_{xy}^0
=
-left(
rac{b}{a_h}H_x+rac{a_h}{b}H_y
ight)sin2Xsin2Y.
]

六个 inner residual：

[
G_{E_x},G_{E_y},G_{B_x},G_{B_y},G_{H_x},G_{H_y}=0.
]

## 6. Gate 状态

### Gate 1 — PASS

条件：

- (A^+=A^-=0)；
- 全材料线弹性。

已解析证明：

[
H_x=H_y=0
]

是 C1 唯一 shear 子系统解，并恢复 Chen–Ji/Airy (N_{xy}=0) 分离解。

对上下对称线弹性组合截面：

[
ar
u=rac{A_{12}}{A_{11}},
qquad
ar K=A_{11}(1-ar
u^2),
]

[
B_x=ar
u C_qrac{b^2}{a_h^2},
qquad
B_y=ar
u C_q,
]

[
N_x=-ar K C_qcos2Y,
]

[
N_y=-rac Pb-ar K C_qrac{b^2}{a_h^2}cos2X,
]

[
N_{xy}=0.
]

### Gate 2 — 未执行

要求：

[
A^+=A^-=0
]

打开 UHPC nonlinear active-set，比较 C0/C1。

### Gate 3 — 未执行

打开 steel-local 后，对 (qA)、(A^2) 产生的 mixed harmonics 做 omitted residual spectrum。

## 7. 当前 UHPC 材料合同

压、拉分别采用多项式/分段多项式。

禁止恢复旧约 10 MPa PCHIP 拉伸峰值。

当前拉伸峰值认知约为 7 MPa 量级；正式 M2 必须用最新用户材料输入或可靠来源锁定具体多项式。

正式区域判断采用材料 operator 输入 (e_x,e_y)，优先解析 active-set，不以三维 Gauss 点定义理论。

## 8. 当前 steel 材料合同

主线：

Chen–Ji-style Mises deformation theory
+ equivalent uniaxial polynomial
+ (E_{m sec}/E_{m tan}).

旧 radial Mises cap 仅作为 baseline。

若主要塑性区发生明显 (darepsilon_i/dq<0) 或强非比例加载，只升级材料 operator 为 plane-stress J2 flow theory，不改变结构级 (q,A^pm) 框架。

## 9. 本轮记录但不阻塞的边界审计

当前最低阶 C0/C1 compatible displacement basis 与 Chen–Ji straight-edge 线弹性退化一致。

由于总体路线不允许把统一端缩作为外部控制，后续 nonlinear Gate 2 / Gate 3 需监测是否存在显著 end-warping omitted residual；只有显著时才增加 compatible enrichment，不新增前置 Gate。

## 10. 已明确排除的主路线

不得在当前理论未被严格证伪前重开：

- 31/41/57 DOF 大系统；
- 独立曲率变量；
- FEM 调 q / 标定 Pu；
- 大量空间 Gauss 点定义 residual；
- HT/Trefftz 取代当前主线；
- 人为负刚度制造下降段；
- 首次开裂/首次屈服/steel local peak 直接定义 Pu。

## 11. 当前唯一 NEXT_ACTION

执行 M2：

[
A^+=A^-=0
]

打开 UHPC nonlinear tension/compression polynomial active-set，建立并计算：

[
P_{C0}(q),quad
P_{C1}(q),quad
H_x(q),quad
H_y(q),quad
widehat G_{H_x}(q),quad
widehat G_{H_y}(q).
]

M2 的目标仅是判断材料非线性本身是否激活 shear membrane channel，不使用 FEM 拟合。
