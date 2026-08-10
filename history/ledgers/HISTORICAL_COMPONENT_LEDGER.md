# NZ-SCCM 历史组件台账（正式组合基线 v1.0）

## 1. 台账目的

本台账不把任何历史阶段整体判定为“成功”或“失败”，而是把公式、代码、测试和边界拆成可继承组件。当前正式基线只组合已经验证且不违反最新硬约束的组件。

## 2. 当前组合结论

\[
\boxed{
\text{m=1连续完整半波}
+\text{D15精确矩引擎}
+\text{D12/D16材料门禁}
+\text{D18/D19零求积状态前沿审计核心}
}
\]

材料生产关系仍为 **OPEN**。D19R材料代码、Liu-TC和D13曲线只作为来源/形状参照，不进入正式零积分矩阵。

## 3. 组件明细

### H01 · DRS · Direct dual-reaction scan concept
- 当前身份：`REFERENCE_ONLY`
- 作用层：`history`
- 理论依据：Continuous half-wave response P,Q_A with root scans
- 继承内容：Root enumeration discipline and separation of physical branches
- 排除边界：3x3 spatial Gauss as formal production; scan/bisection as final analytical matrix
- 证据：MODEL_CHANGE_HISTORY_RECOVERED_20260805.md
- 手算：not inherited
- 测试：historical

### H02 · D11 · m=1 continuous complete-halfwave kinematics
- 当前身份：`ACTIVE_PRODUCTION_CORE`
- 作用层：`kinematics`
- 理论依据：phi=sin(pi x/b)sin(pi y/l), von Karman strains
- 继承内容：Full continuous halfwave and A0A+A^2/2 membrane term
- 排除边界：D11 P4 as complete concrete/UHPC model
- 证据：D11 report + D15 compiler
- 手算：M1_GEOMETRIC_MOMENTS_HAND_CALC.md
- 测试：D15 exact-moment tests

### H03 · D11 · Direct equilibrium/limit equations
- 当前身份：`RETAIN_CONDITIONAL`
- 作用层：`solver`
- 理论依据：U_A=0; det Hessian=0; P=U_delta/l
- 继承内容：Direct algebraic equilibrium and limit-point identity when an admissible energy potential exists
- 排除边界：Claim that every nonsymmetric material tangent admits scalar-potential Hessian
- 证据：D11 report
- 手算：formula-level
- 测试：D11 machine regression in D15 report

### H04 · D11 · 22-term P4 energy
- 当前身份：`ACTIVE_REGRESSION_ONLY`
- 作用层：`tests`
- 理论依据：Theory-derived c3,c4 from compression peak and zero tangent
- 继承内容：Machine regression and proof of zero spatial quadrature
- 排除边界：Formal material law or production prediction
- 证据：D11 report
- 手算：available in source report
- 测试：D15 machine precision regression

### H05 · D12 · Material admissibility gate
- 当前身份：`ACTIVE_GATE`
- 作用层：`material_gate`
- 理论依据：Reject disconnected branch, tensile overshoot, order nonconvergence
- 继承内容：Shape and branch admissibility must precede panel accuracy
- 排除边界：Accepting a material law because one panel load is close
- 证据：D12_CANDIDATE_GATE_SUMMARY.csv
- 手算：curve checks
- 测试：historical candidate table

### H06 · D13 · SAGP continuous single-valued potential
- 当前身份：`REFERENCE_ONLY`
- 作用层：`material_reference`
- 理论依据：Continuous shape-limited potential; Case21 near experiment
- 继承内容：Reference curves and evidence that smooth low-dimensional route can be predictive
- 排除边界：Its 32x32x20 quadrature implementation from production
- 证据：MODEL_CHANGE_HISTORY + D14 report
- 手算：not formal baseline
- 测试：historical convergence

### H07 · D14 · GRC10 panel-level Chebyshev condensation
- 当前身份：`REJECTED_FORMAL`
- 作用层：`rejected`
- 理论依据：198 coefficients from offline continuous integration
- 继承内容：Diagnostic comparison only
- 排除边界：Formal analytical identity or production matrix
- 证据：D14 report
- 手算：not applicable
- 测试：Case21 reproduction only

### H08 · D15 · Exact sparse trigonometric-thickness moment compiler
- 当前身份：`ACTIVE_PRODUCTION_CORE`
- 作用层：`matrix`
- 理论依据：Finite sin/cos monomials and exact zeta powers
- 继承内容：J_pq, Z_m, sparse expansion, exact condensation to r^i q^j
- 排除边界：None in mathematical engine; material coefficients remain separate
- 证据：d15_exact_moment_compiler.py
- 手算：D15R_HAND_CALC + M1 hand calc
- 测试：test_d15_exact_moment_original.py

### H09 · D15 · I1,I2 and Newton principal power sums
- 当前身份：`ACTIVE_MATH_CORE`
- 作用层：`matrix`
- 理论依据：p_j=I1 p_{j-1}-I2 p_{j-2}
- 继承内容：Eliminate explicit eigenvalue radicals for finite invariant bases
- 排除边界：Assumption that one scalar potential is sufficient for all NSC/UHPC states
- 证据：D15 report and compiler
- 手算：p2 identity
- 测试：mapping regression

