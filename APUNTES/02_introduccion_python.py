"""
GUÍA DE REFERENCIA: INTRODUCCIÓN A PYTHON
=======================================

Esta guía cubre los conceptos básicos de Python con ejemplos prácticos.
"""

# ============= TIPOS DE DATOS BÁSICOS =============

def tipos_basicos():
    """Ejemplos de tipos de datos básicos en Python"""
    print("\n=== TIPOS DE DATOS BÁSICOS ===")
    
    # Números
    entero = 42
    decimal = 3.14
    complejo = 1 + 2j
    
    print(f"Entero: {entero}, tipo: {type(entero)}")
    print(f"Decimal: {decimal}, tipo: {type(decimal)}")
    print(f"Complejo: {complejo}, tipo: {type(complejo)}")
    
    # Texto
    texto = "Hola Mundo"
    print(f"\nTexto: {texto}, tipo: {type(texto)}")
    print(f"Longitud: {len(texto)}")
    print(f"Mayúsculas: {texto.upper()}")
    print(f"Minúsculas: {texto.lower()}")
    
    # Booleanos
    verdadero = True
    falso = False
    print(f"\nBooleanos: {verdadero}, {falso}")

# ============= ESTRUCTURAS DE DATOS =============

def estructuras_datos():
    """Ejemplos de estructuras de datos básicas"""
    print("\n=== ESTRUCTURAS DE DATOS ===")
    
    # Listas (mutables)
    lista = [1, 2, 3, "cuatro", 5.0]
    print(f"\nLista: {lista}")
    lista.append(6)
    print(f"Lista después de append: {lista}")
    print(f"Elemento en índice 2: {lista[2]}")
    
    # Tuplas (inmutables)
    tupla = (1, 2, 3, "cuatro")
    print(f"\nTupla: {tupla}")
    print(f"Elemento en índice 1: {tupla[1]}")
    
    # Conjuntos (sets)
    conjunto = {1, 2, 3, 3, 4}  # Note que los duplicados se eliminan
    print(f"\nConjunto: {conjunto}")
    conjunto.add(5)
    print(f"Conjunto después de add: {conjunto}")

# ============= CONTROL DE FLUJO =============

def control_flujo():
    """Ejemplos de estructuras de control de flujo"""
    print("\n=== CONTROL DE FLUJO ===")
    
    # if-elif-else
    print("\nEjemplo de if-elif-else:")
    numero = 15
    if numero < 10:
        print("Número menor que 10")
    elif numero < 20:
        print("Número entre 10 y 20")
    else:
        print("Número mayor o igual a 20")
    
    # for loop
    print("\nEjemplo de for loop:")
    for i in range(3):
        print(f"Iteración {i}")
    
    # while loop
    print("\nEjemplo de while loop:")
    contador = 0
    while contador < 3:
        print(f"Contador: {contador}")
        contador += 1

# ============= OPERADORES =============

def operadores():
    """Ejemplos de operadores en Python"""
    print("\n=== OPERADORES ===")
    
    # Aritméticos
    print("\nOperadores aritméticos:")
    print(f"Suma: 5 + 3 = {5 + 3}")
    print(f"Resta: 5 - 3 = {5 - 3}")
    print(f"Multiplicación: 5 * 3 = {5 * 3}")
    print(f"División: 5 / 3 = {5 / 3}")
    print(f"División entera: 5 // 3 = {5 // 3}")
    print(f"Módulo: 5 % 3 = {5 % 3}")
    print(f"Potencia: 5 ** 3 = {5 ** 3}")
    
    # Comparación
    print("\nOperadores de comparación:")
    print(f"Igual: 5 == 3 : {5 == 3}")
    print(f"Diferente: 5 != 3 : {5 != 3}")
    print(f"Mayor que: 5 > 3 : {5 > 3}")
    print(f"Menor o igual: 5 <= 3 : {5 <= 3}")
    
    # Lógicos
    print("\nOperadores lógicos:")
    print(f"AND: True and False : {True and False}")
    print(f"OR: True or False : {True or False}")
    print(f"NOT: not True : {not True}")

# ============= COMPRENSIÓN DE LISTAS =============

def comprension_listas():
    """Ejemplos de comprensión de listas"""
    print("\n=== COMPRENSIÓN DE LISTAS ===")
    
    # Comprensión de lista básica
    numeros = [1, 2, 3, 4, 5]
    cuadrados = [x**2 for x in numeros]
    print(f"\nCuadrados: {cuadrados}")
    
    # Comprensión con condición
    pares = [x for x in numeros if x % 2 == 0]
    print(f"Números pares: {pares}")
    
    # Comprensión de diccionario
    cuadrados_dict = {x: x**2 for x in numeros}
    print(f"Diccionario de cuadrados: {cuadrados_dict}")

if __name__ == "__main__":
    print("EJEMPLOS DE CONCEPTOS BÁSICOS DE PYTHON")
    print("=====================================")
    
    tipos_basicos()
    estructuras_datos()
    control_flujo()
    operadores()
    comprension_listas() 