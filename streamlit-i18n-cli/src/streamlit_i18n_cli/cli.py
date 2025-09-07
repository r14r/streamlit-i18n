from __future__ import annotations

import argparse
import keyword
import re
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, List

import yaml

from .generator import generate_dataclasses  # Variant 1 (structure-only)

# -------------------------------------------------------------------------------------------------
VERSION = "0.2.0"
TEMPLATES_DIR = Path(__file__).parent / "templates"


# -------------------------------------------------------------------------------------------------
def _py_ident(name: str) -> str:
    s = re.sub(r"[^0-9a-zA-Z_]+", "_", name.strip())
    if not s:
        s = "X"
    if s[0].isdigit():
        s = "_" + s
    if keyword.iskeyword(s):
        s = s + "_"
    return s


def _cls_name(name: str) -> str:
    return _py_ident(name).upper()


def _field_name(name: str) -> str:
    return _py_ident(name).upper()


def _py_str_literal(value: Any) -> str:
    # Safe Python literal for strings (keep unicode)
    if value is None:
        return "''"
    if not isinstance(value, str):
        value = str(value)
    lit = repr(value)
    if lit.startswith("u'") or lit.startswith('u"'):
        lit = lit[1:]
    return lit


def _load_yaml(path: Path) -> Dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def _merge_with_base(base: Dict[str, Any], lang: Dict[str, Any]) -> Dict[str, Any]:
    """Create a merged mapping where missing leaves in `lang` are filled from `base`."""
    out: Dict[str, Any] = {}
    for k, v in base.items():
        if isinstance(v, Dict):
            out[k] = _merge_with_base(v, lang.get(k, {}) if isinstance(lang.get(k), Dict) else {})
        else:
            out[k] = lang.get(k, v)
    # allow extra keys present in lang but not in base
    for k, v in lang.items():
        if k not in out:
            out[k] = v
    return out


def _gen_dc_code_from_mapping(mapping: Dict[str, Any]) -> str:
    """Generate nested dataclasses with literal defaults from a nested mapping."""

    def gen_class(name_chain: List[str], node: Any, indent: int = 0) -> str:
        ind = " " * indent
        class_name = name_chain[-1]
        lines: List[str] = []
        lines.append(f"{ind}@dataclass")
        lines.append(f"{ind}class {class_name}:")
        if not isinstance(node, Dict) or not node:
            lines.append(f"{ind}    pass")
            return "\n".join(lines) + "\n"

        # nested classes first
        for k, v in node.items():
            if isinstance(v, Dict):
                nested = _cls_name(k)
                lines.append("")
                lines.append(gen_class([*name_chain, nested], v, indent + 4).rstrip())

        # leaf fields
        for k, v in node.items():
            if not isinstance(v, Dict):
                fname = _field_name(k)
                lines.append(f"{ind}    {fname}: str = {_py_str_literal(v)}")
        return "\n".join(lines) + "\n"

    parts = [
        "from dataclasses import dataclass",
        "",
    ]
    # top-level classes
    for k, v in mapping.items():
        cname = _cls_name(k)
        parts.append(gen_class([cname], v, 0))
        parts.append("")
    return "\n".join(parts).rstrip() + "\n"


def build_lang_modules(locales_dir: Path, dest_dir: Path, base_lang: str = "en") -> List[Path]:
    """
    Variant 2 builder:
      - Read base_lang YAML to get structure and defaults.
      - For each '<code>.yml' in locales_dir, merge with base, and emit 'dest_dir/<code>.py'.
    """
    assert locales_dir.exists(), f"Locales dir not found: {locales_dir}"
    dest_dir.mkdir(parents=True, exist_ok=True)

    base_yaml = locales_dir / f"{base_lang}.yml"
    assert base_yaml.exists(), f"Base language not found: {base_yaml}"
    base = _load_yaml(base_yaml)

    out_files: List[Path] = []
    for yml in sorted(locales_dir.glob("*.yml")):
        code = yml.stem  # e.g., 'de', 'en'
        merged = _merge_with_base(base, _load_yaml(yml))
        code_text = _gen_dc_code_from_mapping(merged)
        out = dest_dir / f"{code}.py"
        out.write_text(code_text, encoding="utf-8")
        out_files.append(out)
    # ensure packages
    (dest_dir.parent).mkdir(parents=True, exist_ok=True)
    (dest_dir.parent / "__init__.py").write_text("", encoding="utf-8")
    (dest_dir / "__init__.py").write_text("", encoding="utf-8")
    return out_files


