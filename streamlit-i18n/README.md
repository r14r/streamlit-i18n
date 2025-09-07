# streamlit-i18n

Runtime helpers to load YAML translations into **generated dataclasses** (`i18n/dataclasses_.py`) for use in Streamlit apps.

## Install
```bash
pip install streamlit-i18n
```

## Usage
```python
from streamlit_i18n import init, t, set_lang, has, missing_keys
init("de", locales_dir="locales", base_lang="en")
```