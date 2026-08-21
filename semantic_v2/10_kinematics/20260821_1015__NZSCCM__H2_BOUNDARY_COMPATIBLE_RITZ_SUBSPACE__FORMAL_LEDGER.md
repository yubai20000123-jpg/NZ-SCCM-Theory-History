# NZ-SCCM H2 边界兼容面内 Ritz 子空间：显式 strain / residual / Jacobian 账本

- Date: 2026-08-21 10:15 +08:00
- Status: FORMAL DERIVATION LEDGER, pending H2->H4 convergence freeze
- Material: NC-M6 FROZEN
- Formal domain: ONE_CONTINUOUS_COMPLETE_HALFWAVE
- Formal spatial quadrature: ZERO

---

## 1. 坐标与面外场

定义

\[
X=\frac{\pi x}{b},\qquad Y=\frac{\pi y}{\ell},\qquad k=\frac b\ell .
\]

保持原单完整半波，不修改：

\[
w_0=bq_0\sin X\sin Y,\qquad \Delta w=bq\sin X\sin Y.
\]

总面外形状为 `w0 + Delta w`；本账本中的 von Karman 增量膜应变使用

\[
\frac12[(w_0+\Delta w)_{,i}(w_0+\Delta w)_{,j}-w_{0,i}w_{0,j}].
\]

定义

\[
S(q)=q_0q+\frac12q^2,
\qquad
M(q)=\frac{\pi^2}{\varepsilon_0}S(q),
\]

\[
B(q)=\frac{\pi^2t}{2\varepsilon_0 b}q,
\qquad \zeta=\frac{2z}{t}.
\]

其中 `t` 对每个相/层按其物理厚度坐标解释；多相组装时使用各相真实 `z`。

---

## 2. H2 admissible in-plane displacement field

旧单一 `alpha` 正式退出本候选运动学。

H2 取

\[
u=\varepsilon_0\left[
\eta x+\frac{b}{2\pi}
\left(a_{20}\sin2X+a_{22}\sin2X\cos2Y\right)
\right],
\]

\[
v=\varepsilon_0\left[
-Dy+\frac{\ell}{2\pi}
\left(b_{02}\sin2Y+b_{22}\cos2X\sin2Y\right)
\right].
\]

广义坐标：

\[
\mathbf z_{H2}=(D,q,\eta,a_{20},a_{22},b_{02},b_{22}).
\]

### 2.1 Swartz essential in-plane BC

Swartz 取

\[
\boxed{\eta=0}.
\]

于是

\[
u(0,y)=u(b,y)=0
\]

对任意 `y` 逐点成立，因为 `sin(2X)=0` 于 `X=0,pi`。

同时

\[
v(x,0)=0,
\qquad
v(x,\ell)=-\varepsilon_0D\ell,
\]

故底边轴向位移约束与顶边统一轴向缩短逐点成立。

**重要澄清**：essential BC 约束的是位移 `u`，不是总 Green/von-Karman 膜应变的横向积分。即使 `u(0,y)=u(b,y)=0`，`0.5 w_x^2` 仍可使总 `epsilon_x` 具有正的几何膜应变；这代表固定边界下由面外曲率诱发的膜拉伸/压缩反力，不能人为从 strain 中减去。

### 2.2 Z0-Z5 横向自由边

Z 系列令 `eta` 为自由广义坐标，并由其自然虚功方程确定：

\[
R_\eta=0.
\]

由于 `partial epsilon_x / partial eta = epsilon_0`，有

\[
R_\eta=\varepsilon_0\sum_p\int_{V_p}\sigma_x^{(p)}\,dV,
\]

因此

\[
\boxed{R_\eta=0\iff N_x=0}
\]

在当前全局 resultant Ritz 投影意义下成立；H2->H4 用于检查自由边 traction field 的进一步收敛。

---

## 3. H2 显式归一化 strain field

定义

\[
F_x=\cos^2X\sin^2Y,
\qquad
F_y=\sin^2X\cos^2Y,
\]

\[
\phi=\sin X\sin Y,
\qquad
c=\cos X\cos Y,
\]

\[
C_{20}=\cos2X,
\quad C_{02}=\cos2Y,
\quad C_{22}=\cos2X\cos2Y,
\quad S_{22}=\sin2X\sin2Y.
\]

以物理 strain `epsilon = epsilon0 * e` 记，则

\[
\boxed{
e_x=
\eta+a_{20}C_{20}+a_{22}C_{22}+M F_x+B\zeta\phi
}
\]

\[
\boxed{
e_y=
-D+b_{02}C_{02}+b_{22}C_{22}+k^2M F_y+k^2B\zeta\phi
}
\]

\[
\boxed{
\gamma=
-\left(ka_{22}+\frac{b_{22}}k\right)S_{22}
+2kM\phi c
-2kB\zeta c
}
\]

