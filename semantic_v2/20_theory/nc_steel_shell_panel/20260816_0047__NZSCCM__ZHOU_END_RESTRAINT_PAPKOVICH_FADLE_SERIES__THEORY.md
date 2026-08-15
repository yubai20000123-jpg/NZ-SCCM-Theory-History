# NZ-SCCM — Zhou transverse end-restraint Papkovich–Fadle series

**Timestamp:** 2026-08-16 00:47 +08:00  
**Identity:** classical elastic mixed-boundary closure; zero spatial numerical integration.

## 1. Problem carried forward from 00:16

The canonical one-halfwave FvK compatibility particular solution is retained. The exact side-free correction derived at 00:16 removes the lateral traction defect, but leaves an x-dependent loaded-end residual in

`epsilon_x=(Nx-nu Ny)/(E t)`.

For the actual Zhou loaded edges `ux=0`, and because the nonlinear `w_x` contribution vanishes on the loaded edge, the remaining transverse end condition is

`Nx-nu Ny=0` pointwise.

The 00:16 residual is denoted `H(t)`, with centered transverse coordinate

`t=(x-b/2)/c`, `c=b/2`, `-1<=t<=1`.

The present task is to construct a homogeneous biharmonic correction that is simultaneously:

1. traction-free on the lateral sides;
2. capable of cancelling the loaded-end transverse-strain residual;
3. self-equilibrated in the axial direction, so it does not alter the mean axial resultant;
4. analytically representable without spatial quadrature.

## 2. Even Papkovich–Fadle strip eigenfamily

Because the residual `H(t)` is even, use only the even strip family.

For a nonzero complex eigenvalue `lambda`, define

`F(t)=sin(lambda) cos(lambda t)-t cos(lambda) sin(lambda t)`.

This function is even. At `t=+/-1`,

`F(+/-1)=0` identically.

Its derivative at `t=1` is

`F'(1)=-lambda-0.5 sin(2 lambda)`.

Therefore the free-side derivative condition is satisfied when

`sin(2 lambda)+2 lambda=0`.

Thus the even eigenvalues are the nonzero complex roots

`sin(2 lambda_n)+2 lambda_n=0`.

For each mode,

`F_n(+/-1)=F_n'(+/-1)=0`.

With an Airy mode

`Phi_n=A_n F_n(t) Y_n(y)`,

lateral resultants are proportional to

`Nx ~ F_n`, `Nxy ~ F_n'`,

hence every mode satisfies

`Nx=Nxy=0` on `x=0,b` exactly.

The companion odd family satisfies `sin(2 lambda)-2 lambda=0`; it is not required here because the present end residual is even.

## 3. Finite physical-length symmetric end layer

Let the physical panel length be `a` and `c=b/2`. For equal transverse restraint at both physical loaded ends, choose

`Y_n(y)=cosh[lambda_n (y-a/2)/c] / cosh[lambda_n a/(2c)]`.

Then

`Y_n(0)=Y_n(a)=1`,

and

`Y_n'(a/2)=0`.

Also

`Y_n''=(lambda_n/c)^2 Y_n`.

Because `F_n` satisfies `(D_t^2+lambda_n^2)^2 F_n=0`, the product `F_n Y_n` is biharmonic:

`nabla^4(F_n Y_n)=0`.

Hence this is an admissible homogeneous Airy correction on the finite strip.

## 4. Loaded-end boundary operator

At a physical loaded end, the transverse strain condition is

`Nx-nu Ny=0`.

For one homogeneous mode,

`Nx=Phi_yy`, `Ny=Phi_xx`.

Multiplying the boundary operator by `c^2` gives

`B_n(t)=lambda_n^2 F_n(t)-nu F_n''(t)`.

Direct differentiation reduces this to

`B_n(t)=(1+nu) lambda_n^2 F_n(t)+2 nu lambda_n cos(lambda_n) cos(lambda_n t)`.

Therefore the formal mixed-boundary closure is

`H(t)+Re sum_{n=1}^infinity a_n B_n(t)=0`, `-1<=t<=1`.

Complex-conjugate eigenpairs and amplitudes combine to give a real Airy field.

The amplitudes `a_n` are not new physical membrane DOFs. They are boundary-closure coefficients fixed by the end residual.

## 5. Self-equilibrated character

The end-layer modes must not change the prescribed mean axial resultant. For one mode,

`Ny ~ F_n''(t)`.

