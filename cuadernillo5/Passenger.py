# La clase Passenger se utiliza para almacenar la 
# información de cada pasajero: nombre, apellido e id.
# Esta clase tiene un método passenger_data() que devuelve 
# una tupla con los tres valores:

class Passenger:
    def __init__(self, name, surname, id_card):
        self._name = name
        self._surname = surname
        self._id_card = id_card

    def name(self):
        return self._name

    def surname(self):
        return self._surname

    def id_card(self):
        return self._id_card

    def passenger_data(self):
        return self._name, self._surname, self._id_card 


