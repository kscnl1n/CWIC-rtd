# conf.py
# this is the generic theme for the readthedocs website - can be changed if a different appearance for the site is desires.

import os
import sys
sys.path.insert(0, os.path.abspath('..'))  # or '.' if you're documenting a standalone project

project = 'MyProject'
author = 'Your Name'
release = '0.1'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'myst_parser',  # only needed if you're using Markdown
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}


templates_path = ['_templates']
exclude_patterns = []

# HTML theme
html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

