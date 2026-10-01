"""Candidate-only torus plates using the existing geometry3d/PyVista backend.

Standing-mode geometry and shared drawing helpers retained from v4.
The deformation is prescribed, not a solved M1 mode.
No new renderer, dependencies, shared-library edits, or animation encoder.
"""
from torus_mesh import parameter_lines,mesh_record,MAJOR_DIVISIONS,MINOR_DIVISIONS
from pathlib import Path
import sys
import json
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
REPO = next(p for p in ROOT.parents if (p / '.git').exists())
sys.path.insert(0, str(REPO / 'figures/lib'))
from geometry3d.scene_spec import SceneSpec, SceneObject, SceneAnnotation, FigureLayout
from geometry3d.backends import render_scene_with_backend
from geometry3d.cameras import CAMERA_PRESETS, CameraPreset

RB, RF = 2.1, 0.65
EPS_B, EPS_F = 0.18, 0.24
NU, NV = 321, 161
U, V = np.meshgrid(np.linspace(0, 2*np.pi, NU), np.linspace(0, 2*np.pi, NV))
K = np.array([0., 1., 0.])
# Candidate-local presets, registered only in this rendering process.
CAMERA_PRESETS['candidate-history'] = CameraPreset('candidate-history', 35, 18,
    projection_mode='orthographic', orthographic_scale=3.9)
CAMERA_PRESETS['candidate-mode'] = CameraPreset('candidate-mode', 40, 24,
    projection_mode='orthographic', orthographic_scale=3.2)


def xyz(u, v, phase=None, centre=0., lift=0.):
    """Local torus normal is mapped to +Y = k. Rows end in xyz components."""
    radius = np.full_like(np.asarray(u)+np.asarray(v), RF, dtype=float)
    if phase is not None:
        radius *= 1+(EPS_B*np.cos(2*u)+EPS_F*np.cos(2*v))*np.cos(phase)
    radius += lift
    return np.stack(((RB+radius*np.cos(v))*np.cos(u),
                     centre+radius*np.sin(v),
                     -(RB+radius*np.cos(v))*np.sin(u)), axis=-1)


def curve_object(name, points, color, width=0.009, alpha=1.):
    """Smooth thin tube expressed through existing sampled_surface primitive."""
    tangent = np.gradient(points, axis=0)
    tangent /= np.linalg.norm(tangent, axis=1)[:, None]
    normal = np.cross(tangent, np.array([0., 0., 1.]))
    weak = np.linalg.norm(normal, axis=1) < 1.e-5
    normal[weak] = np.cross(tangent[weak], np.array([1., 0., 0.]))
    normal /= np.linalg.norm(normal, axis=1)[:, None]
    other = np.cross(tangent, normal)
    a = np.linspace(0, 2*np.pi, 9)
    mesh = points[:, None, :]+width*(normal[:, None, :]*np.cos(a)[None, :, None]
                                    +other[:, None, :]*np.sin(a)[None, :, None])
    return SceneObject(name, 'sampled_surface', dict(x=mesh[..., 0], y=mesh[..., 1],
        z=mesh[..., 2], color=color, alpha=alpha, shade=True, ambient=.65))


def torus_objects(name, phase=None, centre=0., alpha=1., grid_alpha=.55):
    mesh = xyz(U, V, phase, centre)
    objects = [SceneObject(name, 'sampled_surface', dict(x=mesh[..., 0], y=mesh[..., 1],
        z=mesh[..., 2], color='#b5a0cc', alpha=alpha, shade=True, ambient=.42))]
    # Decouple surface tessellation from the visible coordinate grid. Each
    # visible line remains fully sampled: no coarse chords through the surface.
    for axis,j,u,v in parameter_lines():
        points=xyz(u,v,phase,centre,lift=.009)
        objects.append(curve_object(f'{name}-{axis}-{j}',points,'#614575',.006,grid_alpha))
    return objects


def arrow(name, start, end, color='#16869a', width=1.8):
    d = np.asarray(end)-np.asarray(start)
    return SceneObject(name, 'vector_set', dict(x=[start[0]], y=[start[1]], z=[start[2]],
        u=[d[0]], v=[d[1]], w=[d[2]], color=color, linewidth=width,
        arrow_length_ratio=.025, tip_radius_scale=.7, ambient=.5))


def label(name, text, position, size=30, color='#27364a'):
    return SceneAnnotation(name, 'text3d', text, dict(x=position[0], y=position[1],
        z=position[2], fontsize=size, color=color))


def mode_scene(phase):
    objects = torus_objects('mode', phase)
    # Highlight the very same tube cross-section shown below the 3D portrait.
    vv = np.linspace(0, 2*np.pi, NV)
    objects.append(curve_object('section-cut', xyz(np.full_like(vv, np.pi/4), vv,
        phase, lift=.028), '#c77726', .025))
    objects.append(arrow('k-axis', (0., 0., 0.), (0., 3.2, 0.), width=1.4))
    return SceneSpec('torus-cycle', 'standing-mode', 'candidate-mode', 'light-manuscript',
        layout=FigureLayout(figsize=(4.5, 3.7), dpi=220, xlim=(-3., 3.),
            ylim=(-1.6, 1.6), zlim=(-3., 3.), show_axes=False),
        objects=objects, annotations=[label('k', 'k̂', (0., 3.35, 0.), 34, '#16869a')],
        metadata={'phase':float(phase), 'epsilon_b':EPS_B, 'epsilon_f':EPS_F,
            'prescribed_standing_mode':True, 'minor_angular_mode_number':2, 'physical_mode_solved':False})