其中 `gamma` 为 engineering shear strain，与项目既有 `tau_xy * gamma_xy` 虚功约定一致。

### 3.1 为什么 H2 是第一闭合谐波空间

单 `(1,1)` 半波的 von Karman 二次项只生成

\[
1,\;\cos2X,\;\cos2Y,\;\cos2X\cos2Y,\;\sin2X\sin2Y.
\]

`D,eta` 承担 uniform `1`；`a20,a22,b02,b22` 独立承担其余 compatible in-plane harmonics。H2 因而是对当前单半波二阶几何项的第一闭合有限面内空间；它不是经验拟合，也不含材料参数 `nu`。

---

## 4. 一阶 strain derivatives：全部显式

定义

\[
M_q=\frac{\pi^2}{\varepsilon_0}(q_0+q),
\qquad
B_q=\frac{\pi^2t}{2\varepsilon_0b}.
\]

归一化 derivatives：

### D

\[
\mathbf e_{,D}=(0,-1,0)^T.
\]

### eta

\[
\mathbf e_{,\eta}=(1,0,0)^T.
\]

### q

\[
\mathbf e_{,q}=\begin{bmatrix}
M_qF_x+B_q\zeta\phi\\
k^2M_qF_y+k^2B_q\zeta\phi\\
2kM_q\phi c-2kB_q\zeta c
\end{bmatrix}.
\]

### a20

\[
\mathbf e_{,a20}=(C_{20},0,0)^T.
\]

### a22

\[
\mathbf e_{,a22}=(C_{22},0,-kS_{22})^T.
\]

### b02

\[
\mathbf e_{,b02}=(0,C_{02},0)^T.
\]

### b22

\[
\mathbf e_{,b22}=(0,C_{22},-S_{22}/k)^T.
\]

物理 derivatives 为 `epsilon_,i = epsilon0 * e_,i`。

---

## 5. 二阶 strain derivatives

所有线性面内 Ritz coordinates 对 strain 均线性：

\[
\mathbf e_{,ij}=0
\]

只要 `(i,j)` 不同时为 `(q,q)`。

唯一非零二阶项来自 von Karman `q^2/2`：

\[
M_{qq}=\frac{\pi^2}{\varepsilon_0},
\qquad B_{qq}=0,
\]

\[
\boxed{
\mathbf e_{,qq}=\begin{bmatrix}
M_{qq}F_x\\
k^2M_{qq}F_y\\
2kM_{qq}\phi c
\end{bmatrix}
}.
\]

该项必须保留；不得因引入 Ritz 子空间而删除 Nguyen/von-Karman 二阶几何一致项。

---

## 6. 多相 current constitutive map

每一相 `p` 使用其冻结 current operator：

\[
\boldsymbol\sigma_p=\mathcal M_p(\boldsymbol\varepsilon).
\]

混凝土保持

\[
\boldsymbol\sigma_c=M_6(\boldsymbol\varepsilon),
\]

钢面板、钢筋、web 等保持当前各自冻结的显式材料律。

结构运动学中不再出现 `nu_c D`；任何 Poisson / multiaxial response 只通过材料 operator 进入 stress。

---

## 7. H2 虚功/Galerkin residuals

对任意自由广义坐标 `z_i`：

\[
\boxed{
R_i(\mathbf z)
=
\sum_p\int_{V_p}
\boldsymbol\sigma_p(\mathbf z):
\boldsymbol\varepsilon_{,i}(\mathbf z)\,dV
=0
}
\]

### 7.1 Swartz H2

`eta=0` 为 essential BC，不建立 `R_eta=0`。内部方程为

\[
\boxed{
R_q=R_{a20}=R_{a22}=R_{b02}=R_{b22}=0.
}
\]

未知结构状态为

\[
(D,q,a20,a22,b02,b22).
\]

### 7.2 Z H2

`eta` 自由，内部方程为

\[
\boxed{
R_q=R_\eta=R_{a20}=R_{a22}=R_{b02}=R_{b22}=0.
}
\]

未知结构状态为

\[
(D,q,\eta,a20,a22,b02,b22).
\]

### 7.3 轴压 resultant

保持

\[
\boxed{
P(\mathbf z)=-\frac1\ell\sum_p\int_{V_p}\sigma_y^{(p)}\,dV.
}
\]

---

## 8. source-consistent Jacobian

设材料一致切线

\[
\mathbf D_p=\frac{\partial\boldsymbol\sigma_p}{\partial\boldsymbol\varepsilon}.
\]

则

\[
\boxed{
J_{ij}
=\frac{\partial R_i}{\partial z_j}
=\sum_p\int_{V_p}
\left[
\boldsymbol\varepsilon_{,i}^{T}\mathbf D_p\boldsymbol\varepsilon_{,j}
+\boldsymbol\sigma_p:\boldsymbol\varepsilon_{,ij}
\right]dV.
}
\]

