# UCFT M3 steel-local qA / A² 有限谐波谱审计

更新时间：2026-09-30 14:50 +08:00

## 1. M3 边界

本阶段打开 \(A^+,A^-\)，但不提前进入 M5 的 steel plastic active-set，也不提前求 M6 的 \(R_{A^\pm}=0\) 路径。任务仅为从锁定的 whole-face multiwave geometry 精确展开 \(qA\) 与 \(A^2\) 的有限频谱，并建立 compatible omitted generalized residual。

\[
\psi_\ell=[1-\cos(2NX)][1-\cos(2mY)],\quad
X=\pi x/b,\quad Y=\pi y/a_h,\quad r=b/a_h.
\]

TOP 的 global-local 系数为
\[
q_0A^+ + qA_0^+ + qA^+,
\]
local-local 系数为
\[
(A^+)^2+2A_0^+A^+.
\]
BOTTOM 的 global-local 项反号，local-local 项同号。

## 2. qA exact spectrum

将 qA 应变除以共同因子
\[
\pi^2(q_0A+qA_0+qA)/b,
\]
在 \(N,m\ge2\) 时得到八个且仅八个 mixed pairs。法向为 \(\sin(kX)\sin(lY)\)，剪切为 \(\cos(kX)\cos(lY)\)。

| k | l | ex coefficient | ey coefficient | gamma coefficient |
|---|---|---:|---:|---:|
| 2N-1 | 1 | N | 0 | +Nr |
| 2N+1 | 1 | N | 0 | -Nr |
| 1 | 2m-1 | 0 | mr² | +mr |
| 1 | 2m+1 | 0 | mr² | -mr |
| 2N-1 | 2m-1 | N/2 | mr²/2 | -(N+m)r/2 |
| 2N-1 | 2m+1 | -N/2 | mr²/2 | (m-N)r/2 |
| 2N+1 | 2m-1 | N/2 | -mr²/2 | (N-m)r/2 |
| 2N+1 | 2m+1 | -N/2 | -mr²/2 | (N+m)r/2 |

\(N=1\) 或 \(m=1\) 时重合频率只需代数合并，不产生新频率。

现有 C-family 是 normal cos-cos / shear sin-sin，因此对 qA 的 odd-odd parity 正交。必须允许新的 S-family compatible pair：

\[
\Delta\varepsilon_x=S_{x,kl}\sin(kX)\sin(lY),
\]
\[
\Delta\varepsilon_y=S_{y,kl}\sin(kX)\sin(lY),
\]
\[
\Delta\gamma_{xy}
=
-\left[
\frac{lb}{ka_h}S_{x,kl}
+
\frac{ka_h}{lb}S_{y,kl}
\right]\cos(kX)\cos(lY).
\]

逐项有
\[
\Delta\varepsilon_{x,yy}
+\Delta\varepsilon_{y,xx}
-\Delta\gamma_{xy,xy}=0,
\]
故它是严格 compatible inner nullspace，不是结构级新自由度。

## 3. A² exact spectrum

将 A² 应变除以
\[
\pi^2(A^2+2A_0A)/b^2,
\]
得到

\[
\begin{aligned}
\Delta\varepsilon_x^{A^2}/G
={}&N^2[
3/2-2\cos(2mY)+\tfrac12\cos(4mY)
-\tfrac32\cos(4NX)\\
&+2\cos(4NX)\cos(2mY)
-\tfrac12\cos(4NX)\cos(4mY)],
\end{aligned}
\]

\[
\begin{aligned}
\Delta\varepsilon_y^{A^2}/G
={}&m^2r^2[
3/2-2\cos(2NX)+\tfrac12\cos(4NX)
-\tfrac32\cos(4mY)\\
&+2\cos(2NX)\cos(4mY)
-\tfrac12\cos(4NX)\cos(4mY)],
\end{aligned}
\]

\[
\begin{aligned}
\Delta\gamma_{xy}^{A^2}/G
={}&4Nmr\sin(2NX)\sin(2mY)
-2Nmr\sin(2NX)\sin(4mY)\\
&-2Nmr\sin(4NX)\sin(2mY)
+Nmr\sin(4NX)\sin(4mY),
\end{aligned}
\]
其中 \(G=\pi^2(A^2+2A_0A)/b^2\)。

