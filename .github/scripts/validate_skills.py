"""Validate the repository's standard Skill layout without third-party dependencies."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[2]
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_frontmatter(text: str):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    values = {}
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            return None
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"\'')
    return values


def main() -> int:
    errors = []
    if not SKILLS.is_dir():
        errors.append("missing skills/ directory")
    else:
        for folder in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
            skill_file = folder / "SKILL.md"
            # Empty directories cannot be represented in Git and may be local leftovers.
            if not any(folder.iterdir()):
                continue
            if not NAME_RE.fullmatch(folder.name) or len(folder.name) > 63:
                errors.append(f"{folder.relative_to(ROOT)}: invalid directory name")
            if not skill_file.is_file():
                errors.append(f"{folder.relative_to(ROOT)}: missing SKILL.md")
                continue
            metadata = parse_frontmatter(skill_file.read_text(encoding="utf-8"))
            if metadata is None:
                errors.append(f"{skill_file.relative_to(ROOT)}: invalid YAML frontmatter")
                continue
            if set(metadata) != {"name", "description"}:
                errors.append(f"{skill_file.relative_to(ROOT)}: frontmatter must contain only name and description")
            if metadata.get("name") != folder.name:
                errors.append(f"{skill_file.relative_to(ROOT)}: name must match directory")
            if not metadata.get("description"):
                errors.append(f"{skill_file.relative_to(ROOT)}: description is required")
            if len(metadata.get("name", "")) > 64:
                errors.append(f"{skill_file.relative_to(ROOT)}: name exceeds 64 characters")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("All Skills are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
