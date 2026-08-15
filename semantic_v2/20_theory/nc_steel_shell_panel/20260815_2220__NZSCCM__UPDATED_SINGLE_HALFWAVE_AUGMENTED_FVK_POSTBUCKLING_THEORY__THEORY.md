# NZ-SCCM — 更新后的单一完整半波增广 FvK 后屈曲理论

**Timestamp:** 2026-08-15 22:20 +08:00  
**Status:** current theory consolidation after 21:18 → 21:34 → 21:44 → 21:53

## 1. Domain and coordinates

Keep one continuous complete representative out-of-plane halfwave:

\[
X=\pi x/b,\qquad Y=\pi y/a,\qquad k=b/a.
\]

Initial imperfection and additional transverse deflection:

\[
w_0=A_0\sin X\sin Y,\qquad A_0=q_0b=a/500,
\]

\[
w_m=A\sin X\sin Y,\qquad A=qb.
\]

No `q31`, `q13` or any other out-of-plane production mode is introduced.

## 2. Nguyen second-order source

With `w=w0+wm`, Nguyen Eq.(6.3) supplies the imperfect second-order membrane source. Define

\[
S=A^2+2A_0A.
\]

The nonlinear mid-plane strain source contains exactly

\[
\varepsilon_x^{NL}=\frac{S\pi^2}{8b^2}
[1+\cos2X-\cos2Y-\cos2X\cos2Y],
\]

\[
\varepsilon_y^{NL}=\frac{S\pi^2}{8a^2}
[1-\cos2X+\cos2Y-\cos2X\cos2Y],
\]

\[
\gamma_{xy}^{NL}=\frac{S\pi^2}{4ab}\sin2X\sin2Y.
\]

Hence one `(1,1)` out-of-plane halfwave automatically generates multiple in-plane harmonics. Under the FvK compatibility operator, the independent forcing reduces to basic `(2,0)` and `(0,2)` membrane redistribution directions plus the homogeneous field imposed by mean load and in-plane boundaries.

## 3. Generalized coordinates

External/loading coordinate:

\[
D.
\]

Out-of-plane coordinate:

\[
q.
\]

Minimum in-plane membrane coordinates:

\[
\mathbf m=[c,p_{20},p_{02}]^T.
\]

`c` retains its original role: enforce/represent the already-audited loaded-edge in-plane admissible boundary warp.

`p20,p02` are not new buckling modes. They are in-plane redistribution coordinates demanded by the single-halfwave second-order source.

## 4. Minimum admissible in-plane displacement completion

### 4.1 Boundary warp c

The current normalized strain directions are

\[
e_{x,c}=\frac{4}{\pi}\sin X\sin^2Y,
\]

\[
e_{y,c}=\frac{8k^2}{\pi}\sin X\cos2Y,
\]

with zero added linear engineering shear.

### 4.2 p20 direction

Define

\[
U_{20}=\frac{b}{2\pi}\sin2X\sin^2Y,
\]

\[
V_{20}=\frac{b^2}{4\pi a}\cos2X\sin2Y.
\]

The physical in-plane contribution is

\[
u_{20}=\varepsilon_0p_{20}U_{20},\qquad
v_{20}=\varepsilon_0p_{20}V_{20}.
\]

The normalized virtual strains are

\[
e_{x,20}=\cos2X\sin^2Y,
\]

\[
e_{y,20}=\frac{k^2}{2}\cos2X\cos2Y,
\]

\[
\gamma_{xy,20}=0.
\]

In D15 polynomial variables `xs=sinX`, `ys=sinY`:

\[
e_{x,20}=y_s^2-2x_s^2y_s^2,
\]

\[
e_{y,20}=\frac{k^2}{2}(1-2x_s^2)(1-2y_s^2).
\]

### 4.3 p02 direction

Define

\[
U_{02}=0,\qquad V_{02}=\frac{a}{2\pi}\sin2Y,
\]

so

\[
e_{x,02}=0,
\qquad e_{y,02}=\cos2Y=1-2\sin^2Y,
\qquad \gamma_{xy,02}=0.
\]

All warping contributions vanish on the loaded edges and do not alter the imposed mean end shortening.

## 5. Updated normalized strain field used by the current implementation

Let

\[
x_s=\sin X,\qquad y_s=\sin Y,\qquad \eta\in[-1,1],
\]

and define

