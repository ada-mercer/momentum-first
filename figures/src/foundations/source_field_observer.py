#!/usr/bin/env python3
"""Adapted source -> field -> observer figure for Foundations.

Source adapted from:
- dist/source_field_observer_initial_figure.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(14, 8), dpi=220)
fig.patch.set_facecolor('#0b1020')
ax.set_facecolor('#0b1020')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')


def box(x, y, w, h, edge, title, body, tcolor='#e5e7eb'):
    rect = FancyBboxPatch((x, y), w, h,
                          boxstyle='round,pad=0.015,rounding_size=0.02',
                          linewidth=2.2, edgecolor=edge, facecolor=(0.07, 0.10, 0.18, 0.92))
    ax.add_patch(rect)
    ax.text(x + 0.02 * w, y + h - 0.12 * h, title, color=edge, fontsize=14, fontweight='bold', va='top')
    ax.text(x + 0.02 * w, y + h - 0.23 * h, body, color=tcolor, fontsize=12, va='top', linespacing=1.35)


def arrow(x1, y1, x2, y2, c='#93c5fd'):
    a = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='-|>', mutation_scale=18,
                        linewidth=2.2, color=c)
    ax.add_patch(a)


left_body = (
    "Directional source channels along a chosen direction n-hat\n"
    "J_n^+ and J_n^-\n\n"
    "Parity split:\n"
    "M_n = (J_n^+ + J_n^-)/2   (even / addition)\n"
    "P_n = J_n^+ - J_n^-       (odd / difference)\n\n"
    "Inverse:\n"
    "J_n^± = M_n ± 0.5 P_n"
)
box(0.05, 0.20, 0.28, 0.62, '#fbbf24', '1) Source layer', left_body)

mid_body = (
    "Stationary field intermediates\n\n"
    "theta_0  -> scalar-well side\n"
    "theta_i  -> shift side\n\n"
    "Packaged fields:\n"
    "G(r) = sqrt(1 - 2 theta_0(r))\n"
    "A_i(r) = alpha theta_i(r)\n"
    "B_ij = D_i A_j - D_j A_i"
)
box(0.37, 0.20, 0.27, 0.62, '#22d3ee', '2) Field packaging', mid_body)

right_body = (
    "Observer bookkeeping\n\n"
    "Contextual fermic scale:\n"
    "p_f,c = p_f G(r)\n\n"
    "Mechanical momentum:\n"
    "Pi_i = p_i - p_f,c A_i\n\n"
    "Local packaged magnitude:\n"
    "M_g,loc = sqrt(p_f,c^2 + gamma^ij Pi_i Pi_j)\n\n"
    "Stationary generator:\n"
    "H_g,stat = N M_g,loc - beta^i Pi_i"
)
box(0.68, 0.20, 0.27, 0.62, '#a78bfa', '3) Observer-side quantities', right_body)

arrow(0.33, 0.51, 0.37, 0.51)
arrow(0.64, 0.51, 0.68, 0.51)

ax.text(0.5, 0.94,
        "M1 stationary gravity grammar: source -> field -> observer bookkeeping",
        color='#e5f0ff', fontsize=17, ha='center', va='center', fontweight='bold')

ax.text(0.5, 0.08,
        "Foundations only: grammar and symbol roles. Detailed field equations and coefficient matching come later.",
        color='#cbd5e1', fontsize=11, ha='center')

out = Path(__file__).resolve().parents[2] / 'build' / 'foundations' / 'source-field-observer.png'
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, facecolor=fig.get_facecolor(), bbox_inches='tight')
print(out)
