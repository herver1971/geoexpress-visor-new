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
latex_additional_files = ['_static/images/cabecerakan.png',
'_static/images/logokan.png',
'_static/images/encabezado.png']

latex_elements = {
    'pointsize': '11pt',
    'classoptions': ',openany',
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
\usepackage{graphicx}
\usepackage{titling}
\usepackage{etoolbox}
\usepackage[titles]{tocloft}
\usepackage{xcolor}
\usepackage{geometry}


\usepackage{fancyhdr}
\pagestyle{fancy}


% Definir la ruta de búsqueda para imágenes
\graphicspath{{_static/images/}}

% Configuración de la imagen de fondo para la primera página
\backgroundsetup{
  scale=1,
  color=black,
  opacity=0.3,
  angle=0,
  contents={\includegraphics[width=\paperwidth,height=\paperheight]{logokan.png}}
}

% Ocultar autor y fecha, asegurando que no se muestren
\preauthor {}  % Vaciar autor
\postauthor {}  % Sin efecto de autor
\predate {}  % Sin fecha
\date {}
\postdate {}  % Sin fecha

% Definir la macro de versión a partir del valor en conf.py
\newcommand{\therelease}{''' + release + r'''}

    % Redefinir \sphinxmaketitle para ajustar la posición y formato del título
    \renewcommand{\sphinxmaketitle}{%
      \begingroup
        \begin{center}
          \vspace*{6cm}  % Mover el título hacia abajo
          {\Huge \textbf{\color[RGB]{245,63,97} \thetitle}}  % Título del proyecto en grande y color magenta
          \vspace{0.5cm}  % Espacio entre el título y la versión
          \\
          {\Large \textbf{\color[RGB]{245,63,97} Versión:} \color[RGB]{245,63,97} \therelease}  % Mostrar la versión en grande y en color magenta
        \end{center}
      \endgroup
    }


% Configuración de la tabla de contenidos y estilos
\cftsetpnumwidth{1.25cm}
\cftsetrmarg{1.5cm}
\setlength{\cftchapnumwidth}{0.75cm}
\setlength{\cftsecindent}{\cftchapnumwidth}
\setlength{\cftsecnumwidth}{1.25cm}
\renewcommand{\cftsecpagefont}{\color{red}}

    % Configurar estilo de las páginas de los capítulos
    \fancypagestyle{normal}{ % Estilo para las páginas de los capítulos
        \fancyhf{}  % Eliminar cualquier encabezado y pie por defecto
        \fancyhead[C]{\includegraphics{encabezado.png}}        
        \renewcommand{\headrulewidth}{0pt}  % Eliminar la línea del encabezado
        \renewcommand{\footrulewidth}{0pt}  % Eliminar la línea del pie de página
        \rfoot[\thepage]{\thepage}  % Numerar las páginas de los capítulos en el centro
    }

    % Asegurar que solo las páginas de los capítulos muestren la numeración en arábigos
    \renewcommand{\chapterpagestyle}{normal}  % Aplicar estilo 'normal' a las páginas de los capítulos
    \pagenumbering{arabic}  % Usar numeración arábiga para las páginas del capítulo

% Establecer color y alineación predeterminados para el contenido principal
    \AtBeginDocument{%
      \color{black}  % Establece el color del texto principal a negro
      \raggedright   % Alinea el texto a la izquierda sin justificar
    }

''',
    'sphinxsetup': '''
    InnerLinkColor={RGB}{245,63,97},
    verbatimwithframe=false,
    VerbatimColor={rgb}{0.9,0.9,0.9},
    VerbatimBorderColor={rgb}{0.8,0.8,0.8},
    ''',

    'printindex': r'\footnotesize\raggedright\printindex',
}


# Opciones adicionales de LaTeX, si las hay, pueden añadirse aquí