### H10 · D15 · Original 156 mapping artifact vs 155 nonzero rebuild
- 当前身份：`OPEN_PROVENANCE`
- 作用层：`audit`
- 理论依据：Original report counts 156; independent current compiler counts 155 nonzero
- 继承内容：Both records without forced reconciliation
- 排除边界：Inventing a zero row to force equality
- 证据：D15 report; D15R mapping CSV
- 手算：count table
- 测试：explicit 155 test

### H11 · D15 · UHPC-L0 single-axis principal potential
- 当前身份：`REJECTED_MATERIAL_IDENTITY`
- 作用层：`rejected`
- 理论依据：a2..a6 power-sum potential, beta terms zero
- 继承内容：Formula grammar and exact-moment compatibility only
- 排除边界：Formal UHPC material identity; permanent beta=0; loss of six-state information
- 证据：D15 report and later user lock
- 手算：not active
- 测试：not production

### H12 · D15R · Finite coaxial vector operator a(I1,I2)I+b(I1,I2)E
- 当前身份：`OPEN_MATH_INTERFACE`
- 作用层：`material_open`
- 理论依据：Allows analytic tangent, possibly nonsymmetric
- 继承内容：Mathematical container for future theory-derived finite operators
- 排除边界：Treating arbitrary fitted coefficients as material theory
- 证据：common_isotropic_vector_operator.py
- 手算：derivatives explicit
- 测试：central-difference audit only

### H13 · D16 · Exact-moment integrability classification
- 当前身份：`ACTIVE_GATE`
- 作用层：`material_gate`
- 理论依据：Finite polynomial branches close; rational/exponential/WW need separate treatment
- 继承内容：Classify every candidate term before admission
- 排除边界：Forcing nonintegrable source formulas into high-order fits
- 证据：D16_EXACT_MOMENT_INTEGRABILITY_AUDIT.csv
- 手算：classification table
- 测试：documentary

### H14 · D17 · Thickness principal-threshold front
- 当前身份：`RETAIN_THEORY_SOURCE_ARTIFACT_PENDING`
- 作用层：`state_front`
- 理论依据：At fixed in-plane position, threshold equation is quadratic in z
- 继承内容：Analytical thickness-event concept and 755-root validation result
- 排除边界：Thickness material-point discretization
- 证据：Recovered history; original D17 zip hash only
- 手算：not locally recovered
- 测试：historical 755-root result

### H15 · D18 · u=sin^2X,v=sin^2Y algebraic in-plane front
- 当前身份：`ACTIVE_AUDIT_CORE`
- 作用层：`state_front`
- 理论依据：F=P0+sqrt(uv)P1; squared cubic in v
- 继承内容：Physical root filtering, exact full/incomplete Beta measures
- 排除边界：Treating squared roots without unsquared sign check
- 证据：inplane_algebraic_state_front.py
- 手算：D19 front hand calc
- 测试：D19 root tests

### H16 · D19 · Exact topology-event partition
- 当前身份：`ACTIVE_AUDIT_CORE`
- 作用层：`state_front`
- 理论依据：V0,V1,leading coefficient, discriminant,resultant events
- 继承内容：Grid-free topology partition and branch-count constancy
- 排除边界：u-grid topology scans
- 证据：d19_event_topology_core_zero_quadrature.py
- 手算：event-polynomial inspection
- 测试：composite equivalence tests

### H17 · D19 · Analytic front derivative
- 当前身份：`ACTIVE_AUDIT_CORE`
- 作用层：`state_front`
- 理论依据：dv/dtheta=-F_theta/F_v using unsquared physical equation
- 继承内容：Event-aware analytical derivative
- 排除边界：Using derivative at singular topology event
- 证据：d19_event_topology_core_zero_quadrature.py
- 手算：D19 front hand calc
- 测试：finite-difference audit

### H18 · D19 · Outer 1D state-front quadrature audit
- 当前身份：`REJECTED_FORMAL`
- 作用层：`rejected`
- 理论依据：quad over u after incomplete-Beta inner integral
- 继承内容：Historical comparison only
- 排除边界：Any formal or production use under zero-integration lock
- 证据：branch_event_system_original_with_1d_audit.py
- 手算：Simpson audit historical only
- 测试：original D19 test only

### H19 · D19 · Liu 2023 TC compression scalar branch
- 当前身份：`REFERENCE_ONLY`
- 作用层：`material_reference`
- 理论依据：zeta_sigma and softened compression equations
- 继承内容：Compression-direction scalar law, tangent and event locations as source reference
- 排除边界：Calling it a complete 2D TC/TCX state
- 证据：liu2023_tc_compression.py; D19 report
- 手算：formula reproduction
- 测试：Liu tangent tests

