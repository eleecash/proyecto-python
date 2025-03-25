"""
GUÍA DE REFERENCIA: CLASES Y OBJETOS EN PYTHON
===========================================

Esta guía cubre los conceptos fundamentales de la programación
orientada a objetos en Python con ejemplos prácticos.
"""

# ============= CLASE BÁSICA =============

class Persona:
    """Ejemplo de una clase básica"""
    
    # Variable de clase (compartida por todas las instancias)
    especie = "Homo sapiens"
    
    def __init__(self, nombre, edad):
        """Constructor de la clase"""
        # Atributos de instancia
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        """Método de instancia"""
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años"
    
    @classmethod
    def get_especie(cls):
        """Método de clase"""
        return f"La especie es {cls.especie}"
    
    @staticmethod
    def es_adulto(edad):
        """Método estático"""
        return edad >= 18

# ============= HERENCIA =============

class Empleado(Persona):
    """Ejemplo de herencia"""
    
    def __init__(self, nombre, edad, salario):
        """Constructor de la clase hija"""
        # Llamar al constructor de la clase padre
        super().__init__(nombre, edad)
        self.salario = salario
    
    def presentarse(self):
        """Sobrescritura de método"""
        presentacion = super().presentarse()
        return f"{presentacion} y gano {self.salario}€"

# ============= PROPIEDADES =============

class CuentaBancaria:
    """Ejemplo de uso de propiedades"""
    
    def __init__(self, saldo_inicial=0):
        self._saldo = saldo_inicial  # Atributo protegido
    
    @property
    def saldo(self):
        """Getter para el saldo"""
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        """Setter para el saldo"""
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = valor

# ============= CLASES ABSTRACTAS =============

from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    """Ejemplo de clase abstracta"""
    
    @abstractmethod
    def area(self):
        """Método abstracto que debe ser implementado por las clases hijas"""
        pass
    
    @abstractmethod
    def perimetro(self):
        """Otro método abstracto"""
        pass

class Rectangulo(FiguraGeometrica):
    """Implementación de clase abstracta"""
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)

# ============= COMPOSICIÓN =============

class Motor:
    """Clase para demostrar composición"""
    
    def __init__(self, tipo):
        self.tipo = tipo
    
    def arrancar(self):
        return f"Motor {self.tipo} arrancado"

class Coche:
    """Ejemplo de composición"""
    
    def __init__(self, marca, modelo, tipo_motor):
        self.marca = marca
        self.modelo = modelo
        # Composición
        self.motor = Motor(tipo_motor)
    
    def arrancar(self):
        return f"{self.marca} {self.modelo}: {self.motor.arrancar()}"

# ============= EJEMPLOS DE USO =============

def ejemplos_clases():
    """Ejemplos de uso de las clases"""
    print("\n=== EJEMPLOS DE CLASES Y OBJETOS ===")
    
    # Clase básica
    print("\n1. Clase básica:")
    persona = Persona("Ana", 25)
    print(persona.presentarse())
    print(Persona.get_especie())
    print(f"¿Es adulto? {Persona.es_adulto(25)}")
    
    # Herencia
    print("\n2. Herencia:")
    empleado = Empleado("Juan", 30, 25000)
    print(empleado.presentarse())
    
    # Propiedades
    print("\n3. Propiedades:")
    cuenta = CuentaBancaria(1000)
    print(f"Saldo inicial: {cuenta.saldo}€")
    cuenta.saldo = 2000
    print(f"Nuevo saldo: {cuenta.saldo}€")
    
    # Clases abstractas
    print("\n4. Clases abstractas:")
    rectangulo = Rectangulo(5, 3)
    print(f"Área del rectángulo: {rectangulo.area()}")
    print(f"Perímetro del rectángulo: {rectangulo.perimetro()}")
    
    # Composición
    print("\n5. Composición:")
    coche = Coche("Toyota", "Corolla", "Gasolina")
    print(coche.arrancar())

if __name__ == "__main__":
    print("EJEMPLOS DE PROGRAMACIÓN ORIENTADA A OBJETOS")
    print("=========================================")
    
    ejemplos_clases() 