# 2026-10-04 steel mean-compatibility repair R02

Branch: `diagnostic/20261004-analytic-ninecurve-attempt`

Status: **the exact BOTTOM no-root contradiction in R01 is repaired at the mean-compatibility level.** This file does not yet claim final nine-specimen (P(w)) curves; it establishes the corrected steel closure that the combined-Mises evaluator must use next.

## 1. What is revoked

The following R01 reinterpretation is revoked:

[
R_{A,E}^{pm}
=
rac{Deltaarsigma_{ell,E}^{pm}}{E_s}
-s_pm C_{GL}^{pm}(w_0A+wA_0^pm+wA)=0,
]

when (Deltaarsigma_{ell,E}) is simultaneously identified with the always-compressive-positive Yun mean-stress formula.

For BOTTOM (s_-=-1), (A_0>0,w>0,Age0), this makes every term nonnegative and gives (R^-_{A,E}>0) identically. R01 preserved this exact contradiction as a stop certificate.

## 2. Restore the exact whole-face mean compatibility

The whole-face kinematics gives

[
ar e_{s,kin}^{pm}
=
e_U^pm(w)
+s_pm C_{GL}^pm(w_0A^pm+wA_0^pm+wA^pm)
+C_{LL}^pm[2A_0^pm A^pm+(A^pm)^2].
]

The Yun mean strain gives

[
ar e_{s,Yun}^{pm}
=
rac{arsigma_s^pm}{E_s}
+C_{LL}^pm[2A_0^pm A^pm+(A^pm)^2].
]

The (C_{LL}) terms cancel exactly. Therefore the admissible mean equation is

[
oxed{
R_A^pm(A,e;w)
=
rac{arsigma_{s,EP}^pm(A,e)}{E_s}
-e_U^pm(w)
-s_pm C_{GL}^pm(w_0A+wA_0^pm+wA)
=0.
}
]

The elastic predictor is the special case (e=A).

This is a **total mean stress** equation. It must not be renamed as a local-only mean increment equation.

## 3. Elastic predictor and plastic-corrected mean stress

For (R=A_0+A),

[
oxed{
arsigma_{s,EP}(A,e)
=
rac{pi^2E_st_s^2}{12(1-
u_s^2)b_*^2}
left[
k_{cr}rac{e}{A_0+A}
+
k_p(1-
u_s^2)
rac{2(A_0+A)e-e^2}{t_s^2}
ight].
}
]

When (e=A), this reduces to the Yun elastic mean-stress curve.

For the current nine-specimen family:

[
N=m=4,qquad a_h=2b,qquad eta_*=8,
]

[
k_{cr}=rac{59}{3}=19.6666666666667,
qquad
k_p(8,4)=77.9807266435986.
]

## 4. Keep the good part of the latest global+local correction without double counting

The latest reply was correct that yielding must be checked on the **combined** global+local stress field. The mistake was only the mean-stress split.

Write the R06 field as mean plus zero-mean redistribution:

[
S_x=arsigma_x+widetilde S_x,qquad
S_y=arsigma_y+widetilde S_y,qquad
T_{xy}=widetilde T_{xy}.
]

All seven R06 harmonic terms have zero whole-period mean. Therefore a no-double-count total field can be constructed as

[
oxed{
sigma_y^{tot,pm}
=
sigma_{y,g}^{pm}
-langlesigma_{y,g}^{pm}angle
+arsigma_{s,EP}^{pm}(A,e)
+widetilde S_y^pm(A,e)
}
]

and, because the current one-parameter Yun closure has no independent transverse mean equation,

[
oxed{
sigma_x^{tot,pm}
=
sigma_{x,g}^{pm}
+widetilde S_x^pm(A,e),
}
]

[
oxed{
	au_{xy}^{tot,pm}
=
	au_{xy,g}^{pm}
+widetilde T_{xy}^pm(A,e).
}
]

Thus

[
langlesigma_y^{tot,pm}angle
=
arsigma_{s,EP}^{pm}
]

exactly. The Yun mean stress is **not added on top of** the global mean stress.

The local redistribution uses the R06 seven-harmonic coefficients with

[
Q_e=2(A_0+A)e-e^2
]

in place of the purely elastic amplitude-square difference. In particular the signed shear is

[
widetilde T_{xy}
=
-k_xk_ysin	heta_xsin	heta_y
left[
A_{11}
+4A_{12}cos	heta_y
+4A_{21}cos	heta_x
ight].
]

## 5. Correct combined-Mises closure

For a trial (e=A),

