"""Geometry/loop separation and momentum-scaled local chart with free waves.

Existing Matplotlib route, shared 48x24 torus grid. The local chart is explicitly
rescaled; it does not identify the ordinary torus metric with the momentum norm.
The packet uses first-order free dispersion around its central momentum.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,ConnectionPatch
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from mpl_toolkits.mplot3d import proj3d
from torus_mesh import parameter_lines,mesh_record,MAJOR_DIVISIONS,MINOR_DIVISIONS

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets'
BLUE,AMBER,INK='#2263a5','#be7018','#25364a'
PHASE='#8b3f91'
RB,RF=2.2,.65
P,PF,C,HBAR=1.,1.,1.,.2  # executable values only; manuscript retains p-family
CORE=np.hypot(P,PF)
VG=C*P/CORE; VPH=C*CORE/P
DT=2.;SIGMA=2.
U0,V0,DELTA=np.pi/2,np.pi/4,.3
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,
                     'figure.facecolor':'white','savefig.facecolor':'white'})

def xyz(u,v):
    return np.array([(RB+RF*np.cos(v))*np.cos(u),
                     (RB+RF*np.cos(v))*np.sin(u),RF*np.sin(v)])

def torus(ax):
    lines=[xyz(u,v).T for _,_,u,v in parameter_lines()]
    ax.add_collection3d(Line3DCollection(lines,colors='#9eaab5',alpha=.28,linewidths=.45),autolim=False)
    ax.set(xlim=(-3.1,3.1),ylim=(-3.1,3.1),zlim=(-3.1,3.1))
    ax.set_box_aspect((1,1,1));ax.view_init(elev=31,azim=-65);ax.set_axis_off()

S=np.linspace(0,1,1201)
LOOP=xyz(4*np.pi*S,2*np.pi*S)

def loop(ax,markers=True):
    ax.plot(*LOOP[:,:601],color=INK,lw=2.2)
    ax.plot(*LOOP[:,600:],color=INK,lw=1.6,ls='--',alpha=.55)
    if markers:
        for i,name in [(0,'A'),(600,'B')]:
            q=LOOP[:,i]
            ax.scatter(*q,color=INK,s=28)
            ax.text(*(q+np.array([.1,0,.3])),name,fontsize=14,
                    bbox=dict(facecolor='white',edgecolor='none',alpha=.85,pad=.5))

def save(fig,name):
    fig.savefig(OUT/name,dpi=220,bbox_inches='tight');plt.close(fig)

def geometry_figure():
    fig=plt.figure(figsize=(12.5,4.7))
    g=fig.add_gridspec(1,3,width_ratios=[1,1,1.05],wspace=.12)
    a=fig.add_subplot(g[0,0],projection='3d');torus(a);a.set_box_aspect((1,1,1),zoom=1.22)
    t=np.linspace(0,2*np.pi,641)
    a.plot(*xyz(t,np.zeros_like(t)),color=BLUE,lw=2.2)
    a.plot(*xyz(np.zeros_like(t),t),color=AMBER,lw=2.4)
    a.plot([0,RB],[0,0],[0,0],color=INK,lw=1.2)
    a.plot([RB,RB+RF],[0,0],[0,0],color=AMBER,lw=1.4)
    a.scatter([0,RB,RB+RF],[0,0,0],[0,0,0],color=INK,s=12)
    fig.canvas.draw()
    for point,text,offset,col in [((RB*.45,0,0),r'$r_b$',(0,14),INK),
                                   ((RB+RF/2,0,0),r'$r_f$',(18,-25),AMBER)]:
        xp,yp,_=proj3d.proj_transform(*point,a.get_proj())
        a.annotate(text,(xp,yp),xytext=offset,textcoords='offset points',
                   fontsize=15,color=col,ha='center',
                   bbox=dict(facecolor='white',edgecolor='none',pad=.5),
                   arrowprops=dict(arrowstyle='-',color=col,lw=.9))
    a.text2D(.5,.98,'Two cycles',ha='center',transform=a.transAxes,fontsize=15,fontweight='bold')
    a.text2D(.08,.05,r'$u$: bosic cycle',color=BLUE,transform=a.transAxes,fontsize=13)
    a.text2D(.08,-.015,r'$v$: fermic cycle',color=AMBER,transform=a.transAxes,fontsize=13)
    a=fig.add_subplot(g[0,1],projection='3d');torus(a);a.set_box_aspect((1,1,1),zoom=1.22);loop(a)
    a.text2D(.5,.98,'Coupled loop',ha='center',transform=a.transAxes,fontsize=15,fontweight='bold')
    a.text2D(.5,.025,'Solid: first turn\nDashed: completing turn',ha='center',
             transform=a.transAxes,fontsize=12,linespacing=1.3,color=INK)
    a=fig.add_subplot(g[0,2])
    a.plot(2*S[:601],S[:601],color=INK,lw=2.5)
    a.plot(2*S[600:],S[600:],color=INK,lw=1.8,ls='--',alpha=.55)
    for x,y,name in [(0,0,'A'),(1,.5,'B'),(2,1,'A: return')]:
        a.scatter(x,y,s=28,color=INK)
        a.annotate(name,(x,y),xytext=(6,9) if x<2 else (-5,12),textcoords='offset points',
                   ha='left' if x<2 else 'right',fontsize=12)
    a.axvline(1,color=BLUE,alpha=.2)
    a.set(xlim=(-.12,2.3),ylim=(-.12,1.16),xlabel='Bosic turns',ylabel='Fermic turns',
          xticks=[0,1,2],yticks=[0,.5,1])
    a.set_title('Phase return',fontsize=15,fontweight='bold',pad=15)
    a.grid(alpha=.16)
    fig.subplots_adjust(left=.015,right=.975,bottom=.2,top=.88)
    save(fig,'two-cycles.png')


def chart(u,v):
    return np.array([P*(u-U0)/(2*DELTA),PF*(v-V0)/DELTA])

def envelope(x,t):
    return np.exp(-.5*((x-VG*t)/SIGMA)**2)

def phase(x,t):
    return (P*x-C*CORE*t)/HBAR


def momentum_figure():
    fig=plt.figure(figsize=(11.8,8.5))
    a=fig.add_axes([.025,.48,.40,.47],projection='3d');torus(a);loop(a,markers=False)
    # The highlighted physical drawing patch maps to the exact inset limits.
    xmin,xmax,ymin,ymax=-.48,1.25,-.43,1.25
    u=U0+2*DELTA*np.linspace(xmin,xmax,49)/P
    v=V0+DELTA*np.linspace(ymin,ymax,33)/PF
    uu,vv=np.meshgrid(u,v)
    surface=xyz(uu,vv)
    a.plot_surface(*surface,color='#ead5ac',alpha=.36,shade=False,linewidth=0)
    for uedge in [u[0],u[-1]]:
        a.plot(*xyz(np.full_like(v,uedge),v),color=AMBER,lw=1.0,alpha=.8)
    for vedge in [v[0],v[-1]]:
        a.plot(*xyz(u,np.full_like(u,vedge)),color=AMBER,lw=1.0,alpha=.8)
    q=xyz(U0,V0)
    a.scatter(*q,s=42,color=AMBER)
    a.text(*(q+np.array([0,0,.30])),'Q',color=AMBER,fontsize=14)
    a.text2D(.5,.97,'A section of the loop',transform=a.transAxes,ha='center',fontsize=15,fontweight='bold')
    b=fig.add_axes([.53,.52,.39,.40])
    b.set_aspect('equal');b.set(xlim=(xmin,xmax),ylim=(ymin,ymax));b.axis('off')
    b.add_patch(Rectangle((xmin,ymin),xmax-xmin,ymax-ymin,facecolor='#f5f1f8',edgecolor='#c1afcf',lw=1.))
    # Original parameter-grid stations, transformed without adding new lines.
    for uline in np.linspace(0,2*np.pi,MAJOR_DIVISIONS,endpoint=False):
        x=chart(uline,V0)[0]
        if xmin<x<xmax:b.plot([x,x],[ymin,ymax],color='#ac9bb9',lw=.6,alpha=.45)
    for vline in np.linspace(0,2*np.pi,MINOR_DIVISIONS,endpoint=False):
        y=chart(U0,vline)[1]
        if ymin<y<ymax:b.plot([xmin,xmax],[y,y],color='#ac9bb9',lw=.6,alpha=.45)
    lam=np.linspace(-.45,1.25,321)
    b.plot(P*lam,PF*lam,color=INK,lw=1.4,alpha=.7)
    scale=.84
    O=np.array([0.,0.]);B=np.array([scale*P,0.]);D=np.array([scale*P,scale*PF])
    for start,end,col in [(O,B,BLUE),(B,D,AMBER),(O,D,INK)]:
        b.annotate('',xy=end,xytext=start,arrowprops=dict(arrowstyle='-|>',lw=2.3,color=col,mutation_scale=14))
    b.scatter(0,0,color=AMBER,s=18,zorder=5)
    b.text(-.20,-.16,'Q',fontsize=13,color=AMBER,
           bbox=dict(facecolor='#f5f1f8',edgecolor='none',pad=.5))
    b.text(scale*P/2,-.15,r'$p$',ha='center',fontsize=18,color=BLUE)
    b.text(scale*P+.10,scale*PF/2,r'$p_f$',va='center',fontsize=18,color=AMBER)
    b.text(scale*P*.42-.11,scale*PF*.42+.11,r'$M$',fontsize=18,color=INK,
           bbox=dict(facecolor='#f5f1f8',edgecolor='none',pad=.5))
    d=.11
    b.plot([B[0]-d,B[0]-d,B[0]],[0,d,d],color='#737780',lw=1)
    b.set_title('Momentum-scaled close-up',fontsize=15,fontweight='bold',pad=12)
    b.text(.5,-.115,r'$M^2=p^2+p_f^2$',transform=b.transAxes,ha='center',fontsize=17,color=INK)
    fig.canvas.draw()
    q2=proj3d.proj_transform(*q,a.get_proj())
    connector=ConnectionPatch(xyA=(q2[0],q2[1]),coordsA=a.transData,
        xyB=(xmin,0.),coordsB=b.transData,color=AMBER,lw=1.,ls=':',alpha=.7)
    fig.add_artist(connector)
    # Narrow-packet illustration: first-order expansion of c*M(p) near P.
    w=fig.add_axes([.10,.075,.82,.32])
    x=np.linspace(-5.2,6.5,3201)
    for t,y,label in [(0.,1.6,'Initial'),(DT,0.,r'After $\Delta t$')]:
        amp=.55*envelope(x,t)
        w.plot(x,y+amp*np.cos(phase(x,t)),color=INK,lw=1.05)
        w.plot(x,y+amp,color=BLUE,lw=1.2,ls='--')
        w.plot(x,y-amp,color=BLUE,lw=.85,ls='--',alpha=.7)
        w.text(-5.65,y,label,ha='right',va='center',fontsize=12,color=INK)
        w.scatter(VG*t,y+.55,facecolors='white',edgecolors=BLUE,marker='s',s=78,linewidths=1.4,zorder=5)
        crest=VPH*t
        w.scatter(crest,y+.55*envelope(crest,t),color=PHASE,s=25,zorder=5)
    w.plot([0,0],[-1.8,2.17],color='#9aa5ae',lw=.8,ls=':',alpha=.65)
    for end,y,col,symbol,name in [(VG*DT,-.95,BLUE,r'$v_{\mathrm{g}}\Delta t$','envelope centre'),
                                 (VPH*DT,-1.6,PHASE,r'$v_{\mathrm{ph}}\Delta t$','constant-phase crest')]:
        w.annotate('',xy=(end,y),xytext=(0,y),arrowprops=dict(arrowstyle='<->',color=col,lw=1.6))
        w.text(end/2,y-.11,symbol,ha='center',va='top',fontsize=13,color=col)
        w.text(end+.16,y,name,va='center',fontsize=12,color=col)
        w.plot([end,end],[y,.40],ls=':',lw=.9,color=col,alpha=.5)
    fig.text(.34,.435,r'$v_{\mathrm{g}}/c=p/M$',ha='center',fontsize=15,color=BLUE)
    fig.text(.69,.435,r'$v_{\mathrm{ph}}/c=M/p$',ha='center',fontsize=15,color=PHASE)
    w.annotate('',xy=(6.7,.85),xytext=(5.0,.85),arrowprops=dict(arrowstyle='->',color='#60737d',lw=1.1))
    w.text(6.82,.85,r'$\hat{k}$',va='center',fontsize=14,color='#60737d')
    w.text(-5.2,2.62,'Packet and phase along the translation direction',fontsize=14,fontweight='bold',color=INK)
    w.set(xlim=(-6.6,7.3),ylim=(-2.25,2.95));w.axis('off')
    save(fig,'momentum-wave.png')


def verify():
    assert np.allclose(LOOP[:,0],LOOP[:,-1])
    assert not np.allclose(LOOP[:,0],LOOP[:,600])
    lam=np.linspace(-.45,1.25,51)
    mapped=chart(U0+2*DELTA*lam,V0+DELTA*lam)
    assert np.allclose(mapped,np.array([P*lam,PF*lam]))
    assert np.isclose(np.hypot(P,PF),CORE)
    assert np.isclose(VG*VPH,C*C)
    step=1.e-5
    derivative=C*(np.hypot(PF,P+step)-np.hypot(PF,P-step))/(2*step)
    assert np.isclose(derivative,VG,rtol=1.e-8)
    assert np.isclose(phase(VPH*DT,DT),0.)
    assert np.isclose(envelope(VG*DT,DT),1.)
    assert VPH>VG and VG<C<VPH
    # Expected small dispersive correction during the illustrated interval.
    dispersion_parameter=DT*C*(PF*PF/CORE**3)*HBAR/SIGMA**2
    assert dispersion_parameter<.05
    result={'figures':['assets/two-cycles.png','assets/momentum-wave.png'],
        'mesh':[MAJOR_DIVISIONS,MINOR_DIVISIONS],
        'momentum_chart':'x=p*(u-u0)/(2*delta); y=p_f*(v-v0)/delta',
        'chart_tangent_components':[P,PF],'arrow_scale':.84,'core_momentum':float(CORE),
        'chart_is_momentum_rescaled_not_euclidean_metric':True,
        'bosic_to_fermic_winding_does_not_determine_momentum_ratio':True,
        'p':P,'p_f':PF,'c':C,'hbar':HBAR,'group_velocity':float(VG),
        'phase_velocity':float(VPH),'delta_t':DT,'envelope_sigma':SIGMA,
        'group_advance':float(VG*DT),'phase_advance':float(VPH*DT),
        'narrow_packet_first_order_dispersion':True,
        'neglected_dispersion_parameter':float(dispersion_parameter),
        'internal_speed_law_asserted':False,'new_dependencies':[]}
    (ROOT/'validation/teaching-checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    verify();geometry_figure();momentum_figure()
