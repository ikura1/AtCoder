import argparse
from pathlib import Path
import shutil


def copy_dir(start, end=None):
    if not end:
        end = start
    template_dir = Path("./template")
    for i in range(start, end + 1):
        path = Path(f"./abc/abc{i}")
        if path.is_dir():
            continue
        shutil.copytree(template_dir, path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("integer", metavar="N", type=int, nargs="+")
    args = parser.parse_args()
    copy_dir(*args.integer)


if __name__ == "__main__":
    main()
