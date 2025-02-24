# La clase Aircraft contiene información de la aeronave. 
# De esta clase, cabe mencionar el método seating_plan() 
# que genera una tupla con dos valores. El primero es una 
# lista con el tamaño de filas + 1, siendo None el valor 
# de cada elemento de la lista (ten en cuenta que estamos 
# añadiendo un valor de más, pero que no será una fila 
# real que esté disponible). El segundo es un string de 
# letras (p.e. "ABCDEF"), que representa los asientos de 
# cada fila. El método num_seats simplemente devuelve el 
# número total de asientos reales que tiene la aeronave. 
# A continuación, puedes ver la descripción de ambos métodos:
# seating_plan()
#"Generates a seating plan for the number of rows and seats per 
#    Returns:
#     rows: A list of Nones (size num_rows + 1).
#seats: A string of letters such as "ABCDEF"  
# num_seats()
# Calculates the number of seats
# Returns:
# seats: The number of seats
#  """

# ============================================================================
# Fichero: aircraft.py
# ============================================================================

class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self.__registration = registration
        self.__model = model
        self.__num_rows = num_rows
        self.__num_seats_per_row = num_seats_per_row

    def get_registration(self):
        return self.__registration

    def get_model(self):
        return self.__model

    def get_num_rows(self):
        return self.__num_rows

    def get_num_seats_per_row(self):
        return self.__num_seats_per_row

    def seating_plan(self):
        """
        Generates a seating plan for the number of rows and seats per row

        Returns:
          rows (list): Una lista de None (tamaño num_rows + 1)
          seats (str): Un string con tantas letras como asientos haya en cada fila
        """
        import string
        # Creamos la lista de filas con None (tamaño num_rows + 1).
        # El índice 0 no se usará para asientos reales.
        rows = [None] * (self.__num_rows + 1)

        # Creamos el string de letras, por ejemplo "ABCDEF" para 6 asientos por fila.
        seats = string.ascii_uppercase[: self.__num_seats_per_row]

        return rows, seats

    def num_seats(self):
        """
        Calculates the total number of seats

        Returns:
          int: Número total de asientos
        """
        return self.__num_rows * self.__num_seats_per_row


class Airbus(Aircraft):
    """
    Subclase de Aircraft para un Airbus A319 (ejemplo).
    Por defecto, suponemos 23 filas y 6 asientos por fila.
    """
    def __init__(self, registration, variant):
        # Llamamos a la superclase con los valores típicos de un Airbus A319
        super().__init__(registration, "Airbus A319", 23, 6)
        self.__variant = variant

    def get_variant(self):
        return self.__variant


class Boeing(Aircraft):
    """
    Subclase de Aircraft para un Boeing 777 (ejemplo).
    Por defecto, suponemos 56 filas y 9 asientos por fila.
    """
    def __init__(self, registration, airline):
        # Llamamos a la superclase con los valores típicos de un Boeing 777
        super().__init__(registration, "Boeing 777", 56, 9)
        self.__airline = airline

    def get_airline(self):
        return self.__airline





