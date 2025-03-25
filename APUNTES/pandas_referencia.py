"""
GUÍA DE REFERENCIA: PANDAS EN PYTHON
==================================

Esta guía contiene ejemplos prácticos de las operaciones
más comunes con Pandas, la biblioteca de análisis de datos.
"""

import pandas as pd
import numpy as np

# ============= CREAR DATAFRAMES =============
# definicion de dataframe 
# Un DataFrame es una estructura de datos bidimensional, similar a una tabla en una base de datos o una hoja de cálculo.
# Tiene filas y columnas, donde cada columna puede contener diferentes tipos de datos (numéricos, cadenas, booleanos, etc.).

def ejemplos_crear_dataframes():
    """Ejemplos de creación de DataFrames"""
    print("\n=== CREAR DATAFRAMES ===")
    
    # Método 1: Desde un diccionario
    print("\n1. Crear DataFrame desde diccionario:")
    datos_dict = {
        'nombre': ['Ana', 'Juan', 'María'],
        'edad': [25, 30, 35],
        'ciudad': ['Madrid', 'Barcelona', 'Sevilla']
    }
    df1 = pd.DataFrame(datos_dict)
    print("\nDataFrame desde diccionario:")
    print(df1)

    # Método 2: Desde una lista de listas
    print("\n2. Crear DataFrame desde lista de listas:")
    datos_lista = [
        ['Ana', 25, 'Madrid'],
        ['Juan', 30, 'Barcelona'],
        ['María', 35, 'Sevilla']
    ]
    df2 = pd.DataFrame(datos_lista, columns=['nombre', 'edad', 'ciudad'])
    print("\nDataFrame desde lista:")
    print(df2)

# ============= OPERACIONES BÁSICAS =============

def ejemplos_operaciones_basicas():
    """Ejemplos de operaciones básicas con DataFrames"""
    print("\n=== OPERACIONES BÁSICAS ===")
    
    # Crear DataFrame de ejemplo
    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': ['a', 'b', 'c', 'd', 'e']
    })
    
    # Ver información básica
    print("\n1. Información básica del DataFrame:")
    print("\nPrimeras filas (head):")
    print(df.head())
    print("\nÚltimas filas (tail):")
    print(df.tail(2))
    print("\nInformación del DataFrame:")
    print(df.info())
    print("\nEstadísticas básicas:")
    print(df.describe())

    # Selección de datos
    print("\n2. Selección de datos:")
    print("\nSeleccionar columna:")
    print(df['A'])
    print("\nSeleccionar múltiples columnas:")
    print(df[['A', 'B']])
    print("\nSeleccionar por índice:")
    print(df.iloc[0])  # Primera fila
    print("\nSeleccionar por condición:")
    print(df[df['A'] > 2])

# ============= MANIPULACIÓN DE DATOS =============

def ejemplos_manipulacion():
    """Ejemplos de manipulación de datos"""
    print("\n=== MANIPULACIÓN DE DATOS ===")
    
    # Crear DataFrame de ejemplo
    df = pd.DataFrame({
        'nombre': ['Ana', 'Juan', 'María', 'Pedro'],
        'edad': [25, 30, 35, 40],
        'salario': [30000, 45000, 50000, 35000]
    })
    
    # Agregar columna
    print("\n1. Agregar columna:")
    df['bonus'] = df['salario'] * 0.1
    print(df)
    
    # Modificar valores
    print("\n2. Modificar valores:")
    df.loc[df['salario'] > 40000, 'bonus'] *= 1.5
    print(df)
    
    # Eliminar columna
    print("\n3. Eliminar columna:")
    df_temp = df.drop('bonus', axis=1)
    print(df_temp)

# ============= AGRUPACIÓN Y AGREGACIÓN =============

def ejemplos_agrupacion():
    """Ejemplos de agrupación y agregación de datos"""
    print("\n=== AGRUPACIÓN Y AGREGACIÓN ===")
    
    # Crear DataFrame de ejemplo
    df = pd.DataFrame({
        'departamento': ['IT', 'IT', 'Ventas', 'Ventas', 'IT'],
        'empleado': ['Ana', 'Juan', 'María', 'Pedro', 'Luis'],
        'salario': [30000, 45000, 50000, 35000, 42000]
    })
    
    # Agrupar por departamento
    print("\n1. Agrupar por departamento:")
    grupo = df.groupby('departamento')['salario'].agg(['mean', 'sum', 'count'])
    print(grupo)
    
    # Pivot table
    print("\n2. Tabla pivote:")
    pivot = pd.pivot_table(df, 
                         values='salario',
                         index='departamento',
                         aggfunc=['mean', 'sum', 'count'])
    print(pivot)

# ============= MERGE Y JOIN =============

def ejemplos_merge():
    """Ejemplos de combinación de DataFrames"""
    print("\n=== MERGE Y JOIN ===")
    
    # Crear DataFrames de ejemplo
    empleados = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'nombre': ['Ana', 'Juan', 'María', 'Pedro'],
        'dept_id': [1, 2, 1, 3]
    })
    
    departamentos = pd.DataFrame({
        'dept_id': [1, 2, 3],
        'departamento': ['IT', 'Ventas', 'RRHH']
    })
    
    # Merge básico
    print("\n1. Merge básico:")
    df_merge = pd.merge(empleados, departamentos, on='dept_id')
    print(df_merge)
    
    # Left join
    print("\n2. Left join:")
    df_left = pd.merge(empleados, departamentos, on='dept_id', how='left')
    print(df_left)

if __name__ == "__main__":
    print("EJEMPLOS DE USO DE PANDAS")
    print("========================")
    
    ejemplos_crear_dataframes()
    ejemplos_operaciones_basicas()
    ejemplos_manipulacion()
    ejemplos_agrupacion()
    ejemplos_merge() 