# NZ-SCCM 多波钢壳01——不考虑剪切滑移版本：完整理论推导 R01

**Date:** 2026-09-03  
**Branch:** `diagnostic/bh032-bh050-mode-projection-20260827`  
**Status:** `THEORY DERIVATION / NO SHEAR SLIP / ONE COMPLETE GLOBAL HALFWAVE / FOUR CELL CLASSES / R14-COMPATIBLE N-M ASSEMBLY / PRODUCTION NOT MODIFIED`

---

## 0. Governing assumptions

本版本只处理钢壳与 UHPC 完全不滑移、完全组合，并且只计算一个完整的整板整体屈曲半波。钢壳横向由加劲肋划分为若干等宽格室。每一个会发生局部屈曲的格室，纵向鼓波数量只允许取

\[
n_0-1,\quad n_0,\quad n_0+1,
\]

其中

\[
\boxed{n_0=\left\lfloor\frac{L_G}{s}\right\rfloor}
\]

\(L_G\) 为一个完整整体半波长度，\(s\) 为该侧相邻加劲肋间距。不发生局部屈曲的格室直接按完整钢板理想弹塑性计入。

本版本不引入：界面滑移、界面剪切弹簧、钢壳—UHPC 力流重新分配、99 个独立局部幅值、连续局部最优波长搜索、参与率、随机场或有效宽度。

现有 R14 的四广义截面变量、UHPC 连续厚度积分、理想弹塑性钢材以及 \(R_4\) 平衡框架保持。

---

## 1. Coordinates and geometry

取矩形组合板：

\[
0\le x\le b,
\]

其中 \(x\) 为横向；

\[
0\le y\le a,
\]

其中 \(y\) 为轴压方向。

组合截面的厚度方向为 \(z\)，取 UHPC 中面为

\[
z=0.
\]

规定 \(z>0\) 指向上钢壳。

UHPC 厚度：\(t_c\)。上下钢壳厚度均为：\(t_s\)。

上钢壳中面位置

\[
\boxed{z_+=+z_f}
\]

下钢壳中面位置

\[
\boxed{z_-=-z_f}
\]

其中

\[
\boxed{z_f=\frac{t_c+t_s}{2}}.
\]

统一采用拉应变、拉应力为正，所以轴压时通常 \(\varepsilon_y<0,\sigma_y<0\)。截面结果量单位为 \([N_x]=[N_y]=\mathrm{N/mm}\)，\([M_x]=[M_y]=\mathrm N\)。

---

## 2. Full composite / no-slip kinematics

钢壳与 UHPC 完全不滑移意味着不存在单独的 \(u_s(y),u_c(y)\) 以及 \(u_s-u_c\)，也不存在 \(k_P,C_{PBL},\tau_{interface}\) 等界面传力未知量。

整个组合截面只有同一组广义膜应变和曲率

\[
\boxed{\varepsilon_x^0,\quad\kappa_x,\quad\varepsilon_y^0,\quad\kappa_y}.
\]

任意厚度位置 \(z\) 的组合截面宏观应变

\[
\boxed{\varepsilon_x^{g}(z)=\varepsilon_x^0+\kappa_x z}
\tag{1}
\]

\[
\boxed{\varepsilon_y^{g}(z)=\varepsilon_y^0+\kappa_y z}.
\tag{2}
\]

上钢壳中面的宏观应变

\[
\boxed{e_x^+=\varepsilon_x^0+\kappa_x z_f}
\tag{3}
\]

\[
\boxed{e_y^+=\varepsilon_y^0+\kappa_y z_f}
\tag{4}
\]

下钢壳中面的宏观应变

\[
\boxed{e_x^-=\varepsilon_x^0-\kappa_x z_f}
\tag{5}
\]

\[
\boxed{e_y^-=\varepsilon_y^0-\kappa_y z_f}.
\tag{6}
\]

局部钢板屈曲只是在该共同宏观应变之上改变钢板自身局部膜内响应，不产生钢壳—UHPC 滑移。

---

## 3. Initial full-composite A/D stiffness

钢材参数 \(E_s,\nu_s,f_y\)，UHPC 初始弹性参数 \(E_c,\nu_c\)。

\[
\boxed{K_s=\frac{E_s}{1-\nu_s^2}}
\tag{7}
\]

\[
\boxed{K_c=\frac{E_c}{1-\nu_c^2}}
\tag{8}
\]

\[
\boxed{G_s=\frac{E_s}{2(1+\nu_s)}}
\tag{9}
\]

\[
\boxed{G_c=\frac{E_c}{2(1+\nu_c)}}.
\tag{10}
\]

若保留当前 R14 中纵向 PBL/web 钢面积 \(A_w\)，定义其在 UHPC core 中占据的面积比例

\[
\boxed{\rho_w=\frac{A_w}{bt_c}}.
\tag{11}
\]

横向膜刚度

\[
\boxed{A_{11}=2t_sK_s+(1-\rho_w)t_cK_c}
\tag{12}
\]

