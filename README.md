# Streamlit i18n Monorepo

![Start Page](doc/startpage.png)

Internationalization (i18n) toolkit for Streamlit apps.

---

## What is the idea?

The goal of `streamlit-i18n` is simple: **separate all texts in your app from the code**, so you can easily switch between different languages.

Instead of writing text directly in your app like:

```python
print("App Title")
```

you write:

```python
print(i18n.APP.TITLE)
```

Here, `i18n.APP.TITLE` is not just a string.
It’s an element that gets its value from a translation file.

### How does it work?

All texts are stored in YAML files with a hierarchical structure.
For example, a German translation file (de.yml) might look like this:

```yaml
app:
  title: "Streamlit i18n Demo"
  desc: "Beispielanwendung"
  copyright: "© {year} Deine Firma"
  locale_name: "Deutsch (DE)"
  current_user: "Angemeldet als: {name}"
```

### Generate Python dataclasses

With the generate command from our CLI, we convert the YAML file into Python dataclasses.
This gives you strongly-typed, structured access to your translations:

```python
from dataclasses import dataclass

@dataclass
class APP:
    TITLE: str = "Streamlit i18n Demo"
    DESC: str = "Beispielanwendung"
    COPYRIGHT: str = "© {year} Deine Firma"
    LOCALE_NAME: str = "Deutsch (DE)"
    CURRENT_USER: str = "Angemeldet als: {name}"
```

### Use in your app

In your Streamlit (or plain Python) app, you load the translations and use them directly:

```python
from streamlit_i18n import I18N

def main(lang="de") -> None:
    i18n = I18N(package="lib.i18n.languages")
    i18n.init(lang=lang, base="en")

    print(i18n.APP.TITLE)
    print(i18n.APP.DESC)
```

### Switching the language at runtime is just one line

```python
i18n.set_lang("en")
```

### What’s inside this repository?

This repo contains two packages that work together:

- streamlit-i18n
  
  Runtime helpers to use dataclasses and load translations in your Streamlit app.

- streamlit-i18n-cli
  
  CLI tools to:

  - Generate dataclasses from YAML files
  - Scaffold a demo app with sample translations
  - Help you start multilingual projects quickly


This repository contains two related packages:

## 1. `streamlit-i18n`

Runtime helpers for working with translations.  

### Features

- Use YAML locale files to generated dataclasses
- Pre-generated Python modules with embedded translations
- Nested dataclass support (e.g. `i18n.PAGES.PAGE1.TITLE`)
- Fallback to a base language (e.g. English)

### Install

**Path:** `streamlit-i18n`  

```bash
pip install -e streamlit-i18n
```

## 2. streamlit-i18n-cli

CLI for development and scaffolding.

### Features

- Generate Python dataclasses from YAML files

- Scaffold a demo Streamlit multi-page app

- Create sample locales (en.yml, de.yml, …)

- Convenience commands for projects using Streamlit

### Install

**Path:** `streamlit-i18n-cli`  

```bash
pip install -e streamlit-i18n-cli
```

Provides: streamlit-i18n command

### Usage

Install both packages

```bash
pip install -e ./streamlit-i18n
pip install -e ./streamlit-i18n-cli
```

Scaffold a demo application

```bash
streamlit-i18n scaffold --into demo
```

Generate dataclasses

```bash
# Switch to demo app
cd demo

# Generate dataclasses from YAML
streamlit-i18n generate \
  -i lib/i18n/locales/en.yml \
  -o i18n/dataclasses_.py \
  --rename menu=PAGES
```

Run the demo app

```bash

cd demo
just generate
just run # streamlit run Home.py
```

## Development

### Project Layout

```bash
.
├── streamlit-i18n/        # Runtime helpers
├── streamlit-i18n-cli/    # CLI tool
├── demo/                  # Scaffolded demo project
└── tests/                 # Pytest-based test suite
```

#### Justfile

Convenience commands are included. Typical usage:

```bash
just lint      # run pre-commit linters (ruff, isort, black, mypy, etc.)
just test      # run pytest
just build     # build distributions
just release   # publish to PyPI
```

## Demo App

The scaffolded demo (demo/) illustrates:

- Multiple locales (en, de, es, fr)

- Pages showing headers, forms, navigation, messages

- Placeholders with formatting ({date}, {users}, {amount})

- Dotted API and dataclass access side by side

Run it with:

```bash
cd demo
streamlit run Home.py
```

## Testing

Run the test suite:

```bash
pytest -q
```

## Roadmap

## License
