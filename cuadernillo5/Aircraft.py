# ============================================================================
# Fichero: Aircraft.py
# Autor: Elena Ruiz De La Blanca
# Descripción: Clase Aircraft y subclases Airbus y Boeing para gestionar aviones
# ============================================================================

"""
Módulo que define la clase base Aircraft y sus subclases Airbus y Boeing,
utilizadas para representar diferentes tipos de aviones.
"""

class Aircraft:
    """
    Representa una aeronave genérica con un número de registro, modelo,
    número de filas y número de asientos por fila.

    Atributos:
        __registration (str): Número de registro de la aeronave.
        __model (str): Modelo de la aeronave (ej. 'Airbus A319').
        __num_rows (int): Número de filas que contiene la aeronave.
        __num_seats_per_row (int): Número de asientos en cada fila.
    """

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        """
        Inicializa una aeronave con la información básica.

        Args:
            registration (str): Número de registro de la aeronave.
            model (str): Modelo de la aeronave.
            num_rows (int): Número de filas que contiene la aeronave.
            num_seats_per_row (int): Número de asientos en cada fila.

        Raises:
            ValueError: Si alguno de los parámetros no cumple las condiciones mínimas,
                        por ejemplo:
                        - registration vacío
                        - model vacío
                        - num_rows < 1
                        - num_seats_per_row < 1
        """
        # Validaciones de ejemplo:
        if not registration:
            raise ValueError("El número de registro (registration) no puede estar vacío.")
        if not model:
            raise ValueError("El modelo de la aeronave (model) no puede estar vacío.")
        if num_rows < 1:
            raise ValueError(f"El número de filas (num_rows={num_rows}) debe ser al menos 1.")
        if num_seats_per_row < 1:
            raise ValueError(f"El número de asientos por fila (num_seats_per_row={num_seats_per_row}) debe ser al menos 1.")

        self.__registration = registration
        self.__model = model
        self.__num_rows = num_rows
        self.__num_seats_per_row = num_seats_per_row

    def get_registration(self):
        """
        Devuelve el número de registro de la aeronave.

        Returns:
            str: El número de registro de la aeronave.
        """
        return self.__registration

    def get_model(self):
        """
        Devuelve el modelo de la aeronave.

        Returns:
            str: El modelo de la aeronave.
        """
        return self.__model

    def get_num_rows(self):
        """
        Devuelve el número de filas de la aeronave.

        Returns:
            int: El número de filas.
        """
        return self.__num_rows

    def get_num_seats_per_row(self):
        """
        Devuelve el número de asientos por fila.

        Returns:
            int: El número de asientos en cada fila.
        """
        return self.__num_seats_per_row

    def seating_plan(self):
        """
        Genera el plan de asientos para la aeronave.

        Returns:
            tuple:
                - rows (list): Lista de None (tamaño num_rows + 1), 
                  donde el índice 0 no se utiliza.
                - seats (str): Cadena con las letras de asiento 
                  (ej. 'ABCDEF' para 6 asientos por fila).
        """
        import string
        rows = [None] * (self.__num_rows + 1)
        seats = string.ascii_uppercase[: self.__num_seats_per_row]
        return rows, seats

    def num_seats(self):
        """
        Calcula el número total de asientos de la aeronave.

        Returns:
            int: El número total de asientos (num_rows * num_seats_per_row).
        """
        return self.__num_rows * self.__num_seats_per_row


class Airbus(Aircraft):
    """
    Subclase de Aircraft que representa un Airbus A319.
    Por defecto, asume 23 filas y 6 asientos por fila.

    Atributos adicionales:
        __variant (str): Variante concreta del modelo Airbus.
    """

    def __init__(self, registration, variant):
        """
        Inicializa un Airbus A319 con valores por defecto para filas y asientos.

        Args:
            registration (str): Número de registro de la aeronave.
            variant (str): Variante del Airbus (p.e. 'A319-100').

        Raises:
            ValueError: Si 'registration' está vacío o 'variant' está vacío.
        """
        # Validamos 'registration' antes de llamar a super().__init__:
        if not registration:
            raise ValueError("El número de registro (registration) no puede estar vacío (Airbus).")
        if not variant:
            raise ValueError("La variante (variant) no puede estar vacía para un Airbus.")

        # Llamamos a la superclase con los valores típicos de un Airbus A319
        super().__init__(registration, "Airbus A319", 23, 6)
        self.__variant = variant

    def get_variant(self):
        """
        Devuelve la variante específica del Airbus.

        Returns:
            str: La variante del Airbus (p.e. 'A319-100').
        """
        return self.__variant


class Boeing(Aircraft):
    """
    Subclase de Aircraft que representa un Boeing 777.
    Por defecto, asume 56 filas y 9 asientos por fila.

    Atributos adicionales:
        __airline (str): Aerolínea que opera este Boeing.
    """

    def __init__(self, registration, airline):
        """
        Inicializa un Boeing 777 con valores por defecto para filas y asientos.

        Args:
            registration (str): Número de registro de la aeronave.
            airline (str): Aerolínea que opera el Boeing (p.e. 'Emirates').

        Raises:
            ValueError: Si 'registration' está vacío o 'airline' está vacío.
        """
        # Validaciones de ejemplo:
        if not registration:
            raise ValueError("El número de registro (registration) no puede estar vacío (Boeing).")
        if not airline:
            raise ValueError("La aerolínea (airline) no puede estar vacía para un Boeing.")

        # Llamamos a la superclase con los valores típicos de un Boeing 777
        super().__init__(registration, "Boeing 777", 56, 9)
        self.__airline = airline

    def get_airline(self):
        """
        Devuelve la aerolínea que opera este Boeing.

        Returns:
            str: La aerolínea que opera el avión.
        """
        return self.__airline