轴向膜刚度

\[
\boxed{A_{22}=2t_sK_s+(1-\rho_w)t_cK_c+\rho_wt_cE_s}
\tag{13}
\]

泊松耦合

\[
\boxed{A_{12}=2t_s\nu_sK_s+(1-\rho_w)t_c\nu_cK_c.}
\tag{14}
\]

上下钢壳关于组合截面中面的弯曲刚度

\[
\boxed{D_f=2K_s\left(\frac{t_s^3}{12}+t_sz_f^2\right)}
\tag{15}
\]

UHPC

\[
\boxed{D_c=(1-\rho_w)K_c\frac{t_c^3}{12}}
\tag{16}
\]

纵向 web

\[
\boxed{D_w=\rho_wE_s\frac{t_c^3}{12}}
\tag{17}
\]

\[
\boxed{D_x=D_f+D_c}
\tag{18}
\]

\[
\boxed{D_y=D_f+D_c+D_w}
\tag{19}
\]

\[
\boxed{D_\mu=\nu_sD_f+\nu_cD_c}
\tag{20}
\]

\[
\boxed{D_{66}=2G_s\left(\frac{t_s^3}{12}+t_sz_f^2\right)+(1-\rho_w)G_c\frac{t_c^3}{12}}
\tag{21}
\]

\[
\boxed{H=D_\mu+2D_{66}}.
\tag{22}
\]

---

## 4. Global longitudinal halfwave selection

横向固定一个半波

\[
\alpha=\frac{\pi}{b}.
\]

整个构件长度为 \(a\)。假设整体纵向有 \(m\) 个半波

\[
\beta_m=\frac{m\pi}{a}.
\]

临界膜力

\[
\boxed{N_{cr,m}=\frac{D_x\alpha^4+2H\alpha^2\beta_m^2+D_y\beta_m^4}{\beta_m^2}.}
\tag{23}
\]

总临界荷载

\[
\boxed{P_{cr,m}=bN_{cr,m}.}
\tag{24}
\]

连续极小点

\[
\boxed{m_c=\frac{a}{b}\left(\frac{D_x}{D_y}\right)^{1/4}.}
\tag{25}
\]

取两侧相邻正整数比较

\[
\boxed{m^*=\arg\min_{m\in\mathbb N^+}P_{cr,m}.}
\tag{26}
\]

一个完整整体半波长度

\[
\boxed{L_G=\frac{a}{m^*}.}
\tag{27}
\]

正式计算域

\[
\boxed{0\le x\le b,\qquad 0\le y\le L_G.}
\tag{28}
\]

整体面外形函数

\[
\boxed{\psi(x,y)=\sin\frac{\pi x}{b}\sin\frac{\pi y}{L_G}.}
\tag{29}
\]

---

## 5. Transverse cells and four classes

对上、下钢面分别用 \(f=+,-\)。同侧加劲肋间距记为 \(s_f\)。若全部标准格室等宽且覆盖整个宽度

\[
\boxed{J_f=\frac{b}{s_f}.}
\tag{30}
\]

第 \(j\) 个横向格室

\[
\boxed{(j-1)s_f\le x\le js_f.}
\tag{31}
\]

每个横向格室贯穿整个代表整体半波 \(0\le y\le L_G\)。参考局部鼓波数量

\[
\boxed{n_{0,f}=\left\lfloor\frac{L_G}{s_f}\right\rfloor.}
\tag{32}
\]

三个局部屈曲候选

\[
\boxed{n_{-,f}=n_{0,f}-1}
\tag{33}
\]

\[
\boxed{n_{0,f}=n_{0,f}}
\tag{34}
\]

\[
\boxed{n_{+,f}=n_{0,f}+1.}
\tag{35}
\]

若 \(n_{0,f}=1\)，则删除 \(n_-\) 候选。

每个格室只属于四类之一：未局部屈曲 \(E\)，或局部屈曲 \(L_-\)、\(L_0\)、\(L_+\)。

---

## 6. One cell spanning one complete global halfwave

对于屈曲格室，采用

\[
\boxed{\phi_{fjn}(x,y)=\left[1-\cos\frac{2\pi[x-(j-1)s_f]}{s_f}\right]\left[1-\cos\frac{2\pi n y}{L_G}\right].}
\tag{36}
\]

横向波数

\[
\boxed{k_x=\frac{2\pi}{s_f}.}
\tag{37}
\]

纵向波数

\[
\boxed{k_y(n)=\frac{2\pi n}{L_G}.}
\tag{38}
\]

真实局部纵向波长

\[
\boxed{L_y(n)=\frac{L_G}{n}.}
\tag{39}
\]

在 \(y_k=kL_G/n\) 以及横向格室两边界均有 \(\phi=0\) 和相应法向一阶导数为 0，因此一个横向格室 + 一个局部幅值 + 一个整数 \(n\) 可以表示该格室在一个完整整体半波内的 \(n\) 个局部鼓波。

第 \(j\) 个格室状态变量