四个 mixed C-family pairs：
\[
(2N,2m),(2N,4m),(4N,2m),(4N,4m).
\]

同时严格产生四个 1-D companion harmonics：
\[
(0,2m),(0,4m),(2N,0),(4N,0).
\]

常数项由 \(E_x,E_y\) 吸收。1-D 项分别需要 \(B_{x,k}\cos kX\) 或 \(B_{y,l}\cos lY\) 类型的 compatible inner response；不能因为 M3 原任务强调 mixed pair 就遗漏它们。

## 4. 线弹性 steel-skin omitted residual 的闭式谱

M5 尚未开始，因此 M3 只用 plane-stress linear steel tangent 作不含 FEM、不含拟合的 mechanism audit：

\[
Q_s=\frac{E_st_s}{1-\nu_s^2}.
\]

对任一 \(k,l>0\) 的 C/S harmonic，若归一化 strain coefficients 为 \((a,b,c)\)，则去掉共同幅值和 \((ba_h/4)Q_s\) 后：

\[
\widehat g_x
=
a+\nu_sb
-\frac{1-\nu_s}{2}\frac{lr}{k}c,
\]

\[
\widehat g_y
=
b+\nu_sa
-\frac{1-\nu_s}{2}\frac{k}{lr}c.
\]

一维项：
\[
\widehat g_{B_x,k}=2(a_{k0}+\nu_sb_{k0}),
\qquad
\widehat g_{B_y,l}=2(b_{0l}+\nu_sa_{0l}).
\]

TOP/BOTTOM 的 qA residual 异号组合；A² residual 同号组合。因此完全对称 top/bottom benchmark 可能抵消 qA，但不能把这种特殊对称当作通用删项依据。

## 5. 频谱数值审计

只做无量纲扫描：
\[
\nu_s=0.30,\quad N,m=2,\ldots,12,\quad 0.5\le b/a_h\le2.
\]
不使用 FEM target。

qA：
- 四个 edge pairs 合计 share：74.8746%–98.7147%；
- 再加两个 same-sign diagonal pairs 后，六项合计：95.3120%–99.8324%，平均 99.1172%；
- 两个 off-diagonal high-high pair 单项最大仍可到 2.3440%，所以不能在通用理论中永久删除。

A²：
- mixed (2N,2m)：约 9.24%–9.28%；
- mixed (2N,4m)：最高 38.1537%；
- mixed (4N,2m)：最高 38.1537%；
- mixed (4N,4m)：最高 4.7142%；
- 1-D (0,4m) 与 (4N,0)：最高均可达 42.5647%；
- 1-D (0,2m) 与 (2N,0)：最高均约 6.8198%。

因此 A² 的 1-D companion harmonics 与 mixed harmonics 同量级，必须进入 candidate ledger。

## 6. N=m=4, r=1 纯代数 benchmark

该 benchmark 不锁定任何试件的 \(N,m\)。

qA residual share：
- (9,1) 31.2787%
- (1,9) 31.2787%
- (7,1) 13.3121%
- (1,7) 13.3121%
- (9,9) 4.8189%
- (7,7) 4.8189%
- (7,9) 0.5903%
- (9,7) 0.5903%

A² residual share（包含 1-D）：
- (16,8) 22.4455%
- (8,16) 22.4455%
- (16,0) 17.1833%
- (0,16) 17.1833%
- (8,8) 9.2398%
- (16,16) 4.7142%
- (0,8) 3.3942%
- (8,0) 3.3942%

## 7. M3 裁决

\[
\boxed{\mathrm{M3\ geometric\ spectrum\ audit}=PASS}
\]

但原始单一 C1 \((2,2)\) pair 不能覆盖 steel-local：

- qA 需要 S-family；
- A² 需要有限 C-family + 1-D B-family。

这属于 M3 本来就要识别的 minimal compatible enrichment，不是路线级失败，也不增加结构级 \(q,A^+,A^-\)。

正式实现采用 frequency-generated inner active-set：每一状态先算 omitted residual，只有显著频率才实例化；所有 exact candidate frequencies 保留在候选库中，不做永久先验删项。

## 8. NEXT_ACTION

进入 M4：完成 UHPC 拉压多项式 active-set 的 production 面内解析分区，在保留 M2 厚度闭式的基础上，把二维 residual 降为解析分区 + 最多一个低维确定积分；二维/三维 Gauss 只能作为独立验证。
