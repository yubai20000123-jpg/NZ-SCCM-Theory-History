# NZ-SCCM steel shell — J2 deformation-theory lift of source uniaxial steel curve to a plane-stress current operator

**Timestamp:** 2026-08-13 18:34 +08:00  
**Status:** MATERIAL-OPERATOR DERIVATION / CANDIDATE FOR SOURCE-ONLY FREEZE  
**Structural test calibration:** NO  
**Parent extension:** `20260813_1834__NZSCCM__NC_STEEL_SHELL_PANEL__REBAR_REPLACEMENT_GENERAL_D15__THEORY_EXTENSION_CONTRACT.md`

---

## 0. Why this route

Sun Lipeng's source review states that inelastic plate buckling may be treated by plasticity deformation theory/flow theory, or approximately by a Bleich tangent-modulus orthotropic plate. Sun adopts the latter for a simple local-buckling formula and provides a Ramberg-Osgood uniaxial law in the low-plastic-strain inelastic-buckling range. Sun also uses source-based multilinear von-Mises/isotropic-hardening steel laws in FE verification.

NZ-SCCM requires something more specific than a scalar tangent modulus:

```text
current stress = M_s(current in-plane strain)
full 2D plane stress
consistent directional tangent
no structural load-step history
finite analytic compilability
```

A J2 **deformation-theory** lift is therefore investigated because it produces a path-independent current map under monotonic/proportional material loading and exactly reproduces the approved uniaxial source curve. This lift is a project derivation; it is not claimed to be written explicitly in Sun's thesis.

---

## 1. Uniaxial source curve as the only steel-material input

Let the approved monotonic uniaxial steel relation be written as

\[
\boxed{\varepsilon^{uni}(\bar\sigma)
=\frac{\bar\sigma}{E_s}+\psi(\bar\sigma)}.
\]

Here

\[
\boxed{\psi(\bar\sigma)=\varepsilon_p^{eq}(\bar\sigma)}
\]

is the equivalent plastic-strain source function.

For Sun's Ramberg-Osgood source in its stated range,

\[
\boxed{\psi(\bar\sigma)
=p\left(\frac{\bar\sigma}{f_y}\right)^n}.
\]

The same 2D lift below can use a later approved piecewise/multilinear source curve by replacing only `psi(sigma_bar)` and its derivative. Therefore ordinary/high-strength steel can share one 2D operator architecture.

No panel load, buckling load or ultimate load enters `psi`.

---

## 2. J2 deformation-theory relation

Let the 3D stress tensor be decomposed as

\[
\boldsymbol\sigma=\mathbf s+\sigma_m\mathbf I,
\qquad
\sigma_m=\frac13\operatorname{tr}\boldsymbol\sigma,
\]

with von-Mises equivalent stress

\[
\boxed{\bar\sigma=\sqrt{\frac32\mathbf s:\mathbf s}}.
\]

The deformation-theory plastic strain is taken coaxial with the deviatoric stress:

\[
\boxed{
\boldsymbol\varepsilon^p
=\frac32\frac{\psi(\bar\sigma)}{\bar\sigma}\mathbf s
}.
\]

Adding isotropic elastic strain gives

\[
\boxed{
\boldsymbol\varepsilon
=\frac{1+\nu_s}{E_s}\mathbf s
+\frac{1-2\nu_s}{3E_s}\operatorname{tr}(\boldsymbol\sigma)\mathbf I
+\frac32\frac{\psi(\bar\sigma)}{\bar\sigma}\mathbf s
}.
\]

Define the scalar compliance-like factor

\[
\boxed{
A(\bar\sigma)
=\frac{1+\nu_s}{E_s}
+\frac32\frac{\psi(\bar\sigma)}{\bar\sigma}
}
\]

with the continuous elastic limit

\[
A(0)=\frac{1+\nu_s}{E_s}.
\]

Also define

\[
\boxed{B=\frac{2(1-2\nu_s)}{E_s}}.
\]

---

## 3. Plane-stress exact reduction

For the shell,

\[
\sigma_z=0.
\]

Use the in-plane engineering strain vector

\[
\mathbf e=
\begin{bmatrix}
\varepsilon_x\\
\varepsilon_y\\
\gamma_{xy}
\end{bmatrix}.
\]

Define

\[
\boxed{m=\varepsilon_x+\varepsilon_y},
\qquad
\boxed{d=\varepsilon_x-\varepsilon_y},
\qquad
\boxed{r^2=d^2+\gamma_{xy}^2}.
\]

Let

