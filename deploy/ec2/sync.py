"""Copy or check the reviewed shared delivery in an explicit project checkout."""

import argparse
import hashlib
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", choices=("mp", "sso"))
    parser.add_argument("root", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    source = Path(__file__).resolve().parents[2]
    root = args.root.resolve(strict=True)
    if root == source or not (root / "AGENTS.md").is_file():
        parser.error("Target must be an existing project checkout")
    files = {
        "deploy/ec2/deploy.py": source / "deploy/ec2/deploy.py",
        "deploy/ec2/upload.sh": source / "deploy/ec2/upload.sh",
        "deploy/ec2/project.json": source / f"deploy/ec2/profiles/{args.project}.json",
        "tests/test_shared_deploy.py": source / "tests/test_shared_deploy.py",
    }
    mismatches = []
    for name, original in files.items():
        data = original.read_bytes()
        destination = root / name
        if destination.is_symlink():
            parser.error(f"Refusing symlink target: {name}")
        if args.check:
            if not destination.is_file() or destination.read_bytes() != data:
                mismatches.append(name)
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(data)
    if mismatches:
        parser.exit(1, "Shared deployment differs: " + ", ".join(mismatches) + "\n")
    if not args.check:
        provenance = {
            "source": "alxprgstech/.github",
            "files": {
                name: hashlib.sha256(path.read_bytes()).hexdigest() for name, path in files.items()
            },
        }
        (root / "deploy/ec2/shared-deploy.json").write_text(
            json.dumps(provenance, indent=2) + "\n", encoding="utf-8"
        )
    print("Shared deployment " + ("matches" if args.check else "copied"))


if __name__ == "__main__":
    main()
