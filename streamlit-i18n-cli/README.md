# streamlit-i18n-cli

CLI to generate `i18n/dataclasses_.py` from YAML and scaffold Streamlit example pages.

## Install
```bash
pip install streamlit-i18n-cli
```

## Commands
```bash
streamlit-i18n generate -i locales/en.yml -o i18n/dataclasses_.py --rename menu=PAGES
streamlit-i18n scaffold --into .
```

### Scaffold output
- `Home.py` + `pages/` (Streamlit multi-page app)
- `lib/utilities` helpers
- `lib/818n8/locales/` with sample `en.yml` and `de.yml` for a demo project


### Options

- `--into PATH` – target folder to scaffold into (default: current directory).
- `--out PATH` – output path for the generated dataclasses file used by the scaffolded Justfile (default: `lib/i18n/dataclasses_.py`).

Example:
```bash
streamlit-i18n scaffold --into demo --out src/i18n/dataclasses_.py
```
