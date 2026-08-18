# NZ-SCCM Case21 — R13 finite constructor zero-discretization trial calculation

**Date:** 2026-08-19  
**Identity:** execution smoke test of the R13 material-series replacement  
**Formal discretization:** NONE  
**Historical Pu / experimental comparator used in solve:** NO

## 0. Purpose

This calculation does one narrow thing: take a real Case21 specimen and execute the new finite R13 current-material constructor on a complete continuous specimen branch without any material series, finite prefix, spatial quadrature, grid, material point, or discrete oracle.

This is deliberately the exact unbuckled branch `q=0, alpha=0`, for which the continuous field becomes uniform and the full specimen integral reduces analytically to section area times the exact finite R10 stress. It is therefore a valid zero-discretization trial of the replacement constructor. It is **not** claimed to be the final nonlinear plate `Pu`, because the latter requires the nonuniform coupled `q,alpha` branch.

## 1. Case21 inputs

Representative-halfwave / section data:

```text
b = 1220 mm
t = 19.30 mm
fc = 21.23 MPa
eps0 = 0.00209
nu = 0.18
rho_sy = 0.00375
Es = 200000 MPa
fy = 530 MPa
```

R10 constants:

```text
kappa = 2.0005129533678754
rho_R = 0.1
xcr = rho_R/kappa = 0.04998717945397425...
eta = xcr/20 = 0.0024993589726987125...
H_R = 0.09799750427197301
U_R = 0.03
a_cc = 0.1072329249362415
```

## 2. Exact unbuckled continuous state

Set

\[
q=0,\qquad \alpha=0.
\]

Then the Nguyen second-order terms satisfy

\[
M=0,\qquad B=0,
\]

and the normalized physical strain field is uniform:

\[
e_x=\nu D,\qquad e_y=-D,\qquad \gamma=0.
\]

The equivalent R10 strain matrix is therefore exactly

\[
\boxed{\mathbf E=\operatorname{diag}(0,-D)}.
\]

Hence

\[
\lambda_1=0,\qquad \lambda_2=-D.
\]

The first principal stress is identically zero. The second principal stress is the exact scalar finite-R10 compression response.

## 3. Finite R13/R10 scalar evaluation

Define

\[
\Pi_\eta(z)=\frac{z^2(\sqrt{z^2+\eta^2}+z)}{2(z^2+\eta^2)}.
\]

For \(\lambda_2=-D\):

\[
c(D)=\Pi_\eta(D),\qquad t(D)=\Pi_\eta(-D).
\]

Compression primitive:

\[
C(D)=\frac{\kappa c}{1+(\kappa-2)c+c^2}.
\]

The R13 global three-branch tensile spline is evaluated at

\[
r_t(D)=\frac{t(D)}{x_{cr}},
\]

with

\[
u_R(r)=p_1(r)+A_3(r-1)_+^3+A_4(r-1)_+^4+A_5(r-1)_+^5+B_3(r-10)_+^3+B_4(r-10)_+^4+B_5(r-10)_+^5.
\]

For this compression branch, \(r_t\ll1\), but the same global formula is retained; no branch selector is used.

The exact normalized axial concrete stress is

\[
\boxed{
S_{yy}(D)
=-\kappa D-C(D)+\kappa c(D)+u_R(r_t(D))-\kappa t(D).
}
\]

Because the field is uniform, the complete continuous specimen integral is exact:

\[
\boxed{P_c(D)=-f_cbt\,S_{yy}(D)}.
\]

There is no spatial integration algorithm in this expression.

## 4. Reinforcement contribution

The longitudinal reinforcement strain is

\[
\varepsilon_s=D\varepsilon_0.
\]

Before yield,

\[
P_s(D)=\rho_{sy}btE_s\varepsilon_0D.
\]

The steel yield generalized compression is

\[
D_y=\frac{f_y}{E_s\varepsilon_0}
=1.2679425837320574\ldots
\]

