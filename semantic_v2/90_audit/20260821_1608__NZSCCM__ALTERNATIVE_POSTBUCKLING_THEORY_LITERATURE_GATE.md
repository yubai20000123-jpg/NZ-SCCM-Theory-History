# NZ-SCCM — Alternative postbuckling theory literature gate

时间：2026-08-21 16:08 +08:00
状态：`NEW_RESEARCH_DIRECTION_CANDIDATE / NO FORMAL ADOPTION YET`

## 1. Trigger

PMV1-C73 has passed complete finite analytic expansion but failed the generic noniterative direct-Pu gate. Conservative algebraic degree bounds are too high for a practical universal resultant/companion solve.

Therefore no further effort is authorized on increasing exact constitutive/compiler complexity merely to preserve the same architecture.

## 2. Most important literature architecture found

### A. Closed-form Marguerre/von-Karman + Airy postbuckling

Key sources:

- C. Mittelstedt & K.-U. Schroeder (2010), *Postbuckling of Compressively Loaded Imperfect Composite Plates: Closed-Form Approximate Solutions*, IJSSD 10(4), 761-778, DOI 10.1142/S0219455410003725.
- R. Vescovini & C. Bisagni (2012), *Single-mode solution for post-buckling analysis of composite panels with elastic restraints loaded in compression*, Composites Part B 43(3), 1258-1274, DOI 10.1016/j.compositesb.2011.08.029.
- J.C. Schilling & C. Mittelstedt (2025), *Closed-form postbuckling analysis of shear-deformable composite laminated panels*, Archive of Applied Mechanics 95, article 17, DOI 10.1007/s00419-024-02720-4.
- E. Steen (1989), *Elastic buckling and postbuckling of eccentrically stiffened plates*, IJSS 25(7), 751-768, DOI 10.1016/0020-7683(89)90011-5.
- J.C. Schilling & C. Mittelstedt (2022), *Local postbuckling of omega-stringer-stiffened composite panels*, Thin-Walled Structures 181, 110027.

Common architecture:

1. keep one or a very small number of physically selected out-of-plane buckling modes;
2. introduce an Airy stress function, so in-plane equilibrium is satisfied a priori;
3. solve compatibility analytically for the Airy function rather than introducing a growing in-plane Ritz space;
4. integrate the elastic potential analytically;
5. eliminate auxiliary amplitudes algebraically;
6. obtain a low-degree postbuckling amplitude equation.

For Schilling-Mittelstedt 2025 the final amplitude equation is explicitly cubic:

W^3 + O1 W^2 + O2(N) W + O3(N) = 0,

and is solved in closed form. No load history is required to evaluate the response at an arbitrary load.

This is fundamentally different from the rejected H2/H4/... membrane Ritz route: the in-plane field is not represented by an ever-growing arbitrary displacement basis; equilibrium is carried by the Airy stress function and compatibility.

## 3. Strength/ultimate-load closure as a separate layer

A second literature family deliberately separates elastic/geometric postbuckling from collapse strength:

- Attard (1994/1995) RC wall method: tangent-modulus buckling -> imperfection amplification -> amplified plate moments -> cross-sectional N-M interaction / yield checks.
- Brubak & Hellesland (2007), semi-analytical large-deflection postbuckling + von-Mises membrane collapse criterion.
- Brubak, Andersen & Hellesland (2013), elastic semi-analytical postbuckling + extended strength criteria to approximate local plastic redistribution.
- Ozdemir et al. (2018), elastic large-deflection analysis (ELDA) + initial-yielding checks at critical points to estimate ultimate strength.
- Paik, Thayamballi & Kim (2001), large-deflection equivalent-orthotropic plate approach to derive ultimate-strength formulations for stiffened panels.
- Paik & Lee (2005), elastic-plastic semi-analytical large-deflection analysis to ULS (accurate but incremental, therefore not preferred for current project).

This suggests a potentially useful decomposition:

```text
GEOMETRIC POSTBUCKLING OPERATOR
    (low-order closed-form Airy/Marguerre)
                 +
MATERIAL/CROSS-SECTION FAILURE OPERATOR
    (steel yield / concrete crushing / N-M interaction)
                 ->
DIRECT ULTIMATE CONDITION
```

instead of embedding the full nonlinear concrete/steel current map at every spatial point inside the postbuckling differential operator.

## 4. Proposed candidate architecture for NZ-SCCM (NOT YET DERIVED)

Possible new route:

1. Use Zhou's orthotropic/tangent buckling result as the physically validated critical-state backbone for the ideal panel.
2. Use a Marguerre/von-Karman single physical local mode with initial imperfection.
3. Use an Airy stress function to close membrane equilibrium exactly.
4. Derive a low-order postbuckling amplitude relation, targeting a cubic/quartic form analogous to the closed-form plate literature.
5. Treat steel/concrete material strength only in a separate ultimate section/critical-point criterion, rather than using R10/N48/C73 inside the entire postbuckling field.
6. Solve simultaneously for load P and postbuckling amplitude W from:

   F_post(P,W)=0,
   F_capacity(P,W)=0.

If both are low-degree/algebraic, ultimate capacity can be obtained without load-path tracking.

## 5. Why this route is worth testing

- It directly attacks the cause of PMV1 algebraic explosion: full nonlinear constitutive mapping is removed from the geometric postbuckling field.
- It preserves postbuckling reserve strength, unlike a pure tangent/eigenvalue buckling formula.
- It does not require H6/H60 membrane-mode convergence.
- Literature demonstrates closed-form postbuckling for imperfect single plates and even stiffened composite panels.
- Literature on steel panels demonstrates that elastic large-deflection response plus explicit strength criteria can provide useful ultimate-strength predictions.

## 6. Boundaries

No claim is yet made that the composite steel-concrete panel reduces to the Schilling/Mittelstedt cubic unchanged. The next theoretical audit must derive the corresponding Airy compatibility and amplitude equation for the current ideal steel-concrete plate/backbone. If the derivation ceases to be low-order, stop early rather than repeat PMV1 complexity escalation.

No empirical Winter/DSM/FE-fitted curve is adopted. Those methods are retained only as evidence for the general idea of separating elastic buckling information from strength prediction.

## 7. Unique next research question

Can the current Zhou-equivalent orthotropic panel, with one ideal complete halfwave and initial imperfection, be reduced by Marguerre + Airy compatibility to a cubic or similarly low-degree postbuckling amplitude equation **before** any nonlinear concrete/steel ultimate criterion is introduced?

Only if this gate passes should a second equation for steel/concrete capacity be derived.