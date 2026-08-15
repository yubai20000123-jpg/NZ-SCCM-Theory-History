# NZ-SCCM — D=.50 directional moment-first certificate lock

**Timestamp:** 2026-08-15 22:35 +08:00  
**Identity:** fixed-D execution/certification only; no Pu; no D continuation in this stage.

## Frozen theory

```text
ONE_CONTINUOUS_COMPLETE_HALFWAVE
Nguyen second-order kinematics
R10 / N48-C1-MM / Cayley-Hamilton unchanged
General D15 exact structural moments unchanged
A0=a/500
membrane coordinates m=[c,p20,p02]^T
out-of-plane coordinate q only
N_formal_spatial_sampling=0
N_formal_spatial_quadrature=0
N_formal_spatial_subdomains=1
no Zhou/Winter calibration
no out-of-plane multimode production expansion
```

## Authorized implementation change

Only evaluation ordering/representation is changed.

The evaluator may retain the Cayley-Hamilton material pair `S=A I + B Y`, but it shall **not** first materialize the full directional stress products `Sxx*e_r`, `Syy*e_r` for every residual. Instead it contracts the already-computed coefficient pair directly with the low-order virtual-strain directions through exact Chebyshev product moments.

This is called `DIRECTIONAL_MOMENT_FIRST_V1`.

It is not a new material operator, not spatial collocation, and not a new integration rule.

## D=.50 engineering same-expression certificate

The parent material/compiler tolerance is restored:

```text
concrete coefficient pruning tolerance = 7e-7
steel local-cap degree = 24
steel polynomial tolerance = 1e-9
N48 interval = [-1.75,+0.45]
```

Certificate state:

```text
D=.50
q=0.008003063422252722
c=-0.07766034129851779
p20=-0.06065823792663306
p02=0.16525678113314005
P=37.68992902592416 MN
Pc=21.87837958508659 MN
Ps=15.81154944083757 MN
```

Residual decomposition, MN mm:

```text
Rq : concrete=-2978.793846244867  steel=+2978.447287284371  total=-0.346558960496
Rc : concrete=-13.305155663490    steel=+13.299616141564    total=-0.005539521926
R20: concrete=-3.985649836034     steel=+3.993339065648     total=+0.007689229614
R02: concrete=-12.567297517548    steel=+12.569776919116   total=+0.002479401568
```

Residual/internal-cancellation ratios:

```text
Rq  = 0.00581744 %
Rc  = 0.02082154 %
R20 = 0.09636847 %
R02 = 0.00986352 %
```

Gate definition for this engineering stage:

```text
same frozen operator/compiler tolerance
AND max_i |Ri|/(|Ri_concrete|+|Ri_steel|) < 0.1%
```

Result:

```text
D050_PARENT_TOLERANCE_DIRECTIONAL_EQUILIBRIUM_CERTIFICATE = PASS
THEOREM_LEVEL_ZERO_RESIDUAL_CERTIFICATE = NOT CLAIMED / NOT REQUIRED
Pu = NOT SOLVED
```

The engineering threshold is intentionally distinguished from theorem-level exact-zero certification; current project governance no longer treats ultra-tight remainder/error certificates as a hard production gate.

## Runtime gate

At the same `7e-7` concrete pruning level the new evaluator completed a certificate-state evaluation in about `36.7 s` in the current execution runtime, whereas the previous full stress-field expansion had exceeded the `90 s` execution window near the augmented state.

Therefore:

```text
D050_REPRESENTATION_RUNTIME_GATE = CLEARED_FOR_CURRENT_ENGINEERING_GATE
```

This does **not** mean all dense high-order fill-in has been eliminated. `buildS(K1,K2)` remains dense. The gain comes from eliminating unnecessary final stress-direction products and contracting directly into exact moments.

## Interpretation of P

The certificate load is a **fixed-D state resultant**, not Pu. The only valid same-D comparison is:

```text
parent D+q+c at D=.50      P=37.3451401318 MN
augmented certificate D=.50 P=37.6899290259 MN
change = +0.3447888941 MN = +0.92325%
```

The historical old reduced-branch `Pu≈37.50943 MN` occurred at a different state/branch and must not be compared as if it were the same D=.50 quantity.

## Next allowed execution

```text
D055_AUGMENTED_DIRECTIONAL_MOMENT_FIRST_CONNECTED_CHECKPOINT
```

Continue only the same q,c,p20,p02 system with the certified directional evaluator. Do not infer Pu until a connected D-path is established.