### H20 · D19R · Path-closed NSC/UHPC response-tangent interface
- 当前身份：`REFERENCE_ONLY`
- 作用层：`material_reference`
- 理论依据：U/TC/TT/CC/TCX/CCX point response with AD tangent
- 继承内容：Source registry, state vocabulary, stress/tangent regression cases
- 排除边界：Gauss panel evaluator; project-derived U->TC entry as formal theory
- 证据：path_closed_materials_D19R_reference_only.py
- 手算：not production
- 测试：D19R regression historical

### H21 · D19C · Panel-level Chebyshev residual surfaces
- 当前身份：`REJECTED`
- 作用层：`rejected`
- 理论依据：Offline Gauss sampling and piecewise Chebyshev surfaces
- 继承内容：Five false-branch cases as counterexamples
- 排除边界：Formal matrix, production roots, reported population accuracy
- 证据：D19C/v0.6.3 reports
- 手算：not admissible
- 测试：direct-balance failures

### H22 · v0.6.1 · Fixed m=1 representative halfwave
- 当前身份：`HARD_LOCK`
- 作用层：`kinematics`
- 理论依据：One complete representative halfwave; repeated symmetric waves not independent candidates
- 继承内容：m=1 for every Swartz panel and later representative-halfwave use
- 排除边界：m>1 search, modal envelope, minimum over m
- 证据：D19C M1 correction report + user lock
- 手算：shape definition
- 测试：configuration audit

### H23 · v0.6.3 · NSC-only Source-U enhancement
- 当前身份：`REJECTED`
- 作用层：`rejected`
- 理论依据：Nguyen-specific extra secant/dilatancy/equivalent-strain information
- 继承内容：Diagnostic evidence that simultaneous changes destroy attribution
- 排除边界：Formal common NSC/UHPC baseline
- 证据：v0.6.3 diagnostic report
- 手算：not active
- 测试：not active

### H24 · v0.6.3 · Pseudo-arclength path continuation
- 当前身份：`DISABLED`
- 作用层：`solver`
- 理论依据：Continuation across folds
- 继承内容：May be reconsidered only after true formal residual exists
- 排除边界：Using it to validate a proxy branch
- 证据：v0.6.3 diagnostic history
- 手算：not active
- 测试：not active

### H25 · v0.5.4-v0.5.8 · High-order/anchor/P6 reconstructed material functions
- 当前身份：`REJECTED`
- 作用层：`rejected`
- 理论依据：Orthogonal fits, anchor inversion, global dual-peak P6
- 继承内容：Failure modes and conditioning warnings only
- 排除边界：All coefficients and material identities
- 证据：v0.5.4-v0.5.8 reports
- 手算：not active
- 测试：historical negative controls

### H26 · Current · Zero numerical integration
- 当前身份：`HARD_LOCK`
- 作用层：`contract`
- 理论依据：No Gauss/Simpson/adaptive/offline spatial integration or panel proxy
- 继承内容：Finite theory-derived matrix terms only
- 排除边界：All spatial quadrature in formal path
- 证据：user lock 2026-08-06
- 手算：required
- 测试：static forbidden-import scan

### H27 · Current · Theory-derived terms only
- 当前身份：`HARD_LOCK`
- 作用层：`contract`
- 理论依据：Terms and coefficients must follow theory/source equations, not selected fit points or panel loads
- 继承内容：Explicit derivation/provenance for every active coefficient
- 排除边界：Special-value fitting, panel calibration, hidden regression
- 证据：user lock 2026-08-06
- 手算：required for every formal calculation
- 测试：provenance gate

### H28 · Current · NSC/UHPC information-level symmetry
- 当前身份：`HARD_LOCK`
- 作用层：`contract`
- 理论依据：No temporary NSC-only mechanisms unsupported for UHPC common framework
- 继承内容：Separate source-specific references may exist but not silently enter common formal model
- 排除边界：Asymmetric unannounced additions
- 证据：user lock 2026-08-05
- 手算：source registry
- 测试：component ledger

### H29 · Current · Hand-calculation audit protocol
- 当前身份：`HARD_LOCK`
- 作用层：`contract`
- 理论依据：Inputs, formulas, substitutions, intermediates, result, units, independent check
- 继承内容：Mandatory for all formal computations
- 排除边界：Code-only numerical result
- 证据：HAND_CALC_OUTPUT_PROTOCOL_LOCKED.md
- 手算：self
- 测试：deliverable checklist

### H30 · Current · Swartz 24-panel production
- 当前身份：`PAUSED`
- 作用层：`production`
- 理论依据：One frozen material/matrix version, m=1, no per-panel tuning
- 继承内容：Population computation only after material closure and exact-matrix gate
- 排除边界：Premature representative-panel calibration or partial publication
- 证据：project locks
- 手算：required when resumed
- 测试：not authorized

### H31 · Future · Yunlu steel-shell module
- 当前身份：`NOT_STARTED`
- 作用层：`future`
- 理论依据：Must provide finite exact blocks compatible with zero-integration architecture
- 继承内容：Interface requirement only
- 排除边界：Starting coupling before material baseline closure
- 证据：user requirement
- 手算：required later
- 测试：none
