# i18n_v2.py
from __future__ import annotations

import importlib
import pkgutil
import re
from dataclasses import fields, is_dataclass
from types import ModuleType
from typing import Any


class I18N:
    def __init__(
        self,
        package: str = "i18n.languages",
        module_template: str = "{lang}",
    ) -> None:
        self._package = package
        self._tmpl = module_template
        self._active_mod: ModuleType | None = None
        self._base_mod: ModuleType | None = None
        self._lang: str | None = None
        self._base_lang: str | None = None

    # ---------- Public API ----------
    def init(self, lang: str, base: str = "en") -> None:
        """Sprache setzen und Instanzen + Fallbacks vorbereiten."""
        self._lang = lang
        self._base_lang = base
        self._active_mod = self._import_lang_module(lang)
        self._base_mod = self._import_lang_module(base)
        self._ensure_instances(self._active_mod)
        self._ensure_instances(self._base_mod)
        self._merge_missing(self._active_mod, self._base_mod)
        for name, obj in list(self._active_mod.__dict__.items()):
            if self._is_dc_instance(obj):
                setattr(self, name, obj)

    def set_lang(self, lang: str) -> None:
        if self._base_lang is None:
            raise RuntimeError("init() must be called before set_lang().")
        self.init(lang, self._base_lang)

    def t(self, dotted: str, variables: dict[str, Any] | None = None) -> str:
        """Dotted Lookup über die aktive Sprache (bereits mit Base-Fallback gemerged)."""
        obj: Any = self
        for part in dotted.split("."):
            name = part.upper()
            if hasattr(obj, name):
                obj = getattr(obj, name)
            else:
                return ""
        if isinstance(obj, str):
            return obj.format(**(variables or {}))
        return ""

    def has(self, dotted: str) -> bool:
        return bool(self.t(dotted))

    def languages(self) -> list[str]:
        """
        Liste aller verfügbaren Sprach-Codes gemäß package + module_template.
        Beispiel:
          package="i18n.languages", module_template="{lang}"
          -> scannt i18n/languages und erkennt de.py, en.py, ...
        """
        try:
            pkg = importlib.import_module(self._package)
        except Exception:
            return []

        # Template -> Regex: "{lang}" => (?P<lang>[A-Za-z0-9_\-]+)
        tmpl_regex = re.escape(self._tmpl).replace(
            r"\{lang\}", r"(?P<lang>[A-Za-z0-9_\-]+)"
        )
        pattern = re.compile(rf"^{tmpl_regex}$")

        langs: list[str] = []
        # pkg.__path__ exists for packages (regular and namespace)
        for _, name, _ in pkgutil.iter_modules(getattr(pkg, "__path__", [])):
            m = pattern.match(name)
            if m:
                langs.append(m.group("lang"))
        # uniq + sorted
        return sorted(set(langs))

    # ---------- Internals ----------
    def _import_lang_module(self, lang: str) -> ModuleType:
        full = f"{self._package}.{self._tmpl.format(lang=lang)}"
        try:
            return importlib.import_module(full)
        except Exception as e:
            raise RuntimeError(f"Could not import language module '{full}'.") from e

    @staticmethod
    def _is_dc_type(x: Any) -> bool:
        return isinstance(x, type) and is_dataclass(x)

    @staticmethod
    def _is_dc_instance(x: Any) -> bool:
        return is_dataclass(x) and not isinstance(x, type)

    def _ensure_instances(self, mod: ModuleType) -> None:
        """
        Ersetze Dataclass-KLASSEN am Modul durch INSTANZEN
        und instanziiere verschachtelte Dataclasses.
        """
        for name, obj in list(mod.__dict__.items()):
            if self._is_dc_type(obj):
                inst = obj()
                setattr(mod, name, inst)
                self._instantiate_nested(inst)

    def _instantiate_nested(self, inst: Any) -> None:
        cls = inst.__class__
        for name, attr in list(cls.__dict__.items()):
            if self._is_dc_type(attr):  # verschachtelte DC-Klasse
                sub = attr()
                setattr(inst, name, sub)
                self._instantiate_nested(sub)

    def _merge_missing(self, active_mod: ModuleType, base_mod: ModuleType) -> None:
        """Fülle fehlende/leere Strings der aktiven Instanzen aus der Base-Instanz nach."""
        for name, a in list(active_mod.__dict__.items()):
            b = getattr(base_mod, name, None)
            if self._is_dc_instance(a) and self._is_dc_instance(b):
                self._merge_dc_instances(a, b)

    def _merge_dc_instances(self, a: Any, b: Any) -> None:
        af = {f.name: f for f in fields(a)}
        # bf = {f.name: f for f in fields(b)}

        for fname in af:
            av = getattr(a, fname, None)
            bv = getattr(b, fname, None)
            # verschachtelte DC?
            if self._is_dc_instance(av) and self._is_dc_instance(bv):
                self._merge_dc_instances(av, bv)
            # Leaf-String → nur leere Strings überschreiben
            elif isinstance(av, str) and isinstance(bv, str) and (av == "" or av is None):
                setattr(a, fname, bv)


i18n = I18N()

__all__ = ["I18N", "i18n" ]
