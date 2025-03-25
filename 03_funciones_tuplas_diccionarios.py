"""
GUÍA DE REFERENCIA: FUNCIONES, TUPLAS Y DICCIONARIOS
================================================

Esta guía cubre en detalle el uso de funciones, tuplas y diccionarios
en Python con ejemplos prácticos.
"""

# ============= FUNCIONES BÁSICAS =============

def ejemplos_funciones_basicas():
    """Ejemplos de funciones básicas"""
    print("\n=== FUNCIONES BÁSICAS ===")
    
    # Función simple
    def saludar(nombre):
        return f"¡Hola, {nombre}!"
    
    # Función con múltiples parámetros
    def suma(a, b):
        return a + b
    
    # Función con parámetros por defecto
    def saludar_formal(nombre, titulo="Sr./Sra."):
        return f"Estimado/a {titulo} {nombre}"
    
    # Ejemplos de uso
    print("\n1. Funciones simples:")
    print(saludar("Ana"))
    print(suma(5, 3))
    print(saludar_formal("García"))
    print(saludar_formal("García", "Dr."))

# ============= FUNCIONES AVANZADAS =============

def ejemplos_funciones_avanzadas():
    """Ejemplos de funciones avanzadas"""
    print("\n=== FUNCIONES AVANZADAS ===")
    
    # Función con args y kwargs
    # *args: Permite pasar un número variable de argumentos posicionales.
    # **kwargs: Permite pasar un número variable de argumentos nombrados.   
    def info_persona(*args, **kwargs):
        print("\nArgs (tupla):", args)
        print("Kwargs (diccionario):", kwargs)
    
    # Función con anotaciones de tipo
    def dividir(a: float, b: float) -> float:
        return a / b
    
    # Función lambda
    # lambda: Es una función anónima que puede tener cualquier número de argumentos, pero solo una expresión.
    cuadrado = lambda x: x**2
    
    # Ejemplos de uso
    print("\n1. Args y Kwargs:")
    info_persona("Juan", 30, ciudad="Madrid", profesion="Ingeniero")
    
    print("\n2. Función con tipos:")
    print(f"División: {dividir(10, 2)}")
    print(f"Anotaciones: {dividir.__annotations__}")
    
    print("\n3. Función lambda:")
    print(f"Cuadrado de 5: {cuadrado(5)}")

# ============= TUPLAS =============

def ejemplos_tuplas():
    """Ejemplos de uso de tuplas"""
    print("\n=== TUPLAS ===")
    
    # Crear tuplas
    # Las tuplas son similares a las listas, pero son inmutables.
    tupla_simple = (1, 2, 3) 
    tupla_mixta = (1, "dos", 3.0, True)
    tupla_anidada = (1, (2, 3), 4)
    
    print("\n1. Tipos de tuplas:")
    print(f"Simple: {tupla_simple}")
    print(f"Mixta: {tupla_mixta}")
    print(f"Anidada: {tupla_anidada}")
    
    # Operaciones con tuplas
    print("\n2. Operaciones:")
    print(f"Longitud: {len(tupla_simple)}")
    print(f"Índice de 2: {tupla_simple.index(2)}") 
    print(f"Contar elementos: {tupla_simple.count(1)}")
    
    # Desempaquetado de tuplas
    # El desempaquetado de tuplas es el proceso de asignar los valores de una tupla a variables individuales.
    print("\n3. Desempaquetado:")
    x, y, z = tupla_simple
    print(f"Valores: x={x}, y={y}, z={z}")
    
    # Tuplas como retorno múltiple
    def coordenadas():
        return (10, 20)
    
    lat, lon = coordenadas()
    print(f"Coordenadas: ({lat}, {lon})")

# ============= DICCIONARIOS =============

def ejemplos_diccionarios():
    """Ejemplos de uso de diccionarios"""
    print("\n=== DICCIONARIOS ===")
    
    # Crear diccionarios
    persona = {
        "nombre": "Ana",
        "edad": 25,
        "ciudad": "Madrid"
    }
    
    # Diccionario anidado
    empleado = {
        "datos": {
            "nombre": "Juan",
            "edad": 30
        },
        "puesto": "Desarrollador",
        "habilidades": ["Python", "JavaScript"]
    }
    
    print("\n1. Acceso a datos:")
    print(f"Nombre: {persona['nombre']}")
    print(f"Puesto: {empleado['puesto']}")
    print(f"Edad empleado: {empleado['datos']['edad']}")
    
    # Métodos de diccionarios
    print("\n2. Métodos principales:")
    print(f"Claves: {persona.keys()}")
    print(f"Valores: {persona.values()}")
    print(f"Items: {persona.items()}")
    
    # Modificar diccionarios
    print("\n3. Modificaciones:")
    persona["telefono"] = "123456789"  # Agregar
    persona["edad"] = 26  # Modificar
    print(f"Diccionario actualizado: {persona}")
    
    # Métodos útiles
    print("\n4. Métodos útiles:")
    print(f"Get con valor por defecto: {persona.get('correo', 'No especificado')}")
    
    # Eliminar elementos
    del persona["telefono"]
    edad = persona.pop("edad")
    print(f"Después de eliminar: {persona}")
    print(f"Edad eliminada: {edad}")

# ============= COMBINANDO TODO =============

def ejemplo_combinado():
    """Ejemplo que combina funciones, tuplas y diccionarios"""
    print("\n=== EJEMPLO COMBINADO ===")
    
    def procesar_empleado(info):
        nombre, edad = info  # Desempaquetar tupla
        return {
            "nombre": nombre,
            "edad": edad,
            "adulto": edad >= 18
        }
    
    # Lista de tuplas con información
    empleados = [
        ("Ana", 25),
        ("Juan", 30),
        ("María", 22)
    ]
    
    # Procesar y mostrar resultados
    resultados = [procesar_empleado(emp) for emp in empleados]
    
    for empleado in resultados:
        print(f"\nEmpleado: {empleado['nombre']}")
        print(f"Edad: {empleado['edad']}")
        print(f"Es adulto: {empleado['adulto']}")

if __name__ == "__main__":
    print("EJEMPLOS DE FUNCIONES, TUPLAS Y DICCIONARIOS")
    print("=========================================")
    
    ejemplos_funciones_basicas()
    ejemplos_funciones_avanzadas()
    ejemplos_tuplas()
    ejemplos_diccionarios()
    ejemplo_combinado() 