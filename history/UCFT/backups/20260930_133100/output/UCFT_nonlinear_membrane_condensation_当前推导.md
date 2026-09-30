# UCFT nonlinear membrane condensation 当前推导

**状态时间：2026-09-30 13:31 +08:00**  
**路线合同：用户上传《指示词.md》为最高优先级。**  
**当前任务：M0 + M1。**

---

## 1. 锁定对象

采用：

[
0le xle b,qquad 0le yle a_h,
]

并定义

[
X=rac{pi x}{b},qquad Y=rac{pi y}{a_h}.
]

整体 stress-free 初始构形：

[
W_0=bq_0sin Xsin Y,
]

当前整体构形：

[
W=b(q_0+q)sin Xsin Y.
]

定义纯书写缩写

[
Q(q)=q^2+2q_0q,
qquad
C_q=rac{pi^2Q(q)}{8}.
]

其中 (q) 为整体路径参数，(q_0) 为无应力初始几何缺陷。

---

## 2. 由整体面外场得到的 Kármán 几何增量

有

[
rac12left(W_{,x}^2-W_{0,x}^2ight)
=
C_qleft[
1+cos2X-cos2Y-cos2Xcos2Y
ight],
]

[
rac12left(W_{,y}^2-W_{0,y}^2ight)
=
C_qrac{b^2}{a_h^2}
left[
1-cos2X+cos2Y-cos2Xcos2Y
ight],
]

[
W_{,x}W_{,y}-W_{0,x}W_{0,y}
=
2C_qrac{b}{a_h}sin2Xsin2Y.
]

因此中面兼容源严格为

[
oxed{
arepsilon_{x,yy}^0+
arepsilon_{y,xx}^0-
gamma_{xy,xy}^0
=
rac{pi^4Q(q)}{2a_h^2}
left(cos2X+cos2Yight)
}
]

该式不预设 (N_{xy}=0)。

---

## 3. C1 最小 compatible displacement basis

为避免直接猜应变场，先定义面内位移：

[
oxed{
egin{aligned}
u(x,y)
={}&
(E_x-C_q)x
+rac{b}{2pi}(B_x-C_q)sin2X\
&+rac{b}{2pi}(C_q+H_x)sin2Xcos2Y,
end{aligned}}
]

[
oxed{
egin{aligned}
v(x,y)
={}&
left(E_y-C_qrac{b^2}{a_h^2}ight)y
+rac{a_h}{2pi}
left(B_y-C_qrac{b^2}{a_h^2}ight)sin2Y\
&+rac{a_h}{2pi}
left(C_qrac{b^2}{a_h^2}+H_yight)
cos2Xsin2Y.
end{aligned}}
]

这里

[
E_x,E_y,B_x,B_y,H_x,H_y
]

均为 inner membrane coefficients，不是新的结构路径自由度。

由

[
arepsilon_x^0=u_{,x}
+rac12(W_{,x}^2-W_{0,x}^2),
]

[
arepsilon_y^0=v_{,y}
+rac12(W_{,y}^2-W_{0,y}^2),
]

[
gamma_{xy}^0=u_{,y}+v_{,x}
+
W_{,x}W_{,y}-W_{0,x}W_{0,y},
]

严格得到：

[
oxed{
arepsilon_x^0
=
E_x+B_xcos2X-C_qcos2Y
+H_xcos2Xcos2Y
}
]

[
oxed{
arepsilon_y^0
=
E_y-C_qrac{b^2}{a_h^2}cos2X
+B_ycos2Y
+H_ycos2Xcos2Y
}
]

[
oxed{
gamma_{xy}^0
=
-
left(
rac{b}{a_h}H_x+
rac{a_h}{b}H_y
ight)
sin2Xsin2Y
}
]

---

## 4. compatibility identity 的严格验证

(E_x,E_y) 为常数，因此不进入兼容源。

(B_xcos2X) 对 (y) 二阶导数为零；  
(B_ycos2Y) 对 (x) 二阶导数为零。

特解部分给出：

[
rac{partial^2}{partial y^2}
(-C_qcos2Y)
=
rac{4pi^2C_q}{a_h^2}cos2Y
=
rac{pi^4Q}{2a_h^2}cos2Y,
]

[
rac{partial^2}{partial x^2}
left(
-C_qrac{b^2}{a_h^2}cos2X
ight)
=
rac{pi^4Q}{2a_h^2}cos2X.
]

对 (H_x,H_y)：

[
arepsilon_{x,yy}^{H}
=
-rac{4pi^2}{a_h^2}
H_xcos2Xcos2Y,
]

[
arepsilon_{y,xx}^{H}
=
-rac{4pi^2}{b^2}
H_ycos2Xcos2Y,
]

[
-gamma_{xy,xy}^{H}
=
4pi^2
left(
rac{H_x}{a_h^2}
+
rac{H_y}{b^2}
ight)
cos2Xcos2Y.
]

三者严格相消，因此

