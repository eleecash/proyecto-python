"""
GUÍA DE REFERENCIA: LECTURA DE ARCHIVOS EN PYTHON
===============================================

Este archivo contiene ejemplos prácticos de cómo leer
diferentes tipos de archivos en Python.
"""

import csv
import json
import xml.etree.ElementTree as ET
import yaml  # Requiere instalar: pip install pyyaml
import pandas as pd  # Requiere instalar: pip install pandas

# ============= ARCHIVOS DE TEXTO PLANO =============

def ejemplo_archivo_texto():
    """Ejemplos de lectura de archivos de texto"""
    print("\n=== LECTURA DE ARCHIVOS DE TEXTO ===")
    
    # Método 1: Lectura básica
    print("\n1. Lectura básica del archivo completo:")
    try:
        with open('ejemplo.txt', 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            print(f"Contenido completo:\n{contenido}")
    except FileNotFoundError:
        print("Nota: Crea un archivo 'ejemplo.txt' para probar este código")

    # Método 2: Lectura línea por línea
    print("\n2. Lectura línea por línea:")
    try:
        with open('ejemplo.txt', 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                print(f"Línea: {linea.strip()}")
    except FileNotFoundError:
        print("Archivo no encontrado")

    # Método 3: Lectura en lista de líneas
    print("\n3. Lectura en lista de líneas:")
    try:
        with open('ejemplo.txt', 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            print(f"Lista de líneas: {lineas}")
    except FileNotFoundError:
        print("Archivo no encontrado")

# ============= ARCHIVOS CSV =============

def ejemplo_archivo_csv():
    """Ejemplos de lectura de archivos CSV"""
    print("\n=== LECTURA DE ARCHIVOS CSV ===")
    
    # Método 1: Usando el módulo csv
    print("\n1. Lectura con módulo csv:")
    try:
        with open('ejemplo.csv', 'r', encoding='utf-8') as archivo:
            lector_csv = csv.reader(archivo)
            for fila in lector_csv:
                print(f"Fila: {fila}")
    except FileNotFoundError:
        print("Nota: Crea un archivo 'ejemplo.csv' para probar este código")

    # Método 2: Usando pandas (más potente)
    print("\n2. Lectura con pandas:")
    try:
        df = pd.read_csv('ejemplo.csv')
        print("Primeras 5 filas del DataFrame:")
        print(df.head())
    except FileNotFoundError:
        print("Archivo no encontrado")

    # Método 3: CSV con diccionarios
    print("\n3. Lectura como diccionarios:")
    try:
        with open('ejemplo.csv', 'r', encoding='utf-8') as archivo:
            lector_dict = csv.DictReader(archivo)
            for fila in lector_dict:
                print(f"Fila como diccionario: {fila}")
    except FileNotFoundError:
        print("Archivo no encontrado")

# ============= ARCHIVOS JSON =============

def ejemplo_archivo_json():
    """Ejemplos de lectura de archivos JSON"""
    print("\n=== LECTURA DE ARCHIVOS JSON ===")
    
    # Método 1: Lectura básica
    print("\n1. Lectura básica de JSON:")
    try:
        with open('ejemplo.json', 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            print(f"Datos JSON: {datos}")
    except FileNotFoundError:
        print("Nota: Crea un archivo 'ejemplo.json' para probar este código")

    # Método 2: Usando pandas
    print("\n2. Lectura con pandas:")
    try:
        df = pd.read_json('ejemplo.json')
        print("DataFrame desde JSON:")
        print(df)
    except FileNotFoundError:
        print("Archivo no encontrado")

# ============= ARCHIVOS XML =============

def ejemplo_archivo_xml():
    """Ejemplos de lectura de archivos XML"""
    print("\n=== LECTURA DE ARCHIVOS XML ===")
    
    # Método 1: Usando ElementTree
    print("\n1. Lectura básica de XML:")
    try:
        tree = ET.parse('ejemplo.xml')
        root = tree.getroot()
        print(f"Elemento raíz: {root.tag}")
        
        # Recorrer elementos
        for child in root:
            print(f"Elemento: {child.tag}, Atributos: {child.attrib}")
            
    except FileNotFoundError:
        print("Nota: Crea un archivo 'ejemplo.xml' para probar este código")

    # Método 2: Usando pandas
    print("\n2. Lectura con pandas:")
    try:
        df = pd.read_xml('ejemplo.xml')
        print("DataFrame desde XML:")
        print(df)
    except FileNotFoundError:
        print("Archivo no encontrado")

# ============= ARCHIVOS YAML =============

def ejemplo_archivo_yaml():
    """Ejemplos de lectura de archivos YAML"""
    print("\n=== LECTURA DE ARCHIVOS YAML ===")
    
    try:
        with open('ejemplo.yaml', 'r', encoding='utf-8') as archivo:
            datos = yaml.safe_load(archivo)
            print(f"Datos YAML: {datos}")
    except FileNotFoundError:
        print("Nota: Crea un archivo 'ejemplo.yaml' para probar este código")

# ============= ARCHIVOS EXCEL =============

def ejemplo_archivo_excel():
    """Ejemplos de lectura de archivos Excel"""
    print("\n=== LECTURA DE ARCHIVOS EXCEL ===")
    
    # Método 1: Lectura básica
    print("\n1. Lectura básica de Excel:")
    try:
        df = pd.read_excel('ejemplo.xlsx')
        print("Primeras 5 filas del Excel:")
        print(df.head())
    except FileNotFoundError:
        print("Nota: Crea un archivo 'ejemplo.xlsx' para probar este código")

    # Método 2: Lectura de hojas específicas
    print("\n2. Lectura de hoja específica:")
    try:
        df = pd.read_excel('ejemplo.xlsx', sheet_name='Hoja1')
        print("Datos de Hoja1:")
        print(df)
    except FileNotFoundError:
        print("Archivo no encontrado")

if __name__ == "__main__":
    print("EJEMPLOS DE LECTURA DE DIFERENTES TIPOS DE ARCHIVOS")
    print("================================================")
    
    ejemplo_archivo_texto()
    ejemplo_archivo_csv()
    ejemplo_archivo_json()
    ejemplo_archivo_xml()
    ejemplo_archivo_yaml()
    ejemplo_archivo_excel() 