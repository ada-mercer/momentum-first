"""Generate the two registered QM figures from the existing chapter diagram source.

Run using momentum-first/.venv/bin/python. Equations follow the working
QM derivations 4.3A and 4.5A. No generative-image model is used.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'figures/build/quantum-mechanics'
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12,
                     'mathtext.fontset': 'dejavusans', 'svg.fonttype': 'none'})
ink = '#243047'
blue = '#276896'
purple = '#725397'
orange = '#ac6425'

# Same diagonal momentum distribution, distinct Fourier position readouts.
y = np.linspace(0, 1, 1001)
phase0 = 1 + np.cos(4*np.pi*y)
phasepi = 1 + np.cos(4*np.pi*y + np.pi)
fig, axes = plt.subplots(2, 1, figsize=(8.0, 6.3),
                         gridspec_kw={'height_ratios': [1, 1.8]},
                         layout='constrained')
ax = axes[0]
ax.bar([0, 1], [.5, .5], width=.16, color=blue)
ax.set_xticks([0,1], ['0', r'$\hbar k$'])
ax.set_xlim(-.55,1.55); ax.set_ylim(0,.65)
ax.set_yticks([0,.5]); ax.set_ylabel('Probability')
ax.set_title('(a) The same momentum probabilities', loc='left', color=ink)
ax = axes[1]
ax.plot(y, phase0, color=blue, lw=2.5, label=r'Coherent: $\vartheta=0$')
ax.plot(y, phasepi, color=purple, lw=2.5, ls='--', label=r'Coherent: $\vartheta=\pi$')
ax.axhline(1, color=orange, lw=2, ls=':', label='Incoherent mixture')
ax.set(xlim=(0,1), ylim=(-.06,2.4), xlabel=r'Position $x/\mathscr{L}$',
       ylabel=r'Density $\mathscr{L}|\Psi|^2$')
ax.set_yticks([0,1,2]); ax.set_title('(b) Different interference patterns', loc='left',color=ink)
ax.legend(loc='upper center', ncols=1, fontsize=10, framealpha=.94)
for ax in axes:
 ax.spines[['top','right']].set_visible(False)
 ax.tick_params(colors=ink); ax.grid(axis='y', alpha=.15)
for ext in ['png','pdf','svg']:
 fig.savefig(OUT/f'qm-interference.{ext}',dpi=210,bbox_inches='tight',facecolor='white')
plt.close(fig)

# Preserve the old bridge's three-panel rhythm, with corrected physics.
fig, ax = plt.subplots(figsize=(9.4, 8.3))
ax.set(xlim=(0,1),ylim=(0,1)); ax.axis('off')
rows=[(.72,.25,orange,'Local momentum shell'),
      (.395,.25,blue,'One static reference comparison'),
      (.07,.25,purple,'Evolution through a varying static map')]
for bottom,height,color,title in rows:
 ax.add_patch(FancyBboxPatch((.025,bottom),.95,height,
   boxstyle='round,pad=0.012,rounding_size=0.018',facecolor=color+'0D',
   edgecolor=color,lw=1.5))
 ax.text(.05,bottom+height-.04,title,color=color,fontsize=15,fontweight='bold',va='center')
 ax.plot([.48,.48],[bottom+.028,bottom+height-.075],color=color,alpha=.35)
# left: definitions; right: result, preserving reusable panel architecture.
ax.text(.065,.835,r'$p_f,\quad \mathbf{p}_{\mathrm{local}}$',fontsize=18,va='center',color=ink)
ax.text(.065,.776,'One local orthonormal frame',fontsize=11,va='center',color=ink)
ax.text(.515,.835,r'$M^2=p_f^2+|\mathbf{p}_{\mathrm{local}}|^2$',fontsize=17,va='center',color=ink)
ax.text(.515,.776,'Positive local core',fontsize=11,va='center',color=ink)
ax.text(.065,.518,r'$N=\phi^0{}_0,\quad \phi^a{}_i=b\delta^a{}_i$',fontsize=15,va='center',color=ink)
ax.text(.065,.46,r'$p_{f,r}=Np_f,\quad \mathbf{p}_r=(N/b)\mathbf{p}_{\mathrm{coord}}$',fontsize=13,va='center',color=ink)
ax.text(.515,.518,r'$M_t=M_r=NM$',fontsize=19,va='center',color=ink)
ax.text(.515,.46,'Both momentum roles use one comparison',fontsize=10.5,va='center',color=ink)
ax.text(.065,.186,r'$\psi=b^{3/2}\Psi,\quad F=N/b$',fontsize=15,va='center',color=ink)
ax.text(.065,.129,'Coordinate-volume normalization',fontsize=11,va='center',color=ink)
ax.text(.51,.194,r'$\widehat{M}_t=\beta Np_f+\frac{1}{2}\{F,\boldsymbol{\alpha}\cdot\widehat{\mathbf{p}}_{\mathrm{coord}}\}$',fontsize=13,va='center',color=ink)
ax.text(.515,.129,r'Flux: $cF\psi^\dagger\boldsymbol{\alpha}\psi$',fontsize=13,va='center',color=ink)
for y0,y1,color in [(.706,.658,orange),(.382,.333,blue)]:
 ax.add_patch(FancyArrowPatch((.5,y0),(.5,y1),arrowstyle='-|>',mutation_scale=19,color=color,lw=1.6))
for ext in ['png','pdf','svg']:
 fig.savefig(OUT/f'qm-operator-bridge.{ext}',dpi=210,bbox_inches='tight',facecolor='white')
plt.close(fig)
checks={'wave_number_times_length':float(4*np.pi),
        'phase0_integral':float(np.trapezoid(phase0,y)),
        'phasepi_integral':float(np.trapezoid(phasepi,y)),
        'momentum_weights':[.5,.5],
        'outputs':['qm-interference.png', 'qm-operator-bridge.png']}
print(json.dumps(checks,indent=2))
print('Generated two figure sets under',OUT)
