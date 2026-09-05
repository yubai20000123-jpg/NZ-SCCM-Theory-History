执行了一轮，而且这次我不再追求把 UHPC 的 CC/TC/TT 所有细节都“完美复刻”。我按你刚才定的标准做的是：

```math
\boxed{\text{能不能得到一个足够准确、能够进入完整 Airy 显式体系的最小 UHPC 模型？}}
```

结果是：**可以，至少材料层已经值得继续。** 而且比我前面设想的“很多复杂 tensor branches”还能再简化一层。

我暂时把它称为：

```math
\boxed{\text{AC-UHPC-Branch V0}}
```

即 **Airy-Compatible UHPC Branch V0**。

---

# 1. 第一件事：先验证“多线弹性”到底需要多少线

这里完全没有拿 BH005/BH100 或有限元承载力做拟合。

只逼近现在已经冻结的 UHPC 材料曲线。

当前压缩曲线是：

```math
\sigma_c = -f_c \left( A_c\xi+B_c\xi^5+C_c\xi^6 \right), \qquad \xi=-\frac{\varepsilon}{\varepsilon_{c0}},
```

当前代表参数：

```math
E_c=43400\ {\rm MPa}, \quad f_c=141.1\ {\rm MPa}, \quad \varepsilon_{c0}=0.0035.
```

这是当前 R14/05 已采用的压缩形式；拉伸则是当前 5 锚点 Hermite 曲线。

计算得到：

```math
A_c=1.07654146,
```

```math
B_c=0.61729270,
```

```math
C_c=-0.69383416.
```

然后直接用等间距折线逼近整个峰前压缩曲线。

| 压缩线段数最大应力误差相对 `f_c`RMS误差 |           |           |           |
| ------------------------ | --------- | --------- | --------- |
| 4                        | 4.604 MPa | 3.26%     | 1.673 MPa |
| 6                        | 2.601 MPa | **1.84%** | 0.802 MPa |
| 8                        | 1.648 MPa | **1.17%** | 0.463 MPa |
| 10                       | 1.132 MPa | 0.80%     | 0.300 MPa |

所以：

```math
\boxed{\text{压缩用 6 条线已经足够作为第一版。}}
```

不是理论规定“永远只能 6 条”，而是这条当前材料曲线用 6 条线已经只有不到 2% 的最大材料误差。

---

# 2. 拉伸比压缩难一点，但仍然不严重

当前拉伸锚点为：

```math
(0,0),
```

```math
(0.00042,9.767718),
```

```math
(0.0038,10.734818),
```

```math
(0.0069,10.347978),
```

```math
(0.00759,0),
```

中间是 cubic Hermite。

如果愚蠢地只拿这 5 个锚点直接连 4 条直线：

```math
\max |\Delta \sigma_t| =2.240\ {\rm MPa}
```

达到峰值拉应力的：

```math
20.9\%.
```

这个显然不够。

但是把每个原 Hermite 区间再等分：

| 总线段数最大误差 / `f_{t,\max}`RMS / `f_{t,\max}` |           |           |
| ----------------------------------------- | --------- | --------- |
| 8                                         | 9.24%     | 2.22%     |
| 12                                        | **5.36%** | **1.05%** |
| 16                                        | **3.38%** | **0.60%** |
| 20                                        | 2.30%     | 0.39%     |

所以第一版甚至没必要特别重：

```math
\boxed{ 6\text{ 条压缩支路} + 12\sim16\text{ 条拉伸支路} }
```

已经把原始 UHPC 一维 source curve 保留到几个百分点以内。

而且这些线段只属于**材料本身**，不属于任何 BH 试件。

---

# 3. 真正关键的突破不在这里，而在二维 Poisson coupling

如果只是分别做：

```math
\sigma_1=f(\varepsilon_1), \qquad \sigma_2=f(\varepsilon_2),
```

还是太粗糙。

但我们以前其实已经有一个很好的东西：M3 的 equivalent-uniaxial plane-stress closure：

