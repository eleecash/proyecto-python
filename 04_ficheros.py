"""
GUÍA DE REFERENCIA: MANEJO DE FICHEROS EN PYTHON
============================================

Esta guía cubre las diferentes formas de trabajar con archivos
en Python, incluyendo texto, CSV, JSON y otros formatos.
"""

import os
import csv
import json
import pickle
import shutil

# ============= ARCHIVOS DE TEXTO =============

def ejemplos_archivos_texto():
    """Ejemplos de manejo de archivos de texto"""
    print("\n=== ARCHIVOS DE TEXTO ===")
    
    # Escribir archivo
    print("\n1. Escribir archivo:")
    with open("ejemplo.txt", "w", encoding="utf-8") as archivo:
        archivo.write("Línea 1\n")
        archivo.write("Línea 2\n")
        archivo.writelines(["Línea 3\n", "Línea 4\n"])
    
    # Leer archivo completo
    print("\n2. Leer archivo completo:")
    with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        print(contenido)
    
    # Leer línea por línea
    print("\n3. Leer línea por línea:")
    with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            print(f"Línea: {linea.strip()}")
    
    # Añadir al archivo (append)
    print("\n4. Añadir contenido:")
    with open("ejemplo.txt", "a", encoding="utf-8") as archivo:
        archivo.write("Línea añadida\n")

# ============= ARCHIVOS CSV =============

def ejemplos_archivos_csv():
    """Ejemplos de manejo de archivos CSV"""
    print("\n=== ARCHIVOS CSV ===")
    
    # Escribir CSV
    print("\n1. Escribir CSV:")
    datos = [
        ["Nombre", "Edad", "Ciudad"],
        ["Ana", "25", "Madrid"],
        ["Juan", "30", "Barcelona"]
    ]
    
    with open("datos.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(datos)
    
    # Leer CSV
    print("\n2. Leer CSV:")
    with open("datos.csv", "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            print(f"Fila: {fila}")
    
    # Usar DictWriter y DictReader
    print("\n3. CSV con diccionarios:")
    datos_dict = [
        {"nombre": "Ana", "edad": "25", "ciudad": "Madrid"},
        {"nombre": "Juan", "edad": "30", "ciudad": "Barcelona"}
    ]
    
    with open("datos_dict.csv", "w", newline="", encoding="utf-8") as archivo:
        campos = ["nombre", "edad", "ciudad"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(datos_dict)
    
    with open("datos_dict.csv", "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            print(f"Registro: {fila}")

# ============= ARCHIVOS JSON =============

def ejemplos_archivos_json():
    """Ejemplos de manejo de archivos JSON"""
    print("\n=== ARCHIVOS JSON ===")
    
    # Datos de ejemplo
    datos = {
        "nombre": "Ana",
        "edad": 25,
        "ciudades_visitadas": ["Madrid", "Barcelona", "Valencia"],
        "activo": True,
        "altura": 1.65
    }
    
    # Escribir JSON
    print("\n1. Escribir JSON:")
    with open("datos.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
    
    # Leer JSON
    print("\n2. Leer JSON:")
    with open("datos.json", "r", encoding="utf-8") as archivo:
        datos_leidos = json.load(archivo)
        print(f"Datos leídos: {datos_leidos}")
    
    # Convertir a/desde string JSON
    print("\n3. Trabajar con strings JSON:")
    json_str = json.dumps(datos, indent=2)
    print(f"String JSON:\n{json_str}")
    
    datos_desde_str = json.loads(json_str)
    print(f"Datos desde string: {datos_desde_str}")

# ============= ARCHIVOS BINARIOS =============
# Los archivos binarios son aquellos que contienen datos en formato binario, es decir, no en formato de texto.
# Son útiles para almacenar datos como imágenes, videos, audio y otros tipos de datos no textuales.

def ejemplos_archivos_binarios():
    """Ejemplos de manejo de archivos binarios"""
    print("\n=== ARCHIVOS BINARIOS ===")
    
    # Serialización con pickle
    # pickle es una biblioteca que permite serializar y deserializar objetos Python.
    print("\n1. Serialización con pickle:")
    datos = {
        "numeros": [1, 2, 3, 4, 5],
        "texto": "Ejemplo",
        "diccionario": {"a": 1, "b": 2}
    }
    
    # Escribir con pickle
    with open("datos.pkl", "wb") as archivo:
        pickle.dump(datos, archivo)
    
    # Leer con pickle
    with open("datos.pkl", "rb") as archivo:
        datos_leidos = pickle.load(archivo)
        print(f"Datos deserializados: {datos_leidos}")

# ============= OPERACIONES CON ARCHIVOS =============

def ejemplos_operaciones_archivos():
    """Ejemplos de operaciones con archivos y directorios"""
    print("\n=== OPERACIONES CON ARCHIVOS ===")
    
    # Crear directorio
    print("\n1. Operaciones con directorios:")
    os.makedirs("mi_directorio", exist_ok=True)
    
    # Listar contenido de directorio
    print("\nContenido del directorio actual:")
    print(os.listdir("."))
    
    # Comprobar si existe
    archivo = "ejemplo.txt"
    print(f"\n¿Existe {archivo}?: {os.path.exists(archivo)}")
    
    # Copiar archivo
    if os.path.exists(archivo):
        shutil.copy2(archivo, "mi_directorio/ejemplo_copia.txt")
    
    # Mover/renombrar archivo
    if os.path.exists("mi_directorio/ejemplo_copia.txt"):
        os.rename("mi_directorio/ejemplo_copia.txt", 
                 "mi_directorio/nuevo_nombre.txt")
    
    # Eliminar archivo
    if os.path.exists("mi_directorio/nuevo_nombre.txt"):
        os.remove("mi_directorio/nuevo_nombre.txt")
    
    # Eliminar directorio
    if os.path.exists("mi_directorio"):
        os.rmdir("mi_directorio")

# ============= BUENAS PRÁCTICAS =============

def ejemplo_buenas_practicas():
    """Ejemplos de buenas prácticas en el manejo de archivos"""
    print("\n=== BUENAS PRÁCTICAS ===")
    
    # 1. Usar with para manejo seguro
    print("\n1. Uso de with:")
    try:
        with open("archivo.txt", "w") as f:
            f.write("Contenido")
    except IOError as e:
        print(f"Error de E/S: {e}")
    
    # 2. Manejo de codificación
    print("\n2. Especificar codificación:")
    with open("unicode.txt", "w", encoding="utf-8") as f:
        f.write("Texto con caracteres especiales: áéíóú")
    
    # 3. Manejo de rutas
    print("\n3. Rutas independientes del sistema:")
    ruta = os.path.join("directorio", "subdirectorio", "archivo.txt")
    print(f"Ruta: {ruta}")

if __name__ == "__main__":
    print("EJEMPLOS DE MANEJO DE FICHEROS")
    print("============================")
    
    ejemplos_archivos_texto()
    ejemplos_archivos_csv()
    ejemplos_archivos_json()
    ejemplos_archivos_binarios()
    ejemplos_operaciones_archivos()
    ejemplo_buenas_practicas()
    
    # Limpieza de archivos de ejemplo
    archivos_ejemplo = ["ejemplo.txt", "datos.csv", "datos_dict.csv", 
                       "datos.json", "datos.pkl", "unicode.txt"]
    
    for archivo in archivos_ejemplo:
        if os.path.exists(archivo):
            os.remove(archivo) 