"""
GUÍA DE REFERENCIA: GESTIÓN DE EXCEPCIONES EN PYTHON
================================================

Esta guía cubre los conceptos fundamentales del manejo de
excepciones en Python con ejemplos prácticos.
"""

# ============= EXCEPCIONES BÁSICAS =============

def ejemplos_basicos():
    """Ejemplos básicos de manejo de excepciones"""
    print("\n=== EXCEPCIONES BÁSICAS ===")
    
    # Try-except simple
    # El bloque try se ejecuta si no se produce ninguna excepción.
    print("\n1. Try-except básico:")
    try:
        numero = int("abc")
    except ValueError:
        print("Error: No se puede convertir 'abc' a número")
    
    # Try-except con múltiples excepciones
    # El bloque except se ejecuta si se produce una excepción del tipo especificado.
    print("\n2. Múltiples excepciones:")
    try:
        lista = [1, 2, 3]
        print(lista[10] / 0)
    except IndexError:
        print("Error: Índice fuera de rango")
    except ZeroDivisionError:
        print("Error: División por cero")
    
    # Try-except-else-finally
    # El bloque else se ejecuta si no se produce ninguna excepción.
    # El bloque finally se ejecuta siempre, ya sea que se produzca una excepción o no.
    print("\n3. Try-except-else-finally:")
    try:
        numero = int("123")
    except ValueError:
        print("Error al convertir")
    else:
        print(f"Conversión exitosa: {numero}")
    finally:
        print("Este bloque siempre se ejecuta")

# ============= EXCEPCIONES PERSONALIZADAS =============

class SaldoInsuficienteError(Exception):
    """Excepción personalizada para saldo insuficiente"""
    def __init__(self, saldo_actual, cantidad):
        self.saldo_actual = saldo_actual
        self.cantidad = cantidad
        self.mensaje = f"Saldo insuficiente. Tiene {saldo_actual}€, intenta retirar {cantidad}€"
        super().__init__(self.mensaje)

class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
    
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise SaldoInsuficienteError(self.saldo, cantidad)
        self.saldo -= cantidad
        return f"Retiro exitoso. Nuevo saldo: {self.saldo}€"

# ============= MANEJO AVANZADO =============

def ejemplos_avanzados():
    """Ejemplos avanzados de manejo de excepciones"""
    print("\n=== MANEJO AVANZADO DE EXCEPCIONES ===")
    
    # Capturar información de la excepción
    print("\n1. Información de la excepción:")
    try:
        x = 1 / 0
    except ZeroDivisionError as e:
        print(f"Tipo de error: {type(e).__name__}")
        print(f"Mensaje: {str(e)}")
    
    # Excepciones personalizadas
    print("\n2. Excepciones personalizadas:")
    cuenta = CuentaBancaria(100)
    try:
        print(cuenta.retirar(150))
    except SaldoInsuficienteError as e:
        print(f"Error: {e}")
    
    # Re-lanzar excepciones
    print("\n3. Re-lanzar excepciones:")
    try:
        try:
            raise ValueError("Error original")
        except ValueError:
            print("Capturado, pero lo volvemos a lanzar")
            raise
    except ValueError as e:
        print(f"Capturado nuevamente: {e}")

# ============= CONTEXTOS Y WITH =============
# El contexto es un bloque de código que se ejecuta antes y después de la ejecución de un bloque de código.
# with es una palabra clave que se utiliza para manejar contextos.

def ejemplos_with():
    """Ejemplos de manejo de contextos con with"""
    print("\n=== CONTEXTOS Y WITH ===")
    
    # Manejo de archivos con with
    print("\n1. Manejo de archivos:")
    try:
        with open("ejemplo.txt", "w") as f:
            f.write("Hola Mundo")
        
        with open("ejemplo.txt", "r") as f:
            contenido = f.read()
            print(f"Contenido: {contenido}")
    except FileNotFoundError:
        print("Error: Archivo no encontrado")
    
    # Múltiples contextos
    print("\n2. Múltiples contextos:")
    try:
        with open("entrada.txt", "r") as entrada, \
             open("salida.txt", "w") as salida:
            contenido = entrada.read()
            salida.write(contenido.upper())
    except FileNotFoundError:
        print("Error: Alguno de los archivos no existe")

# ============= MEJORES PRÁCTICAS =============

def ejemplo_mejores_practicas():
    """Ejemplos de mejores prácticas en el manejo de excepciones"""
    print("\n=== MEJORES PRÁCTICAS ===")
    
    # 1. Ser específico con las excepciones
    print("\n1. Ser específico:")
    try:
        # Mal (muy general):
        # except Exception:
        #     pass
        
        # Bien (específico):
        numero = int("abc")
    except ValueError:
        print("Error específico de conversión")
    
    # 2. No silenciar excepciones
    print("\n2. No silenciar excepciones:")
    try:
        with open("no_existe.txt") as f:
            contenido = f.read()
    except FileNotFoundError as e:
        # Bien: Registrar o manejar el error
        print(f"Error controlado: {e}")
    
    # 3. Limpiar recursos
    print("\n3. Limpiar recursos:")
    archivo = None
    try:
        archivo = open("ejemplo.txt")
        # Hacer algo con el archivo
    except FileNotFoundError:
        print("El archivo no existe")
    finally:
        if archivo:
            archivo.close()
            print("Archivo cerrado correctamente")

if __name__ == "__main__":
    print("EJEMPLOS DE GESTIÓN DE EXCEPCIONES")
    print("=================================")
    
    ejemplos_basicos()
    ejemplos_avanzados()
    ejemplos_with()
    ejemplo_mejores_practicas() 