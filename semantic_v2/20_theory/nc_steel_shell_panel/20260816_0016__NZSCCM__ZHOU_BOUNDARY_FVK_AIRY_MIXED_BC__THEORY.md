# Zhou four-edge wall in-plane boundary — Classical FvK/Airy mixed-BC zero-quadrature derivation

**Timestamp:** 2026-08-16 00:16 +08:00

## 1. Source boundary and coordinates

Use `x` across wall width `b`, `y` along the axial loading direction. Zhou thesis Table 1.3 gives, for the four-edge simply-supported wall:

```text
loaded top:    ux=0, uy=unset, uz=0
loaded bottom: ux=0, uy=0,     uz=0
non-loaded left/right: ux=unset, uy=unset, uz=0
```

Hence the in-plane membrane problem has an essential transverse-displacement condition on both loaded ends,

\[
u(x,0)=u(x,a)=0,
\]

while the lateral sides are in-plane free and therefore carry the natural membrane conditions

\[
N_x=N_{xy}=0\qquad (x=0,b).
\]

This is not the uniform free-Poisson membrane state.

## 2. FvK source retained from the 00:07 classical gate

For one complete out-of-plane halfwave

\[
w_0=A_0\sin\alpha x\sin\beta y,
\qquad
w_a=A\sin\alpha x\sin\beta y,
\]

with

\[
\alpha=\pi/b,\qquad \beta=\pi/\ell,
\qquad S=A^2+2A_0A,
\]

the exact incremental curvature-determinant source is

\[
K(w_0+w_a)-K(w_0)
=-\frac{S\alpha^2\beta^2}{2}
[\cos 2\alpha x+\cos2\beta y].
\]

The compatibility equation is

\[
\nabla^4\Phi
=Et\frac{S\alpha^2\beta^2}{2}
[\cos2\alpha x+\cos2\beta y].
\]

The particular coefficients remain

\[
C_{20}=\frac{EtS\beta^2}{32\alpha^2},
\qquad
C_{02}=\frac{EtS\alpha^2}{32\beta^2}.
\]

They are compatibility-generated coefficients, not independent generalized coordinates.

## 3. Why the 00:07 particular field is not Zhou-boundary complete

The particular field

\[
\Phi_p=C_{20}\cos2\alpha x+C_{02}\cos2\beta y
\]

gives

\[
N_x=\Phi_{,yy}
=-4\beta^2C_{02}\cos2\beta y.
\]

This is nonzero at `x=0,b`; therefore it violates the free lateral-side traction condition. The 00:07 field is a correct compatibility particular solution, but not a complete solution for Zhou's mixed in-plane boundary class.

## 4. Exact homogeneous correction for the free lateral sides

Let

\[
k=2\beta,\qquad
\xi=x-b/2,\qquad
h=b/2,\qquad
z=kh=\beta b,
\]

and write the complete `(0,2)` Airy part as

\[
\Phi_{02}=g(x)\cos ky.
\]

Because the forcing is the constant particular amplitude `C02`, write

\[
g(x)=C_{02}G(s),\qquad s=k\xi.
\]

The homogeneous correction obeys

\[
(D_x^2-k^2)^2[g-C_{02}]=0.
\]

Free lateral-side traction requires

\[
g(0)=g(b)=0,
\qquad
g'(0)=g'(b)=0.
\]

The exact even solution is

\[
\boxed{
G(s)=1-
\frac{z\cosh z+\sinh z}{z+\sinh z\cosh z}\cosh s
+\frac{\sinh z}{z+\sinh z\cosh z}s\sinh s
}
\]

with

\[
G(\pm z)=G'(\pm z)=0.
\]

Therefore

\[
N_x=-k^2 C_{02}G(s)\cos ky,
\]

\[
N_y=-N-4\alpha^2C_{20}\cos2\alpha x
+k^2C_{02}G''(s)\cos ky,
\]

\[
N_{xy}=k^2C_{02}G'(s)\sin ky.
\]