Thus the total exact unbuckled-branch load before reinforcement yield is

\[
\boxed{P(D)=P_c(D)+\rho_{sy}btE_s\varepsilon_0D}.
\]

## 5. Continuous stationary point

The branch maximum is defined by the one-dimensional continuous equation

\[
\boxed{\frac{dP}{dD}=0}.
\]

This is a finite-dimensional root solve of the closed scalar formula above; it is not a spatial discretization.

The root is

\[
\boxed{D_*=1.0837948701065467}.
\]

At this state:

\[
\varepsilon_s=D_*\varepsilon_0
=0.002265131278522683<0.00265,
\]

so the reinforcement is still elastic.

Exact finite-R10 internal values:

```text
c = 1.0837905472648861
t = 1.4409446658147746e-6
t/xcr = 2.8826284690488011e-5
C = 0.9967722546204775
u_R = 2.8826284781500085e-6
Syy = -0.9967809025212059
```

Concrete stress:

\[
\sigma_{c,y}=f_cS_{yy}
=-21.1616585605252\ \text{MPa}.
\]

Concrete load:

\[
\boxed{P_c(D_*)=498.272412466126\ \text{kN}}.
\]

Reinforcement stress:

\[
\sigma_s=E_s\varepsilon_s
=453.026255704537\ \text{MPa}<530\ \text{MPa}.
\]

Reinforcement load:

\[
\boxed{P_s(D_*)=40.0010858130713\ \text{kN}}.
\]

Total exact unbuckled-branch stationary load:

\[
\boxed{P_*=538.273498279198\ \text{kN}}.
\]

## 6. Exact elastic halfwave reference from the same specimen

Using the already frozen Case21 initial bending quantities

\[
D_x=D_y=H=12{,}581{,}716.55789238\ \text{N mm},
\]

for the square representative halfwave \(b=\ell=1220\) mm,

\[
N_{cr}=\frac{\pi^2}{b^2}(D_x+2H+D_y),
\]

hence

\[
\boxed{P_{cr}=bN_{cr}=407.136279059126\ \text{kN}}.
\]

This is an exact closed Navier value and uses no spatial discretization.

The fact that

\[
P_{cr}<P_*
\]

shows only that the real plate problem cannot be represented by the uniform material branch alone; the coupled nonuniform \((D,q,\alpha)\) branch must be used for the final plate limit. No experimental or historical Pu value is used here.

## 7. Global-spline algebra check across all three scalar branches

This is a direct algebraic point-evaluation check of the **material function only**, not a spatial sampling validation.

For the same global R13 formula:

```text
r = 0.5  -> u_R = 0.064623752135986505
r = 5    -> u_R = 0.0710237445119991614
r = 12   -> u_R = 0.03
```

These equal the original first-, second-, and third-branch formulas respectively. This confirms that the single finite truncated-power expression executes the complete scalar law without a branch switch or material degree N.

## 8. Trial conclusion

```text
REAL_SPECIMEN = Case21
MATERIAL_SERIES = NONE
FINITE_PREFIX = NONE
SPATIAL_QUADRATURE = NONE
SPATIAL_GRID = NONE
MATERIAL_POINTS = NONE
DISCRETE_ORACLE = NONE
GLOBAL_R13_SPLINE_EXECUTION = PASS
COMPLETE_CONTINUOUS_UNBUCKLED_BRANCH = PASS
UNBUCKLED_STATIONARY_LOAD = 538.273498279198 kN
ELASTIC_HALFWAVE_REFERENCE = 407.136279059126 kN
FINAL_NONUNIFORM_PLATE_Pu = NOT CLAIMED BY THIS TRIAL
```

The next calculation should keep the same R13 finite current operator and move from `q=alpha=0` to the full continuous nonuniform `P(D,q,alpha), Rq(D,q,alpha), Ralpha(D,q,alpha)` system. No new material constructor is required.
