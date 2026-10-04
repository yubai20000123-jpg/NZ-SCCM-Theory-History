# 2026-10-04 combined-Mises corrector feasibility audit R03

Branch: `diagnostic/20261004-analytic-ninecurve-attempt`

## Status

R02's **total mean compatibility repair remains valid**. However, the proposed post-yield closure

[
R_A^pm(A,e;w)=0,
qquad
Phi_{max}^pm(A,e;w)=f_y^2,
qquad 0le e<A,
]

does **not** possess a physical continuation branch immediately after first yield for the nine-specimen family.

This is a direct numerical feasibility result, not a new gate.

## 1. R02 Mises field correction retained in this audit

R02 correctly restored total mean compatibility, but its no-double-count Mises field omitted the explicit pointwise global-local cross-strain fluctuation.

For total geometric amplitude (A),

[
G^pm=w_0A+wA_0^pm+wA.
]

The GL strains are

[
Deltaarepsilon_{x,GL}^pm
=s_pm G^pmphi_{g,x}H_{,x}^pm,
]

[
Deltaarepsilon_{y,GL}^pm
=s_pm G^pmphi_{g,y}H_{,y}^pm,
]

[
Deltagamma_{xy,GL}^pm
=s_pm G^pm
left(
phi_{g,x}H_{,y}^pm+
phi_{g,y}H_{,x}^pm
ight).
]

To avoid adding a second mean stress on top of the Yun total mean stress, the combined-Mises audit uses only the zero-mean GL fluctuation:

[
Deltaoldsymbolsigma_{GL}^{circ,pm}
=
mathbf C_s
left[
Deltaoldsymbolarepsilon_{GL}^{pm}
-
leftlangle
Deltaoldsymbolarepsilon_{GL}^{pm}
ightangle
ight].
]

Therefore

[
leftlangle Deltaoldsymbolsigma_{GL}^{circ,pm}ightangle=0.
]

The total trial field used in the audit is

[
sigma_y^{tot,pm}
=
sigma_{y,g}^{pm}
-langlesigma_{y,g}^{pm}angle
+arsigma_{s,EP}^pm
+widetilde S_y^pm
+Deltasigma_{y,GL}^{circ,pm},
]

[
sigma_x^{tot,pm}
=
sigma_{x,g}^{pm}
+widetilde S_x^pm
+Deltasigma_{x,GL}^{circ,pm},
]

[
	au_{xy}^{tot,pm}
=
	au_{xy,g}^{pm}
+widetilde T_{xy}^pm
+Delta	au_{xy,GL}^{circ,pm}.
]

Hence the axial whole-face mean remains exactly

[
langlesigma_y^{tot,pm}angle
=
arsigma_{s,EP}^pm.
]

## 2. Literal current-lock first-yield audit

The following values are obtained by:
1. solving the repaired elastic predictor (R_A(A,e=A;w)=0);
2. restoring global + R06 + zero-mean GL stress;
3. locating the first (q=w/b) for which (maxsigma_{VM}=355) MPa.

The phase grid used here is **only an independent diagnostic evaluator**. It is not the production definition; the production evaluator remains the tangent-half-angle/resultant finite-candidate construction already derived.

| case | face | q_y | w_y / mm | A_y / mm | mean sigma_y at yield / MPa |
|---|---|---:|---:|---:|---:|
| BH005 | TOP | 2.7248e-5 | 0.006812 | 0.000849 | 353.707 |
| BH005 | BOTTOM | 2.7360e-5 | 0.006840 | 0.000854 | 356.078 |
| BH010 | TOP | 1.1223e-4 | 0.056117 | 0.007267 | 352.120 |
| BH010 | BOTTOM | 1.1321e-4 | 0.056607 | 0.007378 | 357.000 |
| BH020 | TOP | 5.09395e-4 | 0.509395 | 0.080295 | 346.834 |
| BH020 | BOTTOM | 5.21369e-4 | 0.521369 | 0.084344 | 357.953 |
| BH032 | TOP | 1.68943e-3 | 2.703087 | 0.627214 | 325.282 |
| BH032 | BOTTOM | 1.79070e-3 | 2.865118 | 0.708120 | 345.591 |
| BH050 | TOP | 5.92280e-3 | 14.807005 | 1.663729 | 257.005 |
| BH050 | BOTTOM | 7.07197e-3 | 17.679934 | 1.932751 | 299.209 |
| BH060 | TOP | 7.73136e-3 | 23.194072 | 1.970294 | 216.015 |
| BH060 | BOTTOM | 8.69194e-3 | 26.075829 | 2.255149 | 251.887 |
| BH070 | TOP | 8.86772e-3 | 31.037031 | 2.246130 | 187.984 |
| BH070 | BOTTOM | 9.74458e-3 | 34.106043 | 2.560330 | 220.797 |
| BH085 | TOP | 9.91516e-3 | 42.139433 | 2.661090 | 162.482 |
| BH085 | BOTTOM | 1.07546e-2 | 45.707068 | 3.020279 | 192.335 |
| BH100 | TOP | 1.05465e-2 | 52.732414 | 3.086967 | 147.824 |
| BH100 | BOTTOM | 1.13925e-2 | 56.962327 | 3.489214 | 175.642 |

The first-yield event above is **not** automatically (P_u).

## 3. Direct post-yield corrector feasibility test

For every specimen, take TOP at

[
q=1.05q_y^{TOP}.
]

