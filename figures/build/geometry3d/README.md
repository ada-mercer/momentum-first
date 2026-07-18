# Geometry3d build outputs

This is the generated-output root for native 3D geometry families.

- `<family>/canonical/` contains manuscript-facing outputs declared by the
  geometry3d manifest.
- `<family>/preview/` contains fast review renders.
- `<family>/interactive/` contains inspection assets when enabled.
- `<family>/frames/` contains animation frame sequences when a family supports
  them.
- `<family>/review/` contains explicitly preserved comparisons.
- `test-renders/` contains disposable demonstrations and smoke output.

The authority for families, scene names, canonical outputs, and backend policy
is [`../../manifests/geometry3d.yml`](../../manifests/geometry3d.yml). Do not
promote a preview, comparison, or test render merely by moving it into this
tree; update the manifest or retain an explicit review record.