\[
\boxed{c_{fj}\in\{E,L_-,L_0,L_+\}.}
\tag{40}
\]

---

## 7. Nonbuckled E-cell: full-thickness ideal elastoplastic steel

上钢面弹性试算

\[
\boxed{\sigma_{x,E}^{tr,+}=\frac{E_s}{1-\nu_s^2}(e_x^++\nu_se_y^+)}
\tag{41}
\]

\[
\boxed{\sigma_{y,E}^{tr,+}=\frac{E_s}{1-\nu_s^2}(e_y^++\nu_se_x^+)}
\tag{42}
\]

下钢面

\[
\boxed{\sigma_{x,E}^{tr,-}=\frac{E_s}{1-\nu_s^2}(e_x^-+\nu_se_y^-)}
\tag{43}
\]

\[
\boxed{\sigma_{y,E}^{tr,-}=\frac{E_s}{1-\nu_s^2}(e_y^-+\nu_se_x^-).}
\tag{44}
\]

无均匀面内剪切。平面应力 von Mises

\[
\boxed{\sigma_{VM,E}^{tr,f}=\sqrt{(\sigma_{x,E}^{tr,f})^2-\sigma_{x,E}^{tr,f}\sigma_{y,E}^{tr,f}+(\sigma_{y,E}^{tr,f})^2}.}
\tag{45}
\]

理想弹塑性径向截断

\[
\boxed{\lambda_E^f=\min\left(1,\frac{f_y}{\sigma_{VM,E}^{tr,f}}\right).}
\tag{46}
\]

最终

\[
\boxed{\sigma_{x,E}^f=\lambda_E^f\sigma_{x,E}^{tr,f}}
\tag{47}
\]

\[
\boxed{\sigma_{y,E}^f=\lambda_E^f\sigma_{y,E}^{tr,f}.}
\tag{48}
\]

完整物理宽度和厚度均保留。

---

## 8. Buckled L-/L0/L+ cells

对 \(r=-1,0,+1\)

\[
n_r=n_{0,f}+r.
\]

纵向局部波长

\[
\boxed{L_{y,r}=\frac{L_G}{n_r}.}
\tag{49}
\]

横向宽度

\[
\boxed{L_x=s_f.}
\tag{50}
\]

局部长宽比

\[
\boxed{r_{c,r}=\frac{L_{y,r}}{L_x}=\frac{L_G}{n_rs_f}.}
\tag{51}
\]

局部弹性屈曲系数

\[
\boxed{k_{cr,r}=\frac{4(3r_{c,r}^4+2r_{c,r}^2+3)}{3r_{c,r}^2}.}
\tag{52}
\]

局部弹性屈曲应力

\[
\boxed{\sigma_{cr,r}^{E}=\frac{\pi^2E_st_s^2}{12(1-\nu_s^2)s_f^2}k_{cr,r}.}
\tag{53}
\]

若 \(\sigma_{cr,r}^{E}\ge f_y\)，则局部屈曲不先于材料屈服，该格室归入 E；若 \(\sigma_{cr,r}^{E}<f_y\)，则允许进入 R02/R06 局部路径。

---

## 9. Local imperfection and von Karman mean strains

局部初始缺陷幅值 \(A_{0\ell}\)，当前局部幅值 \(U_{fj}\)。

\[
\boxed{w_{0,fj}^{L}=A_{0\ell}\phi_{fjn}(x,y)}
\tag{56}
\]

\[
\boxed{w_{fj}^{L}=U_{fj}\phi_{fjn}(x,y).}
\tag{57}
\]

定义

\[
\boxed{d_{fj}=U_{fj}^2-A_{0\ell}^2.}
\tag{58}
\]

精确周期平均

\[
\boxed{\frac12\langle\phi_{,x}^2\rangle=\frac{3k_x^2}{8}}
\tag{59}
\]

\[
\boxed{c_x=\frac{3k_x^2}{8}=\frac38\left(\frac{2\pi}{s_f}\right)^2}
\tag{60}
\]

\[
\boxed{c_y(n)=\frac{3k_y(n)^2}{8}=\frac38\left(\frac{2\pi n}{L_G}\right)^2.}
\tag{61}
\]

平均剪切几何项为零。

上钢面

\[
\boxed{m_{x,r}^{+}=\varepsilon_x^0+\kappa_xz_f+c_x(U_{+,r}^2-A_{0\ell}^2)}
\tag{62}
\]

\[
\boxed{m_{y,r}^{+}=\varepsilon_y^0+\kappa_yz_f+c_y(n_r)(U_{+,r}^2-A_{0\ell}^2)}
\tag{63}
\]

下钢面

\[
\boxed{m_{x,r}^{-}=\varepsilon_x^0-\kappa_xz_f+c_x(U_{-,r}^2-A_{0\ell}^2)}
\tag{64}
\]

\[
\boxed{m_{y,r}^{-}=\varepsilon_y^0-\kappa_yz_f+c_y(n_r)(U_{-,r}^2-A_{0\ell}^2).}
\tag{65}
\]

