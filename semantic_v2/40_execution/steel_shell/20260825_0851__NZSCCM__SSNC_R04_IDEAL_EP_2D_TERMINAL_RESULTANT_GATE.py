import math
import numpy as np

TOL = 1e-10


def plane_stress_Q(E, nu):
    Q = E / (1.0 - nu**2)
    G = E / (2.0 * (1.0 + nu))
    return np.array(
        [[Q, nu * Q, 0.0], [nu * Q, Q, 0.0], [0.0, 0.0, G]],
        dtype=float,
    )


def layer_abd(Q, t, zc):
    """Exact initial elastic ABD of one uniform layer centered at z=zc."""
    A = Q * t
    B = Q * (t * zc)
    D = Q * (t * zc**2 + t**3 / 12.0)
    return A, B, D


def vm(sig):
    sx, sy, txy = map(float, sig)
    return math.sqrt(max(0.0, sx * sx - sx * sy + sy * sy + 3.0 * txy * txy))


def radial_mises_cap(sig_trial, fy):
    """
    Simplified path-free ideal-EP terminal map used only at the capacity layer.

    It is exact for uniaxial ideal-perfect plasticity and is a proportional-loading
    analytical approximation for the full biaxial/shear face-level terminal.  It
    is NOT a post-yield consistent tangent law and is never fed back into Airy.
    """
    sig_trial = np.asarray(sig_trial, dtype=float)
    v = vm(sig_trial)
    lam = 1.0 if v <= fy else fy / v
    return lam * sig_trial, lam, v


def face_resultant_from_mean_stress(sig_mean, t, zf):
    """
    Homogenized steel-face terminal resultant.

    No through-thickness plastic partition is introduced.  The face acts as a
    membrane layer at its physical centroid zf, hence its gross bending resultant
    is the exact lever-arm term zf*N.  The own-skin Et^3/12 term belongs to the
    initial Airy D0 and is not recreated as a plastic thickness block here.
    """
    N = t * np.asarray(sig_mean, dtype=float)
    M = zf * N
    return N, M


