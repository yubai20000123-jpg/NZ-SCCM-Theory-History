# NZ-SCCM theory — Case21 stable conformal R10 source, certified 16-state field and single-domain semialgebraic period

**Timestamp:** 2026-08-17 11:55 +08:00  
**Identity:** internal derivation of the existing `CASE21_AIRY_SCALAR_FORMAL_ZERO_SPATIAL_ULTIMATE_LOAD` task.

## 1. Starting point

Retain the frozen Airy-scalar strain field

\[
r=\lambda M a(\nu),
\qquad
M=\frac{\pi^2}{\varepsilon_0}\left(q_0q+\frac12q^2\right),
\]

with

\[
a(\nu)=\left[-\frac{1+\nu}{4},-\frac{1-\nu}{4},\frac14,-\frac{1-\nu}{4},\frac14\right]^T.
\]

Let

\[
C_X=\cos2X,\quad C_Y=\cos2Y,
\quad S_X=\sin2X,\quad S_Y=\sin2Y,
\]

\[
B=\frac{\pi^2}{2\varepsilon_0}\frac tb q.
\]

Then

\[
\begin{aligned}
e_x={}&\nu D+\frac M4[1+C_X-C_Y-C_XC_Y\\
&-\lambda(1+\nu)-\lambda(1-\nu)C_X+\lambda C_XC_Y]
+B\sin X\sin Y\,\zeta,
\end{aligned}
\]

\[
\begin{aligned}
e_y={}&-D+\frac M4[1-C_X+C_Y-C_XC_Y\\
&-\lambda(1-\nu)C_Y+\lambda C_XC_Y]
+B\sin X\sin Y\,\zeta,
\end{aligned}
\]

\[
\gamma_{xy}=\frac M2(1-\lambda)S_XS_Y-2B\cos X\cos Y\,\zeta.
\]

The equivalent plane-stress tensor is

\[
E=\begin{bmatrix}
(e_x+\nu e_y)/(1-\nu^2)&\gamma_{xy}/[2(1+\nu)]\\
\gamma_{xy}/[2(1+\nu)]&(\nu e_x+e_y)/(1-\nu^2)
\end{bmatrix}.
\]

## 2. Stable conformal representation of the smoothed positive part

For scalar `x`, define

\[
w=\frac{x}{\sqrt{x^2+\eta^2}+\eta},\qquad |w|<1.
\]

Then

\[
x=\frac{2\eta w}{1-w^2},
\qquad
\sqrt{x^2+\eta^2}=\eta\frac{1+w^2}{1-w^2}.
\]

The frozen smooth positive map is

\[
\pi_\eta(x)=\frac{x^2(\sqrt{x^2+\eta^2}+x)}{2(x^2+\eta^2)}.
\]

Direct substitution yields

\[
\boxed{
\pi_\eta(x)=xw\frac{(1+w)^2}{(1+w^2)^2}
}
\]

and, replacing `x` by `-x`,

\[
\boxed{
\pi_\eta(-x)=xw\frac{(1-w)^2}{(1+w^2)^2}.
}
\]

For a real symmetric 2x2 matrix `E`, define the commuting matrix function

\[
W=E\left(\sqrt{E^2+\eta^2I}+\eta I\right)^{-1}.
\]

By spectral functional calculus the scalar identities lift exactly to

\[
\boxed{
T_0:=\pi_\eta(E)=E W(I+W)^2(I+W^2)^{-2},
}
\]

\[
\boxed{
C_0:=\pi_\eta(-E)=E W(I-W)^2(I+W^2)^{-2}.
}
\]

This is preferable to a representation containing separate inverse powers of `I-W` or `I+W`. The latter can be badly conditioned for a strongly compressive eigenvalue because the corresponding conformal eigenvalue approaches `-1`. In the present certified Case21 neighborhood the negative conformal eigenvalue reaches about `-0.9973`, whereas `1+w^2` stays close to 2 and cannot vanish for real `w`.

## 3. Polynomial invariants for a Bernstein enclosure

Let

\[
u=\sin X,\qquad v=\sin Y,\qquad w=(\zeta+1)/2.
\]

Then

\[
C_X=1-2u^2,\qquad C_Y=1-2v^2,\qquad \zeta=2w-1.
\]