[
oxed{
arepsilon_{x,yy}^0+
arepsilon_{y,xx}^0-
gamma_{xy,xy}^0
=
rac{pi^4Q}{2a_h^2}
(cos2X+cos2Y)
}
]

对任意 (E_x,E_y,B_x,B_y,H_x,H_y) 恒成立。

M0 的 compatible basis 由此通过。

---

## 5. C0：Chen–Ji zero-shear 退化

令

[
H_x=H_y=0,
]

则

[
gamma_{xy}^0=0.
]

若材料剪应力满足

[
N_{xy}proptogamma_{xy}^0,
]

则

[
N_{xy}=0.
]

C0 中面应变为

[
oxed{
arepsilon_x^0
=
E_x+B_xcos2X-C_qcos2Y
}
]

[
oxed{
arepsilon_y^0
=
E_y-C_qrac{b^2}{a_h^2}cos2X
+B_ycos2Y
}
]

内部变量仅为

[
(E_x,E_y,B_x,B_y).
]

---

## 6. C0 / C1 内层虚功残量

设

[
Omega=[0,b]	imes[0,a_h].
]

(N_x,N_y,N_{xy}) 均由 UHPC + 上钢壳 + 下钢壳 current material integration 得到。

横向没有外加总膜力时：

[
oxed{
G_{E_x}
=
int_Omega N_x,dA
=0
}
]

轴向压力 (P>0)，膜力拉正时：

[
oxed{
G_{E_y}
=
int_Omega N_y,dA
+
P a_h
=0
}
]

对 (B_x)：

[
oxed{
G_{B_x}
=
int_Omega
N_xcos2X,dA
=0
}
]

对 (B_y)：

[
oxed{
G_{B_y}
=
int_Omega
N_ycos2Y,dA
=0
}
]

C1 再增加：

[
oxed{
G_{H_x}
=
int_Omega
left[
N_xcos2Xcos2Y
-
rac{b}{a_h}
N_{xy}sin2Xsin2Y
ight]dA
=0
}
]

[
oxed{
G_{H_y}
=
int_Omega
left[
N_ycos2Xcos2Y
-
rac{a_h}{b}
N_{xy}sin2Xsin2Y
ight]dA
=0
}
]

所以：

C0：

[
mathbf G_{C0}
=
(G_{E_x},G_{E_y},G_{B_x},G_{B_y})^T
=mathbf0
]

C1：

[
mathbf G_{C1}
=
(G_{E_x},G_{E_y},G_{B_x},G_{B_y},G_{H_x},G_{H_y})^T
=mathbf0.
]

C0 求解后仍必须额外评价被删去的：

[
widehat G_{H_x}
=
int_Omega
N_xcos2Xcos2Y,dA,
]

[
widehat G_{H_y}
=
int_Omega
N_ycos2Xcos2Y,dA,
]

用于审计 (N_{xy}=0) 是否在 nonlinear state 中仍近似自洽。

---

## 7. Gate 1：一般线弹性层合组合截面的退化

令

[
A^+=A^-=0,
]

所有相均退回线弹性。

对上下对称、各相平面内各向同性的组合截面，膜刚度写成

[
egin{bmatrix}
N_x\N_y\N_{xy}
end{bmatrix}
=
egin{bmatrix}
A_{11}&A_{12}&0\
A_{12}&A_{11}&0\
0&0&A_{66}
end{bmatrix}
egin{bmatrix}
arepsilon_x^0\
arepsilon_y^0\
gamma_{xy}^0
end{bmatrix}.
]

由于每一层均为平面应力各向同性材料，

[
A_{66}
=
rac{A_{11}-A_{12}}{2}.
]

定义

[
ar
u=rac{A_{12}}{A_{11}},
qquad
ar K=A_{11}(1-ar
u^2).
]

C0 中：

[
N_x
=
A_{11}arepsilon_x^0+A_{12}arepsilon_y^0,
]

[
N_y
=
A_{12}arepsilon_x^0+A_{11}arepsilon_y^0.
]

由 (G_{B_x}=0)：

[
A_{11}B_x
-
A_{12}C_qrac{b^2}{a_h^2}
=0,
]

故

[
oxed{
B_x
=
ar
u C_qrac{b^2}{a_h^2}
}
]

由 (G_{B_y}=0)：

[
A_{11}B_y-A_{12}C_q=0,
]

故

[
oxed{
B_y=ar
u C_q
}
]

由横向总合力为零：

[
A_{11}E_x+A_{12}E_y=0,
]

即

[
oxed{
E_x=-ar
u E_y
}
]

再由轴向总合力：

[
A_{12}E_x+A_{11}E_y=-rac{P}{b},
]

得到

[
oxed{
E_y
=
-rac{P/b}{A_{11}(1-ar
u^2)}
}
]

[
oxed{
E_x
=
rac{ar
u,P/b}
{A_{11}(1-ar
u^2)}
}
]

代回，严格得到

[
oxed{
N_x(y)
=
-ar K C_qcos2Y
}
]