---

## 10. R02 local amplitude closure

钢板局部弯曲刚度

\[
\boxed{D_s=\frac{E_st_s^3}{12(1-\nu_s^2)}}
\tag{66}
\]

局部弯曲能量系数

\[
\boxed{K_b(n_r)=D_s\left[\frac34(k_x^4+k_y^4)+\frac12k_x^2k_y^2\right].}
\tag{67}
\]

\[
\boxed{Q_s=\frac{E_s}{1-\nu_s^2}.}
\tag{68}
\]

定义

\[
\boxed{r_k=\frac{k_x}{k_y}.}
\tag{69}
\]

R02 Airy 薄膜系数

\[
\boxed{K_A=k_y^4\frac{P_{16}(r_k)}{256(r_k^2+1)^2(r_k^2+4)^2(4r_k^2+1)^2}}
\tag{70}
\]

其中

\[
\begin{aligned}
P_{16}(r_k)={}&272r_k^{16}+2856r_k^{14}+11273r_k^{12}+23146r_k^{10}\\
&+31506r_k^8+23146r_k^6+11273r_k^4+2856r_k^2+272.
\end{aligned}
\tag{71}
\]

定义

\[
\boxed{B_3^{(r)}=4t_sE_sK_A^{(r)}+2t_sQ_s[c_x^2+2\nu_sc_xc_y^{(r)}+(c_y^{(r)})^2]}
\tag{72}
\]

\[
\boxed{\begin{aligned}B_1^{(f,r)}={}&K_b^{(r)}-A_{0\ell}^2B_3^{(r)}\\&+2t_sQ_s[c_xe_x^f+\nu_sc_xe_y^f+\nu_sc_y^{(r)}e_x^f+c_y^{(r)}e_y^f]
\end{aligned}}
\tag{73}
\]

\[
\boxed{B_0^{(r)}=-A_{0\ell}K_b^{(r)}.}
\tag{74}
\]

局部幅值满足

\[
\boxed{B_3^{(r)}U^3+B_1^{(f,r)}U+B_0^{(r)}=0.}
\tag{75}
\]

对应局部势能

\[
\boxed{\Pi^{(f,r)}(U)=\frac{B_3^{(r)}}4U^4+\frac{B_1^{(f,r)}}2U^2+B_0^{(r)}U.}
\tag{76}
\]

最终取全部非负实根和 \(U=0\) 中能量最低者

\[
\boxed{U_{f,r}^*=\arg\min_{U\ge0}\Pi^{(f,r)}(U).}
\tag{77}
\]

代回平均膜应变

\[
\boxed{m_{x,r}^{f}=e_x^f+c_x[(U_{f,r}^*)^2-A_{0\ell}^2]}
\tag{78}
\]

\[
\boxed{m_{y,r}^{f}=e_y^f+c_y^{(r)}[(U_{f,r}^*)^2-A_{0\ell}^2].}
\tag{79}
\]

弹性平均应力

\[
\boxed{\bar\sigma_{x,r}^{R02,f}=Q_s(m_{x,r}^f+\nu_sm_{y,r}^f)}
\tag{80}
\]

\[
\boxed{\bar\sigma_{y,r}^{R02,f}=Q_s(m_{y,r}^f+\nu_sm_{x,r}^f).}
\tag{81}
\]

---

## 11. R06 local first-yield check

有限 LL harmonic 集合

\[
\mathcal H=\{(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1)\}
\]

系数

\[
h_{01}=1/2,\ h_{02}=-1/2,\ h_{10}=1/2,\ h_{11}=-1,\ h_{12}=1/2,\ h_{20}=-1/2,\ h_{21}=1/2.
\]

\[
\boxed{\Lambda_{pq}=[(pk_x)^2+(qk_y)^2]^2}
\tag{82}
\]

\[
\boxed{F_{pq}=h_{pq}\frac{k_x^2k_y^2}{\Lambda_{pq}}.}
\tag{83}
\]

令 \(\theta_x=k_x\xi,\theta_y=k_yy\)，则局部 Airy 波动应力

\[
\boxed{\widetilde\sigma_x(\xi,y)=-E_sd\sum_{(p,q)\in\mathcal H}(qk_y)^2F_{pq}\cos(p\theta_x)\cos(q\theta_y)}
\tag{84}
\]

\[
\boxed{\widetilde\sigma_y(\xi,y)=-E_sd\sum_{(p,q)\in\mathcal H}(pk_x)^2F_{pq}\cos(p\theta_x)\cos(q\theta_y)}
\tag{85}
\]

\[
\boxed{\widetilde\tau_{xy}(\xi,y)=-E_sd\sum_{(p,q)\in\mathcal H}(pk_x)(qk_y)F_{pq}\sin(p\theta_x)\sin(q\theta_y).}
\tag{86}
\]

其中 \(d=(U^*)^2-A_{0\ell}^2\)。总弹性局部应力

