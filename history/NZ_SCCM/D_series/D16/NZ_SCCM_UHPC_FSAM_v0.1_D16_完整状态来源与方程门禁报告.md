# UHPC-FSAM v0.1：完整状态来源注册、显式方程恢复与解析矩门禁报告

> Archive identity: complete text recovered from File Library `file_000000003c588230b6557f5355bac9a9`. Historical D16 artifact; retained for provenance and not allowed to override later current-operator governance without explicit supersession review.

## 1. 本阶段任务

本阶段执行以下工作：

1. 废止UHPC“仅单轴主曲线”的层0材料边界；
2. 以Nguyen普通混凝土U、TC、TT、CC、TCX为母架构；
3. 增加UHPC特有的三轴受约束状态C3；
4. 检索并注册UHPC单轴、双轴、三轴和真三轴代表性来源；
5. 只实现来源中明确给出的公式；
6. 建立普通混凝土与UHPC状态的一一对应关系；
7. 判断每一类方程能否进入有限精确解析矩；
8. 不用板级试验荷载拟合任何材料参数。

## 2. 状态族

正式状态族冻结为：

\[
\mathcal S_{\mathrm{UHPC}}
=
\{U,TC,TT,CC,TCX,C3\}.
\]

### U

未开裂、未压碎多轴状态。Wang等2024的Willam-Warnke五参数面可作为三维强度边界；D'Alessandro等的直接双轴试验用于校核拉压象限及纤维取向影响。

### TC

一个主方向开裂受拉，另一个主方向受压。Fehling等证明压缩强度在较小横向拉应变下显著降低，并建议双线性折减；Liu等给出UHPC专用应力软化和应变软化研究，但本阶段尚未取得其完整公式，因此TC不能宣告闭合。

### TT

两个主方向处于开裂受拉或多轴拉伸状态。FHWA给出直接拉伸、开裂强度、后开裂承载和纤维取向锚点；Looney和Volz提供多轴拉伸破坏面数据，但完整系数仍未冻结。

### CC

双压峰后/压碎状态。Wang等2024的W-W面提供破坏包络；Zhang等2023提供主动围压下峰值应力、峰值应变、残余应力及全过程曲线，轴对称三轴条件下已经具备显式闭合。

### TCX

先拉裂、后压碎状态。它必须由TC软化峰值和CC/C3峰后关系共同组成。当前没有一篇已定位来源给出完整TCX闭合，故标为材料级综合模型开放项，不得擅自拼接。

### C3

三个主应力均为压应力的受约束状态。W-W、DP、Ottosen、主动围压曲线和真三轴试验共同约束该状态。轴对称主动围压已有显式关系，任意不等三轴应力状态尚未形成完整一致切线。

## 3. 已恢复的显式公式

### 3.1 Wang等2024 W-W破坏面

应力不变量：

\[
f(\sigma)
=
f(I_1,J_2,J_3)
=
f(\rho,\xi,\theta)=0.
\]

受拉、受压子午线：

\[
\frac{\xi_t}{f_{cu}}
=
a_2\left(\frac{k_t\rho_t}{f_{cu}}\right)^2
+a_1\left(\frac{k_t\rho_t}{f_{cu}}\right)+a_0,
\]

\[
\frac{\xi_c}{f_{cu}}
=
b_2\left(\frac{k_c\rho_c}{f_{cu}}\right)^2
+b_1\left(\frac{k_c\rho_c}{f_{cu}}\right)+b_0.
\]

材料常数：

\[
a_0=b_0=0.1775,\quad
a_1=-1.4554,\quad
a_2=-0.1576,
\]

\[
b_1=-0.7806,\quad
b_2=-0.1763.
\]

纤维增强系数：

\[
k_c=1+0.055\lambda_{sf}+0.118\lambda_{pf},
\]

\[
k_t=1+0.0257\lambda_{sf}.
\]

这些系数是材料三轴/双轴数据回归结果，不是板承载力拟合。

### 3.2 Zhou等2023 DP校核线

