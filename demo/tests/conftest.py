import sys
from pathlib import Path

import pytest


@pytest.fixture(scope="session", autouse=True)
def ensure_project_on_sys_path():
    root = Path.cwd()
    lib = root / "lib"

    print(f"conftest: adding {root} and {lib} to sys.path")
    
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))

    if lib.exists() and str(lib) not in sys.path:
        sys.path.insert(0, str(lib))

    yield
