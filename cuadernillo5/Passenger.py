# ============================================================================
# Fichero: Passenger.py
# Autor: Elena Ruiz De La Blanca
# Descripción: Clase Passenger para almacenar la información de cada pasajero.
# ============================================================================

"""
Módulo que define la clase Passenger, utilizada para representar la información
básica de un pasajero: nombre, apellido y documento de identidad.
"""

class Passenger:
    """
    Representa a un pasajero con nombre, apellido e ID.

    Atributos:
        _name (str): El nombre del pasajero.
        _surname (str): El apellido del pasajero.
        _id_card (str): El documento de identidad del pasajero.

    Métodos:
        passenger_data(): Devuelve una tupla con (nombre, apellido, id).
        name(): Devuelve el nombre del pasajero.
        surname(): Devuelve el apellido del pasajero.
        id_card(): Devuelve el documento de identidad del pasajero.
    """

    def __init__(self, name, surname, id_card):
        """
        Inicializa un objeto Passenger con nombre, apellido e ID.

        Args:
            name (str): El nombre del pasajero.
            surname (str): El apellido del pasajero.
            id_card (str): El documento de identidad del pasajero.

        Raises:
            ValueError: Si alguno de los parámetros (name, surname, id_card) está vacío.
        """
        if not name:
            raise ValueError("El nombre del pasajero no puede estar vacío.")
        if not surname:
            raise ValueError("El apellido del pasajero no puede estar vacío.")
        if not id_card:
            raise ValueError("El documento de identidad del pasajero no puede estar vacío.")

        self._name = name
        self._surname = surname
        self._id_card = id_card

    def name(self):
        """
        Devuelve el nombre del pasajero.

        Returns:
            str: El nombre del pasajero.
        """
        return self._name

    def surname(self):
        """
        Devuelve el apellido del pasajero.

        Returns:
            str: El apellido del pasajero.
        """
        return self._surname

    def id_card(self):
        """
        Devuelve el documento de identidad del pasajero.

        Returns:
            str: El documento de identidad del pasajero.
        """
        return self._id_card

    def passenger_data(self):
        """
        Devuelve los datos del pasajero como una tupla (nombre, apellido, id).

        Returns:
            tuple: (nombre, apellido, id_card).
        """
        return (self._name, self._surname, self._id_card)
