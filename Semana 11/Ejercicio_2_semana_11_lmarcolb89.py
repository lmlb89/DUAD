# 2. Cree una clase de `Bus` con:
#    1. Un atributo de `max_passengers`.
#    2. Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase `Person` vista en la lección). **Este solo debe agregar pasajeros si lleva menos de su máximo.** Sino, debe mostrar un mensaje de que el bus está lleno.
#    3. Un método para bajar pasajeros uno por uno (en cualquier orden).






class Person:
    def __init__(self, name=""):
        self.name = name

class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.current_passengers = 0
    
    def add_passenger(self, person):
        if not isinstance(person, Person):
            raise TypeError("Only Person objects can be added as passengers")
            
        if self.current_passengers < self.max_passengers:
            self.current_passengers += 1
            print(f"Passenger added (Name: {person.name}). Current: {self.current_passengers}/{self.max_passengers}")
        else:
            print("The bus is currently full")
    
    def drop_passenger(self):
        if self.current_passengers > 0:
            self.current_passengers -= 1
            print(f"Passenger dropped. Current: {self.current_passengers}/{self.max_passengers}")
        else:
            print("Bus is empty! No passengers to drop.")
    
    def __str__(self):
        return f"Bus with {self.current_passengers}/{self.max_passengers} passengers"


p1 = Person("Andres")
p2 = Person("Juan")
p3 = Person("Manuel")
p4 = Person("Andrea")
p5 = Person("Laura")
p6 = Person("Jose")
p7 = Person("Karina")

bus = Bus(20)


bus.add_passenger(p1)  
bus.add_passenger(p2) 
bus.add_passenger(p3)
bus.add_passenger(p4)
bus.add_passenger(p5)
bus.add_passenger(p6)
bus.add_passenger(p7)

bus.drop_passenger() 