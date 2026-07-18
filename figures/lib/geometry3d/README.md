# Geometry3d shared library

This package is the reusable implementation layer for native 3D figures. It
contains backend-neutral scene contracts, shared primitives, camera and style
presets, exporters, and backend adapters.

Keep family-specific physics and manuscript meaning under
[`../../src/geometry3d/`](../../src/geometry3d/README.md). Move behavior into the
shared library only when multiple families genuinely use the same abstraction.

Authoring and backend guidance lives under
[`../../docs/geometry3d/`](../../docs/geometry3d/README.md); family and backend
authority lives in [`../../manifests/geometry3d.yml`](../../manifests/geometry3d.yml).
