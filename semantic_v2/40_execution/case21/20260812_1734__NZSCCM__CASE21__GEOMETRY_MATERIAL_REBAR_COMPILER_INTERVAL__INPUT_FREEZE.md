# NZ-SCCM Case21 原始输入冻结表

**时间基线：2026-08-12 17:34 +08:00**  
**身份：CURRENT CASE21 RAW INPUT FREEZE / NO THEORY RESULT / NO EXPERIMENT LOAD**

本文件只冻结 Case21 正式重算所需原始材料、几何、配筋与 compiler 区间。它不包含任何历史 Case21 理论根、理论荷载、FE/Gauss/Simpson 结果或试验极限荷载。

## 1. 几何

\[
\boxed{b=\ell=1220\ \mathrm{mm},\qquad t_p=19.30\ \mathrm{mm}}
\]

式中，\(b\) 为完整代表半波宽度；\(\ell\) 为轴向完整半波长度；\(t_p\) 为板厚。

## 2. 普通混凝土

\[
\boxed{f_c=21.23\ \mathrm{MPa},\qquad E_0=20321\ \mathrm{MPa},\qquad \varepsilon_0=0.00209,\qquad \nu=0.18}
\]

式中，\(f_c\) 为单轴抗压强度；\(E_0\) 为初始弹性模量；\(\varepsilon_0\) 为 R10 参考压缩应变；\(\nu\) 为泊松比。

## 3. 初始缺陷

\[
\boxed{q_0=\frac{A_0}{b}=\frac1{400}=0.0025}
\]

式中，\(A_0\) 为 stress-free initial imperfection 物理幅值；\(q_0\) 为初始缺陷比。

## 4. 配筋

总双向配筋率 0.75%，两个方向均分：

\[
\boxed{\rho_{s,x}=\rho_{s,y}=0.00375}
\]

Case21 为中面单层钢筋：

\[
\boxed{z_s=0,\qquad \zeta_s=0}
\]

式中，\(\rho_{s,x},\rho_{s,y}\) 为两个正交方向配筋率；\(z_s\) 为钢筋层相对中面的物理位置；\(\zeta_s=2z_s/t_p\) 为归一化厚度位置。

钢筋材料参数：

\[
\boxed{E_s=200000\ \mathrm{MPa},\qquad \varepsilon_y=0.00265,\qquad f_y=530\ \mathrm{MPa}}
\]

式中，\(E_s\) 为钢筋弹性模量；\(\varepsilon_y\) 为屈服应变；\(f_y\) 为屈服应力。

## 5. R10 冻结常数

\[
\boxed{\rho=0.1,\qquad m_t=-\frac7{90},\qquad \eta_r=0.05,\qquad u_r=0.03}
\]

\[
\boxed{a_{cc}=0.1072329249362415,\qquad a_t=1-2^{-1/8}}
\]

式中，\(\rho\) 为 R10 拉伸强度尺度；\(m_t\) 为 Foster-informed 拉伸下降参数；\(\eta_r\) 为源平滑铰宽度；\(u_r\) 为残余拉应力尺度；\(a_{cc}\) 为项目冻结双压物理目标系数；\(a_t\) 为项目冻结双拉物理目标系数。

## 6. compiler 区间

\[
\boxed{\lambda\in[\lambda_a,\lambda_b]=[-1.15,0.12]}
\]

式中，\(\lambda_a=-1.15\) 为材料主等效应变 compiler 下界；\(\lambda_b=0.12\) 为上界。该区间在求根前冻结，禁止根据历史理论结果或试验荷载调整。

## 7. 隔离声明

```text
HISTORICAL_CASE21_D_Q_P_Pu_ROOT_PATH_INCLUDED = NO
HISTORICAL_FE_GAUSS_SIMPSON_INCLUDED = NO
EXPERIMENTAL_LIMIT_LOAD_INCLUDED = NO
```
