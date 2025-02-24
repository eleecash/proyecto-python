# ============================================================================
# Fichero: test.py
# Autor: Elena Ruiz De La Blanca
# Descripción: Conjunto de pruebas unitarias para la aplicación de gestión de vuelos.
# ============================================================================

import unittest

# Importa las clases que vas a probar.
# Ajusta los nombres de módulos/clases según tu proyecto.
from Flight import Flight
from Aircraft import Aircraft, Airbus, Boeing
from Passenger import Passenger


class TestFlightCreation(unittest.TestCase):
    """Pruebas relacionadas con la creación de objetos Flight."""

    def test_flight_creation_valid(self):
        """Comprueba que se crea un vuelo válido con un número de vuelo y un Aircraft correctos."""
        # Preparación
        aircraft = Aircraft(registration="G-EUAH", model="Airbus A319", num_rows=22, num_seats_per_row=6)
        
        # Ejecución
        flight = Flight(number="BA117", aircraft=aircraft)

        # Verificación
        self.assertEqual(flight.get_number(), "BA117")
        self.assertEqual(flight.get_aircraft(), aircraft)
        self.assertIsNotNone(flight.get_seating())  # Aseguramos que seating se haya creado.

    def test_flight_creation_invalid_number(self):
        """Comprueba que se lanza ValueError al crear un vuelo con un número de vuelo inválido."""
        aircraft = Aircraft(registration="G-EUAH", model="Airbus A319", num_rows=22, num_seats_per_row=6)
        
        with self.assertRaises(ValueError):
            Flight(number="B117", aircraft=aircraft)  # No tiene 2 letras al inicio
        with self.assertRaises(ValueError):
            Flight(number="BA99999", aircraft=aircraft)  # Número >= 9999
        with self.assertRaises(ValueError):
            Flight(number="ba117", aircraft=aircraft)  # Letras no en mayúscula


class TestPassengerAllocation(unittest.TestCase):
    """Pruebas relacionadas con la asignación de pasajeros a asientos."""

    def setUp(self):
        """
        Se ejecuta antes de cada test. Crea un vuelo y algunos pasajeros
        para usarlos en las pruebas.
        """
        # Creamos un vuelo sencillo
        aircraft = Aircraft(registration="G-EUAH", model="Airbus A319", num_rows=5, num_seats_per_row=4)
        self.flight = Flight(number="BA101", aircraft=aircraft)

        # Pasajeros de ejemplo
        self.p1 = Passenger("Jack", "Shephard", "85994003S")
        self.p2 = Passenger("Kate", "Austen", "12589756P")

    def test_allocate_passenger_valid(self):
        """Comprueba la asignación correcta de un pasajero a un asiento libre."""
        self.flight.allocate_passenger("1A", self.p1.passenger_data())
        seating = self.flight.get_seating()
        self.assertEqual(seating[1]["A"], self.p1.passenger_data())

    def test_allocate_passenger_seat_occupied(self):
        """Comprueba que se lanza ValueError al asignar un pasajero a un asiento ya ocupado."""
        self.flight.allocate_passenger("1A", self.p1.passenger_data())
        with self.assertRaises(ValueError):
            # Intentamos asignar a '1A' otro pasajero
            self.flight.allocate_passenger("1A", self.p2.passenger_data())

    def test_allocate_passenger_invalid_seat(self):
        """Comprueba que se lanza ValueError al asignar a un asiento que no existe."""
        with self.assertRaises(ValueError):
            # En este vuelo, las filas llegan hasta la 5, así que '6A' no existe
            self.flight.allocate_passenger("6A", self.p1.passenger_data())
        with self.assertRaises(ValueError):
            # La letra 'E' no existe si solo hay 4 asientos por fila (A, B, C, D)
            self.flight.allocate_passenger("2E", self.p1.passenger_data())


class TestPassengerReallocation(unittest.TestCase):
    """Pruebas relacionadas con la reasignación de pasajeros."""

    def setUp(self):
        aircraft = Aircraft(registration="G-EUAH", model="Airbus A319", num_rows=3, num_seats_per_row=3)
        self.flight = Flight(number="BA102", aircraft=aircraft)

        self.p1 = Passenger("James", "Ford", "56278665F")
        self.flight.allocate_passenger("1A", self.p1.passenger_data())

    def test_reallocate_passenger_valid(self):
        """Comprueba que se reasigna correctamente un pasajero de un asiento a otro."""
        self.flight.reallocate_passenger("1A", "2B")
        seating = self.flight.get_seating()
        self.assertIsNone(seating[1]["A"])  # El asiento antiguo queda libre
        self.assertEqual(seating[2]["B"], self.p1.passenger_data())  # El asiento nuevo queda ocupado

    def test_reallocate_passenger_from_seat_empty(self):
        """Comprueba que se lanza ValueError si el asiento original está vacío."""
        with self.assertRaises(ValueError):
            self.flight.reallocate_passenger("1B", "2B")  # '1B' está vacío

    def test_reallocate_passenger_to_seat_occupied(self):
        """Comprueba que se lanza ValueError si el asiento de destino ya está ocupado."""
        # Ocupamos '2B' con otro pasajero
        p2 = Passenger("Hugo", "Reyes", "89765432T")
        self.flight.allocate_passenger("2B", p2.passenger_data())

        # Intentamos reasignar p1 de '1A' a '2B'
        with self.assertRaises(ValueError):
            self.flight.reallocate_passenger("1A", "2B")


class TestNumAvailableSeats(unittest.TestCase):
    """Pruebas para el método num_available_seats()."""

    def test_num_available_seats_initial(self):
        """Comprueba que inicialmente el número de asientos libres sea total."""
        aircraft = Aircraft(registration="G-EUAH", model="Airbus A319", num_rows=2, num_seats_per_row=2)
        flight = Flight(number="BA111", aircraft=aircraft)
        # 2 filas, 2 asientos por fila => total 4 asientos
        # Seating[0] = None, Seating[1] = { 'A': None, 'B': None }, Seating[2] = { 'A': None, 'B': None }
        self.assertEqual(flight.num_available_seats(), 4)

    def test_num_available_seats_after_allocation(self):
        """Comprueba que el número de asientos libres disminuye al asignar pasajeros."""
        aircraft = Aircraft(registration="G-EUAH", model="Airbus A319", num_rows=2, num_seats_per_row=2)
        flight = Flight(number="BA112", aircraft=aircraft)
        p1 = Passenger("Jack", "Shephard", "85994003S")
        p2 = Passenger("Kate", "Austen", "12589756P")

        flight.allocate_passenger("1A", p1.passenger_data())
        self.assertEqual(flight.num_available_seats(), 3)

        flight.allocate_passenger("1B", p2.passenger_data())
        self.assertEqual(flight.num_available_seats(), 2)


# Si ejecutas este fichero directamente (python test.py), se lanzarán todos los tests.
if __name__ == '__main__':
    unittest.main()