- 不强迫 `J_ij=J_ji`。
- 不强迫 NC-M6 tangent major symmetry。
- `sigma:epsilon_,qq` 项必须保留。
- H2 新增面内坐标没有二阶 strain derivative，因此除 `q-q` 项外 Jacobian 全由 `epsilon_,i^T D epsilon_,j` 构成。

轴压 resultant 导数：

\[
P_{,j}=-\frac1\ell\sum_p\int_{V_p}
\left(\frac{\partial\sigma_y^{(p)}}{\partial\boldsymbol\varepsilon}\right)
\boldsymbol\varepsilon_{,j}\,dV.
\]

---

## 9. 极限点显式扁平矩阵

### Swartz H2

定义

\[
\mathbf F_{H2}^{S}=
(P,R_q,R_{a20},R_{a22},R_{b02},R_{b22})^T.
\]

变量

\[
\mathbf z_{H2}^{S}=(D,q,a20,a22,b02,b22)^T.
\]

极限条件：

\[
\boxed{
\det\left(\frac{\partial\mathbf F_{H2}^{S}}
{\partial\mathbf z_{H2}^{S}}\right)=0
}
\]

即一个 `6 x 6` 扁平显式矩阵。

### Z H2

定义

\[
\mathbf F_{H2}^{Z}=
(P,R_q,R_\eta,R_{a20},R_{a22},R_{b02},R_{b22})^T,
\]

\[
\mathbf z_{H2}^{Z}=(D,q,\eta,a20,a22,b02,b22)^T.
\]

极限条件为对应 `7 x 7` 扁平显式 determinant。

---

## 10. Nested H_{2N} family 与 H4

为避免“想当然增加模态”，定义唯一 nested compatible family：

\[
u=\varepsilon_0\left[
\eta x+
\sum_{m=1}^{N}\sum_{n=0}^{N}
\frac{b}{2m\pi}a_{2m,2n}
\sin(2mX)\cos(2nY)
\right],
\]

\[
v=\varepsilon_0\left[
-Dy+
\sum_{m=0}^{N}\sum_{n=1}^{N}
\frac{\ell}{2n\pi}b_{2m,2n}
\cos(2mX)\sin(2nY)
\right].
\]

其显式 derivatives：

\[
\frac{u_{,x}}{\varepsilon_0}
=\eta+
\sum_{m=1}^{N}\sum_{n=0}^{N}
a_{2m,2n}\cos(2mX)\cos(2nY),
\]

\[
\frac{v_{,y}}{\varepsilon_0}
=-D+
\sum_{m=0}^{N}\sum_{n=1}^{N}
b_{2m,2n}\cos(2mX)\cos(2nY),
\]

\[
\frac{u_{,y}+v_{,x}}{\varepsilon_0}
=-\sum_{m=1}^{N}\sum_{n=1}^{N}
\left[
\frac{nk}{m}a_{2m,2n}+
\frac{m}{nk}b_{2m,2n}
\right]
\sin(2mX)\sin(2nY).
\]

### H2 = N=1

`u`: `a20,a22`  
`v`: `b02,b22`.

### H4 = N=2

`u`:

- `a20,a22,a24`
- `a40,a42,a44`

`v`:

- `b02,b04`
- `b22,b24`
- `b42,b44`

共 12 个非均匀面内 coordinates；H4 比 H2 增加 8 个。

Swartz H4 状态变量：`D,q + 12 modes`，极限矩阵 `14 x 14`。  
Z H4 再加自由 `eta`，极限矩阵 `15 x 15`。

H4 仍是有限扁平显式系统；没有局部材料点或网格自由度。

---

## 11. formal zero-spatial-integration 身份

H2/H4 只增加有限三角基：

`cos(2mX)cos(2nY)`, `sin(2mX)sin(2nY)`。

因此运动学仍是

`finite trigonometric field + thickness polynomial`。

结构链保持

`finite analytic kinematics -> current M6 -> finite analytic structural kernels -> D15/GKZ exact-moment/period machinery`。

本账本没有引入：

- spatial cells
- Gauss/Simpson formal quadrature
- Chebyshev collocation
- material-point grid
- panel-level surrogate
- empirical restraint factor

故正式治理身份保持：

- `N_formal_spatial_sampling=0`
- `N_formal_spatial_quadrature=0`
- `N_formal_spatial_subdomains=1`

---

## 12. 当前冻结/未冻结项

**已冻结为下一轮唯一结构候选路线：**

1. `alpha` 不再作为正式单一面内重分布坐标。
2. H2/H4 均从 admissible `u,v` 位移场出发。
3. Swartz 用 `eta=0` 严格施加侧边 essential BC。
4. Z 用 `R_eta=0` 处理横向自由 resultant。
5. NC-M6 不改。

**尚未冻结：**

- H2 是否为最终 production subspace。

该项只由预先冻结的 H2->H4 无试验值收敛门禁裁决。
