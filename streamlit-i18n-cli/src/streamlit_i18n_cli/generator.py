from __future__ import annotations
import keyword, re
from pathlib import Path
from typing import Any, Dict, List
import yaml

IDENT_RE = re.compile(r"[^0-9a-zA-Z_]+")

def to_ident(name: str) -> str:
    s = IDENT_RE.sub("_", name.strip())
    if not s:
        s = "X"
    if s[0].isdigit():
        s = "_" + s
    if keyword.iskeyword(s):
        s = s + "_"
    return s

def to_class(name: str) -> str:
    return to_ident(name).upper()

def to_field(name: str) -> str:
    return to_ident(name).upper()

def load_yaml(path: Path) -> Dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise SystemExit("Top-level YAML must be a mapping.")
    return data

def build_structure(data: Dict[str, Any]) -> Dict[str, Any]:
    out: Dict[str, Any] = {}
    for k, v in data.items():
        if isinstance(v, dict):
            out[k] = build_structure(v)
        else:
            out[k] = ""
    return out

def apply_renames(struct: Dict[str, Any], renames: Dict[str, str]) -> Dict[str, str]:
    if not renames:
        return struct
    out: Dict[str, Any] = {}
    for k, v in struct.items():
        nk = renames.get(k, k)
        out[nk] = v
    return out

def gen_header(inp: Path) -> str:
    return (
        "from __future__ import annotations\n"
        "from dataclasses import dataclass, field\n"
        "from typing import Any\n\n"
        f"# Auto-generated from: {inp}\n"
        "# Do not edit by hand.\n\n"
    )

def gen_class(name_chain: List[str], node: Any, indent: int = 0) -> str:
    ind = " " * indent
    class_name = name_chain[-1]
    lines: List[str] = []
    lines.append(f"{ind}@dataclass")
    lines.append(f"{ind}class {class_name}:")
    if not isinstance(node, dict) or not node:
        lines.append(f"{ind}    pass")
        return "\n".join(lines) + "\n"
    for k, v in node.items():
        if isinstance(v, dict):
            nested_class_name = to_class(k)
            lines.append("")
            lines.append(gen_class(name_chain + [nested_class_name], v, indent + 4).rstrip())
    for k, v in node.items():
        if isinstance(v, dict):
            nested_class_name = to_class(k)
            lines.append(f"{ind}    {nested_class_name}: '{class_name}.{nested_class_name}' = field(default_factory=lambda: {class_name}.{nested_class_name}())")
        else:
            fname = to_field(k)
            lines.append(f"{ind}    {fname}: str = ''")
    return "\n".join(lines) + "\n"

def generate_dataclasses(input_yaml: Path, output_py: Path, renames: Dict[str, str] | None = None) -> None:
    data = load_yaml(input_yaml)
    struct = build_structure(data)
    struct = apply_renames(struct, renames or {})

    def gen_header(inp: Path) -> str:
        return (
            "from __future__ import annotations\n"
            "from dataclasses import dataclass\n"
            "from typing import Any\n\n"
            f"# Auto-generated from: {inp}\n"
            "# Do not edit by hand.\n\n"
        )

    def gen_class(name_chain: List[str], node: Any, indent: int = 0) -> str:
        ind = " " * indent
        class_name = name_chain[-1]
        lines: List[str] = []
        lines.append(f"{ind}@dataclass")
        lines.append(f"{ind}class {class_name}:")
        if not isinstance(node, dict) or not node:
            lines.append(f"{ind}    pass")
            return "\n".join(lines) + "\n"

        # Emit nested classes first
        for k, v in node.items():
            if isinstance(v, dict):
                nested_class_name = to_class(k)
                lines.append("")
                lines.append(gen_class(name_chain + [nested_class_name], v, indent + 4).rstrip())

        # Emit only leaf (string) fields; no instance fields for dict children
        for k, v in node.items():
            if not isinstance(v, dict):
                fname = to_field(k)
                lines.append(f"{ind}    {fname}: str = '{v}'")

        return "\n".join(lines) + "\n"

    parts = [gen_header(input_yaml)]
    # Deterministic order
    for k in list(struct.keys()):
        cname = to_class(k)
        parts.append(gen_class([cname], struct[k], indent=0))
        parts.append("\n")
    code = "".join(parts)
    output_py.parent.mkdir(parents=True, exist_ok=True)
    output_py.write_text(code, encoding="utf-8")
