# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
project = "{{ cookiecutter.project_name }}"
copyright = "2025, {{ cookiecutter.author_name }}"
author = "{{ cookiecutter.author_name }}"
release = "{{ cookiecutter.release }}"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx_design",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.doctest",
    "sphinx_autodoc_typehints",
    "notfound.extension",  # Custom 404 pages for dead links
    "nbsphinx",  # jupyter notebooks integration
    "sphinxcontrib.mermaid",
    "sphinx_togglebutton",
    "sphinx-pydantic",  # Support for Pydantic models
    "myst_nb",
]

togglebutton_hint = ""
togglebutton_hint_hide = ""

myst_enable_extensions = ["colon_fence"]

nbsphinx_requirejs_path = ""

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "**.ipynb_checkpoints",
    "Thumbs.db",
    ".DS_Store",
    ".env",
    ".venv",
]

source_suffix = [".markdown", ".md"]

# -- Options for HTML output -------------------------------------------------
html_static_path = ["_static"]
html_show_copyright = False
html_show_sphinx = False

import glob
import os
import shutil
import sys
from pathlib import Path

sys.path.insert(0, os.path.abspath(".."))

html_theme = "sphinx_rtd_theme"

DOCS_DIR = Path(__file__).parent.absolute()
PROJECT_DIR = DOCS_DIR.parent / "{{ cookiecutter.project_name }}"
EXTRA_APIDOC_DIR = DOCS_DIR / "api_doc_override"

# List of modules to document - customize this list for your project
modules = []

# Do not execute notebooks
nbsphinx_execute = "never"

def override_apidoc(_):
    """Override generated MD files with custom ones."""
    override_dir = EXTRA_APIDOC_DIR
    output_dir = DOCS_DIR

    for override_file in override_dir.glob("*.md"):
        output_file = output_dir / override_file.name
        shutil.copy2(override_file, output_file)
        print(f"Overriding {output_file} with {override_file}")

def get_exclude_files(project_dir: Path, exclude_patterns: list) -> list:
    exclude_files = []
    for pattern in exclude_patterns:
        full_pattern = str(project_dir / pattern)
        matched_files = glob.glob(full_pattern, recursive=True)
        for file in matched_files:
            file_path = Path(file)
            if file_path.is_file():
                exclude_files.append(file_path)
    return exclude_files

def setup(app):
    app.connect("builder-inited", override_apidoc)
