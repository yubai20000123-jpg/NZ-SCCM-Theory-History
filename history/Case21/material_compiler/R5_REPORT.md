# NZ-SCCM Material Analytic Compiler — Case21 Envelope Gate R5

## 0. Verdict

R5 keeps `M(epsilon)`, `L_P`, `L_R` and D15 unchanged. It executes the R4 next gate up to the point that can be proven without hiding a new numerical integration.

**PASS:** recover a source-backed Case21 `(D,q)` regression search contract; generate a closed-form kinematic reachability certificate; generate one material-only adaptive MSAC object from that certificate; verify material stress+tangent; show an explicit nonlinear `compile -> substitute -> D15 -> P,R_A` component ledger with zero formal spatial quadrature.

**OPEN:** the full N600 factorized `U/C/T/T8` operator has not yet been contracted through D15. A naive nested sparse expansion exhibited expression swell and was stopped rather than replaced by Gauss integration or a state-dependent support mask. Therefore no new Case21 limit point and no Swartz24 batch are released in R5.

## 1. Case21 search contract recovered from the historical solver

The historical root scan used

`D in [0.60,0.78]` and, for every D, searched the first `R_A=0` root in `q in [0.0001,0.006]` using 120 bracketing samples. R5 freezes this only as the **Case21 regression search contract**. It is not a material physical domain and is not a Swartz24 production contract.

## 2. Analytic domain certificate

With `q>=0`,

`Cm(q)=pi^2/eps0*(q0*q+q^2/2)`, `Cb(q)=pi^2/(2 eps0)*(t/b)q`.

At the contract upper q,

`Cm_max=0.155835858965`, `|Cb|_max=0.2241156541`.

Using the exact cancellation of the membrane D term in `X11`, elementary trigonometric bounds, and the 2x2 Gershgorin bound,

`X11 in [-0.273311773292,0.434365782144]`,

`X22 in [-1.05331177329,-0.165634217856]`,

`|X12| <= 0.222944592238`,

hence the entire normalized principal-strain field reachable by the Case21 regression solver is certified inside

`x in [-1.27625636553,0.657310374381]`.

No `(X,Y,zeta)` points are used to obtain this interval.

## 3. R5 adaptive compiler map

The old fixed material interval is not reused. The map landmarks are rebuilt from this certificate and from the material law itself.

The zero-strain gate lies at normalized coordinate `s0=0.660052916295`. Its rational low-order location is `21/32`, hence the finite beta map uses `B_{21,11}`.

The tension natural coordinate reaches `t_max=0.657303246798` (plus a compiler-only 1% guard). The source material has two intrinsic tension landmarks: `r=1` and `r=10`, i.e. `t=xcr` and `t=10*xcr`. Their normalized positions are `0.0752959263874` and `0.752959263874`; R5 uses two finite beta lenses `B_{2,25}` and `B_{3,1}`.

Orders: gate `N=600`, smooth Saenz compression `N=18`, tension and `T^8` `N=600`. `U` is reassembled from the same compiled factors; it is not independently fitted.

### Material scalar qualification

|quantity|max abs|RMS|P99 abs|
|---|---:|---:|---:|
|U|1.96912e-07|3.88667e-08|1.14084e-07|
|C|5.12489e-06|2.00152e-07|6.92857e-07|
|T|5.06628e-05|2.00034e-06|6.86041e-06|
|Uprime|0.00385961|6.18064e-05|0.000305028|
|Cprime|0.0114951|0.000499263|0.0018943|
|Tprime|0.113627|0.00494117|0.0189093|

Full 2D principal operator audit: stress RMS `1.04309e-06`, stress max `5.05465e-05`; consistent-tangent relative RMS `0.139812%`, tangent max `0.107459`. This audit lives entirely in material-coordinate space.

## 4. Visible proof that the formal operation is still integration, not spatial summation

For readability R5 prints a degree-8 Chebyshev compiler for the **loading-direction Saenz compression component** at the Case21 check state. This is a transparent component ledger, not the full 2D production operator.

`c=D-Cm sin^2X cos^2Y-Cb sinX sinY zeta`,

`c_,q=-Cmq sin^2X cos^2Y-Cbq sinX sinY zeta`.

The finite material compiler gives

`psi_hat_c(c)=sum_(n=0)^8 p_n c^n`.

Then the formal quantities are literally

`I_P=sum p_n * D15[c^n]`,

`I_R=sum p_n * D15[c^n c_,q]`.

The first coefficients are `0.0072034482, 1.9137936, 0.43748634, -3.157179, 1.4653457`; the remaining four are stored in the JSON/CSV ledger.

For example

`D15[1]=2*pi^2`,

and the odd-through-thickness pieces vanish because `int_-1^1 zeta^(2m+1) dzeta=0` exactly. Every higher term is evaluated by the same finite multinomial/Beta-function moments.

The degree-8 formal component result is

`I_P=18.4972546608`, `I_R=-99.5799331042`

with **formal spatial quadrature count = 0**.

For audit only, Gauss integration of the original uncompiled component gives `I_P=18.4972546608`, `I_R=-99.5799331041`; relative differences are `-2.180e-13` and `2.903e-13`. Those audit values are not used to produce the formal result.

## 5. Why the full structural gate is intentionally still OPEN

The R5 material object itself is finite and well qualified. The remaining problem is not the material law or the material domain. It is the **adapter** from a high-order nested factorized compiler to D15.

A naive spatial sparse expansion of the nested tension map recreated expression swell: even a low outer truncation made the second tension-map composition exceed the prototype time budget. R5 therefore stops. It does **not** solve that by reintroducing spatial Gauss points, and it does not promote a support mask into the theory.

The next mathematical task is to derive a target-functional contraction/recurrence that takes the finite nested material factor graph directly to `L_P` and `L_R` moments without expanding the entire intermediate stress field.

Until that passes: new Case21 `P_u` = not authorized; Swartz24 = not authorized.