```math
\boxed{ e_1^* = \varepsilon_1+ \frac{\nu_c}{E_c}\sigma_2 }
```

```math
\boxed{ e_2^* = \varepsilon_2+ \frac{\nu_c}{E_c}\sigma_1 }
```

然后：

```math
\sigma_1=\sigma_u(e_1^*), \qquad \sigma_2=\sigma_u(e_2^*).
```

这个模型最大的价值不是它以前预测多准，而是：

1. 不需要运行时 CC/TC/TT classifier；
2. 原点自动恢复正确的 `E,\nu`；
3. 单轴应力轴保持严格正确；
4. 已经有一致 plane-stress tangent 和主方向旋转项。

所以这次我没有重新发明二维 Poisson 结构。

直接保留这个骨架。

---

# 4. 然后只加一个东西：TC 交叉弹性支路

这是这次试验最重要的结果。

定义：

```math
\eta=\frac{\nu_c}{E_c}.
```

在等效主应变空间中，基础一维折线段写为：

```math
\sigma_u(e_i^*) = m_i e_i^*+b_i.
```

现在只对拉压共存加入一个交叉能量支路：

```math
\boxed{ W_{TC} = K_{TC} \left[ \langle e_1^*\rangle_+ \langle e_2^*\rangle_- + \langle e_1^*\rangle_- \langle e_2^*\rangle_+ \right] }
```

其中：

```math
\langle x\rangle_+=\max(x,0), \qquad \langle x\rangle_-=\min(x,0).
```

注意：

- CC：这一项自动为 0；
- TT：自动为 0；
- 单轴：自动为 0；
- 只有 TC/CT 才起作用。

它没有修改单轴曲线。

---

# 5. 这个支路的物理效果恰好是我们想要的

例如：

```math
e_1^*>0,\qquad e_2^*<0.
```

则：

```math
W_{TC}=K_{TC}e_1^*e_2^*.
```

于是：

```math
\Delta\sigma_1 = K_{TC}e_2^*<0,
```

即：

```math
\boxed{\text{拉应力降低}}
```

同时：

```math
\Delta\sigma_2 = K_{TC}e_1^*>0,
```

因为 `\sigma_2<0`，这意味着：

```math
\boxed{\text{压应力绝对值降低}}.
```

也就是说，一个正的：

```math
K_{TC}
```

自然同时产生：

```math
\boxed{ \text{tension weakening} + \text{compression softening}. }
```

