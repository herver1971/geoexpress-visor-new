# docs/source/conf.py

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from sphinx_rtd_theme import get_html_theme_path

# -- Path setup --------------------------------------------------------------

# Añadir el directorio raíz del proyecto al PATH para importar módulos personalizados
sys.path.insert(0, os.path.abspath('../../'))

# -- Project information -----------------------------------------------------

project = 'GeoExpress Visor'
copyright = '2024, Kan Territory & IT'
author = 'Kan Territory & IT'
release = '2.2.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.autosummary',
    'sphinxcontrib.openapi',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'es'
locale_dirs = ['../locale/']   # Directorio que contiene los archivos de traducción
gettext_compact = False         # Para evitar la compresión de mensajes en un solo archivo

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_theme_path = [get_html_theme_path()]
html_static_path = ['_static']

# -- Options for LaTeX output ------------------------------------------------

latex_engine = 'xelatex'
latex_show_urls = 'footnote'
latex_additional_files = ['_static/images/cabecerakan.png']

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'passoptionstopackages': r'''
\PassOptionsToPackage{svgnames}{xcolor}
''',
    'fontpkg': r'''
\setmainfont{DejaVu Serif}
\setsansfont{DejaVu Sans}
\setmonofont{DejaVu Sans Mono}
''',
    'preamble': r'''
% Paquetes adicionales
\usepackage[firstpage=true]{background}
\usepackage{graphicx} % Asegura que graphicx esté cargado

% Definir la ruta de búsqueda para imágenes
\graphicspath{{_static/images/}}

% Configuración de la imagen de fondo para la primera página
\backgroundsetup{
  scale=1,
  color=black,
  opacity=0.3,
  angle=0,
  contents={\includegraphics[width=\paperwidth,height=\paperheight]{cabecerakan.png}} % Ruta relativa de la imagen
}

% Eliminar el autor y la fecha en el título
\author{}  % Vaciar el autor
\date{}    % Eliminar la fecha

% Configuración de la tabla de contenidos y estilos
\usepackage[titles]{tocloft}
\cftsetpnumwidth{1.25cm}
\cftsetrmarg{1.5cm}
\setlength{\cftchapnumwidth}{0.75cm}
\setlength{\cftsecindent}{\cftchapnumwidth}
\setlength{\cftsecnumwidth}{1.25cm}
\renewcommand{\cftsecpagefont}{\color{red}}

% Estilo de los capítulos
\usepackage[Bjornstrup]{fncychap}
''',
    'sphinxsetup': '''
    TitleColor={RGB}{240,56,97},
    InnerLinkColor={RGB}{240,56,97},
''',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'printindex': r'\footnotesize\raggedright\printindex',

}

# Opciones adicionales de LaTeX, si las hay, pueden añadirse aquí