\[
\boxed{\sigma_x(\xi,y)=\bar\sigma_{x,r}^{R02,f}+\widetilde\sigma_x(\xi,y)}
\tag{87}
\]

\[
\boxed{\sigma_y(\xi,y)=\bar\sigma_{y,r}^{R02,f}+\widetilde\sigma_y(\xi,y)}
\tag{88}
\]

\[
\boxed{\tau_{xy}(\xi,y)=\widetilde\tau_{xy}(\xi,y).}
\tag{89}
\]

von Mises 平方

\[
\boxed{\Phi(\xi,y)=\sigma_x^2-\sigma_x\sigma_y+\sigma_y^2+3\tau_{xy}^2}
\tag{90}
\]

\[
\boxed{\Phi_{\max}=\max_{cell}\Phi.}
\tag{91}
\]

若

\[
\boxed{\Phi_{\max}\le f_y^2}
\tag{92}
\]

则格室平均应力直接取

\[
\boxed{\sigma_{x,r}^{f}=\bar\sigma_{x,r}^{R02,f}}
\tag{93}
\]

\[
\boxed{\sigma_{y,r}^{f}=\bar\sigma_{y,r}^{R02,f}.}
\tag{94}
\]

若超过屈服，则定义 radial factor \(0<\lambda\le1\)，缩放宏观面应变

\[
\boxed{e_x^f(\lambda)=\lambda e_x^f}
\tag{95}
\]

\[
\boxed{e_y^f(\lambda)=\lambda e_y^f}
\tag{96}
\]

每个 \(\lambda\) 重新计算 \(B_1,U^*,m_x,m_y\) 及完整有限谐波场，定义

\[
\boxed{\Psi(\lambda)=\Phi_{\max}(\lambda)-f_y^2}
\tag{97}
\]

\[
\boxed{\lambda_y=\min\{\lambda\in(0,1]:\Psi(\lambda)=0\}.}
\tag{98}
\]

最终返回

\[
\boxed{\sigma_{x,r}^{f}=Q_s[m_x(\lambda_y)+\nu_sm_y(\lambda_y)]}
\tag{99}
\]

\[
\boxed{\sigma_{y,r}^{f}=Q_s[m_y(\lambda_y)+\nu_sm_x(\lambda_y)].}
\tag{100}
\]

---

## 12. Face-wise four-class aggregation

上钢壳四类数量满足

\[
\boxed{C_E^++C_-^++C_0^++C_+^+=J_+.}
\tag{101}
\]

下钢壳

\[
\boxed{C_E^-+C_-^-+C_0^-+C_+^-=J_-.}
\tag{102}
\]

等宽格室面积权重

\[
\boxed{\frac{s_fL_G}{bL_G}=\frac1{J_f}.}
\tag{103}
\]

上钢面平均应力

\[
\boxed{\bar\sigma_x^+=\frac{C_E^+\sigma_{x,E}^++C_-^+\sigma_{x,-}^++C_0^+\sigma_{x,0}^++C_+^+\sigma_{x,+}^+}{J_+}}
\tag{104}
\]

\[
\boxed{\bar\sigma_y^+=\frac{C_E^+\sigma_{y,E}^++C_-^+\sigma_{y,-}^++C_0^+\sigma_{y,0}^++C_+^+\sigma_{y,+}^+}{J_+}.}
\tag{105}
\]

下钢面

\[
\boxed{\bar\sigma_x^-=\frac{C_E^-\sigma_{x,E}^-+C_-^-\sigma_{x,-}^-+C_0^-\sigma_{x,0}^-+C_+^-\sigma_{x,+}^-}{J_-}}
\tag{106}
\]

\[
\boxed{\bar\sigma_y^-=\frac{C_E^-\sigma_{y,E}^-+C_-^-\sigma_{y,-}^-+C_0^-\sigma_{y,0}^-+C_+^-\sigma_{y,+}^-}{J_-}.}
\tag{107}
\]

---

## 13. Steel-shell N and M by full physical thickness

\[
\boxed{N_{x,s}^+=t_s\bar\sigma_x^+}
\tag{108}
\]

\[
\boxed{N_{y,s}^+=t_s\bar\sigma_y^+}
\tag{109}
\]

\[
\boxed{N_{x,s}^-=t_s\bar\sigma_x^-}
\tag{110}
\]

\[
\boxed{N_{y,s}^-=t_s\bar\sigma_y^-.}
\tag{111}
\]

钢壳总膜力

\[
\boxed{N_x^s=t_s(\bar\sigma_x^++\bar\sigma_x^-)}
\tag{113}
\]

\[
\boxed{N_y^s=t_s(\bar\sigma_y^++\bar\sigma_y^-).}
\tag{114}
\]

钢壳关于整个组合截面中面的弯矩

\[
\boxed{M_x^s=t_sz_f(\bar\sigma_x^+-\bar\sigma_x^-)}
\tag{117}
\]

\[
\boxed{M_y^s=t_sz_f(\bar\sigma_y^+-\bar\sigma_y^-).}
\tag{118}
\]

