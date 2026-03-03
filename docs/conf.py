# docs/conf.py

from datetime import datetime

project = "Turtini Documentation"
author = "Turtini LLC"
copyright = f"{datetime.utcnow().year}, Turtini LLC"

# Extensions
extensions = [
    "myst_parser",
]

# Markdown support
source_suffix = {
    ".md": "markdown",
}

# Sphinx root doc (index.md -> index.html)
root_doc = "index"

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]

# Theme
html_theme = "sphinx_rtd_theme"

html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 4,
}

# MyST options (same style you used elsewhere)
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "tasklist",
    "attrs_inline",
]

# Templates (for docs/_templates/layout.html overrides)
templates_path = ["_templates"]

# Static assets live in docs/_static
html_static_path = ["_static"]

#These two lines are what make the logo + favicon actually show up
html_logo = "_static/turtini-logo.png"
html_favicon = "_static/favicon.ico"

# Your custom CSS/JS (only include if these files exist in docs/_static)
html_css_files = [
    "turtini.css",
]

# If you have no JS file in this repo, remove this section
# html_js_files = [
#     "turtini-banner.js",
# ]

# “Last updated” formatting (populates the RTD theme footer field)
html_last_updated_fmt = "%B %d, %Y"

# Custom variables usable in Jinja templates (like your footer year)
html_context = {
    "turtini_year": datetime.utcnow().year,
}

# Optional: help Sphinx build correct canonical-ish URLs when RTD provides it
html_baseurl = ""