# ----------------------------
# Commands
# ----------------------------
def cmd_generate(args: argparse.Namespace) -> int:
    input_yaml = Path(args.input)
    output_py = Path(args.output)
    renames = {}
    for item in args.rename or []:
        if "=" not in item:
            print(f"--rename expects key=NewName, got: {item}", file=sys.stderr)
            return 2
        k, v = item.split("=", 1)
        renames[k.strip()] = v.strip().upper()
    generate_dataclasses(input_yaml, output_py, renames)
    print(f"Generated: {output_py}")
    return 0


def cmd_build_langs(args: argparse.Namespace) -> int:
    locales = Path(args.locales)
    dest = Path(args.dest)
    files = build_lang_modules(locales, dest, base_lang=args.base)
    print("Built language modules:")
    for f in files:
        print(f" - {f}")
    return 0


def cmd_scaffold(args: argparse.Namespace) -> int:
    target = Path(args.into)
    target.mkdir(parents=True, exist_ok=True)

    # Copy all files recursively from TEMPLATES_DIR to target folder

    for item in TEMPLATES_DIR.rglob("*"):
        rel_path = item.relative_to(TEMPLATES_DIR)
        dest_path = target / rel_path

        if "__pycache__" in rel_path.parts:
            continue

        print(f"- copying {rel_path} to {dest_path}")
        if item.is_dir():
            dest_path.mkdir(parents=True, exist_ok=True)
        else:
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, dest_path)

    print(f"Scaffolded Streamlit pages into: {target}")
    
    return 0


# -------------------------------------------------------------------------------------------------
def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="streamlit-i18n",
        description="Dataclass i18n generator and Streamlit scaffolder",
    )
    p.add_argument("--version", action="version", version=f"streamlit-i18n-cli {VERSION}")
    sub = p.add_subparsers(dest="cmd", required=True)

    # Variant 1: structure-only dataclasses (values loaded from YAML at runtime)
    g = sub.add_parser("generate", help="Generate dataclasses from YAML (Variant 1)")
    g.add_argument("-i", "--input", required=True, help="Input YAML")
    g.add_argument(
        "-o", "--output", required=True, help="Output Python file (e.g., lib/i18n/dataclasses.py)"
    )
    g.add_argument(
        "--rename",
        action="append",
        default=[],
        help="Map top-level YAML key to class name, e.g., pages=PAGES",
    )
    g.set_defaults(func=cmd_generate)

    # Variant 2: build per-language Python modules with values baked in
    b = sub.add_parser("build-languages", help="Build per-language modules (Variant 2)")
    b.add_argument(
        "--locales",
        default="lib/i18n/locales",
        help="Folder with <lang>.yml files (default: lib/i18n/locales)",
    )
    b.add_argument(
        "--dest",
        default="lib/i18n/languages",
        help="Destination folder for <lang>.py files (default: lib/i18n/languages)",
    )
    b.add_argument(
        "--base", default="en", help="Base language code for fallback merge (default: en)"
    )
    b.set_defaults(func=cmd_build_langs)

    # Demo scaffolder
    s = sub.add_parser("scaffold", help="Create example Streamlit demo project")
    s.add_argument("--into", required=True, help="Target folder for scaffolded project (required)")
    s.add_argument(
        "--out", help="Output path for dataclasses file (default: lib/i18n/dataclasses.py)"
    )
    s.add_argument(
        "--variant",
        choices=["v1", "v2"],
        default="v1",
        help="Scaffold for Variant 1 (runtime YAML) or Variant 2 (prebuilt modules). Default: v1",
    )
    s.set_defaults(func=cmd_scaffold)

    return p


# -------------------------------------------------------------------------------------------------
def main(argv=None):
    argv = argv or sys.argv[1:]
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


# -------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    raise SystemExit(main())
