# NZ-SCCM — AR2 boundary-admissible D15 Ritz lift from PF/FvK to current material

**Timestamp:** 2026-08-16 01:02 +08:00

## 1. Why a kinematic lift is required

The 00:47 PF/Airy solution is an elastic boundary-value solution. In nonlinear concrete/steel it is invalid to impose the elastic Airy stress field directly. The material chain must remain

`continuous displacement/strain -> R10/N48 current material map -> stress -> exact generalized virtual work`.

Therefore PF is used as an **elastic target/limit**, not as a nonlinear stress ansatz.

## 2. AR2 one-halfwave coordinates

For the requested long-aspect Z6 object

```text
a=24000 mm
b=12000 mm
m=2
ell=a/m=12000 mm=b
```

use the physical lower half-panel, which is one complete out-of-plane halfwave:

`0<=x<=b`, `0<=y<=ell=a/2`.

Define

`X=pi x/b`, `Y=pi y/ell`, hence `X,Y in [0,pi]`.

The out-of-plane field remains

`w0=A0 sin X sin Y`, `wa=A sin X sin Y`.

Let

`S=A^2+2 A0 A`,

and use the current normalized geometric coefficient

`M=pi^2/eps0*(q0 q + q^2/2)`.

Because `S/b^2=q^2+2q0q`, the physical coefficient `Gamma=pi^2 S/b^2` satisfies

`Gamma/eps0 = 2 M`.

## 3. D15-compatible boundary-admissible in-plane basis

The PF hyperbolic/complex-root modes are not inserted directly. Instead construct an integer-trigonometric displacement Ritz lift on the one-halfwave domain.

For transverse displacement corrections, use

`u_rs=(b/pi) U_rs cos(r X) [1-cos(s Y)]`,

with odd transverse index

`r=1,3,5,...`, `s=1,2,3,...`.

These modes satisfy the physical-end essential condition exactly:

`u_rs(x,0)=0`.

At the physical midheight interface `Y=pi`, their longitudinal derivative is zero because `sin(s pi)=0`; this is consistent with the symmetric transverse end-restraint field and does **not** impose `ux=0` at the internal interface.

For the symmetric axial correction associated with this transverse-restraint subproblem, use

`v_rs=(b/pi) V_rs cos(r X) sin(s Y)`,

with even transverse index

`r=0,2,4,...`, `s=1,2,3,...`.

These correction modes vanish at `Y=0,pi`; the mean axial shortening remains carried by the external loading coordinate D.

The associated membrane strain modes are

### u-mode

`ex=-r U_rs sin(rX)[1-cos(sY)]`,

`ey=0`,

`gxy= s U_rs cos(rX) sin(sY)`.

### v-mode

`ex=0`,

`ey= s V_rs cos(rX) cos(sY)`,

`gxy=-r V_rs sin(rX) sin(sY)`.

Every component is a finite integer trigonometric polynomial. Hence every finite truncation belongs exactly to the unchanged General-D15 algebra

`sum c_prus sin^p X cos^r X sin^u Y cos^s Y`.

No new spatial quadrature family is introduced.

## 4. Complete nonlinear strain representation

Let the normalized membrane-coordinate vector be `r=[U_rs/eps0,V_rs/eps0]`.

The mid-surface strain is written

`epsilon0*(D,q,r) = epsilon_D(D) + epsilon_g(q,q0) + sum_j r_j B_j`,

where `B_j` are the compatible strain modes above and `epsilon_g` is the Nguyen/FvK second-order geometric source.

Through thickness the existing Nguyen curvature term is added unchanged. The same displacement field is used by concrete, face steel and any retained longitudinal web/PBL steel phase.

For each phase p,

`sigma_p = M_p(epsilon_p)`

is evaluated by the existing current material operator; no PF elastic stress is reused.

The membrane generalized residuals are

`R_j(D,q,r)=sum_p integral_Vp sigma_p : B_j dV = 0`.

The out-of-plane residual remains the current virtual-work residual at fixed `r`:

`Rq=sum_p integral sigma_p : (partial epsilon/partial q)|_r dV`.

Because `R_j=0`, the envelope theorem means no explicit `dr/dq` term is needed in the first derivative of the condensed potential. Consistent tangent coupling still requires the ordinary Jacobian blocks `dRj/drk`, `dRj/dq`, `dRq/drj`.

## 5. Elastic-limit condensation

