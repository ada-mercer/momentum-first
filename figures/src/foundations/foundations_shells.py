#!/usr/bin/env python3
r"""Adapted shell figure for Foundations.

Source adapted from:
- dist/core_momentum_p_eq_pf_true_dipole_surface_v2.py

Purpose:
- show fermic shell p_f,
- core shell M,
- directional shell p_{\hat n}(theta),
- and the directional channels p_{\hat n^+}, p_{\hat n^-}.
"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401


# --- Parameters ---
p_f = 1.0
p = p_f
M = np.sqrt(p_f**2 + p**2)

# directional shell radius profile relative to chosen direction n-hat
# r(theta) = M + (1/2) p cos(theta)
r_dir_max = M + 0.5 * p
r_dir_min = M - 0.5 * p

# --- Grid ---
th = np.linspace(0, np.pi, 340)
ph = np.linspace(0, 2 * np.pi, 340)
TH, PH = np.meshgrid(th, ph)

# remove the near half for a clean cutaway view
keep_half = np.cos(PH) >= 0

pf_back_region = np.cos(TH) <= -0.75
pf_front_region = ~pf_back_region

r_pf = p_f * np.ones_like(TH)
r_M = M * np.ones_like(TH)
r_dir = M + 0.5 * p * np.cos(TH)


def xyz(r, mask):
    x = r * np.cos(TH)
    y = r * np.sin(TH) * np.cos(PH)
    z = r * np.sin(TH) * np.sin(PH)
    return np.where(mask, x, np.nan), np.where(mask, y, np.nan), np.where(mask, z, np.nan)


Xpf, Ypf, Zpf = xyz(r_pf, keep_half)
Xpf_back, Ypf_back, Zpf_back = xyz(r_pf, keep_half & pf_back_region)
Xpf_front, Ypf_front, Zpf_front = xyz(r_pf, keep_half & pf_front_region)
Xm, Ym, Zm = xyz(r_M, keep_half)
Xd, Yd, Zd = xyz(r_dir, keep_half)

Delta = r_M - r_dir
lim = np.nanmax(np.abs(Delta))
val = (Delta + lim) / (2 * lim + 1e-12)
fc = cm.coolwarm(val)
fc[..., 3] = 0.42

fig = plt.figure(figsize=(13.5, 9), dpi=220)
ax = fig.add_subplot(111, projection="3d", computed_zorder=False)
fig.patch.set_facecolor("#0b1020")
ax.set_facecolor("#0b1020")

# core shell
ax.plot_surface(Xm, Ym, Zm, color="#3cf4ef", alpha=0.34, linewidth=0, edgecolor="none", antialiased=True, shade=True, zsort="average", zorder=2)
ax.plot_wireframe(Xm, Ym, Zm, rstride=10, cstride=10, color=(0.60, 1.0, 0.96, 0.46), linewidth=0.52, zorder=3)

# fermic shell, back cap first
ax.plot_surface(Xpf_back, Ypf_back, Zpf_back, color=(1.0, 0.94, 0.82, 1.0), linewidth=0, edgecolor="none", antialiased=True, shade=True, zsort="max", zorder=4)
ax.plot_wireframe(Xpf_back, Ypf_back, Zpf_back, rstride=10, cstride=10, color=(1.0, 0.94, 0.82, 0.58), linewidth=0.56, zorder=5)

# directional shell
ax.plot_surface(Xd, Yd, Zd, facecolors=fc, linewidth=0, edgecolor="none", antialiased=True, shade=False, zsort="average", zorder=6)
ax.plot_wireframe(Xd, Yd, Zd, rstride=10, cstride=10, color=(0.88, 0.92, 1.0, 0.30), linewidth=0.48, zorder=7)

# fermic shell front on top
ax.plot_surface(Xpf_front, Ypf_front, Zpf_front, color=(1.0, 0.94, 0.82, 1.0), linewidth=0, edgecolor="none", antialiased=True, shade=True, zsort="max", zorder=10)
ax.plot_wireframe(Xpf_front, Ypf_front, Zpf_front, rstride=10, cstride=10, color=(1.0, 0.94, 0.82, 0.58), linewidth=0.56, zorder=11)

# directional-channel vectors along chosen direction n-hat (shown here on x-axis)
x_core_plus, x_core_minus = M, -M
x_dir_plus, x_dir_minus = M + 0.5 * p, -(M - 0.5 * p)

ax.quiver(x_core_plus, 0, 0, x_dir_plus - x_core_plus, 0, 0, color="#eaf2ff", linewidth=6.2, arrow_length_ratio=0.33, alpha=0.45, zorder=30)
ax.quiver(x_core_minus, 0, 0, x_dir_minus - x_core_minus, 0, 0, color="#ffe8e8", linewidth=6.2, arrow_length_ratio=0.33, alpha=0.45, zorder=30)
ax.quiver(x_core_plus, 0, 0, x_dir_plus - x_core_plus, 0, 0, color="#60a5fa", linewidth=3.8, arrow_length_ratio=0.38, zorder=31)
ax.quiver(x_core_minus, 0, 0, x_dir_minus - x_core_minus, 0, 0, color="#ef4444", linewidth=3.8, arrow_length_ratio=0.38, zorder=31)
ax.scatter([x_dir_plus, x_dir_minus], [0, 0], [0, 0], c=["#60a5fa", "#ef4444"], s=46, zorder=32)

# radial arrows from fermic shell to core shell
radial_gap = M - p_f
step_deg = 20
th_samples = np.deg2rad(np.arange(20, 161, step_deg))
ph_samples = np.deg2rad(np.arange(0, 360, step_deg))
for ti, th0 in enumerate(th_samples):
    for pi, ph0 in enumerate(ph_samples):
        cph = np.cos(ph0)
        if cph < 0:
            continue
        cut_proximity = 1.0 - np.clip(cph, 0.0, 1.0)
        if cut_proximity < 0.35 and ((ti + pi) % 4 != 0):
            continue
        if 0.35 <= cut_proximity < 0.65 and ((ti + pi) % 2 != 0):
            continue
        nx = np.cos(th0)
        ny = np.sin(th0) * cph
        nz = np.sin(th0) * np.sin(ph0)
        sx, sy, sz = p_f * nx, p_f * ny, p_f * nz
        vx, vy, vz = radial_gap * nx, radial_gap * ny, radial_gap * nz
        lw = 0.8 + 1.2 * cut_proximity
        a = 0.35 + 0.55 * cut_proximity
        ax.quiver(sx, sy, sz, vx, vy, vz, color="#22d3ee", linewidth=lw, arrow_length_ratio=0.18, alpha=a)

ax.text(x_dir_plus + 0.07, 0.15, 0.05, r"$p_{\hat n^+}$", color="#bfdbfe", fontsize=13)
ax.text(x_dir_minus - 0.52, -0.20, 0.05, r"$p_{\hat n^-}$", color="#fecaca", fontsize=13)

ax.text2D(0.02, 0.945, r"$p_{\hat n}(\theta)=M+\frac{1}{2}p\cos\theta$", transform=ax.transAxes, color="#dbeafe", fontsize=12)
ax.text2D(0.02, 0.885, r"fermic shell ($p_f$)", transform=ax.transAxes, color="#ffd29b", fontsize=11)
ax.text2D(0.02, 0.858, r"core shell ($M$)", transform=ax.transAxes, color="#8ef1f3", fontsize=11)
ax.text2D(0.02, 0.831, r"directional shell ($p_{\hat n}$)", transform=ax.transAxes, color="#c9d4ff", fontsize=11)
ax.text2D(0.02, 0.801, r"Here the chosen direction $\hat n$ is drawn along the $x$-axis.", transform=ax.transAxes, color="#a5b4fc", fontsize=10)

assert abs(M - np.sqrt(2) * p_f) < 1e-12
assert abs(r_dir_max - (M + 0.5 * p)) < 1e-12
assert abs(r_dir_min - (M - 0.5 * p)) < 1e-12

ax.set_xlim(-2.2, 2.8)
ax.set_ylim(-2.0, 2.0)
ax.set_zlim(-2.0, 2.0)
ax.set_box_aspect((1.52, 1.1, 1.1))
ax.view_init(elev=20, azim=-58)
ax.grid(False)
for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
    axis.pane.set_facecolor((0.07, 0.10, 0.18, 0.08))
    axis._axinfo["grid"]["linewidth"] = 0.0

ax.set_xlabel("x", color="#9cb5d6", labelpad=8)
ax.set_ylabel("y", color="#9cb5d6", labelpad=8)
ax.set_zlabel("z", color="#9cb5d6", labelpad=8)
ax.tick_params(colors="#8ea8cc", labelsize=9)
ax.set_title("Fermic / Core / directional shells", color="#e5f0ff", fontsize=13, pad=16)

out = Path(__file__).resolve().parents[2] / "build" / "foundations" / "foundations-shells.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, facecolor=fig.get_facecolor(), bbox_inches="tight")
print(out)
