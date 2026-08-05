"""Validate the Skill layout and the documented capability contract without third-party dependencies."""

from pathlib import Path
import json
import re
import sys


ROOT = Path(__file__).resolve().parents[2]
SKILLS = ROOT / "skills"
CATALOG = Path(__file__).resolve().parent.parent / "catalog.json"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
CODE_SPAN_RE = re.compile(r"`([^`\n]+)`")
DOTTED_RE = re.compile(r"^[a-z][a-z0-9_]*(?:\.[a-z][a-z0-9_]*)+$")
UNDERSCORE_RE = re.compile(r"^[a-z][a-z0-9]*(?:_[a-z0-9]+)+$")
MCP_PATH_RE = re.compile(r"/mcp/[a-z0-9-]+")


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


def check_layout(errors):
    if not SKILLS.is_dir():
        errors.append("missing skills/ directory")
        return
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


def load_catalog(errors):
    if not CATALOG.is_file():
        errors.append(f"{CATALOG.relative_to(ROOT)}: missing capability catalog snapshot")
        return None
    try:
        return json.loads(CATALOG.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        errors.append(f"{CATALOG.relative_to(ROOT)}: invalid JSON: {error}")
        return None


def check_contract(errors, catalog):
    """Reject Tool names and MCP paths that no longer exist in the live catalog.

    Documentation drifts silently when a Tool is removed from the service, so every
    Tool-shaped token inside a code span is checked against the snapshot. Only tokens
    in a capability's own namespace are checked, which keeps ordinary field names
    such as `monitor_id` and response paths such as `error.code` out of scope. A bare
    namespace such as `find_leads` is a service identifier, not a Tool, so it is
    skipped; every MCP Tool name carries at least one segment after its namespace.
    """
    tool_ids = {tool for server in catalog["servers"] for tool in server["tools"]}
    mcp_names = {tool.replace(".", "_") for tool in tool_ids}
    paths = {server["path"] for server in catalog["servers"]}
    allowed_fields = set(catalog.get("inputFieldNamesInToolNamespace", []))
    namespaces = {tool.split(".", 1)[0] for tool in tool_ids}

    for markdown in sorted(ROOT.rglob("*.md")):
        if ".git" in markdown.parts:
            continue
        text = markdown.read_text(encoding="utf-8")
        name = markdown.relative_to(ROOT)
        for token in sorted(set(CODE_SPAN_RE.findall(text))):
            token = token.strip()
            if DOTTED_RE.fullmatch(token):
                if token.split(".", 1)[0] in namespaces and token not in tool_ids:
                    errors.append(f"{name}: `{token}` is not a Tool ID in the current catalog")
            elif UNDERSCORE_RE.fullmatch(token) and token not in allowed_fields:
                namespace = next((n for n in namespaces if token.startswith(n + "_")), None)
                if namespace is not None and token not in mcp_names:
                    errors.append(f"{name}: `{token}` is not an MCP Tool in the current catalog")
        for path in sorted(set(MCP_PATH_RE.findall(text))):
            if path not in paths:
                errors.append(f"{name}: `{path}` is not an MCP endpoint in the current catalog")


def main() -> int:
    errors = []
    check_layout(errors)
    catalog = load_catalog(errors)
    if catalog is not None:
        check_contract(errors, catalog)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("All Skills and documented Tool contracts are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
