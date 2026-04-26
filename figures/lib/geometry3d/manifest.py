"""Manifest loading for geometry3d.

This intentionally uses a tiny stdlib-only YAML subset parser so the geometry3d
CLI works inside the repo figure environment without adding a hidden dependency.
The supported subset is enough for the hand-authored `geometry3d.yml` manifest:
- mappings
- lists
- nested list items that are mappings
- plain string/int/float/bool/null scalars
- inline empty lists (`[]`)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(frozen=True, slots=True)
class SceneManifest:
    scene_id: str
    function: str
    output_kind: str = 'canonical_png'
    output_subdir: str = 'canonical'
    filename: str = ''
    default_backend: str | None = None
    canonical_backend: str | None = None
    fallback_backend: str | None = None
    inspection_backend: str | None = None


@dataclass(frozen=True, slots=True)
class FamilyManifest:
    family_id: str
    status: str
    source_dir: str
    build_dir: str
    default_camera: str
    default_backend: str | None = None
    canonical_backend: str | None = None
    fallback_backend: str | None = None
    inspection_backend: str | None = None
    default_style: str | None = None
    canonical_scene: str | None = None
    module: str | None = None
    manuscript_targets: tuple[str, ...] = ()
    migration_from: tuple[str, ...] = ()
    notes: tuple[str, ...] = ()
    scenes: tuple[SceneManifest, ...] = ()

    def get_scene(self, scene_id: str | None = None) -> SceneManifest:
        wanted = scene_id or self.canonical_scene
        if wanted is None:
            raise KeyError(f'Family {self.family_id} has no canonical scene and no scene id was provided')
        for scene in self.scenes:
            if scene.scene_id == wanted:
                return scene
        raise KeyError(f'Family {self.family_id} has no scene {wanted!r}')


@dataclass(frozen=True, slots=True)
class GeometryManifest:
    path: Path
    project_root: Path
    version: int
    phase: str
    default_backend: str
    build_root: Path
    docs_root: Path
    source_root: Path
    library_root: Path
    primary_backend: str | None = None
    fallback_backend: str | None = None
    inspection_backend: str | None = None
    notes: tuple[str, ...] = ()
    backends: tuple[dict[str, Any], ...] = ()
    families: tuple[FamilyManifest, ...] = field(default_factory=tuple)

    def get_family(self, family_id: str) -> FamilyManifest:
        for family in self.families:
            if family.family_id == family_id:
                return family
        raise KeyError(f'Unknown geometry3d family: {family_id}')


def _strip_comments(text: str) -> list[tuple[int, str]]:
    rows: list[tuple[int, str]] = []
    for raw in text.splitlines():
        if not raw.strip():
            continue
        stripped = raw.lstrip(' ')
        if stripped.startswith('#'):
            continue
        indent = len(raw) - len(stripped)
        rows.append((indent, stripped.rstrip()))
    return rows


def _parse_scalar(value: str) -> Any:
    value = value.strip()
    if value == '[]':
        return []
    if value == '{}':
        return {}
    if value in {'true', 'True'}:
        return True
    if value in {'false', 'False'}:
        return False
    if value in {'null', 'None', '~'}:
        return None
    if value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
        return int(value)
    try:
        if '.' in value and value.replace('.', '', 1).replace('-', '', 1).isdigit():
            return float(value)
    except ValueError:
        pass
    if (value.startswith("'") and value.endswith("'")) or (value.startswith('"') and value.endswith('"')):
        return value[1:-1]
    return value


class _SubsetYamlParser:
    def __init__(self, rows: list[tuple[int, str]]):
        self.rows = rows
        self.index = 0

    def parse(self) -> Any:
        if not self.rows:
            return {}
        return self._parse_block(self.rows[0][0])

    def _peek(self) -> tuple[int, str] | None:
        if self.index >= len(self.rows):
            return None
        return self.rows[self.index]

    def _parse_block(self, indent: int) -> Any:
        row = self._peek()
        if row is None:
            return {}
        _current_indent, text = row
        if text.startswith('- '):
            return self._parse_list(indent)
        return self._parse_mapping(indent)

    def _parse_list(self, indent: int) -> list[Any]:
        items: list[Any] = []
        while True:
            row = self._peek()
            if row is None:
                break
            current_indent, text = row
            if current_indent < indent:
                break
            if current_indent != indent or not text.startswith('- '):
                break

            self.index += 1
            content = text[2:].strip()
            if not content:
                items.append(self._parse_block(indent + 2))
                continue

            if ':' in content:
                key, remainder = content.split(':', 1)
                item: dict[str, Any] = {}
                key = key.strip()
                remainder = remainder.strip()
                if remainder:
                    item[key] = _parse_scalar(remainder)
                else:
                    next_row = self._peek()
                    if next_row is not None and next_row[0] > indent:
                        item[key] = self._parse_block(indent + 2)
                    else:
                        item[key] = {}

                while True:
                    next_row = self._peek()
                    if next_row is None:
                        break
                    next_indent, next_text = next_row
                    if next_indent < indent + 2:
                        break
                    if next_indent == indent and next_text.startswith('- '):
                        break
                    if next_indent == indent + 2 and not next_text.startswith('- '):
                        self.index += 1
                        subkey, subremainder = next_text.split(':', 1)
                        subkey = subkey.strip()
                        subremainder = subremainder.strip()
                        if subremainder:
                            item[subkey] = _parse_scalar(subremainder)
                        else:
                            nested_row = self._peek()
                            if nested_row is not None and nested_row[0] > next_indent:
                                item[subkey] = self._parse_block(next_indent + 2)
                            else:
                                item[subkey] = {}
                        continue
                    break

                items.append(item)
                continue

            items.append(_parse_scalar(content))
        return items

    def _parse_mapping(self, indent: int) -> dict[str, Any]:
        mapping: dict[str, Any] = {}
        while True:
            row = self._peek()
            if row is None:
                break
            current_indent, text = row
            if current_indent < indent:
                break
            if current_indent != indent or text.startswith('- '):
                break
            self.index += 1
            key, remainder = text.split(':', 1)
            key = key.strip()
            remainder = remainder.strip()
            if remainder:
                mapping[key] = _parse_scalar(remainder)
                continue
            next_row = self._peek()
            if next_row is not None and next_row[0] > current_indent:
                mapping[key] = self._parse_block(current_indent + 2)
            else:
                mapping[key] = {}
        return mapping


def _load_subset_yaml(text: str) -> dict[str, Any]:
    rows = _strip_comments(text)
    parser = _SubsetYamlParser(rows)
    result = parser.parse()
    if not isinstance(result, dict):
        raise ValueError('Top-level geometry3d manifest must be a mapping')
    return result


def _as_tuple(values: Any) -> tuple[Any, ...]:
    if values is None:
        return ()
    if isinstance(values, list):
        return tuple(values)
    return (values,)


def load_manifest(path: str | Path) -> GeometryManifest:
    manifest_path = Path(path).resolve()
    data = _load_subset_yaml(manifest_path.read_text())
    project_root = manifest_path.parents[2]

    def resolve(rel: str | None) -> Path:
        if not rel:
            return project_root
        candidate = Path(rel)
        return candidate if candidate.is_absolute() else project_root / candidate

    families: list[FamilyManifest] = []
    for item in data.get('families', []):
        scenes = [
            SceneManifest(
                scene_id=scene['id'],
                function=scene['function'],
                output_kind=scene.get('output_kind', 'canonical_png'),
                output_subdir=scene.get('output_subdir', 'canonical'),
                filename=scene.get('filename', scene['id']),
                default_backend=scene.get('default_backend'),
                canonical_backend=scene.get('canonical_backend'),
                fallback_backend=scene.get('fallback_backend'),
                inspection_backend=scene.get('inspection_backend'),
            )
            for scene in item.get('scenes', [])
        ]
        families.append(
            FamilyManifest(
                family_id=item['id'],
                status=item.get('status', 'unknown'),
                source_dir=item['source_dir'],
                build_dir=item['build_dir'],
                default_backend=item.get('default_backend'),
                canonical_backend=item.get('canonical_backend'),
                fallback_backend=item.get('fallback_backend'),
                inspection_backend=item.get('inspection_backend'),
                default_camera=item.get('default_camera', ''),
                default_style=item.get('default_style'),
                canonical_scene=item.get('canonical_scene'),
                module=item.get('module'),
                manuscript_targets=tuple(item.get('manuscript_targets', [])),
                migration_from=tuple(item.get('migration_from', [])),
                notes=tuple(item.get('notes', [])),
                scenes=tuple(scenes),
            )
        )

    return GeometryManifest(
        path=manifest_path,
        project_root=project_root,
        version=int(data.get('version', 0)),
        phase=str(data.get('phase', 'unknown')),
        default_backend=str(data.get('default_backend', data.get('primary_backend', 'pyvista3d'))),
        primary_backend=data.get('primary_backend'),
        fallback_backend=data.get('fallback_backend'),
        inspection_backend=data.get('inspection_backend'),
        build_root=resolve(data.get('build_root', 'figures/build/geometry3d')),
        docs_root=resolve(data.get('docs_root', 'figures/docs/geometry3d')),
        source_root=resolve(data.get('source_root', 'figures/src/geometry3d')),
        library_root=resolve(data.get('library_root', 'figures/lib/geometry3d')),
        notes=_as_tuple(data.get('notes')),
        backends=tuple(data.get('backends', [])),
        families=tuple(families),
    )
