from pprint import pprint

class Flight:
    def __init__(self, number, aircraft):
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
        return self.__number

    def get_aircraft(self):
        return self.__aircraft

    def get_seating(self):
        """
        Retorna la estructura de asientos (lista de diccionarios)
        """
        return self.__seating

    def allocate_passenger(self, seat, passenger):
        """
        Allocate a seat to a passenger
        Args:
          seat (str): A seat designator such as '12C' or '21F'
          passenger (tuple): The passenger data such as ('Jack', 'Shephard', '85994003S')
        """
        row, letter = self.__parse_seat(seat)
        self.__seating[row][letter] = passenger

    def reallocate_passenger(self, from_seat, to_seat):
        """
        Reallocate a passenger to a different seat
        Args:
          from_seat (str): The existing seat designator for the passenger
          to_seat (str): The new seat designator
        """
        from_row, from_letter = self.__parse_seat(from_seat)
        passenger = self.__seating[from_row][from_letter]

        # Lo quitamos del asiento antiguo
        self.__seating[from_row][from_letter] = None

        # Lo colocamos en el nuevo asiento
        to_row, to_letter = self.__parse_seat(to_seat)
        self.__seating[to_row][to_letter] = passenger

    def num_available_seats(self):
        """
        Obtains the amount of unoccupied seats
        Returns:
          int: The number of unoccupied seats
        """
        count = 0
        # Empezamos en la fila 1 porque la 0 es None
        for row in self.__seating[1:]:
            for seat_letter, passenger in row.items():
                if passenger is None:
                    count += 1
        return count

    def print_seating(self):
        """
        Prints in console the seating plan
        Example of one row:
          {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None}
        """
        pprint(self.__seating)

    def print_boarding_cards(self):
        """
        Prints in console the boarding card for each passenger
        Example of one boarding card:
        ----------------------------------------------------------
        |     Jack Sheppard 85994003S 15E BA758 Airbus A319      |
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
        Divide a seat designator in row and letter
        Args:
          seat (str): The seat designator to be divided such as '12C'
        Returns:
          row (int): The row of the seat such as 12
          letter (str): The letter of the seat such as 'C'
        """
        row = int(seat[:-1])     # todo menos el último caracter
        letter = seat[-1]        # el último caracter
        return row, letter

    def __passenger_seats(self):
        """
        A generator function to iterate the occupied seating locations
        Returns:
          generator: Tuple (passenger_data, seat) para cada asiento ocupado
        """
        # self.__seating[0] es None, así que empezamos en 1
        for row_num in range(1, len(self.__seating)):
            row = self.__seating[row_num]
            for seat_letter, passenger in row.items():
                if passenger is not None:
                    # seat es la combinación de la fila y la letra
                    seat = f"{row_num}{seat_letter}"
                    yield (passenger, seat)