At `x=0,b`, both `Nx` and `Nxy` vanish exactly. No spatial quadrature or spatial sampling is used.

Useful exact derivatives/values are

\[
G''(s)=
\frac{s\sinh s\sinh z-z\cosh s\cosh z+\sinh z\cosh s}
{z+\tfrac12\sinh2z},
\]

\[
G(0)=
-\frac{z\cosh z-z+\sinh z-\tfrac12\sinh2z}
{z+\tfrac12\sinh2z},
\]

\[
G''(0)=
-\frac{z\cosh z-\sinh z}
{z+\tfrac12\sinh2z},
\]

\[
G''(z)=
-\frac{z-\tfrac12\sinh2z}
{z+\tfrac12\sinh2z}.
\]

## 5. Loaded-edge `ux=0` check

At `y=0` and `y=ell`, the nonlinear transverse geometric strain term is zero because `sin(beta y)=0`. Since Zhou prescribes `u=0` along the complete loaded edge,

\[
\varepsilon_x(x,0)=u_{,x}(x,0)=0.
\]

For isotropic plane stress,

\[
\varepsilon_x=\frac{N_x-\nu N_y}{Et},
\]

so the pointwise loaded-edge condition is

\[
\boxed{N_x(x,0)-\nu N_y(x,0)=0.}
\]

Substituting the side-free corrected Airy field gives

\[
R_{end}(x)
=-k^2C_{02}[G(s)+\nu G''(s)]
+\nu N
+4\nu\alpha^2C_{20}\cos2\alpha x.
\]

Define

\[
\chi=\beta/\alpha=b/\ell.
\]

After division by `4 alpha^2 C02`, the non-constant part is

\[
H(X)
=-\chi^2[G+\nu G'']
+\nu\chi^4\cos2X,
\qquad X=\alpha x.
\]

The mean resultant `N` can add only one spatial constant. Therefore `R_end(x)=0` can be achieved by a single `N` only if `H(X)` is constant.

For the original Z6 geometry `chi=b/a=4/3`, exact formula evaluation gives, for `nu=0.18`,

```text
H(side)   = +0.251345415562366
H(center) = -2.037087472469174
Delta     = +2.288432888031540
```

and for `nu=0.30`,

```text
H(side)   = +0.418909025937277
H(center) = -2.395786001921834
Delta     = +2.814695027859111
```

Hence the side-traction correction alone cannot satisfy Zhou's pointwise loaded-edge transverse restraint. A second homogeneous biharmonic boundary-layer family is necessary.

This is an algebraic failure of a truncated Airy representation, not a material failure and not a numerical integration failure.

## 6. Exact side-correction moment diagnostic

For the side-free `(0,2)` correction define

