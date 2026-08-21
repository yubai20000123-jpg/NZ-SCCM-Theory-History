# NZ-SCCM — PRE-MEMBRANE MULTIPHASE VOLUME-CONSERVING THEORY V1

简称：`PMV1`  
时间：2026-08-21 15:15 +08:00  
状态：`ACTIVE FORMAL THEORY CANDIDATE / PHASE ACCOUNTING LOCKED / NO EMPIRICAL FIT`

> 本文件的作用等同于此前 NC-M4 的“正式候选公式”文件：把当前可接受理论写成一套可直接实现、可逐式审计的固定数学合同。PMV1 是**结构/多相组装理论层**，不是新的混凝土材料 M7，也不修改 R10。

---

## 1. 理论边界

```text
FORMAL_DOMAIN = ONE_CONTINUOUS_COMPLETE_HALFWAVE
GENERALIZED_COORDINATES = D,q
KINEMATICS = NGUYEN_SECOND_ORDER
CONCRETE = R10 -> N48-C1/MM -> Cayley-Hamilton
EXACT_MOMENTS = GENERAL-D15
FORMAL_SPATIAL_SAMPLING = 0
FORMAL_SPATIAL_QUADRATURE = 0
FORMAL_SPATIAL_SUBDOMAINS = 1
NEW_MEMBRANE_REDISTRIBUTION = DISABLED
RITZ_MEMBRANE_DOF = 0
EMPIRICAL_LOAD_CALIBRATION = PROHIBITED
```

PMV1 的新锁定点只有一个：**所有真实材料相位必须满足体积守恒，不允许“100% 基体 + 额外钢材”的材料重复计数。**

---

## 2. 一个连续完整半波运动学

定义

\[
X=\pi x/b,\qquad Y=\pi y/\ell,\qquad k=b/\ell,
\]

\[
\phi=\sin X\sin Y,
\]

\[
w_0=bq_0\phi,\qquad \Delta w=bq\phi.
\]

取

\[
M(q)=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right),
\]

对厚度为 `t` 的连续相位定义

\[
B_t(q)=\frac{\pi^2t}{2\varepsilon_0b}q,
\qquad \zeta=2z/t.
\]

历史 pre-membrane Nguyen 归一化应变为

\[
\boxed{
e_x=\nu D+M\cos^2X\sin^2Y+B_t\phi\zeta
}
\]

\[
\boxed{
e_y=-D+k^2M\sin^2X\cos^2Y+k^2B_t\phi\zeta
}
\]

\[
\boxed{
g_{xy}=2kM\sin X\cos X\sin Y\cos Y-2kB_t\cos X\cos Y\zeta
}
\]

物理应变：

\[
\varepsilon_x=\varepsilon_0e_x,
\quad
\varepsilon_y=\varepsilon_0e_y,
\quad
\gamma_{xy}=\varepsilon_0g_{xy}.
\]

本式中不新增膜重分布自由度。

---

## 3. 混凝土 current map：R10 -> N48 -> CH

### 3.1 R10 标量源

定义

\[
\kappa=E_0\varepsilon_0/f_c,
\qquad
x_{cr}=0.1/\kappa,
\qquad
\eta=x_{cr}/20.
\]

平滑正部函数

\[
\Pi(z)=\frac{z^2(\sqrt{z^2+\eta^2}+z)}{2(z^2+\eta^2)}.
\]

令

\[
c=\Pi(-\lambda),\qquad t=\Pi(\lambda),
\]

压缩函数

\[
C(\lambda)=\frac{\kappa c}{1+(\kappa-2)c+c^2}.
\]

拉伸源函数 `u_R(t)` 保持冻结 R10 的五次上升支、五次下降支与残余平台；令

\[
T(\lambda)=u_R(t)/\rho,\qquad \rho=0.1,
\]

\[
U(\lambda)=\kappa\lambda-C(\lambda)+\kappa c+u_R(t)-\kappa t.
\]

同时使用 `T^7`。

### 3.2 N48 解析编译

在由材料域预先确定、不得由试验荷载选择的区间

\[
\lambda\in[\lambda_a,\lambda_b],
\]

定义

\[
\lambda_c=(\lambda_a+\lambda_b)/2,
\quad
\lambda_h=(\lambda_b-\lambda_a)/2,
\quad
\xi=(\lambda-\lambda_c)/\lambda_h.
\]

对

\[
F\in\{U,C,T,T^7\}
\]

写为

