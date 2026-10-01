"""Candidate-only explanatory schematics; no canonical asset writes.

Geometry follows the selected two-phase torus and mixed-coordinate helix
contracts. Radii, speeds and scalar waves are illustrative, not fitted data.
Run with momentum-first/.venv/bin/python from any directory.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from torus_mesh import parameter_lines,mesh_record
MESH_RECORDS=[]
CURRENT_TORI=[]

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets'
OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans',
                     'figure.facecolor': 'white', 'savefig.facecolor': 'white'})
BLUE, AMBER, INK = '#2263a5', '#be7018', '#25364a'

def xyz(u, v, rb=2.2, rf=.65):
    return np.array([(rb+rf*np.cos(v))*np.cos(u),
                     (rb+rf*np.cos(v))*np.sin(u), rf*np.sin(v)])

def torus(ax, rb=2.2, rf=.65, lim=3.1):
    lines=[xyz(u,v,rb,rf).T for _,_,u,v in parameter_lines()]
    assert len(lines)==72
    ax.add_collection3d(Line3DCollection(lines,colors='#9eaab5',alpha=.28,linewidths=.45),autolim=False)
    CURRENT_TORI.append((rb,rf))
    ax.set(xlim=(-lim,lim),ylim=(-lim,lim),zlim=(-lim,lim))
    ax.set_box_aspect((1,1,1))
    ax.view_init(elev=31,azim=-65)
    ax.set_axis_off()


def save(fig,name):
    MESH_RECORDS.append(mesh_record('assets/'+name,len(CURRENT_TORI)))
    CURRENT_TORI.clear()
    fig.savefig(OUT/name,dpi=190,bbox_inches='tight')
    plt.close(fig)

s=np.linspace(0,1,1201)
r=xyz(4*np.pi*s,2*np.pi*s)
assert np.allclose(r[:,0],r[:,-1])
assert not np.allclose(r[:,0],r[:,600])

fig=plt.figure(figsize=(11,4.7))
a=fig.add_subplot(121,projection='3d'); torus(a)
t=np.linspace(0,2*np.pi,400)
a.plot(*xyz(t,np.zeros_like(t)),color=BLUE,lw=2,alpha=.85)
a.plot(*xyz(np.full_like(t,np.pi/2),t),color=AMBER,lw=2.4)
a.plot(*r[:,:601],color=INK,lw=2.4)
a.plot(*r[:,600:],color=INK,lw=1.7,ls='--',alpha=.58)
for i,label in [(0,'A'),(600,'B')]:
    a.scatter(*r[:,i],s=32,color=INK)
    a.text(*(r[:,i]+np.array([.18,0,.25])),label,color=INK,fontsize=12,
           bbox=dict(facecolor='white',edgecolor='none',alpha=.85,pad=.5))
a.text2D(.02,.93,'Internal two-cycle picture',transform=a.transAxes,fontweight='bold')
a.text2D(.02,.08,'Blue: major / bosic cycle',color=BLUE,transform=a.transAxes)
a.text2D(.02,.02,'Amber: minor / fermic cycle',color=AMBER,transform=a.transAxes)
b=fig.add_subplot(122)
b.plot(2*s[:601],s[:601],color=INK,lw=2.8)
b.plot(2*s[600:],s[600:],color=INK,lw=2,ls='--',alpha=.6)
for x,y,label in [(0,0,'A'),(1,.5,'B'),(2,1,"A: return")]:
    b.scatter(x,y,color=INK,s=35)
    b.annotate(label,(x,y),xytext=(6,10) if x<2 else (-7,-22),
               ha='left' if x<2 else 'right',textcoords='offset points')
b.axvline(1,color=BLUE,alpha=.25)
b.set(xlim=(-.12,2.32),ylim=(-.12,1.13),xlabel='Bosic turns',ylabel='Fermic turns',
      title='Unwrapped phase chart',xticks=[0,1,2],yticks=[0,.5,1])
b.grid(alpha=.16)
fig.text(.56,.01,'Solid: first turn     Dashed: completing turn',fontsize=10,color=INK)
fig.subplots_adjust(wspace=.18,bottom=.19)
save(fig,'two-cycles.png')

# A separate equal-time comparison, WITHOUT assuming a bosic phase frequency.
# Momentum units: p_f = p_k = p = 1; c*Delta t = 6 display distance units.
chi_values=[1.,2./3.]
speeds=[chi**2/np.sqrt(1.+chi**2) for chi in chi_values]
advances=6*np.array(speeds)
fig=plt.figure(figsize=(11,6.4))
grid=fig.add_gridspec(2,2,width_ratios=[1,1.5],wspace=.2,hspace=.26)
for j,chi in enumerate(chi_values):
    a=fig.add_subplot(grid[j,0],projection='3d')
    rb=2.2/chi;rf=.65
    torus(a,rb,rf,lim=4.1)
    a.plot(*xyz(t,np.zeros_like(t),rb,rf),color=BLUE,lw=2.1)
    a.plot(*xyz(np.full_like(t,np.pi/2),t,rb,rf),color=AMBER,lw=2.4)
    a.text2D(.03,.97,'Reference bosonic geometry' if j==0 else 'Dilated bosonic geometry',transform=a.transAxes,fontweight='bold')
    a.text2D(.03,.02,'Reference major scale' if j==0 else 'Larger major scale; same minor scale',transform=a.transAxes,fontsize=10)
    a=fig.add_subplot(grid[j,1]);a.set(xlim=(-.15,5),ylim=(-.8,.85));a.set_axis_off()
    a.annotate('',(4.8,0),(0,0),arrowprops=dict(arrowstyle='->',color='#8a949e',lw=1.3))
    a.text(4.85,0,r'$+\hat{k}$',va='center')
    steps=np.linspace(0,advances[j],5)
    a.plot(steps,np.zeros_like(steps),color=BLUE,lw=3,marker='o',ms=5)
    for x in [0,advances[j]]:a.plot([x,x],[-.33,-.23],color=AMBER,lw=1.4)
    a.annotate('',(advances[j],-.28),(0,-.28),arrowprops=dict(arrowstyle='<->',color=AMBER,lw=1.5))
    a.text(advances[j]/2,-.47,r'advance during $\Delta t$',ha='center',color=AMBER)
    a.text(0,.22,'start',fontsize=10)
    a.text(advances[j],.22,r'after $\Delta t$',ha='center',fontsize=10)
    a.text(0,.68,'Same momentum content; reference response' if j==0 else 'Same momentum content; reduced translation',fontweight='bold',fontsize=11)
    a.text(0,-.76,'Dots: equal reference-time steps',fontsize=10)
fig.text(.12,.015,r'Matched $p$ and $p_f$; common internal display scale and external distance scale.',fontsize=10)
fig.subplots_adjust(top=.94,bottom=.1)
save(fig,'bosonic-dilation-response.png')

fig=plt.figure(figsize=(12,4.5))
for j,(rb,rf,title,desc) in enumerate([
    (2.2,.65,'Reference','Common display scale across panels'),
    (2.2,1.,'Fermionic dilation','Minor scale grows; major stays fixed'),
    (3.,.65,'Bosonic dilation','Major scale grows; minor stays fixed')]):
    ax=fig.add_subplot(1,3,j+1,projection='3d');torus(ax,rb,rf,lim=3.9)
    ax.plot(*xyz(t,np.zeros_like(t),rb,rf),color=BLUE,lw=2)
    ax.plot(*xyz(np.full_like(t,np.pi/2),t,rb,rf),color=AMBER,lw=2.4)
    ax.text2D(.03,.93,title,transform=ax.transAxes,fontweight='bold')
    ax.text2D(.03,.06,desc,transform=ax.transAxes,fontsize=10)
fig.subplots_adjust(wspace=.01)
save(fig,'two-dilations.png')

# Scalar amplitude is periodic in normalized arclength along the SAME loop.
lengths=np.r_[0,np.cumsum(np.linalg.norm(np.diff(r,axis=1),axis=0))]
q=lengths/lengths[-1]
w=np.cos(2*np.pi*3*q)
points=r.T
segments=np.stack([points[:-1],points[1:]],axis=1)
fig=plt.figure(figsize=(11,4.6))
a=fig.add_subplot(121,projection='3d');torus(a)
lc=Line3DCollection(segments,cmap='coolwarm',linewidths=3.2)
lc.set_array((w[:-1]+w[1:])/2);lc.set_clim(-1,1);a.add_collection3d(lc)
a.text2D(.02,.93,'Scalar amplitude on the loop',transform=a.transAxes,fontweight='bold')
a.text2D(.02,.12,'Loop shown at the first instant',transform=a.transAxes,fontsize=10)
a.scatter(*r[:,0],s=32,color=INK)
a.text(*(r[:,0]+np.array([.12,0,.22])),'start',fontsize=10)
i=45
direction=r[:,i+1]-r[:,i]
direction=.45*direction/np.linalg.norm(direction)
a.quiver(*r[:,i],*direction,color=INK,arrow_length_ratio=.4)
cax=fig.add_axes([.17,.13,.23,.024])
cb=fig.colorbar(lc,cax=cax,orientation='horizontal',ticks=[-1,0,1])
cb.set_label('Scalar amplitude (colour)',fontsize=9)
cb.ax.tick_params(labelsize=9)
b=fig.add_subplot(122)
b.plot(q,w,color=BLUE,lw=2,label='First instant')
b.plot(q,np.cos(2*np.pi*3*q-np.pi/2),color=AMBER,lw=1.8,ls='--',label='Later phase')
b.set(xlim=(0,1),ylim=(-1.25,1.25),xlabel='Fraction of total loop length',ylabel='Illustrative scalar amplitude',title='The loop unwrapped')
b.grid(alpha=.16);b.legend(loc='lower center',bbox_to_anchor=(.5,-.38),ncol=2,frameon=False)
fig.subplots_adjust(wspace=.2,bottom=.23)
save(fig,'loop-wave.png')
checks={'internal_return':bool(np.allclose(r[:,0],r[:,-1])),
        'first_bosic_return_is_incomplete':bool(not np.allclose(r[:,0],r[:,600])),
        'periodic_scalar_amplitude':bool(np.isclose(w[0],w[-1])),
        'wave_mode':3,'figure_count':4,
        'dilation_chi':chi_values,
        'dilation_coordinate_speed_over_c':speeds,
        'dilation_major_radius_ratio':[1/x for x in chi_values],
        'dilation_equal_time_advance_ratio':float(advances[1]/advances[0]),
        'method':'Prescribed geometry and periodic functions; no physical simulation or fitted data.'}
(ROOT/'validation/figure-checks.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))

(ROOT/'validation/mesh-basic.json').write_text(json.dumps(MESH_RECORDS,indent=2)+'\n')