The tensor trace has the compact identity

\[
\operatorname{tr}E=\frac{e_x+e_y}{1-\nu},
\]

and the eigenvalue-gap square is

\[
\boxed{
\Delta_E=(x_{11}-x_{22})^2+4x_{12}^2
}
\]

with

\[
x_{11}-x_{22}=\frac{e_x-e_y}{1+\nu},
\]

\[
x_{12}^2=(1-u^2)(1-v^2)
\left[\frac{M(1-\lambda)uv-B\zeta}{1+\nu}\right]^2.
\]

Therefore, at fixed `(D,q,lambda)`,

```text
deg_{u,v,w} tr(E)    = (2,2,1)
deg_{u,v,w} Delta(E) = (4,4,2)
```

and both can be enclosed over the complete continuum domain by tensor-product Bernstein coefficients. This is a finite polynomial-coefficient transformation, not a spatial point grid.

At the current direct-source peak the resulting enclosures are

\[
-0.9516607416735428\le\operatorname{tr}E\le-0.6221638560307847,
\]

\[
0.5843087672642922\le\Delta_E\le0.6592312757236101.
\]

Hence

\[
0.7644009205019916\le g:=\sqrt{\Delta_E}\le0.8119305855327844,
\]

and

\[
\lambda_+=\frac{\operatorname{tr}E+g}{2}
\in[-0.09362991058577558,0.09488336475099984],
\]

\[
\lambda_-=\frac{\operatorname{tr}E-g}{2}
\in[-0.8817956636031636,-0.6932823882663881].
\]

## 4. R10 source-knot consequences

For Case21

\[
\kappa=2.0005129533678754,
\qquad
\eta=0.0024993589726987125,
\]

\[
a=\rho/\kappa=0.04998717945397425.
\]

The tensile-source transition points are defined by

\[
\pi_\eta(\lambda_1)=a,
\qquad
\pi_\eta(\lambda_{10})=10a,
\]

which gives

\[
\lambda_1=0.05008051764913754,
\qquad
\lambda_{10}=0.49988116674539307.
\]

Applying the monotone source map to the Bernstein principal bounds gives

```text
peak:
0 <= t_plus/a  <= 1.8971668284751766
0 <= t_minus/a <= 4.506313752829062e-5
```

so

```text
minus principal source: low branch only
plus principal source : low or middle branch only
second t=10a source knot: inactive
spectral coincidence: excluded by g>=0.7644
```

The same statements remain certified throughout

```text
D      in [0.75,0.82]
q      in [0.00175,0.00187]
lambda in [0.0,0.15]
```

because a six-variable Bernstein enclosure gives

```text
g >= 0.7242936864852092
t_plus/a  <= 2.6948274361042803 < 10
t_minus/a <= 4.804460717539394e-5 < 1.
```

## 5. Exact branch-specific 16-state field

Let

\[
g=\sqrt{\Delta_E},
\]

\[
s_+=\sqrt{\lambda_+^2+\eta^2},
\qquad
s_-=\sqrt{\lambda_-^2+\eta^2}.
\]

The smooth source maps `t_+`, `t_-`, `c_+`, `c_-` are rational functions of `lambda_+`, `lambda_-`, `s_+`, `s_-`. The compression map

\[
C_i=\frac{\kappa c_i}{1+(\kappa-2)c_i+c_i^2}
\]

introduces no new radical. The spectral projector

\[
P_+=\frac{E-\lambda_-I}{g}
\]

also introduces no new radical because `g` is already present and has a strict positive lower bound.

Because the second tensile knot is inactive, the frozen `C2` tensile spline needs only the first truncated-power selector. Define

\[
f_1=t_+-a,
\qquad
h_1=\sqrt{f_1^2}=|f_1|.
\]

Then

\[
(f_1)_+^p=\left(\frac{f_1+h_1}{2}\right)^p,
\qquad p=3,4,5.
\]

Therefore the complete current source and stress lie in the multiquadratic extension generated by

\[
\{g,s_+,s_-,h_1\}.
\]

A basis is

\[
\boxed{
\mathcal B_{16}
=\{g^i s_+^j s_-^k h_1^\ell\}_{i,j,k,\ell\in\{0,1\}}
}
\]

so the field dimension is bounded by