For an isotropic plane-stress elastic reference, define the dimensionless energy bilinear form

`<e,f>_nu = int [ex_e ex_f + ey_e ey_f + nu(ex_e ey_f+ey_e ex_f) + (1-nu)/2 g_e g_f] dX dY`.

For a finite Ritz space with basis `B_j`, the stationary coordinates satisfy

`K r = - f_D D - f_G Gamma/eps0`,

where

`K_jk=<B_j,B_k>`,

`(f_D)_j=<B_j,e_D>`,

`(f_G)_j=<B_j,g_G>`.

Thus

`r = c_D D + c_G Gamma/eps0 = c_D D + 2 c_G M`,

with

`c_D=-K^-1 f_D`, `c_G=-K^-1 f_G`.

These elastic coefficients are a **verification result only**. In nonlinear R10/N48 they are not frozen; every `r_j` is re-solved from current generalized equilibrium.

## 6. Why the complete elastic limit is PF/FvK

The Ritz functions satisfy the transverse loaded-end essential condition and span the symmetry class by integer trigonometric expansion. The lateral in-plane sides are not assigned displacement essential conditions; their traction conditions are natural conditions of the stationary energy problem.

The complete Ritz space is therefore a conforming displacement formulation of the same linear-elastic membrane minimization problem whose stress formulation is the FvK/Airy/Papkovich-Fadle mixed-boundary solution.

The elastic membrane energy is strictly convex modulo removed rigid motions. By uniqueness of the minimizer,

`complete conforming Ritz displacement solution = PF/Airy stress solution`.

This is the required elastic-limit equivalence. It does not require the PF hyperbolic functions themselves to be members of a finite D15 array.

## 7. Exact coefficient-space integration

All finite-Ritz stiffness/load coefficients are products of integer sines/cosines. The reproduction implementation evaluates them through exact exponential antiderivatives

`int_0^L exp(i k theta)dtheta = (exp(i k L)-1)/(i k)`

with the `k=0` analytic limit `L`.

This is coefficient-space exact integration, not spatial sampling or quadrature.

For `nu=.18`, square AR2 halfwave, equal truncations R=S give the recorded minimized dimensionless energy coefficients:

```text
R=S  nmem   Q_GG             Q_DD             Q_DG
1      2    0.710327899673   9.716401029828  -1.359305267256
2      8    0.380985323731   9.661181203174  -1.280790283542
3     18    0.338757150201   9.639425364487  -1.257398206363
4     32    0.318834041670   9.628042047630  -1.246067137428
5     50    0.307201717849   9.621103682835  -1.239421762215
6     72    0.299568422262   9.616453853076  -1.235062292357
8    128    0.290150329916   9.610639322927  -1.229696366445
10   200    0.284558250341   9.607163461818  -1.226522139050
12   288    0.280851744614   9.604857758524  -1.224424967309
```

`Q_GG>0` at every truncation, consistent with the already-proven positive classical postbuckling membrane stiffness.

For the pre-buckling D forcing, the limiting value lies between the fully free-Poisson and fully restrained references:

`Q_DD,free=(1-nu^2) pi^2`,

`Q_DD,restrained=pi^2`.

At R=S=12, `Q_DD=9.604857758524`, which is physically between those bounds.

## 8. Direct PF-to-D15 versus Ritz lift

Two distinct statements are now fixed:

```text
DIRECT finite PF hyperbolic basis -> current finite D15 array = NOT CLOSED
PF/FvK boundary problem -> conforming integer-trig Ritz lift -> General D15 = CLOSED
```

The second route changes neither the material operator nor General D15. It only changes the in-plane kinematic basis from the retired low-rank `c/p20/p02` constructions to a systematically boundary-admissible family.

## 9. Remaining production issues

This theory gate does **not** yet release a nonlinear Pu because:

1. the current reduced R10/N48 implementation is coded for the historical low-dimensional D-q(/c) strain algebra and has not yet been generalized to an arbitrary membrane-coordinate vector `r` with odd/even integer harmonics;
2. no production membrane truncation rank has been frozen; R=S=4,6,8,... are coefficient-space convergence levels, not spatial grids;
3. Zhou's bottom-edge `uy=0` versus top `uy=unset` asymmetry has not yet been independently proven to be a pure axial datum under the one-halfwave reduction. Therefore `FULL_ZHOU_ALL_INPLANE_END_DOF_EQUIVALENCE` remains open.

No new Pu is authorized at this stage.