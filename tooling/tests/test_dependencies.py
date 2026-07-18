from pathlib import Path
import subprocess
import sys


def test_minimal_dependency_smoke_script_passes() -> None:
    root = Path(__file__).resolve().parents[2]
    script = root / "tooling" / "scripts" / "check_dependencies.py"
    result = subprocess.run(
        [sys.executable, str(script), "--mode", "minimal"],
        cwd=root,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + "\n" + result.stderr
