#!/usr/bin/env python3
"""Checks for the M1 depth=stretch derivation and kappa_A pipeline.

Units set c = G_N = 1 where needed.  The script records the weak-field
coefficient logic:

    gamma_ij = (1 + 2 sigma theta0) delta_ij
    clock factor from stretched confined cycle = 1 / sqrt(1 + 2 sigma theta0)
    existing scalar clock package              = sqrt(1 - 2 theta0)

Matching their linear terms gives sigma = 1.  With odd-source normalization
eta = P_i / j_i = 1, boost consistency gives kappa_A = 2(1 + sigma) / eta = 4.
"""

from __future__ import annotations

import sys

import numpy as np


def assert_close(name: str, value: float, target: float, tol: float = 1e-12) -> None:
    if abs(value - target) > tol:
        raise AssertionError(f"{name}: got {value:.16g}, expected {target:.16g}")


def clock_from_linear_stretch(theta0: np.ndarray, sigma: float) -> np.ndarray:
    return 1.0 / np.sqrt(1.0 + 2.0 * sigma * theta0)


def scalar_clock_package(theta0: np.ndarray) -> np.ndarray:
    return np.sqrt(1.0 - 2.0 * theta0)


def kappa_from_boost(sigma: float, odd_source_ratio: float = 1.0) -> float:
    return 2.0 * (1.0 + sigma) / odd_source_ratio


def lense_thirring_endpoint_error(kappa_a: float, source_ratio: float) -> float:
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
    print("[1] weak-field depth=stretch coefficient")
    # d/dtheta sqrt(1 - 2 theta)|0 = -1.
    target_slope = -1.0
    # d/dtheta (1 + 2 sigma theta)^(-1/2)|0 = -sigma.
    sigma = -target_slope
    print(f"    target clock slope dG/dtheta0     = {target_slope:.12f}")
    print(f"    forced sigma                      = {sigma:.12f}")
    assert_close("sigma", sigma, 1.0)

    theta = np.array([1.0e-6, 1.0e-5, 1.0e-4, 1.0e-3])
    G_target = scalar_clock_package(theta)
    G_stretch = clock_from_linear_stretch(theta, sigma)
    err = np.max(np.abs(G_target - G_stretch))
    print(f"    max finite-theta mismatch         = {err:.3e}  (O(theta0^2), expected)")
    if err > 2.1e-6:
        raise AssertionError("linear stretch and scalar package disagree beyond O(theta^2)")

    print("[2] exact reciprocal-stretch package")
    exact_spatial_factor = 1.0 / (1.0 - 2.0 * theta)
    linear_sigma = (exact_spatial_factor[0] - 1.0) / (2.0 * theta[0])
    print(f"    gamma factor G^-2 at theta=1e-6   = {exact_spatial_factor[0]:.12f}")
    print(f"    inferred linear sigma             = {linear_sigma:.12f}")
    if abs(linear_sigma - 1.0) > 2e-6:
        raise AssertionError("exact reciprocal-stretch package did not linearize to sigma=1")

    print("[3] boost-consistency closure")
    odd_ratio = 1.0
    kappa_a = kappa_from_boost(sigma=sigma, odd_source_ratio=odd_ratio)
    print(f"    odd source ratio P_i/j_i          = {odd_ratio:.12f}")
    print(f"    kappa_A = 2(1+sigma)/ratio        = {kappa_a:.12f}")
    assert_close("kappa_A", kappa_a, 4.0)

    print("[4] PPN light-bending / Shapiro check")
    ppn_gamma = sigma
    deflection_over_gr = (1.0 + ppn_gamma) / 2.0
    shapiro_over_gr = (1.0 + ppn_gamma) / 2.0
    print(f"    PPN gamma                         = {ppn_gamma:.12f}")
    print(f"    light deflection / GR             = {deflection_over_gr:.12f}")
    print(f"    Shapiro delay / GR                = {shapiro_over_gr:.12f}")
    assert_close("PPN gamma", ppn_gamma, 1.0)
    assert_close("deflection ratio", deflection_over_gr, 1.0)
    assert_close("Shapiro ratio", shapiro_over_gr, 1.0)

    print("[5] Lense-Thirring endpoint")
    lt_err = lense_thirring_endpoint_error(kappa_a=kappa_a, source_ratio=odd_ratio)
    print(f"    endpoint err                      = {lt_err:.2e}")
    if lt_err > 1e-12:
        raise AssertionError("Lense-Thirring endpoint failed")

    print(
        "VERDICT: depth=stretch forces sigma=1 at weak-field order; with P_i=j_i, "
        "boost consistency derives kappa_A=4 and the standard PPN gamma=1 checks pass."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