def cross_section(phase, out):
    v = np.linspace(0, 2*np.pi, 641)
    # u=pi/4 makes cos(2u)=0, isolating the minor-cycle contribution.
    r = RF*(1+EPS_F*np.cos(2*v)*np.cos(phase))
    fig, ax = plt.subplots(figsize=(4.5, 2.0), dpi=220)
    ax.plot(RF*np.cos(v), RF*np.sin(v), '--', color='#96a1b0', lw=1.4)
    ax.plot(r*np.cos(v), r*np.sin(v), color='#c77726', lw=2.5)
    ax.plot(0, 0, '.', color='#687586', ms=5)
    if abs(np.cos(phase)) > .9:
        outer = RF*(1+EPS_F*np.cos(phase))
        ax.plot([RF,outer],[0,0],color='#7c4a12',lw=1.4)
        for x in [RF,outer]: ax.plot([x,x],[-.065,.065],color='#7c4a12',lw=1.4)
        ax.annotate(r'$\varepsilon_f r_f$', xy=((RF+outer)/2, 0), xytext=(1.07, .55),
                    fontsize=16, color='#7c4a12', ha='center',
                    arrowprops=dict(arrowstyle='-', color='#7c4a12', lw=.8))
    else:
        ax.text(.98, .45, 'zero\ndisplacement', fontsize=11, color='#566174', ha='center')
    ax.set_aspect('equal'); ax.set_xlim(-1., 1.55); ax.set_ylim(-.91, .91); ax.axis('off')
    fig.subplots_adjust(left=.02, right=.98, bottom=.02, top=.98)
    fig.savefig(out, facecolor='white'); plt.close(fig)


def verify():
    for tau in np.linspace(0, 2*np.pi, 17):
        rr = RF*(1+(EPS_B*np.cos(2*U)+EPS_F*np.cos(2*V))*np.cos(tau))
        assert rr.min()>0 and rr.max()<RB
        g = xyz(U,V,tau)
        assert np.allclose(g[0],g[-1]) and np.allclose(g[:,0],g[:,-1])
    assert np.allclose(xyz(U,V,0),xyz(U,V,2*np.pi))
    assert np.allclose(xyz(U,V,np.pi/2),xyz(U,V))
    base=xyz(U,V); first=xyz(U,V,0); opposite=xyz(U,V,np.pi)
    assert np.allclose(first-base,-(opposite-base))
    v=np.linspace(0,2*np.pi,321)
    r=RF*(1+EPS_F*np.cos(2*v))
    assert np.isclose(r.max()-RF,EPS_F*RF)
    # Separately sampled guide curves are periodic and retain smooth resolution.
    assert np.allclose(xyz(np.zeros_like(v),v,0)[0],xyz(np.zeros_like(v),v,0)[-1])
    result={'backend':'existing geometry3d/pyvista3d', 'new_dependencies':[],
        'surface_samples':[NU,NV], 'visible_coordinate_lines':[MAJOR_DIVISIONS,MINOR_DIVISIONS],
        'guides_sampled_independently_of_surface_density':True,
        'standing_pattern':True,'minor_cycle_amplitude_present':True,
        'epsilon_b':EPS_B,'epsilon_f':EPS_F,'fermic_display_amplitude':EPS_F*RF,
        'mode_periodic':True,'undeformed_quarter_cycle':True,
        'opposite_extremes_antisymmetric':True,'positive_radius_and_open_ring':True,
        'physical_eigenmode_solved':False,'animation_encoded':False}
    (ROOT/'validation/mode-checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


def main():
    verify()
    frames=[]; sections=[]
    for j, phase in enumerate([0., np.pi/2, np.pi]):
        out=ROOT/f'mode-study/keyframe-{j}.png'
        render_scene_with_backend('pyvista3d',scene=mode_scene(phase),output_path=out,
            camera_name='candidate-mode',style_name='light-manuscript')
        section=ROOT/f'mode-study/section-{j}.png'
        cross_section(phase,section)
        frames.append(Image.open(out).convert('RGB'))
        sections.append(Image.open(section).convert('RGB'))
    w,h=frames[0].size; sh=sections[0].height
    plate=Image.new('RGB',(3*w,h+sh+130),'white')
    draw=ImageDraw.Draw(plate)
    font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
    bold='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
    for j,(frame,section,title) in enumerate(zip(frames,sections,
            ['First extreme','Undeformed crossing','Opposite extreme'])):
        draw.text((j*w+w/2,22),title,anchor='mt',font=ImageFont.truetype(bold,34),fill='#27364a')
        plate.paste(frame,(j*w,66));plate.paste(section,(j*w,h+125))
    draw.text((3*w/2,h+83),'Fermic amplitude · orange tube section',anchor='mt',
              font=ImageFont.truetype(font,31),fill='#805024')
    plate.save(ROOT/'mode-study/standing-mode-storyboard.png')
    (ROOT/'validation/mesh-mode.json').write_text(json.dumps([mesh_record('mode-study/standing-mode-storyboard.png',len(frames))],indent=2)+'\n')


if __name__=='__main__':
    main()
