# 2. Cree una clase de `Bus` con:
#    1. Un atributo de `max_passengers`.
#    2. Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase `Person` vista en la lección). **Este solo debe agregar pasajeros si lleva menos de su máximo.** Sino, debe mostrar un mensaje de que el bus está lleno.
#    3. Un método para bajar pasajeros uno por uno (en cualquier orden).


class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.current_passengers = 0
    
    def add_passenger(self):
        if self.current_passengers < self.max_passengers:
            self.current_passengers += 1
            print(f"Passenger added. Current passengers: {self.current_passengers}/{self.max_passengers}")
        else:
            print("The bus is currently full")
    
    def drop_passenger(self):
        """Remove one passenger from the bus if there are any"""
        if self.current_passengers > 0:
            self.current_passengers -= 1
            print(f"Passenger dropped. Current passengers: {self.current_passengers}/{self.max_passengers}")
    
    def __str__(self):
        return f"Bus with {self.current_passengers}/{self.max_passengers} passengers"


my_bus = Bus(20)


my_bus.add_passenger() 
my_bus.add_passenger()
my_bus.add_passenger()
my_bus.add_passenger()
my_bus.add_passenger()
my_bus.add_passenger()

my_bus.drop_passenger() 
my_bus.drop_passenger() 

print(my_bus) 