\[
F_{48}(\lambda)=\sum_{n=0}^{48}a_n^{(F)}\mathcal C_n(\xi).
\]

系数由冻结 N48-C1/MM 规则或其 source-consistent interval 生成，不允许根据结构试验荷载修改。

### 3.3 二维 Cayley-Hamilton current map

由归一化物理应变构造等效张量

\[
X_{xx}=\frac{e_x+\nu e_y}{1-\nu^2},
\]

\[
X_{yy}=\frac{\nu e_x+e_y}{1-\nu^2},
\]

\[
X_{xy}=\frac{g_{xy}}{2(1+\nu)}.
\]

令其主值为 `lambda_1,lambda_2`。在主方向上定义

\[
s_1=U_1-a_{cc}C_1^2C_2+C_1T_2-\rho a_tT_1T_2T_2^7,
\]

\[
s_2=U_2-a_{cc}C_1C_2^2+C_2T_1-\rho a_tT_1T_2T_1^7,
\]

其中

\[
a_{cc}=0.1072329249362415,
\qquad
a_t=1-2^{-1/8}.
\]

旋转回板坐标得到

\[
\boldsymbol\sigma_c=f_c\mathbf S(e_x,e_y,g_{xy}).
\]

全部应力、残量和切线必须来自这一 current map 的同一表达式。

---

## 4. 外钢板相位

外钢板厚 `t_s`，弹性试应力：

\[
\sigma_x^{tr}=\frac{E_s}{1-\nu_s^2}(\varepsilon_x+\nu_s\varepsilon_y),
\]

\[
\sigma_y^{tr}=\frac{E_s}{1-\nu_s^2}(\nu_s\varepsilon_x+\varepsilon_y),
\]

\[
\tau^{tr}=\frac{E_s}{2(1+\nu_s)}\gamma_{xy}.
\]

\[
\sigma_{VM}^{tr}=\sqrt{(\sigma_x^{tr})^2-\sigma_x^{tr}\sigma_y^{tr}+(\sigma_y^{tr})^2+3(\tau^{tr})^2}.
\]

定义精确 local radial cap：

\[
\boxed{
\alpha_s=\min\left(1,\frac{f_y}{\sigma_{VM}^{tr}}\right)
}
\]

\[
\boxed{
(\sigma_x,\sigma_y,\tau)_s=\alpha_s(\sigma_x^{tr},\sigma_y^{tr},\tau^{tr})
}.
\]

本函数是正式钢材相位函数。Chebyshev degree 只是其解析编译实现参数，不属于理论参数。

---

## 5. MCFSTW 内部纵向钢腹板相位

若源截面满足单元节距 `l_s`、钢厚 `t_s`、`b=n_sl_s`，定义

\[
\boxed{\rho_w=t_s/l_s}.
\]

等效腹板钢面积：

\[
\boxed{A_w=\rho_wbt_c=n_st_st_c}.
\]

剩余混凝土面积：

\[
\boxed{A_c=(1-\rho_w)bt_c}.
\]

腹板只保留加载方向材料作用：

\[
u_w=E_s\varepsilon_y/f_y,
\]

\[
\alpha_w=\min(1,1/|u_w|),
\]

\[
\boxed{\sigma_y^w=f_yu_w\alpha_w}.
\]

亦即标准一维理想弹塑性形式：

\[
\sigma_y^w=\operatorname{clip}(E_s\varepsilon_y,-f_y,f_y).
\]

它表示**腹板材料量和纵向轴压贡献**，不表示离散腹板的周期支承、局部腹板屈曲或完整正交各向异性拓扑。

---

## 6. RC 钢筋相位与混凝土体积替换

对源定义的正交钢筋体积分数

\[
\rho_{s,x},\rho_{s,y},
\]

定义

\[
\boxed{\rho_{s,tot}=\rho_{s,x}+\rho_{s,y}}.
\]

钢筋占据真实材料体积，因此矩阵混凝土比例必须为

\[
\boxed{\chi_c=1-\rho_{s,tot}}.
\]

钢筋 current law 为来源一致的一维钢材关系；在 Swartz24 当前极限状态全部未屈服，因此退化为

\[
\sigma_s=E_s\varepsilon_s.
\]

对于历史 square-halfwave、弹性钢筋闭式，加载方向轴力为

\[
P_s=\rho_{s,y}bt_pE_s\varepsilon_0
\left(D-\frac{M}{4}\right),
\]

相应双向钢筋 `R_{q,s}` 沿用已冻结闭式。

---

## 7. 多相总轴力与广义残量