\[
\frac{\tau_{\mathrm{oct}}^u}{f'_c}
=
0.00995
+
1.394
\frac{\sigma_{\mathrm{oct}}^u}{f'_c}.
\]

该式适合作为受压子午线独立校核，不足以单独定义全过程本构。

### 3.3 Wang等2024围压峰值关系

\[
\frac{\sigma_{cc}}{f_f}
=
1+4.122\frac{\sigma_{\mathrm{conf}}}{f_f},
\]

\[
\frac{\varepsilon_{cc}}{\varepsilon_f}
=
1+6.320\frac{\sigma_{\mathrm{conf}}}{f_f},
\]

\[
\frac{E_{cc}}{E_f}
=
1+1.232\frac{\sigma_{\mathrm{conf}}}{f_f}.
\]

### 3.4 Zhang等2023主动围压全过程

峰值应力：

\[
\frac{f_{cc}}{f'_{co}}
=
1+(3.1-16V_s)
\left(\frac{f_l}{f'_{co}}\right)^{0.7}.
\]

峰值应变：

\[
\frac{\varepsilon_{cc}}{\varepsilon_{co}}
=
1+(12+100V_s)
\left(\frac{f_l}{f'_{co}}\right)^{1.05}.
\]

残余应力：

\[
\frac{f_{cr}}{f'_{co}}
=
9V_s+4.7\frac{f_l}{f'_{co}}.
\]

上升段采用Popovics式：

\[
\frac{\sigma_c}{f_{cc}}
=
\frac{x r}{r-1+x^r},
\qquad
x=\frac{\varepsilon_c}{\varepsilon_{cc}},
\]

\[
r=
\frac{E_c}{E_c-f_{cc}/\varepsilon_{cc}}.
\]

下降段：

\[
\sigma_c
=
f_{cr}
+
\frac{f_{cc}-f_{cr}}
{1+n(x-1)^2},
\qquad
n=\frac{2}{1+100V_s}.
\]

## 4. 实际实现和测试

源码 `src/uhpc_explicit_equations.py` 已实现：

- W-W纤维增强系数；
- W-W偏平面插值；
- W-W拉压子午线；
- Zhou DP峰值关系；
- Wang围压峰值应力、峰值应变和弹性模量；
- Zhang峰值、残余、Popovics上升段和有理下降段；
- Fehling双线性趋势的参数化形状函数。

测试结果：

```text
D16 explicit-equation tests: PASS (18 checks)
```

Fehling函数只实现论文所给的双线性形状，不冻结其初始折减参数，因为论文明确说明该量受到构件几何和配筋干扰；它不能作为通用UHPC材料常数。

## 5. 解析矩门禁

### 已经可以有限精确积分

- 连续板应变基；
- 有限应变多项式材料项；
- 弹性和多项式切线项；
- 已知固定状态域内的多项式残量。

### 不能直接凝结成有限普通多项式

- W-W偏平面平方根与Lode角；
- Popovics幂函数；
- Zhang有理下降段；
- 指数型纤维桥接；
- 未知移动状态域。

这些公式仍是解析材料公式，但“解析材料公式”不等于其三维空间积分必然具有有限项初等闭式。

当前最主要的障碍是：

\[
\Omega_U,\Omega_{TC},\Omega_{TT},
\Omega_{CC},\Omega_{TCX},\Omega_{C3}
\]

的空间边界会随荷载变化。几何矩已闭合，状态域尚未闭合。

## 6. 来源门禁结论

```text
D16_NSC_BOTTOM_LOGIC                     = PASS
D16_UHPC_LAYER0                          = ABOLISHED
D16_UHPC_FULL_STATE_FAMILY               = ESTABLISHED
D16_WW_FAILURE_SURFACE                   = PASS
D16_DP_INDEPENDENT_CHECK                 = PASS
D16_AXISYMMETRIC_TRIAXIAL_CURVE          = PASS
D16_TC_COMPLETE_FORMULA                  = OPEN
D16_TT_COMPLETE_FORMULA                  = OPEN
D16_TCX_COMPLETE_FORMULA                 = OPEN
D16_TRUE_TRIAXIAL_CONSISTENT_TANGENT     = OPEN
D16_FULL_UHPC_ANALYTICAL_MATRIX          = NOT YET AUTHORIZED
```

## 7. 下一阶段

下一阶段应按以下顺序闭合，不得直接进入UHPC板承载力计算：

1. 获取并逐式恢复Liu 2023 TC软化关系；
2. 从FHWA/AASHTO直接拉伸关系和Looney多轴拉伸数据确定TT包络及桥接关系；
3. 确定TCX的唯一材料级组合规则；
4. 选定W-W主破坏面，并以DP和Ottosen作独立校核；
5. 建立任意三轴应力状态下的C3应力更新和一致切线；
6. 完成六状态材料域扫描与自然转换审计；
7. 再研究状态域的解析积分或低维全局状态闭合。
