"""Minimal backend-neutral scene contract for geometry3d.

Phase 2 goal: real enough to drive the migrated foundations-shells family,
without pretending the full multi-family framework is finished.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

JsonDict = dict[str, Any]


@dataclass(slots=True)
class OutputTarget:
    output_id: str
    kind: str
    filename: str
    subdir: str = 'canonical'


@dataclass(slots=True)
class FigureLayout:
    figsize: tuple[float, float] = (13.5, 9.0)
    dpi: int = 220
    xlim: tuple[float, float] | None = None
    ylim: tuple[float, float] | None = None
    zlim: tuple[float, float] | None = None
    box_aspect: tuple[float, float, float] | None = None
    axis_labels: tuple[str, str, str] = ('x', 'y', 'z')
    show_axes: bool = True
    show_grid: bool = False
    title: str | None = None
    bbox_inches: str | None = 'tight'


@dataclass(slots=True)
class SceneObject:
    """A backend-neutral object inside a 3D scene."""

    object_id: str
    kind: str
    params: JsonDict = field(default_factory=dict)
    style: str | None = None
    backend_hints: JsonDict = field(default_factory=dict)


@dataclass(slots=True)
class SceneAnnotation:
    """A backend-neutral annotation, legend block, or overlay."""

    annotation_id: str
    kind: str
    text: str | None = None
    params: JsonDict = field(default_factory=dict)


@dataclass(slots=True)
class SceneSpec:
    """A family scene definition independent of renderer choice."""

    family: str
    scene_id: str
    default_camera: str
    default_style: str
    layout: FigureLayout = field(default_factory=FigureLayout)
    outputs: list[OutputTarget] = field(default_factory=list)
    objects: list[SceneObject] = field(default_factory=list)
    annotations: list[SceneAnnotation] = field(default_factory=list)
    metadata: JsonDict = field(default_factory=dict)

    def summary(self) -> str:
        return (
            f'{self.family}/{self.scene_id}: '
            f'{len(self.objects)} object(s), {len(self.annotations)} annotation(s), '
            f'{len(self.outputs)} output target(s)'
        )

    def get_output(self, output_id: str | None = None) -> OutputTarget:
        if not self.outputs:
            raise ValueError(f'{self.family}/{self.scene_id} defines no output targets')
        if output_id is None:
            return self.outputs[0]
        for output in self.outputs:
            if output.output_id == output_id:
                return output
        raise KeyError(f'Unknown output target {output_id!r} for {self.family}/{self.scene_id}')

    def validate(self) -> None:
        if not self.family:
            raise ValueError('SceneSpec.family is required')
        if not self.scene_id:
            raise ValueError('SceneSpec.scene_id is required')
        if not self.default_camera:
            raise ValueError('SceneSpec.default_camera is required')
        if not self.default_style:
            raise ValueError('SceneSpec.default_style is required')

        object_ids = [obj.object_id for obj in self.objects]
        if len(object_ids) != len(set(object_ids)):
            raise ValueError('SceneSpec object ids must be unique within a scene')

        annotation_ids = [ann.annotation_id for ann in self.annotations]
        if len(annotation_ids) != len(set(annotation_ids)):
            raise ValueError('SceneSpec annotation ids must be unique within a scene')

        output_ids = [output.output_id for output in self.outputs]
        if len(output_ids) != len(set(output_ids)):
            raise ValueError('SceneSpec output ids must be unique within a scene')