### 7.1 钢箱/钢腹板体系

混凝土 full-core resultants 记为 `P_c^full,R_qc^full`，则

\[
\boxed{
P=(1-\rho_w)P_c^{full}+P_w+P_{sh}
}
\]

\[
\boxed{
R_q=(1-\rho_w)R_{q,c}^{full}+R_{q,w}+R_{q,sh}
}.
\]

### 7.2 RC 板

\[
\boxed{
P=(1-\rho_{s,tot})P_c^{full}+P_s
}
\]

\[
\boxed{
R_q=(1-\rho_{s,tot})R_{q,c}^{full}+R_{q,s}
}.
\]

所有相位共享同一个连续 Nguyen 结构场；没有材料点网格和空间子域。

---

## 8. 极限承载力定义

首先求 connected equilibrium branch：

\[
\boxed{R_q(D,q)=0}.
\]

极限点由同源两变量 Jacobian 的约束极值条件给出：

\[
\boxed{
L(D,q)=P_{,D}R_{q,q}-P_{,q}R_{q,D}=0
}.
\]

因此

\[
\boxed{(D_u,q_u):\quad R_q=0,\ L=0}
\]

\[
\boxed{P_u=P(D_u,q_u)}.
\]

禁止：

- 用试验/周思铭荷载选根；
- 取“最接近试验”的根；
- 另建第二套 Pu 求解器；
- 为大误差案例临时增加膜自由度。

---

## 9. D15 正式积分接口

若任一相位应力/广义内功在

\[
u=\sin X,\quad v=\sin Y,\quad \zeta
\]

的有限解析基上表示为

\[
F=\sum c_{ijk}\mathcal C_i(u)\mathcal C_j(v)\mathcal C_k(\zeta),
\]

则

\[
\iiint F=\sum c_{ijk}M_iM_jZ_k,
\]

\[
M_0=\pi,
\quad M_n=\frac{2\sin(n\pi/2)}n,
\]

\[
Z_k=0\;(k\ odd),
\quad Z_k=\frac{2}{1-k^2}\;(k\ even).
\]

因此 PMV1 的正式结构计算仍保持零空间数值积分。

---

## 10. 当前验证身份

### Steel-shell Z0-Z5

补回真实腹板材料以后：

```text
signed errors = +0.755% ... +9.973%
mean signed   = +6.898%
sample std    = 3.798 pp
max abs       = 9.973%
```

这是一组统一正偏，不设置 `1/1.06898` 等经验校正系数。

### Swartz24

钢筋体积守恒修正仅造成约 0.2%-1.0% 量级的承载力变化，不能解释原样本的大散差。因此 Swartz24 继续作为 specimen-realization robustness set；PMV1 不以增加结构自由度追逐各单板结果。

---

## 11. 当前适用性与明确遗漏机制

PMV1 当前明确遗漏：

1. 离散钢腹板对外面板的周期侧向支承；
2. 独立腹板板件局部屈曲；
3. 离散 cell topology 对 `Dx,Dy,Dxy,Dmu,H` 的完整影响；
4. 试件初始几何/材料随机偏差；
5. 非理想边界实现。

这些遗漏可形成系统偏差或试验散差，但不得在没有独立物理模型时转化成经验拟合系数。

Z6 继续保持：

```text
OUT_OF_CURRENT_VALIDATED_STEEL_SHELL_DOMAIN_DIAGNOSTIC
```

不得以 Z6 重新开启 Ritz/膜重分布生产分支。

---

## 12. 理论与数值实现的冻结层级

```text
PMV1_PHASE_VOLUME_EQUATIONS = LOCKED CANDIDATE
R10_MATERIAL = UNCHANGED
STEEL_IDEAL_EP_CURRENT_LAW = LOCKED CANDIDATE
Z0_Z5_WEB_MATERIAL_PHASE = REQUIRED
RC_REBAR_VOLUME_REPLACEMENT = REQUIRED
EMPIRICAL_SCALE_FACTOR = NONE
```

尚未冻结为 production 常数的是：

```text
LOCAL_STEEL_CAP_CHEBYSHEV_DEGREE = NOT YET LOCKED
```

原因：degree16/24/32 对 Z0-Z5 Pu 的当前 spread 为约 0.3%-1.6%。最终实现必须根据**材料函数本身的解析误差/阶次收敛**确定阶数，不能根据 Zhou/试验荷载确定。

这一区分与 NC-M4 做法一致：先锁定物理材料/结构公式，再锁定其解析编译实现。