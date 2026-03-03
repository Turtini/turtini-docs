import os
from datetime import datetime

project = "Turtini Documentation"
author = "Turtini LLC"
copyright = f"{datetime.now().year}, Turtini LLC"

extensions = [
    "myst_parser",
]

templates_path = ["_templates"]
html_static_path = ["_static"]

html_theme = "sphinx_rtd_theme"
html_css_files = ["turtini.css"]

html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

html_title = "Turtini Documentation"
