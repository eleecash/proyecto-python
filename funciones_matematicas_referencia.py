"""
GUÍA DE REFERENCIA: FUNCIONES MATEMÁTICAS EN PYTHON
=================================================

Este archivo contiene ejemplos prácticos de las funciones matemáticas
más comunes en Python usando el módulo math.
"""

import math

# ============= FUNCIONES BÁSICAS =============

def ejemplos_funciones_basicas():
    """Ejemplos de operaciones matemáticas básicas"""
    print("\n=== FUNCIONES BÁSICAS ===")
    
    # Valor absoluto
    print("\n1. Valor absoluto (abs):")
    numero = -5
    print(f"   abs({numero}) = {abs(numero)}")  # Resultado: 5
    
    # Redondeo
    print("\n2. Funciones de redondeo:")
    decimal = 3.7
    print(f"   round({decimal}) = {round(decimal)}")      # Redondea al entero más cercano
    print(f"   math.floor({decimal}) = {math.floor(decimal)}")  # Redondea hacia abajo
    print(f"   math.ceil({decimal}) = {math.ceil(decimal)}")    # Redondea hacia arriba

    # Potencia
    print("\n3. Potencia:")
    base = 2
    exponente = 3
    print(f"   {base}^{exponente} usando pow() = {pow(base, exponente)}")
    print(f"   {base}^{exponente} usando ** = {base ** exponente}")

# ============= FUNCIONES TRIGONOMÉTRICAS =============

def ejemplos_trigonometria():
    """Ejemplos de funciones trigonométricas"""
    print("\n=== FUNCIONES TRIGONOMÉTRICAS ===")
    
    # Convertir grados a radianes
    grados = 45
    radianes = math.radians(grados)
    print(f"\n1. Conversión de {grados}° a radianes = {radianes}")
    
    # Seno, Coseno y Tangente
    print("\n2. Funciones trigonométricas básicas:")
    print(f"   sen({grados}°) = {math.sin(radianes)}")
    print(f"   cos({grados}°) = {math.cos(radianes)}")
    print(f"   tan({grados}°) = {math.tan(radianes)}")
    
    # Funciones inversas
    valor = 0.5
    print(f"\n3. Funciones trigonométricas inversas de {valor}:")
    print(f"   arcsen({valor}) = {math.degrees(math.asin(valor))}°")
    print(f"   arccos({valor}) = {math.degrees(math.acos(valor))}°")
    print(f"   arctan({valor}) = {math.degrees(math.atan(valor))}°")

# ============= LOGARITMOS Y EXPONENCIALES =============

def ejemplos_logaritmos():
    """Ejemplos de logaritmos y funciones exponenciales"""
    print("\n=== LOGARITMOS Y EXPONENCIALES ===")
    
    numero = 100
    print(f"\n1. Logaritmos de {numero}:")
    print(f"   Logaritmo natural (ln) = {math.log(numero)}")
    print(f"   Logaritmo base 10 = {math.log10(numero)}")
    print(f"   Logaritmo base 2 = {math.log2(numero)}")
    
    # Exponencial (e^x)
    x = 2
    print(f"\n2. Exponencial de {x}:")
    print(f"   e^{x} = {math.exp(x)}")

# ============= CONSTANTES MATEMÁTICAS =============

def mostrar_constantes():
    """Muestra las constantes matemáticas más importantes"""
    print("\n=== CONSTANTES MATEMÁTICAS ===")
    print(f"\n1. π (pi) = {math.pi}")
    print(f"2. e (número de Euler) = {math.e}")
    print(f"3. τ (tau, 2π) = {math.tau}")
    print(f"4. Infinito = {math.inf}")

# ============= FUNCIONES HIPERBÓLICAS =============

def ejemplos_hiperbolicas():
    """Ejemplos de funciones hiperbólicas"""
    print("\n=== FUNCIONES HIPERBÓLICAS ===")
    
    x = 1
    print(f"\nFunciones hiperbólicas de {x}:")
    print(f"1. senh({x}) = {math.sinh(x)}")
    print(f"2. cosh({x}) = {math.cosh(x)}")
    print(f"3. tanh({x}) = {math.tanh(x)}")

# Ejecutar todos los ejemplos
if __name__ == "__main__":
    print("EJEMPLOS DE FUNCIONES MATEMÁTICAS EN PYTHON")
    print("==========================================")
    
    ejemplos_funciones_basicas()
    ejemplos_trigonometria()
    ejemplos_logaritmos()
    mostrar_constantes()
    ejemplos_hiperbolicas() 