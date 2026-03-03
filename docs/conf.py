# docs/conf.py

import os
from datetime import datetime

project = "Turtini Documentation"
author = "Turtini LLC"
copyright = f"{datetime.now().year}, Turtini LLC"

extensions = [
    "myst_parser",
]

# Templates + static assets
templates_path = ["_templates"]
html_static_path = ["_static"]

# Theme + styling
html_theme = "sphinx_rtd_theme"
html_css_files = ["turtini.css"]

# Brand assets (this is what makes the logo + favicon show up)
html_logo = "_static/turtini-logo.png"
html_favicon = "_static/favicon.ico"

# Read the Docs / canonical base URL (optional but fine to keep)
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")

# Source file types
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# Page title (tab title)
html_title = "Turtini Documentation"
