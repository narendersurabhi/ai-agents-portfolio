import shutil, pathlib, argparse
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", required=True)
    p = pathlib.Path("data/docs"); p.mkdir(parents=True, exist_ok=True)
    for f in pathlib.Path(args.path).glob("*"): shutil.copy(f, p / f.name)
if __name__ == "__main__":
    args = ap.parse_args(); main()