本版本暂不另加 4 mm 钢板自身局部 plate-bending resultant；局部弯曲能量通过 \(K_b(U-A_0)^2\) 进入局部幅值闭合，gross-section M 与 R14 一致由上下钢面膜力在 \(\pm z_f\) 处形成。

完全展开的钢壳四分类结果量：

\[
\boxed{\begin{aligned}N_x^s={}&\frac{t_s}{J_+}[C_E^+\sigma_{x,E}^++C_-^+\sigma_{x,-}^++C_0^+\sigma_{x,0}^++C_+^+\sigma_{x,+}^+]\\&+\frac{t_s}{J_-}[C_E^-\sigma_{x,E}^-+C_-^-\sigma_{x,-}^-+C_0^-\sigma_{x,0}^-+C_+^-\sigma_{x,+}^-]\end{aligned}}
\tag{170}
\]

\[
\boxed{\begin{aligned}N_y^s={}&\frac{t_s}{J_+}[C_E^+\sigma_{y,E}^++C_-^+\sigma_{y,-}^++C_0^+\sigma_{y,0}^++C_+^+\sigma_{y,+}^+]\\&+\frac{t_s}{J_-}[C_E^-\sigma_{y,E}^-+C_-^-\sigma_{y,-}^-+C_0^-\sigma_{y,0}^-+C_+^-\sigma_{y,+}^-]\end{aligned}}
\tag{171}
\]

\[
\boxed{\begin{aligned}M_x^s={}&\frac{t_sz_f}{J_+}[C_E^+\sigma_{x,E}^++C_-^+\sigma_{x,-}^++C_0^+\sigma_{x,0}^++C_+^+\sigma_{x,+}^+]\\&-\frac{t_sz_f}{J_-}[C_E^-\sigma_{x,E}^-+C_-^-\sigma_{x,-}^-+C_0^-\sigma_{x,0}^-+C_+^-\sigma_{x,+}^-]\end{aligned}}
\tag{172}
\]

\[
\boxed{\begin{aligned}M_y^s={}&\frac{t_sz_f}{J_+}[C_E^+\sigma_{y,E}^++C_-^+\sigma_{y,-}^++C_0^+\sigma_{y,0}^++C_+^+\sigma_{y,+}^+]\\&-\frac{t_sz_f}{J_-}[C_E^-\sigma_{y,E}^-+C_-^-\sigma_{y,-}^-+C_0^-\sigma_{y,0}^-+C_+^-\sigma_{y,+}^-]\end{aligned}}
\tag{173}
\]

---

## 14. UHPC exact thickness primitives

完全不滑移条件下 UHPC 应变

\[
\boxed{\varepsilon_x^U(z)=\varepsilon_x^0+\kappa_x z}
\tag{119}
\]

\[
\boxed{\varepsilon_y^U(z)=\varepsilon_y^0+\kappa_y z.}
\tag{120}
\]

端点

\[
\boxed{\varepsilon_x^{U,+}=\varepsilon_x^0+\kappa_x t_c/2,\qquad \varepsilon_x^{U,-}=\varepsilon_x^0-\kappa_x t_c/2}
\tag{121-122}
\]

\[
\boxed{\varepsilon_y^{U,+}=\varepsilon_y^0+\kappa_y t_c/2,\qquad \varepsilon_y^{U,-}=\varepsilon_y^0-\kappa_y t_c/2.}
\tag{123-124}
\]

压缩参数

\[
\boxed{A_c=\frac{E_c\varepsilon_{c0}}{f_c},\quad B_c=6-5A_c,\quad C_c=4A_c-5}
\tag{125-127}
\]

\[
\boxed{\xi=-\varepsilon/\varepsilon_{c0}}
\tag{128}
\]

\[
\boxed{\sigma_U^c(\varepsilon)=-f_c(A_c\xi+B_c\xi^5+C_c\xi^6).}
\tag{129}
\]

原函数

\[
\boxed{F_0^c(\varepsilon)=f_c\varepsilon_{c0}\left(\frac{A_c}{2}\xi^2+\frac{B_c}{6}\xi^6+\frac{C_c}{7}\xi^7\right)}
\tag{131}
\]

\[
\boxed{F_1^c(\varepsilon)=-f_c\varepsilon_{c0}^2\left(\frac{A_c}{3}\xi^3+\frac{B_c}{7}\xi^7+\frac{C_c}{8}\xi^8\right).}
\tag{133}
\]

拉伸段采用 R14 五锚点 PCHIP。对第 j 段，令 \(s=\varepsilon-\varepsilon_j\)，

\[
\boxed{\sigma_U^t(\varepsilon)=a_j+b_js+c_js^2+d_js^3}
\tag{134}
\]

其中

\[
\boxed{a_j=\sigma_j,\quad b_j=\mu_j}
\tag{135-136}
\]

\[
\boxed{c_j=\frac{3\delta_j-2\mu_j-\mu_{j+1}}{h_j}}
\tag{137}
\]