这正是 UHPC 拉压共存实验里观察到的核心行为：已有专门的二维 UHPC 试验指出，主拉应变会降低正交方向的压缩能力，并建立了 TC softening constitutive law。([科学直通车](https://www.sciencedirect.com/science/article/pii/S0950061823026831?dgcid=rss_sd_all "https://www.sciencedirect.com/science/article/pii/S0950061823026831?dgcid=rss_sd_all"))

---

# 6. 更漂亮的是：在每一个线性材料支路内，它完全可以显式解

这是我觉得这条路线真正有资格继续进入 Airy 的原因。

在当前 TC 支路中：

```math
\begin{bmatrix} \sigma_1\\ \sigma_2 \end{bmatrix} = \underbrace{ \begin{bmatrix} m_1&K_{TC}\\ K_{TC}&m_2 \end{bmatrix} }_{\displaystyle \mathbf C^*} \begin{bmatrix} e_1^*\\ e_2^* \end{bmatrix} + \begin{bmatrix} b_1\\ b_2 \end{bmatrix}.
```

而：

```math
\mathbf e^* = \boldsymbol\varepsilon + \eta \begin{bmatrix} 0&1\\ 1&0 \end{bmatrix} \boldsymbol\sigma.
```

因此：

```math
\boxed{ \left[ \mathbf I - \eta\mathbf C^*\mathbf J \right]\boldsymbol\sigma = \mathbf C^*\boldsymbol\varepsilon+\mathbf b. }
```

直接得到：

```math
\boxed{ \boldsymbol\sigma = \left[ \mathbf I-\eta\mathbf C^*\mathbf J \right]^{-1} \left( \mathbf C^*\boldsymbol\varepsilon+\mathbf b \right). }
```

不是材料 Newton。

不是迭代等效应变。

是一个：

```math
\boxed{\text{2×2 显式逆矩阵。}}
```

---

# 7. 甚至可以把它完全展开

定义：

```math
a=1-\eta K_{TC},
```

```math
d= a^2-\eta^2m_1m_2.
```

以及：

```math
r_1 = m_1\varepsilon_1 + K_{TC}\varepsilon_2+b_1,
```

```math
r_2 = K_{TC}\varepsilon_1 + m_2\varepsilon_2+b_2.
```

那么：

```math
\boxed{ \sigma_1 = \frac{ ar_1+\eta m_1r_2 }{d} }
```

```math
\boxed{ \sigma_2 = \frac{ \eta m_2r_1+ar_2 }{d}. }
```

一致主切线则是：

```math
\boxed{ \mathbf D_n = \frac1d \begin{bmatrix} m_1& aK_{TC}+\eta m_1m_2\\ aK_{TC}+\eta m_1m_2& m_2 \end{bmatrix}. }
```

这非常重要。

因为：

```math
K_{TC}=0
```

以后立即退化成以前 M3 的：

```math
\mathbf D_n = \frac1{ 1-\nu_c^2m_1m_2/E_c^2 } \begin{bmatrix} m_1& \nu_cm_1m_2/E_c\\ \nu_cm_1m_2/E_c& m_2 \end{bmatrix},
```

正好就是旧 M3 的 plane-stress equivalent-uniaxial tangent。

所以这不是另起炉灶。

它是：

```math
\boxed{ \text{M3 Poisson closure} + \text{一个 TC cross-stiffness}. }
```

---

# 8. 然后我没有瞎定 `K_{TC}`，而是拿真实 UHPC 二轴实验做了一个很粗的材料级试配

2024 年刘蕊蕊等在二维 PBET 上做了：

- CC；
- TT；
- sequential TC；
- proportional TC；

并提出完整 biaxial strength envelope。特别重要的是，他们认为 biaxial tensile strength 可保守采用 uniaxial tensile strength，同时对 CC 和 TC 分别建立了新的分段强度包络。([科学直通车](https://www.sciencedirect.com/science/article/pii/S0950061824044076 "https://www.sciencedirect.com/science/article/pii/S0950061824044076"))

其 proportional TC 数据包括：

```math
\text{UP-TC-1}, \quad \text{UP-TC-8}, \quad \text{UP-TC-10}, \quad \text{UP-TC-12}.
```

公开二次资料中转载的原试验表给出了这些点的 `f_c,f_t,\sigma_1,\sigma_2`。([ResearchGate](https://www.researchgate.net/publication/407506719_High_performance_construction_materials_fracture_and_high_cycle_fatigue_assessment_based_on_accelerated_PF-CZM?utm_source=chatgpt.com "(PDF) High performance construction materials fracture and high cycle fatigue assessment based on accelerated PF-CZM"))

我没有拿这些数据建立复杂函数。

只拟合：

```math
\boxed{K_{TC}}
```

一个参数。

---

# 9. 得到的量级非常温和

第一轮最简单拟合得到：

```math
\boxed{ K_{TC}\approx1.5\ {\rm GPa} }
```

取约：

```math
K_{TC}=1540\ {\rm MPa}
```

时：

```math
\frac{K_{TC}}{E_c} \approx3.55\%.
```

也就是说，我们不是在材料里面塞一个巨大经验刚度。

只是加了一个相对于：

```math
E_c=43.4\ {\rm GPa}
```

很小的交叉耦合。

---

# 10. 四个 proportional-TC 点的结果

这一轮为了保持最简单，我采用：

> tensile equivalent strain 达到当前单轴拉伸主曲线峰值，作为 V0 的 TC envelope boundary。

所以这不是完整 path-dependent constitutive model，只是一个**材料强度包络级快速试验**。

结果：

| 试件拉应力试验 MPaV0 MPa压应力绝对值试验 MPaV0 MPa相对误差 |      |       |       |       |        |
| --------------------------------------- | ---- | ----- | ----- | ----- | ------ |
| UP-TC-1                                 | 9.16 | 10.08 | 9.23  | 10.16 | +10.1% |
| UP-TC-8                                 | 9.58 | 8.00  | 77.16 | 64.43 | −16.5% |
| UP-TC-10                                | 7.59 | 7.59  | 76.07 | 76.05 | ≈0%    |
| UP-TC-12                                | 6.34 | 7.16  | 76.27 | 86.19 | +13.0% |

按 8 个应力坐标计算平均绝对相对误差：

```math
\boxed{ {\rm MAPE}\approx9.9\%. }
```

我认为这已经达到你刚才说的：

```math
\boxed{\text{“不用十全十美，但有一定预测精度”}}
```

的门槛。

尤其注意：

```math
\boxed{ \text{这里只有一个新 TC 参数。} }
```

没有：

- TC1；
- TC2；
- BH005-TC；
- BH100-TC；
- 各种 specimen correction。

而且这些 UHPC 试验的 `f_c` 大约 126–128 MPa、`f_t\approx10.7` MPa，与我们当前 141.1 MPa、约 10.7 MPa 的 UHPC 并不是相差一个数量级。([ResearchGate](https://www.researchgate.net/publication/407506719_High_performance_construction_materials_fracture_and_high_cycle_fatigue_assessment_based_on_accelerated_PF-CZM?utm_source=chatgpt.com "(PDF) High performance construction materials fracture and high cycle fatigue assessment based on accelerated PF-CZM"))

---

# 11. CC 我也查了一下，但这次反而建议先别加

同一组二维试验的三个 CC 点：

```math
\text{UP-CC-1}: 117.01/117.06\ {\rm MPa},
```

```math
\text{UP-CC-2}: 152.97/76.43\ {\rm MPa},
```

```math
\text{UP-CC-5}: 139.61/27.87\ {\rm MPa}.
```

相应单轴 `f_c` 分别约：

```math
125.98,\quad127.33,\quad128.99\ {\rm MPa}.
```

([ResearchGate](https://www.researchgate.net/publication/407506719_High_performance_construction_materials_fracture_and_high_cycle_fatigue_assessment_based_on_accelerated_PF-CZM?utm_source=chatgpt.com "(PDF) High performance construction materials fracture and high cycle fatigue assessment based on accelerated PF-CZM"))

如果 V0 **完全不做 CC enhancement**，只拿单轴 `f_c` 当第一主压应力容量，三个点的主压应力误差约：

```math
7.6\%,\qquad16.8\%,\qquad7.6\%.
```

平均约：

```math
\boxed{10.7\%.}
```

这其实并不离谱。

更重要的是，三个 CC 点本身没有表现成一个简单“横向压力越大，增强系数越大”的单一规律。

原论文也因此采用 piecewise biaxial compression envelope，而不是一个常数增强系数。([科学直通车](https://www.sciencedirect.com/science/article/pii/S0950061824044076 "https://www.sciencedirect.com/science/article/pii/S0950061824044076"))

所以按照你刚才“别追求十全十美”的要求，我反而建议：

```math
\boxed{K_{CC}=0\quad\text{先进入结构级计算。}}
```

不要为了把三个材料点都拟合漂亮，又增加一个复杂 CC 模型。

---

# 12. TT 更可以先不加 interaction

原论文自己的工程结论就是：

```math
\boxed{ f_{tt}\approx f_t }
```

作为 biaxial tension strength 的保守处理。([科学直通车](https://www.sciencedirect.com/science/article/pii/S0950061824044076 "https://www.sciencedirect.com/science/article/pii/S0950061824044076"))

因此 V0：

```math
\boxed{K_{TT}=0}
```

完全说得过去。

UHPC 板轴压极限问题里，TT 也不是我现在最担心的主要区域。

---

# 13. 三轴围压也先不塞进来

王淑楠的三轴试验明确证明强围压可以大幅改变 UHPC 峰值应力和峰值应变，而且建立了 Willam–Warnke 多轴破坏准则。

周俊的试验也给出了八面体峰值应力关系。

这些资料非常有价值。

但目前我们正在建立的是：

```math
\boxed{\text{plate plane-stress Airy operator}}
```

而不是三维 confinement constitutive model。

因此第一版不把它们硬塞进去。

把 W-W / DP 留作：

```math
\boxed{\text{强度域校核}}
```

比强行变成 current stress law 更干净。

---

# 14. 所以第一版 UHPC 实际上可以非常简单

我现在建议正式试算的 V0 只有三层。

### A. 单轴 material spectrum

```math
\boxed{ \sigma_u(e) = \text{piecewise-linear approximation of source curve}. }
```

第一轮：

```math
N_c=6, \qquad N_t=12\sim16.
```

这已经给：

```math
\text{compression error}\lesssim2\%,
```

```math
\text{tension error}\approx3\sim5\%.
```

---

### B. 原点/Poisson coupling

```math
\boxed{ e_1^* = \varepsilon_1+\frac{\nu_c}{E_c}\sigma_2 }
```

```math
\boxed{ e_2^* = \varepsilon_2+\frac{\nu_c}{E_c}\sigma_1. }
```

---

### C. 一个 TC interaction

```math
\boxed{ K_{TC}\approx1.5\ {\rm GPa}. }
```

并令：

```math
\boxed{ K_{CC}=0,\qquad K_{TT}=0 }
```

作为第一版。

这就是全部。

---

# 15. 我甚至认为这比“完整 CC/TC/TT tensor branch spectrum”更合理

因为我们已经知道一个危险：

理论开发很容易变成：

> 发现一种状态 → 加一个机制 → 又发现一种状态 → 再加一个机制。

最后表面统一，内部已经二三十个参数。

现在这个 V0 的新增材料信息只有：

```math
\boxed{K_{TC}}
```

一个。

其余全部来自：

```math
E_c,\nu_c,f_c,\varepsilon_{c0},
```

以及现有拉伸锚点。

这些本来就是材料参数。

所以从可识别性上，它非常干净。

---

# 16. 更关键：它特别适合你现在设想的 Airy 显式计算

一维 PWL 本构可以统一写成 hinge expansion：

```math
\boxed{ \sigma_u(e) = m_0e+b_0 + \sum_j \Delta m_j \langle e-e_j\rangle_+. }
```

TC 项同样由：

```math
\langle e_1^*\rangle_\pm \langle e_2^*\rangle_\mp
```

组成。

所以当：

```math
e_i^*(x,y,z)
```

是 Airy/Navier 有限三角场时，整个 UHPC 应力场成为：

```math
\boxed{ \text{linear Fourier field} + \text{positive-part Fourier fields} + \text{their convolution}. }
```

这正是前两轮 toy test 已经验证过的结构：

```math
\boxed{ \text{无需显式构造 } \Omega_{CC},\Omega_{TC},\Omega_{TT}. }
```

空间状态仍然物理存在，但 solver 只处理它们的：

```math
\boxed{\text{modal projection}.}
```

---

# 17. 而且现在 branch 内部连 material Newton 都没了

这是一个很实际的优势。

旧 M3 本身需要针对：

```math
\sigma_1,\sigma_2
```

做 damped Newton，因为 `\sigma_u(e)` 是连续非线性函数。

换成当前多线弹性谱以后，在任意一组材料线段里：

```math
\boxed{ \sigma_1,\sigma_2 }
```

直接是刚才那个 2×2 解析解。

也就是说：

```math
\boxed{ \text{非线性从“连续非线性求解” 变成“若干显式线弹性基的组合”。} }
```

这和你最初那个脑洞其实高度一致。

---

# 18. 钢壳与 UHPC 到这里真的开始出现统一结构了

钢壳：

```math
\boxed{ w_s= \sum_r A_r\phi_r(x,y) }
```

复杂性通过：

```math
\text{spatial modes}
```

展开。

UHPC：

```math
\boxed{ \sigma_u= \sum_k\mathcal B_k(e) }
```

复杂性通过：

```math
\text{material branches}
```

展开。

于是整个理论变成：

```math
\boxed{ \text{空间模态谱} \times \text{材料弹性谱}. }
```

两个部分的“基本单元”其实都非常简单：

- steel：单个简单正弦波 + 理想弹塑性；
- UHPC：单个线弹性材料支路 + Airy 谐波。

复杂性来自**叠加**，而不是每个单元本身都是一个黑箱非线性模型。

---

# 19. 这次试验之后，我认为没必要继续磨 UHPC 了

目前材料层已经达到：

- 压缩 source curve：约 **2%**；
- 拉伸 source curve：约 **3–5%**；
- 只用一个 `K_{TC}` 对 proportional TC 二轴强度：约 **10% 平均误差**；
- 不做 CC interaction：现有三个 CC 强度点约 **11% 平均量级误差**；
- TT 采用单轴拉强度：有文献明确支持作为保守简化。([科学直通车](https://www.sciencedirect.com/science/article/pii/S0950061824044076 "https://www.sciencedirect.com/science/article/pii/S0950061824044076"))

对于我们现在整个结构理论本身还在解决 global compatibility 的阶段，我认为继续为了把材料误差从 10% 压到 3% 而增加五六个 interaction parameters，收益很低。

特别是你已经明确说了：

```math
\boxed{\text{以显式性和合理预测能力优先，不追求材料模型十全十美。}}
```

那么这个 V0 已经足够进入下一关。

---

# 20. 下一关现在应该非常明确

不再继续研究材料。

直接把：

```math
\boxed{\text{AC-UHPC-Branch V0}}
```

接入**真正完整 Airy compatibility**：

```math
F(x,y) \rightarrow N_x,N_y,N_{xy},
```

```math
w(x,y) \rightarrow \kappa_x,\kappa_y,\kappa_{xy},
```

然后：

```math
\boxed{ \mathcal C[ \varepsilon(F,w) ] = \mathcal G(w,w_0) }
```

而不是：

```math
F \rightarrow 4\text{ 个 N/M demand} \rightarrow R_4^{-1}.
```

当前审计已经证明后一条 R4 链没有 global compatibility。

新的 UHPC branch operator 则负责：

```math
\boxed{ \text{Airy stress modes} \leftrightarrow \text{compatible strain modes}. }
```

---

## 所以这一轮我的结论是

我认为这个“超级脑洞”现在已经超过纯概念阶段了。

目前最小可用模型可以锁成：

```math
\boxed{ \begin{aligned} &\text{UHPC uniaxial PWL spectrum} \\ &+ \text{M3 equivalent-uniaxial Poisson closure} \\ &+ K_{TC}\approx1.5\ {\rm GPa} \\ &+ K_{CC}=0 \\ &+ K_{TT}=0. \end{aligned} }
```

它的最大优点不是材料点预测天下第一，而是同时具备：

```math
\boxed{\text{材料来源可解释}}
```

```math
\boxed{\text{没有 specimen-specific 参数}}
```

```math
\boxed{\text{不需要二维 CC/TC/TT 空间分区}}
```

```math
\boxed{\text{branch 内 2×2 显式解}}
```

```math
\boxed{\text{一致切线可显式写出}}
```

以及最重要的：

```math
\boxed{\text{能够自然进入 Airy/Fourier 模态计算。}}
```

我认为现在应该停止继续美化材料，下一步直接推 **“完整 Airy + AC-UHPC-Branch V0 + Multiwave steel” 的兼容方程和面外平衡母式**。那一步才真正决定这个新体系能不能取代 R4。