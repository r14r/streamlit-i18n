import importlib.util
from pathlib import Path
import types

def _import_app_module():
    # try common locations
    for candidate in (Path("app.py"), Path("demo/app.py"), Path("demo.py")):
        if candidate.exists():
            spec = importlib.util.spec_from_file_location("app", candidate)
            mod = importlib.util.module_from_spec(spec)
            assert spec and spec.loader
            spec.loader.exec_module(mod)  # type: ignore[attr-defined]
            return mod
    raise ModuleNotFoundError("No demo app found (tried app.py, demo/app.py, demo.py).")

def test_demo_app_prints_sections(capsys):
    app = _import_app_module()
    assert hasattr(app, "main") and isinstance(app.main, types.FunctionType)

    app.main(lang="de")
    out = capsys.readouterr().out

    assert "# APP / HEADER" in out
    assert "# NAVIGATION" in out
    assert "# MESSAGES & ERRORS" in out
    assert "# FORMS" in out
    assert "# PAGES" in out
    assert "# FOOTER" in out
    assert "Dotted:" in out
    assert "Has app.title?" in out