\[
\boxed{d_j=\frac{\mu_j+\mu_{j+1}-2\delta_j}{h_j^2}.}
\tag{138}
\]

对应

\[
\boxed{\Delta F_{0,j}=a_js+\frac{b_j}{2}s^2+\frac{c_j}{3}s^3+\frac{d_j}{4}s^4}
\tag{139}
\]

\[
\boxed{F_0(\varepsilon)=F_0(\varepsilon_j)+\Delta F_{0,j}}
\tag{140}
\]

\[
\boxed{\begin{aligned}\Delta F_{1,j}={}&\varepsilon_j\left(a_js+\frac{b_j}{2}s^2+\frac{c_j}{3}s^3+\frac{d_j}{4}s^4\right)\\&+\frac{a_j}{2}s^2+\frac{b_j}{3}s^3+\frac{c_j}{4}s^4+\frac{d_j}{5}s^5\end{aligned}}
\tag{141}
\]

\[
\boxed{F_1(\varepsilon)=F_1(\varepsilon_j)+\Delta F_{1,j}.}
\tag{142}
\]

UHPC 横向结果量

\[
\boxed{N_x^U=(1-\rho_w)\frac{F_0(\varepsilon_x^{U,+})-F_0(\varepsilon_x^{U,-})}{\kappa_x}}
\tag{145}
\]

\[
\boxed{M_x^U=(1-\rho_w)\frac{F_1(\varepsilon_x^{U,+})-F_1(\varepsilon_x^{U,-})-\varepsilon_x^0[F_0(\varepsilon_x^{U,+})-F_0(\varepsilon_x^{U,-})]}{\kappa_x^2}.}
\tag{147}
\]

纵向

\[
\boxed{N_y^U=(1-\rho_w)\frac{F_0(\varepsilon_y^{U,+})-F_0(\varepsilon_y^{U,-})}{\kappa_y}}
\tag{149}
\]

\[
\boxed{M_y^U=(1-\rho_w)\frac{F_1(\varepsilon_y^{U,+})-F_1(\varepsilon_y^{U,-})-\varepsilon_y^0[F_0(\varepsilon_y^{U,+})-F_0(\varepsilon_y^{U,-})]}{\kappa_y^2}.}
\tag{150}
\]

若 \(\kappa_x=0\)

\[
\boxed{N_x^U=(1-\rho_w)t_c\sigma_U(\varepsilon_x^0),\qquad M_x^U=0}
\tag{151-152}
\]

若 \(\kappa_y=0\)

\[
\boxed{N_y^U=(1-\rho_w)t_c\sigma_U(\varepsilon_y^0),\qquad M_y^U=0.}
\tag{153-154}
\]

---

## 15. Fully bonded longitudinal web/PBL steel

\[
\boxed{\varepsilon_y^w(z)=\varepsilon_y^0+\kappa_y z}
\tag{155}
\]

\[
\boxed{\varepsilon_Y=f_y/E_s.}
\tag{156}
\]

理想弹塑性

\[
\sigma_y^w(z)=
\begin{cases}
-f_y,&\varepsilon_y^w\le-\varepsilon_Y,\\
E_s(\varepsilon_y^0+\kappa_y z),&|\varepsilon_y^w|<\varepsilon_Y,\\
+f_y,&\varepsilon_y^w\ge+\varepsilon_Y.
\end{cases}
\tag{157-159}
\]

\[
\boxed{N_y^w=\rho_w\int_{-t_c/2}^{t_c/2}\sigma_y^w(z)\,dz}
\tag{160}
\]

\[
\boxed{M_y^w=\rho_w\int_{-t_c/2}^{t_c/2}z\sigma_y^w(z)\,dz.}
\tag{161}
\]

厚度内若穿过 \(\pm\varepsilon_Y\)，按解析交点分段积分。

---

## 16. Full-section N and M

\[
\boxed{N_x=N_x^U+N_x^s}
\tag{162}
\]

\[
\boxed{N_x=N_x^U+t_s(\bar\sigma_x^++\bar\sigma_x^-)}
\tag{163}
\]

\[
\boxed{M_x=M_x^U+M_x^s}
\tag{164}
\]

\[
\boxed{M_x=M_x^U+t_sz_f(\bar\sigma_x^+-\bar\sigma_x^-)}
\tag{165}
\]

\[
\boxed{N_y=N_y^U+N_y^s+N_y^w}
\tag{166}
\]

\[
\boxed{N_y=N_y^U+t_s(\bar\sigma_y^++\bar\sigma_y^-)+N_y^w}
\tag{167}
\]

\[
\boxed{M_y=M_y^U+M_y^s+M_y^w}
\tag{168}
\]

\[
\boxed{M_y=M_y^U+t_sz_f(\bar\sigma_y^+-\bar\sigma_y^-)+M_y^w.}
\tag{169}
\]

---

## 17. R14 outer demand retained unchanged

定义

\[
\boxed{Q=q(q+2q_0)}
\tag{174}
\]

\[
\Delta_A=A_{11}A_{22}-A_{12}^2.
\]