Its transverse integral is

`int_{-1}^1 F_n''(t) dt = F_n'(1)-F_n'(-1)=0`.

Likewise the net shear contribution vanishes from the free-side derivative conditions.

Thus the PF correction redistributes the end reaction but carries zero additional mean axial resultant. The mean axial load remains the separate homogeneous Airy component.

## 6. Exact cosine-moment realization — no collocation

A finite coefficient-space reproduction with N complex eigenmodes uses `2N` exact moments:

`int_{-1}^1 [H(t)+Re sum_{n=1}^N a_n B_n(t)] cos(k pi t) dt=0`,

for `k=0,...,2N-1`.

This is NOT spatial collocation. All matrix entries are closed analytical moments.

Define

`I(lambda,k)=int cos(lambda t) cos(k pi t) dt`

on `[-1,1]`. Then

`I(lambda,k)=sin(lambda-k pi)/(lambda-k pi)+sin(lambda+k pi)/(lambda+k pi)`.

Further,

`int t sin(lambda t) cos(k pi t) dt = -dI/dlambda`.

Therefore

`M_F=lambda-moment(F_n)`

is evaluated as

`M_F=sin(lambda) I + cos(lambda) dI/dlambda`,

and

`M_B=(1+nu) lambda^2 M_F + 2 nu lambda cos(lambda) I`.

For a complex amplitude `a_n=u_n+i v_n`,

`Re[a_n M_B]=u_n Re(M_B)-v_n Im(M_B)`.

This yields a finite real linear system for `Re(a_n),Im(a_n)`.

## 7. Exact moments of the inherited end residual

Let

`chi=b/ell`, `z=pi chi`.

The 00:16 side-free correction is

`G(z t)=1-Az cosh(z t)+Bz z t sinh(z t)`

with

`Az=(z cosh z+sinh z)/(z+sinh z cosh z)`,

`Bz=sinh z/(z+sinh z cosh z)`.

Using `cos(2X)=-cos(pi t)`, the end residual can be written

`H(t)=-chi^2 [G+nu G'']-nu chi^4 cos(pi t)`.

Since

`G+nu G'' = 1 + Cg cosh(z t)+Bz(1+nu) z t sinh(z t)`,

where

`Cg=-Az(1+nu)+2 nu Bz`,

all required residual moments are closed.

For integer k,

`C_k(z)=int cosh(z t) cos(k pi t) dt`

is

`C_k(z)=2 z sinh(z) (-1)^k/[z^2+(k pi)^2]`.

Also

`int z t sinh(z t) cos(k pi t) dt = z dC_k/dz`.

The remaining constant and `cos(pi t)` moments are elementary orthogonality relations. No spatial quadrature is present.

## 8. First six even roots

The first six roots in the first quadrant are

```text
lambda1 =  2.1061961152453303 + 1.1253643058009303 i
lambda2 =  5.3562686986396302 + 1.5515743729126248 i
lambda3 =  8.5366824265759143 + 1.7755436735110402 i
lambda4 = 11.6991776128256544 + 1.9294044965527872 i
lambda5 = 14.8540599126380201 + 2.0468524623826670 i
lambda6 = 18.0049330081858026 + 2.1418907938875118 i
```

They are roots in coefficient space, not spatial sample points.

## 9. N=6 exact-moment coefficients

### Original Z6 geometry, chi=4/3, nu=.18

```text
a1= +0.335990069882670 +0.545806083164795 i
a2= +0.034715930748038 -0.180227429104083 i
a3= -0.003869117871152 +0.034997414869053 i
a4= -0.000564541486177 -0.003950311313662 i
a5= +0.000127391073756 +0.000184244296471 i
a6= -0.000004419861121 -0.000000446771897 i
```

### Original Z6 geometry, chi=4/3, nu=.30

```text
a1= +0.314675282455425 +0.511173974674342 i
a2= +0.038586556859290 -0.170924825255711 i
a3= -0.004287826415513 +0.033413507212593 i
a4= -0.000500421622451 -0.003798099158544 i
a5= +0.000121479620375 +0.000178490454236 i
a6= -0.000004276710854 -0.000000456201383 i
```

### AR2 geometry, chi=1, nu=.18

```text
a1= +0.101246004968101 +0.124848549912685 i
a2= +0.010746510623611 -0.056464764626457 i
a3= -0.001115914076303 +0.010655311654025 i
a4= -0.000174014620580 -0.001184074139134 i
a5= +0.000038076133210 +0.000054754858110 i
a6= -0.000001310842929 -0.000000130059714 i
```