For each fixed geometric amplitude (Age A_{tr}), first solve the Mises boundary for the maximum recoverable amplitude (e_y(A)), then evaluate

[
R_A(A,e_y(A);w).
]

The result is:

| case | q=1.05 q_y | A_tr / mm | max R_A over feasible scan | min R_A over feasible scan |
|---|---:|---:|---:|---:|
| BH005 | 2.861e-5 | 0.000892 | -8.5e-5 | -9.1e-5 |
| BH010 | 1.178e-4 | 0.007651 | -8.2e-5 | -1.08e-4 |
| BH020 | 5.348e-4 | 0.085523 | -7.2e-5 | -3.22e-4 |
| BH032 | 1.774e-3 | 0.665421 | -5.7e-5 | -8.87e-4 |
| BH050 | 6.219e-3 | 1.701102 | -7.2e-5 | -8.33e-4 |
| BH060 | 8.118e-3 | 2.019253 | -1.21e-4 | -4.62e-4 |
| BH070 | 9.311e-3 | 2.310844 | -1.72e-4 | -4.11e-4 |
| BH085 | 1.0411e-2 | 2.752061 | -2.70e-4 | -2.70e-4 |
| BH100 | 1.1074e-2 | 3.204936 | -3.98e-4 | -3.98e-4 |

No specimen produces a zero of the proposed two-equation corrector.

For the wider plates, increasing (A) eventually makes even (e=0) exceed the combined Mises surface, so the feasible (e)-interval disappears completely.

## 4. Mechanical reason

Before yield, the mean identity is

[
rac{arsigma_s}{E_s}
=
e_U+sC_{GL}(w_0A+wA_0+wA).
]

After yield, total axial shortening cannot remain equal to elastic strain (arsigma_s/E_s). A new axial plastic-strain part is required:

[
e_U+sC_{GL}(w_0A+wA_0+wA)
=
rac{arsigma_s}{E_s}
+ararepsilon_{p,y}.
]

The quantity

[
A_P=A-e
]

is a permanent **local out-of-plane amplitude**, not a uniform axial plastic strain. Therefore it cannot absorb the missing mean shortening.

This is why reducing (e) to stay on the Mises surface drives (R_A) negative instead of closing it.

## 5. S0/S1 gate must also be restored

For the current whole-face scaling,

[
sigma_{cr}^{E}
=
k_{cr}
rac{pi^2E_s}{12(1-
u_s^2)}
left(rac{t_s}{b/4}ight)^2.
]

The nine values are:

| case | sigma_cr^E / MPa | branch identity |
|---|---:|---|
| BH005 | 14998.06 | yield-first |
| BH010 | 3749.51 | yield-first |
| BH020 | 937.38 | yield-first |
| BH032 | 366.16 | yield-first |
| BH050 | 149.98 | local-first |
| BH060 | 104.15 | local-first |
| BH070 | 76.52 | local-first |
| BH085 | 51.90 | local-first |
| BH100 | 37.50 | local-first |

Hence BH005--BH032 must not activate the Yun elastic postbuckling-growth branch before material yield.

## 6. Minimal admissible repair: restore the existing S2 strength active set

The project already has a layer-0 S2 closure:

[
sigma_{eq,max}(A_u,A_0)=f_y,
]

[
sigma_u^{avg}=sigma_Y(A_u,A_0),
]

then for the strength path

[
oxed{
A=A_u,
qquad
arsigma_s=sigma_u^{avg}.
}
]

This explicitly does **not** claim that real post-yield local deformation stops. It only closes the strength path after the elastic large-deflection formula reaches its material-domain limit.

For the present one-parameter route this gives, after the S2 event,

[
oxed{
ararepsilon_{p,y}^{,pm}(w)
=
e_U^pm(w)
+s_pm C_{GL}^pm
left(
w_0A_u^pm+wA_0^pm+wA_u^pm
ight)
-rac{sigma_u^{avg,pm}}{E_s}.
}
]

Thus the missing post-yield axial shortening is recorded explicitly, while (A_u) and (sigma_u^{avg}) remain fixed strength-path state constants.

For the local-first specimens, using the combined-Mises first-yield states above, the two-face steel-force plateau after both faces have entered S2 is:

| case | P_s,S2 / MN |
|---|---:|
| BH050 | 5.56215 |
| BH060 | 5.61483 |
| BH070 | 5.72293 |
| BH085 | 6.03190 |
| BH100 | 6.46933 |

These are **steel-component strength-path plateaus**, not total UCFT ultimate loads.

## 7. R03 execution decision

The proposed ((A,e)) post-yield corrector is rejected.

The retained route is now:

[
oxed{
	ext{S0 material branch}
ightarrow
	ext{S1 repaired elastic Yun whole-face branch}
ightarrow
	ext{combined-Mises event}
ightarrow
	ext{S2 strength active set}.
}
]

For BH005--BH032 the S1 Yun branch is bypassed because (sigma_{cr}^{E}ge f_y).

For BH050--BH100 the S1 branch is retained until the combined-Mises S2 event.

The next calculation task is therefore no longer “search harder for an ((A,e)) root”. It is to implement the S0 yield-first evaluator for BH005--BH032 and then combine the resulting steel path with the already-locked one-parameter UHPC path to produce the nine total (P(w)) curves.

No FEM (P_u), FEM (q), or fitted coefficient was used in this audit.
