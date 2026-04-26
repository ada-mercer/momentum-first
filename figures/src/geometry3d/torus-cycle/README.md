# torus-cycle family

Status: planned adaptation target

Purpose:
- host torus-cycle scene definitions inside the native figure stack
- reuse shared geometry3d cameras, styles, exporters, and backend selection
- keep cycle-specific semantics family-local rather than leaking into the shared library

Expected early outputs:
- one static preview render
- one optional interactive inspection render

Adaptation source:
- architectural ideas from `torus-cycle-renderer`
