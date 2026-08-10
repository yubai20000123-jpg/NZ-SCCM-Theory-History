# Nguyen Appendix B — effective evidence package

Authoritative source: `Nguyen-011325526.pdf`

- PDF SHA-256: `de4369d427540716e965bd9188ef0aaac77146eab3f054a433703f772e20111e`
- frozen full `pdftotext -layout` extraction SHA-256: `cb1bd34ca0c0ccb6eb0abfeb7e0151da56baad0b3a228b9dddb8ca60512938f4`
- frozen Appendix-B slice: extracted-text lines `12581–15437`, SHA-256 `39079268da5513bd3c20419e5732580d3b3b54e836926317d026672b534d2da1`

Following `EFFECTIVE_SOURCE_EXCERPT_POLICY.md`, Appendix B is **not** mirrored in full. Only source-code regions that materially constrain the project are archived.

## Archived excerpts

1. `01_stab_conc_interface.txt`
   - frozen Appendix-B extracted-text lines: `1919–2138` within the Appendix-B slice used during recovery
   - local excerpt SHA-256: `d85b45c43138938ff834cbb582133889d345beec051fc77a92dedb8bf601e202`
   - role: concrete element → principal strains → state-dependent modulus calls → transformed tangent/stress → stability scratch data.

2. `02_concrete_state_moduli.txt`
   - lines `2142–2623`
   - SHA-256: `c1f5da0a99d05006fab2086aa8b0084c5c4b648e9e8b0892947f9fdeea2e6867`
   - role: `stmodcc`, `stmodtc`, tension/tension state routine, `stmoduc`, compression secant/tangent helpers; direct source provenance for U/TC/TT/CC material-state logic.

3. `03_stab_bar2_rebar.txt`
   - lines `2624–2754`
   - SHA-256: `b51fb2a15de9c6f95ae2c25746ea14b094c3b57228aa8004d7903d1c772d0f3e`
   - role: reinforcement stress/tangent source interface used by stability analysis.

4. `04_stability_matrix_assembly.txt`
   - lines `285–460`
   - SHA-256: `0af06e375ee104a6c66cd9401b8d0f504af166882c7c7432d301c55fa723c579`
   - role: source assembly of element stiffness + geometric/stability contribution for steel and concrete elements.

## Current-theory boundary

These are **PRIMARY_SOURCE_PROGRAM_PROVENANCE** excerpts. They preserve exactly how Nguyen's source implementation generated tangent/stress information for stability analysis and how state-specific material routines were called.

They do **not** authorize reintroduction of:

- Gauss/material-point discretization as the formal NZ-SCCM operator;
- the full historical load-step/history machine as the current material interface;
- Chapter-4 FE architecture as the current zero-formal-spatial-quadrature production route.

The current project may derive or audit a compact current-state operator against these source equations, but any transformation must be identified as a project transformation rather than a verbatim Nguyen law.