\[
S=\sigma_x+\sigma_y,
\qquad
D_\sigma=\sigma_x-\sigma_y.
\]

The deformation-theory equations reduce exactly to

\[
\boxed{S=\frac{3m}{A+B}},
\]

\[
\boxed{D_\sigma=\frac{d}{A}},
\]

\[
\boxed{\tau_{xy}=\frac{\gamma_{xy}}{2A}}.
\]

Hence

\[
\boxed{\sigma_x=\frac12(S+D_\sigma)},
\qquad
\boxed{\sigma_y=\frac12(S-D_\sigma)}.
\]

For plane stress the von-Mises invariant is

\[
\bar\sigma^2
=\sigma_x^2-\sigma_x\sigma_y+\sigma_y^2+3\tau_{xy}^2
\]

which becomes

\[
\boxed{
\bar\sigma^2
=\frac{9m^2}{4(A+B)^2}
+\frac{3r^2}{4A^2}
}.
\]

Because `A=A(sigma_bar)`, the complete 2D material update has been reduced to **one scalar current-state equation**:

\[
\boxed{
F(\bar\sigma;m,r^2)
=\bar\sigma^2
-\frac{9m^2}{4[A(\bar\sigma)+B]^2}
-\frac{3r^2}{4A(\bar\sigma)^2}
=0.
}
\]

Once the nonnegative admissible `sigma_bar` root is known, the full plane-stress tensor follows algebraically from the boxed equations above.

This is not a structural material-point iteration. `F=0` defines the continuous constitutive current map and can be compiled in material-coordinate space before structural D15 integration.

---

## 4. Exact uniaxial-source recovery

For a uniaxial stress state

\[
\sigma_x=\bar\sigma,\qquad \sigma_y=\tau_{xy}=0,
\]

the 3D deformation-theory relation gives

\[
\varepsilon_x
=\frac{\bar\sigma}{E_s}+\psi(\bar\sigma),
\]

exactly reproducing the approved source curve.

Therefore

```text
UNIAXIAL_SOURCE_RECOVERY = EXACT BY CONSTRUCTION
```

No additional steel hardening parameter is introduced by the 2D lift.

---

## 5. Elastic degeneration check

If

\[
\psi(\bar\sigma)=0,
\]

then

\[
A=\frac{1+\nu_s}{E_s}.
\]

The map reduces to

\[
S=\frac{E_s}{1-\nu_s}m,
\qquad
D_\sigma=\frac{E_s}{1+\nu_s}d,
\qquad
\tau_{xy}=\frac{E_s}{2(1+\nu_s)}\gamma_{xy},
\]

and therefore

\[
\boxed{
\begin{bmatrix}
\sigma_x\\\sigma_y\\\tau_{xy}
\end{bmatrix}
=\frac{E_s}{1-\nu_s^2}
\begin{bmatrix}
1&\nu_s&0\\
\nu_s&1&0\\
0&0&(1-\nu_s)/2
\end{bmatrix}
\begin{bmatrix}
\varepsilon_x\\\varepsilon_y\\\gamma_{xy}
\end{bmatrix}
}.
\]

Thus

```text
PLANE_STRESS_ELASTIC_LIMIT = EXACT PASS
```

---

## 6. Consistent tangent by implicit differentiation

Let