[
oxed{
N_y(x)
=
-rac{P}{b}
-
ar K C_q
rac{b^2}{a_h^2}
cos2X
}
]

以及

[
oxed{N_{xy}=0}.
]

因此：

[
N_{x,x}=0,
qquad
N_{y,y}=0,
]

二维膜力平衡严格满足。

对于均质单层：

[
A_{11}=rac{Et}{1-
u^2},
qquad
A_{12}=
u A_{11},
]

所以

[
ar
u=
u,
qquad
ar K=Et,
]

并退回经典 Chen–Ji/Kármán–Airy zero-shear 分离解：

[
N_x
=
-Et,C_qcos2Y,
]

[
N_y
=
-rac{P}{b}
-Et,C_qrac{b^2}{a_h^2}cos2X.
]

---

## 8. 显式 Airy 函数恢复

令

[
k_x=rac{2pi}{b},
qquad
k_y=rac{2pi}{a_h}.
]

取

[
oxed{
Phi(x,y)
=
-rac{P}{2b}x^2
+
rac{ar K C_q b^4}{4pi^2a_h^2}cos2X
+
rac{ar K C_q a_h^2}{4pi^2}cos2Y
}
]

则

[
Phi_{,yy}=N_x,
qquad
Phi_{,xx}=N_y,
qquad
-Phi_{,xy}=0.
]

因此 C0 在线弹性极限下确实恢复 Airy 静力可容场。

---

## 9. C1 在线弹性极限下的 H 子系统

在 C1 中只考察 (H_x,H_y) 产生的增量：

[
deltaarepsilon_x
=
H_xcos2Xcos2Y,
]

[
deltaarepsilon_y
=
H_ycos2Xcos2Y,
]

[
deltagamma_{xy}
=
-
left(
rac{b}{a_h}H_x+
rac{a_h}{b}H_y
ight)
sin2Xsin2Y.
]

利用三角正交性，(G_{H_x}=G_{H_y}=0) 化为

[
rac{ba_h}{4}
egin{bmatrix}
A_{11}+A_{66}r^2 & A_{12}+A_{66}\
A_{12}+A_{66} & A_{11}+A_{66}r^{-2}
end{bmatrix}
egin{bmatrix}
H_x\H_y
end{bmatrix}
=
mathbf0,
]

其中

[
r=rac{b}{a_h}.
]

因

[
A_{66}=rac{A_{11}-A_{12}}{2}
=
rac{A_{11}(1-ar
u)}{2},
]

该 (2	imes2) 子矩阵行列式为

[
oxed{
A_{11}^2
(1-ar
u)
left[
1+rac12(r^2+r^{-2})
ight]
>0
}
]

对物理范围 (ar
u<1) 恒正。

因此唯一解是

[
oxed{
H_x=H_y=0.
}
]

所以 C1 在线弹性极限下唯一退化至 C0；不存在额外 spurious shear branch。

---

## 10. Gate 1 结论

Gate 1 要求：

1. (A^+=A^-=0)；
2. 所有材料线弹性；
3. C1 必须给 (H_x=H_y=0)；
4. 恢复 Chen–Ji/Airy (N_{xy}=0) 分离解。

上述四项均已解析证明。

[
oxed{	ext{Gate 1 = PASS}}
]

这不是数值拟合结果，而是符号恒等式。

---

## 11. 本轮发现的边界问题

当前 C0/C1 compatible displacement basis 在 (y=0,a_h) 上的上述最低阶 (v) 形式会使边界轴向位移的最低阶表示保持直线。该性质与 Chen–Ji 8.8 straight-edge 退化相容，因此不影响 Gate 1。

但当前最高层路线已经明确：端部统一位移不得作为外部控制条件，最终 (Delta(x)) 应由平衡状态恢复。因此在后续 nonlinear Gate 2 / Gate 3 中，需要把“是否需要 end-warping compatible nullspace”作为 omitted generalized residual 的边界审计对象，而不能把 straight-edge 结果当作先验位移控制。

本项目前只记录，不新增阻塞 Gate；只有其 omitted residual 在 nonlinear state 中显著时才激活对应 compatible enrichment。

---

## 12. 当前状态

M0：

- C0 compatible basis：完成；
- C1 compatible displacement basis：完成；
- compatibility identity：符号验证通过；
- 六个 (G) residual：完成。

M1：

- 线弹性 composite C0 closed form：完成；
- Airy 恢复：完成；
- C1 的 (H_x,H_y) 唯一零解证明：完成；
- Gate 1：PASS。

---

## 13. 唯一 NEXT_ACTION

进入 M2：

[
A^+=A^-=0,
]

打开 UHPC nonlinear tension/compression polynomial active-set，保持钢壳无 local mode，分别计算

[
P_{C0}(q),qquad
P_{C1}(q),qquad
H_x(q),qquad
H_y(q),
]

以及

[
widehat G_{H_x}(q),qquad
widehat G_{H_y}(q),
]

以判断“材料非线性本身”是否足以激活 (N_{xy}) 通道。

M2 不使用 FEM 拟合。