\[
\boxed{K_x=\frac{b^2\alpha^2}{8(A_{22}/\Delta_A)}}
\tag{175}
\]

\[
\boxed{G=\frac{b^2\beta^2}{8(A_{11}/\Delta_A)}}
\tag{176}
\]

\[
\boxed{C=\frac{b^3\Delta_A}{16\beta^2}\left(\frac{\alpha^4}{A_{22}}+\frac{\beta^4}{A_{11}}\right)}
\tag{177}
\]

\[
\boxed{J_x=b(D_x\alpha^2+D_\mu\beta^2)}
\tag{178}
\]

\[
\boxed{J_y=b(D_\mu\alpha^2+D_y\beta^2)}
\tag{179}
\]

\[
\boxed{P(q)=P_{cr}\frac{q}{q+q_0}+CQ}
\tag{180}
\]

\[
\boxed{N_x^A=K_xQ}
\tag{181}
\]

\[
\boxed{M_x^A=J_xq}
\tag{182}
\]

\[
\boxed{N_y^A=-\left[\frac{P(q)}b-GQ\right]}
\tag{183}
\]

\[
\boxed{M_y^A=J_yq.}
\tag{184}
\]

---

## 18. Final four equilibrium equations

对给定 \(q\)，未知量仅

\[
\boxed{\varepsilon_x^0,\ \kappa_x,\ \varepsilon_y^0,\ \kappa_y.}
\]

\[
\boxed{R_{N_x}=N_x^U+N_x^s-N_x^A(q)=0}
\tag{185}
\]

\[
\boxed{R_{M_x}=M_x^U+M_x^s-M_x^A(q)=0}
\tag{186}
\]

\[
\boxed{R_{N_y}=N_y^U+N_y^s+N_y^w-N_y^A(q)=0}
\tag{187}
\]

\[
\boxed{R_{M_y}=M_y^U+M_y^s+M_y^w-M_y^A(q)=0.}
\tag{188}
\]

\[
\boxed{\mathbf R_4=[R_{N_x},R_{M_x},R_{N_y},R_{M_y}]^T=\mathbf0.}
\tag{189}
\]

---

## 19. Execution chain

1. 输入 \((b,a,t_c,t_s,A_w,E_s,\nu_s,f_y,E_c,\nu_c,\ldots)\)。
2. 计算 \(A_{11},A_{22},A_{12},D_x,D_y,D_\mu,D_{66}\)。
3. 比较整体模态得到 \(m^*\)，再得 \(L_G=a/m^*\)。
4. 对上、下钢面读取同侧加劲肋间距 \(s_+,s_-\)。
5. 计算 \(n_{0,f}=\lfloor L_G/s_f\rfloor\)。
6. 每个横向格室只分类为 \(E,n_0-1,n_0,n_0+1\)。
7. E 类走完整厚度理想弹塑性；屈曲类依次计算 \(n\to k_y\to c_y,K_b,K_A\to B_3,B_1,B_0\to U^*\to m_x,m_y\to R02/R06\to \sigma_x,\sigma_y\)。
8. 只按格室数量汇总 \(C_E,C_-,C_0,C_+\)，得到上下钢面平均应力。
9. 由完整物理厚度得到钢壳 \(N_x^s,M_x^s,N_y^s,M_y^s\)。
10. UHPC 使用同一组 \(\varepsilon_x^0,\kappa_x,\varepsilon_y^0,\kappa_y\) 进行连续厚度解析积分。
11. 必要时加入完全黏结的 web 理想弹塑性积分。
12. 最终求解原 R14 四平衡 \(R_{N_x}=R_{M_x}=R_{N_y}=R_{M_y}=0\)。

---

## 20. Strict degradation to single-cell R14

若一侧所有格室都采用同一局部类型，例如全部 \(L_0\)，则

\[
C_0^f=J_f,
\]

其余分类数为 0，从而

\[
\bar\sigma_x^f=\sigma_{x,0}^f,\qquad \bar\sigma_y^f=\sigma_{y,0}^f.
\]

钢壳组装严格退化为

\[
N_x^s=t_s(\sigma_x^++\sigma_x^-),\quad M_x^s=t_sz_f(\sigma_x^+-\sigma_x^-),
\]

\[
N_y^s=t_s(\sigma_y^++\sigma_y^-),\quad M_y^s=t_sz_f(\sigma_y^+-\sigma_y^-).
\]

因此多波钢壳01不是另一套平行理论，而是 R14 单格室钢面算子的有限四分类扩展；R14 单格室是本版本的严格退化极限。

---

## 21. Locked scope

本文件仅锁定“多波钢壳01—不考虑剪切滑移版本”。任何部分组合、PBL 界面剪切刚度、钢壳-UHPC 力流重新分配、滑移自由度、99-cell 独立幅值或连续最优局部波长均不属于本文件。若四分类多格室版本在数值执行中不能闭合，唯一退路是上述严格退化的单格室 R14/R13，不再创建额外中间路线。
