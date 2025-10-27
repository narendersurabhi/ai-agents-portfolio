import argparse, pathlib, json
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--out", required=True)
    o = pathlib.Path(args.out); o.mkdir(parents=True, exist_ok=True)
    (o / "meta.json").write_text(json.dumps({"built": True}))
if __name__ == "__main__":
    args = ap.parse_args(); main()
