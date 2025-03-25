"""
GUÍA DE REFERENCIA: CONFIGURACIÓN DEL ENTORNO PYTHON
=================================================

Esta guía explica los pasos básicos para configurar un entorno
de desarrollo en Python y las mejores prácticas.
"""

# ============= ENTORNOS VIRTUALES =============

"""
1. Crear un entorno virtual:
   Windows: python -m venv nombre_entorno
   Linux/Mac: python3 -m venv nombre_entorno

2. Activar el entorno virtual:
   Windows: nombre_entorno\\Scripts\\activate
   Linux/Mac: source nombre_entorno/bin/activate

3. Desactivar el entorno virtual:
   deactivate
"""

# ============= GESTIÓN DE PAQUETES =============

"""
1. Instalar paquetes:
   pip install nombre_paquete
   pip install nombre_paquete==version

2. Instalar desde requirements.txt:
   pip install -r requirements.txt

3. Listar paquetes instalados:
   pip list

4. Generar requirements.txt:
   pip freeze > requirements.txt
"""

# Ejemplo de requirements.txt
REQUIREMENTS = """
# requirements.txt
numpy==1.21.0
pandas==1.3.0
matplotlib==3.4.2
"""

# ============= ESTRUCTURA DE PROYECTO =============

"""
proyecto/
│
├── README.md           # Documentación del proyecto
├── requirements.txt    # Dependencias del proyecto
├── .gitignore         # Archivos a ignorar en git
├── setup.py           # Configuración del paquete
│
├── mi_proyecto/       # Código fuente
│   ├── __init__.py
│   ├── modulo1.py
│   └── modulo2.py
│
├── tests/            # Pruebas unitarias
│   ├── __init__.py
│   ├── test_modulo1.py
│   └── test_modulo2.py
│
└── docs/             # Documentación
    ├── conf.py
    └── index.rst
"""

# ============= VARIABLES DE ENTORNO =============

"""
1. Configurar variables de entorno:
   Windows: set VARIABLE=valor
   Linux/Mac: export VARIABLE=valor

2. Usar variables de entorno en Python:
"""
import os

def ejemplo_variables_entorno():
    # Obtener variable de entorno
    api_key = os.getenv('API_KEY', 'valor_por_defecto')
    
    # Establecer variable de entorno
    os.environ['MI_VARIABLE'] = 'valor'

# ============= EDITORES RECOMENDADOS =============

"""
1. Visual Studio Code
   - Extensiones recomendadas:
     * Python (Microsoft)
     * Pylance
     * Python Test Explorer
     * Python Docstring Generator

2. PyCharm
   - Versión Community (gratuita)
   - Versión Professional (de pago)

3. Jupyter Notebook
   - Para análisis de datos y prototipado
   - Instalación: pip install jupyter
"""

# ============= HERRAMIENTAS DE DESARROLLO =============

"""
1. Linters y Formatters:
   - flake8: pip install flake8
   - black: pip install black
   - pylint: pip install pylint

2. Debugging:
   - pdb (incluido en Python)
   - ipdb: pip install ipdb

3. Testing:
   - pytest: pip install pytest
   - unittest (incluido en Python)
"""

if __name__ == "__main__":
    print("Esta es una guía de referencia para la configuración del entorno Python.")
    print("Revisa los comentarios y docstrings para más información.") 