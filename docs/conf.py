# docs/conf.py

from __future__ import annotations

from datetime import datetime

from turtini_sphinx_theme import get_theme_paths


# -----------------------------------------------------
# Project metadata
# -----------------------------------------------------

project = "Turtini Documentation"
author = "Turtini LLC"
copyright = f"{datetime.utcnow().year}, Turtini LLC"


# -----------------------------------------------------
# Extensions
# -----------------------------------------------------

extensions = [
    "myst_parser",
]


# -----------------------------------------------------
# Source configuration
# -----------------------------------------------------

source_suffix = {
    ".md": "markdown",
}

root_doc = "index"

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]


# -----------------------------------------------------
# Theme configuration
# -----------------------------------------------------

html_theme = "sphinx_rtd_theme"

html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 4,
}


# -----------------------------------------------------
# Shared theme assets from turtini-sphinx-theme
# -----------------------------------------------------

_paths = get_theme_paths()

templates_path = [_paths["templates"]]
html_static_path = ["_static", _paths["static"]]

html_css_files = [
    "turtini.css",
]


# -----------------------------------------------------
# Branding
# -----------------------------------------------------

html_logo = "_static/turtini-logo.png"
html_favicon = "_static/favicon.ico"


# -----------------------------------------------------
# MyST configuration
# -----------------------------------------------------

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "tasklist",
    "attrs_inline",
]


# -----------------------------------------------------
# Footer / build metadata
# -----------------------------------------------------

html_last_updated_fmt = "%B %d, %Y"


# -----------------------------------------------------
# Template variables
# -----------------------------------------------------

html_context = {
    "turtini_year": datetime.utcnow().year,
}


# -----------------------------------------------------
# Base URL (used by Read the Docs)
# -----------------------------------------------------

html_baseurl = ""
