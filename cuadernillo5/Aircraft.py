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

class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    # Generates a seating plan for the number of rows and seats per row
    def seating_plan(self):
        return (range(1, self._num_rows + 1),
                "ABCDEFGHJK"[:self._num_seats_per_row])

    # Calculates the number of seats
    def num_seats(self):
        return self._num_rows * self._num_seats_per_row
    




