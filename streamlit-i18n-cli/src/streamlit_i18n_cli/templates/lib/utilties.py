from __future__ import annotations
from pathlib import Path
import yaml

LOCALES_DIR = Path("locales")

def list_languages() -> list[str]:
    if not LOCALES_DIR.exists():
        return []
    return sorted([p.stem for p in LOCALES_DIR.glob("*.yml")])

def read_lang(lang: str):
    p = LOCALES_DIR / f"{lang}.yml"
    return yaml.safe_load(p.read_text(encoding="utf-8")) if p.exists() else {}

def write_lang(lang: str, data: dict):
    p = LOCALES_DIR / f"{lang}.yml"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")

def flatten(d: dict, prefix=""):
    for k, v in (d or {}).items():
        key = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            yield from flatten(v, key)
        else:
            yield key, v

def unflatten(rows: dict) -> dict:
    root = {}
    for dotted, val in rows.items():
        cur = root
        parts = dotted.split(".")
        for p in parts[:-1]:
            cur = cur.setdefault(p, {})
        cur[parts[-1]] = val
    return root