\[
M=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right),
\qquad
B=\frac{\pi^2t_c}{2\varepsilon_0b}q.
\]

Then the current normalized normal-strain fields are

\[
\hat\varepsilon_x=
M y_s^2-Mx_s^2y_s^2+B x_sy_s\eta
+c\frac{4}{\pi}x_sy_s^2
+p_{20}(y_s^2-2x_s^2y_s^2),
\]

\[
\begin{aligned}
\hat\varepsilon_y={}&-D+k^2Mx_s^2-k^2Mx_s^2y_s^2+k^2B x_sy_s\eta\\
&+c\frac{8k^2}{\pi}x_s(1-2y_s^2)\\
&+p_{20}\frac{k^2}{2}(1-2x_s^2)(1-2y_s^2)\\
&+p_{02}(1-2y_s^2).
\end{aligned}
\]

The added `c,p20,p02` directions contribute no new linear shear. The retained Nguyen shear field may be represented in squared polynomial form as

\[
\hat\gamma_{xy}^2=
4k^2(1-x_s^2)(1-y_s^2)(Mx_sy_s-B\eta)^2.
\]

For q-directional derivatives,

\[
M_q=\frac{\pi^2}{\varepsilon_0}(q_0+q),
\qquad
B_q=\frac{\pi^2t_c}{2\varepsilon_0b}.
\]

The `q,c,p20,p02` virtual-strain directions are finite analytic polynomials and remain inside General D15.

## 6. Material map remains unchanged

The theory still uses

\[
\boldsymbol\varepsilon
\rightarrow M(\boldsymbol\varepsilon)
\rightarrow\boldsymbol\sigma.
\]

For concrete this is the frozen R10 / N48-C1/MM / Cayley-Hamilton current map. Steel retains the frozen local radial-cap current operator. No new constitutive mechanism is introduced by the FvK membrane completion.

## 7. Generalized residual system

For any retained generalized coordinate `r`,

\[
R_r=\int_V \boldsymbol\sigma^T
\frac{\partial\boldsymbol\varepsilon}{\partial r}\,dV.
\]

At fixed D the membrane subsystem is

\[
\mathbf R_m=
\begin{bmatrix}R_c\\R_{20}\\R_{02}\end{bmatrix}=\mathbf0,
\]

while transverse equilibrium is

\[
R_q=0.
\]

The complete fixed-D augmented equilibrium is therefore

\[
R_q=R_c=R_{20}=R_{02}=0.
\]

## 8. Flat membrane condensation

Define

\[
\mathbf J_{mm}=\frac{\partial\mathbf R_m}{\partial\mathbf m},
\qquad
\mathbf J_{mq}=\frac{\partial\mathbf R_m}{\partial q}.
\]

At membrane equilibrium,

\[
\frac{d\mathbf m}{dq}=-\mathbf J_{mm}^{-1}\mathbf J_{mq}.
\]

The condensed scalar out-of-plane tangent is

\[
L_{cond}=R_{q,q}-\mathbf R_{q,m}\mathbf J_{mm}^{-1}\mathbf J_{m,q}.
\]

Thus the intended architecture is one flat `3x3` membrane matrix plus vectors/scalars, not a growing nested matrix hierarchy.

## 9. Structural integration is unchanged

All added strain fields are finite polynomials in `sinX,sinY` and thickness coordinate. Therefore

```text
P, Rq, Rc, R20, R02
and their directional Jacobian contractions
```

remain exact coefficient-space moment contractions under General D15.

```text
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
```

No Gauss, Simpson, adaptive spatial integration, material-point grid or spatial Chebyshev collocation is introduced.

## 10. Current Z6 fixed-D=.50 state

The best released augmented near-equilibrium from the 21:53 stage is

```text
D=.50
q=.008002
c=-.077622
p20=-.060657
p02=.165133
P=37.69591555 MN
```

This is not Pu and is not yet a strict same-expression certificate.

## 11. Current implementation frontier

The physical theory is now the minimum FvK-source-complete Ritz membrane system. The unresolved issue is implementation efficiency: naive full N48 dense coefficient composition retains large high-order dense boxes near the augmented state.

The next evaluator must therefore be directional/moment-first: compute only the contractions needed by `P,Rq,Rc,R20,R02` and the flat membrane/tangent Jacobian before constructing unnecessary full stress-field coefficient tensors.
