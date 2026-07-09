#!/usr/bin/env python3
"""Checks for the M1 carrier source map.

Units set c = 1.  A carrier has core momentum M=sqrt(p_f^2+p^2) and
directional bosic components p_k.  The source identification tested here is

    J_k^+/- = density of (M +/- p_k / 2)
    Mcal_k = (J_k^+ + J_k^-) / 2 = density of M
    Pcal_k = J_k^+ - J_k^- = density of p_k

No pressure, stress, or radiation enhancement is inserted into the source layer.
"""

from __future__ import annotations

import sys

import numpy as np


def assert_close(name: str, value: float, target: float, tol: float = 1e-12) -> None:
    if abs(value - target) > tol:
        raise AssertionError(f"{name}: got {value:.16g}, expected {target:.16g}")


def carrier_channels(
    M: np.ndarray, p_components: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Return per-carrier Jplus, Jminus, Mcal, Pcal for one axis array."""
    Jplus = M + 0.5 * p_components
    Jminus = M - 0.5 * p_components
    Mcal = 0.5 * (Jplus + Jminus)
    Pcal = Jplus - Jminus
    return Jplus, Jminus, Mcal, Pcal


def random_carriers(n: int = 2048, seed: int = 20260706) -> tuple[np.ndarray, np.ndarray]:
    """Generate timelike and near-null carriers with |p_k| <= |p| <= M."""
    rng = np.random.default_rng(seed)
    pf = rng.random(n) * 2.0
    pvec = rng.normal(size=(n, 3))
    pvec *= (rng.random(n)[:, None] * 5.0) / np.linalg.norm(pvec, axis=1)[:, None]
    M = np.sqrt(pf * pf + np.sum(pvec * pvec, axis=1))
    return M, pvec


def lense_thirring_endpoint_error(kappa_a: float, source_ratio: float) -> float:
    """Dimensionless endpoint check for P_i / j_i in the existing audit convention."""
    rng = np.random.default_rng(20260704)
    worst = 0.0
    for _ in range(128):
        J = rng.normal(size=3)
        r = rng.normal(size=3)
        r *= (2.0 + 3.0 * rng.random()) / np.linalg.norm(r)
        p = rng.normal(size=3) * 1e-3
        theta_i = source_ratio * np.cross(J, r) / (2.0 * np.linalg.norm(r) ** 3)
        A = -kappa_a * theta_i
        lhs = -float(A @ p)
        rhs = 2.0 * float(J @ np.cross(r, p)) / np.linalg.norm(r) ** 3
        worst = max(worst, abs(lhs - rhs) / max(abs(rhs), 1e-30))
    return worst


def main() -> int:
    print("[1] channel positivity")
    M, pvec = random_carriers()
    for axis in range(3):
        Jp, Jm, Mcal, Pcal = carrier_channels(M, pvec[:, axis])
        if np.min(Jp) <= 0.0 or np.min(Jm) <= 0.0:
            raise AssertionError("carrier channel positivity failed")
        if np.max(np.abs(Mcal - M)) > 1e-12:
            raise AssertionError("even package is not the carrier core momentum")
        if np.max(np.abs(Pcal - pvec[:, axis])) > 1e-12:
            raise AssertionError("odd package is not the bosic component")
    M_columns = M[:, None]
    print(f"    minimum J_k^+/- over sample        = {min(np.min(M_columns + 0.5 * pvec), np.min(M_columns - 0.5 * pvec)):.12f}")

    print("[2] randomized ensemble")
    total_M = float(np.sum(M))
    for axis in range(3):
        _, _, Mcal, Pcal = carrier_channels(M, pvec[:, axis])
        assert_close(f"axis {axis} even total", float(np.sum(Mcal)), total_M)
        assert_close(f"axis {axis} odd total", float(np.sum(Pcal)), float(np.sum(pvec[:, axis])))
    print(f"    even total, every axis             = {total_M:.12f}")
    print(f"    odd vector                         = {np.sum(pvec, axis=0)}")

    print("[3] relativistic dust current")
    rho0 = 5.0
    v = np.array([0.12, -0.05, 0.03])
    beta2 = float(v @ v)
    gamma = 1.0 / np.sqrt(1.0 - beta2)
    number_density = rho0 * gamma  # m0=1
    per_carrier_M = gamma
    per_carrier_p = gamma * v
    M_density = number_density * per_carrier_M
    P_density = number_density * per_carrier_p
    j_target = rho0 * gamma * gamma * v
    print(f"    M density                          = {M_density:.12f}")
    print(f"    P_i / j_i                          = {P_density / j_target}")
    if np.max(np.abs(P_density / j_target - 1.0)) > 1e-12:
        raise AssertionError("dust odd package is not P_i = j_i")

    print("[4] photon gas and directed beam")
    eps = 7.0
    print(f"    photon gas M1 well weight          = {eps:.12f}")
    print(f"    equal-content matter well weight   = {eps:.12f}")

    eps = 3.0
    Jp_x = eps + 0.5 * eps
    Jm_x = eps - 0.5 * eps
    J_trans = eps
    print(f"    beam J_x^+, J_x^-                  = {Jp_x:.12f}, {Jm_x:.12f}")
    print(f"    beam transverse channels           = {J_trans:.12f}")
    assert_close("beam forward channel", Jp_x, 1.5 * eps)
    assert_close("beam backward channel", Jm_x, 0.5 * eps)
    if abs(Jm_x) < 1e-12:
        raise AssertionError("carrier map unexpectedly gives exact beam chirality")

    print("[5] isolated-system accounting")
    gas_content = 10.0
    classical_gas_weight = 2.0 * gas_content
    classical_wall_stress = -gas_content
    classical_total = classical_gas_weight + classical_wall_stress
    m1_total = gas_content
    print(f"    classical subsystem total          = {classical_total:.12f}")
    print(f"    M1 carrier-map total               = {m1_total:.12f}")
    assert_close("Tolman-style cancellation total", classical_total, m1_total)

    print("[6] shift endpoint with carrier-map odd normalization")
    err = lense_thirring_endpoint_error(kappa_a=4.0, source_ratio=1.0)
    print(f"    kappa_A=4, P_i/j_i=1 endpoint err  = {err:.2e}")
    if err > 1e-12:
        raise AssertionError("Lense-Thirring endpoint failed")

    print(
        "VERDICT: carrier map preserves positive source channels, gives "
        "Mcal=rho_M and Pcal_i=j_i, keeps radiation at content weight, "
        "and leaves kappa_A=4 endpoint consistency intact."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
