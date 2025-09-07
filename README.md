
# Streamlit i18n Monorepo

This repository contains two related packages:

## 1. streamlit-i18n
Runtime helpers for loading YAML into generated dataclasses for Streamlit apps.

- Path: `streamlit-i18n`
- Install: `pip install -e streamlit-i18n`

## 2. streamlit-i18n-cli
CLI to generate dataclasses from YAML and scaffold a demo Streamlit app with sample locales.

- Path: `streamlit-i18n-cli`
- Install: `pip install -e streamlit-i18n-cli`
- Provides `streamlit-i18n` command

### Usage
```bash
# Scaffold a demo
streamlit-i18n scaffold --into .

# Generate dataclasses
streamlit-i18n generate -i locales/en.yml -o i18n/dataclasses_.py --rename menu=PAGES
```
