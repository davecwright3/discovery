# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "discovery"
copyright = "2025, Michele Vallisneri"
author = "Michele Vallisneri"
release = "0.2"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "autoapi.extension",
    "sphinx.ext.autodoc.typehints",
    "sphinxcontrib.mermaid",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "myst_nb", # handles markdown and ipynb
]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]
intersphinx_mapping = {
    "enterprise": ("https://enterprise.readthedocs.io/en/latest/", None),
    "enterprise_extensions": ("https://enterprise-extensions.readthedocs.io/en/latest/", None),
    "pandas": ("https://pandas.pydata.org/docs/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "jax": ("https://docs.jax.dev/en/latest/", None),
}
#intersphinx_disabled_reftypes = ["*"]
autoapi_dirs = [
    "../src/discovery/",
]

autoapi_options = [
    "members",
    "undoc-members",
    "private-members",
    "show-inheritance",
    "show-module-summary",
    "special-members",
    "imported-members",
    "inherited-members",
    "show-inheritance-diagram",
]
autodoc_typehints = "description"
templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_theme_options = {
    "use_edit_page_button": True,
}
html_context = {
    "github_url": "https://github.com", # or your GitHub Enterprise site
    "github_user": "nanograv",
    "github_repo": "discovery",
    "github_version": "main",
    "doc_path": "docs/source/",
}

nb_execution_mode = "off"