[
Phi^{pm}
=
(sigma_x^{tot,pm})^2
-sigma_x^{tot,pm}sigma_y^{tot,pm}
+(sigma_y^{tot,pm})^2
+3(	au_{xy}^{tot,pm})^2.
]

If

[
Phi_{max}^{pm}(A,e=A)le f_y^2,
]

the elastic predictor is accepted.

If it exceeds (f_y^2), (A,e) are determined by

[
oxed{
egin{cases}
R_A^pm(A,e;w)=0,\
Phi_{max}^{pm}(A,e;w)-f_y^2=0,
end{cases}
qquad 0le e<A.
}
]

Here (e) is a constitutive/algebraic condensed variable, not a new structural degree of freedom.

The already-proved tangent-half-angle/resultant construction remains applicable to (Phi_{max}), so production evaluation is still finite algebraic candidates, not a 2D optimizer.

## 6. Elastic predictor root audit — nine specimens

The following audit uses the exact restored mean compatibility and the elastic UHPC surface-average strain implied by the current trial field. It is deliberately only an **elastic predictor/root-existence audit**; rows where the resulting mean stress already exceeds (f_y) must proceed to the combined-Mises corrector.

| q=w/b | Case | A+ / mm | A- / mm |
|---:|---|---:|---:|
|0.001|BH005|0.0581100|0.0586717|
|0.001|BH010|0.1136342|0.1157428|
|0.001|BH020|0.2119355|0.2188833|
|0.001|BH032|0.3051868|0.3186922|
|0.001|BH050|0.4052171|0.4275201|
|0.001|BH060|0.4466902|0.4731958|
|0.001|BH070|0.4813934|0.5116865|
|0.001|BH085|0.5245032|0.5598310|
|0.001|BH100|0.5603634|0.6000806|
|0.005|BH005|1.4251010|1.4402832|
|0.005|BH010|1.4259723|1.4548202|
|0.005|BH020|1.4376818|1.4901666|
|0.005|BH032|1.4668529|1.5426448|
|0.005|BH050|1.5364172|1.6395608|
|0.005|BH060|1.5865019|1.7017579|
|0.005|BH070|1.6436941|1.7692465|
|0.005|BH085|1.7412442|1.8793207|
|0.005|BH100|1.8510074|1.9986446|
|0.010|BH005|1.8082877|1.8324343|
|0.010|BH010|1.8033052|1.8499411|
|0.010|BH020|1.8274925|1.9135511|
|0.010|BH032|1.9075946|2.0312594|
|0.010|BH050|2.1080823|2.2711006|
|0.010|BH060|2.2510160|2.4288428|
|0.010|BH070|2.4111465|2.5998724|
|0.010|BH085|2.6766391|2.8759970|
|0.010|BH100|2.9652467|3.1701248|
|0.020|BH005|2.0295390|2.0725695|
|0.020|BH010|2.0481192|2.1303349|
|0.020|BH020|2.1843198|2.3292748|
|0.020|BH032|2.4821238|2.6754236|
|0.020|BH050|3.1017697|3.3287838|
|0.020|BH060|3.5002974|3.7338848|
|0.020|BH070|3.9230258|4.1580617|
|0.020|BH085|4.5879440|4.8190524|
|0.020|BH100|5.2775201|5.5002163|

Therefore the exact BOTTOM no-root defect is gone over all audited cases and both faces.

## 7. BH050 high-deflection audit

At

[
w=56.05 {m mm}
quad (q=0.02242	ext{ approximately}),
]

the elastic-predictor roots are

[
A^+_{tr}=3.3558323319 {m mm},
qquad
A^-_{tr}=3.5903853404 {m mm}.
]

The corresponding Yun elastic mean stresses are

[
arsigma_{s,E}^+=596.4684 {m MPa},
qquad
arsigma_{s,E}^-=657.9992 {m MPa},
]

well above (f_y=355) MPa. Therefore this state is **not** an admissible final steel state; it proves that the next production step must solve the combined-Mises (A,e) closure, not clip the mean stress and not accept the elastic roots.

## 8. Execution state after R02

Passed:
- total mean compatibility identity restored;
- TOP/BOTTOM parity restored;
- scalar roots exist for both faces over the nine-specimen elastic-predictor audit;
- global stress is retained in the Mises capacity check;
- Yun mean stress is not double counted.

Still to execute before nine final curves:
- instantiate the combined global + zero-mean-R06 finite trigonometric stress field;
- evaluate (Phi_{max}) by finite algebraic candidates/resultants;
- solve the two-equation ((A,e)) closure for each face;
- couple to the already locked UHPC one-parameter evaluator;
- sweep (w) and save every curve point ledger.

No FEM (P_u), FEM (q), or fitted parameter is used in this repair.
