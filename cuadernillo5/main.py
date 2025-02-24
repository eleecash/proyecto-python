from flight import Flight
from aircraft import Aircraft, Airbus, Boeing
from passenger import Passenger

def make_flights():
    # Ejemplo 1: Un vuelo con la clase base Aircraft
    f1 = Flight(
        number="BA117",
        aircraft=Aircraft(
            registration="G-EUAH", 
            model="Airbus A319", 
            num_rows=22, 
            num_seats_per_row=6
        )
    )

    # Ejemplo 2: Un vuelo con Boeing (subclase de Aircraft)
    f2 = Flight(
        number="AF92", 
        aircraft=Boeing(
            registration="F-GSPS", 
            airline="Emirates"
        )
    )

    # Ejemplo 3: Un vuelo con Airbus (subclase de Aircraft)
    f3 = Flight(
        number="BA148", 
        aircraft=Airbus(
            registration="G-EUPT", 
            variant="A319-100"
        )
    )

    # Creamos algunos pasajeros de ejemplo
    p1 = Passenger("Jack", "Shephard", "85994003S")
    p2 = Passenger("Kate", "Austen", "12589756P")
    p3 = Passenger("James", "Ford", "56278665F")
    p4 = Passenger("John", "Locke", "10265448H")
    p5 = Passenger("Sayid", "Jarrah", "15758664M")

    # Asignamos pasajeros a algunos asientos en f1
    f1.allocate_passenger("12A", p1.passenger_data())
    f1.allocate_passenger("18F", p2.passenger_data())
    f1.allocate_passenger("18E", p3.passenger_data())
    f1.allocate_passenger("1C",  p4.passenger_data())
    f1.allocate_passenger("4D",  p5.passenger_data())

    return f1, f2, f3

if __name__ == "__main__":
    f1, f2, f3 = make_flights()

    # Mostramos la información de cada vuelo
    for fl in (f1, f2, f3):
        print(f"\n=== Información del vuelo {fl.get_number()} ===")
        print("Seating plan:")
        fl.print_seating()

        print("\nBoarding cards:")
        fl.print_boarding_cards()
        print()
