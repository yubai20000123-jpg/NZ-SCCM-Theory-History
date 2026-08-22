# NZ-SCCM theory lessons from acquired prior art

## A. SHOULD_DIRECTLY_ADOPT

1. Keep a small, explicit large-deflection structural operator separate from the capacity layer.
2. Use Airy/Kármán compatibility and Galerkin/Ritz projection where the steel-like plate problem permits it.
3. Represent ultimate strength as a direct demand–capacity intersection; retain finite roots when the postbuckling and capacity relations are algebraic.
4. Enumerate a finite, physically motivated set of local/global/control mechanisms and take the governing admissible result.
5. Keep initial imperfection as an explicit input/operator, not a hidden calibration factor.
6. Use fibre/layer integration as the capacity interface for RC/UHPC sections; do not bury it inside the global demand equations.

## B. SHOULD_ADAPT

1. Replace steel plastic fold-line capacity with a heterogeneous steel–concrete/UHPC `N-M-Mxy` capacity surface.
2. Add concrete tension/cracking and UHPC tensile/fibre response only in the capacity module first; add history only if the target limit state requires it.
3. Add connector/interface slip as an explicit capacity or restraint parameter, informed by the DS-UHPC/PBL literature.
4. Extend the finite mode/control set to include local steel plate buckling, concrete crushing, interface slip and composite section interaction.
5. Validate the direct root against a limited incremental/FE benchmark instead of making the benchmark the primary theory.

## C. SHOULD_AVOID

- Re-deriving the generic Airy/Kármán/Galerkin mathematics already explicit in P0-02.
- Treating effective width/area or effective height as a universal physical law.
- Prescribing an FE-informed collapse location without a finite candidate/control-location audit.
- Adding Newton/arc-length history to a path-independent steel-like limit state only because RC examples require it.
- Calling a public scan equation-verified when its text layer is empty.

## D. SHOULD_RETHINK

- If NZ-SCCM currently solves more state variables than are needed to obtain a direct limit load, compare its complexity with the P0-02 quadratic-plus-cubic closure.
- If a control location is selected by a single FE damage hotspot, replace that rule with a finite candidate set or a capacity-driven admissibility test.
- If material history is used for all materials, separate path-independent steel/UHPC limit states from path-dependent cracked-concrete cases.

## E. REAL_RESEARCH_DIFFICULTIES

1. Constructing a stable multiaxial heterogeneous capacity surface for steel, concrete/UHPC and connectors.
2. Performing analytical or semi-analytical section integration without losing finite-root closure.
3. Defining finite control locations that remain valid under support restraint, local buckling and interface slip.
4. Determining when cracking/softening history is physically necessary rather than numerically convenient.
5. Maintaining a common structural operator while switching between steel plate, RC wall and steel–UHPC composite capacity modules.

## Research positioning

The strongest acquired full-text overlap is P0-02's modified Airy postbuckling plus plastic-mechanism cubic intersection. That does not stop NZ-SCCM research; it changes the defensible research question from “inventing the generic chain” to “making the chain work, with auditable control locations and a heterogeneous RC/UHPC capacity closure, without unjustified empirical reduction.”

