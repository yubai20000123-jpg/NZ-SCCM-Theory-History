from pathlib import Path
import json
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

OUT = Path("NZ_SCCM_CURRENT_TARGET_GEOMETRIC_REGULARIZATION_R01_20260810")
OUT.mkdir(parents=True, exist_ok=True)

# Case21 ordinary-concrete regression/reference constants.
nu = 0.18
eps0 = 0.00209
fc = 21.23
kappa = 2.0005129533678754
rho = 0.1
xcr = rho / kappa
eta_pi = xcr / 20.0
eta_r = 0.05
m_t = -7.0 / 90.0
a_cc = 0.1072329249362415
a_t = 1.0 - 2.0 ** (-1.0 / 8.0)

lam_min = -2.4390243902439024
lam_max = 0.7317073170731706
qualification_width = lam_max - lam_min
local_transition_width = eta_r * xcr


def Pi_eta(z, eta=eta_pi):
    z = np.asarray(z, dtype=float)
    return z * z * (np.sqrt(z * z + eta * eta) + z) / (2.0 * (z * z + eta * eta))


def H(r, r0, eta=eta_r):
    r = np.asarray(r, dtype=float)
    return (
        0.5 * ((r - r0) + np.sqrt((r - r0) ** 2 + eta**2))
        - 0.5 * ((-r0) + np.sqrt(r0**2 + eta**2))
    )


def primitives(lam):
    lam = np.asarray(lam, dtype=float)
    c = Pi_eta(-lam)
    t = Pi_eta(lam)
    C = kappa * c / (1.0 + (kappa - 2.0) * c + c * c)
    r = t / xcr
    T = r + (m_t - 1.0) * H(r, 1.0) - m_t * H(r, 10.0)
    U = kappa * lam - C + kappa * c + rho * T - kappa * t
    return U, C, T


def source_shaped_map(lam1, lam2):
    U1, C1, T1 = primitives(lam1)
    U2, C2, T2 = primitives(lam2)
    s1 = U1 - a_cc * C1 * C1 * C2 + C1 * T2 - rho * a_t * T1 * T2**8
    s2 = U2 - a_cc * C2 * C2 * C1 + C2 * T1 - rho * a_t * T2 * T1**8
    return s1, s2


def material_principal_from_actual_strain(e1, e2):
    lam1 = (e1 + nu * e2) / ((1.0 - nu**2) * eps0)
    lam2 = (nu * e1 + e2) / ((1.0 - nu**2) * eps0)
    s1, s2 = source_shaped_map(lam1, lam2)
    return fc * s1, fc * s2, lam1, lam2


# ----------------------------------------------------------------------
# A. Thin-layer curvature diagnosis in material coordinates only.
# ----------------------------------------------------------------------
x = np.linspace(-0.02, 0.60, 310001)
T = primitives(x)[2]
dx = x[1] - x[0]
dT = np.gradient(T, dx)
d2T = np.gradient(dT, dx)

windows = {
    "zero_split": (0.0, 0.01),
    "crack_transition_r1": (0.03, 0.07),
    "postcrack_transition_r10": (0.45, 0.55),
}
peaks = []
for name, (lo, hi) in windows.items():
    mask = (x >= lo) & (x <= hi)
    ids = np.where(mask)[0]
    i = ids[np.argmax(np.abs(d2T[mask]))]
    peaks.append(
        {
            "feature": name,
            "lambda_at_peak_curvature": float(x[i]),
            "T": float(T[i]),
            "dT_dlambda": float(dT[i]),
            "d2T_dlambda2": float(d2T[i]),
        }
    )

metrics = {
    "kappa": kappa,
    "rho": rho,
    "xcr": xcr,
    "eta_pi": eta_pi,
    "eta_r": eta_r,
    "local_transition_width_eta_r_times_xcr": local_transition_width,
    "qualification_lambda_min": lam_min,
    "qualification_lambda_max": lam_max,
    "qualification_width": qualification_width,
    "global_to_local_scale_ratio": qualification_width / local_transition_width,
    "r1_nominal_lambda": xcr,
    "r10_nominal_lambda": 10.0 * xcr,
    "curvature_peaks": peaks,
}
(OUT / "01_transition_metrics.json").write_text(
    json.dumps(metrics, ensure_ascii=False, indent=2), encoding="utf-8"
)

# ----------------------------------------------------------------------
# B. 4D current-map projections in lambda coordinates.
# ----------------------------------------------------------------------
g = np.linspace(-1.15, 0.65, 49)
L1, L2 = np.meshgrid(g, g)
S1, S2 = source_shaped_map(L1, L2)

fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection="3d")
sc = ax.scatter(L1.ravel(), L2.ravel(), S1.ravel(), c=S2.ravel(), s=9)
ax.set_xlabel(r"$\lambda_1=\varepsilon_{1u}/\varepsilon_0$")
ax.set_ylabel(r"$\lambda_2=\varepsilon_{2u}/\varepsilon_0$")
ax.set_zlabel(r"$\sigma_1/f_c$")
cb = fig.colorbar(sc, ax=ax, shrink=0.72)
cb.set_label(r"$\sigma_2/f_c$")
ax.set_title("4D current map: geometry in $(\\lambda_1,\\lambda_2,\\sigma_1)$, color = $\\sigma_2$")
fig.tight_layout()
fig.savefig(OUT / "02_current_map_4D_sigma1_color_sigma2.png", dpi=220)
plt.close(fig)

fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection="3d")
sc = ax.scatter(L1.ravel(), L2.ravel(), S2.ravel(), c=S1.ravel(), s=9)
ax.set_xlabel(r"$\lambda_1=\varepsilon_{1u}/\varepsilon_0$")
ax.set_ylabel(r"$\lambda_2=\varepsilon_{2u}/\varepsilon_0$")
ax.set_zlabel(r"$\sigma_2/f_c$")
cb = fig.colorbar(sc, ax=ax, shrink=0.72)
cb.set_label(r"$\sigma_1/f_c$")
ax.set_title("4D current map: geometry in $(\\lambda_1,\\lambda_2,\\sigma_2)$, color = $\\sigma_1$")
fig.tight_layout()
fig.savefig(OUT / "03_current_map_4D_sigma2_color_sigma1.png", dpi=220)
plt.close(fig)

# ----------------------------------------------------------------------
# C. T(lambda) and curvature concentration.
# ----------------------------------------------------------------------
xt = np.linspace(-0.02, 0.62, 12000)
Tt = primitives(xt)[2]

fig, ax = plt.subplots(figsize=(9, 5.5))
ax.plot(xt, Tt, label="current T(lambda)")
for xx, lab in [(0.0, "0"), (xcr, "r=1"), (10 * xcr, "r=10")]:
    ax.axvline(xx, label=lab)
ax.set_xlabel(r"$\lambda$")
ax.set_ylabel(r"$T(\lambda)$")
ax.set_title("Current tensile utilization and its three narrow transition locations")
ax.legend()
ax.grid(True, alpha=0.25)
fig.tight_layout()
fig.savefig(OUT / "04_tensile_utilization_transitions.png", dpi=220)
plt.close(fig)

_dT = np.gradient(Tt, xt[1] - xt[0])
_d2T = np.gradient(_dT, xt[1] - xt[0])
fig, ax = plt.subplots(figsize=(9, 5.5))
ax.semilogy(xt, np.abs(_d2T) + 1.0e-12)
for xx, lab in [(0.0, "0"), (xcr, "r=1"), (10 * xcr, "r=10")]:
    ax.axvline(xx, label=lab)
ax.set_xlabel(r"$\lambda$")
ax.set_ylabel(r"$|d^2T/d\lambda^2|$")
ax.set_title("Curvature concentration: global approximation pressure")
ax.legend()
ax.grid(True, alpha=0.25)
fig.tight_layout()
fig.savefig(OUT / "05_tensile_curvature_concentration.png", dpi=220)
plt.close(fig)

# ----------------------------------------------------------------------
# D. TT strength-envelope diagnostic contraction corridor.
# ----------------------------------------------------------------------
rows = []
fig, ax = plt.subplots(figsize=(6.8, 6.4))
for p in [8, 4, 2]:
    tau1 = np.linspace(0.0, 1.0, 1200)
    tau2 = np.maximum(0.0, 1.0 - tau1**p) ** (1.0 / p)
    ax.plot(tau1, tau2, label=f"p={p}")
    eq = 2.0 ** (-1.0 / p)
    rows.append(
        {
            "TT_superellipse_p": p,
            "equal_biaxial_strength_over_ft": eq,
            "relative_reduction_vs_p8_percent": 100.0
            * (2.0 ** (-1.0 / 8.0) - eq)
            / (2.0 ** (-1.0 / 8.0)),
        }
    )
ax.set_aspect("equal", adjustable="box")
ax.set_xlim(0.0, 1.02)
ax.set_ylim(0.0, 1.02)
ax.set_xlabel(r"$\sigma_1/f_t$")
ax.set_ylabel(r"$\sigma_2/f_t$")
ax.set_title("TT strength-domain smoothing / conservative contraction corridor")
ax.legend()
ax.grid(True, alpha=0.25)
fig.tight_layout()
fig.savefig(OUT / "06_TT_strength_domain_contraction_candidates.png", dpi=220)
plt.close(fig)

pd.DataFrame(rows).to_csv(OUT / "07_TT_contraction_metrics.csv", index=False)

# ----------------------------------------------------------------------
# E. Actual (eps1, eps2, sigma1, sigma2) visualization.
# ----------------------------------------------------------------------
emicro = np.linspace(-2600.0, 1100.0, 55)
E1m, E2m = np.meshgrid(emicro, emicro)
E1 = E1m * 1.0e-6
E2 = E2m * 1.0e-6
Sig1, Sig2, Lam1, Lam2 = material_principal_from_actual_strain(E1, E2)

fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection="3d")
sc = ax.scatter(E1m.ravel(), E2m.ravel(), Sig1.ravel(), c=Sig2.ravel(), s=8)
ax.set_xlabel(r"$\varepsilon_1$ ($\mu\varepsilon$)")
ax.set_ylabel(r"$\varepsilon_2$ ($\mu\varepsilon$)")
ax.set_zlabel(r"$\sigma_1$ (MPa)")
cb = fig.colorbar(sc, ax=ax, shrink=0.72)
cb.set_label(r"$\sigma_2$ (MPa)")
ax.set_title(r"Current map in $(\varepsilon_1,\varepsilon_2,\sigma_1)$; color = $\sigma_2$")
fig.tight_layout()
fig.savefig(OUT / "10_actual_eps1_eps2_sigma1_color_sigma2.png", dpi=220)
plt.close(fig)

fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection="3d")
sc = ax.scatter(E1m.ravel(), E2m.ravel(), Sig2.ravel(), c=Sig1.ravel(), s=8)
ax.set_xlabel(r"$\varepsilon_1$ ($\mu\varepsilon$)")
ax.set_ylabel(r"$\varepsilon_2$ ($\mu\varepsilon$)")
ax.set_zlabel(r"$\sigma_2$ (MPa)")
cb = fig.colorbar(sc, ax=ax, shrink=0.72)
cb.set_label(r"$\sigma_1$ (MPa)")
ax.set_title(r"Current map in $(\varepsilon_1,\varepsilon_2,\sigma_2)$; color = $\sigma_1$")
fig.tight_layout()
fig.savefig(OUT / "11_actual_eps1_eps2_sigma2_color_sigma1.png", dpi=220)
plt.close(fig)

# TC slices that make the ridge easier to see than the 4D projections.
e1m_line = np.linspace(-200.0, 1200.0, 3000)
for e2m_fixed, fname in [
    (-700.0, "12_TC_slice_eps2_minus700.png"),
    (-1300.0, "13_TC_slice_eps2_minus1300.png"),
]:
    sig1, sig2, _, _ = material_principal_from_actual_strain(
        e1m_line * 1.0e-6, np.full_like(e1m_line, e2m_fixed) * 1.0e-6
    )
    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.plot(e1m_line, sig1, label=r"$\sigma_1$")
    ax.plot(e1m_line, sig2, label=r"$\sigma_2$")
    ax.axvline(0.0, label=r"$\varepsilon_1=0$")
    ax.set_xlabel(r"$\varepsilon_1$ ($\mu\varepsilon$)")
    ax.set_ylabel("principal stress (MPa)")
    ax.set_title(rf"TC slice: fixed $\varepsilon_2={e2m_fixed:.0f}\,\mu\varepsilon$")
    ax.legend()
    ax.grid(True, alpha=0.25)
    fig.tight_layout()
    fig.savefig(OUT / fname, dpi=220)
    plt.close(fig)

# ----------------------------------------------------------------------
# F. Same-route sector decision artifact.
# ----------------------------------------------------------------------
sector_df = pd.DataFrame(
    [
        {
            "sector": "CC",
            "retained_target": "c_i*=c_i(1+a_cc*c1*c2)",
            "status_this_step": "RETAIN_UNCHANGED",
            "reason": "Compression-dominant region; no evidence that CC is the source of analytic sharpness.",
        },
        {
            "sector": "TC/CT",
            "retained_target": "c*=c(1-tau); tensile component not amplified",
            "status_this_step": "RETAIN_AS_CONSERVATIVE_TARGET",
            "reason": "Already frozen as a deliberately conservative low-parameter target relative to G20 C1 TC envelope.",
        },
        {
            "sector": "TT",
            "retained_target": "G20 p=8 outer reference; p=4/p=2 inner diagnostic corridor",
            "status_this_step": "P4_MODERATE_CANDIDATE__P2_STRONG_DIAGNOSTIC",
            "reason": "Final p must be decided by material-level stress/tangent/shape gate, never structural Pu.",
        },
        {
            "sector": "Tensile current-map transition",
            "retained_target": "preserve origin elastic tangent and uniaxial ft; regularize transition ridges conservatively",
            "status_this_step": "PRIMARY_REFORMULATION_TARGET",
            "reason": "Three thin lambda layers dominate curvature and global approximation pressure.",
        },
    ]
)
sector_df.to_csv(OUT / "08_sector_reformulation_decision.csv", index=False)

manifest = {
    "formal_spatial_quadrature": 0,
    "note": "Material-coordinate diagnostics only; no structural spatial numerical integration.",
    "visuals": [
        "02_current_map_4D_sigma1_color_sigma2.png",
        "03_current_map_4D_sigma2_color_sigma1.png",
        "04_tensile_utilization_transitions.png",
        "05_tensile_curvature_concentration.png",
        "06_TT_strength_domain_contraction_candidates.png",
        "10_actual_eps1_eps2_sigma1_color_sigma2.png",
        "11_actual_eps1_eps2_sigma2_color_sigma1.png",
        "12_TC_slice_eps2_minus700.png",
        "13_TC_slice_eps2_minus1300.png",
    ],
}
(OUT / "14_visual_manifest.json").write_text(
    json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
)

print(json.dumps(metrics, ensure_ascii=False, indent=2))
print(pd.DataFrame(rows).to_string(index=False))
print("R01 complete; formal structural spatial quadrature = 0")
