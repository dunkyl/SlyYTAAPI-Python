# Project

project = 'SlyYTAAPI for Python'
copyright = '2023, Dunkyl 🔣🔣'
author = 'Dunkyl 🔣🔣'

# Extensions

extensions = [
    'myst_parser',
    'sphinxcontrib_trio',
    'sphinx_copybutton',
    'sphinxext.opengraph',
    "sphinx.ext.intersphinx",
    'sphinx.ext.autodoc',
    'sphinx.ext.duration',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.coverage',
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "aiohttp": ("https://docs.aiohttp.org/en/stable/", None),
    "SlyAPI": ("https://docs.dunkyl.net/SlyAPI-Python/", None),
}

napoleon_use_rtype = False
napoleon_numpy_docstring = False
napoleon_preprocess_types = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True

autoclass_content = "both"
autosummary_generate = True
numpydoc_show_class_members = False

myst_heading_anchors = 3

autodoc_default_options = {
    "members": True,
    "inherited-members": False,
    "private-members": False,
    "show-inheritance": True,
    "undoc-members": True,
    "member-order": "bysource",
    "special-members": "__await__",
}

autodoc_member_order = 'bysource'
autodoc_typehints = "description"

# Sphinx Behavior

templates_path = ['_templates']
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store']

# HTML Behavior

html_theme = 'furo'
html_static_path = ['_static']
html_title = 'SlySheets for Python'
html_theme_options = {
    "source_repository": "https://github.com/dunkyl/SlyYTAAPI-Python/",
    "source_branch": "main",
    "source_directory": "docs/",
}
html_favicon = '_static/sly logo py.svg'
html_logo = html_favicon

ogp_social_cards = {
    "enable": False
}
