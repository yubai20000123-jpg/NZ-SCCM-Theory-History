# El-Metwally–Chen 外部既有非线性平衡路径法：材料非线性 + 几何非线性 + 指定挠度全过程恢复

## 0. 文献身份与恢复边界

本文件仅恢复既有文献体系，不包含 UCFT single-q、C1、A±、M4/M5/M6 等任何当前项目自建公式。

主文献：
1. S. E. El-Metwally, W. F. Chen, “Load-Deformation Relations for Reinforced Concrete Sections,” ACI Structural Journal, 86(2), 1989, 163–167.
2. S. E. El-Metwally, A. M. El-Shahhat, W. F. Chen, “3-D nonlinear analysis of R/C slender columns,” Computers & Structures, 37(5), 1990, 863–872.
3. S. E. El-Metwally, F. Ashour, W. F. Chen, “Instability Analysis of Eccentrically Loaded Concrete Walls,” Journal of Structural Engineering, 116(10), 1990, 2862–2880.
4. N. M. Newmark, “Numerical Procedure for Computing Deflections, Moments, and Buckling Loads,” Transactions ASCE, 108, 1943.
5. W. F. Chen, E. M. Lui, Stability Design of Steel Frames, 1991, Chapter 1，给出了与 El-Metwally–Chen 同源的截面 M-φ-P 增量切线算法与 Newmark 构件算法。
6. 后续 WASTABT / finite-difference 实现用于恢复 1990 原法的公开细节；凡非 1990 原文逐字方程，均应标为“同源/等价恢复”。

## 1. 材料层

原方法本身并不锁定唯一混凝土 σ–ε 公式，而是要求给定：
σc = fc(εc), Et,c = dσc/dεc
σs = fs(εs), Et,s = dσs/dεs

混凝土拉压可以采用不同本构。

## 2. 截面平截面关系

单轴弯曲：
ε(y)=ε0+φ y

RC 截面内力：
N(ε0,φ)=∫Ac σc[ε0+φy] dA + Σ As σs[ε0+φys]

M(ε0,φ)=∫Ac y σc[ε0+φy] dA + Σ ys As σs[ε0+φys]

固定 N=N*、给定 φ 时，通过轴力平衡求 ε0：
RN=N(ε0,φ)-N*=0

Newton：
ε0^(r+1)=ε0^(r)-
[N(ε0^(r),φ)-N*]/
[∫Ac Et,c dA+ΣEt,s As]

收敛后：
M(φ;N*)=M[ε0(φ,N*),φ]

扫 φ 即得完整 M–φ–N 曲线。

## 3. 截面增量切线矩阵

单轴：
[dN;dM]
=
[K00 K0φ; Kφ0 Kφφ]
[dε0;dφ]

K00=∫Et dA
K0φ=Kφ0=∫Et y dA
Kφφ=∫Et y² dA

固定 N：
dN=0
=> dε0=-(K0φ/K00)dφ

所以固定轴力下的凝聚弯曲切线：
dM/dφ|N = Kφφ-Kφ0 K00^(-1)K0φ

三维/双轴：
D=[ε0,φx,φy]^T
取 b=[1,y,x]^T，使 ε=b^T D。

F=[N,Mx,My]^T
=∫A b σ(b^TD)dA

Q=∂F/∂D
=∫A Et b b^T dA

离散纤维：
Q =
Σ Et,i Ai
[[1, yi, xi],
 [yi, yi², xiyi],
 [xi, xiyi, xi²]]

RC 时 concrete fibers 与 steel bars 的贡献直接相加。

截面 Newton：
Q^(r) ΔD^(r)=F_target-F_int(D^(r))
D^(r+1)=D^(r)+ΔD^(r)

## 4. Newmark 构件层

将构件长度 L 分成 n 段，站点 xk，步长 h=L/n。

给定轴压 P，假定站点附加挠度 vk。

无初弯曲时：
Mk=M1,k+P vk

有初弯曲 v0,k 时：
Mk=M1,k+P(v0,k+vk)

M1,k 是一阶荷载、端弯矩和横向荷载形成的 primary moment。

通过截面 M–φ–P 关系反求：
φk=Φ(P,Mk)

假定相邻站点曲率线性，则：
θ_(k+1)=θ_k+h/2(φ_k+φ_(k+1))

v_(k+1)=v_k+hθ_k+h²/6(2φ_k+φ_(k+1))

等价共轭梁节点荷载：
R_k^(left)=h/6(2φ_k+φ_(k+1))
R_(k+1)^(right)=h/6(φ_k+2φ_(k+1))