def main():
    # Representative source-grounded reduced DSCW geometry used only as a gate.
    h = 130.0
    ts = 4.0
    tc = h - 2.0 * ts
    zf = tc / 2.0 + ts / 2.0

    Es, nus = 206000.0, 0.30
    Ec, nuc = 32500.0, 0.20
    Qs = plane_stress_Q(Es, nus)
    Qc = plane_stress_Q(Ec, nuc)

    Ac, Bc, Dc = layer_abd(Qc, tc, 0.0)
    Ap, Bp, Dp = layer_abd(Qs, ts, +zf)
    Am, Bm, Dm = layer_abd(Qs, ts, -zf)

    A0 = Ac + Ap + Am
    B0 = Bc + Bp + Bm
    D0 = Dc + Dp + Dm

    # Exact steel-face decomposition: own-skin + parallel-axis/offset term.
    Dsteel_full = Dp + Dm
    Dsteel_own = 2.0 * Qs * (ts**3 / 12.0)
    Dsteel_offset = 2.0 * Qs * (ts * zf**2)

    err_D = np.max(np.abs(Dsteel_full - Dsteel_own - Dsteel_offset))
    err_B = np.max(np.abs(B0))

    # Independent direct through-thickness integral of the two steel faces.
    outer = h / 2.0
    inner = tc / 2.0
    Dsteel_direct_11 = Qs[0, 0] * 2.0 * (outer**3 - inner**3) / 3.0
    err_direct = abs(Dsteel_full[0, 0] - Dsteel_direct_11)

    # 2D ideal-EP terminal map gate.
    fy = 355.0
    sig_trial = np.array([200.0, 420.0, 50.0])
    sig_cap, lam, vm_trial = radial_mises_cap(sig_trial, fy)
    vm_cap = vm(sig_cap)
    Nf, Mf = face_resultant_from_mean_stress(sig_cap, ts, zf)

    # Elastic branch and exact uniaxial ideal-EP degeneration.
    sig_el = np.array([20.0, 100.0, 0.0])
    sig_el_cap, lam_el, _ = radial_mises_cap(sig_el, fy)
    sig_uni = np.array([0.0, 500.0, 0.0])
    sig_uni_cap, lam_uni, _ = radial_mises_cap(sig_uni, fy)

    # x <-> y symmetry.
    sig_swap = np.array([sig_trial[1], sig_trial[0], sig_trial[2]])
    sig_swap_cap, _, _ = radial_mises_cap(sig_swap, fy)
    xy_err = np.max(
        np.abs(sig_swap_cap - np.array([sig_cap[1], sig_cap[0], sig_cap[2]]))
    )

    # Symmetric equal top/bottom states give zero gross bending resultant.
    Np, Mp = face_resultant_from_mean_stress(sig_cap, ts, +zf)
    Nm, Mm = face_resultant_from_mean_stress(sig_cap, ts, -zf)
    Nsym = Np + Nm
    Msym = Mp + Mm

    assert err_D < 1e-6
    assert err_B < 1e-10
    assert err_direct < 1e-5
    assert abs(vm_cap - fy) < 1e-10
    assert abs(lam_el - 1.0) < 1e-15
    assert np.max(np.abs(sig_el_cap - sig_el)) < 1e-12
    assert abs(sig_uni_cap[1] - fy) < 1e-10
    assert abs(sig_uni_cap[0]) < 1e-12 and abs(sig_uni_cap[2]) < 1e-12
    assert xy_err < 1e-10
    assert np.max(np.abs(Msym)) < 1e-10

    print("SSNC_R04_IDEAL_EP_2D_TERMINAL_RESULTANT_GATE = PASS")
    print("AIRY_USES_INITIAL_ABD_ONLY = True")
    print("INITIAL_STEEL_OFFSET_STIFFNESS_INCLUDED = True")
    print("CURRENT_TANGENT_FEEDBACK_TO_AIRY = False")
    print("THROUGH_THICKNESS_PLASTIC_PARTITION = False")
    print("POST_YIELD_TANGENT_THEORY = 0.0")
    print("POST_YIELD_TANGENT_NUMERICAL_REGULARIZATION = optional")
    print(f"zf_mm = {zf:.12f}")
    print(f"B0_sym_abs = {err_B:.12e}")
    print(f"Dsteel_parallel_axis_abs = {err_D:.12e}")
    print(f"Dsteel_direct_integral_abs = {err_direct:.12e}")
    print(f"Dsteel11_full_Nmm = {Dsteel_full[0,0]:.12e}")
    print(f"Dsteel11_offset_Nmm = {Dsteel_offset[0,0]:.12e}")
    print(f"Dsteel11_own_skin_Nmm = {Dsteel_own[0,0]:.12e}")
    print(
        f"offset_fraction_of_steel_D11 = "
        f"{Dsteel_offset[0,0]/Dsteel_full[0,0]:.12e}"
    )
    print(
        f"steel_fraction_of_total_D11 = "
        f"{Dsteel_full[0,0]/D0[0,0]:.12e}"
    )
    print(f"trial_vm_MPa = {vm_trial:.12f}")
    print(f"plastic_scale_lambda = {lam:.12f}")
    print(f"capped_vm_MPa = {vm_cap:.12f}")
    print(f"uniaxial_capped_sy_MPa = {sig_uni_cap[1]:.12f}")
    print(f"xy_sym_abs = {xy_err:.12e}")
    print(
        "NOTE: terminal face moment uses M_f = z_f N_f; own-skin Et^3/12 is "
        "retained in initial Airy D0,"
    )
    print(
        "      but no through-thickness plastic bending block is introduced "
        "in the simplified terminal."
    )


if __name__ == "__main__":
    main()
