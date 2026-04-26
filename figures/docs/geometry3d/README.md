# geometry3d docs

This folder is the docs-first entrypoint for the native 3D geometry system.

Current implemented status:
- `foundations-shells` is the first real migrated family
- system-level backend policy is now PyVista-primary, with matplotlib explicitly preserved and Plotly reserved for inspection
- `foundations-shells` remains a deliberate continuity-first exception whose canonical backend is still `matplotlib3d`
- shared primitive support now includes spheres, half-spheres, simple coordinate systems, bounding-box coordinate systems, and reusable vectors
- shared camera calibration now includes orthographic controls and a matplotlib approximation layer
- comparison renders are now a deliberate workflow, with preserved backend copies for review

Read in this order:
1. `QUICKSTART.md`
2. `AUTHORING_GUIDE.md`
3. `CAMERA_GUIDE.md`
4. `BACKENDS.md`
5. `STYLE_GUIDE.md`
6. `FAMILY_INDEX.md`
7. `MIGRATION_GUIDE.md`

If you are resuming work from a fresh session, start with `QUICKSTART.md` and `CAMERA_GUIDE.md` before touching backend code.

If backend intent is the question, read `BACKENDS.md` before changing any family defaults.

If the task is primitive-level authoring rather than backend tuning, read `AUTHORING_GUIDE.md` immediately after `QUICKSTART.md`.
