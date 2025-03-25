"""
GUÍA DE REFERENCIA: TESTING EN PYTHON
==================================

Esta guía cubre los conceptos fundamentales de testing en Python,
incluyendo unittest, pytest y buenas prácticas.
"""

import unittest
import pytest
from typing import List, Optional

# ============= CLASE A TESTEAR =============
# La clase a testear es una clase simple que tiene métodos para sumar, dividir y listar números pares.

class Calculadora:
    """Clase simple para demostrar testing"""
    
    def suma(self, a: float, b: float) -> float:
        return a + b
    
    def division(self, a: float, b: float) -> Optional[float]:
        try:
            return a / b
        except ZeroDivisionError:
            return None
    
    def lista_numeros_pares(self, hasta: int) -> List[int]:
        return [x for x in range(0, hasta + 1, 2)]

# ============= UNITTEST =============
# unittest es una biblioteca que permite crear tests para Python.

class TestCalculadora(unittest.TestCase):
    """Tests usando unittest"""
    
    def setUp(self):
        """Se ejecuta antes de cada test"""
        self.calc = Calculadora()
    
    def tearDown(self):
        """Se ejecuta después de cada test"""
        pass
    
    def test_suma(self):
        """Test del método suma"""
        self.assertEqual(self.calc.suma(3, 5), 8)
        self.assertEqual(self.calc.suma(-1, 1), 0)
        self.assertEqual(self.calc.suma(0, 0), 0)
    
    def test_division(self):
        """Test del método división"""
        self.assertEqual(self.calc.division(6, 2), 3)
        self.assertEqual(self.calc.division(5, 0), None)
    
    def test_lista_pares(self):
        """Test del método lista_numeros_pares"""
        self.assertEqual(self.calc.lista_numeros_pares(6), [0, 2, 4, 6])
        self.assertEqual(self.calc.lista_numeros_pares(0), [0])
        self.assertEqual(len(self.calc.lista_numeros_pares(10)), 6)

# ============= PYTEST =============
# pytest es una biblioteca que permite crear tests para Python.
# Para ejecutar estos tests: pytest nombre_archivo.py

def test_suma_pytest():
    """Test de suma usando pytest"""
    calc = Calculadora()
    assert calc.suma(3, 5) == 8
    assert calc.suma(-1, 1) == 0
    assert calc.suma(0, 0) == 0

def test_division_pytest():
    """Test de división usando pytest"""
    calc = Calculadora()
    assert calc.division(6, 2) == 3
    assert calc.division(5, 0) is None

@pytest.mark.parametrize("numero,esperado", [
    (6, [0, 2, 4, 6]),
    (0, [0]),
    (3, [0, 2])
])
def test_lista_pares_pytest(numero, esperado):
    """Test parametrizado usando pytest"""
    calc = Calculadora()
    assert calc.lista_numeros_pares(numero) == esperado

# ============= FIXTURES =============
# Los fixtures son una forma de proporcionar datos o configuraciones comunes a los tests.

@pytest.fixture
def calculadora():
    """Fixture que proporciona una instancia de Calculadora"""
    return Calculadora()

def test_usando_fixture(calculadora):
    """Test que usa un fixture"""
    assert calculadora.suma(2, 3) == 5

# ============= MOCK =============
# Los mocks son una forma de simular el comportamiento de un objeto.

from unittest.mock import Mock, patch

def test_con_mock():
    """Ejemplo de uso de mocks"""
    # Crear un mock
    mock_calc = Mock()
    
    # Configurar el comportamiento del mock
    mock_calc.suma.return_value = 10
    
    # Usar el mock
    resultado = mock_calc.suma(5, 5)
    assert resultado == 10
    mock_calc.suma.assert_called_once_with(5, 5)

# ============= BUENAS PRÁCTICAS =============

"""
1. Nombrado de tests:
   - Usar nombres descriptivos
   - Prefijo 'test_'
   - Describir el comportamiento esperado

2. Estructura:
   - Un assert por test (cuando sea posible)
   - Setup y teardown claros
   - Tests independientes

3. Cobertura:
   - Testear casos normales
   - Testear casos límite
   - Testear errores esperados

4. Organización:
   - Tests en directorio separado
   - Un archivo de test por módulo
   - Usar fixtures para código común

5. Ejecución:
   - Automatizar los tests
   - Ejecutar tests frecuentemente
   - Integrar con CI/CD
"""

# Ejemplo de test bien estructurado
class TestBuenasPracticas(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial"""
        self.calc = Calculadora()
        self.numeros_prueba = [1, 2, 3]
    
    def test_suma_numeros_positivos(self):
        """Test de suma con números positivos"""
        resultado = self.calc.suma(5, 3)
        self.assertEqual(resultado, 8)
    
    def test_suma_numeros_negativos(self):
        """Test de suma con números negativos"""
        resultado = self.calc.suma(-5, -3)
        self.assertEqual(resultado, -8)
    
    def test_division_por_cero_devuelve_none(self):
        """Test de división por cero"""
        resultado = self.calc.division(5, 0)
        self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main() 