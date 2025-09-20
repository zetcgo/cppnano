import shutil

if not shutil.which("uncrustify"):
    raise SystemExit(0)

import subprocess
import sys
from pathlib import Path

CONFIG = "uncrustify.cfg"


def run_one(path: Path) -> int:
    cmd = [
        "uncrustify",
        "--config",
        CONFIG,
        "--replace",
        "--no-backup",
        "--mtime",
        str(path),
    ]
    p = subprocess.run(cmd, capture_output=True, text=True)  # noqa: S603
    if p.returncode >= 2:
        sys.stderr.write(p.stderr)
        return p.returncode
    return 0


def main(argv: list[str]) -> int:
    rc = 0
    for a in argv:
        if run_one(Path(a)) >= 2:
            rc = 2
    return rc


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