\[
A'=\frac{dA}{d\bar\sigma}
=\frac32
\frac{\psi'(\bar\sigma)\bar\sigma-\psi(\bar\sigma)}{\bar\sigma^2}.
\]

For Ramberg-Osgood,

\[
\psi'=\frac{np}{f_y}\left(\frac{\bar\sigma}{f_y}\right)^{n-1}.
\]

The scalar constitutive equation derivative is

\[
\boxed{
F_{\bar\sigma}
=2\bar\sigma
+\frac{9m^2A'}{2(A+B)^3}
+\frac{3r^2A'}{2A^3}
}.
\]

Hence

\[
\boxed{
\frac{\partial\bar\sigma}{\partial m}
=\frac{9m}{2(A+B)^2F_{\bar\sigma}}
},
\]

\[
\boxed{
\frac{\partial\bar\sigma}{\partial d}
=\frac{3d}{2A^2F_{\bar\sigma}}
},
\]

\[
\boxed{
\frac{\partial\bar\sigma}{\partial\gamma_{xy}}
=\frac{3\gamma_{xy}}{2A^2F_{\bar\sigma}}
}.
\]

For any strain differential,

\[
dA=A'\,d\bar\sigma,
\]

\[
\boxed{
dS=\frac{3}{A+B}dm-\frac{3m}{(A+B)^2}dA
},
\]

\[
\boxed{
dD_\sigma=\frac1A dd-\frac{d}{A^2}dA
},
\]

\[
\boxed{
d\tau_{xy}=\frac1{2A}d\gamma_{xy}-\frac{\gamma_{xy}}{2A^2}dA
}.
\]

Using

\[
dm=d\varepsilon_x+d\varepsilon_y,
\qquad
dd=d\varepsilon_x-d\varepsilon_y,
\]

and

\[
d\sigma_x=\frac12(dS+dD_\sigma),
\qquad
d\sigma_y=\frac12(dS-dD_\sigma),
\]

the complete engineering tangent

\[
\boxed{
\mathbb C_t^{s,eng}
=\frac{\partial(\sigma_x,\sigma_y,\tau_{xy})}
{\partial(\varepsilon_x,\varepsilon_y,\gamma_{xy})}
}
\]

is obtained algebraically with no finite differences.

---

## 7. Material-only compiler variables

The 2D current map depends on the in-plane strain state only through

\[
m=\varepsilon_x+\varepsilon_y,
\qquad
r^2=(\varepsilon_x-\varepsilon_y)^2+\gamma_{xy}^2,
\]

plus the sign/direction information carried by `d` and `gamma` in the final stress reconstruction.

Therefore a compact finite analytic compiler can be constructed in invariant material coordinates such as

\[
\boxed{(m,r^2)}
\]

for the scalar functions

\[
\bar\sigma(m,r^2),\quad A(m,r^2),\quad 1/A,\quad1/(A+B),
\]

followed by algebraic stress reconstruction.

This is analogous in spirit to the concrete Cayley-Hamilton current-map compilation: the material compiler is generated in material coordinate space, not by structural-space sampling.

---

## 8. Compatibility with shell D15 integration

In the locked Nguyen field,

\[
m(X,Y,\eta),\quad d(X,Y,\eta),\quad\gamma(X,Y,\eta)
\]

are finite trigonometric-thickness polynomials. Once the invariant scalar steel functions above are represented by a finite analytic basis, the shell stresses and tangent contractions become finite analytic fields and close under general-D15 exact moments.

```text
FORMAL_STRUCTURAL_GAUSS = 0
FORMAL_SHELL_THICKNESS_QUADRATURE = 0
MATERIAL_COORDINATE_COMPILER_NODES = ALLOWED
STRUCTURAL_MATERIAL_POINTS = 0
```

---

## 9. Source-curve choice by steel grade

The 2D lift is deliberately independent of the final uniaxial source curve.

Source candidates already present in Sun Lipeng include:

- Ramberg-Osgood for inelastic-buckling range where plastic strain remains small;
- high-strength multilinear steel source with von-Mises/isotropic-hardening FE identity;
- ordinary-strength Yun-Gardner strain-hardening source.

Before production, the uniaxial source curve must be frozen by steel grade using material-source evidence only. In particular, Sun explicitly warns that the simple Ramberg-Osgood relation can overpredict stress once plastic strain becomes larger than the stated low-plastic-strain range; therefore it must not automatically be extrapolated to ultimate strain for every steel shell.

---

## 10. Scope/limitation of deformation theory

This current operator is appropriate to the NZ-SCCM architecture because it is path-independent and exactly reproduces monotonic uniaxial source behavior. It represents a deformation-theory approximation to multiaxial plasticity and is not identical to an incremental J2 flow-history model under strongly non-proportional cyclic loading.

The target structural problem is monotonic axial compression with a low-dimensional continuous halfwave. Its suitability must therefore be judged first by source-only material checks and structural-state proportionality diagnostics, not by fitting Pu.

---

## 11. Candidate freeze gates

Before promotion to the steel-shell production operator:

```text
G1 uniaxial source recovery = exact
G2 elastic plane-stress degeneration = exact
G3 stress symmetry / objectivity = pass
G4 tangent analytic differentiation = pass
G5 tangent finite-difference material-only audit = pass
G6 material-domain invariant compiler fidelity = pass
G7 coefficient simplicity / general-D15 compatibility = pass
G8 no structural Pu in coefficient generation = pass
G9 monotonic/proportional-state suitability audit = pass
```

If these gates pass, the operator can be inserted directly into the already-derived

\[
P_{sh},\quad R_{q,sh},\quad L,\quad K_{Z,sh}^{mat},\quad K_{Z,sh}^{geo}
\]

without modifying the locked concrete theory.
