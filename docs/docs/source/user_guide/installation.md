# Installation Guide

This guide will help you install {{ cookiecutter.project_name }}.

## Requirements

- Python 3.8 or higher
- pip package manager

## Quick Install

```bash
pip install {{ cookiecutter.project_slug }}
```

## Development Install

For development, you might want to install in editable mode:

```bash
git clone https://github.com/username/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}
pip install -e ".[dev]"
```

## Verifying Installation

You can verify your installation by running:

```python
import {{ cookiecutter.project_slug }}
print({{ cookiecutter.project_slug }}.__version__)
```
