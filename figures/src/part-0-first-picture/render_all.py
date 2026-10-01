"""Reproduce the adopted Part 0 schematics without overwriting selected assets.

Requires the optional local geometry3d/PyVista stack, not the minimal CI image.
The recipe is preserved byte-for-byte from the adopted chapter's v17 packet.
"""
from pathlib import Path
import argparse
import shutil
import subprocess
import sys
import tempfile

SOURCE = Path(__file__).resolve().parent
REPO = SOURCE.parents[2]
SCRIPTS = ["build_figures.py", "render_geometry_momentum.py", "mode_geometry.py",
           "render_opaque_closeup.py", "render_pitch.py"]
OUTPUTS = ["assets/two-cycles.png", "assets/momentum-wave.png",
           "assets/translation-pitch.png", "assets/two-dilations.png",
           "assets/bosonic-dilation-response.png", "assets/loop-wave.png",
           "mode-study/standing-mode-storyboard.png"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True,
                        help="New review directory for PNGs and generation diagnostics")
    args = parser.parse_args()
    destination = args.output_dir.resolve()
    if destination.exists():
        parser.error("output directory already exists; choose a new review directory")
    scratch = REPO / ".local-review"
    scratch.mkdir(exist_ok=True)
    # Recipes locate the shared geometry3d library through their repository
    # ancestor. Keep temporary work here, not in the source or canonical output.
    with tempfile.TemporaryDirectory(prefix="part0-render-", dir=scratch) as tmp:
        root = Path(tmp)
        shutil.copytree(SOURCE / "recipe/validation", root / "validation")
        (root / "assets").mkdir()
        (root / "mode-study").mkdir()
        for script in SCRIPTS:
            subprocess.run([sys.executable, str(root / "validation" / script)],
                           cwd=REPO, check=True)
        for output in OUTPUTS:
            if not (root / output).is_file():
                raise RuntimeError(f"Missing rendered output: {output}")
        destination.mkdir(parents=True)
        for output in OUTPUTS:
            shutil.copyfile(root / output, destination / Path(output).name)
        diagnostics = destination / "diagnostics"
        diagnostics.mkdir()
        for path in (root / "validation").glob("*.json"):
            shutil.copyfile(path, diagnostics / path.name)
    print(f"Rendered {len(OUTPUTS)} review PNGs to {destination}")


if __name__ == "__main__":
    main()
