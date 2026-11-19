import os
import hashlib
from pathlib import Path
import shutil
import sys


def main():
    source = Path(__file__).resolve().parent / "entry.png"
    destination_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    destination = destination_dir / "entry.png"
    if not source.is_file():
        print(f"Error: source image not found: {source}", file=sys.stderr)
        return 1

    try:
        destination_dir.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
    except OSError as error:
        print(f"Error: unable to write output image: {error}", file=sys.stderr)
        return 1
    digest = hashlib.sha256(destination.read_bytes()).hexdigest()
    print(f"{destination} sha256={digest}")
    return 0


if __name__ == "__main__":
    main()
