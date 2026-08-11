# NZ-SCCM Case21 N48-C1/MM + D15 独立盲算输入

**本文件故意不提供本轮理论答案，也不提供试验破坏荷载。**

## 严格隔离
```text
不得读取项目其他 Case21 历史 Pu/D/q/root/path
不得读取旧 direct-N48 Case21 数值
不得读取历史 Gaussian FE / quadrature 结果
不得读取试验荷载参与求解
正式空间 Gauss/Simpson/adaptive quadrature = 0
正式空间 material-point grid/cells = 0
```

## 原始输入
\[
b=\ell=1220\ {\rm mm},\quad t_p=19.30\ {\rm mm},
\]
\[
f_c=21.23\ {\rm MPa},\quad E_0=20321\ {\rm MPa},
\quad \varepsilon_0=0.00209,\quad \nu=0.18.
\]
\[
q_0=1/400.
\]
总双向配筋率 \(0.75\%\)，每方向 \(0.375\%\)，中面单层。
\[
E_s=200000\ {\rm MPa},\quad \varepsilon_y=0.00265,\quad f_y=530\ {\rm MPa}.
\]
\[
\rho=0.1,\quad m_t=-7/90,\quad \eta_r=0.05,\quad u_r=0.03,
\]
\[
a_{cc}=0.107232924936241,\qquad a_t=1-2^{-1/8}.
\]

fresh compiler 在求解前固定为
\[
\boxed{\lambda\in[-1.15,0.12]}.
\]

## 必须执行
1. 由 Foster 源材料功从零计算 \(W_{src}\) 与 \(h\)。
2. 重新生成闭式 R10 的 \(U,C,T,T^7\)。
3. 对 \(U,C,T^7\) 使用 N48-C1 公式；对 \(T\) 重新做 full-hull strict-C1 constrained-minimax。
4. 自己重新生成49×4系数，不得读取现成答案系数表。
5. Cayley–Hamilton 二维提升。
6. Nguyen 一个连续完整方形半波二阶运动学。
7. 所有空间待积量转为有限解析系数，只允许 D15 精确矩；禁止物理空间数值求积。
8. 钢筋在求根之前进入 \(P,R_q,L\)。
9. 联立
\[
R_q(D,q)=0,
\qquad
L(D,q)=P_{,D}R_{q,q}-P_{,q}R_{q,D}=0.
\]
10. 导数采用同一有限解析表达的解析/自动微分，不使用有限差分生产导数。
11. 给出连续谱域证书，证明最终 \(\lambda\) 全域位于 \([-1.15,0.12]\)。
12. 给出连续钢筋应变证书。
13. 输出 \(D,q,A,C_m,C_b,\mathscr D[S_{yy}],\mathscr D[Q_q],P_c,P_s,P,R_{q,c},R_{q,s},R_q\) 和四个导数、\(L\)。
14. 理论 \(D,q,P_u\) 全部冻结以后停止，不自行寻找试验值。