\[
J(z)=\int_{-z}^{z}
[G^2+(G'')^2+2(G')^2]ds.
\]

Analytical integration gives

\[
\boxed{
J(z)=2\frac{
 z^3+z^2\sinh2z
 +\frac z4(\cosh2z-1)^2
 -\frac z2\cosh2z+\frac z2
 +\frac12\sinh2z-\frac14\sinh4z
}{(z+\tfrac12\sinh2z)^2}
}
\]

so no numerical integration is needed.

Exact-form evaluations:

```text
chi=1      z=pi      J=2.389471026245563
chi=4/3    z=4pi/3   J=4.394765944033305
```

These values are representation diagnostics only; they are not released as the exact Zhou mixed-boundary postbuckling coefficient because the loaded-edge restraint is not yet closed.

## 7. Rigorous sign of the Zhou-boundary membrane contribution

The classical elastic membrane energy is positive definite:

\[
U_m=\frac{Et}{2(1-\nu^2)}\iint
\left[
\varepsilon_x^2+\varepsilon_y^2+2\nu\varepsilon_x\varepsilon_y
+\frac{1-\nu}{2}\gamma_{xy}^2
\right]dA.
\]

The admissible displacement space contains the essential Zhou condition `u(x,0)=u(x,a)=0`; free lateral tractions are natural conditions of the exact minimizer.

For fixed nonlinear source `S`, the membrane problem is linear in the induced in-plane displacement/stress correction. Therefore the condensed minimum energy has the form

\[
U_m^{Zhou}=K_Z S^2.
\]

For `A>0`, the FvK compatibility source is nonzero. If `K_Z=0`, positive definiteness would require all membrane strains to vanish identically, contradicting the nonzero FvK compatibility source. Hence

\[
\boxed{K_Z>0.}
\]

Since

\[
S=A^2+2A_0A,
\qquad
\frac{dS}{dA}=2(A+A_0)>0,
\]

the condensed classical membrane contribution to the transverse equilibrium is positive for `A>0`:

\[
\frac{dU_m^{Zhou}}{dA}
=2K_ZS\frac{dS}{dA}>0.
\]

Thus Zhou's loaded-edge transverse restraint cannot reverse the classical elastic membrane effect into the artificial softening produced by the retired free `p20,p02` closure.

## 8. Zero-quadrature admissible Ritz diagnostic

To verify the essential boundary mechanism independently, use the finite analytic trial family

\[
u=-\frac{S\alpha}{4}
\left[r_0(X-\pi/2)+\frac{r_2}{2}\sin2X\right]\sin^2Y,
\]

\[
v=-\frac{S\beta}{8}s_2\sin2Y\sin^2X.
\]

It satisfies `u=0` at both loaded ends and uses only finite trigonometric/polynomial moments. Its exact strains are

\[
\varepsilon_x=\frac{S\alpha^2}{4}
[(1-r_0)+(1-r_2)\cos2X]\sin^2Y,
\]

\[
\varepsilon_y=\frac{S\beta^2}{4}
[1+(1-s_2)\cos2Y]\sin^2X,
\]

\[
\gamma_{xy}=\frac{S\alpha\beta}{4}
\left[
\left(1-\frac{r_2+s_2}{2}\right)\sin2X-r_0(X-\pi/2)
\right]\sin2Y.
\]

Exact symbolic energy minimization gives, for original Z6 `chi=4/3`:

```text
nu=.18:
r0=0.699436656466086
r2=1.081366761351356
s2=1.072663180284274
positive trial membrane coefficient kp_trial=4.91147853093745

nu=.30:
r0=0.820658109922641
r2=0.959792698594651
s2=1.086743159321920
positive trial membrane coefficient kp_trial=5.23972966834637
```

This is an admissible finite Ritz diagnostic, not the exact Zhou closure and not a production coefficient. It further confirms the sign while the exact mixed-boundary homogeneous family remains open.

## 9. Important `m>1` representative-halfwave issue

Zhou's `ux=0` condition acts at the **physical loaded ends** `y=0,a`. For a physical wall with `m>1`, the internal zero-deflection lines between repeated out-of-plane halfwaves are not physical loaded ends and must not automatically inherit `ux=0`.

Therefore, for the earlier `a/b=2, m=2, ell=a/2` Z6 comparison specimen, a global end-restraint boundary layer is not automatically periodic with the representative out-of-plane halfwave. Before that AR2 specimen can be recomputed under `ONE_CONTINUOUS_COMPLETE_HALFWAVE`, the global mixed-boundary correction must be analytically condensed onto the representative halfwave without falsely imposing `ux=0` at the internal halfwave interface.

This is now an explicit gate item; it does not authorize spatial subdivision.

## 10. Current conclusion

```text
FvK compatibility particular = correct but boundary incomplete
lateral-side exact biharmonic correction = closed
loaded-edge ux=0 residual after side correction = nonzero / x-dependent
full mixed-boundary homogeneous correction = still required
classical membrane postbuckling sign under Zhou BC = strictly positive
zero spatial numerical integration = maintained
new nonlinear-material Pu = not authorized yet
```