### AR2 geometry, chi=1, nu=.30

```text
a1= +0.094589295068904 +0.113966239697886 i
a2= +0.011937994546650 -0.053541404758742 i
a3= -0.001241097143884 +0.010158117952506 i
a4= -0.000154452613524 -0.001136119881445 i
a5= +0.000036233073791 +0.000052922351460 i
a6= -0.000001265372232 -0.000000132550957 i
```

## 10. Exact-moment truncation convergence

For nu=.18, omitted cosine moments were checked analytically through k=24.

Original Z6, `chi=4/3`:

```text
N    max omitted moment    omitted/max|H moment|
2    1.20532532614e-2      6.46218917801e-3
3    3.18188073421e-3      1.70592244271e-3
4    4.97826937963e-4      2.66903198768e-4
5    5.28926545954e-5      2.83576834162e-5
6    4.59790404023e-6      2.46510424082e-6
```

AR2, `chi=1`:

```text
N    max omitted moment    omitted/max|H moment|
2    4.43388717805e-3      5.82951926698e-3
3    1.00981894261e-3      1.32767450901e-3
4    1.51798876186e-4      1.99579835458e-4
5    1.57606435686e-5      2.07215410888e-5
6    1.34959944364e-6      1.77440598813e-6
```

Enforced moments are solved to algebraic/high-precision linear-system tolerance. The N=6 field is a coefficient-space truncation certificate only; pointwise exactness is not claimed. The formal infinite PF series is the mixed-boundary closure object.

## 11. Physical end-layer overlap

At the panel midheight,

`Y_n(a/2)=1/cosh(lambda_n a/b)`.

Original Z6 physical `a/b=.75`:

```text
|Y1(center)|=4.13781180629e-1
|Y2(center)|=3.60145641398e-2
|Y3(center)|=3.31478603916e-3
|Y4(center)|=3.09288516647e-4
|Y5(center)|=2.90237019344e-5
|Y6(center)|=2.73179248701e-6
```

AR2 physical `a/b=2`:

```text
|Y1(center)|=2.96231495568e-2
|Y2(center)|=4.45280951104e-5
|Y3(center)|=7.69417132444e-8
|Y4(center)|=1.37801338356e-10
|Y5(center)|=2.50586394727e-13
|Y6(center)|=4.59350179773e-16
```

Thus the transverse end-restraint field overlaps strongly in squat original Z6, but is already small at the physical midheight of AR2. It is nevertheless retained analytically.

## 12. AR2 one-halfwave mapping

For AR2:

`a=24000 mm`, `b=12000 mm`, `m=2`, `ell=a/m=12000 mm=b`.

The FvK out-of-plane halfwave is periodic/representative, but the physical transverse end-restraint correction is global and symmetric about `y=a/2`.

Because `m=2`, one complete out-of-plane halfwave coincides exactly with the half-panel `0<=y<=a/2`. Therefore choose the production halfwave as:

- `y=0`: physical loaded end, transverse restraint applies;
- `y=ell=a/2`: physical midheight symmetry plane, `Y_n'=0`;
- do NOT impose `ux=0` at `y=ell`.

This preserves `ONE_CONTINUOUS_COMPLETE_HALFWAVE` without inventing an internal loaded boundary.

For general `m>2`, this argument does not make all halfwaves equivalent; further global condensation would be required. The present PASS is specific to the AR2 `m=2` mapping.

## 13. Scope of closure

This gate closes the **transverse loaded-end restraint correction** associated with the confirmed free-Poisson mismatch.

It does not claim that every in-plane finite-element boundary detail has been reduced to an identical continuum condition. In particular, the bottom `uy=0` versus top `uy=unset` condition has not been independently mapped as an additional Airy boundary family here.

Therefore:

```text
TRANSVERSE_END_RESTRAINT_PF_CLOSURE = FORMALLY_CLOSED
AR2_M2_ONE_HALFWAVE_END_LAYER_MAPPING = PASS
FULL_ZHOU_ALL_INPLANE_END_DOF_EQUIVALENCE = NOT_YET_PROVEN
```

The next step is to encode the periodic FvK field plus the PF boundary layer into the R10/N48/Cayley–Hamilton/D15 material operator without introducing spatial quadrature.