由边界条件确定初始转角/共轭梁反力，从而得到新挠度场。
将新挠度与假定挠度比较并重复，直到收敛。

## 5. El-Metwally 的关键改造：指定挠度而不是指定荷载

选择控制站 c，给定：
vc = vbar

要求反求与该挠度平衡的 P。

把文献算法写成完全等价的离散残量形式：

φi=(v_(i-1)-2vi+v_(i+1))/h²

Mi^eq=M1,i(P)+P(v0,i+vi)

截面提供：
Mi^sec=Msec(P,φi)

平衡：
Ri=Msec(P,φi)-M1,i(P)-P(v0,i+vi)=0

i=1,...,n-1。

再加控制方程：
Rc=vc-vbar=0

未知量：
[v1,...,v_(n-1),P]^T

因此是 n 个未知量、n 个方程。

## 6. 指定挠度 Newton 的显式 Jacobian

定义截面在当前状态的两个灵敏度：
Ki=(∂Msec/∂φ)|P
Ci=(∂Msec/∂P)|φ

则：

∂Ri/∂v_(i-1)=Ki/h²

∂Ri/∂vi=-2Ki/h²-P

∂Ri/∂v_(i+1)=Ki/h²

∂Ri/∂P=
Ci-dM1,i/dP-(v0,i+vi)

控制行：
∂Rc/∂vc=1

Newton：
J^(r) Δu^(r)=-R^(r)

u^(r+1)=u^(r)+Δu^(r)

其中 u=[v1,...,v_(n-1),P]^T。

若 M1,i=P ei：
dM1,i/dP=ei

故：
∂Ri/∂P=Ci-ei-v0,i-vi

## 7. 完整全过程路径

选单调控制挠度序列：
vbar_0 < vbar_1 < ... < vbar_j < ...

对每个 vbar_j：
1. 用上一点的 P 和挠度场作初值；
2. 进行截面材料迭代；
3. 组装二阶 P-Δ 平衡；
4. 解指定挠度非线性方程；
5. 得到 P_j。

于是获得：
(vbar_j,P_j)

上升段：
dP/dvbar>0

极值点：
dP/dvbar=0

下降段：
dP/dvbar<0

因为控制参数是 vbar 而不是 P，所以 dP/dvbar=0 并不阻止路径继续。

## 8. 极值点的严格灵敏度解释

把全部平衡方程记为：
F(u,vbar)=0

对 vbar 求导：
Fu du/dvbar + F_vbar =0

所以：
du/dvbar=-Fu^(-1)F_vbar

u 中的最后一项是 P，因此其最后一个分量就是：
dP/dvbar

极限点：
dP/dvbar=0

继续增大 vbar 后若该导数为负，即自然进入下降支。

这只是对 El-Metwally“specified deflection”算法的现代等价数学解释，不宣称是 1990 论文原符号。

## 9. 墙板 equivalent-column / Newmark 版本

1990 wall paper 将 wall strip 视作 beam-column、plane-strain strip，并以 Newmark + equivalent-column 求解。

后续直接基于该方法的 OW wall 实现可写成：

取半高，分 n 段，指定中点挠度 Ym。

初猜：
Yi=Ym sin(π i/(2n))

每站弯矩：
Mi=Mprimary,i+N Yi

由固定 N 下的 M–φ 曲线求：
φi=Φ(N,Mi)

数值双积分曲率得到新 Yi。

若几何步长 Δx 未知，则根据计算得到的无量纲/单位步长中点挠度系数 αm 调整：
Δx_new=sqrt(Ym/αm)

于是：
H=2n Δx_new

对同一个 N，逐步增大 Ym，得到 H(Ym;N)。
其峰值给定该 N 下的最大稳定高度。

反过来，对于固定实际墙高 H0，在每一个指定 Ym 下求：
H(Ym;N)-H0=0

即可获得：
N=N(Ym)

这就是墙的完整 N–Ym 上升—峰值—下降路径的等价恢复方式。

## 10. 方法的物理来源

材料非线性进入 M–φ–N 截面关系。
几何非线性进入 P(v0+v) 二阶矩。
二者在站点平衡中直接耦合。

全过程下降段不需要人为负刚度：
随着 v 增大，PΔ 二阶矩迅速增大，而材料截面可提供的增量抗弯能力逐步降低；达到极值后，为维持更大的指定挠度平衡，所需/可平衡的轴力 P 反而下降。

因此：
材料非线性 + P-Δ 几何非线性 + 位移控制
即可自然产生完整上升—峰值—下降路径。
