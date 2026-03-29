#!/usr/bin/env python3
"""Momentum triangle figure for Foundations.

Styled to match the manuscript's dark-theme figure language.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


fig, ax = plt.subplots(figsize=(10, 7), dpi=220)
fig.patch.set_facecolor("#0b1020")
ax.set_facecolor("#0b1020")
ax.set_xlim(-0.2, 1.95)
ax.set_ylim(-0.2, 1.55)
ax.set_aspect("equal")
ax.axis("off")

# vector endpoints
origin = (0.0, 0.0)
pf_end = (0.0, 1.0)
p_end = (1.28, 0.0)
M_end = (1.28, 1.0)


def arrow(start, end, color, lw=3.2, style="-|>", alpha=1.0, ms=18):
    a = FancyArrowPatch(start, end, arrowstyle=style, mutation_scale=ms, linewidth=lw, color=color, alpha=alpha)
    ax.add_patch(a)


# helper grid / triangle guides
ax.plot([origin[0], p_end[0]], [origin[1], p_end[1]], color=(0.80, 0.86, 0.96, 0.20), lw=1.8)
ax.plot([p_end[0], M_end[0]], [p_end[1], M_end[1]], color=(0.80, 0.86, 0.96, 0.20), lw=1.8)
ax.plot([origin[0], pf_end[0]], [origin[1], pf_end[1]], color=(0.80, 0.86, 0.96, 0.20), lw=1.8)
ax.plot([origin[0], M_end[0]], [origin[1], M_end[1]], color=(0.80, 0.86, 0.96, 0.12), lw=7.0)

# main arrows
arrow(origin, pf_end, "#fbbf24")
arrow(origin, p_end, "#22d3ee")
arrow(origin, M_end, "#a78bfa", lw=3.8, ms=20)

# right-angle marker
ax.plot([0.0, 0.12], [0.12, 0.12], color="#cbd5e1", lw=1.4)
ax.plot([0.12, 0.12], [0.0, 0.12], color="#cbd5e1", lw=1.4)

# labels
ax.text(-0.03, 1.05, r"$p_f$", color="#fde68a", fontsize=16, ha="right", va="bottom")
ax.text(1.32, -0.02, r"$p$", color="#67e8f9", fontsize=16, ha="left", va="top")
ax.text(1.36, 1.04, r"$M$", color="#c4b5fd", fontsize=17, ha="left", va="bottom")

ax.text(0.20, 0.54, "fermic momentum", color="#fde68a", fontsize=13, rotation=90, va="center")
ax.text(0.58, -0.10, "bosic momentum", color="#67e8f9", fontsize=13, ha="center")
ax.text(0.73, 0.63, "total momentum content", color="#ddd6fe", fontsize=13, rotation=38, ha="center")

ax.text(1.45, 1.40, "Momentum Triangle", color="#e5f0ff", fontsize=18, ha="right", fontweight="bold")
ax.text(1.45, 1.27, r"$M^2 = p_f^2 + p^2$", color="#cbd5e1", fontsize=15, ha="right")
ax.text(1.45, 1.14, "Inertial baseline composition of a particle's momentum content", color="#94a3b8", fontsize=11, ha="right")

out = Path(__file__).resolve().parents[2] / "build" / "foundations" / "momentum-triangle.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, facecolor=fig.get_facecolor(), bbox_inches="tight")
print(out)
