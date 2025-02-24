# ============================================================================
# Fichero: Flight.py
# Autor: Elena Ruiz De La Blanca
# Descripción: Clase Flight para gestionar vuelos y asientos de pasajeros en un avión 
# ============================================================================

"""
Módulo Flight para gestionar vuelos y asientos de pasajeros en un avión.

Clases:
    Flight
"""

from pprint import pprint

class Flight:
    """
    Representa un vuelo con un número y una aeronave asociada, además de
    gestionar la asignación de pasajeros a los asientos.

    Atributos:
        __number (str): Número identificativo del vuelo (por ejemplo, 'BA117').
        __aircraft (Aircraft): La aeronave asociada a este vuelo.
        __seating (list): Estructura de asientos; índice 0 es None, y a partir
                          del 1, cada posición es un diccionario con claves
                          (letras de asiento) y valores (None o datos de pasajero).
    """

    def __init__(self, number, aircraft):
        """
        Inicializa la clase Flight con un número de vuelo y una aeronave.

        Args:
            number (str): Número del vuelo (ej. 'BA117').
            aircraft (Aircraft): Objeto que representa la aeronave.

        Raises:
            ValueError: Si el número de vuelo no cumple los requisitos:
                        - Primeros 2 caracteres letras y en mayúsculas.
                        - El resto dígitos, formando un número < 9999.
        """
        # === Validaciones para el número de vuelo ===
        # 1) Verificamos longitud mínima: al menos 3 caracteres (2 letras + dígitos).
        if len(number) < 3:
            raise ValueError(f"Número de vuelo '{number}' demasiado corto.")
        # 2) Los dos primeros caracteres deben ser letras.
        if not number[:2].isalpha():
            raise ValueError(f"Número de vuelo '{number}' debe comenzar con 2 letras.")
        # 3) Las dos letras deben estar en mayúsculas.
        if not number[:2].isupper():
            raise ValueError(f"Número de vuelo '{number}' debe tener las 2 letras en mayúscula.")
        # 4) El resto deben ser dígitos y formar un número < 9999.
        if not number[2:].isdigit():
            raise ValueError(f"Número de vuelo '{number}' debe terminar con dígitos.")
        if int(number[2:]) >= 9999:
            raise ValueError(f"Número de vuelo '{number}' debe tener un número < 9999 tras las letras.")

        self.__number = number
        self.__aircraft = aircraft

        # Construimos la estructura seating usando el seating_plan del aircraft
        rows, seat_letters = self.__aircraft.seating_plan()
        # La posición 0 será None y no se utiliza; a partir de la 1 en adelante, diccionarios
        # con clave = letra de asiento y valor = None (sin pasajero).
        self.__seating = [None]  # índice 0
        for _ in rows[1:]:  # ignoramos el primer elemento (fila 0)
            row_dict = {letter: None for letter in seat_letters}
            self.__seating.append(row_dict)

    def get_number(self):
        """
        Devuelve el número del vuelo.

        Returns:
            str: Número de vuelo.
        """
        return self.__number

    def get_aircraft(self):
        """
        Devuelve la aeronave asociada a este vuelo.

        Returns:
            Aircraft: La aeronave del vuelo.
        """
        return self.__aircraft

    def get_seating(self):
        """
        Retorna la estructura de asientos (lista de diccionarios).

        Returns:
            list: Lista con la ocupación de asientos del vuelo.
        """
        return self.__seating

    def allocate_passenger(self, seat, passenger):
        """
        Asigna un pasajero a un asiento específico.

        Args:
            seat (str): Identificador del asiento, como '12C' o '21F'.
            passenger (tuple): Datos del pasajero (p.e. ('Jack', 'Shephard', '85994003S')).

        Raises:
            ValueError: Si el asiento ya está ocupado.
            ValueError: Si el asiento no cumple el formato o no es válido (se controla en __parse_seat).
        """
        row, letter = self.__parse_seat(seat)

        # === Validar que el asiento esté libre ===
        if self.__seating[row][letter] is not None:
            raise ValueError(f"El asiento {seat} ya está ocupado.")

        self.__seating[row][letter] = passenger

    def reallocate_passenger(self, from_seat, to_seat):
        """
        Reasigna un pasajero de un asiento a otro distinto.

        Args:
            from_seat (str): Asiento de origen (p.e. '12C').
            to_seat (str): Asiento de destino (p.e. '21F').

        Raises:
            ValueError: Si el asiento original está vacío.
            ValueError: Si el asiento de destino está ocupado.
            ValueError: Si alguno de los asientos no cumple el formato (se controla en __parse_seat).
        """
        from_row, from_letter = self.__parse_seat(from_seat)
        passenger = self.__seating[from_row][from_letter]

        # === Validar que el asiento original esté ocupado ===
        if passenger is None:
            raise ValueError(f"El asiento {from_seat} está vacío; no se puede reasignar.")

        # === Validar que el asiento de destino esté libre ===
        to_row, to_letter = self.__parse_seat(to_seat)
        if self.__seating[to_row][to_letter] is not None:
            raise ValueError(f"El asiento {to_seat} ya está ocupado.")

        # Movemos al pasajero
        self.__seating[from_row][from_letter] = None
        self.__seating[to_row][to_letter] = passenger

    def num_available_seats(self):
        """
        Obtiene la cantidad de asientos desocupados en el vuelo.

        Returns:
            int: Número de asientos libres.
        """
        count = 0
        # Empezamos en la fila 1 porque la 0 es None
        for row in self.__seating[1:]:
            for seat_letter, occupant in row.items():
                if occupant is None:
                    count += 1
        return count

    def print_seating(self):
        """
        Muestra por consola el plan de asientos del vuelo.

        Ejemplo de una fila:
            {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None}
        """
        pprint(self.__seating)

    def print_boarding_cards(self):
        """
        Imprime en consola la tarjeta de embarque de cada pasajero.

        Ejemplo de salida de una tarjeta:
            ----------------------------------------------------------
            |  Jack Sheppard 85994003S 15E BA758 Airbus A319          |
            ----------------------------------------------------------
        """
        for passenger, seat in self.__passenger_seats():
            name, surname, id_card = passenger
            row, letter = self.__parse_seat(seat)

            # Datos del vuelo y modelo de avión
            flight_number = self.get_number()
            aircraft_model = self.__aircraft.get_model()

            print("----------------------------------------------------------")
            print(f"|  {name} {surname} {id_card} {row}{letter} {flight_number} {aircraft_model}  |")
            print("----------------------------------------------------------")

    def __parse_seat(self, seat):
        """
        Separa un identificador de asiento en la fila (numérico) y la letra.

        Args:
            seat (str): El identificador del asiento (p.e. '12C').

        Returns:
            tuple: (row (int), letter (str))

        Raises:
            ValueError: Si el asiento no es válido:
                - El último carácter debe ser una letra válida (según la aeronave).
                - El resto deben ser dígitos.
                - El número de fila debe estar entre 1 y num_rows de la aeronave.
        """
        # Ejemplo: seat = '12C'
        # Ultimo char -> 'C' (debe estar en seat_letters)
        # El resto -> '12' (deben ser dígitos y 1 <= 12 <= num_rows)
        seat_letters = self.__aircraft.seating_plan()[1]

        if len(seat) < 2:
            raise ValueError(f"Asiento '{seat}' es demasiado corto.")

        letter = seat[-1]        # el último carácter
        if letter not in seat_letters:
            raise ValueError(f"La letra de asiento '{letter}' no es válida para este avión.")

        row_str = seat[:-1]      # todo menos el último carácter
        if not row_str.isdigit():
            raise ValueError(f"La fila de asiento '{row_str}' no es un número válido.")

        row = int(row_str)
        num_rows = self.__aircraft.get_num_rows()
        if row < 1 or row > num_rows:
            raise ValueError(f"La fila {row} no existe en este avión (máximo {num_rows}).")

        return row, letter

    def __passenger_seats(self):
        """
        Generador que recorre las ubicaciones de asientos ocupados.

        Yields:
            tuple: (passenger_data, seat) para cada asiento ocupado.
        """
        # self.__seating[0] es None, así que empezamos en 1
        for row_num in range(1, len(self.__seating)):
            row = self.__seating[row_num]
            for seat_letter, passenger in row.items():
                if passenger is not None:
                    seat = f"{row_num}{seat_letter}"
                    yield (passenger, seat)