\[
\boxed{\dim\mathcal B\le16.}
\]

This is a strict reduction from the prior generic `<=64` branch-free bound. The generic bound remains necessary outside the certified Case21 box.

## 6. Why the physical period is semialgebraic rather than one analytic algebraic branch

The frozen tensile function is exactly `C2` at `t=a`, but its third derivative has a nonzero jump. In normalized coordinate `z=t/a`, the low and middle source curves satisfy

\[
[u]_{z=1}=[u']_{z=1}=[u'']_{z=1}=0,
\]

but for the Case21 constants

\[
[u''']_{z=1}=-3.485446758727596\ne0.
\]

Equivalently, the first truncated-power coefficient is

\[
A_3=-0.580907793121266\ne0.
\]

The first knot is not merely a possible branch: it is actually crossed on the physical complete halfwave. At the single line `X=Y=pi/2`,

\[
\lambda_+(-1)=-0.08174749432807749<\lambda_1,
\]

\[
\lambda_+(+1)=0.08300094849330153>\lambda_1,
\]

and the crossing occurs at

\[
\zeta\approx0.600355180536.
\]

Thus `h1=|f1|` changes from `-f1` to `+f1` on the physical domain. It is pointwise algebraic but cannot be represented as one holomorphic algebraic branch across the crossing. Formally differentiating

\[
h_1^2=f_1^2
\]

gives

\[
h_1'=\frac{f_1f_1'}{h_1},
\]

which exhibits the branch-switch singularity at `h1=0` even though the final frozen source is `C2` after cancellation in the truncated-power combination.

Consequently an ordinary analytic 16-state Pfaffian propagation in the thickness coordinate is not a complete runtime by itself. A production evaluator must retain the positive-part gluing as a semialgebraic primitive or an equivalent exact selector.

## 7. Exact one-domain rationalization of the structural period

To retain one spatial domain while exposing a rational base, set

\[
r_X=\frac{\tan(X/2)}{1+\tan(X/2)},
\qquad
r_Y=\frac{\tan(Y/2)}{1+\tan(Y/2)}.
\]

For `r in [0,1]`, define

\[
Q(r)=r^2+(1-r)^2.
\]

Then

\[
\sin X=\frac{2r_X(1-r_X)}{Q(r_X)},
\quad
\cos X=\frac{1-2r_X}{Q(r_X)},
\quad
dX=\frac{2dr_X}{Q(r_X)},
\]

and likewise for `Y`. With

\[
w=(\zeta+1)/2,
\qquad d\zeta=2dw,
\]

the complete structural domain is exactly

\[
\boxed{(r_X,r_Y,w)\in[0,1]^3}
\]

with no cell decomposition. Every Nguyen/Airy kinematic term and every T12 weight becomes rational in the unit-cube coordinates. The R10 lift is a finite algebraic extension plus the positive-part semialgebraic selector.

Therefore each formal T12 entry has the mathematical identity

\[
\boxed{
J_i=\iiint_{[0,1]^3}
R_i(r_X,r_Y,w;D,q,\lambda;g,s_+,s_-,h_1)\,dr_Xdr_Ydw,
}
\]

where `R_i` is rational in the base coordinates and the four certified algebraic/semialgebraic generators.

This is the precise surviving production object:

```text
SINGLE_FIXED_DOMAIN_SEMIALGEBRAIC_PERIOD
```

not a spatial quadrature and not a high-order coefficient surface.

## 8. Consequence for the missing numeric runtime

The remaining formal implementation problem is now narrower than the 11:26 statement:

```text
INPUT: (D,q,lambda) inside the certified Case21 box
BASE DOMAIN: one fixed unit cube
SOURCE FIELD: <=16 algebraic states + one physical positive-part gluing already included in h1
OUTPUT: T12 and same-source D/q/lambda derivatives
NO: spatial quadrature, cells, material points, high-order multivariate coefficient enumeration
```

The ordinary algebraic/Pfaffian approach fails at the real Foster knot unless it is upgraded to a semialgebraic period evaluator. This is the current exact runtime boundary. It does not invalidate the R10 source, T12 contraction, Airy-scalar mechanics, or the one-domain formal architecture.

Formal `Rq=RA=L3=0` and `Pu` remain unreleased until this numerical period evaluator actually exists.
