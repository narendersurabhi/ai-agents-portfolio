# import shutil, pathlib, argparse
# def main():
#     ap = argparse.ArgumentParser()
#     ap.add_argument("--path", required=True)
#     p = pathlib.Path("data/docs"); p.mkdir(parents=True, exist_ok=True)
#     for f in pathlib.Path(args.path).glob("*"): shutil.copy(f, p / f.name)
# if __name__ == "__main__":
#     args = ap.parse_args(); main()


import argparse
from pathlib import Path
import shutil
import sys
import time

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", type=Path, required=True, help="Source directory of docs")
    ap.add_argument("--dest", type=Path, default=Path("data/docs"), help="Destination directory")
    ap.add_argument(
        "--recursive",
        action="store_true",
        help="Recursively copy files and preserve subfolders",
    )
    ap.add_argument(
        "--only-newer",
        action="store_true",
        help="Skip copy when destination is same or newer",
    )
    ap.add_argument(
        "--skip-locked",
        action="store_true",
        help="Skip files that are locked by another process (Windows)",
    )
    ap.add_argument(
        "--retries",
        type=int,
        default=2,
        help="Retries on transient PermissionError (e.g., AV scans)",
    )
    ap.add_argument(
        "--retry-delay",
        type=float,
        default=0.25,
        help="Seconds to sleep between retries",
    )
    args = ap.parse_args()

    src: Path = args.path
    dst: Path = args.dest

    if not src.exists():
        print(f"error: source does not exist: {src}", file=sys.stderr)
        return 2
    if not src.is_dir():
        print(f"error: source is not a directory: {src}", file=sys.stderr)
        return 2

    dst.mkdir(parents=True, exist_ok=True)

    def _should_skip(src_file: Path, dst_file: Path) -> bool:
        if args.only_newer and dst_file.exists():
            try:
                return dst_file.stat().st_mtime >= src_file.stat().st_mtime
            except FileNotFoundError:
                return False
        return False

    def _safe_copy(src_file: Path, dst_file: Path) -> bool:
        # Returns True if copied, False if skipped due to lock
        # Ensure parent exists
        dst_file.parent.mkdir(parents=True, exist_ok=True)
        # Optional timestamp check
        if _should_skip(src_file, dst_file):
            return False
        attempts = args.retries + 1
        last_err: BaseException | None = None
        for attempt in range(attempts):
            try:
                print("attempt", attempt + 1, "of", attempts, "to copy file")
                print(f"Copying: {src_file} -> {dst_file}")
                shutil.copy2(src_file, dst_file)
                return True
            except PermissionError as e:
                print(f"PermissionError on copy attempt {attempt + 1} of {attempts}: {e}", file=sys.stderr)
                last_err = e
                time.sleep(args.retry_delay)
        if args.skip_locked:
            print(
                f"warn: locked, skipped: {src_file} -> {dst_file}: {last_err}",
                file=sys.stderr,
            )
            return False
        # Re-raise the last error
        assert last_err is not None
        raise last_err

    copied = 0
    if args.recursive:
        for item in src.rglob("*"):
            if item.is_file():
                rel = item.relative_to(src)
                target = dst / rel
                if _safe_copy(item, target):
                    copied += 1
        print(f"Copied {copied} files (recursive) to {dst}")
    else:
        for f in src.iterdir():
            if f.is_file():
                if _safe_copy(f, dst / f.name):
                    copied += 1
        print(f"Copied {copied} files to {dst}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
