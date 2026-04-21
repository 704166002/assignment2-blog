# Configuration file for the Sphinx documentation builder.

project = 'Static Personal Blog Website'
copyright = '2026, Zixuan Gao'
author = 'Zixuan Gao'

extensions = [
    'sphinx.ext.autodoc',
    'myst_parser',
    'sphinx.ext.mathjax',
]

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']
